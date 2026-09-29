---
name: test-case-writing
description: "Writes detailed, executable test cases with ID, title, preconditions, test data, numbered steps, expected results per step, priority and traceability to requirements. Use when scenarios need to become repeatable manual cases, when preparing cases for execution or automation, or when someone asks to write test cases for a feature or story."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: design
  title: "Write test cases"
  related: "test-scenarios-from-requirements, equivalence-boundary-analysis, test-data-design, test-automation-script, traceability-matrix"
  prompt: "Write test cases for the password reset flow: email link valid for 30 minutes, new password must meet the policy, old sessions are logged out."
---

# Write Test Cases

## Purpose
Turn scenarios into unambiguous, repeatable test cases that any tester (or an automation engineer) can execute and get the same pass/fail verdict, with clear links back to requirements.

## When to use
- Scenarios are agreed and need detailed steps for execution.
- A regression suite, UAT pack or automation backlog needs well-formed cases.
- Existing cases are vague ("check that it works") and must be rewritten.

## When not to use
- You only need the list of what to test. Use `test-scenarios-from-requirements`.
- You need Gherkin for a BDD toolchain. Use `bdd-feature-file`.
- You need unstructured exploration of an area. Use `exploratory-test-charter`.

## Inputs
Required:
- The requirement, story or scenarios to cover.

Optional, improves quality:
- UI screens or API contract, field rules, roles, environment details.
- Team's test case template or mandatory fields; test management conventions.

If there is nothing to derive cases from, ask for it. Unknown field rules become `[UNKNOWN]` in expected results and open questions.

## Process
1. List the scenarios to cover; if none are given, derive them briefly first (positive, negative, edge).
2. Apply design techniques where inputs have ranges or rules: equivalence classes and boundaries, decision tables, state transitions.
3. For each case write a title in the form "<action> <condition> <expected outcome>" so it is readable in a list.
4. State preconditions: user/role, system state, feature flags, required existing data.
5. Specify concrete test data values (not "valid email") or reference a named dataset. Use synthetic or masked data only.
6. Write steps as single, observable user or system actions, one per line, starting with a verb.
7. Write an expected result for every step that has a verifiable outcome; include messages, state changes, persisted data, side effects (email, audit log, event).
8. Add postconditions or cleanup when the case changes shared data.
9. Set priority (from risk), type (functional, negative, boundary...), and traceability (requirement/criterion IDs).
10. Mark automation suitability (Yes / Later / No with reason).
11. Review for independence: each case should run on its own without relying on the result of another.
12. Label inferred expected results `[ASSUMPTION]`; if the user continues, suggest `test-automation-script` for cases marked Yes or `traceability-matrix` to link cases to requirements.

## Output format
```markdown
### TC-<nnn>: <title>
| Field | Value |
|---|---|
| Traces to | <REQ / AC IDs> |
| Priority / Type | <H/M/L> / <type> |
| Preconditions | <role, state, data> |
| Test data | <concrete values or dataset name> |
| Automation | <Yes / Later / No – reason> |

| # | Step | Expected result |
|---|---|---|
| 1 | <verb + action> | <observable outcome> |

Postconditions / cleanup: <...>
```

## Quality checklist
- [ ] Each case verifies one intent and has a clear pass/fail decision.
- [ ] Expected results are specific (exact message, value, state), never "works correctly".
- [ ] Test data is concrete and contains no real personal data.
- [ ] Negative and boundary cases are present, not only happy paths.
- [ ] Every case traces to at least one requirement or criterion.
- [ ] Cases are independent and state their preconditions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Combining many checks in one long case. Split so a failure pinpoints the problem.
- Hard-coding data that expires (dates, tokens). Use relative data ("today + 31 days") or setup steps.
- Omitting side-effect checks such as notifications, audit records or downstream messages.

## Example
Input: "Password reset: link valid 30 minutes, policy-compliant new password, old sessions logged out."

Excerpt of output:
### TC-004: Reset link used after 30 minutes is rejected
| Preconditions | Active user `qa.user01`, reset requested at T0 |
| Test data | Link generated at T0; system clock or wait to T0 + 30 min + 1 s |

| 1 | Open the reset link at T0 + 30:01 | "This link has expired" message shown; no password field `[UNKNOWN: exact text]` |
| 2 | Try to log in with old password | Login succeeds (password unchanged) |
