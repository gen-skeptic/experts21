---
name: statistical-analysis
description: "Analyze process or business data with the right statistics: check the measurement system, plot it, test stability with control charts, compute capability, run hypothesis tests or regression, and report effect sizes with confidence intervals. Use for baselines, before-and-after claims, root-cause checks, marketing tests and dashboards."
---

# Statistical analysis

*Process improvement skill for the DIO expert team.* Pick and run the right statistics: measurement checks, control charts, capability, hypothesis tests and honest uncertainty.

## When to use

Any claim that a number changed, a process is stable or capable, one cause matters more than another, or a test won. Also for baselines and control charts.

## Method

1. **Question first:** what decision does the analysis serve, and what difference would matter in practice?
2. **Check the data:** source, definition, sample size, missing values, outliers (investigate, don't delete). For measurements people take, check agreement (a gauge R&R or attribute agreement analysis).
3. **Plot before testing:** run chart or histogram; look at time order.
4. **Stability:** individuals and moving-range chart (or p, u or X-bar charts as the data demands). Signals: a point beyond the limits, a run of 8 on one side, 6 trending.
5. **Capability** only for a stable process: Cp/Cpk or percent defective against the requirement.
6. **Compare** with the right test: t-test or Mann-Whitney for two groups, ANOVA or Kruskal-Wallis for more, chi-square for proportions, regression for drivers. State the assumptions and check them.
7. **Report** the effect size and a 95% confidence interval, the p-value, and the practical meaning. Small samples get wide intervals; say so.

## Output

A short analysis note: question, data and its limits, plots, the test and why, results with confidence intervals, the plain-language conclusion and how sure we are.

## Quality checks

- No causal claims from correlation alone.
- Never overstate: "no significant difference" isn't "no difference".

## Used by

`gis-remote-sensing-analyst`, `data-engineer`, `marketing-analyst`, `process-data-analyst`.
