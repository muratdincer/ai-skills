---
description: "Writes a use case specification with goal, primary and supporting actors, stakeholders' interests, trigger, preconditions, minimal and success guarantees, a numbered main success scenario, and alternate and exception flows keyed to the steps they branch from. Use when an interaction has many branches, several actors or system-to-system steps, or when asked for a 'use case', 'UC spec' or 'fully dressed use case'."
related: "frd-writing, user-story, business-rules-catalog, error-scenario-catalog, sequence-flow"
prompt: "Write the use case for 'Return a purchased item in store' with card refunds and missing receipts."
---

# Write a Use Case Specification

## Purpose
Describe one actor goal as a complete, step-by-step interaction with the system, including every way it can branch or fail, so that designers, developers and testers share one precise behavioral model.

## When to use
- An interaction has many alternate or exception paths that stories alone would scatter.
- Several actors or external systems take turns within one goal.
- A contract, vendor or regulated context requires a formal behavioral description.

## When not to use
- Behavior is simple and the team works from backlog items. Use `user-story` with `acceptance-criteria`.
- A whole system's behavior across many functions is needed. Use `frd-writing`.
- Only message order between systems matters. Use `sequence-flow`.

## Inputs
Required:
- The actor goal (use case name) and a description of how it happens today or should happen.

Optional, improves quality:
- Business rules, process models, screen sketches, integration descriptions, known failure cases, the organization's use case template.

If the goal or the basic flow is missing, ask for it. Ask at most 5 blocking questions at a time; keep the rest as open questions.

## Process
1. Name the use case as the primary actor's goal: verb + object ("Return purchased item"). Set level (user goal or subfunction) and scope (which system is the black box).
2. List the primary actor, supporting actors (people and systems) and stakeholders with their interest in the outcome.
3. Define the trigger, preconditions (what the system guarantees before start) and guarantees: minimal guarantee (true even on failure, e.g. audit record) and success guarantee.
4. Write the main success scenario as 5-12 numbered steps, each "actor does / system does", in the actor's language and without UI detail.
5. For every step ask "what else can happen here?" and write alternate flows (valid variations) as `3a`, `3b` with the condition, steps and where they rejoin or end.
6. Write exception flows for failures: invalid data, rule violation, timeout or unavailable external system, cancellation, concurrent change. State the end state of each.
7. Reference business rules by ID instead of embedding them; list new rules found and mark inferred ones `[ASSUMPTION]`.
8. Add special requirements that apply only to this use case (response time, audit, accessibility) and data touched.
9. Check that the main scenario delivers the success guarantee and every branch ends in a defined state.
10. List open questions with owners.
11. If the goal continues, suggest `error-scenario-catalog` for detailed failure handling, `business-rules-catalog` for the rules, or `sequence-flow` for system interactions.

## Output format
```markdown
# UC-<nn> <Goal name>
| Field | Value |
|---|---|
| Level / Scope | <user goal / subfunction> · <system> |
| Primary actor | ... |
| Supporting actors | ... |
| Stakeholders and interests | ... |
| Trigger | ... |
| Preconditions | ... |
| Minimal guarantee | ... |
| Success guarantee | ... |

## Main Success Scenario
1. ...
## Alternate Flows
- 3a. <condition>: 3a1 ... → rejoins at step 4
## Exception Flows
- 5x. <failure>: ... → ends with <state>
## Business Rules Referenced
## Special Requirements and Data
## Assumptions and Open Questions
```

## Quality checklist
- [ ] The name is an actor goal, and the main scenario achieves it in 5-12 steps.
- [ ] Every step names who acts; no UI layout or technical detail appears.
- [ ] Every alternate and exception flow references its step, condition and end or rejoin point.
- [ ] Failures of external systems and timeouts are covered.
- [ ] Minimal guarantee holds on every exception path.
- [ ] Rules are referenced by ID; inferred rules are labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing the use case as a screen walkthrough ("clicks OK"). Describe intent and system response; leave controls to design.
- Stuffing branches into the main scenario with "if". Keep the main scenario linear and move every condition to an extension.
- Use cases at the wrong level ("Log in" as a user goal). Treat such steps as subfunctions referenced from goal-level use cases.

## Example
Input: "Customer returns an item in store; card purchases are refunded to the card, missing receipts are handled somehow."

Excerpt of output:
Main success scenario:
1. Customer presents the item and receipt to the clerk.
2. Clerk identifies the sale by receipt number.
3. System shows the sale and the items eligible for return under BR-12.
4. Clerk selects the item and return reason.
5. System calculates the refund and requests card refund from the payment provider.
6. System records the return and prints the return slip.

Alternate flows:
- 1a. No receipt: clerk searches by card used `[ASSUMPTION]`; if no sale is found, see open question 1.
Exception flows:
- 5x. Payment provider unavailable: system records the return as "Refund pending" and retries `[TBD: retry policy]`; the customer receives a pending slip.

Open question 1: Is a refund without receipt allowed, and as store credit? — Retail operations
