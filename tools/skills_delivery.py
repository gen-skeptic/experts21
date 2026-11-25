"""Skills: process improvement, AI and platform delivery, software delivery."""

PROCESS = {
"process-health-check": dict(
 title="Process health check", category="Process improvement",
 summary="Map, measure and judge a process before anyone automates it: SIPOC, current-state map, baseline, waste and a readiness verdict.",
 description="Run a process health check (the fix-first readiness check): SIPOC, interviews and direct observation, a current-state map, baseline metrics, the eight wastes and a readiness verdict of ready, fix first or redesign. Use before any automation or software is designed for a process.",
 body="""## When to use

Before any agent workflow or software is designed around a client's process, and as a paid offer on its own ($2,500–$5,000). If a process hasn't passed this check, nothing gets automated.

## Method

1. **SIPOC:** suppliers, inputs, process (5–7 high-level steps), outputs, customers. Agree the start and end of the process.
2. **Go and see:** interview the people who do the work and watch it done at least twice. Collect real examples (with client data kept in client systems).
3. **Current-state map:** a swimlane map of every step, handoff, wait and rework loop, in the client's own words.
4. **Baseline metrics:** volume per week, lead time, touch time, error or rework rate, and how each was measured. A rough honest baseline beats none.
5. **Waste walk:** mark the eight wastes (defects, overproduction, waiting, unused talent, transport, inventory, motion, extra processing).
6. **Root causes** of the biggest problems with 5 whys (and a fishbone when causes are tangled).
7. **Verdict:**
   - **Ready:** stable, documented, measured; automate it.
   - **Fix first:** fixable problems; run a Kaizen event (`kaizen-event`) or quick fixes, then recheck.
   - **Redesign:** broken or unstable; run a DMAIC project (`dmaic-project`).

## Output

A health-check report: SIPOC, current-state map, baseline table, waste and root causes, the verdict with reasons, and the recommended next step and price.

## Quality checks

- The map was checked by the people who do the work.
- The baseline states its measurement method and sample size.
"""),

"kaizen-event": dict(
 title="Kaizen event", category="Process improvement",
 summary="Plan and run a 2–5 day rapid improvement event with the client's team, and hold the gains.",
 description="Plan and run a Kaizen rapid improvement event (2 to 5 days) with the client's team: charter, current state, waste, future state, quick experiments, standard work and a 30-day follow-up. Use when a process needs fixing before automation and the fixes are within the team's control.",
 body="""## When to use

A health check returned "fix first", the problem sits inside one team's control, and the team can give 2–5 days. Typical price $6,000–$15,000.

## Method

1. **Charter (a week before):** the problem, scope, goal (for example cut request turnaround from 5 days to 2), team members (the people who do the work plus a decision-maker), dates, and the baseline from the health check.
2. **Day 1, understand:** walk the process, validate the current-state map, measure, list the wastes.
3. **Day 2, design:** brainstorm fixes, sort them on an effort-impact grid, and draw the future-state map.
4. **Days 3–4, try:** run the quick fixes for real (new checklist, form, layout, handoff rule), measure, adjust.
5. **Last day, standardize:** write the standard work (step, who, how, how long), a visual control (board or dashboard), and a 30-day action list for what couldn't finish.
6. **Report out** to the owner: before and after, what changed, what's next.
7. **30-day follow-up:** measure again; if the gains held, the process can be automated.

## Output

Charter, before and after maps and metrics, standard work, the 30-day action list, and the follow-up result.

## Quality checks

- The client's team made the changes; we facilitated.
- Results are measured the same way as the baseline.
"""),

"dmaic-project": dict(
 title="DMAIC project", category="Process improvement",
 summary="Run a Define-Measure-Analyze-Improve-Control project for a broken or unstable process, with data at every gate.",
 description="Run a Lean Six Sigma DMAIC project: define the problem and charter, measure with a checked measurement system, analyze root causes with data, improve with tested changes, and control with a control plan and chart. Use for processes the health check marks redesign, or problems whose causes aren't obvious.",
 body="""## When to use

A health check returned "redesign", or the causes of a problem are unclear and need data. Typical price $12,000–$40,000 over 6–12 weeks. Keep projects to Green Belt size until a Black Belt leads.

## Method

1. **Define:** problem statement (what, where, how big, since when, with no cause or solution in it), goal, scope, team, SIPOC, voice of the customer and critical-to-quality measures. Charter signed by the sponsor.
2. **Measure:** operational definitions for each metric, a data collection plan, a measurement system check (`statistical-analysis`), the baseline and process capability.
3. **Analyze:** process analysis (value-added versus waste), Pareto of defects, fishbone, then verify the top causes with data (hypothesis tests, regression). Only verified causes go forward.
4. **Improve:** generate and select solutions against the verified causes, pilot them, prove the improvement statistically, and do a quick FMEA on the new process.
5. **Control:** control plan (what is measured, how often, by whom, what to do when it drifts), a control chart, standard work and training, and handover to the process owner.
6. **Close:** before and after with confidence intervals, savings (signed off by the client), lessons learned.

## Output

The charter, measure and analysis findings, the pilot result, the control plan and chart, and the closeout report.

## Quality checks

- `process-data-analyst` checks every statistical claim.
- Savings are the client's numbers, not ours.
"""),

"statistical-analysis": dict(
 title="Statistical analysis", category="Process improvement",
 summary="Pick and run the right statistics: measurement checks, control charts, capability, hypothesis tests and honest uncertainty.",
 description="Analyze process or business data with the right statistics: check the measurement system, plot it, test stability with control charts, compute capability, run hypothesis tests or regression, and report effect sizes with confidence intervals. Use for baselines, before-and-after claims, root-cause checks, marketing tests and dashboards.",
 body="""## When to use

Any claim that a number changed, a process is stable or capable, one cause matters more than another, or a test won. Also for baselines and control charts.

## Method

1. **Question first:** what decision does the analysis serve, and what difference would matter in practice?
2. **Check the data:** source, definition, sample size, missing values, outliers (investigate, don't delete). For measurements people take, check agreement (a gauge R&R or attribute agreement analysis).
3. **Plot before testing:** run chart or histogram; look at time order.
4. **Stability:** individuals and moving-range chart (or p, u or X-bar charts as the data demands). Signals: a point beyond the limits, a run of 8 on one side, 6 trending.
5. **Capability** only for a stable process: Cp/Cpk or percent defective against the requirement.
6. **Compare** with the right test: t-test or Mann-Whitney for two groups, ANOVA or Kruskal-Wallis for more, chi-square for proportions, regression for drivers. State the assumptions and check them.
7. **Report** the effect size and a 95% confidence interval, the p-value, and the practical meaning. Small samples get wide intervals; say so.

## Output

A short analysis note: question, data and its limits, plots, the test and why, results with confidence intervals, the plain-language conclusion and how sure we are.

## Quality checks

- No causal claims from correlation alone.
- Never overstate: "no significant difference" isn't "no difference".
"""),

"continuous-improvement": dict(
 title="Continuous improvement", category="Process improvement",
 summary="Run the firm's own improvement system: kaizen cards, monthly PDCA, standard work, and changes to agents and skills.",
 description="Run continuous improvement for the firm itself and for retainer clients: collect kaizen cards (problem, evidence, idea), trend QA FAILs and incidents, run the monthly plan-do-check-act cycle, and turn proven changes into the new standard, including changes to this repository's agents and skills. Use for any improvement idea or recurring problem.",
 body="""## When to use

Anyone, person or agent, spots a recurring problem or a better way; every month for the PDCA cycle; and for clients on a continuous-improvement retainer ($1,500–$4,000 a month).

## Method

1. **Kaizen card:** the problem, the evidence (examples, counts), and the idea. Anyone may send one at any time to `continuous-improvement-coordinator`.
2. **Trend monthly:** QA FAIL reasons, correction loops per item, incidents, support tickets, client feedback and the cards themselves.
3. **Plan:** pick one to three experiments with the biggest expected effect for the least effort; each has a hypothesis, a measure and an owner.
4. **Do:** run them for a set period.
5. **Check:** compare with the baseline (`statistical-analysis` when the numbers are noisy).
6. **Act:** standardize what worked (update the skill, the agent definition or the checklist), drop what didn't, and record both.
7. **Changes to this repository:** edit `tools/team.py` or `tools/skills.py`, run `python3 tools/build.py` and `--check`, have `quality-reviewer` review, then commit.
8. **Recognize** the people and agents whose cards led to changes.

## Output

The monthly improvement log: cards received, experiments run, results, standards changed, and next month's experiments.

## Quality checks

- Every standard change has evidence behind it.
- QA steps and correction loops are never removed to save time.
"""),
}

