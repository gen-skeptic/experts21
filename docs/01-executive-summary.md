# Executive summary and current state

*Source: copied from the DIO business plan research in gen-skeptic/experts (`research/dautel-intelligent-operations-business-plan-research.md`, compiled November 19, 2026), updated November 25, 2026 where noted. Process numbers such as P33 refer to the DIO operating manual in that repository; in this repository the same methods are skills in `.claude/skills/`.*

Who the firm is, why it can win, what already exists and what is missing. Read this first.

## 1. Executive summary

Dautel Intelligent Operations (DIO) already has the hard-to-fake part of a consultancy: **working, documented proof**. That proof is a three-node K3s platform run through GitOps, a multi-agent stack with shared memory (OpenBrain), and a deployed MCP-connected application (Cassian). What it lacks is a **commercial shape**. Today dautel.io reads as a strong technical portfolio, not as a company with offers, prices and a buying path.

**Recommended positioning:**

> **Dautel Intelligent Operations helps small and mid-sized businesses fix how work gets done, then put AI agents and software to work safely, connected to real systems with clear ownership, access control, review and recovery.**
> *Fix first, then automate. Operations discipline first, AI second.*

Why this position wins:

1. **The market gap is the setup, not the models.** About 18–20% of US firms use AI (Census BTOS, Dec 2025–May 2026), and SMB agent scaling stayed flat at 22% while large enterprises jumped to 40% (McKinsey State of AI 2026). Small firms say they lack *someone to implement it*, not the budget. JPMorganChase Institute found that small employer firms out-adopt larger firms with no employees, which suggests "having access to additional human capital to implement and integrate AI may be more important than financial resources alone." DIO sells exactly that human capital.
2. **Most pilots fail on governance and integration.** Commonly cited figures say about 95% of generative-AI pilots return nothing, and SMB agent-project abandonment is about 43% (First Page Sage 2026). Erich's published work centers on what those failures lack: scoped credentials, identity-bound agents, idempotent actions, reviewed changes, tested recovery.
3. **Few competitors combine both halves.** "AI automation agencies" are mostly no-code workflow builders with no infrastructure depth. MSPs know infrastructure but lack agent depth. DevOps consultancies rarely talk to a 30-person law firm. An operations manager with an MBA in progress, Lean Six Sigma, utility field leadership *and* hands-on Kubernetes and agent engineering is a rare profile.

**Recommended model:** start as a **side practice (2027)** with fixed-fee assessments and builds, add **managed retainers** as the recurring base, and move to full-time when recurring revenue covers a set threshold (see [§10](06-startup-and-operating-costs.md)). Market **locally on trust and nationally on specialization**: every offer can be delivered remotely, so productized remote services ([§8](09-marketing.md)) extend the market well beyond South Florida. Add **custom software development** (Line G) as a premium offer: the DIO software team designs, builds and tests, and the DevOps team deploys and operates through the same GitOps discipline. Lead with **Lean Six Sigma process improvement** (Line H): DIO doesn't automate broken processes. Every automation and software build starts with a fix-first readiness check, and Process Health Checks, Kaizen events and DMAIC projects become offers of their own. Grow the team only as revenue supports it ([§11](08-staffing.md)). Keep a **utility and field-operations vertical** in reserve for after the FPL tenure, where the domain moat is deepest.

---

## 2. Current state: what exists today

### 2.1 Assets

