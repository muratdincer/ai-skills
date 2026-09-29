---
description: "Creates or revises a Definition of Done: the shared quality checklist every increment or work item must pass to count as complete, layered by item, release and organization level, with verification method per criterion and a plan to close gaps. Use when 'done' means different things to different people, quality escapes to production, or someone asks for a DoD or completion criteria."
related: "definition-of-ready, release-quality-gate, acceptance-criteria, coding-standards, working-agreement"
prompt: "Draft a Definition of Done for our mobile banking team; we have code review and unit tests but releases still break accessibility and security checks."
---

# Define Definition of Done

## Purpose
Make "done" a single, transparent quality commitment so that finished work is truly releasable, hidden work is not deferred, and progress figures reflect reality.

## When to use
- Items are marked done but still need testing, documentation or deployment work.
- Defects, accessibility or security issues keep escaping to production.
- Several teams contribute to one product and need a common quality bar.
- A regulated context requires evidence of quality activities.

## When not to use
- Entry criteria before work starts. Use `definition-of-ready`.
- Item-specific behavior that proves one story works. Use `acceptance-criteria`.
- A go/no-go decision for a specific release. Use `release-quality-gate` or `go-no-go`.

## Inputs
Required:
- What the team delivers (product type, platforms) and its current practices or problems. If missing, ask; the DoD must reflect what the team can actually verify.

Optional, improves quality:
- Existing DoD, organizational or regulatory quality requirements.
- Tooling realities: automated tests, pipeline stages, environments.
- Known escaped defects or audit findings.

## Process
1. Separate three levels: item level (each story/bug), increment/release level (what must hold before release), and organizational baseline (applies to all teams).
2. Cover these quality dimensions and include only what applies: code quality and review; automated tests (unit, integration) passing; acceptance criteria verified; non-functional checks (performance, security per OWASP ASVS level, accessibility per WCAG 2.2 AA); documentation (user, API, operational); deployment to an integrated environment; monitoring/logging in place; data privacy (KVKK/GDPR) considerations checked.
3. Phrase each criterion as verifiable and note the evidence (pipeline stage, checklist, reviewer sign-off).
4. Compare with the current state. Mark criteria the team cannot yet meet as "target" with a gap-closing action instead of pretending they are met.
5. Ensure the DoD does not conflict with acceptance criteria: DoD is generic and applies to all items; AC are item-specific.
6. Define what happens when an item fails the DoD at iteration/sprint end or at release: it is not done, returns to the backlog, and is not counted in progress.
7. Set a review cadence and a rule for strengthening the DoD over time (add one target criterion when capacity allows).
8. Produce a one-page DoD suitable for the team board.

## Output format
```markdown
# Definition of Done – <team/product>
Version: <n> · Agreed: <date or [TBD]> · Applies with org baseline: <yes/no>

## Item Level
| # | Criterion | Evidence | Status |
|---|---|---|---|
| 1 | Code reviewed by at least one other developer | Pull request approval | Met |

## Increment / Release Level
| # | Criterion | Evidence | Status |
|---|---|---|---|

## Target Criteria (not yet met)
- <criterion> – gap – action – owner – by when [TBD]

## Not Done Handling
<what happens when an item fails DoD>

## Review
<cadence and how the DoD is strengthened>
```

## Quality checklist
- [ ] Every criterion is verifiable and names its evidence.
- [ ] Item level and release level are separated.
- [ ] Non-functional dimensions (security, accessibility, performance, operability) are considered explicitly.
- [ ] Unmet criteria are shown as targets with actions, not as met.
- [ ] No item-specific acceptance criteria are mixed into the DoD.
- [ ] Standards are named precisely (e.g. WCAG 2.2 AA, OWASP ASVS level).

## Common pitfalls
- A DoD the team cannot meet in practice. It gets ignored; start with what is achievable and add targets.
- "Done" meaning "done in development". Include integration and deployability or progress numbers become fiction.
- Listing activities ("testing done") instead of outcomes ("all automated tests pass in the pipeline").

## Example
Input: "Mobile banking team, code review and unit tests exist, accessibility and security checks keep breaking."

Excerpt of output:
| 5 | New or changed screens pass WCAG 2.2 AA checks for contrast, labels and focus order | Accessibility checklist attached to item | Target |
| 6 | No new high/critical findings from dependency and static security scans | Pipeline scan stage | Met |
- Target: Screen reader smoke test on both platforms – gap: no device lab – action: define minimal manual script – owner [TBD].
