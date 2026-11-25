"""Skills: strategy and coordination, sales and clients."""

STRATEGY = {
"routing-plan": dict(
 title="Routing plan", category="Strategy and coordination",
 summary="Turn a question that spans several functions into a plan: which experts, what each answers, in what order, on which brain.",
 description="Plan which experts should answer a question that spans several functions, what each one must answer, which can run in parallel and which brain each needs. Use before asking the team anything that touches more than one area.",
 body="""## When to use

A question touches more than one function (for example legal and finance and delivery), or it's unclear who should answer it. The orchestrator uses this before delegating; the chief of staff prepares it when asked.

## Read first

- `docs/expert-roster.md`: every agent's one-line job and skills.
- `docs/agent-brains.md`: each agent's default brain and when to raise or lower it.

## Method

1. **Restate the question** in one sentence, and the decision it serves. If it hides several questions, split them.
2. **List the angles** the answer needs: legal, money, risk, technical, process, market, client, marketing, people.
3. **Pick the fewest experts** that cover every angle (usually 2 to 5). Prefer the specialist over a generalist; never add an agent just to be safe.
4. **Write each assignment:** the exact question for that expert, the inputs it gets (documents, earlier answers), and what a good answer must contain.
5. **Order the work:** run every expert whose inputs are ready **in parallel**; only wait when one expert needs another's output (for example the CPA needs the pricing model first).
6. **Pick the brain** for each assignment from the task-type table in `docs/agent-brains.md`. Raise one level for money, security, legal terms or client-final work; lower one level for routine work that a review will catch.
7. **Name the reviewer** if the answer will leave the team (a proposal, a price, a public claim): usually `quality-reviewer`, plus a specialist reviewer for its area.
8. **Flag the Chairman's decisions:** anything with financial or ethical considerations, any financial transaction and any final deployment to a customer goes to Erich with options and a recommendation.

## Output

```markdown
**Question:** ...
**Decision it serves:** ...

| # | Expert | Their question | Inputs | Brain | Runs |
| - | ------ | -------------- | ------ | ----- | ---- |
| 1 | `business-attorney` | ... | docs/07-permits-and-licenses.md | opus / high | parallel |
| 2 | `cpa-bookkeeper` | ... | answer 1 | opus / medium | after 1 |

**Review:** `quality-reviewer` (and ...)
**For Erich:** ... (or "none")
```

## Quality checks

- Every angle in step 2 has an owner; no two experts answer the same question.
- Parallel where possible; every dependency is real.
- No more than five experts unless the question truly needs more.
"""),

"decision-memo": dict(
 title="Decision memo", category="Strategy and coordination",
 summary="Frame a decision with options, facts, costs, risks and a recommendation, and say who decides.",
 description="Write a decision memo: the decision, the options, facts and assumptions, cost of each option, reversibility, risks, a recommendation with conditions and a review date, and who decides. Use for pricing, hiring, new services, large clients, the full-time move or any choice with money or ethics involved.",
 body="""## When to use

Any decision that commits money, changes what the firm sells, hires or ends work, or has an ethical angle. Also any cross-functional question the orchestrator has to settle.

## Read first

- `docs/05-services-and-pricing.md`, `docs/06-startup-and-operating-costs.md`, `docs/11-risks.md`, and the topic file for the decision.

## Method

1. **State the decision** as a question with a deadline ("Do we hire a contract developer for the Q2 build, by March 1?").
2. **Who decides:** Erich (Chairman) decides anything with financial or ethical considerations, every financial transaction and every final deployment to a customer. The orchestrator decides other cross-functional questions; a process owner decides inside its process.
3. **Options:** at least three, including "do nothing" or "wait". Make each one real, not a straw man.
4. **Facts and assumptions:** separate what is known (with a source and date) from what is assumed. Label estimates *(est.)*.
5. **For each option:** cost (one-time and monthly), revenue or savings, time to result, reversibility (one-way or two-way door), effect on Erich's hours, and the main risk.
6. **Cost of delay:** what waiting a month costs.
7. **Strongest counter-argument** to the recommended option, answered.
8. **Recommend** one option, with the conditions that would change the answer and a review date.

## Output

```markdown
# Decision: <question> (by <date>)
**Decides:** Erich (Chairman) | orchestrator | <owner>     **Reversible:** yes/no

| Option | Cost | Benefit | Time | Risk | Reversible |
| ------ | ---- | ------- | ---- | ---- | ---------- |

**Facts (sourced):** ...
**Assumptions:** ...
**Recommendation:** ... **because** ...
**Strongest objection and answer:** ...
**Would change our mind:** ...
**Review on:** <date>
```

## Quality checks

- Numbers trace to a source or are marked as estimates.
- The recommendation follows from the table, not from enthusiasm.
- The memo is honest about what isn't known.
"""),

"operating-cadence": dict(
 title="Operating cadence", category="Strategy and coordination",
 summary="Run the weekly priorities, the monthly report to the Chairman and quarterly planning.",
 description="Run the firm's operating rhythm: the weekly priorities memo, the monthly operating report to Erich and quarterly goals and planning. Use for status roll-ups, priorities, KPIs, monthly reviews and quarterly plans.",
 body="""## When to use

Every Monday (weekly priorities), the first week of each month (report to the Chairman), and the last two weeks of each quarter (quarterly plan). Also when Erich asks "where do we stand?".

## Read first

- `docs/12-90-day-plan-and-open-questions.md` (current plan), `docs/06-startup-and-operating-costs.md` (revenue scenarios and the full-time trigger), `docs/10-operations-and-delivery.md` (capacity).

## Method

**Weekly (15 minutes to read):**
1. KPI snapshot: pipeline value and next steps, monthly recurring revenue, cash, billable hours used against the 10–12 hour weekly budget, overdue invoices.
2. Delivery status: each engagement green, amber or red, with the one blocker that matters.
3. The top three outcomes for the week, each with one owner.
4. Open decisions, marking the ones with financial or ethical considerations for Erich.
5. One improvement for the week (from a kaizen card or a recent miss).

**Monthly (the report to the Chairman):**
1. A one-paragraph letter: how the month went, honestly.
2. Revenue, costs, cash and pipeline against the plan; the full-time trigger (retainer MRR of $8–10K for three months, six months of reserve, two signed builds) and how far away it is.
3. Delivery and quality: projects, QA first-pass rate, incidents, client feedback.
4. Risks that changed, and decisions needed from Erich, each with options and a recommendation.

**Quarterly:**
1. Review last quarter's goals: met, missed, why.
2. Set three to five goals for next quarter, each measurable, with an owner.
3. Budget for the quarter, the hiring trigger check, and what to stop doing.
4. Team pulse: what's working, what isn't (for people and for the agents).

## Output

A memo with the sections above, in that order, under one page for the weekly version. Status words are exact: green, amber, red.

## Quality checks

- Every number has a source and date; no decorative metrics.
- Every priority has an owner; every decision names who decides.
"""),

"research-and-fact-check": dict(
 title="Research and fact-check", category="Strategy and coordination",
 summary="Research a question from primary sources, cite them with dates, label estimates, and check claims before they're used.",
 description="Research a question or fact-check a claim: search, prefer primary sources, cite every fact with its source and date, label estimates, flag conflicts between sources and say how confident the answer is. Use before any figure, law, price or claim goes into advice, a proposal or published content.",
 body="""## When to use

Any time a figure, a law, a price, a competitor fact or a market claim will be relied on: in advice to Erich, a proposal, a decision memo or published content. Also to check someone else's claim.

## Read first

- The `docs/` topic file for the question. Use what is there, then check whether it is still current.

## Method

1. **Frame the question** precisely: what, where (Florida, Palm Beach County, Boynton Beach, US), as of when.
2. **Search for primary sources first:** statutes and official agency pages (flsenate.gov, floridarevenue.com, dos.fl.gov, the city and county), official statistics (Census, BLS), the company's own site, the original study. Use secondary summaries only to find primary sources.
3. **Read the source**, not just the snippet. Note the date it was published or updated.
4. **Cross-check** every important figure against a second independent source. When sources disagree, report both and say which you trust and why.
5. **Label** each statement: fact (sourced), estimate *(est.)*, or opinion.
6. **Check status** for laws and bills: introduced, passed, signed, effective date, or died. A bill is not a law.
7. **Rate confidence:** high (primary source, current), medium (good secondary source or a little dated), low (single weak source).

## Output

```markdown
**Answer:** ... (confidence: high/medium/low)

| Claim | Source (with date) | Type |
| ----- | ------------------ | ---- |
| ... | [Florida Senate, CS/SB 482](https://...) (checked 2026-11-25) | fact |

**Conflicts or gaps:** ...
**Recheck before use in:** ... (e.g. a client contract)
```

## Quality checks

- No uncited numbers; no invented sources; links go to the page that says it.
- Dates on everything time-sensitive.
- Vendor blogs and directories are marked as such.
"""),

"red-team-review": dict(
 title="Red-team review", category="Strategy and coordination",
 summary="Attack a plan before reality does: pre-mortem, strongest objections, hidden assumptions and the cheapest test.",
 description="Red-team a plan, proposal, price or decision: run a pre-mortem, list the strongest objections and hidden assumptions, find the single point of failure, and propose the cheapest test that would prove the plan wrong. Use before committing money, signing, launching or publishing.",
 body="""## When to use

Before a big commitment: a new service, a price change, signing a client or partner, a hire, the full-time move, a launch. Also when a plan feels too comfortable.

## Method

1. **Pre-mortem:** assume it is a year from now and the plan failed badly. Write the three most likely stories of why.
2. **Hidden assumptions:** list what must be true for the plan to work (buyers will pay $X, Erich has Y hours, the employer allows Z). Mark each as tested or untested.
3. **Four perspectives:** challenge the plan as a skeptical buyer, a competitor, a lender or investor, and the founder's family (time and stress).
4. **Single points of failure:** one client, one person, one vendor, one model, one channel.
5. **Downside:** the worst realistic outcome in money and reputation, and whether the firm survives it.
6. **Cheapest test:** the smallest, fastest experiment that would show the plan is wrong before the full commitment.
7. **Verdict:** go, go with conditions, or don't go yet, with the conditions.

## Output

A one-page memo: failure stories, assumptions table (assumption, tested?, how to test), single points of failure, worst case, cheapest test, verdict.

## Quality checks

- Objections are specific and strong, not generic ("the market may change").
- The review challenges the plan, never the person.
- Advisors advise; the decision stays with its owner.
"""),

"qa-review": dict(
 title="QA review", category="Strategy and coordination",
 summary="Review a deliverable against its standard and return PASS, PASS WITH NOTES or FAIL with itemized findings.",
 description="Review any deliverable (advice, a proposal, code, a price, content, an agent definition) for correctness, evidence, security, privacy, brand and completeness, and return a QA record: PASS, PASS WITH NOTES or FAIL with itemized findings, severity and the fix. Use before anything leaves the team.",
 body="""## When to use

Before any deliverable leaves the team: client documents, prices and invoices, code and infrastructure changes, published content, and changes to agents and skills. Reviewers never review their own work and never fix it; they report.

## Checklist

1. **Correctness:** facts, math, prices and dates are right; prices match `docs/05-services-and-pricing.md` or the SOW.
2. **Evidence:** every claim is sourced or labeled as an estimate; no fake metrics, invented clients or testimonials.
3. **Completeness:** the deliverable answers what was asked and meets its acceptance criteria.
4. **Security:** no secrets or credentials; least privilege; rollback path for changes; tests present for code.
5. **Privacy:** no street addresses, personal phone numbers or emails, client confidential data or personal data where it doesn't belong.
6. **Decision rights:** nothing commits money, deploys to a customer or settles an ethical question without Erich.
7. **Employer boundary:** no utility, vegetation-management or line-clearance work, and no FPL/NextEra vendors.
8. **Brand:** company voice ("we"), sentence case, no emoji, no hype; visuals follow the Dautel Design System (`dautel-brand` skill).

## Severity

- **Critical:** wrong money, a legal or security exposure, private data, a boundary breach. Always FAIL.
- **Major:** a wrong fact, a missing requirement, an unsupported claim. FAIL unless trivial to fix.
- **Minor:** style, clarity, small omissions. PASS WITH NOTES.

## Output

```markdown
**QA record:** <deliverable> — PASS | PASS WITH NOTES | FAIL

| # | Severity | Where | Finding | Fix | Back to |
| - | -------- | ----- | ------- | --- | ------- |
| 1 | major | §3, price table | Assessment priced at $2,000; rate card starts at $2,500 | Use $2,500 | proposal author |

**Likely root cause (for continuous improvement):** ...
```

After three FAILs on the same item, escalate to `chief-of-staff` instead of a fourth loop.
"""),
}

