---
name: model-selection
description: "Choose the model for a task: classify the work into a task type, take the catalog's primary model (the cheapest one that meets the type's quality floor on OpenRouter's benchmarks), escalate or step down by the rules, keep client confidential data on zero-data-retention routes, and name a fallback. Covers Claude models on the Claude API and any model on OpenRouter. Use whenever you assign work to an expert, compare model costs, or someone asks which model to use."
---

# Model selection

*Strategy and coordination skill for the DIO expert team.* Pick the most cost-efficient model for each piece of work, from Claude or OpenRouter, by work task type, with privacy and fallbacks.

## When to use

Every time work is assigned: the orchestrator picks a task type and a model for each assignment, and anyone comparing AI costs for the firm or a client uses the same method. The full catalog, with prices, benchmark scores and sources, is in `docs/model-catalog.md`.

## Where the choice applies

- **The web app** (Netlify): any model in the catalog runs, through the Claude API (Claude models) or OpenRouter (all others). "Auto" uses the catalog below.
- **Claude Code and the Agent SDK:** subagents run on Claude only. Pass the brain in the table's last column as `model` on the Agent call when it differs from the expert's default.
- **Client work:** recommend models with the same method, then put the choice through `vendor-and-tool-approval` (data terms, BAA, retention).

## Method

1. **Classify the work** into one task type from the table (the same types as `docs/agent-brains.md`). When a request mixes types, split it or use the higher tier.
2. **Take the primary model** for that task type. It is the cheapest model that meets the tier's quality floor on two independent benchmarks (GPQA Diamond for careful reasoning, tau2-Bench for following policy while using tools), supports structured outputs, and is fast enough for the web app's 50-second answer window.
3. **Escalate one tier** (Standard → Deep, Deep → Frontier) when the work involves money, production, security or legal terms and is client-final, when it is new to the firm, or after a failed review. Frontier (Gemini 4 Argon) is the orchestrator's call alone, after Deep has not settled the problem.
4. **Step down one tier** for routine, templated or high-volume work that a review step will catch.
5. **Use a different model family for review** than the one that produced the work (the QA gate defaults to Gemini 3.7 Flash because most production runs on Claude or DeepSeek).
6. **Privacy first:** client confidential data and anything personal go only to the Claude API directly or to OpenRouter with zero data retention enforced (`provider.zdr: true`, the web app's default). Regulated data (patient records, privileged legal files) never goes to a model without a signed agreement (a BAA for HIPAA); if unsure, use Claude on the Claude API and say so.
7. **Name the fallback:** if the primary is down, refuses or has no compliant endpoint, use the fallback in the table, then the expert's own Claude brain.
8. **Keep effort low** for Standard and Fast work and medium for Deep; raise it before switching to a pricier model, and only when results show it helps.
9. **Record the choice** in the routing plan: task type, model and a one-line reason.

## Rules of thumb from the benchmarks (November 2026)

- Claude Sonnet 5.5 scored higher than Claude Opus 5.5 on both benchmarks for half the price, so Sonnet is the catalog's Deep-tier default; Opus is kept for explicit choice. (Claude Code still runs the Deep agents on Opus; moving them is Erich's call.)
- DeepSeek V4.1 Flash reaches Standard quality at about one-sixth of Sonnet's cost per task, which makes it the default for code drafts, research and long-form writing.
- For short, high-volume pieces, GPT-6 Luna and Claude Haiku 5.5 cost about a cent per task pair; Haiku is faster and better at following procedures.
- Prices and scores move monthly: refresh the catalog every quarter (`python3 tools/refresh_models.py`) and don't quote these numbers to clients without rechecking.

## The catalog (2026-11-25)

Generated from `tools/models.py`. Cost is the average cost of one GPQA Diamond task plus one tau2-Bench task on OpenRouter's benchmarks: a like-for-like comparison, not a quote. Full details and sources: `docs/model-catalog.md`.

