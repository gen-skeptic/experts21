# Operations and delivery

*Source: copied from the DIO business plan research in gen-skeptic/experts (`research/dautel-intelligent-operations-business-plan-research.md`, compiled November 19, 2026), updated November 25, 2026 where noted. Process numbers such as P33 refer to the DIO operating manual in that repository; in this repository the same methods are skills in `.claude/skills/`.*

How work is delivered, what every engagement ships with, who decides what, and how much work fits in a side practice.

## 9. Operations and delivery standards

DIO's internal operating system is already its marketing:
- **Delivery stack:** the client's GitHub org; GitHub Actions; Flux/GitOps or simple Docker deployments for small clients; SOPS/secret manager; Authentik or the client's IdP; Prometheus/Gatus monitoring.
- **Internal agent team:** DIO's own back office runs on the agents in `.claude/agents/`, led by `orchestrator` (Picard), the CEO agent: it routes each question to the right experts, has them work in parallel, combines their answers, follows the reporting lines in [expert-roster.md](expert-roster.md), and reports to Erich as Chairman. See [CLAUDE.md](../CLAUDE.md). Erich's personal agents (HAL and the SG-1 roster) stay separate and are not used for DIO work. The DIO team is a live demo of the "digital back office" offer.
- **Standard artifacts per engagement:** SOW, architecture diagram, access matrix, test results, runbook, recovery drill record, ROI baseline.
- **System of record: OpsBrain.** Task cards, QA and decision records, approvals, kaizen cards, meeting notes, risks, incidents, the CRM (companies, contacts, the P02 deal pipeline and every sales conversation), proposal, invoice and contract records, hiring records, playbooks and research live in OpsBrain, DIO's self-hosted company database (gen-skeptic/OpsBrain), which is also the agents' shared memory. Each person and agent has its own identity, every record shows who did what on whose behalf, approvals that need Erich are enforced by the database, and a PARA-organized markdown copy is written four times a day. Client deliverables stay in client systems and DIO's delivery repositories; clients never see OpsBrain. Setup is in gen-skeptic/experts (`opsbrain/README.md`). Erich works the pipeline and the approval queue in OpsBrain's private web UI; no separate SaaS CRM is needed.
- **Decision rights:** Erich approves final deployments to customers and financial transactions, and decides anything with financial or ethical considerations; agents decide everything else and record it. Retainer SOWs carry a standing approval for standard changes.
- **Support hours:** each SOW states support hours and response targets; DIO never promises 24/7.
- **Software delivery lifecycle (Line G):** discovery → architecture and prototype → sprints (reviewed pull requests, CI tests) → QA → release handoff package → **DevOps deploys to staging** → client acceptance testing on staging → Erich approves production → DevOps promotes → verification → Software Care plan. Developers never deploy to production; DevOps owns environments, deployment and rollback. The full handoff contract is in the software agent files in `.claude/agents/`.
- **Capacity math (side practice):** about 10–12 billable hours a week realistically means one assessment *or* one build at a time, plus up to four or five retainer clients.

---

### 8.6 Remote operations requirements

- **Contracts:** state the governing law (Florida); include remote-access and data-handling terms in the MSA/DPA; take a deposit (50% upfront for fixed-fee work) through Stripe or ACH.
- **Sales tax and nexus:** consulting services are generally not taxed in Florida, but check how other states treat digital and SaaS-like deliverables (especially managed hosting) with an accountant before selling nationally.
- **Insurance:** make sure the E&O and cyber policy covers clients in all US states (and international clients if pursued).
- **Access hygiene:** a password manager with per-client vaults, hardware MFA keys, a separate work device or profile for client access, and access logs. These are the same disciplines already used in the homelab.
- **Async delivery cadence:** a weekly written update plus a short Loom; one standing 30-minute call. This suits evening and weekend hours while employed.
- **International clients (later):** watch payment fees, contract jurisdiction and data-transfer rules (e.g., GDPR for EU clients). Start US-only.
