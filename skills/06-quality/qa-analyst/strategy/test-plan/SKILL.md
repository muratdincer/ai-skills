---
name: test-plan
description: "Writes a test plan for a release, project or feature set, covering test items, scope, approach, environments, schedule, roles, entry/exit and suspension criteria, deliverables and risks, aligned with ISO/IEC/IEEE 29119-3. Use when a release or project needs an agreed testing scope and schedule, or when someone asks for a test plan document."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 06-quality
  role: qa-analyst
  area: strategy
  title: "Write a test plan"
  related: "test-strategy, risk-based-testing, release-quality-gate, test-summary-report, uat-plan"
  prompt: "Prepare a test plan for release 4.2 of the claims portal: new document upload, revised approval workflow, and two bug fixes. Code freeze is in three weeks."
---

# Write a Test Plan

## Purpose
Agree, before testing starts, on what will be tested, how, where, by whom, when, and what "done" means. A good plan makes scope trade-offs and residual risk visible early instead of at the release decision.

## When to use
- A release, project or significant feature set is entering test preparation.
- Several teams or a vendor share testing and need one agreed scope and schedule.
- A contract, audit or regulator expects a documented plan (ISO/IEC/IEEE 29119-3 structure).

## When not to use
- The organization-wide or product-wide approach is not defined yet. Start with `test-strategy`.
- You only need user acceptance planning with business participants. Use `uat-plan`.
- You need load/stress planning. Use `performance-test-plan`.

## Inputs
Required:
- What is being delivered: release scope, features, changes or requirements list.
- Key dates or constraints (target release date, freeze, environment availability), or confirmation that none exist.

Optional, improves quality:
- The applicable test strategy, risk assessment, previous test summary reports.
- Team members and availability, environment and data status, dependencies on other teams.

If the delivery scope is missing, ask for it. Missing dates become `[TBD]`, not guesses.

## Process
1. Identify test items (components, versions, builds) and the features to be tested and not tested, with a reason for each exclusion.
2. Pull or perform a quick risk assessment per feature; use it to set depth (thorough / standard / smoke). Reference `risk-based-testing` if detailed.
3. Define the approach per feature: test levels and types, design techniques, manual vs automated, regression scope.
4. Specify environments, test data and integrations required, with readiness dates and owners.
5. Define entry criteria (build deployed, smoke passed, test data ready, requirements baselined) and exit criteria (execution %, pass rate on critical tests, no open Critical/High defects or approved waivers, coverage of high risks).
6. Define suspension and resumption criteria (e.g. blocking defect in core flow, environment down more than half a day).
7. Build the schedule backwards from the release date: preparation, execution cycles, regression, fix verification, reporting. Add buffer and name the critical path.
8. Assign roles: test manager/lead, testers, developers for fixes, business for UAT, environment owner.
9. List deliverables: test cases, execution logs, defect reports, daily status, test summary report.
10. List planning risks (not product risks) with mitigation and contingency: late builds, shared environments, key-person dependency.
11. Mark unknowns and collect open questions and approvals needed.
12. If the user continues, suggest `risk-based-testing` to prioritize the scope, `uat-plan` for acceptance, or `release-quality-gate` when execution ends.

## Output format
```markdown
# Test Plan: <release / project>
Version: <x.y> | Author: <name> | Approvers: <names or [TBD]>

## 1. Test Items and Scope
| Feature / item | In scope | Depth | Reason if excluded |
## 2. Approach
| Feature | Levels | Types | Techniques | Manual / Automated |
## 3. Environments and Test Data
| Need | Owner | Ready by | Status |
## 4. Entry, Exit, Suspension and Resumption Criteria
## 5. Schedule
| Activity | Start | End | Owner | Dependency |
## 6. Roles and Responsibilities
## 7. Deliverables and Reporting Cadence
## 8. Planning Risks and Contingencies
| Risk | Likelihood | Impact | Mitigation | Contingency |
## 9. Open Questions and Approvals
```

## Quality checklist
- [ ] Every in-scope feature has an approach and depth; every exclusion has a reason.
- [ ] Exit criteria are measurable and consistent with the release quality gate.
- [ ] Schedule includes at least one regression cycle and fix verification time.
- [ ] Environment and data readiness have owners and dates or `[TBD]`.
- [ ] No names, dates or numbers are invented.
- [ ] Planning risks are distinct from product risks.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Exit criteria like "all tests passed". Allow justified waivers and state the decision owner.
- Planning execution only once. Plan for fix-retest and regression cycles.
- Ignoring non-functional needs for changed components (performance of the new upload, accessibility of new screens).

## Example
Input: "Release 4.2 of claims portal: document upload, revised approval workflow, two bug fixes; code freeze in three weeks."

Excerpt of output:
- Depth: Approval workflow = thorough (state transitions, authorization); document upload = thorough (file types, size limits, malware scan); bug fixes = retest + targeted regression.
- Exit: 100% of critical tests executed, 0 open Critical, High only with product owner waiver.
- Planning risk: Scanner service in test environment not confirmed `[TBD: environment owner]`.
