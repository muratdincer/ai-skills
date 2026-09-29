---
name: deployment-checklist
description: "Builds a deployment checklist with pre-deployment, execution and post-deployment checks, each with an owner, expected result and a stop condition, tailored to the system's components, data changes and deployment mechanism. Use when a production deployment is scheduled, when deployments keep failing on forgotten steps, or when someone asks for a cut-over or deployment-day checklist."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Build a deployment checklist"
  related: "release-plan, rollback-plan, go-no-go, runbook, deployment-strategy"
  prompt: "Create a deployment checklist for tonight's release: two API services on Kubernetes, one SQL migration, a config change in the gateway."
---

# Build a Deployment Checklist

## Purpose
Turn a deployment into a sequence of verifiable checks with owners and explicit stop points, so nothing is forgotten under time pressure and a failing deployment is stopped before it harms users or data.

## When to use
- A production (or other shared-environment) deployment is scheduled and needs a step list.
- Past deployments failed because of forgotten steps, config drift or unverified results.
- A manual or semi-automated cut-over involves several people.

## When not to use
- The overall schedule, contents and communication of a release are needed. Use `release-plan`.
- The detailed procedure to undo the deployment is needed. Use `rollback-plan`.
- A repeatable operational procedure for an alert is needed. Use `runbook`.

## Inputs
Required:
- What is being deployed: components, artifacts or versions, and target environment.
- Deployment mechanism (pipeline, manual steps, scripts) at least at a high level.

Optional, improves quality:
- Database or data migrations, configuration and secret changes, infrastructure changes.
- Monitoring dashboards and key metrics, smoke tests available.
- Organization change-management rules, maintenance window, team members.

If the components or the target environment are unknown, ask. Unknown owners become `[TBD]`; unknown commands are described as intent, not invented.

## Process
1. List everything that changes: artifacts and versions, configuration, secrets, schema/data, infrastructure, external dependencies, feature flags.
2. Pre-deployment checks: approved change record, correct artifact (version, digest or checksum) promoted from staging, backup or snapshot taken and restorable, capacity and quota headroom, dependent teams informed, on-call aware, rollback plan reviewed.
3. Readiness of the environment: current health baseline captured (error rate, latency, saturation), no active incident, no conflicting change in progress.
4. Execution steps in dependency order, each with owner, expected result, and verification (how you know it worked).
5. Insert stop conditions after risky steps: explicit "if X, stop and invoke rollback" with the threshold or `[TBD]`.
6. Mark the point of no return and require an explicit go decision before it.
7. Post-deployment verification: smoke tests, key user journeys, metrics compared to the baseline, logs for new error classes, background jobs and queues draining, data migration row counts or checks.
8. Closure: enable flags if planned, update change record and status channels, confirm monitoring window and hypercare owner, record deviations for the retrospective.
9. Keep each item a verifiable yes/no statement; move explanations to notes.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `rollback-plan` for the undo procedure, `go-no-go` for the decision gate, or `runbook` to turn recurring steps into a reusable procedure.

## Output format
```markdown
# Deployment Checklist: <release/system> – <environment> – <date>
Deployment lead: <name or [TBD]> · Rollback plan: <link or [TBD]>

## Pre-Deployment
| # | Check | Owner | Expected result | Done |
|---|---|---|---|---|

## Execution
| # | Step | Owner | Verification | Stop if | Done |
|---|---|---|---|---|---|
| ⚠ | POINT OF NO RETURN – go decision required | | | | |

## Post-Deployment Verification
| # | Check | Owner | Compared to baseline | Done |

## Closure
- [ ] Change record updated
- [ ] Stakeholders notified of outcome
- [ ] Hypercare owner and duration confirmed

## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every step has an owner and a verifiable expected result.
- [ ] A baseline is captured before deployment so post-checks compare against it.
- [ ] Risky steps are followed by explicit stop conditions linked to rollback.
- [ ] Data changes have backup and a verification check (counts, integrity), not only "migration ran".
- [ ] Background jobs, queues and caches are covered, not only HTTP endpoints.
- [ ] No commands, thresholds or names were invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Check the logs" as a step. State what to look for and what counts as a failure.
- Backups taken but never tested for restore. Include a restore verification or state the last tested restore.
- Declaring success at the end of the deployment. Keep the monitoring window and name its owner.

## Example
Input: "Two APIs on Kubernetes, one additive SQL migration, gateway route change, tonight 23:00."

Excerpt of output:
| # | Step | Owner | Verification | Stop if |
|---|---|---|---|---|
| E1 | Run additive migration | DBA `[TBD]` | New columns exist; row count unchanged | Migration exceeds `[TBD]` min or locks table |
| E2 | Roll out API A | Team A | All pods ready; 5xx rate at baseline | 5xx rate > baseline + `[TBD]` for 5 min |
| E4 | Switch gateway route | Platform | Synthetic check on new route passes | Any 404/502 on new route |
