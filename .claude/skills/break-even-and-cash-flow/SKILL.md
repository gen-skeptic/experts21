---
name: break-even-and-cash-flow
description: "Build or update the firm's financial model: fixed and variable costs, revenue scenarios by service line, break-even, a 12-month cash-flow forecast, the full-time transition trigger and the hiring trigger, with every assumption labeled. Use for pricing decisions, hiring, the full-time move, new offers and lender or partner questions."
---

# Break-even and cash-flow model

*Legal, finance and people skill for the DIO expert team.* Model costs, revenue scenarios, break-even, cash flow and the full-time and hiring triggers.

## When to use

Deciding prices, a hire, the full-time move, a new offer or a big expense; and every quarter to refresh the forecast.

## Read first

- `docs/06-startup-and-operating-costs.md` (costs and revenue scenarios), `docs/05-services-and-pricing.md`, `docs/08-staffing.md` (loaded cost and hiring math).

## Method

1. **Fixed costs per month:** insurance, tools and APIs, workspace, accounting, marketing baseline (the docs estimate about $335–$720 a month home-based).
2. **Variable costs:** pass-through model and hosting costs, subcontractors, payment fees (about 3% on cards).
3. **Revenue lines:** assessments, builds, retainers (MRR), workshops, process improvement; price × volume per month, with a ramp.
4. **Three scenarios:** conservative, expected, strong. Label every input *(est.)* unless it's a signed contract.
5. **Break-even:** monthly fixed costs ÷ contribution margin per engagement; show how many assessments or retainers cover the fixed costs.
6. **Cash flow (12 months):** deposits and payment timing (50% upfront, net 15–30), taxes set aside (about 25–30% of profit *(est.)*), the reserve.
7. **Triggers:**
   - **Full-time:** retainer MRR of $8–10K for three consecutive months, plus six months of personal expenses in reserve, plus at least two signed builds.
   - **Hiring:** revenue the person will deliver or protect of at least 1.5 × their loaded cost, plus three months of that cost in cash.
8. **Sensitivity:** which two inputs move the result most.

## Output

A model table by month, the break-even point, the scenario summary, trigger status, and the key assumptions. Spreadsheets are fine; show the formulas, not just results.

## Quality checks

- The model ties to actual bookkeeping for past months.
- `cpa-bookkeeper` checks tax assumptions.

## Used by

`cpa-bookkeeper`, `advisory-board`, `product-manager`, `operations-finance-manager`.
