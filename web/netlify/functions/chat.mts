// POST /api/chat: one agent's reply, streamed as server-sent events: meta, thinking?, delta..., notice?, done (or error).
// Team mode uses it too: each assigned expert answers its part through this endpoint, in parallel.
//
// Body: { agent, messages | assignment, model?: "auto" | "claude" | <catalog key>, taskType?, planned?, brain?, effort? }.
// "auto" (the default) runs the most cost-efficient model for the task type (docs/model-catalog.md), with fallbacks.
import type { Config } from "@netlify/functions";
import { webBrain, webEffort, type Effort } from "../../server/claude.js";
import { guard, json, sse } from "../../server/http.js";
import { agent, assignmentMessage, cleanMessages, ORCHESTRATOR, system } from "../../server/prompts.js";
import { describe, modelChoice, routeEffort, plannedModel, routeError, routesFor, streamRouted, taskTypeFor } from "../../server/route.js";

export default async (req: Request) => {
  const started = Date.now();
  const checked = await guard(req);
  if ("error" in checked) return checked.error;
  const { body } = checked;
  const a = agent(body.agent);
  if (!a) return json(404, { message: "Unknown agent." });

  let messages;
  const assignment = body.assignment as Record<string, unknown> | undefined;
  if (assignment && typeof assignment === "object") {
    const orchestrator = agent(ORCHESTRATOR)!;
    const text = assignmentMessage(orchestrator, String(assignment.original ?? ""), String(assignment.summary ?? ""), String(assignment.question ?? ""), String(assignment.reason ?? ""));
    messages = [{ role: "user" as const, content: text }];
  } else {
    messages = cleanMessages(body.messages);
  }
  if (!messages) return json(400, { message: "Send a conversation that ends with your question." });

  const choice = modelChoice(body.model);
  const task = taskTypeFor(body.taskType, a.id);
  const brain = webBrain(typeof body.brain === "string" ? body.brain : a.brain);
  // Claude only: the agent's own effort (capped). Auto or a chosen model: the task type's effort from the catalog.
  const effort: Effort = webEffort(typeof body.effort === "string" ? body.effort : choice === "claude" ? a.effort : task.effort);
  const planned = body.planned === undefined ? undefined : plannedModel(body.planned, task);
  const routes = routesFor(choice, task, brain, planned);
  return sse(async (sink) => {
    sink.send("meta", { agent: a.id, brain, effort, taskType: task.name, choice, ...(routes[0] ? { ...describe(routes[0]), effort: routeEffort(routes[0], effort) ?? effort } : {}) });
    try {
      const reply = await streamRouted({
        routes,
        system: system(a),
        messages,
        effort,
        maxTokens: 8_000,
        deadline: started + 50_000,
        signal: req.signal,
        onText: (text) => sink.send("delta", { text }),
        onThinking: () => sink.send("thinking", {}),
        onSwitch: (from, to, reason) => {
          sink.send("notice", { message: `${from.name} (${from.api === "claude" ? "Claude API" : "OpenRouter"}) was not used: ${reason}. Answering with ${to.name}.` });
          sink.send("meta", { ...describe(to), effort: routeEffort(to, effort) ?? effort });
        },
      });
      if (reply.stopReason === "refusal") sink.send("notice", { message: "The model declined this request." });
      if (reply.stopReason === "max_tokens") sink.send("notice", { message: "The answer hit its length limit." });
      if (reply.cutOff) sink.send("notice", { message: "The answer was cut off at the app's time limit. Ask a narrower question, or use the agent in Claude Code for long work." });
      sink.send("done", { ...describe(reply.route), effort: routeEffort(reply.route, effort) ?? effort, modelId: reply.modelId, provider: reply.provider, cost: reply.cost, costEstimated: reply.costEstimated, stop_reason: reply.stopReason });
    } catch (error) {
      sink.send("error", { message: routeError(error) });
    }
  }, req.signal);
};

export const config: Config = {
  path: "/api/chat",
  method: "POST",
  rateLimit: { windowLimit: 40, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
