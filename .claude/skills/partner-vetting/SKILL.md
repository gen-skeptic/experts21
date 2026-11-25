---
name: partner-vetting
description: "Vet a potential partner (MSP, agency, vendor, freelancer marketplace) and set up the relationship: fit, reputation, security practices, client overlap, referral or white-label terms, the employer-boundary screen and a 90-day trial plan. Use before any partnership or subcontracting arrangement."
---

# Partner vetting

*Sales and clients skill for the DIO expert team.* Vet and onboard referral, co-selling and white-label partners: fit, reputation, security, terms and the employer boundary.

## When to use

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

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P21 Partner recruitment and onboarding). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `partner-ecosystem-manager`
- **Starts when:** Partner target identified (MSP, CPA, attorney, agency, vendor)
- **Done when:** Signed partner agreement, enablement kit delivered, partner pipeline tracked.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `partner-ecosystem-manager` | Assess partner fit | Partner fit note |
| 2 | Work | `market-research-analyst` | Background and reputation check | Background brief |
| 3 | Work | `partner-ecosystem-manager` | Draft the outreach and prepare the discovery meeting | Outreach draft + meeting brief |
| 4 | QA review | `quality-reviewer` | Check the outreach (accuracy, brand, employer boundary) and the background findings (outreach → step 3, background → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Work | `partner-ecosystem-manager` | Send the outreach and hold the discovery meeting | Meeting notes |
| 6 | Work | `business-attorney` | Draft the partner agreement | Agreement draft |
| 7 | Work | `operations-finance-manager` | Check partner economics | Economics check |
| 8 | QA review | `quality-reviewer` | Check the agreement against the economics and DIO standards (agreement → step 6, economics → step 7) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 9 | **Approval: Erich** | Erich (Chairman) | Approve and sign the agreement | Decision record (approved / changes requested / stopped) |
| 10 | Work | `partner-ecosystem-manager`, `graphic-designer`, `content-marketing` | Build the enablement kit | Enablement kit |
| 11 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 12 | Work | `partner-ecosystem-manager` | Deliver the kit; track partner pipeline monthly | Partner tracker |

## Used by

`business-attorney`, `partner-ecosystem-manager`.
