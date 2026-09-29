---
description: "Specifies screen or UI requirements per screen: purpose and entry points, roles and permissions, fields with source, format, mandatory rules, defaults and validations with message behavior, actions and their outcomes, screen states (empty, loading, error, read-only, no permission), navigation, accessibility and responsive needs, without prescribing visual design. Use when a screen, form or page must be specified for design and development, or when asked 'what should this screen do'."
related: "wireframe-spec, error-message-writing, frd-writing, data-requirements, accessibility-audit"
prompt: "Specify the screen requirements for the 'Edit customer address' form in the call-center application."
---

# Specify Screen Requirements

## Purpose
Describe what each screen must show, accept and do in every state, so design can focus on layout and interaction, developers implement consistent behavior, and testers know exactly what to verify.

## When to use
- A new screen, form, page or dialog is needed, or an existing one changes.
- Designers have a mock-up, but fields, validations and states are not specified.
- Behavior differs by role or status and must be pinned down before development.

## When not to use
- Layout and visual hierarchy of a wireframe are the focus. Use `wireframe-spec`.
- Only error and help texts need writing. Use `error-message-writing` or `microcopy`.
- Whole-system behavior beyond individual screens is needed. Use `frd-writing`.

## Inputs
Required:
- The screen's purpose and the process step or story it supports.

Optional, improves quality:
- Mock-up or sketch, data requirements, business rules, role matrix, existing screen, design system conventions, accessibility target.

If the purpose or the supported step is missing, ask for it. Ask at most 5 blocking questions at a time; everything else becomes an open question.

## Process
1. State the screen's purpose, the users/roles, entry points (from where and with what context) and exit points.
2. Define permissions per role: view, edit, action availability; state what a user without permission sees.
3. List fields in logical order with label, business meaning, source (data element or calculation), editable or read-only, format and length, mandatory (always or conditional), default and allowed values.
4. Write validations per field and across fields, when they fire (on change, on leave, on submit) and the message behavior; reference business rule IDs.
5. List actions (buttons, links, bulk actions) with precondition, outcome, confirmation need, and what happens on success, failure and double submit.
6. Specify states: initial, empty (no data), loading, partial data, validation error, system error, read-only (e.g. by status), concurrent change detected, no permission.
7. Specify navigation and unsaved-change behavior, pagination/search/sort for lists, and what is remembered between visits.
8. Specify accessibility (WCAG 2.2 AA: labels, keyboard order, error announcement, contrast owner) and device/responsive needs; leave visual styling to design.
9. Note personal data shown on the screen and masking needs (e.g. partially masked phone for agents).
10. List assumptions and open questions with owners; mark inferred behavior `[ASSUMPTION]`.
11. If the goal continues, suggest `wireframe-spec` for layout, `error-message-writing` for the message texts, or `accessibility-audit` once built.

## Output format
```markdown
# Screen Requirements: <screen name> (SCR-<nn>)
Purpose: ... · Supports: <story / use case> · Roles: ...
Entry points: ... · Exit points: ...

## Permissions
| Element / action | Role A | Role B |
## Fields
| # | Label | Meaning / source | Editable | Format | Mandatory | Default / values | Validation (when) | Message behavior |
## Actions
| Action | Precondition | Success outcome | Failure outcome | Confirmation |
## States
| State | Condition | What the user sees / can do |
## Navigation and Persistence
## Accessibility and Devices
## Personal Data and Masking
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every field has source, editability, mandatory rule and validation with timing.
- [ ] Every action has precondition, success and failure outcomes, and double-submit behavior.
- [ ] Empty, loading, error, read-only and no-permission states are specified.
- [ ] Role-based differences are explicit.
- [ ] Accessibility target and personal data masking are addressed.
- [ ] No visual styling is prescribed; inferred behavior is labeled `[ASSUMPTION]`.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Specifying only the filled-in happy state. Empty, error and read-only states are where users get stuck; specify them.
- Mixing layout with behavior ("red text under the field"). Specify the message trigger and content; design decides the presentation.
- Validations only on submit for long forms. Decide timing per field so users are not surprised by ten errors at once.

## Example
Input: "Call-center agents edit a customer's address; addresses of customers with an open delivery need care."

Excerpt of output:
| # | Label | Meaning / source | Editable | Mandatory | Validation (when) |
|---|---|---|---|---|---|
| 3 | Postal code | Customer.address.postalCode | Yes | Yes | Valid for the selected city (on leave) `[TBD: reference source]` |
| 4 | District | Customer.address.district | Yes | Yes | Must belong to the selected city (on change of city: reset) |

| State | Condition | What the user sees / can do |
|---|---|---|
| Open delivery | Customer has a delivery not yet dispatched | Warning that the change affects the delivery; agent chooses "apply to delivery" or "future only" `[ASSUMPTION]` |
| Read-only | Agent role without edit permission | Address shown with phone partially masked; no Save action |

Open question: May agents change the address while a delivery is already dispatched? — Logistics
