---
description: "Designs a database backup and restore plan derived from RPO and RTO: backup types and frequency (full, differential/incremental, log or continuous archiving, snapshots), retention and immutable/off-site copies, encryption and access, restore procedures for each failure scenario, and a scheduled restore-test program with evidence. Use when setting up or reviewing backups for a database, after a failed or slow restore, for audit evidence, or when RPO/RTO targets change."
related: "dr-plan, retention-policy, database-health-check, schema-migration-plan, runbook"
prompt: "Design a backup and restore plan for our 2 TB order database: RPO 15 minutes, RTO 2 hours, we must also keep monthly backups for 1 year for audit."
---

# Plan Backup and Restore

## Purpose
Guarantee that data can be restored to the required point within the required time, for every realistic failure. A backup plan is judged by tested restores, not by successful backup jobs.

## When to use
- A new database goes to production or an existing one has no documented backup design.
- RPO/RTO targets are set or changed, or a restore failed or took longer than expected.
- Auditors or security require evidence of backup coverage, immutability and restore tests.

## When not to use
- Full site or region failover of the whole service is being designed. Use `dr-plan`; this skill covers the database piece.
- The question is how long business data may be kept or must be deleted. Use `retention-policy`.
- A step-by-step operational procedure for a single restore is needed. Use `runbook` with this plan as input.

## Inputs
Required:
- The database engine, deployment model (self-managed, managed service, container) and size/growth.
- RPO and RTO targets, or the business owner who can set them.

Optional:
- Change rate and log volume, existing backup tooling, storage targets, legal retention requirements, encryption/key management, replication topology, budget constraints.

If RPO/RTO are unknown, do not invent them; propose candidate tiers marked `[ASSUMPTION]` and list the decision owner as an open question.

## Process
1. Record the targets and scope: databases, RPO, RTO, required restore granularity (whole instance, single database, table, row-level via point-in-time), and data classification. Label inferred values `[ASSUMPTION]`.
2. List failure scenarios to cover: hardware/storage loss, logical corruption or bad deploy, accidental delete/update, ransomware or malicious admin, region/site loss, silent corruption discovered late.
3. Choose backup methods that meet RPO: full + differential/incremental cadence, transaction log or WAL/binlog archiving frequency (continuous for minute-level RPO), storage snapshots (with application consistency), managed point-in-time recovery. Note that replicas are not backups.
4. Check RTO feasibility: estimate restore time as base restore + log replay + verification + application reconnect, using measured throughput where available; if the estimate exceeds RTO, change the design (more frequent full/diff, snapshots, warm standby).
5. Define retention tiers and copies: operational (short, fast), long-term (audit), at least one copy off-site/other account or region, and one immutable or logically air-gapped copy (3-2-1-1-0 as a heuristic).
6. Secure the backups: encryption at rest and in transit, key management separate from the backup storage, least-privilege access, deletion protection, and alerting on backup deletion or policy changes. Backups containing personal data follow the same privacy and retention rules as the source.
7. Define monitoring: job success, duration trend, size anomalies (sudden drop or growth), log archive gaps, age of latest restorable point versus RPO.
8. Write restore procedures per scenario: point-in-time restore to a side instance for logical errors, full restore for loss, partial extraction for single-table recovery; include who decides and who executes.
9. Define the restore-test program: frequency per tier, randomized selection, full restore to isolated environment, integrity checks (engine consistency check, row counts, application smoke test), measured duration against RTO, and recorded evidence.
10. List gaps, risks, assumptions and cost drivers (storage, egress, standby). If the goal continues, suggest `dr-plan` for the wider service recovery, `runbook` for executable restore steps or `retention-policy` for legal retention alignment.

## Output format
```markdown
# Backup and Restore Plan: <database/system>
Engine / model: <...> | Size / growth: <...> | RPO: <...> | RTO: <...> | Classification: <...>

## Failure Scenarios
| Scenario | Recovery method | Achievable RPO / RTO | Gap |
|---|---|---|---|

## Backup Schedule
| Type | Frequency | Window | Target storage | Retention | Immutable / off-site |
|---|---|---|---|---|---|

## Security
Encryption: <...> | Keys: <...> | Access: <...> | Deletion protection: <...>

## Monitoring and Alerts
- <check> – threshold – recipient

## Restore Procedures
| Scenario | Steps (summary) | Decision owner | Executor | Est. duration |
|---|---|---|---|---|

## Restore Testing
Frequency: <...> | Scope: <...> | Checks: <...> | Evidence: <where recorded>

## Gaps, Risks, Assumptions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every listed failure scenario has a recovery method whose RPO/RTO is compared with the target.
- [ ] RTO feasibility is estimated from restore plus replay plus verification, not from backup duration.
- [ ] At least one off-site and one immutable or air-gapped copy exist, with separated keys and access.
- [ ] Replication is not counted as a backup.
- [ ] Restore tests are scheduled, measured against RTO and produce evidence.
- [ ] RPO/RTO or durations not given by the user are labeled; nothing is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Monitoring backup job success but never restoring: corrupt, incomplete or unencryptable-without-key backups surface only during an incident.
- Relying on replicas or snapshots in the same account: a bad delete replicates instantly, and a compromised admin deletes both.
- Keeping backups longer than the source data retention allows, turning backups into a privacy liability.

## Example
Input: "2 TB order database, RPO 15 min, RTO 2 h, monthly backups kept 1 year for audit."

Excerpt of output:
- Backups: weekly full, daily differential, log archiving every 5 min to a separate account; monthly full copied to immutable storage for 12 months.
- RTO check: full restore ~70 min + differential ~15 min + log replay up to 24 h of changes ~30 min `[ASSUMPTION: measure throughput in first restore test]` → 1 h 55 min, too close to 2 h; add daily differentials at 12-hour intervals or a warm standby.
- Restore test: monthly random-point restore to isolated environment, consistency check plus order count reconciliation, duration recorded against RTO.
