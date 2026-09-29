---
name: facilitation-guide
description: "Produces a facilitator script for a meeting or workshop with a minute-by-minute run sheet, opening and closing words, prompts per agenda item, decision rules, and tactics for dominance, silence, derailment and conflict. Use when someone will run a meeting and wants to lead it confidently, especially decision, alignment or cross-team sessions."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: during
  title: "Facilitate a meeting"
  related: "meeting-agenda, conflict-resolution, retrospective-facilitation, workshop-plan, decision-matrix"
  prompt: "I am facilitating a 90-minute session with product, sales and engineering to agree on Q3 priorities. Give me a facilitation guide."
---

# Facilitate a Meeting

## Purpose
Give the facilitator a ready-to-run script so the group reaches the intended outcome on time, everyone contributes, and disagreements are resolved or parked explicitly instead of derailing the session.

## When to use
- Leading a decision, prioritization, alignment or problem-solving meeting with several parties.
- A contentious topic or senior audience makes improvisation risky.
- A new facilitator needs a script and fallback moves.

## When not to use
- The agenda is not yet designed. Use `meeting-agenda` first.
- It is a retrospective. Use `retrospective-facilitation`.
- It is a multi-session discovery workshop with exercises. Use `workshop-plan`.

## Inputs
Required:
- Meeting goal and expected output.
- Duration and participants (roles; count if names are unknown).

Optional:
- Agenda, known tensions or positions, decision maker and decision rule, remote/in-person setup, materials.

If the decision maker is unknown for a decision meeting, flag it as a blocker in the guide; do not assume one.

## Process
1. Restate the outcome as a completion test ("we leave with a ranked list of 5 priorities signed off by X").
2. Choose the decision rule up front: decider after consultation, consent (no reasoned objection), majority vote, or consensus. State it in the opening.
3. Build the run sheet with timeboxes that sum to 90% of the slot; keep 10% buffer and 5 minutes for closing.
4. Write a 60-second opening: purpose, outcome, decision rule, agenda, ground rules (one conversation, parking lot, cameras if remote).
5. For each agenda item, pick a technique that fits: silent writing then round-robin (divergence), dot voting or ranking (convergence), 1-2-4-all (many voices), fist-of-five (consent check). With more than ~8 people, use breakouts of 3-5 with a named reporter and a fixed output format (e.g. top 3 options with one-line rationale); converge with note-and-vote: silent individual notes, share without debate, silent dot vote, then the decider picks and states why.
6. Write 2-3 open prompts per item, plus one convergence prompt ("What would we need to believe to choose A?").
7. Prepare interventions for: a dominant voice, silent participants, going off-topic, repeating arguments, a HiPPO shutting down debate, open conflict.
8. Define the parking lot rule: what goes there and how it will be followed up.
9. Write the closing: read back decisions and actions with owners, confirm the decision rule was met, quick check-out, who sends the summary.
10. Add a remote/hybrid note if relevant: chat monitor, turn order, shared board.
11. If the user's goal continues, suggest `decision-matrix` when options need structured scoring or `conflict-resolution` when a known tension needs preparation before the session.

## Output format
```markdown
# Facilitation Guide: <meeting>
Outcome test: <...>   Decision rule: <...>   Decider: <name or [UNKNOWN] – blocker>

## Run Sheet
| Time | Item | Technique | Output | Prompt |
|---|---|---|---|---|

## Opening (script)
"<...>"

## Item Prompts
### <Item>
- Diverge: ...
- Converge: ...

## Interventions
| Situation | Move | Words to use |
|---|---|---|

## Parking Lot Rule
## Closing (script)
```

## Quality checklist
- [ ] The outcome test is observable at the end of the meeting.
- [ ] The decision rule and decider are stated or flagged as missing.
- [ ] Timeboxes include buffer and closing time.
- [ ] Every item has both divergence and convergence prompts.
- [ ] Interventions include exact wording, not just advice.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Choosing the decision rule after the discussion; losers then contest the process. Announce it in the opening.
- Facilitator also arguing a position. If you must contribute, say "facilitator hat off" and keep it short.
- Spending all time on divergence. Protect the convergence slot in the run sheet.

## Example
Input: 90 min, product/sales/engineering, agree Q3 priorities, CPO decides.

Excerpt of output:
| 0:10-0:25 | Candidate list | Silent writing, then round-robin | Deduplicated list | "What must be true by end of Q3 for this quarter to be a success?" |
Intervention – dominant voice: "Thanks, Ali, that is clear. Let's hear from engineering before we go further. Deniz?"
