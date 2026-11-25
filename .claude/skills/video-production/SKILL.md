---
name: video-production
description: "Produce video: pick topics from search demand and real systems, write the script and shot list, prepare recordings (with privacy checks on every screen), edit for pace with captions and lower thirds, write the title, description and thumbnail, cut short clips for other platforms, publish and read the retention analytics. Use for YouTube videos, walkthroughs, demos and short clips."
---

# Video production

*Marketing skill for the DIO expert team.* Plan, script, record, edit and publish YouTube videos and short clips, with titles, thumbnails and analytics.

## When to use

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

## Rules for everything published

- **QA before publishing:** nothing is posted, sent, boosted or paid for until it passes `quality-reviewer`.
- **Erich approves** any spending, anything in his name, voice or likeness, and any ethical question (claims about clients, privacy, consent).
- **Real engagement only:** no bought followers, engagement pods, fake accounts, bots posing as people or fake reviews.
- **Disclosure:** FTC endorsement rules; label realistic AI-generated or altered media; say so when an AI agent answers on the firm's behalf.
- **Rights and consent:** only owned or licensed music, footage, images and fonts; written consent before showing a client, their data, or a person's face or voice.
- **Privacy and the employer boundary:** no family, home location, home network, dashboards with private data or secrets; no FPL/NextEra content, logos, sites, crews or data.
- **Measure:** tag links with UTM parameters and report results honestly, including what didn't work.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P16 YouTube video production). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `youtube-producer`
- **Starts when:** Video slot in the master marketing calendar
- **Done when:** Video published with full packaging, Shorts cut, promoted and reviewed at 7 and 28 days.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `youtube-producer` | Select the idea; research search demand and competing videos | Video brief |
| 2 | Work | `youtube-producer` | Write the outline, script and shot list | Script |
| 3 | QA review | `senior-agent-engineer`, `platform-devops-engineer`, `software-engineering-lead`, `lean-six-sigma-lead` | Subject-expert technical accuracy review (by topic) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | QA review | `quality-reviewer` | Script check: claims, privacy plan for screen recordings, brand | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | Erich does it | Erich (Chairman) | Review the script and record it with the shot list (Erich records only scripts he agrees with) | Raw footage |
| 6 | Work | `video-editor` | Edit, caption, blur sensitive areas, cut Shorts | Edited video + clips |
| 7 | Work | `graphic-designer` | Thumbnail variants | Thumbnails |
| 8 | Work | `youtube-producer` | Title, description, chapters, tags, UTM links, end screens | Upload package |
| 9 | QA review | `quality-reviewer` | Frame-by-frame privacy, captions, licensing, AI-content label (edit → step 6, thumbnail → step 7, package → step 8) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 10 | **Approval: Erich** | Erich (Chairman) | Approve publishing (the video uses Erich's likeness and voice) | Decision record (approved / changes requested / stopped) |
| 11 | Work | `youtube-producer`, `social-media-manager` | Publish or schedule; promote through `social-media-cycle` | Published video |
| 12 | Work | `marketing-analyst` | 7- and 28-day analytics; lessons to `youtube-producer` | Video report |

## Used by

`youtube-producer`, `video-editor`, `graphic-designer`.
