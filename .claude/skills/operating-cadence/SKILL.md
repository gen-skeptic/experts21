---
name: operating-cadence
description: "Run the firm's operating rhythm: the weekly priorities memo, the monthly operating report to Erich and quarterly goals and planning. Use for status roll-ups, priorities, KPIs, monthly reviews and quarterly plans."
---

# Operating cadence

*Strategy and coordination skill for the DIO expert team.* Run the weekly priorities, the monthly report to the Chairman and quarterly planning.

## When to use

Every Monday (weekly priorities), the first week of each month (report to the Chairman), and the last two weeks of each quarter (quarterly plan). Also when Erich asks "where do we stand?".

## Read first

- `docs/12-90-day-plan-and-open-questions.md` (current plan), `docs/06-startup-and-operating-costs.md` (revenue scenarios and the full-time trigger), `docs/10-operations-and-delivery.md` (capacity).

## Method

**Weekly (15 minutes to read):**
1. KPI snapshot: pipeline value and next steps, monthly recurring revenue, cash, billable hours used against the 10–12 hour weekly budget, overdue invoices.
2. Delivery status: each engagement green, amber or red, with the one blocker that matters.
3. The top three outcomes for the week, each with one owner.
4. Open decisions, marking the ones with financial or ethical considerations for Erich.
5. One improvement for the week (from a kaizen card or a recent miss).

**Monthly (the report to the Chairman):**
1. A one-paragraph letter: how the month went, honestly.
2. Revenue, costs, cash and pipeline against the plan; the full-time trigger (retainer MRR of $8–10K for three months, six months of reserve, two signed builds) and how far away it is.
3. Delivery and quality: projects, QA first-pass rate, incidents, client feedback.
4. Risks that changed, and decisions needed from Erich, each with options and a recommendation.

**Quarterly:**
1. Review last quarter's goals: met, missed, why.
2. Set three to five goals for next quarter, each measurable, with an owner.
3. Budget for the quarter, the hiring trigger check, and what to stop doing.
4. Team pulse: what's working, what isn't (for people and for the agents).

## Output

A memo with the sections above, in that order, under one page for the weekly version. Status words are exact: green, amber, red.

## Quality checks

- Every number has a source and date; no decorative metrics.
- Every priority has an owner; every decision names who decides.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P01 Weekly operating cadence). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `orchestrator`
- **Starts when:** Every Monday
- **Done when:** Priorities decided, financial or ethical items decided by Erich, task cards issued, decisions recorded, memo shared at the weekly line-up.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `operations-finance-manager` | Compile the KPI snapshot: pipeline, MRR, cash, utilization, AR aging | KPI snapshot |
| 2 | Work | `delivery-lead` | Roll up project status (green/amber/red), risks and blockers | Delivery status roll-up |
| 3 | Work | `marketing-director` | Summarize marketing results and pipeline sources | Marketing snapshot |
| 4 | Work | `chief-of-staff` | Draft the weekly priorities memo: top 3 outcomes, open decisions (marking any with financial or ethical considerations), delegation briefs, and one improvement for the weekly line-up | Priorities memo draft |
| 5 | QA review | `quality-reviewer` | Check figures against their sources and priorities against the quarterly plan (memo → step 4, KPI snapshot → step 1, status → step 2, marketing snapshot → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Decision | `orchestrator` | Decide the priorities and every open decision without financial or ethical considerations | Decision record |
| 7 | **Approval: Erich** | Erich (Chairman) | Decide the financial or ethical items in the memo (skip when there are none) | Decision record (approved / changes requested / stopped) |
| 8 | Work | `orchestrator` | Delegate: issue task cards to each owner, record the decisions, and share the memo at the weekly line-up | Task cards + decision records |

## Used by

`orchestrator`, `chief-of-staff`, `operations-coordinator`, `delivery-lead`, `operations-finance-manager`, `continuous-improvement-coordinator`.
