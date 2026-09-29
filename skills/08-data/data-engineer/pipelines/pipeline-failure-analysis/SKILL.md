---
description: "Analyzes a failed or silently wrong data pipeline run: reconstructs the timeline, isolates the root cause (source, code, infrastructure, data, dependency), quantifies the data impact on partitions, tables and consumers, and produces a safe, idempotent backfill and prevention plan. Use when a load failed, produced duplicates, missing or late data, a quality check tripped, or a consumer reports numbers that stopped matching."
related: "incremental-load-design, pipeline-spec, data-lineage-doc, data-quality-rules, postmortem"
prompt: "Last night's orders load succeeded but today's revenue dashboard is 12% low. Here are the run logs and row counts; find out what happened and how to fix the data."
---

# Analyze a Data Pipeline Failure

## Purpose
Find the real root cause of a data pipeline failure, state exactly which data is wrong or missing and who consumed it, and repair it with a backfill that cannot make things worse. A data incident is closed only when the data is correct again, not when the job turns green.

## When to use
- A pipeline run failed, hung, or was retried and the state of the target is unclear.
- A run "succeeded" but produced duplicates, missing rows, stale data or wrong values.
- A data quality check or reconciliation tripped, or a consumer reports a number shift.

## When not to use
- The CI/CD build or deployment pipeline failed, not a data pipeline. Use `pipeline-failure-triage`.
- The load logic itself must be redesigned (watermarks, CDC, merge). Use `incremental-load-design`.
- A formal incident review with timeline and actions for a wide audience is needed after analysis. Use `postmortem`.

## Inputs
Required:
- The symptom (error message, failed check, or observed wrong number) and the affected pipeline/table.
- Run evidence: at least logs or run history for the failing run and one last known good run.

Optional:
- Row counts/checksums per partition, recent code/config/schema changes, source system notices, lineage to downstream consumers, the pipeline spec.

If there is no run evidence at all, ask for it; do not guess a root cause from the symptom alone.

## Process
1. State the symptom precisely: what is wrong (fails, duplicates, missing, late, wrong values), in which table/partitions, first detected when and by whom. Separate observed facts from reports and label inferences `[ASSUMPTION]`.
2. Read the full error and the run timeline: start/end, retries, step durations, rows read/written per step, compared with the last good run. Note the exact first point where the numbers diverge.
3. List what changed since the last good run: code, configuration, dependency versions, source schema or volume, credentials, infrastructure, upstream schedule, calendar effects (month end, DST, holiday).
4. Form hypotheses across the failure classes: source (outage, late delivery, schema drift, backdated changes, hard deletes), logic (join fan-out, filter, timezone, null handling), load mechanics (watermark advanced without commit, non-idempotent retry, partial overwrite), infrastructure (timeouts, OOM, permissions), dependency (upstream job ran late or on partial data).
5. Test hypotheses one variable at a time with concrete queries (counts by partition and key, duplicate key checks, min/max timestamps, source vs target diffs). Rule each hypothesis in or out with evidence. No fix is proposed before the root cause is confirmed; if three fixes fail, question the design.
6. Quantify the data impact: affected tables, partitions/time range, row counts, key metrics shifted, and downstream consumers via lineage (reports, models, exports, reverse ETL) that already read the bad data.
7. Design the repair: stop or pause the pipeline if it keeps corrupting data, then an idempotent backfill (partition overwrite or keyed merge) with explicit range, order, dependencies to re-run downstream, source load limits and a dry run on one partition.
8. Define verification: reconciliation queries and thresholds that must pass after backfill (counts, sums, duplicate keys, freshness), and who signs off with consumers.
9. Define prevention: the missing test, quality rule, alert or design change that would have caught or prevented it, each with an owner.
10. Draft consumer communication: what was wrong, time range, whether decisions or external outputs used the bad data, when it is corrected. Mask any personal data shown in samples.
11. Fill the output template. If the goal continues, suggest `postmortem` for the formal review, `data-quality-rules` for the new checks or `incremental-load-design` if the load mechanism was the cause.

## Output format
```markdown
# Pipeline Failure Analysis: <pipeline> – <date>
Status: <investigating / root cause confirmed / repaired> | Severity: <...>

## Symptom
<what, where, since when, detected by>

## Timeline
| Time | Event | Evidence |
|---|---|---|

## Hypotheses
| # | Hypothesis | Test | Result (confirmed / ruled out / open) |
|---|---|---|---|

## Root Cause
<cause> – <evidence> | Contributing factors: ...

## Data Impact
| Table | Partitions / range | Rows affected | Consumers exposed |
|---|---|---|---|

## Repair and Backfill
1. <step, range, mode, dry run>
Verification: <query, threshold>

## Prevention
| Action | Type (test/rule/alert/design) | Owner |
|---|---|---|

## Consumer Communication
<short message>

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The root cause is backed by evidence, not only by timing coincidence.
- [ ] Impact lists exact tables, ranges and exposed downstream consumers.
- [ ] The backfill is idempotent, scoped, ordered with downstream re-runs and has a dry run.
- [ ] Verification queries and pass thresholds are defined.
- [ ] At least one prevention action would have caught this failure earlier.
- [ ] Inferences are labeled and nothing (counts, dates, owners) is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Re-running the job and calling it fixed: a non-idempotent retry doubles rows, and a green run hides the rows lost in the failed one.
- Stopping at the proximate cause ("timeout") instead of why it happened now (volume doubled, missing index, upstream late).
- Backfilling the table but not the downstream aggregates, extracts and caches that already consumed the bad data.

## Example
Input: "Orders load succeeded at 02:10, revenue dashboard 12% low today. Rows written 1.08M vs usual 1.23M."

Excerpt of output:
- Hypothesis 2 (confirmed): source replica lagged 40 min; extraction upper bound was `now()`, so late-committed orders fell before the next watermark `[ASSUMPTION: verify replica lag metric at 01:30]`.
- Impact: `fact_orders` partition 2026-03-14, ~150k rows missing; `agg_daily_revenue` and the finance export consumed it.
- Repair: overwrite partition 2026-03-14 from source, then re-run `agg_daily_revenue` for that day; verify count and sum(amount) within 0.1% of source.
- Prevention: fixed upper bound = source commit position at run start; freshness check on replica lag before extraction.
