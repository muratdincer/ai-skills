---
description: Writes a Product Requirements Document covering problem and evidence, goals and success metrics, target users, scope and non-goals, prioritized requirements with acceptance criteria, user experience, non-functional needs, dependencies, risks, release plan and open questions. Use when a product initiative must be aligned across engineering, design and stakeholders before build, when someone asks for a PRD or product spec, or when an existing PRD needs a review for gaps.
related: feature-brief, mvp-scoping, epic-breakdown, nfr-specification, acceptance-criteria
prompt: Write a PRD for letting B2B customers set approval workflows on purchase orders above a threshold.
---

# Write a Product Requirements Document

## Purpose
Create a single source of truth that explains why an initiative matters, what outcome it must achieve and what the product must do, precise enough for engineering and design to plan, and clear about what is out of scope and still unknown.

## When to use
- A multi-iteration initiative or significant feature needs cross-team alignment before build.
- Leadership or partners need a reviewable spec with goals, scope and risks.
- An existing PRD must be checked for missing sections, vague requirements or untestable goals.

## When not to use
- A small feature only needs a one-page alignment note. Use `feature-brief`.
- Formal business or functional requirements for a contractual or regulated project are required. Use `brd-writing` or `frd-writing`.
- The scope is still too large and needs cutting first. Use `mvp-scoping`.

## Inputs
Required:
- The problem or opportunity and the target users.
- Whatever is known about the intended solution direction.

Optional, improves quality:
- Evidence: research, feedback themes, analytics, sales/support data.
- Strategy/OKR link, constraints (dates, compliance, platforms), dependencies.
- Designs, technical notes, prior decisions.

If the problem or target users are missing, ask (at most 5 questions in one batch). Everything else unknown becomes `[TBD]` in open questions; do not invent metrics, dates or customer names.

## Process
1. Write the problem statement without a solution: who, what struggle, when, impact, evidence. Label anything inferred `[ASSUMPTION]`.
2. Link the initiative to strategy or an objective and state why now.
3. Define goals as outcomes with success metrics (baseline, target, timeframe, source), plus guardrail metrics and explicit non-goals.
4. Describe target users and key scenarios; reference personas or jobs if they exist.
5. Set scope: in scope, out of scope (with reason), and later phases.
6. Write functional requirements as numbered, testable statements tied to scenarios, each with priority (Must/Should/Could or equivalent) and 1-3 acceptance criteria; separate the requirement from any suggested implementation.
7. Capture UX notes (flows, states, empty/error cases, accessibility per WCAG 2.2) and link designs.
8. List non-functional requirements that matter here: performance, availability, security/privacy (KVKK/GDPR if personal data), auditability, localization, scalability.
9. Record dependencies, risks with mitigations, and assumptions to validate.
10. Outline rollout: phasing, feature flags, migration, beta cohort, launch criteria, support and documentation needs.
11. Collect open questions with owner and needed-by date, and add a decision log and change history.
12. If the user's goal continues, suggest the next skill: `epic-breakdown` or `story-mapping` to turn requirements into backlog items, or `nfr-specification` for deeper quality requirements.

## Output format
```markdown
# PRD: <initiative name>
Status: Draft · Owner: <PM> · Reviewers: <eng, design, ...> · Last updated: <date>

## 1. Problem and Evidence
## 2. Strategic Fit and Why Now
## 3. Goals, Success Metrics and Non-goals
| Metric | Baseline | Target | Timeframe | Source |
|---|---|---|---|---|
Guardrails: ... · Non-goals: ...
## 4. Users and Key Scenarios
## 5. Scope
- In: ... · Out (why): ... · Later: ...
## 6. Requirements
| ID | Requirement | Scenario | Priority | Acceptance criteria |
|---|---|---|---|---|
| R1 | The system shall ... | S1 | Must | Given/When/Then ... |
## 7. User Experience
## 8. Non-functional Requirements
## 9. Dependencies, Risks and Assumptions
## 10. Rollout and Launch Criteria
## 11. Open Questions
| # | Question | Owner | Needed by |
## 12. Decision Log and Change History
```

## Quality checklist
- [ ] The problem is stated without a solution and cites evidence or is marked `[ASSUMPTION]`.
- [ ] Each goal has a metric with baseline, target and timeframe; unknown values are `[TBD]`, not invented.
- [ ] Non-goals and out-of-scope items are explicit.
- [ ] Every requirement is uniquely numbered, testable, prioritized and has acceptance criteria.
- [ ] Relevant NFRs, privacy and accessibility are addressed or explicitly marked not applicable.
- [ ] Open questions have owners and dates; risks have mitigations.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing the PRD as a feature list. Anchor every requirement to a scenario and goal, or cut it.
- Specifying implementation ("use a modal with three tabs"). State the need and constraints; leave design and architecture choices to the owners.
- Treating the PRD as frozen. Keep a change history and decision log so reviewers can see what moved and why.

## Example
Input: "B2B customers need approval workflows on purchase orders above a threshold."

Excerpt of output:
- Problem: Finance managers at mid-size customers cannot stop large purchase orders before they are sent, which leads to after-the-fact cancellations `[ASSUMPTION – confirm with support data]`.
- Goal: share of POs above threshold cancelled after sending drops from [TBD – baseline] to under 2% within 2 quarters.
- R3 (Must): The system shall hold a PO above the account threshold in "Pending approval" until an approver approves or rejects it.
  - Given threshold 10,000 and a PO of 12,000, when the buyer submits, then status is "Pending approval" and approvers are notified.
- Non-goal: multi-level approval chains (later phase).
