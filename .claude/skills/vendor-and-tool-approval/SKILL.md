---
name: vendor-and-tool-approval
description: "Evaluate a new tool, SaaS vendor, AI model or provider before the firm or a client relies on it: the need, total cost, security and data terms (training on data, retention, BAA), license limits, lock-in and the exit path, then record an approval with conditions. Use before buying, subscribing or putting client data into any new tool."
---

# Vendor and tool approval

*Legal, finance and people skill for the DIO expert team.* Evaluate and approve a tool, vendor or AI model: need, cost, security, data terms, license, lock-in and exit.

## When to use

Before the firm adopts a new tool or model provider, before recommending one to a client, and when a vendor changes its terms or prices.

## Method

1. **Need:** the problem, and whether an approved tool already solves it.
2. **Cost:** monthly and yearly, per seat or per token, at today's and next year's volume; pass-through to clients at cost.
3. **Security:** SSO and MFA, encryption, incident history, certifications (SOC 2, ISO 27001) where relevant.
4. **Data terms:** does the vendor train on our or clients' data? Retention and deletion? Where is data stored? Will it sign a BAA or DPA if needed?
5. **License:** what the license allows (for example Open Brain and OpsBrain are FSL-1.1-MIT: internal use and client-owned deployments, never a competing product or hosted service).
6. **Lock-in and exit:** data export, open formats, and the cost of leaving.
7. **Fallback:** for AI models, a second provider or model the design can switch to.
8. **Decide:** approved, approved with conditions, or rejected; Erich approves anything that costs money.

## Output

A one-page evaluation and the approval record with conditions and a review date.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P42 Tool, vendor and AI model approval). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `security-compliance`
- **Starts when:** Someone wants a new tool, SaaS service, AI model or API provider, or subprocessor
- **Done when:** Tool approved or declined, recorded in the tool register and subprocessor list.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `operations-coordinator` | Log the request: need, cost, and what data the tool would touch | Tool request |
| 2 | Work | `security-compliance` | Vendor review: data handling, retention, training on customer data, location, SSO and MFA | Vendor review |
| 3 | Work | `operations-finance-manager` | Cost and alternatives | Cost note |
| 4 | QA review | `quality-reviewer` | Check the review and cost note (security → step 2, cost → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Decision | `orchestrator` | Decide free tools that touch no client data; paid tools and tools that touch client data go to Erich | Decision record |
| 6 | **Approval: Erich** | Erich (Chairman) | Approve paid tools and tools that touch client data (skip otherwise) | Decision record (approved / changes requested / stopped) |
| 7 | Work | `operations-coordinator` | Add the tool to the tool register and subscription tracker; `security-compliance` adds it to the subprocessor list | Updated registers |

## Used by

`operations-coordinator`, `security-compliance`, `cto-principal-architect`, `operations-finance-manager`.
