---
description: Decomposes a system or monolith into service or module boundaries by combining business capabilities, bounded contexts, data ownership, change and scaling drivers and team structure, then evaluates each candidate for coupling, chattiness and distributed-transaction risk and recommends a granularity, including a modular monolith when services are not justified. Use when splitting a monolith, designing a new service landscape, or reviewing whether existing services are too fine or too coarse.
related: bounded-context-map, event-storming, migration-strategy, team-topology, database-schema-design
prompt: We want to split our 400k-line insurance monolith into services; help us find the boundaries and data ownership for policy, claims, billing and customer.
---

# Decompose Into Services

## Purpose
Find service or module boundaries that let teams change, deploy and scale parts of the system independently, with clear data ownership, while avoiding a distributed monolith.

## When to use
- A monolith is being split, or a greenfield system needs a service landscape.
- Services change together in most releases, call each other chattily or share tables.
- The team needs to decide between microservices and a modular monolith.

## When not to use
- The domain's boundaries and language are not yet understood. Use `event-storming` and `bounded-context-map` first.
- The question is the sequence and risk of moving from the old to the new structure. Use `migration-strategy`.
- Only the internal structure of one service is in question. Use `technical-design-doc`.

## Inputs
Required:
- A description of the system's capabilities or modules and the main business flows.

Optional:
- Bounded context map, data model or table list, change history (which modules change together), load profile per function.
- Team structure and size, deployment and operational maturity (CI/CD, observability, on-call).

If only a system name is given, ask for its main capabilities and flows. Mark unknown drivers `[UNKNOWN]`.

## Process
1. List the decomposition drivers and weigh them with the user: independent deployability, team autonomy, differing scaling or availability needs, security or compliance isolation, technology heterogeneity. If none applies strongly, recommend a modular monolith.
2. Start from bounded contexts or business capabilities, not from technical layers or entities; one context is the default upper bound for a service.
3. Assign data ownership: each entity or table has exactly one owning candidate service; other services read through APIs, events or replicated read models.
4. Use change coupling as evidence: modules that change together in most work items belong together `[ASSUMPTION if no history is available]`.
5. For each main flow, trace the calls across candidates; count synchronous hops and cross-service transactions. More than two synchronous hops on a user-facing path or any required cross-service ACID transaction is a boundary smell.
6. Check cohesion and size: a candidate should be ownable by one team and meaningful without the others; merge candidates that cannot act alone (nano-services).
7. Separate volatile from stable parts and isolate components with distinct non-functional needs (e.g., a high-load pricing engine, a PCI-scoped payment component).
8. Evaluate each candidate in a table: responsibility, owned data, dependencies, sync/async interactions, team, scaling profile, risks.
9. Check operational readiness for the proposed number of services: pipelines, observability, on-call and platform capacity. If immature, reduce the number or phase it.
10. Recommend the target decomposition with rationale, the alternatives rejected and the first candidate to extract (high value, low coupling). Label inferences.
11. If the goal continues, suggest `migration-strategy` for the extraction path, `team-topology` for ownership or `adr` for the granularity decision.

## Output format
```markdown
# Service Decomposition: <system>

## Drivers
| Driver | Weight (H/M/L) | Evidence |
|---|---|---|

## Candidate Services / Modules
| Candidate | Responsibility | Owned data | Depends on (sync/async) | Team | Scaling / NFR profile | Risks |
|---|---|---|---|---|---|---|

## Flow Check
| Flow | Hops (sync) | Cross-service writes | Verdict |
|---|---|---|---|

## Data Ownership
- <entity/table> → <owner>; consumers read via <API | events | read model>

## Recommendation
- Target: <microservices | modular monolith | hybrid> — because ...
- Rejected alternatives: ...
- First extraction: <candidate> — because ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every entity has exactly one owning candidate; no shared writable tables remain.
- [ ] Boundaries follow capabilities or contexts, not technical layers.
- [ ] No main flow requires a cross-service ACID transaction; exceptions have a saga or a merge.
- [ ] Each candidate is ownable by one team and meaningful on its own.
- [ ] Operational readiness for the proposed count is addressed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Splitting by layer (UI service, business service, data service), which forces every change through all of them.
- One service per entity (Customer service, Address service), producing chatty CRUD calls and a distributed monolith.
- Keeping a shared database "for now", which preserves the coupling the split was meant to remove.

## Example
Input: "Insurance monolith: policy, claims, billing, customer; claims and policy change together in most releases."

Excerpt of output:
- Drivers: claims needs seasonal scaling (H); billing has PCI-DSS scope isolation (H); team autonomy (M).
- Candidates: Policy Administration, Claims, Billing, Party/Customer.
- Flow check: "Submit claim" validates coverage synchronously against Policy (1 hop): acceptable. Claims reading policy tables directly: must move to a policy read model fed by "Policy Changed" events.
- `[ASSUMPTION]` Change coupling between claims and policy reflects the shared coverage rules; consider keeping them in one module until coverage is modeled explicitly.
- First extraction: Billing — distinct compliance scope, few inbound dependencies.
