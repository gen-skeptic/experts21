# Marketing and go-to-market

*Source: copied from the DIO business plan research in gen-skeptic/experts (`research/dautel-intelligent-operations-business-plan-research.md`, compiled November 19, 2026), updated November 25, 2026 where noted. Process numbers such as P33 refer to the DIO operating manual in that repository; in this repository the same methods are skills in `.claude/skills/`.*

Message, website, channels, lead magnets and the sales process, locally and nationally.

## 7. Marketing and go-to-market

### 7.1 Message architecture

- **Headline:** *Fix first, then automate.* Supporting line: *AI agents that your business can actually operate.*
- **Sub:** *We don't automate broken processes. We fix them with Lean Six Sigma, then connect AI agents to your real systems with clear access, human review and a recovery plan, so automation keeps working after the demo.*
- **Three pillars** (these map to the existing Agents, Infrastructure and Operations brand colors):
  1. **Agents** (blue): useful work, connected through MCP to your tools
  2. **Infrastructure** (mint): private, secure, yours
  3. **Operations** (lavender): reviewed, measured, recoverable
- **Proof voice:** keep the brand rule "no fake metrics." Turn it into a promise: *"Every claim on this site is backed by a running system. Every client gets the same standard."*

### 7.2 Website changes (dautel.io)

