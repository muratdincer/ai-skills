---
description: Plans and runs a big-picture or design-level event storming session and turns the result into a structured model of domain events, commands, actors, policies, read models, external systems, aggregates and hot spots. Use when a team needs a shared understanding of a business flow, wants to discover bounded contexts or aggregates, or has a messy wall of stickies to consolidate.
related: bounded-context-map, aggregate-design, event-driven-design, workshop-plan, glossary-builder
prompt: Help me run a design-level event storming for our order-to-delivery flow and structure the stickies from yesterday's session.
---

# Run Event Storming

## Purpose
Produce a shared, timeline-ordered model of what happens in a domain, expressed as domain events and the commands, actors, policies and data around them, so that boundaries, aggregates and open conflicts become visible before design starts.

## When to use
- A new domain or a large feature must be understood across business and engineering.
- Service or module boundaries are disputed and need evidence from the business flow.
- A session already happened and its raw stickies (photo transcript, list) need consolidating into a model.
- Before `aggregate-design` or `event-driven-design`, to find the events and invariants that drive them.

## When not to use
- The flow is already modeled and only needs a formal process diagram. Use `bpmn-model` or `as-is-process`.
- The contexts are known and only their relationships are unclear. Use `bounded-context-map`.
- The session logistics (room, agenda, invites) are the main need. Use `workshop-plan`.

## Inputs
Required:
- The domain or flow in scope, with a start and end event (e.g., "order placed" to "order delivered").
- Either the planned session setup or the raw session output (sticky list, transcript, photo notes).

Optional:
- Participants and their roles (domain experts are essential).
- Existing glossary, process documents, known pain points.
- Level: big picture (whole domain) or process/design level (one flow, down to aggregates).

If the scope has no clear start and end, ask for them first. Treat every other gap as an open question.

## Process
1. Fix the level and scope: big picture for exploring a whole value stream, design level for one flow where aggregates and policies must be found. State the start and end events explicitly.
2. If planning a session, define the legend (orange: domain event, blue: command, yellow: actor, lilac: policy, pink: external system, green: read model, pale yellow: aggregate, red/magenta: hot spot) and the timebox; require at least one domain expert per sub-flow.
3. Collect domain events as past-tense business facts ("Payment Authorized"), not UI actions or technical steps ("Button Clicked", "Row Inserted"). Rewrite or discard those that are not.
4. Enforce the timeline: order events left to right, deduplicate synonyms, and record the chosen term in the glossary. Mark parallel and alternative paths explicitly.
5. Identify pivotal events where the business meaning changes hands (e.g., "Order Confirmed", "Shipment Dispatched"); these are candidate context boundaries.
6. For each event, add the triggering command and the actor or external system that issues it; add policies ("whenever X, then Y") that link an event to the next command.
7. Add read models: the information an actor needs to decide on a command. Missing read models often reveal missing data requirements.
8. At design level, group commands and events around the business rule that must hold consistently; name those clusters as candidate aggregates, labeled `[ASSUMPTION]` until the invariant is confirmed by a domain expert.
9. Capture every disagreement, unknown or pain point as a hot spot with the question, who raised it and who can resolve it. Do not resolve hot spots by guessing.
10. Separate what participants stated from what you inferred (e.g., an unnamed policy, a merged synonym) and label each inference.
11. Fill the output template, ordered by timeline, with swimlanes per pivotal segment.
12. If the goal continues, suggest `bounded-context-map` for the boundaries found, `aggregate-design` for the candidate aggregates or `event-driven-design` for integration events.

## Output format
```markdown
# Event Storming: <flow> (<big picture | design level>)
Scope: <start event> → <end event> · Participants: <roles or [UNKNOWN]>

## Timeline
| # | Segment | Actor / System | Command | Domain Event | Policy | Read Model | Aggregate (candidate) |
|---|---|---|---|---|---|---|---|

## Pivotal Events and Candidate Boundaries
- <event> — separates <segment A> from <segment B>

## Candidate Aggregates
- <name> — invariant: <rule> — events: ... [ASSUMPTION until confirmed]

## Hot Spots
| # | Question / conflict | Raised by | Can resolve | Blocks |
|---|---|---|---|---|

## Glossary Decisions
- <chosen term> (not: <synonyms>) — meaning

## Inferences and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every domain event is a past-tense business fact, not a UI or technical step.
- [ ] Events are in timeline order with parallel and alternative paths marked.
- [ ] Every command has an actor, external system or policy that triggers it.
- [ ] Hot spots are recorded as questions with an owner, not silently resolved.
- [ ] Candidate aggregates are tied to a named invariant and labeled until confirmed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Running the session with only engineers. Without domain experts you model the current software, not the business.
- Jumping to aggregates and services in a big-picture session. Finish the timeline and hot spots first.
- CRUD events ("Order Updated") that hide the real business facts. Ask what actually changed and why it matters.

## Example
Input: "Stickies: Add to cart, Order Created, Payment OK, Stock Reserved, Invoice Row Inserted, Order Shipped, Customer Notified."

Excerpt of output:
- Rewritten events: "Item Added to Cart", "Order Placed", "Payment Authorized", "Stock Reserved", "Invoice Issued" (was "Invoice Row Inserted", technical), "Shipment Dispatched".
- Pivotal event: "Order Placed" separates Shopping from Fulfilment.
- Policy `[ASSUMPTION]`: whenever Payment Authorized, then Reserve Stock.
- Hot spot: Is stock reserved before or after payment for pre-orders? Raised by: warehouse lead. Can resolve: product owner.
