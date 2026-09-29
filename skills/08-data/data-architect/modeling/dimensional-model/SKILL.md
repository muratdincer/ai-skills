---
description: "Designs a dimensional (star/snowflake) model from business processes: declares the grain, fact tables and measure additivity, conformed dimensions, SCD type per attribute and handling of late-arriving and unknown members. Use when building a warehouse or lakehouse gold/mart layer, a semantic model for BI, or when asked for a star schema, bus matrix or fact/dimension design."
related: "metric-definition, dashboard-spec, report-requirements, data-vault-model, source-to-target-mapping"
prompt: "Design a star schema for retail sales and returns analysis; users need daily store/product KPIs and customer segment history."
---

# Design a Dimensional Model

## Purpose
Produce an analytics model that answers the business questions with consistent numbers across reports, predictable query performance and correct history, by fixing grain, facts and conformed dimensions before any table is built.

## When to use
- A BI, reporting or self-service analytics layer is being built or rebuilt.
- Different reports give different numbers for the same KPI and a conformed model is needed.
- A semantic layer or metric store needs a well-defined star schema underneath.

## When not to use
- The target is an auditable, source-aligned integration layer. Use `data-vault-model`.
- Operational/transactional schema design. Use `logical-data-model` or `database-schema-design`.
- Only one metric must be defined precisely. Use `metric-definition`.

## Inputs
Required:
- The business process(es) to analyse and the key questions or KPIs users need.
- The source events/records available (tables, feeds or descriptions).

Optional:
- Existing reports, metric definitions, dimensional bus matrix, volumes, latency needs, BI tool constraints (described generically), history requirements.

If business questions or sources are missing, ask for them; a model without a declared process and grain cannot be validated.

## Process
1. Choose the business process (an operational event, e.g. order line shipped), not a department or report.
2. Declare the grain in one sentence at the most atomic level the source supports ("one row per order line per shipment"). Everything else must conform to it.
3. Select the fact table type: transaction, periodic snapshot, accumulating snapshot, or factless (coverage/event). Use separate facts for different grains; never mix grains in one table.
4. List measures and classify additivity: additive, semi-additive (balances: not across time), non-additive (ratios: store numerator and denominator, compute in the semantic layer).
5. Identify dimensions via the "who, what, where, when, why, how" of the event. Build the bus matrix (processes × dimensions) and reuse conformed dimensions across facts.
6. Design each dimension: surrogate key, durable natural key, descriptive attributes flattened (prefer star over snowflake unless a shared outrigger is justified), hierarchies as columns.
7. Assign SCD type per attribute, not per table: 0 (fixed), 1 (overwrite), 2 (history with effective dates and current flag), 3/6 or mini-dimension for fast-changing attributes. Justify every Type 2 with a question that needs as-was reporting.
8. Handle special cases: date/time dimensions (fiscal calendar, time zone), role-playing dimensions via views, degenerate dimensions (order number), junk dimension for low-cardinality flags, bridge tables for multi-valued dimensions with weighting factors.
9. Define unknown/not-applicable/late-arriving members (fixed surrogate keys, inferred members updated later) and late-arriving facts policy.
10. Specify load rules per table: key lookup, SCD processing, restatement window, and reconciliation totals against the source.
11. Map each business question to the fact(s) and dimensions that answer it; flag questions the design cannot answer.
12. Note physical hints generically: partition facts by date, clustering on frequent filters, aggregate tables only for measured performance needs.
13. Label every inference `[ASSUMPTION]` and move unsupported items to open questions. If the goal continues, suggest the next skill: `source-to-target-mapping` to specify loads, or `metric-definition` to pin down the measures.

## Output format
```markdown
# Dimensional Model: <subject>
## Bus Matrix
| Business process (fact) | Grain | Date | Customer | Product | Store | ... |
|---|---|---|---|---|---|---|

## Fact: <name>
Type: <transaction/periodic/accumulating/factless> | Grain: <one sentence>
| Measure | Definition | Additivity | Unit |
|---|---|---|---|
Dimension keys: <list> | Degenerate: <list>

## Dimension: <name>
Natural key: <...> | Surrogate key: <...>
| Attribute | SCD type | Reason | Hierarchy level |
|---|---|---|---|
Special members: -1 Unknown, -2 Not applicable, inferred-member rule: <...>

## Question Coverage
| Business question | Fact(s) | Dimensions | Answerable? |
|---|---|---|---|

## Load and Reconciliation Rules
- ...

## Open Questions / Assumptions
- ...
```

## Quality checklist
- [ ] Every fact has exactly one declared grain, and all its measures and keys are true at that grain.
- [ ] Semi- and non-additive measures are flagged, with ratio components stored.
- [ ] Shared dimensions are conformed (same keys, attributes and meaning) across facts.
- [ ] SCD type is chosen per attribute and every Type 2 is justified.
- [ ] Unknown and late-arriving member handling is defined.
- [ ] Every business question maps to the model or is flagged as unanswerable.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Declaring the grain as a report ("monthly sales by region"). Start atomic; aggregate later.
- Type 2 everything "just in case", exploding dimension size and confusing users. Track only attributes with an as-was question.
- Storing percentages or averages in facts and then summing them. Store components.
- Snowflaking for storage savings that no longer matter, adding joins for every query.

## Example
Input: "Retail sales and returns, daily KPIs by store/product, and sales by customer segment as it was at purchase time."

Excerpt of output:
- Fact Sales Line: transaction; grain "one row per POS receipt line"; measures quantity, net amount (additive), unit price (non-additive, not summed).
- Fact Returns: separate fact at return-line grain, conformed Date, Store, Product, Customer.
- Customer.segment: SCD Type 2 (as-was reporting required); Customer.email: Type 1, personal data, masked in the mart.
