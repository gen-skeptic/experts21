# Expert roster

*Generated from `tools/team.py` and `tools/skills.py` by `tools/build.py`. 50 agents and 57 skills.*

The experts a consultant would want around the table to plan, open and run **Dautel Intelligent Operations**, an AI consulting and deployment firm in Boynton Beach, Florida. They come from the research in [`docs/`](README.md) and from the team plan in the DIO operating manual (gen-skeptic/experts), which already defined 49 of these roles. Each role is built as an agent in [`.claude/agents/`](../.claude/agents/) and each skill as a reusable method in [`.claude/skills/`](../.claude/skills/), written once and shared by every agent that needs it.

Two agents run the team itself: **`orchestrator`** takes any question, brings in the right experts and returns one combined answer; **`agent-builder`** creates new agents and skills and improves existing ones.

Every agent's Star Trek name, voice, working style and brain are in [agent-brains.md](agent-brains.md).

## The experts

### Leadership and coordination

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 1 | `orchestrator` | Picard | Orchestrator (CEO agent) | Takes any question, decides which experts to bring in, has them work in parallel and returns one combined answer; runs the firm day to day for Erich. | `routing-plan`, `decision-memo`, `operating-cadence`, `red-team-review`, `employer-boundary-screen`, `continuous-improvement`, `model-selection` |
| 2 | `chief-of-staff` | Riker | Chief of Staff (routing and cadence) | Turns cross-functional requests into routing plans and runs the weekly, monthly and quarterly operating rhythm. | `routing-plan`, `operating-cadence`, `decision-memo`, `project-plan-and-status`, `model-selection` |
| 3 | `advisory-board` | Guinan | Advisory Board (strategy sounding board) | Pressure-tests big decisions (pricing, hires, the full-time move) from several perspectives before money is committed. | `red-team-review`, `decision-memo`, `break-even-and-cash-flow`, `research-and-fact-check` |
| 4 | `cto-principal-architect` | Spock | CTO and Principal Architect | Sets the technical standard, reference architectures and approved stack, and owns architecture decisions. | `architecture-decision-record`, `threat-model`, `governed-agent-design`, `private-ai-platform`, `vendor-and-tool-approval`, `decision-memo`, `model-selection` |
| 5 | `operations-finance-manager` | Sisko | Operations and Finance Manager | Runs budgets, cash flow, the rate card, vendors and the monthly close so growth stays profitable. | `break-even-and-cash-flow`, `monthly-finance-close`, `pricing-and-estimating`, `risk-register`, `vendor-and-tool-approval`, `operating-cadence`, `model-selection` |

### Team builder

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 6 | `agent-builder` | Soong | Agent Builder (meta agent) | Creates new agents and skills and improves existing ones, following the official Claude Code docs and this repository's patterns. | `agent-and-skill-authoring`, `qa-review`, `research-and-fact-check` |

### Advisors

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 7 | `business-attorney` | Cogley | Business Attorney (legal advisor) | Drafts and reviews contracts (MSA, SOW, NDA, DPA, BAA), Florida business law and AI and privacy rules, for review by a licensed attorney. | `contract-review`, `florida-business-compliance`, `employer-boundary-screen`, `proposal-and-sow`, `partner-vetting` |
| 8 | `cpa-bookkeeper` | Tuvok | CPA and Bookkeeper (finance and tax advisor) | Keeps the books, the tax calendar and sales-tax questions straight, flagging what needs a licensed CPA. | `monthly-finance-close`, `florida-business-compliance`, `break-even-and-cash-flow` |
| 9 | `insurance-risk-advisor` | Saru | Insurance and Risk Advisor | Sizes E&O, cyber and other coverage, keeps the risk register and checks contract insurance clauses. | `risk-register`, `contract-review`, `florida-business-compliance`, `red-team-review` |

### Quality

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 10 | `quality-reviewer` | Odo | Quality Reviewer (QA gate) | The independent QA gate: checks every deliverable for correctness, evidence, security, privacy and brand. | `qa-review`, `research-and-fact-check`, `red-team-review`, `dautel-brand` |

