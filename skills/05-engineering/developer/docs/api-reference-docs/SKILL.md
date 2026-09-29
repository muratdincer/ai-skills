---
description: Writes API reference documentation for HTTP, RPC or message-based APIs, covering authentication, each endpoint or operation with parameters, request and response examples, error codes, pagination, rate limits and versioning, derived from a contract, code or notes. Use when an API needs consumer-facing reference docs, existing docs drift from the implementation, or a spec exists but lacks descriptions and examples.
related: api-contract, api-design-review, readme-writing, error-message-writing, changelog-entry
prompt: Write API reference docs for our orders API from this OpenAPI file. Consumers keep asking what the error codes mean and how paging works.
---

# Write API Reference Docs

## Purpose
Let an integrating developer call the API correctly on the first attempt without reading the source or asking the team: every operation, field, error and limit is described with a working example. Precise reference docs reduce support load and integration defects.

## When to use
- An API is being opened to other teams, partners or the public.
- A contract (OpenAPI, AsyncAPI, protobuf, GraphQL schema) exists but has empty descriptions and no examples.
- Consumers report confusion about errors, pagination, idempotency or authentication.

## When not to use
- Designing the contract itself. Use `api-contract`.
- Judging whether the API design is good. Use `api-design-review`.
- Getting-started or tutorial content for the whole product. Use `readme-writing` or `tutorial`.

## Inputs
Required:
- A source of truth for the API surface: a contract file, route definitions or handler code, or a precise description of the operations.

Optional, improves quality:
- Authentication scheme, environments and base URLs.
- Error model, rate limits, pagination and versioning policy.
- Real (sanitized) request and response samples, known consumer questions.

If no source of the API surface is given, ask for it. Never document an endpoint, field or error that is not in the input; list suspected gaps as open questions.

## Process
1. Inventory the surface from the source: operations, paths or topics, methods, schemas, and which ones are public versus internal. Document only the intended public surface.
2. Write the overview once: base URLs per environment (placeholders if unknown), authentication and authorization (scopes or roles per operation), content types, versioning scheme, and conventions (casing, date-time format and time zone, money and decimal representation, ID format).
3. Describe the cross-cutting behaviors once and link to them: error model with the full list of error codes, pagination (cursor or offset, limits, ordering guarantees), filtering and sorting syntax, idempotency keys, rate limits and the headers that report them, retry guidance.
4. For each operation write: a one-line purpose in consumer terms, method and path, required permission, path, query and header parameters, request body fields, and response fields per status code.
5. For every field state type, required or optional, nullability, allowed values or format, constraints (length, range, pattern) and default; describe meaning, not just the name.
6. Add a complete request and response example for the main success case and at least one error case per operation, using synthetic data that satisfies the schema.
7. Document operation-specific errors: status, error code, when it happens, and what the consumer should do (fix input, retry with backoff, contact support).
8. Note behavioral guarantees consumers rely on: idempotency, consistency (eventual or immediate), ordering, side effects such as emitted events or emails, and deprecation status with the replacement.
9. Cross-check examples against the schema and flag every mismatch between contract and implementation as an open question rather than choosing silently.
10. Mark unknown values `[UNKNOWN]` and inferred behavior `[ASSUMPTION]`, and collect them as open questions for the API owner. If the user continues, suggest `api-design-review` for design problems found while documenting, or `changelog-entry` to publish API changes.

## Output format
```markdown
# <API name> Reference
## Overview
Base URLs · Authentication · Versioning · Conventions (dates, money, IDs)

## Errors
| HTTP status | Error code | Meaning | Consumer action |
|---|---|---|---|

## Pagination, Rate Limits, Idempotency
...

## <Operation name>
`<METHOD> <path>` — <purpose>. Permission: <scope/role>
### Parameters
| Name | In | Type | Required | Description / constraints |
|---|---|---|---|---|
### Request Body / Response (<status>)
| Field | Type | Required | Nullable | Description / constraints |
|---|---|---|---|---|
### Examples
<request> / <response> / <error response>
### Errors
| Status | Code | When | Action |
|---|---|---|---|

## Open Questions
- ...
```

## Quality checklist
- [ ] Every documented operation, field and error exists in the source; nothing is invented.
- [ ] Every field has type, requiredness, nullability and constraints, not just a name.
- [ ] Each operation has a success example and at least one error example that match the schema.
- [ ] Each error code tells the consumer what to do next.
- [ ] Examples use synthetic data only; no real customer data, tokens or internal hosts.
- [ ] Cross-cutting rules (auth, errors, paging, limits) are defined once and referenced, not repeated inconsistently.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Descriptions that repeat the field name ("customerId: the customer ID"). State meaning, format and origin (where the consumer gets the value).
- Documenting only the happy path. Most integration time is spent on errors, paging edges and retries.
- Letting docs silently diverge from the contract. When they disagree, raise it; do not pick one.

## Example
Input: OpenAPI with `GET /orders` (query `cursor`, `limit`) and error schema `{code, message}`; descriptions empty.

Weak: "`limit` — the limit."

Strong excerpt:
- `limit` | query | integer | optional | Page size, 1-100, default 20 `[ASSUMPTION: default not in spec, confirm]`.
- `cursor` | query | string | optional | Opaque value from `next_cursor` of the previous page; do not parse or build it.
- Errors: `400` | `INVALID_CURSOR` | cursor expired or malformed | restart from the first page without `cursor`.
- Open question: Is ordering stable across pages when new orders arrive during paging?
