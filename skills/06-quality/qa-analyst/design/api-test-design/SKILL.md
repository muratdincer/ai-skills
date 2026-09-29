---
description: "Designs API tests per endpoint covering contract and schema, status codes, authentication and authorization, input validation, business rules, idempotency, pagination, concurrency and error format, with negative and security-oriented cases. Use when an API contract (OpenAPI, GraphQL schema, gRPC proto or informal spec) needs a test design, before automating API tests, or when reviewing whether existing API tests are sufficient."
related: api-contract, api-design-review, test-automation-script, security-requirements, integration-test-writing
prompt: "Design API tests for POST /orders and GET /orders/{id}: JWT auth, customers see only their own orders, idempotency key header, 422 on validation errors."
---

# Design API Tests

## Purpose
Produce a complete, prioritized API test design that verifies the contract, the business behavior and the security boundaries of each endpoint, ready to be automated.

## When to use
- A new or changed endpoint has a contract and needs tests before or during implementation.
- API automation is about to start and needs a case inventory.
- Consumers report integration defects and coverage of the existing API suite is in doubt.

## When not to use
- The contract itself needs review for design quality. Use `api-design-review`.
- You need the automation code. Use `test-automation-script`.
- You need a full security assessment or penetration scope. Use `pentest-scope` or `threat-model`.

## Inputs
Required:
- The API contract or specification (endpoints, methods, request/response shapes).

Optional, improves quality:
- Auth model (scopes, roles, tenants), business rules, rate limits, error format standard (e.g. RFC 9457 problem details).
- Consumer list, versioning policy, idempotency and pagination conventions, downstream dependencies.

If no contract or example exists, ask for it. Undocumented behavior becomes `[UNKNOWN]` and an open question, not an assumed status code.

## Process
1. Inventory endpoints and operations; note for each the resource, method, auth requirement, side effects and whether it is safe/idempotent by HTTP semantics.
2. Contract tests: response schema, required/optional fields, types, formats, enum values, content type, headers (caching, location, correlation ID), and backward compatibility with the previous version.
3. Functional positive tests: main success path per operation, including persisted state and emitted events or messages.
4. Input validation: missing required fields, wrong types, boundaries, overlong strings, invalid formats, unknown fields, empty body, malformed JSON; expect the documented 4xx and error body.
5. Authentication: no token, expired, malformed, wrong audience/issuer, revoked. Authorization: wrong role, wrong scope, other tenant's or user's resource (BOLA/IDOR), mass assignment of protected fields (see OWASP API Security Top 10).
6. Business rules and state: operations invalid for the current resource state, conflicts (409), not found vs forbidden distinction, precondition headers (ETag/If-Match).
7. Reliability semantics: idempotency keys and retries, duplicate submissions, concurrent updates, pagination/sorting/filtering stability, rate limiting (429 and retry headers), timeouts from dependencies.
8. Error format consistency: same structure, no stack traces or internal details, correlation ID present.
9. Prioritize each case by risk (security and data integrity first), and flag which run as smoke, per-commit and nightly.
10. Define data and environment needs: test tenants, tokens per role, dependency stubs or contract mocks.
11. List open questions for undocumented codes or rules; if the user continues, suggest `test-automation-script` to implement the suite or `api-design-review` when the contract has gaps.

## Output format
```markdown
# API Test Design: <API / version>
## Endpoint Inventory
| Endpoint | Method | Auth | Idempotent | Side effects |
|---|---|---|---|---|

## Test Cases
| ID | Endpoint | Category | Condition | Request essentials | Expected status | Expected body / effect | Priority | Suite |
|---|---|---|---|---|---|---|---|---|

Categories: Contract, Positive, Validation, AuthN, AuthZ, State/Rule, Reliability, Error format.

## Test Data and Environment
- Tokens / roles: ...
- Stubs / mocks: ...

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every endpoint has contract, positive, validation and authorization cases.
- [ ] Cross-user and cross-tenant access (BOLA) is tested for every resource ID in the path or body.
- [ ] Expected statuses come from the contract; undocumented ones are `[UNKNOWN]` and questioned.
- [ ] Idempotency, concurrency and pagination are covered where the API promises them.
- [ ] Error responses are checked for consistent structure and absence of internal details.
- [ ] Test data uses synthetic identities and tokens only.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asserting only the status code. A 200 with the wrong body or a missing event is still a failure; assert schema, values and side effects.
- Testing authorization only with "no token". Most real breaches use a valid token for someone else's resource.
- Accepting whatever the implementation returns as expected. Derive expectations from the contract; mismatches are findings.

## Example
Input: "POST /orders, GET /orders/{id}; JWT; customers only see their own orders; Idempotency-Key header; 422 on validation."

Excerpt of output:
| ID | Endpoint | Category | Condition | Expected status | Expected body / effect | Priority |
|---|---|---|---|---|---|---|
| API-07 | GET /orders/{id} | AuthZ | Valid token of customer B, order of customer A | 404 or 403 `[UNKNOWN: which]` | No order data leaked | High |
| API-12 | POST /orders | Reliability | Same Idempotency-Key sent twice with same body | 201 then same response replayed `[ASSUMPTION]` | Exactly one order persisted | High |
| API-13 | POST /orders | Reliability | Same key, different body | 422 or 409 `[UNKNOWN]` | No new order | Medium |
