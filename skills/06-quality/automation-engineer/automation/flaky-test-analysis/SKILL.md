---
name: flaky-test-analysis
description: "Analyzes flaky automated tests by measuring flake rate from run history, classifying the cause (timing and async, shared state and order dependence, test data, environment and infrastructure, external dependencies, concurrency, non-deterministic product behavior), confirming it with one-variable experiments and proposing a root-cause stabilization plus a quarantine policy. Use when tests pass and fail without code changes, when CI reruns are routine, or when the team no longer trusts red builds."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: automation-engineer
  area: automation
  title: "Analyze flaky tests"
  related: "test-automation-script, automation-framework-design, debugging-hypotheses, pipeline-failure-triage, log-analysis"
  prompt: "These 6 end-to-end tests fail randomly in CI about once every 10 runs, never locally. Here are the failure logs. Why, and how do we fix them?"
---

# Analyze Flaky Tests

## Purpose
Restore trust in the test suite by finding why specific tests give different results on the same code and fixing the cause, not hiding it with retries, while keeping real product bugs from being dismissed as "just flaky".

## When to use
- A test fails intermittently on unchanged code, locally or in CI.
- Reruns have become a normal step to get a green build.
- The team is about to disable or quarantine tests and needs a decision basis.

## When not to use
- A test fails consistently after a code change. Use `debugging-hypotheses` or `stack-trace-analysis`.
- The whole pipeline fails for infrastructure or configuration reasons. Use `pipeline-failure-triage`.
- You need to rewrite a test from scratch. Use `test-automation-script`.

## Inputs
Required:
- The flaky test(s) and at least one failure output (error, stack trace, screenshot or log).

Optional, improves quality:
- Run history (pass/fail per run, runner, parallelism, order, duration), test code, recent changes to tests, product or infrastructure.
- Environment details: parallel workers, shared databases, external services, clock/timezone settings.

If no failure output is available, ask for it. Without run history, state that the flake rate is unknown and do not estimate one.

## Process
1. Read the full failure output for every failing run, not only the assertion line; note where it failed (setup, action, assertion, teardown) and whether all failures share the same point.
2. Quantify: flake rate over the available runs, first-seen date, correlation with runner, parallelism, time of day, test order or duration. Check recent changes around the first-seen date.
3. Classify the likely cause: timing/async (fixed sleeps, missing waits, animations), shared state/order dependence, test data collisions, environment/resources (CPU, memory, containers), external dependency, concurrency in the product, time/locale, or genuinely non-deterministic product behavior (a real bug).
4. State one hypothesis at a time, each with the evidence for and against it; label it `[HYPOTHESIS]`.
5. Design a one-variable experiment per hypothesis: run in isolation vs in suite, randomize order, force parallelism, loop the test N times, throttle CPU or network, freeze the clock. Change only one factor per run.
6. Trace backwards from the failing assertion to the state that caused it (which data, which earlier step, which async event) until the root cause is confirmed.
7. If the root cause is in the product (race condition, lost update, inconsistent read), stop treating it as a test issue and raise a defect with the evidence.
8. Propose the stabilization at the cause: condition-based waits, isolated data, reset of shared state, stubbing or contract-testing the external dependency, deterministic clock. Reject "add retries" or "increase timeout" as the fix unless the timeout is provably too small.
9. If three stabilization attempts fail, stop and question the test's design or level (can the check move to API or component level?).
10. Define the quarantine policy for the interim: quarantined tests still run and report, have an owner and an expiry date, and do not block merges; nothing stays quarantined indefinitely.
11. If the user continues, suggest `test-automation-script` to rewrite the test, `automation-framework-design` for systemic causes (shared data, waits), or `bug-report` when the product is at fault.

## Output format
```markdown
# Flaky Test Analysis: <test/suite>
## Evidence
| Test | Runs observed | Failures | Flake rate | Failure point | Correlates with |
|---|---|---|---|---|---|

## Cause Classification
| Test | Category | Evidence | Confidence |
|---|---|---|---|

## Hypotheses and Experiments
1. [HYPOTHESIS] ... — experiment: <one variable> — result: <confirmed/refuted/pending>

## Root Cause
- ... (or: not yet confirmed — next experiment: ...)

## Stabilization Plan
| Test | Fix at the cause | Level change? | Owner | Verification (N consecutive green runs) |
|---|---|---|---|---|

## Quarantine Decision
- Tests quarantined, owner, expiry date, still reported: yes/no

## Product Defects Raised
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The full failure output was read and the failure point identified for each run.
- [ ] Flake rates come from actual run data; none are estimated without history.
- [ ] Each hypothesis is tested with a one-variable experiment and labeled until confirmed.
- [ ] The fix addresses the root cause; retries or longer timeouts are not presented as the fix.
- [ ] Possible product defects are separated from test defects and raised.
- [ ] Every quarantined test has an owner and an expiry date.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Adding automatic retries. It turns the build green and hides both test and product races; use retries only to collect evidence.
- Assuming "flaky" means "test problem". Intermittent failures are often real concurrency bugs that users will hit.
- Changing several things at once. When the test stabilizes you no longer know why, and the cause returns.

## Example
Input: 6 end-to-end tests fail about 1 in 10 CI runs, never locally; logs show "element not clickable" and one "order not found".

Excerpt of output:
- Evidence: all failures on 4-worker runs; none on single-worker runs → correlates with parallelism.
- `[HYPOTHESIS]` tests share the fixed customer `test-user-01`; parallel runs modify the same cart — experiment: run the suite with 4 workers and unique customers per test — result: 0 failures in 50 runs → confirmed.
- Fix: create a customer per test via the data API; remove the shared account from fixtures. "Element not clickable": replace 2-second sleep with wait for the overlay to be hidden.
