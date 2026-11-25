---
name: test-plan
description: "Write and run a test plan: scope and risks, test cases from the acceptance criteria, unit, integration and end-to-end automation, accessibility and security checks, agent evaluation sets with pass thresholds, and an objective test report. Use for every release of software or agents."
---

# Test plan

*Software delivery skill for the DIO expert team.* Plan and automate testing from the acceptance criteria, including agent evaluation sets, and report results objectively.

## When to use

For every release: software, integrations and agents. Start when the acceptance criteria are written, not when the code is done.

## Method

1. **Scope and risk:** what changes, what could break, what matters most to the client; test hardest where the risk is highest.
2. **Test cases** from each acceptance criterion: the happy path, errors, edge cases (empty, huge, duplicate, wrong format, no permission).
3. **Automate** what repeats: unit tests (logic), integration tests (APIs, databases, MCP tools), end-to-end tests (critical journeys in a real browser).
4. **Non-functional checks:** accessibility (WCAG 2.1 AA, keyboard and screen reader), performance on realistic data, security basics (auth, permissions, secret scan).
5. **Agents:** an evaluation set of 30–100 realistic cases with expected outputs, including misuse and prompt-injection attempts; score each run; the release passes only above the agreed threshold, with every failure reviewed.
6. **Regression:** rerun the full suite before every release.
7. **Report:** what was tested, results, open defects with severity, and a clear recommendation (release or not).

## Output

A test plan, the automated tests in the repository, and a test report attached to the release handoff package.

## Quality checks

- Every acceptance criterion maps to at least one test.
- Defects are reported with steps to reproduce, without blame.

## Used by

`senior-agent-engineer`, `software-engineering-lead`, `full-stack-developer`, `backend-api-engineer`, `mobile-developer`, `qa-test-automation-engineer`.
