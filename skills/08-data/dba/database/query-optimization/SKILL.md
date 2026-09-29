---
name: query-optimization
description: "Diagnoses a slow SQL query from its text, execution plan and statistics, finds the dominant cost (bad cardinality estimate, wrong join order or method, scans, spills, non-sargable predicates, parameter sensitivity, blocking) and proposes ranked rewrites, index or statistics changes with expected effect and verification. Use when a query, report or endpoint is slow, a plan regressed after a release or data growth, or someone shares an execution plan and asks why it is slow."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: dba
  area: database
  title: "Optimize a slow query"
  related: "index-recommendation, database-health-check, sql-query-writing, performance-optimization, schema-migration-plan"
  prompt: "This order search query went from 200 ms to 9 seconds after last week's data import. Here are the query and the actual execution plan; why is it slow and how do we fix it?"
---

# Optimize a Slow Query

## Purpose
Make a specific query fast and predictably fast by fixing the actual cause shown in its execution plan, not by guessing indexes. Each recommendation carries its expected effect, its cost for the rest of the workload, and how to prove it worked.

## When to use
- A known query, report or API call is slower than its target.
- A plan regressed after a deployment, statistics refresh, parameter change or data growth.
- An execution plan is available and the question is "why is this slow?".

## When not to use
- The whole database or server is slow and the culprit query is unknown. Use `database-health-check`.
- Indexes should be designed for a whole workload, not one query. Use `index-recommendation`.
- The query does not exist yet and must be written. Use `sql-query-writing`.

## Inputs
Required:
- The query text (with representative parameter values) and the database engine.
- An actual execution plan (with runtime row counts) or, failing that, the estimated plan plus timing.

Optional:
- Table sizes, existing indexes, statistics age, wait/IO/CPU metrics for the run, target latency, call frequency, recent changes.

If only an estimated plan is available, say which conclusions need the actual plan. Do not invent row counts.

## Process
1. Establish the baseline: engine, current duration, target duration, call frequency, whether it is always slow or only for some parameter values. Label anything inferred `[ASSUMPTION]`.
2. Read the plan from the most expensive operators, not top to bottom: highest actual time, rows or IO; spills to temp; sorts and hashes over large inputs; nested loops with large outer inputs; key/row lookups repeated many times.
3. Compare estimated vs actual rows at each operator. An order-of-magnitude gap is usually the root cause; trace it to stale or missing statistics, correlated predicates, skew, functions on columns, implicit conversions, table variables or parameter sniffing.
4. Check predicates for sargability: functions or casts on indexed columns, leading wildcards, OR across columns, mismatched data types or collations, `NOT IN` with nullable columns.
5. Check query shape: unnecessary columns (`SELECT *` blocking covering indexes), row-by-row scalar functions, correlated subqueries that could be joins or `EXISTS`, `DISTINCT` hiding join fan-out, pagination by large offsets, missing filters pushing work late.
6. Separate query cost from environment: blocking, lock waits, memory grant waits, cold cache, parallelism skew. If waits dominate, the fix is not in the query text.
7. Propose fixes ranked by impact and risk: statistics refresh or extended statistics, predicate rewrite, query restructuring, new or changed index (with write and storage cost), plan-stabilizing options as a last resort. Never recommend hints without stating why the optimizer chose otherwise.
8. For each fix, state the expected plan change (e.g. seek instead of scan, hash join replaced by nested loop on 200 rows) and side effects on other queries and DML.
9. Define verification: compare duration, logical reads and the new plan across representative and extreme parameter values; check that results are identical.
10. Fill the output template. If the goal continues, suggest `index-recommendation` for workload-wide index design, `schema-migration-plan` to deploy index or schema changes safely, or `database-health-check` if waits dominate.

## Output format
```markdown
# Query Optimization: <query name/purpose>
Engine: <...> | Current: <duration, reads> | Target: <...> | Frequency: <...>

## Diagnosis
- Dominant cost: <operator, % of time/IO>
- Estimate vs actual: <operator: est X / act Y> → cause: <...>
- Other findings: <non-sargable predicate, spill, lookups, waits>

## Recommendations
| # | Change | Why (evidence) | Expected effect | Cost / risk | Priority |
|---|---|---|---|---|---|

## Rewritten Query (if applicable)
<SQL>

## Verification
- Parameters tested: <typical, extreme>
- Compare: duration, logical reads, plan shape, identical results

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The diagnosis points to specific plan operators and numbers, not generic advice.
- [ ] Estimate-vs-actual gaps are explained with a cause.
- [ ] Every index recommendation states write and storage cost and overlap with existing indexes.
- [ ] Rewrites preserve result semantics (nulls, duplicates, ordering).
- [ ] Verification covers typical and extreme parameter values.
- [ ] Unsupported claims are labeled; no row counts or timings are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Adding an index for every slow query: write amplification and plan instability grow; check whether an existing index can be extended first.
- Testing only with the parameter value that is fast; parameter-sensitive plans need the skewed values too.
- Fixing with hints or forced plans that silently become wrong as data changes; fix estimates first.

## Example
Input: "Order search 200 ms → 9 s after import. Plan: index seek on orders.created_at est 120 rows, actual 2.4M; nested loop to order_lines."

Excerpt of output:
- Dominant cost: nested loop into order_lines executed 2.4M times (≈85% of reads).
- Cause: statistics on `orders.created_at` predate the import; the ascending-key range is estimated as nearly empty `[ASSUMPTION: confirm last statistics update time]`.
- Rec 1: update statistics on `orders` (low risk); expected: hash join, ~50x fewer reads. Rec 2: include `status` in the `created_at` index to remove lookups; cost: wider index on a write-heavy table.
