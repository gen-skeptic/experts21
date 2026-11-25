// Test the Netlify Functions against a mock Claude API: no real key, no cost. Run `npm run build` first.
//
// Checks the agent list, one-agent streaming, team routing (structured output), synthesis, the request shapes sent to
// the API (model per brain, effort, prompt caching, refusal fallbacks), and the guards (password, missing key,
// cross-site requests, unknown agents, malformed conversations).
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { findRoute, loadFunctions } from "./functions.mjs";

// ---------------------------------------------------------------- mock Claude API
const seen = [];
const mock = createServer(async (req, res) => {
  let raw = "";
  for await (const chunk of req) raw += chunk;
  const body = JSON.parse(raw || "{}");
  seen.push({ path: req.url, headers: req.headers, body });
  // The SDK sends the key as x-api-key or, from SDK 1.x, as Authorization: Bearer.
  if (req.headers["x-api-key"] !== "test-key" && req.headers.authorization !== "Bearer test-key") {
    res.writeHead(401, { "Content-Type": "application/json" }).end(JSON.stringify({ type: "error", error: { type: "authentication_error", message: "invalid x-api-key" } }));
    return;
  }
  if (!body.stream) {
    const names = body.output_config?.format?.schema?.properties?.assignments?.items?.properties?.agent?.enum ?? [];
    const plan = {
      summary: "Legal and money questions, so the attorney and the finance manager.",
      assignments: [
        { agent: "business-attorney", question: "What must the MSA say?", brain: "opus", effort: "medium", reason: "Contract terms." },
        { agent: "operations-finance-manager", question: "Is $9,000 enough?", brain: "sonnet", effort: "low", reason: "Price and hours." },
        { agent: "orchestrator", question: "never me", brain: "opus", effort: "low", reason: "should be dropped" },
        { agent: "not-an-agent", question: "x", brain: "opus", effort: "low", reason: "should be dropped" },
      ].filter((a) => a.agent === "not-an-agent" || a.agent === "orchestrator" || names.includes(a.agent)),
    };
    res.writeHead(200, { "Content-Type": "application/json" }).end(
      JSON.stringify({ id: "msg_plan", type: "message", role: "assistant", model: body.model, content: [{ type: "text", text: JSON.stringify(plan) }], stop_reason: "end_turn", stop_sequence: null, usage: { input_tokens: 10, output_tokens: 20 } }),
    );
    return;
  }
  res.writeHead(200, { "Content-Type": "text/event-stream" });
  const send = (event, data) => res.write(`event: ${event}\ndata: ${JSON.stringify({ type: event, ...data })}\n\n`);
  send("message_start", { message: { id: "msg_1", type: "message", role: "assistant", model: body.model, content: [], stop_reason: null, stop_sequence: null, usage: { input_tokens: 10, output_tokens: 1 } } });
  send("content_block_start", { index: 0, content_block: { type: "thinking", thinking: "", signature: "" } });
  send("content_block_stop", { index: 0 });
  send("content_block_start", { index: 1, content_block: { type: "text", text: "" } });
  for (const text of ["Hello ", "from ", body.model]) send("content_block_delta", { index: 1, delta: { type: "text_delta", text } });
  send("content_block_stop", { index: 1 });
  send("message_delta", { delta: { stop_reason: "end_turn", stop_sequence: null }, usage: { output_tokens: 5 } });
  send("message_stop", {});
  res.end();
});
await new Promise((ok) => mock.listen(0, "127.0.0.1", ok));
process.env.ANTHROPIC_BASE_URL = `http://127.0.0.1:${mock.address().port}`;
process.env.ANTHROPIC_API_KEY = "test-key";
delete process.env.APP_PASSWORD;
delete process.env.WEB_MAX_EFFORT;

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
let passed = 0;
async function test(name, fn) {
  seen.length = 0;
  try {
    await fn();
    passed++;
    console.log(`ok   ${name}`);
  } catch (error) {
    console.error(`FAIL ${name}\n${error.stack}`);
    process.exitCode = 1;
  }
}

