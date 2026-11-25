# Model catalog

*Generated from `tools/models.py` by `tools/build.py`. Chosen on 2026-11-25 from OpenRouter's live model list and benchmark data. Prices and scores change monthly: refresh every quarter (`python3 tools/refresh_models.py`).*

The most cost-efficient model for each type of work, across Claude and every model on OpenRouter. The web app uses it when **Auto** is chosen; the orchestrator uses it, through the `model-selection` skill, to name a model for each assignment; and the team uses the same method when it recommends models to clients.

## How the models were chosen

1. **Two independent benchmarks** from OpenRouter, run on every model with the same harness: **GPQA Diamond** (198 graduate-level science questions: careful reasoning) and **tau2-Bench Airline** (multi-turn customer-service tasks with tools and a policy: following rules while using tools). Each gives an accuracy and an average cost and time per task.
2. **A quality floor per tier**, below. A model qualifies if it meets both floors, supports structured outputs (the routing plan needs them) and answers a GPQA task in 120 seconds or less (the web app stops an answer at about 50 seconds, so slow models fall back).
3. **The primary is the qualifying model with the lowest cost per task** (one GPQA task plus one tau2 task). The fallback is the next-best qualifying model from a different provider.
4. **Privacy and routing rules** apply on top: see the last section.

| Tier | GPQA floor | tau2 floor | For |
| --- | -: | -: | --- |
| **Deep** | 0.925 | 0.75 | Judgment where a mistake is expensive |
| **Reasoning** | 0.930 | 0.00 | Math, statistics and science-style reasoning; tool use not needed |
| **Standard** | 0.890 | 0.74 | Everyday specialist work that a review step checks |
| **Fast** | 0.860 | 0.68 | High-volume, well-defined work |
| **Frontier** | 0.960 | 0.78 | The hardest problems only; best quality regardless of price |

## Model by type of work

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

| Task type | Examples | Why this model |
| --- | --- | --- |
| Strategy and high-stakes decisions | Decision memos, quarterly goals, the monthly report to the Chairman, offer and pricing design | Sonnet is the cheapest model that meets the Deep floor and the fastest; Gemini 3.7 Flash scores higher on GPQA as backup. |
| Architecture and technical design | Solution designs, architecture decision records, platform and data architecture, build-versus-buy | Design mistakes multiply; Deep floor at the lowest price. |
| Security, legal and compliance review | Threat models, agent safety audits, contract review, risk reviews | Careful reading at the Deep floor; Claude runs on the Claude API directly, which keeps sensitive text off third-party routes. |
| QA gates and fact-checks | Every QA step, estimate and pricing checks, claims in published content | Highest GPQA in the Deep tier at almost Sonnet's cost, and a different model family from most of the work it reviews. |
| Root-cause analysis and statistics | Incident reviews, DMAIC analysis, control charts, measurement system checks | Cheapest model with GPQA of 0.93 or more; this work needs reasoning, not multi-turn tool use. |
| Software and automation build | Features, APIs, agent workflows, data pipelines, tests, infrastructure as code | Standard floor at about one-sixth of Sonnet's cost; escalate security-sensitive code to the Deep tier. |
| Infrastructure and production changes | Deployment plans, migrations, runbooks, rollback plans | Production work needs Deep-tier care; a cheaper model saves cents and risks an outage. |
| Research and analysis | Market research, competitor matrices, data analysis, financial models, vertical briefs | Long-context reading at the Standard floor for a fraction of the cost; claims still go through a Deep QA gate. |
| Client-facing documents | Proposals, SOWs, assessment reports, QBR decks, case studies | Clients read every word; Deep floor at the lowest price. |
| Long-form content and training | Articles, newsletters, scripts, curricula, workshop materials | Good writing at the Standard floor; fact-checks happen at the QA step. |
| Planning, coordination and communication | Routing plans, assignments, schedules, status reports, check-ins, support replies, outreach drafts | Clear, reliable everyday work at the lowest Standard-tier price. |
| Short-form and high-volume content | Social posts, captions, hooks, ad variants, titles and meta descriptions, thumbnail text | Many small pieces; GPT-6 Luna is the cheapest model that meets the Fast floor. |
| Routine operations | Filing records, CRM hygiene, tagging, summaries of long threads, formatting, reminders, monitoring triage | Templated steps that follow a procedure; Haiku is nearly as cheap as Luna, faster, and better at following procedures. |
| Hardest problems (CEO escalation only) | A problem the Deep brain has not settled after two passes, or a novel decision with many interacting unknowns | Top score on both benchmarks; only the orchestrator assigns it, after the Deep tier has not settled the problem. |

