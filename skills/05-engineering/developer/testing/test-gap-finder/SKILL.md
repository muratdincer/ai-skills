---
description: "Finds untested code paths by comparing code with its existing tests: enumerates branches, boundaries, error handlers, state transitions and requirement rules, maps each to covering tests, flags gaps and weak tests (no assertion, over-mocked, happy-path only), and ranks them by risk with a concrete test to add. Use when someone asks what is missing from the tests, wants to raise coverage meaningfully, reviews a pull request's tests, or has a coverage report and needs to know which gaps matter."
related: "unit-test-writing, integration-test-writing, code-review, regression-selection, risk-based-testing"
prompt: "Here is our InvoiceService and its test class. Which paths are not tested and which gaps matter most?"
---

# Find Untested Code Paths

## Purpose
Show precisely which behaviors of a piece of code are not protected by tests, and which existing tests give false confidence, ranked by risk, so the team adds the few tests that matter instead of chasing a coverage percentage.

## When to use
- A pull request adds or changes code and the tests need a sufficiency check.
- A coverage report exists but the team does not know which uncovered lines matter.
- Code is about to be refactored or is a frequent source of bugs.

## When not to use
- The tests should be written right away for a known behavior. Use `unit-test-writing` or `integration-test-writing`.
- The question is which existing tests to run for a change. Use `regression-selection`.
- A full review of the change (design, security, readability) is needed. Use `code-review`.

## Inputs
Required:
- The code under analysis and its existing tests (or a statement that there are none).

Optional, improves quality:
- Requirements or acceptance criteria, a line/branch coverage report, bug history, change frequency, known critical paths.

If the tests are not provided, ask for them; without them, list candidate tests but state that coverage status is `[UNKNOWN]`. Coverage percentages are never inferred from code reading.

## Process
1. Enumerate the behaviors the code must show: from requirements where given, and from the code itself (each branch, loop boundary, guard clause, catch block, early return, state transition, configuration switch). Label code-derived behaviors `[ASSUMPTION]` about intent.
2. List hidden paths that line coverage misses: short-circuit conditions (`a && b` with each operand deciding), default and fall-through cases, null/empty collections, exceptions thrown by collaborators, retries and timeouts, concurrency and ordering, time-dependent logic (month end, leap day, time zone, DST).
3. Map each behavior to the existing tests that exercise it and actually assert its outcome. A test that executes a path without asserting on it does not cover it.
4. Assess existing tests for false confidence: missing or trivial assertions, assertions on mocks instead of outcomes, expectations copied from output, disabled or skipped tests, shared state, only happy-path inputs.
5. Classify each behavior: COVERED, WEAK (executed but not properly asserted, or only one side of a boundary) or GAP (not exercised), with evidence (test name or line reference).
6. Rank gaps by risk: impact if wrong (money, data integrity, security, compliance, user-visible), likelihood (complexity, change frequency, bug history) and detectability elsewhere. Do not rank on line count.
7. For each high and medium gap, propose a concrete test: name, input, expected outcome, level (unit or integration). If the correct outcome is unclear from requirements, raise it as an open question instead of guessing.
8. Note code that is hard to test (hidden dependencies, static time, global state) and the minimal seam that would make it testable.
9. Flag dead or unreachable code found during mapping as a candidate for removal rather than for testing.
10. Summarize: counts per class, top gaps and whether the change is adequately tested for merge.
11. If the goal continues, suggest `unit-test-writing` or `integration-test-writing` to write the proposed tests, or `code-review` to include the findings in a pull request review.

## Output format
```markdown
# Test Gap Analysis: <unit or change>
Inputs: <code, tests, coverage report?, requirements?> · Assumptions: <list or none>
Summary: COVERED <n> · WEAK <n> · GAP <n> · Verdict: <adequate / add tests before merge>

## Behavior Map
| # | Behavior / path | Source | Status | Evidence | Risk |
|---|---|---|---|---|---|
| 1 | Discount capped at 50% | AC-3 | GAP | no test hits cap branch (L42) | High |

## Proposed Tests (by risk)
| # | Test name | Input | Expected | Level |

## Weak Tests
- <test> — <problem> — <fix>

## Testability Issues and Dead Code
- ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Every branch, error handler and boundary in the code appears in the behavior map.
- [ ] Each status has evidence; executed-but-unasserted paths are WEAK, not COVERED.
- [ ] Gaps are ranked by impact and likelihood, not by line count.
- [ ] Each proposed test has a concrete input and expected outcome, or an open question where the rule is unclear.
- [ ] No coverage figures or intended behaviors are invented; inferences are labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating line coverage as behavior coverage; a line hit by a test without an assertion proves nothing.
- Proposing tests for getters and trivial mappings to lift the percentage while the rounding or authorization branch stays untested.
- Writing expected values for gaps from the current code; if the code is the only source, the expectation is an assumption to confirm.

## Example
Input: `InvoiceService.calculateTotal` with discount, tax and currency rounding; tests cover one standard invoice.

Excerpt of output:
- GAP (High): discount cap at 50% branch never hit. Test `discount_above_cap_is_limited_to_50_percent`: 70% discount → 50% applied.
- WEAK (High): `calculates_total` asserts `total != null` only. Fix: assert exact amount incl. tax.
- GAP (Medium): zero-decimal currency rounding path. Expected rounding mode `[UNKNOWN]` → open question to finance.
- Dead code: `if (items == null)` after a guard that already throws; remove instead of testing.
