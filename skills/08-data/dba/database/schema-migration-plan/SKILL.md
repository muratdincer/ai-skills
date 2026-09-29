---
name: schema-migration-plan
description: "Plans a database schema migration on a live system with zero or minimal downtime: assesses lock and rewrite behavior of each DDL, splits breaking changes into expand-migrate-contract steps aligned with application releases, designs batched backfills, and defines verification, rollback and the point of no return. Use when adding, renaming, retyping or dropping columns, tables, constraints or indexes on production databases, or when a migration script needs a safety review before release."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: dba
  area: database
  title: "Plan a schema migration"
  related: "schema-evolution-plan, index-recommendation, backup-restore-plan, deployment-strategy, rollback-plan"
  prompt: "We need to split the customers.full_name column into first_name and last_name on a 90-million-row PostgreSQL table without downtime. Write the migration plan."
---

# Plan a Schema Migration

## Purpose
Change a production database schema without an outage, data loss or a blocked release. The plan orders DDL, backfill and application deploys so that old and new application versions both work at every step, and it says exactly how to go back.

## When to use
- A column, table, constraint, index or data type must change on a live, sizable table.
- A rename, split, merge or type change must happen while the application keeps serving traffic.
- A migration script is written and needs a lock/duration/rollback review before release.

## When not to use
- The change affects shared datasets or event streams consumed by other teams. Use `schema-evolution-plan`.
- Only the index set is being redesigned. Use `index-recommendation`, then this skill to deploy it.
- The new schema itself is being designed. Use `database-schema-design`.

## Inputs
Required:
- The database engine and version family, the current and target schema of the affected objects.
- Table sizes and traffic profile (rows, write rate, peak hours) of the affected tables.

Optional:
- Migration tooling in use, replication/failover setup, application release process, maintenance windows, backup status, lock timeout policies.

If the engine is unknown, ask; lock behavior of DDL differs fundamentally between engines and versions. Mark any engine behavior you are not sure of `[ASSUMPTION]`.

## Process
1. List each schema change and classify it: additive (new nullable column, new table), constraint/index, rewrite-causing (type change, some defaults, column reorder), or destructive (drop, rename, narrowing).
2. For each DDL, assess engine behavior: lock level and duration, full table rewrite or metadata-only, online option availability, replication lag impact, and whether it waits behind long-running transactions (lock queue pileup).
3. Break breaking changes into expand-migrate-contract: add new structure, dual write from the application (or trigger), backfill history, switch reads, stop writing the old structure, drop it in a later release.
4. Align steps with application releases: which app version is compatible with which schema state; every step must work with both the previous and the next app version.
5. Design the backfill: batched by key range, batch size and pause, throttling on replication lag and load, idempotent and resumable, off-peak scheduling, progress tracking.
6. Make constraints safe: add as not-validated/invalid first, then validate separately; create indexes with online/concurrent options; set lock timeouts and retry so DDL fails fast instead of blocking traffic.
7. Define verification for each step: row counts, null checks on new columns, old-vs-new value comparison on a sample and on aggregates, constraint validation, application error rates and latency.
8. Define rollback for each step and the point of no return (usually dropping old structures or irreversible data transformation); require a verified backup or restore point before it.
9. Write the runbook: order, owner, expected duration, go/no-go criteria, monitoring during execution (locks, replication lag, errors), communication.
10. List risks, assumptions and open questions. If the goal continues, suggest `backup-restore-plan` for the restore point, `deployment-strategy` or `rollback-plan` for the application side.

## Output format
```markdown
# Schema Migration Plan: <change>
Engine: <...> | Tables: <name – rows – write rate> | Downtime target: <zero / window>

## Change Classification
| Change | Type | Lock / rewrite | Online option | Risk |
|---|---|---|---|---|

## Steps
| # | Step | App version | Duration est. | Verification | Rollback |
|---|---|---|---|---|---|
Point of no return: step <n> – prerequisite: <verified backup/restore point>

## Backfill
Batching: <key range, size, pause> | Throttle: <lag/load threshold> | Resumable: <how>

## Safety Settings
Lock timeout: <...> | Statement timeout: <...> | Retry: <...>

## Monitoring and Go/No-Go
- Watch: <locks, replication lag, error rate, latency>
- Abort if: <...>

## Risks, Assumptions, Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every DDL has its lock level, rewrite behavior and duration risk stated for the named engine.
- [ ] Each step is compatible with both the previous and the next application version.
- [ ] The backfill is batched, throttled, idempotent and resumable.
- [ ] Every step has verification and rollback, and the point of no return has a verified restore point.
- [ ] Lock timeouts prevent DDL from queueing behind long transactions and blocking traffic.
- [ ] Engine behaviors not confirmed are labeled `[ASSUMPTION]`; durations are not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Renaming or dropping a column in the same release that stops using it; running instances of the old version fail immediately.
- A "fast" DDL waiting behind a long transaction while every new query queues behind it; always set a lock timeout.
- Backfilling in one transaction: huge undo/log volume, replication lag and a rollback that takes as long as the update.

## Example
Input: "Split customers.full_name into first_name, last_name; PostgreSQL, 90M rows, 800 writes/s."

Excerpt of output:
- Step 1: add nullable `first_name`, `last_name` (metadata-only) with `lock_timeout = 3s` and retry.
- Step 2: app v2 writes both old and new columns; reads still from `full_name`.
- Step 3: backfill in 10k-row key batches, pause when replica lag > 5 s; split rule for single-word names `[TBD: business decision]`.
- Step 4: app v3 reads new columns; Step 5 (point of no return, after verified snapshot): drop `full_name` in a later release.
