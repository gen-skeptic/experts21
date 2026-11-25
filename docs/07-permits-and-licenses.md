# Permits and licenses

*Researched November 25, 2026 for an AI consulting and deployment firm based in Boynton Beach, Palm Beach County, Florida. The setup checklist at the end is copied from the DIO business plan research in gen-skeptic/experts. This is research, not legal or tax advice: confirm each item with the issuing office, a licensed Florida attorney and a CPA before relying on it.*

**Short version:** Florida has no state license for AI, software or IT consulting. To open, the firm needs a Florida LLC, an EIN, a **City of Boynton Beach business tax receipt** and a **Palm Beach County local business tax receipt** (both, in that order), plus a fictitious name registration only if it trades under a name other than the LLC's. Employer registrations (reemployment tax, workers' compensation) come later, with the first employees. Most of the legal weight is in the **contracts and data rules that apply to the work itself**, covered in the second half.

## 1. What to file, in order

| # | Item | Who issues it | Cost | Notes |
| :-: | --- | --- | --- | --- |
| 0 | **Employer clearance** | FPL/NextEra (Erich's employer) | — | Review the outside-employment, conflict-of-interest and IP-assignment policies and get written clearance if required. Do this before anything else ([risks](11-risks.md)) |
| 1 | **Florida LLC** (articles of organization, registered agent) | Florida Division of Corporations ([Sunbiz](https://dos.fl.gov/sunbiz/forms/fees/llc-fees/)) | $125 | Check name availability first. The annual report is due between January 1 and May 1 every year after formation: $138.75, or $538.75 late |
| 2 | **EIN** | IRS | Free | Needed for the bank account, payroll and 1099s |
| 3 | **Fictitious name** (DBA), only if needed | Florida Division of Corporations ([Sunbiz](https://dos.fl.gov/sunbiz/start-business/efile/fl-fictitious-name-registration/)) | $50 | Advertise the name once in a newspaper in Palm Beach County **before** filing; the form certifies it. Not needed if the firm trades as "Dautel Intelligent Operations, LLC" |
| 4 | **City of Boynton Beach business tax receipt** | City of Boynton Beach, Business Tax Unit ([BTR page](https://www.boynton-beach.org/btr)) | By classification; confirm with the city | Required **before** starting work, including for home-based businesses. There is a separate **home-based application**; home occupations limit customer visits, signage, employees and outside impacts to keep the street residential. A third-party summary reports a $125 fine for operating without one ([cityrulelookup](https://cityrulelookup.com/blog/home-business-rules-in-boynton-beach-fl)); verify the current limits in the city's Land Development Regulations |
| 5 | **Palm Beach County local business tax receipt** | Palm Beach County Tax Collector ([business tax](https://www.pbctax.gov/taxes/business-tax/)) | By classification | Required **in addition** to the city receipt, including one-person and home-based businesses. Apply after the city's zoning approval, with the fictitious name registration if any. Issued October to March: full-year price; April to September: half. Renew July 1 to September 30; late from October 1 (10% rising to 25% plus fees, and a $250 fine from February 1) |
| 6 | **Business bank account and bookkeeping** | — | — | Keep business and personal money separate from day one |
| 7 | **Insurance** (not a permit, but clients will ask) | Broker | About $1,200–$3,000 a year | Technology E&O plus cyber; certificates are often required by clients and MSP partners ([costs](06-startup-and-operating-costs.md)) |

### Taxes the firm may have to register for

| Tax | Applies when | Source |
| --- | --- | --- |
| **Florida sales and use tax** | Consulting and services built for one client are generally **not taxable** in Florida, and remotely accessed software (SaaS) has been ruled not taxable when nothing tangible is delivered. **Information services** sold to many customers (newsletters, research reports and compiled information not produced exclusively for one client) **are taxable**, and so is hardware (a pre-built "lab in a box"). Register with the Department of Revenue only before selling something taxable | Florida DOR [TAA 25A-011](https://floridarevenue.com/TaxLaw/Documents/25A-011.pdf); Rule 12A-1.062; vendor summaries of TAA 16A-014 |
| **Reemployment (unemployment) tax** | Once the firm pays $1,500 or more in wages in a calendar quarter, or has an employee on any part of a day in 20 different weeks of a year | [Florida DOR RT-800002](https://floridarevenue.com/Forms_library/current/rt800002.pdf) |
| **Workers' compensation** | Non-construction employers with **four or more employees**, counting LLC members who are officers of the business | [Florida Division of Workers' Compensation](https://www.myfloridacfo.com/division/wc/employer/coverage.htm) |
| **Tangible personal property tax** | Business furniture, fixtures and equipment worth $25,000 or more (count homelab hardware used for the business) | [Palm Beach County Tax Collector](https://www.pbctax.gov/taxes/business-tax/) |
| **Federal income and self-employment tax** | Always; a single-member LLC is taxed on the owner's return unless it elects otherwise | IRS; ask the CPA whether an S-corporation election pays off once profit is steady |

## 2. Rules that apply to the work itself

These don't need a permit, but they decide what the firm may build, what its contracts must say and what clients will ask.

| Rule | Who it affects | What the firm does about it |
| --- | --- | --- |
| **HIPAA** (privacy and security rules) | Medical, dental and therapy clients | Sign a business associate agreement (BAA) before touching patient data, and only when the stack, insurance and processes support it. Otherwise decline HIPAA work |
| **Florida Information Protection Act** (s. 501.171, F.S.) | Any client holding Floridians' personal information, and the firm itself | Breach notice to affected people within 30 days, and to the Attorney General when 500 or more Floridians are affected. Build logging and incident response into every design, and put breach-notice duties in the MSA and DPA |
| **Florida Digital Bill of Rights** (2023) | Mainly very large companies (over $1 billion in revenue) | Most small clients are outside its scope, but contracts with larger clients may pass its duties down to the firm |
| **Florida AI law** | Everyone | No general Florida AI statute as of November 2026: the AI Bill of Rights (CS/SB 482) died in the House on March 13, 2026, and SB 484 (signed May 7, 2026) covers hyperscale data centers. Keep bot disclosure, human review and data minimization in every design anyway; check other states' laws for remote clients ([market](02-market.md)) |
| **Florida Telephone Solicitation Act and the federal TCPA** | Agents that call or text a client's customers, and the firm's own outbound marketing | Automated calls and texts need prior express written consent; build consent records and opt-outs into any calling or texting agent. Have an attorney confirm the current rules before building one |
| **FTC rules on AI and marketing claims** | The firm's own marketing | No fake metrics, invented clients or testimonials; claims must be backed by evidence. This is also company value 2 |
| **Attorney confidentiality and privilege** (Florida Bar rules) | Law-firm clients | Private, client-owned AI; no client data in shared tools; confidentiality terms in the SOW |
| **Condominium and HOA website rules** (HB 1021, Ch. 2024-244) | Community association managers | A selling point, not a duty for the firm: associations with 25 or more units must post records online since January 1, 2026 |
| **Professional titles** | The firm's job titles | Florida licenses engineers; don't use "Professional Engineer" or "P.E." Ask the attorney whether "engineer" in role titles needs care in client-facing copy |
| **Employer boundary** | All work while Erich is employed at FPL/NextEra | No utility clients, no vegetation-management or line-clearance contractors, no known FPL/NextEra vendors, no competing work, and never employer time, equipment, data or confidential information |

## 3. Setup checklist

### From the business plan (§12)

- [ ] **Confirm no conflict with current employment** ([§13](11-risks.md)). Do this first.
- [ ] Form **Dautel Intelligent Operations, LLC** on Sunbiz (check name availability; consider a DBA if the LLC name differs).
- [ ] EIN, business bank account, bookkeeping (separate from personal).
- [ ] County and city **local business tax receipts**.
- [ ] **E&O plus cyber liability** insurance. Many SMB clients and MSP partners will ask for certificates.
- [ ] Contract templates: MSA, SOW, change order, data processing addendum, mutual NDA; a **BAA** for healthcare clients (or decline HIPAA work until the stack and insurance support it).
- [ ] **Subcontractor agreement** for contract developers and freelancers: IP assignment (to DIO or directly to the client), confidentiality, security obligations, and client approval of subcontractors in the MSA.
- [ ] **Workmanship warranty clause:** defects against the SOW's acceptance criteria, reported within the warranty period (proposed default 30 days after acceptance), fixed at no charge; excludes new features, changes by others, third-party changes and AI model behavior beyond the tested acceptance criteria.
- [ ] **Support terms** in every retainer SOW: support hours, response targets per tier, and the standing approval for standard changes.
- [ ] Written **AI use and data policy** (published on the trust page).
- [ ] Trademark search for "Dautel Intelligent Operations" and the Terminal Monogram (optional, later).
- [ ] Keep the brand privacy lock: no personal address, phone or email on public pages. Use the contact form relay already in place.

### Added November 25, 2026

- [ ] City of Boynton Beach **home-based** business tax receipt first (zoning approval), then the Palm Beach County receipt with the city approval attached.
- [ ] Put the county renewal (July 1 to September 30) and the Sunbiz annual report (January 1 to May 1) on the calendar.
- [ ] Ask the CPA which deliverables, if any, count as taxable information services or tangible goods before selling reports or hardware.
- [ ] Register for reemployment tax with the first payroll; add workers' compensation at four employees.
- [ ] Have the attorney review the calling and texting rules before building any outbound voice or SMS agent for a client.

## Sources

All retrieved November 25, 2026.

- Florida Division of Corporations: [LLC fees](https://dos.fl.gov/sunbiz/forms/fees/llc-fees/), [fictitious name registration](https://dos.fl.gov/sunbiz/start-business/efile/fl-fictitious-name-registration/), [annual report reminder](https://dos.fl.gov/communications/press-releases/2026/secretary-of-state-cord-byrd-reminds-florida-businesses-to-file-annual-report-before-may-1-deadline/)
- City of Boynton Beach: [Business Tax Receipts](https://www.boynton-beach.org/btr); home occupation summary from [cityrulelookup.com](https://cityrulelookup.com/blog/home-business-rules-in-boynton-beach-fl) (third party; verify)
- Palm Beach County Tax Collector: [Local Business Tax](https://www.pbctax.gov/taxes/business-tax/)
- Florida Department of Revenue: [TAA 25A-011](https://floridarevenue.com/TaxLaw/Documents/25A-011.pdf), [RT-800002 reemployment tax](https://floridarevenue.com/Forms_library/current/rt800002.pdf)
- Florida Division of Workers' Compensation: [coverage requirements](https://www.myfloridacfo.com/division/wc/employer/coverage.htm)
- Florida Senate: [CS/SB 482 (2026)](https://www.flsenate.gov/Session/Bill/2026/482); WUSF on [SB 484](https://www.wusf.org/politics-issues/2026-05-07/desantis-signs-bill-adding-regulations-for-hyper-scale-ai-data-centers); [Governor's press release](https://www.flgov.com/eog/news/press/2026/governor-ron-desantis-signs-law-protect-floridians-subsidizing-data-centers)
- Florida Legislature: [HB 1021 (2024)](https://www.flsenate.gov/Session/Bill/2024/1021)
