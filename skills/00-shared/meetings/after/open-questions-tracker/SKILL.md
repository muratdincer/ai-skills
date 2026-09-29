---
name: open-questions-tracker
description: "Collects unresolved questions from meetings, documents and threads into a tracker with a precise question, why it matters, what it blocks, owner, needed-by date, status and answer, and prioritizes by what each blocks. Use when a project has many loose questions, when analysis or design is waiting on answers, or when someone asks \"what are we still waiting on?\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: meetings
  area: after
  title: "Track open questions"
  related: "action-item-extraction, meeting-notes, raid-log, request-clarification-questions, decision-log"
  prompt: "Go through these three meeting notes and the requirements doc and build an open questions list with owners and due dates."
---

# Track Open Questions

## Purpose
Make every unresolved question visible, owned and time-bound so that work waiting on answers is unblocked on time and answers are recorded where people will find them.

## When to use
- Several meetings or documents left questions unanswered.
- Analysis, design, estimation or a decision is blocked by missing information.
- An existing question list must be updated with new answers or new questions.

## When not to use
- The items are tasks someone committed to do. Use `action-item-extraction`.
- Clarification questions for a single new request must be drafted. Use `request-clarification-questions`.
- Risks, assumptions, issues and dependencies must be tracked together. Use `raid-log`.

## Inputs
Required:
- Source material with questions (notes, documents, threads) or an existing list.

Optional:
- Milestones or dates the questions affect, stakeholder list with areas of responsibility, existing tracker to update.

If no milestone dates are given, derive "needed-by" from what the question blocks and mark it `[ASSUMPTION]`.

## Process
1. Harvest questions: explicit "?", "not sure", "TBD", "to be confirmed", "depends on", disagreements left open, and `[UNKNOWN]` markers in documents.
2. Rewrite each as a closed or specific question answerable by one person ("Which fields must the audit export contain?" not "export details?").
3. Merge duplicates and split compound questions.
4. For each, state why it matters and what it blocks (a work item, decision, estimate or milestone).
5. Assign an owner who can answer or obtain the answer; if unknown, write `[OWNER UNKNOWN]` and suggest a role.
6. Set needed-by = the latest date the answer is useful for the blocked work, not an arbitrary date.
7. Prioritize: P1 blocks the critical path or a decision this week; P2 blocks planned work; P3 nice to know.
8. Set status: Open, Asked (date), Answered, Closed-no-longer-relevant, Escalated. Record answers verbatim with source and date.
9. When updating an existing list, move answered questions to a closed section and note which decisions or documents must be updated.
10. Flag questions past needed-by for escalation.
11. If the user's goal continues, suggest `raid-log` for questions that have become risks or issues and `decision-log` to record answers that settle a decision.

## Output format
```markdown
# Open Questions – <project/topic> (as of <date>)
| ID | Question | Why it matters / blocks | Priority | Owner | Needed by | Status | Source |
|---|---|---|---|---|---|---|---|
| Q1 | ... | ... | P1 | ... | YYYY-MM-DD | Open | <meeting/doc> |

Overdue / escalate: <IDs>

## Answered since last update
| ID | Answer | Answered by | Date | Update needed in |
|---|---|---|---|---|
```

## Quality checklist
- [ ] Every question is specific and answerable by one person.
- [ ] Each question states what it blocks.
- [ ] Each has an owner or `[OWNER UNKNOWN]` with a suggested role.
- [ ] Needed-by dates derive from blocked work, assumptions are marked.
- [ ] Answered items record the answer, source and follow-up updates.
- [ ] Anything not stated in the input is labeled `[ASSUMPTION]` or listed as an open question, never presented as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Vague questions ("performance?") that nobody can answer. Make them specific and measurable.
- Owner is the person who asked, not the one who can answer. Assign the answer holder.
- Answers that stay in chat. Record them and update the affected document or decision.

## Example
Input: Notes mention "retention period for logs? legal to confirm" and "not sure if SSO is needed for partners".

Excerpt of output:
| Q1 | What retention period applies to application logs containing personal data? | Blocks logging design and storage estimate | P1 | Legal/DPO `[confirm name]` | [ASSUMPTION] before design review | Open | Arch sync 03/06 |
| Q2 | Must partner users authenticate via corporate SSO? | Blocks authentication scope and estimate | P2 | [OWNER UNKNOWN] – product owner | [UNKNOWN] | Open | Kickoff notes |
