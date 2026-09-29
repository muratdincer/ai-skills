---
description: Writes a one-page feature brief that aligns a team on a single feature: the problem and who has it, the expected outcome and success signal, the proposed approach, scope boundaries, key risks and the decisions still needed. Use when a feature is small enough not to need a full PRD, when a stakeholder asks for "a quick write-up" before a kickoff or refinement, or when a request must be framed for a go/no-go conversation.
related: prd-writing, hypothesis-statement, mvp-scoping, epic-breakdown, problem-statement
prompt: Write a feature brief for adding bulk CSV import of contacts to our CRM.
---

# Write a Feature Brief

## Purpose
Give everyone involved in a feature the same short answer to "why this, for whom, what does done look like, and what are we not doing", so refinement and design start from shared intent instead of assumptions.

## When to use
- A feature fits in roughly one to a few iterations and needs alignment, not a full spec.
- Before a kickoff, design session or backlog refinement.
- A stakeholder needs a concise basis for a go/no-go or prioritization decision.

## When not to use
- The initiative spans many teams or iterations, or has compliance weight. Use `prd-writing`.
- The core problem is still unclear. Use `problem-statement` first.
- The feature is agreed and must be split into stories. Use `epic-breakdown`.

## Inputs
Required:
- The feature idea or request and the user group it is for.

Optional, improves quality:
- Evidence (tickets, feedback themes, analytics), related goals or OKRs.
- Known constraints: deadline and reason, platforms, dependencies.
- Rough solution ideas or designs.

If the feature or its users are missing, ask. Keep unknowns as `[TBD]` in open decisions rather than asking up front.

## Process
1. Separate the literal ask from the underlying need; write the problem in 2-3 sentences (who, situation, impact) without the solution, and note evidence or mark it `[ASSUMPTION]`.
2. State the expected outcome and one primary success signal with a target or `[TBD]`; add a guardrail if the feature could harm something else.
3. Describe the proposed approach at the level of user-visible behavior (main flow in 3-6 steps), not implementation.
4. Draw scope lines: in scope, explicitly out of scope, and "later" ideas.
5. Note UX considerations: entry points, empty/error states, permissions, accessibility.
6. List dependencies and top 3 risks (value, usability, feasibility, viability) with a mitigation or test for each.
7. Give a rough size signal only if the team provided one; otherwise mark `[TBD – team estimate]`.
8. List open decisions with owner and needed-by date; separate them from open questions that do not block starting.
9. Trim to one page: move detail to links.
10. If the user's goal continues, suggest the next skill: `epic-breakdown` to create stories, `hypothesis-statement` if the outcome is uncertain enough to test first, or `prd-writing` if the scope turns out larger.

## Output format
```markdown
# Feature Brief: <feature name>
Owner: <name> · Status: <draft/agreed> · Date: <date> · Related goal: <OKR/goal | [TBD]>

**Problem:** <who, situation, impact> (evidence: ...)
**Outcome and success signal:** <metric, baseline -> target, timeframe> · Guardrail: ...

**Proposed approach**
1. ...

| In scope | Out of scope | Later |
|---|---|---|
| ... | ... | ... |

**UX notes:** ...
**Dependencies:** ...
**Risks:** <risk> – <mitigation/test>
**Size signal:** <team estimate | [TBD]>

**Open decisions**
| Decision | Owner | Needed by |
|---|---|---|
```

## Quality checklist
- [ ] The problem is written without the solution and names a specific user group.
- [ ] There is one primary success signal, measured or marked `[TBD]`, never invented.
- [ ] Out-of-scope is explicit and non-empty.
- [ ] The approach describes behavior, not implementation.
- [ ] The brief fits on one page.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Letting the brief grow into a PRD. If it needs more than a page, the feature is too big or the brief holds detail that belongs in stories.
- Leaving "out of scope" empty. Every feature has tempting neighbors; name them so they do not creep back in.
- Using output as the success signal ("feature shipped"). Name the behavior that should change.

## Example
Input: "Add bulk CSV import of contacts to our CRM."

Excerpt of output:
- Problem: Sales ops admins at newly onboarded accounts re-enter hundreds of contacts by hand when migrating from spreadsheets, delaying first use by days `[ASSUMPTION – check onboarding tickets]`.
- Success signal: median time from account creation to 100 contacts drops from [TBD] to under 1 day.
- Out of scope: sync with external CRMs; deduplication beyond exact e-mail match.
- Risk (usability): column mapping errors – test with 5 admins using their real files (anonymized).
