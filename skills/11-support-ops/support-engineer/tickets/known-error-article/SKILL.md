---
description: "Writes a known error article for the support knowledge base: searchable symptom, scope and affected versions, confirmed or suspected cause, step-by-step workaround with risks, permanent fix status and linked records. Use when a problem has a documented root cause or workaround, when the same ticket keeps recurring, or when support agents need a consistent answer to give while a fix is pending."
related: "problem-management, ticket-response, ticket-triage, how-to-guide, faq-builder"
prompt: "Write a known error article: PDF export fails with 'Error 500' for reports over 10,000 rows since version 7.3; workaround is exporting to CSV; fix planned for 7.4."
---

# Write a Known Error Article

## Purpose
Let any agent or user recognize a known issue from its symptom in seconds and apply a safe workaround, so recurring tickets are resolved at first contact and the fix status is communicated consistently.

## When to use
- Problem management has confirmed a root cause or a workaround.
- The same symptom has appeared in several tickets and agents answer it differently.
- A defect is accepted but the permanent fix will take one or more releases.

## When not to use
- The cause is still under investigation across incidents. Use `problem-management` first.
- The content is a general task guide, not an error. Use `how-to-guide`.
- A live outage affecting customers now needs notice. Use `customer-outage-notice`.

## Inputs
Required:
- The symptom (error text or observed behavior) and the workaround or cause known so far.

Optional, improves quality:
- Affected products, versions, platforms, configurations; linked problem, defect and change IDs.
- Fix status and target release, if committed.
- Audience (internal agents only or customer-facing) and the knowledge base template.

If neither a cause nor a workaround is known, say that the article is premature and suggest `problem-management`. Never publish an internal-only detail (server names, internal URLs, security weaknesses) in a customer-facing article.

## Process
1. Decide the audience: internal (may include diagnostics, admin steps) or external (only safe, user-executable steps). If both are needed, produce two variants from the same facts.
2. Write the title as the symptom the user sees, with the exact error text, not the internal cause ("PDF export fails with Error 500 on large reports", not "Renderer heap limit").
3. Add search keywords: error codes, message fragments, product area names and common user phrasings.
4. Define scope precisely: affected versions, platforms, configurations, and conditions that trigger it (thresholds, data types). State what is NOT affected to prevent false matches.
5. Describe the cause at the confirmed level only. Label unconfirmed explanations `[ASSUMPTION]`, and leave out security-sensitive details for external audiences.
6. Write the workaround as numbered, testable steps with the expected result, side effects, data risks and who may perform it (user, admin, support only).
7. Add a quick diagnostic: how an agent confirms that a ticket matches this known error before applying the workaround.
8. State the permanent fix status (investigating, fix planned, fixed in version X, will not fix with reason) and the target only if committed; otherwise `[TBD]`.
9. Link records: problem ID, defect ID, change ID, related incidents; set an owner and a review date so the article is retired when the fix ships.
10. Hand off: suggest `ticket-response` to answer matching tickets using the article, or `problem-management` to update the problem record with the known error status.

## Output format
```markdown
# Known Error: <symptom as the user sees it>
| Field | Value |
|---|---|
| KE ID / Problem ID | <...> / <...> |
| Audience | internal / external |
| Affected | <product, versions, platforms, conditions> |
| Not affected | <...> |
| Status | investigating / fix planned (<release or TBD>) / fixed in <version> / won't fix |
| Owner / Review date | <...> / <date> |
| Keywords | <error codes, phrases> |

## Symptom
<exact message and behavior>
## How to Confirm
1. ...
## Cause
<confirmed cause, or [ASSUMPTION] ...>
## Workaround
1. <step> – expected result: ...
- Side effects / risks: ...
- Who can perform: ...
## Permanent Fix
<status, target, how customers will be informed>
## Related Records
- ...
```

## Quality checklist
- [ ] The title and keywords match the words and error text users actually report.
- [ ] Scope states both affected and not-affected conditions.
- [ ] Every workaround step is testable and lists its risks and required role.
- [ ] Fix dates appear only when committed; otherwise `[TBD]`.
- [ ] External variants contain no internal hostnames, credentials or exploitable security detail.
- [ ] The article has an owner, linked records and a review or retirement date.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Titling by internal cause, so agents searching by symptom never find it. Lead with the symptom.
- Workarounds that silently lose data or bypass controls. State side effects and restrict risky steps to admins.
- Leaving the article live after the fix ships, sending users down an obsolete path. Set a review date and retire it.
- Promising a fix version that is not committed; it becomes a customer commitment.

## Example
Input: "PDF export fails with 'Error 500' for reports over 10,000 rows since 7.3; workaround CSV; fix planned for 7.4."

Weak title: "Renderer memory issue."
Strong excerpt:
- Title: "PDF export fails with 'Error 500' for reports over 10,000 rows"
- Affected: version 7.3, all browsers, reports above ~10,000 rows [ASSUMPTION: exact threshold to confirm]. Not affected: CSV and Excel exports; reports under the threshold.
- Workaround: 1. Choose Export > CSV. 2. Open in a spreadsheet tool. Expected: all rows present. Risk: CSV loses formatting and charts.
- Status: fix planned for 7.4 [confirm with release owner before publishing externally].
