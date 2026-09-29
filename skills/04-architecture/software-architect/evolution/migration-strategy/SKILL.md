---
description: Plans how to move from a current system or platform to a target one by comparing strangler fig, parallel run, phased and big-bang approaches, defining slices and their order, data migration and synchronization, coexistence and routing, verification and rollback per step, and cutover criteria. Use when replacing or re-platforming a system, extracting services from a monolith, moving to a new database or cloud, or when a migration plan needs a risk review.
related: target-state-architecture, service-decomposition, modernization-assessment, rollback-plan, schema-migration-plan
prompt: Plan the migration of our on-premise order management monolith to the new cloud-based order services without downtime during the sales season.
---

# Plan a Migration

## Purpose
Produce a stepwise migration plan in which every step delivers or de-risks something, can be verified and can be rolled back, so that the move from old to new does not depend on a single high-risk cutover.

## When to use
- A target architecture exists and the path from the current state must be planned.
- A monolith is being split and extraction order and coexistence must be designed.
- Data must move to a new store or platform while the business keeps running.
- An existing migration plan relies on one big cutover and needs challenging.

## When not to use
- The decision whether to modernize, and how (retain, rehost, refactor, replace), is still open. Use `modernization-assessment`.
- The target state itself is undefined. Use `target-state-architecture`.
- Only one release's rollback steps are needed. Use `rollback-plan`.

## Inputs
Required:
- Current and target state (systems, data stores, interfaces) at least at block level.
- Business constraints: allowed downtime, blackout periods, deadlines and their reasons.

Optional:
- Data volumes and change rates, integration inventory, consumer list, team capacity, regulatory constraints (data residency, audit trail).

If allowed downtime or blackout periods are unknown, ask; they decide the approach. Mark other gaps `[UNKNOWN]`.

## Process
1. Summarize the gap between current and target, and the migration drivers (end of support, cost, capability). State what must not change for users.
2. Compare approaches against the constraints: strangler fig (incremental routing of functionality), parallel run (both systems process and outputs are compared), phased by user group, region or function, and big bang. Recommend one or a combination with reasons; big bang only when coexistence is impossible or cheaper and the risk is accepted explicitly.
3. Define slices: thin vertical units (a capability, a flow, a customer segment) that can move independently. Order them by learning value, risk and dependency; start with a low-risk slice that exercises the whole path.
4. Design coexistence: routing mechanism (facade, API gateway, feature flag), anti-corruption layer between old and new models, and how cross-cutting concerns (authentication, IDs, reporting) work during the transition.
5. Plan data migration per slice: ownership during coexistence (single writer), initial load, ongoing sync (CDC, dual write via outbox, batch), reconciliation checks and how conflicts are resolved.
6. Define verification per step: functional parity tests, output comparison for parallel runs, performance baselines and business KPIs to watch.
7. Define rollback per step: trigger conditions, the mechanism (route back, re-sync data backwards), and the point of no return where rollback stops being possible.
8. Set cutover and decommissioning criteria: which evidence allows switching fully and when the old component, its data and its licenses are retired.
9. Map risks (data loss, prolonged dual running, team capacity, consumer readiness) with mitigations, and respect blackout periods in the timeline.
10. Label every sizing, duration or dependency not provided by the user as `[ASSUMPTION]`; do not invent dates.
11. If the goal continues, suggest `schema-migration-plan` for database changes, `rollback-plan` for individual releases or `adr` to record the chosen approach.

## Output format
```markdown
# Migration Strategy: <from> → <to>
Constraints: downtime <...> · blackout <...> · deadline <... or [UNKNOWN]>

## Approach
- Chosen: <strangler fig | parallel run | phased | big bang | combination> — because ...
- Rejected: <approach> — because ...

## Slices and Order
| # | Slice | Why this order | Depends on | Coexistence / routing | Data strategy | Verification | Rollback (point of no return) |
|---|---|---|---|---|---|---|---|

## Data Migration
- Ownership during coexistence: ...
- Initial load / sync / reconciliation: ...

## Cutover and Decommissioning Criteria
- ...

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] The approach is justified against stated downtime, blackout and deadline constraints.
- [ ] Every slice has verification, a rollback path and a stated point of no return.
- [ ] Each data set has exactly one writer at any time during coexistence, or conflict resolution is defined.
- [ ] Decommissioning of old components is planned, not left open.
- [ ] No dates, volumes or durations are invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Migrating technical layers (first the database, then the backend, then the UI), which delivers no value until the end. Migrate vertical slices.
- Dual writes from application code without an outbox or reconciliation, which silently diverge.
- Never finishing: the strangler facade and old system live forever. Set decommissioning criteria and track them.

## Example
Input: "Move on-premise order management to cloud order services; no downtime during sales season."

Excerpt of output:
- Approach: strangler fig with a routing facade, plus a two-week parallel run for order pricing, because downtime is not allowed and pricing errors are costly.
- Slice 1: order status queries (read-only) — low risk, exercises facade, auth and data sync end to end.
- Slice 3: order placement for one sales channel; point of no return: when the new service becomes the only writer of order headers.
- Blackout: no cutover steps during the sales season `[exact dates UNKNOWN, confirm with sales]`.
