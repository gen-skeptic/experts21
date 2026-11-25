import { loadPassword } from "./storage";
import type { Catalog } from "./types";

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public passwordRequired = false,
  ) {
    super(message);
  }
}

function headers(json: boolean): Record<string, string> {
  const h: Record<string, string> = {};
  if (json) h["Content-Type"] = "application/json";
  const password = loadPassword();
  if (password) h["X-App-Password"] = password;
  return h;
}

async function readError(res: Response): Promise<ApiError> {
  let body: { message?: string; passwordRequired?: boolean } = {};
  try {
    body = await res.json();
  } catch {
    // not JSON
  }
  return new ApiError(res.status, body.message ?? `The server returned HTTP ${res.status}.`, !!body.passwordRequired);
}

export async function getCatalog(): Promise<Catalog> {
  const res = await fetch("/api/agents", { headers: headers(false) });
  if (!res.ok) throw await readError(res);
  return res.json();
}

export async function postJson<T>(path: string, body: unknown, signal?: AbortSignal): Promise<T> {
  const res = await fetch(`/api/${path}`, { method: "POST", headers: headers(true), body: JSON.stringify(body), signal });
  if (!res.ok) throw await readError(res);
  return res.json();
}

/** POST JSON and read the server-sent event stream. Throws on an "error" event or a non-stream response. */
export async function stream(
  path: string,
  body: unknown,
  onEvent: (event: string, data: Record<string, unknown>) => void,
  signal?: AbortSignal,
): Promise<void> {
  const res = await fetch(`/api/${path}`, { method: "POST", headers: headers(true), body: JSON.stringify(body), signal });
  if (!res.ok || !(res.headers.get("content-type") ?? "").includes("text/event-stream") || !res.body) throw await readError(res);
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    let end: number;
    while ((end = buffer.indexOf("\n\n")) >= 0) {
      const block = buffer.slice(0, end);
      buffer = buffer.slice(end + 2);
      let event = "message";
      let data = "";
      for (const line of block.split("\n")) {
        if (line.startsWith("event:")) event = line.slice(6).trim();
        else if (line.startsWith("data:")) data += line.slice(5).trim();
      }
      if (!data) continue;
      const parsed = JSON.parse(data) as Record<string, unknown>;
      if (event === "error") throw new ApiError(502, String(parsed.message ?? "The model call failed."));
      onEvent(event, parsed);
    }
  }
}
