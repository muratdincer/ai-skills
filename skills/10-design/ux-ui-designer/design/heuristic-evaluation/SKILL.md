---
description: Runs a heuristic evaluation of a product, flow or screens against Nielsen's 10 usability heuristics, producing located findings with the violated heuristic, evidence, a 0-4 severity rating and a concrete recommendation, plus a prioritized summary. Use when a quick expert usability review is needed before or instead of user testing, when someone asks "what's wrong with this UI", or to audit screenshots, prototypes or a live flow.
related: usability-test-script, accessibility-audit, design-critique, research-synthesis, user-flow
prompt: Do a heuristic evaluation of our expense submission flow; screenshots of the 4 screens are attached.
---

# Run a Heuristic Evaluation

## Purpose
Find usability problems quickly and cheaply by inspecting the interface against established heuristics, and rank them by severity so the team fixes what hurts users most before investing in testing or release.

## When to use
- A prototype or live flow needs an expert review before user testing or launch.
- There is no budget or time for user research, and a structured review is still needed.
- A competitor or legacy product must be benchmarked for usability issues.

## When not to use
- The goal is conformance with accessibility standards. Use `accessibility-audit`.
- Feedback is wanted on a design in progress against its goals, in a team review. Use `design-critique`.
- Evidence from real users is required for the decision. Use `usability-test-script`.

## Inputs
Required:
- The interface to evaluate (screenshots, prototype description, screen list or live flow description) and its primary users and tasks.

Optional, improves quality:
- User flow, known complaints or analytics, platform conventions, design system, scope limits.

If the interface or its main tasks are missing, ask for them. If only part of the flow is visible, evaluate what is visible and list the rest as not evaluated.

## Process
1. Define scope: users, 3-5 key tasks, screens and states in scope, platform; state what is excluded.
2. Walk each task step by step as the target user; note every point of hesitation, surprise or extra effort. Evaluate only what is visible or described; mark inferred behavior as `[ASSUMPTION]`.
3. Inspect against the 10 heuristics: visibility of system status; match with the real world; user control and freedom; consistency and standards; error prevention; recognition rather than recall; flexibility and efficiency; aesthetic and minimalist design; help users recognize, diagnose and recover from errors; help and documentation.
4. Record each finding once, at its location, with the violated heuristic(s), what happens, why it matters for the task, and evidence (screen, element, quote of label).
5. Rate severity 0-4 (0 not a problem, 1 cosmetic, 2 minor, 3 major, 4 catastrophe/blocker) based on frequency, impact and persistence; explain the rating in one line.
6. Write a concrete recommendation per finding (what to change, not only "improve clarity"); note effort as S/M/L if estimable.
7. Record positive findings worth keeping, so fixes do not break them.
8. Merge duplicates, group findings by task or screen, and sort by severity.
9. State limitations: single evaluator bias (recommend 3-5 evaluators for coverage), no real-user data, unseen states.
10. Summarize the top issues and suggest `usability-test-script` to validate major findings with users or `accessibility-audit` for WCAG coverage.

## Output format
```markdown
# Heuristic Evaluation: <product / flow>
Scope: <tasks, screens, platform> · Evaluator(s): <...> · Out of scope: <...>

## Summary
- Findings: <n> (4: x, 3: y, 2: z, 1: w)
- Top issues: 1) ... 2) ... 3) ...

## Findings
| # | Location | Heuristic | Issue | Evidence | Severity (0-4) | Recommendation | Effort |
|---|---|---|---|---|---|---|---|

## Strengths to Keep
- ...

## Limitations and Open Questions
- ...
```

## Quality checklist
- [ ] Each finding has a location, heuristic, evidence and a concrete recommendation.
- [ ] Severity ratings follow the 0-4 scale and each rating is justified.
- [ ] Findings are about users' task success, not personal taste.
- [ ] Duplicates are merged and the list is sorted by severity.
- [ ] Unseen screens or states are listed as not evaluated rather than guessed.
- [ ] Limitations (evaluator count, no user data) are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Listing violations without a recommendation. Each finding must state what to change.
- Rating everything major. Use frequency, impact and persistence to differentiate.
- Treating the evaluation as user evidence. Present it as expert judgment and validate major issues with users.

## Example
Input: 4 screenshots of an expense submission flow.

Weak finding: "Form is confusing. Heuristic 2. Severity 3."
Strong finding: "Screen 2, 'Cost center' field: expects a code (e.g. 4410) with no list or hint; users must recall it from another system. Heuristic: recognition rather than recall. Severity 3: every submission, blocks non-finance staff. Recommendation: searchable dropdown with name + code, default to the user's own cost center. Effort: M."
