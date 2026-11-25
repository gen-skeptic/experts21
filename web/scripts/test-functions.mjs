// Test the Netlify Functions against a mock Claude API and a mock OpenRouter API: no real keys, no cost.
// Run `npm run build` first.
//
// Checks the agent list and model catalog, one-agent streaming on Claude and on OpenRouter, Auto routing by task type,
// fallbacks when a model fails, privacy settings (zero data retention), effort mapping, team routing (structured output)
// and synthesis, and the guards (password, missing keys, cross-site requests, unknown agents, malformed conversations).
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { findRoute, loadFunctions } from "./functions.mjs";

// ---------------------------------------------------------------- mock APIs
const seen = [];
/** OpenRouter model IDs the mock answers with HTTP 404, as if no endpoint met the privacy settings. */
const failing = new Set();

function planFor(names, withModels) {
  const extra = (taskType, model) => (withModels ? { task_type: taskType, model } : {});
  return {
    summary: "Legal and money questions, so the attorney and the finance manager.",
    assignments: [
      { agent: "business-attorney", question: "What must the MSA say?", ...extra("Security, legal and compliance review", "claude-sonnet-5.5"), brain: "opus", effort: "medium", reason: "Contract terms." },
      // Frontier is only for the hardest-problems type, so the app downgrades this one to the task type's primary.
      { agent: "operations-finance-manager", question: "Is $9,000 enough?", ...extra("Research and analysis", "gemini-4-argon"), brain: "sonnet", effort: "low", reason: "Price and hours." },
      { agent: "orchestrator", question: "never me", ...extra("Routine operations", "gpt-6-luna"), brain: "opus", effort: "low", reason: "should be dropped" },
      { agent: "not-an-agent", question: "x", ...extra("Routine operations", "gpt-6-luna"), brain: "opus", effort: "low", reason: "should be dropped" },
    ].filter((a) => a.agent === "not-an-agent" || a.agent === "orchestrator" || names.includes(a.agent)),
  };
}

function claudeApi(req, res, body) {
  // The SDK sends the key as x-api-key or, from SDK 1.x, as Authorization: Bearer.
  if (req.headers["x-api-key"] !== "test-key" && req.headers.authorization !== "Bearer test-key") {
    res.writeHead(401, { "Content-Type": "application/json" }).end(JSON.stringify({ type: "error", error: { type: "authentication_error", message: "invalid x-api-key" } }));
    return;
  }
  if (!body.stream) {
    const item = body.output_config?.format?.schema?.properties?.assignments?.items?.properties ?? {};
    const plan = planFor(item.agent?.enum ?? [], !!item.task_type);
    res.writeHead(200, { "Content-Type": "application/json" }).end(
      JSON.stringify({ id: "msg_plan", type: "message", role: "assistant", model: body.model, content: [{ type: "text", text: JSON.stringify(plan) }], stop_reason: "end_turn", stop_sequence: null, usage: { input_tokens: 1000, output_tokens: 200, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 } }),
    );
    return;
  }
  res.writeHead(200, { "Content-Type": "text/event-stream" });
  const send = (event, data) => res.write(`event: ${event}\ndata: ${JSON.stringify({ type: event, ...data })}\n\n`);
  send("message_start", { message: { id: "msg_1", type: "message", role: "assistant", model: body.model, content: [], stop_reason: null, stop_sequence: null, usage: { input_tokens: 10, output_tokens: 1, cache_read_input_tokens: 30000, cache_creation_input_tokens: 0 } } });
  send("content_block_start", { index: 0, content_block: { type: "thinking", thinking: "", signature: "" } });
  send("content_block_stop", { index: 0 });
  send("content_block_start", { index: 1, content_block: { type: "text", text: "" } });
  for (const text of ["Hello ", "from ", body.model]) send("content_block_delta", { index: 1, delta: { type: "text_delta", text } });
  send("content_block_stop", { index: 1 });
  send("message_delta", { delta: { stop_reason: "end_turn", stop_sequence: null }, usage: { output_tokens: 500 } });
  send("message_stop", {});
  res.end();
}

