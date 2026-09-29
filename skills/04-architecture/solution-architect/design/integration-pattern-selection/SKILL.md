---
name: integration-pattern-selection
description: "Selects integration patterns for each interaction between systems (synchronous API, asynchronous messaging, event streaming, file/batch transfer, CDC, shared database) by analyzing coupling, latency, consistency, volume, ordering and failure behavior, and records the trade-offs. Use when designing how two or more systems exchange data or commands, replacing point-to-point or file interfaces, or when an integration keeps failing under load or change."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: solution-architect
  area: design
  title: "Choose integration patterns"
  related: "integration-requirements, event-driven-design, api-contract, adr, resilience-review"
  prompt: "Choose integration patterns between our order system, the ERP and the warehouse system; ERP only supports SOAP and nightly files, the warehouse needs stock updates within a minute."
---

# Choose Integration Patterns

## Purpose
Pick, per interaction, the integration style that meets the actual latency, consistency and coupling needs, and make the trade-offs explicit so the choice survives review and operations.

## When to use
- A new solution must exchange data or commands with existing systems.
- Point-to-point or file interfaces are being rationalized or moved to messaging/APIs.
- An integration breaks under load, schema change or partner downtime.

## When not to use
- The interfaces are chosen and only the contract must be written. Use `api-contract`.
- The whole flow is event-driven and needs topics, schemas and sagas designed. Use `event-driven-design`.
- Business-level data needs are still unclear. Use `integration-requirements` first.

## Inputs
Required:
- The systems involved and what each interaction must achieve (data or command, direction).
- Latency/freshness expectation per interaction, or permission to mark it `[UNKNOWN]`.

Optional:
- Volumes and peaks, payload sizes, ordering and exactly-once needs.
- Technical capabilities of each endpoint (protocols, CDC support, vendor limits).
- Existing middleware (API gateway, broker, iPaaS, ESB), security and compliance constraints.

If the list of interactions is missing, ask for it. Everything else becomes an open question.

## Process
1. List interactions as rows: source, target, intent (query, command, event notification, state transfer, bulk sync), trigger and direction.
2. For each interaction record the forces: freshness (ms/s/min/daily), volume and peak, consistency need (strong, read-your-writes, eventual), ordering, payload size, and whether the source must know the result.
3. Record endpoint capabilities and limits as stated; label anything inferred `[ASSUMPTION]`.
4. Generate candidates per row: sync request/response (REST/gRPC/SOAP), async command via queue, event notification or event-carried state transfer on a broker/stream, CDC from the source database, file/batch transfer, shared database (flag as last resort).
5. Evaluate candidates against temporal coupling, schema coupling, availability dependency (compound SLA of sync chains), back-pressure, replay/reprocessing, operability and team skills.
6. Decide the delivery guarantee and idempotency strategy for each async choice (at-least-once plus idempotent consumer, dedup key, outbox on the producer side).
7. Define the failure behavior: timeouts, retries with backoff, dead-letter handling, reconciliation for batch/CDC, and what the user sees when the target is down.
8. Check cross-cutting concerns: security (authn between systems, data classification in transit and at rest), versioning and schema evolution, observability (correlation ID end to end).
9. Consolidate: avoid a zoo of styles; justify every deviation from the organization's default pattern.
10. Write the recommendation table and one ADR candidate per significant choice; list open questions by owner.
11. If the goal continues, suggest `api-contract` for chosen APIs, `event-driven-design` for event flows or `adr` to record the decision.

## Output format
```markdown
# Integration Pattern Selection: <solution>
## Interaction Inventory
| # | Source → Target | Intent | Freshness | Volume/peak | Consistency | Ordering |
|---|---|---|---|---|---|---|
## Recommendation
| # | Pattern | Why | Rejected alternative and reason | Guarantee / idempotency | Failure handling |
|---|---|---|---|---|---|
## Cross-Cutting Decisions
- Security: ...
- Schema evolution / versioning: ...
- Observability: ...
## Assumptions and Risks
- [ASSUMPTION] ...
## ADR Candidates
## Open Questions
1. <question> — <owner>
```

## Quality checklist
- [ ] Every interaction has a stated or `[UNKNOWN]` freshness and volume; none is invented.
- [ ] Each choice names the rejected alternative and the reason.
- [ ] Sync chains show their compound availability dependency.
- [ ] Every async flow has a delivery guarantee, idempotency and dead-letter strategy.
- [ ] Shared-database integration is justified or rejected explicitly.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Choosing messaging "because it is modern" when the caller needs an immediate answer. Match the pattern to intent and freshness.
- Treating CDC as an integration contract. Raw table changes leak the source schema; publish curated events or use an outbox.
- Ignoring reconciliation for batch and eventual flows. Plan a periodic compare-and-repair job.

## Example
Input: "Order system, ERP (SOAP and nightly files only), warehouse needs stock within a minute."

Excerpt of output:
| # | Pattern | Why | Rejected alternative |
|---|---|---|---|
| 1 Order → Warehouse | Event notification on broker, at-least-once, idempotent consumer on order ID | < 1 min freshness, warehouse outage must not block checkout | Sync REST: couples checkout availability to warehouse |
| 2 Order → ERP | Nightly file via managed transfer + reconciliation report | ERP only accepts files; daily freshness `[ASSUMPTION: finance confirms]` | SOAP per order: vendor rate limit `[UNKNOWN]` |
