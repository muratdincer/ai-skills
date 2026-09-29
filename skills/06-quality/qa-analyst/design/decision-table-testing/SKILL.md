---
name: decision-table-testing
description: "Builds decision tables from business rules by listing conditions and actions, enumerating combinations, collapsing irrelevant ones and deriving one test per rule column, while exposing missing and contradictory rules. Use when behavior depends on combinations of conditions (eligibility, pricing, approvals, discounts, routing), or when someone asks to test a set of if-then rules."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: design
  title: "Build decision table tests"
  related: "equivalence-boundary-analysis, business-rules-catalog, test-case-writing, pairwise-testing, state-transition-testing"
  prompt: "Build a decision table for shipping fees: free for members over 200 TL, 29 TL standard, express +40 TL, islands add 50 TL, members get express at half price."
---

# Build Decision Table Tests

## Purpose
Make every combination of rule conditions explicit so that each distinct outcome is tested once, and so that gaps and conflicts in the rules are found before they become production defects.

## When to use
- An outcome depends on two or more conditions (customer type, amount, channel, region, flags).
- Rules are written as prose paragraphs, and people disagree on edge combinations.
- Pricing, eligibility, approval routing or fee logic changes.

## When not to use
- A single input with ranges drives the outcome. Use `equivalence-boundary-analysis`.
- Behavior depends on prior events or status. Use `state-transition-testing`.
- Many parameters are independent and just need combination coverage. Use `pairwise-testing`.

## Inputs
Required:
- The business rules (text, spec excerpt, existing rule catalog).

Optional, improves quality:
- Priority/precedence of rules, rounding rules, examples from business.
- Existing implementation behavior for comparison.

If rules are missing, ask for them. Where the rule text does not determine an outcome, mark the cell `[UNKNOWN]` and raise a question.

## Process
1. Extract conditions and make each one boolean or a small set of partitions (e.g. Amount: <200, >=200). Take partitions from boundary analysis where ranges exist.
2. Extract actions/outcomes (fee amount, approval level, message, flag set).
3. Compute the full combination count; if it is under ~32, enumerate all; otherwise group conditions or apply the limited-entry approach per sub-table.
4. Fill each column (rule) with the expected actions from the rule text; mark cells without a stated outcome `[UNKNOWN]`.
5. Identify impossible combinations (e.g. non-member AND member discount) and mark them, with reason.
6. Collapse columns whose outcome does not depend on a condition, using "-" (don't care), and verify the collapse does not hide a difference.
7. Detect anomalies: missing rules (combinations with no outcome), conflicts (two rules giving different outcomes), redundant rules.
8. Derive one test case per remaining column, with concrete data that satisfies exactly that column; add boundary values for range-based conditions.
9. Prioritize columns by business impact and frequency.
10. Output the table, the tests and a list of rule gaps for the product owner.
11. Label every inferred rule or outcome `[ASSUMPTION]`; if the user continues, suggest `test-case-writing` to turn rules into cases or `pairwise-testing` when conditions explode.

## Output format
```markdown
# Decision Table: <rule set>
| | R1 | R2 | R3 | ... |
|---|---|---|---|---|
| C1: <condition> | Y | Y | N | |
| C2: <condition> | Y | N | - | |
| A1: <action> | X | | X | |
| A2: <action / value> | | 29 TL | | |

Impossible combinations: <list and reason>
## Rule Gaps and Conflicts
| Columns | Issue | Question |
## Derived Tests
| Test | Rule column | Data | Expected |
```

## Quality checklist
- [ ] Every condition combination is either tested, marked impossible, or collapsed with "-" justified.
- [ ] Each column has exactly one expected outcome or is flagged `[UNKNOWN]`.
- [ ] Conflicts and gaps are listed as questions, not silently resolved.
- [ ] Test data satisfies the column precisely, including boundary values for ranges.
- [ ] Rule precedence (which rule wins) is stated or questioned.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Collapsing columns too early and missing an interaction (e.g. express + island + member).
- Encoding ranges as boolean without boundary tests at the thresholds.
- Resolving ambiguous rules yourself. Present the options and ask the rule owner.

## Example
Input: "Free shipping for members over 200 TL, standard 29 TL, express +40 TL, islands +50 TL, members get express at half price."

Excerpt of output:
| C1 Member | Y | Y | N | N |
| C2 Basket >= 200 | Y | Y | Y | N |
| C3 Express | N | Y | Y | N |
| A Fee | 0 | 20 | 69 | 29 |
- Gap: Does the island surcharge apply to free-shipping orders? `[UNKNOWN]`
- Question: Is "express at half price" 20 TL on top of free shipping, or half of 69 TL?
