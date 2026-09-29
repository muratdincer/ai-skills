---
name: customer-journey-map
description: "Maps a customer journey for one persona and scenario across stages, with actions, thoughts, emotions, touchpoints, channels, pains, moments of truth and backstage owners, and ranks improvement opportunities. Use when you need to understand an end-to-end experience, find where customers struggle or drop out, align teams across channels, or when someone asks for a journey map."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: discovery
  title: "Map the customer journey"
  related: "persona, jobs-to-be-done, funnel-analysis, user-flow, as-is-process"
  prompt: "Map the customer journey for a first-time buyer of home insurance through our website and call center."
---

# Map the Customer Journey

## Purpose
Show the end-to-end experience of one customer type in one scenario, including what they do, think and feel at each stage, so that teams can see where the experience breaks and who owns the fix.

## When to use
- An experience spans several channels or teams and no one sees the whole.
- Conversion, satisfaction or complaint data shows a problem but not where it comes from.
- Designing a new service or redesigning an existing one.

## When not to use
- You need screen-level navigation. Use `user-flow`.
- You need internal process steps and roles. Use `as-is-process`.
- You need quantitative drop-off per step. Use `funnel-analysis`.

## Inputs
Required:
- The persona or customer type and the scenario (start and end point).

Optional, improves quality:
- Research findings, analytics, support tickets, NPS/CSAT verbatims, channel list, internal process knowledge.
- Whether the map is current-state or future-state.

If persona or scenario is missing, ask. Items not backed by evidence are marked `[ASSUMPTION]`; strip personal data from verbatims.

## Process
1. Fix scope: one persona, one scenario, current or future state, start trigger and end point.
2. Define 5-8 stages from the customer's perspective (e.g. aware, consider, buy, onboard, use, get help, renew), not your org chart.
3. For each stage capture: customer actions, thoughts/questions, emotion (-2 to +2), touchpoints and channels.
4. Capture pains and gains per stage with evidence (quote, metric, ticket category).
5. Mark moments of truth: stages where the emotion or decision determines retention or abandonment.
6. Add backstage: internal teams, systems and policies behind each touchpoint, and the owner.
7. Identify opportunities: each tied to a pain, with expected impact and effort (H/M/L) and the owner.
8. Rank opportunities and propose 2-3 to address first, plus the metrics that should move.
9. Mark every point you inferred rather than read in the input as `[ASSUMPTION]` and carry it into assumptions or open questions. If the user's goal continues, suggest the next skill: `funnel-analysis` to quantify drop-offs at the painful stages, or `persona` / `jobs-to-be-done` if the actor or goal is still weakly evidenced.

## Output format
```markdown
# Customer Journey: <persona> — <scenario> (<current/future> state)
Trigger: ... · End: ... · Evidence: <sources>

| | Stage 1 | Stage 2 | ... |
|---|---|---|---|
| Actions | | | |
| Thoughts / questions | | | |
| Emotion (-2..+2) | | | |
| Touchpoints / channels | | | |
| Pains | | | |
| Backstage / owner | | | |

## Moments of Truth
- ...

## Opportunities
| # | Opportunity | Pain addressed | Impact | Effort | Owner | Metric |
|---|---|---|---|---|---|---|

## Gaps and Assumptions
- ...
```

## Quality checklist
- [ ] One persona and one scenario only.
- [ ] Stages are from the customer's point of view.
- [ ] Emotions and pains are backed by evidence or marked `[ASSUMPTION]`.
- [ ] Every opportunity links to a specific pain and has an owner.
- [ ] Backstage owners are named for broken touchpoints.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mapping the ideal journey and calling it current state. Use real evidence of what happens.
- Covering all personas in one map. Different goals produce different journeys.
- Producing a poster with no follow-up. End with prioritized opportunities and owners.

## Example
Input: "First-time buyer of home insurance, website and call center."

Excerpt of output:
- Stage "Get a quote": Action: fills 4-page form; Thought: "Why do they need my ID number already?"; Emotion: -1; Pain: form abandonment at step 3 `[confirm analytics]`.
- Moment of truth: first call to confirm coverage; long hold time drives abandonment.
- Opportunity: allow a price estimate before identity data — owner: Digital Sales.
