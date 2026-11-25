"""Skills: legal, finance and people; products, training and the team itself."""

BUSINESS = {
"contract-review": dict(
 title="Contract review", category="Legal, finance and people",
 summary="Review a contract or client redline clause by clause, rate each risk, propose fallback language and flag what a licensed attorney must see.",
 description="Review a contract, client redline or template (MSA, SOW, NDA, DPA, BAA, partner, subcontractor or lease) clause by clause against the firm's standard positions: scope, payment, IP and ownership, liability cap, indemnity, warranty, insurance, data and security, termination and governing law. Rate each issue, propose fallback language, and mark it for review by a licensed Florida attorney.",
 body="""## When to use

Before signing anything, when a client sends redlines, and when drafting or updating a template.

## Standard positions (what we want)

| Clause | Our position | Walk-away |
| --- | --- | --- |
| Scope | Fixed deliverables with acceptance criteria; changes by written change order | Open-ended "and anything else needed" |
| Payment | 50% deposit on fixed-fee work; net 15–30; late fee | Net 90, or payment only on "satisfaction" |
| IP and ownership | Client owns deliverables on full payment; DIO keeps its pre-existing tools and know-how, licensed to the client | Assignment of all DIO IP, including tools and templates |
| Liability | Capped at fees paid in the last 12 months; no consequential damages | Unlimited liability |
| Indemnity | Mutual, limited to third-party claims from each party's own fault | One-way indemnity for anything |
| Warranty | Workmanship warranty: defects against the acceptance criteria, reported within the warranty period (default 30 days), fixed at no charge; no warranty of AI model behavior beyond the tested criteria | Guarantees of outcomes or accuracy |
| Insurance | E&O and cyber at amounts we actually carry | Limits we don't carry |
| Data and security | Client data stays in client systems; least-privilege access; breach notice duties both ways | Unlimited audit rights or data in our systems |
| Non-solicitation | Mutual, 12 months, employees only | Broad non-compete on our work |
| Termination | Either side with notice; paid for work done | No payment for work done |
| Law | Florida; Palm Beach County venue | Foreign venue without reason |

## Method

1. **Read the whole document** once before marking anything.
2. **Clause by clause**, compare with the positions above; quote the clause.
3. **Rate** each issue: high (could cost the business or breach a law), medium (unfavorable), low (wording).
4. **Propose** fallback language for every high and medium issue.
5. **Check fit** with how we actually work (support hours, no 24/7, the employer boundary) and with insurance (`risk-register`).
6. **List questions** for the licensed attorney.

## Output

An issue table (clause, quote, risk, why, proposed language), a plain-English summary, questions for outside counsel, and the recommendation: sign, sign with changes, or don't sign.

**Every output carries:** "Draft for review by a licensed Florida attorney. Not legal advice." High-risk items (litigation, a regulator, an employment conflict, a HIPAA breach) go to Erich and human counsel at once.
"""),

"florida-business-compliance": dict(
 title="Florida business compliance", category="Legal, finance and people",
 summary="Keep the firm's filings, local business tax receipts, sales tax, employer registrations and data-law duties current in Florida.",
 description="Check and keep the firm compliant in Florida and Palm Beach County: Sunbiz LLC and annual report, fictitious name, City of Boynton Beach and Palm Beach County business tax receipts, sales tax on information services and goods, reemployment tax and workers' compensation thresholds, and data-law duties (FIPA breach notice, HIPAA, Florida Digital Bill of Rights, AI bill status). Use for filings, renewals, new offers and hiring.",
 body="""## When to use

Opening the business, the annual renewals, launching a new kind of offer (reports, hardware, hosting), hiring the first employee, and whenever a client asks about compliance.

## Read first

- `docs/07-permits-and-licenses.md`: the full list with costs, sources and dates. Recheck any rule older than six months.

## Calendar

| When | What |
| --- | --- |
| January 1 to May 1 | Sunbiz LLC annual report ($138.75; $538.75 after May 1) |
| July 1 to September 30 | Palm Beach County local business tax receipt renewal (late from October 1) |
| City renewal date | City of Boynton Beach business tax receipt renewal (confirm the date with the city) |
| Quarterly | Estimated federal taxes; reemployment tax reports once registered |
| Before each new offer | Sales-tax check: information services sold to many customers and tangible goods are taxable in Florida; one-client consulting and SaaS generally aren't |
| First payroll | Register for reemployment tax ($1,500 in wages in a quarter, or an employee in 20 weeks) |
| Fourth employee | Workers' compensation (non-construction; LLC members who are officers count) |

## Data-law duties in the work

- **Florida Information Protection Act (s. 501.171):** breach notice to affected people within 30 days; the Attorney General at 500 or more.
- **HIPAA:** a BAA before any patient data; otherwise decline.
- **Florida Digital Bill of Rights:** mainly companies over $1 billion in revenue; watch for duties passed down by contract.
- **Florida AI law:** no general statute as of November 2026 (CS/SB 482 died in the House on March 13, 2026; SB 484 covers hyperscale data centers). Check before relying on this.
- **Calls and texts:** the Florida Telephone Solicitation Act and federal TCPA need prior express written consent for automated calls and texts.

## Output

A compliance status table (item, status, due date, owner, source) and the actions due in the next 90 days. Mark anything that needs the CPA or the attorney. This is research, not legal or tax advice.
"""),

"employer-boundary-screen": dict(
 title="Employer-boundary screen", category="Legal, finance and people",
 summary="Screen any prospect, partner, project or content for conflicts with Erich's employment at FPL/NextEra, and decline when unsure.",
 description="Screen a prospect, partner, project, piece of content or data source against the employer boundary while Erich is employed at FPL/NextEra: no utility clients, no vegetation-management or line-clearance contractors, no known FPL/NextEra vendors, no competing work, and never employer time, equipment, data or confidential information. Decline when unsure. Use before scoping, partnering or publishing anything near utilities, tree care or field services.",
 body="""## When to use

Before scoping any prospect in field services, tree care, landscaping, electrical work, utilities or energy; before any partnership or subcontract; before publishing content about utilities or field operations; and whenever a data source might come from the employer.

## The rule

While Erich is employed at FPL/NextEra:

- **No** utility clients; no vegetation-management or line-clearance contractors; no company known to be an FPL/NextEra vendor; no work that competes with the employer.
- **Never** use employer time, equipment, data, contacts or confidential information.
- **Phase-2 work** (Line E, utility and field-operations intelligence) waits for written employer clearance or the end of the employment.

## Method

1. **Identify** the business: what it does, who its customers are, whether it works for utilities or does electrical or tree work.
2. **Check** public sources for any FPL/NextEra vendor or contractor relationship.
3. **Classify:**
   - **Clear:** no connection (for example a law firm or a dental practice).
   - **Flag for Erich:** field services, tree care, landscaping, HVAC with electrical work, energy, or anything adjacent.
   - **Decline:** a utility, a vegetation-management or line-clearance contractor, a known vendor, or any doubt that can't be resolved.
4. **Record** the result with the evidence; a flagged deal can't move to scoping until Erich clears it.

## Output

The screen result (clear, flagged or declined), the evidence and the date. **When unsure, decline.**
"""),

"break-even-and-cash-flow": dict(
 title="Break-even and cash-flow model", category="Legal, finance and people",
 summary="Model costs, revenue scenarios, break-even, cash flow and the full-time and hiring triggers.",
 description="Build or update the firm's financial model: fixed and variable costs, revenue scenarios by service line, break-even, a 12-month cash-flow forecast, the full-time transition trigger and the hiring trigger, with every assumption labeled. Use for pricing decisions, hiring, the full-time move, new offers and lender or partner questions.",
 body="""## When to use

Deciding prices, a hire, the full-time move, a new offer or a big expense; and every quarter to refresh the forecast.

## Read first

- `docs/06-startup-and-operating-costs.md` (costs and revenue scenarios), `docs/05-services-and-pricing.md`, `docs/08-staffing.md` (loaded cost and hiring math).

## Method

1. **Fixed costs per month:** insurance, tools and APIs, workspace, accounting, marketing baseline (the docs estimate about $335–$720 a month home-based).
2. **Variable costs:** pass-through model and hosting costs, subcontractors, payment fees (about 3% on cards).
3. **Revenue lines:** assessments, builds, retainers (MRR), workshops, process improvement; price × volume per month, with a ramp.
4. **Three scenarios:** conservative, expected, strong. Label every input *(est.)* unless it's a signed contract.
5. **Break-even:** monthly fixed costs ÷ contribution margin per engagement; show how many assessments or retainers cover the fixed costs.
6. **Cash flow (12 months):** deposits and payment timing (50% upfront, net 15–30), taxes set aside (about 25–30% of profit *(est.)*), the reserve.
7. **Triggers:**
   - **Full-time:** retainer MRR of $8–10K for three consecutive months, plus six months of personal expenses in reserve, plus at least two signed builds.
   - **Hiring:** revenue the person will deliver or protect of at least 1.5 × their loaded cost, plus three months of that cost in cash.
8. **Sensitivity:** which two inputs move the result most.

## Output

A model table by month, the break-even point, the scenario summary, trigger status, and the key assumptions. Spreadsheets are fine; show the formulas, not just results.

## Quality checks

- The model ties to actual bookkeeping for past months.
- `cpa-bookkeeper` checks tax assumptions.
"""),

"monthly-finance-close": dict(
 title="Monthly finance close", category="Legal, finance and people",
 summary="Close the books each month: reconcile, invoice, chase collections, review margins and set aside taxes.",
 description="Run the monthly finance close and billing: categorize and reconcile transactions, send invoices (deposits, milestones, retainers), chase overdue payments politely and on schedule, review revenue, margin and cash against the plan, set aside taxes and prepare the business review. Use at each month end and for billing questions.",
 body="""## When to use

The first five business days of every month, and whenever an invoice is due or overdue.

## Method

1. **Reconcile:** every bank and card transaction categorized and matched to receipts; business and personal kept apart.
2. **Invoice:** deposits on signature, milestones on acceptance, retainers on the 1st, pass-through costs at cost with the provider's invoice attached.
3. **Collections:** a friendly reminder 3 days before due; on the due date; at 7 days late; at 15 days a call; at 30 days pause non-critical work (as the SOW allows) and tell Erich.
4. **Review:** revenue by service line, gross margin per engagement (hours used against the estimate), cash, AR aging, MRR and its change.
5. **Taxes:** set aside the agreed percentage; track estimated payment dates; note sales tax only if something taxable was sold.
6. **Business review:** a one-page summary for the operating cadence: numbers against plan, surprises, and decisions needed.

## Output

Closed books for the month, invoices sent, an AR aging list with actions, and the one-page business review.

## Quality checks

- Invoice math matches the SOW; numbers tie to the bank.
- **Every payment out and every refund or write-off is Erich's decision.**
"""),

"risk-register": dict(
 title="Risk register", category="Legal, finance and people",
 summary="Keep the risk register: likelihood, impact, owner and mitigation for each risk, mapped to insurance and reviewed quarterly.",
 description="Build and review the firm's risk register: identify business, legal, security, delivery, vendor and personal risks, rate likelihood and impact, assign owners and mitigations, map each to insurance coverage or contract terms, and review every quarter. Use for quarterly risk reviews, insurance decisions and before big commitments.",
 body="""## When to use

Every quarter, before buying or renewing insurance, before a large contract, and after any incident.

## Read first

- `docs/11-risks.md` (the current risks and mitigations), `docs/06-startup-and-operating-costs.md` (insurance costs).

## Method

1. **Identify** risks in each area: legal and contract, security and data, delivery, vendor and model, people (founder availability, hurricane season), money, reputation, regulation, the employer boundary.
2. **Rate** likelihood and impact 1–5; score = likelihood × impact.
3. **Mitigate:** avoid, reduce, transfer (insurance, contract terms) or accept. Every risk scoring 12 or more needs a mitigation and an owner.
4. **Insurance map:** which policy covers it (technology E&O, cyber, general liability), the limit, the deductible, and gaps against what contracts require.
5. **Review:** what changed since last quarter, which mitigations worked, new risks.

## Output

```markdown
| Risk | Area | L | I | Score | Mitigation | Insurance / contract | Owner | Status |
```

Plus a short summary of the top five risks and any coverage gaps. Anything accepting financial risk goes to Erich.
"""),

"hiring-kit": dict(
 title="Hiring kit", category="Legal, finance and people",
 summary="Hire and onboard well: hiring trigger check, job description, pay band, structured interviews, onboarding and offboarding.",
 description="Run hiring for employees, contractors and subcontractors: check the hiring trigger, write the job description and pay band, design structured interviews and a work sample, check references, prepare the offer or contract (IP assignment, confidentiality), and run onboarding and offboarding. Use before any hire or contractor engagement.",
 body="""## When to use

When revenue suggests adding a person (contractor first, then employee), and when anyone joins or leaves.

## Read first

- `docs/08-staffing.md` (phases, salary ranges and the hiring math), `docs/07-permits-and-licenses.md` (reemployment tax and workers' compensation).

## Method

1. **Trigger check:** revenue the person will deliver or protect is at least 1.5 × their loaded cost, and three months of that cost is in cash (`break-even-and-cash-flow`). Erich decides every hire.
2. **Job description:** the outcomes the role owns in the first 90 days, the must-have skills, the nice-to-haves, the pay band from `docs/08-staffing.md` (published, fair and transparent), remote or local.
3. **Sourcing:** referrals, FAU graduates and the MBA network, veteran transition programs, KubeCraft and CNCF communities, partner MSPs.
4. **Structured interviews:** the same questions for every candidate, scored against a rubric; a short paid work sample that resembles the real work.
5. **References:** two, focused on the work sample skills.
6. **Contract:** for contractors and subcontractors, IP assignment (to DIO or the client), confidentiality, security duties, and the client's approval of subcontractors where the MSA requires it.
7. **Onboarding:** accounts with least privilege, the values and the fix-first method, a buddy, and a 30-60-90 day plan.
8. **Offboarding:** access removed the same day, devices and data returned, knowledge handed over, a respectful exit conversation.

## Output

A job description, interview kit and rubric, work sample brief, onboarding checklist, and offboarding checklist. No personal data of candidates goes into this repository.
"""),

"vendor-and-tool-approval": dict(
 title="Vendor and tool approval", category="Legal, finance and people",
 summary="Evaluate and approve a tool, vendor or AI model: need, cost, security, data terms, license, lock-in and exit.",
 description="Evaluate a new tool, SaaS vendor, AI model or provider before the firm or a client relies on it: the need, total cost, security and data terms (training on data, retention, BAA), license limits, lock-in and the exit path, then record an approval with conditions. Use before buying, subscribing or putting client data into any new tool.",
 body="""## When to use

Before the firm adopts a new tool or model provider, before recommending one to a client, and when a vendor changes its terms or prices.

## Method

1. **Need:** the problem, and whether an approved tool already solves it.
2. **Cost:** monthly and yearly, per seat or per token, at today's and next year's volume; pass-through to clients at cost.
3. **Security:** SSO and MFA, encryption, incident history, certifications (SOC 2, ISO 27001) where relevant.
4. **Data terms:** does the vendor train on our or clients' data? Retention and deletion? Where is data stored? Will it sign a BAA or DPA if needed?
5. **License:** what the license allows (for example Open Brain and OpsBrain are FSL-1.1-MIT: internal use and client-owned deployments, never a competing product or hosted service).
6. **Lock-in and exit:** data export, open formats, and the cost of leaving.
7. **Fallback:** for AI models, a second provider or model the design can switch to.
8. **Decide:** approved, approved with conditions, or rejected; Erich approves anything that costs money.

## Output

A one-page evaluation and the approval record with conditions and a review date.
"""),
}

