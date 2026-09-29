---
name: estimation-session
description: "Prepares and guides a relative estimation session (planning poker, t-shirt sizing, affinity estimation): selects the scale, builds a reference-story ladder, runs estimation rounds that surface assumptions, and records sizes, spread and follow-ups. Use when a team needs to size backlog items, calibrate a new scale, speed up slow estimation meetings, or when someone asks how to run planning poker or t-shirt sizing."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Facilitate relative estimation"
  related: "backlog-refinement, story-splitting, technical-estimation, velocity-analysis, iteration-planning"
  prompt: "We have 25 unsized stories for the new onboarding epic and a 1-hour session. The team is new and has no reference stories. How should we estimate?"
---

# Facilitate Relative Estimation

## Purpose
Give the team consistent relative sizes quickly, with the real value of estimation captured: shared understanding, exposed assumptions and items flagged for splitting or spikes.

## When to use
- A batch of refined backlog items needs sizes before planning or forecasting.
- A new team, or a team after major changes, needs a calibrated scale and reference stories.
- Estimation meetings run long, are dominated by one voice, or produce numbers nobody trusts.

## When not to use
- Items are still unclear or lack acceptance criteria. Use `backlog-refinement` first.
- A bottom-up engineering estimate in hours or days for a design or bid. Use `technical-estimation` or `estimation-three-point`.
- The team forecasts from throughput counts without sizing. Use `monte-carlo-forecast`.

## Inputs
Required:
- The list of items to estimate with short descriptions.
- Time available and number of estimators.

Optional, improves quality:
- Existing reference stories and their sizes; scale in use.
- Acceptance criteria, known technical constraints.
- The purpose of the estimates (iteration planning, release forecast, go/no-go of an epic).

If the item list is missing, ask. Do not invent sizes; the team produces them.

## Process
1. Clarify the purpose; it drives granularity. Release-level sizing can use t-shirt sizes; iteration planning usually needs a finer scale.
2. Pick the technique by batch size: fewer than about 15 items → planning poker; 15-100 items → affinity/silent grouping, then poker only for disputed items; epics → t-shirt sizes.
3. Define the scale (e.g. modified Fibonacci 1, 2, 3, 5, 8, 13, 20, or XS-XL) and what a size combines: effort, complexity and uncertainty, not hours of one person.
4. Build a reference ladder: pick 3-5 completed items the team knows well as anchors for small, medium and large. If none exist, pick a clear small item as "2" and size others relative to it; mark this calibration as provisional.
5. Set rules: product owner answers questions but does not estimate; simultaneous reveal; time box per item (e.g. 3-5 minutes); an item above an agreed threshold (e.g. 13) must be split or spiked.
6. For each round: read the item, clarify, reveal, let the highest and lowest estimators explain, re-vote once. If still spread by more than two steps, record the assumptions and park the item.
7. Capture for every item: size, spread (min-max of first vote), key assumptions and follow-ups (split, spike, question to the product owner).
8. Review the batch for consistency against the reference ladder at the end; adjust outliers.
9. Summarize total size, items needing split or spike and open questions; do not convert points to hours or dates.
10. If the user's goal continues, suggest `story-splitting` for oversized items, `iteration-planning` for selection, or `velocity-analysis` for forecasting.

## Output format
```markdown
# Estimation Session – <team>, <date>
Purpose: <...> · Technique: <poker/affinity/t-shirt> · Scale: <...>

## Reference Ladder
| Size | Reference item | Why it is this size |
|---|---|---|

## Session Rules
- ...

## Results
| Item | Size | First-vote spread | Key assumptions | Follow-up |
|---|---|---|---|---|

## Needs Split / Spike
- <item> – <reason>

## Open Questions for the Product Owner
- ...
```

## Quality checklist
- [ ] The technique fits the number of items and the time box.
- [ ] A reference ladder exists, and a provisional calibration is labeled as such.
- [ ] No sizes are invented by the assistant; unestimated items are marked `[TBD]`.
- [ ] Wide spreads are explained by recorded assumptions, not averaged away.
- [ ] Items above the threshold are routed to splitting or a spike.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Averaging divergent votes. The divergence is the signal; discuss it and record the assumption.
- Converting points to hours or comparing points across teams. Relative sizes are team-local.
- Estimating items nobody understands. Stop and send them back to refinement.
- Letting the most senior person reveal first or anchor. Always reveal simultaneously.

## Example
Input: "25 unsized onboarding stories, 1 hour, new team, no references."

Excerpt of output:
- Technique: silent affinity grouping (20 min) → poker only for disputed items (30 min) → consistency pass (10 min).
- Reference: "Change welcome email text" = 2 (provisional calibration).
- Result: "Upload ID document" | 13 | 5-20 | assumes an external verification service `[confirm]` | Spike on vendor API.
