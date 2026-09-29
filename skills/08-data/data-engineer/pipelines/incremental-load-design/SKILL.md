---
description: "Designs an incremental load for a table or stream: change detection method (log-based CDC, timestamp or sequence watermark, snapshot diff), watermark management, idempotent merge, delete propagation, late and out-of-order data handling, reconciliation and full-reload fallback. Use when full reloads become too slow or costly, a source must be replicated with low latency, or someone asks how to load only changed data safely."
related: "pipeline-spec, source-to-target-mapping, data-vault-model, schema-evolution-plan, pipeline-failure-analysis"
prompt: "Design an incremental load for a 400-million-row transactions table that currently takes 6 hours to reload fully."
---

# Design Incremental Loads

## Purpose
Load only what changed without losing, duplicating or misordering data, so pipelines meet freshness and cost targets and can be rerun safely after any failure.

## When to use
- Full reloads exceed the batch window, source load limits or cost budget.
- Consumers need lower latency than a full refresh allows.
- An existing incremental load drops or duplicates rows and must be redesigned.

## When not to use
- The whole pipeline (schedule, SLAs, operations) must be specified. Use `pipeline-spec`.
- A specific incremental load failed and needs diagnosis. Use `pipeline-failure-analysis`.
- The problem is a structural change of source or target schema. Use `schema-evolution-plan`.

## Inputs
Required:
- Source object with its key, how rows change (insert-only, updates, deletes) and the target with its intended history behavior (current state, full history, append log).

Optional:
- Volume and change rate, available change columns or change logs, source constraints, latency target, clock/timezone behavior of the source, existing load code.

If it is unknown whether the source updates or deletes rows, ask; the method depends on it.

## Process
1. Characterize the source change pattern: insert-only, updates in place, hard deletes, soft deletes, backdated corrections; and whether a reliable change indicator exists.
2. Choose the change detection method and justify it: log-based CDC (captures deletes and every change, needs log access), monotonic sequence/ID watermark (insert-only), last-modified timestamp watermark (requires trustworthy, indexed column maintained on every change), snapshot comparison/hash diff (no indicator available, higher cost).
3. Define the watermark: column, storage location, update only after the target commit succeeds, and the overlap window (look-back) that absorbs clock skew and long-running source transactions.
4. Define extraction: predicate (`> last watermark − overlap` and `<= run upper bound`), fixed upper bound per run to avoid moving targets, and source-side cost (index use, read replica).
5. Define the idempotent apply: merge/upsert on business key with deterministic ordering (latest change by sequence or commit position wins), or partition overwrite; duplicates from the overlap must be harmless.
6. Define delete propagation: CDC delete events, tombstones, soft-delete flag, or periodic key reconciliation when the source hard-deletes without logs.
7. Define late and out-of-order handling: event-time vs. processing-time, allowed lateness, how late records update aggregates or history (SCD effective dates), and when a partition is considered final.
8. Define history behavior in the target: overwrite current, SCD2 versions, or append change log with operation type.
9. Define reconciliation: periodic row count and checksum comparison against the source per partition or key range, and the trigger for a targeted re-sync.
10. Define the initial load and full-reload fallback: consistent snapshot plus change position hand-off without gaps, and when a full reload is forced (schema break, detected drift).
11. List failure scenarios and the expected behavior (crash after write before watermark update, source restore, clock change), plus assumptions. If the goal continues, suggest `pipeline-spec` for the full job or `schema-evolution-plan` for source changes.

## Output format
```markdown
# Incremental Load Design: <source> → <target>
Change pattern: <...> | Method: <CDC / sequence / timestamp / diff> — <rationale>

## Watermark
Column: <...> | Stored in: <...> | Overlap: <...> | Updated: after target commit

## Extraction
Predicate: <...> | Upper bound: <...> | Source impact: <...>

## Apply
Mode: <merge/overwrite partition/append> | Key: <...> | Ordering: <...> | Idempotency: <how>

## Deletes, Late Data and History
- Deletes: <...>
- Late/out-of-order: <allowed lateness, handling>
- History: <current/SCD2/change log>

## Reconciliation and Fallback
- Reconcile: <frequency, method> | Re-sync trigger: <...>
- Initial load / full reload: <...>

## Failure Scenarios
| Scenario | Expected behavior |
|---|---|

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The method fits the change pattern, including deletes and backdated updates.
- [ ] The watermark advances only after a successful commit; an overlap window exists.
- [ ] Rerunning any window is idempotent; ordering of multiple changes per key is deterministic.
- [ ] Late and out-of-order data has defined behavior.
- [ ] Reconciliation detects drift, and a gap-free initial/full reload path exists.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Trusting a last-modified column that some code paths (bulk updates, triggers, manual fixes) do not maintain.
- Using `>=` or `>` on the watermark without an upper bound or overlap: rows committed late by long transactions are lost forever.
- Forgetting deletes: timestamp watermarks never see hard-deleted rows, so the target silently diverges.

## Example
Input: "400 M-row transactions table, updates allowed, no deletes, full reload 6 h; last_updated column exists."

Excerpt of output:
- Method: timestamp watermark on last_updated `[ASSUMPTION: verify it is set by every write path, incl. batch corrections]`; fallback to CDC if not.
- Extraction: last_updated > watermark − 15 min AND <= run_start; overlap duplicates removed by merge on txn_id keeping max(last_updated).
- Reconciliation: weekly count + sum(amount) per month partition vs. source; mismatch triggers re-sync of that month only.
