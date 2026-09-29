---
name: sql-query-writing
description: "Writes a correct, readable and index-friendly SQL query for a stated question in the target database dialect: clarifies grain and join cardinality, handles NULLs, duplicates and time zones, uses sargable predicates and parameters, and states the indexes it relies on and how to verify results. Use when someone needs a query for a report, feature, data fix or investigation, asks to translate a question into SQL, or wants an existing query rewritten for correctness or readability."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: coding
  title: "Write a SQL query"
  related: "query-optimization, index-recommendation, database-schema-design, metric-definition, performance-optimization"
  prompt: "Write a PostgreSQL query that returns, per customer, the number of orders and total revenue in the last 90 days, including customers with no orders."
---

# Write a SQL Query

## Purpose
Turn a data question into a query that returns the right rows at the right grain, reads clearly, runs efficiently on realistic volumes and is safe to embed in application code.

## When to use
- A report, feature, API or investigation needs data from a relational database.
- A business question must be translated into SQL.
- An existing query returns wrong counts, duplicates or is hard to read.

## When not to use
- A query is correct but slow and an execution plan is available. Use `query-optimization`.
- The need is choosing indexes for a workload. Use `index-recommendation`.
- The metric itself is not yet defined. Use `metric-definition` first.

## Inputs
Required:
- The question the result must answer.
- The relevant tables with columns and keys (DDL or description), and the database engine.

Optional, improves quality:
- Row volumes, existing indexes, sample data, how the query will be called (ad hoc, report, application with parameters), time zone and currency rules.

If the schema is not given, ask for it; do not invent table or column names. If it is partial, write the query and mark assumed names `[ASSUMED COLUMN]`.

## Process
1. Define the result grain: one row per what? List output columns with their definitions and units.
2. Identify source tables and join paths; for each join, state the cardinality (1:1, 1:N, N:M) and whether it can multiply rows.
3. Choose join types from the question: inner for "must have", left for "including those without"; put filters on the outer table in the `ON` clause when they must not remove unmatched rows.
4. Aggregate at the correct level: pre-aggregate the many side in a CTE or subquery before joining, to avoid fan-out double counting; never fix duplicates with `DISTINCT` without knowing why they appear.
5. Handle NULLs explicitly: `COALESCE` for display, `COUNT(col)` vs `COUNT(*)`, `NOT IN` with nullable subqueries (prefer `NOT EXISTS`).
6. Time: use half-open ranges (`>= start AND < end`), state the time zone, avoid functions on indexed columns in predicates (sargability).
7. Write for readability: CTEs with meaningful names, one clause per line, explicit column lists (no `SELECT *` in application code), consistent aliases.
8. Parameterize every external value; never build SQL by string concatenation.
9. State the indexes the query relies on and the expected access path; flag large scans, sorts and window functions over big sets.
10. Give verification queries: row count at grain, reconciliation total against a known figure, spot-check of edge rows (no orders, boundary dates).
11. If the goal continues, suggest `query-optimization` with the actual execution plan or `index-recommendation` if supporting indexes are missing.

## Output format
````markdown
# SQL Query: <question>
Engine: <dialect> · Grain: one row per <...> · Parameters: <list>

```sql
<query>
```

## Logic Notes
- Joins and cardinality: ...
- NULL / time zone handling: ...

## Index Assumptions
- ...

## Verification
```sql
<check queries>
```

## Assumptions and Open Questions
- ...
````

## Quality checklist
- [ ] The grain is stated and every join is checked for row multiplication.
- [ ] Filters on outer-joined tables do not silently turn the join into an inner join.
- [ ] NULL behavior and time ranges are explicit and half-open.
- [ ] Predicates are sargable and all external values are parameters.
- [ ] No table or column name is invented; assumptions are marked.
- [ ] Verification queries are provided.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Joining orders and order lines, then summing order totals, which multiplies revenue by the number of lines.
- `WHERE o.created_at >= ...` after a `LEFT JOIN orders`, which drops customers without orders.
- `BETWEEN '2024-01-01' AND '2024-01-31'` on a timestamp, which excludes almost all of the last day.
- `WHERE YEAR(created_at) = 2024`, which prevents index use.

## Example
Input: "Per customer, orders and revenue in the last 90 days, including customers with none. PostgreSQL. customers(id, name), orders(id, customer_id, total_amount, created_at)."

Weak: `SELECT c.name, COUNT(*), SUM(o.total_amount) FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.created_at > now() - interval '90 days' GROUP BY c.name;` (drops customers without orders, counts 1 for them, groups by non-unique name).

Strong excerpt:
```sql
WITH recent AS (
  SELECT customer_id, COUNT(*) AS order_count, SUM(total_amount) AS revenue
  FROM orders
  WHERE created_at >= now() - interval '90 days'
  GROUP BY customer_id
)
SELECT c.id, c.name, COALESCE(r.order_count, 0) AS order_count, COALESCE(r.revenue, 0) AS revenue
FROM customers c
LEFT JOIN recent r ON r.customer_id = c.id;
```
Index assumption: `orders(created_at, customer_id)` or `orders(customer_id, created_at)` depending on selectivity `[VERIFY with plan]`.
