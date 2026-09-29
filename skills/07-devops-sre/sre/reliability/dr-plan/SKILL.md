---
name: dr-plan
description: "Writes a disaster recovery plan for a system: business-driven RTO/RPO per service tier, disaster scenarios, recovery strategy and dependency order, step-by-step failover and failback procedures, roles and declaration authority, communication and a test schedule with evidence. Use when a system lacks a DR plan, when RTO/RPO targets must be set or verified, before an audit, or after a DR test or incident revealed gaps."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Write a disaster recovery plan"
  related: "backup-restore-plan, runbook, chaos-experiment, incident-communication, resilience-review"
  prompt: "Write a DR plan for our core banking API and its PostgreSQL database. Business wants RTO 1 hour and RPO 5 minutes; we run in one region with nightly backups."
---

# Write a Disaster Recovery Plan

## Purpose
Define how a system is restored after a major disruption within agreed recovery time and data loss limits, with procedures precise enough to execute under stress and tests that prove the targets are achievable.

## When to use
- A critical system has no DR plan, or the plan has never been tested.
- RTO/RPO targets must be agreed with the business or checked against the current architecture.
- An audit, regulator or customer requires documented and tested recovery capability.

## When not to use
- The scope is only database backups and restores. Use `backup-restore-plan`.
- A single failure mode needs a response procedure. Use `runbook`.
- A disaster is happening now. Use `incident-response`, then this plan's procedures if one exists.

## Inputs
Required:
- The system in scope, its components and where they run.
- Business impact of downtime and data loss, or targets the business has stated.

Optional, improves quality:
- Current backup, replication and infrastructure-as-code setup; dependency map including third parties.
- Regulatory or contractual obligations (e.g. business continuity requirements under ISO 22301 or sector rules).
- Previous DR tests and incidents; budget constraints.

If the business impact or targets are unknown, ask who owns them; do not set RTO/RPO on their behalf. Proposed values are marked `[PROPOSED]` and need business sign-off.

## Process
1. Inventory components and dependencies (compute, data stores, queues, DNS, identity, secrets, certificates, third-party APIs) and tier each service by business criticality.
2. Agree RTO and RPO per tier with the business owner; record who approved and flag targets that are unapproved.
3. Define disaster scenarios: zone loss, region loss, data corruption or accidental deletion, ransomware or compromised account, critical third-party outage, loss of key people or access.
4. Assess the current capability per scenario: achievable RTO/RPO with today's backups, replication and automation; list gaps against targets.
5. Choose a recovery strategy per tier (backup and restore, pilot light, warm standby, active-active) and show the trade-off between cost, complexity and targets.
6. Write the recovery order from dependencies: foundations first (network, identity, secrets, DNS), then data, then services, then traffic switch.
7. Write step-by-step failover procedures with expected duration, owner and verification per step, including data consistency checks and how to handle in-flight transactions.
8. Write failback procedures and the criteria for returning to the primary site; failback is often riskier than failover.
9. Define roles and declaration: who can declare a disaster, decision criteria, escalation contacts, and how the team gets access if the primary identity provider is down (break-glass accounts stored securely).
10. Define communication: internal, customers, regulators, with templates and timing.
11. Define the test program: tabletop, component restore, full failover; frequency, success criteria (measured RTO/RPO) and evidence kept.
12. Label every inference `[ASSUMPTION]`, list open questions, and suggest next skills: `backup-restore-plan` for data details, `runbook` per procedure, `chaos-experiment` for component tests, `incident-communication` for templates.

## Output format
```markdown
# Disaster Recovery Plan: <system>
Owner: <name> · Business approver: <name or [UNKNOWN]> · Last tested: <date or never>

## Scope and Service Tiers
| Service | Tier | RTO | RPO | Approved by |

## Dependencies and Recovery Order
## Scenarios and Current Capability
| Scenario | Achievable RTO/RPO today | Gap | Strategy |

## Failover Procedure
| # | Step | Owner | Expected duration | Verification |

## Failback Procedure and Criteria
## Roles, Declaration and Access
## Communication Plan
## Test Program
| Test type | Frequency | Success criteria | Evidence |

## Assumptions, Risks and Open Questions
```

## Quality checklist
- [ ] Every RTO/RPO has a named business approver or is marked `[PROPOSED]`.
- [ ] Current capability is compared with targets and gaps are explicit.
- [ ] Recovery order follows dependencies, including identity, secrets and DNS.
- [ ] Each procedure step has an owner, expected duration and verification.
- [ ] Data corruption and compromised-account scenarios are covered, not only infrastructure loss.
- [ ] A test program with measurable success criteria and evidence is defined.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Replication treated as backup. Replication copies corruption and deletions instantly; point-in-time recovery or immutable backups are needed.
- A plan that depends on the failed region's tools (identity, secrets vault, CI/CD, runbook wiki). Keep recovery access independent.
- RTO counted from the failure, while the plan ignores detection and declaration time. Include both.

## Example
Input: "Core banking API + PostgreSQL, target RTO 1 h / RPO 5 min, single region, nightly backups."

Excerpt of output:
| Scenario | Achievable today | Gap | Strategy |
|---|---|---|---|
| Region loss | RTO `[UNKNOWN]` (never tested), RPO up to 24 h | RPO misses 5-minute target | Warm standby with cross-region streaming replication + point-in-time recovery |
| Data corruption | RPO up to 24 h | Same | Continuous WAL archiving to immutable storage |

Open question: who in the business approved RTO 1 h / RPO 5 min, and is the standby cost accepted?
