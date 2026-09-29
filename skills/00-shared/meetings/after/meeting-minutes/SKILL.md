---
description: Produces formal meeting minutes with meeting metadata, attendance and quorum, agenda items in order, concise discussion records, numbered resolutions with voting or approval outcome, actions and approval signatures. Use for steering committees, boards, change advisory boards, audits, contractual or vendor meetings, or whenever the record may be relied on as evidence.
related: meeting-notes, meeting-summary, decision-log, steering-committee-pack, audit-preparation
prompt: Write formal minutes for yesterday's project steering committee from these notes; two change requests were approved and one deferred.
---

# Write Formal Meeting Minutes

## Purpose
Create an accurate, neutral and approvable record of a formal meeting that shows who attended, what was considered and what was resolved, so it can serve as governance or contractual evidence.

## When to use
- Steering committee, board, change advisory board, vendor or contract governance meetings.
- Meetings whose outcomes must be auditable (compliance, budget approval, acceptance).
- The organization or contract requires signed or approved minutes.

## When not to use
- An internal working session where a readable record is enough. Use `meeting-notes`.
- A short outcome recap for leaders. Use `meeting-summary`.

## Inputs
Required:
- Notes, transcript or recording summary of the meeting.
- Meeting type and date.

Optional:
- Attendance list with roles, quorum rule, agenda, previous minutes, organization minute template, numbering scheme for resolutions.

If attendance or quorum rules are missing, record them as `[UNKNOWN]` and list them as items to confirm before circulation.

## Process
1. Fill the header: body/meeting name, meeting number, date, start and end time, location/medium, chair, secretary.
2. Record attendance in three groups: present (with role), apologies/absent, guests/in attendance for specific items. Note quorum status if a rule exists.
3. Record the approval of previous minutes and status of matters arising, if on the agenda.
4. Follow the agenda order. For each item: presenter, papers considered, a neutral 2-5 line summary of discussion, and the outcome.
5. Phrase outcomes formally and unambiguously: "The committee approved...", "The committee deferred... pending...", "The committee noted...". Record votes or dissent where applicable.
6. Number resolutions (e.g. SC-2026-07/R1) so they can be referenced later.
7. Record declared conflicts of interest and any members who left for an item.
8. List actions with owner and due date; tie each to its agenda item.
9. Keep the tone third-person and neutral; no opinions, adjectives or verbatim arguments unless the body requires them.
10. Add the next meeting date and the approval block (chair signature/approval date).
11. List items to confirm before circulation (spelling of names, figures, resolution wording).

## Output format
```markdown
# Minutes – <body/meeting name> No. <n>
Date: <date>  Time: <start–end>  Location: <place/online>
Chair: <name>  Secretary: <name>
Present: <name – role>; ...
Apologies: <...>   In attendance: <name – item>
Quorum: <met / not met / [UNKNOWN]>

## 1. Previous minutes and matters arising
<approved as circulated / with amendments>

## 2. <Agenda item>
Presented by: <name>. Papers: <ref>.
Discussion: <neutral summary>
Resolution <ID>: The <body> <approved/rejected/deferred/noted> <...>. <Vote/dissent if any>

## Actions
| # | Action | Owner | Due | Item |
## Next meeting: <date or [TBD]>
Approved by chair: ____________  Date: ______
## To confirm before circulation
- ...
```

## Quality checklist
- [ ] Attendance, apologies and quorum are recorded or flagged.
- [ ] Every agenda item has an explicit outcome (approved, rejected, deferred, noted).
- [ ] Resolutions are numbered and wording is unambiguous.
- [ ] Tone is neutral and third-person; no personal opinions.
- [ ] Figures, dates and names match the source; gaps are marked `[UNKNOWN]`.
- [ ] Next meeting and approval block are present.

## Common pitfalls
- Writing a transcript. Minutes record what was decided and the essential reasoning, not every argument.
- Vague outcomes like "discussed further". Every item needs a formal status.
- Circulating without chair approval; errors then become the official record. Include the confirmation list.

## Example
Input: Notes of steering committee: CR-14 and CR-15 approved, CR-16 deferred until cost estimate.

Excerpt of output:
Resolution SC-07/R2: The committee approved CR-15 (SSO integration), with budget impact to be absorbed within the existing contingency.
Resolution SC-07/R3: The committee deferred CR-16 pending a cost estimate from the vendor. `[due date UNKNOWN]`
