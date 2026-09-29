---
description: "Reviews requirements, user stories or acceptance criteria for testability and flags items that are ambiguous, unmeasurable, incomplete, untestable or missing error behavior, with a concrete rewrite suggestion for each. Use before test design or estimation, in refinement sessions, or when someone asks whether requirements are clear enough to test."
related: ambiguity-detection, acceptance-criteria, requirements-review-checklist, test-scenarios-from-requirements, nfr-specification
prompt: "Check these 8 user stories for testability before we start writing test cases."
---

# Review Requirements for Testability

## Purpose
Catch requirements that cannot be verified before anyone designs tests or writes code, and turn each finding into a concrete question or rewrite so that the expected behavior becomes checkable.

## When to use
- Requirements, stories or acceptance criteria are about to be refined, estimated or tested.
- Testers keep discovering "what should happen here?" questions during execution.
- Non-functional requirements use words like "fast", "secure", "user-friendly".

## When not to use
- You need a general linguistic ambiguity scan for a whole document. Use `ambiguity-detection`.
- You need to write the acceptance criteria from scratch. Use `acceptance-criteria`.
- You need a full document review against a standard checklist. Use `requirements-review-checklist`.

## Inputs
Required:
- The requirements, stories or acceptance criteria text.

Optional, improves quality:
- Domain glossary, business rules, UI mockups, related NFRs.
- Known constraints (roles, data volumes, integrations).

If the requirement text is missing, ask for it.

## Process
1. Number each requirement or criterion so that findings can reference it.
2. Check each item against testability criteria: observable outcome, measurable threshold, defined inputs and preconditions, defined actor/role, single behavior (atomic), no internal contradiction.
3. Flag vague terms: fast, easy, appropriate, etc., some, all (unbounded), should (optional?), as needed, user-friendly, secure.
4. Check for missing behavior: error and validation cases, empty/null data, limits (max length, size, count), concurrency, permissions, time zones and dates, localization.
5. Check NFRs for metric, target, measurement condition (e.g. p95 latency under stated load) and verification method.
6. Check dependencies on unstated rules or external systems whose behavior is not specified.
7. Classify each finding: Ambiguous, Unmeasurable, Incomplete, Untestable (no observable result), Conflicting, Missing negative path.
8. Rate severity by how much it blocks test design: Blocker, Major, Minor.
9. Propose a rewrite or a precise question for each finding. Mark proposed thresholds `[ASSUMPTION]`; never present them as agreed.
10. Summarize: testability score per item (Testable / Testable with questions / Not testable) and top questions for the product owner.

## Output format
```markdown
# Testability Review: <scope>
Summary: <n> items reviewed · <n> testable · <n> need clarification · <n> not testable

| # | Requirement (short) | Finding type | Severity | Issue | Suggested rewrite / question |
|---|---|---|---|---|---|

## Missing Scenarios to Specify
- <item #>: <missing error, limit or permission behavior>

## Questions for the Product Owner (by priority)
1. ...
```

## Quality checklist
- [ ] Every finding references a specific item and quotes the problematic phrase.
- [ ] Every finding has a rewrite or a concrete question.
- [ ] Proposed numbers are marked `[ASSUMPTION]`.
- [ ] Negative paths, limits and permissions were checked for every item.
- [ ] Findings concern verifiability, not solution preference.

## Common pitfalls
- Flagging style instead of testability. Only raise what changes whether a test can decide pass/fail.
- Proposing solutions (UI design) in the rewrite. Specify observable behavior only.
- Missing implicit NFRs, e.g. a list screen with no stated data volume or paging behavior.

## Example
Input: "US-3: As a user I can search customers quickly and see relevant results."

Excerpt of output:
| 3 | Search customers | Unmeasurable + Ambiguous | Blocker | "quickly" and "relevant" have no criteria | "Given 1M customers, search by name prefix (min 3 chars) returns first page (20 rows) within 1 s at p95 `[ASSUMPTION]`; results sorted by exact match first, then alphabetical." |
- Missing: search with no results, special characters, users without customer-view permission.
