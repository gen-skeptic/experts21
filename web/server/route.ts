// Model routing for the web app: which model answers, through which API, with what fallbacks.
//
// The choice comes from the browser's model menu:
//   "auto"   the most cost-efficient model for the task type (docs/model-catalog.md), then its fallback
//   "claude" the agent's own Claude brain (Opus, Sonnet or Haiku), as in Claude Code
//   a key    one model from the catalog, for example "deepseek-v4.1-flash"
// Every chain ends with the agent's own Claude brain. Claude models go to the Claude API directly when ANTHROPIC_API_KEY
// is set (prompt caching and Anthropic's refusal fallback), otherwise through OpenRouter; every other model goes
// through OpenRouter (OPENROUTER_API_KEY). A route that fails before writing any text hands over to the next one.
import type Anthropic from "@anthropic-ai/sdk";
import { DATA } from "./agents-data.generated.js";
import type { ModelRecord, TaskTypeRecord } from "./agents-data.generated.js";
import { claudeReady, EFFORTS, errorMessage as claudeError, modelFor, streamReply, structuredReply, webBrain, type Effort, type Usage, type WebBrain } from "./claude.js";
import { OpenRouterError, openrouterErrorMessage, openrouterReady, streamOpenRouter, structuredOpenRouter } from "./openrouter.js";

export const CATALOG = DATA.catalog;
export const MODEL_KEYS = Object.keys(CATALOG.models);
export const TASK_NAMES = CATALOG.task_types.map((t) => t.name);
const FRONTIER_KEYS = new Set(CATALOG.task_types.filter((t) => t.tier === "frontier").map((t) => t.primary));
const BRAIN_KEY: Record<WebBrain, string> = { opus: "claude-opus-5.5", sonnet: "claude-sonnet-5.5", haiku: "claude-haiku-5.5" };
const OPENROUTER_EFFORTS = ["none", "minimal", "low", "medium", "high", "xhigh", "max"];
/** A route that has shown no sign of life (no text, no thinking) after this long hands over to the next one. */
const FIRST_TEXT_MS = 20_000;

export type ModelChoice = string;

export interface Route {
  /** Catalog key, when the model is in the catalog. */
  key: string | null;
  name: string;
  api: "claude" | "openrouter";
  /** Claude API model ID or OpenRouter model ID. */
  model: string;
  brain: WebBrain | null;
  efforts: string[] | null;
}

export function anyModelReady(): boolean {
  return claudeReady() || openrouterReady();
}

export function modelChoice(value: unknown): ModelChoice {
  if (value === "auto" || value === "claude") return value;
  if (typeof value === "string" && Object.hasOwn(CATALOG.models, value)) return value;
  return "auto";
}

export function taskTypeFor(value: unknown, agentId: string): TaskTypeRecord {
  const name = typeof value === "string" && TASK_NAMES.includes(value) ? value : CATALOG.agent_task_type[agentId];
  return CATALOG.task_types.find((t) => t.name === name) ?? CATALOG.task_types[0];
}

export function taskType(name: string): TaskTypeRecord {
  return CATALOG.task_types.find((t) => t.name === name) ?? CATALOG.task_types[0];
}

/** A model the orchestrator picked for an assignment: any catalog key, but the Frontier model only for Frontier work. */
export function plannedModel(value: unknown, task: TaskTypeRecord): string {
  const key = typeof value === "string" && Object.hasOwn(CATALOG.models, value) ? value : task.primary;
  return FRONTIER_KEYS.has(key) && task.tier !== "frontier" ? task.primary : key;
}

function brainOfKey(key: string): WebBrain | null {
  const hit = (Object.entries(BRAIN_KEY) as [WebBrain, string][]).find(([, k]) => k === key);
  return hit ? hit[0] : null;
}