| Task type | Tier | Primary model (OpenRouter ID) | Cost | Fallback | Effort | Claude Code brain |
| --- | --- | --- | -: | --- | --- | --- |
| Strategy and high-stakes decisions | Deep | Claude Sonnet 5.5 (`anthropic/claude-sonnet-5.5`) | $0.21 | Gemini 3.7 Flash | medium | Deep (`opus`) |
| Architecture and technical design | Deep | Claude Sonnet 5.5 (`anthropic/claude-sonnet-5.5`) | $0.21 | Gemini 3.7 Flash | medium | Deep (`opus`) |
| Security, legal and compliance review | Deep | Claude Sonnet 5.5 (`anthropic/claude-sonnet-5.5`) | $0.21 | Gemini 3.7 Flash | medium | Deep (`opus`) |
| QA gates and fact-checks | Deep | Gemini 3.7 Flash (`google/gemini-3.7-flash`) | $0.22 | Claude Sonnet 5.5 | medium | Deep (`opus`) |
| Root-cause analysis and statistics | Reasoning | GPT-6.1 Sol (`openai/gpt-6.1-sol`) | $0.13 | Gemini 3.7 Flash | medium | Deep (`opus`) |
| Software and automation build | Standard | DeepSeek V4.1 Flash (`deepseek/deepseek-v4.1-flash-1017`) | $0.034 | Claude Sonnet 5.5 | low | Standard (`sonnet`) |
| Infrastructure and production changes | Deep | Claude Sonnet 5.5 (`anthropic/claude-sonnet-5.5`) | $0.21 | Gemini 3.7 Flash | medium | Standard (`sonnet`) |
| Research and analysis | Standard | DeepSeek V4.1 Flash (`deepseek/deepseek-v4.1-flash-1017`) | $0.034 | Gemini 3.7 Flash | low | Standard (`sonnet`) |
| Client-facing documents | Deep | Claude Sonnet 5.5 (`anthropic/claude-sonnet-5.5`) | $0.21 | Gemini 3.7 Flash | medium | Standard (`sonnet`) |
| Long-form content and training | Standard | DeepSeek V4.1 Flash (`deepseek/deepseek-v4.1-flash-1017`) | $0.034 | Claude Haiku 5.5 | low | Standard (`sonnet`) |
| Planning, coordination and communication | Standard | DeepSeek V4.1 Flash (`deepseek/deepseek-v4.1-flash-1017`) | $0.034 | Claude Haiku 5.5 | low | Standard (`sonnet`) |
| Short-form and high-volume content | Fast | GPT-6 Luna (`openai/gpt-6-luna`) | $0.012 | Claude Haiku 5.5 | low | Fast (`haiku`) |
| Routine operations | Fast | Claude Haiku 5.5 (`anthropic/claude-haiku-5.5`) | $0.017 | GPT-6 Luna | low | Fast (`haiku`) |
| Hardest problems (CEO escalation only) | Frontier | Gemini 4 Argon (`google/gemini-4-argon`) | $0.59 | Claude Sonnet 5.5 | medium | Frontier (`fable`) |

The orchestrator's own routing plan runs on Claude Sonnet 5.5 (fallback Gemini 3.7 Flash) at low effort; its combined answer uses the "Strategy and high-stakes decisions" row.

| Model | OpenRouter ID | Claude API ID | Price per M tokens (in / out) | GPQA | tau2 | Cost |
| --- | --- | --- | --- | -: | -: | -: |
| Claude Sonnet 5.5 | `anthropic/claude-sonnet-5.5` | `claude-sonnet-5-5` | $2 / $10 | 0.930 | 0.778 | $0.21 |
| Gemini 3.7 Flash | `google/gemini-3.7-flash` | n/a | $0.75 / $3.75 | 0.945 | 0.772 | $0.22 |
| GPT-6.1 Sol | `openai/gpt-6.1-sol` | n/a | $2 / $10 | 0.938 | 0.683 | $0.13 |
| DeepSeek V4.1 Flash | `deepseek/deepseek-v4.1-flash-1017` | n/a | $0.15 / $0.6 | 0.906 | 0.754 | $0.034 |
| GPT-6 Luna | `openai/gpt-6-luna` | n/a | $0.1 / $0.5 | 0.878 | 0.684 | $0.012 |
| Claude Haiku 5.5 | `anthropic/claude-haiku-5.5` | `claude-haiku-5-5` | $0.1 / $0.5 | 0.868 | 0.735 | $0.017 |
| Gemini 4 Argon | `google/gemini-4-argon` | n/a | $2 / $10 | 0.965 | 0.787 | $0.59 |
| Claude Opus 5.5 | `anthropic/claude-opus-5.5` | `claude-opus-5-5` | $4 / $20 | 0.900 | 0.752 | $0.43 |

## Used by

`orchestrator`, `chief-of-staff`, `cto-principal-architect`, `operations-finance-manager`.
