---
name: performance-test-plan
description: "Writes a performance test plan with objectives tied to measurable acceptance criteria (latency percentiles, throughput, error rate, resource limits), a workload model derived from production data or business forecasts, test types (load, stress, soak, spike, scalability), scenarios, test data, environment and its gap to production, monitoring, entry/exit criteria and risks. Use before a release, migration or expected traffic increase, when non-functional requirements must be verified, or when a performance test must be designed from scratch."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: performance-engineer
  area: performance
  title: "Write a performance test plan"
  related: "load-test-analysis, capacity-test-report, slo-definition, test-data-design, nfr-to-architecture"
  prompt: "We launch a campaign that may triple checkout traffic. Write a performance test plan for the checkout API and its dependencies."
---

# Write a Performance Test Plan

## Purpose
Design performance tests that answer a concrete business question ("can checkout handle the campaign peak within its SLO?") with a realistic workload, a representative environment and pass/fail criteria agreed before the first run.

## When to use
- A release, platform migration or infrastructure change could affect performance.
- A traffic increase (campaign, season, new market) is expected.
- Non-functional requirements or SLOs exist but have never been verified under load.

## When not to use
- Results of an executed test must be interpreted. Use `load-test-analysis`.
- The maximum sustainable load and headroom must be reported. Use `capacity-test-report`.
- A known slow code path must be optimized. Use `performance-optimization`.

## Inputs
Required:
- System or transactions under test and the question the test must answer (release check, peak readiness, capacity limit).

Optional, improves quality:
- Production traffic data (requests per second by endpoint, peak hour, user journeys, think times), growth forecasts.
- NFRs/SLOs, architecture and dependencies, environment details, available load tool and budget.
- Data volumes and data privacy constraints.

If the question or the transactions are unknown, ask. If no production data exists, derive the workload from business forecasts and mark it `[ASSUMPTION]`.

## Process
1. Write the objectives as testable questions and link each to acceptance criteria: p95/p99 latency per transaction, throughput, error rate, resource ceilings (CPU, memory, connection pools), stated under a defined load.
2. Build the workload model: transaction mix (percentages), arrival rate or concurrent users with think time, peak vs average, growth factor; use an open (arrival-rate) model for public traffic. Show the calculation and its source.
3. Choose test types and their purpose: baseline, load (expected peak), stress (beyond peak to breaking point), spike (sudden surge), soak (hours at steady load for leaks), scalability (autoscaling behavior).
4. Define scenarios per test type: ramp-up, steady state duration, ramp-down, target load levels, and what is measured in each.
5. Design test data: volumes comparable to production, cardinality and distribution (hot keys, cache hit ratio), unique data for write paths, reset strategy; use synthetic or masked data, never raw personal data.
6. Describe the environment and every difference from production (size, topology, data volume, shared components, third-party stubs) and how results will be scaled or caveated.
7. Plan monitoring on both sides: load generator health, client-side metrics, server-side metrics (resources, GC, pools, queues, database), distributed traces; align clocks and timestamps.
8. Define entry criteria (functional stability, environment ready, data loaded, monitoring verified) and exit criteria (acceptance criteria met or deviations accepted by a named role).
9. List risks and constraints: shared environments, third-party rate limits, cost of load generation, test windows; plan how to notify affected teams.
10. Define schedule, roles and the reporting format; mark any unknown numbers `[TBD]` or `[ASSUMPTION]`.
11. If the goal continues, suggest `load-test-analysis` after execution, `capacity-test-report` for headroom decisions, or `slo-definition` if acceptance criteria are missing.

## Output format
```markdown
# Performance Test Plan: <system / release>
Question to answer: ...

## Objectives and Acceptance Criteria
| Transaction | Load level | p95 | p99 | Throughput | Error rate | Resource limit |
|---|---|---|---|---|---|---|

## Workload Model
| Transaction | Mix % | Peak rate | Think time | Source |
|---|---|---|---|---|
Calculation: ...

## Test Types and Scenarios
| Test | Purpose | Ramp-up | Steady state | Target load | Measured |
|---|---|---|---|---|---|

## Test Data
## Environment and Differences from Production
| Aspect | Production | Test | Impact on results |
|---|---|---|---|
## Monitoring
## Entry and Exit Criteria
## Risks, Schedule and Roles
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every objective has a numeric acceptance criterion stated as a percentile under a defined load, or is marked `[TBD]`.
- [ ] The workload model shows its source and calculation; forecast-based numbers are labeled `[ASSUMPTION]`.
- [ ] Each test type has a stated purpose, not just a name.
- [ ] Environment differences from production are listed with their effect on results.
- [ ] Test data avoids raw personal data and matches production distribution where it matters.
- [ ] Monitoring covers load generators as well as the system under test.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using averages as acceptance criteria. Averages hide tail latency; use p95/p99.
- Closed-model tests with few virtual users and no think time, which throttle themselves when the system slows (coordinated omission). Use arrival-rate models for public traffic.
- Tiny test databases with perfect cache hit rates, producing results that production never sees.

## Example
Input: "Campaign may triple checkout traffic; current peak 40 req/s on checkout."

Excerpt of output:
- Objective: At 120 req/s checkout (3 × current peak of 40 req/s, from input), p95 ≤ 800 ms `[ASSUMPTION: confirm SLO]`, error rate < 0.5%.
| Test | Purpose | Ramp-up | Steady state | Target load | Measured |
|---|---|---|---|---|---|
| Load | Verify campaign peak | 15 min | 60 min | 120 req/s | Latency, errors, DB pool usage |
| Stress | Find breaking point | Step +20 req/s every 10 min | Until SLO breach | > 120 req/s | First saturated resource |
| Soak | Detect leaks | 10 min | 6 h | 60 req/s | Memory trend, connection count |
