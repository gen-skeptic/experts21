# Services and pricing

*Source: copied from the DIO business plan research in gen-skeptic/experts (`research/dautel-intelligent-operations-business-plan-research.md`, compiled November 19, 2026), updated November 25, 2026 where noted. Process numbers such as P33 refer to the DIO operating manual in that repository; in this repository the same methods are skills in `.claude/skills/`.*

The eight service lines, the productized offers, the value ladder and the 2026 market rates behind the prices.

## 4. Recommended service lines (best fit, ranked)

The ranking weighs four things: fit with proven skills, buyer demand, ability to run as a side business, and potential for recurring revenue.

### Line A: AI Operations Readiness Assessment (entry offer)
- **What:** a two-to-three-week fixed-fee engagement. Interview the owner and staff, map three to five core workflows (Lean value-stream style), inventory systems and data, score AI opportunities by ROI and risk, define an access and governance baseline, and deliver a prioritized 90-day roadmap with a quoted first build.
- **Why it fits:** it uses Lean Six Sigma, the MBA and operations leadership directly. It is low-risk for buyers, can be done on evenings and weekends, and feeds every other line.
- **Price:** **$2,500 (≤25 staff) / $4,500 (25–100 staff)**, credited toward a build within 60 days.

### Line B: Governed Agent Workflows (core build offer)
- **What:** design and deploy one or more agent workflows connected to the client's real systems through **MCP servers and APIs**, with identity-bound agent accounts, least-privilege credentials, human review checkpoints, idempotent actions, audit logs, tests, and a runbook. Typical projects:
  - Intake, triage and drafting (legal and medical front office, property management requests)
  - Document and knowledge assistants grounded in company files (the career-agent pattern)
  - Scheduling, follow-up and CRM hygiene agents
  - Reporting agents that pull from several SaaS tools into a weekly owner briefing
- **Proof points:** the Cassian MCP architecture, the career agent, the OpenBrain integrations.
- **Price:** **$6,000–$15,000 per workflow**; multi-workflow programs $15,000–$40,000.

### Line C: Company Memory and Private AI Platform
- **What:** stand up an **OpenBrain-style shared memory** (PostgreSQL + pgvector) and, where privacy demands it, a **self-hosted or sovereign AI stack**: SSO (Authentik/Entra), private networking (WireGuard/Tailscale/Pangolin), model routing (OpenRouter or local models), encrypted backups, and monitoring. Deploy on a small on-prem cluster or a VPS, with everything in Git.
- **Buyers:** healthcare, legal, financial and wealth firms, and any owner who doesn't want client data in consumer chatbots. Florida's AI and privacy legislation adds urgency.
- **Price:** **$8,000–$25,000** setup plus a managed retainer. Optional hardware pass-through.
- **License note:** Open Brain and OpsBrain are licensed FSL-1.1-MIT, which allows internal use and professional services to a client who uses the software under that license for their own internal purposes, but forbids offering it (or something substantially similar) as a commercial product or service. Line C is delivered as professional services into the client's own environment, owned and licensed by the client; DIO never hosts a memory service for clients, never resells OpsBrain, and never puts client data in OpsBrain. Have the business attorney confirm the approach before the first Line C sale.

### Line D: Managed Agent Operations (recurring base)
- **What:** a monthly retainer to monitor agents and infrastructure (Prometheus/Gatus-style checks), patch and upgrade, tune prompts and tools, review logs, add small enhancements, hold a quarterly business review with ROI tracking, and maintain recovery drills.
- **Tiers:**
  - **Essentials, $750/mo:** one workflow, monitoring, monthly patching, 2 hrs of changes
  - **Operate, $2,000/mo:** up to four workflows or a private platform, 6 hrs, quarterly review
  - **Partner, $4,500/mo:** fractional "Head of AI Operations," roadmap ownership, 15 hrs, priority response
- **Note:** spell out business-hours response targets. A solo founder must **not** promise 24/7.

