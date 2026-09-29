---
description: "Plans user acceptance testing: objectives, business participants and their roles, scenario coverage, environment and data readiness, schedule, defect handling, entry/exit criteria and the formal sign-off route. Use when a release, project phase or vendor delivery needs business acceptance, when someone asks how to organize UAT, or when business users must confirm a solution supports their real work before go-live."
related: uat-scenarios, test-plan, acceptance-certificate, requirements-sign-off, release-quality-gate
prompt: "Plan UAT for the new invoicing module: finance and sales users will test for two weeks before the go-live."
---

# Plan UAT

## Purpose
Give business users a well-prepared, time-boxed acceptance window with clear responsibilities and criteria, so the acceptance decision reflects real business work and is formally recorded, not a rushed second system test.

## When to use
- A solution or release is about to go live and business owners must accept it.
- A vendor or contract delivery requires formal acceptance before payment or handover.
- Previous UAT rounds were chaotic (unprepared users, broken data, unclear sign-off) and need structure.

## When not to use
- You need the business scenarios themselves. Use `uat-scenarios`.
- You are planning system or integration testing done by the QA team. Use `test-plan`.
- You need the go/no-go assessment against exit criteria. Use `release-quality-gate`.

## Inputs
Required:
- What is being accepted (scope: features, processes, release) and the target go-live or acceptance date.
- The business areas affected.

Optional, improves quality:
- Named business owners and key users, their availability, contract acceptance terms.
- Test environment status, data sources, system test results, known open defects.

If scope or the target date is missing, ask for them. Record participant names you do not have as `[TBD]`; never invent people or dates.

## Process
1. State UAT objectives in business terms: which processes must be proven to work end to end, and which decisions the sign-off enables (go-live, payment, handover).
2. Define scope: business processes and roles in scope, out of scope, and items already accepted elsewhere. Flag scope that has not passed system test as a risk.
3. Identify participants: acceptance owner (signs), business process owners, key users per role, UAT coordinator, support from QA/dev for defect handling. Check that every in-scope role has at least one real user.
4. Set entry criteria: system test exit met, no open Critical defects in scope, environment deployed with the release candidate, test data and user accounts ready, scenarios reviewed by business, participants briefed.
5. Plan environment and data: production-like configuration, integrations (real or stubbed, stated explicitly), masked or synthetic personal data, account and permission setup per role.
6. Build the schedule: kickoff and training, execution windows per process area, daily defect review, retest slots, buffer, sign-off meeting. Respect users' business calendar (month end, peak season).
7. Define defect handling: how users report (minimum fields), severity scale in business language, triage cadence, who decides fix-now vs accept-with-workaround vs defer.
8. Set exit criteria and the sign-off rule: required scenario pass rate, no open Critical/High without an accepted workaround, deferred items listed with owners, who signs and in what form.
9. List risks (user availability, data readiness, unstable environment, scope creep through "new requirements" raised in UAT) with mitigations; route new requirements to change control, not the defect list.
10. If the user continues, suggest `uat-scenarios` to write the scenarios, `acceptance-certificate` for the sign-off document, or `release-quality-gate` for the release decision.

## Output format
```markdown
# UAT Plan: <solution/release>
| Field | Value |
|---|---|
| Acceptance owner | <name/role or [TBD]> |
| UAT window | <from–to or [TBD]> |
| Go-live / acceptance date | <date> |
| Environment | <name, build> |

## Objectives
- ...
## Scope
| Business process | Roles | In/Out | Notes |
|---|---|---|---|
## Participants and Responsibilities
| Role | Person | Responsibility | Availability |
|---|---|---|---|
## Entry Criteria
- [ ] ...
## Environment and Data
- ...
## Schedule
| Day/Date | Activity | Participants |
|---|---|---|
## Defect Handling
- Reporting fields / severity scale / triage cadence / decision owner
## Exit Criteria and Sign-off
- ...
## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Objectives and exit criteria are in business terms and say which decision the sign-off enables.
- [ ] Every in-scope role has a named or `[TBD]` real business participant, not QA staff.
- [ ] Entry criteria prevent starting UAT on an untested or unstable build.
- [ ] Personal data in the UAT environment is masked or synthetic, or the gap is flagged.
- [ ] The sign-off owner and form are explicit.
- [ ] New requirements raised during UAT are routed to change control.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Using UAT as the first real test. Enforce system-test exit as an entry criterion; otherwise users spend the window finding basic bugs.
- Letting QA execute "on behalf of" business users. Acceptance must come from the people who own the work.
- Scheduling UAT during the business's peak period. Check the business calendar before fixing dates.

## Example
Input: "UAT for the new invoicing module, finance and sales, two weeks before go-live on the 1st."

Excerpt of output:
- Objective: prove that finance can issue, correct and cancel invoices end to end and that sales sees correct invoice status on orders; sign-off enables go-live.
- Entry criterion: system test exit met; no open Critical defects in invoicing; customer data masked.
- Risk: window overlaps month-end close (High impact) — mitigation: run finance scenarios in week 1 `[confirm close dates]`.
