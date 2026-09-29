---
description: "Elicits requirements from existing documents such as specifications, user manuals, procedures, contracts, regulations, forms and reports, producing a source-traced list of candidate requirements, business rules, data items and conflicts. Use when legacy documentation, a regulation or a contract must be mined before interviews, or when asked 'what requirements can we get out of these documents?'."
related: "business-rules-catalog, interview-question-set, requirements-consistency-check, traceability-matrix, glossary-builder"
prompt: "Extract the requirements from this 20-page operations manual of our current claims system and the new regulation text, and show where they conflict."
---

# Elicit From Existing Documents

## Purpose
Turn existing documents into a traceable set of candidate requirements, rules and questions, so interviews start from evidence and stakeholder time is spent on what the documents cannot answer.

## When to use
- A legacy system is being replaced and its manuals, specs or procedures are the main knowledge source.
- A regulation, standard or contract imposes obligations that must become requirements.
- Before interviews or workshops, to prepare hypotheses and avoid asking what is already written.

## When not to use
- The input is interview or meeting notes. Use `interview-notes-analysis`.
- The input is already a requirements set to be checked for gaps. Use `requirements-gap-analysis`.
- Only the business rules need to be normalized. Use `business-rules-catalog`.

## Inputs
Required:
- The document text or excerpts, with a name and, if known, version and date.
- The scope or question the analysis serves (e.g., "claims intake for the new system").

Optional, improves quality:
- Document owner and status (current, draft, superseded).
- Glossary or known domain terms.
- A list of what is already known, to avoid duplicates.

If no document text is given, ask for it. If the scope is missing, ask one question for it; otherwise every sentence becomes a candidate requirement.

## Process
1. Inventory the sources: title, type (regulation, contract, manual, procedure, spec, form, report), version, date, owner, authority level (binding / descriptive / informal). Flag outdated or superseded sources.
2. Mask personal data found in samples, forms or screenshots; keep only field names and formats.
3. Read against the scope and extract statements that express an obligation, capability, rule, constraint, data item, calculation, exception or quality expectation. Record the exact location (section, page, clause).
4. Classify each extract: Obligation (legal/contractual), Functional, Business rule, Data, NFR, Interface, Report, Process step, Term.
5. Separate what the document says from how the current system happens to do it. A screen layout in a manual describes today's solution, not a requirement; mark it `As-is behavior`.
6. Rewrite each item as a candidate requirement in neutral form, keeping modal strength from the source (must/shall vs should vs may). Anything you interpret beyond the text is labeled `[ASSUMPTION]`.
7. Detect conflicts and overlaps across sources (e.g., manual says 30 days, regulation says 15), and gaps where the document is silent on an obvious case.
8. Extract domain terms and data items into a mini glossary with the source definition.
9. Rate confidence per item: High (binding, current source), Medium (descriptive, current), Low (old, informal or single mention). Low items need confirmation.
10. Produce questions for stakeholders only for conflicts, gaps and low-confidence items, each with a likely owner.
11. If the goal continues, suggest `business-rules-catalog` for the rules, `interview-question-set` to confirm open points, or `traceability-matrix` to keep source links.

## Output format
```markdown
# Document Analysis: <scope>

## Sources
| ID | Document | Type | Version / date | Authority | Status |
|---|---|---|---|---|---|
| S1 | ... | Regulation | ... | Binding | Current |

## Candidate Requirements
| ID | Statement (neutral) | Category | Source (doc, section) | Strength | Confidence | Note |
|---|---|---|---|---|---|---|
| DR-01 | ... | Obligation | S1 §4.2 | Must | High | |

## As-Is Behavior (not requirements)
- ...

## Conflicts and Gaps
| # | Topic | Source A | Source B / silence | Impact | Question | Owner |

## Glossary Extract
- <term>: <definition> (S#)

## Open Questions
1. ...
```

## Quality checklist
- [ ] Every item cites a source and location; nothing is untraceable.
- [ ] As-is implementation details are kept apart from requirements.
- [ ] Modal strength matches the source; "should" was not upgraded to "must".
- [ ] Conflicts between sources are shown, not resolved silently.
- [ ] Superseded or undated sources are flagged and their items rated Low.
- [ ] Personal data from samples is masked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Copying the old system into the new one. Ask for each as-is item whether the need still exists.
- Treating a regulation summary as the regulation. Cite the binding text and flag secondary sources.
- Extracting everything. Filter by the scope, or the list becomes unreviewable.

## Example
Input: Claims manual v3 (2019) §5: "Clerk enters the claim within 30 days and prints form K-12." Regulation §4.2: "Claims shall be registered within 15 days of notification."

Excerpt of output:
| ID | Statement | Category | Source | Strength | Confidence |
|---|---|---|---|---|---|
| DR-01 | A claim must be registered within 15 days of notification. | Obligation | S2 §4.2 | Must | High |
| DR-02 | Printing form K-12 | As-is behavior | S1 §5 | – | Low |

Conflict: S1 says 30 days, S2 says 15 days. The regulation is binding; confirm with Compliance whether the manual is outdated.