### Line E: Utility and Field-Operations Intelligence (strategic vertical, phase 2)
- **What:** apply agents, GIS/LiDAR workflows and drone data (FAA Part 107) to **vegetation management, storm restoration logistics, vendor work-order QA, and safety and compliance documentation** for **utility contractors, tree-care and arborist companies, municipalities and co-ops**.
- **Why it's the deepest moat:** eight-plus years inside FPL/ACRT vegetation operations, NERC corridor knowledge, ISA certification, plus the hackathon recognition. UVM tech vendors (AiDash, Sheltera, GE Vernova) sell platforms to utilities. The **contractor and field layer** around them is underserved.
- **Constraint:** conflict of interest while employed at FPL/NextEra ([§13](11-risks.md)). Plan it as a **post-transition** vertical, or limit it to non-competing clients (for example, residential tree-care companies or out-of-territory co-ops) *only with written employer approval*.

### Line F: Training and workshops (marketing engine plus side revenue)
- **What:** half-day "AI agents for operators" workshops covering safe use, prompt and tool discipline, and when *not* to automate. Also team enablement on Claude Code / Codex for small dev shops.
- **Price:** **$1,500–$3,500 per session** for private teams; free or low-cost at chambers, the SBDC and FAU as lead generation.

### Line G: Custom Software Solutions (premium build offer)
- **What:** custom software where off-the-shelf SaaS doesn't fit. Examples: internal tools and dashboards that replace spreadsheets, client and tenant portals, scheduling and dispatch apps, offline-capable field apps for crews, APIs and integrations between SaaS tools, and AI-enabled applications with agents and MCP tools built in. Every project starts with a **build-versus-buy check**. DIO recommends SaaS when it is enough.
- **How it's delivered:**
  1. **Discover and design:** solutions architect, business analyst and UX designer produce requirements, architecture, a clickable prototype and an estimate.
  2. **Build and test:** developers (full-stack, back-end/API, mobile) and QA work in short sprints with weekly demos, all in the client's repository.
  3. **Release handoff:** the engineering lead signs off a standard package: an image with an immutable digest, deployment spec, config by name, health checks, migrations with rollback, runbook and test results.
  4. **Deploy and operate:** the **platform/DevOps team deploys** through GitOps (staging, then production), verifies and owns rollback, then runs the app under a care plan.
- **Why it fits:** Cassian (a Node app with tests, SSO, an image pipeline and GitOps delivery to K3s) and the dautel.io site already show the full path from code to running service. Most small dev shops stop at "it works on my laptop." DIO's edge is that the software arrives **already operable**: monitored, recoverable, documented.
- **Price:**
  - **Discovery and prototype sprint:** $3,500–$7,500 (credited to the build)
  - **Internal tool or MVP:** $15,000–$50,000
  - **Client portal or mid-complexity app:** $50,000–$150,000
  - **Software Care plan** (hosting operations, patching, monitoring, small fixes): 15–20% of build cost per year, billed monthly (typically $500–$3,000/mo)
- **Capacity guardrail:** while DIO is a side practice, take only internal tools and MVPs under about $50K, delivered with contract developers. Take larger platforms only once the phase-2 team exists. Fixed-price builds always follow a paid discovery; scope changes go through change orders, and estimates carry 15–20% contingency.

### Line H: Lean Six Sigma Process Improvement ("fix first, then automate")
- **The principle:** automating a broken process just makes the mistakes happen faster. DIO maps, measures and fixes the process first (removing waste, proving root causes with data, standardizing the work), then automates what is left, and keeps improving it.
- **Built into every build:** Lines B (agent workflows) and G (custom software) start with a **fix-first readiness check** (process P33). If the process isn't ready, it goes through a Kaizen event or a DMAIC project before design starts. The Readiness Assessment (Line A) now includes a waste walk and process health check.
- **Offers:**

  | Offer | What the client gets | Price *(est.)* | Process |
  | --- | --- | --- | --- |
  | **Process Health Check** | SIPOC, current-state map, baseline metrics, waste and bottleneck analysis, readiness verdict | $2,500–$5,000 (1–2 weeks) | P33 |
  | **Kaizen rapid improvement event** | 2–5 day facilitated event with the client team; changes implemented on the spot; 30-day follow-up | $6,000–$15,000 | P35 |
  | **DMAIC improvement project** | Charter → measured baseline → proven root causes → piloted fix → control plan and SOPs | $12,000–$40,000 (6–12 weeks) | P34 |
  | **Fix-and-automate bundle** | Health check or Kaizen, then the automation or software build on the fixed process | Bundle discount of about 10% | P33 → P34/P35 → P05/P09 |
  | **Continuous improvement retainer** | Fractional CI lead: monthly PDCA, control charts on key processes, kaizen coaching | $1,500–$4,000/month | P36 method, applied to the client |
  | **Lean fundamentals workshop** (Line F) | Half-day "fix first" training for owners and teams | $1,500–$3,500 | P12 |

