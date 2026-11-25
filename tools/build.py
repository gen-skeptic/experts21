#!/usr/bin/env python3
"""Generate the expert team from the data in tools/.

    python3 tools/build.py           write every generated file
    python3 tools/build.py --check   fail if any generated file is missing, stale or edited by hand

Inputs:  tools/team.py (agents), tools/skills.py and tools/skills_*.py (skills), tools/workflows.py (team workflows),
         tools/brains.py (brains and task types), tools/models.py (the model catalog).
Outputs: .claude/agents/<agent>.md, .claude/skills/<skill>/SKILL.md, knowledge/README.md and knowledge/<agent>/README.md,
         docs/expert-roster.md, docs/agent-brains.md, docs/model-catalog.md and .json, and the generated team section
         of CLAUDE.md.
Documents you add to a knowledge folder are never touched.
"""
import json
import sys
from collections import Counter
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from brains import BRAIN_FACTS, BRAIN_ORDER, BRAINS, TASK_TYPES  # noqa: E402
from models import AGENT_TASK, CATALOG_DATE, MODELS, ROLES, SOURCES, TASK_MODELS, TIERS  # noqa: E402
from skills import CATEGORIES, SKILLS  # noqa: E402
from skills_marketing import MARKETING_RULES  # noqa: E402
from team import AGENTS, ORG_UNITS  # noqa: E402
from workflows import WORKFLOWS  # noqa: E402

BY_ID = {a["id"]: a for a in AGENTS}
GROUPS = []
for a in AGENTS:
    if a["group"] not in GROUPS:
        GROUPS.append(a["group"])
GROUP_ORDER = ["Leadership and coordination", "Team builder", "Advisors", "Quality", "Process improvement",
               "Sales, clients and partners", "AI and platform delivery", "Software team", "Marketing and social media",
               "Company operations, products and training", "Utility vertical (phase 2)"]
GROUPS.sort(key=GROUP_ORDER.index)
ALIAS_BRAIN = {b["alias"]: key for key, b in BRAINS.items()}
COLORS = {"Leadership and coordination": "blue", "Team builder": "purple", "Advisors": "purple", "Quality": "red",
          "Process improvement": "yellow", "Sales, clients and partners": "orange", "AI and platform delivery": "cyan",
          "Software team": "green", "Marketing and social media": "pink",
          "Company operations, products and training": "yellow", "Utility vertical (phase 2)": "green"}
SERIES = {"TOS": "Star Trek: The Original Series", "TNG": "Star Trek: The Next Generation", "DS9": "Star Trek: Deep Space Nine",
          "VOY": "Star Trek: Voyager", "ENT": "Star Trek: Enterprise", "DIS": "Star Trek: Discovery",
          "SNW": "Star Trek: Strange New Worlds"}

DOC_TITLES = {
    "docs/README.md": "Research index",
    "docs/01-executive-summary.md": "Executive summary and current state",
    "docs/02-market.md": "Market",
    "docs/03-target-customers.md": "Target customers",
    "docs/04-competitors.md": "Competitors",
    "docs/05-services-and-pricing.md": "Services and pricing",
    "docs/06-startup-and-operating-costs.md": "Startup and operating costs",
    "docs/07-permits-and-licenses.md": "Permits and licenses",
    "docs/08-staffing.md": "Staffing",
    "docs/09-marketing.md": "Marketing and go-to-market",
    "docs/10-operations-and-delivery.md": "Operations and delivery",
    "docs/11-risks.md": "Biggest risks",
    "docs/12-90-day-plan-and-open-questions.md": "90-day plan and open questions",
    "docs/local-prospects.md": "Local prospects",
    "docs/expert-roster.md": "Expert roster",
    "docs/agent-brains.md": "Agent brains and personalities",
    "docs/model-catalog.md": "Model catalog: the most cost-efficient model per task type",
}
GROUP_DOCS = {
    "Leadership and coordination": ["01", "05", "06", "11", "12"],
    "Team builder": ["expert-roster", "agent-brains"],
    "Advisors": ["07", "06", "11"],
    "Quality": ["05", "10", "07"],
    "Process improvement": ["05", "10", "03"],
    "Sales, clients and partners": ["03", "05", "09", "04", "local-prospects"],
    "AI and platform delivery": ["05", "10", "07", "11"],
    "Software team": ["05", "10", "07"],
    "Marketing and social media": ["09", "03", "04", "05"],
    "Company operations, products and training": ["05", "06", "08"],
    "Utility vertical (phase 2)": ["05", "11", "01"],
}
AGENT_DOCS = {
    "business-attorney": ["07", "05", "10", "11"],
    "cpa-bookkeeper": ["06", "07", "08"],
    "insurance-risk-advisor": ["11", "07", "06"],
    "talent-people-partner": ["08", "07"],
    "operations-coordinator": ["07", "06", "10"],
    "market-research-analyst": ["02", "03", "04", "local-prospects"],
    "operations-finance-manager": ["06", "05", "08", "11", "model-catalog"],
    "trainer-curriculum": ["05", "09", "03"],
    "product-manager": ["05", "03", "04", "06"],
    "orchestrator": ["01", "05", "06", "11", "12", "expert-roster", "agent-brains", "model-catalog"],
    "chief-of-staff": ["01", "05", "06", "11", "12", "model-catalog"],
    "cto-principal-architect": ["01", "05", "06", "11", "12", "model-catalog"],
    "ai-solutions-engineer": ["05", "10", "07", "11", "model-catalog"],
}


def doc_path(key):
    for path in DOC_TITLES:
        name = path.split("/")[-1]
        if name.startswith(key + "-") or name == key + ".md":
            return path
    raise KeyError(key)


