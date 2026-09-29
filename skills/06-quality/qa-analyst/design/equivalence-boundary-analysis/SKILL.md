---
description: "Applies equivalence partitioning and boundary value analysis to input fields, parameters and business rules, producing valid and invalid partitions, boundary values (two- or three-value) and a minimal set of test values with expected outcomes. Use when an input has ranges, lengths, formats, dates or enumerations, or when someone asks which values to test for a field or rule."
related: test-case-writing, decision-table-testing, pairwise-testing, test-data-design, test-scenarios-from-requirements
prompt: "Apply boundary value analysis to the loan application: amount 1,000-50,000, term 6-60 months, applicant age 18-70 at loan end."
---

# Apply Equivalence and Boundary Analysis

## Purpose
Reduce an effectively infinite input space to a small, defensible set of test values that exercises each behavior class once and every edge where off-by-one and comparison errors cluster.

## When to use
- Fields or parameters have numeric ranges, lengths, formats, dates, enumerations or counts.
- Business rules contain thresholds (discount tiers, age limits, cut-off times).
- A tester needs to justify why a given set of values is sufficient.

## When not to use
- Behavior depends on combinations of several conditions. Use `decision-table-testing`.
- Many independent parameters must be combined efficiently. Use `pairwise-testing`.
- Behavior depends on history or state. Use `state-transition-testing`.

## Inputs
Required:
- The fields, parameters or rules with their stated constraints.

Optional, improves quality:
- Data types and storage limits (e.g. column length, integer size), formats, locale rules.
- Whether boundaries are inclusive or exclusive; rounding and precision rules.

If a constraint is not stated, do not assume it. List it as an open question and mark candidate values `[ASSUMPTION]`.

## Process
1. List each input with type, unit, precision and stated constraints. Note whether bounds are inclusive.
2. Identify valid partitions (one per distinct expected behavior, e.g. each discount tier) and invalid partitions (below min, above max, wrong type, wrong format, empty, null).
3. Add hidden partitions: technical limits (field length, integer overflow), special values (0, negative, whitespace, leading zeros, Unicode, decimal separator by locale), date specials (leap day, month end, DST change).
4. For each ordered partition boundary pick values: two-value method (boundary and nearest invalid neighbor) by default; three-value method (below, on, above) for high-risk rules.
5. Use the smallest meaningful step (1 for integers, 0.01 for currency, 1 second or 1 day for time) based on precision.
6. For dependent or computed boundaries (age at loan end = age now + term), derive boundaries on the computed value, not only the raw inputs.
7. Choose one representative for each non-boundary partition.
8. Assign the expected outcome to every value; for invalid values specify the exact rejection behavior if known, else `[UNKNOWN]`.
9. Combine: test valid values together where possible; test each invalid value alone so failures are attributable.
10. Output the partition table, the value table and open questions.
11. Label inferred limits `[ASSUMPTION]`; if the user continues, suggest `test-case-writing` for executable cases or `test-data-design` for the datasets.

## Output format
```markdown
# Equivalence and Boundary Analysis: <feature>
## Partitions
| Input | Partition ID | Description | Valid? | Expected behavior |
## Test Values
| TV | Input | Value | Partition | Boundary? | Expected outcome |
## Combined Test Set
| Case | Values | Expected |
## Open Questions
- <inclusive/exclusive, precision, error text>
```

## Quality checklist
- [ ] Every partition has at least one value; every ordered boundary has its boundary and neighbor values.
- [ ] Invalid values are tested one at a time.
- [ ] Step size matches the data precision.
- [ ] Computed and cross-field boundaries are considered.
- [ ] Unstated limits are questions, not assumptions presented as facts.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Testing only the requirement boundaries and ignoring technical limits (max length in the database, integer size).
- Using a step of 1 for currency or time fields with finer precision.
- Mixing several invalid values in one case, which hides which validation failed.

## Example
Input: "Amount 1,000-50,000, term 6-60 months, age 18-70 at loan end."

Excerpt of output:
| TV-1 | Amount | 999.99 | Below min | Yes | Rejected |
| TV-2 | Amount | 1,000.00 | Valid | Yes | Accepted |
| TV-3 | Amount | 50,000.00 | Valid | Yes | Accepted |
| TV-4 | Amount | 50,000.01 | Above max | Yes | Rejected |
| TV-9 | Age at end | 70 y 0 d (age 65 + 60 months) | Valid | Yes | Accepted `[ASSUMPTION: 70 inclusive]` |
- Open question: Is "age 70 at loan end" inclusive, and is age computed by exact birth date?
