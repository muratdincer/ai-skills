---
description: Synthesizes raw research data (interview notes, usability observations, open survey answers) into evidence-backed findings, insights and prioritized recommendations through affinity clustering, with frequency, severity and confidence for each. Use after interviews or usability sessions, when someone asks "what did we learn", or when notes must become a readout for a decision.
related: research-plan, usability-test-script, interview-notes-analysis, feedback-synthesis, customer-journey-map
prompt: Synthesize these notes from 8 onboarding interviews into key insights and recommendations for the product team.
---

# Synthesize Research Findings

## Purpose
Turn scattered observations into a small set of insights that are traceable to evidence, honest about confidence, and tied to decisions, so the team acts on patterns instead of the loudest quote.

## When to use
- Fieldwork (interviews, usability tests, diary studies, open-ended survey answers) is finished.
- Several researchers' notes must be merged into one view.
- A readout for stakeholders or a decision meeting is needed.

## When not to use
- Only one interview transcript needs structuring. Use `interview-notes-analysis`.
- The input is a stream of customer feedback, reviews or tickets rather than a study. Use `feedback-synthesis`.
- The study has not been planned yet. Use `research-plan`.

## Inputs
Required:
- Raw research data: notes, transcripts, observation grids or survey answers.

Optional, improves quality:
- Research plan and questions, participant profiles (pseudonymized), task outcomes, the decision the study serves.

If no raw data is supplied, ask for it; do not synthesize from summaries of summaries without flagging it. Remove or mask names, contact details and other personal data before quoting.

## Process
1. Restate the research questions and the decision; if missing, infer them from the material and mark `[ASSUMPTION]`.
2. Break the data into atomic observations (one behavior, quote or outcome each), tagged with participant ID, segment and task/topic; keep observed behavior separate from what participants said and from your interpretation.
3. Cluster observations bottom-up by affinity (do not start from preset categories), then name each cluster with a sentence that states the pattern, not a topic label.
4. Count coverage for each cluster (e.g. 6 of 8 participants) and note disconfirming evidence and segment differences.
5. Turn clusters into insights: observation + why it happens (the underlying need or mental model) + consequence for the product. Label the "why" as inference unless participants demonstrated it.
6. Rate each insight: severity or impact (High/Medium/Low), confidence (High/Medium/Low based on coverage, consistency and method), and link it to research questions.
7. For usability data, list issues per task with a severity scale (e.g. 0-4: cosmetic to blocker) and completion results.
8. Write recommendations as problems to solve or directions, each linked to insights; separate quick fixes from items needing more research.
9. Record what the study cannot answer (sample limits, "how many" questions) and the open questions.
10. Draft the readout: top 3-5 insights first, then detail and evidence appendix; suggest `customer-journey-map` or `opportunity-solution-tree` if the goal continues into design or prioritization.

## Output format
```markdown
# Research Synthesis: <study>
Participants: <n, segments> · Method: <method> · Dates: <dates>

## Key Insights
1. **<insight sentence>** — Coverage: <x of n> · Impact: <H/M/L> · Confidence: <H/M/L>
   - Evidence: P3 "<quote>", P5 <behavior>
   - Why (inferred): ...
   - Implication: ...

## Usability Issues (if applicable)
| Task | Issue | Participants | Severity (0-4) | Evidence |
|---|---|---|---|---|

## Recommendations
| # | Recommendation | Based on | Type (quick fix / design / research) |
|---|---|---|---|

## Limitations and Open Questions
- ...

## Appendix: Clusters and Observations
- <cluster> → P1, P4, P6
```

## Quality checklist
- [ ] Every insight cites evidence from at least two participants or is marked as a single-case signal.
- [ ] Observed behavior, reported statements and interpretation are distinguishable.
- [ ] Coverage counts are real, not percentages inflated from small samples.
- [ ] Contradicting evidence and segment differences are reported.
- [ ] Quotes are pseudonymized and contain no personal data.
- [ ] Recommendations trace to insights and do not prescribe untested solutions as facts.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Topic buckets ("Navigation", "Pricing") instead of insights. Name what is happening and why.
- Reporting "60% of users" from 5 participants. Use counts and state qualitative limits.
- Cherry-picking quotes that confirm the team's plan. Show the disconfirming cases next to the pattern.

## Example
Input: notes from 8 onboarding interviews.

Weak: "Onboarding: users had problems with setup."
Strong: "**New admins postpone inviting teammates because they want to 'clean up' the workspace first** — Coverage: 5 of 8 · Impact: High · Confidence: Medium. Evidence: P2 'I don't want them to see this mess'; P6 closed the invite modal twice. Implication: invite prompts at signup are ignored; team activation is delayed."
