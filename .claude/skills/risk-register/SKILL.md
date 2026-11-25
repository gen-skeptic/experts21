---
name: risk-register
description: "Build and review the firm's risk register: identify business, legal, security, delivery, vendor and personal risks, rate likelihood and impact, assign owners and mitigations, map each to insurance coverage or contract terms, and review every quarter. Use for quarterly risk reviews, insurance decisions and before big commitments."
---

# Risk register

*Legal, finance and people skill for the DIO expert team.* Keep the risk register: likelihood, impact, owner and mitigation for each risk, mapped to insurance and reviewed quarterly.

## When to use

Every quarter, before buying or renewing insurance, before a large contract, and after any incident.

## Read first

- `docs/11-risks.md` (the current risks and mitigations), `docs/06-startup-and-operating-costs.md` (insurance costs).

## Method

1. **Identify** risks in each area: legal and contract, security and data, delivery, vendor and model, people (founder availability, hurricane season), money, reputation, regulation, the employer boundary.
2. **Rate** likelihood and impact 1–5; score = likelihood × impact.
3. **Mitigate:** avoid, reduce, transfer (insurance, contract terms) or accept. Every risk scoring 12 or more needs a mitigation and an owner.
4. **Insurance map:** which policy covers it (technology E&O, cyber, general liability), the limit, the deductible, and gaps against what contracts require.
5. **Review:** what changed since last quarter, which mitigations worked, new risks.

## Output

```markdown
| Risk | Area | L | I | Score | Mitigation | Insurance / contract | Owner | Status |
```

Plus a short summary of the top five risks and any coverage gaps. Anything accepting financial risk goes to Erich.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P26 Quarterly risk and compliance review). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `insurance-risk-advisor`
- **Starts when:** Quarterly
- **Done when:** Risk register, policies and coverage updated; actions owned and tracked.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `insurance-risk-advisor` | Update the risk register | Risk register |
| 2 | Work | `security-compliance` | Review controls; update policies | Control review |
| 3 | Work | `business-attorney`, `market-research-analyst` | Summarize regulatory changes (Florida AI and privacy law, federal) | Regulatory update |
| 4 | Work | `operations-finance-manager` | Review insurance renewals and costs | Coverage cost note |
| 5 | QA review | `quality-reviewer` | Check completeness and that every risk has an owner and mitigation (register → step 1, controls → step 2, regulatory → step 3, costs → step 4) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Decision | `orchestrator` | Decide the actions; insurance purchases and accepting a risk go to Erich | Decision record |
| 7 | **Approval: Erich** | Erich (Chairman) | Approve insurance purchases and any risk acceptance (skip when none) | Decision record (approved / changes requested / stopped) |
| 8 | Work | `chief-of-staff` | Issue task cards for the actions | Task cards |

## Used by

`insurance-risk-advisor`, `operations-finance-manager`.
