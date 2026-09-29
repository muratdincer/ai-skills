---
description: Prepares a developer-ready design handoff for a screen, flow or feature, covering layout and spacing specs, design tokens, component mapping, interactions and motion, all edge states, responsive rules, accessibility annotations, content and assets, plus open decisions. Use when a design is approved and moves to implementation, when developers ask "what exactly should this do", or when a handoff note must accompany mockups or a design file.
related: wireframe-spec, design-system-component-spec, user-flow, microcopy, acceptance-criteria
prompt: Prepare a design handoff for the new checkout payment step so the web team can start building it next iteration.
---

# Prepare a Design Handoff

## Purpose
Turn an approved design into a complete, unambiguous implementation brief so developers build what was designed without guessing states, spacing, behavior or content, and so QA can verify it.

## When to use
- A screen, flow or feature design is approved and about to be implemented.
- Developers repeatedly ask about behavior, states or measurements not visible in mockups.
- A design changes an existing component or introduces a new pattern that must be flagged.
- An outsourced or distributed team needs a self-contained spec.

## When not to use
- The structure of the screen is still being decided. Use `wireframe-spec`.
- A reusable component is being defined for the design system. Use `design-system-component-spec`.
- You need feedback on design quality. Use `design-critique`.

## Inputs
Required:
- The design to hand off: mockup description, design file export, screenshots or a detailed wireframe.
- The target platform(s): web, iOS, Android, desktop.

Optional, improves quality:
- Design system name and token set; existing component library.
- User flow, requirements or user stories the design implements.
- Breakpoints, supported devices and browsers, localization languages.
- Analytics events to track.

If the design or platform is missing, ask for it. Everything else becomes an open question.

## Process
1. Restate the scope: which screens, flow steps and platforms the handoff covers, and which requirement or story each implements. Anything outside is listed as out of scope.
2. Map every visible element to an existing design-system component and variant. Flag each deviation or new component as `[NEW]` or `[DEVIATION]` with the reason; do not silently fork components.
3. Specify layout: grid, regions, alignment and spacing using tokens (e.g. `space-300`), not raw pixels, wherever tokens exist. Where only pixel values are known, give them and mark `[NO TOKEN]`.
4. Specify visual tokens per element: color, typography, elevation, radius, iconography. Never invent token names; if the token set is unknown, mark `[UNKNOWN]`.
5. Describe interactions for each interactive element: trigger, response, navigation target, focus movement, disabled conditions, and motion (duration, easing, reduced-motion fallback).
6. Enumerate states for each screen and component: default, hover, focus, active, disabled, loading, empty, partial, error, success, offline, permission-denied, long content and truncation. Every state is either specified or explicitly listed as `[TBD]`.
7. Define responsive behavior per breakpoint: what reflows, hides, stacks or changes component.
8. Add accessibility annotations against WCAG 2.2: reading and focus order, accessible names and roles, heading levels, contrast pairs, target size, error announcement, keyboard paths.
9. Collect content: final strings with keys, dynamic values and their limits, pluralization, and localization expansion. Point unfinished copy to `microcopy` or `error-message-writing`.
10. List assets (icons, illustrations, images) with format, sizes, density variants and alt text, plus analytics events if given.
11. Derive verifiable acceptance checks from the states and interactions, and list open decisions with owner. Separate what the design shows from what you inferred; label inferences `[ASSUMPTION]`.
12. If the goal continues, suggest `acceptance-criteria` to formalize checks, `design-system-component-spec` for any `[NEW]` component, or `microcopy` for missing copy.

## Output format
```markdown
# Design Handoff: <feature / screen>
| Field | Value |
|---|---|
| Platforms / breakpoints | ... |
| Implements | <story / requirement IDs> |
| Design source | <file / version / link or [UNKNOWN]> |
| Design system | <name / version or [UNKNOWN]> |

## Scope
- In scope: ...  - Out of scope: ...

## Component Mapping
| Element | Component / variant | Status (existing / [NEW] / [DEVIATION]) | Note |

## Layout and Tokens
| Region / element | Spacing | Color | Type | Other |

## Interactions and Motion
| Element | Trigger | Behavior | Focus / navigation | Motion |

## States
| Screen / component | State | Visual change | Content | Behavior |

## Responsive Rules
| Breakpoint | Changes |

## Accessibility (WCAG 2.2)
- Focus order: ...  - Names / roles: ...  - Contrast: ...  - Announcements: ...

## Content
| Key | String | Max length / dynamic value | Note |

## Assets and Analytics
- ...

## Acceptance Checks
- [ ] ...

## Open Decisions and Assumptions
1. <decision> — <owner> — <needed by>
```

## Quality checklist
- [ ] Every element maps to a component or is flagged `[NEW]` / `[DEVIATION]`.
- [ ] Every screen has loading, empty, error and long-content states specified or marked `[TBD]`.
- [ ] Values use design tokens where they exist; no token names are invented.
- [ ] Every interactive element has keyboard, focus and accessible-name notes.
- [ ] Acceptance checks are observable by QA without asking the designer.
- [ ] Inferences are labeled `[ASSUMPTION]` and open decisions have owners.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Handing off only the happy path. Most rework comes from missing error, empty and overflow states; enumerate them per screen.
- Redlining raw pixels when tokens exist. It breaks theming and drifts from the system; reference tokens.
- Leaving behavior implicit in a prototype. Write it down; prototypes do not show timing, validation or focus rules.

## Example
Input: "Checkout payment step, web only, card form plus saved cards list, uses our DS."

Weak excerpt: "Card form as in mockup. Show error if invalid."

Strong excerpt:
| Screen / component | State | Visual change | Content | Behavior |
|---|---|---|---|---|
| Card number field | error | border `color-border-danger`, icon | "Check the card number" `[copy TBD]` | Validate on blur, announce via live region, focus stays |
| Saved cards list | empty | list hidden | — | Card form expanded by default `[ASSUMPTION]` |
| Pay button | loading | spinner, label kept | — | Disabled, prevents double submit |
