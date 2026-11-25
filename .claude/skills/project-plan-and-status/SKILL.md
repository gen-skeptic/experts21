---
name: project-plan-and-status
description: "Plan and run an engagement: milestones and dependencies, a RAID log (risks, assumptions, issues, decisions), weekly one-line status (green, amber, red), change requests with impact and a written approval, and closeout with a retrospective and handover. Use for every engagement from kickoff to closeout."
---

# Project plan and status

*Software delivery skill for the DIO expert team.* Plan and run an engagement: plan, risks and issues log, weekly status, change requests and closeout.

## When to use

Every engagement, from kickoff to closeout.

## Method

1. **Plan:** milestones from the SOW deliverables, owners, dependencies (especially the client's), and buffer. Weekly demos on the calendar.
2. **RAID log:** risks (with likelihood, impact and response), assumptions, issues (with owner and due date) and decisions.
3. **Weekly status:** one line first ("Green: intake agent in staging, client testing Thursday"), then progress, next week, risks and help needed.
4. **Change requests:** anything outside the SOW: describe it, estimate effort and cost (`pricing-and-estimating`), the effect on schedule, and get written approval before work starts. Erich approves anything with a price.
5. **Watch scope and margin:** compare hours used with the estimate every week; raise amber early.
6. **Closeout:** acceptance signed, final invoice, handover (runbook, training, access returned or transferred), a retrospective (what went well, what to change, planned against actual), a kaizen card for anything systemic, and the 30-day check-in booked (`account-review`).

## Output

The plan, the RAID log, weekly status notes, change request records and the closeout report.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P29 Change request). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `delivery-lead`
- **Starts when:** Client asks for anything outside the SOW
- **Done when:** Signed change order and updated plan, or the request declined in writing.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `client-success-manager` | Log the request in the client's words | Change request log |
| 2 | Work | `delivery-lead`, `software-engineering-lead`, `senior-agent-engineer`, `platform-devops-engineer`, `lean-six-sigma-lead` | Analyze impact on scope, cost, schedule and risk (by service line) | Impact analysis |
| 3 | Work | `business-development` | Price the change order | Change order draft |
| 4 | QA review | `quality-reviewer` | Check impact analysis, pricing math and wording (impact → step 2, price → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | **Approval: Erich** | Erich (Chairman) | Approve the change order | Decision record (approved / changes requested / stopped) |
| 6 | Work | `client-success-manager` | Get the client's signature; `delivery-lead` updates the plan and backlog | Signed change order |

## Used by

`chief-of-staff`, `delivery-lead`, `software-engineering-lead`.
