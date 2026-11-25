---
name: managed-operations
description: "Run the monthly managed operations cycle for retainer clients (Line D, $750–$4,500 a month) and Software Care (15–20% of build cost a year): monitoring review, patching, agent tuning and evaluation reruns, backups and restore tests, support requests, cost review and the monthly report. Use for every retainer and support request."
---

# Managed operations

*AI and platform delivery skill for the DIO expert team.* Run the monthly retainer cycle for agents, platforms and Software Care: monitor, patch, tune, support and report.

## When to use

Every month for each retainer and Software Care client, and whenever a support request comes in.

## Monthly cycle

1. **Health review:** uptime, errors, alerts, agent success and review rates, latency, costs against the estimate.
2. **Patch and update:** dependencies, base images, platform versions, model versions; test on staging first.
3. **Agent tuning:** rerun the evaluation set; investigate drops; adjust prompts or tools with a reviewed change; never relax human review without evidence.
4. **Backups:** confirm they ran; do a restore test at least each quarter.
5. **Access review:** remove accounts no longer needed.
6. **Support requests:** log each one, answer within the SOW's response targets, fix standard changes under the standing approval, and quote anything bigger as a change order.
7. **Monthly report:** what we did, what we saw, costs, recommendations, and what's next. Short, honest, in plain words.

## Quality checks

- Support hours and response targets match the SOW; no 24/7 promises.
- Every change follows the release process.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P37 Support request). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `client-success-manager`
- **Starts when:** A client question, bug report or request that is not an incident (incidents follow `incident-response`)
- **Done when:** Request answered or fixed, client told, recurring causes sent to `continuous-improvement`.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `client-success-manager` | Log the request with the engagement ID and acknowledge it within the SOW response target | Support record |
| 2 | Work | `delivery-lead` | Triage: incident → `incident-response`; out of scope → `project-plan-and-status` (any charge goes through Erich there); defect under warranty or Software Care, or a how-to question → step 3 | Triage decision |
| 3 | Work | `platform-devops-engineer`, `senior-agent-engineer`, `full-stack-developer`, `backend-api-engineer`, `technical-writer` | Resolve by area: answer the question, or fix the defect in staging. Code fixes release through `release-and-deployment` | Answer or fix |
| 4 | QA review | `qa-test-automation-engineer` | Verify the fix in staging (skip for answers) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | QA review | `quality-reviewer` | Check the reply and resolution summary | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Work | `client-success-manager` | Reply to the client, close the request and ask the one-question satisfaction check (feeds `account-review`) | Closed request |
| 7 | Work | `delivery-lead` | Send recurring issues as kaizen cards to `continuous-improvement` | Kaizen cards |

## Used by

`platform-devops-engineer`, `client-success-manager`.
