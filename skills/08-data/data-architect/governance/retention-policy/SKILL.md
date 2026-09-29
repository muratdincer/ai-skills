---
description: "Defines a data retention policy for datasets or systems: retention periods with their legal or business basis, trigger events, archival tiers, deletion or anonymization methods, legal holds, backup handling and evidence of deletion. Use when data is kept indefinitely by default, a privacy law such as KVKK or GDPR requires storage limitation, storage costs grow, or someone asks how long data may or must be kept."
related: "data-classification, privacy-impact-assessment, backup-restore-plan, policy-writing, data-catalog-entry"
prompt: "Define a retention policy for our customer, order and application log data under KVKK and GDPR."
---

# Define Data Retention

## Purpose
Decide for each category of data how long it is kept, why, where it lives over time and how it is disposed of, so the organization meets legal minimums and maximums, limits breach exposure and controls storage cost.

## When to use
- Data is kept "forever" because nobody decided otherwise.
- A privacy review, audit or regulator asks for storage limitation and deletion evidence.
- A new system or data product is designed and its lifecycle must be defined.
- Storage or backup costs grow with no archival or purge rules.

## When not to use
- The sensitivity of the data is not yet known. Use `data-classification` first.
- A full privacy risk assessment of a processing activity is needed. Use `privacy-impact-assessment`.
- Backup frequency and restore procedures are the topic. Use `backup-restore-plan`.

## Inputs
Required:
- The data categories or datasets in scope and their business purpose.

Optional:
- Classification, applicable jurisdictions and sector regulation, existing policies, contractual obligations, storage locations including backups and replicas, legal hold process.

If the purposes are unknown, ask: retention is justified by purpose. Never state a specific legal retention period as fact unless the user or their legal counsel provided it; otherwise mark it `[TO CONFIRM WITH LEGAL]`.

## Process
1. List data categories at a useful granularity (e.g. customer master, orders and invoices, support tickets, application logs, marketing consents, CCTV) with purpose and classification.
2. For each category, identify the retention drivers: legal minimum (tax, commercial, sector law), legal maximum or storage-limitation principle (KVKK/GDPR), contractual, operational and analytical need. Record the source of each driver.
3. Define the trigger event that starts the clock (end of contract, last activity, transaction date, account closure), not merely "creation date".
4. Set the retention period as the longest justified minimum and no longer than purpose allows; where drivers conflict, split the data (e.g. keep invoice fields, anonymize behavioral fields).
5. Define lifecycle tiers: active (online), restricted/archived (access limited to named roles and purposes), disposed. State access rules for each tier.
6. Define disposal method per category: hard delete, crypto-shredding, irreversible anonymization (not pseudonymization) or aggregation. Explain how derived copies (warehouse, extracts, caches, test environments) are covered.
7. Address backups and replicas: backups expire by their own cycle rather than being edited, and restored data must re-apply deletions made since the backup.
8. Define legal hold: who can place and lift it, how it suspends disposal, and how it is recorded.
9. Define execution and evidence: automated purge jobs or manual procedure, frequency, deletion logs with counts, exception handling, and periodic review of the policy.
10. Assign ownership per category (data owner approves, technical owner executes) and list assumptions and open questions. If the goal continues, suggest `policy-writing` to formalize it, `backup-restore-plan` to align backup expiry, or `data-catalog-entry` to publish retention on each dataset.

## Output format
```markdown
# Data Retention Policy: <scope>
Jurisdictions: <...> | Owner: <...> | Review cycle: <...>

## Retention Schedule
| Category | Purpose | Class | Driver(s) and source | Trigger event | Active | Archive | Total | Disposal method | Owner |
|---|---|---|---|---|---|---|---|---|---|

## Derived Copies and Backups
- <warehouse, extracts, test data, backups: how retention applies>

## Legal Hold
- <authority, process, record>

## Execution and Evidence
- <jobs/procedures, frequency, deletion log, exceptions>

## Assumptions and Open Questions
- [TO CONFIRM WITH LEGAL] ...
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Every period cites a driver and its source; no legal period is invented.
- [ ] Every category has a trigger event, not only a duration.
- [ ] Disposal method is defined and anonymization is truly irreversible.
- [ ] Derived copies, test environments and backups are covered.
- [ ] Legal hold can suspend disposal and is auditable.
- [ ] Personal data is kept no longer than its purpose requires.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- One retention period for a whole system. Different fields often have different drivers; split by category or field group.
- Deleting from production but not from the warehouse, logs, extracts and test copies.
- Calling pseudonymized data anonymous. If it can be re-identified with other data held, it is still personal data.

## Example
Input: "Customer, order and application log data; we operate under KVKK and GDPR."

Excerpt of output:
- Orders and invoices: driver tax/commercial record keeping `[TO CONFIRM WITH LEGAL: period]`; trigger end of fiscal year of the transaction; archive after 2 years `[ASSUMPTION]`; then hard delete.
- Application logs: operational need only; 90 days active `[ASSUMPTION]`; IP and user ID masked at ingestion; purge job daily with count logged.
- Marketing consent records: kept for as long as consent is used plus proof period `[TO CONFIRM WITH LEGAL]`.
