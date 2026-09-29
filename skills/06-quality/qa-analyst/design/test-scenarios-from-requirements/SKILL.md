---
description: "Derives high-level test scenarios (positive, negative, edge, permission, integration and non-functional) from requirements, user stories, use cases or acceptance criteria, with traceability to the source and a priority for each. Use when test design starts for a feature, when checking coverage of a story, or when someone asks what should be tested for a requirement."
related: test-case-writing, testability-review, equivalence-boundary-analysis, traceability-matrix, bdd-feature-file
prompt: "Derive test scenarios for this story: a customer can cancel an order until it is shipped and gets a refund to the original payment method."
---

# Derive Test Scenarios

## Purpose
Produce a complete, traceable list of what must be verified for a requirement, at scenario level, before detailed test cases are written. Scenarios make coverage gaps visible and are cheap to review with the product owner.

## When to use
- A story, use case or requirement set is ready for test design.
- The team wants to review coverage with business before writing detailed cases.
- Acceptance criteria exist but only describe the happy path.

## When not to use
- You need step-by-step cases with data and expected results. Use `test-case-writing`.
- The requirements are still vague. Run `testability-review` first.
- You need executable Gherkin. Use `bdd-feature-file`.

## Inputs
Required:
- The requirement, story, use case or acceptance criteria.

Optional, improves quality:
- Business rules, UI designs, API contracts, roles and permissions, related NFRs.
- Known defects or incidents in this area.

If the requirement is missing, ask for it. Unclear behavior becomes an open question, not an invented expectation.

## Process
1. Extract testable conditions: each business rule, input, state, role, output and integration mentioned or implied.
2. Write the main success scenario(s) covering each acceptance criterion at least once.
3. Add alternative flows: valid variations (different payment types, optional fields, other roles).
4. Add negative scenarios: invalid input, rule violations, unauthorized access, wrong state (e.g. action after a deadline or status change).
5. Add edge scenarios using boundaries, empty/max values, time (cut-off times, time zones, month end), concurrency (two users, double submit), idempotency.
6. Add integration scenarios: downstream failure, timeout, partial success, retries, message duplication.
7. Add relevant non-functional scenarios: audit log, notifications, accessibility of new UI, performance of heavy operations, data privacy.
8. Give each scenario an ID, source reference (criterion, rule) and priority (High/Medium/Low from risk).
9. Check coverage: every acceptance criterion and business rule maps to at least one scenario; list uncovered items.
10. List open questions where expected behavior is not defined.

## Output format
```markdown
# Test Scenarios: <feature / story ID>
| ID | Scenario | Type | Source | Priority |
|---|---|---|---|---|
| TS-01 | <Verify that ... when ...> | Positive / Negative / Edge / Permission / Integration / NFR | AC-1, BR-2 | H |

## Coverage
| Source item | Scenarios |
Uncovered: <items or "none">

## Open Questions
1. <undefined behavior> — <scenario affected>
```

## Quality checklist
- [ ] Every acceptance criterion and business rule is covered by at least one scenario.
- [ ] Negative and edge scenarios outnumber or at least equal happy-path scenarios for high-risk features.
- [ ] Each scenario states a single intent and a condition, not steps.
- [ ] No expected behavior is invented; unclear ones are open questions.
- [ ] Priorities reflect risk, not order of appearance.

## Common pitfalls
- Writing test cases instead of scenarios. Keep it to one line of intent; details belong in `test-case-writing`.
- Covering only UI paths. Include state changes, integrations and asynchronous effects (emails, refunds, events).
- Forgetting time-dependent rules such as cut-offs and status transitions.

## Example
Input: "Customer can cancel an order until it is shipped; refund to original payment method."

Excerpt of output:
| TS-01 | Cancel an unshipped card-paid order → order cancelled, full refund to card | Positive | AC-1 | H |
| TS-04 | Cancel an order already shipped → cancel rejected with message | Negative | AC-1 | H |
| TS-07 | Cancel while shipment status changes at the same moment | Edge | AC-1 | M |
| TS-09 | Refund provider times out → order state and retry behavior | Integration | AC-2 | H |
- Open question: Partially shipped orders: cancel remaining items or reject?
