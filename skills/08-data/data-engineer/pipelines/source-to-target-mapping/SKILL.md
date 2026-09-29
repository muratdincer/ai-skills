---
description: "Writes a column-level source-to-target mapping (STTM) for a data load: target columns with type and nullability, source columns, transformation and business rules, lookups, defaults, key generation, filters, join conditions, rejects handling and test cases. Use when a pipeline, migration or integration load must be built or reviewed, when business rules for derived fields must be pinned down, or when someone asks for a mapping sheet between two schemas."
related: "pipeline-spec, field-mapping, data-lineage-doc, dimensional-model, test-data-design"
prompt: "Create a source-to-target mapping from the CRM customer and address tables into our dim_customer table."
---

# Write a Source-to-Target Mapping

## Purpose
Specify exactly how every target column is populated, so developers build the same logic analysts intended, testers can derive cases, and anyone can trace a target value back to its source.

## When to use
- Building a warehouse load, data migration or integration feed between two schemas.
- Reviewing an existing load whose logic lives only in code.
- Business rules for derived columns (status, segments, amounts) must be agreed and signed off.

## When not to use
- Mapping fields between application screens, APIs or messages in a business analysis context. Use `field-mapping`.
- The pipeline's scheduling, SLAs and operations are the topic. Use `pipeline-spec`.
- End-to-end flow across many hops for audit or impact. Use `data-lineage-doc`.

## Inputs
Required:
- Target schema (or target model) and source schema(s) or samples.

Optional:
- Business rules, code lists and reference data, existing SQL, data profiling results, known data issues, key strategy (surrogate/natural), SCD requirements.

If the target structure is missing, ask for it or suggest `dimensional-model` / `logical-data-model` first; mapping into an undefined target produces rework.

## Process
1. Define the target grain and the driving source (the table whose rows produce target rows), plus the join path and join types to other sources with their cardinality.
2. State dataset-level rules: filters (which source rows are included/excluded and why), deduplication rule, incremental selection criterion.
3. For each target column, record source table.column (or "derived"/"constant"/"generated"), and the transformation: cast, trim, case, split/concatenate, lookup, calculation, conditional logic, unit/currency/timezone conversion.
4. Write transformation logic unambiguously, as pseudo-SQL or CASE expressions, including null handling and the default for unmatched lookups (e.g. unknown member key -1).
5. Define key handling: natural/business key, surrogate key generation, and for dimensions the SCD type per attribute and effective-date logic.
6. Flag type and length mismatches between source and target (truncation, precision loss, encoding) and state the resolution.
7. Define rejects: which conditions reject or quarantine a row vs. load it with a default, and where rejects go.
8. Mark personal data columns and required masking or exclusion in the target.
9. Add test cases per non-trivial rule: input values and expected output, including nulls, boundaries and unmatched lookups.
10. Record the status of each mapping row (confirmed by business, `[ASSUMPTION]`, `[TBD]`) and the open questions. If the goal continues, suggest `pipeline-spec` to operationalize the load or `test-data-design` for fuller test data.

## Output format
```markdown
# Source-to-Target Mapping: <source> → <target>
Grain: <...> | Driving source: <...> | Load type: <full/incremental> | Version: <...>

## Joins and Filters
- <source A> LEFT JOIN <source B> ON <...> (1:n) — <reason>
- Filter: <...> | Dedup: <...>

## Column Mapping
| # | Target column | Type | Null | Source (table.column) | Transformation / rule | Default / unmatched | PII | Status |
|---|---|---|---|---|---|---|---|---|

## Keys and History
<business key, surrogate key, SCD type per attribute>

## Rejects
| Condition | Action | Destination |
|---|---|---|

## Test Cases
| Rule # | Input | Expected output |
|---|---|---|

## Open Questions
- [TBD] ...
```

## Quality checklist
- [ ] Every target column is mapped or explicitly marked derived/constant/generated.
- [ ] Grain, driving source and join cardinalities are stated; fan-out risks are addressed.
- [ ] Every transformation handles nulls and unmatched lookups.
- [ ] Type/length mismatches are flagged with a resolution.
- [ ] Personal data columns are marked with masking/exclusion.
- [ ] Unconfirmed rules are labeled `[ASSUMPTION]` or `[TBD]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- "Direct move" for every column. Silent casts, trims and timezone shifts are where defects hide; state them.
- Missing join cardinality: a 1:n join to addresses duplicates customers in the target.
- Business rules written in prose ("active customers only") without the precise predicate.

## Example
Input: "CRM customer + address into dim_customer (SCD2 on segment and city)."

Excerpt of output:
- Join: customer LEFT JOIN address ON customer_id AND address.type = 'BILLING' AND address.is_current = 1 (1:0..1) — prevents fan-out.
- segment: CASE WHEN annual_revenue >= [TBD threshold] THEN 'Enterprise' ELSE 'SMB' END; null revenue → 'Unknown'. `[ASSUMPTION: confirm with Sales Ops]`
- email: trim, lower; PII, masked in non-production targets.
