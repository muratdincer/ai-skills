---
name: integration-test-writing
description: "Writes integration tests that exercise code across real boundaries (database, message broker, HTTP APIs, file storage, cache) with disposable real dependencies where feasible and test doubles only for systems the team does not own, covering mapping, transactions, serialization, error and timeout behavior, with isolated data and deterministic setup. Use when someone asks for integration tests, wants to verify a repository, API endpoint, consumer or external client against real infrastructure, or when unit tests with mocks cannot prove the behavior."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: testing
  title: "Write integration tests"
  related: "unit-test-writing, api-test-design, test-data-design, flaky-test-analysis, test-gap-finder"
  prompt: "Write integration tests for our OrderRepository and the OrderPlaced consumer; we use a relational database and a message broker."
---

# Write Integration Tests

## Purpose
Prove that components work together across real boundaries (queries, mappings, transactions, serialization, protocol and error behavior) that unit tests with mocks cannot verify, while keeping the tests reliable enough to run on every change.

## When to use
- Data access code, ORM mappings, migrations or queries need verification against a real database engine.
- An API endpoint, message consumer/producer or external client must be tested end to end within one service.
- A bug slipped through mocked unit tests because the real dependency behaved differently.

## When not to use
- The logic can be verified in isolation without infrastructure. Use `unit-test-writing`.
- The goal is a test design for an API from the consumer's side (status codes, auth matrix). Use `api-test-design`.
- Existing integration tests fail intermittently. Use `flaky-test-analysis`.

## Inputs
Required:
- The component(s) to test and the boundaries they cross (which database, broker, APIs).

Optional, improves quality:
- Code of the component and its configuration; existing test infrastructure (containers, in-memory substitutes, shared fixtures).
- Contracts (API spec, message schema), expected transactional and retry behavior, CI constraints (time budget, container support).

If the boundaries are not stated, derive them from the code and mark them `[ASSUMPTION]`. If the test infrastructure is unknown, propose disposable real dependencies and list it as an open question.

## Process
1. Define the test boundary: which components are real (the service, its database, broker) and which are replaced (third-party systems not owned by the team). State why for each replacement.
2. Choose realistic dependencies: prefer the same engine and major version as production in a disposable instance over in-memory substitutes whose dialect, locking or constraint behavior differs; mark any divergence as a known limitation.
3. List the integration risks per boundary: mapping and column types, null and default handling, constraints and unique violations, transactions and rollback, isolation and concurrent writes, serialization and schema evolution, pagination and ordering, time zones and precision, timeouts, retries, idempotency, poison messages.
4. Turn each risk into a scenario with a clear observable outcome (row state, response, published message, dead-letter entry); separate stated requirements from behavior inferred from code and label the latter `[ASSUMPTION]`.
5. Design data isolation: each test creates its own data with unique keys, or runs inside a rolled-back transaction when the code does not manage transactions itself; never depend on data left by other tests or on seed order.
6. Replace external systems with stubbed HTTP servers or contract-based fakes that can return errors, delays and malformed payloads; verify the request the service sent where it is part of the behavior.
7. Handle asynchrony without sleeps: poll with a timeout for the expected state or message, and fail with a message that shows the last observed state.
8. Write each test as Arrange-Act-Assert through the component's real entry point (repository method, HTTP call, published message), asserting on persisted state or emitted output, not on internal calls.
9. Control cost: share expensive infrastructure per test run, reset state between tests, tag integration tests so they can run separately, and keep the suite within the stated CI time budget.
10. Verify each test can fail: break a mapping, constraint or handler and confirm the test turns red with a clear message.
11. Report covered risks, known limitations of the environment and open questions.
12. If the goal continues, suggest `test-data-design` for richer datasets, `api-test-design` for consumer-facing API coverage or `test-gap-finder` to find remaining untested paths.

## Output format
```markdown
# Integration Tests: <component>
Real: <service, DB engine/version, broker> · Replaced: <system → stub/fake, reason> · Assumptions: <list or none>

## Risk Coverage
| # | Boundary | Risk | Scenario | Test |
|---|---|---|---|---|
| R1 | DB | Unique violation on duplicate order number | Insert same number twice → domain error, no partial row | <test name> |

## Setup and Isolation
<infrastructure lifecycle, data strategy, reset approach>

## Tests
<test code, grouped by boundary>

## Known Limitations and Open Questions
- ...
```

## Quality checklist
- [ ] Each replaced dependency is a system the team does not own, and the reason is stated.
- [ ] Database and broker behavior is tested on the production engine or the divergence is listed.
- [ ] Tests are isolated: no shared mutable data, no order dependence, no fixed sleeps.
- [ ] Error paths are covered: constraint violations, timeouts, malformed payloads, retries or dead letters.
- [ ] Assertions check persisted state or emitted output, and each test was shown to fail for the right reason.
- [ ] Inferred behavior and boundaries are labeled `[ASSUMPTION]`; environment gaps are listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using an in-memory database with a different dialect; tests pass while production queries fail on locking, collation or types. Use the real engine or document the gap.
- Mocking the database in "integration" tests; that is a unit test with extra setup and proves nothing about the boundary.
- `sleep(5)` for asynchronous consumers; it is slow and still flaky. Poll for the expected state with a timeout.

## Example
Input: "Test OrderRepository and the OrderPlaced consumer that reserves stock."

Excerpt of output:
- Real: service, relational DB in a disposable container (same major version as production `[ASSUMPTION]`), broker container. Replaced: payment provider → HTTP stub.
- R3 (broker): Same OrderPlaced message delivered twice → stock reserved once (idempotency key on message id). Poll for reservation row, max 10 s.
- R5 (broker): Malformed payload → message ends in dead-letter queue, no reservation, error logged with message id.
- Limitation: Isolation level in tests matches production only if the connection string sets it `[open question: owner of DB config]`.