// ---------------------------------------------------------------- tests
await test("agent list: 50 agents, Star Trek names, no prompts", async () => {
  const res = await call("GET", "/api/agents");
  assert.equal(res.status, 200);
  const data = await res.json();
  assert.equal(data.agents.length, 50);
  assert.equal(data.orchestrator, "orchestrator");
  assert.equal(data.configured, true);
  assert.equal(data.passwordRequired, false);
  const cogley = data.agents.find((a) => a.id === "business-attorney");
  assert.equal(cogley.name, "Cogley");
  assert.equal(cogley.brain, "opus");
  assert.ok(cogley.knowledgeFiles.includes("2026-11-sample-client-msa-draft.md"));
  const raw = JSON.stringify(data);
  assert.ok(!raw.includes("## Rules (apply to everything you produce)"), "prompts must not reach the browser");
  assert.ok(!raw.includes("Master Services Agreement (draft received"), "knowledge text must not reach the browser");
});

await test("chat: streams one agent on its own brain with caching and fallbacks", async () => {
  const res = await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "Should we sign the sample MSA?" }] }, { Origin: ORIGIN });
  const ev = await events(res);
  assert.deepEqual(ev[0], { event: "meta", data: { agent: "business-attorney", brain: "opus", effort: "medium" } });
  assert.ok(ev.some((e) => e.event === "thinking"));
  assert.equal(ev.filter((e) => e.event === "delta").map((e) => e.data.text).join(""), "Hello from claude-opus-5-5");
  assert.deepEqual(ev.at(-1), { event: "done", data: { model: "claude-opus-5-5", stop_reason: "end_turn" } });
  const sent = seen[0];
  assert.match(sent.path, /^\/v1\/messages/);
  assert.equal(sent.body.model, "claude-opus-5-5");
  assert.equal(sent.body.output_config.effort, "medium", "high effort is capped at medium in the web app");
  assert.equal(sent.body.fallbacks, "default");
  assert.match(sent.headers["anthropic-beta"], /server-side-fallback-2026-07-01/);
  assert.deepEqual(sent.body.system[0].cache_control, { type: "ephemeral" });
  const prompt = sent.body.system[0].text;
  for (const part of ["Your name is **Cogley**", "=== SKILL: contract-review", "2026-11-sample-client-msa-draft.md", "--- docs/07-permits-and-licenses.md ---"]) assert.ok(prompt.includes(part), part);
});

await test("chat: Haiku agents run without the fallback beta", async () => {
  const res = await call("POST", "/api/chat", { agent: "operations-coordinator", messages: [{ role: "user", content: "When is the county receipt due?" }] });
  assert.equal((await events(res)).at(-1).event, "done");
  assert.equal(seen[0].body.model, "claude-haiku-5-5");
  assert.equal(seen[0].body.fallbacks, undefined);
  assert.ok(!String(seen[0].headers["anthropic-beta"] ?? "").includes("server-side-fallback"));
});

await test("chat: an assignment from the orchestrator, on the brain it picked", async () => {
  const res = await call("POST", "/api/chat", { agent: "operations-finance-manager", brain: "sonnet", effort: "low", assignment: { original: "Take the job?", summary: "Money question.", question: "Is $9,000 enough?", reason: "Price." } });
  await events(res);
  assert.equal(seen[0].body.model, "claude-sonnet-5-5");
  assert.equal(seen[0].body.output_config.effort, "low");
  assert.match(seen[0].body.messages[0].content, /Picard \(`orchestrator`\) routed a question/);
  assert.match(seen[0].body.messages[0].content, /Your part: Is \$9,000 enough\?/);
});