SALES = {
"prospect-research": dict(
 title="Prospect research", category="Sales and clients",
 summary="Find and rank local or remote prospects by fit, pain, scale, ownership and proximity, with the employer-boundary screen built in.",
 description="Find and rank prospects for the firm: define the area and segments, collect public listings, score each business on fit, pain, scale, ownership and proximity, apply the employer-boundary deduction, tier them and recommend the first campaigns. Use to build or refresh a prospect list.",
 body="""## When to use

Building or refreshing a prospect list for a segment or area (for example community association managers within 10 miles of Boynton Beach), or checking whether a market is big enough.

## Read first

- `docs/local-prospects.md` (the method used in November 2026), `docs/03-target-customers.md`, `docs/02-market.md`.

## Method

1. **Scope:** the area (a radius from a point, or a list of cities), the segments, and the size band (10–100 staff is the core).
2. **Size the market** with Census County Business Patterns (establishments by NAICS and size class) and ACS population shares. Label the radius estimate *(est.)*.
3. **Collect** public listings by segment and city; merge duplicates; set managed IT providers and agencies aside as partners.
4. **Score out of 100:** segment fit 30, workflow pain 10, scale 30 (review counts as a stand-in for volume, adjusted for segments whose clients rarely review), ownership and decision access 20 (independent and local scores highest; chains, PE-backed groups, franchises, hospitals and government score low), proximity 10.
5. **Employer-boundary deduction:** −5 for field services (needs Erich's screen), −10 for electrical work; exclude utilities, vegetation-management and line-clearance contractors and known FPL/NextEra vendors entirely.
6. **Tier:** A ≥ 85, B 72–84, C 58–71, D below 58. Verify the website of every tier A business before outreach.
7. **Recommend** the first two or three campaigns, each with a segment, a pain, a lead offer and a warm channel.

## Output

A brief (method, market size, segment ranking, top prospects, exclusions and flags, next steps, sources) and a CSV for the CRM. **Keep named prospect lists out of public repositories.**

## Quality checks

- Every figure is sourced and dated; scores are explained, not magic.
- Every field-service business carries a screen flag.
- No personal contact data is collected without consent.
"""),

"lead-qualification": dict(
 title="Lead qualification", category="Sales and clients",
 summary="Run a fit call: qualify budget, authority, need, timing and data sensitivity, screen the employer boundary, and pick the first offer.",
 description="Qualify a lead and run the free 30-minute fit call: prepare, ask the discovery questions, score budget, authority, need, timing and data sensitivity, screen the employer boundary, and recommend the first fixed-fee offer or a polite no. Use for any new inquiry or referral.",
 body="""## When to use

A new inquiry, referral or prospect who agreed to a call. Also to decide whether to keep pursuing a cold lead.

## Read first

- `docs/03-target-customers.md`, `docs/05-services-and-pricing.md` (the value ladder), `docs/09-marketing.md` (sales process).

## Method

1. **Prepare (a prepared welcome):** read their website and public reviews; note their segment, size, tools they mention and likely pain. Never make a client repeat themselves.
2. **Employer-boundary screen first:** utility, vegetation management, line clearance, tree care, electrical or a known FPL/NextEra vendor? If yes or unsure, stop and send it to Erich (`employer-boundary-screen`).
3. **Discovery questions (listen 80% of the time):**
   - What takes the most hours each week that you wish didn't?
   - Walk me through that process from request to done. Who touches it?
   - What tools and systems are involved? Who owns the accounts?
   - What data is sensitive (patient, client, financial)? Any compliance rules?
   - Have you tried AI or automation already? What happened?
   - What would success look like in 90 days? What is it worth to you?
   - Who else decides, and what's your timing and budget range?
4. **Score** each 1–3: budget, authority, need, timing, data sensitivity (3 = we can handle it safely now). Total 12+ is a strong fit.
5. **Pick the first step** on the value ladder: usually the Readiness Assessment ($2,500–$4,500, credited toward a build), a Process Health Check ($2,500–$5,000) if the process is clearly broken, or the Agent Safety Audit ($1,500) for teams that already run agents.
6. **Say no well** when it isn't a fit: too small, wrong data risk, boundary conflict, or something off-the-shelf solves it. Refer them if you can.

## Output

Fit-call notes: the pain in their words, the process sketch, systems and data, the score, the recommended next step and price, and the dated next action.

## Quality checks

- The boundary screen happened before scoping.
- No promises of results, timelines or prices outside the rate card.
"""),

"proposal-and-sow": dict(
 title="Proposal and SOW", category="Sales and clients",
 summary="Write a fixed-fee proposal and statement of work with scope, acceptance criteria, warranty, support terms and payment.",
 description="Write a proposal and statement of work (SOW): the client's problem in their words, the fix-first approach, fixed scope and exclusions, deliverables with acceptance criteria, timeline, fixed fee and payment terms, warranty, support hours and who owns what. Use after a qualified fit call or for any change of scope.",
 body="""## When to use

After a qualified fit call, to quote a new engagement, a renewal or an expansion. Change requests on a live engagement use the same structure.

## Read first

- `docs/05-services-and-pricing.md` (rate card, value ladder), `docs/10-operations-and-delivery.md` (standard artifacts), `docs/07-permits-and-licenses.md` (rules that apply to the work).

## Method

1. **Problem** in the client's own words, and what it costs them today (hours, errors, delay).
2. **Approach:** fix first, then automate. Include the readiness check unless a recent assessment or health check already covered the process.
3. **Scope:** in-scope items, explicit exclusions, assumptions, and what the client provides (access, people's time, data).
4. **Deliverables with acceptance criteria:** each one testable ("intake agent drafts a summary for 95% of test cases in the evaluation set; staff approve before anything is sent").
5. **Timeline** in weeks, with the client's dependencies marked.
6. **Fee:** fixed, from the rate card (`pricing-and-estimating`). 50% deposit for fixed-fee work; model and tool costs passed through at cost with a monthly estimate.
7. **Standard terms:** the client owns the code, accounts and data; the workmanship warranty (defects against the acceptance criteria reported within the warranty period, default 30 days after acceptance, fixed at no charge; excludes new features, third-party changes and AI model behavior beyond the tested acceptance criteria); support hours and response targets, never 24/7; change orders in writing; Florida law.
8. **Every build ships with** tests, a runbook, an access matrix and a recovery procedure, in the client's own repository and accounts.
9. **Next step:** how to accept, and the start date.

## Output

A proposal of two to four pages plus an SOW with numbered deliverables and acceptance criteria. Pricing and legal terms go through `quality-reviewer` and `business-attorney` before sending; **Erich approves every price and signs.**

## Quality checks

- Prices match the rate card; the math adds up; the deposit and payment dates are clear.
- Nothing promises outcomes the acceptance criteria don't measure.
"""),

"pricing-and-estimating": dict(
 title="Pricing and estimating", category="Sales and clients",
 summary="Estimate effort and price fixed-fee work from the rate card and benchmarks, with contingency and margin checks.",
 description="Estimate the effort for an engagement and set a fixed price: break the work down, estimate hours with a range, add contingency, price from the rate card and 2026 benchmarks, check margin and capacity, and record the assumptions. Use for quotes, change orders, retainers and productized offers.",
 body="""## When to use

Quoting an engagement, a change order, a retainer tier or a new productized offer; or checking whether a price still makes sense.

## Read first

- `docs/05-services-and-pricing.md` (rate card, benchmarks, value ladder), `docs/06-startup-and-operating-costs.md`, `docs/10-operations-and-delivery.md` (capacity: about 10–12 billable hours a week while Erich is employed).

## Method

1. **Break down the work** into deliverables, then tasks of no more than a day.
2. **Estimate each task** as low, likely and high hours. Use past actuals when they exist.
3. **Expected effort** = (low + 4 × likely + high) / 6 per task; sum them.
4. **Contingency:** 15–20% for builds, more when the client's systems are unknown. Paid discovery first when uncertainty is high.
5. **Price:** start from the rate card band for the offer; check the implied hourly rate stays at or above the $175 floor; compare with the 2026 market ranges.
6. **Pass-through costs:** model APIs, hosting and tools at cost, estimated monthly, never hidden.
7. **Capacity check:** calendar weeks at the available hours; one build at a time while employed.
8. **Record assumptions** that would change the price (data quality, access, number of users, integrations).

## Output

```markdown
| Deliverable | Low | Likely | High | Expected h |
| ----------- | --- | ------ | ---- | ---------- |
Total expected: __ h + contingency __% = __ h → price $__ (implied $__/h)
Pass-through: ~$__/month   Calendar: __ weeks   Assumptions: ...
```

## Quality checks

- Price inside the rate card band, or the exception is explained for Erich.
- Implied hourly rate at or above the floor; contingency stated.
- Erich approves every final price.
"""),

"client-onboarding": dict(
 title="Client onboarding", category="Sales and clients",
 summary="Start an engagement cleanly: signed SOW, deposit, access by least privilege, kickoff, communication plan and success measures.",
 description="Onboard a new client after the SOW is signed: confirm the deposit, set up least-privilege access in the client's own accounts, hold the kickoff, agree the communication rhythm and success measures, and record the baseline. Use at the start of every engagement.",
 body="""## When to use

Right after a client signs. Also when a client adds a new engagement.

## Method

1. **Paperwork:** signed SOW and MSA, deposit received, insurance certificate sent if asked, BAA signed if any patient data is involved (otherwise no patient data).
2. **Access, least privilege:** accounts are created by the client in their own systems, one per person or agent, with MFA; DIO never asks for shared passwords; record every grant in an access matrix (who, what, why, until when).
3. **Kickoff (prepared welcome):** goals in the client's words, the success measures and their baseline, the people involved, the schedule, what we need from them and by when.
4. **Communication plan:** one weekly written update plus a short recorded demo; one standing 30-minute call; support hours and response targets from the SOW; who to call for what.
5. **Data handling:** what data we will touch, where it lives (client systems only), and how access ends at handover.
6. **Baseline:** measure the current process (time, volume, errors) before anything changes, so results can be proven later.

## Output

An onboarding checklist with every item ticked or explained, the access matrix, the kickoff notes with success measures and baseline, and the dated first milestone.

## Quality checks

- No client confidential data in DIO's own systems.
- Every access grant has an owner and an end date.
"""),

"account-review": dict(
 title="Account review", category="Sales and clients",
 summary="Run 30-day check-ins and quarterly business reviews: results against the baseline, health score, risks, renewal and expansion.",
 description="Run a client account review: the 30-day check-in after handover, the quarterly business review (QBR) for retainers, client feedback, account health score, renewal risk and expansion ideas. Use for check-ins, QBRs, renewals and at-risk clients.",
 body="""## When to use

30 days after every handover, every quarter for retainer clients, before every renewal, and whenever a client seems unhappy.

## Method

1. **Results against the baseline** set at onboarding: hours saved, errors avoided, turnaround time, with the measurement method.
2. **Health score (1–5 each):** results, relationship (are they responsive, do they refer?), adoption (are people using it?), support load, payment.
3. **Listen:** ask what is working, what isn't, what they'd change, and how likely they are to recommend us (0–10). Read the tone, not just the words.
4. **Risks:** a champion leaving, unused features, rising support tickets, late payments, a competitor in the room.
5. **Next steps:** fixes we owe them (warranty items first), improvements, and expansion ideas only where they solve a real problem.
6. **Ask** for a referral, a testimonial or a case study only when the results are real; record their permission.

## Output

A one-page QBR or check-in summary: results, health score, what they said, risks, actions with owners and dates, and the renewal recommendation.

## Quality checks

- Results use the same measure as the baseline; no rounding up.
- Warranty fixes are scheduled before any upsell.
"""),

"partner-vetting": dict(
 title="Partner vetting", category="Sales and clients",
 summary="Vet and onboard referral, co-selling and white-label partners: fit, reputation, security, terms and the employer boundary.",
 description="Vet a potential partner (MSP, agency, vendor, freelancer marketplace) and set up the relationship: fit, reputation, security practices, client overlap, referral or white-label terms, the employer-boundary screen and a 90-day trial plan. Use before any partnership or subcontracting arrangement.",
 body="""## When to use

A managed IT provider, agency, vendor or other firm proposes or is proposed as a partner, reseller, referral source or subcontractor.

## Read first

- `docs/09-marketing.md` (§7.3 channels), `docs/04-competitors.md` (local MSPs as partners).

## Method

1. **Fit:** do they serve our ideal customers? Do they lack what we offer (agents, MCP, process improvement) so we complement rather than compete?
2. **Reputation:** reviews, how long in business, references from two clients.
3. **Security and data practices:** how they handle client credentials, MFA, incident history; would we trust them with our clients?
4. **Employer boundary:** no utility or vegetation-management work, no FPL/NextEra vendors.
5. **Model:** referral (fee or reciprocal), co-selling, white-label (they resell under their brand) or subcontracting; who owns the client relationship and support.
6. **Terms** (drafted with `business-attorney`): referral fee and when it's paid, non-solicitation, confidentiality, data handling, IP, insurance, termination.
7. **Trial:** a 90-day plan with one joint opportunity and a review date.

## Output

A partner profile (fit, reputation, security, boundary result), the recommended model and terms, risks, and the trial plan. Erich approves any agreement with money in it.
"""),
}
