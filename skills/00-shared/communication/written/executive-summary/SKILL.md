---
description: Condenses a document, analysis, proposal or discussion into a one-page, decision-oriented executive summary that leads with the conclusion and the ask, followed by the supporting points, options, risks and next steps. Use when a senior reader must understand and act on long or technical content quickly, or someone asks for a "TL;DR", "exec summary" or "one-pager for leadership".
related: status-update, steering-committee-pack, document-simplify, decision-matrix, presentation-outline
prompt: Turn this 20-page vendor evaluation into an executive summary for the CIO, who has to choose between the two shortlisted vendors next week.
---

# Write an Executive Summary

## Purpose
Give a senior reader the conclusion, the reasoning behind it and the decision required on one page, so they can act without reading the source and can trust that nothing material was left out.

## When to use
- A long report, analysis, business case or proposal goes to executives or a steering group.
- A decision maker asks for the short version of a technical topic.
- A pre-read must be skimmable in two minutes.

## When not to use
- Reporting recurring progress. Use `status-update`.
- Building a full steering committee deck. Use `steering-committee-pack`.
- Making a document shorter and clearer without changing its audience. Use `document-simplify`.

## Inputs
Required:
- The source content (text, notes or key findings).
- The reader and what they must decide or know.

Optional:
- Deadline for the decision, organizational constraints, preferred recommendation, format limits (words, one slide).

If the reader or the purpose is missing, ask once: "Who reads this and what should they do after reading it?" Never add a recommendation the source does not support; if the source has none, present options neutrally and say so.

## Process
1. Define the single question the reader needs answered (decide, approve, be informed, unblock).
2. Extract from the source: the conclusion/recommendation, the 3-5 findings that support it, the options considered, costs, risks, and what happens if nothing is done.
3. Write the Bottom Line Up Front (BLUF): one or two sentences with the conclusion and the ask.
4. Order supporting points by importance to the decision, not by the source's order. Each point is one sentence with its number or evidence.
5. If there is a choice, present the options in a compact table with the trade-off per option and the recommended one marked.
6. State the key risks and the cost of delay or inaction, only if the source supports them.
7. Write the ask precisely: who decides what, by when, and what happens next once decided.
8. Translate jargon to business impact (cost, risk, time, customers, compliance); keep one technical term only if the reader uses it.
9. Mark anything not in the source as `[ASSUMPTION]`; list material gaps as open questions rather than smoothing them over.
10. Cut to one page (about 250-400 words); link to the source for detail.
11. If the user's goal continues, suggest `steering-committee-pack` for a presentation version or `decision-matrix` if the options need structured scoring.

## Output format
```markdown
# Executive Summary: <topic>
**For:** <reader / forum>   **Decision needed by:** <date or [TBD]>

**Bottom line:** <conclusion and the ask in 1-2 sentences>

**Why**
- <finding 1 with evidence/number>
- <finding 2>
- <finding 3>

**Options**
| Option | Benefit | Cost / risk | |
|---|---|---|---|
| A | ... | ... | Recommended |

**Risks and cost of inaction**
- ...

**Ask and next steps**
- <who> decides <what> by <date>; then <next step>.

**Assumptions / open questions**
- ...
Source: <link or document name>
```

## Quality checklist
- [ ] The first two sentences alone give the conclusion and the ask.
- [ ] Every figure and claim traces to the source; nothing is added.
- [ ] Options include their trade-offs, not only the benefits of the recommended one.
- [ ] The language is business impact, with no unexplained jargon.
- [ ] One page or less.
- [ ] Assumptions and gaps are listed, not hidden.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Summarizing the document's structure ("Section 2 covers...") instead of its conclusions.
- Narrative build-up that saves the recommendation for the end. Executives stop reading early; lead with it.
- Dropping the inconvenient risk to make the recommendation look cleaner. It will come up in the meeting and damage trust.

## Example
Input: 20-page vendor evaluation, CIO chooses between two vendors next week.

Weak: "This document summarizes the evaluation process, which consisted of an RFP, demos and reference checks. Several criteria were considered..."

Strong (excerpt):
**Bottom line:** Select Vendor B; it meets all mandatory requirements and has a lower 3-year cost `[figure from source section 5]`. Decision needed by the steering meeting on `[date]` to keep the Q1 start.
**Why:** Vendor A fails the data residency requirement; B passed all reference checks.
