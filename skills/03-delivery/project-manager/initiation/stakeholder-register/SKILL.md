---
description: Builds a project stakeholder register listing each stakeholder's role, interest, influence, current and desired engagement, key concerns and communication needs, with an engagement strategy per group. Use when a project starts, when new parties join, or when resistance or silence from a group signals that engagement must be planned deliberately.
related: stakeholder-identification, stakeholder-map, raci-matrix, communication-plan, project-charter
prompt: Build a stakeholder register for our ERP rollout to three plants; here is the org chart and the charter.
---

# Build a Stakeholder Register

## Purpose
Maintain a single, actionable list of everyone who affects or is affected by the project, with an explicit engagement gap and strategy, so that support is built and resistance is handled before it becomes a schedule risk.

## When to use
- At initiation, after the charter names the sponsor and main affected groups.
- When organizational changes, new vendors or new sites enter the project.
- When a stakeholder group is disengaged or resistant.

## When not to use
- Only a first brainstorm of who might be involved. Use `stakeholder-identification`.
- A visual power/interest grid for a workshop. Use `stakeholder-map`.
- Assigning responsibilities to tasks. Use `raci-matrix`.

## Inputs
Required:
- Project summary (charter or scope) and a list or description of involved parties.

Optional, improves quality:
- Org charts, previous project experience with these groups, known conflicts.
- Contract parties, regulators, works councils or unions.

If no parties are given, ask for at least the sponsor and affected departments.

## Process
1. List stakeholders at the right granularity: individuals for decision makers, groups for large user populations.
2. For each, record role in the project and organizational position.
3. Capture interest (what they gain or lose) and main concerns in their own terms where known.
4. Rate influence and interest (High/Medium/Low) with a one-line justification.
5. Assess current engagement (Unaware, Resistant, Neutral, Supportive, Leading) and the desired level.
6. Highlight gaps where current is below desired and influence is High; these are priority.
7. Define an engagement strategy per priority stakeholder: owner, actions, channel, frequency.
8. Record communication needs (format, detail, language, timing) to feed the communication plan.
9. Mark sensitive personal assessments as internal; keep only work-relevant information and minimize personal data.
10. Set a review cadence and trigger events for updating the register.

## Output format
```markdown
# Stakeholder Register: <project>
Version <x> | Owner <PM> | Next review <date or [TBD]> | Classification: Internal

| ID | Stakeholder | Role / position | Interest & concerns | Influence | Interest | Current | Desired | Strategy & owner | Comms needs |
|---|---|---|---|---|---|---|---|---|---|

## Priority Engagement Gaps
| Stakeholder | Gap | Actions | Owner | Due |

## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every High-influence stakeholder has an engagement strategy and owner.
- [ ] Current vs desired engagement is stated for every row.
- [ ] Ratings have justifications, not bare labels.
- [ ] Indirect stakeholders (operations, support, audit, regulators) are considered.
- [ ] No unnecessary personal data or judgmental language.

## Common pitfalls
- Listing only supportive, visible stakeholders. Look for those who lose something from the change.
- Creating the register once and never updating it. Tie updates to milestones and org changes.
- Writing candid assessments in a document shared widely. Keep sensitive notes restricted.

## Example
Input: "ERP rollout to 3 plants. Plant managers skeptical, finance pushing."

Excerpt of output:
| S-04 | Plant managers (3) | Operational owners | Fear production downtime during cutover | H | M | Resistant | Supportive | Joint cutover planning, plant-specific go/no-go criteria – PM | Weekly 15-min briefing, plant KPIs |
