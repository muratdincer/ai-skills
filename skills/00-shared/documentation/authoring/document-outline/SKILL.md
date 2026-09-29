---
name: document-outline
description: "Proposes a fit-for-purpose structure for any document (design doc, policy, guide, report, proposal, specification) from its purpose, audience and decisions it must support, with section goals and content notes. Use when someone must start a new document, faces a blank page, inherited a messy document to restructure, or asks what sections a document should have."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: documentation
  area: authoring
  title: "Outline a document"
  related: "docs-information-architecture, document-review, executive-summary, technical-design-doc, brd-writing"
  prompt: "Outline a document proposing that we move our batch reporting jobs to an event-driven pipeline; readers are the architecture board."
---

# Outline a Document

## Purpose
Produce a section-by-section skeleton that is derived from what the document must achieve, so the writer fills a proven structure instead of discovering it while writing, and readers find what they need in the order they need it.

## When to use
- A new document is needed and the author knows the topic but not the structure.
- An existing document has grown organically and needs a new structure before rewriting.
- Several authors will contribute and need an agreed skeleton with owners per section.
- An organization template exists but does not fit the specific case and needs tailoring.

## When not to use
- The whole documentation set (many pages) needs organizing. Use `docs-information-architecture`.
- The document exists and needs quality feedback, not a new structure. Use `document-review`.
- The document type has a dedicated skill with its own template (for example `technical-design-doc`, `brd-writing`, `adr`). Use that skill.

## Inputs
Required:
- The document's purpose: what the reader should know, decide or do after reading.
- The primary audience.

Optional, improves quality:
- Document type and any mandatory organizational template or standard.
- Source material, notes or an existing draft.
- Length limit, deadline, reviewers and approvers.

If purpose or audience is missing, ask for them in one question. Everything else becomes an assumption or open question.

## Process
1. Restate the purpose as a single "After reading, <audience> will <know/decide/do> <X>" sentence. If the reader must decide something, the structure is decision-first.
2. Classify the document: decision (proposal, ADR-like), reference (spec, policy, API), instructional (guide, runbook), or narrative/report (status, post-review). Each has a different backbone.
3. Identify secondary audiences and what each will skim for; plan a summary or table that serves them without reading everything.
4. Choose the backbone: decision = context, problem, options, recommendation, consequences; reference = scope, definitions, rules/items, exceptions; instructional = prerequisites, steps, verification, troubleshooting; report = summary, findings, analysis, next steps.
5. Check for mandated content: regulatory sections, standard structures (for example ISO/IEC/IEEE 29148 for requirements, arc42 for architecture), organization templates. Map them onto the backbone rather than duplicating.
6. For each section, write one line stating its goal and the key question it answers, plus content notes and sources to use.
7. Order sections by reader need, not by writing order or chronology; put what the primary reader needs first.
8. Remove sections that do not serve the purpose; move nice-to-have material to appendices.
9. Add length guidance per section so the total fits the limit, and mark sections needing input from others with an owner or `[TBD]`.
10. List open questions that block specific sections.
11. Label every section, audience or purpose you inferred rather than read in the input as `[ASSUMPTION]`, so the requester can confirm it before writing starts.
12. If the user's goal continues, suggest `technical-design-doc` or `brd-writing` to fill the outline, then `document-review` on the draft.

## Output format
```markdown
# Outline: <document title>
Purpose: After reading, <audience> will <know/decide/do> <X>.
Document type: <decision / reference / instructional / report>
Primary audience: <...> | Secondary: <...>
Target length: <pages or words> | Mandated template/standard: <name or none>

| # | Section | Goal / question it answers | Content notes and sources | Length | Owner |
|---|---|---|---|---|---|
| 1 | Summary | <...> | <...> | <...> | <...> |

## Appendices
- <material moved out of the main flow>

## Open Questions
1. <question> — <section blocked> — <who can answer>
```

## Quality checklist
- [ ] The purpose sentence names an audience and an outcome.
- [ ] The backbone matches the document type (decision documents lead with the recommendation or the decision needed).
- [ ] Every section has a stated goal; none exists "because templates have it".
- [ ] Mandated sections are present and mapped, not duplicated.
- [ ] Section lengths add up to the target length.
- [ ] Unknowns are marked `[TBD]` or listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Outlining in the order the author learned things (history first). Readers want the conclusion and the ask first.
- Copying a generic template wholesale; half the sections end up "N/A". Tailor and delete.
- Mixing reference and instructional content in one flow. Split steps from facts, or use separate sections.

## Example
Input: "Proposal to move batch reporting jobs to an event-driven pipeline, for the architecture board."

Excerpt of output:
- Purpose: After reading, the architecture board will decide whether to fund a pilot for event-driven reporting.
- Type: decision.
- | 1 | Decision requested | What exactly is the board asked to approve? | Scope, budget `[TBD]`, pilot length | 0.5 page | Author |
- | 4 | Options considered | Why not keep batch or tune it? | Status quo, optimized batch, CDC + streaming | 1 page | Author |
- Open question: Is the pilot budget within the board's approval limit? — section 1 — PMO.
