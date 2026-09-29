---
name: go-no-go
description: "Prepares and records a go/no-go decision for a release or cut-over: agreed criteria, evidence per criterion, open risks with owners, conditions for a conditional go, and a decision record with approvers. Use when a release, migration or launch needs a formal decision, when someone asks for a go/no-go meeting pack or checklist, or when the team must document why it shipped or postponed."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Run a go/no-go decision"
  related: "release-quality-gate, release-plan, rollback-plan, decision-log, test-summary-report"
  prompt: "Prepare the go/no-go for tomorrow's CRM migration cut-over. Here are the test results, open defects and the rehearsal notes."
---

# Run a Go/No-Go Decision

## Purpose
Make the release decision on evidence against criteria agreed in advance, and record it with its conditions and owners, so the decision is defensible and not driven by schedule pressure or the loudest voice.

## When to use
- A release, data migration, cut-over or launch needs a formal decision point.
- Several parties (business, QA, operations, security) must sign off.
- A decision must be documented for audit or change management.

## When not to use
- Only the quality evidence from testing is needed. Use `release-quality-gate` or `test-summary-report`.
- The release schedule and contents are still being planned. Use `release-plan`.
- A general decision among options, not a release gate. Use `decision-matrix`.

## Inputs
Required:
- What is being decided (release, migration, launch) and the planned window.
- The evidence available: test results, open defects, rehearsal or staging results, readiness of operations and support.

Optional, improves quality:
- Previously agreed go/no-go criteria, organization change policy.
- Rollback plan and point of no return, business constraints on postponing.
- List of approvers and their roles.

If there is no evidence at all, ask for it; a go/no-go without evidence is a status meeting. Missing criteria are proposed and marked `[PROPOSED]` for approval.

## Process
1. Fix the criteria before looking at the evidence: functional quality, open defects by severity, non-functional results (performance, security), data migration reconciliation, operational readiness (monitoring, runbooks, on-call), support and user readiness, rollback readiness, business readiness, external dependencies.
2. For each criterion, define the pass threshold and whether it is mandatory (any failure = no-go) or weighable.
3. Map each piece of evidence to a criterion and rate it Met / Partially met / Not met / No evidence; quote the source (report, run, person) and its date.
4. Treat "no evidence" as not met; do not accept verbal assurance for mandatory criteria without noting it.
5. List open risks and accepted deviations with owner, mitigation and expiry.
6. Evaluate the cost of no-go as well: business impact of postponing, next available window; state it without inventing figures.
7. Formulate the recommendation: Go, Conditional go (with explicit conditions, owner and deadline for each), or No-go (with what must change and the next decision point).
8. Record the decision: who decided, who was consulted, dissent noted, time, and the rollback decision owner for the window.
9. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest `rollback-plan` if rollback readiness is weak, `release-plan` to reschedule after a no-go, or `decision-log` to file the record.

## Output format
```markdown
# Go/No-Go: <release/cut-over> – <window>
Decision meeting: <date/time> · Decision owner: <name or [TBD]>

## Criteria and Evidence
| # | Criterion | Mandatory | Threshold | Evidence (source, date) | Status |
|---|---|---|---|---|---|

## Open Risks and Accepted Deviations
| Risk/deviation | Impact | Mitigation | Owner | Valid until |

## Cost of Postponing
<qualitative impact, next window>

## Recommendation
Go / Conditional go / No-go – <rationale in 2-3 sentences>
Conditions: <condition – owner – deadline>

## Decision Record
- Decision: ... · Time: ...
- Approvers: ... · Consulted: ... · Dissent: ...
- Rollback decision owner during window: ...
```

## Quality checklist
- [ ] Criteria and thresholds were stated before evidence was rated.
- [ ] Every status cites a source; "no evidence" is not treated as met.
- [ ] Mandatory criteria that are not met lead to no-go or an explicitly accepted deviation with an owner.
- [ ] Conditional go conditions are verifiable, owned and time-bound.
- [ ] Dissent and the rollback decision owner are recorded.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Changing the criteria in the meeting to fit the date. Record any criterion change as a deviation with an owner.
- Conditional go with vague conditions ("monitor closely"). Name the metric, the owner and what triggers rollback.
- Ignoring operations and support readiness because tests passed. Readiness to run the system is part of the gate.

## Example
Input: "CRM migration: 2 open high defects in reporting, reconciliation 99.97% rows matched on rehearsal, support not yet trained."

Excerpt of output:
| # | Criterion | Mandatory | Status |
|---|---|---|---|
| 3 | Data reconciliation = 100% of in-scope records, differences explained | Yes | Partially met: 0.03% unexplained `[source: rehearsal 2 report]` |
| 6 | Support trained on new screens | No | Not met |

Recommendation: No-go unless the unexplained 0.03% is classified before `[TBD]`; if it is explained as out-of-scope archive records, Conditional go with support training completed before business open.
