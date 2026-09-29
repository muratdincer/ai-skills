---
description: "Models an entity or workflow as states, events, guards and actions, then derives tests for all valid transitions, invalid transitions (state-event pairs that must be rejected) and key transition sequences (0-switch and 1-switch coverage). Use when behavior depends on status or history, such as orders, applications, approvals, accounts, sessions or devices, or when someone asks to test a workflow or lifecycle."
related: state-model, decision-table-testing, test-case-writing, test-scenarios-from-requirements, api-test-design
prompt: "Create state transition tests for our purchase request: Draft, Submitted, Approved, Rejected, Cancelled, Ordered. Only the requester can cancel, only before Ordered."
---

# Build State Transition Tests

## Purpose
Verify that a lifecycle allows exactly the transitions it should, under the right conditions and roles, and rejects every other one, since illegal transitions are a frequent source of data corruption and security defects.

## When to use
- An entity has statuses and actions allowed only in some statuses.
- Workflows include approvals, timeouts, retries, cancellations or reopenings.
- An API exposes status-changing endpoints that could be called in the wrong order.

## When not to use
- The state model itself must be designed or documented for business. Use `state-model`.
- Outcome depends only on current input combinations, not status. Use `decision-table-testing`.
- You need all scenarios of a feature at high level. Use `test-scenarios-from-requirements`.

## Inputs
Required:
- States and allowed transitions, or a description of the workflow.

Optional, improves quality:
- Guards (conditions, roles), actions on transition (notifications, stock, audit), timeouts.
- Existing diagram or status field values.

If the workflow description is missing, ask for it. Transitions not stated as allowed or forbidden become open questions.

## Process
1. List states including initial, final and implicit ones (e.g. "Expired" after a timeout, "Deleted").
2. List events/triggers: user actions, system events, timers, external callbacks.
3. Build the state transition table: for each valid transition give from-state, event, guard, to-state, actions.
4. Draw or describe the diagram in text (e.g. a Mermaid state diagram) so it can be reviewed.
5. Build the full state x event matrix; every empty cell is a candidate invalid transition. Decide expected behavior: rejected with message, ignored, or `[UNKNOWN]`.
6. Derive 0-switch tests: one test per valid transition, including guard true/false variants and role variants.
7. Derive invalid transition tests for high-risk cells (terminal states, financial effects, security-relevant roles), including direct API calls that bypass the UI.
8. Derive 1-switch or longer sequences for risky paths: reopen after reject, cancel after approve, retry after failure, loops.
9. Add timing and concurrency cases: timeout at boundary, two actors triggering conflicting events simultaneously.
10. Verify side effects per transition: audit trail, notifications, dependent entities.
11. List open questions for undefined cells.

## Output format
```markdown
# State Transition Tests: <entity / workflow>
## States and Events
## Transition Table
| # | From | Event | Guard | To | Actions |
## Diagram
<text or Mermaid stateDiagram>
## State x Event Matrix
| State \ Event | E1 | E2 | ... |   (to-state, "Reject", or [UNKNOWN])
## Tests
| Test | Type (valid / invalid / sequence) | Path | Data / role | Expected |
## Open Questions
```

## Quality checklist
- [ ] Every valid transition is covered by at least one test (0-switch coverage).
- [ ] Every cell of the state x event matrix has an expected behavior or is an open question.
- [ ] Terminal states are tested for rejection of all events.
- [ ] Guards are tested in both true and false variants, including role checks.
- [ ] Side effects are verified, not only the resulting status.

## Common pitfalls
- Testing only through the UI, where invalid buttons are hidden. Call the underlying API or service directly.
- Forgetting timer-driven and system-driven transitions.
- Ignoring concurrent transitions (approve and cancel at the same moment).

## Example
Input: "Draft, Submitted, Approved, Rejected, Cancelled, Ordered; only requester cancels, only before Ordered."

Excerpt of output:
| 5 | Approved | Cancel | actor = requester | Cancelled | Notify approver |
| ST-12 | Invalid | Ordered → Cancel | requester | Rejected, status unchanged |
| ST-15 | Invalid | Approved → Cancel | approver (not requester) | Rejected with authorization error |
- Open question: Can a Rejected request be edited and resubmitted, or is a new request needed?
