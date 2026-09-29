---
name: finops-review
description: "Reviews cloud or platform spend to find waste, rightsizing opportunities, commitment and pricing-model options, storage and data-transfer savings, and tagging/allocation gaps, and returns a prioritized savings backlog with effort and risk. Use when a cost report, bill export or resource inventory is shared, costs grew unexpectedly, or a periodic cost review is due."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: devops-engineer
  area: infrastructure
  title: "Review cloud cost"
  related: "cloud-cost-estimate, capacity-planning, iac-review, environment-strategy, budget-proposal"
  prompt: "Here is our last three months of cloud cost by service and resource group. Where are we wasting money and what should we do first?"
---

# Review Cloud Cost

## Purpose
Turn a cost dataset into a prioritized, owned list of savings actions that do not compromise reliability, and close the allocation gaps that hide who spends what.

## When to use
- A bill export, cost explorer extract or resource inventory is available.
- Spend grew faster than usage or budget.
- A quarterly or monthly FinOps review is due.
- Commitment (reserved/savings plan style) purchases are being considered.

## When not to use
- Estimating the cost of a system not yet built. Use `cloud-cost-estimate`.
- Forecasting resource needs for growth. Use `capacity-planning`.
- Requesting next year's budget. Use `budget-proposal`.

## Inputs
Required:
- Cost data at least by service and by resource or tag, for a period of at least one month (ideally three).

Optional, improves quality:
- Utilization metrics (CPU, memory, storage IOPS, request volume), environment tags, existing commitments and their coverage/utilization.
- Business drivers (active users, transactions) for unit-cost analysis.
- Reliability constraints (SLOs, DR requirements) that justify redundancy.

If no cost data is given, ask for it. Never invent amounts; compute only from provided data and label estimates as ranges with `[ASSUMPTION]`.

## Process
1. Summarize spend: total, trend, top 10 services and resources, share by environment and team; flag unallocated (untagged) spend percentage.
2. Find waste: idle or orphaned resources (unattached disks, unused IPs, idle load balancers, stopped-but-billed instances, old snapshots), non-production running 24/7, over-retained logs.
3. Rightsizing: compare provisioned versus used capacity; recommend smaller sizes, autoscaling or newer generation types; keep headroom consistent with SLOs.
4. Pricing model: commitment coverage and utilization, candidates for commitments based on steady baseline only, spot/preemptible for fault-tolerant workloads.
5. Storage and data: tiering and lifecycle policies, compression, retention alignment with policy, backup duplication.
6. Network: cross-zone and cross-region transfer, egress, NAT/gateway processing, CDN caching.
7. Architecture-level: managed service vs self-hosted, chatty designs, over-provisioned databases, license-included vs bring-your-own.
8. Unit economics: cost per transaction/user/tenant where drivers exist.
9. Prioritize actions by savings (from data), effort and risk; assign an owner and a verification metric.
10. Recommend governance: tagging policy enforcement, budgets and anomaly alerts, showback/chargeback.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `capacity-planning` for demand-based sizing, `iac-review` to enforce tagging and sizing in code, or `budget-proposal` for the next budget cycle.

## Output format
```markdown
# Cloud Cost Review: <scope, period>
## Spend Summary
- Total / trend / unallocated share
| Rank | Service/resource | Cost | Share | Trend |
## Savings Backlog
| # | Action | Category | Evidence | Est. savings | Effort | Risk | Owner |
## Commitment Recommendation
## Governance Gaps
## Open Questions / Assumptions
```

## Quality checklist
- [ ] Every amount traces to the provided data or is a labeled estimate range.
- [ ] Rightsizing respects SLO and DR constraints.
- [ ] Commitments are sized only on stable baseline usage.
- [ ] Each action has an owner and a way to verify the saving.
- [ ] Unallocated spend is quantified and addressed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Buying commitments before rightsizing, locking in waste. Rightsize first.
- Cutting redundancy that exists for DR or SLOs. Check the reason before removing.
- Counting list-price savings when discounts apply. Use effective rates from the data.

## Example
Input: 3-month export: compute 55%, database 20%, storage 12%; 30% of spend untagged; non-prod VMs run 24/7.

Excerpt of output:
| # | Action | Evidence | Est. savings | Effort | Risk |
|---|---|---|---|---|---|
| 1 | Schedule non-prod compute off nights/weekends | Non-prod VMs 24/7 in data | ~ up to 60% of non-prod compute `[ASSUMPTION: 12h x 5d usage]` | Low | Low |
| 2 | Enforce owner/env tags at creation | 30% untagged | Enables allocation | Medium | Low |