1. **Hero CTA:** "Book an AI fit call" (peach, the contact color) plus "See how we work."
2. **New `/services` page** with Lines A–H, "starting at" prices, and what's included, built in the Dautel theme.
3. **"How an engagement works"** timeline: Assess → Fix → Build → Operate and improve.
4. **Recast case studies for buyers:** add a "What this means for your business" block to Cassian (it's the client-facing agent pattern), OpenBrain ("company memory"), and the homelab ("the same change control I bring to your systems").
5. **Repurpose the career agent as a pre-sales agent** ("Ask whether AI fits my business"), still curated and rate-limited, with an option to book a call.
6. **Move the resume** to `/about`, framed as founder credentials.
7. **Industry landing pages** (law, medical, field services) for local SEO: "AI automation for law firms in Palm Beach County."
8. **Trust page:** security and data-handling principles (least privilege, no training on client data, client-owned infrastructure).

### 7.3 Channels (ranked by expected ROI for a side practice)

The marketing and social media team ([§11.4b](08-staffing.md), `marketing-director` and its agents) runs these channels. Everything passes QA before it's published; Erich approves spending, anything in his name, voice or likeness, and ethical questions.

| Channel | Tactics | Cadence |
| --- | --- | --- |
| **YouTube** | Build-in-public series ("Build it right", "Recover it"), business-owner explainers, Shorts cut from each video | 2 videos/month + 4–6 Shorts |
| **LinkedIn** (founder-led) | Short build-in-public posts (agent architecture diagrams, "what went wrong and how we recovered"), operations-to-AI translation posts, local business tips | 2–3 posts/week |
| **Referral partners** | 2–3 local **MSPs** and IT providers (DIO handles AI/agents, they handle desk and devices), **CPAs and attorneys** who advise SMB owners, web agencies | Monthly check-ins; 10% referral fee on first project |
| **Local presence** | Free workshops at chambers of commerce, **Florida SBDC at FAU**, FAU MBA network, BNI-style groups | 1 event/month |
| **Content and SEO** | Monthly long-form case study or guide on dautel.io; vertical landing pages; Google Business Profile | Monthly |
| **Technical community** | KubeCraft, CNCF/K8s meetups (South Florida), GitHub open-source pieces (sanitized MCP adapters, runbook templates) | Ongoing; builds credibility with the secondary ICP |
| **Marketplaces** (early only) | Upwork/Contra for 1–2 quick wins to bootstrap reviews and case studies | First 6 months only |
| **Email newsletter** | "Operator's AI brief": monthly, practical, no hype | Monthly |

### 7.4 Lead magnets
- **"AI Readiness Scorecard"**, a 15-question self-assessment on dautel.io that routes to a fit call.
- **"Agent Safety Checklist for Small Businesses"**: credentials, review, logging, recovery (drawn from the Cassian and homelab practices).
- **Workshop recordings.**

### 7.5 Sales process
1. Fit call (30 min, free): qualify budget, pain and owner commitment; screen for the employer boundary.
2. Proposal within 2 business days of the estimate: a fixed-fee assessment or Process Health Check.
3. Assessment readout ends in fix-first actions, a quoted build and a retainer recommendation.
4. Fix the process (Kaizen or DMAIC) where needed, then build with weekly demos, client acceptance on staging and Erich's production approval.
5. Handover: runbook, recovery test, retainer start.
6. Quarterly review: ROI tracked against assessment baselines, which is where expansion work comes from.

Every prospect, contact, conversation and deal is tracked in OpsBrain's built-in CRM, with stages that follow P02 (Prospect, Fit call, Qualified, Scoping, Proposal sent, Redlines, Won, Lost) and a weighted forecast. Flagged prospects can't reach Scoping until Erich clears the employer-boundary screen, and only Erich marks a deal won.

---

### 8.4 Remote marketing channels

| Channel | Remote tactics | Priority |
| --- | --- | --- |
| **LinkedIn (national reach)** | On Erich's founder profile, in his own voice: position him as "the operator's AI engineer." Post architecture breakdowns, "how I'd secure this agent" teardowns and short screen-recorded demos. Optimize the profile headline for "AI agent / MCP / DevOps consultant" | 1 |
| **Content plus SEO for national intent** | Long-form guides on dautel.io targeting non-local queries ("MCP server security checklist," "self-hosted AI for law firms," "shared memory for AI agents," "GitOps for small teams") | 1 |
| **Open source and GitHub** | Publish sanitized building blocks: an MCP server template with identity-bound auth, idempotency receipts and audit logging, OpenBrain-style memory starter, runbook templates. Stars and forks act as remote credibility; READMEs link to dautel.io | 1 |
| **YouTube / short video** | 5–10 minute walkthroughs ("Connecting three MCP servers to one family feed," "Recovering a K3s cluster from Git"). Good for trust and SEO; repurpose clips to LinkedIn | 2 |
| **Newsletter** ("Operator's AI brief") | National list; every issue ends with a productized offer | 2 |
| **Marketplaces** | **Upwork** and **Contra** for the first 3–5 reviews, using the Agent Safety Audit and MCP Integration Sprint as packaged listings; **Toptal** later for higher-rate technical engagements. Leave once referrals take over | 2 (first 6–9 months) |
| **Communities** | Answer questions in KubeCraft, CNCF Slack, r/kubernetes, r/selfhosted, r/LocalLLaMA, MCP/agent framework Discords. Help first, no pitching | 2 |
| **Podcasts and virtual talks** | Guest spots on DevOps, AI and small-business podcasts; virtual meetups and webinars. The "arborist and soldier turned AI operations engineer" story is memorable | 3 |
| **Directories** | Clutch, GoodFirms, Google Business Profile (service-area business), and vendor partner directories where available | 3 |
| **Cold outbound (targeted)** | Small, researched lists (e.g., 20 firms a week in one vertical) with a personalized Loom showing one specific automation idea for *their* business | 3 |

### 8.5 Website changes for remote buyers

- Say it in the hero: **"Based in South Florida. Working with teams across the US, fully remote."**
- Add a **"How remote engagements work"** page: kickoff call → async discovery → weekly demos → handover recording → retainer. List tools (Zoom/Meet, Loom, GitHub, shared docs) and time-zone coverage (US Eastern; overlap with Pacific until early afternoon).
- **Self-serve checkout** for the productized offers (Stripe payment links) plus a scheduling link. Remote buyers want to buy without a sales call for under-$2K items.
- **Security and access page:** how remote access to client systems works (least-privilege accounts, client-issued credentials, VPN/WireGuard or bastion access, MFA, access revoked at handover, no client data stored in DIO systems). This answers the biggest objection remote buyers have.
- **Social proof** that doesn't depend on geography: GitHub repos, recorded demos, written case studies, testimonials with company names (with permission).
- Keep the **career agent / pre-sales agent** available around the clock. It's a natural remote "front desk."

### 8.6 Remote operations requirements

- **Contracts:** state the governing law (Florida); include remote-access and data-handling terms in the MSA/DPA; take a deposit (50% upfront for fixed-fee work) through Stripe or ACH.
- **Sales tax and nexus:** consulting services are generally not taxed in Florida, but check how other states treat digital and SaaS-like deliverables (especially managed hosting) with an accountant before selling nationally.
- **Insurance:** make sure the E&O and cyber policy covers clients in all US states (and international clients if pursued).
- **Access hygiene:** a password manager with per-client vaults, hardware MFA keys, a separate work device or profile for client access, and access logs. These are the same disciplines already used in the homelab.
- **Async delivery cadence:** a weekly written update plus a short Loom; one standing 30-minute call. This suits evening and weekend hours while employed.
- **International clients (later):** watch payment fees, contract jurisdiction and data-transfer rules (e.g., GDPR for EU clients). Start US-only.

### 8.7 Local vs. remote mix (recommended)

| Phase | Local (South Florida) | Remote (US) | Rationale |
| --- | --- | --- | --- |
| **2027 H1** | 70% | 30% | Local trust and in-person workshops land the founding clients and case studies fastest; remote marketplace listings collect first reviews |
| **2027 H2 – 2028** | 50% | 50% | Productized remote offers and content start compounding; retainers can be delivered from anywhere |
| **2029+** | 30% | 70% | National content, open source and partner channels dominate; local work focuses on high-value on-prem and private-AI clients |

**Bottom line:** compete **locally on trust** (the in-person, operations-minded expert who will sit with the owner) and **nationally on specialization** (governed agents, secure MCP integrations, company memory and GitOps for small teams). The local market builds the case studies; the remote market scales the revenue.

---
