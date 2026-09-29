---
description: "Scans requirements text for vague words, undefined terms, weak or subjective phrases, unbounded lists, passive voice without an actor and untestable statements, and proposes precise rewrites. Use when reviewing requirements, user stories or acceptance criteria for clarity, or when testers or developers say a requirement can be read more than one way."
related: "requirements-gap-analysis, requirements-consistency-check, glossary-builder, acceptance-criteria, testability-review"
prompt: "Check these 20 requirements for ambiguous wording and suggest testable rewrites."
---

# Detect Ambiguous Requirements

## Purpose
Make every requirement readable in exactly one way, so that design, build and test reach the same interpretation. The output flags each ambiguity, explains the risk and proposes a precise, verifiable rewrite.

## When to use
- Before sign-off or estimation of a requirements document or story set.
- When developers, testers or vendors interpret the same requirement differently.
- When requirements come from a contract, RFP or regulation and will be used for acceptance.

## When not to use
- Content is missing rather than vague. Use `requirements-gap-analysis`.
- Requirements conflict with each other. Use `requirements-consistency-check`.
- Full checklist review before approval. Use `requirements-review-checklist`.

## Inputs
Required:
- The requirement statements, ideally with IDs.

Optional, improves quality:
- Project glossary or domain terms.
- Existing NFR targets or SLAs that define "fast", "secure" etc.

If there are no IDs, number the statements yourself (R1, R2...) and say so.

## Process
1. Split compound statements so each finding refers to one "shall"/behavior.
2. Flag vague qualifiers: fast, easy, user-friendly, flexible, robust, efficient, adequate, as appropriate, minimal, sufficient, modern, seamless.
3. Flag weak or optional modality: should, may, might, ideally, if possible, try to, support (without defined behavior).
4. Flag unbounded or open lists: etc., and so on, including but not limited to, such as, and/or.
5. Flag missing actors and triggers: passive voice ("is validated", "will be sent") without who/what/when.
6. Flag undefined or overloaded terms: domain words used with different meanings, acronyms without definition, pronouns (it, they, this) with unclear antecedent.
7. Flag unquantified quantities and times: many, large, quickly, real time, regularly, immediately, 24/7, all users.
8. Flag untestable statements: absolutes (never, always, 100%), negatives without scope, subjective satisfaction.
9. For each finding, write a rewrite that names actor, action, object, condition and measurable criterion; unknown values become `[TBD]` placeholders, never invented numbers.
10. Collect terms needing definition into a glossary candidate list.
11. If the user wants to continue, suggest `requirements-gap-analysis` for missing content, `glossary-builder` for the collected terms or `acceptance-criteria` to make rewritten statements testable.

## Output format
```markdown
# Ambiguity Review: <document / scope>

## Summary
<count of statements reviewed, count with findings, top patterns>

## Findings
| Req ID | Original text | Ambiguity type | Why it is risky | Proposed rewrite | Question to owner |
|---|---|---|---|---|---|

## Glossary Candidates
| Term | Observed usages | Proposed definition | Owner |
|---|---|---|---|

## Clean Statements
<IDs with no findings>
```

## Quality checklist
- [ ] Every finding quotes the exact problematic words.
- [ ] Rewrites keep the original intent; no scope is added or removed silently.
- [ ] No numeric target is invented; unknown thresholds are `[TBD]` with a question.
- [ ] Each rewrite is verifiable by a test, inspection, analysis or demonstration.
- [ ] Undefined terms are collected in the glossary candidates.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Replacing a vague word with another vague word ("fast" to "performant"). Always add a measurable criterion or a `[TBD]` placeholder.
- Treating every "should" as an error when the organization uses it deliberately for lower priority. Ask about the convention once and apply it consistently.
- Rewriting into solution design (e.g. "use a Redis cache") instead of observable behavior.

## Example
Input: "R4: The search should be fast and return relevant results for all users."

Excerpt of output:
| Req ID | Original text | Ambiguity type | Why it is risky | Proposed rewrite | Question to owner |
|---|---|---|---|---|---|
| R4 | "should be fast" | Vague qualifier, weak modality | No pass/fail threshold | The system shall return the first result page within `[TBD]` seconds at the 95th percentile under `[TBD]` concurrent users. | What response time and load are acceptable? |
| R4 | "relevant results" | Undefined term | Relevance cannot be tested | Results shall be ordered by `[TBD: ranking rule, e.g. exact match first, then date desc]`. | What ranking do users expect? |
