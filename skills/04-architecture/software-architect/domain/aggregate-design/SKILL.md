---
description: Designs DDD aggregates by deriving the aggregate root, boundaries and members from the invariants that must hold in one transaction, then defines commands, emitted events, identity, cross-aggregate references and eventual-consistency rules, and checks size and contention. Use when a domain model must be turned into consistency boundaries, when aggregates are too large or cause lock contention, or when deciding what must be strongly versus eventually consistent.
related: event-storming, bounded-context-map, event-driven-design, database-schema-design, business-rules-catalog
prompt: Design the aggregates for our ordering context; rules are credit limit per customer, max 50 lines per order, and no changes after dispatch.
---

# Design Aggregates

## Purpose
Define consistency boundaries that protect true business invariants in a single transaction while keeping aggregates small enough to avoid contention, so the model stays correct under concurrency and easy to evolve.

## When to use
- After `event-storming` produced candidate aggregates, commands and events for a context.
- An existing aggregate is large, slow to load or suffers optimistic-lock conflicts.
- The team argues whether a rule must be enforced transactionally or can be eventually consistent.

## When not to use
- The context boundaries themselves are unclear. Use `bounded-context-map` first.
- The concern is the physical table layout rather than the domain model. Use `database-schema-design`.
- The area is simple CRUD without meaningful invariants; a transaction script or active record is enough, and no aggregate design is needed.

## Inputs
Required:
- The bounded context and its business rules (or event storming output with commands and events).

Optional:
- Expected concurrency (who changes what, how often), data volumes per entity.
- Existing model or code, persistence technology, integration events consumed/published.

If no business rules are given, ask for the rules that must never be violated. Do not invent invariants.

## Process
1. List candidate invariants as testable statements ("order total never exceeds the customer's available credit"). Label each as stated by the user or `[ASSUMPTION]`.
2. For each invariant, decide whether it must hold at the end of every transaction (true invariant) or may be repaired shortly after (eventual rule). Ask the business what happens if it is violated for seconds or minutes.
3. Group only the data needed to enforce true invariants into one aggregate; choose the root that all changes pass through. Everything else becomes a separate aggregate.
4. Reference other aggregates by identity only, never by object reference; record which ID types are held.
5. Define commands on the root (intention-revealing names), preconditions, the invariants each checks and the domain events it emits.
6. For rules that span aggregates, design the eventual-consistency mechanism: domain event plus policy/handler, process manager or saga, with compensation for failure.
7. Check size and contention: estimate members per instance (e.g., lines per order) and concurrent writers per instance. If large or hot, split or move the rule out of the aggregate.
8. Define identity (natural vs. generated), versioning for optimistic concurrency, and lifecycle states with allowed transitions.
9. Note persistence implications (one aggregate per transaction, loading strategy) without coupling the design to a specific ORM.
10. List trade-offs and open questions, especially invariants whose strictness the business has not confirmed.
11. If the goal continues, suggest `event-driven-design` for cross-aggregate events, `database-schema-design` for persistence or `business-rules-catalog` to register the rules.

## Output format
```markdown
# Aggregate Design: <context>

## Invariants
| # | Rule | Source | Strength (transactional / eventual) | Enforced in |
|---|---|---|---|---|

## Aggregates
### <Aggregate root>
- Members: <entities, value objects>
- Identity: <type, generation> · Concurrency: <version field>
- References (by ID): <other aggregates>
- Lifecycle: <state> → <state> ...
| Command | Preconditions | Invariants checked | Events emitted |
|---|---|---|---|

## Cross-Aggregate Rules
- <rule> — mechanism: <event + policy | saga> — compensation: <action>

## Size and Contention Check
- <aggregate>: ~<members> per instance, ~<writers> concurrent — OK / split because ...

## Trade-offs, Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every aggregate protects at least one named invariant; none exists only for navigation.
- [ ] Other aggregates are referenced by ID only.
- [ ] One command changes one aggregate per transaction; multi-aggregate rules use a named eventual mechanism.
- [ ] Size and concurrent-writer estimates are stated or marked `[UNKNOWN]`.
- [ ] Each invariant's strength is confirmed by the business or labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Modeling aggregates after the entity-relationship diagram ("Customer owns Orders owns Lines"). Boundaries follow invariants, not containment.
- Pulling a whole collection into the root to check a rule across all instances (e.g., unique username). Use a dedicated check, a reservation aggregate or a database constraint.
- Treating every rule as transactional. Many "rules" tolerate seconds of inconsistency and are cheaper as policies.

## Example
Input: "Rules: customer credit limit, max 50 lines per order, no changes after dispatch."

Excerpt of output:
- Order (root): lines as entities; invariants "≤ 50 lines" and "no change after Dispatched" are transactional inside Order.
- Credit limit spans many orders: CustomerCredit aggregate reserves credit on "Order Placed"; if the reservation fails, the order is rejected by policy `[ASSUMPTION: short delay acceptable, confirm with finance]`.
- Order references Customer by CustomerId only.
