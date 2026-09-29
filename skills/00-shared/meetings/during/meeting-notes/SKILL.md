---
description: Turns raw meeting notes, chat logs or a transcript into topic-based structured notes that separate discussion points, decisions, action items and open questions, with speakers attributed where it matters. Use when someone shares messy notes or a transcript and asks to "clean up", "structure" or "write up" what was discussed.
related: transcript-cleanup, meeting-summary, action-item-extraction, decision-log, open-questions-tracker
prompt: Here are my raw notes from today's sprint planning with the platform team. Turn them into structured meeting notes.
---

# Take Structured Meeting Notes

## Purpose
Produce a faithful, scannable record of what was discussed, grouped by topic, so attendees and absentees can find decisions, commitments and open issues without re-listening to the meeting.

## When to use
- Raw bullet notes, chat logs or an auto-generated transcript need to become readable notes.
- Notes must be shared with the team or stored with a project.
- Several note-takers' fragments must be merged into one record.

## When not to use
- A short, leadership-oriented recap is needed. Use `meeting-summary`.
- A formal record with attendance and resolutions is required (board, steering, audit). Use `meeting-minutes`.
- The transcript itself must be cleaned while staying verbatim. Use `transcript-cleanup`.

## Inputs
Required:
- Raw notes or transcript.

Optional:
- Meeting title, date, attendees and roles, agenda, previous notes, glossary of project terms.

If the raw content is missing, ask for it. If the agenda is missing, infer topics from the content and say so.

## Process
1. Scan the whole input once and list the distinct topics; map them to agenda items if an agenda exists, otherwise order them as they occurred.
2. For each topic, write 2-6 bullets capturing the substance: positions taken, data cited, constraints raised. Paraphrase; keep numbers, names of systems and dates exactly.
3. Attribute a statement to a person only when ownership matters (a commitment, a dissent, an expert opinion). Otherwise keep it neutral.
4. Tag items inline: `DECISION`, `ACTION`, `QUESTION`, `RISK`. A decision needs explicit agreement in the input; a proposal without agreement stays a discussion point.
5. For every ACTION capture owner and due date; if missing write `[UNKNOWN]`, never guess.
6. Collect all tagged items again in consolidated sections at the end so they can be copied into trackers.
7. Flag unclear passages (inaudible, contradictory, ambiguous acronym) as `[UNCLEAR: ...]` rather than smoothing them over.
8. Remove small talk, repetition and off-record remarks; mask personal data not needed for the record (phone numbers, health, HR matters).
9. Add a header with meeting metadata and a "Not covered" line for agenda items that were skipped.
10. If the user's goal continues, suggest `action-item-extraction` for a full commitment list or `meeting-summary` for a short recap.

## Output format
```markdown
# <Meeting title> – Notes
Date: <date>  |  Attendees: <names/roles or [UNKNOWN]>  |  Note-taker: <name or [UNKNOWN]>
Agenda coverage: <covered items> | Not covered: <items>

## 1. <Topic>
- <discussion point>
- DECISION: <what was agreed>
- ACTION: <task> — <owner> — <due>
- QUESTION: <open question> — <who can answer>

## 2. <Topic>
- ...

## Decisions
| # | Decision | Topic |
## Action Items
| # | Action | Owner | Due | Status |
## Open Questions and Risks
| # | Item | Type | Owner |
```

## Quality checklist
- [ ] Every topic in the input appears; nothing substantive was dropped.
- [ ] Decisions are only those explicitly agreed in the input.
- [ ] Every action has an owner and due date or an `[UNKNOWN]` marker.
- [ ] Numbers, dates and system names match the source exactly.
- [ ] Unclear parts are flagged, not guessed.
- [ ] Sensitive personal data is masked or removed.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Turning "we should probably..." into a decision. Keep it as a discussion point or a QUESTION.
- Writing chronological minutes of who said what. Group by topic and keep attribution for commitments only.
- Losing dissent. If someone disagreed with a decision, record it briefly; it matters later.

## Example
Input: "infra cost up 18% ... Ayse: need reserved instances? ... ok go with 1yr RI for prod db, Mehmet to check w/ finance by fri ... staging still open"

Excerpt of output:
## 1. Infrastructure cost
- Monthly infrastructure cost increased 18%.
- DECISION: Use 1-year reserved instances for the production database.
- ACTION: Confirm budget approval with Finance — Mehmet — Friday `[confirm date]`.
- QUESTION: Should staging also move to reserved capacity? — [UNKNOWN]
