// Bundle the Netlify Functions with esbuild (as Netlify does) and route requests to them, for local runs and tests.
import { build } from "esbuild";
import { mkdirSync, readdirSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const web = resolve(dirname(fileURLToPath(import.meta.url)), "..");

export async function loadFunctions() {
  const src = join(web, "netlify", "functions");
  const out = join(web, ".test", "functions");
  mkdirSync(out, { recursive: true });
  const routes = [];
  for (const file of readdirSync(src).filter((f) => f.endsWith(".mts")).sort()) {
    const target = join(out, `${basename(file, ".mts")}-${Date.now()}.mjs`);
    await build({ entryPoints: [join(src, file)], outfile: target, bundle: true, platform: "node", format: "esm", target: "node22", packages: "external", logLevel: "silent" });
    const mod = await import(pathToFileURL(target).href);
    const paths = [].concat(mod.config?.path ?? `/.netlify/functions/${basename(file, ".mts")}`);
    const methods = [].concat(mod.config?.method ?? []);
    routes.push({ name: basename(file, ".mts"), paths, methods, handler: mod.default, config: mod.config ?? {} });
  }
  return routes;
}

export function findRoute(routes, url) {
  const path = new URL(url).pathname;
  return routes.find((r) => r.paths.includes(path)) ?? null;
}
