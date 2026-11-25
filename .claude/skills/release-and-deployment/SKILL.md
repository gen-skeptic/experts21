---
name: release-and-deployment
description: "Release software or an agent to a client: assemble the release handoff package, deploy to staging, run client acceptance testing, get Erich's production approval, promote through GitOps, verify, and keep rollback ready. Builders build; DevOps deploys. Use for every release to a client's production."
---

# Release and deployment

*AI and platform delivery skill for the DIO expert team.* Ship a release safely: handoff package, staging, client acceptance, Erich's approval, GitOps promotion, verification and rollback.

## When to use

Every release to a client's production: software, agents, integrations, platform changes.

## Release handoff package (from the builders)

1. Source merged through a reviewed pull request, CI green (build, tests, lint, type checks, dependency and secret scans).
2. A build artifact or container image with an immutable digest, plus an SBOM and vulnerability scan.
3. Deployment spec, resource limits, and ports.
4. Configuration contract: every environment variable and secret **by name only**, never values.
5. Health checks, structured logs and the metrics to alert on.
6. Backward-compatible migrations with a tested rollback or restore.
7. Release notes, a runbook draft, and test results (agent releases: evaluation results).

## Method

1. `platform-devops-engineer` checks the package; anything missing goes back to the builders.
2. **Deploy to staging** through GitOps; smoke test.
3. **Client acceptance testing** on staging against the SOW's acceptance criteria; the client signs off.
4. **Erich approves** the production deployment (a final deployment to a customer is always his decision).
5. **Promote** through GitOps in the agreed window; progressive rollout where available.
6. **Verify:** health checks, key journeys, metrics and logs for the first hour.
7. **Rollback** at once if verification fails; then a blameless review.
8. **Close:** release recorded, runbook updated, client told.

## Quality checks

- Developers never deploy to production; DevOps owns environments and rollback.
- No secret values anywhere in the package.

## Team workflow

How the team runs this end to end, from the DIO operating manual (gen-skeptic/experts, P10 Release and deployment to customers). Records it names (assignments, decision records, the CRM) live in the firm's private system of record; in this repository, put them in your answer.

- **Owner:** `platform-devops-engineer`
- **Starts when:** A signed release handoff package from `software-build-standards`, `governed-agent-design` or `managed-operations`, or a retainer change outside the standing approval (`managed-operations`)
- **Done when:** Release accepted by the client on staging, approved by Erich, live and verified in production (or submitted to the app store), release notes published.

| # | Step | Who | What | Output |
| -: | --- | --- | --- | --- |
| 1 | QA review | `platform-devops-engineer` | Check the handoff package is complete; return incomplete packages to whoever assembled it | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 2 | Work | `platform-devops-engineer` | Open the GitOps pull request (image digest + config); CI policy checks | GitOps PR |
| 3 | QA review | `security-compliance` | Review production config, secrets references and network policy | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 4 | Work | `platform-devops-engineer` | Deploy to staging | Staging release |
| 5 | QA review | `qa-test-automation-engineer` | Smoke and regression tests on staging (code defects → `software-build-standards` step 10 or `governed-agent-design` step 7, config defects → step 2) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 6 | QA review | `business-analyst`, `ai-solutions-engineer` | Client acceptance testing on staging, with the client (software: business analyst; agent workflows: AI solutions engineer) | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 7 | QA review | `quality-reviewer` | Release readiness: staging and acceptance results, release notes, rollback plan, change record | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 8 | **Approval: Erich** | Erich (Chairman) | Approve production promotion (final deployment to the customer) | Decision record (approved / changes requested / stopped) |
| 9 | Work | `platform-devops-engineer` | Promote to production (rolling or blue/green) or submit the signed app-store build; verify health | Production release |
| 10 | QA review | `qa-test-automation-engineer` | Production smoke test; on failure DevOps rolls back first, then the defect returns to the builders | QA record: PASS / PASS WITH NOTES / FAIL with itemized fixes |
| 11 | Work | `technical-writer`, `client-success-manager` | Publish the release notes and notify the client | Release notes + notice |

## Used by

`senior-agent-engineer`, `platform-devops-engineer`, `delivery-lead`, `software-engineering-lead`, `technical-writer`.
