---
description: "Recommends a deployment strategy (recreate, rolling, blue-green, canary, shadow, feature flags or a combination) for a specific service by weighing risk, statefulness, database changes, traffic control, cost and rollback speed. Use when a team must decide how a release reaches users, or when current releases cause downtime or risky big-bang cutovers."
related: "pipeline-design, rollback-plan, release-plan, schema-migration-plan, slo-definition"
prompt: "We deploy our payment service with a 20-minute maintenance window. Which deployment strategy should we move to so we get zero downtime?"
---

# Choose a Deployment Strategy

## Purpose
Select a rollout mechanism that matches the service's risk and constraints, with explicit promotion criteria and a rollback path, so releases stop being all-or-nothing events.

## When to use
- A service is moving from maintenance windows to zero-downtime releases.
- A high-risk change needs progressive exposure.
- The team is debating blue-green versus canary versus feature flags.

## When not to use
- The whole pipeline needs designing. Use `pipeline-design`.
- The question is how to undo a specific release. Use `rollback-plan`.
- The question is sequencing a multi-team release. Use `release-plan`.

## Inputs
Required:
- Service description: runtime platform, statefulness, traffic entry (load balancer, gateway, mesh, client apps), database coupling.
- Business tolerance: acceptable downtime and user-visible error budget during release.

Optional, improves quality:
- Traffic volume (needed for canary statistical meaning), SLOs, available metrics.
- Infrastructure budget (blue-green doubles capacity temporarily).
- Existing feature flag capability, session handling, backward compatibility of APIs and schema.

If the platform or the downtime tolerance is unknown, ask. Other gaps become open questions.

## Process
1. Establish constraints: can two versions run at once? Are the API and database schema backward compatible? Are there sticky sessions, long-lived connections, background consumers or singleton jobs?
2. If two versions cannot coexist, first plan expand-and-contract for schema and API changes; otherwise only recreate is safe.
3. Evaluate candidates against: downtime, blast radius, rollback time, infrastructure cost, traffic-control requirement, observability requirement, operational complexity.
4. Check canary feasibility: enough traffic to detect a regression within the step duration; per-version metrics available.
5. Separate deploy from release: decide whether feature flags should gate user exposure independently of binaries.
6. Define promotion steps (e.g. 1% → 10% → 50% → 100%) with duration and automated analysis criteria (error rate, latency percentiles, saturation, business KPI).
7. Define abort criteria and the rollback mechanism per strategy (traffic switch, rollout undo, flag off).
8. Address stateful parts: queue consumers, scheduled jobs, caches, migrations; state who runs them during overlap.
9. Recommend one strategy (or combination) with rationale and prerequisites to build.
10. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `rollback-plan` for the detailed undo path, `release-plan` for sequencing the release, or `slo-definition` if promotion criteria lack agreed SLOs.

## Output format
```markdown
# Deployment Strategy: <service>
## Constraints
- Version coexistence: yes/no – reason
- Schema/API compatibility: ...
## Options Compared
| Strategy | Downtime | Blast radius | Rollback time | Extra cost | Prerequisites | Fit |
## Recommendation
<strategy> because ...
## Rollout Steps
| Step | Exposure | Duration | Promote if | Abort if |
## Rollback Mechanism
## Stateful Components During Overlap
## Prerequisites / Open Questions
```

## Quality checklist
- [ ] Version coexistence and schema compatibility were checked before recommending a non-recreate strategy.
- [ ] Promotion and abort criteria are metric-based with thresholds or `[TBD]`.
- [ ] Canary is recommended only if traffic allows meaningful comparison.
- [ ] Background jobs and consumers are covered, not only HTTP traffic.
- [ ] Cost impact of duplicate capacity is stated qualitatively without invented numbers.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Choosing blue-green while sharing one database with a breaking migration. Use expand-and-contract first.
- Canary with low traffic, where 1% means a handful of requests. Use longer steps or synthetic traffic.
- Rolling back binaries while a feature flag or data migration has already changed state. Plan both.

## Example
Input: "Payment API on Kubernetes behind an ingress, ~300 rps, 20-minute maintenance window today, schema changes every few releases."

Excerpt of output:
- Recommendation: canary via weighted routing, combined with expand-and-contract migrations and feature flags for new payment methods.
- Step 1: 5% for 15 min; promote if 5xx rate and p99 latency of canary are not worse than stable by more than `[TBD]`; abort on any payment-authorization error spike.
