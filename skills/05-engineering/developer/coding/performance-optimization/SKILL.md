---
name: performance-optimization
description: "Finds and fixes performance hotspots in code from measurements rather than guesses: defines the target metric, reads profiles, traces or query plans, ranks bottlenecks by share of cost, proposes fixes with expected gain and trade-offs, and specifies how to verify the improvement. Use when code, an endpoint or a job is too slow or too resource-hungry, or someone asks to optimize, speed up or reduce CPU, memory or latency."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: coding
  title: "Optimize performance"
  related: "sql-query-writing, query-optimization, load-test-analysis, web-performance-audit, logging-instrumentation"
  prompt: "Our order search endpoint has a p95 of 2.4 s under normal load. Here is the handler code and a CPU profile, help me make it faster."
---

# Optimize Performance

## Purpose
Reduce latency, throughput limits or resource use where it matters, backed by measurements, so that effort goes to the real bottleneck and every change can be shown to help without breaking behavior.

## When to use
- An endpoint, job or function misses a latency, throughput or cost target.
- A profile, trace, flame graph or slow query log is available and needs interpreting.
- Resource usage (CPU, memory, allocations, connections) grows faster than load.

## When not to use
- Browser page speed and Core Web Vitals. Use `web-performance-audit`.
- A single slow SQL statement with its plan. Use `query-optimization` or `sql-query-writing`.
- Analyzing load test results for a whole system. Use `load-test-analysis`.

## Inputs
Required:
- The code or component, and the symptom with a number (for example p95 latency, duration, memory peak).

Optional, improves quality:
- Profiles, traces, query plans, metrics dashboards, load profile and data volumes.
- The target (SLO, budget) and constraints (no new infrastructure, API must not change).

If no measurement exists, do not guess a hotspot: give a measurement plan first and mark any suspicion `[HYPOTHESIS]`.

## Process
1. State the target as a metric, percentile and load condition (for example "p95 < 500 ms at 50 req/s"); if missing, propose one and mark it `[ASSUMPTION]`.
2. Establish a baseline: how it was measured, environment, data volume, warm or cold. Reject comparisons across different conditions.
3. Locate where time or resources go using the evidence: wall-clock vs CPU time, I/O waits, lock contention, GC or allocation pressure, N+1 calls, serialization.
4. Rank bottlenecks by their share of total cost (Amdahl): a 50% gain on 5% of the time is worth little.
5. For each top bottleneck, choose the cheapest effective fix class: do less work (remove, batch, paginate), avoid repeated work (cache, memoize, precompute), do it closer to data (push filter to the database, add index), do it concurrently, or use a better algorithm or data structure.
6. State the expected gain with reasoning and the trade-offs: memory, staleness, complexity, consistency, cost.
7. For caches, define key, TTL, invalidation, size limit and stampede protection; for concurrency, define limits and back-pressure.
8. Keep behavior identical: name the tests that guard it, and add missing ones before changing code.
9. Define the verification: same benchmark or load, same environment, before/after numbers, and a regression guard (benchmark in CI, alert, SLO).
10. Label every unmeasured claim as `[HYPOTHESIS]` and list what to measure next.
11. If the goal continues, suggest `query-optimization` for database-bound hotspots, `logging-instrumentation` if signals were missing, or `load-test-analysis` to confirm at scale.

## Output format
```markdown
# Performance Optimization: <component>
Target: <metric, percentile, load> · Baseline: <value, how measured>

## Where the Cost Is
| Rank | Hotspot | Evidence | Share of cost |

## Proposed Changes
| # | Change | Fix class | Expected gain | Trade-offs | Guarding tests |

## Code Changes
<diff or code for the top change>

## Verification Plan
- Benchmark / load: ...
- Regression guard: ...

## Hypotheses and Open Questions
- [HYPOTHESIS] ...
```

## Quality checklist
- [ ] The target is a number with a percentile and a load condition.
- [ ] Every hotspot cites evidence (profile, trace, plan, metric), or is marked `[HYPOTHESIS]`.
- [ ] Changes are ordered by share of cost, not by ease or taste.
- [ ] Each change states its trade-offs and the tests that protect behavior.
- [ ] Before/after measurement uses the same conditions.
- [ ] No gains or numbers are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Micro-optimizing code that takes 2% of the time while an N+1 query takes 70%. Rank first.
- Averages hide tail latency. Use percentiles and look at the slowest requests' traces.
- Adding a cache without invalidation rules and turning a speed problem into a correctness problem.
- Benchmarking in a warm local loop and expecting the same gain in production.

## Example
Input: "Order search p95 is 2.4 s. CPU profile shows 18% in JSON serialization; trace shows 40 DB calls per request."

Excerpt of output:
| Rank | Hotspot | Evidence | Share of cost |
|---|---|---|---|
| 1 | N+1 loading order lines per order | Trace: 40 sequential DB spans, ~1.6 s | ~65% |
| 2 | Serializing full order graph | Profile: 18% CPU | ~15% `[HYPOTHESIS: CPU share ≠ wall time]` |

Change 1: load lines with one batched query by order ids; expected p95 drop of roughly the DB span time; guarded by existing search contract tests plus a new test with 50 orders.
