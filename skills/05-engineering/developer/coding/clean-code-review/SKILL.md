---
description: "Reviews code for maintainability: naming, function size and responsibility, SOLID and coupling, duplication, comments, and recognizable code smells, producing prioritized findings with location, impact and a concrete fix. Use when someone asks whether code is clean, readable or well designed, wants a maintainability review of a file, class or module, or prepares code for handover."
related: "refactoring, code-review, coding-standards, review-comment-writing, code-quality-report"
prompt: "Do a clean code review of this OrderService class; it has grown over two years and new people struggle to change it."
---

# Review for Clean Code

## Purpose
Give a prioritized, actionable maintainability assessment of a piece of code, focused on what makes it expensive to read and change, rather than on personal taste.

## When to use
- A file, class or module feels hard to understand or modify and the team wants specifics.
- Code is being handed over or will be extended significantly.
- A developer wants feedback on design quality beyond "it works".

## When not to use
- A full pull request review including correctness, security and tests. Use `code-review`.
- Applying the improvements. Use `refactoring`.
- Team-wide standards or metrics. Use `coding-standards` or `code-quality-report`.

## Inputs
Required:
- The code under review (file, class or module) and its language.

Optional, improves quality:
- Team coding standards, architecture rules, the upcoming change to this code, known pain points.

If only a fragment is provided, review it and state which conclusions depend on unseen code.

## Process
1. Understand intent first: summarize in 2-3 sentences what the code is responsible for; if you cannot, that is finding number one.
2. Naming: do names reveal intent and domain language; are there misleading names, encodings, vague verbs (`process`, `handle`, `data`)?
3. Functions: size, single level of abstraction, number of parameters, flag arguments, hidden side effects, command-query separation.
4. Classes and modules: single responsibility, cohesion, dependency direction, SOLID violations that actually hurt (not theoretical), law of Demeter, temporal coupling.
5. Duplication: identical and near-identical logic, especially duplicated business rules.
6. Smells: long parameter list, primitive obsession, data clumps, feature envy, switch on type, shotgun surgery, speculative generality, dead code.
7. Comments and error handling from a readability view: comments that restate code or lie, swallowed exceptions, error codes mixed with exceptions.
8. Testability: hard-wired dependencies, static state, time/random/IO not injectable.
9. Rate each finding: Blocker (causes bugs or blocks change), Major (slows change), Minor (readability), Nit (style). Respect existing team conventions over generic rules.
10. For each finding give location, impact, and the concrete fix, preferably a named refactoring with a short before/after.
11. End with strengths and the top 3 actions in order.
12. If the goal continues, suggest `refactoring` to apply the top actions safely or `review-comment-writing` to turn findings into pull request comments.

## Output format
```markdown
# Clean Code Review: <unit>
Responsibility summary: <2-3 sentences>

## Findings
| # | Severity | Location | Finding | Impact | Suggested fix |
|---|---|---|---|---|---|

## Before / After (top findings)
<short code excerpts>

## Strengths
- ...

## Top 3 Actions
1. ...
```

## Quality checklist
- [ ] Every finding cites a location and explains the cost, not just the rule name.
- [ ] Severity reflects impact on change and correctness, not taste.
- [ ] Suggested fixes are concrete and compatible with the language and existing conventions.
- [ ] Findings are deduplicated; systemic issues are stated once with examples.
- [ ] At least one strength is noted where it exists.
- [ ] Inferences are labeled `[ASSUMPTION]` and listed as assumptions or open questions; nothing unsupported is stated as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Dogmatic rule application (e.g. "functions must be under N lines") where the code is actually clear. Judge by readability and change cost.
- Recommending abstractions for one implementation. Speculative generality is itself a smell.
- A long list of nits hiding the one structural problem. Lead with the top 3.

## Example
Input: "OrderService, 900 lines: validation, pricing, persistence, email sending."

Excerpt of output:
| # | Severity | Location | Finding | Impact | Suggested fix |
|---|---|---|---|---|---|
| 1 | Major | `OrderService` | Four responsibilities in one class | Every change risks unrelated behavior; tests need all dependencies | Extract `OrderPricing` and `OrderNotifier`; keep service as orchestrator |
| 2 | Major | `placeOrder(…, boolean sendMail)` | Flag argument | Two behaviors behind one name | Split into `placeOrder` and publish an `OrderPlaced` event for mail |