function openRouterApi(req, res, body) {
  if (req.headers.authorization !== "Bearer or-key") {
    res.writeHead(401, { "Content-Type": "application/json" }).end(JSON.stringify({ error: { code: 401, message: "No auth credentials found" } }));
    return;
  }
  if (failing.has(body.model)) {
    res.writeHead(404, { "Content-Type": "application/json" }).end(JSON.stringify({ error: { code: 404, message: "No endpoints found matching your data policy" } }));
    return;
  }
  if (!body.stream) {
    const item = body.response_format?.json_schema?.schema?.properties?.assignments?.items?.properties ?? {};
    const plan = planFor(item.agent?.enum ?? [], !!item.task_type);
    res.writeHead(200, { "Content-Type": "application/json" }).end(
      JSON.stringify({ id: "gen-plan", model: body.model, provider: "Azure", choices: [{ index: 0, finish_reason: "stop", message: { role: "assistant", content: JSON.stringify(plan) } }], usage: { prompt_tokens: 1000, completion_tokens: 200, cost: 0.0042 } }),
    );
    return;
  }
  res.writeHead(200, { "Content-Type": "text/event-stream" });
  const chunk = (delta, extra = {}) => res.write(`data: ${JSON.stringify({ id: "gen-1", model: body.model, provider: "Together", choices: [{ index: 0, delta, finish_reason: null, ...extra }] })}\n\n`);
  res.write(": OPENROUTER PROCESSING\n\n");
  chunk({ role: "assistant", content: "", reasoning: "Thinking about it." });
  for (const text of ["Hello ", "from ", body.model]) chunk({ content: text });
  chunk({}, { finish_reason: "stop" });
  res.write(`data: ${JSON.stringify({ id: "gen-1", model: body.model, provider: "Together", choices: [], usage: { prompt_tokens: 30000, completion_tokens: 500, cost: 0.0012 } })}\n\n`);
  res.write("data: [DONE]\n\n");
  res.end();
}

const mock = createServer(async (req, res) => {
  let raw = "";
  for await (const chunk of req) raw += chunk;
  const body = JSON.parse(raw || "{}");
  seen.push({ path: req.url, headers: req.headers, body });
  if (req.url.startsWith("/openrouter/")) openRouterApi(req, res, body);
  else claudeApi(req, res, body);
});
await new Promise((ok) => mock.listen(0, "127.0.0.1", ok));
const MOCK = `http://127.0.0.1:${mock.address().port}`;
process.env.ANTHROPIC_BASE_URL = MOCK;
process.env.ANTHROPIC_API_KEY = "test-key";
process.env.OPENROUTER_BASE_URL = `${MOCK}/openrouter/api/v1`;
process.env.OPENROUTER_API_KEY = "or-key";
for (const name of ["APP_PASSWORD", "WEB_MAX_EFFORT", "OPENROUTER_ZDR", "NETLIFY_AI_GATEWAY_KEY"]) delete process.env[name];