### Process improvement

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 11 | `lean-six-sigma-lead` | Seven | Lean Six Sigma Lead (process improvement) | Makes sure no broken process gets automated: health checks, Kaizen events and DMAIC projects. | `process-health-check`, `kaizen-event`, `dmaic-project`, `readiness-assessment`, `continuous-improvement`, `workshop-design` |
| 12 | `process-data-analyst` | Bashir | Process Data Analyst (Six Sigma statistics) | Proves with statistics whether a process is stable, capable and actually improved. | `statistical-analysis`, `dmaic-project`, `process-health-check` |
| 13 | `continuous-improvement-coordinator` | Rom | Continuous Improvement Coordinator (and manual maintainer) | Collects improvement ideas, runs the monthly PDCA cycle and keeps the team's standards current. | `continuous-improvement`, `kaizen-event`, `operating-cadence` |

### Sales, clients and partners

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 14 | `client-success-manager` | Troi | Client Success and Account Manager | Keeps clients succeeding and renewing: onboarding, check-ins, quarterly reviews and support. | `account-review`, `client-onboarding`, `managed-operations`, `incident-response` |
| 15 | `business-development` | Kirk | Business Development Lead | Fills and works the sales pipeline: qualification, fit calls, proposals and closing at healthy prices. | `lead-qualification`, `prospect-research`, `proposal-and-sow`, `pricing-and-estimating`, `employer-boundary-screen` |
| 16 | `partner-ecosystem-manager` | Sarek | Partner Ecosystem Manager | Builds referral and white-label channels with local MSPs, agencies and vendors. | `partner-vetting`, `lead-qualification`, `employer-boundary-screen` |
| 17 | `market-research-analyst` | Dax | Market Research Analyst | Supplies current, sourced market, competitor and prospect research for every decision. | `prospect-research`, `research-and-fact-check`, `employer-boundary-screen` |

### AI and platform delivery

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 18 | `senior-agent-engineer` | Data | Senior AI Agent Engineer | Designs and builds governed AI agents and MCP integrations that are scoped, tested and recoverable. | `governed-agent-design`, `mcp-integration`, `agent-safety-audit`, `test-plan`, `runbook`, `release-and-deployment` |
| 19 | `platform-devops-engineer` | O'Brien | Platform and DevOps Engineer | Deploys and runs client platforms through GitOps, with monitoring, runbooks and tested rollback. | `release-and-deployment`, `incident-response`, `managed-operations`, `private-ai-platform`, `runbook`, `threat-model` |
| 20 | `ai-solutions-engineer` | The Doctor | AI Solutions Engineer | Runs AI readiness assessments, scores automation opportunities and scopes the first workflows. | `readiness-assessment`, `process-health-check`, `governed-agent-design`, `lead-qualification`, `pricing-and-estimating` |
| 21 | `security-compliance` | Worf | Security and Compliance Specialist | Threat-models every system, audits agent safety and keeps work compliant for healthcare, legal and finance clients. | `threat-model`, `agent-safety-audit`, `florida-business-compliance`, `vendor-and-tool-approval`, `incident-response`, `qa-review` |
| 22 | `data-engineer` | Stamets | Data Engineer | Designs the data models, pipelines and company-memory stores (PostgreSQL and pgvector) agents depend on. | `private-ai-platform`, `mcp-integration`, `architecture-decision-record`, `statistical-analysis` |
| 23 | `delivery-lead` | Janeway | Technical Project Manager / Delivery Lead | Plans and runs every engagement on scope, on time and on budget, with weekly status and a clean handover. | `project-plan-and-status`, `client-onboarding`, `release-and-deployment`, `pricing-and-estimating`, `operating-cadence` |

