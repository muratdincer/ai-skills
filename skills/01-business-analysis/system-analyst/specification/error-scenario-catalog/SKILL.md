---
description: "Builds a catalog of error scenarios for a feature, flow or interface: each failure case with trigger, detection point, expected system behaviour, data state afterwards, user or caller message, error code, logging and alerting, and recovery path. Use when requirements describe only the happy path, before design or test of an integration or transaction flow, or when support and developers disagree on what the system should do when something fails."
related: "error-message-writing, edge-case-elicitation, sequence-flow, resilience-review, test-case-writing"
prompt: "Create an error scenario catalog for our money transfer flow: validation, limits, core banking timeout and duplicate submissions."
---

# Catalog Error Scenarios

## Purpose
Specify how the system behaves when things go wrong, consistently across screens, APIs and batch jobs, so developers implement one agreed behaviour, testers can verify it and support knows what users see. The catalog turns scattered "handle errors" statements into decidable requirements.

## When to use
- A feature or integration flow is specified but failure behaviour is missing or inconsistent.
- A transactional flow (payment, order, booking) must stay consistent under partial failure.
- Support tickets or incidents show users receiving unclear errors or data left half-processed.

## When not to use
- You need to discover unusual inputs and boundary cases in general. Use `edge-case-elicitation`.
- You only need user-facing wording for known errors. Use `error-message-writing`.
- You are reviewing implemented code for exception handling. Use `error-handling-review`.

## Inputs
Required:
- The feature, flow or interface description (requirements, sequence, use case or API).

Optional, improves quality:
- Sequence or integration details, state model, business rules and limits.
- Existing error code scheme, message style guide, support and monitoring setup.
- Incident history or known problem areas.

If the flow description is missing, ask for it. Do not ask for more; unknown behaviour becomes `[TBD]` with an owner.

## Process
1. Split the flow into steps and, for each step, note what it depends on: user input, business rules, internal services, external systems, data stores, time.
2. Generate failure cases per category: input validation, business rule rejection, authorization, not found or stale data, conflict and concurrency, duplicate request, dependency unavailable or slow, partial failure after commit, capacity or rate limit, configuration or reference data missing.
3. For each case, define the detection point (client, API gateway, service, batch) and whether it is expected (business) or unexpected (technical).
4. Specify expected behaviour: reject, retry automatically, queue for later, compensate, degrade gracefully, or hand to manual processing. State the data state afterwards so nothing is left half-processed.
5. Define the response to the user or caller: error code from the agreed scheme (or `[TBD]`), HTTP status or equivalent, message intent (what happened, what to do next) without leaking internals or personal data.
6. Define operability: log level and correlation ID, whether an alert fires and to whom, and metric or dashboard impact. Personal data must be masked in logs.
7. Define recovery: how the user, support or an automated job completes or reverses the operation, and which runbook or support procedure applies.
8. Rate each scenario by likelihood and impact (High/Medium/Low) with a one-line reason; mark scenarios where behaviour is a business decision and label your proposals `[ASSUMPTION]`.
9. Consolidate: merge duplicates, make codes and messages consistent across similar cases, and check each step of the flow has at least one scenario.
10. If the user wants to continue, suggest `error-message-writing` for final wording, `test-case-writing` to verify each scenario or `resilience-review` for the dependency failures.

## Output format
```markdown
# Error Scenario Catalog: <feature / flow>
Scope: <steps covered> · Code scheme: <given / [TBD]>

## Scenarios
| ID | Step | Category | Trigger | Detected at | Expected behaviour | Data state after | Code / status | Message intent | Log / alert | Recovery | L / I |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Coverage by Step
| Step | Scenarios |
|---|---|

## Business Decisions Needed
- [ASSUMPTION] <proposed behaviour> — owner

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every step of the flow has at least one scenario, including dependency failure.
- [ ] Every scenario states the data state afterwards; no half-processed outcome is left undefined.
- [ ] Messages tell the user what to do next and expose no stack traces, internal names or personal data.
- [ ] Retries are only specified for idempotent operations or with an idempotency key.
- [ ] Each scenario has a detection point, logging decision and recovery path.
- [ ] Proposed business behaviours are labeled `[ASSUMPTION]` and listed for decision.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- One generic "technical error, try again later" for everything. Users retry non-idempotent actions and create duplicates; differentiate by recoverability.
- Covering only validation errors. The costly failures are timeouts and partial failure after data was committed.
- Letting developers decide business outcomes (e.g. whether a failed transfer is reversed). Route these to the business owner as explicit decisions.

## Example
Input: "Customer transfers money: enter IBAN and amount, check daily limit, call core banking, show receipt."

Excerpt of output:
| ID | Step | Category | Trigger | Expected behaviour | Data state after | Code | Message intent | Recovery |
|---|---|---|---|---|---|---|---|---|
| E03 | Limit check | Business rule | Amount exceeds remaining daily limit | Reject before core call | No transfer created | TRF-LIMIT `[TBD]` | Show remaining limit, suggest a smaller amount | None needed |
| E07 | Core call | Dependency slow | No response within `[TBD]` s | Do not retry; mark Pending, poll status | Transfer Pending | TRF-PENDING | "Transfer is being processed; do not resend" | Status job resolves; support procedure `[TBD]` |

Weak: "E07: show an error." Strong: states the Pending data state, the no-retry rule and the user instruction not to resend.