const routes = await loadFunctions();
const ORIGIN = "https://experts21.example";
async function call(method, path, body, headers = {}) {
  const url = ORIGIN + path;
  const route = findRoute(routes, url);
  assert.ok(route, `no function for ${path}`);
  const req = new Request(url, { method, headers: { "Content-Type": "application/json", ...headers }, body: body === undefined ? undefined : JSON.stringify(body) });
  return route.handler(req, {});
}
async function events(response) {
  assert.match(response.headers.get("content-type") ?? "", /text\/event-stream/);
  const text = await response.text();
  return text
    .split("\n\n")
    .map((block) => ({ event: block.match(/^event: (.+)$/m)?.[1], data: block.match(/^data: (.+)$/m)?.[1] }))
    .filter((e) => e.event && e.data)
    .map((e) => ({ event: e.event, data: JSON.parse(e.data) }));
}
const text = (ev) => ev.filter((e) => e.event === "delta").map((e) => e.data.text).join("");
const done = (ev) => ev.find((e) => e.event === "done")?.data;
const ask = (agent, extra = {}) => call("POST", "/api/chat", { agent, messages: [{ role: "user", content: "A short question." }], ...extra });
async function withEnv(vars, fn) {
  const before = Object.fromEntries(Object.keys(vars).map((k) => [k, process.env[k]]));
  for (const [k, v] of Object.entries(vars)) v === undefined ? delete process.env[k] : (process.env[k] = v);
  try {
    await fn();
  } finally {
    for (const [k, v] of Object.entries(before)) v === undefined ? delete process.env[k] : (process.env[k] = v);
  }
}
let passed = 0;
async function test(name, fn) {
  seen.length = 0;
  failing.clear();
  try {
    await fn();
    passed++;
    console.log(`ok   ${name}`);
  } catch (error) {
    console.error(`FAIL ${name}\n${error.stack}`);
    process.exitCode = 1;
  }
}

// ---------------------------------------------------------------- the list and the catalog
await test("agent list: 50 agents, Star Trek names, the model catalog, no prompts", async () => {
  const res = await call("GET", "/api/agents");
  assert.equal(res.status, 200);
  const data = await res.json();
  assert.equal(data.agents.length, 50);
  assert.equal(data.orchestrator, "orchestrator");
  assert.equal(data.configured, true);
  assert.deepEqual(data.providers, { claude: true, claudeKey: true, openrouter: true, zdr: true });
  assert.equal(data.passwordRequired, false);
  const cogley = data.agents.find((a) => a.id === "business-attorney");
  assert.equal(cogley.name, "Cogley");
  assert.equal(cogley.brain, "opus");
  assert.equal(cogley.taskType, "Security, legal and compliance review");
  assert.ok(cogley.knowledgeFiles.includes("2026-11-sample-client-msa-draft.md"));
  assert.equal(data.models.length, 8);
  assert.equal(data.taskTypes.length, 14);
  assert.ok(data.models.every((m) => m.taskCost > 0 && m.input > 0));
  assert.equal(data.taskTypes.find((t) => t.name === "Software and automation build").primary, "deepseek-v4.1-flash");
  const raw = JSON.stringify(data);
  assert.ok(!raw.includes("## Rules (apply to everything you produce)"), "prompts must not reach the browser");
  assert.ok(!raw.includes("Master Services Agreement (draft received"), "knowledge text must not reach the browser");
});

// ---------------------------------------------------------------- Claude only (the agent's own brain)
await test("Claude only: one agent on its own brain with caching and refusal fallbacks", async () => {
  const ev = await events(await call("POST", "/api/chat", { agent: "business-attorney", model: "claude", messages: [{ role: "user", content: "Should we sign the sample MSA?" }] }, { Origin: ORIGIN }));
  assert.deepEqual(
    { agent: ev[0].data.agent, brain: ev[0].data.brain, effort: ev[0].data.effort, model: ev[0].data.model, api: ev[0].data.api },
    { agent: "business-attorney", brain: "opus", effort: "medium", model: "Claude Opus 5.5", api: "Claude API" },
  );
  assert.ok(ev.some((e) => e.event === "thinking"));
  assert.equal(text(ev), "Hello from claude-opus-5-5");
  assert.equal(done(ev).modelId, "claude-opus-5-5");
  assert.equal(done(ev).costEstimated, true);
  assert.ok(done(ev).cost > 0);
  const sent = seen[0];
  assert.match(sent.path, /^\/v1\/messages/);
  assert.equal(sent.body.model, "claude-opus-5-5");
  assert.equal(sent.body.output_config.effort, "medium", "high effort is capped at medium in the web app");
  assert.equal(sent.body.fallbacks, "default");
  assert.match(sent.headers["anthropic-beta"], /server-side-fallback-2026-07-01/);
  assert.deepEqual(sent.body.system[0].cache_control, { type: "ephemeral" });
  const prompt = sent.body.system[0].text;
  for (const part of ["Your name is **Cogley**", "=== SKILL: contract-review", "2026-11-sample-client-msa-draft.md", "--- docs/07-permits-and-licenses.md ---", "don't claim to be a particular model"]) assert.ok(prompt.includes(part), part);
});

