---
name: software-build-standards
description: "Apply the firm's software standards: the custom software lifecycle (discovery, design, sprints, QA, release handoff), coding conventions, small reviewed pull requests, tests with every change, no secrets in code, accessibility, and the definition of done. Use while building or reviewing any code."
---

# Software build standards

*Software delivery skill for the DIO expert team.* The firm's coding standards, definition of done, pull-request review and the custom software lifecycle.

## When to use

Building or reviewing any software, agent code, integration or infrastructure code for the firm or a client.

## Lifecycle (custom software, Line G)

Discovery → architecture and prototype → sprints with weekly demos → QA → release handoff package → DevOps deploys to staging → client acceptance → Erich approves production → DevOps promotes → Software Care.

## Standards

1. **Repository:** in the client's GitHub organization; the client owns the code.
2. **Branches and pull requests:** small PRs (under about 400 changed lines), one purpose each, a clear description, linked to the story.
3. **Review:** every PR reviewed by another engineer (or agent plus human) before merge; reviewers check correctness, tests, security, readability.
4. **Tests:** unit tests for logic, integration tests for boundaries, and an end-to-end test for each critical journey; CI must be green.
5. **Security:** no secrets in code or logs; parameterized queries; input validation; dependencies pinned and scanned; least-privilege service accounts.
6. **Code:** typed where the language allows; linted and formatted automatically; clear names over comments; handle errors explicitly.
7. **Accessibility and design:** WCAG 2.1 AA; the Dautel Design System for DIO-branded work, the client's brand for theirs.
8. **Docs:** README with setup and run steps; changes noted for the release notes.

## Definition of done

The story's acceptance criteria pass; tests written and green; reviewed and merged; docs updated; no new high or critical scan findings; demoed to the client.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P09 Custom software development (Line G)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `software-engineering-lead`
- **Starts when:** Kickoff of a custom software engagement
- **Done when:** Release live after client acceptance on staging and Erich's production approval; docs delivered; Software Care started.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `business-analyst` | Gather requirements; write user stories with acceptance criteria against the future-state process | Requirements + backlog |
| 2 | QA review | `lean-six-sigma-lead` | Process readiness check on the workflows the software supports. FAIL sends them to `process-health-check`, which routes them to `kaizen-event` or `dmaic-project`; a current `process-health-check` verdict of 'fix first' goes straight there | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 3 | Work | `software-solutions-architect` | Build-versus-buy check, architecture, estimate | Architecture + estimate |
| 4 | Work | `ux-ui-designer` | User flows, wireframes, clickable prototype | Prototype |
| 5 | QA review | `quality-reviewer` | Discovery package: testable requirements, consistent architecture, estimate math (requirements → step 1, architecture or estimate → step 3, prototype → step 4) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | QA review | `cto-principal-architect` | Architecture review | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 7 | QA review | `client-success-manager` | Get the client's sign-off on the requirements and prototype (requirements → step 1, prototype → step 4) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | **Approval: Erich** | Erich (Chairman) | Approve the fixed quote for the build; the client signs the build SOW through `proposal-and-sow` step 15 and `contract-review` | Decision record (approved / changes requested / stopped) |
| 9 | Work | `software-engineering-lead` | Plan the sprint | Sprint plan |
| 10 | Work | `full-stack-developer`, `backend-api-engineer`, `mobile-developer` | Build stories with tests as pull requests | Pull requests |
| 11 | QA review | `software-engineering-lead` | Code review (at least one other engineer) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 12 | QA review | `qa-test-automation-engineer` | Automated and exploratory testing against acceptance criteria; defects as tickets | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 13 | QA review | `ux-ui-designer` | Design QA of built screens | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 14 | QA review | `security-compliance` | Security review: OWASP, auth, secrets, dependencies | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 15 | Work | `client-success-manager` | Sprint demo; feedback becomes change requests (`project-plan-and-status`). Repeat steps 9–15 until scope is done | Demo notes |
| 16 | Work | `technical-writer` | User and admin docs, release notes, runbook draft | Documentation |
| 17 | Work | `software-engineering-lead` | Assemble and sign the release handoff package (mobile: include the signed store build and listing) | Release handoff package |
| 18 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (code → step 10, docs → step 16, package → step 17) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 19 | Work | `platform-devops-engineer` | Release through `release-and-deployment`: staging, client acceptance testing on staging, Erich's production approval, promotion | Deployed release |
| 20 | Work | `client-success-manager` | Get the client's acceptance sign-off; start Software Care (`managed-operations`); close out (`project-plan-and-status`) | Acceptance record |

## Used by

`software-engineering-lead`, `full-stack-developer`, `backend-api-engineer`, `mobile-developer`, `qa-test-automation-engineer`.
