---
description: "Refactors code safely by identifying the smells that matter for the next change, securing behavior with characterization tests, and applying named refactorings (Extract Function, Replace Conditional with Polymorphism, Introduce Parameter Object, etc.) in small behavior-preserving steps. Use when code is hard to change, before adding a feature to messy code, or when someone asks to clean up, restructure or refactor code without changing behavior."
related: "clean-code-review, legacy-code-comprehension, unit-test-writing, tech-debt-assessment, code-review"
prompt: "Refactor this 200-line calculatePrice method; I need to add a new discount type next sprint and every change here breaks something."
---

# Refactor Code

## Purpose
Improve the internal structure of code without changing its observable behavior, so that the next change becomes cheap and safe, and do it in steps small enough to verify and review.

## When to use
- A feature or fix is blocked by code that is hard to understand or change ("make the change easy, then make the easy change").
- Review or analysis found smells worth fixing in actively changing code.
- Duplicated logic must be consolidated before it diverges further.

## When not to use
- Only an assessment of problems is needed, no changes. Use `clean-code-review` or `tech-debt-assessment`.
- The code is not yet understood. Use `legacy-code-comprehension` first.
- The goal is speed, not structure. Use `performance-optimization`.

## Inputs
Required:
- The code to refactor and the reason (the upcoming change or the pain it causes).

Optional, improves quality:
- Existing tests, coding standards, language/framework version, constraints (public API must not change, no new dependencies).

If there are no tests and none can be run, say so and start with characterization tests; never claim behavior is preserved without evidence.

## Process
1. State the goal in terms of the next change ("adding a discount type should touch one class").
2. Identify the smells that block that goal (long function, duplicated conditional, feature envy, primitive obsession, shotgun surgery); ignore cosmetic ones.
3. Check the safety net: which behaviors are covered by tests? Add characterization tests for uncovered paths, including odd current behavior (record it, do not fix it now).
4. Choose named refactorings from the catalog vocabulary and order them from low risk (rename, extract variable, extract function) to structural (move function, replace conditional with polymorphism, split phase).
5. Apply one refactoring per step; after each step the code compiles and tests pass. Keep behavior changes and bug fixes out of refactoring commits.
6. Keep public contracts stable unless agreed; when a signature must change, use a parallel change (add new, migrate callers, remove old).
7. Watch for semantic traps: evaluation order, side effects in moved code, null/empty handling, exception types, floating-point or rounding differences, thread safety of extracted state.
8. After the sequence, compare before/after against the goal and remove scaffolding.
9. Report each step with its refactoring name, suggested commit boundary and any behavior quirk discovered.

## Output format
```markdown
# Refactoring: <unit>
Goal: <what the next change should look like>
Safety net: <existing tests / added characterization tests>

## Smells Addressed
| Smell | Location | Why it blocks the goal |

## Steps
| # | Refactoring | Change | Tests green? |
|---|---|---|---|
| 1 | Extract Function | `applySeasonalDiscount` from lines .. | Yes |

## Result
<final code or diff>

## Discovered Behavior Quirks (not changed)
- ...
```

## Quality checklist
- [ ] Observable behavior is unchanged, backed by tests that ran before and after.
- [ ] Each step is a named refactoring small enough to review in isolation.
- [ ] No bug fixes or features are mixed in; quirks are reported separately.
- [ ] Public API is unchanged or changed via parallel change.
- [ ] The result demonstrably makes the stated next change easier.

## Common pitfalls
- "Big bang" rewrite labeled as refactoring. If it cannot be done in green steps, it is a rewrite and needs its own plan.
- Refactoring code nobody will change again. Prioritize by change frequency and upcoming work.
- Silently "fixing" odd behavior during extraction; callers may depend on it. Record it and fix in a separate change.

## Example
Input: "calculatePrice has nested if/else for customer type and discount type; adding a new discount breaks things."

Excerpt of output:
1. Characterization tests: 12 combinations of customer type × discount type, including the current rounding of half cents (quirk recorded).
2. Split Phase: separate "determine applicable discounts" from "apply discounts to price".
3. Replace Conditional with Polymorphism: `Discount` interface with one implementation per type; new type = new class + registration.
