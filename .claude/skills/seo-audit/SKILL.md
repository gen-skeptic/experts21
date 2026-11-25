---
name: seo-audit
description: "Run search engine optimization: keyword research by segment and intent (local Boynton Beach and Palm Beach County queries and national specialist queries), technical audits (indexing, speed, structured data, internal links), the Google Business Profile, and content briefs that can rank. Use for SEO audits, keyword research, content briefs and monthly SEO reviews."
---

# SEO audit and briefs

*Marketing skill for the DIO expert team.* Research keywords by intent, audit the site's technical SEO and write content briefs that can rank.

## When to use

Monthly SEO review, before writing any article, and when the site changes.

## Method

1. **Keywords:** two sets.
   - **Local:** "AI consultant Boynton Beach", "process improvement consultant Palm Beach County", industry plus town (for example "law firm automation Delray Beach").
   - **National specialist:** "MCP server security checklist", "self-hosted AI for law firms", "shared memory for AI agents", "GitOps for small teams".
   For each: intent (learn, compare, buy), difficulty, and which page should rank.
2. **Technical audit:** indexing and sitemap, page speed and Core Web Vitals, mobile layout, titles and meta descriptions, headings, structured data (Organization, LocalBusiness as a service-area business, Article, FAQ), internal links, broken links, image alt text.
3. **Local presence:** Google Business Profile as a service-area business (no street address shown, per the privacy lock), consistent name and website across directories, real reviews only.
4. **Content briefs:** target query and intent, the questions to answer, the outline, the sources, internal links, and the call to action (`long-form-content`).
5. **Report monthly:** rankings for the target terms, organic visits, conversions from organic, and the next three actions.

## Output

The keyword map, the audit with prioritized fixes, briefs, and the monthly SEO report.

## Rules for everything published

- **QA before publishing:** nothing is posted, sent, boosted or paid for until it passes `quality-reviewer`.
- **Erich approves** any spending, anything in his name, voice or likeness, and any ethical question (claims about clients, privacy, consent).
- **Real engagement only:** no bought followers, engagement pods, fake accounts, bots posing as people or fake reviews.
- **Disclosure:** FTC endorsement rules; label realistic AI-generated or altered media; say so when an AI agent answers on the firm's behalf.
- **Rights and consent:** only owned or licensed music, footage, images and fonts; written consent before showing a client, their data, or a person's face or voice.
- **Privacy and the employer boundary:** no family, home location, home network, dashboards with private data or secrets; no FPL/NextEra content, logos, sites, crews or data.
- **Measure:** tag links with UTM parameters and report results honestly, including what didn't work.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P19 SEO monthly cycle). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `seo-specialist`
- **Starts when:** Monthly
- **Done when:** Change requests sent to `website-change`, briefs sent to `long-form-content`, organic report delivered.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `seo-specialist` | Update the keyword map and audit the site | Audit + keyword map |
| 2 | Work | `seo-specialist` | Write technical fixes and on-page optimizations as change requests for `website-change` | Change requests |
| 3 | Work | `seo-specialist` | Write content briefs for `long-form-content` | Content briefs |
| 4 | QA review | `quality-reviewer` | No keyword stuffing, accurate claims, no street address (change requests → step 2, briefs → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Work | `seo-specialist` | Send the change requests to `website-change` and the briefs to `long-form-content` | Requests sent |
| 6 | Work | `marketing-analyst` | Organic search report | SEO report |

## Used by

`content-marketing`, `web-developer-designer`, `youtube-producer`, `seo-specialist`.