await test("team plan: structured output, unknown agents and the orchestrator dropped", async () => {
  const res = await call("POST", "/api/team/plan", { messages: [{ role: "user", content: "Should we take a $9,000 build?" }] });
  assert.equal(res.status, 200);
  const plan = await res.json();
  assert.deepEqual(plan.assignments.map((a) => a.agent), ["business-attorney", "operations-finance-manager"]);
  assert.equal(plan.assignments[0].name, "Cogley");
  assert.equal(plan.routedBy, "Picard");
  const sent = seen[0].body;
  assert.equal(sent.model, "claude-opus-5-5");
  assert.equal(sent.output_config.effort, "low");
  assert.equal(sent.output_config.format.type, "json_schema");
  assert.ok(!sent.output_config.format.schema.properties.assignments.items.properties.agent.enum.includes("orchestrator"));
  assert.match(sent.system[1].text, /TEAM MODE: ROUTING/);
});

await test("team synthesis: the orchestrator combines the answers", async () => {
  const res = await call("POST", "/api/team/synthesize", {
    messages: [{ role: "user", content: "Should we take it?" }],
    summary: "Legal and money.",
    answers: [{ agent: "business-attorney", text: "Only with a liability cap." }, { agent: "nobody", text: "ignored" }],
  });
  const ev = await events(res);
  assert.equal(ev.at(-1).event, "done");
  const sent = seen[0].body;
  assert.match(sent.system[1].text, /TEAM MODE: SYNTHESIS/);
  assert.match(sent.messages.at(-1).content, /### Cogley \(`business-attorney`/);
  assert.ok(!sent.messages.at(-1).content.includes("ignored"));
});

await test("guards: malformed conversations, unknown agents, cross-site requests, GET", async () => {
  assert.equal((await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "assistant", content: "hi" }] })).status, 400);
  assert.equal((await call("POST", "/api/chat", { agent: "no-such-agent", messages: [{ role: "user", content: "hi" }] })).status, 404);
  assert.equal((await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] }, { Origin: "https://evil.example" })).status, 403);
  assert.equal((await call("GET", "/api/chat")).status, 405);
  assert.equal(seen.length, 0, "no model call for rejected requests");
});

await test("APP_PASSWORD: model calls need the password; the list says so", async () => {
  process.env.APP_PASSWORD = "make-it-so";
  try {
    const list = await (await call("GET", "/api/agents")).json();
    assert.equal(list.passwordRequired, true);
    assert.equal(list.passwordOk, undefined);
    assert.equal((await (await call("GET", "/api/agents", undefined, { "X-App-Password": "wrong" })).json()).passwordOk, false);
    assert.equal((await (await call("GET", "/api/agents", undefined, { "X-App-Password": "make-it-so" })).json()).passwordOk, true);
    const denied = await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] });
    assert.equal(denied.status, 401);
    assert.equal((await denied.json()).passwordRequired, true);
    const allowed = await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] }, { "X-App-Password": "make-it-so" });
    assert.equal(allowed.status, 200);
    await events(allowed);
  } finally {
    delete process.env.APP_PASSWORD;
  }
});

await test("no ANTHROPIC_API_KEY: the list loads, model calls explain what to set", async () => {
  process.env.ANTHROPIC_API_KEY = "";
  try {
    assert.equal((await (await call("GET", "/api/agents")).json()).configured, false);
    const res = await call("POST", "/api/chat", { agent: "business-attorney", messages: [{ role: "user", content: "hi" }] });
    assert.equal(res.status, 503);
    assert.match((await res.json()).message, /ANTHROPIC_API_KEY/);
  } finally {
    process.env.ANTHROPIC_API_KEY = "test-key";
  }
});

await test("every function has a rate limit and a method, except the read-only list", async () => {
  for (const r of routes.filter((r) => r.name !== "agents")) {
    assert.ok(r.config.rateLimit?.windowLimit > 0, `${r.name} rate limit`);
    assert.equal(r.config.method, "POST");
  }
});

mock.close();
console.log(`\n${passed} test(s) passed${process.exitCode ? ", some failed" : ""}.`);