def docs_for(agent):
    return [doc_path(k) for k in AGENT_DOCS.get(agent["id"], GROUP_DOCS[agent["group"]])]


def first_line(s):
    return s.strip().split("\n")[0]


def label(agent):
    return f"{agent['name']} (`{agent['id']}`)" if PERSONAS else f"`{agent['id']}`"


def reports(agent_id):
    return [a for a in AGENTS if a["reports_to"] == agent_id]


def manager_text(agent):
    if agent["reports_to"] == "erich":
        return "Erich (Chairman), the owner"
    boss = BY_ID[agent["reports_to"]]
    return f"{label(boss)}, {boss['title']}"


# ---------------------------------------------------------------- shared text

FIRM = """## The firm

You work for **Dautel Intelligent Operations (DIO)**, an AI consulting and deployment firm in Boynton Beach, Palm Beach County, Florida, founded and owned by J. Erich Dautel, its **Chairman**. Positioning: **"Fix first, then automate."** DIO maps, measures and fixes how work gets done with Lean Six Sigma, then connects AI agents and software to real business systems with clear ownership, least-privilege access, human review, verification and a tested recovery path.

- **Service lines:** (A) AI Operations Readiness Assessment; (B) Governed Agent Workflows and MCP integrations; (C) Company Memory and Private AI Platform; (D) Managed Agent Operations; (E) Utility and Field-Operations Intelligence (phase 2, gated by the employer boundary); (F) Training, workshops and coaching; (G) Custom Software Solutions; (H) Lean Six Sigma Process Improvement. Productized offers: Agent Safety Audit, MCP Integration Sprint, Company Memory Starter, GitOps Platform Launch, Agent Workflow Coaching.
- **Customers:** owner-operated firms with 10–100 staff in South Florida and across the US (law, medical and dental, CPA and wealth, property and community association management, insurance, title), plus small software teams and MSPs.
- **Situation:** Erich runs the firm as a side practice while employed full time and finishing an MBA, so his hours are scarce. Protect them.
- **Source of truth:** the research in `docs/` (start with `docs/README.md`) for prices, plans, costs, permits and the market. If it doesn't answer the question, say so and research it.

You are one of the expert agents in this repository (`.claude/agents/`), led by `orchestrator`. The roster is `docs/expert-roster.md`."""

RULES = """## Rules (apply to everything you produce)

1. **Evidence over claims.** No fake metrics, invented clients or testimonials. Cite sources with dates and label estimates *(est.)*.
2. **Fix first, then automate.** Never design automation or software around an unmeasured or broken process; when in doubt, ask for a `process-health-check`.
3. **Reviewed, verifiable, recoverable.** Every change has an owner, a review, a way to verify it and a way to roll it back.
4. **Least privilege and client ownership.** Clients own their code, accounts and data. Client confidential data stays in client systems. Never ask for more access than the task needs.
5. **Privacy lock.** Never publish a street address, personal phone, personal email, home location, family content or secrets. Never put credentials in files, commits or messages. This repository is public.
6. **Employer boundary.** While Erich is employed at FPL/NextEra: no utility clients, no vegetation-management or line-clearance contractors, no company known to be an FPL/NextEra vendor, no competing work, and never employer time, equipment, data or confidential information. Flag anything near it for Erich and decline when unsure (`employer-boundary-screen`).
7. **Decision rights.** Erich (Chairman) approves final deployments to customers and every financial transaction, and decides anything with financial or ethical considerations. You advise and recommend with options; you never commit money, sign or deploy on his behalf.
8. **Voice and brand.** Company copy says "we"; plain, confident and specific; sentence case; no emoji; no hype. Visual work follows the Dautel Design System in `design-system/` (the `dautel-brand` skill).
9. **Stop the line.** You may stop work that is unsafe, insecure or wrong. Say so plainly and tell the orchestrator."""

ANSWER = """## How to answer

- **Lead with the answer** or recommendation, then the reasons, then risks and next steps.
- **Answer from your role.** If part of the question belongs to another expert, name that expert and why instead of guessing.
- **Use the right skill:** follow the method of the preloaded skill that fits the task, and use its output format.
- **Show your sources:** end with **Sources used:** the {sources} you relied on, with dates.
- **Be honest about limits:** label estimates, say what you couldn't verify, and list the decisions only Erich can make.
- **When the orchestrator gives you an assignment,** answer your part only; it combines the answers.
- Be as brief as the question allows."""

HANDOFF = """## Release handoff

Builders build and test; **`platform-devops-engineer` deploys.** Nobody else deploys to a client's production. A release is ready for handoff only with the package in the `release-and-deployment` skill: reviewed and merged source with CI green, an immutable build artifact, the deployment spec, configuration and secrets **by name only**, health checks and metrics, backward-compatible migrations with a tested rollback, release notes, a runbook draft and test results (agent releases: evaluation results). Erich approves every production deployment."""

