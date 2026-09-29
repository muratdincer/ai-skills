---
description: Builds a project communication plan that specifies, for each audience, what information they receive, when and how often, through which channel, from whom, and how feedback and escalations flow back. Use at project start, when stakeholders complain about being uninformed or overloaded, or when governance and reporting cadences must be agreed.
related: stakeholder-register, project-status-report, governance-framework, status-update, announcement
prompt: Create a communication plan for our core banking upgrade covering executives, branch staff, IT operations and the vendor.
---

# Build a Communication Plan

## Purpose
Ensure every stakeholder group gets the right information at the right level of detail and frequency, with clear senders and feedback paths, so that surprises and noise are both minimized.

## When to use
- At initiation, after the stakeholder register is drafted.
- When complaints arise about missing information or too many messages.
- Before critical phases (cutover, go-live, decommissioning) that need tighter communication.

## When not to use
- Writing a single message or update. Use `status-update` or `stakeholder-email`.
- Defining decision rights and forums. Use `governance-framework`.
- Change-management communication for an org restructuring. Use `org-change-communication`.

## Inputs
Required:
- Stakeholder list or register with their interests.
- Project governance basics (sponsor, steering body, PM).

Optional, improves quality:
- Existing corporate channels and tools, language needs, time zones.
- Milestones and sensitive events (cutover, layoffs, vendor changes).

If there is no stakeholder list, ask for it or run a quick identification first.

## Process
1. Group audiences with similar needs; keep decision makers individual.
2. For each audience define the information need: decisions, progress, impact on them, actions required.
3. Choose format and level of detail (dashboard, one-page report, briefing, demo, newsletter).
4. Set frequency and timing tied to decision cycles (e.g. status before steering meeting).
5. Select channel (meeting, email, intranet, chat channel, portal) considering reach and confidentiality.
6. Assign a sender/owner per communication and a backup.
7. Define feedback and escalation paths: how audiences ask questions or raise concerns, and response time.
8. Add event-driven communications: go-live, incidents, delays, scope changes, with approval rules for sensitive messages.
9. Define how effectiveness is checked (attendance, read rates, pulse questions, stakeholder feedback) and the plan review cadence.

## Output format
```markdown
# Communication Plan: <project>
## Communication Matrix
| Audience | Information need | Format | Frequency / timing | Channel | Owner (backup) | Feedback path |
## Event-Driven Communications
| Trigger | Audience | Message owner | Approver | Lead time |
## Escalation Path
## Effectiveness Measures
## Calendar (first 3 months)
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every high-influence stakeholder appears in the matrix.
- [ ] Each communication has an owner and a clear purpose.
- [ ] Timing is linked to decision points, not arbitrary.
- [ ] Sensitive communications have an approver.
- [ ] Feedback paths exist, not only outbound messages.

## Common pitfalls
- One status report for everybody. Tailor depth: executives need decisions and risks, teams need detail.
- Planning too many recurring meetings. Prefer asynchronous updates where no discussion is needed.
- Forgetting indirect audiences like service desk and operations before go-live.

## Example
Input: "Core banking upgrade; executives, branch staff, IT ops, vendor."

Excerpt of output:
| Branch staff | What changes for them, when, training | 1-page bulletin + short video | Bi-weekly; weekly from T-4 weeks | Intranet + branch manager briefing | Change lead (PM) | Questions via branch managers, 2-day answer |
