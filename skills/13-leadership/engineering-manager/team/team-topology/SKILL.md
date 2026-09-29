---
description: Designs or reviews a team topology using stream-aligned, platform, enabling and complicated-subsystem team types and their interaction modes, based on value streams, cognitive load and dependencies. Use when forming or splitting teams, when handoffs and cross-team dependencies slow delivery, when a platform team is being considered, or when team boundaries do not match the architecture.
related: bounded-context-map, service-decomposition, role-definition, cross-team-dependency-board, org-change-communication
prompt: We have 5 teams and 40 engineers, every feature needs 3 teams. Propose a team topology for our e-commerce platform.
---

# Design Team Topology

## Purpose
Align team boundaries with value streams and architecture so that most work can flow through one team, cognitive load is sustainable, and the remaining cross-team interactions are deliberate and time-boxed.

## When to use
- Teams are being formed, split or merged, or the organization is growing fast.
- Most features need several teams and handoffs dominate lead time.
- A platform, enabling or specialist team is proposed and its mandate is unclear.
- Team boundaries and service/domain boundaries have drifted apart.

## When not to use
- The need is domain boundaries only, not teams. Use `bounded-context-map`.
- Defining one role's responsibilities. Use `role-definition`.
- Announcing an already decided change. Use `org-change-communication`.

## Inputs
Required:
- Current teams (size, skills, what they own) and the main products or value streams.

Optional, improves quality:
- Architecture or domain map, dependency data (items blocked by other teams), lead-time metrics.
- Constraints: headcount, locations and time zones, budget, regulatory separation of duties.

If current ownership is unknown, ask for a list of teams and what they own; do not invent a current state.

## Process
1. Map value streams (customer journeys or products) and the systems/domains each touches.
2. Map current ownership and the dependencies: for a sample of recent work items, which teams were needed and where did it wait.
3. Assess cognitive load per team (number of domains, systems, technologies, on-call surface); flag teams above a sustainable load.
4. Propose stream-aligned teams first, one per value stream or bounded context, sized for sustainable ownership (commonly 5-9 people).
5. Identify capabilities that many streams need and that reduce their load; only then propose a platform team with a product mindset and a clear "thinnest viable platform" scope.
6. Use complicated-subsystem teams only for genuinely specialist areas (e.g. pricing engine, video codec) and enabling teams as time-boxed coaches, not permanent gatekeepers.
7. Define interaction modes between teams (collaboration, X-as-a-service, facilitating) with duration and exit criteria.
8. Check Conway's law alignment: target architecture and team boundaries must reinforce each other; note where architecture must change for the topology to work.
9. Plan the transition in steps with ownership handover, on-call changes and measures (lead time, cross-team dependencies, load survey) to verify.
10. List people impacts as open questions for HR and managers; do not assign named individuals or assume preferences.
11. Mark inferred dependencies and loads as `[ASSUMPTION]`.
12. If the user's goal continues, suggest `role-definition` for new roles, `bounded-context-map` for domain boundaries or `org-change-communication` to announce the change.

## Output format
```markdown
# Team Topology: <organization / area>

## Value Streams and Domains
| Value stream | Domains / systems | Current teams involved |
|---|---|---|

## Current Pain (evidence)
- ...

## Proposed Teams
| Team | Type | Owns | Size | Cognitive load notes |
|---|---|---|---|---|

## Interaction Modes
| Team A | Team B | Mode | Duration / exit criteria |
|---|---|---|---|

## Architecture Changes Needed
- ...

## Transition Plan and Success Measures
| Step | Change | Measure |
|---|---|---|

## Open Questions / Assumptions
- ...
```

## Quality checklist
- [ ] Each stream-aligned team can deliver most items in its stream without waiting on others.
- [ ] Platform and enabling teams have explicit consumers, scope and interaction modes.
- [ ] Cognitive load is assessed per team, not only headcount.
- [ ] Team boundaries match the target architecture or the needed architecture change is stated.
- [ ] Collaboration modes are time-boxed with exit criteria.
- [ ] No named individuals are assigned; people impacts are listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Component teams by technology (frontend team, database team) labeled as stream-aligned. Test with real work items.
- A platform team that becomes a ticket queue. Define self-service interfaces and measure consumer lead time.
- Reorganizing without architecture change. If the monolith is shared, the new teams will still wait on each other.

## Example
Input: 5 teams (web, mobile, backend, data, ops), 40 engineers; checkout changes need web, backend and ops.

Excerpt of output:
- Proposed: Checkout (stream-aligned: web+mobile+backend skills), Catalog & Search (stream-aligned), Fulfilment (stream-aligned), Developer Platform (platform: CI/CD, runtime, observability as a service), Data Enablement (enabling, 2 quarters).
- Interaction: Checkout ↔ Developer Platform = X-as-a-service; Data Enablement ↔ Checkout = facilitating until events are self-published.
- `[ASSUMPTION]` Checkout owns payment-adapter code today split across two repositories; confirm.
