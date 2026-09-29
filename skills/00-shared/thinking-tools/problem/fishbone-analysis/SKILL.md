---
description: Builds an Ishikawa (fishbone) diagram that organizes all plausible causes of a clearly stated effect into categories suited to the domain, separates evidenced causes from hypotheses, and selects the few causes worth verifying first. Use when a problem likely has several interacting causes, when a team brainstorms causes and needs structure, or before running 5 Whys on the most promising branches.
related: problem-statement, five-whys, postmortem, diagram-as-code, assumption-mapping
prompt: Do a fishbone analysis: our release lead time went from 3 days to 2 weeks over the last two quarters.
---

# Run a Fishbone Analysis

## Purpose
Widen the search for causes before narrowing it, so the team does not fix the first cause it thinks of, and end with a short, evidence-ranked list of causes to verify.

## When to use
- A quality, delivery or operational problem probably has multiple contributing causes.
- A group brainstorm on causes produced a long, unstructured list.
- Previous single-cause fixes did not move the metric.

## When not to use
- The effect is not agreed or measurable yet. Use `problem-statement` first.
- A single causal chain with clear evidence already exists. Use `five-whys`.
- A running system fault needs debugging. Use `debugging-hypotheses`.

## Inputs
Required:
- The effect (problem) to analyze, ideally with its measure and time frame.

Optional, improves quality:
- Data: metrics, defect or ticket categories, timelines, change history.
- Candidate causes already raised by the team.
- Preferred category set used in the organization.

If the effect is missing, ask for it. If it is phrased as a solution or a cause, restate it as an observable effect and confirm with the user.

## Process
1. Write the effect at the head of the fish as an observable, measurable statement with a time frame ("release lead time rose from 3 days to 14 days in Q1-Q2").
2. Choose 4-7 categories that fit the domain: for software delivery, for example People/Skills, Process, Tools/Platform, Code/Architecture, Environment/Infrastructure, Requirements/Input, Measurement; for services or manufacturing, the 6M or 8P sets. Rename categories to the team's language.
3. Populate each category with candidate causes from the input first, then add plausible causes you infer, labeled `[HYPOTHESIS]`.
4. Ask "why does this happen?" once or twice per cause to add sub-causes; stop when the sub-cause would need its own analysis.
5. Remove duplicates and move causes that belong in another category; a cause appears once, in the category where it can be changed.
6. Mark each cause's evidence status: Evidenced (data or record cited), Reported (someone stated it), Hypothesis (inferred).
7. Rate each cause on likely impact on the effect and ease of verification (High/Medium/Low), with a one-line reason.
8. Select the 3-5 causes to verify first: high impact first, then easy to verify; note what data or test would confirm or refute each.
9. Render the diagram as a nested list or as diagram code if requested, and keep the table as the source of truth.
10. List open questions and data needed, and note causes outside the team's control separately.
11. If the user's goal continues, suggest `five-whys` on the selected causes, `diagram-as-code` for a visual, or `assumption-mapping` to plan verification.

## Output format
```markdown
# Fishbone: <effect short title>

**Effect:** <observable, measurable statement with time frame>

## Causes by Category
### <Category 1>
- <cause> [Evidenced | Reported | Hypothesis]
  - <sub-cause>
### <Category 2>
- ...

## Prioritized Causes to Verify
| # | Cause | Category | Evidence status | Impact | Ease to verify | How to verify |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | H/M/L | H/M/L | <data or test> |

## Outside Our Control
- ...

## Open Questions and Data Needed
- ...
```

## Quality checklist
- [ ] The effect is observable, measurable and free of causes or solutions.
- [ ] Categories fit the domain; no category is empty without a stated reason.
- [ ] Every cause has an evidence status; inferred causes are labeled `[HYPOTHESIS]`.
- [ ] No cause is a person; people-related causes describe skills, load or incentives.
- [ ] The prioritized list has a concrete verification method per cause.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Treating the diagram as the conclusion. It lists candidates; only verification makes something a cause.
- Forcing the classic 6M categories onto software work. Use categories the team can act on.
- Letting the loudest voice fill one bone. Seek at least one candidate in each category before ranking.
- Writing solutions as causes ("no automated tests"). Rewrite as the condition ("regressions are found only in manual UAT").

## Example
Input: "Release lead time went from 3 days to 2 weeks over the last two quarters."

Excerpt of output:
- Process: change approval board moved from weekly to biweekly [Reported]
- Tools/Platform: shared staging environment is blocked by other teams' tests [Hypothesis]
- Code/Architecture: merge conflicts rose after two teams started working in one repository [Evidenced – merge request data]

| # | Cause | Impact | Ease | How to verify |
|---|---|---|---|---|
| 1 | Biweekly approval board | H | H | Compare approval wait time per release before/after the change |
