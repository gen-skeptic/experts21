// Build step 1 of 3: package the expert team for the Netlify Functions.
//
// Reads the repository at build time: every .claude/agents/*.md (instructions, Star Trek name, voice, working style,
// brain and skills), the skills they preload (.claude/skills/<skill>/SKILL.md), each knowledge/<agent>/ folder, the
// docs/ research files each agent relies on, docs/expert-roster.md (one-line jobs) and docs/agent-brains.md (brains).
// Writes server/agents-data.generated.js, which only the functions import: the browser bundle never carries prompts,
// skills, knowledge or research.
import { execFileSync } from "node:child_process";
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { dirname, extname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const web = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repo = resolve(web, "..");
const out = join(web, "server", "agents-data.generated.js");

const TEXT_TYPES = new Set([".md", ".txt", ".csv", ".json", ".yaml", ".yml"]);
const MAX_FILE_CHARS = 40_000;
const MAX_KNOWLEDGE_CHARS = 80_000;
const MAX_DOCS_CHARS = 90_000;
const ORCHESTRATOR = "orchestrator";

const fail = (message) => {
  console.error(`build-agents: ${message}`);
  process.exit(1);
};
const read = (path) => readFileSync(path, "utf8");
const need = (text, re, what, file) => {
  const m = text.match(re);
  if (!m) fail(`${file}: could not find ${what}`);
  return m[1].trim();
};

function frontmatter(text, file) {
  const m = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!m) fail(`${file}: no frontmatter`);
  const meta = {};
  let list = null;
  for (const line of m[1].split("\n")) {
    const item = line.match(/^\s+-\s+(.+)$/);
    if (item && list) {
      meta[list].push(item[1].trim());
      continue;
    }
    const pair = line.match(/^([A-Za-z-]+):\s*(.*)$/);
    if (!pair) continue;
    if (pair[2] === "") {
      meta[pair[1]] = [];
      list = pair[1];
    } else {
      list = null;
      meta[pair[1]] = pair[2].startsWith('"') ? JSON.parse(pair[2]) : pair[2];
    }
  }
  return { meta, body: text.slice(m[0].length).trim() };
}

function clip(text, max, label) {
  return text.length > max ? `${text.slice(0, max)}\n\n[${label} truncated at ${max.toLocaleString()} characters]` : text;
}