**Escalate one tier** (Standard to Deep, Deep to Frontier) when the work involves money, production, security or legal terms and is client-final, is new to the firm, or failed a review. **Step down one tier** for routine work a review step will catch. Frontier is the orchestrator's call alone.

**Claude Code** subagents run on Claude only and keep the brains in [agent-brains.md](agent-brains.md). On these two benchmarks Claude Sonnet 5.5 scored higher than Claude Opus 5.5 at half the price, so moving the Deep agents from Opus to Sonnet in Claude Code would cut their cost about in half; that change is Erich's decision and has not been made.

## The models

| Model | Maker | OpenRouter ID | Claude API ID | Price per M tokens (in / out) | Context | GPQA | tau2 | Cost per task pair | Seconds per GPQA task | Reasoning efforts | Note |
| --- | --- | --- | --- | --- | -: | -: | -: | -: | -: | --- | --- |
| **GPT-6 Luna** | OpenAI | `openai/gpt-6-luna` | n/a | $0.1 / $0.5 | 1,050K | 0.878 | 0.684 | $0.012 | 92 | none, low, medium, high, xhigh, max | The cheapest model that meets the Fast floor; best for short, single-turn writing. |
| **Claude Haiku 5.5** | Anthropic | `anthropic/claude-haiku-5.5` | `claude-haiku-5-5` | $0.1 / $0.5 | 1,000K | 0.868 | 0.735 | $0.017 | 36 | none, low, medium, high, xhigh, max | Nearly as cheap as GPT-6 Luna, faster, and better at following procedures over several turns. |
| **DeepSeek V4.1 Flash** | DeepSeek | `deepseek/deepseek-v4.1-flash-1017` | n/a | $0.15 / $0.6 | 1,048K | 0.906 | 0.754 | $0.034 | 84 | none, low, high, max | About one-sixth of Sonnet's cost per task for Standard-tier quality; open weights served by many providers. |
| **GPT-6.1 Sol** | OpenAI | `openai/gpt-6.1-sol` | n/a | $2 / $10 | 1,050K | 0.938 | 0.683 | $0.13 | 33 | low, medium, high, xhigh, max | Cheapest GPQA-grade reasoning; weaker on multi-turn policy and tool use, so used for statistics and analysis only. |
| **Claude Sonnet 5.5** | Anthropic | `anthropic/claude-sonnet-5.5` | `claude-sonnet-5-5` | $2 / $10 | 1,000K | 0.930 | 0.778 | $0.21 | 19 | low, medium, high, xhigh, max | Cheapest and fastest model that meets the Deep floor; beats Claude Opus 5.5 on both benchmarks at half the price. |
| **Gemini 3.7 Flash** | Google | `google/gemini-3.7-flash` | n/a | $0.75 / $3.75 | 1,048K | 0.945 | 0.772 | $0.22 | 61 | low, medium, high | Highest GPQA in the Deep tier at nearly the same cost as Sonnet; a different family, so a good independent reviewer. Slower. |
| **Claude Opus 5.5** | Anthropic | `anthropic/claude-opus-5.5` | `claude-opus-5-5` | $4 / $20 | 1,000K | 0.900 | 0.752 | $0.43 | 36 | low, medium, high, xhigh, max | Not the primary for any task type: Sonnet 5.5 scored higher on both benchmarks for half the price. Kept for explicit choice. |
| **Gemini 4 Argon** | Google | `google/gemini-4-argon` | n/a | $2 / $10 | 1,048K | 0.965 | 0.787 | $0.59 | 102 | low, medium, high | Top score on both benchmarks; about three times the cost of Sonnet per task, and slow. Escalation only. |

