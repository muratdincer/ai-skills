---
description: Builds a user story map with a left-to-right backbone of user activities and steps, stories stacked by priority beneath each step, and horizontal release slices that each deliver a usable end-to-end outcome. Use when planning a product or large feature across the whole user journey, when the flat backlog has lost the big picture, or when a team must agree on what goes into the first and following releases.
related: epic-breakdown, mvp-scoping, release-planning, customer-journey-map, roadmap
prompt: Build a story map for our B2B expense management app, from employee submitting a receipt to finance reimbursing it.
---

# Build a User Story Map

## Purpose
Lay out the user's journey as a backbone of activities and steps, hang stories beneath it, and cut horizontal release slices so every release lets a real user complete the journey end to end and the team sees gaps a flat backlog hides.

## When to use
- A new product, major feature or re-platforming must be planned across the full user journey.
- The backlog is a long flat list and stakeholders cannot see what a release enables.
- A team needs to agree on MVP and following release slices together.

## When not to use
- Only one epic must be decomposed into stories. Use `epic-breakdown`.
- The goal is to understand the customer's current experience, emotions and pains. Use `customer-journey-map`.
- Scope is known and dates, dependencies and confidence must be planned. Use `release-planning`.

## Inputs
Required:
- The product or feature, its primary user(s) and the goal of the journey (from trigger to done).

Optional, improves quality:
- Existing backlog items, personas, journey map, research findings.
- Release goals, time or capacity constraints, known must-haves (legal, contractual).

If the users or journey goal are missing, ask (at most 3 questions). Do not invent release dates or capacity; mark them `[TBD]`.

## Process
1. Fix the frame: primary persona(s), the journey's trigger and definition of done, and the outcome the map should move. Name personas specifically; mark proposed ones `[ASSUMPTION]`.
2. Build the backbone: 4-8 user activities in narrative order (verb phrases from the user's view, e.g. "Submit expense"), then the steps under each activity. Keep it user-centric, not system components.
3. Walk the backbone aloud as a story ("First the employee..., then...") to find missing or misordered steps; add alternate personas' steps where the journey diverges.
4. Under each step, list stories/options as user-visible capabilities, ordered vertically from most essential to nice-to-have. Place existing backlog items here; mark items that fit no step as candidates to drop or reframe.
5. Mark non-functional needs (security, privacy/KVKK/GDPR, accessibility, performance) and operational/support steps as cards where they apply, not as a separate column.
6. Cut release slices horizontally: slice 1 is the thinnest set that lets the persona complete the whole backbone (walking skeleton / MVP); later slices deepen steps. Every slice must touch every activity that the journey requires.
7. Give each slice a named outcome and a measurable signal ("employees submit 80% of receipts in-app" as a target to confirm, not invented baseline).
8. Check each slice for gaps: a step with no card in a slice breaks the journey; either add the simplest option (even manual) or explicitly accept the gap with a reason.
9. Note dependencies, open questions and risks per slice; flag cards needing research or a spike.
10. Label inferred steps and priorities `[ASSUMPTION]`. If the user's goal continues, suggest the next skill: `epic-breakdown` for detailed stories, `mvp-scoping` to challenge slice 1, or `release-planning` to schedule slices.

## Output format
```markdown
# Story Map: <product / journey>
Persona(s): <...> · Trigger: <...> · Done when: <...> · Outcome: <...>

## Backbone
| Activity | <Activity 1> | <Activity 2> | ... |
|---|---|---|---|
| Steps | <step a>, <step b> | <step c> | ... |

## Map (stories under each step, top = most essential)
| Slice | <step a> | <step b> | <step c> | ... |
|---|---|---|---|---|
| Release 1 – <outcome> | <card> | <card> | <card (manual)> | |
| Release 2 – <outcome> | <card> | – | <card> | |
| Later | ... | | | |

## Slice Outcomes and Signals
| Slice | Outcome | Signal / target | Gaps accepted |
|---|---|---|---|

## Cross-Cutting Cards (NFR, support, compliance)
- ...

## Dependencies, Risks and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Backbone activities are user actions in narrative order, not system modules.
- [ ] Release 1 lets the persona complete the whole journey, even if some steps are manual.
- [ ] Every slice has a named outcome and a measurable signal; no baseline is invented.
- [ ] Gaps in any slice are filled or explicitly accepted with a reason.
- [ ] NFR, privacy and support needs appear as cards on the relevant steps.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Backbone made of screens or services ("Login page", "Payment API"). Rewrite as what the user is trying to do.
- Slicing vertically by activity ("Release 1 = submission, Release 2 = approval"). Nobody can finish the journey until the last release; slice horizontally.
- Treating the map as a one-off artifact. Revisit it after each release with feedback and adoption data.

## Example
Input: "B2B expense app, from employee submitting a receipt to finance reimbursing it."

Excerpt of output:
| Slice | Capture receipt | Submit claim | Approve | Reimburse |
|---|---|---|---|---|
| Release 1 – employees get reimbursed without paper | Photo upload | Single-currency claim form | Manager approves by email link | Finance exports approved claims to existing payroll (manual) |
| Release 2 – faster, fewer errors | OCR prefill | Multi-currency, policy warnings | In-app approval with delegation | Direct bank file |
- Weak slice: "Release 1 = receipt capture with OCR, multi-currency" (no one gets reimbursed).
- Open question: Is the payroll export format fixed by the finance system?
