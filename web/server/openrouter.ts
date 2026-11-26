// OpenRouter calls: any model in docs/model-catalog.md through one OpenAI-compatible endpoint. Every call runs inside a
// Netlify Function with the key from OPENROUTER_API_KEY, so the key never reaches the browser.
//
// Privacy: by default every request asks for zero-data-retention endpoints only (provider.zdr) and never an endpoint
// that may store or train on prompts (provider.data_collection: "deny"). Set OPENROUTER_ZDR=false to allow endpoints
// that keep data for a while (still never for training).
import { env } from "./env.js";
import { isGatewayUrl, keySource, usable, type KeySource } from "./gateway.js";

/** Where the OpenRouter key in this function's environment came from: yours, Netlify's AI Gateway, or nowhere. */
export function openrouterSource(): KeySource {
  return keySource(env("OPENROUTER_API_KEY"), env("OPENROUTER_BASE_URL"));
}

/** True when the app may call OpenRouter: your own OPENROUTER_API_KEY (the AI Gateway's only with ALLOW_NETLIFY_AI_GATEWAY=true). */
export function openrouterReady(): boolean {
  return usable(openrouterSource());
}

export function zdrEnforced(): boolean {
  return env("OPENROUTER_ZDR").toLowerCase() !== "false";
}

/** Your own key goes to openrouter.ai (or the base URL you set), never to the AI Gateway's URL. */
function baseUrl(): string {
  const base = env("OPENROUTER_BASE_URL");
  const url = openrouterSource() === "own" && isGatewayUrl(base) ? "" : base;
  return (url || "https://openrouter.ai/api/v1").replace(/\/+$/, "");
}

export class OpenRouterError extends Error {
  constructor(
    public status: number,
    message: string,
  ) {
    super(message);
  }
}

export function openrouterErrorMessage(error: OpenRouterError): string {
  const detail = error.message ? `: ${error.message}` : "";
  switch (error.status) {
    case 401:
      return "The OpenRouter API key set in Netlify was rejected. Check OPENROUTER_API_KEY.";
    case 402:
      return "The OpenRouter account is out of credit.";
    case 403:
      return `OpenRouter refused the request${detail}`;
    case 404:
      return `OpenRouter has no endpoint for this model that meets the privacy settings${detail}`;
    case 408:
      return "The model on OpenRouter took too long to answer.";
    case 429:
      return "OpenRouter is rate limiting this app or the model's provider. Try again in a minute.";
    case 400:
    case 422:
      return `OpenRouter rejected the request${detail}`;
    default:
      return `OpenRouter returned an error${error.status ? ` (HTTP ${error.status})` : ""}${detail}`;
  }
}

export interface SystemBlock {
  text: string;
  cache?: boolean;
}

interface Common {
  /** OpenRouter model ID, for example deepseek/deepseek-v4.1-flash-1017. */
  model: string;
  system: SystemBlock[];
  messages: { role: "user" | "assistant"; content: string }[];
  /** A reasoning effort the model supports, or null to leave it to the model. */
  effort: string | null;
  maxTokens: number;
}

export interface OpenRouterResult {
  model: string;
  provider: string | null;
  stopReason: string | null;
  cutOff: boolean;
  /** What the call cost in USD, as OpenRouter reports it. */
  cost: number | null;
}

function privacy(): Record<string, unknown> {
  return zdrEnforced() ? { zdr: true, data_collection: "deny" } : { data_collection: "deny" };
}

function requestBody(o: Common): Record<string, unknown> {
  // Anthropic and Google models take explicit cache breakpoints; the others cache long prompts automatically.
  const breakpoints = /^(anthropic|google)\//.test(o.model);
  const system = breakpoints
    ? { role: "system", content: o.system.map((b) => ({ type: "text", text: b.text, ...(b.cache ? { cache_control: { type: "ephemeral" } } : {}) })) }
    : { role: "system", content: o.system.map((b) => b.text).join("\n\n") };
  return {
    model: o.model,
    messages: [system, ...o.messages],
    max_tokens: o.maxTokens,
    ...(o.effort ? { reasoning: { effort: o.effort, exclude: false } } : {}),
    provider: privacy(),
  };
}

async function post(body: Record<string, unknown>, signal: AbortSignal): Promise<Response> {
  const res = await fetch(`${baseUrl()}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env("OPENROUTER_API_KEY")}`,
      "Content-Type": "application/json",
      "HTTP-Referer": env("URL") || "https://dio-experts21.netlify.app",
      "X-Title": "DIO Experts21",
    },
    body: JSON.stringify(body),
    signal,
  });
  if (!res.ok) {
    let message = "";
    try {
      const data = (await res.json()) as { error?: { message?: string } };
      message = String(data?.error?.message ?? "");
    } catch {
      // not JSON
    }
    throw new OpenRouterError(res.status, message.slice(0, 300));
  }
  return res;
}

