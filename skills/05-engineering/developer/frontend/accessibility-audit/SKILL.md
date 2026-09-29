---
description: Audits a web or mobile UI (page, flow, component, or its markup) against WCAG 2.2 Level A and AA success criteria, records each finding with the criterion, affected users, evidence and severity, and proposes concrete code or design fixes. Use when a screen or component needs an accessibility check before release, after a complaint or legal request, or when someone asks "is this accessible?" or "check this for WCAG".
related: component-design, heuristic-evaluation, design-handoff, microcopy, test-case-writing
prompt: Audit this checkout form markup against WCAG 2.2 AA and tell me what to fix first.
---

# Audit Accessibility (WCAG)

## Purpose
Find the barriers that stop people with disabilities from completing a task, map each one to a WCAG 2.2 success criterion, and give developers a prioritized, fixable list. The output is an audit report that can drive work items and be re-checked after fixes.

## When to use
- A page, flow or component is about to ship and needs an A/AA conformance check.
- A user complaint, customer requirement or legal obligation asks for an accessibility review.
- A design system component must be verified before other teams adopt it.

## When not to use
- Designing a new component's accessibility contract before code exists. Use `component-design`.
- A general usability review against heuristics, not WCAG. Use `heuristic-evaluation`.
- Writing test cases for accessibility regression suites only. Use `test-case-writing`.

## Inputs
Required:
- The UI under audit: markup or code, a URL description with screenshots, or a detailed description of the flow, plus the key user task.

Optional, improves quality:
- Target level (default AA) and any legal or contractual requirement.
- Results from automated checkers, screen reader or keyboard test notes.
- Supported platforms, browsers and assistive technologies; design tokens (colors, focus styles).

If the UI itself is missing, ask for it. If only screenshots are given, state that semantics, names and keyboard behavior are `[UNKNOWN]` and cannot be confirmed.

## Process
1. Define scope: pages or screens, states (default, error, loading, modal open), the critical user task, target level, and what evidence is available (code, screenshots, test notes). Record what could not be checked.
2. Walk the task keyboard-only: reachability of every control, logical focus order, visible focus indicator not hidden by sticky content (2.4.7, 2.4.11), no keyboard trap (2.1.2), and focus management on dialogs and route changes.
3. Check semantics and names: headings and landmarks, native elements before ARIA, every control has an accessible name that includes its visible label (4.1.2, 2.5.3), form fields have programmatic labels and instructions (1.3.1, 3.3.2).
4. Check perceivable content: text alternatives for meaningful images and icons (1.1.1), text contrast 4.5:1 or 3:1 for large text (1.4.3), non-text contrast 3:1 for controls and focus (1.4.11), no information by color alone (1.4.1), reflow at 320 CSS px and 200% text resize (1.4.10, 1.4.4).
5. Check interaction and input: target size at least 24x24 CSS px or sufficient spacing (2.5.8), dragging alternatives (2.5.7), no timing traps (2.2.1), motion and auto-play controls (2.2.2, 2.3.3 if AAA is in scope).
6. Check errors and help: errors identified in text and linked to the field (3.3.1), suggestions (3.3.3), confirmation or reversal for legal or financial submissions (3.3.4), redundant entry avoided (3.3.7), accessible authentication without cognitive tests (3.3.8), consistent help (3.2.6).
7. Check dynamic content: status messages announced without moving focus (4.1.3), live regions used sparingly, content on hover or focus dismissible and persistent (1.4.13).
8. For each finding record: location, criterion number and name, who is affected, evidence (snippet or observed behavior), and whether it is Confirmed or `[ASSUMPTION]` (inferred from a screenshot or partial code).
9. Rate severity by task impact: Blocker (task cannot be completed), High (completed with major effort), Medium, Low. A Level A failure on the critical path is at least High.
10. Propose a concrete fix for each finding: the corrected markup, attribute, token or behavior, preferring native HTML or platform controls over ARIA.
11. Summarize conformance per criterion checked (Pass, Fail, Not applicable, Not tested) and list what needs manual assistive-technology testing.
12. If the user continues, suggest `component-design` to fix a component contract at its source, `test-case-writing` to add regression checks, or `microcopy` for label and error text.

## Output format
```markdown
# Accessibility Audit: <scope>
Target: WCAG 2.2 Level <A/AA> · Evidence: <code / screenshots / AT test> · Date: <date>
Not checked: <items and why>

## Summary
- Blockers: <n> · High: <n> · Medium: <n> · Low: <n>
- Top 3 fixes: ...

## Findings
| # | Location | Criterion | Affected users | Evidence | Severity | Status | Fix |
|---|---|---|---|---|---|---|---|

## Conformance Overview
| Criterion | Result (Pass/Fail/N/A/Not tested) | Note |
|---|---|---|

## Manual Testing Needed
- <screen reader / voice control / zoom scenario>

## Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Every finding cites a specific WCAG 2.2 criterion number and name, and evidence.
- [ ] Each fix is concrete (markup, attribute, token or behavior), not "make it accessible".
- [ ] Severity reflects impact on the critical task, not the criterion's level alone.
- [ ] Items that could not be verified from the evidence are marked `[ASSUMPTION]` or "Not tested".
- [ ] Native elements are preferred over ARIA in proposed fixes.
- [ ] No claim of full conformance is made from automated or screenshot-only evidence.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating an automated checker's clean result as conformance. Automated tools detect only part of the failures; keyboard, focus and name checks need manual review.
- Adding ARIA roles to generic containers instead of using native buttons, links and inputs, which breaks keyboard behavior.
- Reporting contrast issues only for body text and missing focus indicators, icons and input borders (1.4.11).

## Example
Input: "Checkout form: `<div class="btn" onclick="pay()">Pay</div>`, placeholder-only fields, errors shown in red."

Excerpt of output:
| # | Location | Criterion | Affected users | Evidence | Severity | Status | Fix |
|---|---|---|---|---|---|---|---|
| 1 | Pay button | 2.1.1 Keyboard, 4.1.2 Name, Role, Value | Keyboard and screen reader users | `div` with click handler, no role or tabindex | Blocker | Confirmed | Use `<button type="submit">Pay</button>` |
| 2 | Card number field | 3.3.2 Labels or Instructions | Screen reader, cognitive | Placeholder only, disappears on input | High | Confirmed | Add visible `<label for>`; keep format hint in `aria-describedby` |
| 3 | Error state | 1.4.1 Use of Color, 3.3.1 Error Identification | Color-blind users | Red border only | High | `[ASSUMPTION]` from screenshot | Add error text linked via `aria-describedby`, and an icon |