await test("Claude only: Haiku agents run without the fallback beta", async () => {
  assert.equal(done(await events(await ask("operations-coordinator", { model: "claude" }))).modelId, "claude-haiku-5-5");
  assert.equal(seen[0].body.model, "claude-haiku-5-5");
  assert.equal(seen[0].body.fallbacks, undefined);
  assert.ok(!String(seen[0].headers["anthropic-beta"] ?? "").includes("server-side-fallback"));
});

await test("Claude only: an assignment from the orchestrator, on the brain it picked", async () => {
  await events(await call("POST", "/api/chat", { agent: "operations-finance-manager", model: "claude", brain: "sonnet", effort: "low", assignment: { original: "Take the job?", summary: "Money question.", question: "Is $9,000 enough?", reason: "Price." } }));
  assert.equal(seen[0].body.model, "claude-sonnet-5-5");
  assert.equal(seen[0].body.output_config.effort, "low");
  assert.match(seen[0].body.messages[0].content, /Picard \(`orchestrator`\) routed a question/);
  assert.match(seen[0].body.messages[0].content, /Your part: Is \$9,000 enough\?/);
});

// ---------------------------------------------------------------- Auto: the most cost-efficient model per task type
await test("Auto (default): legal review runs on Claude Sonnet 5.5 on the Claude API", async () => {
  const ev = await events(await ask("business-attorney"));
  assert.equal(ev[0].data.taskType, "Security, legal and compliance review");
  assert.equal(seen.length, 1);
  assert.match(seen[0].path, /^\/v1\/messages/);
  assert.equal(seen[0].body.model, "claude-sonnet-5-5");
  assert.equal(seen[0].body.output_config.effort, "medium");
  assert.deepEqual({ model: done(ev).model, api: done(ev).api }, { model: "Claude Sonnet 5.5", api: "Claude API" });
});

await test("Auto: a software build runs on DeepSeek through OpenRouter, private by default", async () => {
  const ev = await events(await ask("full-stack-developer", { model: "auto" }));
  assert.equal(seen.length, 1);
  const sent = seen[0];
  assert.equal(sent.path, "/openrouter/api/v1/chat/completions");
  assert.equal(sent.headers.authorization, "Bearer or-key");
  assert.equal(sent.headers["x-title"], "DIO Experts21");
  assert.equal(sent.body.model, "deepseek/deepseek-v4.1-flash-1017");
  assert.equal(sent.body.stream, true);
  assert.deepEqual(sent.body.provider, { zdr: true, data_collection: "deny" });
  assert.equal(sent.body.reasoning.effort, "low");
  assert.equal(done(ev).effort, "low");
  assert.equal(sent.body.messages[0].role, "system");
  assert.equal(typeof sent.body.messages[0].content, "string", "no explicit cache breakpoints for DeepSeek");
  assert.match(sent.body.messages[0].content, /You are Wesley/);
  assert.equal(sent.body.messages.at(-1).content, "A short question.");
  assert.ok(ev.some((e) => e.event === "thinking"), "reasoning shows as thinking");
  assert.equal(text(ev), "Hello from deepseek/deepseek-v4.1-flash-1017");
  const d = done(ev);
  assert.deepEqual({ model: d.model, api: d.api, provider: d.provider, cost: d.cost, costEstimated: d.costEstimated, stop: d.stop_reason }, { model: "DeepSeek V4.1 Flash", api: "OpenRouter", provider: "Together", cost: 0.0012, costEstimated: false, stop: "end_turn" });
});

