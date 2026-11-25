---
name: requirements-and-user-stories
description: "Gather and write requirements: interview users, map the future-state process, write user stories with testable acceptance criteria (given-when-then), non-functional requirements, a glossary and a prioritized backlog (must, should, could). Use at the start of any software or agent build, and for change requests."
---

# Requirements and user stories

*Software delivery skill for the DIO expert team.* Turn business needs into user stories with testable acceptance criteria, a process map and a prioritized backlog.

## When to use

Discovery for custom software (paid discovery $3,500–$7,500), agent builds, and change requests.

## Method

1. **Who and why:** users and their goals; the business outcome and how it will be measured.
2. **Process first:** map the approved future-state process (from `process-health-check` or a Kaizen); software follows the process, not the other way round.
3. **User stories:** "As a <role>, I want <capability> so that <benefit>." Small enough to build in a few days.
4. **Acceptance criteria** for each story in given-when-then form, including errors and edge cases.
5. **Non-functional requirements:** security and access, privacy and data classes, performance, accessibility (WCAG 2.1 AA), availability, audit, retention.
6. **Glossary** of the client's terms.
7. **Prioritize** with MoSCoW; the first release holds only the musts.
8. **Confirm** with the client: read back the stories and criteria in their words.

## Output

A requirements document: goals and measures, process map, story list with acceptance criteria, non-functional requirements, glossary, prioritized backlog and open questions.

## Quality checks

- Every story has testable acceptance criteria.
- `qa-test-automation-engineer` can write a test from each criterion.

## Used by

`product-manager`, `software-solutions-architect`, `business-analyst`, `ux-ui-designer`.
