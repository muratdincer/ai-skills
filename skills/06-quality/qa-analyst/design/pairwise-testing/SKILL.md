---
description: "Generates a reduced set of test combinations that covers every pair of parameter values (or higher strength for critical parameters), respecting constraints between values, and explains the reduction and residual risk. Use when many parameters or configurations (browsers, devices, roles, settings, product options) combine into too many cases to test exhaustively."
related: equivalence-boundary-analysis, decision-table-testing, test-case-writing, risk-based-testing, test-data-design
prompt: "Generate pairwise combinations for checkout: 4 browsers, 3 payment methods, 2 user types, 3 delivery options, coupon yes/no. Apple Pay only on Safari."
---

# Generate Pairwise Combinations

## Purpose
Cover all two-way interactions between parameters with a fraction of the full combination count, since most interaction defects are triggered by one or two parameters, while keeping constraints valid and residual risk visible.

## When to use
- Configuration or compatibility testing across environments, devices, locales or settings.
- Features with many independent options (product configurators, search filters, feature flags).
- The exhaustive combination count exceeds the time available.

## When not to use
- Outcomes are governed by explicit rules per combination. Use `decision-table-testing`.
- A single parameter's ranges matter. Use `equivalence-boundary-analysis` first to pick values.
- Parameters are not independent but sequential (workflow). Use `state-transition-testing`.

## Inputs
Required:
- Parameters and their values.

Optional, improves quality:
- Constraints (invalid or mandatory combinations), usage share per value, known risky interactions.
- Required strength (2-way default; 3-way for critical parameter groups).

If parameters or values are missing, ask for them. If values are ranges, reduce them to partitions first.

## Process
1. List parameters and values; reduce each value set with equivalence partitioning so values are behaviorally distinct.
2. Capture constraints as explicit rules (e.g. Payment = Apple Pay ⇒ Browser = Safari; Guest ⇒ no saved card).
3. Compute the exhaustive count and the theoretical pairwise lower bound (product of the two largest value counts).
4. Construct the covering array: start with the two largest parameters as the base grid, then fill remaining parameters row by row, choosing values that cover the most uncovered pairs and satisfy constraints. For large models, state that a pairwise generator should be used and provide the model in a neutral text format.
5. Verify coverage: list every value pair and confirm it appears in at least one valid row; pairs excluded by constraints are listed as not applicable.
6. Add seeded rows: high-usage configurations (most common browser + payment) and known risky combinations, even if already pair-covered.
7. Raise strength to 3-way for parameter subsets with high risk (e.g. payment x currency x country) if capacity allows.
8. Replace "don't care" cells with the most frequently used value.
9. Report the reduction, the residual risk (untested higher-order interactions) and how to map rows to test cases.

## Output format
```markdown
# Pairwise Combinations: <feature>
Parameters: <P1 (n values), P2 (n values), ...>
Constraints: <list>
Exhaustive: <n> · Pairwise rows: <n> · Strength: 2-way (+3-way for <subset>)

| Row | P1 | P2 | P3 | ... | Note (seeded / risky) |
|---|---|---|---|---|---|

## Coverage Check
- All valid pairs covered: <Yes / list of missing>
- Pairs excluded by constraints: <list>

## Residual Risk
- <higher-order interactions not covered>
```

## Quality checklist
- [ ] Every valid value pair appears in at least one row.
- [ ] No row violates a constraint.
- [ ] High-usage and known risky combinations are included explicitly.
- [ ] Parameter values are behaviorally distinct partitions, not arbitrary samples.
- [ ] Residual risk is stated.

## Common pitfalls
- Forgetting constraints, producing rows that cannot be executed.
- Using pairwise where outcome rules are explicit; you may miss the exact rule combination.
- Treating pairwise as complete testing. It covers pairs, not every three-way interaction.

## Example
Input: "4 browsers, 3 payments, 2 user types, 3 delivery options, coupon yes/no; Apple Pay only on Safari."

Excerpt of output:
Exhaustive: 144 · Pairwise rows: 13 (lower bound 12, +1 for constraint)
| 1 | Chrome | Card | Member | Standard | Yes | seeded (top usage) |
| 5 | Safari | Apple Pay | Guest | Express | No | |
- Excluded pairs: Apple Pay with Chrome, Firefox, Edge.