await test("Auto: when the primary has no endpoint, the fallback answers and the person is told", async () => {
  failing.add("deepseek/deepseek-v4.1-flash-1017");
  const ev = await events(await ask("full-stack-developer"));
  assert.equal(seen.length, 2);
  assert.equal(seen[1].body.model, "claude-sonnet-5-5", "the Software build fallback is Sonnet, on the Claude API");
  const notice = ev.find((e) => e.event === "notice").data.message;
  assert.match(notice, /DeepSeek V4\.1 Flash \(OpenRouter\) was not used: OpenRouter has no endpoint for this model that meets the privacy settings/);
  assert.match(notice, /Answering with Claude Sonnet 5\.5/);
  assert.equal(done(ev).model, "Claude Sonnet 5.5");
});

await test("Auto: when the primary and fallback fail, the agent's own Claude brain answers", async () => {
  failing.add("openai/gpt-6.1-sol");
  failing.add("google/gemini-3.7-flash");
  const ev = await events(await ask("lean-six-sigma-lead"));
  assert.deepEqual(seen.map((s) => s.body.model), ["openai/gpt-6.1-sol", "google/gemini-3.7-flash", "claude-opus-5-5"]);
  assert.equal(ev.filter((e) => e.event === "notice").length, 2);
  assert.equal(done(ev).model, "Claude Opus 5.5");
});

await test("Auto: short-form work runs on GPT-6 Luna; Claude models skip OpenRouter when the Claude key is set", async () => {
  await events(await ask("social-media-manager"));
  assert.equal(seen[0].body.model, "openai/gpt-6-luna");
  seen.length = 0;
  await events(await ask("operations-coordinator"));
  assert.match(seen[0].path, /^\/v1\/messages/);
  assert.equal(seen[0].body.model, "claude-haiku-5-5");
  assert.equal(seen[0].body.output_config.effort, "low");
});

await test("One model: Gemini through OpenRouter, with cache breakpoints and a supported effort", async () => {
  await events(await ask("business-attorney", { model: "gemini-3.7-flash" }));
  const sent = seen[0].body;
  assert.equal(sent.model, "google/gemini-3.7-flash");
  assert.deepEqual(sent.messages[0].content[0].cache_control, { type: "ephemeral" });
  assert.equal(sent.reasoning.effort, "medium");
});

await test("Effort mapping: a model without medium effort gets the closest lower one", async () => {
  await events(await ask("business-attorney", { model: "deepseek-v4.1-flash" }));
  assert.equal(seen[0].body.reasoning.effort, "low", "DeepSeek supports none/low/high/max, so medium becomes low");
});

await test("OPENROUTER_ZDR=false: still never an endpoint that collects data", async () => {
  await withEnv({ OPENROUTER_ZDR: "false" }, async () => {
    await events(await ask("full-stack-developer"));
    assert.deepEqual(seen[0].body.provider, { data_collection: "deny" });
    assert.equal((await (await call("GET", "/api/agents")).json()).providers.zdr, false);
  });
});

await test("No OpenRouter key: Auto skips non-Claude models and uses the Claude fallback", async () => {
  await withEnv({ OPENROUTER_API_KEY: "" }, async () => {
    assert.equal((await (await call("GET", "/api/agents")).json()).providers.openrouter, false);
    const ev = await events(await ask("full-stack-developer"));
    assert.equal(seen.length, 1);
    assert.equal(seen[0].body.model, "claude-sonnet-5-5");
    assert.ok(!ev.some((e) => e.event === "notice"), "skipping an unconfigured provider is silent");
  });
});

await test("No Claude key: Claude models run through OpenRouter with cache breakpoints", async () => {
  await withEnv({ ANTHROPIC_API_KEY: "" }, async () => {
    const ev = await events(await ask("business-attorney", { model: "claude" }));
    assert.equal(seen[0].path, "/openrouter/api/v1/chat/completions");
    assert.equal(seen[0].body.model, "anthropic/claude-opus-5.5");
    assert.deepEqual(seen[0].body.messages[0].content[0].cache_control, { type: "ephemeral" });
    assert.equal(seen[0].body.messages[0].content.length, 1);
    assert.equal(done(ev).api, "OpenRouter");
  });
});

