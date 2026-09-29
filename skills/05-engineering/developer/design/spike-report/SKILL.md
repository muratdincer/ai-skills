---
description: "Writes a spike report that records the question a time-boxed investigation had to answer, what was tried, evidence found, options with trade-offs and a clear recommendation with follow-up work. Use when a spike, proof of concept or technical investigation has finished (or is being planned) and its result must be shared so the team can decide and estimate."
related: "technical-design-doc, adr, technology-selection, trade-off-analysis, task-breakdown"
prompt: "Write a spike report: we spent two days checking whether our current search can handle typo-tolerant product search or whether we need a dedicated search engine."
---

# Write a Spike Report

## Purpose
Convert a time-boxed investigation into a decision-ready summary so that the knowledge gained is not lost in someone's head and the follow-up work can be planned and estimated.

## When to use
- A spike or proof of concept finished and the team must decide how to proceed.
- A spike is about to start and needs a sharp question, time box and exit criteria.
- An estimate is blocked by a technical unknown that has now been investigated.

## When not to use
- The approach is already chosen and needs a full design. Use `technical-design-doc`.
- Only the final decision must be recorded. Use `adr`.
- Comparing products or vendors at portfolio level. Use `technology-selection`.

## Inputs
Required:
- The question the spike was meant to answer and the raw findings (notes, measurements, code observations).

Optional, improves quality:
- Time box used, environment and data set, constraints and evaluation criteria agreed beforehand.
- Links to prototype branches, benchmarks, vendor docs.

If findings are missing, offer to write the planning half (question, time box, exit criteria, method) instead.

## Process
1. State the question as a decision to be made ("Can X meet Y under Z?"), not a topic ("look into X").
2. Record the time box, actual time spent and whether the spike ended by answer or by time out.
3. List evaluation criteria with thresholds agreed beforehand; if none were set, derive them and mark `[ASSUMPTION]`.
4. Describe what was tried: approach, environment, data set size and shape, versions. Enough for someone to repeat it.
5. Present evidence separately from interpretation: measurements, observed behavior, errors, limits hit.
6. Summarize options (usually 2-4) against the criteria with effort, risk and reversibility.
7. Give one recommendation with confidence level (high/medium/low) and what would change the recommendation.
8. State what the spike did not cover and the residual risks.
9. List follow-up work as candidate backlog items with rough size, and note that prototype code is throwaway unless stated otherwise.
10. If the goal continues, suggest `adr` to record the decision, `technical-design-doc` to detail the chosen option or `task-breakdown` to plan the follow-up work.

## Output format
```markdown
# Spike Report: <question in short form>
Time box: <planned> / Spent: <actual> · Ended by: answer | time box · Author: <name> · Date: <date>

## Question
## Evaluation Criteria
| Criterion | Threshold | Result |

## What We Tried
## Evidence
## Options
| Option | Meets criteria? | Effort | Risk | Reversible? |

## Recommendation
<option> — confidence: <H/M/L> — would change if: <condition>

## Not Covered / Residual Risks
## Follow-up Work
| Item | Rough size | Notes |
```

## Quality checklist
- [ ] The question is answerable with yes/no or a choice, not open-ended.
- [ ] Evidence is reproducible: environment, data and versions are stated.
- [ ] Measurements are reported as observed; nothing extrapolated without saying so.
- [ ] A single recommendation is given with confidence and change conditions.
- [ ] Gaps in coverage are explicit.
- [ ] Follow-up items are concrete enough to enter the backlog.
- [ ] Inferences are labeled `[ASSUMPTION]` and listed as assumptions or open questions; nothing unsupported is stated as fact.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Spikes without a question or time box that become unplanned feature work. Fix the question and exit criteria first.
- Shipping prototype code as production code. Call out explicitly that it must be rewritten or hardened.
- Benchmarks on toy data. State data size and shape and flag results that may not scale.

## Example
Input: "Two days on typo-tolerant search: current DB full-text vs dedicated search engine. 50k products."

Excerpt of output:
- Question: Can the existing database full-text search return typo-tolerant results for 50k products under the latency target `[target UNKNOWN, assumed p95 < 200 ms]`?
- Evidence: trigram similarity found 9 of 10 sample typos; p95 140 ms on a 50k copy of production data (masked).
- Recommendation: stay on database search with trigram index — confidence medium — would change if catalog growth pushes p95 over the target or faceting becomes a requirement.