ORCHESTRATION = """## Orchestrating the team

You can call the other experts with the **Agent** tool: set `subagent_type` to the expert's name (for example `business-attorney`). Each one starts fresh and sees only the prompt you give it, its own instructions, its preloaded skills and the project files.

1. **Plan** (`routing-plan`): restate the question, list the angles it needs, pick the fewest experts that cover them (usually 2 to 5), and write each one's exact question. For a simple question that one expert can answer, use that one expert.
2. **Launch in parallel:** put every Agent call whose inputs are ready **in the same message**, so they run at the same time. Only wait when one expert needs another's output (then run that one next, with the earlier answer in its prompt).
3. **Give each expert a complete assignment:** the original question, its part, the documents or earlier answers it needs, what a good answer must contain, and "answer your part only; the orchestrator combines the answers".
4. **Choose the brain and model** (`model-selection`): name the task type of each assignment. Each expert has a default `model` and `effort`; pass `model` on the Agent call only when the task type calls for a different brain (`docs/agent-brains.md`). Where any model can run (the web app, or a client recommendation), use the most cost-efficient model for the task type from `docs/model-catalog.md`, and keep client confidential data on the Claude API or zero-data-retention routes.
5. **Review before it leaves:** send proposals, prices, contracts, public content and code to `quality-reviewer` (and the specialist reviewer for its area) before you present them as final.
6. **Combine** everything into one answer:
   - **Answer:** the recommendation in one or two sentences.
   - **What the experts said:** the key points, credited to each expert by name.
   - **Where they disagree,** and how you would settle it.
   - **Risks** and how to reduce them.
   - **Next steps,** each with an owner and a date.
   - **For Erich:** the decisions only he can make (money, ethics, final deployments), with options and your recommendation.
   - **Experts and sources used.**
7. **If the Agent tool isn't available** (some runtimes, including some cloud sessions, don't let a subagent call other subagents): don't write the specialists' answers yourself. Return only a plan headed **ROUTING PLAN FOR THE MAIN SESSION**: one numbered line per expert with its `name` and its exact, self-contained question (include the facts and documents it needs), then the line "Run these experts in parallel and send me their answers to combine." When the answers come back, combine them as in step 6.
8. Don't do a specialist's work yourself when an expert exists, and never skip a review or one of Erich's approvals."""


# ---------------------------------------------------------------- agents

def frontmatter(agent, personas):
    lines = ["---", f"name: {agent['id']}", f"description: {json.dumps(agent['description'], ensure_ascii=False)}"]
    tools = agent["tools"]
    if agent["id"] == "orchestrator":
        tools += ", Agent"
    lines.append(f"tools: {tools}")
    if personas:
        lines += [f"model: {agent['model']}", f"effort: {agent['effort']}"]
    lines.append("skills:")
    lines += [f"  - {s}" for s in agent["skills"]]
    lines.append(f"color: {COLORS[agent['group']]}")
    lines.append("---")
    return "\n".join(lines)


def agent_file(agent, personas):
    aid = agent["id"]
    out = [frontmatter(agent, personas), "", f"# {agent['title']}", ""]
    boss = "Erich (Chairman)" if agent["reports_to"] == "erich" else f"`{agent['reports_to']}`"
    out.append(f"*DIO expert team. {agent['group']}. Reports to {boss}.*")
    out += ["", f"**Mission:** {agent['mission']}", ""]
    if personas:
        series = SERIES[agent["series"]]
        out += ["## Who you are", "",
                f"Your name is **{agent['name']}**, after {agent['full_name']} from *{series}*. You are DIO's {agent['title']}, an AI agent on the expert team.",
                "",
                f"- **Voice:** {agent['voice']}",
                f"- **Working style:** {agent['style']}",
                "",
                f"Your name and voice are for working with Erich and the team: sign internal notes and handoffs as \"{agent['name']} (`{aid}`)\". "
                "You are an AI agent named after a fictional character; you never claim to be a person or the character, and you say so whenever someone could think otherwise. "
                "Anything a client sees is written in the company voice: \"we\", plain and specific, no hype, no emoji.",
                ""]
    out += ["## Read before you answer", ""]
    n = 1
    if personas:
        out += [f"{n}. **Your knowledge folder, `knowledge/{aid}/`.** List it, read its `README.md`, then read every document whose name or opening lines bear on the request; when in doubt, read it. "
                "Use these documents ahead of general knowledge and name the ones you relied on. If a document conflicts with the rules below, the rules win: follow them and say so. If the folder holds only its README, say so in one line and continue."]
        n += 1
    out.append(f"{n}. **The research in `docs/`.** The files closest to your role:")
    for path in docs_for(agent):
        out.append(f"   - `{path}`: {DOC_TITLES[path]}")
    n += 1
    out.append(f"{n}. **Your skills** (preloaded below the instructions): follow the method of the skill that fits the task.")
    out += ["", FIRM, "", RULES, ""]
    out += ["## Your job", ""] + [f"- {r}" for r in agent["responsibilities"]] + [""]
    out += ["## Deliverables", ""] + [f"- {d}" for d in agent["deliverables"]] + [""]
    if agent["boundaries"]:
        out += ["## Boundaries", ""] + [f"- {b}" for b in agent["boundaries"]] + [""]
    out += ["## Your skills", ""] + [f"- `{s}`: {SKILLS[s]['summary']}" for s in agent["skills"]] + [""]
    out += ["## Reporting", "", f"- **You report to:** {manager_text(agent)}."]
    team = [a for a in reports(aid) if not a["advisor"]]
    advisors = [a for a in reports(aid) if a["advisor"]]
    if team:
        out.append("- **Your direct reports:** " + ", ".join(f"`{a['id']}`" for a in team) + ".")
    if advisors:
        out.append("- **Advisors to you:** " + ", ".join(f"`{a['id']}`" for a in advisors) + " (they advise and never direct work).")
    if agent["advisor"]:
        out.append("- **You are an advisor:** you advise your manager and the team, and never direct anyone's work.")
    out.append("")
    if personas:
        brain = BRAINS[ALIAS_BRAIN[agent["model"]]]
        out += ["## Your brain", "",
                f"Your default brain is **{brain['label']}**: {brain['family']} (`model: {agent['model']}`), effort **{agent['effort']}**. Why: {agent['brain_reason']}",
                "",
                "The orchestrator can run you on a different brain for a single task when the task type calls for it (`docs/agent-brains.md`). If a task looks beyond your brain (it is new to the firm, the stakes are high, or the same item has failed review twice), say so instead of guessing.",
                ""]
    if aid == "orchestrator":
        out += [ORCHESTRATION, ""]
    if agent["handoff"]:
        out += [HANDOFF, ""]
    if agent["marketing"]:
        out += [MARKETING_RULES.replace("## Rules for everything published", "## Marketing rules").strip(), ""]
    out.append(ANSWER.format(sources="knowledge-folder documents, `docs/` files and web sources" if personas else "`docs/` files and web sources"))
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- skills