// ---------------------------------------------------------------- team mode
await test("team plan (Auto): routing model, task types and models per assignment, unsafe picks fixed", async () => {
  const res = await call("POST", "/api/team/plan", { messages: [{ role: "user", content: "Should we take a $9,000 build?" }] });
  assert.equal(res.status, 200);
  const plan = await res.json();
  assert.deepEqual(plan.assignments.map((a) => a.agent), ["business-attorney", "operations-finance-manager"]);
  assert.equal(plan.assignments[0].name, "Cogley");
  assert.deepEqual([plan.assignments[0].taskType, plan.assignments[0].model, plan.assignments[0].modelName], ["Security, legal and compliance review", "claude-sonnet-5.5", "Claude Sonnet 5.5"]);
  assert.equal(plan.assignments[1].model, "deepseek-v4.1-flash", "Frontier picked for research is downgraded to the task type's primary");
  assert.equal(plan.routedBy, "Picard");
  assert.equal(plan.model, "Claude Sonnet 5.5");
  const sent = seen[0].body;
  assert.equal(sent.model, "claude-sonnet-5-5", "the routing plan runs on the catalog's routing model");
  assert.equal(sent.output_config.effort, "low");
  assert.equal(sent.output_config.format.type, "json_schema");
  const props = sent.output_config.format.schema.properties.assignments.items.properties;
  assert.ok(!props.agent.enum.includes("orchestrator"));
  assert.equal(props.task_type.enum.length, 14);
  assert.ok(props.model.enum.includes("deepseek-v4.1-flash"));
  assert.match(sent.system[1].text, /TEAM MODE: ROUTING/);
  assert.match(sent.system[0].text, /=== SKILL: model-selection/);
});

await test("team plan (Claude only): the orchestrator's own brain", async () => {
  await call("POST", "/api/team/plan", { model: "claude", messages: [{ role: "user", content: "Should we take it?" }] });
  assert.equal(seen[0].body.model, "claude-opus-5-5");
});

await test("team plan on an OpenRouter model: strict JSON schema, endpoints that support it", async () => {
  const res = await call("POST", "/api/team/plan", { model: "gpt-6.1-sol", messages: [{ role: "user", content: "Should we take it?" }] });
  const plan = await res.json();
  assert.equal(res.status, 200);
  assert.equal(plan.assignments.length, 2);
  assert.equal(plan.cost, 0.0042);
  const sent = seen[0].body;
  assert.equal(sent.model, "openai/gpt-6.1-sol");
  assert.equal(sent.response_format.type, "json_schema");
  assert.equal(sent.response_format.json_schema.strict, true);
  assert.deepEqual(sent.provider, { zdr: true, data_collection: "deny", require_parameters: true });
});

await test("team plan: a failed routing model falls back and says so", async () => {
  await withEnv({ ANTHROPIC_API_KEY: "" }, async () => {
    failing.add("anthropic/claude-sonnet-5.5");
    const plan = await (await call("POST", "/api/team/plan", { messages: [{ role: "user", content: "Should we take it?" }] })).json();
    assert.deepEqual(seen.map((s) => s.body.model), ["anthropic/claude-sonnet-5.5", "google/gemini-3.7-flash"]);
    assert.equal(plan.notices.length, 1);
    assert.match(plan.notices[0], /Routed with Gemini 3\.7 Flash/);
  });
});

await test("team member (Auto): the model the orchestrator planned answers first", async () => {
  await events(await call("POST", "/api/chat", { agent: "market-research-analyst", model: "auto", taskType: "Research and analysis", planned: "gpt-6-luna", assignment: { original: "Q", summary: "S", question: "Your part", reason: "R" } }));
  assert.equal(seen[0].body.model, "openai/gpt-6-luna");
  assert.equal(seen[0].body.reasoning.effort, "low");
});