- **Why it fits:** Lean Six Sigma Green Belt, an MBA in Operations Management, utility operations (vendor workload, budgets, storm restoration) and Army leadership. Few AI consultancies can do process improvement properly, and few process consultants can build the automation afterwards. DIO does both, and uses the same discipline internally (QA loops, andon rule, monthly PDCA).
- **Readiness check pricing:** every Line B or G quote includes the fix-first readiness check (about 1–2 days of work, priced into the build) unless a Readiness Assessment or Process Health Check covered the process in the last 6 months. A check that finds a broken process leads to a separately priced Kaizen event or DMAIC project.
- **Pricing note:** no reliable public rate card exists for small-business Lean Six Sigma consulting, so prices are estimates anchored to the AI assessment and build bands in §3.3 and to Black Belt salary levels ([§11](08-staffing.md)). Validate them with the first 3–5 clients.
- **Guardrails:** DIO teaches Lean and Six Sigma methods but does not issue belt certifications. Savings are claimed only when measured against a baseline. Process problems are never blamed on people.

### Not recommended (for now)
- **Generic chatbot agency** work: commoditized, low margin, and against the brand.
- **Full 24/7 MSP** service: not viable solo. Partner instead.
- **Building DIO's own SaaS product** first: possibly later (a company-memory product, built independently because Open Brain and OpsBrain are FSL-licensed; see [§13](11-risks.md)), but services fund and validate it first. (Custom software built *for clients* under Line G is different: the client pays for it and owns it.)

---

## 6. Business model and pricing strategy

**The value ladder:**

```
Free 30-min AI fit call
   → Readiness Assessment ($2.5K–$4.5K, credited)
      → Governed Workflow build ($6K–$15K) / Private Platform ($8K–$25K)
         → Managed Agent Operations ($750–$4.5K/mo)
            → Expansion builds + workshops

Process improvement path (Line H):
Process Health Check ($2.5K–$5K)
   → Kaizen event ($6K–$15K) or DMAIC project ($12K–$40K)
      → Automation or software build on the fixed process (Lines B / G)
         → Continuous improvement retainer ($1.5K–$4K/mo)

Custom software path (Line G):
Discovery & prototype sprint ($3.5K–$7.5K, credited)
   → Build: internal tool / MVP ($15K–$50K) or portal / platform ($50K–$150K)
      → DevOps deployment
         → Software Care plan (15–20% of build per year, monthly)
```

**Principles:**
- **Fixed fees for scoped work, retainers for operations.** Avoid hourly billing except for small change requests ($175/hr floor, inside the independent band).
- **Every build ships with a runbook, tests and a recovery procedure.** This is the differentiator; make it visible in proposals.
- **The client owns the code and infrastructure** (their GitHub org and cloud accounts). Lock-in comes from trust, not hostage-taking. This also lowers the buyer's perceived risk.
- **Pass-through tool and model costs** with a clear monthly estimate. No hidden markup, or a disclosed management fee.
- **Raise prices** once two or three case studies exist (target: assessments at $5K and builds from $10K by 2028).

---

### 3.3 Pricing benchmarks (2026 US)

