---
description: Writes an escalation that states the issue, verified facts, business impact and deadline, what has already been tried, the options with trade-offs, a recommendation and one clear ask of the escalation owner. Use when a blocker, dependency, conflict or risk cannot be resolved at the current level and needs a decision, resources or intervention from a manager, sponsor, vendor account lead or another team's leadership.
related: stakeholder-email, status-update, raid-log, trade-off-analysis, conflict-resolution
prompt: Escalate to my director that the identity team has not delivered the SSO integration for three weeks and our pilot on the 15th will slip if it does not land by the 8th.
---

# Write an Escalation

## Purpose
Move a stuck issue to the level that can resolve it, with enough facts and options that the decision can be made in one reply or one short meeting, without blaming individuals or damaging working relationships.

## When to use
- A blocker or dependency has not been resolved through normal channels and a deadline is at risk.
- Two parties disagree and neither has authority to decide.
- A risk exceeds the current owner's tolerance or budget authority.

## When not to use
- The issue has not yet been raised with the directly responsible person. Use `stakeholder-email` first.
- It is a routine progress report with an Amber item. Use `status-update`.
- It is a live production incident. Use `incident-communication`.

## Inputs
Required:
- The issue and its impact (what slips, costs or breaks, and when).
- Who has been asked so far and what happened.

Optional:
- Evidence (ticket numbers, dates of requests), options considered, the escalation owner's role, organizational escalation path.

If the impact or deadline is missing, ask for it: without it the escalation cannot be prioritized. Never estimate cost or delay figures that the user has not given; mark them `[TBD]`.

## Process
1. Confirm escalation is warranted: normal channel tried, deadline or tolerance at risk, current level lacks authority. If not, recommend a direct message first.
2. Identify the escalation owner: the lowest level that can decide. Copy the counterpart's manager only if agreed or already informed; tell the counterpart before escalating ("no surprises").
3. Write the subject as `Escalation: <issue> – decision needed by <date>`.
4. State the ask in the first sentence: the decision, resource or intervention needed, and by when.
5. List verified facts with dates and references; separate them clearly from interpretations, which you label as such.
6. Quantify impact in the reader's terms: dates, customers, money, compliance, other teams. Use only supplied numbers.
7. Summarize what was already tried and the result, in neutral language about systems and commitments, not people.
8. Give 2-3 options with trade-offs, including "do nothing", and your recommendation with the reason.
9. State the consequence of no decision by the deadline and the next check-in date.
10. Remove emotive words, blame and sarcasm; re-read as if the counterpart will see it, because they probably will.
11. If the user's goal continues, suggest `trade-off-analysis` if options need deeper comparison or `raid-log` to track the issue until closure.

## Output format
```markdown
Subject: Escalation: <issue> – decision needed by <date>

<Name>, I need <decision/resource/intervention> by <date> to <protect outcome>.

**Facts**
- <date>: <fact with reference>

**Impact if unresolved**
- <what slips/costs/breaks, when, for whom>

**Already tried**
- <action> → <result>

**Options**
| Option | Pros | Cons / cost |
|---|---|---|
| A (recommended) | ... | ... |
| B | ... | ... |
| Do nothing | ... | ... |

**Ask:** <exact decision> by <date>. If no decision by then, <consequence>.
<Counterpart informed: yes/no>   Next check-in: <date>
```

## Quality checklist
- [ ] The ask and deadline are in the first sentence.
- [ ] Facts are dated and referenced; interpretations are labeled.
- [ ] Impact is stated in the escalation owner's terms, with no invented figures.
- [ ] Options include trade-offs and "do nothing"; a recommendation is given.
- [ ] Language is neutral and addresses commitments, not personal fault.
- [ ] The counterpart has been or will be informed before the escalation lands.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Escalating a feeling ("they are never responsive") instead of facts. Replace with dated requests and missed commitments.
- Escalating without options, which pushes the analysis upward. Always bring a recommendation.
- Escalating too late. When the tolerance is crossed, escalate the same day; a late escalation leaves no options.

## Example
Input: identity team has not delivered SSO for three weeks; pilot on the 15th slips unless it lands by the 8th.

Weak: "Hi, we are really frustrated with the identity team. They keep promising and nothing happens. Can you do something?"

Strong (excerpt):
Subject: Escalation: SSO integration for pilot – decision needed by the 5th
"Selin, I need a priority decision on the SSO integration by the 5th; without it on the 8th, the customer pilot on the 15th slips.
Facts: requested on `[date]` (ticket `[ID]`); committed dates `[date]` and `[date]` missed."
Options: A) identity team prioritizes SSO for one week (recommended); B) pilot with local accounts `[security approval needed]`; C) move the pilot.
