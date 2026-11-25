---
name: pricing-and-estimating
description: "Estimate the effort for an engagement and set a fixed price: break the work down, estimate hours with a range, add contingency, price from the rate card and 2026 benchmarks, check margin and capacity, and record the assumptions. Use for quotes, change orders, retainers and productized offers."
---

# Pricing and estimating

*Sales and clients skill for the DIO expert team.* Estimate effort and price fixed-fee work from the rate card and benchmarks, with contingency and margin checks.

## When to use

Quoting an engagement, a change order, a retainer tier or a new productized offer; or checking whether a price still makes sense.

## Read first

- `docs/05-services-and-pricing.md` (rate card, benchmarks, value ladder), `docs/06-startup-and-operating-costs.md`, `docs/10-operations-and-delivery.md` (capacity: about 10–12 billable hours a week while Erich is employed).

## Method

1. **Break down the work** into deliverables, then tasks of no more than a day.
2. **Estimate each task** as low, likely and high hours. Use past actuals when they exist.
3. **Expected effort** = (low + 4 × likely + high) / 6 per task; sum them.
4. **Contingency:** 15–20% for builds, more when the client's systems are unknown. Paid discovery first when uncertainty is high.
5. **Price:** start from the rate card band for the offer; check the implied hourly rate stays at or above the $175 floor; compare with the 2026 market ranges.
6. **Pass-through costs:** model APIs, hosting and tools at cost, estimated monthly, never hidden.
7. **Capacity check:** calendar weeks at the available hours; one build at a time while employed.
8. **Record assumptions** that would change the price (data quality, access, number of users, integrations).

## Output

```markdown
| Deliverable | Low | Likely | High | Expected h |
| ----------- | --- | ------ | ---- | ---------- |
Total expected: __ h + contingency __% = __ h → price $__ (implied $__/h)
Pass-through: ~$__/month   Calendar: __ weeks   Assumptions: ...
```

## Quality checks

- Price inside the rate card band, or the exception is explained for Erich.
- Implied hourly rate at or above the floor; contingency stated.
- Erich approves every final price.

## Used by

`ai-solutions-engineer`, `business-development`, `product-manager`, `delivery-lead`, `operations-finance-manager`, `software-engineering-lead`.
