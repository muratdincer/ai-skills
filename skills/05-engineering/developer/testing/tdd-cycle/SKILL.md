---
name: tdd-cycle
description: "Drives a behavior into code with strict red-green-refactor cycles: a test list ordered from simplest to hardest, one failing test at a time that is seen failing for the right reason, the minimal code to pass, and refactoring only on green, with no production code written without a failing test. Use when someone wants to build a feature, function or bug fix test-first, asks for TDD steps, or wants to practice or demonstrate TDD on a concrete behavior."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: testing
  title: "Drive code with TDD"
  related: "unit-test-writing, implement-from-story, refactoring, acceptance-criteria, test-gap-finder"
  prompt: "Let's build a password strength validator with TDD: min 12 chars, at least one digit and one symbol, and it must reject the user's email."
---

# Drive Code With TDD

## Purpose
Grow working, fully tested code in small verified steps, so that every line of production code exists because a test demanded it and the design emerges from how the code is used rather than from speculation.

## When to use
- A new behavior, function or class is about to be written and its expected behavior can be stated.
- A bug must be fixed: start with a failing test that reproduces it.
- A team wants a worked TDD sequence for a concrete behavior (pairing, kata, teaching).

## When not to use
- The code already exists and only needs tests. Use `unit-test-writing`.
- The behavior itself is unknown and must be explored first; spike, then use `spike-report` and restart with TDD.
- A larger story needs planning across components. Use `implement-from-story`, which can apply this skill per task.

## Inputs
Required:
- The behavior to build, as rules, examples or acceptance criteria.

Optional, improves quality:
- Language and test framework, existing code the behavior plugs into, coding conventions.

If the behavior is too vague to write a first failing test, ask one focused question at a time (at most 5 in a batch) about the rule. Treat any rule you fill in yourself as `[ASSUMPTION]` and list it before the first cycle.

## Process
1. Write a test list: concrete examples of the behavior, from the simplest degenerate case (empty, null, zero) through the core rule to edge and error cases. Mark examples you inferred as `[ASSUMPTION]`. The list is a living backlog; add new ideas to it instead of coding them.
2. Red: pick the next example that teaches the most with the least code. Write one test for it, using the API you wish existed, in Arrange-Act-Assert form.
3. Run it and watch it fail for the right reason: an assertion failure on the expected value, not a compile error, missing import or wrong setup. If it passes unexpectedly, the behavior already exists or the test is wrong; investigate before continuing.
4. Green: write the minimal production code to pass, including fake-it (returning a constant) when that is the simplest step. Do not add behavior no failing test demands.
5. Run all tests; all must be green. If a previous test breaks, fix the code, not the test, unless the test was wrong.
6. Refactor on green only: remove duplication between test and code, improve names, extract functions, generalize a faked constant once a second example forces it (triangulation). Tests stay green after every change; refactor test code too.
7. Repeat steps 2-6 for the next item. Keep each cycle to a few minutes of work; if a step grows large, revert to green and pick a smaller example.
8. When a bug surfaces, add a test that reproduces it first, see it fail, then fix.
9. Stop when the test list is empty and the acceptance criteria are covered; review the final design and the test names as a readable specification.
10. Report the cycle log, the final code and tests, and the assumptions made.
11. If the goal continues, suggest `test-gap-finder` to probe for missed cases, `refactoring` for larger structural cleanup, or `implement-from-story` to continue the surrounding story.

## Output format
```markdown
# TDD: <behavior>
Assumptions: <list or none>

## Test List
- [x] <example> → <expected>
- [ ] <example> [ASSUMPTION]

## Cycle Log
| # | Red: test | Fails because | Green: minimal change | Refactor |
|---|---|---|---|---|
| 1 | empty password rejected | returns true (stub) | `if empty return false` | – |

## Final Code
<production code>

## Final Tests
<test code>
```

## Quality checklist
- [ ] No production code was written without a failing test that required it.
- [ ] Every red step states the failure and it is the expected assertion failure, not a compile or setup error.
- [ ] Each green step is the minimal change; no speculative generality was added.
- [ ] Refactoring happened only on green and all tests stayed green.
- [ ] The test list covers degenerate, core, edge and error cases, and inferred rules are labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing several tests up front and then all the code; the feedback loop and emergent design are lost. One test at a time.
- Skipping the red check; a test that never failed may be asserting nothing. Always see it fail.
- Skipping refactoring because "it is green"; duplication piles up and the code rots in small steps.
- Starting with the hardest example; the first test should be trivial so the API and setup are validated cheaply.

## Example
Input: "Password validator: min 12 chars, at least one digit and one symbol, must not contain the user's email."

Weak cycle: one test with all four rules, then the full validator in one go.

Strong cycles (excerpt):
1. Red: `empty_password_is_rejected` fails (stub returns valid). Green: return invalid when empty.
2. Red: `11_chars_with_digit_and_symbol_is_rejected`. Green: length check `< 12`. Refactor: extract `MIN_LENGTH`.
3. Red: `12_chars_without_digit_is_rejected`. Green: digit check.
4. Red: `password_containing_email_case_insensitive_is_rejected` `[ASSUMPTION: case-insensitive; confirm with security]`.
