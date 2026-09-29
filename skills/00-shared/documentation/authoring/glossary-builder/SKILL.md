---
name: glossary-builder
description: "Extracts domain terms, acronyms and overloaded words from source material and writes unambiguous, testable definitions with synonyms, forbidden usages and owners. Use when a project, document or team has inconsistent terminology, when onboarding people to a domain, when writing requirements or data models, or when someone asks for a glossary or ubiquitous language."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: documentation
  area: authoring
  title: "Build a glossary"
  related: "business-rules-catalog, bounded-context-map, technical-translation, data-catalog-entry, ambiguity-detection"
  prompt: "Build a glossary from these requirement notes; people use customer, client, account and subscriber interchangeably."
---

# Build a Glossary

## Purpose
Create a shared vocabulary in which each term has exactly one meaning per context, so requirements, code, data and conversations stop drifting apart and ambiguity-driven defects are prevented.

## When to use
- Source documents use several words for one concept, or one word for several concepts.
- A new domain, product or client engagement starts and people need a common language.
- Requirements, data models or APIs are being written and names must be fixed first.
- A translation or localization effort needs agreed term pairs.

## When not to use
- The need is to split a domain into models with different languages. Use `bounded-context-map` first, then build one glossary per context.
- A single dataset or table must be documented. Use `data-catalog-entry`.
- The task is to find ambiguous sentences in a requirement document. Use `ambiguity-detection`.

## Inputs
Required:
- Source material (documents, notes, transcripts, schemas, screens) or a list of terms.

Optional, improves quality:
- Domain or bounded context the glossary belongs to.
- Existing glossaries, standards or regulatory definitions to align with.
- Subject matter experts who can confirm definitions.

If no source material or term list is given, ask for it. Never define a domain term from general knowledge alone without marking it `[ASSUMPTION]`.

## Process
1. Scan the source for candidate terms: capitalized nouns, acronyms, domain verbs (for example "settle", "activate"), statuses, roles, units and identifiers.
2. Filter out general vocabulary; keep a term if a newcomer could misread it or if two people could reasonably define it differently.
3. Cluster synonyms and homonyms: note where different words point to one concept and where one word covers several concepts.
4. For each concept pick a preferred term, listing alternatives as synonyms or deprecated terms.
5. Write the definition in genus-differentia form: "<Term> is a <broader class> that <distinguishing characteristics>". Avoid circular definitions and do not use the term inside its own definition.
6. Add what the term is not (the nearest confusable concept), its lifecycle or states if relevant, and an example.
7. Record the context (domain, system, regulation) and source for each definition; when a legal or standard definition exists, reference it by name.
8. Mark definitions inferred from limited evidence as `[ASSUMPTION]` and assign a likely owner to confirm.
9. Sort alphabetically, expand acronyms, and cross-link related terms.
10. List conflicts that need a decision (for example, "Sales and Billing define active customer differently").
11. If the user's goal continues, suggest `business-rules-catalog` for rules hidden in definitions or `technical-translation` when the glossary must be bilingual.

## Output format
```markdown
# Glossary: <domain / context>
Scope: <what this glossary covers> | Sources: <documents used> | Status: draft

| Term | Definition | Not to be confused with | Synonyms / deprecated | Example | Source | Owner |
|---|---|---|---|---|---|---|
| <Preferred term> | <genus + differentia> | <nearest concept> | <alt terms> | <...> | <doc/section> | <role or [TBD]> |

## Acronyms
- <ACR>: <expansion> — see <term>

## Terminology Conflicts to Resolve
1. <term> — <meaning A (who)> vs <meaning B (who)> — <proposed resolution> — <decider>
```

## Quality checklist
- [ ] Each concept has one preferred term; synonyms are listed, not defined separately.
- [ ] No definition is circular or uses the defined term.
- [ ] Each definition distinguishes the term from its nearest confusable concept.
- [ ] Every definition cites its source or is marked `[ASSUMPTION]`.
- [ ] Conflicts are surfaced, not silently resolved.
- [ ] Acronyms are expanded.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Defining by example only ("A customer is e.g. ACME"). Give the class and distinguishing criteria, then the example.
- Forcing one enterprise-wide definition when contexts legitimately differ. Scope definitions per context and state the mapping.
- Including every noun. A long glossary nobody reads is worse than twenty sharp entries.

## Example
Input: Requirement notes using "customer", "client", "account" and "subscriber" interchangeably.

Excerpt of output:
- | Customer | A legal or natural person that has signed at least one contract with the company | Account (billing construct) | client (deprecated) | ACME Ltd. | Notes §2 | Sales ops `[TBD]` |
- | Account | A billing construct that groups one or more subscriptions under one invoice address | Customer | — | ACC-1042 | Notes §4 | Billing |
- Conflict: "active customer" — Sales: signed in last 12 months; Billing: has an unpaid or open invoice — needs product owner decision.