Claude models run on the Claude API directly when `ANTHROPIC_API_KEY` is set (same price; prompt caching and Anthropic's refusal fallback), otherwise through OpenRouter.

## The API calls

OpenRouter speaks the OpenAI Chat Completions format at one endpoint for every model; the model ID picks the model. Keys stay in environment variables (`OPENROUTER_API_KEY`), never in code or this repository.

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "models": ["deepseek/deepseek-v4.1-flash-1017", "anthropic/claude-haiku-5.5"],
    "messages": [{"role": "system", "content": "You are ..."}, {"role": "user", "content": "..."}],
    "reasoning": {"effort": "low"},
    "provider": {"zdr": true, "data_collection": "deny", "require_parameters": true},
    "max_tokens": 4000,
    "stream": true
  }'
```

| Field | What it does |
| --- | --- |
| `model` or `models` | One model ID, or a list: OpenRouter tries them in order if one is down, rate-limited or refuses |
| `reasoning.effort` | How hard the model thinks; use only the efforts the model supports (table above) |
| `provider.zdr: true` | Only endpoints with zero data retention; use for anything a client would call confidential |
| `provider.data_collection: "deny"` | Never an endpoint that may train on or store prompts |
| `provider.require_parameters: true` | Only endpoints that support every parameter sent (for example structured outputs) |
| `response_format: {"type": "json_schema", ...}` | Structured output that matches a JSON schema (the routing plan) |
| `usage.cost` in the response | What the call cost, in USD |

The Claude API call for the same work is `POST https://api.anthropic.com/v1/messages` with `model` set to the Claude API ID above and `output_config.effort` for effort. The web app's code is in `web/server/openrouter.ts` and `web/server/claude.ts`.

## Privacy and routing rules

- **Client confidential data** goes only to the Claude API directly or to OpenRouter with zero data retention enforced. The web app enforces it by default (`OPENROUTER_ZDR`, on unless set to `false`). Every model in the catalog had at least one zero-data-retention endpoint that supports structured outputs on 2026-11-25, so the default rules none of them out.
- **Regulated data** (patient records, privileged legal files, anything under a BAA) goes to no model without a signed agreement that covers it. When unsure, use Claude on the Claude API and say so.
- **Review with a different family** than the one that wrote the work; the QA gate's primary is Gemini for that reason.
- **Recommending a model to a client** also goes through `vendor-and-tool-approval` (data terms, retention, BAA, exit path).

## Sources

- OpenRouter model list (prices, context, parameters): <https://openrouter.ai/api/v1/models> (retrieved 2026-11-25)
- OpenRouter benchmarks: GPQA Diamond: <https://openrouter.ai/benchmarks/gpqa-diamond> (retrieved 2026-11-25)
- OpenRouter benchmarks: tau2-Bench Airline: <https://openrouter.ai/benchmarks/tau2-bench-airline> (retrieved 2026-11-25)
- Benchmark leaderboard export, snapshot 2026-11-25 (CC BY 4.0): <https://openrouter.ai/api/v1/datasets/exports/benchmark-leaderboard/2026-11-25.json> (retrieved 2026-11-25)
- OpenRouter zero-data-retention endpoints (each catalog model has one that supports structured outputs): <https://openrouter.ai/api/v1/endpoints/zdr> (retrieved 2026-11-25)
- OpenRouter API: provider routing and zero data retention: <https://openrouter.ai/docs/guides/routing/provider-selection.md> (retrieved 2026-11-25)
- OpenRouter API: structured outputs: <https://openrouter.ai/docs/guides/features/structured-outputs.md> (retrieved 2026-11-25)
- OpenRouter API: reasoning effort: <https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.md> (retrieved 2026-11-25)

Benchmark data: Source: OpenRouter (openrouter.ai), licensed CC BY 4.0. Costs per task are OpenRouter's measured averages for its own runs, not quotes; real costs depend on prompt length and caching.
