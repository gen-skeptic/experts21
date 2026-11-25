# Knowledge folder: Soong (`agent-builder`)

Reference documents for DIO's Agent Builder (meta agent). [`agent-builder`](../../.claude/agents/agent-builder.md) reads this folder before it answers or starts any task, and uses what is here ahead of general knowledge.

## What belongs here

- Notes on agents that answered badly and what fixed them
- Patterns for good descriptions, tool lists and skills
- Links to the official Claude Code subagent and skill documentation
- Approved examples and templates of this role's work: new or improved agent definitions (in `tools/team.py`); new or improved skills (in `tools/skills.py`); change notes: what changed, why, and how it was tested
- Lessons that change how this role works

## What never goes here

- Client confidential data or client deliverables, credentials, secrets or personal data
- Confidential information from Erich's employer
- Copies of the research in `docs/` (link to it instead)

## Adding a document

On GitHub, open this folder and choose **Add file → Upload files** (or **Create new file** to paste text), then commit to `main`. Use Markdown or plain text where you can (the web app reads `.md`, `.txt`, `.csv`, `.json` and `.yaml`), keep each file under 1 MB, name it `YYYY-MM-short-topic.md`, and put the source, owner and review date in the first lines.

**This repository is public:** anything you add here can be read by anyone. Use sample or redacted documents.

*This README is generated from `tools/team.py`; the documents beside it are not, and the build never touches them.*