KIND = {"work": "Work", "qa": "QA review", "decision": "Decision", "gate": "**Approval: Erich**", "human": "Erich does it"}


def who_text(names):
    return ", ".join("Erich (Chairman)" if n == "erich" else f"`{n}`" for n in names)


def skill_file(name, skill):
    users = [a for a in AGENTS if name in a["skills"]]
    out = ["---", f"name: {name}", f"description: {json.dumps(skill['description'], ensure_ascii=False)}", "---", "",
           f"# {skill['title']}", "", f"*{skill['category']} skill for the DIO expert team.* {skill['summary']}", "",
           skill["body"].strip(), ""]
    wf = WORKFLOWS.get(name)
    if wf:
        out += ["## Team workflow", "",
                f"How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, {wf['source']}). "
                "Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.",
                "",
                f"- **Owner:** {who_text([wf['owner']])}",
                f"- **Starts when:** {wf['trigger']}",
                f"- **Done when:** {wf['done']}",
                "",
                "| # | Step | Who | What | Output |",
                "| -: | --- | --- | --- | --- |"]
        for i, step in enumerate(wf["steps"], 1):
            what = step["does"].replace("|", "/")
            outp = step["out"].replace("|", "/")
            out.append(f"| {i} | {KIND[step['kind']]} | {who_text(step['who'])} | {what} | {outp} |")
        out.append("")
    if name == "model-selection":
        out += model_tables(skill=True)
    out += ["## Used by", "", ", ".join(f"`{a['id']}`" for a in users) + ".", ""]
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- docs

def expert_roster(personas):
    n_agents = len(AGENTS)
    out = ["# Expert roster", "",
           f"*Generated from `tools/team.py` and `tools/skills.py` by `tools/build.py`. {n_agents} agents and {len(SKILLS)} skills.*", "",
           "The experts a consultant would want around the table to plan, open and run **Dautel Intelligent Operations**, an AI consulting and deployment firm in Boynton Beach, Florida. "
           "They come from the research in [`docs/`](README.md) and from the team plan in the DIO operating manual (gen-skeptic/experts), which already defined 49 of these roles. "
           "Each role is built as an agent in [`.claude/agents/`](../.claude/agents/) and each skill as a reusable method in [`.claude/skills/`](../.claude/skills/), written once and shared by every agent that needs it.", "",
           "Two agents run the team itself: **`orchestrator`** takes any question, brings in the right experts and returns one combined answer; **`agent-builder`** creates new agents and skills and improves existing ones.", ""]
    if personas:
        out += ["Every agent's Star Trek name, voice, working style and brain are in [agent-brains.md](agent-brains.md).", ""]
    out += ["## The experts", ""]
    num = 0
    for group in GROUPS:
        members = [a for a in AGENTS if a["group"] == group]
        out += [f"### {group}", ""]
        if personas:
            out += ["| # | Agent | Name | Role | Job (one line) | Skills |", "| -: | --- | --- | --- | --- | --- |"]
        else:
            out += ["| # | Agent | Role | Job (one line) | Skills |", "| -: | --- | --- | --- | --- |"]
        for a in members:
            num += 1
            skills = ", ".join(f"`{s}`" for s in a["skills"])
            if personas:
                out.append(f"| {num} | `{a['id']}` | {a['name']} | {a['title']} | {a['job']} | {skills} |")
            else:
                out.append(f"| {num} | `{a['id']}` | {a['title']} | {a['job']} | {skills} |")
        out.append("")
    out += ["## Who reports to whom", "",
            "Erich (Chairman) owns the firm and decides what only the owner should: financial transactions, final deployments to customers and anything with financial or ethical considerations. "
            "`orchestrator` runs everything else as the CEO agent. Advisors advise and never direct work.", "",
            "| Unit | Head (reports to `orchestrator`) | Team |", "| --- | --- | --- |",
            "| Board | Erich (Chairman), advised by `advisory-board` | `orchestrator` |"]
    for head, unit in ORG_UNITS.items():
        team = [a for a in reports(head)]
        def tree(aid):
            subs = reports(aid)
            if not subs:
                return f"`{aid}`"
            return f"`{aid}` (leads " + ", ".join(tree(s["id"]) for s in subs) + ")"
        team_text = ", ".join(tree(a["id"]) for a in team) or "—"
        out.append(f"| {unit} | `{head}` | {team_text} |")
    out.append("| Team builder | `agent-builder` | — |")
    out.append("")
    out += ["## Shared skills", "",
            "A skill is a reusable method (\"review a contract\", \"build a break-even model\"). One skill is shared by every agent that uses it, so it is written once.", ""]
    for cat in CATEGORIES:
        names = [n for n, s in SKILLS.items() if s["category"] == cat]
        out += [f"### {cat}", "", "| Skill | What it's for | Used by |", "| --- | --- | --- |"]
        for n in names:
            users = ", ".join(f"`{a['id']}`" for a in AGENTS if n in a["skills"])
            out.append(f"| `{n}` | {SKILLS[n]['summary']} | {users} |")
        out.append("")
    counts = Counter(len([a for a in AGENTS if n in a["skills"]]) for n in SKILLS)
    most = sorted(SKILLS, key=lambda n: -len([a for a in AGENTS if n in a["skills"]]))[:5]
    out += ["## Coverage", "",
            f"- {n_agents} agents in {len(GROUPS)} groups; {len(SKILLS)} skills in {len(CATEGORIES)} categories.",
            f"- Most shared: " + ", ".join(f"`{n}` ({len([a for a in AGENTS if n in a['skills']])} agents)" for n in most) + ".",
            f"- Every skill is used by at least one agent, and every agent uses between {min(len(a['skills']) for a in AGENTS)} and {max(len(a['skills']) for a in AGENTS)} skills.",
            ""]
    return "\n".join(out).rstrip() + "\n"


