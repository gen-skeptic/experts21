---
name: dmaic-project
description: "Run a Lean Six Sigma DMAIC project: define the problem and charter, measure with a checked measurement system, analyze root causes with data, improve with tested changes, and control with a control plan and chart. Use for processes the health check marks redesign, or problems whose causes aren't obvious."
---

# DMAIC project

*Process improvement skill for the DIO expert team.* Run a Define-Measure-Analyze-Improve-Control project for a broken or unstable process, with data at every gate.

## When to use

A health check returned "redesign", or the causes of a problem are unclear and need data. Typical price $12,000–$40,000 over 6–12 weeks. Keep projects to Green Belt size until a Black Belt leads.

## Method

1. **Define:** problem statement (what, where, how big, since when, with no cause or solution in it), goal, scope, team, SIPOC, voice of the customer and critical-to-quality measures. Charter signed by the sponsor.
2. **Measure:** operational definitions for each metric, a data collection plan, a measurement system check (`statistical-analysis`), the baseline and process capability.
3. **Analyze:** process analysis (value-added versus waste), Pareto of defects, fishbone, then verify the top causes with data (hypothesis tests, regression). Only verified causes go forward.
4. **Improve:** generate and select solutions against the verified causes, pilot them, prove the improvement statistically, and do a quick FMEA on the new process.
5. **Control:** control plan (what is measured, how often, by whom, what to do when it drifts), a control chart, standard work and training, and handover to the process owner.
6. **Close:** before and after with confidence intervals, savings (signed off by the client), lessons learned.

## Output

The charter, measure and analysis findings, the pilot result, the control plan and chart, and the closeout report.

## Quality checks

- `process-data-analyst` checks every statistical claim.
- Savings are the client's numbers, not ours.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P34 DMAIC process improvement project (Line H)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `lean-six-sigma-lead`
- **Starts when:** Signed improvement SOW, or a `process-health-check` verdict of 'fix first (DMAIC)'
- **Done when:** Improvement proven against the baseline, controls in place and owned by the client, automation candidates identified.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `lean-six-sigma-lead` | Define: project charter (problem, goal, scope, critical-to-quality requirements, voice of the customer), SIPOC, stakeholders | Project charter |
| 2 | QA review | `quality-reviewer` | Charter check: measurable goal, clear scope, real customer requirements | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 3 | QA review | `client-success-manager` | Get the client's sign-off on the charter | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | Work | `process-data-analyst` | Measure: data collection plan, measurement system check, baseline and process capability | Measure report |
| 5 | QA review | `lean-six-sigma-lead` | Check data validity, sample sizes and operational definitions | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Work | `lean-six-sigma-lead` | Analyze: root causes with data (fishbone, 5 whys, Pareto, hypothesis tests or regression with `process-data-analyst`); root-cause sessions with the client team are led by Erich | Verified root causes |
| 7 | QA review | `quality-reviewer` | Root causes are proven with data, not opinion; people are not blamed for process failures | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | Work | `lean-six-sigma-lead` | Improve: design and pilot countermeasures with the client team (standard work, flow, error-proofing, policy). Automation only after the process itself is fixed | Pilot results |
| 9 | QA review | `process-data-analyst` | Compare pilot results to the baseline; confirm the improvement is real, not noise | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 10 | QA review | `client-success-manager` | Get the client's sign-off on the rollout | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | Work | `lean-six-sigma-lead` | Control: control plan, control charts, response plan, owner training | Control plan |
| 12 | Work | `technical-writer` | Write standard operating procedures and training materials | SOPs + training |
| 13 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (control plan → step 11, SOPs → step 12) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 14 | Work | `client-success-manager` | Hand over; automation candidates → `governed-agent-design`/`software-build-standards`; control checks in `continuous-improvement` or at the 30-day check-in (`account-review`); case study → `long-form-content` | Handover record |

## Used by

`lean-six-sigma-lead`, `process-data-analyst`.
