---
name: incident-response
description: "Respond to an incident (outage, security event, data exposure or an agent that did something wrong): triage severity, contain, communicate with the client, fix and recover, check legal notification duties (Florida Information Protection Act, HIPAA), and run a blameless review. Use the moment something breaks or looks unsafe."
---

# Incident response

*AI and platform delivery skill for the DIO expert team.* Handle an outage, security event or agent mistake: triage, contain, communicate, fix, recover, notify where required, and review blamelessly.

## When to use

A client system is down or degraded, an agent took a wrong or unsafe action, credentials may have leaked, or data may have been exposed.

## Method

1. **Triage (first 15 minutes):** what is affected, since when, how many people; severity SEV1 (data exposure, client unable to work), SEV2 (degraded), SEV3 (minor).
2. **Contain:** pause the agent, revoke or rotate credentials, block access, roll back the last change. Preserve logs and evidence; don't wipe anything.
3. **Communicate:** tell the client early and plainly what we know, what we're doing and when the next update is (SEV1 every hour). Bad news early.
4. **Fix and recover:** restore service from a known-good state; verify.
5. **Legal check:** if personal information of Floridians may be exposed, the Florida Information Protection Act requires notice to affected people within 30 days (and the Attorney General at 500 or more); HIPAA has its own rules for patient data. Bring in `business-attorney` and Erich at once.
6. **Blameless review** within five business days: timeline, root cause (5 whys), what made it worse or better, actions with owners. Process causes, never blame.
7. **Improve:** runbook updates, tests or monitors added, a kaizen card for anything systemic.

## Output

The incident log (timeline, actions, communications), the client summary, and the review with actions.

## Quality checks

- Containment came before root-cause hunting.
- Every notification duty was checked and recorded.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P08 Incident response). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `platform-devops-engineer`
- **Starts when:** Alert, client report or failed check affecting a DIO-run system
- **Done when:** Service restored and verified, client kept informed, review shared, actions tracked to done.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `platform-devops-engineer` | Triage and set severity. Tell Erich now for severity 1 or any possible exposure of personal or confidential data; otherwise in the daily summary | Incident record |
| 2 | Work | `client-success-manager` | Send the initial client notice from the approved template, within the SOW response target | Initial notice |
| 3 | Work | `platform-devops-engineer` | Contain and mitigate per the runbook. Rolling back to the last approved version is pre-approved | Mitigation log |
| 4 | Work | `security-compliance` | If security-related: preserve evidence and assess breach scope | Security assessment |
| 5 | Work | `business-attorney` | If personal data may be affected: draft the notification-obligation memo for counsel | Notification memo |
| 6 | **Approval: Erich** | Erich (Chairman) | Decide on any legal or breach notification (skip when no personal data is affected) | Decision record (approved / changes requested / stopped) |
| 7 | QA review | `qa-test-automation-engineer` | Verify recovery with functional checks | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | Work | `client-success-manager` | Send status updates and the resolution notice | Client updates |
| 9 | Work | `platform-devops-engineer` | Write the blameless post-incident review: timeline, root cause, actions | Post-incident review |
| 10 | QA review | `quality-reviewer` | Check evidence, root-cause depth and that every action has an owner and date | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | Work | `client-success-manager` | Share the post-incident review summary with the client | Shared summary |
| 12 | Work | `delivery-lead` | Track corrective actions to done; send systemic causes as kaizen cards to `continuous-improvement` | Action tracker |

## Used by

`platform-devops-engineer`, `client-success-manager`, `security-compliance`.
