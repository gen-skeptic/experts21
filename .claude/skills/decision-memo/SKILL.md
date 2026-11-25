---
name: decision-memo
description: "Write a decision memo: the decision, the options, facts and assumptions, cost of each option, reversibility, risks, a recommendation with conditions and a review date, and who decides. Use for pricing, hiring, new services, large clients, the full-time move or any choice with money or ethics involved."
---

# Decision memo

*Strategy and coordination skill for the DIO expert team.* Frame a decision with options, facts, costs, risks and a recommendation, and say who decides.

## When to use

Any decision that commits money, changes what the firm sells, hires or ends work, or has an ethical angle. Also any cross-functional question the orchestrator has to settle.

## Read first

- `docs/05-services-and-pricing.md`, `docs/06-startup-and-operating-costs.md`, `docs/11-risks.md`, and the topic file for the decision.

## Method

1. **State the decision** as a question with a deadline ("Do we hire a contract developer for the Q2 build, by March 1?").
2. **Who decides:** Erich (Chairman) decides anything with financial or ethical considerations, every financial transaction and every final deployment to a customer. The orchestrator decides other cross-functional questions; a process owner decides inside its process.
3. **Options:** at least three, including "do nothing" or "wait". Make each one real, not a straw man.
4. **Facts and assumptions:** separate what is known (with a source and date) from what is assumed. Label estimates *(est.)*.
5. **For each option:** cost (one-time and monthly), revenue or savings, time to result, reversibility (one-way or two-way door), effect on Erich's hours, and the main risk.
6. **Cost of delay:** what waiting a month costs.
7. **Strongest counter-argument** to the recommended option, answered.
8. **Recommend** one option, with the conditions that would change the answer and a review date.

## Output

```markdown
# Decision: <question> (by <date>)
**Decides:** Erich (Chairman) | orchestrator | <owner>     **Reversible:** yes/no

| Option | Cost | Benefit | Time | Risk | Reversible |
| ------ | ---- | ------- | ---- | ---- | ---------- |

**Facts (sourced):** ...
**Assumptions:** ...
**Recommendation:** ... **because** ...
**Strongest objection and answer:** ...
**Would change our mind:** ...
**Review on:** <date>
```

## Quality checks

- Numbers trace to a source or are marked as estimates.
- The recommendation follows from the table, not from enthusiasm.
- The memo is honest about what isn't known.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P30 Strategic decision with financial or ethical impact). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `orchestrator`
- **Starts when:** A major decision with financial or ethical considerations: pricing, new service line, hire, full-time move, large client, investment. Strategic choices without them are decided by orchestrator in `operating-cadence`
- **Done when:** Decision made by Erich and recorded with rationale and a review date.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `chief-of-staff` | Frame the decision: options, facts, assumptions, reversibility, cost of delay | Decision frame |
| 2 | Work | `market-research-analyst`, `operations-finance-manager` | Supply market facts and a financial model for each option | Facts + model |
| 3 | Work | `advisory-board` | Pressure-test from four perspectives; recommend with conditions | Board memo |
| 4 | Work | `orchestrator` | Recommend an option to the Chairman, with conditions, the risks it accepts and a review date | CEO recommendation |
| 5 | QA review | `quality-reviewer` | Check evidence quality, balance and that the strongest counter-argument is addressed (frame → step 1, facts or model → step 2, board memo → step 3, recommendation → step 4) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | **Approval: Erich** | Erich (Chairman) | Decide | Decision record (approved / changes requested / stopped) |
| 7 | Work | `chief-of-staff` | Record the decision, owner and review date; issue task cards | Decision record |

## Used by

`orchestrator`, `chief-of-staff`, `advisory-board`, `cto-principal-architect`.