### Software team

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 24 | `software-engineering-lead` | Geordi | Software Engineering Lead | Leads the software team, sets the definition of done and assembles each release for DevOps. | `software-build-standards`, `project-plan-and-status`, `release-and-deployment`, `test-plan`, `pricing-and-estimating`, `hiring-kit` |
| 25 | `software-solutions-architect` | Brahms | Software Solutions Architect | Designs custom software and integrations with the simplest architecture the firm can build and operate. | `architecture-decision-record`, `requirements-and-user-stories`, `threat-model`, `mcp-integration` |
| 26 | `business-analyst` | Chakotay | Business Analyst | Turns business needs into clear requirements, user stories and testable acceptance criteria. | `requirements-and-user-stories`, `process-health-check`, `readiness-assessment` |
| 27 | `ux-ui-designer` | Kes | UX/UI Designer | Designs flows and screens that are easy to learn, fast to use and accessible (WCAG 2.1 AA). | `ux-design-review`, `dautel-brand`, `requirements-and-user-stories` |
| 28 | `full-stack-developer` | Wesley | Full-Stack Developer | Builds features end to end, from user story to tested, reviewed pull request. | `software-build-standards`, `test-plan`, `ux-design-review`, `dautel-brand` |
| 29 | `backend-api-engineer` | Torres | Back-End and API Engineer | Builds reliable back ends, APIs and integrations that other systems and agents can depend on. | `software-build-standards`, `mcp-integration`, `threat-model`, `test-plan` |
| 30 | `mobile-developer` | Barclay | Mobile Developer | Builds mobile and offline-first PWA apps for people who work away from a desk. | `software-build-standards`, `ux-design-review`, `test-plan`, `dautel-brand` |
| 31 | `qa-test-automation-engineer` | T'Pol | QA and Test Automation Engineer | Writes the test plans and automated tests that prove each release works before a client sees it. | `test-plan`, `qa-review`, `software-build-standards` |
| 32 | `technical-writer` | Jake | Technical Writer | Writes the runbooks, user guides and release notes clients' own staff can follow. | `runbook`, `release-and-deployment`, `dautel-brand` |

### Marketing and social media

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 33 | `content-marketing` | Hoshi | Content and Marketing Specialist (long-form) | Writes long-form content: articles, case studies, newsletters and lead magnets. | `long-form-content`, `research-and-fact-check`, `seo-audit`, `dautel-brand` |
| 34 | `web-developer-designer` | Trip | Web Developer and Designer (DIO sites) | Builds and improves dautel.io and landing pages for clarity, speed and conversion. | `website-change`, `seo-audit`, `ux-design-review`, `dautel-brand` |
| 35 | `marketing-director` | Uhura | Marketing Director (head of marketing) | Owns the message, the marketing plan and budget, and the results of every channel. | `marketing-plan`, `marketing-metrics`, `long-form-content`, `paid-campaign`, `dautel-brand` |
| 36 | `social-media-manager` | Tilly | Social Media Manager | Runs the weekly social calendar on LinkedIn and other platforms where buyers are. | `social-media-cycle`, `marketing-metrics`, `dautel-brand` |
| 37 | `youtube-producer` | Paris | YouTube Channel Producer | Plans and scripts the YouTube channel: series, titles, thumbnails and analytics. | `video-production`, `seo-audit`, `dautel-brand` |
| 38 | `video-editor` | Harry | Video Editor and Short-Form Specialist | Edits recordings into tight videos and short clips with captions for every platform. | `video-production`, `social-media-cycle`, `dautel-brand` |
| 39 | `graphic-designer` | Garak | Graphic Designer (brand and social assets) | Makes on-brand graphics, social assets, slides and thumbnails in the Dautel Design System. | `dautel-brand`, `social-media-cycle`, `video-production` |
| 40 | `community-manager` | Neelix | Community Manager | Answers, moderates and grows the firm's online community and replies. | `social-media-cycle`, `dautel-brand` |
| 41 | `seo-specialist` | Chekov | SEO Specialist | Gets the firm found in search: keyword research, technical audits and content briefs. | `seo-audit`, `website-change`, `long-form-content`, `marketing-metrics` |
| 42 | `paid-ads-specialist` | Quark | Paid Advertising Specialist | Runs small, measured paid campaigns and stops spending the moment they stop paying back. | `paid-campaign`, `marketing-metrics`, `dautel-brand` |
| 43 | `podcast-webinar-producer` | Vic | Podcast and Webinar Producer | Books podcast guest spots and produces webinars, then repurposes each one. | `podcast-and-webinar`, `workshop-design`, `dautel-brand` |
| 44 | `marketing-analyst` | Ro | Marketing Analyst | Measures which marketing creates clients: metrics, attribution and honest monthly reports. | `marketing-metrics`, `statistical-analysis`, `marketing-plan`, `paid-campaign` |

