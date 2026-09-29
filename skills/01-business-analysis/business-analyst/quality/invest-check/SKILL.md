---
description: "Evaluates user stories against the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable), scores each criterion with evidence and gives concrete fixes such as splits, rewrites or missing acceptance criteria. Use when refining a backlog, before stories enter an iteration or commitment, or when a story keeps getting re-estimated or carried over."
related: "user-story, acceptance-criteria, story-splitting, definition-of-ready, backlog-refinement"
prompt: "Run an INVEST check on these 8 stories for the checkout epic and tell me which ones are not ready."
---

# Check Stories Against INVEST

## Purpose
Tell the team, story by story, whether it is ready to be planned and built, and exactly what to change if not. The output is a scored table with evidence and actionable fixes, not a generic lecture on INVEST.

## When to use
- During backlog refinement or before a planning session.
- A story has been carried over, re-estimated or disputed repeatedly.
- A new team or stakeholder writes stories and wants quick feedback.

## When not to use
- You need to write the stories from scratch. Use `user-story`.
- The story is fine but too large and you need split options. Use `story-splitting`.
- You need the team's full readiness criteria, not just INVEST. Use `definition-of-ready`.

## Inputs
Required:
- One or more stories: title, narrative, and acceptance criteria if any.

Optional, improves quality:
- Epic or goal context, related stories, dependencies known.
- The team's typical story size or iteration length (for "Small").
- The team's definition of ready.

If acceptance criteria are absent, still evaluate, but mark Testable as failing.

## Process
1. Restate each story in one line: user, capability, benefit. If the benefit is missing, technical ("so that the API is called") or merely restates the want, note it for Valuable. Flag generic personas ("as a user") and technical tasks written as stories; the latter belong in the work breakdown, not the story list.
2. Independent: list dependencies on other stories, teams or systems. Distinguish hard (cannot start) from soft (ordering preference). Suggest reordering, stubbing or merging.
3. Negotiable: check whether the story prescribes UI or technical solution details that should be open. Flag over-specification.
4. Valuable: check that a user or business stakeholder would notice the result. Technical-only stories should state the enabled outcome or be tied to a value story.
5. Estimable: identify unknowns blocking estimation (domain, technical, external). Suggest a spike or question for each.
6. Small: judge against the team's typical size; if unknown, flag stories with many acceptance criteria, several roles, multiple workflows or "and" in the title. Name a split pattern (workflow step, business rule, data variation, happy/unhappy path, interface).
7. Testable: check acceptance criteria for observable outcomes, data conditions and error cases. Propose missing criteria in Given/When/Then or rule form; a scenario with more than one When or Then is a split candidate.
8. Score each letter Pass / Partial / Fail with one-line evidence; overall verdict: Ready / Needs work / Not ready.
9. Order fixes by effort-to-impact so the team can act in the refinement session.
10. If the user wants to continue, suggest `story-splitting` for stories failing Small, `acceptance-criteria` for stories failing Testable, or `definition-of-ready` for the full readiness gate.

## Output format
```markdown
# INVEST Check: <epic / set>

## Overview
| Story | I | N | V | E | S | T | Verdict |
|---|---|---|---|---|---|---|---|
| S1 <title> | Pass | Partial | Pass | Fail | Pass | Partial | Needs work |

## Story Details
### S1 <title>
- Evidence: I … / N … / V … / E … / S … / T …
- Fixes:
  1. <concrete change>
  2. <missing acceptance criterion in Given/When/Then>
- Questions: <what blocks estimation, who answers>
```

## Quality checklist
- [ ] Every score has evidence quoted or referenced from the story.
- [ ] Every Fail or Partial has at least one concrete fix.
- [ ] Split suggestions name a split pattern and yield vertically sliced, valuable stories.
- [ ] Proposed acceptance criteria are marked as proposals, not as agreed scope.
- [ ] No size judgment is made in story points unless the team's scale was given.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Splitting by technical layer (UI story, API story, DB story). This breaks Valuable and Independent; split by behavior instead.
- Treating Independent as absolute. Some ordering is normal; only flag dependencies that block parallel work or planning.
- Failing Negotiable for legitimate constraints (regulation, contract). Mark them as constraints instead.

## Example
Input: "S3: As a user I want to pay with card and PayPal and save my card, so that checkout is easier." No acceptance criteria.

Excerpt of output:
| Story | I | N | V | E | S | T | Verdict |
|---|---|---|---|---|---|---|---|
| S3 | Partial | Pass | Pass | Partial | Fail | Fail | Not ready |

Fixes: split by payment method and by "save card" (business rule variation); add criteria for declined card and 3-D Secure failure; ask Security whether card storage is tokenized by the payment provider `[UNKNOWN]`.


Weak rewrite: "As a user I want to pay easily so that I can pay." (generic persona, benefit restates the want)
Strong rewrite: "As a returning customer I want to pay with a saved card so that I can complete checkout without re-entering card details."
