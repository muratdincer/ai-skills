---
name: feedback-sbi
description: "Frames positive or corrective feedback with the Situation-Behavior-Impact model, separating observed behavior from interpretation, stating the concrete impact, and ending with a request and an open question. Use when someone must give feedback to a colleague, report, peer or manager, prepare a difficult conversation, or rewrite feedback that sounds like a judgment of the person."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 00-shared
  role: communication
  area: interpersonal
  title: "Give feedback (SBI)"
  related: "one-on-one-prep, performance-review, conflict-resolution, tone-rewrite, underperformance-plan"
  prompt: "Help me give feedback to a senior developer who keeps merging pull requests without waiting for review, in a way that doesn't make him defensive."
---

# Give Feedback (SBI)

## Purpose
Turn an observation about someone's work into specific, fair and actionable feedback that the receiver can recognize, understand the consequence of, and act on, while keeping the relationship intact.

## When to use
- Preparing corrective or reinforcing feedback for a one-on-one or after an event.
- Feedback drafted so far is vague ("be more proactive") or personal ("you are careless").
- Giving upward or peer feedback where tone and fairness matter.

## When not to use
- A structured, period-based evaluation is due. Use `performance-review`.
- The issue is repeated, documented underperformance needing a formal plan. Use `underperformance-plan`.
- Two parties are in an ongoing dispute and need mediation. Use `conflict-resolution`.

## Inputs
Required:
- What happened: the specific situation and the behavior observed (by whom, when, where).
- The relationship (manager, peer, report, upward) and the goal of the feedback.

Optional:
- Impact already known, previous feedback on the topic, receiver's context (workload, new role), preferred language and setting.

If the behavior is only described as a trait ("he is arrogant"), ask one question at a time for the concrete instances behind it. Never invent incidents, dates or quotes; keep second-hand reports marked as such. Minimize personal details not needed for the feedback.

## Process
1. Check the intent and timing: feedback is given soon after the event, in private for corrective feedback, and when the giver can stay calm. Note if timing is off.
2. Write the Situation: when and where, specific enough to recall ("in Tuesday's release of the billing service"), not "always" or "lately".
3. Write the Behavior: observable actions or words only, what a camera would record. Remove adjectives, motives and labels; move any interpretation to a separate line marked `[INTERPRETATION]`.
4. Write the Impact: the concrete effect on the team, customer, quality, schedule or the giver ("two defects reached production; on-call was paged twice"). Use "I" statements for personal impact. Mark unverified impact `[TBD]`.
5. Add the invitation: an open, non-leading question to hear their view ("How did you see it?"), because the receiver may have context the giver lacks.
6. Add the request or reinforcement: for corrective feedback, a specific expected behavior going forward; for positive feedback, what exactly to keep doing.
7. Check balance and fairness: one topic per conversation, no stacked complaints, no "feedback sandwich" that hides the message.
8. Adapt to relationship and culture: upward feedback asks permission and focuses on impact on your work; in Turkish, keep "siz" where the relationship is formal and avoid indirectness that hides the request.
9. Prepare for reactions: likely defensive responses and a calm reply to each; decide what follow-up will confirm the change.
10. If the user's goal continues, suggest `one-on-one-prep` to plan the conversation, `conflict-resolution` if the other side disputes the situation, or `performance-review` for period-based evaluation.

## Output format
```markdown
# Feedback: <receiver role> – <topic>
Type: Corrective / Reinforcing | Setting: <1:1, private, when>

- Situation: <when, where>
- Behavior: <observable actions/words>
- Impact: <concrete effect on team/customer/work/me>
- Invitation: "<open question>"
- Request / keep doing: <specific behavior going forward>

Spoken version (3-5 sentences):
"<...>"

Likely reactions and responses:
- "<reaction>" -> <calm reply>
Follow-up: <how and when change will be noticed>
[INTERPRETATION] / [TBD] items kept out of the message: ...
```

## Quality checklist
- [ ] Behavior contains only observable facts, no traits, motives or adjectives.
- [ ] Situation is specific; no "always", "never" or "lately".
- [ ] Impact is concrete and verified or marked `[TBD]`.
- [ ] There is one topic, an open invitation and a specific request.
- [ ] Wording fits the relationship (upward, peer, down) and language formality.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Describing the person instead of the behavior ("you are careless"). Describe the action a camera would see.
- Delivering feedback weeks later in a review. Give it close to the event.
- Only corrective feedback. Use SBI for reinforcing good behavior too, so it is not associated only with criticism.

## Example
Input: senior developer merges pull requests without waiting for review.

Weak: "You don't respect the team's process and you act like the rules don't apply to you."

Strong (excerpt):
- Situation: In the last two releases of the billing service (`[dates]`).
- Behavior: Three pull requests were merged within minutes of opening, before any reviewer commented.
- Impact: One of them introduced the rounding defect customers reported; the team also stopped reviewing your changes because they assume they are already live.
- Invitation: "What was going on for you with those merges?"
- Request: "Going forward, wait for one approval, and if something is urgent, ping me or the on-call reviewer."
