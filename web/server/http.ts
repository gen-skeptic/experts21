import { createHash, timingSafeEqual } from "node:crypto";
import { env } from "./env.js";

export const SECURITY_HEADERS: Record<string, string> = {
  "Cache-Control": "no-store",
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "no-referrer",
};

export function json(status: number, body: unknown, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", ...SECURITY_HEADERS, ...headers },
  });
}

/** True when APP_PASSWORD is set in Netlify; then every model call needs the password in the X-App-Password header. */
export function passwordRequired(): boolean {
  return env("APP_PASSWORD") !== "";
}

export function passwordOk(req: Request): boolean {
  const expected = env("APP_PASSWORD");
  if (!expected) return true;
  const given = req.headers.get("x-app-password") ?? "";
  const a = createHash("sha256").update(given).digest();
  const b = createHash("sha256").update(expected).digest();
  return timingSafeEqual(a, b);
}

/** Checks shared by every model call: POST, same origin, the password, the API key, and a JSON body of sane size. */
export async function guard(req: Request): Promise<{ body: Record<string, unknown> } | { error: Response }> {
  if (req.method !== "POST") return { error: json(405, { message: "Use POST." }, { Allow: "POST" }) };
  const origin = req.headers.get("origin");
  if (origin && origin !== new URL(req.url).origin) return { error: json(403, { message: "Cross-site requests are not allowed." }) };
  if (!passwordOk(req)) return { error: json(401, { message: "This app needs its password.", passwordRequired: true }) };
  if (!env("ANTHROPIC_API_KEY")) {
    return { error: json(503, { message: "ANTHROPIC_API_KEY is not set. Add it in Netlify under Project configuration > Environment variables, then redeploy." }) };
  }
  const raw = await req.text();
  if (raw.length > 200_000) return { error: json(413, { message: "The request is too large." }) };
  try {
    const body = JSON.parse(raw);
    if (!body || typeof body !== "object" || Array.isArray(body)) throw new Error("not an object");
    return { body };
  } catch {
    return { error: json(400, { message: "The request body must be a JSON object." }) };
  }
}

// ---------------------------------------------------------------- server-sent events

export interface EventSink {
  send(event: string, data: Record<string, unknown>): void;
  close(): void;
  readonly closed: boolean;
}

/** A streamed text/event-stream response. `run` writes events; the stream closes when it returns. */
export function sse(run: (sink: EventSink) => Promise<void>, signal: AbortSignal): Response {
  const encoder = new TextEncoder();
  let closed = false;
  const stream = new ReadableStream<Uint8Array>({
    async start(controller) {
      const sink: EventSink = {
        send(event, data) {
          if (closed) return;
          try {
            controller.enqueue(encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`));
          } catch {
            closed = true;
          }
        },
        close() {
          if (closed) return;
          closed = true;
          try {
            controller.close();
          } catch {
            // already closed
          }
        },
        get closed() {
          return closed || signal.aborted;
        },
      };
      // A comment first, so proxies flush the headers and the browser sees the stream open.
      controller.enqueue(encoder.encode(`: ${" ".repeat(512)}\n\n`));
      try {
        await run(sink);
      } catch (error) {
        sink.send("error", { message: error instanceof Error ? error.message : "The request failed." });
      } finally {
        sink.close();
      }
    },
    cancel() {
      closed = true;
    },
  });
  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream; charset=utf-8", "X-Accel-Buffering": "no", ...SECURITY_HEADERS },
  });
}
