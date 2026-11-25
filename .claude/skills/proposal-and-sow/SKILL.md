---
name: proposal-and-sow
description: "Write a proposal and statement of work (SOW): the client's problem in their words, the fix-first approach, fixed scope and exclusions, deliverables with acceptance criteria, timeline, fixed fee and payment terms, warranty, support hours and who owns what. Use after a qualified fit call or for any change of scope."
---

# Proposal and SOW

*Sales and clients skill for the DIO expert team.* Write a fixed-fee proposal and statement of work with scope, acceptance criteria, warranty, support terms and payment.

## When to use

After a qualified fit call, to quote a new engagement, a renewal or an expansion. Change requests on a live engagement use the same structure.

## Read first

- `docs/05-services-and-pricing.md` (rate card, value ladder), `docs/10-operations-and-delivery.md` (standard artifacts), `docs/07-permits-and-licenses.md` (rules that apply to the work).

## Method

1. **Problem** in the client's own words, and what it costs them today (hours, errors, delay).
2. **Approach:** fix first, then automate. Include the readiness check unless a recent assessment or health check already covered the process.
3. **Scope:** in-scope items, explicit exclusions, assumptions, and what the client provides (access, people's time, data).
4. **Deliverables with acceptance criteria:** each one testable ("intake agent drafts a summary for 95% of test cases in the evaluation set; staff approve before anything is sent").
5. **Timeline** in weeks, with the client's dependencies marked.
6. **Fee:** fixed, from the rate card (`pricing-and-estimating`). 50% deposit for fixed-fee work; model and tool costs passed through at cost with a monthly estimate.
7. **Standard terms:** the client owns the code, accounts and data; the workmanship warranty (defects against the acceptance criteria reported within the warranty period, default 30 days after acceptance, fixed at no charge; excludes new features, third-party changes and AI model behavior beyond the tested acceptance criteria); support hours and response targets, never 24/7; change orders in writing; Florida law.
8. **Every build ships with** tests, a runbook, an access matrix and a recovery procedure, in the client's own repository and accounts.
9. **Next step:** how to accept, and the start date.

## Output

A proposal of two to four pages plus an SOW with numbered deliverables and acceptance criteria. Pricing and legal terms go through `quality-reviewer` and `business-attorney` before sending; **Erich approves every price and signs.**

## Quality checks

- Prices match the rate card; the math adds up; the deposit and payment dates are clear.
- Nothing promises outcomes the acceptance criteria don't measure.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P02 Lead to proposal). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `business-development`
- **Starts when:** Outbound: a new target segment (start at step 1). Inbound lead, referral or marketplace inquiry: start at step 5
- **Done when:** Proposal sent (or lead closed with a reason), with the CRM deal showing the outcome; won deals start `client-onboarding`, lost deals get a win/loss note.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `market-research-analyst` | Research the vertical and target companies (outbound only) | Prospect research brief |
| 2 | Work | `business-development` | Build the prospect list in the CRM (company, contacts with their consent status, a deal at Prospect) and personalized outreach drafts. Exclude utilities, vegetation-management and line-clearance contractors, and any company you know to be an FPL/NextEra vendor | Prospect list + outreach drafts |
| 3 | QA review | `quality-reviewer` | Check accuracy, personalization, CAN-SPAM and platform rules, brand voice, employer boundary | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | Work | `business-development` | Send the outreach that passed QA, log each touch as a CRM activity, and book fit calls (deal to Fit call) | Sent outreach |
| 5 | Work | `business-development` | For every booked call, outbound or inbound: research the company and write the fit-call brief | Fit-call brief |
| 6 | Erich does it | Erich (Chairman) | Hold the fit call | Call notes |
| 7 | Work | `business-development` | Qualify: budget, authority, need, timing, data sensitivity. Flag any field-services, tree-care or utility-adjacent prospect for Erich's employer-boundary screen (flag the company in the CRM; its deal can't reach Scoping until he clears it). Close unfit leads politely (deal to Lost, with the reason) | Qualification record |
| 8 | **Approval: Erich** | Erich (Chairman) | Employer-boundary screen for flagged prospects, cleared or declined in the CRM: decline when unsure (skip for prospects that weren't flagged) | Decision record (approved / changes requested / stopped) |
| 9 | Work | `delivery-lead` | Capacity check: can DIO start within the promised window under the WIP limits? If not, propose a later start date | Capacity note |
| 10 | Work | `ai-solutions-engineer`, `software-solutions-architect`, `platform-devops-engineer`, `lean-six-sigma-lead`, `security-compliance`, `trainer-curriculum` | Scope and estimate by service line: A and B AI solutions engineer; G software architect; C DevOps; H and every fix-first readiness check Lean Six Sigma lead; audits security; F trainer. Every B or G estimate includes the `process-health-check` readiness check unless a `readiness-assessment` or `process-health-check` covered the process in the last 6 months | Technical scope + estimate |
| 11 | Work | `business-development` | Write the proposal and SOW from the rate card, within 2 business days of the estimate (tell the prospect if it will take longer) | Proposal + SOW draft |
| 12 | Work | `business-attorney` | Check contract terms, SOW language and the warranty clause | Legal issue list |
| 13 | QA review | `quality-reviewer` | Check pricing math, scope clarity, assumptions and claims (proposal → step 11, estimate → step 10, contract terms → step 12) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 14 | **Approval: Erich** | Erich (Chairman) | Approve price and scope | Decision record (approved / changes requested / stopped) |
| 15 | Work | `business-development` | Send the proposal and follow up (deal to Proposal sent; log every touch). Client redlines go through `contract-review` (deal to Redlines). When the SOW is signed, Erich marks the deal won in the CRM (only he can) and that starts `client-onboarding`; a loss gets its lost reason and a win/loss note shared with `marketing-analyst` | Sent proposal + outcome |

## Used by

`business-attorney`, `business-development`.
