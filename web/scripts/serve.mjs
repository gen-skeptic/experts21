// Run the built app and the functions locally: http://127.0.0.1:8888 (npm run build first).
// Needs ANTHROPIC_API_KEY in the environment for real answers; APP_PASSWORD is optional.
import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, join, resolve, dirname } from "node:path";
import { Readable } from "node:stream";
import { fileURLToPath } from "node:url";
import { findRoute, loadFunctions } from "./functions.mjs";

const web = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const dist = join(web, "dist");
const port = Number(process.env.PORT ?? 8888);
const types = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".woff2": "font/woff2" };

if (!existsSync(join(dist, "index.html"))) {
  console.error("serve: dist/ is missing; run npm run build first.");
  process.exit(1);
}
const routes = await loadFunctions();

createServer(async (req, res) => {
  const url = `http://${req.headers.host}${req.url}`;
  const route = findRoute(routes, url);
  if (route) {
    const controller = new AbortController();
    res.on("close", () => controller.abort());
    const request = new Request(url, {
      method: req.method,
      headers: req.headers,
      body: req.method === "GET" || req.method === "HEAD" ? undefined : Readable.toWeb(req),
      duplex: "half",
      signal: controller.signal,
    });
    try {
      const response = await route.handler(request, {});
      res.writeHead(response.status, Object.fromEntries(response.headers));
      if (response.body) for await (const chunk of response.body) res.write(chunk);
      res.end();
    } catch (error) {
      res.writeHead(500, { "Content-Type": "text/plain" }).end(String(error));
    }
    return;
  }
  const path = join(dist, decodeURIComponent(new URL(url).pathname));
  const file = path.startsWith(dist) && existsSync(path) && statSync(path).isFile() ? path : join(dist, "index.html");
  res.writeHead(200, { "Content-Type": types[extname(file)] ?? "application/octet-stream" });
  createReadStream(file).pipe(res);
}).listen(port, "127.0.0.1", () => console.log(`serve: http://127.0.0.1:${port}/ (${routes.map((r) => r.paths.join(",")).join(" ")})`));
