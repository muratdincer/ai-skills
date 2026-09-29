---
name: index-recommendation
description: "Recommends indexes for a table or database from its real workload: groups queries by access pattern, designs key column order, included columns, filtered/partial indexes, consolidates overlapping and removes unused indexes, and weighs read gains against write amplification, storage and maintenance cost. Use when designing indexes for a new schema or feature, reviewing an over-indexed or under-indexed table, or acting on missing-index suggestions from the engine."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: dba
  area: database
  title: "Recommend indexes"
  related: "query-optimization, database-health-check, schema-migration-plan, database-schema-design, capacity-planning"
  prompt: "Our orders table has 14 indexes, inserts are getting slow and some reports are still scanning. Here are the top 20 queries and index usage stats; recommend an index set."
---

# Recommend Indexes

## Purpose
Produce a deliberate index set for a workload: every index justified by queries it serves, overlaps consolidated, dead indexes removed, and the write-side cost stated. The result is fewer, better indexes rather than one per complaint.

## When to use
- A new table, schema or feature needs its initial indexes from known access patterns.
- A table has many indexes, slow writes or large storage, and reads still scan.
- The engine's missing-index suggestions or an advisor report must be evaluated before applying.

## When not to use
- One specific query is slow and its plan is available. Use `query-optimization`.
- The table structure itself (keys, normalization, partitioning) is being designed. Use `database-schema-design`.
- Deploying the chosen index changes safely on a large live table. Use `schema-migration-plan`.

## Inputs
Required:
- The database engine and the table definitions with existing indexes.
- The workload: top queries by total cost or frequency (text or described predicates, joins, sorts) and the DML pattern (insert/update/delete rates).

Optional:
- Index usage statistics (seeks, scans, lookups, updates), table sizes and growth, missing-index suggestions, latency targets, maintenance windows, replication setup.

If the workload is unknown, ask for the top queries; do not design indexes from the schema alone except as `[ASSUMPTION]`-marked starting points.

## Process
1. Profile the workload: list queries with frequency, cost and latency target; mark the table as read-heavy, write-heavy or mixed. Label inferred patterns `[ASSUMPTION]`.
2. Extract per query the access pattern: equality predicates, range predicates, join columns, `ORDER BY`/`GROUP BY`, selected columns and selectivity of each predicate.
3. Group queries that share leading equality columns; design one index per group rather than per query.
4. Order key columns: equality columns first (most selective or most shared first), then the range or sort column; add columns needed only for output as included/non-key columns when the engine supports it, to avoid lookups on hot paths.
5. Consider specialized forms where justified: filtered/partial indexes for hot subsets (e.g. open orders), unique indexes that also enforce business keys, composite indexes that support foreign key checks and cascades, and engine-specific types (full-text, spatial, inverted, columnar) for analytics or search patterns.
6. Review existing indexes: flag unused (no reads since a representative period, including month-end jobs), duplicate, and left-prefix redundant indexes; propose merges.
7. Estimate the write-side cost of the final set: extra writes per insert/update, lock and log volume, page splits for non-sequential keys, storage size, and maintenance/rebuild time.
8. Evaluate engine suggestions critically: merge them into the grouped design instead of applying them one by one; reject those serving rare queries on write-heavy tables.
9. Define the rollout: create before drop, online creation where supported, disable or make invisible before dropping when possible, and monitoring of target queries and write latency.
10. Fill the output template. If the goal continues, suggest `schema-migration-plan` to deploy the changes, `query-optimization` for queries still slow afterwards or `capacity-planning` if storage growth is significant.

## Output format
```markdown
# Index Recommendation: <table/schema>
Engine: <...> | Workload profile: <read-heavy/write-heavy/mixed> | Period of stats: <...>

## Workload Summary
| Query / pattern | Frequency | Predicates (eq / range) | Sort / group | Current access |
|---|---|---|---|---|

## Proposed Index Set
| Action (create/alter/drop/keep) | Index | Key columns | Included | Filter | Serves queries | Write/storage cost |
|---|---|---|---|---|---|---|

## Removed or Merged Indexes
- <index> – <reason: unused since / duplicate of / prefix of>

## Rollout and Monitoring
1. <step> – online? – verification
Monitor: <target queries, write latency, index usage after N days>

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every proposed index lists the queries it serves; no index serves nothing.
- [ ] Column order follows equality, then range/sort, and matches the grouped patterns.
- [ ] Overlapping, duplicate and unused indexes are addressed, with usage period checked against periodic jobs.
- [ ] Write amplification and storage cost are stated for the final set.
- [ ] Rollout creates before it drops and names monitoring after the change.
- [ ] Assumed workload patterns are labeled; no usage numbers are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Applying missing-index suggestions one by one; they overlap heavily and ignore write cost.
- Dropping an "unused" index whose usage statistics were reset by a restart or that serves a quarterly job.
- Indexing low-selectivity columns alone (status, flags) instead of combining them with a selective column or using a filtered index.

## Example
Input: "orders: 14 indexes, 3k inserts/s, 40 updates/s on status; reports filter by customer_id + created_at range, ops screen shows open orders by warehouse."

Excerpt of output:
- Create `(customer_id, created_at) INCLUDE (status, total)` serving 6 report queries; replaces `ix_customer` and `ix_customer_date` (left-prefix duplicates).
- Create filtered `(warehouse_id, created_at) WHERE status = 'OPEN'` serving the ops screen; small because open orders are ~2% `[ASSUMPTION: confirm ratio]`.
- Drop 4 indexes with zero reads over 35 days including month end; net result 9 indexes, fewer writes per insert.
