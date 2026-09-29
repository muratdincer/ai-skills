---
name: career-development-plan
description: "Builds a career development plan that compares a person's current level with a target level or path, identifies evidence-based gaps per competency and defines development actions, opportunities, support and checkpoints. Use when someone asks about promotion or a path change (IC vs management, specialization), after a review, or when a manager needs a structured growth conversation."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Write a career development plan"
  related: "career-ladder, goal-setting, performance-review, one-on-one-prep, onboarding-plan-30-60-90"
  prompt: "Create a development plan for Burak, Senior Engineer, who wants to move to Staff within 18 months."
---

# Write a Career Development Plan

## Purpose
Make growth concrete: where the person is today, where they want to go, what specifically separates the two, and which experiences and support will close the gap.

## When to use
- A person asks what they need for promotion or for a different path.
- After a review, to turn growth areas into a longer-term plan.
- When a role change (tech lead, manager, architect, domain specialist) is being explored.

## When not to use
- Goals for a single review period only. Use `goal-setting`.
- A remediation plan for underperformance. Use `underperformance-plan`.
- Defining level expectations for the organization. Use `career-ladder`.

## Inputs
Required:
- Current role and level, the target level or path as the person states it, and the career ladder or competency expectations (or permission to use generic ones).

Optional, improves quality:
- Recent review, self-assessment, peer feedback, examples of work.
- Business context: upcoming projects, team needs, promotion process and timing.
- Constraints: time available, learning budget, location, working pattern.

If the target comes only from the manager, confirm the person's own aspiration first. If no ladder exists, use generic dimensions and mark `[ASSUMPTION]`.

## Process
1. Restate the person's aspiration in their words and the motivation behind it.
2. For each competency, record current evidence and the target level expectation side by side.
3. Rate each gap (none / small / significant) with evidence; do not rate from impressions.
4. Choose 2-3 priority gaps with the highest leverage for the target; park the rest.
5. For each priority gap, plan the 70-20-10 mix: stretch experiences on real work, coaching or mentoring, and formal learning.
6. Identify concrete opportunities (projects, ownership areas, reviews to lead) and check they are fairly distributed across the team, not reserved for visible favorites.
7. Define observable evidence that will show the gap is closed.
8. List manager commitments: sponsorship, visibility, time, budget, introductions.
9. Set checkpoints and be explicit about what the plan does not guarantee (promotion depends on the process, business need and demonstrated evidence).
10. Mark unconfirmed items `[ASSUMPTION]` or `[TBD]`.
11. If the user's goal continues, suggest `goal-setting` to turn actions into period goals, or `one-on-one-prep` to schedule progress check-ins.

## Output format
```markdown
# Career Development Plan: <name>
Current: <role, level> · Target: <level / path> · Horizon: <months> · Updated: <date>

## Aspiration (in their words)

## Gap Analysis
| Competency | Current evidence | Target expectation | Gap |
|---|---|---|---|

## Priority Gaps and Actions
| Gap | Experience (on the job) | Coaching / mentor | Learning | Evidence of progress | By |
|---|---|---|---|---|---|

## Manager Commitments
- ...

## Checkpoints
- <date>: <what we review>

## What This Plan Does Not Guarantee
- ...

## Open Points
- [TBD] ...
```

## Quality checklist
- [ ] The aspiration is the person's, confirmed, not assumed.
- [ ] Every gap is backed by evidence against a stated expectation.
- [ ] No more than three priority gaps.
- [ ] Most actions are on-the-job experiences, not only courses.
- [ ] Manager commitments and checkpoints are explicit.
- [ ] Expectations about promotion timing are realistic and not promised.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Plans made entirely of trainings and certificates. Growth at senior levels comes from scope and ownership.
- Promising a promotion date. Commit to the plan and evidence, not the outcome.
- Assuming everyone wants management. Offer IC and management paths as equals.

## Example
Input: "Burak, Senior Engineer, wants Staff in 18 months."

Excerpt of output:
| Cross-team technical influence | Leads designs within own team | Shapes decisions across 2+ teams `[ladder wording to confirm]` | Significant |
- Action: Own the event schema governance proposal across order and billing teams; mentor: principal engineer; evidence: proposal adopted by both teams.
- Does not guarantee: Staff promotion depends on calibration and an open business need.
