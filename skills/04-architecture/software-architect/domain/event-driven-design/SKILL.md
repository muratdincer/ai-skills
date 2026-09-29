---
description: Designs an event-driven flow end to end, covering event types and naming, schemas and versioning, topics and partition keys, ordering, delivery semantics, idempotent consumers, outbox publishing, error handling with retries and dead-letter queues, and saga orchestration or choreography with compensations. Use when services must integrate asynchronously through events, when a business process spans several services, or when an existing event flow suffers duplicates, lost messages or ordering bugs.
related: event-storming, aggregate-design, integration-pattern-selection, data-contract, schema-evolution-plan
prompt: Design the event flow for order placement across ordering, payment, inventory and shipping, with compensation when payment fails.
---

# Design an Event-Driven Flow

## Purpose
Specify an asynchronous flow precisely enough that producers and consumers can be built independently and still behave correctly under duplicates, reordering, partial failure and schema change.

## When to use
- A business process spans several services and must not rely on a distributed transaction.
- A new integration was chosen to be event-based and now needs contracts and semantics.
- An existing flow shows duplicate processing, lost events, out-of-order updates or stuck sagas.

## When not to use
- Whether to use events at all is still open. Use `integration-pattern-selection` first.
- Only a single event schema contract between two teams is needed. Use `data-contract`.
- The events and commands of the domain are not yet known. Use `event-storming`.

## Inputs
Required:
- The business flow: trigger, participating services and desired end state, including failure outcomes.

Optional:
- Broker or streaming platform in use, throughput and latency targets, retention needs.
- Existing event catalog, schema registry conventions, regulatory constraints on data in events.

If the failure outcomes are not stated, ask what must happen when each step fails. Mark unknown targets `[UNKNOWN]`.

## Process
1. Draw the flow as a sequence of steps and decide coordination: choreography (services react to events) for short, stable flows; orchestration (a saga orchestrator issues commands) when there are many steps, branching or compensation. Justify the choice.
2. Classify each message: domain event (fact, past tense, owned by the producer), integration event (published contract derived from domain events) or command (request to one handler). Do not publish internal domain events as public contracts by accident.
3. Choose payload style per event: event notification (IDs only, consumer calls back), event-carried state transfer (enough data to act) or full snapshot. Minimize personal data in payloads and flag fields needing masking or encryption.
4. Define the envelope: event ID, type, version, source, occurred-at, correlation and causation IDs, partition key; align with CloudEvents where the organization uses it.
5. Map topics or channels, and choose partition keys to preserve the ordering that matters (usually per aggregate ID). State explicitly where no global ordering is guaranteed.
6. Guarantee publication: transactional outbox or change data capture from the producer's store, so the state change and event cannot diverge.
7. Assume at-least-once delivery: make every consumer idempotent (processed-ID store, natural idempotency or version checks) and define how stale or out-of-order events are detected and ignored.
8. Design failure handling: retry policy with backoff and limits, poison-message routing to a dead-letter queue, alerting, and a replay procedure with an owner.
9. For each saga step, define the compensating action, its idempotency and what happens if compensation itself fails (manual intervention path). Add timeouts for steps that may never answer.
10. Set schema evolution rules: compatibility mode (backward/forward/full), additive-only changes, version bump and deprecation path for breaking changes.
11. Define observability: tracing via correlation IDs, consumer lag, DLQ depth and end-to-end latency. Label every design choice not backed by a stated requirement as `[ASSUMPTION]`.
12. If the goal continues, suggest `data-contract` for each published event, `schema-evolution-plan` for versioning or `adr` to record the coordination choice.

## Output format
```markdown
# Event-Driven Flow: <process>
Coordination: <choreography | orchestration> — because <reason>

## Flow
| Step | Producer | Message (type: event/command) | Topic / channel | Partition key | Consumers | On failure |
|---|---|---|---|---|---|---|

## Event Catalog
| Event | Version | Payload style | Key fields | Personal data | Owner |
|---|---|---|---|---|---|

## Delivery and Consistency
- Publication: <outbox | CDC>
- Delivery: at-least-once; idempotency: <mechanism per consumer>
- Ordering: <guaranteed per key / not guaranteed where>

## Saga and Compensation
| Step | Action | Compensation | Timeout | If compensation fails |
|---|---|---|---|---|

## Error Handling
- Retry: <policy> · DLQ: <name, owner, alert> · Replay: <procedure>

## Schema Evolution
- Compatibility: <mode> · Breaking change process: ...

## Observability
- ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every consumer is idempotent and the mechanism is named.
- [ ] Publication cannot diverge from the state change (outbox, CDC or equivalent).
- [ ] Ordering guarantees are stated per partition key, and consumers tolerate reordering elsewhere.
- [ ] Every saga step has a compensation, a timeout and a manual fallback.
- [ ] Personal data in payloads is minimized and flagged.
- [ ] DLQs have an owner, an alert and a replay procedure.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Assuming exactly-once end to end. Brokers may offer it internally, but side effects outside the broker still need idempotency.
- Dual writes (save to the database, then publish) without an outbox, which loses or invents events on crash.
- Events named as commands ("ReserveStock") or as CRUD ("OrderUpdated"), which couple consumers to the producer's intent or hide meaning.
- A DLQ nobody watches; it becomes silent data loss.

## Example
Input: "Order placement across ordering, payment, inventory, shipping; compensate if payment fails."

Excerpt of output:
- Coordination: orchestration, because four steps with compensation and a timeout on the external payment provider.
- Step 2: Orchestrator → "AuthorizePayment" (command) → payment.commands, key = orderId; on failure → "ReleaseStock" compensation, then "Order Rejected" event.
- Idempotency: inventory stores processed eventId per orderId; a duplicate "ReserveStock" command is acknowledged without a second reservation.
- `[ASSUMPTION]` Payment timeout 15 minutes; confirm with the payment provider's SLA.
