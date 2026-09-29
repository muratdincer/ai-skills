---
description: Drafts a project charter that formally authorizes a project, stating purpose, measurable objectives, high-level scope, key stakeholders, budget envelope, milestones, risks and the project manager's authority. Use when a project has been approved or is seeking approval and needs a one-document mandate signed by a sponsor.
related: scope-statement, stakeholder-register, kickoff-deck, business-model-canvas, governance-framework
prompt: Write a project charter for migrating our on-prem CRM to a SaaS platform; sponsor is the Sales VP, target go-live is Q2.
---

# Write a Project Charter

## Purpose
Produce a concise, sponsor-signed mandate that authorizes the project, anchors it to a business justification and defines the boundaries within which the project manager may act without escalation.

## When to use
- A business case or request has been approved and a project must be formally started.
- A project is already running informally and needs an explicit mandate, sponsor and authority limits.
- A re-baseline after a major change in objectives or sponsor.

## When not to use
- Detailed scope with deliverables and acceptance criteria is needed. Use `scope-statement`.
- The investment decision itself is still open. Use `feasibility-study` or `cost-benefit-analysis`.
- The work is a small change inside an existing product backlog. Use `feature-brief`.

## Inputs
Required:
- Project name and the business need or approved business case (any format).
- Sponsor name or role.

Optional, improves quality:
- Budget envelope, target dates and their drivers, known constraints.
- Organizational charter template, governance forums, approval thresholds.
- Related programs, contracts or regulatory drivers.

If the business need or sponsor is missing, ask for it. Everything else goes to open questions.

## Process
1. Restate the business need as a problem/opportunity and link it to a strategic objective or driver (regulation, cost, revenue, risk).
2. Define 3-5 SMART objectives. Separate project objectives (delivered at close) from business benefits (realized later, owned by the business).
3. Write high-level scope in and out, and the major deliverables. Keep detail for the scope statement.
4. List key milestones with dates only where given; otherwise mark `[TBD]` and state what drives the date.
5. Record the budget envelope and funding source. Never invent figures; mark `[UNKNOWN]` and state the approval threshold if known.
6. Identify sponsor, project manager, key stakeholders and the steering body.
7. Define PM authority: budget variance, schedule variance and staffing decisions allowed without escalation, and the escalation path.
8. Capture top 5 risks, assumptions and constraints at summary level.
9. Define success criteria for project closure and who accepts them.
10. Add an approvals block and list open questions ordered by how much they block kickoff.

## Output format
```markdown
# Project Charter: <name>
| Field | Value |
|---|---|
| Sponsor | <name/role> |
| Project manager | <name or [TBD]> |
| Version / date | <v0.1, date> |
| Budget envelope | <amount + source or [UNKNOWN]> |
| Target end | <date + driver or [TBD]> |

## Business Need and Strategic Alignment
## Objectives (SMART)
| # | Objective | Measure | Target | Date |
## Expected Benefits (owned by business)
## High-Level Scope
- In: ... / Out: ...
## Major Deliverables
## Milestones
| Milestone | Target date | Driver |
## Stakeholders and Governance
## PM Authority and Escalation
| Decision | PM may decide up to | Escalate to |
## Summary Risks, Assumptions, Constraints
## Success Criteria for Closure
## Open Questions
## Approvals
| Role | Name | Decision | Date |
```

## Quality checklist
- [ ] Every objective is measurable and time-bound.
- [ ] Objectives and business benefits are not mixed.
- [ ] PM authority limits are explicit numbers or rules, or marked `[TBD]`.
- [ ] No budget, date or name is invented.
- [ ] Out-of-scope items are listed.
- [ ] The charter fits on about two pages.

## Common pitfalls
- Writing a solution design into the charter. Keep it at mandate level; design comes later.
- Leaving authority undefined, which forces every decision to the sponsor. Set tolerances.
- Using a charter as a status document. Freeze it after approval and change it only via `change-control`.

## Example
Input: "Charter for CRM migration to SaaS, sponsor Sales VP, go-live Q2, current licence expires June."

Excerpt of output:
- Objective 1: Migrate 100% of active accounts and open opportunities to the SaaS CRM before the licence expiry `[confirm date]`.
- PM authority: schedule variance up to 2 weeks without escalation `[ASSUMPTION]`; above that, steering committee.
- Open question: Is data archiving of closed accounts older than 5 years in scope?
