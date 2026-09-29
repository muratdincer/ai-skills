---
name: acceptance-criteria
description: "Writes testable acceptance criteria for a user story or requirement, in Given/When/Then scenarios or rule form, covering the happy path, business rule variations, validation, permissions and failure cases, with one trigger and one outcome per scenario. Use when a story needs its conditions of done, when criteria are vague or untestable, or when asked for 'AC', 'Gherkin' or 'Given/When/Then'."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Write acceptance criteria"
  related: "user-story, invest-check, edge-case-elicitation, bdd-feature-file, test-scenarios-from-requirements"
  prompt: "Write acceptance criteria for: As a store manager, I want to approve or reject a pending shift swap from my phone."
---

# Write Acceptance Criteria

## Purpose
Define, in terms the business and testers both accept, exactly what must be true for a story or requirement to be done, so that nothing is left to interpretation at review time.

## When to use
- A story or requirement is ready for refinement and lacks criteria.
- Existing criteria are vague ("works correctly", "fast", "user-friendly").
- Testers or automation need scenarios traceable to a story.

## When not to use
- The story itself is unclear or has no specific persona and outcome. Use `user-story` first.
- Executable feature files for an automation framework are needed. Use `bdd-feature-file`.
- A full test design with data combinations is needed. Use `test-scenarios-from-requirements`.

## Inputs
Required:
- The user story or requirement statement.

Optional, improves quality:
- Business rules, data definitions, screen or API behavior, permissions, known edge cases, the team's preferred criteria format.

If the story is missing, ask for it. If a rule that decides the outcome is unknown (a limit, a status, a role), ask for it in one short batch; otherwise mark it `[TBD]` in the criterion.

## Process
1. Restate the story's outcome in one line and list the business rules it depends on. Label any rule you infer `[ASSUMPTION]`.
2. Choose the format: Given/When/Then for behavior with state and sequence; rule form ("A swap cannot be approved after the shift has started") for simple constraints. Use one format consistently per story.
3. Write the happy-path scenario first.
4. Add one scenario per rule variation, validation failure, permission boundary and error or timeout case relevant to the story.
5. Enforce one When and one Then per scenario. Several triggers or outcomes means several scenarios; "And" in Then is allowed only for facets of the same outcome.
6. Make every Then observable and measurable: state, message, record, notification or number. Replace vague words with concrete values, or `[TBD]` if unknown.
7. Use concrete example data in Given (a named status, an amount, a date relation) instead of abstract phrasing; mask any personal data.
8. Keep criteria implementation-free: no UI controls, table names or endpoints unless they are part of the agreed contract.
9. Check coverage against the story: every rule and every "so that" outcome has at least one scenario; flag scope creep that belongs to another story.
10. List open questions and assumptions with owners.
11. If the goal continues, suggest `edge-case-elicitation` for deeper boundary cases, `invest-check` for story quality, or `bdd-feature-file` for automation.

## Output format
```markdown
# Acceptance Criteria: <story ID and title>
Rules referenced: <BR-xx, ...>

### AC-1 <scenario name> (happy path)
Given <context with concrete data>
When <single trigger>
Then <single observable outcome>

### AC-2 <scenario name>
...

### Rule-form criteria (if used)
- R-1 <constraint>

## Out of scope for this story
- ...
## Assumptions and Open Questions
- [ASSUMPTION] ...
1. <question> — <owner>
```

## Quality checklist
- [ ] Every scenario has exactly one When and one Then outcome.
- [ ] Every Then is observable and contains no vague terms.
- [ ] Happy path, rule variations, validation, permission and failure cases are covered where relevant.
- [ ] Criteria describe behavior, not UI controls or implementation.
- [ ] Every rule and the story outcome trace to at least one criterion.
- [ ] Unknown values are `[TBD]`, inferred rules are `[ASSUMPTION]`; nothing is invented.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
| Pitfall | Fix |
|---|---|
| "Then the system works correctly" | Name the exact state, message or record that proves it. |
| Two Whens in one scenario | Split into two scenarios; each tests one trigger. |
| Only the happy path | Add rejection, invalid input, no-permission and timeout scenarios. |
| Criteria that restate the story | Criteria must add conditions the story does not state. |

## Example
Input: "As a store manager, I want to approve or reject a pending shift swap from my phone."

Weak: "Manager can approve and reject swaps and everything is updated."

Strong:
### AC-1 Approve a pending swap
Given a swap request between two employees with status "Pending"
When the store manager approves it
Then both employees' schedules show the swapped shifts and the request status is "Approved"

### AC-2 Swap for a started shift
Given a swap request whose shift started 10 minutes ago
When the store manager tries to approve it
Then the approval is refused with the message that the shift has already started

Open question: Does rejection require a reason? `[TBD]` — Operations
