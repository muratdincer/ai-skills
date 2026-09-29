---
description: Gives structured design critique that is anchored in the design's goals, users and constraints, specific about location and effect, separates observations from opinions, and prioritizes feedback into must-fix, should-consider and nits with suggested directions. Use when a designer shares work in progress and asks for feedback, when preparing for a design review or crit session, or when someone asks "what do you think of this design".
related: heuristic-evaluation, accessibility-audit, wireframe-spec, feedback-sbi, review-comment-writing
prompt: Critique this dashboard redesign; the goal is to help ops managers spot failing stores within 10 seconds.
---

# Give Design Critique

## Purpose
Help a designer improve work in progress by judging it against its goals rather than taste, with specific, prioritized and actionable feedback that keeps what works and focuses discussion on what matters most.

## When to use
- A designer shares a mockup, prototype or flow and asks for feedback.
- A team crit or design review is scheduled and feedback must be prepared.
- Stakeholder feedback is vague ("make it pop") and needs to be turned into goal-based critique.

## When not to use
- A systematic usability inspection with severity ratings is needed. Use `heuristic-evaluation`.
- The check is conformance with WCAG. Use `accessibility-audit`.
- The feedback is about a person's behavior or performance, not a design. Use `feedback-sbi`.

## Inputs
Required:
- The design (image, prototype link description or detailed description) and its goal: who it is for and what it must achieve.

Optional, improves quality:
- Stage (exploration, refinement, final), constraints (design system, technical, brand, deadline), what kind of feedback the designer wants, previous feedback.

If the goal or target user is missing, ask for it first; critique without a goal becomes taste. Ask which stage the work is in if unclear, because it changes what feedback is useful.

## Process
1. Restate the goal, user, key task and stage in one line each so the designer can confirm the frame.
2. Ask or infer what feedback is wanted (concept, flow, layout, visual, copy); keep other feedback brief or park it.
3. Look at the design as the user doing the key task: what is seen first, what is understood, what action is obvious, what is missing.
4. Note strengths first and specifically (what works and why), so they survive iteration.
5. Write observations as "I notice X at location Y" before judgment; then state the effect on the goal ("which means the user may…"); label personal preference as such.
6. Check hierarchy and focus, flow and task fit, consistency with the design system and platform, content and copy, states and edge cases, and basic accessibility (contrast, target size, text alternatives).
7. Frame problems as questions or directions where the designer owns the solution ("What if the failing stores were sorted to the top?"), not as prescriptive redesigns.
8. Prioritize: Must fix (blocks the goal), Should consider (weakens the goal), Nit (polish), and limit Must fix items to the few that matter most.
9. Separate evidence-based points from opinions and assumptions about users; propose how to validate contested points (quick test, data check).
10. Close with the top 3 actions and suggest `heuristic-evaluation` or `accessibility-audit` for a systematic pass, or `usability-test-script` if user evidence is needed.

## Output format
```markdown
# Design Critique: <design name>
Goal: <...> · User / key task: <...> · Stage: <...> · Feedback focus: <...>

## What Works
- <specific strength> — why it helps the goal

## Must Fix
1. <location>: I notice ... → effect on goal ... → direction/question ...

## Should Consider
- ...

## Nits
- ...

## Opinions and Assumptions (to validate)
- [OPINION] ... / [ASSUMPTION] ...

## Top 3 Next Actions
1. ...
```

## Quality checklist
- [ ] Every point is tied to the stated goal, user or constraint, not taste.
- [ ] Every point names a location and an effect.
- [ ] Strengths are specific and included.
- [ ] Feedback is prioritized and Must fix items are few.
- [ ] Opinions and assumptions are labeled and separated from evidence.
- [ ] Feedback matches the stage (no pixel nits on an early concept).
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "I don't like the blue." Taste without a goal gives the designer nothing to act on.
- Redesigning the screen in the feedback. Offer directions and questions; let the designer solve.
- Burying the one blocker among twenty nits. Lead with what blocks the goal.

## Example
Input: "Dashboard redesign; ops managers must spot failing stores within 10 seconds."

Weak: "Too busy, and the colors feel off. Maybe try a cleaner look."
Strong: "Must fix — Store grid: I notice failing stores are marked only by a small red dot, and the grid is sorted alphabetically. With 120 stores, a manager has to scan every tile, which works against the 10-second goal. What if failing stores were pinned to the top with a count in the header? Also, red-only status fails for color-blind users; pair it with an icon or label."
