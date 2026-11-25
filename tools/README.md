# tools/

The expert team is data. These files define it, and `build.py` turns them into the files Claude Code reads.

| File | What it holds |
| --- | --- |
| [`team.py`](team.py) | Every agent: id, role, group, one-line job, description (when to use it), mission, responsibilities, deliverables, boundaries, tools, skills, reporting line, Star Trek persona, brain and knowledge folder contents |
| [`skills.py`](skills.py) | The list of skill categories; it gathers the skills from the files below |
| `skills_strategy.py`, `skills_delivery.py`, `skills_business.py`, `skills_marketing.py` | Each skill's title, one-line summary, description (when to use it) and method |
| [`workflows.py`](workflows.py) | Who does each step of the team workflows shown at the end of the process skills |
| [`brains.py`](brains.py) | The four brains (model families) and the work task types that pick one |
| [`models.py`](models.py) | The model catalog: the most cost-efficient model per task type across Claude and OpenRouter, each model's IDs, prices and benchmark scores, and each agent's usual task type |
| [`refresh_models.py`](refresh_models.py) | Read-only: downloads OpenRouter's live model list and benchmark data and prints the ranking per tier, to update `models.py` every quarter |
| [`build.py`](build.py) | The generator and its check |
| [`export_skill.py`](export_skill.py) | Packages one agent as a standalone Claude skill zip in `exports/` |

## Build

```bash
python3 tools/build.py
```

```bash
python3 tools/build.py --check
```

The build writes `.claude/agents/<agent>.md`, `.claude/skills/<skill>/SKILL.md`, `docs/expert-roster.md`, `docs/agent-brains.md`, `docs/model-catalog.md` and `docs/model-catalog.json`, `knowledge/README.md` and each `knowledge/<agent>/README.md`, and the team table in `CLAUDE.md`, and removes agent or skill files that are no longer defined. `--check` fails if any of them is missing, stale or edited by hand. It needs only Python 3 (standard library).

## Where the data came from

`team.py`, `workflows.py` and `brains.py` were converted on November 25, 2026 from the DIO operating manual in gen-skeptic/experts (`tools/agents_data.py`, `tools/team_data.py` and `tools/processes_data.py`): the `dio-` prefix was dropped, `dio-ceo` became `orchestrator`, process numbers were replaced by the skills that carry the same methods, and `agent-builder` was added. The skills were written for this repository from those processes and the research in `docs/`.
