---
description: Reviews how a system scales by modeling load growth against each component, locating bottlenecks (CPU, I/O, locks, connections, hot partitions, shared state), and assessing statelessness, partitioning, caching, asynchronous processing and data-tier limits, with prioritized recommendations and the scaling limit of the current design. Use before an expected growth step or peak event, when latency degrades with load, or when choosing between scale-up and scale-out.
related: capacity-planning, performance-test-plan, load-test-analysis, resilience-review, query-optimization
prompt: Review the scalability of our reporting API; traffic will grow 5x after we onboard a large customer and p95 latency already rises sharply at month end.
---

# Review Scalability

## Purpose
Establish how far the current design can grow, what breaks first and why, and which changes buy the most headroom, so growth is handled by design rather than emergency hardware.

## When to use
- A known growth step, customer onboarding or seasonal peak is coming.
- Latency or error rate rises non-linearly with load.
- The team must choose between scaling up, scaling out or redesigning a component.

## When not to use
- The need is a capacity forecast and procurement plan. Use `capacity-planning`.
- Failure behavior rather than growth is the concern. Use `resilience-review`.
- A specific slow query or code path is already identified. Use `query-optimization` or `performance-optimization`.

## Inputs
Required:
- The architecture of the flows under review (components, data stores, call paths).
- Current and expected load (requests, data volume, concurrent users) or permission to mark them `[UNKNOWN]`.

Optional:
- Performance and utilization metrics, load test results, peak patterns, data growth rates.
- Latency/throughput targets, cost ceiling, platform limits (quotas, licence caps).

If load figures are missing, proceed with relative multipliers (e.g., "5x current") and list measurements to collect.

## Process
1. Define the workload model: key operations, mix, arrival pattern (steady, bursty, month-end), read/write ratio, data growth, and the target multiplier.
2. Trace each key operation through the components and record per-hop resource use and fan-out (calls per request, queries per request, N+1 risks).
3. Check statelessness: session, in-memory caches, local files, sticky routing, scheduled jobs that assume a single instance.
4. Check the data tier: connection limits and pooling, lock and hot-row contention, index and query plans under larger data, read replica suitability and lag tolerance, partitioning/sharding key and hot partition risk.
5. Check caching: what is cached, hit ratio, invalidation strategy, stampede protection, cache as a hidden single point of failure.
6. Check asynchronous paths: queue depth growth, consumer parallelism vs. ordering constraints, back-pressure, batch window lengths as data grows.
7. Check shared and external limits: third-party rate limits, platform quotas, licence-bound components, network egress, single-writer components.
8. Identify the first three bottlenecks with the evidence or reasoning, and estimate the load at which each saturates, labeling estimates `[ASSUMPTION]` until measured.
9. Recommend changes ordered by headroom gained per effort: configuration and pooling, query/index fixes, caching, horizontal scaling, async offloading, partitioning, redesign; note cost and consistency trade-offs.
10. Define how to verify: load test scenarios, metrics and saturation signals (utilization, saturation, errors) to monitor.
11. If the goal continues, suggest `performance-test-plan` to verify limits, `capacity-planning` for sizing or `query-optimization` for data-tier hotspots.

## Output format
```markdown
# Scalability Review: <system> – <date>
## Workload Model
| Operation | Current rate | Target rate | Pattern | Read/Write |
|---|---|---|---|---|
## Request Path Analysis
| Operation | Hop | Resource | Fan-out | Concern |
|---|---|---|---|---|
## Bottlenecks
| Rank | Component | Mechanism | Saturates at (est.) | Evidence |
|---|---|---|---|---|
## Recommendations
| ID | Change | Headroom gained | Effort | Trade-off |
|---|---|---|---|---|
## Verification Plan
## Current Design Limit
## Assumptions, Measurements to Collect, Open Questions
```

## Quality checklist
- [ ] The workload model states the target multiplier and arrival pattern, not only an average.
- [ ] Every bottleneck names a mechanism (lock, pool, partition, fan-out), not only "database is slow".
- [ ] Saturation estimates are labeled as estimates with the data needed to confirm.
- [ ] Recommendations are ordered by headroom per effort and state trade-offs.
- [ ] Stateful components and external limits were checked explicitly.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Assuming horizontal scaling of the app tier solves everything while the database or a third-party limit is the ceiling.
- Designing for average load; month-end or campaign bursts drive the real requirement.
- Adding caches without invalidation and stampede design, trading latency for incorrect data.

## Example
Input: "Reporting API, 5x growth expected, p95 already spikes at month end."

Excerpt of output:
| Rank | Component | Mechanism | Saturates at (est.) |
|---|---|---|---|
| 1 | Primary DB | Month-end reports run heavy aggregations on the OLTP primary; lock waits and I/O saturation | ~1.5x current month-end load `[ASSUMPTION – confirm from DB metrics]` |
| 2 | API pods | Each report request holds a DB connection for the full query; pool of 20 per pod | Pool exhaustion before CPU |

Top recommendation: move report queries to a read replica or pre-aggregated store, make large reports asynchronous (request, poll, download).