def agent_brains():
    by_model = Counter(a["model"] for a in AGENTS)
    out = ["# Agent brains and personalities", "",
           "*Generated from `tools/team.py` and `tools/brains.py` by `tools/build.py`.*", "",
           "Every agent has a **brain** (the model it runs on and how hard it thinks), a **personality** (a Star Trek name, a voice and a working style) and a **knowledge folder** (`knowledge/<agent>/`) it reads before it answers.", "",
           "## The brains", "",
           "| Brain | Model (`model:` alias) | Strengths | Price per million tokens (input / output) | Speed | Agents |",
           "| --- | --- | --- | --- | --- | -: |"]
    for key in BRAIN_ORDER:
        b = BRAINS[key]
        out.append(f"| **{b['label']}** | {b['family']} (`{b['alias']}`) | {b['strengths']} | {b['cost']} | {b['speed']} | {by_model.get(b['alias'], 0)} |")
    out += ["", BRAIN_FACTS, "",
            "**How the defaults were chosen:** **Opus** (Deep) for judgment where a mistake is expensive: strategy, legal, finance, risk, architecture, security, statistics and the QA gate. "
            "**Sonnet** (Standard) for most specialist work: building, research, writing, planning and coordination. **Haiku** (Fast) for fast, simple, high-volume work: scheduling and admin, short-form posts, clips and community replies. "
            "Frontier (`fable`) is never a default; only the orchestrator assigns it, task by task.", "",
            f"**Totals:** {by_model.get('opus', 0)} agents on Opus, {by_model.get('sonnet', 0)} on Sonnet, {by_model.get('haiku', 0)} on Haiku.", "",
            "## When to use each brain", "", "| Brain | Use for | Avoid |", "| --- | --- | --- |"]
    for key in BRAIN_ORDER:
        b = BRAINS[key]
        out.append(f"| **{b['label']}** | {b['use']} | {b['avoid']} |")
    out += ["", "## Brain by type of work", "",
            "The orchestrator picks the brain for each assignment from this table: start from the task type, raise one level (effort first, then brain) for money, security, legal terms, client-final work or after a failed review, and lower one level for routine work that a review will catch.", "",
            "| Task type | Examples | Brain | Effort | Why |", "| --- | --- | --- | --- | --- |"]
    for name, ex, brain, effort, why in TASK_TYPES:
        out.append(f"| {name} | {ex} | {BRAINS[brain]['label']} (`{BRAINS[brain]['alias']}`) | {effort} | {why} |")
    out += ["", "Where any model can run (the web app, or a model recommendation for a client), the most cost-efficient model for each task type, across Claude and OpenRouter, is in [model-catalog.md](model-catalog.md).",
            "", "## Every agent", "",
            "| Name | Star Trek character | Agent | Role | Brain | Effort | Why this brain | Voice | Working style |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for group in GROUPS:
        for a in [x for x in AGENTS if x["group"] == group]:
            b = BRAINS[ALIAS_BRAIN[a["model"]]]
            out.append(f"| **{a['name']}** | {a['full_name']} ({a['series']}) | `{a['id']}` | {a['title']} | {b['label']} (`{a['model']}`) | {a['effort']} | {a['brain_reason']} | {a['voice']} | {a['style']} |")
    out += ["", "Series: " + "; ".join(f"{k} = *{v}*" for k, v in SERIES.items()) + ". "
            "The agents are AI agents named after fictional characters. They never claim to be people or the characters, and anything a client sees is written in the company voice.", ""]
    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- model catalog

TASK_INFO = {name: dict(examples=ex, brain=brain, effort=effort, why=why) for name, ex, brain, effort, why in TASK_TYPES}


def task_cost(key):
    m = MODELS[key]
    return m["gpqa_cost"] + m["tau_cost"]


def money(x):
    return f"${x:.3f}" if x < 0.1 else f"${x:.2f}"


def price(m):
    return f"${m['input']:g} / ${m['output']:g}"


def model_tables(skill=False):
    out = [f"## The catalog ({CATALOG_DATE})" if skill else "## Model by type of work", ""]
    if skill:
        out += ["Generated from `tools/models.py`. Cost is the average cost of one GPQA Diamond task plus one tau2-Bench task on OpenRouter's benchmarks: a like-for-like comparison, not a quote. Full details and sources: `docs/model-catalog.md`.", ""]
    out += ["| Task type | Tier | Primary model (OpenRouter ID) | Cost | Fallback | Effort | Claude Code brain |",
            "| --- | --- | --- | -: | --- | --- | --- |"]
    for task, tier, primary, fallback, effort, why in TASK_MODELS:
        b = BRAINS[TASK_INFO[task]["brain"]]
        pm, fm = MODELS[primary], MODELS[fallback]
        out.append(f"| {task} | {TIERS[tier]['label']} | {pm['name']} (`{pm['openrouter']}`) | {money(task_cost(primary))} | {fm['name']} | {effort} | {b['label']} (`{b['alias']}`) |")
    r = ROLES["routing"]
    out += ["", f"The orchestrator's own routing plan runs on {MODELS[r[0]]['name']} (fallback {MODELS[r[1]]['name']}) at {r[2]} effort; its combined answer uses the \"{ROLES['synthesis'][0]}\" row.", ""]
    if skill:
        out += ["| Model | OpenRouter ID | Claude API ID | Price per M tokens (in / out) | GPQA | tau2 | Cost |",
                "| --- | --- | --- | --- | -: | -: | -: |"]
        for key, m in MODELS.items():
            api = f"`{m['anthropic']}`" if m["anthropic"] else "n/a"
            out.append(f"| {m['name']} | `{m['openrouter']}` | {api} | {price(m)} | {m['gpqa']:.3f} | {m['tau']:.3f} | {money(task_cost(key))} |")
        out.append("")
    return out


def model_catalog_md():
    out = ["# Model catalog", "",
           f"*Generated from `tools/models.py` by `tools/build.py`. Chosen on {CATALOG_DATE} from OpenRouter's live model list and benchmark data. Prices and scores change monthly: refresh every quarter (`python3 tools/refresh_models.py`).*", "",
           "The most cost-efficient model for each type of work, across Claude and every model on OpenRouter. The web app uses it when **Auto** is chosen; the orchestrator uses it, through the `model-selection` skill, to name a model for each assignment; and the team uses the same method when it recommends models to clients.", "",
           "## How the models were chosen", "",
           "1. **Two independent benchmarks** from OpenRouter, run on every model with the same harness: **GPQA Diamond** (198 graduate-level science questions: careful reasoning) and **tau2-Bench Airline** (multi-turn customer-service tasks with tools and a policy: following rules while using tools). Each gives an accuracy and an average cost and time per task.",
           "2. **A quality floor per tier**, below. A model qualifies if it meets both floors, supports structured outputs (the routing plan needs them) and answers a GPQA task in 120 seconds or less (the web app stops an answer at about 50 seconds, so slow models fall back).",
           "3. **The primary is the qualifying model with the lowest cost per task** (one GPQA task plus one tau2 task). The fallback is the next-best qualifying model from a different provider.",
           "4. **Privacy and routing rules** apply on top: see the last section.", "",
           "| Tier | GPQA floor | tau2 floor | For |", "| --- | -: | -: | --- |"]
    for key, tier in TIERS.items():
        out.append(f"| **{tier['label']}** | {tier['gpqa']:.3f} | {tier['tau']:.2f} | {tier['why']} |")
    out += [""] + model_tables()
    out += ["| Task type | Examples | Why this model |", "| --- | --- | --- |"]
    for task, tier, primary, fallback, effort, why in TASK_MODELS:
        out.append(f"| {task} | {TASK_INFO[task]['examples']} | {why} |")
    out += ["", "**Escalate one tier** (Standard to Deep, Deep to Frontier) when the work involves money, production, security or legal terms and is client-final, is new to the firm, or failed a review. **Step down one tier** for routine work a review step will catch. Frontier is the orchestrator's call alone.", "",
            "**Claude Code** subagents run on Claude only and keep the brains in [agent-brains.md](agent-brains.md). On these two benchmarks Claude Sonnet 5.5 scored higher than Claude Opus 5.5 at half the price, so moving the Deep agents from Opus to Sonnet in Claude Code would cut their cost about in half; that change is Erich's decision and has not been made.", "",
            "## The models", "",
            "| Model | Maker | OpenRouter ID | Claude API ID | Price per M tokens (in / out) | Context | GPQA | tau2 | Cost per task pair | Seconds per GPQA task | Reasoning efforts | Note |",
            "| --- | --- | --- | --- | --- | -: | -: | -: | -: | -: | --- | --- |"]
    for key, m in sorted(MODELS.items(), key=lambda kv: task_cost(kv[0])):
        api = f"`{m['anthropic']}`" if m["anthropic"] else "n/a"
        ctx = f"{m['context'] // 1000:,}K"
        out.append(f"| **{m['name']}** | {m['maker']} | `{m['openrouter']}` | {api} | {price(m)} | {ctx} | {m['gpqa']:.3f} | {m['tau']:.3f} | {money(task_cost(key))} | {m['gpqa_s']} | {', '.join(m['efforts'])} | {m['note']} |")
    out += ["", "Claude models run on the Claude API directly when `ANTHROPIC_API_KEY` is set (same price; prompt caching and Anthropic's refusal fallback), otherwise through OpenRouter.", "",
            "## The API calls", "",
            "OpenRouter speaks the OpenAI Chat Completions format at one endpoint for every model; the model ID picks the model. Keys stay in environment variables (`OPENROUTER_API_KEY`), never in code or this repository.", "",
            "```bash",
            "curl https://openrouter.ai/api/v1/chat/completions \\",
            "  -H \"Authorization: Bearer $OPENROUTER_API_KEY\" \\",
            "  -H \"Content-Type: application/json\" \\",
            "  -d '{",
            f"    \"models\": [\"{MODELS['deepseek-v4.1-flash']['openrouter']}\", \"{MODELS['claude-haiku-5.5']['openrouter']}\"],",
            "    \"messages\": [{\"role\": \"system\", \"content\": \"You are ...\"}, {\"role\": \"user\", \"content\": \"...\"}],",
            "    \"reasoning\": {\"effort\": \"low\"},",
            "    \"provider\": {\"zdr\": true, \"data_collection\": \"deny\", \"require_parameters\": true},",
            "    \"max_tokens\": 4000,",
            "    \"stream\": true",
            "  }'",
            "```", "",
            "| Field | What it does |", "| --- | --- |",
            "| `model` or `models` | One model ID, or a list: OpenRouter tries them in order if one is down, rate-limited or refuses |",
            "| `reasoning.effort` | How hard the model thinks; use only the efforts the model supports (table above) |",
            "| `provider.zdr: true` | Only endpoints with zero data retention; use for anything a client would call confidential |",
            "| `provider.data_collection: \"deny\"` | Never an endpoint that may train on or store prompts |",
            "| `provider.require_parameters: true` | Only endpoints that support every parameter sent (for example structured outputs) |",
            "| `response_format: {\"type\": \"json_schema\", ...}` | Structured output that matches a JSON schema (the routing plan) |",
            "| `usage.cost` in the response | What the call cost, in USD |", "",
            "The Claude API call for the same work is `POST https://api.anthropic.com/v1/messages` with `model` set to the Claude API ID above and `output_config.effort` for effort. The web app's code is in `web/server/openrouter.ts` and `web/server/claude.ts`.", "",
            "## Privacy and routing rules", "",
            "- **Client confidential data** goes only to the Claude API directly or to OpenRouter with zero data retention enforced. The web app enforces it by default (`OPENROUTER_ZDR`, on unless set to `false`).",
            "- **Regulated data** (patient records, privileged legal files, anything under a BAA) goes to no model without a signed agreement that covers it. When unsure, use Claude on the Claude API and say so.",
            "- **Review with a different family** than the one that wrote the work; the QA gate's primary is Gemini for that reason.",
            "- **Recommending a model to a client** also goes through `vendor-and-tool-approval` (data terms, retention, BAA, exit path).", "",
            "## Sources", ""]
    for label_, url in SOURCES:
        out.append(f"- {label_}: <{url}> (retrieved {CATALOG_DATE})")
    out += ["", "Benchmark data: Source: OpenRouter (openrouter.ai), licensed CC BY 4.0. Costs per task are OpenRouter's measured averages for its own runs, not quotes; real costs depend on prompt length and caching.", ""]
    return "\n".join(out).rstrip() + "\n"


def model_catalog_json():
    data = dict(
        date=CATALOG_DATE,
        sources=[dict(label=label_, url=url) for label_, url in SOURCES],
        tiers=TIERS,
        models={key: dict(m, task_cost=round(task_cost(key), 4)) for key, m in MODELS.items()},
        task_types=[dict(name=task, tier=tier, primary=primary, fallback=fallback, effort=effort, why=why,
                         examples=TASK_INFO[task]["examples"], claude_brain=TASK_INFO[task]["brain"])
                    for task, tier, primary, fallback, effort, why in TASK_MODELS],
        roles=dict(routing=dict(primary=ROLES["routing"][0], fallback=ROLES["routing"][1], effort=ROLES["routing"][2], why=ROLES["routing"][3]),
                   synthesis=dict(task_type=ROLES["synthesis"][0])),
        agent_task_type=AGENT_TASK,
    )
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def knowledge_readme(agent):
    aid = agent["id"]
    deliver = "; ".join(d[0].lower() + d[1:] if d[1:2].islower() else d for d in agent["deliverables"])
    out = [f"# Knowledge folder: {agent['name']} (`{aid}`)", "",
           f"Reference documents for DIO's {agent['title']}. [`{aid}`](../../.claude/agents/{aid}.md) reads this folder before it answers or starts any task, and uses what is here ahead of general knowledge.", "",
           "## What belongs here", ""]
    out += [f"- {k}" for k in agent["knowledge"]]
    out += [f"- Approved examples and templates of this role's work: {deliver}",
            "- Lessons that change how this role works", "",
            "## What never goes here", "",
            "- Client confidential data or client deliverables, credentials, secrets or personal data",
            "- Confidential information from Erich's employer",
            "- Copies of the research in `docs/` (link to it instead)", "",
            "## Adding a document", "",
            "On GitHub, open this folder and choose **Add file → Upload files** (or **Create new file** to paste text), then commit to `main`. "
            "Use Markdown or plain text where you can (the web app reads `.md`, `.txt`, `.csv`, `.json` and `.yaml`), keep each file under 1 MB, name it `YYYY-MM-short-topic.md`, and put the source, owner and review date in the first lines.", "",
            "**This repository is public:** anything you add here can be read by anyone. Use sample or redacted documents.", "",
            "*This README is generated from `tools/team.py`; the documents beside it are not, and the build never touches them.*"]
    return "\n".join(out).rstrip() + "\n"


def knowledge_index():
    out = ["# Knowledge folders", "",
           "*The READMEs here are generated from `tools/team.py`; the documents beside them are not, and the build never touches them.*", "",
           "Each agent has its own folder of reference documents. **Every agent reads its folder before it answers a question or starts a task**, uses what is there ahead of general knowledge, and names the documents it relied on.", "",
           "## Rules for every folder", "",
           "- **What goes in:** reference documents that make the role better: approved templates and good examples, standards and checklists, guidance from licensed advisors, and lessons learned.",
           "- **What never goes in:** client confidential data, credentials or secrets, personal data, or confidential information from Erich's employer. **This repository is public.**",
           "- **Shared research stays in `docs/`:** link to it rather than copying it.",
           "- **Format:** Markdown or plain text where possible, under 1 MB each, named `YYYY-MM-short-topic.md`, with the source, owner and review date in the first lines.", "",
           "## Folders", "", "| Folder | Agent | What belongs there |", "| --- | --- | --- |"]
    for group in GROUPS:
        for a in [x for x in AGENTS if x["group"] == group]:
            out.append(f"| [`{a['id']}/`]({a['id']}/README.md) | {a['name']}, {a['title']} | " + "; ".join(a["knowledge"]) + " |")
    return "\n".join(out).rstrip() + "\n"


def claude_team_section(personas):
    out = ["<!-- BEGIN GENERATED: team (tools/build.py) -->", "",
           f"| Group | Agents |", "| --- | --- |"]
    for group in GROUPS:
        members = [a for a in AGENTS if a["group"] == group]
        if personas:
            out.append(f"| {group} | " + ", ".join(f"{a['name']} `{a['id']}`" for a in members) + " |")
        else:
            out.append(f"| {group} | " + ", ".join(f"`{a['id']}`" for a in members) + " |")
    out += ["", "<!-- END GENERATED: team -->"]
    return "\n".join(out)


def claude_md(current, personas):
    start, end = "<!-- BEGIN GENERATED: team (tools/build.py) -->", "<!-- END GENERATED: team -->"
    if start not in current or end not in current:
        raise SystemExit("CLAUDE.md: generated team markers not found")
    head = current.split(start)[0]
    tail = current.split(end, 1)[1]
    return head + claude_team_section(personas) + tail


# ---------------------------------------------------------------- build

def validate():
    problems = []
    names = [a["name"] for a in AGENTS]
    for n, c in Counter(names).items():
        if c > 1:
            problems.append(f"persona name {n} used {c} times")
    for a in AGENTS:
        for s in a["skills"]:
            if s not in SKILLS:
                problems.append(f"{a['id']}: unknown skill {s}")
        if a["reports_to"] != "erich" and a["reports_to"] not in BY_ID:
            problems.append(f"{a['id']}: unknown manager {a['reports_to']}")
        if a["model"] not in ALIAS_BRAIN:
            problems.append(f"{a['id']}: unknown model {a['model']}")
        if len(a["skills"]) > 32:
            problems.append(f"{a['id']}: more than 32 skills")
    for name, skill in SKILLS.items():
        if not any(name in a["skills"] for a in AGENTS):
            problems.append(f"skill {name} is used by no agent")
        if len(skill["description"]) > 1024:
            problems.append(f"skill {name}: description longer than 1,024 characters")
        if name not in WORKFLOWS and False:
            pass
    for name in WORKFLOWS:
        if name not in SKILLS:
            problems.append(f"workflow {name} has no skill")
    task_names = [x[0] for x in TASK_TYPES]
    for task, tier, primary, fallback, effort, why in TASK_MODELS:
        if task not in task_names:
            problems.append(f"models: unknown task type {task}")
        if tier not in TIERS:
            problems.append(f"models: {task}: unknown tier {tier}")
        for key in (primary, fallback):
            if key not in MODELS:
                problems.append(f"models: {task}: unknown model {key}")
        if primary == fallback:
            problems.append(f"models: {task}: fallback is the primary")
        for key in (primary, fallback):
            if key in MODELS and effort not in MODELS[key]["efforts"] and key == primary:
                problems.append(f"models: {task}: {key} does not support effort {effort}")
    for task in task_names:
        if task not in [x[0] for x in TASK_MODELS]:
            problems.append(f"models: task type {task} has no model")
    if ROLES["synthesis"][0] not in task_names or any(k not in MODELS for k in ROLES["routing"][:2]):
        problems.append("models: ROLES names an unknown task type or model")
    for aid, task in AGENT_TASK.items():
        if aid not in BY_ID:
            problems.append(f"models: AGENT_TASK names unknown agent {aid}")
        if task not in task_names:
            problems.append(f"models: {aid}: unknown task type {task}")
    for a in AGENTS:
        if a["id"] not in AGENT_TASK:
            problems.append(f"models: {a['id']} has no task type in AGENT_TASK")
    if problems:
        raise SystemExit("build: " + "\n  ".join(["invalid data:"] + problems))


def outputs(personas):
    files = {}
    for a in AGENTS:
        files[f".claude/agents/{a['id']}.md"] = agent_file(a, personas)
    for name, skill in SKILLS.items():
        files[f".claude/skills/{name}/SKILL.md"] = skill_file(name, skill)
    files["docs/expert-roster.md"] = expert_roster(personas)
    if personas:
        files["docs/agent-brains.md"] = agent_brains()
        files["knowledge/README.md"] = knowledge_index()
        for a in AGENTS:
            files[f"knowledge/{a['id']}/README.md"] = knowledge_readme(a)
    files["docs/model-catalog.md"] = model_catalog_md()
    files["docs/model-catalog.json"] = model_catalog_json()
    claude = ROOT / "CLAUDE.md"
    if claude.exists():
        files["CLAUDE.md"] = claude_md(claude.read_text(), personas)
    return files


PERSONAS = True  # names, brains and knowledge folders; False builds the team without them


def main():
    check = "--check" in sys.argv[1:]
    validate()
    files = outputs(PERSONAS)
    expected_agents = {p for p in files if p.startswith(".claude/agents/")}
    expected_skills = {p for p in files if p.startswith(".claude/skills/")}
    stale = [str(p.relative_to(ROOT)) for p in (ROOT / ".claude/agents").glob("*.md") if str(p.relative_to(ROOT)) not in expected_agents] if (ROOT / ".claude/agents").exists() else []
    stale += [str(p.relative_to(ROOT)) for p in (ROOT / ".claude/skills").glob("*/SKILL.md") if str(p.relative_to(ROOT)) not in expected_skills] if (ROOT / ".claude/skills").exists() else []
    if check:
        bad = [p for p, text in files.items() if not (ROOT / p).exists() or (ROOT / p).read_text() != text]
        if bad or stale:
            print("build --check: out of date (run python3 tools/build.py):")
            for p in bad:
                print(f"  {p}")
            for p in stale:
                print(f"  {p} (not generated; remove it or add it to tools/)")
            sys.exit(1)
        print(f"build --check: {len(files)} generated files are current")
        return
    for p in stale:
        (ROOT / p).unlink()
        print(f"removed stale {p}")
    written = 0
    for p, text in files.items():
        path = ROOT / p
        if path.exists() and path.read_text() == text:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        written += 1
    print(f"build: {len(AGENTS)} agents, {len(SKILLS)} skills, {len(files)} files ({written} written)")


if __name__ == "__main__":
    main()
