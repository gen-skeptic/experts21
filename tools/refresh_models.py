#!/usr/bin/env python3
"""Re-rank models for the catalog in tools/models.py from OpenRouter's live data. Read-only: prints, changes nothing.

    python3 tools/refresh_models.py

Downloads OpenRouter's model list, its zero-data-retention endpoint list and today's benchmark leaderboard export
(CC BY 4.0, "Source: OpenRouter (openrouter.ai)"), joins them, and for each quality tier in tools/models.py prints the
models that meet the floor, support structured outputs, have a zero-data-retention endpoint that supports them, and
answered a GPQA task in 120 seconds or less, cheapest first (cost per GPQA task plus cost per tau2 task). Update MODELS
and TASK_MODELS in tools/models.py from it, then run python3 tools/build.py.
"""
import collections
import datetime
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from models import TIERS  # noqa: E402

MODELS_URL = "https://openrouter.ai/api/v1/models"
ZDR_URL = "https://openrouter.ai/api/v1/endpoints/zdr"
EXPORT_URL = "https://openrouter.ai/api/v1/datasets/exports/benchmark-leaderboard/{day}.json"
MAX_SECONDS = 120


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "experts21-refresh"}), timeout=60) as r:
        return json.load(r)


def leaderboard():
    for back in range(0, 4):
        day = (datetime.date.today() - datetime.timedelta(days=back)).isoformat()
        try:
            return day, fetch(EXPORT_URL.format(day=day))["rows"]
        except Exception:  # noqa: BLE001 - try the previous day's snapshot
            continue
    raise SystemExit("no benchmark export found for the last four days")


def main():
    models = {m["id"]: m for m in fetch(MODELS_URL)["data"]}
    zdr = {e["model_id"] for e in fetch(ZDR_URL)["data"] if "structured_outputs" in (e.get("supported_parameters") or [])}
    day, rows = leaderboard()
    best = collections.defaultdict(dict)
    for r in rows:
        prev = best[r["model_slug"]].get(r["benchmark"])
        if not prev or (r["total_questions"], r["accuracy"]) > (prev["total_questions"], prev["accuracy"]):
            best[r["model_slug"]][r["benchmark"]] = r
    candidates = []
    for slug, bench in best.items():
        m, g, t = models.get(slug), bench.get("gpqa_diamond"), bench.get("tau_bench_verified_airline")
        if not m or not g or not t or ":" in slug or "preview" in slug:
            continue
        if "structured_outputs" not in (m.get("supported_parameters") or []) or slug not in zdr:
            continue
        candidates.append(dict(slug=slug, gpqa=g["accuracy"], tau=t["accuracy"], cost=g["avg_cost_per_task_usd"] + t["avg_cost_per_task_usd"],
                               seconds=g["avg_duration_per_task_ms"] / 1000, price=(float(m["pricing"]["prompt"]) * 1e6, float(m["pricing"]["completion"]) * 1e6)))
    print(f"OpenRouter benchmark snapshot {day}; {len(candidates)} models with both benchmarks, structured outputs and a zero-data-retention endpoint.\n")
    for key, tier in TIERS.items():
        fit = [c for c in candidates if c["gpqa"] >= tier["gpqa"] and c["tau"] >= tier["tau"] and c["seconds"] <= MAX_SECONDS]
        fit.sort(key=lambda c: c["cost"] if key != "frontier" else -(c["gpqa"] + c["tau"]))
        print(f"{tier['label']} (GPQA >= {tier['gpqa']}, tau2 >= {tier['tau']}):")
        for c in fit[:6]:
            print(f"  {c['slug']:44s} GPQA {c['gpqa']:.3f}  tau2 {c['tau']:.3f}  ${c['cost']:.4f}/task pair  {c['seconds']:.0f}s  ${c['price'][0]:g}/${c['price'][1]:g} per M")
        print()


if __name__ == "__main__":
    main()
