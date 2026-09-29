---
name: transcript-cleanup
description: "Cleans up a raw or auto-generated meeting transcript by removing filler, false starts and crosstalk, fixing speaker labels and obvious recognition errors, and keeping the meaning and wording intact. Use when a transcript must be made readable, quotable or archivable without turning it into a summary."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: during
  title: "Clean up a meeting transcript"
  related: "meeting-notes, meeting-minutes, meeting-summary, glossary-builder"
  prompt: "Clean up this auto-generated transcript of our vendor call. Speaker 1 is me (Selin), Speaker 2 is the vendor PM."
---

# Clean Up a Meeting Transcript

## Purpose
Produce a readable, accurate transcript that preserves who said what and what they meant, so it can be quoted, reviewed or used as the source for notes and minutes.

## When to use
- An auto-generated transcript has filler, broken sentences and generic speaker labels.
- A conversation (interview, vendor call, design review) must be archived close to verbatim.
- Quotes will be taken from the transcript for a report or decision record.

## When not to use
- The user wants structure or conclusions rather than the dialogue. Use `meeting-notes` or `meeting-summary`.
- A formal record of resolutions is needed. Use `meeting-minutes`.

## Inputs
Required:
- The transcript text.

Optional:
- Speaker mapping (label to name/role), glossary of product names, acronyms and people's names, desired cleanup level (light "clean verbatim" or heavier "readable").

If speaker mapping is missing, keep the original labels and propose a mapping with `[ASSUMPTION]` where the content makes it obvious.

## Process
1. Confirm the cleanup level. Default is clean verbatim: remove fillers, keep the speaker's words and order.
2. Normalize speaker labels to names or roles consistently; merge fragments of one speaker's turn that were split by the recognizer.
3. Remove fillers (uh, um, "you know", "like", Turkish "şey", "yani" when used as filler), stutters, false starts and repeated words.
4. Fix obvious recognition errors using context and the glossary (product names, acronyms, technical terms). If uncertain, keep the original and add `[?]`.
5. Add punctuation and paragraph breaks; do not rephrase into different words or reorder arguments.
6. Keep hedges and qualifiers that change meaning ("I think", "probably", "not before Q3"). They are content, not filler.
7. Mark inaudible or crosstalk parts as `[inaudible hh:mm:ss]` or `[crosstalk]`; never fill them in.
8. Keep timestamps at turn or paragraph level if they exist in the source.
9. Mask sensitive personal data not needed for the purpose (phone numbers, IDs, health details) as `[REDACTED]`.
10. Append a short change log: cleanup level, speaker mapping used, number of uncertain spots.
11. If the user's goal continues, suggest `meeting-notes` to structure the cleaned transcript or `meeting-summary` for a short recap.

## Output format
```markdown
# Transcript: <meeting title> – <date>
Cleanup level: <clean verbatim / readable>
Speakers: <label> = <name, role>; ...

[00:00:12] **<Name>:** <cleaned text>

[00:01:05] **<Name>:** <cleaned text> [?term]

[00:02:40] [crosstalk]

---
Cleanup notes
- Speaker mapping: <confirmed / [ASSUMPTION]>
- Uncertain terms: <list with timestamps>
- Redactions: <count and type>
```

## Quality checklist
- [ ] No sentence changes meaning compared with the source.
- [ ] Hedges, numbers, dates and negations are preserved.
- [ ] Speaker labels are consistent across the whole transcript.
- [ ] Every uncertain word is marked with `[?]`, not guessed.
- [ ] Inaudible parts are marked, not invented.
- [ ] Sensitive personal data is redacted.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Drifting into summarization. A cleaned transcript keeps every substantive turn.
- "Correcting" a speaker's factual mistake. Keep what was said; add `[sic]` if needed.
- Dropping negations or qualifiers during filler removal ("not really", "not yet"), which inverts meaning.

## Example
Input: "Speaker 2: yeah so um we we can maybe deliver the the API by uh end of May but not the reporting part"

Output excerpt:
[00:14:22] **Vendor PM:** We can maybe deliver the API by end of May, but not the reporting part.
