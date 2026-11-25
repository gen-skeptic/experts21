---
name: qa-review
description: "Review any deliverable (advice, a proposal, code, a price, content, an agent definition) for correctness, evidence, security, privacy, brand and completeness, and return a QA record: PASS, PASS WITH NOTES or FAIL with itemized findings, severity and the fix. Use before anything leaves the team."
---

# QA review

*Strategy and coordination skill for the DIO expert team.* Review a deliverable against its standard and return PASS, PASS WITH NOTES or FAIL with itemized findings.

## When to use

Before any deliverable leaves the team: client documents, prices and invoices, code and infrastructure changes, published content, and changes to agents and skills. Reviewers never review their own work and never fix it; they report.

## Checklist

1. **Correctness:** facts, math, prices and dates are right; prices match `docs/05-services-and-pricing.md` or the SOW.
2. **Evidence:** every claim is sourced or labeled as an estimate; no fake metrics, invented clients or testimonials.
3. **Completeness:** the deliverable answers what was asked and meets its acceptance criteria.
4. **Security:** no secrets or credentials; least privilege; rollback path for changes; tests present for code.
5. **Privacy:** no street addresses, personal phone numbers or emails, client confidential data or personal data where it doesn't belong.
6. **Decision rights:** nothing commits money, deploys to a customer or settles an ethical question without Erich.
7. **Employer boundary:** no utility, vegetation-management or line-clearance work, and no FPL/NextEra vendors.
8. **Brand:** company voice ("we"), sentence case, no emoji, no hype; visuals follow the Dautel Design System (`dautel-brand` skill).

## Severity

- **Critical:** wrong money, a legal or security exposure, private data, a boundary breach. Always FAIL.
- **Major:** a wrong fact, a missing requirement, an unsupported claim. FAIL unless trivial to fix.
- **Minor:** style, clarity, small omissions. PASS WITH NOTES.

## Output

```markdown
**QA record:** <deliverable> — PASS | PASS WITH NOTES | FAIL

| # | Severity | Where | Finding | Fix | Back to |
| - | -------- | ----- | ------- | --- | ------- |
| 1 | major | §3, price table | Assessment priced at $2,000; rate card starts at $2,500 | Use $2,500 | proposal author |

**Likely root cause (for continuous improvement):** ...
```

After three FAILs on the same item, escalate to `chief-of-staff` instead of a fourth loop.

## Used by

`security-compliance`, `qa-test-automation-engineer`, `quality-reviewer`, `agent-builder`.
