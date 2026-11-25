---
name: routing-plan
description: "Plan which experts should answer a question that spans several functions, what each one must answer, which can run in parallel and which brain each needs. Use before asking the team anything that touches more than one area."
---

# Routing plan

*Strategy and coordination skill for the DIO expert team.* Turn a question that spans several functions into a plan: which experts, what each answers, in what order, on which brain.

## When to use

A question touches more than one function (for example legal and finance and delivery), or it's unclear who should answer it. The orchestrator uses this before delegating; the chief of staff prepares it when asked.

## Read first

- `docs/expert-roster.md`: every agent's one-line job and skills.
- `docs/agent-brains.md`: each agent's default brain and when to raise or lower it.

## Method

1. **Restate the question** in one sentence, and the decision it serves. If it hides several questions, split them.
2. **List the angles** the answer needs: legal, money, risk, technical, process, market, client, marketing, people.
3. **Pick the fewest experts** that cover every angle (usually 2 to 5). Prefer the specialist over a generalist; never add an agent just to be safe.
4. **Write each assignment:** the exact question for that expert, the inputs it gets (documents, earlier answers), and what a good answer must contain.
5. **Order the work:** run every expert whose inputs are ready **in parallel**; only wait when one expert needs another's output (for example the CPA needs the pricing model first).
6. **Pick the brain** for each assignment from the task-type table in `docs/agent-brains.md`. Raise one level for money, security, legal terms or client-final work; lower one level for routine work that a review will catch.
7. **Name the reviewer** if the answer will leave the team (a proposal, a price, a public claim): usually `quality-reviewer`, plus a specialist reviewer for its area.
8. **Flag the Chairman's decisions:** anything with financial or ethical considerations, any financial transaction and any final deployment to a customer goes to Erich with options and a recommendation.

## Output

```markdown
**Question:** ...
**Decision it serves:** ...

| # | Expert | Their question | Inputs | Brain | Runs |
| - | ------ | -------------- | ------ | ----- | ---- |
| 1 | `business-attorney` | ... | docs/07-permits-and-licenses.md | opus / high | parallel |
| 2 | `cpa-bookkeeper` | ... | answer 1 | opus / medium | after 1 |

**Review:** `quality-reviewer` (and ...)
**For Erich:** ... (or "none")
```

## Quality checks

- Every angle in step 2 has an owner; no two experts answer the same question.
- Parallel where possible; every dependency is real.
- No more than five experts unless the question truly needs more.

## Used by

`orchestrator`, `chief-of-staff`.
