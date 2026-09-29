---
description: "Reviews any document for clarity, completeness, internal consistency, correctness of claims and fit to its audience and purpose, returning prioritized, located findings with suggested fixes and a verdict. Use when someone asks for feedback on a draft, needs a document checked before approval or publication, or wants a second opinion on a specification, proposal, policy, guide or report."
related: "requirements-review-checklist, architecture-review, document-simplify, style-guide-check, doc-diff-summary"
prompt: "Review this incident process document before we send it to the operations directors for approval."
---

# Review a Document

## Purpose
Give the author actionable, prioritized findings that make the document fit for its readers and its decision, instead of a list of stylistic opinions.

## When to use
- A draft is about to go for approval, sign-off or publication.
- An author asks for feedback or a second pair of eyes.
- A document received from a vendor, client or another team must be assessed before relying on it.

## When not to use
- The document is a requirements specification needing formal quality criteria. Use `requirements-review-checklist`.
- The content is an architecture to be evaluated on its merits. Use `architecture-review` or `atam-evaluation`.
- Only conformance to a style guide is needed. Use `style-guide-check`. Only shortening is needed: `document-simplify`.

## Inputs
Required:
- The document text.

Optional, improves quality:
- Purpose, audience and the decision or action it should enable.
- Review focus (for example completeness only), organization template, related documents.
- Review depth: quick scan or full review.

If the document is missing, ask for it. If purpose and audience are not given, infer them from the text, state the inference as `[ASSUMPTION]` and review against it.

## Process
1. Determine purpose, audience and document type; write them at the top of the review so findings can be judged against them.
2. Read once end to end without commenting to understand the argument; then write a two-sentence summary. If you cannot, clarity is the first finding.
3. Structure: does the order serve the reader (conclusion or ask early, details later)? Are headings informative?
4. Completeness: check the sections the document type requires (for example scope, owners, exceptions, dates, success criteria, rollback) and questions the audience will ask that are not answered.
5. Consistency: compare numbers, names, dates, terms and statements across sections, tables and diagrams; list contradictions with both locations.
6. Correctness and support: flag claims without evidence, figures without source, and statements that conflict with known standards or the provided context. Do not assert facts you cannot verify; ask instead.
7. Clarity: find ambiguous words (appropriate, quickly, etc.), undefined acronyms, passive sentences that hide the actor, and paragraphs doing two jobs.
8. Audience fit: jargon level, length, tone and whether required actions are explicit for each reader group.
9. Classify each finding: Critical (blocks purpose or is wrong), Major (reader will misunderstand or ask), Minor (polish). Give location, issue and a concrete fix or rewrite.
10. Give an overall verdict: ready, ready with minor changes, or needs rework, plus the top three actions.
11. If the user's goal continues, suggest `document-simplify` when length or jargon is the main finding, or `requirements-review-checklist` for requirement documents.

## Output format
```markdown
# Review: <document title / version>
Purpose (assumed?): <...> | Audience: <...> | Verdict: <Ready / Minor changes / Rework>
Summary of the document: <2 sentences>

## Top 3 Actions
1. ...

## Findings
| # | Severity | Location | Issue | Suggested fix |
|---|---|---|---|---|
| 1 | Critical | §3.2 | <...> | <rewrite or action> |

## Questions for the Author
- ...

## Strengths to Keep
- ...
```

## Quality checklist
- [ ] Every finding has a location and a concrete fix, not just a complaint.
- [ ] Severities are justified by impact on purpose and audience.
- [ ] Contradictions cite both locations.
- [ ] No new facts are introduced; unverifiable claims become questions.
- [ ] The verdict is consistent with the Critical and Major findings.
- [ ] Comments focus on the document, not the author.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Drowning critical issues among fifty typo comments. Group minor issues and lead with what blocks the purpose.
- Reviewing against your preferred structure rather than the document's purpose and audience.
- Rewriting the whole document instead of reviewing. Suggest targeted rewrites; offer a full rewrite only if asked.

## Example
Input: Incident process draft for operations directors.

Excerpt of output:
- Verdict: Minor changes. Summary: defines severity levels and escalation paths for production incidents.
- | 1 | Critical | §4 table vs §2 text | Sev-1 response time is 15 min in §2 but 30 min in §4 | Align to one value; confirm with the service owner |
- | 2 | Major | §5 | No owner for closing the incident and triggering the postmortem | Add "Incident commander closes and schedules postmortem within `[TBD]` days" |
