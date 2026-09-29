---
description: Builds a deliverable-oriented work breakdown structure that decomposes project scope into a numbered hierarchy of work packages, with a WBS dictionary covering description, owner, acceptance and dependencies. Use when scope is agreed and must be broken down for estimation, scheduling, resourcing and progress tracking.
related: scope-statement, estimation-three-point, schedule-plan, resource-plan, task-breakdown
prompt: Create a WBS for the mobile banking app redesign using this scope statement.
---

# Build a Work Breakdown Structure

## Purpose
Decompose the full project scope into manageable, estimable and assignable work packages so that nothing in scope is missed and nothing out of scope is planned.

## When to use
- After the scope statement is agreed, before estimation and scheduling.
- When a plan exists but work is unclear or overlaps between teams.
- When preparing a bottom-up estimate for a bid or budget.

## When not to use
- Splitting a single user story into developer tasks. Use `task-breakdown`.
- Splitting epics into backlog items. Use `epic-breakdown`.
- Scope itself is not agreed. Use `scope-statement` first.

## Inputs
Required:
- Scope statement, deliverable list or equivalent description.

Optional, improves quality:
- Organizational WBS templates, standard phases, lifecycle model.
- Team structure, vendors, contract boundaries.

If no deliverable description is available, ask for it.

## Process
1. Set level 1 as the project and level 2 by major deliverables (or by phase if the organization requires it; keep one principle per level).
2. Always include a Project Management branch (planning, governance, reporting, closure) and cross-cutting work (testing, migration, training, deployment, hypercare).
3. Decompose until each work package is independently estimable, assignable to one owner, and fits a reporting period (heuristic: 8-80 hours or up to one iteration).
4. Name elements as nouns/deliverables, not verbs.
5. Apply the 100% rule: children add up to exactly the parent's scope; no out-of-scope work.
6. Number elements hierarchically (1, 1.1, 1.1.1).
7. Write a WBS dictionary entry for each work package: description, acceptance, owner role, key dependencies, assumptions.
8. Flag packages with high uncertainty for three-point estimation.
9. Trace every scope deliverable to at least one work package and list any gaps.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `estimation-three-point` to estimate the work packages, then `schedule-plan`.

## Output format
```markdown
# WBS: <project>
## Hierarchy
1 <Project>
  1.1 Project Management
    1.1.1 Planning and baseline
  1.2 <Deliverable A>
    1.2.1 <Work package>
## WBS Dictionary
| WBS ID | Name | Description | Acceptance | Owner role | Dependencies | Uncertainty |
## Scope Traceability
| Scope deliverable | WBS IDs |
## Gaps and Open Questions
```

## Quality checklist
- [ ] The 100% rule holds at every level.
- [ ] All elements are nouns; no activity verbs at package level.
- [ ] Project management, testing, migration, training and deployment are present or explicitly excluded.
- [ ] Every work package has a single owner role and acceptance.
- [ ] Every scope deliverable traces to a package.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mixing organizational units, phases and deliverables at the same level. Choose one decomposition principle per level.
- Decomposing too deep, turning the WBS into a task list. Stop at work packages.
- Forgetting integration and non-functional work, which then surfaces as unplanned effort.

## Example
Input: "Mobile banking redesign: new login, dashboard, transfers; accessibility compliance."

Excerpt of output:
1.3 Transfers module
  1.3.1 Transfer UI designs (approved)
  1.3.2 Transfer API adaptations
  1.3.3 Transfer test suite and results
1.6 Accessibility conformance (WCAG 2.2 AA audit report)
- Gap: Is app-store release management in scope?