### Company operations, products and training

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 45 | `operations-coordinator` | Nog | Operations Coordinator (virtual assistant) | Handles scheduling, renewals, filings, vendor lists and the routine admin that eats Erich's hours. | `monthly-finance-close`, `florida-business-compliance`, `client-onboarding`, `vendor-and-tool-approval`, `operating-cadence` |
| 46 | `trainer-curriculum` | Pike | Trainer and Curriculum Developer | Designs workshops, courses and coaching on AI agents and Lean methods for clients and the community. | `workshop-design`, `podcast-and-webinar`, `product-offer-design`, `dautel-brand` |
| 47 | `product-manager` | Burnham | Product Manager | Turns repeated client needs into productized offers and decides the roadmap from evidence. | `product-offer-design`, `pricing-and-estimating`, `requirements-and-user-stories`, `marketing-plan`, `break-even-and-cash-flow` |
| 48 | `talent-people-partner` | Beverly | Talent and People Partner | Plans hires, writes job descriptions and interview kits, and runs onboarding and offboarding. | `hiring-kit`, `florida-business-compliance` |

### Utility vertical (phase 2)

| # | Agent | Name | Role | Job (one line) | Skills |
| -: | --- | --- | --- | --- | --- |
| 49 | `gis-remote-sensing-analyst` | Sulu | GIS and Remote-Sensing Analyst | Phase 2: turns LiDAR, imagery and drone data into field decisions for utility and vegetation work. | `utility-field-ops`, `employer-boundary-screen`, `statistical-analysis` |
| 50 | `utility-industry-advisor` | Scotty | Utility Industry Advisor (fractional) | Phase 2: advises on the utility and field-operations market once the employer boundary allows it. | `utility-field-ops`, `employer-boundary-screen`, `red-team-review` |

## Who reports to whom

Erich (Chairman) owns the firm and decides what only the owner should: financial transactions, final deployments to customers and anything with financial or ethical considerations. `orchestrator` runs everything else as the CEO agent. Advisors advise and never direct work.

| Unit | Head (reports to `orchestrator`) | Team |
| --- | --- | --- |
| Board | Erich (Chairman), advised by `advisory-board` | `orchestrator` |
| Office of the CEO | `chief-of-staff` | — |
| Technology and delivery | `cto-principal-architect` | `senior-agent-engineer`, `platform-devops-engineer`, `ai-solutions-engineer`, `security-compliance`, `gis-remote-sensing-analyst`, `utility-industry-advisor`, `data-engineer`, `delivery-lead`, `software-engineering-lead` (leads `software-solutions-architect`, `business-analyst`, `ux-ui-designer`, `full-stack-developer`, `backend-api-engineer`, `mobile-developer`, `qa-test-automation-engineer`, `technical-writer`) |
| Operations and finance | `operations-finance-manager` | `cpa-bookkeeper`, `insurance-risk-advisor`, `operations-coordinator`, `talent-people-partner` |
| Sales and partnerships | `business-development` | `partner-ecosystem-manager`, `market-research-analyst` |
| Client success | `client-success-manager` | — |
| Marketing | `marketing-director` | `content-marketing`, `web-developer-designer`, `social-media-manager` (leads `community-manager`), `youtube-producer` (leads `video-editor`), `graphic-designer`, `seo-specialist`, `paid-ads-specialist`, `podcast-webinar-producer`, `marketing-analyst` |
| Products and training | `product-manager` | `trainer-curriculum` |
| Process improvement | `lean-six-sigma-lead` | `process-data-analyst`, `continuous-improvement-coordinator` |
| Quality (independent) | `quality-reviewer` | — |
| Legal (advisor) | `business-attorney` | — |
| Team builder | `agent-builder` | — |

## Shared skills

A skill is a reusable method ("review a contract", "build a break-even model"). One skill is shared by every agent that uses it, so it is written once.

### Strategy and coordination