await test("team synthesis (Auto): the orchestrator combines the answers on the strategy model", async () => {
  const ev = await events(
    await call("POST", "/api/team/synthesize", {
      messages: [{ role: "user", content: "Should we take it?" }],
      summary: "Legal and money.",
      answers: [{ agent: "business-attorney", text: "Only with a liability cap." }, { agent: "nobody", text: "ignored" }],
    }),
  );
  assert.ok(done(ev));
  const sent = seen[0].body;
  assert.equal(sent.model, "claude-sonnet-5-5");
  assert.match(sent.system[1].text, /TEAM MODE: SYNTHESIS/);
  assert.match(sent.messages.at(-1).content, /### Cogley \(`business-attorney`/);
  assert.ok(!sent.messages.at(-1).content.includes("ignored"));
});

// ---------------------------------------------------------------- guards
await test("guards: malformed conversations, unknown agents, cross-site requests, GET", async () => {
  assert.equal((await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "assistant", content: "hi" }] })).status, 400);
  assert.equal((await call("POST", "/api/chat", { agent: "no-such-agent", messages: [{ role: "user", content: "hi" }] })).status, 404);
  assert.equal((await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] }, { Origin: "https://evil.example" })).status, 403);
  assert.equal((await call("GET", "/api/chat")).status, 405);
  assert.equal(seen.length, 0, "no model call for rejected requests");
});

await test("an unknown model choice falls back to Auto", async () => {
  await events(await ask("full-stack-developer", { model: "evil/model" }));
  assert.equal(seen[0].body.model, "deepseek/deepseek-v4.1-flash-1017");
});

await test("APP_PASSWORD: model calls need the password; the list says so", async () => {
  await withEnv({ APP_PASSWORD: "make-it-so" }, async () => {
    const list = await (await call("GET", "/api/agents")).json();
    assert.equal(list.passwordRequired, true);
    assert.equal(list.passwordOk, undefined);
    assert.equal((await (await call("GET", "/api/agents", undefined, { "X-App-Password": "wrong" })).json()).passwordOk, false);
    assert.equal((await (await call("GET", "/api/agents", undefined, { "X-App-Password": "make-it-so" })).json()).passwordOk, true);
    const denied = await ask("business-attorney");
    assert.equal(denied.status, 401);
    assert.equal((await denied.json()).passwordRequired, true);
    const ok = await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] }, { "X-App-Password": "make-it-so" });
    assert.equal(ok.status, 200);
    await events(ok);
  });
});

await test("Netlify AI Gateway: its injected key counts as configured", async () => {
  await withEnv({ ANTHROPIC_API_KEY: "", OPENROUTER_API_KEY: "", NETLIFY_AI_GATEWAY_KEY: "gateway-key" }, async () => {
    const list = await (await call("GET", "/api/agents")).json();
    assert.equal(list.configured, true);
    assert.equal(list.providers.claude, true);
  });
});

await test("no keys at all: the list loads, model calls explain what to set", async () => {
  await withEnv({ ANTHROPIC_API_KEY: "", OPENROUTER_API_KEY: "" }, async () => {
    assert.equal((await (await call("GET", "/api/agents")).json()).configured, false);
    const res = await ask("business-attorney");
    assert.equal(res.status, 503);
    const { message } = await res.json();
    assert.match(message, /ANTHROPIC_API_KEY/);
    assert.match(message, /OPENROUTER_API_KEY/);
  });
});

await test("every function has a rate limit and a method, except the read-only list", async () => {
  for (const r of routes.filter((r) => r.name !== "agents")) {
    assert.ok(r.config.rateLimit?.windowLimit > 0, `${r.name} rate limit`);
    assert.equal(r.config.method, "POST");
  }
});

mock.close();
console.log(`\n${passed} test(s) passed${process.exitCode ? ", some failed" : ""}.`);
