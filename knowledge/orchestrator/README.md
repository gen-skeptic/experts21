# Knowledge folder: Picard (`orchestrator`)

Reference documents for DIO's Orchestrator (CEO agent). [`orchestrator`](../../.claude/agents/orchestrator.md) reads this folder before it answers or starts any task, and uses what is here ahead of general knowledge.

## What belongs here

- The Chairman's standing guidance and the current quarterly goals (`operating-cadence`)
- Notes on which brain worked for which kind of task
- Department heads' reviews and lessons from `operating-cadence`
- Approved examples and templates of this role's work: one combined answer to every team question: recommendation, who said what, disagreements and how to settle them, risks, next steps with owners, and open questions for Erich; weekly priorities and delegation decisions; task cards for every delegated step; monthly CEO letter and operating report for the Chairman; decision records for decisions under delegated authority; escalations to the Chairman with options and a recommendation
- Lessons that change how this role works

## What never goes here

- Client confidential data or client deliverables, credentials, secrets or personal data
- Confidential information from Erich's employer
- Copies of the research in `docs/` (link to it instead)

## Adding a document

On GitHub, open this folder and choose **Add file → Upload files** (or **Create new file** to paste text), then commit to `main`. Use Markdown or plain text where you can (the web app reads `.md`, `.txt`, `.csv`, `.json` and `.yaml`), keep each file under 1 MB, name it `YYYY-MM-short-topic.md`, and put the source, owner and review date in the first lines.

**This repository is public:** anything you add here can be read by anyone. Use sample or redacted documents.

*This README is generated from `tools/team.py`; the documents beside it are not, and the build never touches them.*
