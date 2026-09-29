---
name: capacity-planning
description: "Produces a capacity plan for a service or platform: demand forecast from organic growth and known events, per-resource saturation limits from load tests or production data, required capacity with headroom and N+1 redundancy, lead times, scaling triggers and cost impact. Use when a launch, campaign or seasonal peak is coming, when utilization trends toward limits, or when budgeting infrastructure for the next period."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Plan capacity"
  related: "capacity-test-report, load-test-analysis, scalability-review, finops-review, observability-plan"
  prompt: "Plan capacity for our checkout for Black Friday. Normal peak is 800 req/s, marketing expects 4x traffic; we run 12 pods and one primary database."
---

# Plan Capacity

## Purpose
Make sure a service has enough capacity, with explicit headroom and redundancy, to meet forecast demand within its SLOs, and that resources with long lead times are ordered in time, without over-provisioning that wastes budget.

## When to use
- A known demand event is coming: launch, campaign, seasonal peak, new customer onboarding, migration of traffic.
- Utilization trends show a resource approaching its limit (connections, storage, throughput, quotas).
- Infrastructure budget or reserved capacity must be planned for the next period.

## When not to use
- The need is to run or analyze a load test itself. Use `performance-test-plan` or `load-test-analysis`.
- The architecture cannot scale and needs redesign. Use `scalability-review`.
- The goal is cutting cost of existing capacity. Use `finops-review`.

## Inputs
Required:
- Service scope and the demand driver (requests, users, transactions, data volume) with a current baseline.
- Forecast period and any known demand event.

Optional, improves quality:
- Historical usage per resource (peak, not only average), load test results, known bottlenecks.
- Scaling mechanisms (autoscaling bounds, manual steps), provider quotas, procurement lead times.
- SLO targets, redundancy requirements, budget limits.

If the baseline or forecast driver is missing, ask. Never invent growth rates; mark estimates `[ASSUMPTION]` with their source.

## Process
1. Define the demand unit that drives load (e.g. requests/s at peak minute, orders/hour, GB ingested/day) and establish the current peak baseline from real data.
2. Forecast demand for the period: organic trend (from history), plus known events (with a multiplier and its source), plus uncertainty band (low/expected/high).
3. Translate demand into resource needs for every constrained resource: compute, memory, database connections and IOPS, storage growth, queue throughput, network egress, third-party rate limits and cloud quotas.
4. Determine the safe limit per unit of capacity from load tests or production saturation points, measured at the SLO latency threshold, not at failure.
5. Compute required capacity: forecast peak / safe limit per unit, plus headroom (commonly 20-40% `[PROPOSED]`) and redundancy (N+1 or zone failure tolerance), and identify the first bottleneck.
6. Check scaling paths and lead times: which resources autoscale and how fast, which need manual change, which need procurement or quota increases, and schedule them backwards from the event date.
7. Identify non-linear risks: shared databases, caches with cold-start behavior, connection pool exhaustion, dependency limits, retry storms.
8. Estimate cost impact per scenario without inventing prices; use given rates or mark cost `[TBD]`.
9. Define triggers and monitoring: utilization thresholds that prompt the next scaling step, plus a load-shedding or degradation plan if demand exceeds the high scenario.
10. Label every inference `[ASSUMPTION]`, list open questions, and suggest `performance-test-plan` to validate limits, `finops-review` to optimize cost, or `scalability-review` if a bottleneck needs design change.

## Output format
```markdown
# Capacity Plan: <service> – <period or event>
Demand unit: <unit> · Baseline peak: <value, source> · Owner: <team>

## Demand Forecast
| Scenario | Peak demand | Basis |

## Resource Requirements
| Resource | Safe limit per unit | Current | Required (with headroom, N+1) | Gap | Scaling path | Lead time |

## Bottlenecks and Non-linear Risks
## Actions and Schedule
| Action | Owner | Due (relative to event) |

## Cost Impact
## Triggers, Monitoring and Degradation Plan
## Assumptions and Open Questions
```

## Quality checklist
- [ ] The baseline uses peak values from real data, or is marked `[UNKNOWN]`.
- [ ] Every constrained resource is covered, including quotas and third-party limits.
- [ ] Safe limits are measured at the SLO threshold, not at breaking point.
- [ ] Headroom and redundancy are applied explicitly and the first bottleneck is named.
- [ ] Lead-time actions are scheduled backwards from the event date.
- [ ] No growth rate or price is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Planning on average utilization. Peaks drive saturation; use the peak minute or the relevant percentile.
- Scaling stateless pods and forgetting the database connection limit that they all share.
- Counting autoscaling as capacity without checking its maximum, its reaction time and the underlying quota.

## Example
Input: "Checkout, normal peak 800 req/s, 4x expected, 12 pods, one primary database."

Excerpt of output:
| Resource | Safe limit per unit | Current | Required | Gap |
|---|---|---|---|---|
| API pods | 90 req/s per pod at p99 < 400 ms `[ASSUMPTION: from last load test, confirm]` | 12 | 3200 / 90 × 1.3 headroom ≈ 47 | +35 |
| DB connections | 500 max | 12 × 20 = 240 | 47 × 20 = 940 | exceeds limit: first bottleneck |

Action: add connection pooling proxy or cut pool size per pod; validate with a load test before the event.
