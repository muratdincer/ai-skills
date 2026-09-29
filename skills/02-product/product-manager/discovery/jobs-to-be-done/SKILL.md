---
description: Frames Jobs-to-be-Done by writing a solution-free core job statement, related and emotional/social jobs, job steps, and measurable desired outcome statements that can be prioritized by importance and satisfaction. Use when defining what customers are trying to get done, when innovation or roadmap work needs a solution-agnostic frame, or when someone asks for JTBD, job stories or desired outcomes.
related: persona, opportunity-solution-tree, customer-journey-map, problem-interview-script, feedback-synthesis
prompt: Frame the jobs-to-be-done for restaurant owners who manage supplier orders.
---

# Frame Jobs-to-be-Done

## Purpose
Describe the progress customers want to make, independent of any product, so that teams can find unmet needs, compare solutions fairly and prioritize by what customers value.

## When to use
- Starting discovery in a problem space or before ideation.
- A roadmap is feature-driven and needs a customer-progress frame.
- Comparing your product with non-obvious alternatives customers "hire" today.

## When not to use
- You need a behavioral profile of a user group. Use `persona`.
- You need to link outcomes to solutions and experiments. Use `opportunity-solution-tree`.
- You need an interview guide to gather job data. Use `problem-interview-script`.

## Inputs
Required:
- The target customer (job executor) and the problem space or situation.

Optional, improves quality:
- Interview notes, switch stories (why customers moved from one solution to another), support and review data.

If the job executor or the situation is missing, ask. Statements not backed by research are marked `[ASSUMPTION]`.

## Process
1. Identify the job executor and other roles (buyer, approver, beneficiary).
2. Write the core functional job as "verb + object + contextual clarifier", without solution or technology words ("keep the kitchen supplied with ingredients at the lowest waste").
3. Add related jobs and emotional/social jobs ("feel in control", "be seen as reliable by staff").
4. Map job steps using a universal job map: define, locate, prepare, confirm, execute, monitor, modify, conclude.
5. For each step, write desired outcome statements: "Minimize the time/likelihood of <undesired result> when <step context>". Keep them measurable and stable over time.
6. Capture the situation/trigger with job stories where helpful: "When <situation>, I want to <motivation>, so I can <expected outcome>".
7. List current solutions hired and their shortcomings, including non-consumption.
8. Propose how to prioritize outcomes (importance vs satisfaction survey) and flag likely underserved outcomes from evidence.

## Output format
```markdown
# Jobs-to-be-Done: <job executor> — <situation>
**Core job:** <verb + object + clarifier>
Related jobs: ... · Emotional/social jobs: ...

## Job Map and Desired Outcomes
| Step | Desired outcome statements | Evidence |
|---|---|---|
| Define | Minimize ... | ... |

## Job Stories
- When ..., I want to ..., so I can ...

## Current Solutions and Shortcomings
- ...

## Likely Underserved Outcomes
- ...

## Next Research
- Importance/satisfaction survey on outcomes ...
```

## Quality checklist
- [ ] The core job contains no product, feature or technology.
- [ ] Outcome statements are measurable (time, likelihood, number) and solution-free.
- [ ] Emotional and social jobs are considered.
- [ ] Non-consumption and workarounds appear among current solutions.
- [ ] Assumed items are marked `[ASSUMPTION]`.

## Common pitfalls
- Writing jobs at the wrong altitude ("click export"). Ask "why?" until you reach a stable goal.
- Mixing needs with solutions ("an app to reorder"). Remove the solution, keep the progress.
- Stopping at the job statement. The value is in the outcome statements used to prioritize.

## Example
Input: "Restaurant owners managing supplier orders."

Excerpt of output:
- Core job: Keep the kitchen stocked with the right ingredients for upcoming service at minimal waste.
- Outcome (Monitor): Minimize the likelihood of discovering a missing ingredient after service has started.
- Current solutions: paper stock counts, phoning suppliers, over-ordering as a buffer.
