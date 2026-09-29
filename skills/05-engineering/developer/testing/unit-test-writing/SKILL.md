---
description: "Writes unit tests in Arrange-Act-Assert form that pin down observable behavior of a function, class or module, covering the happy path, equivalence classes, boundaries, error paths and state transitions, with test doubles only at true boundaries and names that read as specifications. Use when someone asks to write, add or improve unit tests, increase coverage of specific code, or secure code before a change."
related: "tdd-cycle, test-gap-finder, integration-test-writing, equivalence-boundary-analysis, refactoring"
prompt: "Write unit tests for this ShippingCostCalculator class; it has rules for weight tiers, free shipping over a threshold and express surcharge."
---

# Write Unit Tests

## Purpose
Produce fast, deterministic unit tests that specify what the code does from the caller's point of view, so regressions fail loudly with a clear message and the code can be refactored without rewriting the tests.

## When to use
- New or existing code needs tests for its behavior, rules and edge cases.
- A change or refactoring is planned and the current behavior must be secured first.
- A bug was fixed and needs a regression test that fails without the fix.

## When not to use
- The behavior crosses real infrastructure (database, broker, HTTP). Use `integration-test-writing`.
- The code does not exist yet and should be driven by tests. Use `tdd-cycle`.
- The question is which paths are untested, not writing the tests. Use `test-gap-finder`.

## Inputs
Required:
- The code under test (or its signature and specified behavior).

Optional, improves quality:
- Language, test framework and mocking library in use; existing test conventions and helpers.
- Requirements or acceptance criteria; known bugs; coverage report.

If the code is missing, ask for it. If the framework is not stated, infer it from the code's language and ecosystem and mark it `[ASSUMPTION]`; follow existing test style when examples are given.

## Process
1. Identify the unit's public contract: inputs, outputs, thrown errors, observable state changes and calls to collaborators that are part of the contract (e.g., "publishes event"). Do not test private methods directly.
2. List behaviors, not methods: one line per rule ("orders over the free-shipping threshold pay zero"). Separate stated requirements from behavior inferred from the code and label the latter `[ASSUMPTION]`; if the code looks wrong, record it as a suspected bug instead of asserting it.
3. Derive cases per behavior: typical value, equivalence classes, boundaries (min, max, just below/above, empty, null, zero, negative, maximum length), invalid inputs, error paths, and state sequences for stateful units.
4. Decide on test doubles: replace only non-deterministic or slow boundaries (clock, random, network, file system, external services). Prefer fakes or stubs for queries and mocks only for commands whose call is the behavior; never mock the unit itself or value objects.
5. Make tests deterministic: inject clock, random seed, time zone, locale and culture; no sleeps, no shared mutable state, no dependence on test order.
6. Write each test in Arrange-Act-Assert with one behavior per test and a single Act. Name it as a specification (`<condition>_<expected result>` or a sentence) following the project convention.
7. Use data-driven (parameterized) tests for the same rule across many inputs; keep one test per distinct rule so failures point at the rule.
8. Assert on outcomes precisely: exact values, exception type and relevant message part, emitted events; avoid asserting incidental details (log text, call counts that are not part of the contract).
9. Check each test can fail: mentally (or actually) break the code or invert the expected value and confirm the test goes red with a readable message. A regression test must be seen failing on the unfixed code, for the reason the bug describes.
10. Keep test code clean: builders or factory helpers for complex setup, no logic (loops, conditionals) in test bodies, no copy-pasted arrange blocks beyond three repetitions.
11. Report which behaviors are covered, which cases were deliberately left out and any suspected bugs found.
12. If the goal continues, suggest `test-gap-finder` to look for remaining untested branches, `integration-test-writing` for boundary behavior, or `refactoring` now that behavior is secured.

## Output format
```markdown
# Unit Tests: <unit>
Framework: <framework> · Doubles: <which collaborators and why> · Assumptions: <list or none>

## Behavior Map
| # | Behavior | Source (requirement / inferred) | Test(s) |
|---|---|---|---|
| B1 | <rule> | <AC id or [ASSUMPTION]> | <test name> |

## Tests
<test code, grouped by behavior>

## Not Covered and Why
- <case> — <reason: needs integration test / out of scope / unclear rule>

## Suspected Bugs
- <input> → <actual> vs <expected per rule> — [ASSUMPTION until confirmed]
```

## Quality checklist
- [ ] Every test verifies one behavior through the public contract and has a single Act.
- [ ] Boundaries, invalid inputs and error paths are covered, not only the happy path.
- [ ] Tests are deterministic: no real clock, random, network, file system or order dependence.
- [ ] Mocks are used only where the interaction itself is the behavior.
- [ ] Each test can fail for the right reason and its name states the expected behavior.
- [ ] Inferred behavior is labeled `[ASSUMPTION]`; suspected bugs are reported, not locked in by assertions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Testing the implementation: asserting call sequences on mocks makes every refactoring break the tests. Assert outcomes instead.
- Cementing bugs: writing expectations by running the code and copying its output. Derive expectations from the rule.
- One giant test per method with many asserts; the first failure hides the rest. Split per behavior.

## Example
Input: "ShippingCostCalculator: tiers 0-1 kg = 5, 1-5 kg = 9, >5 kg = 15; free over 100; express +10."

Weak test:
```
test_calculate() { assert calc.cost(order(2kg, 50)) == 9; assert calc.cost(order(2kg, 150)) == 0 }
```
Strong tests (excerpt):
- `weight_exactly_1kg_uses_first_tier` → 5 (boundary; tier edge inclusivity `[ASSUMPTION]`, open question to product owner).
- `order_total_exactly_100_is_not_free` → 9 (rule says "over 100").
- `express_on_free_shipping_order_charges_only_surcharge` → 10 `[ASSUMPTION]`: code returns 0, flagged as suspected bug.
- `negative_weight_throws_InvalidWeight`.
