// Netlify's AI Gateway: on credit-based plans Netlify injects its own ANTHROPIC_API_KEY / ANTHROPIC_BASE_URL and
// OPENROUTER_API_KEY / OPENROUTER_BASE_URL into functions whenever it can't see yours, and bills every call that goes
// through it to your Netlify credits. This app uses your own keys only, so it never runs up Netlify AI charges by
// accident. Set ALLOW_NETLIFY_AI_GATEWAY=true to let it use the gateway's credentials when yours are missing.
import { env } from "./env.js";

/** Where a provider's credentials in this function's environment came from. */
export type KeySource = "own" | "netlify-gateway" | "none";

export function gatewayAllowed(): boolean {
  return env("ALLOW_NETLIFY_AI_GATEWAY").toLowerCase() === "true";
}

/** True for a base URL that points at Netlify's AI Gateway (for example https://<site>.netlify.app/.netlify/ai). */
export function isGatewayUrl(url: string): boolean {
  if (!url) return false;
  const gatewayUrl = env("NETLIFY_AI_GATEWAY_URL");
  return /\/\.netlify\/ai(\/|$)/.test(url) || (!!gatewayUrl && url.startsWith(gatewayUrl));
}

/** Classify a key and base URL pair: your own key, Netlify's injected gateway key, or nothing. */
export function keySource(key: string, baseUrl: string): KeySource {
  if (!key) return "none";
  const gatewayKey = env("NETLIFY_AI_GATEWAY_KEY");
  return (gatewayKey && key === gatewayKey) || isGatewayUrl(baseUrl) ? "netlify-gateway" : "own";
}

/** Whether calls may use credentials from this source. */
export function usable(source: KeySource): boolean {
  return source === "own" || (source === "netlify-gateway" && gatewayAllowed());
}