| Asset | What it proves to a buyer |
| --- | --- |
| **dautel.io**: "AI workflows. Operational depth." | Professional brand, case studies written as challenge, approach and evidence, plus an honest "evidence-aware" tone |
| **Career agent** on dautel.io (curated knowledge base, 10-question limit) | Can ship a scoped, safe, customer-facing AI assistant |
| **Cassian** (cassian.dautel.cloud) | Multiple MCP servers (Sprout Track, OpenBrain, Cassian), identity-bound agent publishing, Authentik SSO, idempotency receipts, image pipeline, 40 server tests, data-preserving rollout |
| **OpenBrain** shared memory (PostgreSQL + pgvector) | Cross-agent context with attribution, in practice a "company memory" product |
| **OpsBrain** (gen-skeptic/OpsBrain), a fork of Open Brain | DIO's own multi-user, multi-agent system of record: people and agents with their own keys, full attribution, restricted records, database-enforced approvals, and a PARA markdown copy four times a day. Self-hosted; clients never see it |
| **Agent coordination study**: Claude Code, Codex, OpenClaw, Hermes Agent, Herdr/tmux, Paperclip | Current, vendor-neutral, hands-on knowledge of the agent tool landscape |
| **Homelab platform**: K3s ×3, Flux, SOPS, GitHub Actions, Jenkins + OpenTofu + Ansible, Argo Rollouts, Prometheus/Grafana/Alertmanager/Gatus, CloudNativePG, TrueNAS/ZFS, Proxmox, OPNsense, Pangolin/Newt/WireGuard | Can design, deliver and *operate* private infrastructure with change control and recovery |
| **Specialist-role agent design** (HAL plus the SG-1 roster: scheduling, documents and process mapping, coding, research, analysis, QA) | A ready blueprint for a "digital back office" offer |
| **Dautel Design System** (`dautel_brand`, copied into `design-system/` in this repo): Terminal Monogram logo, five themes, stylesheet, fonts, voice rules ("no fake metrics") | Brand consistency is solved for every site, app, document and marketing asset (Dautel theme for DIO sites; Catppuccin themes for software, examples, social media and customer sites), and the honesty rule is a selling point |
| **Lean Six Sigma Green Belt** (FAU) plus an MBA in Operations Management in progress | Credible, uncommon process-improvement depth for an AI practice: the basis of the "fix first, then automate" position |
| **GitHub** (@gen-skeptic), **LinkedIn** | Public credibility channels |

### 2.2 Founder profile (from the published resume)

- **Founder and Chairman, Dautel Intelligent Operations** (2026–present)
- **Sr. Arborist, Florida Power & Light Transmission** (2022–present): NERC and non-NERC corridor patrols, vendor workload and safety oversight, budget forecasting, storm restoration, GIS/LiDAR hazard scoping, and regular **Acting Operations Lead** coverage
- **Arborist I, FPL Distribution** (2020–2022); **VM Arborist, ACRT for FPL** (2017–2020)
- **NextEra Energy Hackathon** (July 2026): 2nd of 13 teams (Grid Guardians) plus the individual challenge win
- **Earlier:** environmental systems and GIS, green building and energy auditing, teaching and mentoring, **U.S. Army** technical leadership
- **Education:** MBA in Operations Management, FAU (expected 2027); B.S. Environmental Studies, FIU
- **Credentials:** Lean Six Sigma Green Belt, ISA Certified Arborist, FAA Remote Pilot (Part 107), LEED AP, plus generative-AI coursework (Microsoft/LinkedIn)

**What this means commercially:** Erich can sell to the *business owner* (operations, budgets, process, vendor management, safety culture) and then build what he sold. That combination supports premium pricing compared with freelance "AI automation" builders.

### 2.3 Gaps to close

| Gap | Why it matters | Fix |
| --- | --- | --- |
| No **service menu or prices** on dautel.io | Buyers can't self-qualify, so the site generates curiosity, not leads | Add a services page with three to four named offers and "starting at" prices |
| Case studies are **personal and homelab** | SMB buyers ask "has he done this for a business like mine?" | Land two or three paid or discounted pilot clients in 2027 and publish outcome-based case studies |
| Tone leans **job-seeker** ("View experience") | Mixed signal: hire me or buy from me? | Split it: dautel.io becomes the company, and a /about or /erich page keeps the resume |
| No **booking path** | Friction | Add a scheduling link for a free 30-minute "AI fit call" |
| No **formal entity, insurance or contracts** visible | Required before any B2B engagement | See [§12](07-permits-and-licenses.md) |
| **Lean Six Sigma Black Belt** not yet earned | Larger DMAIC engagements and enterprise buyers expect Black Belt leadership | Earn it in 2027–28 after the MBA; until then, scope DMAIC projects to Green Belt size |
| **Kubernetes certs** not yet earned (the Kubestronaut path is linked) | Not needed for SMBs, but helps with technical buyers | CKA first, then CKAD and CKS over 2027–28 (optional) |

---
