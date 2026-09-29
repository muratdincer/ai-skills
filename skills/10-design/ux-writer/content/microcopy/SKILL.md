---
name: microcopy
description: "Writes interface microcopy such as button and link labels, form labels, helper text, placeholders, tooltips, empty states, confirmations and success messages, fitted to the user's task, the product's voice, length limits and localization. Use when a screen or flow needs its UI text written or improved, when labels are vague or inconsistent, or when someone asks \"what should this button say\"."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 10-design
  role: ux-writer
  area: content
  title: "Write microcopy"
  related: "error-message-writing, voice-and-tone-guide, design-handoff, style-guide-check, glossary-builder"
  prompt: "Write the microcopy for our new \"invite teammates\" dialog: title, field labels, helper text, buttons and the empty state."
---

# Write Microcopy

## Purpose
Give every interface element text that tells users what it is and what will happen, in as few words as clarity allows, consistent with the product's voice and terminology.

## When to use
- A new screen, dialog or flow needs its UI text.
- Existing labels are vague ("Submit", "OK"), inconsistent or cause support questions.
- Empty states, onboarding hints or confirmations need to guide the next action.

## When not to use
- The text is an error or validation message. Use `error-message-writing`.
- You need the product's overall voice principles. Use `voice-and-tone-guide`.
- You are checking long-form documentation against a style guide. Use `style-guide-check`.

## Inputs
Required:
- The screen or flow context: what the user is trying to do and the elements needing text (a list, wireframe or screenshot description).

Optional, improves quality:
- Voice and tone guide, glossary, capitalization rules.
- Character limits, platforms, target languages.
- Current copy and known user confusion (support tickets, test findings).

If the context or element list is missing, ask for it. Everything else becomes an open question.

## Process
1. Identify the user's goal on this screen and the single primary action. The primary action's label names the outcome ("Send invites"), not the mechanism ("Submit").
2. List every element needing text: title, labels, helper text, placeholders, buttons, links, tooltips, empty states, confirmations, success messages.
3. Use the product's terms from the glossary; if none exists, pick one term per concept and keep it everywhere (never alternate "workspace"/"project"). Flag new terms `[NEW TERM]`.
4. Write labels as short noun phrases and buttons as verb + object. Pair buttons so the choice is clear without reading the body ("Delete file" / "Keep file", not "Yes" / "No").
5. Keep required guidance out of placeholders; placeholders vanish on input and fail accessibility. Put format rules in helper text.
6. For empty states, write what this area is for, why it is empty, and the next action; distinguish first use, no results and cleared states.
7. For confirmations of destructive actions, state the object and the consequence, and whether it can be undone.
8. Front-load the key word, use sentence case unless the style guide says otherwise, avoid jargon, double negatives and blame, and check against length limits. Allow roughly 30-40% expansion for localization and avoid concatenated strings.
9. Check accessibility: link and button text makes sense out of context; icon-only buttons have accessible names; nothing relies on color or position ("click the green button").
10. Provide one recommended option per element, with an alternative only where a real trade-off exists, and a one-line rationale for non-obvious choices. Label any assumption about user intent `[ASSUMPTION]`.
11. If the goal continues, suggest `error-message-writing` for failure paths, `voice-and-tone-guide` if voice is undefined, or `design-handoff` to attach the strings to specs.

## Output format
```markdown
# Microcopy: <screen / flow>
User goal: <one line>  ·  Primary action: <label>

| Key | Element | Copy | Chars | Rationale / note |
|---|---|---|---|---|
| invite.title | Dialog title | ... | .. | ... |
| invite.email.label | Field label | ... | .. | ... |
| invite.email.help | Helper text | ... | .. | ... |
| invite.cta.primary | Primary button | ... | .. | ... |

## Empty / Confirmation / Success States
| State | Title | Body | Action |

## Terminology Used
- <term>: <meaning> [NEW TERM if not in glossary]

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] The primary button names the outcome, and paired buttons are distinguishable without context.
- [ ] One term per concept, consistent with the glossary; new terms flagged.
- [ ] No essential instruction lives only in a placeholder.
- [ ] Every empty state gives a reason and a next action.
- [ ] Strings fit limits, allow localization expansion and are not concatenated.
- [ ] Link, button and icon names make sense to a screen-reader user out of context.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing clever instead of clear. Humor in the primary path slows users and translates badly; save personality for low-stakes moments.
- Generic labels ("Submit", "Continue", "OK"). Name what happens.
- Copy written per screen without a shared term list, so the same thing gets three names across the product.

## Example
Input: "Invite teammates dialog: email field, role selector, send button, and an empty state when no one is invited yet."

Weak: Button "Submit" · Placeholder "Enter emails separated by commas" · Empty state "Nothing here."

Strong:
| Element | Copy |
|---|---|
| Field label | Email addresses |
| Helper text | Separate multiple addresses with commas. |
| Primary button | Send invites |
| Empty state | No teammates yet. Invite people to share projects and assign tasks. [Invite teammates] |
