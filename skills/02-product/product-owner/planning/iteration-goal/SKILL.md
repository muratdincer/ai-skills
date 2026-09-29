---
description: "Writes a single, coherent iteration/sprint goal that states the outcome the team commits to, why it matters and how success will be observed, and checks which candidate items serve it and which do not. Use when preparing iteration/sprint planning, when a draft goal is just a list of tickets, or when someone asks for a sprint goal or iteration objective."
related: "iteration-planning, backlog-prioritization, roadmap, okr-definition, iteration-review-prep"
prompt: "Our next sprint candidates are: SSO login, password reset email fix, audit log export and two tech-debt items. Write a sprint goal."
---

# Write an Iteration Goal

## Purpose
Give the team one focal outcome for the iteration/sprint that guides trade-offs during the cycle, lets scope flex while the commitment stays stable, and makes the review meaningful.

## When to use
- Before or during iteration/sprint planning.
- A proposed goal reads like "finish tickets 101-108".
- Candidate items pull in different directions and focus is needed.
- Stakeholders need a one-line answer to "what is this iteration about?".

## When not to use
- The team works in continuous flow without iterations; use a service or quarterly goal via `okr-definition` or a flow goal in `wip-policy`.
- Running the full planning session with capacity and task breakdown. Use `iteration-planning`.
- Setting product goals over quarters. Use `roadmap` or `okr-definition`.

## Inputs
Required:
- Candidate backlog items for the iteration, or the product objective the iteration should advance. If neither is given, ask.

Optional, improves quality:
- Current product/release goal or OKR.
- Team capacity signal and known constraints (holidays, incidents).
- Stakeholder expectations or deadlines inside the iteration.

## Process
1. Identify the higher-level objective (release goal, OKR, roadmap theme) the iteration should advance.
2. Cluster candidate items by the outcome they contribute to; find the cluster with the highest value or learning for that objective.
3. Draft the goal as an outcome in one sentence using the pattern: "<who> can <do/experience what> so that <benefit>" or "Validate <assumption> by <evidence>". Avoid listing items.
4. Add a "we will know it is achieved when" line with 1-3 observable signals (demo scenario, metric, test result).
5. Map each candidate item: supports goal / independent but necessary (bugs, maintenance, commitments) / does not fit. Recommend what to remove or defer if capacity is tight.
6. Keep independent work visible but secondary; a common guideline is that the goal-related work uses the majority of capacity `[ASSUMPTION: adjust to team norm]`.
7. Check the goal against: one outcome, achievable within the iteration, meaningful to stakeholders, gives the team room to negotiate scope.
8. Offer 2 alternative phrasings if the focus is debatable, with the trade-off of each.

## Output format
```markdown
# Iteration Goal: <iteration name/number>
Advances: <release goal / OKR / theme>

**Goal:** <one sentence>
**We will know it is achieved when:**
- <signal>

## Item Fit
| Item | Supports goal | Independent but necessary | Does not fit |
|---|---|---|---|

## Recommendation
- Keep: ...
- Defer/remove: ... – <reason>

## Alternative Goals (if focus is debatable)
1. <goal> – <trade-off>
```

## Quality checklist
- [ ] The goal is one sentence describing an outcome, not a list of items.
- [ ] Success signals are observable at the review.
- [ ] Every candidate item is classified against the goal.
- [ ] The goal allows scope negotiation (not all items are required to meet it).
- [ ] The link to a higher-level objective is stated or marked `[UNKNOWN]`.

## Common pitfalls
- "Complete all planned stories" as a goal. It gives no guidance for trade-offs; name the outcome instead.
- Compound goals joined with "and". Two goals mean no focus; pick one and treat the rest as independent work.
- A goal nobody outside the team understands. Write it so a stakeholder could repeat it.

## Example
Input: "Candidates: SSO login, password reset email fix, audit log export, two tech-debt items. Release goal: enterprise readiness."

Excerpt of output:
**Goal:** Enterprise pilot users can sign in with their corporate identity so that onboarding no longer needs manual password setup.
**We will know it is achieved when:** a pilot user signs in via SSO on staging in the review demo.
| SSO login | ✓ | | |
| Password reset email fix | | ✓ (live defect) | |
| Audit log export | | | ✓ defer to next iteration |
