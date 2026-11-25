---
name: runbook
description: "Write an operational runbook for a system or agent: what it does, how to start, stop and pause it, how to check health, common failures and fixes, rollback and restore steps, access and secrets (by name only), and who to contact. Use for every system the firm hands over."
---

# Runbook

*Software delivery skill for the DIO expert team.* Write a runbook a client's own staff can follow: start, stop, check health, common failures, rollback, restore and contacts.

## When to use

Every system, agent or integration the firm builds or operates, before handover; update it after every incident or change.

## Structure

1. **Purpose:** what the system does and for whom, in two sentences.
2. **Architecture at a glance:** a small diagram and where each part runs.
3. **Access:** who can do what; secrets listed **by name only** with where they are stored.
4. **Daily operation:** how to check it's healthy (dashboard, health URL, key log lines).
5. **Start, stop and pause:** exact commands or clicks; for agents, how to pause all actions immediately.
6. **Common failures:** symptom, likely cause, fix, and when to escalate.
7. **Rollback:** how to return to the last good version.
8. **Backup and restore:** where backups are, how to restore, when it was last tested.
9. **Contacts and support:** support hours and response targets from the SOW.

## Rules

- Write for the client's own staff, not for us. Numbered steps, one action each, exact commands.
- Test the runbook: someone who didn't build the system follows it.

## Used by

`senior-agent-engineer`, `platform-devops-engineer`, `technical-writer`.
