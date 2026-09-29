---
description: Describes a software system with the C4 model - system context, container and, where useful, component diagrams - as diagrams-as-code (Structurizr DSL, PlantUML C4 or Mermaid) with consistent element names, responsibilities, technologies and labeled relationships. Use when someone needs architecture diagrams for a design, review, onboarding or documentation, or wants to turn a textual description or existing sketch into C4 views.
related: solution-architecture-document, diagram-as-code, bounded-context-map, adr, architecture-review
prompt: Create C4 context and container diagrams in Structurizr DSL for our e-commerce checkout: web shop, mobile app, checkout API, payment provider, order DB and message broker.
---

# Describe Architecture with C4

## Purpose
Produce clear, consistent C4 views as code so the architecture can be versioned, reviewed and regenerated, and so every audience sees the right level of detail.

## When to use
- A design, review or ADR needs context and container diagrams.
- An existing whiteboard sketch or prose description must become maintainable diagrams.
- Onboarding needs a map of a system and its neighbors.
- Diagrams in different documents disagree and need one model.

## When not to use
- Sequence or flow diagrams of one interaction only. Use `sequence-flow`.
- Non-architecture diagrams (org charts, generic flowcharts). Use `diagram-as-code`.
- Domain boundaries and team relationships. Use `bounded-context-map`.

## Inputs
Required:
- The system in scope and a description of its parts, users and external systems.

Optional:
- Preferred notation (Structurizr DSL, PlantUML with C4-PlantUML, Mermaid C4); default to Structurizr DSL.
- Technologies, protocols, deployment targets.
- Existing diagrams or naming conventions.

If the scope system is unclear, ask which system is being described. Unknown technologies are labeled `[TBD]`.

## Process
1. Fix the scope: one software system in scope; everything else is a person or external system.
2. Build the model first, then views. List elements: people (roles, not names), software systems, containers (separately deployable/runnable units and data stores), and components only where they help a decision.
3. For each element, record name, one-line responsibility, technology (containers and components) and owner if known.
4. For each relationship, write a verb phrase and, for containers, protocol/format (e.g., "Places orders using [HTTPS/JSON]", "Publishes OrderPlaced to [AMQP]"). Direction follows the dependency or data initiation.
5. Create the System Context view: scope system, users, external systems; no technology detail.
6. Create the Container view: containers of the scope system plus directly connected people and externals. Show data stores and message brokers as containers or externals consistently.
7. Create Component views only for containers with architecturally significant internals; keep to 5-15 components.
8. Optionally add a Deployment view mapping containers to environments and nodes.
9. Validate: every relationship has a label; no element appears with two names; each view fits in ~20 elements; a legend or key is present.
10. Output the diagram code and a short element catalog table; list `[TBD]` items as open questions.
11. Label every element or relationship inferred rather than stated as `[ASSUMPTION]`; if the goal continues, suggest `solution-architecture-document`, `adr` or `architecture-review`.

## Output format
````markdown
# C4 Model – <system>
## Element Catalog
| Element | Type | Responsibility | Technology | Owner |
|---|---|---|---|---|

## Diagram Code (<notation>)
```
workspace { model { ... } views { systemContext ... container ... } }
```

## Notes
- Assumptions and `[TBD]` items
- Open questions
````

## Quality checklist
- [ ] Levels are not mixed: no components on the container view, no technology on the context view.
- [ ] Every relationship is directional, labeled with intent and (for containers) protocol.
- [ ] Element names and responsibilities are identical across views and the catalog.
- [ ] Data stores and brokers are shown explicitly.
- [ ] The code is syntactically valid for the chosen notation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using "API" or "Service" as responsibilities. State what the element does for the business.
- Drawing libraries or modules as containers. Containers run or store data separately.
- Bidirectional arrows everywhere. Pick the initiating direction; add a second relationship only if both sides initiate.

## Example
Input: "Checkout: web shop and mobile app call checkout API; API stores orders in PostgreSQL, calls payment provider, publishes events to a broker."

Excerpt of output:
```
customer = person "Customer" "Buys products online"
shop = softwareSystem "Online Shop" {
  web = container "Web Shop" "Browsing and checkout UI" "React"
  api = container "Checkout API" "Validates carts, creates orders, starts payment" "[TBD language]"
  db = container "Order Database" "Stores orders and payment status" "PostgreSQL"
}
psp = softwareSystem "Payment Provider" "Authorizes card payments" "External"
customer -> web "Places orders using" "HTTPS"
web -> api "Submits checkout requests to" "HTTPS/JSON"
api -> psp "Requests payment authorization from" "HTTPS/JSON"
```
