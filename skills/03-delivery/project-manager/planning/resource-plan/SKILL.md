---
name: resource-plan
description: "Builds a project resource plan showing required roles and skills over time, allocation per person or role per period, over-allocations, capacity gaps and options to close them (hire, contract, reprioritize, reschedule). Use when a schedule exists and the team must be staffed, when people are shared across projects, or when a skill gap threatens the plan."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Build a resource plan"
  related: "schedule-plan, wbs, budget-plan, raci-matrix, onboarding-plan-30-60-90"
  prompt: "Build a resource plan for the next 6 months of our payment gateway project; here is the schedule and the team list with availability."
---

# Build a Resource Plan

## Purpose
Show whether the project has the right skills at the right time in the right quantity, and make gaps and over-allocations visible early enough to act.

## When to use
- After the schedule draft, to staff the project and validate feasibility.
- When team members are shared across projects or have limited availability.
- When a new phase needs different skills (e.g. migration, testing, hypercare).

## When not to use
- Deciding who is responsible or accountable for deliverables. Use `raci-matrix`.
- Long-term organizational capacity or team design. Use `team-topology`.
- Iteration capacity planning inside a team. Use `iteration-planning`.

## Inputs
Required:
- Schedule or phase plan with work packages and time periods.
- Required roles/skills per work package, or enough scope to derive them.

Optional, improves quality:
- Named team members with availability (% or hours), holidays, other commitments.
- Rate cards (for budget linkage), hiring or contracting lead times.

If neither the schedule nor the required roles are given, ask for them. Never assume a person's availability; mark `[UNKNOWN]`.

## Process
1. Derive demand: for each period (week or month), required FTE per role/skill from the schedule and estimates.
2. Capture supply: named people or open positions per role with realistic availability (deduct meetings, support duties, leave; typical productive share 70-85%, state what you use).
3. Build the allocation matrix per period and calculate demand minus supply.
4. Flag over-allocations (>100%) and gaps (demand without supply), and single points of failure (critical skills held by one person).
5. For each gap, propose options with lead time and cost/impact: internal transfer, hire, contractor, vendor, scope reduction, reschedule, training.
6. Check alignment with the critical path: gaps on critical activities have priority.
7. Plan onboarding time for new members and knowledge transfer for leavers.
8. Record assumptions and the review cadence.
9. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `budget-plan` to cost the allocation, or `raci-matrix` to clarify responsibilities.

## Output format
```markdown
# Resource Plan: <project>
Period unit <week/month> | Productive share assumption <x%>
## Demand vs Supply (FTE)
| Role / skill | P1 demand | P1 supply | P2 demand | P2 supply | ... |
## Allocation by Person
| Person / position | Role | P1 % | P2 % | ... | Other commitments |
## Gaps and Over-Allocations
| Period | Role | Gap (FTE) | On critical path? | Option | Lead time | Decision owner |
## Single Points of Failure
## Onboarding and Knowledge Transfer
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Demand is derived from the schedule, not from the current team size.
- [ ] Availability is realistic and the productive-share assumption is stated.
- [ ] No person exceeds 100% without being flagged.
- [ ] Every gap has at least one option and a decision owner.
- [ ] Personal data is limited to what planning needs (no reasons for leave or health data).
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Counting shared experts as full-time. Confirm their real allocation with their line manager.
- Ignoring ramp-up time for new joiners and contractors.
- Planning only headcount and missing specific skills (e.g. a single DBA for three migrations).

## Example
Input: "Months 3-4 need 2 QA engineers; one QA is 50% on another project."

Excerpt of output:
| M3 | QA engineer | 1.5 FTE | Yes (system test) | Contract tester, 4-week lead time | Delivery manager |
- Single point of failure: payment scheme certification knowledge held by one developer.
