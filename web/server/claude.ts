// Claude API calls. Every call runs inside a Netlify Function, so the API key never reaches the browser.
import Anthropic from "@anthropic-ai/sdk";
import { env } from "./env.js";

/** Brains the web app runs. Frontier (fable) is left out: its long turns don't fit Netlify's 60-second limit. */
export const WEB_BRAINS = ["haiku", "sonnet", "opus"] as const;
export type WebBrain = (typeof WEB_BRAINS)[number];
export const EFFORTS = ["low", "medium", "high"] as const;
export type Effort = (typeof EFFORTS)[number];

const DEFAULT_MODELS: Record<WebBrain, string> = {
  opus: "claude-opus-5-5",
  sonnet: "claude-sonnet-5-5",
  haiku: "claude-haiku-5-5",
};

export function webBrain(brain: string): WebBrain {
  return (WEB_BRAINS as readonly string[]).includes(brain) ? (brain as WebBrain) : "opus";
}

/** The model for a brain: an ANTHROPIC_MODEL_<BRAIN> override from Netlify, otherwise the current release. */
export function modelFor(brain: string): string {
  const b = webBrain(brain);
  return env(`ANTHROPIC_MODEL_${b.toUpperCase()}`) || DEFAULT_MODELS[b];
}

/**
 * Effort for the web app. Netlify ends a function at 60 seconds, so the web app caps effort (medium by default; set
 * WEB_MAX_EFFORT to low or high to change it). Claude Code and the SDK script run each agent at its full effort.
 */
export function webEffort(effort: string, cap?: Effort): Effort {
  const configured = (EFFORTS as readonly string[]).includes(env("WEB_MAX_EFFORT")) ? (env("WEB_MAX_EFFORT") as Effort) : "medium";
  const limit = cap ?? configured;
  const want = (EFFORTS as readonly string[]).includes(effort) ? (effort as Effort) : "medium";
  return EFFORTS.indexOf(want) <= EFFORTS.indexOf(limit) ? want : limit;
}

/**
 * True when the functions can call Claude: an ANTHROPIC_API_KEY set in Netlify, or Netlify's AI Gateway, which injects
 * Claude credentials into functions on credit-based plans (billed to Netlify credits) unless you set your own key.
 */
export function aiConfigured(): boolean {
  return env("ANTHROPIC_API_KEY") !== "" || env("NETLIFY_AI_GATEWAY_KEY") !== "";
}

let client: Anthropic | null = null;
function anthropic(): Anthropic {
  client ??= new Anthropic({
    apiKey: env("ANTHROPIC_API_KEY"),
    baseURL: env("ANTHROPIC_BASE_URL") || undefined,
    maxRetries: 1,
    timeout: 55_000,
  });
  return client;
}

/**
 * Server-side refusal fallbacks: when a safety classifier declines a request, the API re-runs it on Anthropic's
 * recommended fallback model in the same call. Opus and Sonnet support it; Haiku has no server-side fallback.
 */
function fallbackParams(brain: WebBrain): Pick<Anthropic.Beta.MessageCreateParams, "betas" | "fallbacks"> {
  return brain === "haiku" ? {} : { betas: ["server-side-fallback-2026-07-01"], fallbacks: "default" };
}

export function errorMessage(error: unknown): string {
  if (error instanceof Anthropic.AuthenticationError) return "The Anthropic API key set in Netlify was rejected. Check ANTHROPIC_API_KEY.";
  if (error instanceof Anthropic.PermissionDeniedError) return "The Anthropic API key can't use this model.";
  if (error instanceof Anthropic.RateLimitError) return "The Claude API is rate limiting this app. Try again in a minute.";
  if (error instanceof Anthropic.BadRequestError) return `The Claude API rejected the request: ${error.message}`;
  if (error instanceof Anthropic.APIConnectionTimeoutError) return "The Claude API took too long to answer.";
  if (error instanceof Anthropic.APIError) return `The Claude API returned an error${error.status ? ` (HTTP ${error.status})` : ""}.`;
  return error instanceof Error ? error.message : "The request failed.";
}

export interface ReplyResult {
  model: string;
  stopReason: string | null;
  cutOff: boolean;
}

/**
 * Stream one reply. The system prompt's first block carries a cache breakpoint (it is the same for every turn with an
 * agent). Stops at `deadline` (milliseconds since the epoch) so the function finishes inside Netlify's limit.
 */
export async function streamReply(options: {
  system: Anthropic.Beta.BetaTextBlockParam[];
  messages: Anthropic.Beta.BetaMessageParam[];
  brain: string;
  effort: Effort;
  maxTokens: number;
  deadline: number;
  signal: AbortSignal;
  onText: (text: string) => void;
  onThinking?: () => void;
}): Promise<ReplyResult> {
  const brain = webBrain(options.brain);
  const model = modelFor(brain);
  const controller = new AbortController();
  const stop = () => controller.abort();
  options.signal.addEventListener("abort", stop);
  let cutOff = false;
  const timer = setTimeout(() => {
    cutOff = true;
    controller.abort();
  }, Math.max(1_000, options.deadline - Date.now()));
  const result: ReplyResult = { model, stopReason: null, cutOff: false };
  try {
    const stream = anthropic().beta.messages.stream(
      {
        model,
        max_tokens: options.maxTokens,
        system: options.system,
        messages: options.messages,
        output_config: { effort: options.effort },
        ...fallbackParams(brain),
      },
      { signal: controller.signal },
    );
    for await (const event of stream) {
      if (event.type === "message_start") result.model = event.message.model;
      else if (event.type === "content_block_start" && event.content_block.type === "thinking") options.onThinking?.();
      else if (event.type === "content_block_delta" && event.delta.type === "text_delta") options.onText(event.delta.text);
      else if (event.type === "message_delta" && event.delta.stop_reason) result.stopReason = event.delta.stop_reason;
    }
  } catch (error) {
    if (!(error instanceof Anthropic.APIUserAbortError) && !controller.signal.aborted) throw error;
  } finally {
    clearTimeout(timer);
    options.signal.removeEventListener("abort", stop);
  }
  result.cutOff = cutOff;
  return result;
}

/** One structured-output call (the routing plan): returns the parsed JSON object, or null on a refusal. */
export async function structuredReply(options: {
  system: Anthropic.Beta.BetaTextBlockParam[];
  messages: Anthropic.Beta.BetaMessageParam[];
  brain: string;
  effort: Effort;
  schema: Record<string, unknown>;
  maxTokens: number;
  signal: AbortSignal;
}): Promise<{ model: string; value: unknown }> {
  const brain = webBrain(options.brain);
  const response = await anthropic().beta.messages.create(
    {
      model: modelFor(brain),
      max_tokens: options.maxTokens,
      system: options.system,
      messages: options.messages,
      output_config: { effort: options.effort, format: { type: "json_schema", schema: options.schema } },
      ...fallbackParams(brain),
    },
    { signal: options.signal, timeout: 50_000 },
  );
  if (response.stop_reason === "refusal") return { model: response.model, value: null };
  const text = response.content.map((block) => (block.type === "text" ? block.text : "")).join("");
  try {
    return { model: response.model, value: JSON.parse(text) };
  } catch {
    return { model: response.model, value: null };
  }
}
