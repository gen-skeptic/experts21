---
name: website-change
description: "Make a change to dautel.io or a landing page: write the brief (goal, audience, success measure), design in the Dautel theme, build, check accessibility (WCAG 2.1 AA), speed, SEO and the privacy lock, preview, pass QA, publish and measure the effect. Use for any new page, copy change, offer page, booking path or landing page."
---

# Website change

*Marketing skill for the DIO expert team.* Change dautel.io or a landing page safely: brief, design, build, accessibility and speed checks, QA, publish and measure.

## When to use

Any new page, copy change, offer or pricing page, booking path, "How remote engagements work" page, trust and security page, or campaign landing page.

## Read first

- `docs/09-marketing.md` (§7.2 website changes and §8.5 changes for remote buyers).

## Method

1. **Brief:** the goal (for example "more fit calls booked from the services page"), the audience, the success measure and its baseline.
2. **Copy first:** a headline that says what we do and for whom; the offers with "starting at" prices; proof the buyer can check; one primary action per page (book a fit call).
3. **Design** in the Dautel theme (`data-theme="dautel"`) with the design system's components (`dautel-brand`).
4. **Build** on a branch; preview deploy.
5. **Check:** accessibility (contrast, keyboard, alt text, focus), mobile at 360 px, speed (no heavy images), SEO (title, description, headings, structured data), links, forms, and the privacy lock (no street address, personal phone or email; the contact form relay only).
6. **QA, then publish.** Prices and claims need Erich's approval.
7. **Measure** after two to four weeks against the baseline.

## Output

The brief, the change (pull request with preview link), the check results, and the measured effect.

## Rules for everything published

- **QA before publishing:** nothing is posted, sent, boosted or paid for until it passes `quality-reviewer`.
- **Erich approves** any spending, anything in his name, voice or likeness, and any ethical question (claims about clients, privacy, consent).
- **Real engagement only:** no bought followers, engagement pods, fake accounts, bots posing as people or fake reviews.
- **Disclosure:** FTC endorsement rules; label realistic AI-generated or altered media; say so when an AI agent answers on the firm's behalf.
- **Rights and consent:** only owned or licensed music, footage, images and fonts; written consent before showing a client, their data, or a person's face or voice.
- **Privacy and the employer boundary:** no family, home location, home network, dashboards with private data or secrets; no FPL/NextEra content, logos, sites, crews or data.
- **Measure:** tag links with UTM parameters and report results honestly, including what didn't work.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P20 DIO website change (dautel.io and landing pages)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `web-developer-designer`
- **Starts when:** Change request from marketing, sales, SEO (`seo-audit`), content publishing (`long-form-content`) or event registration (`podcast-and-webinar`). Content-only changes with copy already approved in `long-form-content` skip steps 2 and 6
- **Done when:** Change live on the DIO site and verified; analytics tagged.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `marketing-director` | Change brief: goal, audience, success metric | Change brief |
| 2 | Work | `content-marketing` | Write the copy (skip when `long-form-content` already approved it) | Copy |
| 3 | Work | `web-developer-designer` | Design and implement on a preview branch with the Dautel theme | Preview build |
| 4 | QA review | `seo-specialist` | SEO review (build → step 3, copy → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | QA review | `qa-test-automation-engineer` | Accessibility, links, forms, responsive checks | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | QA review | `security-compliance` | Review forms, scripts, trackers and headers when they change | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 7 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (build → step 3, copy → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | Decision | `marketing-director` | Decide to publish. Price changes, new paid tools, new trackers and privacy questions go to Erich | Decision record |
| 9 | **Approval: Erich** | Erich (Chairman) | Approve price changes, paid tools, new trackers or privacy questions (skip otherwise) | Decision record (approved / changes requested / stopped) |
| 10 | Work | `platform-devops-engineer` | Deploy through GitOps and verify | Live change |
| 11 | QA review | `qa-test-automation-engineer` | Production check; on failure DevOps rolls back first | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |

## Used by

`web-developer-designer`, `seo-specialist`.
