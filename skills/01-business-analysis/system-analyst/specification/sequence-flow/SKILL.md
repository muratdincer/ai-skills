---
name: sequence-flow
description: "Describes how systems, services and actors interact in one end-to-end scenario: participants, ordered messages, sync or async style, payload essentials, responses, timeouts, retries and alternative or failure paths, delivered as a step table plus sequence diagram code. Use when a scenario crosses several systems, when integration behaviour must be agreed between teams, or when someone asks 'what calls what, in which order, and what happens if it fails?'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: system-analyst
  area: specification
  title: "Describe a system interaction sequence"
  related: "integration-requirements, api-contract, error-scenario-catalog, state-model, diagram-as-code"
  prompt: "Describe the sequence for an online order: web shop, order service, payment gateway, stock service and notification, including payment timeout."
---

# Describe a System Interaction Sequence

## Purpose
Give designers, developers and testers one agreed picture of who talks to whom, in what order, with what contract and failure behaviour, for a specific scenario. It closes the gap between functional requirements and interface or API design.

## When to use
- A user or business scenario spans two or more systems, services or external partners.
- Teams owning different systems need to agree on call order, synchronous vs asynchronous style and error handling.
- An incident or change needs the current interaction documented before redesign.

## When not to use
- You need the full specification of one interface (fields, formats, SLAs). Use `integration-requirements` or `api-contract`.
- You need the lifecycle of one entity. Use `state-model`.
- You need the human business process across roles. Use `bpmn-model`.

## Inputs
Required:
- The scenario (trigger, goal, end state) and the systems or actors involved.

Optional, improves quality:
- Interface list or API specs, architecture context (e.g. a C4 container view).
- Non-functional expectations: latency, availability of partners, volumes.
- Known failure incidents or constraints (batch windows, rate limits).

If the scenario or the participating systems are unknown, ask for them, one question at a time. Everything else becomes `[TBD]` or an open question.

## Process
1. State the scenario: trigger, preconditions, success end state and the business outcome. One scenario per sequence; list variants separately.
2. List participants left to right in call order: actor, front end, services, data stores that matter, external partners, message broker. Mark who owns each.
3. Write the main success path as numbered messages: sender, receiver, operation or event name, sync (request/response) or async (event/queue), key payload fields and the response.
4. Mark transactional and consistency boundaries: where data is committed, where eventual consistency starts, and what compensates if a later step fails (e.g. release stock, refund).
5. For each synchronous call, define timeout, retry policy and idempotency key; for each asynchronous message, define delivery guarantee, ordering needs and duplicate handling. Unknown values become `[TBD]`.
6. Add alternative and failure paths: partner down, timeout, business rejection, partial success, duplicate request, late response after timeout. Show what the user sees in each.
7. Note security and data points: authentication between systems, personal data crossing boundaries (mask or minimize), audit or log entries.
8. Label every behaviour not stated in the input `[ASSUMPTION]` and list open questions with the owning team.
9. Produce sequence diagram code (Mermaid sequenceDiagram or PlantUML) with alt/opt blocks matching the table.
10. If the user wants to continue, suggest `integration-requirements` or `api-contract` for each interface, `error-scenario-catalog` for the failure paths or `state-model` for entities whose status changes along the way.

## Output format
```markdown
# Sequence: <scenario>
Trigger: <...> · Preconditions: <...> · Success end state: <...>

## Participants
| Participant | Type (actor / service / store / partner / broker) | Owner |
|---|---|---|

## Main Flow
| # | From → To | Message / operation | Style (sync / async) | Key data | Response / result |
|---|---|---|---|---|---|

## Reliability Rules
| Step | Timeout | Retry | Idempotency / duplicates | Compensation |
|---|---|---|---|---|

## Alternative and Failure Paths
| Ref | Condition | Behaviour | User sees |
|---|---|---|---|

## Diagram
<Mermaid sequenceDiagram or PlantUML code>

## Assumptions and Open Questions
- [ASSUMPTION] ... — owner team
```

## Quality checklist
- [ ] The sequence covers exactly one scenario with a clear trigger and end state.
- [ ] Every message has sender, receiver, style and response or acknowledgement.
- [ ] Every external or remote call has timeout, retry and duplicate handling defined or marked `[TBD]`.
- [ ] Each step that can fail after data was committed has a compensation or an explicit "none".
- [ ] Table and diagram contain the same messages in the same order.
- [ ] Inferred behaviour is labeled `[ASSUMPTION]`; personal data crossing boundaries is flagged.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Drawing only the happy path. The value of a sequence lies in timeouts, retries and compensation, which is where teams disagree.
- Retrying non-idempotent calls such as payment capture. Require an idempotency key or a status query before retrying.
- Mixing several scenarios with nested alt blocks until nobody can read it. Split into separate sequences.

## Example
Input: "Customer places an order: web shop calls order service, order service charges via payment gateway, reserves stock, sends confirmation email."

Excerpt of output:
| # | From → To | Message | Style | Key data | Response |
|---|---|---|---|---|---|
| 1 | Web shop → Order service | createOrder | sync | cart, customerId, idempotencyKey | orderId, status Pending |
| 2 | Order service → Payment gateway | authorize | sync | orderId, amount | authCode or declined |
| 3 | Order service → Broker | OrderConfirmed | async | orderId, lines | ack |

Failure path F1: payment gateway timeout after `[TBD]` s. Do not retry blindly; query payment status by orderId, keep order Pending, and show "Payment is being verified". `[ASSUMPTION]`: stock is reserved only after authorization.