| Skill | What it's for | Used by |
| --- | --- | --- |
| `routing-plan` | Turn a question that spans several functions into a plan: which experts, what each answers, in what order, on which brain. | `orchestrator`, `chief-of-staff` |
| `decision-memo` | Frame a decision with options, facts, costs, risks and a recommendation, and say who decides. | `orchestrator`, `chief-of-staff`, `advisory-board`, `cto-principal-architect` |
| `operating-cadence` | Run the weekly priorities, the monthly report to the Chairman and quarterly planning. | `orchestrator`, `chief-of-staff`, `operations-coordinator`, `delivery-lead`, `operations-finance-manager`, `continuous-improvement-coordinator` |
| `research-and-fact-check` | Research a question from primary sources, cite them with dates, label estimates, and check claims before they're used. | `advisory-board`, `content-marketing`, `market-research-analyst`, `quality-reviewer`, `agent-builder` |
| `model-selection` | Pick the most cost-efficient model for each piece of work, from Claude or OpenRouter, by work task type, with privacy and fallbacks. | `orchestrator`, `chief-of-staff`, `cto-principal-architect`, `operations-finance-manager` |
| `red-team-review` | Attack a plan before reality does: pre-mortem, strongest objections, hidden assumptions and the cheapest test. | `orchestrator`, `insurance-risk-advisor`, `advisory-board`, `utility-industry-advisor`, `quality-reviewer` |
| `qa-review` | Review a deliverable against its standard and return PASS, PASS WITH NOTES or FAIL with itemized findings. | `security-compliance`, `qa-test-automation-engineer`, `quality-reviewer`, `agent-builder` |

### Sales and clients

| Skill | What it's for | Used by |
| --- | --- | --- |
| `prospect-research` | Find and rank local or remote prospects by fit, pain, scale, ownership and proximity, with the employer-boundary screen built in. | `business-development`, `market-research-analyst` |
| `lead-qualification` | Run a fit call: qualify budget, authority, need, timing and data sensitivity, screen the employer boundary, and pick the first offer. | `ai-solutions-engineer`, `business-development`, `partner-ecosystem-manager` |
| `proposal-and-sow` | Write a fixed-fee proposal and statement of work with scope, acceptance criteria, warranty, support terms and payment. | `business-attorney`, `business-development` |
| `pricing-and-estimating` | Estimate effort and price fixed-fee work from the rate card and benchmarks, with contingency and margin checks. | `ai-solutions-engineer`, `business-development`, `product-manager`, `delivery-lead`, `operations-finance-manager`, `software-engineering-lead` |
| `client-onboarding` | Start an engagement cleanly: signed SOW, deposit, access by least privilege, kickoff, communication plan and success measures. | `operations-coordinator`, `client-success-manager`, `delivery-lead` |
| `account-review` | Run 30-day check-ins and quarterly business reviews: results against the baseline, health score, risks, renewal and expansion. | `client-success-manager` |
| `partner-vetting` | Vet and onboard referral, co-selling and white-label partners: fit, reputation, security, terms and the employer boundary. | `business-attorney`, `partner-ecosystem-manager` |

### Process improvement

| Skill | What it's for | Used by |
| --- | --- | --- |
| `process-health-check` | Map, measure and judge a process before anyone automates it: SIPOC, current-state map, baseline, waste and a readiness verdict. | `ai-solutions-engineer`, `business-analyst`, `lean-six-sigma-lead`, `process-data-analyst` |
| `kaizen-event` | Plan and run a 2–5 day rapid improvement event with the client's team, and hold the gains. | `lean-six-sigma-lead`, `continuous-improvement-coordinator` |
| `dmaic-project` | Run a Define-Measure-Analyze-Improve-Control project for a broken or unstable process, with data at every gate. | `lean-six-sigma-lead`, `process-data-analyst` |
| `statistical-analysis` | Pick and run the right statistics: measurement checks, control charts, capability, hypothesis tests and honest uncertainty. | `gis-remote-sensing-analyst`, `data-engineer`, `marketing-analyst`, `process-data-analyst` |
| `continuous-improvement` | Run the firm's own improvement system: kaizen cards, monthly PDCA, standard work, and changes to agents and skills. | `orchestrator`, `lean-six-sigma-lead`, `continuous-improvement-coordinator` |

### AI and platform delivery

