---
name: contract-review
description: "Review a contract, client redline or template (MSA, SOW, NDA, DPA, BAA, partner, subcontractor or lease) clause by clause against the firm's standard positions: scope, payment, IP and ownership, liability cap, indemnity, warranty, insurance, data and security, termination and governing law. Rate each issue, propose fallback language, and mark it for review by a licensed Florida attorney."
---

# Contract review

*Legal, finance and people skill for the DIO expert team.* Review a contract or client redline clause by clause, rate each risk, propose fallback language and flag what a licensed attorney must see.

## When to use

Before signing anything, when a client sends redlines, and when drafting or updating a template.

## Standard positions (what we want)

| Clause | Our position | Walk-away |
| --- | --- | --- |
| Scope | Fixed deliverables with acceptance criteria; changes by written change order | Open-ended "and anything else needed" |
| Payment | 50% deposit on fixed-fee work; net 15–30; late fee | Net 90, or payment only on "satisfaction" |
| IP and ownership | Client owns deliverables on full payment; DIO keeps its pre-existing tools and know-how, licensed to the client | Assignment of all DIO IP, including tools and templates |
| Liability | Capped at fees paid in the last 12 months; no consequential damages | Unlimited liability |
| Indemnity | Mutual, limited to third-party claims from each party's own fault | One-way indemnity for anything |
| Warranty | Workmanship warranty: defects against the acceptance criteria, reported within the warranty period (default 30 days), fixed at no charge; no warranty of AI model behavior beyond the tested criteria | Guarantees of outcomes or accuracy |
| Insurance | E&O and cyber at amounts we actually carry | Limits we don't carry |
| Data and security | Client data stays in client systems; least-privilege access; breach notice duties both ways | Unlimited audit rights or data in our systems |
| Non-solicitation | Mutual, 12 months, employees only | Broad non-compete on our work |
| Termination | Either side with notice; paid for work done | No payment for work done |
| Law | Florida; Palm Beach County venue | Foreign venue without reason |

## Method

1. **Read the whole document** once before marking anything.
2. **Clause by clause**, compare with the positions above; quote the clause.
3. **Rate** each issue: high (could cost the business or breach a law), medium (unfavorable), low (wording).
4. **Propose** fallback language for every high and medium issue.
5. **Check fit** with how we actually work (support hours, no 24/7, the employer boundary) and with insurance (`risk-register`).
6. **List questions** for the licensed attorney.

## Output

An issue table (clause, quote, risk, why, proposed language), a plain-English summary, questions for outside counsel, and the recommendation: sign, sign with changes, or don't sign.

**Every output carries:** "Draft for review by a licensed Florida attorney. Not legal advice." High-risk items (litigation, a regulator, an employment conflict, a HIPAA breach) go to Erich and human counsel at once.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P25 Contract and legal review). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `business-attorney`
- **Starts when:** Any contract, client redline, policy or legal question
- **Done when:** Final document approved and filed; high-risk items reviewed by a licensed attorney.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `business-attorney` | Issue-spot and redline | Redline + issue list |
| 2 | Work | `insurance-risk-advisor` | Check insurance and indemnity alignment (contracts only) | Coverage notes |
| 3 | QA review | `quality-reviewer` | Check consistency with the SOW, pricing and policies (redline → step 1, coverage → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | **Approval: Erich** | Erich (Chairman) | Decide; send high-risk items to a licensed attorney | Decision record (approved / changes requested / stopped) |
| 5 | Work | `business-attorney`, `operations-coordinator` | Final version with a plain-English summary; file the signed copy | Final document |

## Used by

`business-attorney`, `insurance-risk-advisor`.
