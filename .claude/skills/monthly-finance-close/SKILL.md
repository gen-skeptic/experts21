---
name: monthly-finance-close
description: "Run the monthly finance close and billing: categorize and reconcile transactions, send invoices (deposits, milestones, retainers), chase overdue payments politely and on schedule, review revenue, margin and cash against the plan, set aside taxes and prepare the business review. Use at each month end and for billing questions."
---

# Monthly finance close

*Legal, finance and people skill for the DIO expert team.* Close the books each month: reconcile, invoice, chase collections, review margins and set aside taxes.

## When to use

The first five business days of every month, and whenever an invoice is due or overdue.

## Method

1. **Reconcile:** every bank and card transaction categorized and matched to receipts; business and personal kept apart.
2. **Invoice:** deposits on signature, milestones on acceptance, retainers on the 1st, pass-through costs at cost with the provider's invoice attached.
3. **Collections:** a friendly reminder 3 days before due; on the due date; at 7 days late; at 15 days a call; at 30 days pause non-critical work (as the SOW allows) and tell Erich.
4. **Review:** revenue by service line, gross margin per engagement (hours used against the estimate), cash, AR aging, MRR and its change.
5. **Taxes:** set aside the agreed percentage; track estimated payment dates; note sales tax only if something taxable was sold.
6. **Business review:** a one-page summary for the operating cadence: numbers against plan, surprises, and decisions needed.

## Output

Closed books for the month, invoices sent, an AR aging list with actions, and the one-page business review.

## Quality checks

- Invoice math matches the SOW; numbers tie to the bank.
- **Every payment out and every refund or write-off is Erich's decision.**

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P24 Monthly finance close and business review). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `operations-finance-manager`
- **Starts when:** First business week of each month
- **Done when:** Books reconciled, financial actions approved, quarterly taxes approved and paid, monthly business review shared.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `cpa-bookkeeper` | Categorize, reconcile, AR aging | Reconciled books |
| 2 | Work | `operations-coordinator` | Hand overdue invoices to the collections steps in `monthly-finance-close` | Overdue list |
| 3 | Work | `operations-finance-manager` | P&L, margin by service line, cash forecast, KPI dashboard | Monthly finance pack |
| 4 | QA review | `quality-reviewer` | Math checks and tie-out to reconciled balances (books → step 1, reports → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | **Approval: Erich** | Erich (Chairman) | Review results and approve financial actions | Decision record (approved / changes requested / stopped) |
| 6 | Work | `cpa-bookkeeper` | Quarterly tax estimate (quarter-end months only) | Tax estimate |
| 7 | QA review | `quality-reviewer` | Check the tax estimate math against the books | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | **Approval: Erich** | Erich (Chairman) | Approve and pay estimated taxes (quarter-end months only) | Decision record (approved / changes requested / stopped) |
| 9 | Work | `chief-of-staff` | Monthly business review: finance, pipeline, delivery health, marketing, improvement metrics; share it at the weekly line-up | Monthly business review |

## Used by

`cpa-bookkeeper`, `operations-coordinator`, `operations-finance-manager`.
