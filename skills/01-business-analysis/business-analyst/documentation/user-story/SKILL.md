---
description: "Writes user stories in the As a / I want / So that form with a specific persona, a real outcome, context, business rules, dependencies and acceptance criteria hooks, and flags items that are really technical tasks or need splitting. Use when a need, requirement or feature must become backlog items, or when asked to 'write stories', 'turn this into user stories' or rewrite weak ones."
related: "acceptance-criteria, invest-check, story-splitting, persona, epic-breakdown"
prompt: "Write user stories for letting store managers approve staff shift swaps from their phone."
---

# Write User Stories

## Purpose
Turn a need into small, valuable backlog items that state who benefits, what they can do and why it matters, so the team can discuss, estimate and verify each one independently.

## When to use
- A feature, requirement or intake request must become backlog items.
- Existing stories are vague ("As a user I want a button") and need rewriting.
- A refinement session needs draft stories to discuss.

## When not to use
- The work is still a large, unshaped capability. Use `epic-breakdown` or `story-mapping` first.
- Only the conditions of done are needed for an existing story. Use `acceptance-criteria`.
- A story exists and must be cut into smaller pieces. Use `story-splitting`.

## Inputs
Required:
- The need, feature description or requirement to express as stories.

Optional, improves quality:
- Personas or user roles, business rules, process model, screen sketches, the team's story template and Definition of Ready.

If the need is missing, ask for it. If the user roles are unclear, ask one question about who performs the task; otherwise write stories and list gaps as open questions.

## Process
1. Identify the actors from the input. Use a specific persona or role ("store manager", "first-time applicant"), never "user"; if the role is inferred, mark it `[ASSUMPTION]`.
2. List the user goals per actor as verb + object. Separate what the requester said from what you infer.
3. Write each story: "As a <specific persona>, I want <capability>, so that <outcome>". The "so that" must state a real benefit (time saved, risk avoided, decision enabled), not restate the want.
4. Detect technical tasks disguised as stories ("As a developer I want to migrate the database"). Reframe them to the user value they enable, or mark them as technical work items outside the story set.
5. Check size: if a story contains "and", several roles, several workflows or several data variations, propose a split and name the split pattern (workflow step, rule variation, data type, happy/unhappy path).
6. Add context per story: business rules (by ID if a catalog exists), relevant data, dependencies, and out-of-scope notes.
7. Draft 2-5 acceptance criteria headlines per story (rule form, one outcome each); leave full Given/When/Then to `acceptance-criteria`.
8. Order the stories so the first delivers a thin end-to-end slice; note dependencies explicitly.
9. Collect assumptions and open questions with a likely owner; never invent rules, limits or numbers.
10. If the goal continues, suggest `acceptance-criteria` for detailed criteria, `invest-check` for a quality review, or `story-splitting` for oversized stories.

## Output format
```markdown
# User Stories: <feature>
Personas: <list> · Source: <requirement / intake ID>

## US-01 <short title>
As a <specific persona>, I want <capability>, so that <outcome>.
- Context / rules: <BR-xx, notes>
- Acceptance criteria (headlines):
  1. ...
- Dependencies: ...
- Out of scope: ...
- Split suggestion: <none / pattern + proposed stories>

## Technical work items (not user stories)
- ...

## Assumptions and Open Questions
- [ASSUMPTION] ...
1. <question> — <owner>
```

## Quality checklist
- [ ] Every story names a specific persona; none says "as a user" or "as the system".
- [ ] Every "so that" states an outcome that differs from the "I want".
- [ ] Technical tasks are separated from user stories.
- [ ] Each story describes one capability; compound stories carry a split suggestion.
- [ ] Each story has acceptance criteria headlines, each with a single outcome.
- [ ] No rules, limits or numbers were invented; inferences are labeled.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
| Pitfall | Fix |
|---|---|
| "As a user..." | Name the role whose goal it is; different roles usually mean different stories. |
| "So that I can use the feature" | Ask "why does that matter?" until a business or user outcome appears. |
| Story describes the UI ("a dropdown") | Describe the capability; leave the control to design. |
| Stories sliced by layer (UI story, API story) | Slice vertically so each story is usable on its own. |

## Example
Input: "Store managers should approve shift swaps on mobile."

Weak: "As a user, I want a swap approval screen, so that I can approve swaps."

Strong:
US-01 As a store manager, I want to approve or reject a pending shift swap from my phone, so that staffing gaps are resolved before the shift starts without me being at the back office.
- Rules: swap allowed only between staff with the same qualification `[ASSUMPTION – confirm with HR]`.
- Acceptance criteria headlines: 1. Approved swap updates both schedules. 2. Rejection notifies both employees with the reason. 3. A swap for a shift already started cannot be approved.
- Open question: Is there a deadline before shift start after which swaps are locked? — Operations
