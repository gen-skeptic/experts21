// Environment variables: Netlify.env inside Netlify Functions, process.env in local development and tests.
declare const Netlify: { env: { get(name: string): string | undefined } } | undefined;

export function env(name: string): string {
  try {
    if (typeof Netlify !== "undefined") return Netlify.env.get(name) ?? "";
  } catch {
    // not running on Netlify
  }
  return process.env[name] ?? "";
}
