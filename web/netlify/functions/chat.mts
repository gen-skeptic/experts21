// POST /api/chat: one agent's reply, streamed as server-sent events: meta, thinking?, delta..., notice?, done (or error).
// Team mode uses it too: each assigned expert answers its part through this endpoint, in parallel.
import type { Config } from "@netlify/functions";
import { errorMessage, streamReply, webBrain, webEffort } from "../../server/claude.js";
import { guard, json, sse } from "../../server/http.js";
import { agent, assignmentMessage, cleanMessages, ORCHESTRATOR, system } from "../../server/prompts.js";

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

  const brain = webBrain(typeof body.brain === "string" ? body.brain : a.brain);
  const effort = webEffort(typeof body.effort === "string" ? body.effort : a.effort);
  return sse(async (sink) => {
    sink.send("meta", { agent: a.id, brain, effort });
    try {
      const reply = await streamReply({
        system: system(a),
        messages,
        brain,
        effort,
        maxTokens: 8_000,
        deadline: started + 50_000,
        signal: req.signal,
        onText: (text) => sink.send("delta", { text }),
        onThinking: () => sink.send("thinking", {}),
      });
      if (reply.stopReason === "refusal") sink.send("notice", { message: "The model declined this request." });
      if (reply.stopReason === "max_tokens") sink.send("notice", { message: "The answer hit its length limit." });
      if (reply.cutOff) sink.send("notice", { message: "The answer was cut off at the app's time limit. Ask a narrower question, or use the agent in Claude Code for long work." });
      sink.send("done", { model: reply.model, stop_reason: reply.stopReason });
    } catch (error) {
      sink.send("error", { message: errorMessage(error) });
    }
  }, req.signal);
};

export const config: Config = {
  path: "/api/chat",
  method: "POST",
  rateLimit: { windowLimit: 40, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
