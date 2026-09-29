---
description: Builds or revises a career ladder for a job family with levels, scope and impact per level, competency expectations with observable examples, and parallel individual contributor and management tracks. Use when an organization needs consistent levelling for promotions, hiring and reviews, when levels are vague or inconsistent across teams, or when adding a staff/principal or management track.
related: role-definition, performance-review, career-development-plan, job-description, interview-plan
prompt: Build a career ladder for our software engineers from junior to principal, with a separate management track from team lead to director.
---

# Build a Career Ladder

## Purpose
Give people and managers a shared, fair definition of what each level means, so that hiring, reviews and promotions are calibrated across teams and growth paths are visible to everyone.

## When to use
- There is no ladder, or levels are defined only by years of experience or title.
- Promotions are inconsistent across teams, or people cannot tell what the next level requires.
- A new track (staff/principal IC, management, specialist) or job family is added.

## When not to use
- One person's growth plan against an existing ladder. Use `career-development-plan`.
- Defining a single role's responsibilities and decision rights. Use `role-definition`.
- Compensation bands and pay policy. Keep them out of the ladder and refer to HR policy.

## Inputs
Required:
- Job family (e.g. software engineering) and the number or names of levels wanted, or the current levels.

Optional, improves quality:
- Company values, existing competencies, current ladder or review template.
- Organization size and structure, whether IC and management tracks should be parallel.

If the level structure is missing, propose one (e.g. 6 IC levels, 3 management levels) and mark it `[ASSUMPTION]`.

## Process
1. Define 4-6 competencies that matter for the job family (e.g. technical craft, delivery and ownership, system design, collaboration and communication, leadership and influence, business impact).
2. Define the scope axis for each level: task, feature, team, multiple teams, organization, company; this axis differentiates levels more than skills.
3. Write each level's summary in 2-3 sentences: scope, autonomy, ambiguity handled and impact.
4. For each competency and level, write expectations as observable behaviors with 1-2 examples; each level must add something, not repeat the previous with "more".
5. Design the IC and management tracks as parallel with equivalent levels; management is a different job, not a promotion from senior IC.
6. Specify how the ladder is used: level is judged on sustained evidence over a period, not a single project; not all behaviors are needed, the overall pattern is.
7. Check inclusivity: remove requirements that reward visibility over impact, availability over results, or a single working style; value glue work such as mentoring, reviews and incident follow-up.
8. Check for gaps and jumps: the step between adjacent levels should be of similar size; flag any level that is hard to reach without a specific opportunity.
9. Add a calibration guide: how managers compare evidence across teams and resolve disagreements.
10. List items needing HR or leadership decision (titles, level counts, mapping of current employees) as open questions; do not map named people.
11. If the user's goal continues, suggest `career-development-plan` for individuals, `performance-review` for reviews against the ladder or `job-description` for hiring.

## Output format
```markdown
# Career Ladder: <job family>

## Principles of Use
- ...

## Levels Overview
| Level | Title | Scope | Summary |
|---|---|---|---|

## Competency Matrix
| Competency | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|

## Management Track
| Level | Equivalent IC level | Scope | Summary |
|---|---|---|---|

## Calibration Guide
- ...

## Open Questions / Decisions Needed
- ...
```

## Quality checklist
- [ ] Each level differs from its neighbor by scope and behavior, not by adjectives like "more" or "better".
- [ ] Expectations are observable and have examples.
- [ ] No years-of-experience gates or requirements tied to availability, visibility or personal circumstances.
- [ ] Glue work (mentoring, reviews, incidents, documentation) is recognized.
- [ ] IC and management tracks are parallel and equally valued.
- [ ] Usage and calibration guidance is included.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Senior = mid-level but faster." Levels must differ in scope and ambiguity, not speed.
- Using the ladder as a checklist where every cell must be ticked. State that the overall pattern of evidence decides.
- Making staff+ promotion depend on being assigned a big project. Describe multiple valid paths to the scope.

## Example
Input: Software engineering, levels L1-L6 IC, M1-M3 management.

Excerpt of output:
- L4 Senior, System design: Designs features spanning several services in the team's domain, documents trade-offs and gets reviews from affected teams; example: design doc for idempotent payment retries adopted by two teams.
- Weak cell (avoid): "L5: Very strong design skills." Strong cell: "L5: Sets technical direction across 2-4 teams; resolves conflicting designs by making trade-offs explicit."
- `[ASSUMPTION]` M1 is equivalent in scope to L5; confirm with HR.
