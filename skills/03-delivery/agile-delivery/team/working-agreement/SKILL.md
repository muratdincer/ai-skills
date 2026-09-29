---
name: working-agreement
description: "Facilitates and writes a team working agreement: collects norms for communication channels and response times, availability and core hours, code review and pairing, meetings, decision making, on-call and conflict handling, turns them into specific observable commitments, and sets how the agreement is reviewed and enforced. Use when a team forms or changes, recurring friction appears (slow reviews, meeting overload, after-hours pings), or someone asks for a team charter or ground rules."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 03-delivery
  role: agile-delivery
  area: team
  title: "Create a team working agreement"
  related: "wip-policy, team-health-check, retrospective-facilitation, definition-of-done, conflict-resolution"
  prompt: "Our team is now split between Istanbul and Berlin, reviews wait for days and people get pinged at night. Help us draft a working agreement."
---

# Create a Team Working Agreement

## Purpose
Turn the team's implicit expectations into a short, explicit set of norms that everyone has agreed to, so friction is handled by pointing at a shared agreement rather than at a person.

## When to use
- A team is newly formed, merged, or has new members or locations.
- Recurring friction: slow reviews, unclear availability, meeting overload, after-hours messages.
- A retrospective produced norm-related actions that need to be written down.

## When not to use
- Board columns, WIP limits and pull rules. Use `wip-policy`.
- The quality bar for finished work. Use `definition-of-done`.
- A specific interpersonal conflict. Use `conflict-resolution`.

## Inputs
Required:
- Team context: size, roles, locations/time zones, and the problems or goals that triggered the agreement (or raw inputs from a team session).

Optional, improves quality:
- The current agreement, if any.
- Organizational policies that bind the team (working hours, on-call compensation, security rules).
- Tools categories in use (chat, video, issue tracker) without needing product names.

If the triggering problems are unknown, ask the user for the top 3 frictions; the agreement must address real issues. If drafting without a team session, mark every norm `[DRAFT – TEAM TO AGREE]`.

## Process
1. List the frictions and goals from the input and map each to an agreement area: communication, availability, code review/pairing, meetings, decisions, quality/done, on-call/support, conflict and feedback, onboarding.
2. If running with the team, propose a session: silent individual writing of "I work best when..." and "It frustrates me when...", cluster the notes, then dot-vote the 5-8 areas that matter most. Use existing notes instead if provided.
3. For each chosen area, write 1-3 norms as specific, observable behaviors with numbers where useful (e.g. "reviews picked up within 4 working hours", "core overlap 10:00-13:00 Istanbul / 09:00-12:00 Berlin").
4. Test each norm: Can a newcomer tell if it was followed? Does it respect organizational policy and local law on working hours? Does it work for every location and role? Rewrite or drop norms that fail.
5. Resolve conflicts between norms (e.g. fast response vs. focus time) by defining when each applies, such as focus blocks with an urgent-channel exception.
6. Add a decision rule for the team (e.g. consent: proceed unless someone has a reasoned objection) and a disagreement path.
7. Define how the agreement is kept alive: where it lives, how anyone can call out a breach kindly, and a review trigger (every N iterations, on member change, or when a norm is repeatedly broken).
8. Keep it to one page; move detailed procedures to linked documents.
9. Mark inferred norms `[DRAFT – TEAM TO AGREE]` and list open questions; suggest `retrospective-facilitation` for the next review and `team-health-check` to see whether friction declined.

## Output format
```markdown
# Team Working Agreement – <team>
Agreed on: <date or [TBD]> · Next review: <trigger/date> · Members: <roles/locations>

## Communication
- ...
## Availability and Core Hours
- ...
## Code Review and Collaboration
- ...
## Meetings
- ...
## Decisions and Disagreement
- ...
## Support / On-call
- ...
## Feedback and Conflict
- ...

## Keeping This Alive
- Breach call-out: ...
- Review trigger: ...

## Open Questions
- ...
```

## Quality checklist
- [ ] Every norm addresses a stated friction or goal.
- [ ] Norms are specific and observable, with numbers or conditions where useful.
- [ ] Norms work across all locations, time zones and roles in the team.
- [ ] Nothing contradicts organizational policy or working-time rules; conflicts are flagged.
- [ ] Norms not agreed by the team are marked `[DRAFT – TEAM TO AGREE]`.
- [ ] A review trigger and a way to call out breaches are included.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing values instead of behaviors ("we respect each other"). Replace with what people will actually do.
- Imposing the agreement from a manager. It only works when the team has shaped and agreed it.
- Writing it once and forgetting it. Review it when the team or its frictions change.

## Example
Input: Istanbul and Berlin members; reviews wait for days; night-time pings.

Excerpt of output:
- Weak norm: "Be responsive." Strong norm: "Pull requests are picked up within 4 working hours of the reviewer's time zone; if not possible, the reviewer says so and suggests someone else."
- Availability: core overlap 10:00-13:00 Istanbul (09:00-12:00 Berlin) `[DRAFT – TEAM TO AGREE]`; outside own working hours, messages are sent scheduled, and only production incidents use the urgent channel.
