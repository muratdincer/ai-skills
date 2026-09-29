---
name: feedback-synthesis
description: "Clusters raw customer feedback (support tickets, NPS/CSAT verbatims, app reviews, sales notes, community posts) into themes with frequency, severity, affected segments, representative anonymized quotes and the underlying need behind each request. Use when a pile of feedback must be turned into prioritizable insights, when someone asks \"what are customers telling us\", or before roadmap and backlog discussions."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 02-product
  role: product-manager
  area: discovery
  title: "Synthesize customer feedback"
  related: "research-synthesis, jobs-to-be-done, opportunity-solution-tree, persona, backlog-prioritization"
  prompt: "Here are 120 NPS comments from last quarter; group them into themes and tell me what matters most."
---

# Synthesize Customer Feedback

## Purpose
Turn scattered feedback into a small set of evidence-backed themes that show what customers struggle with, how often, how badly and for whom, so product decisions rest on patterns rather than the loudest voice.

## When to use
- A batch of feedback from one or more channels needs a structured summary.
- Before roadmap planning, backlog prioritization or a quarterly review.
- Stakeholders cite individual complaints and the team needs to know how representative they are.

## When not to use
- The input is interview transcripts from planned research. Use `research-synthesis`.
- A single ticket needs handling. Use `ticket-triage` or `ticket-response`.
- A shipped feature's usage data must be assessed. Use `feature-adoption-review`.

## Inputs
Required:
- The feedback items (text, export or pasted list), ideally with channel and date.

Optional, improves quality:
- Customer attributes per item: segment, plan, account size, tenure, NPS score.
- Product areas or an existing theme taxonomy to map to.
- The decision the synthesis should inform.

If no feedback is supplied, ask for it. Mask names, e-mails, phone numbers and account identifiers in any quoted text.

## Process
1. Inventory the input: count items per channel and period, note sampling bias (e.g. reviews skew negative, sales notes skew toward prospects, only detractors commented).
2. Split multi-topic items into atomic observations; discard items with no actionable content and report how many.
3. For each observation, separate the literal ask ("add Excel export") from the underlying need ("prove numbers to my auditor"); record the need, and mark needs you inferred as `[INFERRED]`.
4. Cluster observations bottom-up into themes named as customer problems, not features ("Can't share reports with people outside the tool", not "Sharing feature").
5. For each theme record frequency (count and share), severity (blocker / major / minor with the rule used), affected segments, trend versus prior period if data allows, and 1-2 representative quotes.
6. Weight by who is affected when attributes exist: flag themes concentrated in strategic or high-revenue segments and themes linked to churn or detractor scores.
7. Separate bugs and service issues from product gaps and from praise; route bugs to the defect process rather than the theme list.
8. Rank themes by frequency x severity x segment importance; state the formula and where you applied judgement.
9. Write implications: which themes point to opportunities, which need more research, which are noise or out of strategy.
10. List limitations (sample size, bias, missing attributes) and open questions.
11. If the user's goal continues, suggest the next skill: `opportunity-solution-tree` or `jobs-to-be-done` to frame the top themes as opportunities, or `backlog-prioritization` to weigh them against current work.

## Output format
```markdown
# Feedback Synthesis: <source(s)>, <period>
Items: <n> (<channel breakdown>) · Discarded: <n> · Known biases: ...

## Top Themes
| # | Theme (customer problem) | Freq. | Severity | Segments | Trend | Underlying need |
|---|---|---|---|---|---|---|
| 1 | ... | 23 (19%) | Major | ... | up | ... |

## Theme Details
### 1. <theme>
- Evidence: <count, channels>
- Representative quotes: > "..." (anonymized)
- Literal asks seen: <feature requests>
- Implication: <opportunity / research / ignore> – <why>

## Bugs and Service Issues (route separately)
- ...
## Praise (what to protect)
- ...
## Limitations and Open Questions
- ...
```

## Quality checklist
- [ ] Themes are phrased as customer problems, not as solutions.
- [ ] Every theme shows a count and at least one real, anonymized quote; nothing is invented.
- [ ] Literal asks and underlying needs are separated; inferred needs are labeled.
- [ ] Ranking logic is explicit, and sampling biases are stated.
- [ ] Bugs are separated from product gaps.
- [ ] Personal data in quotes is masked.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Counting feature requests literally. Ten different requests may share one need, and one request may hide three needs; cluster on the need.
- Treating frequency as importance. A rare blocker in a key segment can outweigh a common minor irritation.
- Presenting a channel's bias as the customer base's view. State who is missing from the sample.

## Example
Input: "120 NPS comments from last quarter."

Excerpt of output:
| # | Theme | Freq. | Severity | Segments | Underlying need |
|---|---|---|---|---|---|
| 1 | Month-end reports take hours to assemble | 31 (26%) | Major | Finance admins, mid-market | Close the books without manual copy-paste |
| 2 | Hard to invite external accountants | 14 (12%) | Blocker for 6 | Small firms | Collaborate with outside advisors safely |
- Bias: 70% of comments come from detractors; promoters rarely commented.
- Literal asks for theme 1: "Excel export", "scheduled PDF", "API" – one need, three solutions.
