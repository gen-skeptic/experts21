---
name: governed-agent-design
description: "Design a governed AI agent workflow (Line B): scope and non-goals, the agent's identity and least-privilege access, tools and MCP servers, human review checkpoints, idempotent actions, audit logging, an evaluation set, failure modes, rollback and a runbook. Use for any agent that will touch a client's real systems."
---

# Governed agent design

*AI and platform delivery skill for the DIO expert team.* Design an AI agent workflow that is scoped, identity-bound, least-privilege, reviewed, tested, logged and recoverable.

## When to use

Designing any agent that reads or changes a client's real systems: intake, drafting, triage, records posting, scheduling, follow-ups. Builds run $6,000–$15,000 per workflow.

## Method

1. **Job and non-goals:** one sentence for what the agent does; a list of what it must never do.
2. **Approved process:** design against the future-state process that passed `process-health-check`, never today's workarounds.
3. **Identity:** the agent has its own account in each system, never a person's credentials or a shared login.
4. **Least privilege:** list every permission and why; read-only wherever possible; scoped tokens that expire.
5. **Tools:** each tool or MCP server, its inputs and outputs, and its blast radius if misused (`mcp-integration`).
6. **Human review:** where a person approves before anything is sent, filed, paid or deleted. Start with review on everything, relax only with evidence.
7. **Idempotency:** every write carries a key so a retry can't double-send or double-file; record a receipt.
8. **Audit log:** who (which agent, on whose behalf), what, when, inputs, outputs and the approval.
9. **Data handling:** what the model sees; redaction; where prompts and outputs are stored (client systems only); model provider terms.
10. **Evaluation set:** 30–100 realistic cases with expected results, including edge cases and attempts to misuse it; a pass threshold agreed with the client.
11. **Failure modes:** wrong answer, tool down, model refusal, prompt injection in incoming documents; the agent's behavior for each.
12. **Recovery:** how to pause it, roll back a bad change, and restore data; tested before go-live.

## Output

An agent design document with the sections above, the access matrix, the evaluation set, and the runbook outline. `security-compliance` reviews the design before the build starts.

## Quality checks

- No permission without a reason; no shared credentials.
- Human review sits before every irreversible action.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P05 Governed agent workflow build and MCP Integration Sprint (Line B)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `senior-agent-engineer`
- **Starts when:** Kickoff of an agent workflow or MCP integration engagement
- **Done when:** Workflow live after client acceptance and Erich's production approval, verified, documented and handed over; retainer started.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | QA review | `lean-six-sigma-lead` | Process readiness check: the target process is mapped, measured, stable and stripped of waste. FAIL sends it to `process-health-check`, which routes it to a Kaizen event (`kaizen-event`) or DMAIC project (`dmaic-project`); a current `process-health-check` verdict of 'fix first' goes straight there | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 2 | Work | `senior-agent-engineer` | Design architecture and access against the approved future-state process: roles, tools, MCP servers, identities, review checkpoints | Design document |
| 3 | QA review | `security-compliance` | Threat-model the design: injection paths, credential scope, data egress | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | QA review | `cto-principal-architect` | Architecture review: simplicity, operability, exit path | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | QA review | `client-success-manager` | Get the client's sign-off on the design; requested changes return to step 2 | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Work | `data-engineer` | Build data sources and memory pipelines if needed | Data pipelines |
| 7 | Work | `senior-agent-engineer` | Build MCP servers and agents with tests and evaluation sets, in non-production | Code + tests + evals |
| 8 | QA review | `ai-solutions-engineer` | Run evaluations against the success metrics (agents → step 7, data pipelines → step 6) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 9 | QA review | `security-compliance` | Pre-release security review (agents → step 7, data pipelines → step 6) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 10 | Work | `technical-writer` | Write the runbook, access matrix and user guide | Documentation |
| 11 | Work | `senior-agent-engineer` | Assemble the release handoff package | Release handoff package |
| 12 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (code → step 7, docs → step 10, package → step 11) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 13 | Work | `platform-devops-engineer` | Release through `release-and-deployment`: staging, client acceptance testing, Erich's production approval, promotion | Live deployment |
| 14 | QA review | `ai-solutions-engineer` | Verify behavior in production; on failure DevOps rolls back first | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 15 | Work | `client-success-manager` | Get the client's acceptance sign-off; start the retainer (`managed-operations`); close out (`project-plan-and-status`) | Acceptance record |

## Used by

`senior-agent-engineer`, `ai-solutions-engineer`, `cto-principal-architect`.
