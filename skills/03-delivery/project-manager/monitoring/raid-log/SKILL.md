---
description: Creates or updates a RAID log that tracks Risks, Assumptions, Issues and Dependencies in one place with consistent IDs, owners, dates, status and cross-links, and produces a short summary of what changed and what needs attention. Use for ongoing project control, when raw notes, meeting outputs or emails must be triaged into the right RAID category, or before status reporting.
related: risk-register, issue-management, dependency-map, decision-log, project-status-report
prompt: Update our RAID log with the points from today's steering meeting notes and tell me what needs escalation.
---

# Maintain a RAID Log

## Purpose
Keep a single, current control log of risks, assumptions, issues and dependencies, correctly classified and owned, so that nothing raised in meetings or emails gets lost and reporting draws from one source.

## When to use
- Weekly project control and before status reports.
- After meetings, workshops or escalations that raised new concerns.
- When a legacy log is messy and needs cleanup and re-classification.

## When not to use
- A detailed, scored risk analysis for a gate. Use `risk-register`.
- Managing one significant issue through resolution. Use `issue-management`.
- Recording decisions with rationale. Use `decision-log`.

## Inputs
Required:
- New raw items (notes, emails, meeting outputs) and/or the existing RAID log.

Optional, improves quality:
- Project plan and milestones, organizational scales, escalation thresholds.

If neither new items nor an existing log is given, ask for them.

## Process
1. Classify each raw item using tests: Risk = uncertain future event; Assumption = believed true, not yet verified; Issue = happening now and affecting the project; Dependency = something needed from or by another party.
2. Deduplicate against existing entries; update rather than duplicate.
3. Write each entry precisely (risks as cause-event-effect, issues as current impact, assumptions with validation method, dependencies with need-by date).
4. Assign owner, due or review date, priority (H/M/L or score) and status.
5. Cross-link: invalid assumptions become issues or risks; slipped dependencies become issues; realized risks become issues.
6. Age items: flag entries without update for more than two review cycles and overdue actions.
7. Identify escalation candidates: High priority with no viable action at PM level, or overdue on the critical path.
8. Close items with a closure note and date; do not delete.
9. Produce a change summary: new, changed, closed, escalations.
10. Label every inferred element `[ASSUMPTION]` and move it to assumptions or open questions. If the user's goal continues, suggest the next skill: `issue-management` for issues that need a resolution path, or `project-status-report` to report the change summary.

## Output format
```markdown
# RAID Log: <project> – updated <date>
## Change Summary
- New: ... | Closed: ... | Escalate: ...
## Risks
| ID | Description | P | I | Owner | Response / action | Due | Status |
## Assumptions
| ID | Assumption | Validation method | Owner | Validate by | Status (Open/Valid/Invalid) |
## Issues
| ID | Description | Impact | Priority | Owner | Action | Due | Status |
## Dependencies
| ID | Item | Provider | Receiver | Need-by | Status |
## Stale or Overdue Items
```

## Quality checklist
- [ ] Every item passes its category test.
- [ ] No duplicates; updates are applied to existing IDs.
- [ ] Every open item has an owner and a date.
- [ ] Transitions (assumption → issue, risk → issue) are recorded with links.
- [ ] Escalation candidates are explicit.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Logging issues as risks to avoid alarming sponsors. If it is happening, it is an issue.
- Assumptions without a validation date, which silently turn into issues.
- Letting the log grow without closure; stale items hide the real ones.

## Example
Input: "Steering notes: vendor says API docs next week; we're assuming 2 test environments; data center move may clash with cutover."

Excerpt of output:
- D-07 API documentation from vendor – Need-by `[date]` – Status Requested.
- A-04 Two test environments available from sprint 4 – Validate by `[TBD]` with Infrastructure – Open.
- R-12 Because the data center move is scheduled near cutover, infrastructure changes may conflict, delaying go-live – P3/I4 – Owner Infra lead.
