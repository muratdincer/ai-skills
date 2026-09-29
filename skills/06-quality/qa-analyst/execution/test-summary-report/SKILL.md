---
description: "Writes a test summary (completion) report that states scope tested and not tested, execution results, coverage against requirements and risks, open defects by severity, deviations from the plan, residual risk and a clear recommendation, aligned with ISO/IEC/IEEE 29119-3 content. Use at the end of a test level, iteration or release cycle, when stakeholders need a decision-ready quality status, or when raw execution numbers must be turned into a report."
related: test-plan, release-quality-gate, bug-triage, defect-trend-analysis, executive-summary
prompt: "Write the test summary report for release 3.4 from these numbers: 412 cases, 389 passed, 11 failed, 12 blocked, 7 open bugs (1 critical), performance test not run."
---

# Write a Test Summary Report

## Purpose
Give decision makers an honest, evidence-based picture of product quality at the end of a test effort, including what was not tested, so they can accept the residual risk consciously.

## When to use
- A test level (system, integration, UAT) or release cycle finishes.
- Management or a release board asks "are we ready?" and needs a written basis.
- An iteration closes and quality status must be recorded.

## When not to use
- You need the formal go/no-go assessment against exit criteria. Use `release-quality-gate` (it can consume this report).
- You need trend and root cause analysis across releases. Use `defect-trend-analysis`.
- You need an in-progress daily status. Use `status-update`.

## Inputs
Required:
- Execution results (counts or lists) and open defects for the scope.

Optional, improves quality:
- Test plan with scope, exit criteria and schedule; requirement/risk coverage data.
- Environment issues, deviations, time lost, test types not executed.
- Audience (team, management, customer) and release decision date.

If results are missing, ask for them. Never derive percentages from numbers that are not given; mark gaps `[UNKNOWN]`.

## Process
1. Identify the audience and the decision the report supports; put the recommendation first for management audiences.
2. State scope: build/versions tested, environments, test levels and types executed, period.
3. State explicitly what was not tested or only partially tested, and why (descoped, blocked, environment, time).
4. Summarize execution: planned, executed, passed, failed, blocked, not run; compute percentages only from given numbers and show the denominator.
5. Report coverage against requirements and against identified product risks; highlight high-risk areas with low coverage.
6. Summarize defects: found and fixed in the period, open by severity and priority, blockers, notable accepted/deferred defects with workarounds.
7. List deviations from the plan: schedule slips, entry criteria not met, environment downtime, scope changes, and their effect on confidence.
8. Compare results with exit criteria from the plan, criterion by criterion (met / not met / not measurable).
9. Assess residual risk in business terms: what could go wrong in production, likelihood and impact, and mitigations (monitoring, feature flag, hotfix readiness).
10. Give a clear recommendation (release / release with conditions / do not release / continue testing) with conditions and owners; separate facts from the tester's judgment.
11. If the user continues, suggest `release-quality-gate` for the formal decision or `defect-trend-analysis` for a retrospective view.

## Output format
```markdown
# Test Summary Report: <product / release / level>
**Recommendation:** <release / with conditions / do not release / continue> – <one-line reason>

## Scope
- Tested: <build, environments, levels, types, period>
- Not tested / partial: <item – reason>

## Execution Results
| Planned | Executed | Passed | Failed | Blocked | Not run |
|---|---|---|---|---|---|

## Coverage
| Requirement / risk area | Coverage | Result | Note |
|---|---|---|---|

## Defects
| Severity | Found | Fixed | Open | Blockers |
|---|---|---|---|---|
Notable open defects: ...

## Exit Criteria
| Criterion | Status | Evidence |
|---|---|---|

## Deviations from Plan
- ...

## Residual Risk and Mitigations
- ...

## Conditions and Next Steps
- <condition> – <owner> – <due>
```

## Quality checklist
- [ ] The recommendation is stated first and is consistent with the exit criteria status.
- [ ] Not-tested areas are listed explicitly with reasons.
- [ ] Every percentage shows its denominator and comes from given numbers.
- [ ] Residual risk is written in business terms with mitigations.
- [ ] Facts and the tester's judgment are clearly separated; unknowns are `[UNKNOWN]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting a high pass rate while blocked and not-run tests hide untested risk. Show all states.
- Omitting descoped test types (performance, security, accessibility). Their absence is residual risk, not a footnote.
- A recommendation that contradicts the data to please the schedule. Say "release with conditions" and list them instead.

## Example
Input: "Release 3.4: 412 cases, 389 passed, 11 failed, 12 blocked, 7 open bugs (1 critical), performance test not run."

Excerpt of output:
**Recommendation:** Do not release until the critical defect is fixed and verified; otherwise release with conditions.
| Planned | Executed | Passed | Failed | Blocked | Not run |
|---|---|---|---|---|---|
| 412 | 400 | 389 (97.3% of executed) | 11 | 12 | `[UNKNOWN]` |

- Not tested: Performance testing – not run `[UNKNOWN: reason]`. Residual risk: peak-hour response times unverified; mitigation: enhanced monitoring and rollback plan ready.
