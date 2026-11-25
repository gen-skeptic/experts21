// POST /api/team/plan: the orchestrator decides which experts answer what, with which task type and model (structured
// JSON output). Body: { messages, model?: "auto" | "claude" | <catalog key> }. On "auto" the plan itself runs on the
// catalog's routing model; on "claude", on the orchestrator's own brain.
import type { Config } from "@netlify/functions";
import { webEffort } from "../../server/claude.js";
import { guard, json } from "../../server/http.js";
import { agent, cleanMessages, ORCHESTRATOR, parsePlan, PLAN_INSTRUCTIONS, planSchema, system } from "../../server/prompts.js";
import { CATALOG, describe, modelChoice, routeError, routesFor, structuredRouted, taskType } from "../../server/route.js";

export default async (req: Request) => {
  const checked = await guard(req);
  if ("error" in checked) return checked.error;
  const messages = cleanMessages(checked.body.messages);
  if (!messages) return json(400, { message: "Send a conversation that ends with your question." });
  const orchestrator = agent(ORCHESTRATOR)!;
  const choice = modelChoice(checked.body.model);
  const routing = CATALOG.roles.routing;
  // The routing role as a one-off task type: its primary and fallback, then the orchestrator's own brain.
  const routes = routesFor(choice, { ...taskType(CATALOG.roles.synthesis.task_type), primary: routing.primary, fallback: routing.fallback }, orchestrator.brain);
  const notices: string[] = [];
  try {
    // Routing is a quick judgment call, so it runs at low effort.
    const reply = await structuredRouted({
      routes,
      system: system(orchestrator, PLAN_INSTRUCTIONS),
      messages,
      effort: webEffort("low"),
      schema: planSchema(),
      maxTokens: 4_000,
      signal: req.signal,
      onSwitch: (from, to, reason) => notices.push(`${from.name} was not used for routing: ${reason}. Routed with ${to.name}.`),
    });
    if (reply.value === null) return json(502, { message: "The orchestrator couldn't make a routing plan for this question. Try rephrasing it." });
    return json(200, { ...parsePlan(reply.value), ...describe(reply.route), modelId: reply.modelId, cost: reply.cost, notices, routedBy: orchestrator.name });
  } catch (error) {
    return json(502, { message: routeError(error) });
  }
};

export const config: Config = {
  path: "/api/team/plan",
  method: "POST",
  rateLimit: { windowLimit: 15, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