DELIVERY = {
"readiness-assessment": dict(
 title="AI readiness assessment", category="AI and platform delivery",
 summary="Assess a client's AI readiness: map workflows, score automation opportunities, set a governance baseline and a 90-day roadmap.",
 description="Run the AI Operations Readiness Assessment (Line A): interviews and workflow mapping, an inventory of systems and data, opportunity scoring by value, feasibility and risk, a governance baseline (access, data, review, recovery), what not to automate, and a 90-day roadmap with prices. Use as the entry engagement for any new client.",
 body="""## When to use

The first paid engagement with most clients ($2,500–$4,500, credited toward a build), in person or remote.

## Read first

- `docs/05-services-and-pricing.md` (Line A), `docs/03-target-customers.md` (pains by segment).

## Method

1. **Intake questionnaire** (async): goals, team, systems, data types, current AI use, compliance constraints.
2. **Interviews** (3–6 people, 45 minutes each): what fills their week, where work waits or repeats.
3. **Workflow inventory:** list the top 10–15 workflows with volume, time per item, error rate and the systems they touch.
4. **Systems and data map:** each system, who owns the account, API or export available, data sensitivity (public, internal, confidential, regulated).
5. **Score every opportunity** 1–5 on value (hours and errors saved), feasibility (data and API access, process stability), and risk (data sensitivity, harm if wrong). Rank by value × feasibility ÷ risk.
6. **Fix-first filter:** any process that isn't stable goes to a health check first (`process-health-check`).
7. **Governance baseline:** identity and access, shared passwords, where AI tools already touch data, logging, human review, backups and recovery. Score each red, amber or green.
8. **What not to automate:** say it plainly where off-the-shelf software, a checklist or no change at all is the better answer.
9. **Roadmap:** the first one to three workflows with fixed prices, the governance fixes, and a 90-day timeline.

## Output

A report (10–15 pages) and a recorded readout: summary, workflow inventory, opportunity scores, governance baseline, what not to automate, roadmap with prices.

## Quality checks

- Savings estimates show their math and are labeled *(est.)*.
- No recommendation needs data the client hasn't agreed to share.
"""),

"governed-agent-design": dict(
 title="Governed agent design", category="AI and platform delivery",
 summary="Design an AI agent workflow that is scoped, identity-bound, least-privilege, reviewed, tested, logged and recoverable.",
 description="Design a governed AI agent workflow (Line B): scope and non-goals, the agent's identity and least-privilege access, tools and MCP servers, human review checkpoints, idempotent actions, audit logging, an evaluation set, failure modes, rollback and a runbook. Use for any agent that will touch a client's real systems.",
 body="""## When to use

Designing any agent that reads or changes a client's real systems: intake, drafting, triage, records posting, scheduling, follow-ups. Builds run $6,000–$15,000 per workflow.

## Method

1. **Job and non-goals:** one sentence for what the agent does; a list of what it must never do.
2. **Approved process:** design against the future-state process that passed `process-health-check`, never today's workarounds.
3. **Identity:** the agent has its own account in each system, never a person's credentials or a shared login.
4. **Least privilege:** list every permission and why; read-only wherever possible; scoped tokens that expire.
5. **Tools:** each tool or MCP server, its inputs and outputs, and its blast radius if misused (`mcp-integration`).
6. **Human review:** where a person approves before anything is sent, filed, paid or deleted. Start with review on everything, relax only with evidence.
7. **Idempotency:** every write carries a key so a retry can't double-send or double-file; record a receipt.
8. **Audit log:** who (which agent, on whose behalf), what, when, inputs, outputs and the approval.
9. **Data handling:** what the model sees; redaction; where prompts and outputs are stored (client systems only); model provider terms.
10. **Evaluation set:** 30–100 realistic cases with expected results, including edge cases and attempts to misuse it; a pass threshold agreed with the client.
11. **Failure modes:** wrong answer, tool down, model refusal, prompt injection in incoming documents; the agent's behavior for each.
12. **Recovery:** how to pause it, roll back a bad change, and restore data; tested before go-live.

## Output

An agent design document with the sections above, the access matrix, the evaluation set, and the runbook outline. `security-compliance` reviews the design before the build starts.

## Quality checks

- No permission without a reason; no shared credentials.
- Human review sits before every irreversible action.
"""),

"mcp-integration": dict(
 title="MCP integration", category="AI and platform delivery",
 summary="Design and build a secure Model Context Protocol server that connects agents to one system with scoped, logged, idempotent tools.",
 description="Design and build an MCP (Model Context Protocol) integration: pick the tools to expose, design their schemas, authenticate per user or agent, scope permissions, make writes idempotent, log every call, handle errors and rate limits, and test it. Use for the MCP Integration Sprint and any agent that needs a new system connection.",
 body="""## When to use

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
"""),

"agent-safety-audit": dict(
 title="Agent safety audit", category="AI and platform delivery",
 summary="Audit an existing AI or agent setup: credentials, permissions, MCP servers, data flows, logging, review and recovery, with a scored report.",
 description="Run an Agent Safety Audit ($1,500, one week, remote): inventory the client's AI tools and agents, check credentials, permissions, MCP servers, data flows, prompt-injection exposure, logging, human review and recovery, then deliver a scored report with prioritized fixes. Use when a team already runs agents or AI tools.",
 body="""## When to use

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
"""),

"threat-model": dict(
 title="Threat model", category="AI and platform delivery",
 summary="Threat-model a system or agent: assets, trust boundaries, data flows, STRIDE threats including prompt injection, and mitigations.",
 description="Threat-model a system, agent or integration: list assets and trust boundaries, draw the data flows, walk STRIDE threats plus AI-specific ones (prompt injection, data leakage to model providers, excessive agency), rate each and assign mitigations. Use before building anything that handles client data or acts in client systems.",
 body="""## When to use

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
"""),

"architecture-decision-record": dict(
 title="Architecture decision record", category="AI and platform delivery",
 summary="Record a technical decision: context, options (including buy), trade-offs, the choice, consequences and how to reverse it.",
 description="Write an architecture decision record (ADR) and build-versus-buy analysis: context and constraints, options including off-the-shelf software, trade-offs on cost, security, operability and lock-in, the decision, consequences and the exit path. Use for any significant technical choice for the firm or a client.",
 body="""## When to use

Choosing a platform, database, model provider, framework, hosting, integration pattern, or build versus buy, for the firm or a client.

## Method

1. **Context:** the problem, constraints (budget, skills, data rules, who will operate it), and the quality attributes that matter most (security, recoverability, cost, simplicity).
2. **Options:** at least three, always including an off-the-shelf product and "do less".
3. **Compare** on: total cost over 3 years, security and compliance, who can operate it (can the client's team?), lock-in and exit, maturity, fit with the approved stack.
4. **Decide** with the simplest option that meets the constraints. Prefer what the firm can build, deploy and operate well.
5. **Consequences:** what gets easier, what gets harder, new risks, follow-up work.
6. **Exit path:** how to reverse or migrate if it proves wrong.

## Output

```markdown
# ADR-NNN: <decision>
Status: proposed | accepted | superseded   Date:   Decider:
## Context
## Options considered (table)
## Decision
## Consequences
## Exit path
```

## Quality checks

- The buy option was considered honestly.
- The client's ability to run it without us was weighed.
"""),

"private-ai-platform": dict(
 title="Private AI platform", category="AI and platform delivery",
 summary="Design a company memory and private AI platform in the client's own environment: PostgreSQL with pgvector, SSO, private networking and recovery.",
 description="Design a company memory and private AI platform (Line C): shared memory on PostgreSQL with pgvector, single sign-on, private networking, model access with data agreements, backups and restore drills, monitoring, and a GitOps deployment, all in the client's own accounts. Use for Company Memory Starter, private AI and GitOps Platform Launch work.",
 body="""## When to use

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
"""),

"release-and-deployment": dict(
 title="Release and deployment", category="AI and platform delivery",
 summary="Ship a release safely: handoff package, staging, client acceptance, Erich's approval, GitOps promotion, verification and rollback.",
 description="Release software or an agent to a client: assemble the release handoff package, deploy to staging, run client acceptance testing, get Erich's production approval, promote through GitOps, verify, and keep rollback ready. Builders build; DevOps deploys. Use for every release to a client's production.",
 body="""## When to use

Every release to a client's production: software, agents, integrations, platform changes.

## Release handoff package (from the builders)

1. Source merged through a reviewed pull request, CI green (build, tests, lint, type checks, dependency and secret scans).
2. A build artifact or container image with an immutable digest, plus an SBOM and vulnerability scan.
3. Deployment spec, resource limits, and ports.
4. Configuration contract: every environment variable and secret **by name only**, never values.
5. Health checks, structured logs and the metrics to alert on.
6. Backward-compatible migrations with a tested rollback or restore.
7. Release notes, a runbook draft, and test results (agent releases: evaluation results).

## Method

1. `platform-devops-engineer` checks the package; anything missing goes back to the builders.
2. **Deploy to staging** through GitOps; smoke test.
3. **Client acceptance testing** on staging against the SOW's acceptance criteria; the client signs off.
4. **Erich approves** the production deployment (a final deployment to a customer is always his decision).
5. **Promote** through GitOps in the agreed window; progressive rollout where available.
6. **Verify:** health checks, key journeys, metrics and logs for the first hour.
7. **Rollback** at once if verification fails; then a blameless review.
8. **Close:** release recorded, runbook updated, client told.

## Quality checks

- Developers never deploy to production; DevOps owns environments and rollback.
- No secret values anywhere in the package.
"""),

"incident-response": dict(
 title="Incident response", category="AI and platform delivery",
 summary="Handle an outage, security event or agent mistake: triage, contain, communicate, fix, recover, notify where required, and review blamelessly.",
 description="Respond to an incident (outage, security event, data exposure or an agent that did something wrong): triage severity, contain, communicate with the client, fix and recover, check legal notification duties (Florida Information Protection Act, HIPAA), and run a blameless review. Use the moment something breaks or looks unsafe.",
 body="""## When to use

A client system is down or degraded, an agent took a wrong or unsafe action, credentials may have leaked, or data may have been exposed.

## Method

1. **Triage (first 15 minutes):** what is affected, since when, how many people; severity SEV1 (data exposure, client unable to work), SEV2 (degraded), SEV3 (minor).
2. **Contain:** pause the agent, revoke or rotate credentials, block access, roll back the last change. Preserve logs and evidence; don't wipe anything.
3. **Communicate:** tell the client early and plainly what we know, what we're doing and when the next update is (SEV1 every hour). Bad news early.
4. **Fix and recover:** restore service from a known-good state; verify.
5. **Legal check:** if personal information of Floridians may be exposed, the Florida Information Protection Act requires notice to affected people within 30 days (and the Attorney General at 500 or more); HIPAA has its own rules for patient data. Bring in `business-attorney` and Erich at once.
6. **Blameless review** within five business days: timeline, root cause (5 whys), what made it worse or better, actions with owners. Process causes, never blame.
7. **Improve:** runbook updates, tests or monitors added, a kaizen card for anything systemic.

## Output

The incident log (timeline, actions, communications), the client summary, and the review with actions.

## Quality checks

- Containment came before root-cause hunting.
- Every notification duty was checked and recorded.
"""),

"managed-operations": dict(
 title="Managed operations", category="AI and platform delivery",
 summary="Run the monthly retainer cycle for agents, platforms and Software Care: monitor, patch, tune, support and report.",
 description="Run the monthly managed operations cycle for retainer clients (Line D, $750–$4,500 a month) and Software Care (15–20% of build cost a year): monitoring review, patching, agent tuning and evaluation reruns, backups and restore tests, support requests, cost review and the monthly report. Use for every retainer and support request.",
 body="""## When to use

Every month for each retainer and Software Care client, and whenever a support request comes in.

## Monthly cycle

1. **Health review:** uptime, errors, alerts, agent success and review rates, latency, costs against the estimate.
2. **Patch and update:** dependencies, base images, platform versions, model versions; test on staging first.
3. **Agent tuning:** rerun the evaluation set; investigate drops; adjust prompts or tools with a reviewed change; never relax human review without evidence.
4. **Backups:** confirm they ran; do a restore test at least each quarter.
5. **Access review:** remove accounts no longer needed.
6. **Support requests:** log each one, answer within the SOW's response targets, fix standard changes under the standing approval, and quote anything bigger as a change order.
7. **Monthly report:** what we did, what we saw, costs, recommendations, and what's next. Short, honest, in plain words.

## Quality checks

- Support hours and response targets match the SOW; no 24/7 promises.
- Every change follows the release process.
"""),
}

