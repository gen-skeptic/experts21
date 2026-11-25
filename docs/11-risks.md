# Biggest risks

*Source: copied from the DIO business plan research in gen-skeptic/experts (`research/dautel-intelligent-operations-business-plan-research.md`, compiled November 19, 2026), updated November 25, 2026 where noted. Process numbers such as P33 refer to the DIO operating manual in that repository; in this repository the same methods are skills in `.claude/skills/`.*

What could sink the firm, and the mitigation for each.

## 13. Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| **Employer conflict of interest / outside-employment policy** (FPL/NextEra) | Review the NextEra code of conduct and outside-activity policy; disclose in writing if required; **no utility, FPL vendor or competing clients** while employed; never use employer time, equipment, data or confidential information; check IP-assignment clauses |
| Limited time while employed and in the MBA | Productized fixed-scope offers, a strict WIP limit of one build at a time, retainers capped at about five |
| "Homelab ≠ business experience" objection | Discounted founding-client pilots (2–3) in exchange for case studies; lean on operations leadership credentials |
| AI tool churn (agent frameworks change monthly) | Sell architecture and operating discipline (MCP, identity, review, recovery), not specific tools. The ongoing tool evaluations become content |
| Client data incident | Least privilege by default, client-owned infrastructure, insurance, incident runbook, no client data in personal or homelab systems |
| Fixed-price software projects overrun | Paid discovery first; MVP-first phasing; 15–20% contingency; written change orders; weekly demos; release handoff checklist so deployment surprises don't land on DevOps at the end |
| Commoditized pricing pressure | Stay out of the chatbot-agency race; compete on governance, operations and local trust |
| Regulatory change (Florida AI law, federal preemption debates) | Track via newsletter; turn compliance readiness into a selling point |
| **Founder availability** (FPL storm-restoration duty in hurricane season, travel, illness) | Only financial, ethical and final-deployment decisions wait for Erich; standing approvals for retainer changes; pre-approved rollback; reduced-availability client notice; SOW response targets with no 24/7 promise; name a backup approver ([§15](12-90-day-plan-and-open-questions.md)) |
| **AI agent errors** (agents produce wrong or unsafe work) | QA in every process, correction loops, Erich's approval for deployments and money, evaluation sets for client agents, blameless reviews feeding P36 |
| **Open-source license limits** (Open Brain and OpsBrain are FSL-1.1-MIT: no competing commercial product or service until each version turns MIT two years after release) | Use OpsBrain internally only; deliver Line C as professional services into client-owned, client-licensed environments; build any memory product independently; attorney review before the first Line C sale and before any product launch |
| **AI vendor dependence** (model price, availability or policy changes) | Vendor review through P42, pass-through model costs in contracts, model-agnostic designs (MCP, OpenRouter), a fallback model for client agents |

---

### Updates (November 25, 2026)

| Risk | What changed | Mitigation |
| --- | --- | --- |
| **Regulatory change** | Florida's AI Bill of Rights (CS/SB 482) died in the House on March 13, 2026; the AI law that passed (SB 484) covers hyperscale data centers. There is still no general Florida AI statute, but other states have their own, and federal preemption is still debated ([market](02-market.md#32b-florida-rules-that-move-demand-checked-november-25-2026)) | Track Florida's 2027 session; check the client's state law before every remote engagement; keep compliance readiness (bot disclosure, data minimization, human review) in every design anyway |
| **Crowded local entry level** | At least four AI consultancies started near Boynton Beach in 2025–2026, and out-of-area agencies buy local search terms ([competitors](04-competitors.md)) | Don't compete on price; lead with the fix-first assessment and governance, and with proof buyers can check |
| **Hurricane season** (June 1 to November 30) | A Boynton Beach firm can lose power, internet or the founder's time (FPL storm duty) for days | Client systems run in client-owned cloud accounts, never on the homelab; written reduced-availability notice; backup connectivity; recovery drills before June |
| **Permits and local tax** | The city and county business tax receipts are separate, both are required, and the county's is delinquent from October 1 with penalties from 10% to 25% plus fines | Calendar both renewals (county: July 1 to September 30) in the [permits checklist](07-permits-and-licenses.md) |