function catalogRoute(key: string): Route | null {
  const m: ModelRecord = CATALOG.models[key];
  const brain = brainOfKey(key);
  if (m.anthropic && brain && claudeReady()) return { key, name: m.name, api: "claude", model: modelFor(brain), brain, efforts: null };
  if (openrouterReady()) return { key, name: m.name, api: "openrouter", model: m.openrouter, brain: null, efforts: m.efforts };
  return null;
}

/** The ordered routes to try: the choice, then (for Auto) the task type's fallback, then the agent's own Claude brain. */
export function routesFor(choice: ModelChoice, task: TaskTypeRecord, brain: string, planned?: string): Route[] {
  const keys = choice === "claude" ? [] : choice === "auto" ? [planned ?? task.primary, task.primary, task.fallback] : [choice];
  keys.push(BRAIN_KEY[webBrain(brain)]);
  const out: Route[] = [];
  for (const key of keys) {
    const r = catalogRoute(key);
    if (r && !out.some((x) => x.api === r.api && x.model === r.model)) out.push(r);
  }
  return out;
}

/** Effort for a route: Claude takes low, medium or high; other models get the closest effort they support, never higher. */
export function routeEffort(route: Route, effort: Effort): string | null {
  if (route.api === "claude") return effort;
  const supported = (route.efforts ?? []).filter((e) => OPENROUTER_EFFORTS.includes(e));
  if (!supported.length) return null;
  if (supported.includes(effort)) return effort;
  const want = OPENROUTER_EFFORTS.indexOf(effort);
  const lower = supported.filter((e) => OPENROUTER_EFFORTS.indexOf(e) <= want && e !== "none");
  return lower.length ? lower[lower.length - 1] : supported.find((e) => e !== "none") ?? null;
}

export function routeError(error: unknown): string {
  return error instanceof OpenRouterError ? openrouterErrorMessage(error) : claudeError(error);
}

/** Estimated cost of a Claude API call from token counts and the catalog's list prices (USD). */
function claudeCost(route: Route, usage: Usage): number | null {
  const m = route.key ? CATALOG.models[route.key] : null;
  if (!m) return null;
  return (usage.input * m.input + usage.cacheWrite * m.input * 1.25 + usage.cacheRead * m.cache_read + usage.output * m.output) / 1e6;
}

export function describe(route: Route) {
  return { model: route.name, modelId: route.model, api: route.api === "claude" ? "Claude API" : "OpenRouter" };
}

export interface RoutedReply {
  route: Route;
  modelId: string;
  provider: string | null;
  stopReason: string | null;
  cutOff: boolean;
  cost: number | null;
  costEstimated: boolean;
}

