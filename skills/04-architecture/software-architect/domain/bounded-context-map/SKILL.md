---
name: bounded-context-map
description: "Produces a context map that names each bounded context, its ubiquitous language and ownership, and classifies the relationships between contexts (partnership, shared kernel, customer-supplier, conformist, anticorruption layer, open host service, published language, separate ways) with upstream/downstream direction and integration style. Use when defining module or service boundaries, onboarding a team to a landscape, or diagnosing coupling and translation problems between teams."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 04-architecture
  role: software-architect
  area: domain
  title: "Map bounded contexts"
  related: "event-storming, service-decomposition, aggregate-design, integration-pattern-selection, team-topology"
  prompt: "Draw a context map for our retail platform: catalog, pricing, ordering, payment (external PSP), warehouse and CRM, owned by four teams."
---

# Map Bounded Contexts

## Purpose
Make the model boundaries and the power relationships between them explicit, so that integration contracts, translation layers and team responsibilities follow deliberate choices instead of accidental coupling.

## When to use
- After `event-storming` has revealed pivotal events and candidate boundaries.
- Before splitting a monolith or assigning services to teams.
- When the same term means different things in different parts of the system and causes defects.
- When a downstream team keeps breaking because of upstream model changes.

## When not to use
- Boundaries are not yet discovered at all. Start with `event-storming`.
- The question is how to cut deployable services and own data. Use `service-decomposition`.
- Only the transport mechanism between two systems must be chosen. Use `integration-pattern-selection`.

## Inputs
Required:
- The list of subdomains, modules or systems in scope, with a sentence on what each does.

Optional:
- Owning teams, existing integrations, known pain points, glossary conflicts.
- Event storming output, org chart, external vendors and their contracts.

If no list of parts is given, ask for it. Mark unknown ownership or directions as `[UNKNOWN]`.

## Process
1. Classify subdomains as core (differentiating), supporting or generic; this drives where to invest in modeling and where to buy or conform.
2. Define each bounded context: name, responsibility, key terms of its ubiquitous language, owning team and whether it is internal or external.
3. Find terms that cross contexts with different meanings (e.g., "Customer" in CRM vs. Billing) and record each meaning per context; do not force a single enterprise model.
4. For every pair that exchanges data or behavior, decide upstream (whose model changes propagate) and downstream (who is affected).
5. Classify each relationship by pattern: Partnership, Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer (ACL), Open Host Service (OHS), Published Language (PL), Separate Ways, or Big Ball of Mud for legacy areas.
6. Check pattern fit against team reality: Shared Kernel and Partnership need tight collaboration; a downstream core context facing an external or legacy upstream should normally have an ACL rather than conform.
7. Note the integration style per relationship (synchronous API, events, file, shared DB) and flag shared databases as coupling risks.
8. Mark every relationship you inferred rather than were told as `[ASSUMPTION]`, and list problems: missing ACLs, circular dependencies, one team owning many unrelated contexts, contexts split across teams.
9. Produce the map as a diagram-as-code (e.g., Mermaid or Context Mapper DSL) plus a relationship table.
10. Recommend changes in priority order, each with the pain it removes and the cost it adds.
11. If the goal continues, suggest `service-decomposition` for deployment boundaries, `aggregate-design` inside a core context or `team-topology` to align team ownership.

## Output format
```markdown
# Context Map: <landscape>

## Bounded Contexts
| Context | Subdomain type | Responsibility | Key terms | Owner team | Internal/External |
|---|---|---|---|---|---|

## Relationships
| Upstream | Downstream | Pattern | Integration style | Notes / risks |
|---|---|---|---|---|

## Diagram
<Mermaid or Context Mapper DSL source, e.g. flowchart LR; Catalog -- "OHS/PL" --> Ordering>

## Term Conflicts
- <term>: <context A meaning> vs <context B meaning>

## Problems and Recommendations
1. <problem> → <recommended change> — benefit / cost

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every context has one owning team or is marked `[UNKNOWN]`.
- [ ] Every relationship has a direction and one named pattern.
- [ ] Conflicting terms are listed per context, not unified by force.
- [ ] External and legacy upstreams feeding a core context are protected by an ACL or the risk is stated.
- [ ] Shared databases between contexts are flagged.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Drawing the map as the desired future while presenting it as today. Keep an as-is map and a to-be map separate.
- Equating one context with one microservice. A context can contain several deployables, and one deployable should not span contexts.
- Labeling everything Customer-Supplier. If the upstream ignores downstream needs, the honest pattern is Conformist.

## Example
Input: "Ordering calls the external PSP; Warehouse reads the Ordering DB directly; Pricing and Catalog teams share a Product library."

Excerpt of output:
- Ordering (downstream) ← PSP (upstream, external): Conformist today; recommend ACL to keep PSP status codes out of the ordering model.
- Warehouse ← Ordering: shared database, high coupling risk; recommend Ordering publish "Order Placed" events (OHS/PL).
- Pricing ↔ Catalog: Shared Kernel (Product library) `[ASSUMPTION: joint change process exists]`.
