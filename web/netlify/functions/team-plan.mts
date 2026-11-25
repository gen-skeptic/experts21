// POST /api/team/plan: the orchestrator decides which experts answer what, on which brain (structured JSON output).
import type { Config } from "@netlify/functions";
import { errorMessage, structuredReply, webEffort } from "../../server/claude.js";
import { guard, json } from "../../server/http.js";
import { agent, cleanMessages, ORCHESTRATOR, parsePlan, PLAN_INSTRUCTIONS, planSchema, system } from "../../server/prompts.js";

export default async (req: Request) => {
  const checked = await guard(req);
  if ("error" in checked) return checked.error;
  const messages = cleanMessages(checked.body.messages);
  if (!messages) return json(400, { message: "Send a conversation that ends with your question." });
  const orchestrator = agent(ORCHESTRATOR)!;
  try {
    // Routing is a quick judgment call, so the orchestrator's brain runs at low effort here.
    const reply = await structuredReply({
      system: system(orchestrator, PLAN_INSTRUCTIONS),
      messages,
      brain: orchestrator.brain,
      effort: webEffort("low"),
      schema: planSchema(),
      maxTokens: 4_000,
      signal: req.signal,
    });
    if (reply.value === null) return json(502, { message: "The orchestrator couldn't make a routing plan for this question. Try rephrasing it." });
    return json(200, { ...parsePlan(reply.value), model: reply.model, routedBy: orchestrator.name });
  } catch (error) {
    return json(502, { message: errorMessage(error) });
  }
};

export const config: Config = {
  path: "/api/team/plan",
  method: "POST",
  rateLimit: { windowLimit: 15, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
