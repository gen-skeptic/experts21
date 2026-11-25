---
name: agent-safety-audit
description: "Run an Agent Safety Audit ($1,500, one week, remote): inventory the client's AI tools and agents, check credentials, permissions, MCP servers, data flows, prompt-injection exposure, logging, human review and recovery, then deliver a scored report with prioritized fixes. Use when a team already runs agents or AI tools."
---

# Agent safety audit

*AI and platform delivery skill for the DIO expert team.* Audit an existing AI or agent setup: credentials, permissions, MCP servers, data flows, logging, review and recovery, with a scored report.

## When to use

A team already uses AI assistants, agents or automations and wants to know whether they are safe. Also as a check on our own builds before go-live.

## Method

1. **Inventory:** every AI tool, agent, automation and MCP server; who set it up; what it can reach.
2. **Credentials:** shared passwords, long-lived keys, keys in code or chat, personal accounts used by agents.
3. **Permissions:** what each agent can read and change compared with what its job needs.
4. **Data flows:** what data goes to which model provider, under which terms; regulated data (patient, client, financial) in tools without agreements.
5. **Prompt injection:** can untrusted content (email, documents, web pages) reach an agent that has write access?
6. **Human review:** which actions happen without a person approving.
7. **Logging and audit:** can you tell what an agent did, when and for whom?
8. **Recovery:** can you pause an agent, undo its changes and restore data? When was that last tested?
9. **Score** each area 0–3 and rate each finding critical, high, medium or low.

## Output

A scored report: summary and overall score, findings by area with evidence, a prioritized fix list (quick wins first), and an offer for the fixes if wanted.

## Quality checks

- Findings cite evidence (a screenshot, a config line), never guesses.
- No secrets are copied into the report.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P11 Agent Safety Audit). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `security-compliance`
- **Starts when:** Signed audit SOW
- **Done when:** Scored report delivered at a readout; remediation offered.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `security-compliance` | Confirm scope and the systems in scope | Audit scope |
| 2 | QA review | `business-attorney` | Confirm written authorization and an NDA are in place before any testing | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 3 | Work | `security-compliance` | Review credentials, MCP exposure, injection paths, logging, recovery. A critical live exposure is reported to the client at once through `client-success-manager` | Findings |
| 4 | QA review | `senior-agent-engineer` | Validate findings technically and check fix recommendations | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Work | `security-compliance` | Write the scored report with prioritized fixes | Report draft |
| 6 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 7 | Work | `client-success-manager` | Deliver the readout; remediation → `proposal-and-sow` step 10 and `governed-agent-design` | Readout record |

## Used by

`senior-agent-engineer`, `security-compliance`.
