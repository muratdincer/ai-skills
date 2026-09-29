---
description: "Runs a structured health check of a database instance from the metrics, views and settings the user provides: wait profile, top resource-consuming queries, locking and blocking, storage growth and bloat/fragmentation, index and statistics health, configuration, replication, backups and security basics, then prioritizes findings with evidence and fixes. Use for periodic database reviews, before peak season or a migration, when a database feels slow overall, or when taking over an unfamiliar database."
related: "query-optimization, index-recommendation, backup-restore-plan, capacity-planning, alert-design"
prompt: "Do a health check of our production SQL database. I pasted the top waits, the top 10 queries by CPU, file sizes and the configuration settings."
---

# Run a Database Health Check

## Purpose
Give a clear, evidence-based picture of a database instance's health and a prioritized list of fixes, so the team acts on the few issues that matter instead of a long list of generic best practices.

## When to use
- A periodic (e.g. quarterly) review of a production database.
- Before a peak season, a major release, a migration or a hardware/tier change.
- The database is slow in general and the culprit is not known, or a team takes over an unfamiliar database.

## When not to use
- One known query is slow. Use `query-optimization`.
- The goal is future sizing and growth forecasting. Use `capacity-planning`.
- Only the backup and recovery design is in question. Use `backup-restore-plan`.

## Inputs
Required:
- The database engine and deployment model.
- At least one evidence set: wait statistics or equivalent, top queries by resource, or resource metrics (CPU, memory, IO, storage) over a representative period.

Optional:
- Configuration settings, storage/file sizes and growth history, index and statistics metadata, blocking/deadlock history, replication status, backup history, user and permission list, error log excerpts, hardware/tier specs.

If no evidence is provided, give the user a short, engine-appropriate list of what to collect (maximum 5 items) instead of guessing. Mark areas not covered by evidence as `[NOT ASSESSED]`.

## Process
1. Record context: engine, version family, deployment model, workload type (OLTP, reporting, mixed), size, business criticality, the period the evidence covers. Label inferences `[ASSUMPTION]`.
2. Analyze the wait profile: dominant wait classes (CPU, IO, locks, memory grants, log writes, network/client, parallelism) and what each implies; ignore benign idle waits.
3. Review top queries by total CPU, reads and duration: flag a handful that dominate cost, plan regressions, high execution counts with small cost (chatty application) and missing parameterization.
4. Check concurrency: blocking chains, long-running and idle-in-transaction sessions, deadlock frequency and patterns, isolation level choices.
5. Check storage: data and log growth rate, free space, autogrowth settings, table/index bloat or fragmentation where it actually affects scans, temp space usage, log reuse blockers.
6. Check indexes and statistics: unused and duplicate indexes, missing index signals, statistics staleness on large or fast-changing tables, maintenance job results.
7. Check configuration against workload: memory allocation, parallelism thresholds, connection limits and pooling, checkpoint/log settings, relevant engine-specific options; flag defaults unsuitable for the workload, not deviations from folklore.
8. Check resilience and hygiene: replication/HA lag and health, last successful backup and last restore test, consistency check results, error log issues, patch level recency, excess privileges and shared admin accounts (no credentials copied into the report).
9. Rate each finding by severity (Critical: risk of outage or data loss; High: user-visible performance or near-term capacity; Medium; Low) with evidence and a concrete fix, effort and owner if known.
10. Summarize the overall health status and top 3 actions. If the goal continues, suggest `query-optimization` for dominant queries, `index-recommendation` for index findings, `backup-restore-plan` for recovery gaps or `alert-design` to monitor the found risks.

## Output format
```markdown
# Database Health Check: <instance> – <date>
Engine / model: <...> | Workload: <...> | Evidence period: <...> | Overall: <Healthy / At risk / Critical>

## Top 3 Actions
1. ...

## Findings
| # | Area | Finding | Evidence | Severity | Fix | Effort |
|---|---|---|---|---|---|---|

## Area Summary
| Area | Status | Notes |
|---|---|---|
| Waits | | |
| Top queries | | |
| Concurrency | | |
| Storage | | |
| Indexes / statistics | | |
| Configuration | | |
| HA / backups / integrity | | |
| Security basics | | |

## Not Assessed / Data to Collect
- ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every finding cites specific evidence from the inputs; generic best practices without evidence are excluded.
- [ ] Areas without evidence are marked `[NOT ASSESSED]` rather than rated healthy.
- [ ] Severity reflects outage/data-loss risk first, then user-visible impact.
- [ ] Each finding has a concrete fix and, where risky, a note on how to apply it safely.
- [ ] No credentials, connection strings or personal data appear in the report.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reporting fragmentation percentages as the headline while the real issue is a missing backup test or a blocking chain.
- Tuning configuration from generic rules of thumb instead of the observed wait profile and workload.
- Treating a single snapshot as representative; peak hours, batch windows and month end often tell a different story.

## Example
Input: "OLTP DB, waits: 45% lock waits, 25% log write; top query runs 1.2M times/h; log file 180 GB, 5% used; last restore test unknown."

Excerpt of output:
- Overall: At risk.
- Finding 1 (High): lock waits dominate; blocking chains headed by a batch update that holds locks for minutes `[ASSUMPTION: confirm with blocking history]`. Fix: batch the update and shorten transactions.
- Finding 2 (Critical): no evidence of restore testing; recovery capability unknown. Fix: restore test within 2 weeks, then quarterly.
- Finding 3 (Medium): 1.2M executions/h of a single-row lookup suggests N+1 access from the application; fix in code or cache.
