---
description: Prepares a focused 1:1 meeting plan with a direct report, including follow-ups from the previous session, report-owned topics, open coaching questions and signals to watch. Use when a manager has an upcoming 1:1, wants to structure a recurring 1:1, or needs to prepare for a harder conversation (feedback, workload, career, morale).
related: one-on-one-notes, feedback-sbi, career-development-plan, goal-setting, conflict-resolution
prompt: Prepare my 1:1 with Ayşe tomorrow. Last time she said she felt stuck on the billing migration and wanted more design ownership.
---

# Prepare a 1:1

## Purpose
Turn a 1:1 into a conversation that belongs to the report, closes loops from last time and surfaces problems early, instead of a status meeting.

## When to use
- A recurring 1:1 is coming up and the manager wants a structured agenda.
- The previous 1:1 left open commitments, concerns or career topics.
- The manager must raise feedback, workload, a change or a sensitive topic.
- A new report joins and the first 1:1s set the working relationship.

## When not to use
- Documenting what was said after the meeting. Use `one-on-one-notes`.
- Formal feedback on sustained underperformance. Use `underperformance-plan`.
- Delivering a single piece of feedback only. Use `feedback-sbi`.

## Inputs
Required:
- Who the 1:1 is with (role, tenure in team) and the meeting purpose (recurring, first, or topic-driven).

Optional, improves quality:
- Notes and commitments from the last 1:1.
- Current work, goals, recent wins or incidents, feedback from peers.
- Topics the report has already added.
- Known context: workload, leave, org changes, career aspirations.

If the person or purpose is missing, ask. Everything else becomes a "to check" item in the plan.

## Process
1. Separate observed facts (events, deliverables, quotes) from impressions. Only facts go into feedback items.
2. List open follow-ups from the last 1:1 with owner and status. Manager-owned items come first; closing your own loops builds trust.
3. Reserve the first half for the report's topics. If none are known, plan open prompts rather than filling the time.
4. Pick at most two manager topics. For each, state the intent, the fact base and the desired outcome of the conversation.
5. If feedback is included, draft it in situation-behavior-impact form and prepare a question inviting their view.
6. Add one rotating deeper theme (career, growth, team health, workload, motivation) chosen by what has not been discussed recently.
7. Prepare 3-5 open, non-leading questions. Avoid questions that can be answered with yes/no or that presume a cause.
8. Note signals to listen for: energy change, disengagement, overload, conflict, flight risk. These are hypotheses to check, not conclusions.
9. Plan the close: summary, commitments with owners and dates, and the next check-in point.
10. Check the plan for bias: would you raise the same topic, in the same way, with another report in the same situation?

## Output format
```markdown
# 1:1 Plan: <name> – <date>
Type: <recurring / first / topic-driven> · Duration: <min>

## Follow-ups From Last Time
| Item | Owner | Status |
|---|---|---|

## Their Topics (first)
- <topic or open prompt>

## My Topics (max 2)
| Topic | Intent | Facts | Desired outcome |
|---|---|---|---|

## Deeper Theme This Time
<theme> – questions:
1. ...

## Signals to Listen For (hypotheses)
- ...

## Close
- Summary, commitments (owner, date), next check-in
```

## Quality checklist
- [ ] The report's topics come before the manager's topics.
- [ ] Every feedback point is based on observable behavior, not personality.
- [ ] Previous commitments are listed, especially the manager's own.
- [ ] Questions are open and non-leading.
- [ ] Signals are phrased as things to check, not judgments.
- [ ] Sensitive personal details (health, family) are not recorded beyond what the report chose to share.

## Common pitfalls
- Running the 1:1 as a status update. Move status to async channels and keep this time for the person.
- Overloading the agenda. Two manager topics maximum; carry the rest forward.
- Arriving with a conclusion ("you seem unmotivated"). Bring facts and ask for their perspective.

## Example
Input: "1:1 with Ayşe tomorrow. Last time she felt stuck on billing migration and wants more design ownership."

Excerpt of output:
- Follow-up: "Ask architect to include Ayşe in migration design review" – Owner: me – Status: `[UNKNOWN, confirm before meeting]`.
- Deeper theme: Growth – "What part of the migration design would you want to own end to end?"
- Signal to check: Frustration with blocked work may be a workload or autonomy issue; ask, do not assume.
