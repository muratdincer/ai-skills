---
description: Reviews the resilience of a system by walking every critical flow and dependency through its failure modes, and checking timeouts, retries, circuit breakers, bulkheads, idempotency, graceful degradation, data durability and disaster recovery against availability targets (SLO, RTO, RPO). Use before go-live of a critical service, after incidents caused by dependency failures, when adding a new external dependency, or when DR readiness must be demonstrated.
related: chaos-experiment, dr-plan, slo-definition, integration-pattern-selection, architecture-review
prompt: Review the resilience of our checkout flow: it calls pricing, inventory, a payment provider and a fraud service synchronously, and we had two outages last month when the fraud service slowed down.
---

# Review Resilience

## Purpose
Find where a system will fail badly when its parts or dependencies fail, and recommend specific mechanisms so that failures stay contained, degrade gracefully and recover within agreed targets.

## When to use
- A critical service is approaching go-live or a major release.
- Incidents were caused or amplified by a slow or failing dependency (cascading failure, retry storms).
- A new external dependency or a new region/DR setup is added.
- Auditors or customers require evidence of DR readiness.

## When not to use
- The goal is to test resilience in practice. Use `chaos-experiment` after this review.
- A full DR plan with procedures and roles must be written. Use `dr-plan`.
- The concern is throughput under growth rather than failure. Use `scalability-review`.

## Inputs
Required:
- The critical flows and their dependencies (internal services, databases, queues, third parties), with call style (sync/async).
- Availability expectations (SLO, RTO, RPO) or permission to mark them `[TBD]`.

Optional:
- Current timeout/retry/pool settings, deployment topology (zones, regions), incident history and postmortems.
- Dependency SLAs, rate limits, capacity headroom.

If the flows or dependencies are missing, ask for them; do not assume a topology.

## Process
1. Draw the dependency chain for each critical flow and mark sync vs. async, criticality (hard vs. soft dependency) and the compound availability of sync chains.
2. For every dependency enumerate failure modes: unavailable, slow (latency spike), erroring, returning wrong/partial data, throttling, network partition, and for data stores failover and replication lag.
3. Check timeouts: every remote call has one, derived from the caller's own budget; the sum along a chain fits within the user-facing timeout.
4. Check retries: only on idempotent or idempotency-keyed operations, bounded attempts, exponential backoff with jitter, retry budget to prevent storms, no retries at multiple layers compounding.
5. Check isolation: circuit breakers with sensible thresholds and half-open probing, bulkheads (separate pools/queues per dependency), load shedding and rate limiting at entry.
6. Check degradation: what the user gets when each soft dependency fails (cached value, default, queued for later, feature switched off); hard dependencies are minimized.
7. Check data durability and consistency: outbox/transactional messaging, dead-letter queues and replay, reconciliation, backup frequency vs. RPO, tested restores.
8. Check infrastructure resilience: multi-zone redundancy, no single points of failure (including DNS, secrets, CI/CD, identity provider), health checks that reflect real readiness, safe deployment and rollback.
9. Check detection and response: alerts on symptoms, runbooks, on-call ownership, and DR drill evidence against RTO/RPO.
10. Rate each finding by likelihood × impact, propose concrete remediations with parameter suggestions marked `[ASSUMPTION]` until validated, and list experiments to verify them.
11. If the goal continues, suggest `chaos-experiment` to verify findings, `dr-plan` for recovery procedures or `slo-definition` if targets are missing.

## Output format
```markdown
# Resilience Review: <system/flow> – <date>
## Targets
SLO: ... · RTO: ... · RPO: ...
## Dependency Map
| Flow | Dependency | Sync/Async | Hard/Soft | Timeout | Retry | Breaker | Fallback |
|---|---|---|---|---|---|---|---|
## Failure Mode Analysis
| Dependency | Failure mode | Current behavior | Impact | Likelihood | Finding |
|---|---|---|---|---|---|
## Findings and Recommendations
| ID | Severity | Finding | Recommendation | Verification |
|---|---|---|---|---|
## DR Readiness
## Proposed Experiments
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every dependency of each critical flow is analyzed for slow as well as down.
- [ ] Timeout budgets along each sync chain add up within the user-facing limit.
- [ ] Every retry is tied to an idempotent operation and has a bound and backoff.
- [ ] Each soft dependency has a defined degraded behavior.
- [ ] RPO/RTO claims are backed by tested restore or drill evidence, or flagged.
- [ ] Suggested parameter values are marked as assumptions to be validated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Only testing "dependency down". Slow dependencies exhaust thread and connection pools and cause most cascades.
- Retries at client, gateway and service layers multiplying load during an incident.
- Health checks that call downstream dependencies, so one failing dependency takes every instance out of rotation.

## Example
Input: "Checkout calls pricing, inventory, payment and fraud synchronously; fraud slowdowns caused two outages."

Excerpt of output:
| ID | Severity | Finding | Recommendation |
|---|---|---|---|
| R1 | Critical | Fraud call has no timeout; slow responses exhausted the shared HTTP pool and blocked payment calls | Timeout `[ASSUMPTION: 800 ms]`, dedicated pool (bulkhead), circuit breaker; on open, accept low-risk orders and queue for post-authorization review per business rule `[confirm with risk team]` |
| R2 | Major | Payment retries at gateway and service (3 × 3) with no idempotency key | Retry only in service, with provider idempotency key and jittered backoff |
