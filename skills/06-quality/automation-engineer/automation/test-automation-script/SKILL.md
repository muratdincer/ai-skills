---
name: test-automation-script
description: "Writes a maintainable automated test in the team's language and framework using page objects or API clients, independent test data, explicit condition-based waits and precise assertions, and first shows the test failing for the right reason. Use when a manual test case, scenario or Gherkin step must become automated test code, when someone asks for a UI or API test to be written, or when an existing automated test needs to be rewritten to be reliable."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: automation-engineer
  area: automation
  title: "Write an automated test"
  related: "automation-candidate-selection, automation-framework-design, test-case-writing, bdd-feature-file, flaky-test-analysis"
  prompt: "Automate this test case as an API test in our TypeScript suite: creating an order with an expired coupon must return 422 and not reserve stock."
---

# Write an Automated Test

## Purpose
Produce automated test code that fails only when the behavior is broken, explains itself when it fails, and survives UI and data changes, so the suite stays trusted and cheap to maintain.

## When to use
- A test case, scenario or feature file step has been selected for automation.
- A new UI journey or API endpoint needs an automated check at the agreed level.
- An existing automated test is unreadable or brittle and must be rewritten.

## When not to use
- You still need to decide what is worth automating. Use `automation-candidate-selection`.
- The suite has no structure yet (layers, runners, reporting). Use `automation-framework-design`.
- You are writing developer-level unit tests next to production code. Use `unit-test-writing`.

## Inputs
Required:
- The behavior to test (test case, scenario, story or Gherkin) with the expected result.
- The test level (UI or API) and the language/framework the suite uses.

Optional, improves quality:
- Existing page objects, API clients, fixtures, helpers and naming conventions.
- Selectors or API contract, authentication approach, test data setup mechanisms, CI constraints.

If the behavior, expected result or framework is missing, ask for it (at most 3 questions in one batch). Do not invent selectors, endpoints or field names; write them as clearly marked placeholders `[TBD]` and list them as open questions.

## Process
1. Restate the behavior as one test intention: "Given <state>, when <action>, then <observable outcome>". If there is more than one When or Then, split into separate tests.
2. Reuse existing page objects, API clients and fixtures; add only the missing methods, expressed as user or business actions (`checkout.applyCoupon(code)`), not raw clicks.
3. Arrange data independently: create what the test needs through API or fixtures with unique identifiers, never depend on another test or shared mutable records. Plan cleanup or isolation.
4. Choose robust locators or contract fields: dedicated test IDs or accessible roles/labels for UI; schema fields and status codes for API. Avoid positional or styling-based selectors.
5. Replace fixed sleeps with waits on explicit conditions (element state, response received, event observed) with a bounded timeout.
6. Write assertions on business-visible outcomes and side effects (status, body fields, persisted state, emitted event), with messages that state what was expected. Assert the negative side effect as well where it matters (stock not reserved).
7. Show the test failing for the right reason first: against a known-broken build, a temporarily inverted expectation, or a mutated input; confirm the failure message points at the behavior, not at setup.
8. Make it pass against the correct build and run it repeatedly (and in parallel if the suite does) to confirm determinism.
9. Tag the test (level, feature, risk) and link it to the requirement or test case ID for traceability.
10. List placeholders, assumptions and enabling work (missing test IDs, data seeding endpoints); if the user continues, suggest `flaky-test-analysis` if it is unstable or `automation-framework-design` if shared helpers are missing.

## Output format
````markdown
# Automated Test: <test name>
- Intention: Given ..., when ..., then ...
- Level: UI | API · Traces to: <requirement/test case ID>
- Tags: ...

## Code
```<language>
<test code + any new page object / API client methods>
```

## Data and Isolation
- Setup: ... · Cleanup: ...

## Verified Failure
- How it was made to fail: ... · Failure message: ...

## Placeholders and Open Questions
- [TBD] <selector/endpoint/field> — who can confirm
- [ASSUMPTION] ...
````

## Quality checklist
- [ ] One behavior per test; the name states the behavior and expected outcome.
- [ ] No fixed sleeps; all waits are on explicit conditions with bounded timeouts.
- [ ] Test data is created independently and does not rely on test order.
- [ ] Assertions check business-visible outcomes and relevant negative side effects, with clear messages.
- [ ] The test was shown to fail for the right reason before being declared passing.
- [ ] No invented selectors, endpoints or credentials; secrets come from configuration, not code.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asserting only that "no error occurred". A test that cannot fail proves nothing; assert the specific outcome.
- Chaining tests (test B uses the order created in test A). It breaks parallel runs and hides the real failure.
- Putting locators and waits inside the test body. Keep them in page objects so a UI change is fixed once.

## Example
Input: "Order with expired coupon must return 422 and not reserve stock" — API level, TypeScript.

Weak: `await post('/orders', body); expect(res.ok).toBe(false);` — any failure (auth, 500) passes.

Strong excerpt:
```ts
test('rejects order with expired coupon and reserves no stock', async ({ api, data }) => {
  const product = await data.createProduct({ stock: 5 });
  const coupon = await data.createCoupon({ expiresAt: daysAgo(1) });
  const res = await api.orders.create({ productId: product.id, qty: 1, coupon: coupon.code });
  expect(res.status, 'expired coupon should be a validation error').toBe(422);
  expect(res.body.errors[0].field).toBe('coupon'); // [TBD] confirm error shape in contract
  expect((await api.products.get(product.id)).stock).toBe(5);
});
```