// ---------------------------------------------------------------- roster: groups (in order) and one-line jobs
const roster = read(join(repo, "docs", "expert-roster.md"));
const groups = [];
const jobs = {};
const order = [];
let group = null;
for (const line of roster.split("\n")) {
  const heading = line.match(/^### (.+)$/);
  if (heading) group = heading[1].trim();
  if (line.startsWith("## Who reports")) break;
  const row = line.match(/^\| \d+ \| `([a-z0-9-]+)` \| [^|]+ \| [^|]+ \| ([^|]+) \|/);
  if (row && group) {
    if (!groups.includes(group)) groups.push(group);
    jobs[row[1]] = row[2].trim();
    order.push(row[1]);
  }
}
if (!groups.length) fail("docs/expert-roster.md: no roster tables found");

// ---------------------------------------------------------------- brains
const brains = {};
const brainTable = read(join(repo, "docs", "agent-brains.md")).split("## The brains")[1]?.split("\n## ")[0] ?? "";
for (const line of brainTable.split("\n")) {
  const m = line.match(/^\| \*\*(\w+)\*\* \| ([^|]+?) \(`(\w+)`\) \| ([^|]+?) \| ([^|]+?) \|/);
  if (m) brains[m[3]] = { label: m[1], family: m[2], strengths: m[4], cost: m[5] };
}
for (const alias of ["haiku", "sonnet", "opus"]) if (!brains[alias]) fail(`docs/agent-brains.md: no ${alias} brain`);

// ---------------------------------------------------------------- knowledge folders
function knowledgeFor(id) {
  const folder = join(repo, "knowledge", id);
  const docs = [];
  const skipped = [];
  if (!existsSync(folder)) return { docs, skipped };
  const files = [];
  const walk = (dir) => {
    for (const entry of readdirSync(dir).sort()) {
      const path = join(dir, entry);
      if (statSync(path).isDirectory()) {
        if (entry !== "archive" && !entry.startsWith(".")) walk(path);
      } else if (!entry.startsWith(".")) files.push(path);
    }
  };
  walk(folder);
  files.sort((a, b) => (a.endsWith("README.md") ? -1 : b.endsWith("README.md") ? 1 : a.localeCompare(b)));
  let total = 0;
  for (const path of files) {
    const file = relative(folder, path);
    if (!TEXT_TYPES.has(extname(path).toLowerCase())) {
      skipped.push(`${file} (not a text format the web app reads)`);
      continue;
    }
    const text = clip(read(path), MAX_FILE_CHARS, file);
    if (total + text.length > MAX_KNOWLEDGE_CHARS) {
      skipped.push(`${file} (over the size budget)`);
      continue;
    }
    total += text.length;
    docs.push({ file, text });
  }
  return { docs, skipped };
}

// ---------------------------------------------------------------- skills and research used by the agents
const skills = {};
const docs = {};
function skill(name) {
  if (!skills[name]) {
    const file = join(repo, ".claude", "skills", name, "SKILL.md");
    if (!existsSync(file)) fail(`missing skill ${name}`);
    const { body } = frontmatter(read(file), `.claude/skills/${name}/SKILL.md`);
    skills[name] = body.split("\n## Used by")[0].trim();
  }
  return name;
}
function doc(path) {
  if (!docs[path]) {
    const file = join(repo, path);
    if (!existsSync(file)) fail(`missing research file ${path}`);
    docs[path] = read(file).trim();
  }
  return path;
}

// ---------------------------------------------------------------- agents
const agents = {};
for (const fileName of readdirSync(join(repo, ".claude", "agents")).filter((f) => f.endsWith(".md")).sort()) {
  const file = `.claude/agents/${fileName}`;
  const { meta, body } = frontmatter(read(join(repo, file)), file);
  const id = meta.name;
  const persona = body.match(/Your name is \*\*(.+?)\*\*, after (.+?) from \*(.+?)\*\./);
  if (!persona) fail(`${file}: no persona line (run python3 tools/build.py)`);
  const docList = [...body.matchAll(/^ {3}- `(docs\/[^`]+)`/gm)].map((m) => m[1]);
  const research = [];
  let used = 0;
  for (const path of docList) {
    const text = docs[doc(path)];
    if (used + text.length > MAX_DOCS_CHARS) continue;
    used += text.length;
    research.push(path);
  }
  const { docs: knowledge, skipped } = knowledgeFor(id);
  agents[id] = {
    id,
    name: persona[1],
    fullName: persona[2],
    series: persona[3],
    title: need(body, /^# (.+)$/m, "title", file),
    group: need(body, /^\*DIO expert team\. (.+?)\. Reports to/m, "group", file),
    job: jobs[id] ?? "",
    voice: need(body, /^- \*\*Voice:\*\* (.+)$/m, "voice", file),
    style: need(body, /^- \*\*Working style:\*\* (.+)$/m, "working style", file),
    brain: meta.model,
    effort: meta.effort ?? "medium",
    why: need(body, /effort \*\*\w+\*\*\. Why: (.+)$/m, "brain reason", file),
    skills: (meta.skills ?? []).map(skill),
    docs: research,
    knowledge,
    knowledgeSkipped: skipped,
    prompt: body,
  };
  if (!brains[agents[id].brain]) fail(`${file}: unknown brain ${agents[id].brain}`);
  if (!groups.includes(agents[id].group)) fail(`${file}: group ${agents[id].group} is not in the roster`);
}
if (!agents[ORCHESTRATOR]) fail("the orchestrator agent is missing");

let source = "gen-skeptic/experts21";
try {
  source += `@${execFileSync("git", ["-C", repo, "rev-parse", "--short", "HEAD"], { encoding: "utf8" }).trim()}`;
} catch {
  // not a git checkout
}

for (const id of Object.keys(agents)) if (!order.includes(id)) fail(`${id} is not in docs/expert-roster.md`);
const data = { generated: new Date().toISOString(), source, orchestrator: ORCHESTRATOR, groups, order, brains, agents, skills, docs };
writeFileSync(out, `// Generated by scripts/build-agents.mjs. Do not edit; do not commit.\nexport const DATA = ${JSON.stringify(data)};\n`);

const sizes = Object.values(agents).map((a) => ({
  id: a.id,
  chars: a.prompt.length + a.skills.reduce((n, s) => n + skills[s].length, 0) + a.knowledge.reduce((n, d) => n + d.text.length, 0) + a.docs.reduce((n, d) => n + docs[d].length, 0),
}));
const largest = sizes.sort((a, b) => b.chars - a.chars)[0];
console.log(
  `build-agents: ${Object.keys(agents).length} agents, ${Object.keys(skills).length} skills, ${Object.keys(docs).length} research files from ${source}; ` +
    `largest prompt ${largest.id} at ${largest.chars.toLocaleString()} characters → ${relative(web, out)}`,
);
