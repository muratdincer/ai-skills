---
name: traceability-matrix
description: "Builds a requirements traceability matrix linking business goals and sources to requirements, design elements, test cases and releases in both directions, and reports orphans, uncovered requirements and coverage percentages. Use when an audit, regulator or customer needs proof of coverage, before a release or UAT, or when assessing which items a change affects."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "Build a traceability matrix"
  related: "requirements-gap-analysis, impact-analysis, test-scenarios-from-requirements, requirements-sign-off, release-quality-gate"
  prompt: "Build a traceability matrix from these 30 requirements and 55 test cases and show me what is not covered."
---

# Build a Traceability Matrix

## Purpose
Prove that every requirement comes from a legitimate source, is designed, built and tested, and that nothing is built or tested without a requirement. The matrix supports audits, change impact and release decisions.

## When to use
- Regulated or contractual projects needing evidence of coverage (e.g. finance, health, public sector).
- Before UAT or a release quality gate.
- When a change request arrives and affected tests and designs must be found quickly.

## When not to use
- You only need the impact of a single change. Use `impact-analysis`.
- Test cases do not exist yet and must be derived. Use `test-scenarios-from-requirements`.
- You need to find missing requirements, not coverage. Use `requirements-gap-analysis`.

## Inputs
Required:
- Requirement list with IDs.
- At least one other linked artifact set: goals/sources, designs, test cases or releases, with IDs.

Optional, improves quality:
- Existing links (e.g. test case "covers" fields, story-to-epic links).
- Test execution results and defect IDs.
- Required trace levels defined by the organization or regulator.

If IDs are missing, propose an ID scheme and ask the user to confirm before mapping.

## Process
1. Agree the trace levels: e.g. Business goal / Source → Requirement → Design element → Test case → Test result → Release. Use only the levels for which data exists; mark others `[N/A]` or `[TBD]`.
2. Normalize IDs and versions for each artifact set.
3. Use explicit links first (fields, references). Only infer a link from text similarity when necessary, and mark it `[INFERRED]` for confirmation.
4. Build forward traceability: each requirement to its design, tests, results and release.
5. Build backward traceability: each test and design element back to a requirement; each requirement back to a goal or source.
6. Identify issues: requirements without tests, tests without requirements (orphans), requirements without source, failed or not-run tests on in-scope requirements, requirements with open defects.
7. Calculate coverage: requirements with at least one test, with at least one passed test, by priority.
8. Highlight high-priority or regulatory requirements with weak coverage first.
9. State maintenance rules: who updates the matrix, when (each change request, each test cycle).
10. If the user wants to continue, suggest `impact-analysis` to use the matrix for a change, `test-scenarios-from-requirements` for uncovered requirements or `requirements-sign-off` to baseline it.

## Output format
```markdown
# Traceability Matrix: <scope> · Baseline <version> · Date <date>

## Coverage Summary
| Metric | Value |
|---|---|
| Requirements total | n |
| With ≥1 test case | n (x%) |
| With ≥1 passed test | n (x%) |
| Orphan test cases | n |
| Requirements without source | n |

## Matrix
| Req ID | Priority | Source / Goal | Design ref | Test case IDs | Last result | Open defects | Release | Status |
|---|---|---|---|---|---|---|---|---|

## Issues
| # | Type | Item | Detail | Action | Owner |
|---|---|---|---|---|---|

## Maintenance
- Update trigger: <change request / test cycle / release>
- Owner: <role>
```

## Quality checklist
- [ ] Both forward and backward directions are checked.
- [ ] Inferred links are marked `[INFERRED]` and listed for confirmation.
- [ ] Coverage percentages are computed from the matrix, not estimated.
- [ ] High-priority and regulatory requirements with gaps are listed first.
- [ ] Every issue has an action and an owner role.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Counting a requirement as covered because a test exists, even though the test never ran or failed. Report "tested" and "passed" separately.
- Linking tests to requirements only at epic level. Trace at the lowest requirement level that is verified.
- Building the matrix once and never updating it. Tie updates to change control and test cycles.

## Example
Input: REQ-01..REQ-05; TC-10 covers REQ-01, TC-11 covers REQ-01 and REQ-03, TC-12 has no reference.

Excerpt of output:
| Req ID | Priority | Source / Goal | Design ref | Test case IDs | Last result | Status |
|---|---|---|---|---|---|---|
| REQ-01 | High | BRD 3.1 | [TBD] | TC-10, TC-11 | Passed | Covered |
| REQ-02 | High | Regulation Art. 5 | [TBD] | – | – | Not covered |

Issues: REQ-02 (regulatory) has no test – create test scenario, owner QA lead; TC-12 is an orphan – link or retire.
