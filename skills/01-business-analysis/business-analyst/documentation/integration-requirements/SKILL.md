---
name: integration-requirements
description: "Specifies integration requirements between systems, covering participating systems, direction, data exchanged, trigger and frequency, volumes, error handling, security and SLAs, in a form both sides can build and test against. Use when a feature needs data to flow to or from another system, a new interface or API is requested, or a third-party/vendor integration must be agreed before design."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Specify integration requirements"
  related: "field-mapping, error-scenario-catalog, api-contract, integration-pattern-selection, data-requirements"
  prompt: "Specify the integration requirements for sending approved orders from our e-commerce platform to the ERP and getting stock levels back."
---

# Specify Integration Requirements

## Purpose
Define, per interface, what moves between which systems, when, how much, how failures are handled and what service level is expected, so that both owning teams can design, build and test the integration without renegotiating basics later.

## When to use
- A feature needs data from, or must push data to, another internal or external system.
- A vendor, partner or SaaS integration must be agreed before contracts or design.
- An existing point-to-point interface is being replaced or extended and its behavior must be made explicit.

## When not to use
- The pattern or middleware choice (sync vs async, ESB vs event bus) is the open question. Use `integration-pattern-selection`.
- Field-level source-to-target mapping is the only gap. Use `field-mapping`.
- The API is being designed at endpoint/schema level. Use `api-contract`.

## Inputs
Required:
- The business need or feature that requires the integration.
- The systems involved (at least source and target).

Optional, improves quality:
- Existing interface documentation, API specs, sample payloads.
- Volumes, peak hours, business calendars, SLAs from contracts.
- Security, data classification and regulatory constraints (e.g. KVKK/GDPR).
- System owners and support contacts.

If the need or the systems are missing, ask for them in one short batch. Treat everything else as open questions.

## Process
1. Restate the business need in one sentence and name the business event that makes the integration necessary (e.g. "order approved"). Separate what the user stated from what you infer; label inferences `[ASSUMPTION]`.
2. Build the interface inventory: one row per interface with ID, source system, target system, direction, business owner and technical owner. Split bidirectional flows into two interfaces.
3. For each interface, define trigger and timing: event-driven, scheduled (with schedule and time zone), or on-demand; required latency (real time, near real time with maximum delay, batch).
4. Define the data exchanged at entity level: business objects, key identifiers, mandatory attributes, master system for each attribute and reference data/code lists that must match. Defer field detail to `field-mapping`.
5. Quantify volumes: average and peak messages or records per period, payload size and growth. Mark missing numbers `[UNKNOWN]`; never invent them.
6. Specify delivery semantics: ordering needs, idempotency key, duplicate handling, at-least-once vs exactly-once expectation, partial success rules for batches.
7. Specify error handling per interface: validation failures, target unavailable, timeouts, business rejections; retry policy, dead-letter/parking, alerting, who is notified and manual reprocessing path.
8. Capture non-functional requirements: availability window, response time, throughput, SLA/OLA and support hours, maintenance windows, monitoring and reconciliation (counts/totals between systems).
9. Capture security and compliance: authentication method, authorization scope, encryption in transit and at rest, personal or sensitive data carried (minimize and mask), audit logging, retention.
10. Record dependencies, constraints (rate limits, vendor contract terms, legacy formats) and cutover/migration needs such as initial load and backfill.
11. Fill the template, mark every unsupported field `[UNKNOWN]` or `[TBD]`, and list open questions with the owner who can answer.
12. If the goal continues, suggest `field-mapping` for attribute detail, `error-scenario-catalog` for failure cases, `api-contract` for the interface design, or `integration-pattern-selection` if the style is undecided.

## Output format
```markdown
# Integration Requirements: <integration name>
Business need: <one sentence> · Triggering event: <event>

## Interface Inventory
| ID | Source → Target | Direction | Trigger / timing | Latency | Business owner | Tech owner |
|---|---|---|---|---|---|---|

## Interface <ID>: <name>
- Data exchanged: <objects, keys, mandatory attributes, master system>
- Reference data to align: ...
- Volume: avg <n>/<period>, peak <n> at <time> [UNKNOWN if not given]
- Delivery semantics: ordering, idempotency key, duplicates, batch partial success
- Error handling: | Error type | Detection | Retry | Final handling | Notified |
- NFRs: availability, response time, throughput, SLA, support hours, reconciliation
- Security: authN, authZ, encryption, personal data (masked/minimized), audit

## Dependencies and Constraints
## Cutover / Initial Load
## Assumptions
- [ASSUMPTION] ...
## Open Questions
1. <question> — <why it matters> — <owner>
```

## Quality checklist
- [ ] Every interface has a named source, target, direction and owner on both sides.
- [ ] Trigger, latency and volume are stated or explicitly marked `[UNKNOWN]`; no invented numbers.
- [ ] Each interface has error handling covering retry, final failure and notification.
- [ ] Idempotency/duplicate handling and reconciliation are addressed.
- [ ] Personal or sensitive data is identified with minimization and protection stated.
- [ ] Inferences are labeled and appear in assumptions or open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing "real time" without a maximum delay. Ask what business decision breaks if data is late and derive a number from it.
- Specifying only the happy path. Most integration incidents come from retries, duplicates and silent partial failures; require reconciliation.
- Leaving attribute ownership implicit. When both systems can edit a field, state which one is master or conflicts will surface in production.

## Example
Input: "Approved orders go from the web shop to the ERP; the ERP sends stock back."

Excerpt of output:
| ID | Source → Target | Direction | Trigger / timing | Latency |
|---|---|---|---|---|
| INT-01 | Web shop → ERP | Push | Event: order approved | ≤ 5 min `[ASSUMPTION]` |
| INT-02 | ERP → Web shop | Push | Scheduled, every 15 min `[TBD]` | Batch |

- INT-01 error handling: ERP unavailable → retry 5 times with backoff, then park and alert order-ops; duplicates rejected by order number (idempotency key).
- Open question: Is the web shop or the ERP the master for delivery address after approval? — Order management owner.
