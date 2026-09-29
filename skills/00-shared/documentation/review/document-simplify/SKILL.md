---
name: document-simplify
description: "Rewrites a document or passage to be shorter and easier to read for its audience by removing redundancy, jargon, hedging and nominalizations while preserving every obligation, number, condition and decision. Use when a text is too long, dense or technical for its readers, when someone asks to shorten, simplify or make something plain-language, or when a document must fit a length limit."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: documentation
  area: review
  title: "Simplify a document"
  related: "document-review, executive-summary, tone-rewrite, microcopy, technical-translation"
  prompt: "Simplify this three-page data retention policy so that team leads can understand what they must do; keep all obligations."
---

# Simplify a Document

## Purpose
Reduce reading effort substantially without losing meaning, so the intended readers understand and act on the content on the first read.

## When to use
- A policy, guide, specification or email is accurate but too long or dense for its audience.
- A technical text must be understood by non-specialists.
- A document must fit a page, word or character limit.

## When not to use
- The goal is a short decision-oriented summary of a longer text, not a simplified full version. Use `executive-summary`.
- The problem is tone (too harsh, too informal), not length or complexity. Use `tone-rewrite`.
- The content itself is incomplete or wrong. Use `document-review` first.

## Inputs
Required:
- The text to simplify.

Optional, improves quality:
- Target audience and their expertise level.
- Target length or reduction goal.
- Terms or sections that must stay verbatim (legal wording, defined terms, contract clauses).

If the text is missing, ask. If the audience is unknown, assume an informed non-specialist and state it as `[ASSUMPTION]`.

## Process
1. Inventory the load-bearing content before editing: obligations (must/shall), permissions, prohibitions, numbers, dates, thresholds, conditions, exceptions, owners and decisions. This list is the invariant.
2. Identify verbatim zones (legal clauses, defined terms, quoted requirements) and leave them untouched or reference them.
3. Cut at the document level: remove repeated sections, background the reader does not need to act, and history that does not change decisions; move reference material to an appendix.
4. Restructure: lead with what the reader must do or know; convert sequences to numbered steps and parallel conditions to tables or lists.
5. Simplify sentences: one idea per sentence, active voice with a named actor, verbs instead of nominalizations ("decide" not "make a decision"), aim for about 15-20 words on average.
6. Replace jargon with plain words for the audience; keep necessary technical terms and define them once.
7. Remove hedges and fillers ("it should be noted that", "in order to", "basically") unless the hedge expresses real uncertainty.
8. Compare the result to the invariant list; every item must still be present with the same strength and value.
9. Report the reduction (approximate word count before/after) and any content deliberately removed or moved.
10. If the user's goal continues, suggest `document-review` for a full quality pass or `executive-summary` when a decision maker needs a one-page version.

## Output format
```markdown
## Simplified Version
<rewritten text>

## Change Notes
- Length: ~<before> → ~<after> words
- Removed: <what and why>
- Moved to appendix / referenced: <...>
- Kept verbatim: <...>
- Meaning check: all <n> obligations, numbers and conditions preserved | issues: <none or list>
```

## Quality checklist
- [ ] Every obligation, number, date, threshold, condition and exception from the source is still present.
- [ ] Modal strength is unchanged (must did not become should).
- [ ] Verbatim zones are untouched.
- [ ] Each sentence has a clear actor and one main idea.
- [ ] Jargon left in place is defined once.
- [ ] Change notes list anything removed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Simplifying away conditions and exceptions ("unless", "only if"), which changes the rule. Protect them in the invariant list.
- Shortening by making text vague ("as appropriate"). Short and precise, not short and ambiguous.
- Replacing precise terms with casual synonyms that have a different meaning in the domain.

## Example
Input (excerpt): "It should be noted that in the event that personal data is no longer required for the purpose for which it was originally collected, it is the responsibility of the data owner to ensure that the deletion of said data is carried out within a period not exceeding 30 days."

Excerpt of output: "When personal data is no longer needed for its original purpose, the data owner must delete it within 30 days."
Change note: 52 → 20 words; obligation (must), actor (data owner) and limit (30 days) preserved.
