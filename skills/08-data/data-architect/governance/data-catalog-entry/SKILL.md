---
name: data-catalog-entry
description: "Writes a data catalog entry for a dataset, table, report or data product: business description, owner and steward, grain, key fields, lineage summary, quality status, freshness, sensitivity and access, and usage guidance. Use when registering or documenting a dataset for discovery, preparing it for self-service, or when asked to describe a table or data product for the catalog."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: data-architect
  area: governance
  title: "Write a data catalog entry"
  related: "data-lineage-doc, data-classification, data-quality-rules, data-contract, glossary-builder"
  prompt: "Write a catalog entry for the table sales.fact_invoice_line using this DDL and the notes from the finance team."
---

# Write a Data Catalog Entry

## Purpose
Let a consumer who has never talked to the producer decide in two minutes whether a dataset fits their need, how to use it correctly and whom to ask, while giving governance the ownership and sensitivity facts it needs.

## When to use
- A new dataset, table, view, report or data product is published.
- Consumers repeatedly ask the same questions about a dataset or misuse it.
- A catalog clean-up or certification campaign is running.

## When not to use
- Binding producer-consumer guarantees are needed. Use `data-contract`.
- Full transformation-level lineage is needed. Use `data-lineage-doc`.
- Business terms rather than datasets are being defined. Use `glossary-builder`.

## Inputs
Required:
- The dataset identifier and at least one of: schema/DDL, sample query, producer description.

Optional:
- Owner/steward, upstream sources, refresh schedule, known quality issues, classification, typical queries, related glossary terms.

If neither schema nor description is provided, ask. Everything else becomes `[UNKNOWN]` rather than a guess.

## Process
1. Write a business-first summary: what one row represents (grain), what questions it answers, and what it does not cover.
2. Record ownership: data owner (accountable business role), steward (day-to-day), technical custodian; mark unknowns.
3. Describe the key fields: primary/business key, time fields (which date to filter on and its time zone), main measures with units, main dimensions; link each to glossary terms.
4. Summarize lineage in one line per hop: source systems → key transformations → this dataset → known downstream consumers.
5. State freshness and schedule: update frequency, expected availability time, history depth, late-data behaviour.
6. State quality status: certified/uncertified, active checks, known issues and workarounds, last incident.
7. State sensitivity and access: classification level, personal data fields, masking in place, how to request access.
8. Give usage guidance: correct join keys, common filters, pitfalls (double counting, cancelled records, currency), sample query in neutral SQL.
9. Add tags and search synonyms the business actually uses.
10. Set lifecycle fields: status (draft, published, deprecated), version, review date.
11. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest the next skill: `data-lineage-doc` to document lineage in depth, `data-quality-rules` to back the quality section, or `data-classification` if sensitivity is unconfirmed.

## Output format
```markdown
# <Dataset display name>
Identifier: <...> | Type: <table/view/stream/report/data product> | Status: <...> | Certified: <yes/no>

## Summary
<2-3 sentences: grain, purpose, not covered>

## Ownership
Owner: <...> | Steward: <...> | Technical custodian: <...>

## Key Fields
| Field | Meaning | Glossary term | Notes (unit, TZ, nulls) |
|---|---|---|---|

## Lineage (summary)
<source> → <transformation> → this → <consumers>

## Freshness
Frequency: <...> | Available by: <...> | History from: <...>

## Quality
Checks: <...> | Known issues: <...>

## Sensitivity and Access
Classification: <...> | Personal fields: <...> | Masking: <...> | Access request: <...>

## How to Use
- Join on: <...> | Filter on: <...>
- Pitfalls: <...>
- Sample query: <...>

## Tags / Synonyms | Review date
```

## Quality checklist
- [ ] Grain is stated in one sentence.
- [ ] Owner and steward are named or explicitly `[UNKNOWN]`.
- [ ] The correct date field and time zone for filtering are stated.
- [ ] Sensitivity and access process are present; personal fields are listed.
- [ ] At least one pitfall and one sample query are given.
- [ ] No invented SLAs, owners or quality claims.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Restating column names as descriptions ("customer_id: customer id"). Describe meaning, units and edge cases.
- Technical-only entries readable by engineers alone. Lead with the business summary.
- Stale entries. Set a review date and tie updates to schema changes.

## Example
Input: "fact_invoice_line DDL; finance: includes credit notes as negative lines; loaded nightly."

Excerpt of output:
- Summary: One row per invoice line, including credit notes as negative lines. Answers billed revenue by customer, product and period. Does not include unbilled orders.
- Pitfall: Filter on invoice_date (local time) for revenue; order_date gives different totals.
- Owner: `[UNKNOWN]` (proposed: Finance Controlling); Freshness: nightly, available by `[TBD]`.