SOFTWARE = {
"requirements-and-user-stories": dict(
 title="Requirements and user stories", category="Software delivery",
 summary="Turn business needs into user stories with testable acceptance criteria, a process map and a prioritized backlog.",
 description="Gather and write requirements: interview users, map the future-state process, write user stories with testable acceptance criteria (given-when-then), non-functional requirements, a glossary and a prioritized backlog (must, should, could). Use at the start of any software or agent build, and for change requests.",
 body="""## When to use

Discovery for custom software (paid discovery $3,500–$7,500), agent builds, and change requests.

## Method

1. **Who and why:** users and their goals; the business outcome and how it will be measured.
2. **Process first:** map the approved future-state process (from `process-health-check` or a Kaizen); software follows the process, not the other way round.
3. **User stories:** "As a <role>, I want <capability> so that <benefit>." Small enough to build in a few days.
4. **Acceptance criteria** for each story in given-when-then form, including errors and edge cases.
5. **Non-functional requirements:** security and access, privacy and data classes, performance, accessibility (WCAG 2.1 AA), availability, audit, retention.
6. **Glossary** of the client's terms.
7. **Prioritize** with MoSCoW; the first release holds only the musts.
8. **Confirm** with the client: read back the stories and criteria in their words.

## Output

A requirements document: goals and measures, process map, story list with acceptance criteria, non-functional requirements, glossary, prioritized backlog and open questions.

## Quality checks

- Every story has testable acceptance criteria.
- `qa-test-automation-engineer` can write a test from each criterion.
"""),

"software-build-standards": dict(
 title="Software build standards", category="Software delivery",
 summary="The firm's coding standards, definition of done, pull-request review and the custom software lifecycle.",
 description="Apply the firm's software standards: the custom software lifecycle (discovery, design, sprints, QA, release handoff), coding conventions, small reviewed pull requests, tests with every change, no secrets in code, accessibility, and the definition of done. Use while building or reviewing any code.",
 body="""## When to use

Building or reviewing any software, agent code, integration or infrastructure code for the firm or a client.

## Lifecycle (custom software, Line G)

Discovery → architecture and prototype → sprints with weekly demos → QA → release handoff package → DevOps deploys to staging → client acceptance → Erich approves production → DevOps promotes → Software Care.

## Standards

1. **Repository:** in the client's GitHub organization; the client owns the code.
2. **Branches and pull requests:** small PRs (under about 400 changed lines), one purpose each, a clear description, linked to the story.
3. **Review:** every PR reviewed by another engineer (or agent plus human) before merge; reviewers check correctness, tests, security, readability.
4. **Tests:** unit tests for logic, integration tests for boundaries, and an end-to-end test for each critical journey; CI must be green.
5. **Security:** no secrets in code or logs; parameterized queries; input validation; dependencies pinned and scanned; least-privilege service accounts.
6. **Code:** typed where the language allows; linted and formatted automatically; clear names over comments; handle errors explicitly.
7. **Accessibility and design:** WCAG 2.1 AA; the Dautel Design System for DIO-branded work, the client's brand for theirs.
8. **Docs:** README with setup and run steps; changes noted for the release notes.

## Definition of done

The story's acceptance criteria pass; tests written and green; reviewed and merged; docs updated; no new high or critical scan findings; demoed to the client.
"""),

"test-plan": dict(
 title="Test plan", category="Software delivery",
 summary="Plan and automate testing from the acceptance criteria, including agent evaluation sets, and report results objectively.",
 description="Write and run a test plan: scope and risks, test cases from the acceptance criteria, unit, integration and end-to-end automation, accessibility and security checks, agent evaluation sets with pass thresholds, and an objective test report. Use for every release of software or agents.",
 body="""## When to use

For every release: software, integrations and agents. Start when the acceptance criteria are written, not when the code is done.

## Method

1. **Scope and risk:** what changes, what could break, what matters most to the client; test hardest where the risk is highest.
2. **Test cases** from each acceptance criterion: the happy path, errors, edge cases (empty, huge, duplicate, wrong format, no permission).
3. **Automate** what repeats: unit tests (logic), integration tests (APIs, databases, MCP tools), end-to-end tests (critical journeys in a real browser).
4. **Non-functional checks:** accessibility (WCAG 2.1 AA, keyboard and screen reader), performance on realistic data, security basics (auth, permissions, secret scan).
5. **Agents:** an evaluation set of 30–100 realistic cases with expected outputs, including misuse and prompt-injection attempts; score each run; the release passes only above the agreed threshold, with every failure reviewed.
6. **Regression:** rerun the full suite before every release.
7. **Report:** what was tested, results, open defects with severity, and a clear recommendation (release or not).

## Output

A test plan, the automated tests in the repository, and a test report attached to the release handoff package.

## Quality checks

- Every acceptance criterion maps to at least one test.
- Defects are reported with steps to reproduce, without blame.
"""),

"ux-design-review": dict(
 title="UX design and review", category="Software delivery",
 summary="Design and review flows and screens for ease of use and accessibility (WCAG 2.1 AA), and test them with real users.",
 description="Design or review user flows, wireframes and screens: task-based flows from the future-state process, clear hierarchy and copy, accessibility to WCAG 2.1 AA (contrast, keyboard, screen readers, touch targets), responsive layouts, and quick usability tests with five users. Use for any interface the firm builds.",
 body="""## When to use

Designing or reviewing any interface: client apps, portals, agent review screens, dautel.io and landing pages.

## Method

1. **Users and tasks:** the top three to five tasks each user must do, from the requirements.
2. **Flows:** the shortest path for each task; remove steps; put the most common action first.
3. **Wireframes**, then screens in the Dautel Design System (DIO work) or the client's brand.
4. **Content:** plain, specific labels and messages; errors that say what happened and what to do.
5. **Accessibility (WCAG 2.1 AA):** text contrast at least 4.5:1, visible focus, full keyboard use, labels on every input, alt text, touch targets at least 44 by 44 px, no meaning by color alone, respects reduced motion.
6. **Responsive:** works at phone width (360 px) without horizontal scrolling.
7. **Agent review screens:** show what the agent proposes, its sources and confidence, and make approve, edit and reject equally easy.
8. **Test** with five real users on the key tasks; note where they hesitate; fix and retest.

## Output

Flows, wireframes or screens, an accessibility checklist result, and usability findings with fixes.
"""),

"runbook": dict(
 title="Runbook", category="Software delivery",
 summary="Write a runbook a client's own staff can follow: start, stop, check health, common failures, rollback, restore and contacts.",
 description="Write an operational runbook for a system or agent: what it does, how to start, stop and pause it, how to check health, common failures and fixes, rollback and restore steps, access and secrets (by name only), and who to contact. Use for every system the firm hands over.",
 body="""## When to use

Every system, agent or integration the firm builds or operates, before handover; update it after every incident or change.

## Structure

1. **Purpose:** what the system does and for whom, in two sentences.
2. **Architecture at a glance:** a small diagram and where each part runs.
3. **Access:** who can do what; secrets listed **by name only** with where they are stored.
4. **Daily operation:** how to check it's healthy (dashboard, health URL, key log lines).
5. **Start, stop and pause:** exact commands or clicks; for agents, how to pause all actions immediately.
6. **Common failures:** symptom, likely cause, fix, and when to escalate.
7. **Rollback:** how to return to the last good version.
8. **Backup and restore:** where backups are, how to restore, when it was last tested.
9. **Contacts and support:** support hours and response targets from the SOW.

## Rules

- Write for the client's own staff, not for us. Numbered steps, one action each, exact commands.
- Test the runbook: someone who didn't build the system follows it.
"""),

"project-plan-and-status": dict(
 title="Project plan and status", category="Software delivery",
 summary="Plan and run an engagement: plan, risks and issues log, weekly status, change requests and closeout.",
 description="Plan and run an engagement: milestones and dependencies, a RAID log (risks, assumptions, issues, decisions), weekly one-line status (green, amber, red), change requests with impact and a written approval, and closeout with a retrospective and handover. Use for every engagement from kickoff to closeout.",
 body="""## When to use

Every engagement, from kickoff to closeout.

## Method

1. **Plan:** milestones from the SOW deliverables, owners, dependencies (especially the client's), and buffer. Weekly demos on the calendar.
2. **RAID log:** risks (with likelihood, impact and response), assumptions, issues (with owner and due date) and decisions.
3. **Weekly status:** one line first ("Green: intake agent in staging, client testing Thursday"), then progress, next week, risks and help needed.
4. **Change requests:** anything outside the SOW: describe it, estimate effort and cost (`pricing-and-estimating`), the effect on schedule, and get written approval before work starts. Erich approves anything with a price.
5. **Watch scope and margin:** compare hours used with the estimate every week; raise amber early.
6. **Closeout:** acceptance signed, final invoice, handover (runbook, training, access returned or transferred), a retrospective (what went well, what to change, planned against actual), a kaizen card for anything systemic, and the 30-day check-in booked (`account-review`).

## Output

The plan, the RAID log, weekly status notes, change request records and the closeout report.
"""),
}
