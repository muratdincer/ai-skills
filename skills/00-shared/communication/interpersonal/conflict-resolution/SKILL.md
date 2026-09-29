---
name: conflict-resolution
description: "Maps a workplace conflict into parties, stated positions, underlying interests, facts versus perceptions and conflict type, then proposes a mediated resolution path with options that serve shared interests and agreed next steps. Use when two people, teams or functions disagree on priorities, ownership, approach or behavior and the disagreement is blocking work or damaging the relationship."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: interpersonal
  title: "Resolve a conflict"
  related: "feedback-sbi, negotiation-prep, facilitation-guide, trade-off-analysis, decision-log"
  prompt: "Our backend and mobile teams keep arguing about who owns API versioning and releases are slipping. Help me mediate."
---

# Resolve a Conflict

## Purpose
Move a conflict from competing positions to an agreement built on the parties' actual interests, with a clear decision path when agreement is not possible, so work unblocks and the working relationship survives.

## When to use
- Two people or teams disagree on ownership, priorities, technical approach or ways of working and it blocks delivery.
- A manager or lead has to mediate between reports or peer teams.
- A recurring tension needs preparation before a meeting.

## When not to use
- One person's behavior needs feedback, not a two-sided dispute. Use `feedback-sbi`.
- You are one of the parties bargaining over terms with an external side. Use `negotiation-prep`.
- The disagreement is a well-framed technical choice between options. Use `trade-off-analysis`.

## Inputs
Required:
- Who is in conflict and what it is about, as described by the user.
- The user's role (mediator, manager, one of the parties).

Optional:
- Each side's view in their own words, history, impact on delivery, decision rights (who can decide if no agreement), organizational constraints.

If only one side's view is available, say so and mark the other side's perspective `[UNKNOWN]` or `[ASSUMPTION]`; plan to hear it before proposing a solution. Keep names and personal details to the minimum needed; describe behavior, not character. If the conflict involves harassment, discrimination or safety, stop and recommend HR or the formal channel.

## Process
1. Clarify the user's role and neutrality. If they are a party, they cannot mediate; suggest a neutral facilitator or switch to `negotiation-prep`.
2. Map the parties and anyone else affected or holding decision rights.
3. Separate each side's position (what they demand) from their interests (why: workload, accountability, quality, recognition, risk). Label every inferred interest `[ASSUMPTION]`.
4. Separate facts (verifiable) from perceptions and emotions; list facts to verify.
5. Classify the conflict: task (what), process (how, who owns), relationship (trust, respect) or values/priority. Relationship conflict is handled privately first; task and process conflict can be worked jointly.
6. Find shared interests and the cost of continued conflict for both sides; these open the joint conversation.
7. Plan the process: separate one-on-one listening sessions, then a joint session with ground rules (one speaker at a time, restate before responding, focus on the future).
8. Generate options that serve both sides' interests (split ownership by criteria, rotation, a trial period with review, explicit interface or working agreement), not a compromise that satisfies nobody.
9. Agree objective criteria to choose among options (delivery date, incident rate, effort) and a fallback: who decides if no agreement by when.
10. Define the agreement format: what changes, owners, review date, how to raise issues early next time.
11. If the user's goal continues, suggest `facilitation-guide` for the joint session, `decision-log` to record the agreement, or `feedback-sbi` for individual behavior follow-up.

## Output format
```markdown
# Conflict Map and Resolution Plan: <topic>
Mediator: <role> | Type: Task / Process / Relationship / Values | Urgency: <impact on delivery>

| Party | Position (stated) | Interests (why) | Facts | Perceptions |
|---|---|---|---|---|
| A | ... | ... [ASSUMPTION] | ... | ... |
| B | ... | ... | ... | ... |

Shared interests: ...
Cost of no resolution: ...

## Process
1. 1:1 with A – questions: ...
2. 1:1 with B – questions: ...
3. Joint session – ground rules, agenda, timebox

## Options
| Option | Serves A because | Serves B because | Risk |
Decision criteria: ...  | Fallback decider and deadline: ...

## Draft agreement
- Change: ... | Owner: ... | Review date: ... | Escalation path: ...
Open questions / facts to verify: ...
```

## Quality checklist
- [ ] Positions and interests are separated for every party, with inferences labeled.
- [ ] Both sides' views are represented, or the missing view is marked `[UNKNOWN]`.
- [ ] Facts and perceptions are separated; no blame language.
- [ ] Options serve interests of both sides, with objective selection criteria.
- [ ] A fallback decider and deadline exist if agreement fails.
- [ ] Safety, harassment or discrimination issues are routed to the formal channel.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Splitting the difference on positions. Work on interests; a midpoint often solves nobody's real problem.
- Holding the joint session first. Listen to each side privately so neither feels ambushed.
- Leaving without a review date. Agreements decay; schedule a check.

## Example
Input: backend and mobile teams argue about who owns API versioning; releases slip.

Weak: "Both teams should communicate better and respect each other. Let's have a meeting."

Strong (excerpt):
- Backend position: "Mobile must adapt to our API changes." Interest `[ASSUMPTION]`: freedom to evolve services without waiting on app store cycles.
- Mobile position: "Backend must never break the API." Interest: users on old app versions keep working.
- Type: Process (ownership). Shared interest: fewer release slips.
- Option: backend owns versioning, supports the last `[TBD: n]` API versions; mobile commits to a minimum-version upgrade window. Review after two releases.
