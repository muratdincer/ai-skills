---
name: load-test-analysis
description: "Analyzes load test results by validating the test run, comparing throughput, latency percentiles and error rates against acceptance criteria, correlating client-side results with server-side resource, pool, queue and database metrics to locate bottlenecks, and recommending evidence-based fixes and retests. Use when a load, stress, spike or soak test has been executed and its report, metrics or charts must be interpreted, or when a test result is disputed and needs a second opinion."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: performance-engineer
  area: performance
  title: "Analyze load test results"
  related: "performance-test-plan, capacity-test-report, performance-optimization, query-optimization, observability-plan"
  prompt: "Here are the results of yesterday's checkout load test: summary table, latency chart description and database CPU. Did we pass, and what is the bottleneck?"
---

# Analyze Load Test Results

## Purpose
Give a clear pass/fail verdict against agreed criteria and, when it fails or degrades, name the bottleneck with evidence and the next experiment. The analysis must be trustworthy: an invalid test run is reported as invalid, not interpreted.

## When to use
- A load, stress, spike or soak test has finished and results must be interpreted.
- A result is disputed ("the test environment was the problem") and needs an objective review.
- Several runs must be compared after a fix or configuration change.

## When not to use
- The test has not been designed yet. Use `performance-test-plan`.
- The question is maximum sustainable load and headroom for planning. Use `capacity-test-report`.
- A specific slow query or code path is already identified. Use `query-optimization` or `performance-optimization`.

## Inputs
Required:
- Test results: at least throughput, latency (percentiles preferred) and errors per transaction or overall, with the load profile.

Optional, improves quality:
- Acceptance criteria/SLOs, test plan, server-side metrics (CPU, memory, GC, thread/connection pools, queue depth, database waits), traces, load generator metrics.
- Previous runs or production baseline, recent changes.

If results are missing, ask. If acceptance criteria are missing, analyze behavior and mark the verdict `[ASSUMPTION: criteria not given]`.

## Process
1. Validate the run: did the load generator reach the target rate, were generators saturated (CPU, network), was there a warm-up, did the error types include test-side errors (data exhausted, script errors)? If the run is invalid, stop and state what to fix.
2. Segment the timeline: ramp-up, steady state, ramp-down; analyze only steady state for acceptance and note transient effects separately.
3. Compare each transaction against criteria: achieved throughput vs target, p50/p95/p99 and max latency, error rate by type (HTTP code, timeout, business error). Mark pass/fail per criterion.
4. Look for the saturation pattern: the load level where throughput stops rising while latency rises (knee point), or where errors begin.
5. Correlate with server-side metrics at that moment: CPU, memory and GC pauses, thread and connection pool exhaustion, queue depth, database waits and locks, downstream latency, autoscaling events. Use the utilization-saturation-errors view per resource.
6. Form bottleneck hypotheses ranked by evidence; state for each what supports it and what would disprove it. Do not name a root cause without correlating evidence; label inferences `[ASSUMPTION]`.
7. For soak tests, check trends over time: memory growth, connection leaks, degrading latency, disk or log growth.
8. Compare with previous runs or baseline where available; quantify the change.
9. Recommend fixes and the retest that would verify each (change one variable per rerun).
10. State limitations: environment differences, data volume, missing metrics.
11. If the goal continues, suggest `capacity-test-report` once the system passes, `performance-optimization` or `query-optimization` for the identified bottleneck, or `observability-plan` if key metrics were missing.

## Output format
```markdown
# Load Test Analysis: <system / test / date>
Run validity: Valid / Invalid (reason) · Test type: ... · Load profile: ...
Verdict: Pass / Fail / Pass with risks

## Results vs Criteria (steady state)
| Transaction | Target rate | Achieved | p95 (target) | p99 (target) | Error rate (target) | Result |
|---|---|---|---|---|---|---|

## Saturation and Bottleneck
- Knee point: ...
| # | Hypothesis | Evidence | Disproved if | Confidence |
|---|---|---|---|---|

## Comparison with Baseline
## Recommendations and Retests
| Fix | Expected effect | Verify by |
|---|---|---|
## Limitations and Open Questions
```

## Quality checklist
- [ ] Run validity was checked before any interpretation, including load generator saturation.
- [ ] Acceptance is judged on steady-state percentiles, not averages or ramp phases.
- [ ] Every number cited comes from the supplied results; missing ones are `[UNKNOWN]`.
- [ ] The bottleneck claim cites correlated client and server evidence, or is labeled a hypothesis.
- [ ] Each recommendation has a verification retest that changes one variable.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting average response time as the result. Tail latency drives user experience and timeouts.
- Blaming the application when the load generator was saturated or the test data ran out.
- Declaring "database is the bottleneck" from high CPU alone. Check waits, locks and connection pool usage at the same timestamp.

## Example
Input: Target 120 req/s; achieved 95 req/s; p95 rises from 300 ms to 2.4 s after 90 req/s; app CPU 45%; DB connection pool 50/50 in use; timeouts 3%.

Weak: "Performance is bad, add more servers."

Strong excerpt:
- Verdict: Fail — throughput 95/120 req/s, p95 2.4 s (target ≤ 800 ms), error rate 3% (target < 0.5%).
- Knee point at ~90 req/s. Hypothesis 1: connection pool exhaustion (pool at 50/50 exactly when latency rises, app CPU only 45%). Disproved if DB waits show lock contention instead.
- Retest: raise pool to a size validated against DB max connections, rerun the same profile; expected knee above 120 req/s.
