# Knowledge folder: Data (`senior-agent-engineer`)

Reference documents for DIO's Senior AI Agent Engineer. [`senior-agent-engineer`](../../.claude/agents/senior-agent-engineer.md) reads this folder before it answers or starts any task, and uses what is here ahead of general knowledge.

## What belongs here

- Agent architecture patterns and reference implementations (Cassian, OpenBrain integrations)
- MCP server and tool design conventions
- Agent safety checklists and lessons from past incidents
- Approved examples and templates of this role's work: architecture and access design; working code in the client's repository; test and evaluation results; release handoff packages; runbook and handover notes
- Lessons that change how this role works

## What never goes here

- Client confidential data or client deliverables, credentials, secrets or personal data
- Confidential information from Erich's employer
- Copies of the research in `docs/` (link to it instead)

## Adding a document

On GitHub, open this folder and choose **Add file → Upload files** (or **Create new file** to paste text), then commit to `main`. Use Markdown or plain text where you can (the web app reads `.md`, `.txt`, `.csv`, `.json` and `.yaml`), keep each file under 1 MB, name it `YYYY-MM-short-topic.md`, and put the source, owner and review date in the first lines.

**This repository is public:** anything you add here can be read by anyone. Use sample or redacted documents.

*This README is generated from `tools/team.py`; the documents beside it are not, and the build never touches them.*
