---
name: continuous-improvement
description: "Run continuous improvement for the firm itself and for retainer clients: collect kaizen cards (problem, evidence, idea), trend QA FAILs and incidents, run the monthly plan-do-check-act cycle, and turn proven changes into the new standard, including changes to this repository's agents and skills. Use for any improvement idea or recurring problem."
---

# Continuous improvement

*Process improvement skill for the DIO expert team.* Run the firm's own improvement system: kaizen cards, monthly PDCA, standard work, and changes to agents and skills.

## When to use

Anyone, person or agent, spots a recurring problem or a better way; every month for the PDCA cycle; and for clients on a continuous-improvement retainer ($1,500–$4,000 a month).

## Method

1. **Kaizen card:** the problem, the evidence (examples, counts), and the idea. Anyone may send one at any time to `continuous-improvement-coordinator`.
2. **Trend monthly:** QA FAIL reasons, correction loops per item, incidents, support tickets, client feedback and the cards themselves.
3. **Plan:** pick one to three experiments with the biggest expected effect for the least effort; each has a hypothesis, a measure and an owner.
4. **Do:** run them for a set period.
5. **Check:** compare with the baseline (`statistical-analysis` when the numbers are noisy).
6. **Act:** standardize what worked (update the skill, the agent definition or the checklist), drop what didn't, and record both.
7. **Changes to this repository:** edit `tools/team.py` or `tools/skills.py`, run `python3 tools/build.py` and `--check`, have `quality-reviewer` review, then commit.
8. **Recognize** the people and agents whose cards led to changes.

## Output

The monthly improvement log: cards received, experiments run, results, standards changed, and next month's experiments.

## Quality checks

- Every standard change has evidence behind it.
- QA steps and correction loops are never removed to save time.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P45 Operating manual change (this repository)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `continuous-improvement-coordinator`
- **Starts when:** A standard change from `continuous-improvement`, a playbook update from `project-plan-and-status`, a plan update from `operating-cadence`, or any requested change to agents, processes, the README or the business plan
- **Done when:** Change built, checked, decided, committed and announced; the build check passes on main.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `continuous-improvement-coordinator` | Write down the change and its reason (kaizen card, decision record or request) | Change request |
| 2 | Work | `continuous-improvement-coordinator` | Edit the definitions in tools/ (never the generated agents/ or processes/ files), the README or the plan, then run ./tools/build.sh | Edited definitions + build output |
| 3 | QA review | `quality-reviewer` | Review the diff and build output: QA steps and correction loops intact, handoffs consistent, README in sync, wording clear | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | Decision | `orchestrator` | Decide the change; changes to pricing, approval rules or anything with financial or ethical considerations go to Erich | Decision record |
| 5 | **Approval: Erich** | Erich (Chairman) | Approve changes with financial or ethical considerations (skip otherwise) | Decision record (approved / changes requested / stopped) |
| 6 | Work | `continuous-improvement-coordinator` | Commit and push; the CI build check re-runs; add the change to the changelog and tell the affected agents and people | Committed change + changelog |

## Used by

`orchestrator`, `lean-six-sigma-lead`, `continuous-improvement-coordinator`.