const STOP: Record<string, string> = { stop: "end_turn", length: "max_tokens", content_filter: "refusal", tool_calls: "tool_use" };

/** Stream one reply. Stops at `deadline` (milliseconds since the epoch) so the function finishes inside Netlify's limit. */
export async function streamOpenRouter(
  o: Common & {
    deadline: number;
    signal: AbortSignal;
    onText: (text: string) => void;
    onThinking?: () => void;
  },
): Promise<OpenRouterResult> {
  const controller = new AbortController();
  const stop = () => controller.abort();
  o.signal.addEventListener("abort", stop);
  let cutOff = false;
  const timer = setTimeout(() => {
    cutOff = true;
    controller.abort();
  }, Math.max(1_000, o.deadline - Date.now()));
  const result: OpenRouterResult = { model: o.model, provider: null, stopReason: null, cutOff: false, cost: null };
  let thinking = false;
  try {
    const res = await post({ ...requestBody(o), stream: true }, controller.signal);
    if (!res.body) throw new OpenRouterError(502, "empty response");
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    let done = false;
    while (!done) {
      const chunk = await reader.read();
      if (chunk.done) break;
      buffer += decoder.decode(chunk.value, { stream: true });
      let end: number;
      while ((end = buffer.indexOf("\n")) >= 0) {
        const line = buffer.slice(0, end).trim();
        buffer = buffer.slice(end + 1);
        if (!line.startsWith("data:")) continue; // blank lines and ": OPENROUTER PROCESSING" keep-alives
        const data = line.slice(5).trim();
        if (data === "[DONE]") {
          done = true;
          break;
        }
        let event: Record<string, any>;
        try {
          event = JSON.parse(data);
        } catch {
          continue;
        }
        if (event.error) throw new OpenRouterError(Number(event.error.code) || 502, String(event.error.message ?? "").slice(0, 300));
        if (typeof event.model === "string") result.model = event.model;
        if (typeof event.provider === "string") result.provider = event.provider;
        if (typeof event.usage?.cost === "number") result.cost = event.usage.cost;
        const choice = event.choices?.[0];
        if (!choice) continue;
        const delta = choice.delta ?? {};
        if (!thinking && (delta.reasoning || (Array.isArray(delta.reasoning_details) && delta.reasoning_details.length))) {
          thinking = true;
          o.onThinking?.();
        }
        if (typeof delta.content === "string" && delta.content) o.onText(delta.content);
        if (choice.finish_reason) {
          if (choice.finish_reason === "error") throw new OpenRouterError(502, String(choice.error?.message ?? "the model's provider failed mid-answer"));
          result.stopReason = STOP[choice.finish_reason] ?? choice.finish_reason;
        }
      }
    }
    if (done || result.stopReason) await reader.cancel().catch(() => undefined);
  } catch (error) {
    if (!controller.signal.aborted) throw error;
  } finally {
    clearTimeout(timer);
    o.signal.removeEventListener("abort", stop);
  }
  result.cutOff = cutOff;
  return result;
}

/** One structured-output call (the routing plan): the parsed JSON object, or null on a refusal or unparsable output. */
export async function structuredOpenRouter(
  o: Common & { schema: Record<string, unknown>; name: string; signal: AbortSignal },
): Promise<{ model: string; provider: string | null; value: unknown; cost: number | null }> {
  const signal = AbortSignal.any([o.signal, AbortSignal.timeout(50_000)]);
  const res = await post(
    {
      ...requestBody(o),
      response_format: { type: "json_schema", json_schema: { name: o.name, strict: true, schema: o.schema } },
      // Only endpoints that support structured outputs, with the same privacy rules.
      provider: { ...privacy(), require_parameters: true },
    },
    signal,
  );
  const data = (await res.json()) as Record<string, any>;
  const choice = data.choices?.[0];
  const content = choice?.message?.content;
  const text = typeof content === "string" ? content : Array.isArray(content) ? content.map((c: { text?: string }) => c?.text ?? "").join("") : "";
  const out = { model: String(data.model ?? o.model), provider: typeof data.provider === "string" ? data.provider : null, cost: typeof data.usage?.cost === "number" ? data.usage.cost : null };
  if (choice?.finish_reason === "content_filter" || !text) return { ...out, value: null };
  try {
    return { ...out, value: JSON.parse(text) };
  } catch {
    return { ...out, value: null };
  }
}
