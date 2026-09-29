---
description: Generates a ranked list of debugging hypotheses from symptoms and evidence, and pairs each with the cheapest discriminating test, so the investigation converges instead of wandering. Use when a bug's cause is unknown, several explanations seem plausible, a debugging session is going in circles, or a team needs to split investigation work.
related: bug-reproduction, stack-trace-analysis, log-analysis, five-whys, fishbone-analysis
prompt: After the last deploy, about 2% of API requests take over 5 seconds, only on some pods. Give me ranked hypotheses and how to test each.
---

# Generate Debugging Hypotheses

## Purpose
Replace trial-and-error with a disciplined search: explicit hypotheses, ranked by likelihood and cost to test, each with a test whose outcome eliminates or confirms it. This shortens time to root cause and keeps the team from fixing symptoms.

## When to use
- The symptom is known but the cause is not.
- Several plausible explanations compete, or the team is stuck.
- Investigation needs to be parallelized across people.

## When not to use
- There is no reliable way to trigger the defect yet and it is cheap to build one. Start with `bug-reproduction`.
- A process or organizational root cause analysis after an incident. Use `five-whys` or `postmortem`.

## Inputs
Required:
- The symptom: what is wrong, where, and how it was observed.

Optional, improves quality:
- Facts known so far: when it started, scope (users, pods, regions, versions), frequency, recent changes.
- Evidence already gathered: logs, metrics, traces, stack traces, what was already tried and ruled out.
- Architecture context and dependencies.

If the scope or start time is unknown, list establishing them as the first cheap tests rather than guessing.

## Process
1. Read the full error, trace and evidence before theorizing. Write the symptom precisely with scope and frequency; list facts separately from beliefs, and label every inference.
2. Ask the discriminating questions: What changed (code, config, data, traffic, dependencies, infrastructure)? What is different between failing and working cases? Is it deterministic?
3. Generate hypotheses across categories so none is skipped: code change, configuration/feature flag, data shape or volume, dependency or third-party behavior, infrastructure/resources, concurrency/timing, environment/time (clock, DST, certificates, quotas).
4. For each hypothesis, state the mechanism in one sentence (how it would cause exactly this symptom) and the evidence for and against it.
5. Discard hypotheses that contradict known facts; note why.
6. Estimate likelihood (High/Medium/Low) from evidence, and cost to test (minutes, hours, days, needs production access).
7. Design the cheapest discriminating test for each, changing one variable per experiment: an observation or experiment whose result differs depending on whether the hypothesis is true (query, metric split, log field, toggle flag, roll back one pod, replay a request).
8. Order the plan by likelihood divided by cost; group tests that can run in parallel and assign owners if a team is involved.
9. Define the stop condition: what result confirms root cause (the defect can be switched on and off by changing that factor), and what to do if all hypotheses are eliminated (widen scope, add instrumentation). Iron law: no fix without a confirmed root cause; if three fixes have already failed, stop and question the design and the assumptions instead of trying a fourth.
10. When root cause is confirmed, suggest `bug-reproduction` to lock it into a failing test; when evidence is thin, suggest `log-analysis` or `stack-trace-analysis`; for recurring or systemic causes, suggest `five-whys` or `fishbone-analysis`.

## Output format
```markdown
# Debugging Hypotheses: <symptom>
## Facts
- ...
## Unknowns to Establish First
- ...

## Hypotheses
| # | Hypothesis | Mechanism | Evidence for / against | Likelihood | Cheapest test | Cost | Expected result if true |
|---|---|---|---|---|---|---|---|

## Discarded
- <hypothesis> — contradicts <fact>

## Test Plan
1. <test> — owner [TBD] — parallel with #...

## Root Cause Confirmation Criteria
- ...
```

## Quality checklist
- [ ] Hypotheses span multiple categories, not only the first idea.
- [ ] Each hypothesis explains the specific symptom, including its scope and frequency.
- [ ] Every test discriminates: its result would change your belief.
- [ ] The plan is ordered by likelihood and cost, not by curiosity.
- [ ] Hypotheses contradicted by facts are explicitly discarded.
- [ ] Confirmation requires turning the defect on and off, not just correlation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Anchoring on the recent deployment and ignoring data or traffic changes in the same window.
- Running tests that cannot fail (e.g., checking that the service is up). Each test must be able to eliminate something.
- Stopping at the first plausible cause. Confirm it by toggling the factor before declaring root cause.
- Red flags: "quick fix for now", "just try X and see", stacking several changes at once. Each means guessing has replaced diagnosis; return to the hypothesis table.

## Example
Input: After deploy v4.12, ~2% of requests exceed 5 s, only on some pods; CPU normal.

Excerpt of output:
- H1 (High, 10 min): New pods run with a smaller DB connection pool from the changed config default. Test: compare pool settings and wait-time metrics between slow and fast pods. If true: only slow pods show pool wait > 0.
- H2 (Medium, 30 min): Slow pods sit on nodes with a noisy neighbor. Test: map slow pods to nodes; if true, slowness follows the node, not the version.
- Discarded: GC pauses — CPU and GC metrics flat on slow pods.
