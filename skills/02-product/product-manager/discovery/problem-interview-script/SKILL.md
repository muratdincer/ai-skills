---
name: problem-interview-script
description: "Writes a non-leading customer problem interview script in the spirit of The Mom Test, asking about past behavior, real spending and current workarounds instead of opinions or pitches, with a funnel-ordered guide, follow-up probes, commitment signals and a note-taking sheet. Use when a team wants to validate that a problem exists before building, prepares discovery interviews, or asks to review questions that may be leading or hypothetical."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: discovery
  title: "Write a problem interview script"
  related: "interview-question-set, research-plan, screener-survey, jobs-to-be-done, research-synthesis"
  prompt: "Write a problem interview script to check whether small clinic owners actually struggle with appointment no-shows."
---

# Write a Problem Interview Script

## Purpose
Give interviewers a script that uncovers whether a problem is real, frequent and costly for a specific customer, based on facts about past behavior rather than compliments, hypotheticals or polite agreement.

## When to use
- Before committing to a solution, to test whether the target problem exists and matters.
- When a team keeps hearing "great idea" but sees no adoption and suspects biased interviews.
- To prepare a round of discovery interviews for a new segment or market.

## When not to use
- The goal is to test a prototype's usability. Use `usability-test-script`.
- Requirements must be elicited from internal stakeholders. Use `requirements-interview` or `interview-question-set`.
- A full study (sampling, recruitment, schedule) needs planning. Use `research-plan`, and `screener-survey` for recruitment.

## Inputs
Required:
- The problem hypothesis to explore and the target customer segment.

Optional, improves quality:
- Current assumptions about triggers, workarounds and spending.
- Interview length and format (remote/in person), number of interviews planned.
- What decision the interviews should support.

If the problem or segment is missing, ask for it. Remind the user to get consent for recording and to anonymize notes.

## Process
1. Rewrite the problem hypothesis as 2-4 learning goals phrased as questions about behavior ("How do clinic owners handle a no-show today?"), not about the solution.
2. List the riskiest assumptions each goal tests and what evidence would confirm or refute each; mark assumptions not stated by the user as `[ASSUMPTION]`.
3. Order the guide as a funnel: context and role, then the last concrete occurrence of the problem, then impact and frequency, then current workarounds and spending, then priority relative to other problems; move from broad to specific.
4. Write questions about specific past events ("Tell me about the last time..."), never hypotheticals ("Would you use...?") or leading framings ("Isn't it frustrating that...?").
5. Add probes for each main question: "What did you do next?", "What did that cost you?", "Why was that hard?", "What else have you tried?", "Who else was involved?".
6. Keep the solution out of the first 80% of the interview; if a pitch is needed, place it at the end and ask for a concrete commitment (time, introduction, pilot, pre-payment) instead of opinion.
7. Add a red-flag list for the interviewer: compliments, generic claims ("I always..."), future promises, feature requests without the underlying why.
8. Write the intro (purpose, no sales, consent, anonymization) and the close (who else to talk to, permission to follow up).
9. Provide a note sheet that separates facts, quotes, emotions, workarounds, spending and commitments, plus a post-interview scoring of the problem signal.
10. Timebox the guide to the stated length and mark optional questions to drop if time runs short.
11. If the user's goal continues, suggest the next skill: `screener-survey` to recruit the right participants, or `research-synthesis` / `jobs-to-be-done` after the interviews.

## Output format
```markdown
# Problem Interview Script: <segment> – <problem area>
Length: <min> · Format: <remote/in person> · Interviews planned: <n | [TBD]>

## Learning Goals
1. <question about behavior> – confirms if ... / refutes if ...

## Intro (2 min)
<purpose, not selling, consent to record, anonymized notes>

## Guide
| Min | Section | Main question | Probes |
|---|---|---|---|
| 3-8 | Context | ... | ... |
| 8-20 | Last occurrence | "Tell me about the last time ..." | ... |
| ... | Workarounds and spending | ... | ... |
| ... | Priority | ... | ... |
| ... | (Optional) Commitment | ... | ... |

## Close
- Who else should we talk to? · May we follow up?

## Red Flags for the Interviewer
- ...

## Note Sheet
| Facts | Quotes | Workarounds | Spending (time/money) | Commitments | Signal (strong/weak/none) |
|---|---|---|---|---|---|
```

## Quality checklist
- [ ] No question is hypothetical, leading or asks for an opinion on the idea.
- [ ] Every main question anchors on a specific past event or existing behavior.
- [ ] The solution is not mentioned before the optional commitment section.
- [ ] Each learning goal has confirming and refuting evidence defined.
- [ ] The guide fits the stated length, with optional questions marked.
- [ ] Consent and anonymization are covered.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Asking "Would you pay for X?". People are bad at predicting their behavior; ask what they paid for the last workaround.
- Pitching too early and collecting compliments. Hold the solution back and listen for spending, workarounds and emotion.
- Ending with "Any other ideas?". Close with an introduction or a commitment request; it tests how much the problem matters.

## Example
Input: "Check whether small clinic owners struggle with appointment no-shows."

Weak: "Would an automated reminder app help you reduce no-shows?"

Strong (excerpt):
- "Tell me about the last day a patient didn't show up. What happened next?"
- Probe: "What did you do with that slot? What did it cost you?"
- "What have you tried so far to reduce this? What did you like or dislike about it?"
- Commitment (end): "We are running a 4-week pilot with a few clinics. Would you like to join?"
