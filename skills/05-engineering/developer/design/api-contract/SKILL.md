---
description: "Writes an API contract as an OpenAPI (HTTP) or AsyncAPI (events/messages) specification from requirements, including resources, operations, schemas, error model, security, versioning and examples. Use when a new endpoint, service or event must be agreed between producer and consumers before implementation, or when someone asks for an OpenAPI/Swagger or AsyncAPI spec."
related: "api-design-review, api-reference-docs, integration-requirements, technical-design-doc, api-test-design"
prompt: "Write an OpenAPI contract for a service that lets partners create shipments, get shipment status and cancel a shipment before pickup."
---

# Write an API Contract

## Purpose
Produce a machine-readable, reviewable contract that producers and consumers can build and test against in parallel, and that stays the single source of truth for documentation, mocks and contract tests.

## When to use
- A new HTTP API or event stream is being designed and consumers are waiting on it.
- An existing API needs a new version or breaking change and the delta must be explicit.
- Integration requirements exist in prose and must become a precise spec.

## When not to use
- Reviewing an already written API design. Use `api-design-review`.
- Human-facing reference pages from an existing spec. Use `api-reference-docs`.
- Integration needs are still unclear. Use `integration-requirements` first.

## Inputs
Required:
- The requirements or use cases the API must serve, and whether it is request/response or event-based.

Optional, improves quality:
- Organization API guidelines (naming, pagination, error format, versioning), auth mechanism, existing domain model.
- Consumer list, expected volumes, latency targets, idempotency needs.

If the interaction style is unclear, ask. Missing details become `[TBD]` in the spec with a comment.

## Process
1. List consumer use cases and derive resources (nouns) or event types (past-tense facts) from them; do not mirror database tables.
2. For HTTP: define operations with correct method semantics, status codes, idempotency (`Idempotency-Key` for unsafe retries), and concurrency control (ETag / `If-Match`) where updates race.
3. For events: define channels/topics, message key (ordering scope), payload schema, headers (event id, type, time, correlation id), delivery semantics and consumer expectations for duplicates.
4. Model schemas with types, formats, required fields, enums, lengths and patterns; use ISO 8601 for dates and explicit units/currency for amounts.
5. Define one error model for all operations (for HTTP, RFC 9457 problem details unless the guideline says otherwise), with a stable machine-readable error code list.
6. Define collection behavior: pagination (cursor preferred for large or changing sets), filtering, sorting, limits.
7. Specify security schemes and per-operation scopes; mark personal data fields and minimize them.
8. State versioning and compatibility rules: which changes are additive, how breaking changes are introduced and deprecated.
9. Add at least one realistic request/response or message example per operation, using fake data.
10. Validate the spec mentally against each use case and list open questions.

## Output format
````markdown
# API Contract: <name> v<version>
Style: HTTP (OpenAPI 3.1) | Events (AsyncAPI 3.0) · Owner: <team> · Consumers: <list or [TBD]>

## Use Case to Operation Map
| Use case | Operation / event |

## Specification
```yaml
openapi: 3.1.0   # or asyncapi: 3.0.0
info: { title: <name>, version: <x.y.z> }
paths / channels: ...
components:
  schemas: ...
  securitySchemes: ...
```

## Error Codes
| Code | HTTP status | Meaning | Client action |

## Compatibility and Versioning Rules
## Open Questions
````

## Quality checklist
- [ ] Every use case maps to an operation or event and vice versa.
- [ ] Every operation has success and error responses, security and an example.
- [ ] Unsafe operations that clients may retry are idempotent or document why not.
- [ ] Field names, casing, date and money formats are consistent across the spec.
- [ ] Personal data is identified and only fields consumers need are exposed.
- [ ] The spec is syntactically plausible YAML/JSON for the stated version.

## Common pitfalls
- Exposing internal models or database IDs that lock the schema. Design from consumer use cases.
- Using `200` with an error body, or generic `400` for everything. Use precise statuses plus stable error codes.
- Events that carry only an ID and force consumers to call back, or that dump the whole aggregate. Decide deliberately between notification and state transfer.
- No pagination on list endpoints "because data is small today".

## Example
Input: "Partners create shipments, get status, cancel before pickup."

Excerpt of output:
- `POST /shipments` requires `Idempotency-Key`; returns `201` with `Location`; `409 SHIPMENT_DUPLICATE_REFERENCE` if `partnerReference` exists.
- `POST /shipments/{id}/cancellation` returns `409 SHIPMENT_ALREADY_PICKED_UP` after pickup (state conflict, not `400`).
- Open question: Is status also pushed as an event (`shipment.status-changed`) or polling only? `[TBD]`
