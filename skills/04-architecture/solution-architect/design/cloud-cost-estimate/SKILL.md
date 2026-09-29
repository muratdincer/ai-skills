---
description: Sizes each component of a solution design (compute, storage, database, network egress, managed services, observability, licences) from workload drivers and produces a transparent monthly run-cost estimate with ranges, assumptions and cost-reduction levers. Use when a design needs a cost figure for approval, when comparing architecture options on cost, or when a cloud budget must be set before build.
related: finops-review, capacity-planning, build-vs-buy, solution-architecture-document, budget-proposal
prompt: Estimate the monthly cloud cost of this design: 6 containerized services, a managed PostgreSQL, Redis, object storage for 5 TB of documents and about 20 million API calls a month.
---

# Estimate Cloud Cost of a Design

## Purpose
Give decision makers a monthly run-cost estimate that can be traced line by line to workload drivers and assumptions, so it can be challenged, refined and later compared with actual spend.

## When to use
- A solution design needs a run-cost figure for approval or business case.
- Two architecture options must be compared on cost.
- A budget or cost guardrail must be set before build or migration.

## When not to use
- Actual spend of a running system is to be analyzed and optimized. Use `finops-review`.
- The question is how much capacity is needed over time. Use `capacity-planning` first, then price it here.
- A full sourcing decision including build effort. Use `build-vs-buy`.

## Inputs
Required:
- The architecture components (containers, data stores, managed services) and target cloud or hosting model.
- Workload drivers: users/requests, data volume and growth, or permission to state them as `[ASSUMPTION]`.

Optional:
- Region, availability targets (multi-AZ, multi-region, DR), environments (dev/test/stage/prod).
- Pricing model constraints (on-demand, commitments, enterprise discounts), existing shared platform costs.
- Currency and exchange-rate convention.

If components or workload drivers are missing, ask. Never state unit prices from memory as facts: use user-supplied prices or the provider's price calculator, and mark unverified prices `[TO VERIFY]`.

## Process
1. List cost-bearing components per environment, including the ones designs forget: load balancers, NAT/gateways, egress, logs/metrics/traces, backups and snapshots, secrets/key management, CI runners, DR replicas.
2. Define workload drivers and assumptions in one table: request rate (average and peak), data stored and growth, data transferred out, active hours for non-production.
3. Size each component: instance class and count (from peak with headroom and HA), storage tier and volume, IOPS/throughput, managed-service tiers.
4. Price each line as quantity × unit price, with the unit price source and date noted by the user or `[TO VERIFY]`.
5. Produce low / expected / high estimates by varying the most uncertain drivers (typically traffic, egress, log volume).
6. Add non-production environments explicitly (scaled down, scheduled off-hours) and the DR posture's cost.
7. Identify the top 3-5 cost drivers and their sensitivity (cost per unit of the driver, e.g., per million requests or per TB).
8. List cost levers: commitments/reserved capacity, autoscaling and scale-to-zero, storage lifecycle tiers, log sampling/retention, egress avoidance via caching/CDN, right-sizing after load test.
9. State what is excluded (people, support plans, licences, taxes) and the unit-cost KPI to track later (e.g., cost per order).
10. If the goal continues, suggest `finops-review` after go-live, `capacity-planning` for growth or `budget-proposal` to request funding.

## Output format
```markdown
# Cloud Cost Estimate: <solution> (<provider/region>, <currency>/month)
## Workload Drivers and Assumptions
| Driver | Value | Source |
|---|---|---|
## Cost Lines
| Env | Component | Sizing | Quantity | Unit price (source) | Monthly |
|---|---|---|---|---|---|
## Summary
| Scenario | Prod | Non-prod | DR | Total |
|---|---|---|---|---|
| Low / Expected / High | | | | |
## Top Cost Drivers and Sensitivity
## Cost Levers
## Exclusions
## Unit-Cost KPI
## Open Questions
```

## Quality checklist
- [ ] Every cost line traces to a driver and a sizing decision.
- [ ] Unit prices come from the user or are marked `[TO VERIFY]`; none are presented as authoritative from memory.
- [ ] Egress, observability, backups and non-production environments are included or explicitly excluded.
- [ ] A range (low/expected/high) is given, not a single precise-looking number.
- [ ] Exclusions and the unit-cost KPI are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Sizing for average load and forgetting HA pairs and peak headroom.
- Ignoring observability and egress, which often rival compute in chatty or log-heavy systems.
- False precision: two decimals on a figure built from guessed traffic. Round and show the range.

## Example
Input: "6 container services, managed PostgreSQL, Redis, 5 TB object storage, ~20M API calls/month."

Excerpt of output:
| Env | Component | Sizing | Monthly |
|---|---|---|---|
| Prod | Container compute | 6 services × 2 replicas, `[ASSUMPTION: 0.5 vCPU/1 GB each]`, multi-AZ | `[unit price TO VERIFY]` |
| Prod | Object storage | 5 TB standard, `[ASSUMPTION: 30% moves to infrequent tier after 90 days]` | ... |
| Prod | Logs | `[ASSUMPTION: 2 KB per request]` × 20M = ~40 GB/month ingest | ... |

Top driver: managed PostgreSQL HA instance; sensitivity: moving to one size smaller after load test changes the total by `[calc after prices verified]`.
