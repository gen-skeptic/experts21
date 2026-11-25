"""Skills: marketing and the brand."""

MARKETING_RULES = """## Rules for everything published

- **QA before publishing:** nothing is posted, sent, boosted or paid for until it passes `quality-reviewer`.
- **Erich approves** any spending, anything in his name, voice or likeness, and any ethical question (claims about clients, privacy, consent).
- **Real engagement only:** no bought followers, engagement pods, fake accounts, bots posing as people or fake reviews.
- **Disclosure:** FTC endorsement rules; label realistic AI-generated or altered media; say so when an AI agent answers on the firm's behalf.
- **Rights and consent:** only owned or licensed music, footage, images and fonts; written consent before showing a client, their data, or a person's face or voice.
- **Privacy and the employer boundary:** no family, home location, home network, dashboards with private data or secrets; no FPL/NextEra content, logos, sites, crews or data.
- **Measure:** tag links with UTM parameters and report results honestly, including what didn't work.
"""

MARKETING = {
"marketing-plan": dict(
 title="Marketing plan", category="Marketing",
 summary="Set positioning, audiences, channels, budget and monthly targets, and review results every month.",
 description="Build and review the marketing plan: positioning and message, audience segments, the channel mix ranked by expected return for a side practice, the content calendar, budget, targets per channel and the monthly review of what worked. Use for quarterly marketing planning, monthly reviews and any new campaign.",
 body="""## When to use

Each quarter (the plan) and each month (the review); before any new campaign or channel.

## Read first

- `docs/09-marketing.md` (message architecture, channels ranked by expected return, lead magnets, sales process), `docs/03-target-customers.md`, `docs/04-competitors.md`.

## Method

1. **Positioning:** "Fix first, then automate" and "AI agents your business can actually operate"; local on trust, national on specialization.
2. **Audiences:** pick at most three segments for the quarter (for example community association managers, PI and elder law firms, multi-dentist practices), each with its pain and lead offer.
3. **Channels:** rank by expected return for a side practice with 10–12 hours a week: referrals and local partners, LinkedIn on Erich's profile, workshops, content with SEO, then video, newsletter and paid tests.
4. **Calendar:** what ships each week per channel, with owners.
5. **Budget:** by channel, with a stop-loss rule for paid spend. Erich approves all spending.
6. **Targets:** leads, fit calls, proposals and wins per channel; cost per lead for paid.
7. **Monthly review:** results against targets (`marketing-metrics`), what to double, what to stop, one experiment for next month.

## Output

A one-page plan per quarter and a one-page monthly review.
""" + "\n" + MARKETING_RULES),

"long-form-content": dict(
 title="Long-form content", category="Marketing",
 summary="Write articles, case studies, newsletters and lead magnets from real work, in the company voice, with every claim checked.",
 description="Write long-form content: articles and guides, case studies (the fix-first story with before-and-after data and client permission), the newsletter and lead magnets (checklists, guides), from a brief with audience, search intent, outline and sources, in the company voice, fact-checked. Use for any article, case study, newsletter, guide or lead magnet.",
 body="""## When to use

Any article, guide, case study, newsletter issue or lead magnet (for example the Agent Safety Checklist).

## Method

1. **Brief:** audience, the problem they search for, the one takeaway, the call to action, target keyword and intent (`seo-audit`), and the sources.
2. **Outline:** a headline that promises something specific; sections as questions the reader has.
3. **Draft from real work:** the firm's own systems, engagements (with permission) and evidence. Concrete examples over adjectives.
4. **Case studies** follow the fix-first story: the client's problem, the process fix, then the automation, with before-and-after numbers measured the same way, and the client's written approval of every detail.
5. **Voice:** company copy says "we"; "I" only in Erich's own founder posts. Plain, confident and specific; sentence case; no emoji; no hype; no fake metrics.
6. **Fact-check** every number, law and claim (`research-and-fact-check`).
7. **Format:** short paragraphs, descriptive headings, one idea per paragraph, alt text on images, a clear call to action.

## Output

The draft, its sources, the meta title and description, and the suggested social snippets.
""" + "\n" + MARKETING_RULES),

"social-media-cycle": dict(
 title="Social media cycle", category="Marketing",
 summary="Plan, write and schedule the weekly social posts, reply to the community, and report what worked.",
 description="Run the weekly social media cycle: plan the week's posts from real work and the content calendar, write hooks, posts and captions for each platform, prepare visuals and clips, schedule after QA, answer comments and messages within the reply guidelines, and report results. Use for posts, captions, hooks, replies and community moderation.",
 body="""## When to use

Every week, and whenever a comment or message needs a reply.

## Method

1. **Plan (Monday):** three to five posts for the week from real work: a lesson from an engagement (with permission), a how-to, a teardown, a workshop or article announcement.
2. **Platform first:** LinkedIn is the main channel (Erich's founder profile in his own voice, the company page in "we"); others only where buyers are.
3. **Write:** a hook in the first line (specific, no clickbait), one idea per post, a clear ending (a question or a link). No emoji, no hype, no hashtag walls.
4. **Visuals:** Catppuccin themes for social graphics and clips (`dautel-brand`); captions on every video.
5. **QA, then schedule.** Erich approves anything in his name or voice.
6. **Reply** within one business day, helpful and human, following the written reply guidelines; anything outside them goes through QA first. Never argue; take problems to a private channel.
7. **Moderate** fairly: remove spam and abuse, never criticism.
8. **Report (Friday):** reach, engagement, profile visits, clicks and any leads, with notes on what to repeat.

## Output

The week's calendar with final copy and visuals, the reply log, and the weekly report.
""" + "\n" + MARKETING_RULES),

"video-production": dict(
 title="Video production", category="Marketing",
 summary="Plan, script, record, edit and publish YouTube videos and short clips, with titles, thumbnails and analytics.",
 description="Produce video: pick topics from search demand and real systems, write the script and shot list, prepare recordings (with privacy checks on every screen), edit for pace with captions and lower thirds, write the title, description and thumbnail, cut short clips for other platforms, publish and read the retention analytics. Use for YouTube videos, walkthroughs, demos and short clips.",
 body="""## When to use

YouTube walkthroughs and demos (5–10 minutes), recorded workshops, and short clips for LinkedIn and other platforms.

## Method

1. **Topic:** a question buyers search for or a real system worth showing ("Recovering a K3s cluster from Git", "How we review an agent's draft before it's sent").
2. **Script:** a hook in the first 15 seconds that says what the viewer will get, then the steps, then one call to action. Write for the ear.
3. **Shot list:** screens, camera segments, diagrams.
4. **Privacy check before recording:** no secrets, IP addresses, private dashboards, client data, family or home details on screen; use a demo environment.
5. **Edit:** cut pauses and repeats, keep a steady pace, captions always, lower thirds for names and terms, Catppuccin theme for graphics.
6. **Package:** a title that matches the search intent, a description with timestamps and links (UTM-tagged), a thumbnail with at most four words, chapters.
7. **Shorts:** two or three clips of 30–60 seconds, each one idea, captioned, vertical.
8. **Disclose** synthetic or altered media with the platform's label.
9. **Review analytics** after a week: click-through rate, average view duration, where viewers drop off; note the lesson.

## Output

The script and shot list, the edited video and clips, the title, description and thumbnail, and the one-week analytics note.
""" + "\n" + MARKETING_RULES),

"podcast-and-webinar": dict(
 title="Podcast and webinar", category="Marketing",
 summary="Book podcast guest spots and run webinars: pitch, prep pack, run of show, follow-up and repurposing.",
 description="Get Erich on podcasts and run webinars: find shows and audiences that match the buyers, write the pitch, prepare the guest prep pack (bio, talking points, stories, links), plan the webinar run of show, handle registration and follow-up, and repurpose each recording into clips, posts and an article. Use for podcast outreach, guest prep, webinars and virtual talks.",
 body="""## When to use

Podcast guesting, webinars, virtual meetups and talks.

## Method

1. **Find shows:** small-business, DevOps, AI and veteran podcasts whose listeners match the buyers; check recent episodes and audience.
2. **Pitch:** short and specific: why this guest for this audience, three topic angles, one memorable story (the arborist and soldier turned AI operations engineer), links.
3. **Prep pack:** bio (approved by Erich), talking points, three stories with numbers that are true, the call to action, and what not to say (client names without permission, employer matters).
4. **Webinar run of show:** 45 minutes: 5 welcome, 25 teaching with a live example, 10 questions, 5 next step. Rehearse the demo; have a backup recording.
5. **Registration and reminders**, then a recap email with the recording and one clear next step.
6. **Repurpose:** clips (`video-production`), posts (`social-media-cycle`) and an article (`long-form-content`).

## Output

The target list and pitches, the prep pack, the run of show, the follow-up email, and the repurposing plan.
""" + "\n" + MARKETING_RULES),

"paid-campaign": dict(
 title="Paid campaign", category="Marketing",
 summary="Run small, measured ad tests with a budget cap and stop-loss, then scale only what pays back.",
 description="Plan and run a paid advertising campaign: objective and offer, audience, a budget cap and stop-loss rule approved by Erich, ad variants and landing page, conversion tracking with UTM tags, daily checks, and a results report with cost per lead and pipeline. Use for LinkedIn, Google or other paid tests, boosts and retargeting.",
 body="""## When to use

Testing a paid channel or promoting a workshop, lead magnet or productized offer. Paid is a test channel for a side practice, never the base.

## Method

1. **Objective:** one measurable result (workshop registrations, lead-magnet downloads, fit calls booked).
2. **Offer and landing page:** one offer per campaign; the page says the same thing as the ad (`website-change`).
3. **Audience:** for LinkedIn, job titles and company sizes from the target segments in South Florida or nationally; for Google, the search terms with clear buying intent and a list of negative keywords.
4. **Budget:** a total cap and a daily cap, plus a stop-loss (for example stop if no conversion after spending two times the target cost per lead). **Erich approves the budget before anything runs.**
5. **Variants:** two or three ads differing in one thing at a time.
6. **Tracking:** conversion events and UTM parameters on every link; check they fire before launch.
7. **Check daily:** spend, clicks, conversions, cost per lead; pause losers early.
8. **Report:** results, cost per lead and per fit call, what happened in the pipeline later, and a recommendation (stop, keep testing or scale).

## Output

The campaign brief, ad copy and visuals, the tracking plan, and the results report.
""" + "\n" + MARKETING_RULES),

"seo-audit": dict(
 title="SEO audit and briefs", category="Marketing",
 summary="Research keywords by intent, audit the site's technical SEO and write content briefs that can rank.",
 description="Run search engine optimization: keyword research by segment and intent (local Boynton Beach and Palm Beach County queries and national specialist queries), technical audits (indexing, speed, structured data, internal links), the Google Business Profile, and content briefs that can rank. Use for SEO audits, keyword research, content briefs and monthly SEO reviews.",
 body="""## When to use

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
""" + "\n" + MARKETING_RULES),

"website-change": dict(
 title="Website change", category="Marketing",
 summary="Change dautel.io or a landing page safely: brief, design, build, accessibility and speed checks, QA, publish and measure.",
 description="Make a change to dautel.io or a landing page: write the brief (goal, audience, success measure), design in the Dautel theme, build, check accessibility (WCAG 2.1 AA), speed, SEO and the privacy lock, preview, pass QA, publish and measure the effect. Use for any new page, copy change, offer page, booking path or landing page.",
 body="""## When to use

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
""" + "\n" + MARKETING_RULES),

"marketing-metrics": dict(
 title="Marketing metrics", category="Marketing",
 summary="Define the funnel metrics, tag every link, attribute leads to channels and report honestly, including what didn't work.",
 description="Measure marketing: define the funnel metrics (reach, engagement, leads, fit calls, proposals, wins, revenue), UTM conventions, lead-source attribution in the CRM, dashboards, and an honest monthly report that separates vanity metrics from pipeline. Use for any marketing report, dashboard, channel comparison or campaign result.",
 body="""## When to use

Monthly marketing reviews, campaign results, and any question about which channel works.

## Metric definitions

| Stage | Metric | Source |
| --- | --- | --- |
| Attention | Impressions, reach, video views | Platform analytics |
| Interest | Engagement rate, site visits, newsletter subscribers | Platform analytics, web analytics |
| Lead | Form fills, lead-magnet downloads, workshop registrations | Web analytics, forms |
| Opportunity | Fit calls booked and held | CRM |
| Pipeline | Proposals sent and their value | CRM |
| Revenue | Deals won, revenue, retainer MRR | CRM and bookkeeping |

## Method

1. **UTM convention:** `utm_source` (linkedin, youtube, newsletter, partner-name), `utm_medium` (social, video, email, referral, cpc), `utm_campaign` (yyyy-mm-topic). Every link out uses it.
2. **Lead source:** every lead in the CRM records its first and most recent source; ask "how did you hear about us?" on the fit call.
3. **Report monthly:** each funnel stage by channel against the targets in the marketing plan; cost per lead and per fit call for paid; conversion between stages.
4. **Vanity check:** say plainly when impressions rose but leads didn't.
5. **Small numbers:** a side practice has few leads; treat month-to-month changes with caution (`statistical-analysis`) and look at quarters.
6. **Recommend:** what to double, what to stop, one experiment.

## Output

The monthly marketing report (one page plus a table) and any dashboard spec.
"""),

"dautel-brand": dict(
 title="Dautel brand and design system", category="Marketing",
 summary="Apply the Dautel Design System and company voice to any site, app, document, slide, graphic or video.",
 description="Apply the Dautel brand to anything visual or written for the firm: the voice rules (\"we\", sentence case, no emoji, no hype, no fake metrics, privacy lock), the right theme (Dautel for the firm's own sites; Catppuccin for software, demos, social and customer work; the client's own brand when it has one), the role color tokens and their meanings, JetBrains Mono and Manrope, shapes, the Terminal Monogram logo rules and accessibility. Use for any website, app, slide, document, graphic, thumbnail or video.",
 body="""## When to use

Anything visual or published: sites, apps, slides, documents, social graphics, thumbnails, video graphics. The design system files are in `design-system/` (copied from gen-skeptic/dautel_brand); `design-system/BRAND.md` is the full rule set and `design-system/index.html` the reference page.

## Voice

- Company copy says **"we"**; "I" only in Erich's own founder posts and personal portfolio pages.
- Plain, confident and specific; **sentence case** for headlines and buttons; **no emoji, no hype, no fake metrics**, no decorative status. Status shown must be real.
- Section titles are short noun phrases with the terminal prompt: `>_ Selected systems`.
- **Privacy lock:** never publish a street address, personal phone, personal email or a resume with contact details.

## Which theme

| Where | Theme |
| --- | --- |
| The firm's own sites: dautel.io, home.dautel.cloud, its landing and campaign pages | **Dautel** (`data-theme="dautel"`) |
| Software, examples and demos, social graphics and video, customer sites | **Catppuccin**: Mocha by default; Macchiato, Frappé or Latte when there's a reason |
| A client with its own brand | **The client's brand**, without the Dautel mark |
| A client without a brand | Catppuccin, the client's name in mono, no Dautel mark |

## In code

- Load `design-system/dautel.css` once and set `data-theme` on `<html>`.
- Style only with role tokens: `var(--ink)`, `var(--ink-soft)`, `var(--surface)`, `var(--surface-strong)`, `var(--text)`, `var(--muted)`, `var(--quiet)`, `var(--rule)`, `var(--blue)`, `var(--mint)`, `var(--lavender)`, `var(--peach)`, `var(--danger)`. **Never hard-code hex values or other fonts.**
- Type and components: `.display`, `.lead`, `.section-title`, `.label`, `.micro`; `.button.button-primary`, `.section-heading`, `.panel`, `.panel-cut`, `.topology-node`, `.topology-status`, `.contact-form`, `.dot-grid`, `.container`.

## Color meaning (one accent per element)

- **blue:** primary action, the `>_` prompt, focus, Agents.
- **mint:** live or healthy status, secondary action, success, Infrastructure.
- **lavender:** the descriptor, Operations.
- **peach:** contact actions only.
- **danger:** errors, always with a word.

## Type and shape

- **JetBrains Mono** (the Nerd Font where installed) for navigation, controls, labels and short headings; **Manrope** for prose. Section titles start with a blue `>_`.
- Small radii only, **no pills**; 12px clipped corners on feature panels; 1px hairlines; dot and line grids drawn, never washed. **No shadows, gradients, glow or glassmorphism.**
- Motion: 160ms color and small lifts; `prefers-reduced-motion` turns it off.

## Logo

- The Terminal Monogram files in `design-system/logos/`, used as provided, on `ink` or another approved dark surface; lockup 220px or wider, mark 24px or larger; alt text "Dautel Intelligent Operations".
- Never stretch, rotate, outline, recolor, add effects, or place it on a busy image. Never on customer work that has its own brand.

## Accessibility

WCAG 2.1 AA contrast (keep `quiet` for icons and large text only), a visible blue focus ring with 4px offset, full keyboard paths. Latte's green and peach are under 3:1 on its base: use them only as fills or outlines beside words in `text`.

## Non-web media

Slides, video, images and print use the palette values of the right theme from `dautel.css`, the same fonts and the same shape rules. `quality-reviewer` fails branded work that breaks these rules.
"""),
}