| Skill | What it's for | Used by |
| --- | --- | --- |
| `readiness-assessment` | Assess a client's AI readiness: map workflows, score automation opportunities, set a governance baseline and a 90-day roadmap. | `ai-solutions-engineer`, `business-analyst`, `lean-six-sigma-lead` |
| `governed-agent-design` | Design an AI agent workflow that is scoped, identity-bound, least-privilege, reviewed, tested, logged and recoverable. | `senior-agent-engineer`, `ai-solutions-engineer`, `cto-principal-architect` |
| `mcp-integration` | Design and build a secure Model Context Protocol server that connects agents to one system with scoped, logged, idempotent tools. | `senior-agent-engineer`, `data-engineer`, `software-solutions-architect`, `backend-api-engineer` |
| `agent-safety-audit` | Audit an existing AI or agent setup: credentials, permissions, MCP servers, data flows, logging, review and recovery, with a scored report. | `senior-agent-engineer`, `security-compliance` |
| `threat-model` | Threat-model a system or agent: assets, trust boundaries, data flows, STRIDE threats including prompt injection, and mitigations. | `platform-devops-engineer`, `security-compliance`, `cto-principal-architect`, `software-solutions-architect`, `backend-api-engineer` |
| `architecture-decision-record` | Record a technical decision: context, options (including buy), trade-offs, the choice, consequences and how to reverse it. | `data-engineer`, `cto-principal-architect`, `software-solutions-architect` |
| `private-ai-platform` | Design a company memory and private AI platform in the client's own environment: PostgreSQL with pgvector, SSO, private networking and recovery. | `platform-devops-engineer`, `data-engineer`, `cto-principal-architect` |
| `release-and-deployment` | Ship a release safely: handoff package, staging, client acceptance, Erich's approval, GitOps promotion, verification and rollback. | `senior-agent-engineer`, `platform-devops-engineer`, `delivery-lead`, `software-engineering-lead`, `technical-writer` |
| `incident-response` | Handle an outage, security event or agent mistake: triage, contain, communicate, fix, recover, notify where required, and review blamelessly. | `platform-devops-engineer`, `client-success-manager`, `security-compliance` |
| `managed-operations` | Run the monthly retainer cycle for agents, platforms and Software Care: monitor, patch, tune, support and report. | `platform-devops-engineer`, `client-success-manager` |

### Software delivery

| Skill | What it's for | Used by |
| --- | --- | --- |
| `requirements-and-user-stories` | Turn business needs into user stories with testable acceptance criteria, a process map and a prioritized backlog. | `product-manager`, `software-solutions-architect`, `business-analyst`, `ux-ui-designer` |
| `software-build-standards` | The firm's coding standards, definition of done, pull-request review and the custom software lifecycle. | `software-engineering-lead`, `full-stack-developer`, `backend-api-engineer`, `mobile-developer`, `qa-test-automation-engineer` |
| `test-plan` | Plan and automate testing from the acceptance criteria, including agent evaluation sets, and report results objectively. | `senior-agent-engineer`, `software-engineering-lead`, `full-stack-developer`, `backend-api-engineer`, `mobile-developer`, `qa-test-automation-engineer` |
| `ux-design-review` | Design and review flows and screens for ease of use and accessibility (WCAG 2.1 AA), and test them with real users. | `web-developer-designer`, `ux-ui-designer`, `full-stack-developer`, `mobile-developer` |
| `runbook` | Write a runbook a client's own staff can follow: start, stop, check health, common failures, rollback, restore and contacts. | `senior-agent-engineer`, `platform-devops-engineer`, `technical-writer` |
| `project-plan-and-status` | Plan and run an engagement: plan, risks and issues log, weekly status, change requests and closeout. | `chief-of-staff`, `delivery-lead`, `software-engineering-lead` |

### Legal, finance and people

| Skill | What it's for | Used by |
| --- | --- | --- |
| `contract-review` | Review a contract or client redline clause by clause, rate each risk, propose fallback language and flag what a licensed attorney must see. | `business-attorney`, `insurance-risk-advisor` |
| `florida-business-compliance` | Keep the firm's filings, local business tax receipts, sales tax, employer registrations and data-law duties current in Florida. | `business-attorney`, `cpa-bookkeeper`, `insurance-risk-advisor`, `operations-coordinator`, `security-compliance`, `talent-people-partner` |
| `employer-boundary-screen` | Screen any prospect, partner, project or content for conflicts with Erich's employment at FPL/NextEra, and decline when unsure. | `orchestrator`, `business-attorney`, `business-development`, `gis-remote-sensing-analyst`, `utility-industry-advisor`, `partner-ecosystem-manager`, `market-research-analyst` |
| `break-even-and-cash-flow` | Model costs, revenue scenarios, break-even, cash flow and the full-time and hiring triggers. | `cpa-bookkeeper`, `advisory-board`, `product-manager`, `operations-finance-manager` |
| `monthly-finance-close` | Close the books each month: reconcile, invoice, chase collections, review margins and set aside taxes. | `cpa-bookkeeper`, `operations-coordinator`, `operations-finance-manager` |
| `risk-register` | Keep the risk register: likelihood, impact, owner and mitigation for each risk, mapped to insurance and reviewed quarterly. | `insurance-risk-advisor`, `operations-finance-manager` |
| `hiring-kit` | Hire and onboard well: hiring trigger check, job description, pay band, structured interviews, onboarding and offboarding. | `software-engineering-lead`, `talent-people-partner` |
| `vendor-and-tool-approval` | Evaluate and approve a tool, vendor or AI model: need, cost, security, data terms, license, lock-in and exit. | `operations-coordinator`, `security-compliance`, `cto-principal-architect`, `operations-finance-manager` |

