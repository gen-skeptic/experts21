---
name: private-ai-platform
description: "Design a company memory and private AI platform (Line C): shared memory on PostgreSQL with pgvector, single sign-on, private networking, model access with data agreements, backups and restore drills, monitoring, and a GitOps deployment, all in the client's own accounts. Use for Company Memory Starter, private AI and GitOps Platform Launch work."
---

# Private AI platform

*AI and platform delivery skill for the DIO expert team.* Design a company memory and private AI platform in the client's own environment: PostgreSQL with pgvector, SSO, private networking and recovery.

## When to use

A client wants AI that works over its own documents and knowledge without sending everything to public tools: law, medical, CPA and other regulated firms. Setup runs $7,500–$25,000.

## Method

1. **Requirements:** users and roles, data classes, retention, compliance (HIPAA, attorney confidentiality), budget, who will operate it.
2. **Hosting choice** (`architecture-decision-record`): client cloud account, VPS, or on-premises hardware; the client owns and licenses everything deployed.
3. **Memory store:** PostgreSQL with pgvector; schema with source, owner, classification and timestamps on every record; access control by role; deletion that really deletes.
4. **Ingestion:** connectors per source, chunking and embedding, deduplication, and a curation guide so the memory stays clean.
5. **Identity:** SSO (the client's identity provider or Authentik), MFA, per-agent identities.
6. **Network:** private networking (WireGuard or the client's VPN), no public database ports, TLS everywhere.
7. **Models:** which providers, under what data terms (no training on client data; BAA where needed), or self-hosted models where data can't leave.
8. **Operations:** GitOps deployment, secrets management (SOPS or a secrets manager), monitoring and alerts, backups with a tested restore, upgrade path.
9. **Licensing:** never deliver OpsBrain or Open Brain as a product or hosted service; build client memory layers for and owned by the client.

## Output

An architecture document with diagram, data model, access matrix, threat model, cost estimate (setup and monthly pass-through), and the runbook outline.

## Quality checks

- A restore was tested before go-live.
- No client data in DIO's own systems.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P06 Company memory, private AI platform and GitOps Platform Launch (Line C)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `platform-devops-engineer`
- **Starts when:** Kickoff of a platform engagement
- **Done when:** Platform live in client-owned accounts after client acceptance and Erich's go-live approval; restore drill passed; runbooks handed over.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `cto-principal-architect` | Select the reference architecture and size it | Architecture fit note |
| 2 | Work | `platform-devops-engineer` | Design SSO, networking, storage, backups, monitoring | Platform design |
| 3 | QA review | `security-compliance` | Review the design for access, exposure and data handling | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | QA review | `client-success-manager` | Get the client's sign-off on the design; requested changes return to step 2 | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Work | `platform-devops-engineer` | Build with IaC and GitOps in client-owned accounts, before go-live | Platform code |
| 6 | Work | `data-engineer` | Build the memory schema, ingestion and attribution | Memory layer |
| 7 | Work | `senior-agent-engineer` | Connect agent runtimes to memory through MCP/API | Agent connections |
| 8 | Work | `platform-devops-engineer` | Run a restore drill and test alerts | Drill record |
| 9 | QA review | `qa-test-automation-engineer` | Functional test: SSO login, agent retrieval, backup restore, alerts (platform → step 5, memory → step 6, agent connections → step 7) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 10 | QA review | `security-compliance` | Access review and exposure check (platform → step 5, memory → step 6, agent connections → step 7) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | Work | `technical-writer` | Write runbooks and the memory curation guide | Documentation |
| 12 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (platform → step 5, docs → step 11) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 13 | QA review | `client-success-manager` | Client acceptance walkthrough on the platform before go-live; requested changes return to step 5 | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 14 | **Approval: Erich** | Erich (Chairman) | Approve go-live (final deployment to the customer) | Decision record (approved / changes requested / stopped) |
| 15 | Work | `platform-devops-engineer` | Go live and verify | Live platform |
| 16 | Work | `client-success-manager` | Hand over; start the retainer (`managed-operations`); close out (`project-plan-and-status`) | Handover record |

## Used by

`platform-devops-engineer`, `data-engineer`, `cto-principal-architect`.
