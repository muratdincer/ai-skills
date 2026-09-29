---
description: Reviews an API design (OpenAPI/AsyncAPI spec, gRPC/protobuf definition, GraphQL schema or a written proposal) for resource modeling, naming consistency, versioning and compatibility, error model, pagination and filtering, idempotency and concurrency, security and operability, and returns rated findings with concrete fixes. Use when an API is proposed or changed before implementation or publication, when a public or partner API is about to be released, or when an existing API needs a consistency audit.
related: api-contract, api-deprecation-plan, api-test-design, threat-model, api-reference-docs
prompt: Review this OpenAPI spec for our new orders API before we publish it to partners. Focus on versioning, errors and pagination.
---

# Review an API Design

## Purpose
Find design flaws while they are still cheap to fix: once consumers integrate, every naming, error or compatibility mistake becomes a breaking change or a permanent workaround. The review produces a verdict and a prioritized list of fixes grounded in the given spec.

## When to use
- A new API or a significant change is specified and awaits approval before implementation.
- A public, partner or cross-team API is about to be published or versioned.
- An existing API surface shows inconsistency and needs an audit against the organization's guidelines.

## When not to use
- The contract does not exist yet and must be written. Use `api-contract`.
- An endpoint or version is being retired. Use `api-deprecation-plan`.
- The goal is test cases for an implemented API. Use `api-test-design`.

## Inputs
Required:
- The API definition (spec, schema, IDL or a proposal with endpoints/operations, payloads and errors).

Optional, improves quality:
- Consumers (internal, partner, public) and their integration style; expected volumes.
- Organization API guidelines, existing APIs to stay consistent with, authentication model.
- Compatibility promise (semantic versioning, support window).

If no definition is provided, ask for it. If consumers are unknown, assume external consumers `[ASSUMPTION]` and review with the stricter compatibility bar.

## Process
1. Establish context: API style (REST, gRPC, GraphQL, event), consumers, and the guideline set being applied. If no guideline is given, state the baseline used (e.g., the organization's own or widely used REST conventions) as `[ASSUMPTION]`.
2. Resource and operation model: resources map to domain concepts, not tables or screens; no verbs in REST paths except well-justified actions; operations have one responsibility; no chatty patterns that force N+1 calls.
3. Naming and consistency: one casing convention per surface, consistent pluralization, identifiers, timestamps (ISO 8601 with offset), money (amount + currency), enums documented and extensible.
4. Versioning and compatibility: explicit versioning scheme; classify every change as additive or breaking; tolerant-reader expectations stated; unknown enum values handled by clients.
5. Error model: one structured error format (e.g., RFC 9457 problem details), correct status codes (400 vs 422, 401 vs 403, 404 vs 410, 409, 429), machine-readable error codes, no stack traces or internal details.
6. Collections: pagination on every unbounded list (cursor preferred for large or changing sets), maximum page size, stable sort, filtering and field selection conventions.
7. Idempotency and concurrency: safe retries for POST via idempotency keys, PUT/DELETE idempotent, optimistic concurrency (ETag/If-Match or version field), long-running operations modeled explicitly.
8. Security: authentication scheme, authorization at object level (BOLA), scopes per operation, no sensitive data in URLs, input limits, rate limits; check against OWASP API Security Top 10. Flag personal data in payloads and recommend minimization.
9. Operability: correlation/trace IDs, rate-limit headers, deprecation signaling, caching headers, documented SLAs where promised.
10. Rate each finding Critical (blocks publication), Required, Nit, Optional or FYI; give the concrete fix (changed path, field or schema snippet), not only the problem. Label inferences `[ASSUMPTION]`.
11. Give a verdict and, if the goal continues, suggest `api-contract` to rewrite the spec, `threat-model` for security-heavy findings, or `api-test-design` to cover the agreed behavior.

## Output format
```markdown
# API Design Review: <API name / version>
Style: <REST/gRPC/GraphQL/event> · Consumers: <...> · Baseline: <guideline>
Verdict: Approve / Approve with changes / Rework

## Summary
- Strengths: ...
- Top risks: ...

## Findings
| # | Severity | Area | Location (path/operation/field) | Finding | Proposed fix |
|---|---|---|---|---|---|

## Compatibility Assessment
| Change | Additive / Breaking | Consumer impact | Mitigation |
|---|---|---|---|

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every finding points to a concrete location in the given definition and has a proposed fix.
- [ ] Error model, pagination, idempotency and versioning are each explicitly assessed, even if no issue was found.
- [ ] Object-level authorization and sensitive data exposure are checked.
- [ ] Breaking changes are identified and separated from additive ones.
- [ ] Severity labels are applied consistently; only Critical items block the verdict.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reviewing style while missing semantics: perfect naming but a POST that double-charges on retry. Check idempotency and concurrency first.
- Offset pagination on large, frequently changing collections, causing skipped or duplicated items. Recommend cursors.
- Returning 200 with an error body, which breaks client retry and monitoring logic.

## Example
Input: `POST /createOrder` returns `200 {"success": false, "msg": "Stock error"}`; `GET /orders` returns all orders without paging.

Weak: "Endpoints could be more RESTful."

Strong excerpt:
| # | Severity | Area | Location | Finding | Proposed fix |
|---|---|---|---|---|---|
| 1 | Critical | Errors | POST /createOrder | Failure returned as 200 with free-text message | `POST /orders`; return 409 with problem details `{type, title, status, code: "OUT_OF_STOCK"}` |
| 2 | Critical | Collections | GET /orders | Unbounded list | Add `limit` (max 100) and `cursor`; return `next_cursor` |
| 3 | Required | Idempotency | POST /orders | Retry can create duplicate orders | Accept `Idempotency-Key` header; replay stored response |
