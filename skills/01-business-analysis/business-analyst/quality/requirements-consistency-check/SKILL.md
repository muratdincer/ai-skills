---
name: requirements-consistency-check
description: "Compares requirements against each other and against business rules, glossary, data and NFRs to find contradictions, duplicates, overlaps, inconsistent terminology and conflicting values, and proposes a resolution path for each. Use when several documents, authors or versions describe the same scope, after merging stories from multiple teams, or before baselining requirements."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "Check requirements consistency"
  related: "ambiguity-detection, requirements-gap-analysis, business-rules-catalog, glossary-builder, traceability-matrix"
  prompt: "We have a BRD, an FRD and 45 user stories for the same billing scope. Find contradictions and duplicates."
---

# Check Requirements Consistency

## Purpose
Ensure the requirement set says one thing once. Contradictions and near-duplicates are found early, each with evidence and a proposed resolution owner, so the baseline can be trusted.

## When to use
- Multiple sources (BRD, FRD, stories, contract annex, regulation) cover the same scope.
- Several analysts or teams wrote requirements in parallel.
- A new version or change request was merged into an existing baseline.

## When not to use
- Individual statements are vague. Use `ambiguity-detection`.
- Things are missing rather than conflicting. Use `requirements-gap-analysis`.
- Building business rules from scratch. Use `business-rules-catalog`.

## Inputs
Required:
- The requirements to compare, with source and ID for each.

Optional, improves quality:
- Precedence order of sources (e.g. regulation > contract > BRD > stories).
- Glossary, business rules catalog, data dictionary, NFR targets.

If sources have no IDs, assign `<source>-<n>` IDs and state the mapping.

## Process
1. Normalize: restate each requirement as actor + action + object + condition + value, keeping the source ID.
2. Group requirements by business object, process step and quality attribute so comparable statements sit together.
3. Detect direct contradictions: same condition, different outcomes (e.g. "approve automatically" vs "always requires manager approval").
4. Detect value conflicts: different numbers, limits, formats, time windows, rounding or currencies for the same thing.
5. Detect rule/state conflicts: a transition allowed in one place and forbidden in another; conflicting mandatory/optional fields.
6. Detect NFR tensions: e.g. data retention vs deletion right, real-time vs batch, availability vs maintenance windows.
7. Detect terminology inconsistency: different words for the same concept, or one word for different concepts.
8. Detect duplicates and overlaps: identical or near-identical requirements; partial overlaps that will drift.
9. For each finding, classify severity (Blocking / Major / Minor), cite both sources, and propose a resolution: which source prevails under the stated precedence, merge, or escalate to a named decision owner. Never pick a winner by guessing.
10. Summarize decisions needed and suggest a consolidated wording where the resolution is clear.
11. If the user wants to continue, suggest `business-rules-catalog` to consolidate the resolved rules, `glossary-builder` for conflicting terms or `traceability-matrix` to keep merged IDs traceable.

## Output format
```markdown
# Consistency Check: <scope>
Sources: <list with versions> · Precedence: <order or [UNKNOWN]>

## Summary
<counts by type and severity; decisions needed>

## Findings
| # | Type | Requirement A (source/ID) | Requirement B (source/ID) | Conflict | Severity | Proposed resolution | Decision owner |
|---|---|---|---|---|---|---|---|

## Terminology Alignment
| Concept | Terms used (where) | Proposed single term |
|---|---|---|

## Duplicates to Merge
| Keep | Retire | Note |
|---|---|---|
```

## Quality checklist
- [ ] Both sides of every conflict are cited with source and ID.
- [ ] Resolutions follow the stated precedence or are escalated, never guessed.
- [ ] Value conflicts quote exact numbers/units from both sources.
- [ ] Terminology findings map to one proposed term each.
- [ ] Duplicates identify which ID survives so traceability is not lost.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Flagging different detail levels as conflicts (a BRD goal and a story that refines it). Conflict means both cannot be true at once.
- Silently resolving in favor of the newest document. Recency is not precedence unless the team agreed so.
- Missing conflicts hidden in NFRs and data rules because only functional statements were compared.

## Example
Input: BRD-12 "Invoices are issued on the 1st of each month." Story ST-40 "As a customer I want my invoice on my contract anniversary day."

Excerpt of output:
| # | Type | Requirement A | Requirement B | Conflict | Severity | Proposed resolution | Decision owner |
|---|---|---|---|---|---|---|---|
| C1 | Contradiction | BRD-12 | ST-40 | Billing date: fixed 1st vs anniversary | Blocking | Escalate; if both needed, define segment rule (e.g. corporate vs retail) `[TBD]` | Billing product owner |
