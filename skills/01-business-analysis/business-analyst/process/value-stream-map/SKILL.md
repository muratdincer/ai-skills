---
description: "Maps a value stream from customer request to delivered value, separating process time from wait time for every step, classifying steps as value-adding, necessary non-value-adding or waste, and computing lead time, process time, flow efficiency and rework rates. Use when a process or delivery flow feels slow, when lead time must be reduced, or when someone asks where the waste, waiting or bottleneck is."
related: "as-is-process, to-be-process, cycle-time-analysis, five-whys, process-gap-analysis"
prompt: "Map the value stream for our customer onboarding: from application to active account it takes about 12 days and we want to know where the time goes."
---

# Map a Value Stream

## Purpose
Show where time goes between a customer request and delivered value, so improvement targets the biggest waits and waste instead of speeding up steps that barely matter.

## When to use
- Lead time is long or unpredictable and the cause is unclear.
- A to-be design needs a quantified baseline and target.
- An end-to-end flow spans several teams and nobody owns the whole.

## When not to use
- You only need the step-by-step description without timings. Use `as-is-process`.
- You are analyzing a delivery team's work item flow from tracker data. Use `cycle-time-analysis`.
- You need the root cause of one specific delay. Use `five-whys`.

## Inputs
Required:
- The flow's start trigger and end point (what "value delivered" means).
- The main steps, with at least rough process time and wait time per step, or data from which they can be derived.

Optional, improves quality:
- Volume (items per day/week), batch sizes, number of people per step.
- Percent complete and accurate (%C&A) or rework rate per step.
- Timestamps from a system log or tracker.

If timings are missing, ask for them step by step (at most 5 questions at once). If only estimates are available, use them and mark them `[ASSUMPTION]`; never fabricate numbers.

## Process
1. Fix the boundaries: customer, trigger, end state and unit of flow (one application, one order, one change).
2. List steps in order with the performing team/system and handoffs; include queues, approvals and batch jobs as explicit steps or waits.
3. Record per step: process time (hands-on work), wait time before the next step, %C&A, and batch/volume if known. Use median, not best case; note spread when it is large.
4. Classify each step: Value-adding (the customer would pay for it), Necessary non-value-adding (regulation, control), Waste. Tag waste type: waiting, rework/defects, overprocessing, handoffs/transport, motion, inventory/queues, unused talent.
5. Compute lead time (sum of process + wait), total process time, flow efficiency (process ÷ lead time) and rolled %C&A (product of step %C&A).
6. Identify the bottleneck (step with the longest wait or lowest capacity) and the top 3 waste sources by time lost.
7. Draw the map as a text timeline or diagram code, with a time ladder showing process vs wait.
8. Propose improvement ideas per waste (remove, merge, parallelize, automate, reduce batch size, move quality upstream), each with an estimated effect marked `[ASSUMPTION]`.
9. Sketch the future-state metrics (target lead time, flow efficiency) only as derived from the ideas; state which data would confirm them.
10. If the user wants to continue, suggest `to-be-process` to redesign the flow, `five-whys` for the bottleneck or `process-gap-analysis` to plan the changes.

## Output format
```markdown
# Value Stream Map: <flow>
Trigger: <...> · End: <...> · Unit: <...> · Time unit: <hours/days>

## Steps
| # | Step | Owner | Process time | Wait after | %C&A | Class (VA / NNVA / Waste: type) |
|---|---|---|---|---|---|---|

## Summary Metrics
| Metric | Value |
|---|---|
| Lead time | ... |
| Process time | ... |
| Flow efficiency | ...% |
| Rolled %C&A | ...% |

## Timeline
<text ladder or diagram code>

## Bottleneck and Top Waste
1. <step> – <time lost> – <waste type>

## Improvement Ideas
| Idea | Targets | Expected effect | Confidence |
|---|---|---|---|

## Data Quality and Open Questions
- [ASSUMPTION] ...
```

## Quality checklist
- [ ] Process time and wait time are separated for every step.
- [ ] Summary metrics are arithmetically consistent with the step table.
- [ ] Every number is from the input or marked `[ASSUMPTION]`; nothing is invented.
- [ ] Each waste is typed and each idea points to a specific waste.
- [ ] Controls required by regulation are classified NNVA, not waste to be removed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Optimizing process time when 90% of lead time is waiting. Attack queues, handoffs and batching first.
- Using best-case timings from the process owner. Ask for typical and worst cases or use real timestamps.
- Ignoring rework loops. A low %C&A step multiplies downstream waits; show it.

## Example
Input: "Onboarding takes ~12 days: application check 30 min, then waits 3 days; KYC review 1 h, waits 5 days for documents; account setup 20 min, waits 2 days for batch; welcome call 15 min."

Excerpt of output:
| Metric | Value |
|---|---|
| Lead time | ~10.1 days (the stated 12 days leaves ~2 days unexplained `[ASSUMPTION]`: ask where) |
| Process time | 2 h 05 min |
| Flow efficiency | ~0.9% (on 24 h days) |

Top waste: waiting for customer documents after KYC (5 days) – idea: request documents at application, not after review.
