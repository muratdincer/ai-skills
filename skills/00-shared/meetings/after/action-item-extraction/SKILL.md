---
name: action-item-extraction
description: "Finds every explicit and implicit commitment in meeting notes, transcripts, emails or chat threads and turns each into a verifiable action item with a single owner, due date, status and source reference, flagging missing owners or dates. Use when someone asks \"what are the action items?\", \"who does what?\", or needs tasks ready for a tracker after a meeting or discussion."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: after
  title: "Extract action items"
  related: "meeting-notes, meeting-follow-up, open-questions-tracker, decision-log, task-breakdown"
  prompt: "Extract all action items from this transcript of our release readiness call and put them in a table."
---

# Extract Action Items

## Purpose
Make sure no commitment made in a conversation gets lost, by turning each one into a clear, owned, dated and trackable task.

## When to use
- After a meeting, workshop, incident call or long chat/email thread.
- Notes exist but actions are buried in discussion.
- Actions must be loaded into a work tracker or follow-up message.

## When not to use
- The need is a full structured record of the meeting. Use `meeting-notes`.
- Unresolved questions, not tasks, must be tracked. Use `open-questions-tracker`.
- A feature must be broken down into engineering tasks. Use `task-breakdown`.

## Inputs
Required:
- The source text (notes, transcript, thread).

Optional:
- Meeting date (to resolve relative dates like "next Friday"), attendee list and roles, existing action list to update.

If the meeting date is missing, keep relative dates as written and mark them `[confirm date]`.

## Process
1. Scan for commitment signals: "I will", "we'll", "can you", "let's", "X to do Y", "by Friday", "follow up", "send", "check", "ask", "prepare", and agreed next steps in decisions.
2. Include implicit actions that follow directly from a decision (decision "use vendor B" implies "notify vendor A") and mark them `[IMPLIED]`.
3. Rewrite each as a verb-first, verifiable task with a clear done state ("Send the revised estimate to Finance", not "estimate").
4. Assign exactly one owner. If the source names a group, pick the named lead if stated, otherwise `[OWNER UNKNOWN]`. Never assign by guess.
5. Resolve due dates to calendar dates when the meeting date is known; otherwise keep the phrase and flag it.
6. Set status: Open, In progress, Done (if completed during the meeting), Blocked (with blocker).
7. Record dependencies between actions and link each to its source (topic, timestamp or quote).
8. Merge duplicates and split compound actions ("Ali and Zeynep will review and deploy") into separate items.
9. Separate items that are really questions or risks and list them below the table.
10. Summarize gaps: count of actions without owner or date, to be resolved in the follow-up.
11. If the user's goal continues, suggest `meeting-follow-up` to circulate the actions, `open-questions-tracker` for questions that are not commitments, or `task-breakdown` for actions too large to finish as one item.

## Output format
```markdown
# Action Items – <meeting/thread>, <date>
| # | Action (verb first) | Owner | Due | Status | Depends on | Source |
|---|---|---|---|---|---|---|
| A1 | ... | ... | YYYY-MM-DD | Open | – | <topic/timestamp> |

Implied actions: <IDs marked [IMPLIED]>
Gaps: <n> without owner, <n> without due date
Not actions (move to questions/risks):
- ...
```

## Quality checklist
- [ ] Every commitment in the source is captured, including implied ones (marked).
- [ ] Each action starts with a verb and has a clear done state.
- [ ] Each action has exactly one owner or `[OWNER UNKNOWN]`.
- [ ] Relative dates are resolved or flagged.
- [ ] Questions and risks are not disguised as actions.
- [ ] Each action links back to its source.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Assigning "the team" or two people as owner. Accountability needs one name.
- Missing soft commitments ("I'll take a look"). They are actions; capture them and confirm in the follow-up.
- Treating ideas raised in discussion as agreed actions. Only include what someone committed to or was asked and agreed to do.

## Example
Input: "Burak: I'll check the rollback script before Thursday. We agreed to freeze merges from Wednesday. Someone should tell support about the window."

Excerpt of output:
| A1 | Verify the rollback script in staging | Burak | Thu `[confirm date]` | Open | – | Rollback topic |
| A2 | Announce merge freeze from Wednesday to all developers `[IMPLIED]` | [OWNER UNKNOWN] | before Wed | Open | – | Freeze decision |
| A3 | Inform support about the release window | [OWNER UNKNOWN] | [UNKNOWN] | Open | – | "Someone should tell support" |
