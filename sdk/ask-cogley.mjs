#!/usr/bin/env node
// Ask one expert agent a question with the Claude Agent SDK, from outside Claude.
//
//   node ask-cogley.mjs --check                      load the agent and its knowledge folder; no model call, no cost
//   node ask-cogley.mjs "Should we sign this MSA?"   ask the question (billed to ANTHROPIC_API_KEY)
//
// The agent is read from ../.claude/agents/<AGENT>.md (its instructions, tools, model, effort and skills) together
// with its knowledge folder ../knowledge/<AGENT>/, and runs as the main agent with read-only tools.
// To use a different expert, change AGENT below or set EXPERT_AGENT, for example EXPERT_AGENT=lean-six-sigma-lead.
import { query } from "@anthropic-ai/claude-agent-sdk";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, extname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const AGENT = process.env.EXPERT_AGENT ?? "business-attorney";

const here = dirname(fileURLToPath(import.meta.url));
const repo = resolve(here, "..");
const READ_ONLY_TOOLS = ["Read", "Grep", "Glob", "WebSearch", "WebFetch"];
const TEXT_TYPES = new Set([".md", ".txt", ".csv", ".json", ".yaml", ".yml"]);
const MAX_KNOWLEDGE_CHARS = 150_000;

function fail(message) {
  console.error(`ask: ${message}`);
  process.exit(1);
}

/** Parse the agent file: the small YAML frontmatter the build writes, and the instruction body. */
function loadAgent(name) {
  const file = join(repo, ".claude", "agents", `${name}.md`);
  if (!existsSync(file)) fail(`no agent file at ${relative(process.cwd(), file)}`);
  const text = readFileSync(file, "utf8");
  const match = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) fail(`${name}.md has no frontmatter`);
  const meta = {};
  let listKey = null;
  for (const line of match[1].split("\n")) {
    const item = line.match(/^\s+-\s+(.+)$/);
    if (item && listKey) {
      meta[listKey].push(item[1].trim());
      continue;
    }
    const pair = line.match(/^([A-Za-z-]+):\s*(.*)$/);
    if (!pair) continue;
    const [, key, raw] = pair;
    if (raw === "") {
      meta[key] = [];
      listKey = key;
    } else {
      listKey = null;
      meta[key] = raw.startsWith('"') ? JSON.parse(raw) : raw;
    }
  }
  for (const key of ["name", "description", "tools", "model"]) {
    if (!meta[key]) fail(`${name}.md frontmatter has no ${key}`);
  }
  const body = text.slice(match[0].length).trim();
  const persona = body.match(/Your name is \*\*(.+?)\*\*/)?.[1] ?? name;
  return {
    name: meta.name,
    persona,
    description: meta.description,
    tools: meta.tools.split(",").map((t) => t.trim()),
    model: meta.model,
    effort: meta.effort,
    skills: meta.skills ?? [],
    body,
  };
}

/** Every text document in knowledge/<name>/ (README first), skipping archive/ and anything over the size budget. */
function loadKnowledge(name) {
  const folder = join(repo, "knowledge", name);
  const docs = [];
  const skipped = [];
  if (!existsSync(folder)) return { folder, docs, skipped };
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
    const file = relative(repo, path);
    if (!TEXT_TYPES.has(extname(path).toLowerCase())) {
      skipped.push(`${file} (not a text file; the agent can still open it with Read)`);
      continue;
    }
    const text = readFileSync(path, "utf8");
    if (total + text.length > MAX_KNOWLEDGE_CHARS) {
      skipped.push(`${file} (over the size budget; the agent can still open it with Read)`);
      continue;
    }
    total += text.length;
    docs.push({ file, text });
  }
  return { folder, docs, skipped };
}

function systemPrompt(agent, knowledge) {
  const parts = [
    agent.body,
    "",
    "=== RUNNING FROM THE AGENT SDK ===",
    `You are answering one question from the command line (sdk/ask-cogley.mjs). Your working directory is the experts21 repository, so docs/ and knowledge/${agent.name}/ are readable with your tools. You have read-only tools: you can't write files or hand off to other agents. Where your instructions say to hand off or file a record, say what you would do instead.`,
    "",
    `=== YOUR KNOWLEDGE FOLDER: knowledge/${agent.name}/ (already read for you) ===`,
  ];
  for (const doc of knowledge.docs) parts.push("", `--- ${doc.file} ---`, doc.text);
  for (const file of knowledge.skipped) parts.push("", `(Also in the folder, not included above: ${file})`);
  return parts.join("\n");
}

