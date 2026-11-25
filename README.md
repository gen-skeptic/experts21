# Experts21: the DIO expert team

A team of **50 synthetic employees**, expert AI agents built with Claude Code, for **Dautel Intelligent Operations (DIO)**, an AI consulting and deployment firm in Boynton Beach, Florida. They advise on planning, opening and running the firm, each with its own knowledge, brain and Star Trek personality, and they work together through an orchestrator. Built by following the "Build a team of synthetic employees with Claude Code" guide, steps 1 to 11, for the multi-agent systems course.

- **Live app:** <https://dio-experts21.netlify.app> (deploy steps in [web/README.md](web/README.md))
- **Source:** <https://github.com/gen-skeptic/experts21>
- **Talk to the team:** [docs/how-to-talk-to-your-experts.md](docs/how-to-talk-to-your-experts.md)

## What's here

| Step | What was built | Where |
| :-: | --- | --- |
| 3 | Research on the firm: market, target customers, competitors, services and pricing, startup and operating costs, permits and licenses in Boynton Beach and Palm Beach County, staffing, marketing, biggest risks, 90-day plan | [`docs/`](docs/README.md) |
| 4 | The expert roster: 50 roles with one-line jobs and reporting lines, and 57 shared skills with the agents that use each | [`docs/expert-roster.md`](docs/expert-roster.md) |
| 5 | Every role as a Claude Code subagent, every skill as a project skill, plus an orchestrator (Picard) and a meta agent that builds agents (Soong), and the team guide for Claude | [`.claude/agents/`](.claude/agents/), [`.claude/skills/`](.claude/skills/), [`CLAUDE.md`](CLAUDE.md) |
| 6 | Example prompts: one expert, the whole team, a skill on its own | [`docs/how-to-talk-to-your-experts.md`](docs/how-to-talk-to-your-experts.md) |
| 7 | A knowledge folder per agent, a brain per agent (12 Opus, 34 Sonnet, 4 Haiku) and a Star Trek name, voice and working style for each | [`knowledge/`](knowledge/README.md), [`docs/agent-brains.md`](docs/agent-brains.md) |
| 8 | A test document in Cogley's (the business attorney's) knowledge folder: a fictional client MSA | [`knowledge/business-attorney/`](knowledge/business-attorney/) |
| 9 | Cogley packaged as a standalone Claude skill to upload under Customize → Skills | [`exports/`](exports/README.md) |
| 10 | A Node.js script that asks Cogley questions through the Claude Agent SDK | [`sdk/`](sdk/README.md) |
| 11 | A React web app with Netlify Functions: talk to any expert or the whole team | [`web/`](web/README.md), [`netlify.toml`](netlify.toml) |
| + | Any model through OpenRouter: a model catalog with the most cost-efficient model for each type of work (from OpenRouter's prices and benchmarks), a `model-selection` skill for the orchestrator, and an Auto model choice in the web app | [`docs/model-catalog.md`](docs/model-catalog.md), [`.claude/skills/model-selection/`](.claude/skills/model-selection/SKILL.md) |

Supporting folders: [`design-system/`](design-system/README.md) (the Dautel brand kit, from gen-skeptic/dautel_brand) and [`tools/`](tools/README.md) (the data the agents and skills are generated from).

## The team

Picard (`orchestrator`) runs the team as the CEO agent, with Riker (chief of staff), Guinan (advisory board), Spock (CTO) and Sisko (operations and finance). Cogley (attorney), Tuvok (CPA) and Saru (insurance and risk) advise; Odo is the independent quality gate; Seven leads Lean Six Sigma; Kirk sells; Troi keeps clients happy; Data builds governed agents; O'Brien runs the platforms; Geordi leads the software team; Uhura leads marketing; Soong builds new agents. The full list, with every voice, working style and brain, is in [docs/agent-brains.md](docs/agent-brains.md).

The firm's rules hold for every agent: Erich (the Chairman) decides anything with money or ethics and approves every deployment to a customer; nothing is published with private data; no work crosses the boundary with Erich's employer; and every claim is backed by evidence.

Most of the content was reused from the DIO operating manual (gen-skeptic/experts): the business plan research, the 49 role definitions, their brains and personas, and the processes behind the skills. The names are new (Star Trek characters), and the permits, costs, local competitors and Florida AI-law research is new as of November 25, 2026. Named prospect lists stay in the private repository.

## Use it

**In Claude Code** (claude.ai/code, or the terminal on the laptop), from this repository:

```text
@agent-business-attorney What should our MSA say about AI output we can't guarantee?
```

```text
@agent-orchestrator Should we take a $9,000 intake-agent build for a 12-attorney law firm next month? Bring in the experts.
```

**On the laptop (Omarchy / Arch Linux):**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
git clone https://github.com/gen-skeptic/experts21.git ~/experts21
```

```bash
cd ~/experts21 && claude
```

**From code:** see [sdk/README.md](sdk/README.md). **In a browser:** the live app above, or deploy your own with [web/README.md](web/README.md).

## Change the team

The agents, skills, roster, brains table and knowledge READMEs are generated. Edit `tools/team.py` (agents) or `tools/skills_*.py` (skills), then:

```bash
python3 tools/build.py
```

```bash
python3 tools/build.py --check
```

Or ask `@agent-agent-builder` to do it. Documents you add to a knowledge folder are never touched by the build. **This repository is public:** put only sample or redacted documents in it.
