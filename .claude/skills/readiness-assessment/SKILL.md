---
name: readiness-assessment
description: "Run the AI Operations Readiness Assessment (Line A): interviews and workflow mapping, an inventory of systems and data, opportunity scoring by value, feasibility and risk, a governance baseline (access, data, review, recovery), what not to automate, and a 90-day roadmap with prices. Use as the entry engagement for any new client."
---

# AI readiness assessment

*AI and platform delivery skill for the DIO expert team.* Assess a client's AI readiness: map workflows, score automation opportunities, set a governance baseline and a 90-day roadmap.

## When to use

The first paid engagement with most clients ($2,500–$4,500, credited toward a build), in person or remote.

## Read first

- `docs/05-services-and-pricing.md` (Line A), `docs/03-target-customers.md` (pains by segment).

## Method

1. **Intake questionnaire** (async): goals, team, systems, data types, current AI use, compliance constraints.
2. **Interviews** (3–6 people, 45 minutes each): what fills their week, where work waits or repeats.
3. **Workflow inventory:** list the top 10–15 workflows with volume, time per item, error rate and the systems they touch.
4. **Systems and data map:** each system, who owns the account, API or export available, data sensitivity (public, internal, confidential, regulated).
5. **Score every opportunity** 1–5 on value (hours and errors saved), feasibility (data and API access, process stability), and risk (data sensitivity, harm if wrong). Rank by value × feasibility ÷ risk.
6. **Fix-first filter:** any process that isn't stable goes to a health check first (`process-health-check`).
7. **Governance baseline:** identity and access, shared passwords, where AI tools already touch data, logging, human review, backups and recovery. Score each red, amber or green.
8. **What not to automate:** say it plainly where off-the-shelf software, a checklist or no change at all is the better answer.
9. **Roadmap:** the first one to three workflows with fixed prices, the governance fixes, and a 90-day timeline.

## Output

A report (10–15 pages) and a recorded readout: summary, workflow inventory, opportunity scores, governance baseline, what not to automate, roadmap with prices.

## Quality checks

- Savings estimates show their math and are labeled *(est.)*.
- No recommendation needs data the client hasn't agreed to share.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P04 AI Operations Readiness Assessment (Line A)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `delivery-lead`
- **Starts when:** Kickoff of an assessment engagement
- **Done when:** Report with fix-first actions, 90-day roadmap and an approved quote delivered at a readout; next step decided.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `delivery-lead` | Schedule interviews and the process walk; send the pre-assessment questionnaire | Schedule |
| 2 | Work | `lean-six-sigma-lead`, `business-analyst` | Prepare the interview guide and the process walk plan | Interview guide |
| 3 | Erich does it | Erich (Chairman) | Interview the owner and staff and walk the process (go and see); keep notes, photos and recordings with consent | Interview and walk notes |
| 4 | Work | `business-analyst` | Write up the interviews and map the current-state processes | Process maps |
| 5 | Work | `ai-solutions-engineer` | Inventory systems and data; score opportunities by ROI and risk | Opportunity scorecard |
| 6 | Work | `security-compliance` | Assess the governance and access baseline | Governance findings |
| 7 | Work | `market-research-analyst` | Add industry benchmarks and regulation notes | Benchmark notes |
| 8 | Work | `lean-six-sigma-lead` | Waste analysis and process health check on the top opportunities (`process-health-check` method) from the walk notes and maps: what must be fixed before anything is automated | Fix-first findings |
| 9 | Work | `ai-solutions-engineer` | Draft the report: fix-first actions, 90-day roadmap and quoted first build | Report draft |
| 10 | QA review | `market-research-analyst` | Fact-check every number and external claim written by others; your own benchmarks are checked by `quality-reviewer` at step 11 | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (report → step 9, maps → step 4, benchmarks → step 7, fix-first findings → step 8) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 12 | **Approval: Erich** | Erich (Chairman) | Approve the quoted price in the report | Decision record (approved / changes requested / stopped) |
| 13 | Work | `client-success-manager` | Hold the readout; a build → `proposal-and-sow` step 10; fix first → `kaizen-event` or `dmaic-project` | Readout record |

## Used by

`ai-solutions-engineer`, `business-analyst`, `lean-six-sigma-lead`.
