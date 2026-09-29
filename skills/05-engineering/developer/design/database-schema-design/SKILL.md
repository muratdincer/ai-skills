---
description: "Designs a relational database schema from a domain description: tables, columns and types, primary and foreign keys, constraints, indexes driven by access patterns, and a migration script outline. Use when a new feature needs persistent storage, an existing schema must be extended, or someone asks for tables, an ER model, DDL or indexes for a domain."
related: "logical-data-model, data-requirements, schema-migration-plan, index-recommendation, aggregate-design"
prompt: "Design the database schema for a meeting room booking feature: rooms, bookings with start/end time, attendees, and no overlapping bookings per room."
---

# Design a Database Schema

## Purpose
Produce a schema that enforces the domain's invariants in the database, supports the real access patterns efficiently, and can evolve through safe migrations.

## When to use
- A feature introduces new entities or relationships that must be stored.
- An existing schema is extended and the change must stay backward compatible.
- Query performance or data integrity problems point to the table design.

## When not to use
- Enterprise or cross-system data modeling. Use `logical-data-model` or `conceptual-data-model`.
- Only an index is needed for a slow query. Use `index-recommendation` or `query-optimization`.
- Rolling out a schema change to production. Use `schema-migration-plan`.

## Inputs
Required:
- The domain description or entities with their rules, and the target database engine (or "relational, engine-neutral").

Optional, improves quality:
- Main read/write access patterns and expected volumes, retention needs, multi-tenancy model.
- Naming conventions, existing schema, ID strategy, audit/soft-delete policy.

If the engine is unknown, write portable SQL and flag engine-specific choices as `[ENGINE-SPECIFIC]`.

## Process
1. Extract entities, attributes and relationships with cardinalities; list the invariants in plain language ("a room cannot have overlapping bookings").
2. Normalize to 3NF by default; denormalize only for a named access pattern and state the consistency cost.
3. Choose keys: surrogate primary key strategy (sequence, UUIDv7/ULID for distributed inserts), natural unique keys as `UNIQUE` constraints.
4. Choose column types precisely: exact decimals for money with separate currency, timestamps with time zone in UTC, bounded text lengths, no free-form strings for enumerations without a check or lookup table.
5. Enforce invariants in the database where possible: `NOT NULL`, `CHECK`, `UNIQUE`, foreign keys with deliberate `ON DELETE` behavior, exclusion or partial unique constraints where the engine supports them.
6. Derive indexes from access patterns: each foreign key used in joins, composite indexes in filter-then-sort order, covering indexes only for hot queries; note write cost.
7. Decide cross-cutting columns: tenant id, audit (created/updated by and at), optimistic concurrency version, soft delete (and how uniqueness works with it).
8. Mark personal data columns, and state retention and masking needs.
9. Write DDL and a migration outline that is backward compatible (expand, backfill, switch, contract).
10. List assumptions and open questions, especially on volumes and deletion rules.

## Output format
````markdown
# Schema Design: <feature>
Engine: <engine or engine-neutral> · Assumptions: <list>

## Entities and Invariants
| Entity | Key attributes | Invariants |

## Tables
### <table>
| Column | Type | Null | Default | Constraint | Notes (PII?) |

## Relationships
| From | To | Cardinality | FK on delete |

## Indexes
| Index | Columns | Serves access pattern | Write cost note |

## DDL
```sql
CREATE TABLE ...
```

## Migration Outline
1. Expand ... 2. Backfill ... 3. Switch ... 4. Contract ...

## Open Questions
````

## Quality checklist
- [ ] Every stated invariant is enforced by a constraint or explicitly assigned to application code with a reason.
- [ ] Every index maps to an access pattern; no speculative indexes.
- [ ] Money, time and identifiers use precise, unambiguous types.
- [ ] Foreign key delete behavior is chosen deliberately, not left to default.
- [ ] Personal data columns are marked and retention is addressed.
- [ ] The migration can run without downtime or states why it cannot.

## Common pitfalls
- Enforcing uniqueness or non-overlap only in application code; concurrent requests will break it. Use constraints or explicit locking.
- Soft delete that silently breaks unique constraints. Use partial unique indexes or include the deletion marker.
- Storing local time without zone, or floats for money.
- Generic "entity-attribute-value" or JSON columns for data that is queried and validated. Use them only for truly schemaless extensions.

## Example
Input: "Rooms, bookings with start/end, attendees, no overlapping bookings per room. Engine: PostgreSQL."

Excerpt of output:
- `booking(id uuid PK, room_id FK → room ON DELETE RESTRICT, period tstzrange NOT NULL, organizer_id FK, version int NOT NULL DEFAULT 0)`
- Invariant enforced: `EXCLUDE USING gist (room_id WITH =, period WITH &&)` `[ENGINE-SPECIFIC]`; portable fallback: serialize inserts per room with `SELECT ... FOR UPDATE` on the room row.
- Index: `booking(room_id, lower(period))` for "room calendar for a day".
- Open question: Are cancelled bookings kept? If yes, the exclusion must ignore them `[TBD]`.
