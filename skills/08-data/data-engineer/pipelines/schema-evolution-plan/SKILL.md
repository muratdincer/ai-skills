---
description: "Plans a schema change in a data pipeline, event stream or shared dataset: classifies each change as backward, forward or fully compatible or breaking, picks the evolution pattern (additive, expand-contract, versioned dataset or topic, dual write), and sequences producer, pipeline and consumer changes with backfill, validation and deprecation. Use when a source adds, renames, retypes or removes fields, when a data contract must change, or when consumers keep breaking on upstream schema drift."
related: "data-contract, schema-migration-plan, incremental-load-design, source-to-target-mapping, data-lineage-doc"
prompt: "The CRM team will rename customer_type to segment and change it from free text to an enum next month. Plan the schema evolution for our pipeline and the 6 downstream consumers."
---

# Plan Schema Evolution

## Purpose
Change the shape of data that others depend on without breaking consumers, losing history or freezing producers. The plan makes compatibility explicit per change and orders the rollout so every intermediate state is valid.

## When to use
- A source system or producer will add, rename, retype, split or remove fields.
- A shared dataset, event schema or data contract needs a new version.
- Unannounced schema drift keeps breaking pipelines and a controlled process is needed.

## When not to use
- The change is a DDL migration inside one operational database. Use `schema-migration-plan`.
- The agreement between producer and consumer itself (semantics, SLAs, ownership) must be written. Use `data-contract`.
- A pipeline has already broken on drift and needs diagnosis first. Use `pipeline-failure-analysis`.

## Inputs
Required:
- The current schema and the intended change (field-level: add, rename, type change, nullability, semantics, removal).
- Where the data flows: storage format or transport (table, file format, event/topic with or without a schema registry).

Optional:
- Consumer list from lineage, data contract, compatibility mode in use, retention of historical data, release dates of producer and consumers.

If the consumers are unknown, say so and make consumer discovery the first step; do not assume there are none.

## Process
1. List every change at field level and classify each: backward compatible (new readers read old data), forward compatible (old readers read new data), full, or breaking. Treat semantic changes (unit, meaning, allowed values) as breaking even when the type stays the same.
2. Identify consumers and how they read: by position or name, strict or tolerant parser, schema-on-read or on-write, cached schemas, BI extracts, ML features. Record each consumer's owner and release cadence.
3. Choose the evolution pattern per change: additive with default (safe), expand-contract (add new, dual populate, migrate consumers, remove old), versioned dataset/topic/view (`v2` side by side), or a compatibility view that maps new to old shape.
4. Define the target schema and mapping rules: old to new field mapping, type conversion and value mapping (for enums, a complete table plus handling of unmapped values), defaults for historical rows, null semantics.
5. Decide how history is handled: rewrite/backfill historical partitions, keep mixed schemas with read-time coalescing, or freeze old data under the old version. Note storage format constraints (column reorder, type widening vs narrowing, partition column changes).
6. Sequence the rollout so every step is valid on its own: registry/compatibility setting, pipeline accepts both shapes, producer emits new shape (and old if dual writing), backfill, consumers migrate one by one, old fields deprecated then removed.
7. Define validation at each step: schema compatibility check in CI or registry, row counts and null rates of new vs old fields, value mapping coverage, consumer smoke tests.
8. Define rollback per step and the point of no return (usually removal of the old field or dropping the old version).
9. Set the deprecation policy: announcement, window, usage monitoring on old fields or versions, and the removal criterion (zero reads for a defined period, not a date alone).
10. List risks, assumptions and open questions, and name owners for producer, pipeline and each consumer step.
11. Fill the output template. If the goal continues, suggest `data-contract` to formalize the new version, `source-to-target-mapping` to update mappings or `data-lineage-doc` to refresh lineage.

## Output format
```markdown
# Schema Evolution Plan: <dataset/stream> v<old> → v<new>
Pattern: <additive / expand-contract / versioned / compatibility view>

## Changes
| Field | Change | Compatibility | Pattern | Notes |
|---|---|---|---|---|

## Consumers
| Consumer | Owner | Reads how | Impact | Migration step |
|---|---|---|---|---|

## Mapping Rules
- <old> → <new>: <conversion, value map, default, unmapped handling>

## Historical Data
<backfill / mixed with coalesce / frozen> – <reason>

## Rollout Sequence
| Step | Action | Owner | Validation | Rollback |
|---|---|---|---|---|
Point of no return: <step>

## Deprecation
Announcement: <...> | Window: <...> | Removal criterion: <...>

## Risks, Assumptions, Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every field change is classified, and semantic changes are treated as breaking.
- [ ] Each rollout step leaves producers, pipeline and all consumers in a working state.
- [ ] Value mappings are complete and unmapped values have defined handling.
- [ ] Historical data treatment is explicit.
- [ ] Removal depends on measured zero usage, and the point of no return is named.
- [ ] Inferences about consumers and formats are labeled; nothing is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Renaming a field in place: for every reader this is a removal plus an addition, and it breaks them all at once. Use expand-contract.
- Checking only syntactic compatibility; a registry accepts a field whose unit changed from cents to euros.
- Forgetting consumers outside the lineage graph (spreadsheets, ad hoc exports, cached BI extracts); monitor reads before removal.

## Example
Input: "CRM renames customer_type (free text) to segment (enum: RETAIL, SME, CORPORATE) next month; 6 consumers."

Excerpt of output:
- Change: rename + retype + semantic restriction → breaking; pattern expand-contract.
- Mapping: 'retail', 'Retail ', 'individual' → RETAIL; unmapped values → UNKNOWN and counted daily `[ASSUMPTION: CRM confirms full value list]`.
- Rollout: (1) pipeline adds `segment`, derives it from `customer_type` for history; (2) CRM emits both fields; (3) consumers migrate; (4) `customer_type` removed after 30 days with zero reads.