PRODUCTS = {
"product-offer-design": dict(
 title="Productized offer design", category="Products, training and team",
 summary="Turn repeated client work into a fixed-scope, fixed-price offer with a one-pager, delivery checklist and success measures.",
 description="Design a productized offer: find work clients ask for repeatedly, define the fixed scope, deliverables, timeline and price, write the one-pager and the delivery checklist, set the success measures, check the license of anything it builds on, and plan a pilot. Use for new offers (like the Agent Safety Audit) and for deciding what should become software.",
 body="""## When to use

The same kind of engagement has been sold or asked for three or more times, or a remote buyer needs something they can buy without a sales call.

## Read first

- `docs/05-services-and-pricing.md` (current offers and productized products), `docs/03-target-customers.md`.

## Method

1. **Evidence:** the past engagements or requests this would have served; what they had in common.
2. **Buyer and promise:** who it's for, the problem, the outcome in one sentence.
3. **Fixed scope:** what's included and excluded; the inputs the buyer provides.
4. **Deliverables and timeline:** a short list, with a delivery checklist the team follows every time.
5. **Price:** from the effort estimate (`pricing-and-estimating`) and the market range; a price that makes it an easy first purchase where it's an entry offer.
6. **Success measures:** for the buyer (the outcome) and for us (margin, time to deliver, conversion to the next step).
7. **License check** for anything it builds on.
8. **Pilot:** two or three buyers at a founding price in exchange for feedback and a case study; review after the pilot.
9. **Retire** offers that don't sell or don't make margin after two quarters.

## Output

A one-pager, the delivery checklist, the price and its rationale, the success measures and the pilot plan. Erich approves new prices.
"""),

"workshop-design": dict(
 title="Workshop design", category="Products, training and team",
 summary="Design and run workshops, courses and coaching: learner personas, objectives, exercises, materials and feedback.",
 description="Design and deliver a workshop, course, webinar or coaching program (Line F, $1,500–$3,500 a session; coaching $1,200 a month): the learner persona, measurable objectives, a run of show with hands-on exercises, materials in the Dautel Design System, a feedback survey and improvements after each session. Use for client training, free community workshops and lead-generation events.",
 body="""## When to use

Client training on new agents or processes, Lean fundamentals, Agent Workflow Coaching, and free workshops for local businesses, chambers and veterans.

## Method

1. **Learners:** who they are, what they already know, what they fear (job loss, mistakes), and what they need to do differently afterwards.
2. **Objectives:** three to five, each starting with a verb ("map their intake process", "review an agent's draft safely").
3. **Run of show:** 10-minute segments; at most 20 minutes of talking before an exercise; real examples from their industry.
4. **Exercises:** hands-on, with their own processes where possible (a SIPOC, a waste walk, reviewing agent output, writing a prompt with guardrails).
5. **Materials:** slides and handouts in the Dautel Design System; a one-page cheat sheet to keep.
6. **Safety and honesty:** what AI shouldn't be used for; privacy rules; no hype.
7. **Feedback:** a three-question survey at the end; what to change next time.
8. **Follow-up:** a recap email, the materials, and one clear next step (a fit call, a health check).

## Output

The run of show, slides, exercises, handout, survey, and the post-session notes.
"""),

"utility-field-ops": dict(
 title="Utility and field-operations intelligence (phase 2)", category="Products, training and team",
 summary="Phase 2 only: GIS, LiDAR, imagery and drone analysis for vegetation management, storm logistics and field documentation, once the employer boundary allows.",
 description="Phase-2 work for Line E, utility and field-operations intelligence: GIS and remote-sensing analysis (LiDAR, imagery, drone data) for vegetation management, storm logistics and field documentation, with correct projections, licenses and field validation. Gated: no work until Erich has written employer clearance or has left FPL/NextEra. Use only for planning and public-research preparation until then.",
 body="""## When to use

**Today: planning only.** Market notes from public sources, data-source catalogs and processing recipes. No utility clients, no vegetation-management or line-clearance contractors, no FPL/NextEra vendors, and never employer data or confidential information (`employer-boundary-screen`).

**After clearance:** engagements with utility contractors, municipalities and co-ops outside the restricted list.

## Method (when allowed)

1. **Question:** the field decision the analysis supports (where to trim, where crews go first after a storm, what to inspect).
2. **Data catalog:** each source, its license, resolution, date and coordinate reference system; public sources first (USGS 3DEP LiDAR, NAIP imagery, county GIS).
3. **Processing:** reproject to one CRS; classify LiDAR (ground, vegetation, structures); measure clearance or canopy change; document every step so it can be rerun.
4. **Drone work:** FAA Part 107 rules, airspace checks, landowner permission, and privacy.
5. **Validate** a sample in the field; report accuracy honestly.
6. **Deliver** maps and tables the crews can use on a phone, plus the method.

## Output

Today: a phase-2 brief (market, buyers, public data, the clearance needed). Later: analysis maps, data tables, the method and its accuracy.
"""),

"agent-and-skill-authoring": dict(
 title="Agent and skill authoring", category="Products, training and team",
 summary="Create or improve agents and skills in this repository the right way: data in tools/, the official frontmatter, then build and check.",
 description="Create a new agent or skill, or improve an existing one, in this repository: follow the official Claude Code subagent and skill formats, edit the data in tools/team.py and tools/skills.py (never the generated .claude/ files), give agents least-privilege tools, a clear description, skills, a knowledge folder, a brain and a persona, then run python3 tools/build.py and --check and send the change to review. Use whenever the team needs a new role or method, or an agent answered badly.",
 body="""## When to use

A new role or repeatable method is needed, two agents overlap, or an agent or skill produced a wrong or weak answer.

## Read first

- The official docs: https://code.claude.com/docs/en/sub-agents and https://code.claude.com/docs/en/skills. Fields change; check them.
- `docs/expert-roster.md` and `docs/agent-brains.md` for what already exists.
- `tools/README.md` for how the build works.

## Rules for agents

- **One clear job.** The `description` says when to use the agent (start with "Use for ..." or "Use when ..."; add "proactively" only when the main session should delegate on its own).
- **Least-privilege tools:** read-only advisors get `Read, Grep, Glob, WebSearch, WebFetch`; writers add `Write, Edit`; builders add `Bash`. Only the orchestrator gets `Agent`.
- **Skills:** list the skills the agent uses (they are preloaded into its context); keep it to the ones it really needs.
- **Brain:** `opus` for strategy, legal, finance, security, architecture and QA judgment; `sonnet` for most specialist work; `haiku` for fast, high-volume, well-defined work. Give the reason.
- **Knowledge folder:** `knowledge/<agent>/` with a README saying what belongs there.
- **Persona:** a Star Trek name no other agent uses, a voice and a working style. Agents never claim to be people.
- **Guardrails stay:** decision rights, the privacy lock and the employer boundary are in every agent and never weakened.

## Rules for skills

- A skill is a **method**, reusable by several agents: when to use it, what to read first, numbered steps, the output format and quality checks.
- `name` is lowercase with hyphens and matches the folder; the `description` says what it does **and when to use it**, under about 1,000 characters.
- Keep `SKILL.md` under 500 lines; move long reference material into a separate file in the skill folder.

## Method

1. Read the request and the evidence (for a fix: the bad answer, what was expected, and the instruction or document that caused it).
2. Edit `tools/team.py` (agents) or the `tools/skills_*.py` files (skills).
3. Run `python3 tools/build.py`, then `python3 tools/build.py --check`.
4. Test: ask the agent a question that would have failed before.
5. Send the change to `quality-reviewer`, then commit with a message that says what changed and why.
"""),
}
