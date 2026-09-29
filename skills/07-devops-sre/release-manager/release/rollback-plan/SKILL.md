---
name: rollback-plan
description: "Writes a rollback plan for a release or change with measurable triggers, decision owner and deadline, component-by-component steps, data and schema considerations, roll-forward alternatives and post-rollback verification. Use before a production change is approved, when a change includes migrations or irreversible steps, or when someone asks how a release would be undone."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Write a rollback plan"
  related: "deployment-checklist, release-plan, deployment-strategy, schema-migration-plan, backup-restore-plan"
  prompt: "Write a rollback plan for our release that upgrades the order service and migrates the order status column from text to an enum table."
---

# Write a Rollback Plan

## Purpose
Decide in advance when and how a change is reversed, including what happens to data written in the meantime, so a failing release is undone quickly by people who are tired and under pressure.

## When to use
- A production change needs approval and must show a tested way back.
- The change includes a schema or data migration, configuration or infrastructure changes, or external contract changes.
- A previous rollback failed, took too long or corrupted data.

## When not to use
- Choosing the rollout mechanism itself (canary, blue-green). Use `deployment-strategy`.
- Designing the migration steps in detail. Use `schema-migration-plan`.
- Restoring after a disaster rather than reversing a release. Use `dr-plan` or `backup-restore-plan`.

## Inputs
Required:
- The change: components, versions, configuration, and any data or schema changes.
- How it is deployed (pipeline, manual, infrastructure as code).

Optional, improves quality:
- SLOs and key metrics, deployment strategy, feature flag capability.
- Backup and restore capability and last tested restore.
- Dependencies on other teams, external systems or client apps.

If data or schema changes are unknown, ask; they decide whether rollback is even possible. Other gaps become open questions.

## Process
1. Classify each change by reversibility: stateless and reversible (binary, config), reversible with care (additive schema, flags), irreversible or lossy (destructive migration, external side effects such as sent emails or payments, data format rewrites).
2. Define triggers as measurable conditions tied to SLOs or business metrics (error rate, latency, failed transactions, data integrity check) with observation windows; add a catch-all "release owner judgment".
3. Name the decision owner, the people who must be consulted, and a decision deadline, especially before any point of no return.
4. Choose the mechanism per component: traffic switch, redeploy previous artifact, flag off, config revert, infrastructure revert, or roll forward with a fix.
5. Handle data explicitly: what happens to rows written by the new version; is the old version able to read them; is a reverse migration or compensating script needed; is a restore required and what data loss (RPO) it implies.
6. Order the rollback steps in reverse dependency order and give each an owner, expected duration `[TBD]` if unknown, and verification.
7. Cover side channels: caches, queues with messages in the new format, scheduled jobs, search indexes, client apps already updated, partner integrations.
8. Define post-rollback verification and communication (internal, support, customers, status page).
9. State when roll forward is preferable (e.g. after an irreversible migration) and what that requires.
10. Require evidence the rollback was rehearsed or state that it was not, as a risk.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `deployment-checklist` to embed the stop conditions, `schema-migration-plan` to make the migration reversible, or `go-no-go` for the approval decision.

## Output format
```markdown
# Rollback Plan: <change/release>
Decision owner: <name or [TBD]> · Decision deadline: <time or step> · Rehearsed: yes/no

## Reversibility
| Component | Change | Class (reversible / with care / irreversible) | Notes |

## Triggers
| Signal | Threshold | Window | Source |
- Plus: release owner judgment.

## Rollback Steps
| # | Step | Owner | Est. duration | Verification |

## Data Considerations
- Data written by new version: ...
- Reverse migration / compensation: ...
- Restore needed: yes/no – expected data loss: ...

## Side Channels
- Queues, caches, jobs, clients, partners: ...

## Roll-Forward Option
## Verification and Communication
## Risks, Assumptions and Open Questions
```

## Quality checklist
- [ ] Every trigger is measurable with a threshold and window, or marked `[TBD]`.
- [ ] Data written after the deployment is explicitly addressed.
- [ ] Irreversible steps are identified and a decision deadline precedes them.
- [ ] Steps are in reverse dependency order, each with owner and verification.
- [ ] Rehearsal status is stated; an unrehearsed rollback is listed as a risk.
- [ ] No durations, thresholds or names were invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Redeploy the previous version" as the whole plan. The previous binary may not read the new data or schema.
- Triggers like "if things go wrong". Tie each trigger to a metric and a window so the decision is fast.
- Forgetting messages already in queues in the new format. Drain, convert or make old consumers tolerant.

## Example
Input: "Order service v5 plus migration changing order_status from text to a status table."

Excerpt of output:
- Reversibility: migration is irreversible if the text column is dropped in the same release → split: keep text column and dual-write in v5, drop in a later release `[ASSUMPTION: team accepts two-phase]`.
- Trigger: failed order creation rate above `[TBD]` % for 10 min, or any integrity check mismatch between text and status table.
- Data: orders created on v5 are written to both columns, so v4 can read them after rollback.
