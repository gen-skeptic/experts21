"""The model catalog: the most cost-efficient model for each work task type, across Claude and OpenRouter.

Chosen on November 25, 2026 from OpenRouter's live model list (https://openrouter.ai/api/v1/models: prices, context,
supported parameters) and its independent benchmark export (https://openrouter.ai/benchmarks, dataset
benchmark-leaderboard 2026-11-25, CC BY 4.0: "Source: OpenRouter (openrouter.ai)"). Two benchmarks give a quality and a
cost-per-task figure for each model: GPQA Diamond (careful reasoning) and tau2-Bench Airline (following policy while
using tools over several turns).

Method: each task type has a quality floor (a tier below). The primary model is the one with the lowest combined cost
per task (GPQA + tau2) that meets the floor, supports structured outputs and answered a GPQA task in 120 seconds or
less. The fallback is the next-best model from a different provider. Refresh it every quarter: re-run
`python3 tools/refresh_models.py` (prints the ranking) and update this file.

build.py turns this into docs/model-catalog.md, docs/model-catalog.json (read by the web app) and the table in the
`model-selection` skill.
"""

CATALOG_DATE = "2026-11-25"

# Quality floors per tier: (minimum GPQA Diamond accuracy, minimum tau2-Bench Airline accuracy).
TIERS = {
    "deep": dict(label="Deep", gpqa=0.925, tau=0.75, why="Judgment where a mistake is expensive"),
    "reasoning": dict(label="Reasoning", gpqa=0.93, tau=0.0, why="Math, statistics and science-style reasoning; tool use not needed"),
    "standard": dict(label="Standard", gpqa=0.89, tau=0.74, why="Everyday specialist work that a review step checks"),
    "fast": dict(label="Fast", gpqa=0.86, tau=0.68, why="High-volume, well-defined work"),
    "frontier": dict(label="Frontier", gpqa=0.96, tau=0.78, why="The hardest problems only; best quality regardless of price"),
}

# Models in the catalog. `openrouter` is the OpenRouter model ID; `anthropic` is the Claude API model ID (Claude models
# are called on the Claude API directly when ANTHROPIC_API_KEY is set: same price, better caching and refusal
# fallbacks; otherwise through OpenRouter). Prices are USD per million tokens. Benchmarks: accuracy, average cost per
# task (USD) and average seconds per task.
MODELS = {
    "claude-sonnet-5.5": dict(
        name="Claude Sonnet 5.5", maker="Anthropic", openrouter="anthropic/claude-sonnet-5.5", anthropic="claude-sonnet-5-5",
        input=2.0, output=10.0, cache_read=0.1, context=1_000_000,
        gpqa=0.930, gpqa_cost=0.0261, gpqa_s=19, tau=0.778, tau_cost=0.1801, tau_s=65,
        efforts=["low", "medium", "high", "xhigh", "max"],
        note="Cheapest and fastest model that meets the Deep floor; beats Claude Opus 5.5 on both benchmarks at half the price."),
    "gemini-3.7-flash": dict(
        name="Gemini 3.7 Flash", maker="Google", openrouter="google/gemini-3.7-flash", anthropic=None,
        input=0.75, output=3.75, cache_read=0.075, context=1_048_576,
        gpqa=0.945, gpqa_cost=0.0301, gpqa_s=61, tau=0.772, tau_cost=0.1856, tau_s=213,
        efforts=["low", "medium", "high"],
        note="Highest GPQA in the Deep tier at nearly the same cost as Sonnet; a different family, so a good independent reviewer. Slower."),
    "gpt-6.1-sol": dict(
        name="GPT-6.1 Sol", maker="OpenAI", openrouter="openai/gpt-6.1-sol", anthropic=None,
        input=2.0, output=10.0, cache_read=0.1, context=1_050_000,
        gpqa=0.938, gpqa_cost=0.0221, gpqa_s=33, tau=0.683, tau_cost=0.1071, tau_s=135,
        efforts=["low", "medium", "high", "xhigh", "max"],
        note="Cheapest GPQA-grade reasoning; weaker on multi-turn policy and tool use, so used for statistics and analysis only."),
    "deepseek-v4.1-flash": dict(
        name="DeepSeek V4.1 Flash", maker="DeepSeek", openrouter="deepseek/deepseek-v4.1-flash-1017", anthropic=None,
        input=0.15, output=0.6, cache_read=0.003, context=1_048_576,
        gpqa=0.906, gpqa_cost=0.0084, gpqa_s=84, tau=0.754, tau_cost=0.0260, tau_s=76,
        efforts=["none", "low", "high", "max"],
        note="About one-sixth of Sonnet's cost per task for Standard-tier quality; open weights served by many providers."),
    "gpt-6-luna": dict(
        name="GPT-6 Luna", maker="OpenAI", openrouter="openai/gpt-6-luna", anthropic=None,
        input=0.1, output=0.5, cache_read=0.01, context=1_050_000,
        gpqa=0.878, gpqa_cost=0.0029, gpqa_s=92, tau=0.684, tau_cost=0.0087, tau_s=302,
        efforts=["none", "low", "medium", "high", "xhigh", "max"],
        note="The cheapest model that meets the Fast floor; best for short, single-turn writing."),
    "claude-haiku-5.5": dict(
        name="Claude Haiku 5.5", maker="Anthropic", openrouter="anthropic/claude-haiku-5.5", anthropic="claude-haiku-5-5",
        input=0.1, output=0.5, cache_read=0.01, context=1_000_000,
        gpqa=0.868, gpqa_cost=0.0043, gpqa_s=36, tau=0.735, tau_cost=0.0130, tau_s=73,
        efforts=["none", "low", "medium", "high", "xhigh", "max"],
        note="Nearly as cheap as GPT-6 Luna, faster, and better at following procedures over several turns."),
    "gemini-4-argon": dict(
        name="Gemini 4 Argon", maker="Google", openrouter="google/gemini-4-argon", anthropic=None,
        input=2.0, output=10.0, cache_read=0.1, context=1_048_576,
        gpqa=0.965, gpqa_cost=0.0947, gpqa_s=102, tau=0.787, tau_cost=0.4983, tau_s=348,
        efforts=["low", "medium", "high"],
        note="Top score on both benchmarks; about three times the cost of Sonnet per task, and slow. Escalation only."),
    "claude-opus-5.5": dict(
        name="Claude Opus 5.5", maker="Anthropic", openrouter="anthropic/claude-opus-5.5", anthropic="claude-opus-5-5",
        input=4.0, output=20.0, cache_read=0.2, context=1_000_000,
        gpqa=0.900, gpqa_cost=0.0582, gpqa_s=36, tau=0.752, tau_cost=0.3689, tau_s=141,
        efforts=["low", "medium", "high", "xhigh", "max"],
        note="Not the primary for any task type: Sonnet 5.5 scored higher on both benchmarks for half the price. Kept for explicit choice."),
}

