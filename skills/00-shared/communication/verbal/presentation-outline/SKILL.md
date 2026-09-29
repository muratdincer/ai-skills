---
description: Builds an audience-specific storyline and a slide-by-slide outline with one message per slide, supporting evidence, a clear ask and timing. Use when someone must present a proposal, status, design, result or decision to managers, customers, a committee or a team and needs the structure before designing slides.
related: executive-summary, steering-committee-pack, demo-script, elevator-pitch, stakeholder-map
prompt: Outline a 20-minute presentation to the leadership team proposing we move our reporting workloads to a new data platform next year.
---

# Outline a Presentation

## Purpose
Turn a topic and an audience into a storyline where every slide carries one message that moves the audience toward a decision or understanding, so slide design starts from a tested argument instead of a pile of content.

## When to use
- A proposal, design, result or status must be presented live or on a call.
- An existing deck is long and unfocused and needs a new storyline.
- The same content must be told to two different audiences (e.g. executives and engineers).

## When not to use
- The content will be read, not presented. Use `executive-summary`.
- The core of the session is showing working software. Use `demo-script`.
- A governance body needs its standard pack. Use `steering-committee-pack`.

## Inputs
Required:
- Topic and the outcome wanted from the audience (decide, approve, understand, adopt).
- Audience (who, seniority, what they already know) and time slot.

Optional:
- Source material, data, constraints, previous objections, organization template.

If the desired outcome or audience is missing, ask for it first (one question at a time). Unknown figures, dates and names stay `[TBD]`; never invent data to make a slide land.

## Process
1. State the governing message in one sentence: what the audience should think or do at the end. If you cannot, the topic is not ready; list what is missing as open questions.
2. Profile the audience: decision power, what they care about (cost, risk, speed, customers, team load), prior knowledge, likely objections. Label every inference `[ASSUMPTION]`.
3. Choose the storyline: Situation-Complication-Resolution for proposals, answer-first (pyramid) for executives, problem-approach-result for technical reviews, before-after-bridge for change.
4. Put the ask or conclusion near the start for senior audiences; build up to it only for audiences that need context first.
5. Draft action titles: each slide title is a full sentence that states its message ("Batch jobs miss the 07:00 SLA twice a week"), not a label ("Current state").
6. Attach evidence to each message: one chart, table, example or quote; mark missing evidence `[TBD: source]`.
7. Budget time: about 2 minutes per content slide; reserve at least 25% of the slot for questions and discussion. Cut slides that do not support the governing message into an appendix.
8. Pre-empt the top 2-3 objections with a slide or a prepared appendix answer.
9. Close with an explicit ask: decision, owner, date, and what happens next.
10. Run the headline test: reading only the slide titles in order must tell the whole story. Fix gaps or repeats.
11. If the user's goal continues, suggest `demo-script` for a live product segment, `executive-summary` for a pre-read, or `elevator-pitch` for a short verbal version.

## Output format
```markdown
# Presentation Outline: <title>
Audience: <who, decision power> | Slot: <minutes> | Desired outcome: <decide/approve/...>
Governing message: <one sentence>
Storyline: <SCR / answer-first / ...>

| # | Action title (message) | Evidence / visual | Time | Notes |
|---|---|---|---|---|
| 1 | <message sentence> | <chart/table/example or [TBD]> | 2 min | |
| ... | | | | |
| n | Ask: <decision, owner, date> | | | |

Q&A reserve: <minutes>
Anticipated objections: <objection> -> <answer / appendix slide>
Appendix: <backup slides>
Assumptions and open questions: [ASSUMPTION] ... / [TBD] ...
```

## Quality checklist
- [ ] The governing message is one sentence and states what the audience should think or do.
- [ ] Every slide title is a full-sentence message; titles alone tell the story.
- [ ] Each message has evidence or is marked `[TBD]`; no invented figures.
- [ ] Timing fits the slot with at least 25% left for discussion.
- [ ] The ask is explicit: decision, owner, date.
- [ ] Top objections are anticipated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Chronological storytelling ("first we did, then we found...") for executives. Lead with the answer.
- Topic labels as titles, so the audience must decode each slide. Write the message as the title.
- Stuffing every analysis into the main flow. Keep the main flow to what supports the message; move the rest to the appendix.

## Example
Input: 20 minutes, leadership team, propose moving reporting workloads to a new data platform.

Weak titles: "Background", "Current Architecture", "Options", "Next Steps".

Strong (excerpt):
- Governing message: Approve a two-phase migration of reporting to the new platform, starting with finance reports `[date TBD]`.
- 1 "Reporting misses its morning SLA regularly and the gap is growing" – SLA breach chart `[TBD: data source]`.
- 2 "Scaling the current platform costs more than migrating" – cost comparison `[ASSUMPTION: estimates pending]`.
- 6 "Ask: approve phase 1 budget and name a business owner by `[date]`".
