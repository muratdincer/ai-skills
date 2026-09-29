---
description: Defines a role with its mission, outcomes, responsibilities, decision rights, interfaces with other roles, and what the role is not accountable for. Use when creating a new role (e.g. staff engineer, tech lead, platform product owner), when two roles overlap or conflict, or when decision rights are unclear and work falls between roles.
related: raci-matrix, career-ladder, job-description, team-topology, governance-framework
prompt: Define the tech lead role in our teams; people confuse it with the engineering manager and the architect.
---

# Define a Role

## Purpose
Make a role's purpose, accountabilities and decision rights explicit, so the person in it, their peers and their manager share the same expectations and nothing important falls between roles.

## When to use
- A new role is introduced or an existing one changes after a reorg.
- Two roles overlap (tech lead vs engineering manager, architect vs staff engineer, PO vs PM) and cause friction.
- Decisions stall because nobody knows who decides.

## When not to use
- A public hiring advertisement. Use `job-description` (it can reuse this definition).
- Level expectations across a job family. Use `career-ladder`.
- Mapping many tasks to many roles for one project. Use `raci-matrix`.

## Inputs
Required:
- Role name and the team or organization context it sits in.

Optional, improves quality:
- Adjacent roles and their current definitions, known conflicts or dropped balls.
- Reporting line, team topology, governance forums, existing career ladder.

If adjacent roles are unknown, ask which roles the new one works with most; interfaces cannot be defined without them.

## Process
1. Write the role's mission in one sentence: why it exists and what would go wrong without it.
2. Define 3-5 outcomes the role is accountable for, measurable or observable over a period (not activities).
3. List responsibilities grouped by area (technical, delivery, people, stakeholders), each as a verb phrase.
4. Define decision rights with levels: decides alone, decides after consulting, recommends, is informed. Name the decisions concretely (e.g. library choice within the team, production release, hiring decision).
5. Map interfaces with adjacent roles: what this role needs from them and gives to them; resolve each known overlap with one explicit owner.
6. State explicit non-responsibilities to prevent scope creep (e.g. tech lead does not write performance reviews).
7. Describe the time split as a range (e.g. hands-on coding 30-50%) if the role blends activities; mark as `[ASSUMPTION]` if not confirmed.
8. Note reporting line, span, and whether the role is a level, a position or a temporary assignment.
9. Keep language inclusive and role-based; avoid describing the current holder's personality.
10. List open questions where decision rights are disputed and who should settle them.
11. If the user's goal continues, suggest `raci-matrix` for project-level allocation, `job-description` to hire for the role or `career-ladder` to place it in levels.

## Output format
```markdown
# Role: <name>
Context: <team / org> · Reports to: <role> · Type: <level / position / assignment>

## Mission
<one sentence>

## Outcomes
1. ...

## Responsibilities
| Area | Responsibility |
|---|---|

## Decision Rights
| Decision | Decides | Consulted | Informed |
|---|---|---|---|

## Interfaces
| Role | This role provides | This role needs |
|---|---|---|

## Not Responsible For
- ...

## Time Allocation (indicative)
- ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Mission explains why the role exists, not what it does day to day.
- [ ] Outcomes are observable and not a restatement of responsibilities.
- [ ] Every known overlap with an adjacent role has one explicit owner.
- [ ] Decision rights name concrete decisions.
- [ ] Non-responsibilities are listed.
- [ ] The definition describes the role, not the current person.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing every task anyone might do. Keep to what the role is accountable for.
- Leaving "shared" ownership for contested decisions. Shared means nobody; pick one and consult the other.
- Writing the role around one strong individual. The definition must survive a change of person.

## Example
Input: Tech lead role; conflicts with engineering manager on who decides sprint scope and who handles underperformance.

Excerpt of output:
- Mission: Ensures the team's technical decisions are sound and consistent so the team delivers safely at sustainable speed.
- Decision rights: Technical design within team boundaries – tech lead decides, architect consulted for cross-team impact. Iteration scope – product owner decides, tech lead consulted.
- Not responsible for: performance reviews, compensation, formal performance plans (engineering manager).
