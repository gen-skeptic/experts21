---
name: process-health-check
description: "Run a process health check (the fix-first readiness check): SIPOC, interviews and direct observation, a current-state map, baseline metrics, the eight wastes and a readiness verdict of ready, fix first or redesign. Use before any automation or software is designed for a process."
---

# Process health check

*Process improvement skill for the DIO expert team.* Map, measure and judge a process before anyone automates it: SIPOC, current-state map, baseline, waste and a readiness verdict.

## When to use

Before any agent workflow or software is designed around a client's process, and as a paid offer on its own ($2,500–$5,000). If a process hasn't passed this check, nothing gets automated.

## Method

1. **SIPOC:** suppliers, inputs, process (5–7 high-level steps), outputs, customers. Agree the start and end of the process.
2. **Go and see:** interview the people who do the work and watch it done at least twice. Collect real examples (with client data kept in client systems).
3. **Current-state map:** a swimlane map of every step, handoff, wait and rework loop, in the client's own words.
4. **Baseline metrics:** volume per week, lead time, touch time, error or rework rate, and how each was measured. A rough honest baseline beats none.
5. **Waste walk:** mark the eight wastes (defects, overproduction, waiting, unused talent, transport, inventory, motion, extra processing).
6. **Root causes** of the biggest problems with 5 whys (and a fishbone when causes are tangled).
7. **Verdict:**
   - **Ready:** stable, documented, measured; automate it.
   - **Fix first:** fixable problems; run a Kaizen event (`kaizen-event`) or quick fixes, then recheck.
   - **Redesign:** broken or unstable; run a DMAIC project (`dmaic-project`).

## Output

A health-check report: SIPOC, current-state map, baseline table, waste and root causes, the verdict with reasons, and the recommended next step and price.

## Quality checks

- The map was checked by the people who do the work.
- The baseline states its measurement method and sample size.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P33 Process Health Check and fix-first readiness). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `lean-six-sigma-lead`
- **Starts when:** Before any agent or software build (gate in `governed-agent-design` and `software-build-standards`), or sold standalone
- **Done when:** Readiness verdict delivered: ready to automate, fix first with quick wins (`kaizen-event`), or fix first with DMAIC (`dmaic-project`).

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `lean-six-sigma-lead` | Scope with the process owner: SIPOC, customers and what they value; prepare the interview guide and observation plan | SIPOC + plan |
| 2 | Erich does it | Erich (Chairman) | Interview the process owner and staff and observe the work (go and see); keep notes and recordings with consent | Interview and observation notes |
| 3 | Work | `business-analyst` | Map the current state from the notes and recordings (value stream or swimlane map) | Current-state map |
| 4 | Work | `process-data-analyst` | Baseline: lead time, cycle time, volume, error and rework rates, cost per transaction; check the data can be trusted | Baseline metrics |
| 5 | QA review | `lean-six-sigma-lead` | Check the baseline: data validity, operational definitions, sample sizes | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Work | `lean-six-sigma-lead` | Waste analysis (the 8 wastes), bottlenecks, root-cause hypotheses; verdict: ready / fix first (quick wins) / fix first (DMAIC) | Health check report draft |
| 7 | QA review | `process-data-analyst` | Check that every conclusion follows from the data | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (report → step 6, map → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 9 | Work | `client-success-manager` | Readout for standalone checks, or hand the verdict to the waiting build; route: ready → `governed-agent-design`/`software-build-standards`, quick wins → `kaizen-event`, complex → `dmaic-project` (new work is priced in `proposal-and-sow` step 10) | Readout record |

## Used by

`ai-solutions-engineer`, `business-analyst`, `lean-six-sigma-lead`, `process-data-analyst`.
