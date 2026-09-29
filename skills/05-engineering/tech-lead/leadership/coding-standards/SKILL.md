---
description: Writes or revises a team's coding standards as a short set of numbered rules, each with rationale, a good and a bad example, a severity (must or should) and how it is enforced (formatter, linter, review, test), focusing on decisions that tools cannot settle. Use when a team is forming or merging, reviews keep arguing about the same style or design questions, a new language or framework is adopted, or existing standards are too long, outdated or ignored.
related: clean-code-review, code-review, review-comment-writing, working-agreement, adr
prompt: Write coding standards for our backend team. We keep arguing in reviews about exception handling, naming and how big a pull request should be.
---

# Write Coding Standards

## Purpose
Give the team a small, enforceable set of conventions that removes recurring debates from code review and makes code look like one team wrote it. Every rule carries its reason, so people can apply it to cases the rule did not foresee.

## When to use
- A new team, repository or language needs agreed conventions.
- Reviews repeatedly debate the same topics (naming, error handling, test style, PR size).
- Existing standards are long, outdated, contradicted by the codebase, or not followed.

## When not to use
- Reviewing a specific change against clean code principles. Use `clean-code-review` or `code-review`.
- Team working norms beyond code (meetings, availability, on-call). Use `working-agreement`.
- A single significant architectural decision. Use `adr`.

## Inputs
Required:
- The language(s) and scope (repository, service, team), and the pain points or topics the standards must settle.

Optional, improves quality:
- Current standards, linter and formatter configuration, examples of contested review threads.
- Architecture style and layering rules, testing approach, security requirements.
- Team size and experience mix, regulatory or customer constraints.

If the language or scope is missing, ask. Ask at most five focused questions about the contested topics; turn anything unanswered into a proposed rule marked `[PROPOSAL]` for team discussion.

## Process
1. Collect the topics: contested review themes, recurring defects, onboarding questions. Rank by how often they cost review time or cause bugs.
2. Delegate to tools first: anything a formatter or linter can enforce (formatting, import order, simple naming patterns, complexity limits) becomes a tool rule with a reference to the config, not prose.
3. Adopt a widely used community style guide for the language as the baseline instead of re-deriving it; list only the team's deviations and additions.
4. Write the remaining rules for judgment topics: naming and domain language, error handling and logging, module boundaries and dependencies, null and optional handling, concurrency, testing conventions, comments and documentation, security-sensitive patterns (input validation, secrets, SQL), PR size and commit conventions.
5. Give each rule an ID, a one-line imperative statement, severity (Must: blocks merge / Should: default, deviate with a reason), rationale in one or two sentences, and a bad and a good example in the team's language.
6. Define enforcement per rule: formatter, linter rule, static analysis, architecture test, CI check, or review. Rules enforced only by review should be few.
7. Check the set for conflicts with each other, with the existing codebase (how much would violate it) and with frameworks in use; add a migration note (new code only, or boy-scout rule on touched code) rather than demanding a mass rewrite.
8. Keep it short: aim for a document the team reads in about ten minutes; move rare details to linked pages.
9. Define the change process: who can propose changes, how decisions are made, and how exceptions are recorded (inline suppression with reason).
10. Mark inferred rules `[PROPOSAL]` and list open decisions for the team. If the user continues, suggest `working-agreement` to adopt the standards formally, `clean-code-review` to review code against them, or `adr` for significant decisions within them.

## Output format
```markdown
# Coding Standards: <team / repository>
Scope: <languages, repos> · Baseline: <community style guide> · Owner: <name or [UNKNOWN]> · Version: <n>

## Enforced by Tools
| Area | Tool / config | Notes |
|---|---|---|

## Rules
### <ID> <Imperative rule statement> (Must/Should)
Why: <rationale>
Bad:
    <code>
Good:
    <code>
Enforced by: <linter rule / architecture test / review>

## Adoption
- Applies to: <new code / touched code> · Exceptions: <how recorded>

## Changing These Standards
- ...

## Open Decisions
- [PROPOSAL] ...
```

## Quality checklist
- [ ] Every rule has an ID, severity, rationale and a bad/good example.
- [ ] Anything a tool can enforce is delegated to a tool, not written as prose.
- [ ] Rules do not contradict each other or the chosen baseline guide.
- [ ] Each Must rule has an enforcement mechanism other than memory.
- [ ] Rules inferred rather than agreed are marked `[PROPOSAL]` and appear in open decisions.
- [ ] The document is short enough to read in about ten minutes.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a long style manual about formatting. Formatters settle that for free; spend words on design and error-handling rules.
- Rules without rationale ("Do not use X"). People follow reasons, and reasons help decide the unforeseen cases.
- Standards that the existing codebase violates everywhere with no adoption plan; they are ignored within weeks.

## Example
Input: "Backend team, arguments about exceptions, naming, PR size."

Weak rule: "Handle exceptions properly."

Strong rule:
### ERR-2 Do not catch an exception unless you can handle it or add context (Must)
Why: swallowed or re-wrapped-without-context exceptions hide root causes and break alerting.
Bad:
    try { charge(order) } catch (e) { log.warn("error") }
Good:
    try { charge(order) } catch (e: GatewayTimeout) { throw PaymentFailed(orderId = order.id, cause = e) }
Enforced by: static analysis rule for empty or log-only catch blocks; review for context.
