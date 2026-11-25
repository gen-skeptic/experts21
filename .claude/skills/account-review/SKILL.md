---
name: account-review
description: "Run a client account review: the 30-day check-in after handover, the quarterly business review (QBR) for retainers, client feedback, account health score, renewal risk and expansion ideas. Use for check-ins, QBRs, renewals and at-risk clients."
---

# Account review

*Sales and clients skill for the DIO expert team.* Run 30-day check-ins and quarterly business reviews: results against the baseline, health score, risks, renewal and expansion.

## When to use

30 days after every handover, every quarter for retainer clients, before every renewal, and whenever a client seems unhappy.

## Method

1. **Results against the baseline** set at onboarding: hours saved, errors avoided, turnaround time, with the measurement method.
2. **Health score (1–5 each):** results, relationship (are they responsive, do they refer?), adoption (are people using it?), support load, payment.
3. **Listen:** ask what is working, what isn't, what they'd change, and how likely they are to recommend us (0–10). Read the tone, not just the words.
4. **Risks:** a champion leaving, unused features, rising support tickets, late payments, a competitor in the room.
5. **Next steps:** fixes we owe them (warranty items first), improvements, and expansion ideas only where they solve a real problem.
6. **Ask** for a referral, a testimonial or a case study only when the results are real; record their permission.

## Output

A one-page QBR or check-in summary: results, health score, what they said, risks, actions with owners and dates, and the renewal recommendation.

## Quality checks

- Results use the same measure as the baseline; no rounding up.
- Warranty fixes are scheduled before any upsell.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P27 Quarterly business review, renewal and expansion). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `client-success-manager`
- **Starts when:** Quarterly for retainer clients; 60 days before renewal
- **Done when:** QBR held, renewal decided, expansion opportunities passed to sales.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `client-success-manager` | Collect usage, incidents, support requests, changes and feedback results (`account-review`) | QBR data |
| 2 | Work | `ai-solutions-engineer`, `process-data-analyst` | Measure ROI or control-plan results against the baseline (AI and software: AI solutions engineer; process improvement: process data analyst) | ROI measurement |
| 3 | Work | `client-success-manager` | Draft the QBR deck, health score and renewal or expansion recommendations | QBR deck draft |
| 4 | QA review | `quality-reviewer` | Check numbers, ROI method and claims (measurement → step 2, deck → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | **Approval: Erich** | Erich (Chairman) | Approve renewal pricing or any commercial offer in the QBR (skip when there is none) | Decision record (approved / changes requested / stopped) |
| 6 | Work | `client-success-manager` | Run the QBR; expansion → a new CRM deal and `proposal-and-sow` step 10; testimonial or case study → `long-form-content` | QBR record |

## Used by

`client-success-manager`.