/** Stream a reply through the first route that works. `onSwitch` reports each handover. */
export async function streamRouted(options: {
  routes: Route[];
  system: Anthropic.Beta.BetaTextBlockParam[];
  messages: { role: "user" | "assistant"; content: string }[];
  effort: Effort;
  maxTokens: number;
  deadline: number;
  signal: AbortSignal;
  onText: (text: string) => void;
  onThinking?: () => void;
  onSwitch?: (from: Route, to: Route, reason: string) => void;
}): Promise<RoutedReply> {
  const { routes } = options;
  if (!routes.length) throw new Error("No model is available: add ANTHROPIC_API_KEY or OPENROUTER_API_KEY in Netlify under Project configuration > Environment variables, then redeploy.");
  for (let i = 0; i < routes.length; i++) {
    const route = routes[i];
    const next = routes[i + 1];
    let wrote = false;
    let alive = false;
    const onText = (text: string) => {
      wrote = alive = true;
      options.onText(text);
    };
    const onThinking = () => {
      alive = true;
      options.onThinking?.();
    };
    // Hand over to the next route if this one is silent for too long (only while a next route exists).
    const attempt = new AbortController();
    const parent = () => attempt.abort();
    options.signal.addEventListener("abort", parent);
    let stalled = false;
    const watchdog = next
      ? setTimeout(() => {
          if (!alive) {
            stalled = true;
            attempt.abort();
          }
        }, FIRST_TEXT_MS)
      : null;
    try {
      let reply: RoutedReply;
      if (route.api === "claude") {
        const r = await streamReply({
          system: options.system,
          messages: options.messages,
          brain: route.brain ?? "sonnet",
          model: route.model,
          effort: (routeEffort(route, options.effort) as Effort) ?? options.effort,
          maxTokens: options.maxTokens,
          deadline: options.deadline,
          signal: attempt.signal,
          onText,
          onThinking,
        });
        reply = { route, modelId: r.model, provider: "Anthropic", stopReason: r.stopReason, cutOff: r.cutOff, cost: claudeCost(route, r.usage), costEstimated: true };
      } else {
        const r = await streamOpenRouter({
          model: route.model,
          system: options.system.map((b) => ({ text: b.text, cache: !!b.cache_control })),
          messages: options.messages,
          effort: routeEffort(route, options.effort),
          maxTokens: options.maxTokens,
          deadline: options.deadline,
          signal: attempt.signal,
          onText,
          onThinking,
        });
        reply = { route, modelId: r.model, provider: r.provider, stopReason: r.stopReason, cutOff: r.cutOff, cost: r.cost, costEstimated: false };
      }
      if (options.signal.aborted) return reply;
      if (stalled && next) {
        options.onSwitch?.(route, next, "it had not started after 20 seconds");
        continue;
      }
      if (!wrote && next && !reply.cutOff && reply.stopReason === "refusal") {
        options.onSwitch?.(route, next, "it declined the request");
        continue;
      }
      return reply;
    } catch (error) {
      if (wrote || !next || options.signal.aborted || Date.now() > options.deadline - 8_000) throw error;
      options.onSwitch?.(route, next, routeError(error));
    } finally {
      if (watchdog) clearTimeout(watchdog);
      options.signal.removeEventListener("abort", parent);
    }
  }
  throw new Error("Every model in the chain failed.");
}

/** One structured-output call through the first route that works. */
export async function structuredRouted(options: {
  routes: Route[];
  system: Anthropic.Beta.BetaTextBlockParam[];
  messages: { role: "user" | "assistant"; content: string }[];
  effort: Effort;
  schema: Record<string, unknown>;
  maxTokens: number;
  signal: AbortSignal;
  onSwitch?: (from: Route, to: Route, reason: string) => void;
}): Promise<{ route: Route; modelId: string; value: unknown; cost: number | null }> {
  const { routes } = options;
  if (!routes.length) throw new Error("No model is available: add ANTHROPIC_API_KEY or OPENROUTER_API_KEY in Netlify under Project configuration > Environment variables, then redeploy.");
  const started = Date.now();
  for (let i = 0; i < routes.length; i++) {
    const route = routes[i];
    const next = routes[i + 1];
    try {
      let out: { route: Route; modelId: string; value: unknown; cost: number | null };
      if (route.api === "claude") {
        const r = await structuredReply({
          system: options.system,
          messages: options.messages,
          brain: route.brain ?? "sonnet",
          model: route.model,
          effort: options.effort,
          schema: options.schema,
          maxTokens: options.maxTokens,
          signal: options.signal,
        });
        out = { route, modelId: r.model, value: r.value, cost: claudeCost(route, r.usage) };
      } else {
        const r = await structuredOpenRouter({
          model: route.model,
          system: options.system.map((b) => ({ text: b.text, cache: !!b.cache_control })),
          messages: options.messages,
          effort: routeEffort(route, options.effort),
          maxTokens: options.maxTokens,
          schema: options.schema,
          name: "routing_plan",
          signal: options.signal,
        });
        out = { route, modelId: r.model, value: r.value, cost: r.cost };
      }
      if (out.value === null && next && Date.now() - started < 30_000) {
        options.onSwitch?.(route, next, "it returned no usable plan");
        continue;
      }
      return out;
    } catch (error) {
      if (!next || options.signal.aborted || Date.now() - started > 30_000) throw error;
      options.onSwitch?.(route, next, routeError(error));
    }
  }
  throw new Error("Every model in the chain failed.");
}

export { EFFORTS };