### Marketing

| Skill | What it's for | Used by |
| --- | --- | --- |
| `marketing-plan` | Set positioning, audiences, channels, budget and monthly targets, and review results every month. | `product-manager`, `marketing-director`, `marketing-analyst` |
| `long-form-content` | Write articles, case studies, newsletters and lead magnets from real work, in the company voice, with every claim checked. | `content-marketing`, `marketing-director`, `seo-specialist` |
| `social-media-cycle` | Plan, write and schedule the weekly social posts, reply to the community, and report what worked. | `social-media-manager`, `video-editor`, `graphic-designer`, `community-manager` |
| `video-production` | Plan, script, record, edit and publish YouTube videos and short clips, with titles, thumbnails and analytics. | `youtube-producer`, `video-editor`, `graphic-designer` |
| `podcast-and-webinar` | Book podcast guest spots and run webinars: pitch, prep pack, run of show, follow-up and repurposing. | `trainer-curriculum`, `podcast-webinar-producer` |
| `paid-campaign` | Run small, measured ad tests with a budget cap and stop-loss, then scale only what pays back. | `marketing-director`, `paid-ads-specialist`, `marketing-analyst` |
| `seo-audit` | Research keywords by intent, audit the site's technical SEO and write content briefs that can rank. | `content-marketing`, `web-developer-designer`, `youtube-producer`, `seo-specialist` |
| `website-change` | Change dautel.io or a landing page safely: brief, design, build, accessibility and speed checks, QA, publish and measure. | `web-developer-designer`, `seo-specialist` |
| `marketing-metrics` | Define the funnel metrics, tag every link, attribute leads to channels and report honestly, including what didn't work. | `marketing-director`, `social-media-manager`, `seo-specialist`, `paid-ads-specialist`, `marketing-analyst` |
| `dautel-brand` | Apply the Dautel Design System and company voice to any site, app, document, slide, graphic or video. | `content-marketing`, `web-developer-designer`, `trainer-curriculum`, `ux-ui-designer`, `full-stack-developer`, `mobile-developer`, `technical-writer`, `marketing-director`, `social-media-manager`, `youtube-producer`, `video-editor`, `graphic-designer`, `community-manager`, `paid-ads-specialist`, `podcast-webinar-producer`, `quality-reviewer` |

### Products, training and team

| Skill | What it's for | Used by |
| --- | --- | --- |
| `product-offer-design` | Turn repeated client work into a fixed-scope, fixed-price offer with a one-pager, delivery checklist and success measures. | `trainer-curriculum`, `product-manager` |
| `workshop-design` | Design and run workshops, courses and coaching: learner personas, objectives, exercises, materials and feedback. | `trainer-curriculum`, `podcast-webinar-producer`, `lean-six-sigma-lead` |
| `utility-field-ops` | Phase 2 only: GIS, LiDAR, imagery and drone analysis for vegetation management, storm logistics and field documentation, once the employer boundary allows. | `gis-remote-sensing-analyst`, `utility-industry-advisor` |
| `agent-and-skill-authoring` | Create or improve agents and skills in this repository the right way: data in tools/, the official frontmatter, then build and check. | `agent-builder` |

## Coverage

- 50 agents in 11 groups; 57 skills in 8 categories.
- Most shared: `dautel-brand` (16 agents), `employer-boundary-screen` (7 agents), `operating-cadence` (6 agents), `pricing-and-estimating` (6 agents), `test-plan` (6 agents).
- Every skill is used by at least one agent, and every agent uses between 2 and 7 skills.
