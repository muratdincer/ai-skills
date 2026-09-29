---
name: bug-reproduction
description: "Turns a vague bug report into a minimal, deterministic reproduction with exact steps, environment, data preconditions, expected versus actual result and a reproduction rate, ideally ending in a failing automated test. Use when a defect is reported as hard to reproduce, intermittent, environment-specific, or only described in user terms, and before starting a fix."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: debugging
  title: "Reproduce a bug"
  related: "bug-report, debugging-hypotheses, log-analysis, unit-test-writing, flaky-test-analysis"
  prompt: "Users say the export sometimes produces an empty file. Help me build a reliable reproduction."
---

# Reproduce a Bug

## Purpose
Establish a reproduction that fails every time (or at a known rate) with the fewest steps and variables. Without it, fixes are guesses and verification is impossible; with it, the fix can be proven and protected by a regression test.

## When to use
- A bug report lacks steps, or the developer cannot trigger the defect.
- The defect is intermittent or appears only in some environments, tenants or devices.
- Before fixing, to capture the defect as a failing test.

## When not to use
- The reproduction is known and you need to find the cause. Use `debugging-hypotheses` or `stack-trace-analysis`.
- Writing the defect ticket for tracking. Use `bug-report`.
- The failure is in a test that passes and fails without code changes. Use `flaky-test-analysis`.

## Inputs
Required:
- The bug description: what was observed and where.

Optional, improves quality:
- Environment and version, time of occurrence, affected users or tenants, device/browser.
- Logs, error IDs, correlation/trace IDs, screenshots.
- Recent changes (deployments, config, data migrations, feature flags).

If you do not know which system or feature is affected, ask. Mask personal data in any logs or sample records shared.

## Process
1. Restate the defect as expected vs actual behavior in one sentence each; separate observations from the reporter's interpretation.
2. Inventory the variables that could matter: version/build, environment, config and feature flags, data shape and volume, user role/permissions, locale/time zone/clock, concurrency and timing, network conditions, client device/browser.
3. Compare a failing case with a working case and list the differences, including recent changes (commits, config, data, dependencies) between the last known good and first bad occurrence; each difference is a candidate variable.
4. Draft the first reproduction as close to the reported conditions as possible (same version, similar data, same role). Record whether it fails and how often (e.g., 3/20 runs).
5. Minimize: remove or fix one variable at a time and re-run; keep a variable only if removing it makes the failure disappear. Use bisection over data sets, commits or config when the space is large.
6. For intermittent defects, force the suspected condition: fixed seed, frozen clock, injected latency, reduced pool sizes, parallel execution, larger data volume. Report the reproduction rate before and after.
7. When the reproduction is stable, express it at the lowest level possible: unit or integration test first, then API call sequence, then UI steps.
8. Document preconditions and test data explicitly, using synthetic or masked data.
9. If you cannot reproduce, document what was tried, the variables ruled out, and the exact additional evidence needed (log fields, trace, dump, customer data sample).
10. Hand over: with a stable reproduction, suggest `debugging-hypotheses` to find the root cause (no fix before it is confirmed) and `unit-test-writing` to keep the failing test; if the report itself is incomplete, suggest `bug-report`.

## Output format
```markdown
# Reproduction: <defect title>
**Status:** Reproduced (<n>/<m> runs) | Not reproduced yet
**Expected:** ...
**Actual:** ...

## Environment
| Item | Value |
|---|---|
| Version / build | ... |
| Environment | ... |
| Config / flags | ... |
| Client | ... |

## Preconditions and Test Data
- ...

## Minimal Steps
1. ...

## Variables Ruled Out
- <variable> — <how tested>

## Automated Reproduction
<failing test name and outline, or TBD>

## If Not Reproduced: Evidence Needed
- ...
```

## Quality checklist
- [ ] Expected and actual results are stated separately and precisely.
- [ ] Every step and precondition is needed; removing any makes the failure disappear.
- [ ] Reproduction rate is stated for non-deterministic failures.
- [ ] Test data is synthetic or masked.
- [ ] A failing automated test is proposed or its absence explained.
- [ ] Unverified environment details are marked `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reproducing on the latest code instead of the reported version, then declaring "cannot reproduce". Pin the version first.
- Changing several variables at once during minimization. You lose the ability to say which one matters.
- Starting a fix before the reproduction is reliable ("quick fix for now"). Without a stable reproduction you cannot prove the fix works.
- Ignoring time: time zones, DST transitions, month ends and cache expiry produce "random" bugs that are fully deterministic.

## Example
Input: "Export sometimes produces an empty CSV file."

Excerpt of output:
- Variables: file size, concurrent exports by the same user, storage latency, time of day.
- Minimization: fails 0/20 with a single export; 6/20 when two exports run for the same user within 1 s.
- Minimal steps: 1) Log in as a user with >1,000 orders. 2) Start two exports in parallel. 3) Download the first file: 0 bytes.
- Next: hypothesis that both jobs share a temp file name keyed by user ID — hand over to `debugging-hypotheses`.
