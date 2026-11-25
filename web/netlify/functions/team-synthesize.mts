// POST /api/team/synthesize: the orchestrator combines the experts' answers into one, streamed like /api/chat.
// Body: { messages, summary, answers, model?: "auto" | "claude" | <catalog key> }.
import type { Config } from "@netlify/functions";
import { webEffort } from "../../server/claude.js";
import { guard, json, sse } from "../../server/http.js";
import { agent, cleanMessages, ORCHESTRATOR, synthesisMessage, SYNTHESIS_INSTRUCTIONS, system } from "../../server/prompts.js";
import { CATALOG, describe, modelChoice, routeEffort, routeError, routesFor, streamRouted, taskType } from "../../server/route.js";

export default async (req: Request) => {
  const started = Date.now();
  const checked = await guard(req);
  if ("error" in checked) return checked.error;
  const { body } = checked;
  const messages = cleanMessages(body.messages);
  if (!messages) return json(400, { message: "Send a conversation that ends with your question." });
  const answers = (Array.isArray(body.answers) ? body.answers : [])
    .filter((x): x is { agent: string; text: string } => !!x && typeof x === "object" && typeof x.agent === "string" && typeof x.text === "string")
    .slice(0, 5);
  const question = String(messages[messages.length - 1].content);
  messages[messages.length - 1] = { role: "user", content: synthesisMessage(question, String(body.summary ?? ""), answers) };
  const orchestrator = agent(ORCHESTRATOR)!;
  const choice = modelChoice(body.model);
  const task = taskType(CATALOG.roles.synthesis.task_type);
  const effort = webEffort(choice === "claude" ? orchestrator.effort : task.effort);
  const routes = routesFor(choice, task, orchestrator.brain);
  return sse(async (sink) => {
    sink.send("meta", { agent: orchestrator.id, brain: orchestrator.brain, effort, taskType: task.name, choice, ...(routes[0] ? { ...describe(routes[0]), effort: routeEffort(routes[0], effort) ?? effort } : {}) });
    try {
      const reply = await streamRouted({
        routes,
        system: system(orchestrator, SYNTHESIS_INSTRUCTIONS),
        messages,
        effort,
        maxTokens: 8_000,
        deadline: started + 50_000,
        signal: req.signal,
        onText: (text) => sink.send("delta", { text }),
        onThinking: () => sink.send("thinking", {}),
        onSwitch: (from, to, reason) => {
          sink.send("notice", { message: `${from.name} was not used: ${reason}. Combining with ${to.name}.` });
          sink.send("meta", { ...describe(to), effort: routeEffort(to, effort) ?? effort });
        },
      });
      if (reply.stopReason === "refusal") sink.send("notice", { message: "The model declined this request." });
      if (reply.cutOff) sink.send("notice", { message: "The combined answer was cut off at the app's time limit." });
      sink.send("done", { ...describe(reply.route), effort: routeEffort(reply.route, effort) ?? effort, modelId: reply.modelId, provider: reply.provider, cost: reply.cost, costEstimated: reply.costEstimated, stop_reason: reply.stopReason });
    } catch (error) {
      sink.send("error", { message: routeError(error) });
    }
  }, req.signal);
};

export const config: Config = {
  path: "/api/team/synthesize",
  method: "POST",
  rateLimit: { windowLimit: 15, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
