---
name: kaizen-event
description: "Plan and run a Kaizen rapid improvement event (2 to 5 days) with the client's team: charter, current state, waste, future state, quick experiments, standard work and a 30-day follow-up. Use when a process needs fixing before automation and the fixes are within the team's control."
---

# Kaizen event

*Process improvement skill for the DIO expert team.* Plan and run a 2–5 day rapid improvement event with the client's team, and hold the gains.

## When to use

A health check returned "fix first", the problem sits inside one team's control, and the team can give 2–5 days. Typical price $6,000–$15,000.

## Method

1. **Charter (a week before):** the problem, scope, goal (for example cut request turnaround from 5 days to 2), team members (the people who do the work plus a decision-maker), dates, and the baseline from the health check.
2. **Day 1, understand:** walk the process, validate the current-state map, measure, list the wastes.
3. **Day 2, design:** brainstorm fixes, sort them on an effort-impact grid, and draw the future-state map.
4. **Days 3–4, try:** run the quick fixes for real (new checklist, form, layout, handoff rule), measure, adjust.
5. **Last day, standardize:** write the standard work (step, who, how, how long), a visual control (board or dashboard), and a 30-day action list for what couldn't finish.
6. **Report out** to the owner: before and after, what changed, what's next.
7. **30-day follow-up:** measure again; if the gains held, the process can be automated.

## Output

Charter, before and after maps and metrics, standard work, the 30-day action list, and the follow-up result.

## Quality checks

- The client's team made the changes; we facilitated.
- Results are measured the same way as the baseline.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P35 Kaizen rapid improvement event (Line H)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `lean-six-sigma-lead`
- **Starts when:** Signed Kaizen SOW, or a `process-health-check` verdict of 'fix first (quick wins)'
- **Done when:** Changes implemented during the event, results measured, 30-day action list closed.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `lean-six-sigma-lead` | Charter the event: scope, target, team, schedule, pre-event data request | Event charter |
| 2 | Work | `process-data-analyst` | Pre-event baseline | Baseline |
| 3 | QA review | `quality-reviewer` | Check the charter and baseline are ready (charter → step 1, baseline → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | QA review | `client-success-manager` | Get the client's sign-off on the charter and schedule | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Work | `lean-six-sigma-lead`, `trainer-curriculum` | Facilitator plan and a short Lean basics module for participants | Facilitation plan |
| 6 | QA review | `quality-reviewer` | Check the facilitator plan and module | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 7 | Erich does it | Erich (Chairman) | Facilitate the event with the client team: current state, waste, future state, implement changes on the spot | Event outputs |
| 8 | Work | `lean-six-sigma-lead` | Report out: before/after, standard work, 30-day action list | Event report |
| 9 | QA review | `process-data-analyst` | Verify the before/after measurements | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 10 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | Work | `client-success-manager` | 30-day follow-up on open actions; automation candidates → `governed-agent-design`/`software-build-standards` | Follow-up record |

## Used by

`lean-six-sigma-lead`, `continuous-improvement-coordinator`.
