---
name: client-onboarding
description: "Onboard a new client after the SOW is signed: confirm the deposit, set up least-privilege access in the client's own accounts, hold the kickoff, agree the communication rhythm and success measures, and record the baseline. Use at the start of every engagement."
---

# Client onboarding

*Sales and clients skill for the DIO expert team.* Start an engagement cleanly: signed SOW, deposit, access by least privilege, kickoff, communication plan and success measures.

## When to use

Right after a client signs. Also when a client adds a new engagement.

## Method

1. **Paperwork:** signed SOW and MSA, deposit received, insurance certificate sent if asked, BAA signed if any patient data is involved (otherwise no patient data).
2. **Access, least privilege:** accounts are created by the client in their own systems, one per person or agent, with MFA; DIO never asks for shared passwords; record every grant in an access matrix (who, what, why, until when).
3. **Kickoff (prepared welcome):** goals in the client's words, the success measures and their baseline, the people involved, the schedule, what we need from them and by when.
4. **Communication plan:** one weekly written update plus a short recorded demo; one standing 30-minute call; support hours and response targets from the SOW; who to call for what.
5. **Data handling:** what data we will touch, where it lives (client systems only), and how access ends at handover.
6. **Baseline:** measure the current process (time, volume, errors) before anything changes, so results can be proven later.

## Output

An onboarding checklist with every item ticked or explained, the access matrix, the kickoff notes with success measures and baseline, and the dated first milestone.

## Quality checks

- No client confidential data in DIO's own systems.
- Every access grant has an owner and an end date.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P03 Client onboarding). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `client-success-manager`
- **Starts when:** Signed SOW
- **Done when:** Deposit invoiced, kickoff held, access granted with least privilege, delivery process started.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | Work | `operations-coordinator` | Create the engagement project from the won CRM deal (its ID is the engagement ID) and open the onboarding checklist: signed SOW, deposit status, kickoff date, shared folder | Onboarding checklist |
| 2 | Work | `cpa-bookkeeper` | Create the client record and prepare the deposit invoice | Deposit invoice draft |
| 3 | **Approval: Erich** | Erich (Chairman) | Approve and send the deposit invoice | Decision record (approved / changes requested / stopped) |
| 4 | Work | `delivery-lead` | Build the project plan, risk log and acceptance criteria from the SOW | Project plan |
| 5 | Work | `security-compliance` | Prepare the least-privilege access request, the credential handover method (client-issued accounts, shared through a password manager, MFA on) and data-handling requirements | Access request |
| 6 | Work | `client-success-manager` | Prepare the kickoff agenda, success metrics, communication cadence, and the support hours and response targets from the SOW | Kickoff pack |
| 7 | QA review | `quality-reviewer` | Check the onboarding pack is complete and consistent with the SOW (checklist → step 1, plan → step 4, access request → step 5, kickoff pack → step 6) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | Work | `client-success-manager` | Run the kickoff, confirm access and deposit received, and hand to the delivery process (`readiness-assessment`/`governed-agent-design`/`private-ai-platform`/`software-build-standards`/`agent-safety-audit`/`workshop-design`/`process-health-check`/`dmaic-project`/`kaizen-event`) | Kickoff record |

## Used by

`operations-coordinator`, `client-success-manager`, `delivery-lead`.
