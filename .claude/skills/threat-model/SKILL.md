---
name: threat-model
description: "Threat-model a system, agent or integration: list assets and trust boundaries, draw the data flows, walk STRIDE threats plus AI-specific ones (prompt injection, data leakage to model providers, excessive agency), rate each and assign mitigations. Use before building anything that handles client data or acts in client systems."
---

# Threat model

*AI and platform delivery skill for the DIO expert team.* Threat-model a system or agent: assets, trust boundaries, data flows, STRIDE threats including prompt injection, and mitigations.

## When to use

At design time for every agent, integration, platform or app that handles client data or acts in client systems; again after any major change.

## Method

1. **Assets:** what an attacker or an accident could harm: data (by class), money, accounts, reputation, availability.
2. **Data-flow diagram:** users, agents, services, stores and external providers, with the trust boundaries between them.
3. **STRIDE per element:** spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege.
4. **AI-specific threats:**
   - prompt injection from untrusted content reaching an agent with tools;
   - sensitive data sent to a model provider without an agreement;
   - excessive agency (more tools or permissions than the job needs);
   - hallucinated actions or citations reaching a client;
   - model or vendor changes that alter behavior.
5. **Rate** each threat by likelihood and impact (low, medium, high).
6. **Mitigate:** least privilege, MFA, scoped tokens, review before irreversible actions, input isolation, logging, rate limits, backups, encryption, vendor agreements (BAA where needed).
7. **Residual risk:** what remains, accepted by whom.

## Output

A threat model: diagram, assets, threat table (threat, element, rating, mitigation, owner, status), and the residual risks for sign-off.

## Quality checks

- Every high threat has a mitigation and an owner.
- Residual risks with financial impact go to Erich.

## Used by

`platform-devops-engineer`, `security-compliance`, `cto-principal-architect`, `software-solutions-architect`, `backend-api-engineer`.
