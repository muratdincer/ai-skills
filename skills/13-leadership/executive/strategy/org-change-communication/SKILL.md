---
description: Plans and writes the communication of an organizational change (reorganization, new teams, reporting line changes, role changes, office or process changes): why, what changes, what does not, who is affected, timeline, support and where to ask, sequenced so affected people hear first and privately. Use when a leader announces a reorg or team change, when rumors must be addressed, or when a change needs a message set for different audiences.
related: team-topology, announcement, bad-news-delivery, faq-builder, communication-plan
prompt: We are merging the mobile and web teams into product-aligned teams next month; write the announcement and a plan for who hears what, when.
---

# Communicate an Org Change

## Purpose
Help people understand an organizational change, how it affects them and where to get support, so that trust is kept, rumors are pre-empted and the change starts working rather than being resisted.

## When to use
- A reorganization, team merger or split, new reporting lines or role changes are about to be announced.
- A change leaked or rumors spread, and a clear message is needed quickly.
- Different audiences (affected individuals, their managers, the wider department, partners) need tailored messages.

## When not to use
- Designing the new team structure itself. Use `team-topology` or `role-definition`.
- Telling an individual about a negative decision (role elimination, performance outcome). Use `bad-news-delivery`.
- A product or release announcement. Use `announcement`.

## Inputs
Required:
- What is changing, why, and the effective date (or that it is not decided yet).

Optional, improves quality:
- Who is affected and how (by group, not by name unless needed for private conversations).
- What is not changing (pay, location, projects, tools), decisions still open, and the support offered.
- Legal, HR or works-council constraints and required consultation steps.

If the reason for the change is missing, ask; a change without a stated why reads as arbitrary. Do not invent reasons, dates or guarantees (e.g. "no one will lose their job"); only state what the user confirms, and mark the rest `[TBD]`.

## Process
1. Clarify the change: before and after structure, reason (the problem it solves), effective date, decision status (final or consultation) and what remains open.
2. Map audiences by impact: directly affected (role, manager or team changes), indirectly affected (interfaces, stakeholders), and informed only; keep individual details private and minimize personal data.
3. Sequence communication: affected individuals first in private conversations with their manager, then managers briefed with talking points, then the wider announcement, then partners; keep the gap between steps short (hours, not weeks) to avoid leaks.
4. Check fairness and consistency: the same criteria were applied to everyone affected; flag any change that disproportionately affects a group (e.g. by location, part-time status, leave) for HR review, and avoid language that singles out individuals.
5. Draft the core message: why, what changes, what does not change, who is affected, when, what happens next, where to ask; lead with the why and the impact on people, not with the org chart.
6. Be explicit about uncertainty: say what is not decided yet and when it will be; never promise what is not confirmed.
7. Write a manager briefing: key messages, likely questions with answers, what not to speculate on, escalation path.
8. Build an FAQ from likely questions: my role, my manager, my projects, pay and title, location, career paths, timeline, how to raise concerns.
9. Define feedback and support channels (office hours, skip-level sessions, anonymous questions) and a follow-up date.
10. Review tone: respectful, direct, no corporate euphemisms, no blame on people or previous leaders.
11. If the user's goal continues, suggest `faq-builder` to expand the FAQ, `communication-plan` for a longer change program, or `bad-news-delivery` for difficult individual conversations.

## Output format
```markdown
# Org Change Communication: <change>

## Sequence
| Step | Audience | Channel | Owner (role) | When |
|---|---|---|---|---|

## Core Announcement
Subject: <clear subject>
- Why: ...
- What changes: ...
- What does not change: ...
- Who is affected: ...
- Timeline: ...
- Not yet decided: ... (decision expected <date or [TBD]>)
- Support and questions: ...

## Manager Briefing
- Key messages: ...
- Likely questions and answers: ...
- Do not speculate on: ...

## FAQ
1. <question> – <answer or [TBD]>

## Fairness and Risk Notes (internal)
- ...
```

## Quality checklist
- [ ] Directly affected people hear before the wider announcement, in private.
- [ ] The message states why, what changes, what does not change, timeline and where to ask.
- [ ] Nothing is promised or stated as fact that the user has not confirmed; open items are `[TBD]`.
- [ ] Criteria are applied consistently; disproportionate impacts on any group are flagged for HR review.
- [ ] No names or personal details appear in broad communications.
- [ ] Tone is direct and respectful, without euphemism or blame.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Announcing to everyone at once. People affected in their role should never learn it from an all-hands slide.
- Only describing the new org chart. People first want to know what happens to them; answer that before structure.
- Over-reassuring. "Nothing changes for you" that later proves false costs more trust than an honest "not decided yet".

## Example
Input: Mobile and web teams merge into product-aligned teams next month.

Excerpt of output:
- Why: Features that span web and mobile need two teams and two backlogs today, which slows delivery `[confirm with evidence, e.g. lead time]`.
- Weak line (avoid): "We are excited to announce a new structure to unlock synergies." Strong line: "From <date>, each product area has one team owning web and mobile. Your manager will talk to you this week about your team; pay and titles do not change."
- Not yet decided: tech lead assignments for two teams – decision by `[TBD]`.
