---
description: "Specifies a batch or streaming data pipeline end to end: sources and extraction, schedule or trigger, dependencies, transformation steps, targets and write mode, load strategy, data quality gates, SLAs, failure handling, backfill, observability, security and ownership. Use before building or changing a pipeline, when handing pipeline work to an engineer, or when someone asks to design or document an ETL/ELT or streaming job."
related: "source-to-target-mapping, incremental-load-design, data-quality-rules, data-contract, runbook"
prompt: "Write a pipeline spec for loading daily orders from the ERP database into the warehouse for the finance mart."
---

# Specify a Data Pipeline

## Purpose
Give implementers and operators one unambiguous description of what a pipeline moves, when, how, with what guarantees and what happens when it fails, so it can be built, reviewed, operated and changed safely.

## When to use
- A new ingestion or transformation pipeline is about to be built.
- An existing pipeline is undocumented and keeps surprising its operators.
- A pipeline is handed over between teams or to a vendor.

## When not to use
- Only the column-level transformation logic is needed. Use `source-to-target-mapping`.
- Only the change-capture and watermark design is in question. Use `incremental-load-design`.
- The CI/CD pipeline for application code is meant. Use `pipeline-design`.

## Inputs
Required:
- Source(s), target(s) and the consumer need the pipeline serves (what data, for whom, by when).

Optional:
- Volumes and growth, source constraints (maintenance windows, load limits), existing platform and orchestration conventions, mappings, quality expectations, sensitivity classification.

If the consumer need or the freshness requirement is unknown, ask; batch vs. streaming and the SLA depend on it.

## Process
1. State the purpose and consumers, and derive the freshness requirement and completeness deadline from the consumer need, not from what is convenient.
2. Describe each source: system, objects, access method (query, CDC log, API, file, event topic), volume per run, change pattern, source-side constraints and the owning team.
3. Choose processing mode (batch, micro-batch, streaming) and trigger (time schedule, upstream completion, file arrival, event), and list upstream and downstream dependencies explicitly.
4. Describe transformations as ordered steps (clean, conform, deduplicate, join, aggregate, enrich), referencing a mapping document for column-level logic.
5. Define targets: object, layer, partitioning, write mode (append, merge/upsert, overwrite partition, SCD handling) and the idempotency guarantee on rerun.
6. Define load strategy: full vs. incremental, change detection, late and out-of-order data handling, deletes propagation.
7. Place data quality gates: which checks run where and whether a failure blocks, quarantines or warns.
8. Define failure handling: retry policy with backoff, which errors are retryable, partial-failure behavior, dead-letter or quarantine, alerting route and escalation.
9. Define backfill and reprocessing: how to rerun a date range safely, expected duration, impact on source and consumers.
10. Define observability: run metadata, row counts in/out/rejected, lag, duration, cost indicators, and dashboards or alerts on SLA breach.
11. Define security and compliance: credentials handled via a secret store, least-privilege access, personal data masking or minimization, encryption and data residency where relevant.
12. Record ownership, on-call, runbook link and open questions; mark unconfirmed values `[TBD]` or `[ASSUMPTION]`. If the goal continues, suggest `source-to-target-mapping`, `incremental-load-design` or `runbook`.

## Output format
```markdown
# Pipeline Spec: <name>
Owner: <team> | On-call: <...> | Status: <draft/approved> | Version: <...>

## Purpose and Consumers
<what, for whom> | Freshness: <...> | Complete by: <...>

## Sources
| Source | Objects | Access | Volume/run | Change pattern | Constraints | Owner |
|---|---|---|---|---|---|---|

## Trigger and Dependencies
Mode: <batch/streaming> | Trigger: <...> | Upstream: <...> | Downstream: <...>

## Transformations
1. <step> — see mapping <ref>

## Targets
| Target | Layer | Partitioning | Write mode | Idempotency |
|---|---|---|---|---|

## Load Strategy
<full/incremental, change detection, late data, deletes>

## Quality Gates
| Check | Stage | On failure |
|---|---|---|

## Failure Handling and Backfill
<retries, quarantine, alerting, rerun procedure>

## Observability
<metrics, alerts, dashboards>

## Security and Compliance
<secrets, access, masking, residency>

## Open Questions
- [TBD] ...
```

## Quality checklist
- [ ] Freshness and completeness deadlines trace to a consumer need.
- [ ] Rerunning any run or date range produces the same target state (idempotent).
- [ ] Late data, deletes and schema changes have a defined behavior.
- [ ] Every quality gate has an on-failure action; alerts have a route.
- [ ] No credentials in the spec; personal data handling is stated.
- [ ] Unknown volumes and SLAs are `[TBD]`, not invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Specifying the happy path only. Most operational cost lives in retries, partial loads and backfills.
- Append-only writes without deduplication: every retry creates duplicates.
- Scheduling by wall clock when the real dependency is "upstream finished". Use completion triggers or sensors.

## Example
Input: "Daily ERP orders into the warehouse for the finance mart, needed by 06:00."

Excerpt of output:
- Trigger: after ERP nightly close signal, not a fixed 02:00 time; complete by 06:00 local.
- Write mode: merge on (order_id) into fact partitioned by order_date; rerun of a day overwrites that day's partitions only.
- Quality gate: row count vs. ERP control total per day, Critical, blocks mart refresh and pages on-call.