| Engagement | Market range | Sources |
| --- | --- | --- |
| Independent AI consultant, hourly | $150–$350/hr (freelancers $40–$150; boutiques $250–$600; Big Four $400–$800) | AIDOLS via Alice Labs (Oct 2026), ChanAutomation, Taskip |
| AI readiness assessment (SMB) | $2,000–$10,000 (mid-market $10K–$25K) | CloudMotiv, ChanAutomation, JanBask via OriginsHQ |
| Single-workflow build ("quick win") | $2,500–$15,000 | CloudMotiv, Iternal |
| Multi-workflow implementation | $10,000–$75,000 | CloudMotiv, ChanAutomation |
| Fractional AI / managed retainer | $1,500–$8,000/mo for SMBs ($500–$1,500 at the low end) | Iternal, CloudMotiv, Taskip |
| Managed AI operations (mid-market) | $5,000–$25,000/mo | Alice Labs |
| Custom software: simple internal tool | $10,000–$50,000 (1–3 months) | Leads360 (2026), Shimira IT (Nov 2026) |
| Custom software: MVP | $15,000–$80,000 (2–4 months) | Leads360, Shimira IT |
| Custom software: mid-complexity platform | $75,000–$250,000 (4–9 months); Clutch verified average ~$132K over ~13 months | Shimira IT, Clutch via FullStack (Oct 2026) |
| US software bill rates | Mid-level dev $90–$130/hr; senior/architect $130–$200+/hr; Miami $80–$145/hr; US agency blended $150–$250/hr | Leads360, Shimira IT |
| Software maintenance | 15–25% of build cost per year | Leads360, Shimira IT |

**Market norm:** a fixed-fee discovery or assessment first, then a fixed-scope build, then a retainer. Buyers prefer fixed fees when the scope is unknown.

## 8. Remote services: go-to-market

Nearly everything DIO delivers is remote by nature: agents, MCP integrations, GitOps platforms and managed operations all run over secure connections. Erich already runs his own lab remotely through Pangolin/Newt tunnels, WireGuard and SSO. Remote delivery widens the market from one county to the whole country (and English-speaking international clients), and it fits a side practice better than on-site work because it allows async, evening and weekend delivery.

### 8.1 Which offers travel well remotely

| Offer | Remote fit | Notes |
| --- | --- | --- |
| **A. Readiness Assessment** | High | Video interviews, screen-share process walkthroughs, async questionnaires and a recorded readout. Sell a **"Remote AI Ops Assessment"** at the same price |
| **B. Governed Agent Workflows** | Very high | Built in the client's GitHub org and cloud accounts; weekly demo calls |
| **C. Company Memory / Private AI Platform** | High (cloud/VPS), medium (on-prem) | Cloud or VPS deployments are fully remote. On-prem hardware can ship pre-built ("lab-in-a-box") with remote setup over a tunnel, or be installed by a local MSP partner |
| **D. Managed Agent Operations** | Very high | Monitoring, patching and tuning are remote by definition. Bill as a subscription |
| **E. Utility / field-ops intelligence** | Medium | Data and GIS work is remote; field validation needs local partners or travel |
| **G. Custom software** | Very high | Discovery workshops over video; sprints with recorded demos; everything in the client's repository; DevOps deploys to the client's own cloud account or hardware (client confidential data never sits in DIO systems) |
| **F. Workshops** | High | Live virtual cohorts and recorded courses; scales beyond one room |

### 8.2 Remote-specific products (productized for scale)

Remote buyers have never met you, so they buy **clearly packaged, fixed-price products** more readily than open-ended consulting:

1. **"Agent Safety Audit" ($1,500, 1 week, fully async):** review an existing AI or agent setup (credentials, permissions, MCP servers, logging, recovery) and deliver a scored report with fixes. This is a low-friction first purchase for remote clients and draws directly on the Cassian and homelab practices.
2. **"MCP Integration Sprint" ($5,000–$9,000, 2–3 weeks):** connect one internal system or SaaS tool to the client's agents (Claude, ChatGPT, Codex, OpenClaw and others) through a secure, identity-scoped MCP server, with tests and docs. Demand for MCP work is visible on marketplaces in 2026, and few providers bring access-control discipline to it.
3. **"Company Memory Starter" ($7,500):** an OpenBrain-style shared memory deployed into the client's cloud, connected to two agent runtimes, with a curation guide. The client owns and licenses what is deployed (see the Line C license note).
4. **"GitOps Platform Launch" ($8,000–$20,000):** for small dev teams, covering K3s/managed Kubernetes, Flux, CI/CD, secrets, monitoring and a recovery runbook. Modeled on the homelab pipeline.
5. **"Agent Workflow Coaching" ($1,200/mo, 4 sessions):** for developers and technical founders adopting Claude Code, Codex and multi-agent coordination (the Herdr/tmux and Paperclip evaluations become curriculum).
6. **Remote retainers (Line D):** identical tiers, sold as a subscription with a monthly async report and video review.