# Primary and fallback model for each work task type (the names match tools/brains.py), with the reasoning effort the
# web app asks for (capped at medium there). Claude Code subagents run on Claude only and keep the brain that
# tools/brains.py gives the task type.
TASK_MODELS = [
    ("Strategy and high-stakes decisions", "deep", "claude-sonnet-5.5", "gemini-3.7-flash", "medium",
     "Sonnet is the cheapest model that meets the Deep floor and the fastest; Gemini 3.7 Flash scores higher on GPQA as backup."),
    ("Architecture and technical design", "deep", "claude-sonnet-5.5", "gemini-3.7-flash", "medium",
     "Design mistakes multiply; Deep floor at the lowest price."),
    ("Security, legal and compliance review", "deep", "claude-sonnet-5.5", "gemini-3.7-flash", "medium",
     "Careful reading at the Deep floor; Claude runs on the Claude API directly, which keeps sensitive text off third-party routes."),
    ("QA gates and fact-checks", "deep", "gemini-3.7-flash", "claude-sonnet-5.5", "medium",
     "Highest GPQA in the Deep tier at almost Sonnet's cost, and a different model family from most of the work it reviews."),
    ("Root-cause analysis and statistics", "reasoning", "gpt-6.1-sol", "gemini-3.7-flash", "medium",
     "Cheapest model with GPQA of 0.93 or more; this work needs reasoning, not multi-turn tool use."),
    ("Software and automation build", "standard", "deepseek-v4.1-flash", "claude-sonnet-5.5", "low",
     "Standard floor at about one-sixth of Sonnet's cost; escalate security-sensitive code to the Deep tier."),
    ("Infrastructure and production changes", "deep", "claude-sonnet-5.5", "gemini-3.7-flash", "medium",
     "Production work needs Deep-tier care; a cheaper model saves cents and risks an outage."),
    ("Research and analysis", "standard", "deepseek-v4.1-flash", "gemini-3.7-flash", "low",
     "Long-context reading at the Standard floor for a fraction of the cost; claims still go through a Deep QA gate."),
    ("Client-facing documents", "deep", "claude-sonnet-5.5", "gemini-3.7-flash", "medium",
     "Clients read every word; Deep floor at the lowest price."),
    ("Long-form content and training", "standard", "deepseek-v4.1-flash", "claude-haiku-5.5", "low",
     "Good writing at the Standard floor; fact-checks happen at the QA step."),
    ("Planning, coordination and communication", "standard", "deepseek-v4.1-flash", "claude-haiku-5.5", "low",
     "Clear, reliable everyday work at the lowest Standard-tier price."),
    ("Short-form and high-volume content", "fast", "gpt-6-luna", "claude-haiku-5.5", "low",
     "Many small pieces; GPT-6 Luna is the cheapest model that meets the Fast floor."),
    ("Routine operations", "fast", "claude-haiku-5.5", "gpt-6-luna", "low",
     "Templated steps that follow a procedure; Haiku is nearly as cheap as Luna, faster, and better at following procedures."),
    ("Hardest problems (CEO escalation only)", "frontier", "gemini-4-argon", "claude-sonnet-5.5", "medium",
     "Top score on both benchmarks; only the orchestrator assigns it, after the Deep tier has not settled the problem."),
]

