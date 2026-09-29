---
description: Turns raw 1:1 notes or a transcript into concise, factual notes with topics discussed, commitments with owners and dates, feedback exchanged and career or wellbeing signals to follow up. Use after a 1:1 with a direct report or mentee, or when building a running 1:1 log that later supports reviews and development plans.
related: one-on-one-prep, action-item-extraction, performance-review, career-development-plan, meeting-notes
prompt: Clean up my notes from today's 1:1 with Emre and pull out what we both committed to.
---

# Capture 1:1 Notes

## Purpose
Produce a short, factual record of a 1:1 that keeps commitments visible, preserves evidence for later reviews and respects the report's privacy.

## When to use
- Right after a 1:1, from rough notes, bullet points or a transcript.
- To keep a running log per report that feeds reviews and development plans.
- When a commitment or concern from a 1:1 must be tracked to closure.

## When not to use
- Preparing the next conversation. Use `one-on-one-prep`.
- Group or team meeting notes. Use `meeting-notes`.
- Formal documentation of a performance issue. Use `underperformance-plan`.

## Inputs
Required:
- The raw notes or transcript of the 1:1 and the report's name or alias.

Optional, improves quality:
- Date, the previous notes, the 1:1 plan.
- Whether the notes will be shared with the report (recommended) or kept private.

If raw notes are missing, ask for them. Do not reconstruct a conversation from memory prompts.

## Process
1. Group the raw content by topic; drop small talk that carries no decision, commitment or signal.
2. For each topic, write what was discussed in neutral language. Attribute opinions ("Emre feels...") rather than stating them as fact.
3. Extract every commitment. Record owner (report or manager), concrete action and due date; mark a missing date `[TBD]`.
4. Record feedback given and received, in situation-behavior-impact terms, including feedback to the manager.
5. Capture career and growth signals: aspirations, interests, skills they want to build, frustrations with growth.
6. Capture wellbeing or retention signals only as stated by the report; do not diagnose or speculate.
7. Mark items that need action outside the 1:1 (escalation, HR, another team) and who takes them.
8. Remove or generalize sensitive personal data (health, family, legal) unless the report explicitly asked to record it, and note that it was minimized.
9. Link to open items from previous notes; close those that were resolved.
10. Produce a shareable version and flag anything that should stay in the manager's private notes.

## Output format
```markdown
# 1:1 Notes: <name> – <date>

## Topics
- **<topic>**: <neutral summary; opinions attributed>

## Commitments
| # | Action | Owner | Due | Status |
|---|---|---|---|---|

## Feedback
- To <name>: <situation – behavior – impact>
- From <name> to manager: ...

## Career and Growth Signals
- ...

## Wellbeing / Retention Signals (as stated)
- ...

## Carried Over / Closed From Last Time
- ...

## Private Note (not shared) – optional
- ...
```

## Quality checklist
- [ ] Every commitment has an owner and a due date or `[TBD]`.
- [ ] Opinions and interpretations are attributed, not stated as facts.
- [ ] No diagnosis, speculation or labels about personality or health.
- [ ] Sensitive personal data is minimized or removed.
- [ ] The shareable version would not surprise or embarrass the report.
- [ ] Previous open items are closed or carried over explicitly.

## Common pitfalls
- Writing judgments ("lazy", "not a team player") into notes. Record behavior and impact only; notes can be read later in disputes.
- Recording only the report's commitments. Manager commitments are the ones most often dropped.
- Keeping notes that differ from what was said to the person. Share the notes to confirm a common understanding.

## Example
Input: "emre - on-call is killing him, 3 pages last week at night. wants to learn k8s. i'll talk to platform about alert noise. he'll write the runbook for the payment job by friday."

Excerpt of output:
- **On-call load**: Emre reports three night-time pages last week and says the load is unsustainable.
- Commitments: 1) Raise alert noise with platform team – Owner: manager – Due: `[TBD]`. 2) Runbook for payment job – Owner: Emre – Due: Friday.
- Growth signal: Wants to build Kubernetes skills.
