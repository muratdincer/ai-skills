---
name: component-design
description: "Designs the technical API of a UI component before implementation: responsibility, props or inputs, internal and controlled state, events, slots or composition points, variants, visual and interaction states, accessibility semantics and keyboard behavior, and test cases, in a framework-neutral form. Use when a developer is about to build or refactor a reusable component, a design handoff must be turned into a component contract, or a component has grown too many props."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 05-engineering
  role: developer
  area: frontend
  title: "Design a UI component"
  related: "design-system-component-spec, accessibility-audit, state-management-design, unit-test-writing, design-handoff"
  prompt: "Design the component API for a searchable select (combobox) we will reuse across our admin screens. It needs async options and multi-select."
---

# Design a UI Component

## Purpose
Agree on a component's contract before code is written, so it is reusable, accessible and testable, and does not collapse into a prop-flag monster. The output is a component specification developers can implement and reviewers can check against.

## When to use
- A new reusable component is about to be built for a product or design system.
- A designer's handoff shows a component and developers need its technical API.
- An existing component has become hard to use (many boolean props, unclear state ownership) and needs a redesign.

## When not to use
- The design-system level specification with visual tokens and usage guidance for designers. Use `design-system-component-spec`.
- Deciding where application-wide or server data lives. Use `state-management-design`.
- Checking an implemented UI against WCAG. Use `accessibility-audit`.

## Inputs
Required:
- What the component must do: a design, screenshot description, user story or a list of use cases.

Optional, improves quality:
- UI framework and styling approach, existing design system components and naming conventions.
- Known consumers (screens) and their differing needs.
- Design tokens, supported locales, directionality (LTR/RTL), browsers and devices.

If use cases are missing, ask for the two or three main screens where it will be used. Mark any requirement you inferred from the design as `[ASSUMPTION]`.

## Process
1. State the single responsibility in one sentence and list the use cases it must support and those it deliberately does not (to avoid scope creep).
2. Check for an existing native element or design-system component, or a well-known ARIA Authoring Practices pattern (e.g., combobox, dialog, tabs, disclosure) that the component should follow; name the pattern.
3. Split into composition parts if the component has distinct regions (trigger, list, item, footer); prefer composition (children, slots, render functions) over configuration flags when consumers need to vary content.
4. Define the props or inputs: name, type, required or optional, default, and constraints. Replace clusters of booleans with a single enumerated variant or size prop, and keep impossible combinations unrepresentable.
5. Decide state ownership: which state is internal, which can be controlled by the parent (value/on-change pairs, open/on-open-change), and which is derived. Support controlled and uncontrolled use only where consumers need both.
6. Define events or callbacks with payloads and timing (on change vs on commit, debounce for async search), and cancellation of stale async results.
7. Enumerate visual and interaction states: default, hover, focus-visible, active, disabled, read-only, loading, empty, error, and overflow (long text, many items, narrow width, RTL).
8. Specify accessibility: role and accessible name source, relationships (labelled-by, described-by, controls, active-descendant), keyboard interaction table, focus management on open and close, announcements for async changes, target size and contrast per WCAG 2.2.
9. Note performance and resilience: large lists (virtualization threshold `[ASSUMPTION]` unless given), memoization boundaries, error display for failed loads, and no layout shift on loading.
10. Write test cases: behavior tests per use case, keyboard-only tests, screen reader name and state checks, and edge cases (empty, error, slow network).
11. List open questions for design and product, then suggest `design-system-component-spec` if the component joins a design system, `state-management-design` if state crosses screens, or `unit-test-writing` for the tests.

## Output format
```markdown
# Component: <Name>
Responsibility: <one sentence> · Pattern: <native element / ARIA pattern>
Out of scope: ...

## Anatomy / Composition
- <Part> — <role>

## API
| Prop / input | Type | Default | Required | Notes / constraints |
|---|---|---|---|---|
| Event | Payload | When fired | Notes |
|---|---|---|---|

## State Ownership
- Internal: ... · Controllable: ... · Derived: ...

## States and Variants
| State / variant | Visual | Behavior |
|---|---|---|

## Accessibility
- Role / name: ... · Keyboard: | Key | Action | · Focus: ... · Announcements: ...

## Test Cases
- ...

## Open Questions and Assumptions
- ...
```

## Quality checklist
- [ ] The component has one responsibility and an explicit out-of-scope list.
- [ ] No cluster of boolean props allows contradictory combinations; variants are enumerated.
- [ ] State ownership is explicit for every piece of state (internal, controllable, derived).
- [ ] Keyboard interaction, focus management and accessible names are specified and match the named pattern.
- [ ] Loading, empty, error and overflow states are defined, not only the default.
- [ ] Inferred requirements are marked `[ASSUMPTION]` and listed as open questions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Adding a prop per consumer request until the component has dozens of flags. Use composition and variants instead.
- Rebuilding native controls with generic containers and click handlers. Start from the native element or the ARIA pattern and keep its keyboard behavior.
- Designing only the happy state. Async components fail, load slowly and return nothing; design those states first.

## Example
Input: "Searchable select for admin screens, async options, multi-select."

Weak: "Props: `isMulti`, `isAsync`, `isSearchable`, `isClearable`, `isLoading`, `options`, `onChange`."

Strong excerpt:
- Pattern: ARIA combobox with listbox popup; multi-select shows chosen items as removable chips.
- API: `value: Option[]` + `onValueChange(Option[])` (controllable); `loadOptions(query, signal) => Promise<Option[]>`; `selectionMode: "single" | "multiple"`.
- Behavior: search debounced `[ASSUMPTION: 250 ms, confirm with design]`; stale responses are aborted via `signal`.
- Keyboard: Down opens list and moves active option; Enter selects; Escape closes and returns focus to the input; Backspace on empty input removes the last chip.
- States: loading ("Searching..." announced politely), empty ("No results for ..."), error with retry.
