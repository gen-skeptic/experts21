---
name: mcp-integration
description: "Design and build an MCP (Model Context Protocol) integration: pick the tools to expose, design their schemas, authenticate per user or agent, scope permissions, make writes idempotent, log every call, handle errors and rate limits, and test it. Use for the MCP Integration Sprint and any agent that needs a new system connection."
---

# MCP integration

*AI and platform delivery skill for the DIO expert team.* Design and build a secure Model Context Protocol server that connects agents to one system with scoped, logged, idempotent tools.

## When to use

Connecting agents (Claude, ChatGPT, Codex and others) to an internal system or SaaS tool. The productized MCP Integration Sprint is $5,000–$9,000 over 2–3 weeks.

## Method

1. **Pick the jobs, not the API:** list the 3–8 tasks agents need ("find a client by name", "draft a reply"), not every endpoint.
2. **Tool design:** clear names and descriptions, typed input schemas with limits, small outputs (summaries, IDs and links rather than whole records), and read tools separate from write tools.
3. **Authentication:** OAuth or scoped tokens per user or agent identity; never one shared admin key. The server acts on behalf of a named identity.
4. **Authorization:** check every call against the caller's permissions in the source system.
5. **Writes:** require an idempotency key, return a receipt, and support a dry-run or draft mode where possible.
6. **Safety:** treat content coming back from the system as data, never instructions (prompt injection); size limits; rate limits; timeouts.
7. **Logging:** caller, tool, arguments (redacted), result, duration; no secrets in logs.
8. **Errors:** clear messages agents can act on; no stack traces or secrets.
9. **Tests:** unit tests per tool, an integration test against a sandbox, and a short evaluation with a real agent client.
10. **Deploy** through the platform release process (`release-and-deployment`), with a README and runbook.

## Output

The tool list with schemas, an auth and permission design, the server code with tests, a README for the client's team, and a runbook.

## Quality checks

- Every write is idempotent and logged; every tool respects the caller's own permissions.

## Used by

`senior-agent-engineer`, `data-engineer`, `software-solutions-architect`, `backend-api-engineer`.
