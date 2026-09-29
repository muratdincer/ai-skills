---
name: review-comment-writing
description: "Writes or rewrites code review comments so they are specific, kind and actionable, labeled by severity and intent (Critical, Required, Nit, Optional, FYI, plus question and praise) and backed by a reason and a proposed change. Use when a reviewer has raw observations or blunt draft comments on a pull request and wants them phrased clearly, or when review threads are turning tense."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: collaboration
  title: "Write review comments"
  related: "code-review, feedback-sbi, tone-rewrite, coding-standards, conflict-resolution"
  prompt: "Rewrite my review comments so they are clear but not harsh. First one is 'this is wrong, why would you query in a loop?'"
---

# Write Review Comments

## Purpose
Turn review observations into comments the author can act on without guessing severity or feeling attacked. Clear labels and reasons reduce back-and-forth, keep reviews about the code, and make it obvious what blocks the merge.

## When to use
- A reviewer has findings and wants them written as PR comments.
- Draft comments are terse, sarcastic or ambiguous about whether they block.
- A review thread has become a debate and needs a constructive reply.

## When not to use
- Finding the issues in the first place. Use `code-review`.
- Feedback about a person's behavior or performance rather than code. Use `feedback-sbi`.

## Inputs
Required:
- The observations or draft comments, each with the code it refers to (or a description of it).

Optional, improves quality:
- The team's comment label convention and coding standards.
- Relationship context (new joiner, cross-team contributor, senior peer).
- The author's reply, if answering within a thread.

If a comment's code context is missing and the comment makes a technical claim, ask for the snippet or keep the claim as a question.

## Process
1. For each observation, decide the label: `Critical` (blocks merge, state the risk), Required (the default, no prefix: must be addressed before merge), `Nit` (trivial, author may ignore), `Optional` (better alternative, author decides), `FYI` (information, no action), `question` (you do not know yet), `praise` (specific and genuine). Valid points outside this PR become `Optional` with "follow-up".
2. Check that the claim is correct and specific. If you cannot prove it from the visible code, convert it to a question.
3. Write the observation about the code, not the person: "this loop issues one query per item", not "you query in a loop".
4. State the consequence or reason: bug, risk, cost, standard violated (link the rule if one exists).
5. Propose the concrete fix, not only the problem: snippet, API to use, or pattern; offer it as an option when there are several valid fixes.
6. Keep it short: one issue per comment, two to four sentences, no rhetorical questions, no sarcasm, no "just" or "obviously".
7. Consolidate repeated issues: comment once and say "same applies to lines X, Y".
8. For contested threads: restate the author's point fairly, name the actual disagreement, propose a decision rule (standard, data, tech lead call) or take it offline.
9. Add at least one specific praise comment when something is genuinely well done.
10. If the observations themselves are incomplete or unverified, suggest running `code-review` first; for feedback about behavior rather than code, suggest `feedback-sbi`.

## Output format
```markdown
**[<label>]** <observation about the code, with location>
<reason / consequence, one or two sentences>
<proposed change or snippet>   (optional: "Same applies to <locations>.")
```
For rewrites, show each original next to the rewritten version in a table:
| # | Original | Rewritten | Label |
|---|---|---|---|

## Quality checklist
- [ ] Every comment's severity is unambiguous (one label, or no prefix meaning Required) and Critical comments explain the risk.
- [ ] No comment addresses the person ("you always...", "why would you...").
- [ ] Each non-question comment offers a concrete change.
- [ ] Claims that cannot be verified from the code are phrased as questions.
- [ ] Repeated issues are consolidated.
- [ ] Nits are few, and a linter or formatter rule is suggested when they recur.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Unlabeled comments: the author treats every remark as blocking, and reviews stall. Label everything.
- Softening a real Critical issue into a vague "maybe consider". Be kind and clear: state that it blocks and why.
- Leading questions ("Did you test this?") that are criticism in disguise. Ask real questions or state the concern.

## Example
Input: "this is wrong, why would you query in a loop?" on `for (id in ids) repo.findById(id)`.

Weak (original): "this is wrong, why would you query in a loop?" — no severity, aimed at the person, no fix.

Strong (rewritten):
**[Critical]** `OrderLoader.kt:31` issues one database query per order ID. For a 500-item cart this is 500 round trips on the checkout path.
Could we fetch them in one call, e.g. `repo.findAllById(ids)`, and map the results by ID? Same pattern at `InvoiceLoader.kt:58`.
