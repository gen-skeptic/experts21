---
name: architecture-decision-record
description: "Write an architecture decision record (ADR) and build-versus-buy analysis: context and constraints, options including off-the-shelf software, trade-offs on cost, security, operability and lock-in, the decision, consequences and the exit path. Use for any significant technical choice for the firm or a client."
---

# Architecture decision record

*AI and platform delivery skill for the DIO expert team.* Record a technical decision: context, options (including buy), trade-offs, the choice, consequences and how to reverse it.

## When to use

Choosing a platform, database, model provider, framework, hosting, integration pattern, or build versus buy, for the firm or a client.

## Method

1. **Context:** the problem, constraints (budget, skills, data rules, who will operate it), and the quality attributes that matter most (security, recoverability, cost, simplicity).
2. **Options:** at least three, always including an off-the-shelf product and "do less".
3. **Compare** on: total cost over 3 years, security and compliance, who can operate it (can the client's team?), lock-in and exit, maturity, fit with the approved stack.
4. **Decide** with the simplest option that meets the constraints. Prefer what the firm can build, deploy and operate well.
5. **Consequences:** what gets easier, what gets harder, new risks, follow-up work.
6. **Exit path:** how to reverse or migrate if it proves wrong.

## Output

```markdown
# ADR-NNN: <decision>
Status: proposed | accepted | superseded   Date:   Decider:
## Context
## Options considered (table)
## Decision
## Consequences
## Exit path
```

## Quality checks

- The buy option was considered honestly.
- The client's ability to run it without us was weighed.

## Used by

`data-engineer`, `cto-principal-architect`, `software-solutions-architect`.
