---
description: "Extracts business rules from documents, notes, requirements or code descriptions and normalizes them into a catalog with IDs, rule type (constraint, computation, inference, action enabler, fact), atomic declarative statement, source, owner, effective dates, exceptions and the requirements that use them. Use when rules are scattered or buried in processes and screens, conflict between sources, or when asked to 'list the business rules' or build a rulebook."
related: "document-analysis, decision-table-testing, requirements-consistency-check, frd-writing, glossary-builder"
prompt: "Extract and normalize the business rules from these credit application procedure notes into a catalog."
---

# Build a Business Rules Catalog

## Purpose
Make the organization's rules explicit, atomic and traceable in one place, so that they can be implemented once, tested precisely and changed without hunting through every document, screen and program that embeds them.

## When to use
- Rules are buried in procedures, emails, requirement documents or legacy system behavior.
- Different sources state the same rule differently, or rules change often (pricing, eligibility, approvals).
- Requirements, use cases or tests need stable rule IDs to reference.

## When not to use
- The source documents have not been read and mined yet. Use `document-analysis` first.
- Test cases must be derived from a complex rule set. Use `decision-table-testing`.
- Only term definitions are needed. Use `glossary-builder`.

## Inputs
Required:
- The source material containing rules (documents, notes, requirements, descriptions of system behavior).

Optional, improves quality:
- Existing rule catalog and ID scheme, glossary, rule owners, regulation references, effective dates.

If no source material is given, ask for it; do not write rules from general domain knowledge. Mark any rule you infer rather than read as `[ASSUMPTION]`.

## Process
1. Scan the sources for rule signals: "must", "only if", "cannot", "at least", "within", thresholds, calculations, approval levels, eligibility and status conditions.
2. Separate rules from process steps and UI behavior: a rule holds regardless of who or which system applies it.
3. Classify each rule: constraint (must/must not), computation (formula), inference (if conditions then conclusion), action enabler (condition triggers an action), or fact/definition.
4. Rewrite each as one atomic, declarative statement using glossary terms: one condition set, one consequence. Split compound rules; keep the original wording as the source quote.
5. Make parameters explicit (amounts, periods, percentages, roles) and separate them from the rule logic so they can change without rewriting the rule; unknown values become `[TBD]`.
6. For complex condition combinations, express the rule as a decision table and check it for completeness (every combination has an outcome) and overlap.
7. Record source (document, section, person), owner (who can change it), effective date, exceptions and enforcement point (manual, system, both).
8. Detect duplicates and contradictions across sources; do not resolve them silently, list them with both quotes and the owner who must decide.
9. Link each rule to the requirements, use cases or stories that apply it.
10. Collect assumptions and open questions with owners.
11. If the goal continues, suggest `decision-table-testing` to derive tests, `requirements-consistency-check` for wider contradictions, or `glossary-builder` for undefined terms.

## Output format
```markdown
# Business Rules Catalog: <domain>
Sources: <list> · ID scheme: BR-<area>-<nn>

| ID | Type | Rule statement | Parameters | Exceptions | Source (quote) | Owner | Effective | Enforced by | Used by |
|---|---|---|---|---|---|---|---|---|---|

## Decision Tables (for complex rules)
## Duplicates and Contradictions
| Rule A | Rule B | Conflict | Decision owner |
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every rule is atomic: one condition set, one consequence.
- [ ] Rules contain no process steps, UI behavior or implementation detail.
- [ ] Every rule has a type, a source quote and an owner (or `[UNKNOWN]` owner as an open question).
- [ ] Parameters are separated from logic; unknown values are `[TBD]`.
- [ ] Decision tables are complete and non-overlapping.
- [ ] Contradictions are listed with both sources, not resolved by guess; inferred rules are `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Cataloguing steps as rules ("The clerk checks the ID"). Ask what must be true; the rule is "An application requires a verified identity".
- Hard-coding thresholds in the statement. Parameterize them, because they change more often than the logic.
- Choosing the newest-looking source when two conflict. Only the rule owner can decide; list the conflict.

## Example
Input (procedure note): "Applications above 250,000 need the regional manager's approval, but for existing customers with no delays in the last 12 months branch approval is enough."

Excerpt of output:
| ID | Type | Rule statement | Parameters | Source | Owner |
|---|---|---|---|---|---|
| BR-CR-01 | Constraint | A credit application with amount above the regional approval limit requires regional manager approval, unless BR-CR-02 applies. | Regional limit = 250,000 `[TBD: currency]` | Procedure note §3 | Credit policy `[UNKNOWN]` |
| BR-CR-02 | Inference | An existing customer with no payment delay in the last N months qualifies for branch approval. | N = 12 | Procedure note §3 | Credit policy |

Open question: What counts as a "delay" (any days past due or above a threshold)? — Credit risk
