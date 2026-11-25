---
name: agent-and-skill-authoring
description: "Create a new agent or skill, or improve an existing one, in this repository: follow the official Claude Code subagent and skill formats, edit the data in tools/team.py and tools/skills.py (never the generated .claude/ files), give agents least-privilege tools, a clear description, skills, a knowledge folder, a brain and a persona, then run python3 tools/build.py and --check and send the change to review. Use whenever the team needs a new role or method, or an agent answered badly."
---

# Agent and skill authoring

*Products, training and team skill for the DIO expert team.* Create or improve agents and skills in this repository the right way: data in tools/, the official frontmatter, then build and check.

## When to use

A new role or repeatable method is needed, two agents overlap, or an agent or skill produced a wrong or weak answer.

## Read first

- The official docs: https://code.claude.com/docs/en/sub-agents and https://code.claude.com/docs/en/skills. Fields change; check them.
- `docs/expert-roster.md` and `docs/agent-brains.md` for what already exists.
- `tools/README.md` for how the build works.

## Rules for agents

- **One clear job.** The `description` says when to use the agent (start with "Use for ..." or "Use when ..."; add "proactively" only when the main session should delegate on its own).
- **Least-privilege tools:** read-only advisors get `Read, Grep, Glob, WebSearch, WebFetch`; writers add `Write, Edit`; builders add `Bash`. Only the orchestrator gets `Agent`.
- **Skills:** list the skills the agent uses (they are preloaded into its context); keep it to the ones it really needs.
- **Brain:** `opus` for strategy, legal, finance, security, architecture and QA judgment; `sonnet` for most specialist work; `haiku` for fast, high-volume, well-defined work. Give the reason.
- **Knowledge folder:** `knowledge/<agent>/` with a README saying what belongs there.
- **Persona:** a Star Trek name no other agent uses, a voice and a working style. Agents never claim to be people.
- **Guardrails stay:** decision rights, the privacy lock and the employer boundary are in every agent and never weakened.

## Rules for skills

- A skill is a **method**, reusable by several agents: when to use it, what to read first, numbered steps, the output format and quality checks.
- `name` is lowercase with hyphens and matches the folder; the `description` says what it does **and when to use it**, under about 1,000 characters.
- Keep `SKILL.md` under 500 lines; move long reference material into a separate file in the skill folder.

## Method

1. Read the request and the evidence (for a fix: the bad answer, what was expected, and the instruction or document that caused it).
2. Edit `tools/team.py` (agents) or the `tools/skills_*.py` files (skills).
3. Run `python3 tools/build.py`, then `python3 tools/build.py --check`.
4. Test: ask the agent a question that would have failed before.
5. Send the change to `quality-reviewer`, then commit with a message that says what changed and why.

## Used by

`agent-builder`.
