// POST /api/team/synthesize: the orchestrator combines the experts' answers into one, streamed like /api/chat.
import type { Config } from "@netlify/functions";
import { errorMessage, streamReply, webEffort } from "../../server/claude.js";
import { guard, json, sse } from "../../server/http.js";
import { agent, cleanMessages, ORCHESTRATOR, synthesisMessage, SYNTHESIS_INSTRUCTIONS, system } from "../../server/prompts.js";

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
  return sse(async (sink) => {
    const effort = webEffort(orchestrator.effort);
    sink.send("meta", { agent: orchestrator.id, brain: orchestrator.brain, effort });
    try {
      const reply = await streamReply({
        system: system(orchestrator, SYNTHESIS_INSTRUCTIONS),
        messages,
        brain: orchestrator.brain,
        effort,
        maxTokens: 8_000,
        deadline: started + 50_000,
        signal: req.signal,
        onText: (text) => sink.send("delta", { text }),
        onThinking: () => sink.send("thinking", {}),
      });
      if (reply.stopReason === "refusal") sink.send("notice", { message: "The model declined this request." });
      if (reply.cutOff) sink.send("notice", { message: "The combined answer was cut off at the app's time limit." });
      sink.send("done", { model: reply.model, stop_reason: reply.stopReason });
    } catch (error) {
      sink.send("error", { message: errorMessage(error) });
    }
  }, req.signal);
};

export const config: Config = {
  path: "/api/team/synthesize",
  method: "POST",
  rateLimit: { windowLimit: 15, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
