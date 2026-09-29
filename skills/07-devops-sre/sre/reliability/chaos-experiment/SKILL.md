---
description: "Designs a controlled chaos experiment: steady-state definition, falsifiable hypothesis, fault to inject, blast radius and progressive scope, abort conditions and rollback, observation plan, prerequisites and a findings record. Use when a team wants to verify resilience claims (failover, retries, timeouts, autoscaling), prepare for a game day, or validate a disaster recovery or degradation design before relying on it."
related: "resilience-review, dr-plan, slo-definition, runbook, observability-plan"
prompt: "Design a chaos experiment to check that our order service survives losing one of three Redis replicas without customer-visible errors."
---

# Design a Chaos Experiment

## Purpose
Turn a resilience assumption into a safe, falsifiable experiment with a bounded blast radius and clear abort rules, so the team learns how the system really behaves under failure before customers find out.

## When to use
- A resilience mechanism exists on paper (failover, retry, circuit breaker, autoscaling) but has never been exercised.
- A game day or failure-injection program is being planned.
- A recent incident suggests a hidden dependency or weak fallback that should be confirmed.

## When not to use
- The architecture has not been reviewed for failure modes yet. Use `resilience-review` first to find what to test.
- The goal is a full site or region recovery procedure. Use `dr-plan` (its tests can then use this skill).
- The system is currently unstable or in an incident. Stabilize first; experiments need a known steady state.

## Inputs
Required:
- The target system and the resilience claim to test.
- The environment where the experiment may run and who approves it.

Optional, improves quality:
- SLOs and dashboards that define normal behavior.
- Architecture and dependency map, known failure history, existing runbooks.
- Available fault injection capabilities and change-management rules.

If the claim or the permitted environment is unknown, ask. Never propose production injection without explicit approval and an abort mechanism.

## Process
1. State the resilience claim in the user's words, then define the steady state as measurable signals (e.g. success ratio, p99 latency, queue lag) with their normal range, preferably SLIs.
2. Write a falsifiable hypothesis: "When <fault> happens to <target>, <steady-state signals> stay within <range>, because <mechanism>."
3. Choose the fault to inject and its realism: instance or pod termination, dependency latency or errors, network partition, resource exhaustion, zone loss, clock skew, expired credential.
4. Bound the blast radius: environment, share of traffic or hosts, duration, time window, and a progressive plan (smallest scope first, widen only after a pass).
5. Define abort conditions tied to user impact (e.g. error budget burn above a threshold, SLI below a floor) and the rollback: how the fault is stopped and how fast recovery is verified.
6. List prerequisites: monitoring in place and watched, on-call informed, stakeholders notified, no concurrent changes, approved change record, a verified manual recovery path.
7. Plan observations: which dashboards, logs and traces to capture, who watches what, and what timeline notes to take during the run.
8. Define roles: experiment lead, operator injecting the fault, observer, and the person with authority to abort.
9. Prepare the findings record: hypothesis confirmed or refuted, observed behavior vs. expected, surprises, and follow-up actions with owners.
10. Label every inference `[ASSUMPTION]`, list open questions, and suggest next skills: `runbook` for gaps found in response, `resilience-review` for design fixes, or `postmortem` format if the experiment caused unexpected impact.

## Output format
```markdown
# Chaos Experiment: <name>
Owner: <lead> · Environment: <env> · Window: <date/time or [TBD]> · Approval: <who>

## Claim and Hypothesis
- Claim: ...
- Steady state: <signals and normal range>
- Hypothesis: When ..., then ..., because ...

## Fault Injection
| Fault | Target | Method (neutral) | Duration |

## Blast Radius and Progression
## Abort Conditions and Rollback
## Prerequisites Checklist
## Roles
## Observation Plan
## Findings (filled after run)
| Expected | Observed | Result | Follow-up action | Owner |
## Assumptions and Open Questions
```

## Quality checklist
- [ ] The hypothesis is falsifiable and references measurable steady-state signals.
- [ ] Blast radius is bounded in scope, traffic share and duration, with progressive widening.
- [ ] Abort conditions are tied to user impact and a tested way to stop the fault exists.
- [ ] Prerequisites include monitoring, notification, approval and no concurrent changes.
- [ ] A named person has authority to abort.
- [ ] The findings record separates observed facts from interpretation.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Running an experiment without a steady state. Without a baseline, "it looked fine" is not evidence.
- Starting at full scope in production. Begin with the smallest radius, often in a pre-production environment, then widen.
- Treating a refuted hypothesis as a failure of the exercise. Finding a weakness is the goal; record it and fix it.

## Example
Input: "Order service should survive losing one of three Redis replicas."

Excerpt of output:
- Steady state: order API success ratio ≥ 99.9% and p99 < 300 ms over 5-minute windows `[ASSUMPTION: from SLO]`.
- Hypothesis: When one Redis replica is terminated, success ratio and p99 stay within steady state, because the client reconnects to the remaining replicas within 5 s.
- Blast radius: staging first; then production, one replica, 10 minutes, off-peak window.
- Abort: success ratio < 99.5% for 2 consecutive minutes, or any cache write failure alert → restart replica, confirm recovery on dashboard.