# Roles the web app runs for the orchestrator itself.
ROLES = {
    "routing": ("claude-sonnet-5.5", "gemini-3.7-flash", "low",
                "The routing plan is a short structured-output judgment over a long, cached team prompt."),
    "synthesis": ("Strategy and high-stakes decisions",),
}

# Each agent's usual work, which sets its model when the web app picks automatically. A single question to one agent
# uses this task type; in team mode the orchestrator names the task type for each assignment.
AGENT_TASK = {
    "orchestrator": "Strategy and high-stakes decisions",
    "chief-of-staff": "Planning, coordination and communication",
    "advisory-board": "Strategy and high-stakes decisions",
    "cto-principal-architect": "Architecture and technical design",
    "operations-finance-manager": "Strategy and high-stakes decisions",
    "agent-builder": "Architecture and technical design",
    "business-attorney": "Security, legal and compliance review",
    "cpa-bookkeeper": "Security, legal and compliance review",
    "insurance-risk-advisor": "Security, legal and compliance review",
    "quality-reviewer": "QA gates and fact-checks",
    "lean-six-sigma-lead": "Root-cause analysis and statistics",
    "process-data-analyst": "Root-cause analysis and statistics",
    "continuous-improvement-coordinator": "Planning, coordination and communication",
    "client-success-manager": "Client-facing documents",
    "business-development": "Client-facing documents",
    "partner-ecosystem-manager": "Planning, coordination and communication",
    "market-research-analyst": "Research and analysis",
    "senior-agent-engineer": "Software and automation build",
    "platform-devops-engineer": "Infrastructure and production changes",
    "ai-solutions-engineer": "Research and analysis",
    "security-compliance": "Security, legal and compliance review",
    "data-engineer": "Software and automation build",
    "delivery-lead": "Planning, coordination and communication",
    "software-engineering-lead": "Software and automation build",
    "software-solutions-architect": "Architecture and technical design",
    "business-analyst": "Research and analysis",
    "ux-ui-designer": "Long-form content and training",
    "full-stack-developer": "Software and automation build",
    "backend-api-engineer": "Software and automation build",
    "mobile-developer": "Software and automation build",
    "qa-test-automation-engineer": "QA gates and fact-checks",
    "technical-writer": "Long-form content and training",
    "marketing-director": "Planning, coordination and communication",
    "content-marketing": "Long-form content and training",
    "web-developer-designer": "Software and automation build",
    "social-media-manager": "Short-form and high-volume content",
    "youtube-producer": "Long-form content and training",
    "video-editor": "Short-form and high-volume content",
    "graphic-designer": "Short-form and high-volume content",
    "community-manager": "Short-form and high-volume content",
    "seo-specialist": "Research and analysis",
    "paid-ads-specialist": "Short-form and high-volume content",
    "podcast-webinar-producer": "Long-form content and training",
    "marketing-analyst": "Root-cause analysis and statistics",
    "operations-coordinator": "Routine operations",
    "trainer-curriculum": "Long-form content and training",
    "product-manager": "Planning, coordination and communication",
    "talent-people-partner": "Client-facing documents",
    "gis-remote-sensing-analyst": "Research and analysis",
    "utility-industry-advisor": "Research and analysis",
}

SOURCES = [
    ("OpenRouter model list (prices, context, parameters)", "https://openrouter.ai/api/v1/models"),
    ("OpenRouter benchmarks: GPQA Diamond", "https://openrouter.ai/benchmarks/gpqa-diamond"),
    ("OpenRouter benchmarks: tau2-Bench Airline", "https://openrouter.ai/benchmarks/tau2-bench-airline"),
    ("Benchmark leaderboard export, snapshot 2026-11-25 (CC BY 4.0)", "https://openrouter.ai/api/v1/datasets/exports/benchmark-leaderboard/2026-11-25.json"),
    ("OpenRouter zero-data-retention endpoints (each catalog model has one that supports structured outputs)", "https://openrouter.ai/api/v1/endpoints/zdr"),
    ("OpenRouter API: provider routing and zero data retention", "https://openrouter.ai/docs/guides/routing/provider-selection.md"),
    ("OpenRouter API: structured outputs", "https://openrouter.ai/docs/guides/features/structured-outputs.md"),
    ("OpenRouter API: reasoning effort", "https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.md"),
]
