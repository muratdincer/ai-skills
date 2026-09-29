---
description: Writes a capacity test report that determines the maximum sustainable load within SLOs from stepped or stress test results, identifies the limiting resource, calculates headroom against current and forecast peaks, describes scaling behavior and its limits, and recommends capacity actions with their triggers. Use after capacity, stress or scalability tests, when leadership asks how much growth the system can absorb, or when infrastructure sizing and scaling limits must be justified with test evidence.
related: load-test-analysis, performance-test-plan, capacity-planning, scalability-review, finops-review
prompt: We ran a stepped load test on the search service up to failure. Write a capacity report: how much headroom do we have for next year's forecast?
---

# Write a Capacity Report

## Purpose
State, with evidence, how much load the system can sustain while meeting its SLOs, which resource runs out first, and how much headroom remains against current and forecast demand, so that scaling and investment decisions are made before users feel the limit.

## When to use
- A stepped, stress or scalability test has been run to find the system's limits.
- Stakeholders ask whether the system can absorb forecast growth, a campaign or a new tenant.
- Infrastructure sizing, autoscaling limits or reserved capacity must be justified.

## When not to use
- A single test run needs a pass/fail interpretation. Use `load-test-analysis`.
- Long-term capacity planning from production telemetry is needed rather than test results. Use `capacity-planning`.
- The test has not been designed yet. Use `performance-test-plan`.

## Inputs
Required:
- Test results across increasing load levels (throughput, latency percentiles, errors per step) and the SLO or acceptance criteria to judge "sustainable".

Optional, improves quality:
- Resource metrics per step (CPU, memory, pools, database, queues), instance counts and autoscaling configuration.
- Current production peak and growth forecast, environment differences from production, cost per instance.

If results per load step are missing, ask. If no SLO is given, ask; without it "sustainable" cannot be defined. If the user cannot provide one, use a proposed threshold marked `[ASSUMPTION]`.

## Process
1. Define "sustainable": the highest load at which all SLO criteria (e.g., p95 latency, error rate) hold during steady state for the full step duration, with no degrading trend.
2. Tabulate each load step with its results and mark the last step that meets the definition; this is the maximum sustainable load (MSL). Note the breaking point separately.
3. Identify the limiting resource at MSL: the first resource to saturate (CPU, memory, connection or thread pools, database, downstream dependency, rate limit). Support it with metrics; otherwise label it `[ASSUMPTION]`.
4. Describe scaling behavior: does throughput scale linearly with instances; where does it stop (shared database, locks, external limits); autoscaling reaction time vs. spike rise time.
5. Adjust for environment differences from production (instance size, count, data volume) and state the resulting uncertainty; do not extrapolate linearly beyond evidence.
6. Calculate headroom: (MSL − current peak) / current peak, and against forecast peaks; also express it as time until exhaustion if a growth rate is given.
7. Set a safety margin and alert thresholds (e.g., act when peak reaches a stated share of MSL) with the reasoning.
8. Recommend capacity actions: scale-out limits to raise, bottleneck to remove, configuration changes, cost-relevant options; each with the expected new MSL as a hypothesis to verify.
9. List assumptions, limitations and open questions.
10. If the goal continues, suggest `capacity-planning` for ongoing forecasting, `scalability-review` if the limit is architectural, or `finops-review` for the cost side of scaling options.

## Output format
```markdown
# Capacity Report: <system / test date>
Sustainable = <definition with SLO values>
Maximum sustainable load: <value> · Limiting resource: <resource> · Breaking point: <value>

## Results per Load Step
| Step | Target load | Achieved | p95 | p99 | Error rate | Key resource usage | Within SLO? |
|---|---|---|---|---|---|---|---|

## Headroom
| Reference | Load | Headroom vs MSL | Time to exhaustion |
|---|---|---|---|
| Current peak | | | |
| Forecast peak | | | |

## Scaling Behavior
## Environment Differences and Confidence
## Recommendations and Alert Thresholds
| Action | Expected effect (hypothesis) | Trigger / threshold | Verify by |
|---|---|---|---|
## Assumptions and Open Questions
```

## Quality checklist
- [ ] "Sustainable" is defined with explicit SLO values before the MSL is stated.
- [ ] MSL comes from a measured step, not an interpolation or extrapolation beyond tested load.
- [ ] The limiting resource is backed by metrics or labeled `[ASSUMPTION]`.
- [ ] Headroom is calculated against both current and forecast peak, with the formula shown.
- [ ] Environment differences and the resulting confidence are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting the breaking point as capacity. Capacity is the highest load that still meets the SLO, usually well below the breaking point.
- Linear extrapolation ("2 instances handle 200 req/s, so 10 handle 1000"). Shared resources stop linear scaling; test it or state it as an assumption.
- Ignoring autoscaling lag: capacity after scale-out does not help if spikes rise faster than new instances start.

## Example
Input: Steps 100/150/200/250/300 req/s; p95 SLO 500 ms; p95 = 180/220/310/480/1900 ms; errors 0/0/0.1/0.3/4%; DB CPU 85% at 250; current peak 160 req/s; forecast +40% next year.

Excerpt of output:
- MSL: 250 req/s (last step within SLO). Breaking point: 300 req/s. Limiting resource: database CPU (85% at 250) `[confirm with wait statistics]`.
| Reference | Load | Headroom vs MSL |
|---|---|---|
| Current peak | 160 req/s | (250 − 160) / 160 = 56% |
| Forecast peak (+40%) | 224 req/s | (250 − 224) / 224 = 12% |
- Recommendation: alert when peak exceeds 200 req/s (80% of MSL); reduce database load before forecast peak.
