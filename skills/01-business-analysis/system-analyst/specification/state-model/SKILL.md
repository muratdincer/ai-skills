---
name: state-model
description: "Models the lifecycle of a business entity (order, application, claim, contract, ticket): states, transitions, triggering events, guard conditions, actions, who may trigger each transition, and invalid transitions, delivered as a transition table plus diagram code. Use when an entity has statuses that drive behaviour, when status rules are scattered or disputed, or before designing workflows, APIs or state transition tests."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: system-analyst
  area: specification
  title: "Model entity states"
  related: "business-rules-catalog, state-transition-testing, sequence-flow, error-scenario-catalog, diagram-as-code"
  prompt: "Model the states of an insurance claim from submission to payment or rejection, including reopen and cancel."
---

# Model Entity States

## Purpose
Make an entity's lifecycle explicit and complete, so that every status, allowed move, rule and side effect is agreed once and can be built and tested consistently across screens, APIs, batch jobs and reports.

## When to use
- An entity has a status field that controls what users or systems can do.
- Teams disagree on what "Approved" or "Closed" means, or status rules live in several documents.
- A workflow, API or event design, or state transition testing, is about to start.

## When not to use
- You need the step-by-step business process across roles. Use `bpmn-model` or `as-is-process`.
- You need message order between systems for one scenario. Use `sequence-flow`.
- You only need a rendered diagram from an agreed model. Use `diagram-as-code`.

## Inputs
Required:
- The entity and any description of its lifecycle (requirements, process notes, existing status list).

Optional, improves quality:
- Current status values from the database or screens, business rules, roles and permissions.
- Integrations or reports that read the status, SLA timers, regulatory retention rules.

If the entity or any lifecycle description is missing, ask for it. Do not ask more; record unknown rules as open questions.

## Process
1. List candidate states from the input. Merge synonyms, split states that hide two meanings (e.g. "Pending" for both awaiting customer and awaiting approver), and name each state as a condition ("Under Review"), not an action.
2. Mark the initial state, the final states (terminal) and any states that are only reachable by administrators or batch processes.
3. For every state, ask which events move the entity out: user action, system event, timer or external message. Record each as a transition: from, event, guard condition, to, action or side effect, allowed actor.
4. Build the full state-by-event matrix and classify each empty cell as Not allowed (reject with error), Ignored (no-op) or `[TBD]`; do not leave cells unconsidered.
5. Check lifecycle completeness: cancel or withdraw, reopen, expiry and time-outs, rollback on downstream failure, correction after final state, and archival or deletion under retention rules.
6. Check concurrency: two actors triggering conflicting transitions at once, duplicated events, out-of-order external messages. State the expected rule (first wins, optimistic lock, idempotent event).
7. List side effects per transition: notifications, integration messages, audit entries, SLA timer start/stop. Flag personal data in notifications for minimization.
8. Label every rule not stated in the input `[ASSUMPTION]` and move it to open questions with a likely owner.
9. Produce diagram code (Mermaid stateDiagram-v2 or PlantUML) consistent with the table; every transition appears in both.
10. If the user wants to continue, suggest `state-transition-testing` to derive tests, `business-rules-catalog` for guard rules or `error-scenario-catalog` for rejected transitions.

## Output format
```markdown
# State Model: <entity>
Initial: <state> · Final: <states> · Source: <documents>

## States
| State | Meaning (condition) | Entry via | Final? | Visible to |
|---|---|---|---|---|

## Transitions
| # | From | Event / trigger | Guard | To | Action / side effect | Actor |
|---|---|---|---|---|---|---|

## Not Allowed / Ignored Events
| State | Event | Handling (Reject + message / Ignore / TBD) |
|---|---|---|

## Concurrency and Timing Rules
- ...

## Diagram
<Mermaid stateDiagram-v2 or PlantUML code>

## Assumptions and Open Questions
- [ASSUMPTION] ... — owner
```

## Quality checklist
- [ ] Every state is reachable from the initial state and every non-final state has at least one exit.
- [ ] Every transition has an event, and guards are written as testable conditions.
- [ ] Each state-event combination is covered: allowed, not allowed or `[TBD]`.
- [ ] Cancel, reopen, expiry and failure paths were considered explicitly.
- [ ] Table and diagram match exactly.
- [ ] Inferred rules are labeled `[ASSUMPTION]` and listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using actions as states ("Approve", "Send"). States describe a condition that persists until an event occurs.
- Mixing several dimensions in one status (payment status and review status). Model them as separate state machines or orthogonal regions.
- Forgetting non-human triggers such as timers, batch jobs and inbound messages, which cause most production surprises.

## Example
Input: "A claim is submitted, reviewed by an adjuster, approved or rejected, then paid. Customers can cancel before a decision."

Excerpt of output:
| # | From | Event | Guard | To | Action | Actor |
|---|---|---|---|---|---|---|
| T1 | Submitted | Assign adjuster | Documents complete | Under Review | Start SLA timer | Team lead |
| T2 | Under Review | Approve | Amount ≤ adjuster limit `[ASSUMPTION]` | Approved | Create payment order | Adjuster |
| T3 | Submitted, Under Review | Cancel | No decision yet | Cancelled (final) | Notify customer | Customer |

Not allowed: Cancel in Approved → reject with "Claim already decided". Open question: can a Rejected claim be reopened after an appeal, and by whom?
