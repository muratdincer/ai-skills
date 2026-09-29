---
name: api-deprecation-plan
description: "Plans the deprecation and removal of an API, version, endpoint, field or event with a consumer inventory, versioning strategy, machine-readable Deprecation/Sunset signalling, a migration guide, brownouts and measurable removal gates. Use when a breaking change, a new API version or a retired endpoint must reach internal, partner or public consumers without surprise outages."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "Plan an API deprecation"
  related: "api-design-review, api-contract, migration-strategy, api-reference-docs, product-sunset-plan"
  prompt: "We are replacing /v1/orders with /v2/orders (new pagination and money format). Plan the deprecation of v1 for our partners and internal apps."
---

# Plan an API Deprecation

## Purpose
Remove an API surface safely: every consumer is known, told in-band and out-of-band, given a tested migration path, and the removal happens only when traffic data proves it is safe.

## When to use
- A new major version replaces an old one, or an endpoint, field, parameter, event or schema is being removed.
- A breaking behavior change (error format, pagination, auth scheme) must be rolled out to existing consumers.
- An integration platform or gateway is being retired and its APIs must move.

## When not to use
- The whole customer-facing product or feature is being retired. Use `product-sunset-plan` (and this skill for its API part).
- The new API itself still needs design review. Use `api-design-review` or `api-contract` first.
- It is a data or platform migration without a consumer-facing contract change. Use `migration-strategy`.

## Inputs
Required:
- The API surface being deprecated and what replaces it (or "no replacement").

Optional, improves quality:
- Consumer list or traffic data (API keys, client IDs, user agents, gateway logs) and consumer types (internal, partner, public, mobile apps with slow update cycles).
- Contractual or published deprecation policy (minimum notice, support window).
- Protocol and style: REST/HTTP, GraphQL, gRPC, async events.
- Target dates and the driver (security issue, cost, platform end-of-life).

If the deprecated surface is unclear, ask for it. Unknown consumers, dates and policies become `[UNKNOWN]`/`[TBD]` and open questions.

## Process
1. Define the change precisely: old surface, replacement, the exact breaking differences (field by field), and whether a non-breaking path (additive change, adapter, default) could avoid deprecation altogether. Label inferred differences `[ASSUMPTION]`.
2. Build the consumer inventory from traffic evidence, not memory: consumer ID, owner/contact, type, call volume, endpoints used, last seen, client release cycle. Consumers without an identifiable owner are a risk; plan to require client identification if absent. Mask API keys and personal data.
3. Choose the versioning and coexistence approach (URI, header or media-type version; field-level deprecation; GraphQL `@deprecated`; protobuf `deprecated` option; new event type/topic) and how long both run in parallel.
4. Set the policy and timeline: announcement date, deprecation date, brownout windows, sunset (removal) date. The notice period is at least the published policy or contract minimum and long enough for the slowest consumer release cycle (e.g. mobile apps).
5. Add in-band signalling: the `Deprecation` response header (RFC 9745) and `Sunset` header (RFC 8594) with a `Link` to the migration guide (`rel="deprecation"`/`rel="sunset"`), warnings in the API reference and SDK compile-time deprecation markers. Specify the exact header values `[TBD dates]`.
6. Write the migration guide outline: before/after request and response examples, field mapping table, behavioral differences (errors, pagination, rounding, time zones), SDK versions, test sandbox, and an FAQ.
7. Plan out-of-band communication: changelog, developer portal notice, direct e-mail to each inventoried owner, partner account managers for high-volume consumers, and reminders at fixed T-minus points.
8. Design brownouts: scheduled, announced, time-boxed windows where the old surface returns the documented error (e.g. 410 Gone or a clear error code) to flush out unknown consumers; increase duration stepwise, never during a consumer's known peak, with an instant revert switch.
9. Define removal gates: traffic on the old surface below an agreed threshold `[TBD]` for N consecutive days, all named consumers confirmed migrated or explicitly accepted, no open migration blockers, support and on-call briefed, rollback (re-enable) tested. Owner signs off each gate.
10. Plan the removal and cleanup: final response behavior after sunset (410 with link vs. 404), monitoring and alerting for the first days, then removal of code, routes, docs, SDK methods and gateway config.
11. List risks, assumptions and open questions, then fill the template. Suggest next skills: `api-reference-docs` for the migration guide, `api-contract` for the replacement contract, or `product-sunset-plan` if customers lose functionality.

## Output format
```markdown
# API Deprecation Plan: <surface> → <replacement>
| Field | Value |
|---|---|
| Deprecated surface | <endpoints / fields / events> |
| Replacement | <surface or none> |
| Breaking differences | <list> |
| Policy / minimum notice | <policy or [UNKNOWN]> |
| Owner | <team or [UNKNOWN]> |

## Consumer Inventory
| Consumer | Owner / contact | Type | Volume | Endpoints used | Last seen | Status |
|---|---|---|---|---|---|---|

## Timeline
| Milestone | Date | Signal / action |
|---|---|---|
| Announce | [TBD] | changelog, e-mail, portal |
| Deprecated | [TBD] | `Deprecation` + `Sunset` + `Link` headers |
| Brownout 1..n | [TBD] | <duration, error returned> |
| Sunset | [TBD] | <410 / 404 behavior> |

## Migration Guide Outline
- Field mapping / before-after examples / behavior changes / SDK / sandbox / FAQ

## Removal Gates
- [ ] <measurable condition> — <owner>

## Risks, Assumptions, Open Questions
- [RISK] ... / [ASSUMPTION] ... / 1. <question> — <owner>
```

## Quality checklist
- [ ] The consumer inventory is based on traffic evidence, and unidentified consumers are handled explicitly.
- [ ] Every breaking difference is listed with its migration mapping.
- [ ] In-band (headers, docs, SDK) and out-of-band (direct contact, changelog) signals are both planned.
- [ ] Brownouts are announced, time-boxed and reversible.
- [ ] Removal gates are measurable and owned; the date alone is not a gate.
- [ ] No dates, volumes or consumer names are invented; unknowns are marked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Relying on a changelog entry alone. Most consumers never read it; contact inventoried owners directly and signal in every response.
- Removing on the announced date regardless of traffic. The date is a target; the gates decide.
- Forgetting slow-moving clients (mobile apps, on-premise installs, batch jobs that run monthly). Check "last seen" over a full business cycle before concluding traffic is gone.
- Silently changing behavior inside the same version. Any breaking change needs either a new version or this plan.

## Example
Input: "Replace /v1/orders with /v2/orders (cursor pagination, money as minor units + currency). Partners and internal apps use v1."

Excerpt of output:
- Breaking differences: offset → cursor pagination; `amount: 12.5` → `amount: {value: 1250, currency: "TRY"}` `[ASSUMPTION – confirm currency source]`.
- Inventory: 3 internal apps identified from gateway logs; partner traffic without client ID `[UNKNOWN owner]` → require `client_id` from the deprecation date.
- Signal: `Deprecation: @<unix-time>`, `Sunset: <HTTP-date>`, `Link: <https://.../migrate-v2>; rel="deprecation"` `[TBD dates]`.
- Removal gate: v1 traffic below `[TBD]` requests/day for 30 consecutive days including a month-end, and every partner has confirmed migration in writing.