function check(agent, knowledge) {
  const missingSkills = agent.skills.filter((s) => !existsSync(join(repo, ".claude", "skills", s, "SKILL.md")));
  console.log(`Agent:      ${agent.persona} (${agent.name})`);
  console.log(`Model:      ${agent.model}${agent.effort ? `, effort ${agent.effort}` : ""}`);
  console.log(`Tools here: ${agent.tools.filter((t) => READ_ONLY_TOOLS.includes(t)).join(", ")} (read-only)`);
  console.log(`Skills:     ${agent.skills.join(", ") || "none"}`);
  console.log(`Knowledge:  ${knowledge.docs.length} document(s) in ${relative(process.cwd(), knowledge.folder) || "."}`);
  for (const doc of knowledge.docs) console.log(`  - ${doc.file} (${doc.text.length.toLocaleString()} characters)`);
  for (const file of knowledge.skipped) console.log(`  - skipped: ${file}`);
  console.log(`Prompt:     ${systemPrompt(agent, knowledge).length.toLocaleString()} characters`);
  if (missingSkills.length) fail(`skills not found in .claude/skills/: ${missingSkills.join(", ")}`);
  if (!agent.body.includes("## How to answer")) fail("the agent body looks incomplete");
  console.log(`\nOK: ${agent.persona} loads correctly. No model was called and nothing was billed.`);
  console.log(`Ask a question with: node ask-cogley.mjs "your question"`);
}

async function ask(agent, knowledge, question) {
  if (!process.env.ANTHROPIC_API_KEY && !process.env.ANTHROPIC_AUTH_TOKEN && !process.env.ANTHROPIC_BASE_URL) {
    fail('set ANTHROPIC_API_KEY first (export ANTHROPIC_API_KEY="your-key"), or run --check to test without a key.');
  }
  const tools = agent.tools.filter((t) => READ_ONLY_TOOLS.includes(t));
  console.error(`Asking ${agent.persona} (${agent.name}, ${agent.model}${agent.effort ? ` / ${agent.effort}` : ""})...`);
  const conversation = query({
    prompt: question,
    options: {
      cwd: repo,
      agent: agent.name,
      agents: {
        [agent.name]: {
          description: agent.description,
          prompt: systemPrompt(agent, knowledge),
          tools,
          model: agent.model,
          ...(agent.effort ? { effort: agent.effort } : {}),
          skills: agent.skills,
        },
      },
      settingSources: ["project"],
      allowedTools: tools,
      disallowedTools: ["Write", "Edit", "NotebookEdit", "Bash", "Agent"],
      permissionMode: "dontAsk",
      maxTurns: 25,
    },
  });
  let result = null;
  for await (const message of conversation) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if (block.type === "tool_use") {
          const target = block.input?.file_path ?? block.input?.pattern ?? block.input?.query ?? block.input?.url ?? "";
          const shown = String(target).startsWith("/") ? relative(repo, String(target)) : String(target);
          console.error(`  ${block.name} ${shown}`);
        }
      }
    }
    if (message.type === "result") result = message;
  }
  if (!result) fail("no answer came back");
  if (result.subtype !== "success") fail(`the run ended with ${result.subtype}`);
  console.log(`\n${result.result}\n`);
  console.error(`(${result.num_turns} turn(s), $${(result.total_cost_usd ?? 0).toFixed(4)} billed to your API key)`);
}

const args = process.argv.slice(2);
const agent = loadAgent(AGENT);
const knowledge = loadKnowledge(AGENT);
if (args.includes("--check")) {
  check(agent, knowledge);
} else {
  const question = args.filter((a) => !a.startsWith("--")).join(" ").trim();
  if (!question) fail('ask a question: node ask-cogley.mjs "Should we sign the Example Law Group MSA as written?"');
  await ask(agent, knowledge, question);
}
