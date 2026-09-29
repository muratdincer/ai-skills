---
name: design-system-component-spec
description: "Specifies a reusable design system component with its purpose, anatomy, variants, sizes, states, design tokens, behavior, content rules, accessibility requirements, usage do's and don'ts, and API/props for implementation. Use when a new component is proposed for the design system, an existing one needs documentation or a breaking change, or teams are building divergent versions of the same pattern."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Specify a design system component"
  related: "design-handoff, wireframe-spec, component-design, accessibility-audit, microcopy"
  prompt: "Write a design system spec for a Toast notification component that web and mobile teams can both implement."
---

# Specify a Design System Component

## Purpose
Define a component once, precisely enough that designers use it consistently and every platform team implements the same anatomy, states, tokens and accessibility behavior.

## When to use
- A new pattern appears in two or more products and should become a shared component.
- An existing component is undocumented, inconsistently implemented or about to change.
- A contribution to the design system must be reviewed before it is accepted.

## When not to use
- You are specifying one feature screen for implementation. Use `design-handoff`.
- You are designing the code-level structure of a front-end component. Use `component-design`.
- You need to audit existing UI for accessibility. Use `accessibility-audit`.

## Inputs
Required:
- The component name and the problem it solves (or examples of where it appears).
- Target platforms (web, iOS, Android, other).

Optional, improves quality:
- Existing token set and naming convention.
- Screenshots or descriptions of current divergent implementations.
- Related components it must coexist with or replace.
- Brand voice guidance for built-in content.

If name, problem or platforms are missing, ask. Other gaps become open questions.

## Process
1. State the component's job in one sentence and when it should be chosen over similar components (e.g. Toast vs. Banner vs. Dialog). Reject the component if an existing one covers the need; record that recommendation.
2. Inventory current usages or examples, noting where they diverge; divergence drives the variant set, not taste.
3. Define the anatomy: numbered parts, which are required and which optional, and nesting rules.
4. Define variants (semantic, e.g. info/success/warning/error) and sizes. Keep each variant justified by a distinct use; drop decorative ones.
5. Define states: default, hover, focus-visible, pressed, disabled, loading, selected, error, and any component-specific states (e.g. auto-dismissing, persistent).
6. Map every part and state to design tokens (color, type, spacing, radius, elevation, motion). Use the team's naming; never invent tokens without marking `[PROPOSED TOKEN]`.
7. Specify behavior: triggers, dismissal, timing, stacking/queuing, overflow and truncation, responsive and RTL behavior, reduced motion.
8. Specify accessibility against WCAG 2.2 and the relevant WAI-ARIA Authoring Practices pattern: role, accessible name, keyboard interaction, focus management, announcements, contrast, target size.
9. Write content rules: length limits, tone, capitalization, what never goes in the component; link to `microcopy`.
10. Write usage guidance as paired do/don't rules, plus the implementation API (props, events, slots) with defaults, and a versioning note for breaking changes.
11. Mark inferences `[ASSUMPTION]` and list open questions with owners.
12. If the goal continues, suggest `component-design` for the code implementation, `design-handoff` for the first feature using it, or `accessibility-audit` after build.

## Output format
```markdown
# Component: <Name>
| Field | Value |
|---|---|
| Status | Proposed / Beta / Stable / Deprecated |
| Platforms | ... |
| Replaces / related | ... |

## Purpose and When to Use
- Use when: ...  - Use instead: <component> when ...

## Anatomy
1. <part> (required/optional) — ...

## Variants and Sizes
| Variant | Use for | Notes |

## States
| State | Visual change | Tokens | Behavior |

## Tokens
| Part | Property | Token |

## Behavior
- Trigger / dismissal / timing / stacking / overflow / RTL / reduced motion

## Accessibility
- Role / name / keyboard / focus / announcement / contrast / target size

## Content Rules
- ...

## Usage
| Do | Don't |

## API
| Prop / event | Type | Default | Description |

## Open Questions and Assumptions
- ...
```

## Quality checklist
- [ ] The spec states when to use a neighboring component instead.
- [ ] Every variant has a distinct use; every state has token mappings.
- [ ] Keyboard, focus, role and announcement behavior are specified.
- [ ] Behavior covers overflow, stacking, RTL and reduced motion.
- [ ] The API has defaults and names consistent across platforms.
- [ ] Proposed tokens and inferences are labeled; nothing is presented as existing that is not.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Specifying visuals only. Components break on behavior (timing, focus, queuing), not color; spec behavior first.
- Variant explosion. Each variant multiplies maintenance; merge those without a distinct use.
- One platform's idioms forced onto all. Keep shared semantics, allow platform-native interaction where guidelines differ, and document it.

## Example
Input: "Toast component for web and mobile; teams currently build their own."

Weak excerpt: "Toast: small popup at the bottom, disappears after a few seconds."

Strong excerpt:
- Use when: brief, non-blocking confirmation of a user action. Use Banner instead for persistent system status; Dialog when a decision is required.
- Behavior: auto-dismiss after `[TBD]` seconds unless it contains an action; timer pauses on hover and focus; max 1 visible, others queue.
- Accessibility: `role="status"` (error variant `role="alert"`); never moves focus; action reachable by keyboard.
