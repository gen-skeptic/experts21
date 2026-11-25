---
name: workshop-design
description: "Design and deliver a workshop, course, webinar or coaching program (Line F, $1,500–$3,500 a session; coaching $1,200 a month): the learner persona, measurable objectives, a run of show with hands-on exercises, materials in the Dautel Design System, a feedback survey and improvements after each session. Use for client training, free community workshops and lead-generation events."
---

# Workshop design

*Products, training and team skill for the DIO expert team.* Design and run workshops, courses and coaching: learner personas, objectives, exercises, materials and feedback.

## When to use

Client training on new agents or processes, Lean fundamentals, Agent Workflow Coaching, and free workshops for local businesses, chambers and veterans.

## Method

1. **Learners:** who they are, what they already know, what they fear (job loss, mistakes), and what they need to do differently afterwards.
2. **Objectives:** three to five, each starting with a verb ("map their intake process", "review an agent's draft safely").
3. **Run of show:** 10-minute segments; at most 20 minutes of talking before an exercise; real examples from their industry.
4. **Exercises:** hands-on, with their own processes where possible (a SIPOC, a waste walk, reviewing agent output, writing a prompt with guardrails).
5. **Materials:** slides and handouts in the Dautel Design System; a one-page cheat sheet to keep.
6. **Safety and honesty:** what AI shouldn't be used for; privacy rules; no hype.
7. **Feedback:** a three-question survey at the end; what to change next time.
8. **Follow-up:** a recap email, the materials, and one clear next step (a fit call, a health check).

## Output

The run of show, slides, exercises, handout, survey, and the post-session notes.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P12 Workshop, training and coaching (Line F)). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `trainer-curriculum`
- **Starts when:** Booked private workshop, public event or coaching program (coaching: steps 1–5 once per program, steps 6–10 for each session)
- **Done when:** Session delivered, feedback analyzed, curriculum updated, attendees followed up.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `trainer-curriculum` | Set learning objectives and outline from the request | Outline |
| 2 | Work | `trainer-curriculum` | Build the slide outline, labs and facilitator guide | Curriculum draft |
| 3 | Work | `graphic-designer` | Design the slides with the Dautel Design System | Slides |
| 4 | QA review | `senior-agent-engineer`, `lean-six-sigma-lead` | Check technical accuracy by topic (AI and agents: agent engineer; Lean and process: Lean Six Sigma lead) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 5 | QA review | `quality-reviewer` | Final gate: correctness, evidence, security, privacy, brand voice and Dautel Design System compliance, completeness (content → step 2, slides → step 3) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | Work | `podcast-webinar-producer`, `operations-coordinator` | Logistics: registration and reminders for public events (registration pages go through `website-change`), scheduling for private sessions | Logistics ready |
| 7 | Erich does it | Erich (Chairman) | Deliver the session with the facilitator guide | Delivered session |
| 8 | Work | `marketing-analyst` | Analyze feedback and assessments | Feedback report |
| 9 | Work | `trainer-curriculum` | Update the curriculum from feedback; changed material repeats steps 4–5 before the next delivery | Updated curriculum |
| 10 | Work | `business-development` | Follow up with attendees → `proposal-and-sow` | Follow-up list |

## Used by

`trainer-curriculum`, `podcast-webinar-producer`, `lean-six-sigma-lead`.
