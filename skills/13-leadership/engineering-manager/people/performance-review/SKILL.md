---
description: Writes an evidence-based, competency-aligned and balanced performance review for an engineer or other team member, with a calibrated rating rationale, strengths, growth areas and next-period focus. Use when a review cycle is due, when converting 1:1 notes, peer feedback and delivery evidence into a written review, or when checking a draft review for bias and unsupported claims.
related: career-ladder, goal-setting, one-on-one-notes, career-development-plan, feedback-sbi
prompt: Draft Can's annual review from these notes, peer feedback and his goals. Our ladder level is Senior Engineer.
---

# Write a Performance Review

## Purpose
Produce a review the person can recognize as fair: every statement backed by evidence from the whole period, mapped to the organization's competencies and level, with clear direction for the next period.

## When to use
- A mid-year or annual review must be written or finalized.
- Scattered evidence (1:1 notes, peer feedback, goal results, incidents, delivered work) needs to become one coherent review.
- A draft review needs a bias and evidence check before calibration.

## When not to use
- Sustained performance gap needing a formal plan. Use `underperformance-plan`.
- Setting next-period objectives in detail. Use `goal-setting`.
- Defining the level expectations themselves. Use `career-ladder`.

## Inputs
Required:
- The person's role and level, the review period, and evidence for that period (notes, goal outcomes, feedback, work examples).

Optional, improves quality:
- The competency framework or career ladder and the rating scale with definitions.
- Self-assessment, peer and stakeholder feedback, previous review.
- Context: role change, leave, reorg, on-call load, project cancellations.

If the rating scale or competency framework is missing, use generic dimensions (impact, craft, collaboration, ownership, growth) and mark them `[ASSUMPTION]`. If evidence is thin, say so; do not fill the gap with impressions.

## Process
1. Build an evidence table: date, observation, source, competency. Cover the full period, not just the last weeks (recency bias).
2. Discard or flag evidence that is hearsay, about personality, or about protected characteristics, leave or personal circumstances.
3. Map evidence to each competency and compare against the level's expectations, not against peers or the manager's own style.
4. For goals, state the outcome versus the target and the context that changed it (scope cuts, dependencies).
5. Write strengths with concrete examples and their impact on team, product or customers.
6. Write growth areas in behavioral terms with at least one example each, and what "good" looks like at this level.
7. Propose a rating and a short rationale tied to the scale definitions; state the strongest counter-evidence too.
8. Run a bias pass: recency, halo/horns, similarity, attribution (credit to individual vs team), gendered or coded language ("abrasive", "aggressive" vs "assertive"), penalizing flexible work or leave.
9. Define 2-4 focus points for the next period, linked to growth areas and career goals.
10. Mark every claim without evidence as `[NEEDS EVIDENCE]` and list open questions for the manager.
11. If the user's goal continues, suggest `goal-setting` for next-period goals, or `career-development-plan` for growth areas.

## Output format
```markdown
# Performance Review: <name> – <period>
Role / level: <role, level> · Reviewer: <manager> · Rating: <proposed> [draft]

## Summary (3-4 sentences)

## Goal Outcomes
| Goal | Target | Outcome | Context |
|---|---|---|---|

## Competency Assessment
| Competency | Level expectation | Evidence (date, source) | Assessment |
|---|---|---|---|

## Strengths
- <behavior> – <example> – <impact>

## Growth Areas
- <behavior> – <example> – <what good looks like at this level>

## Rating Rationale
<why this rating per scale definition; strongest counter-evidence>

## Focus for Next Period
1. ...

## Open Questions / Evidence Gaps
- [NEEDS EVIDENCE] ...
```

## Quality checklist
- [ ] Every strength and growth area has at least one dated, sourced example.
- [ ] Evidence spans the whole period.
- [ ] Assessment is against level expectations, not against other people.
- [ ] No personality labels, coded language or references to leave, health, family or other protected characteristics.
- [ ] Nothing in the review would be a surprise if feedback was given during the period.
- [ ] Personal data from notes is minimized to what the review needs.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Recency bias. Build the evidence table from the whole period before writing prose.
- Crediting visible work (launches) and ignoring glue work (mentoring, reviews, incident follow-ups). Ask for it explicitly.
- Vague growth areas ("be more strategic"). Describe the behavior and a concrete example of the expected one.

## Example
Input: Senior Engineer, H1 review; notes mention led cache redesign (p95 -40%), two peers say reviews are slow, missed one goal because of reorg.

Excerpt of output:
- Strength: Technical leadership – led cache redesign (Mar, design doc + rollout); p95 latency down 40% per team dashboard.
- Growth area: Review turnaround – two peers report PRs waiting 2-3 days (peer feedback, May); at Senior level reviews are expected to unblock others within a day `[confirm ladder wording]`.
- Goal context: "Migrate reporting service" not met; project paused by reorg in April, not attributable to performance.
