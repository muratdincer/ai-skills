---
description: Describes a wireframe in text for one screen or view, covering purpose, layout regions, components, content priority, interactions, all states (default, loading, empty, error, partial, permission), responsive behavior and accessibility notes. Use when a screen must be defined before or instead of visual mockups, when someone asks "what goes on this screen", or when a wireframe must be reviewable by product and engineering in text.
related: user-flow, information-architecture, screen-requirements, design-handoff, microcopy
prompt: Describe a wireframe for the order history screen of our e-commerce web app, including empty and error states.
---

# Describe a Wireframe

## Purpose
Specify what a screen contains, in what priority and in which states, without visual styling, so stakeholders can agree on structure and behavior early and designers and developers build the same thing.

## When to use
- A user flow is agreed and each screen now needs structure.
- A screen must be discussed or reviewed in text (documents, tickets, async review).
- An existing screen is being redesigned and content priority must be reset.

## When not to use
- The step sequence across screens is not defined yet. Use `user-flow`.
- The need is field-level functional requirements for developers. Use `screen-requirements`.
- The design is final and needs specs for build. Use `design-handoff`.

## Inputs
Required:
- The screen's purpose: which user, which task or step in the flow.

Optional, improves quality:
- User flow, data available on the screen, business rules, design system components, platforms and breakpoints, existing screen and its analytics.

If the screen's user and task are missing, ask for them. Unknown data fields or rules become `[ASSUMPTION]` or open questions.

## Process
1. State the screen's user, primary task, entry points and the single most important action (primary CTA).
2. Rank content and actions by priority (must see first, secondary, on demand) based on the task; justify the top three.
3. Define layout regions (header, navigation, main, side, footer) and place content by priority in reading order; keep it grid-agnostic and style-free.
4. For each region, list components (preferably design system names), their content and data source, and labels or `[copy TBD]`.
5. Describe interactions: what each control does, feedback, navigation targets, validation timing, destructive-action confirmation.
6. Specify states: default, loading (skeleton vs. spinner), empty (first use vs. no results vs. cleared), error (full page vs. inline), partial data, permission-restricted, offline, long content and truncation.
7. Define responsive behavior per breakpoint: what reflows, collapses, hides or moves; touch targets on mobile.
8. Add accessibility notes: heading structure, focus order, landmarks, labels for icon buttons, error announcement, contrast needs; reference WCAG 2.2 AA where it applies.
9. Render a low-fidelity text or ASCII sketch of the default state if helpful, labeled as illustrative.
10. List assumptions and open questions; suggest `microcopy` for the texts and `design-handoff` once visuals are final.

## Output format
```markdown
# Wireframe: <screen name>
User: <...> · Task: <...> · Entry: <...> · Primary action: <...>

## Content Priority
1. <item> — why
2. ...

## Layout
| Region | Components | Content / data | Notes |
|---|---|---|---|

## Interactions
| Element | Action | Result / feedback |
|---|---|---|

## States
| State | Trigger | What the user sees | Action offered |
|---|---|---|---|
| Loading | ... | ... | ... |
| Empty (first use) | ... | ... | ... |
| Error | ... | ... | ... |

## Responsive Behavior
- <breakpoint>: ...

## Accessibility Notes
- ...

## Sketch (illustrative)
<ASCII or text sketch>

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] The screen has one clear primary action and a justified content priority.
- [ ] Every data element has a source or is marked `[ASSUMPTION]`.
- [ ] Loading, empty, error, partial and permission states are specified.
- [ ] Responsive changes are defined for each target breakpoint.
- [ ] Focus order, headings and labels for non-text controls are covered.
- [ ] The spec contains no visual styling decisions (colors, fonts) beyond structure.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Specifying only the "full data" state. Empty and error states are where users get stuck.
- Giving every element equal weight. Force a ranking; the screen can have only one primary action.
- Writing placeholder lorem ipsum. Use realistic content lengths or mark copy `[TBD]` to expose truncation issues.

## Example
Input: "Order history screen for our e-commerce web app, with empty and error states."

Excerpt of output:
- Primary action: open an order to track or return it.
- Priority: 1) recent orders with status, 2) search/filter by date and status, 3) reorder.
- Empty (first use): "You haven't ordered yet" + link to continue shopping. Empty (no results): "No orders match these filters" + clear filters.
- Error: inline banner "We couldn't load your orders" + retry; cached list shown if available `[ASSUMPTION]`.
