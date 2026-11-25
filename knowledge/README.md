# Knowledge folders

*The READMEs here are generated from `tools/team.py`; the documents beside them are not, and the build never touches them.*

Each agent has its own folder of reference documents. **Every agent reads its folder before it answers a question or starts a task**, uses what is there ahead of general knowledge, and names the documents it relied on.

## Rules for every folder

- **What goes in:** reference documents that make the role better: approved templates and good examples, standards and checklists, guidance from licensed advisors, and lessons learned.
- **What never goes in:** client confidential data, credentials or secrets, personal data, or confidential information from Erich's employer. **This repository is public.**
- **Shared research stays in `docs/`:** link to it rather than copying it.
- **Format:** Markdown or plain text where possible, under 1 MB each, named `YYYY-MM-short-topic.md`, with the source, owner and review date in the first lines.

## Folders

| Folder | Agent | What belongs there |
| --- | --- | --- |
| [`orchestrator/`](orchestrator/README.md) | Picard, Orchestrator (CEO agent) | The Chairman's standing guidance and the current quarterly goals (`operating-cadence`); Notes on which brain worked for which kind of task; Department heads' reviews and lessons from `operating-cadence` |
| [`chief-of-staff/`](chief-of-staff/README.md) | Riker, Chief of Staff (routing and cadence) | Routing plan templates and good examples; The meeting and reporting calendar; Past escalations and how they were resolved |
| [`advisory-board/`](advisory-board/README.md) | Guinan, Advisory Board (strategy sounding board) | Open questions in the business plan and the Chairman's goals; Past strategic decisions and how they turned out; Market and competitor briefs worth challenging |
| [`cto-principal-architect/`](cto-principal-architect/README.md) | Spock, CTO and Principal Architect | Architecture decision records and reference architectures; Technology standards and the approved stack; Post-incident reviews and their lessons |
| [`operations-finance-manager/`](operations-finance-manager/README.md) | Sisko, Operations and Finance Manager | Budget, rate card and cash-flow model notes; Vendor and subscription register (no credentials); Month-end close checklist and past closes |
| [`agent-builder/`](agent-builder/README.md) | Soong, Agent Builder (meta agent) | Notes on agents that answered badly and what fixed them; Patterns for good descriptions, tool lists and skills; Links to the official Claude Code subagent and skill documentation |
| [`business-attorney/`](business-attorney/README.md) | Cogley, Business Attorney (legal advisor) | Approved contract templates (MSA, SOW, NDA) and fallback clauses; Guidance from DIO's licensed attorney on recurring issues; Summaries of laws that affect clients (Florida AI and privacy law) |
| [`cpa-bookkeeper/`](cpa-bookkeeper/README.md) | Tuvok, CPA and Bookkeeper (finance and tax advisor) | Chart of accounts and bookkeeping policies; Tax and filing calendar; Guidance from DIO's licensed CPA |
| [`insurance-risk-advisor/`](insurance-risk-advisor/README.md) | Saru, Insurance and Risk Advisor | Policy summaries and limits (no policy numbers); Insurance requirements from client contracts seen so far; Risk register excerpts and broker guidance |
| [`quality-reviewer/`](quality-reviewer/README.md) | Odo, Quality Reviewer (QA gate) | Review checklists by type of deliverable; Recurring findings and their root causes; Severity definitions with examples |
| [`lean-six-sigma-lead/`](lean-six-sigma-lead/README.md) | Seven, Lean Six Sigma Lead (process improvement) | Kaizen and DMAIC templates (SIPOC, charters, control plans); Process health check findings, anonymized; Facilitation guides |
| [`process-data-analyst/`](process-data-analyst/README.md) | Bashir, Process Data Analyst (Six Sigma statistics) | Statistical method notes and worked examples; Measurement system analysis templates; Baseline datasets (synthetic or anonymized) |
| [`continuous-improvement-coordinator/`](continuous-improvement-coordinator/README.md) | Rom, Continuous Improvement Coordinator (and manual maintainer) | Kaizen card log and outcomes; PDCA review notes; Change history of the operating manual |
| [`client-success-manager/`](client-success-manager/README.md) | Troi, Client Success and Account Manager | Account health criteria and check-in templates; QBR deck template and past QBR outcomes; Common client questions and approved answers |
| [`business-development/`](business-development/README.md) | Kirk, Business Development Lead | Ideal customer profile, prospect research briefs and segment pitches; Discovery-call question bank and qualification notes; Proposal examples and win/loss notes |
| [`partner-ecosystem-manager/`](partner-ecosystem-manager/README.md) | Sarek, Partner Ecosystem Manager | Partner profiles and agreement summaries; Referral and co-selling playbooks; Partner vetting results |
| [`market-research-analyst/`](market-research-analyst/README.md) | Dax, Market Research Analyst | Prospect research briefs and their source lists (such as the Boynton Beach brief); Segment briefs and the regulation tracker; Trusted sources, with notes on their biases |
| [`senior-agent-engineer/`](senior-agent-engineer/README.md) | Data, Senior AI Agent Engineer | Agent architecture patterns and reference implementations (Cassian, OpenBrain integrations); MCP server and tool design conventions; Agent safety checklists and lessons from past incidents |
| [`platform-devops-engineer/`](platform-devops-engineer/README.md) | O'Brien, Platform and DevOps Engineer | Runbooks and recovery drill results; Cluster, GitOps and secrets-management conventions; Approved base images and dependency policy |
| [`ai-solutions-engineer/`](ai-solutions-engineer/README.md) | The Doctor, AI Solutions Engineer | Readiness assessment templates and scoring rubrics; Workflow maps by industry (law, dental, community association management, CPA); Past assessment findings, anonymized |
| [`security-compliance/`](security-compliance/README.md) | Worf, Security and Compliance Specialist | Security baselines and control checklists; Regulatory references (HIPAA BAA, Florida privacy and AI law); Threat models and audit findings, anonymized |
| [`data-engineer/`](data-engineer/README.md) | Stamets, Data Engineer | Data models, naming conventions and lineage notes; Pipeline templates and synthetic test datasets; PostgreSQL and pgvector tuning notes |
| [`delivery-lead/`](delivery-lead/README.md) | Janeway, Technical Project Manager / Delivery Lead | Project plan and status report templates; Estimation history: planned versus actual; Risk and issue logs from closed projects, anonymized |
| [`software-engineering-lead/`](software-engineering-lead/README.md) | Geordi, Software Engineering Lead | Coding standards, review checklist and definition of done; Release handoff packages that passed; Estimation and velocity history |
| [`software-solutions-architect/`](software-solutions-architect/README.md) | Brahms, Software Solutions Architect | Solution design templates and past designs; Build-versus-buy evaluations; Integration patterns and vendor API notes |
| [`business-analyst/`](business-analyst/README.md) | Chakotay, Business Analyst | Requirements and user-story templates; Process maps and glossaries by industry; Good acceptance-criteria examples |
| [`ux-ui-designer/`](ux-ui-designer/README.md) | Kes, UX/UI Designer | Notes on using the design system and component decisions; Usability test scripts and findings; Approved flows and wireframes |
| [`full-stack-developer/`](full-stack-developer/README.md) | Wesley, Full-Stack Developer | Project scaffolds and code conventions; Snippets for recurring features (auth, forms, dashboards); Lessons from code reviews |
| [`backend-api-engineer/`](backend-api-engineer/README.md) | Torres, Back-End and API Engineer | API style guide and versioning rules; Integration notes for common client systems; Idempotency and retry patterns |
| [`mobile-developer/`](mobile-developer/README.md) | Barclay, Mobile Developer | Mobile and PWA conventions and offline patterns; Device test matrix; App store submission checklists |
| [`qa-test-automation-engineer/`](qa-test-automation-engineer/README.md) | T'Pol, QA and Test Automation Engineer | Test strategy and test plan templates; Automation framework conventions; Defect categories and escaped-defect history |
| [`technical-writer/`](technical-writer/README.md) | Jake, Technical Writer | Documentation style guide and templates (runbooks, user guides); Glossary of DIO and client terms; Examples of documents readers praised |
| [`content-marketing/`](content-marketing/README.md) | Hoshi, Content and Marketing Specialist (long-form) | Brand voice examples that worked, and some that didn't; Audience personas and the questions they ask; Published pieces and how they performed |
| [`web-developer-designer/`](web-developer-designer/README.md) | Trip, Web Developer and Designer (DIO sites) | Site structure, component inventory and analytics notes for dautel.io; Accessibility and performance budgets; Approved page templates and copy blocks |
| [`marketing-director/`](marketing-director/README.md) | Uhura, Marketing Director (head of marketing) | Quarterly marketing plans and their results; Positioning and message architecture; Budget and channel performance history |
| [`social-media-manager/`](social-media-manager/README.md) | Tilly, Social Media Manager | Platform playbooks and the posting calendar; Approved post examples and hooks that worked; Community guidelines and escalation rules |
| [`youtube-producer/`](youtube-producer/README.md) | Paris, YouTube Channel Producer | Channel strategy, series plans and title formulas; Retention and analytics notes per video; Script templates |
| [`video-editor/`](video-editor/README.md) | Harry, Video Editor and Short-Form Specialist | Edit style guide (pace, captions, lower thirds); Clip library index; Export presets per platform |
| [`graphic-designer/`](graphic-designer/README.md) | Garak, Graphic Designer (brand and social assets) | Approved asset templates in the Dautel Design System; Image and icon sources with their licenses; Examples of on-brand and off-brand work |
| [`community-manager/`](community-manager/README.md) | Neelix, Community Manager | Community guidelines and moderation playbook; FAQ and approved answers; Member highlights and event notes |
| [`seo-specialist/`](seo-specialist/README.md) | Chekov, SEO Specialist | Keyword research by segment and search intent; Technical SEO audit history; Content briefs that ranked |
| [`paid-ads-specialist/`](paid-ads-specialist/README.md) | Quark, Paid Advertising Specialist | Campaign structures, audiences and budgets that worked; Ad copy and creative test results; Advertising platform policy notes |
| [`podcast-webinar-producer/`](podcast-webinar-producer/README.md) | Vic, Podcast and Webinar Producer | Run-of-show templates and guest prep packs; Guest list and topic backlog; Repurposing checklist |
| [`marketing-analyst/`](marketing-analyst/README.md) | Ro, Marketing Analyst | Metric definitions and dashboard specs; Attribution model notes; Monthly marketing reports |
| [`operations-coordinator/`](operations-coordinator/README.md) | Nog, Operations Coordinator (virtual assistant) | Scheduling and travel preferences (no personal details); Procedures for vendors and tools (no credentials); Recurring admin checklists |
| [`trainer-curriculum/`](trainer-curriculum/README.md) | Pike, Trainer and Curriculum Developer | Course outlines, exercises and slide templates; Workshop feedback and what changed after it; Learner personas by industry |
| [`product-manager/`](product-manager/README.md) | Burnham, Product Manager | Productized offer one-pagers and pricing rationale (from the business plan); Customer interview notes, anonymized; Roadmap decisions and the evidence behind them |
| [`talent-people-partner/`](talent-people-partner/README.md) | Beverly, Talent and People Partner | Job description and interview kit templates; Onboarding checklists; Compensation bands from the business plan (no personal data) |
| [`gis-remote-sensing-analyst/`](gis-remote-sensing-analyst/README.md) | Sulu, GIS and Remote-Sensing Analyst | Data source catalog with licenses and projections; Processing recipes for LiDAR, imagery and drone data; Phase-2 vertical notes (no work until the employer boundary allows it) |
| [`utility-industry-advisor/`](utility-industry-advisor/README.md) | Scotty, Utility Industry Advisor (fractional) | Summaries of public utility regulations and standards; Field operations glossaries and safety practices; Phase-2 market notes (never employer confidential information) |
