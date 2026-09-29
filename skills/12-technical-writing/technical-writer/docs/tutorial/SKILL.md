---
description: Writes a learning-oriented tutorial in the Diátaxis sense: a single guided path in which a newcomer builds something concrete, with a defined learning outcome, prerequisites, small verifiable steps, visible results after each step and no detours. Use when onboarding new users or developers to a product, API, SDK or platform, when a "getting started" or first-project lesson is needed, or when existing getting-started content is a mix of reference and how-to.
related: how-to-guide, user-guide, docs-information-architecture, technical-onboarding, readme-writing
prompt: Write a getting-started tutorial for our payments API where a developer creates a test payment and handles the webhook, in about 30 minutes.
---

# Write a Tutorial

## Purpose
Give a newcomer a safe, reliable first success with the product by leading them through one concrete project, so they gain confidence and a mental model before they need how-to guides or reference.

## When to use
- New users or developers need a first hands-on experience.
- A "getting started" path is missing or overloaded with options and theory.
- A new product, API or platform capability needs an onboarding lesson.

## When not to use
- Readers already know the basics and want to achieve a specific goal. Use `how-to-guide`.
- Documenting all tasks of a feature for end users. Use `user-guide`.
- Explaining concepts or architecture in depth. That is explanation content; see `docs-information-architecture`.

## Inputs
Required:
- The product or technology and the concrete thing the learner will build or do.
- The learner profile (role, assumed prior knowledge).

Optional, improves quality:
- Environment details (sandbox, sample data, versions to pin), sample code, known setup pitfalls.
- Target duration, style guide.

If the end result or learner profile is missing, ask for it. Do not invent commands, API endpoints, parameters or outputs; mark any you cannot confirm `[TBD – verify]`.

## Process
1. Define one learning outcome ("By the end, you will have ...") and a realistic duration; cut anything that does not serve it.
2. Choose a meaningful but minimal project; the learner must see a working result, not a toy fragment.
3. List prerequisites precisely: accounts, tools, versions, prior knowledge; offer a sandbox or sample data so the path cannot fail on missing access.
4. Break the path into 4-8 sections, each ending in a visible, checkable result ("You should now see ...").
5. Write steps as direct instructions with exact commands, code and inputs; the learner should never have to choose between options.
6. After each significant step show the expected output, so learners can confirm they are on track; add one likely error and its fix where learners commonly fail.
7. Keep explanation minimal: one sentence of "why" at most, with links to explanation pages for depth.
8. Test the path mentally end to end (or ask the user to run it): every step must depend only on earlier steps, and versions must be pinned.
9. End with a recap of what was learned and 2-3 next steps linking to how-to guides and reference.
10. Mark all unverified commands, outputs and UI labels `[TBD – verify]` and list them for a technical review.
11. If the user's goal continues, suggest `how-to-guide` for follow-up tasks or `docs-information-architecture` to place the tutorial in the documentation set.

## Output format
````markdown
# Tutorial: <what you will build>
Duration: <~N min> | Level: <beginner/...> | Tested with: <versions or TBD>

In this tutorial you will <learning outcome>.

## Before You Start
- <account / tool / version>
- <prior knowledge>

## Step 1: <action-oriented title>
<one sentence why>
```<language>
<exact command or code>
```
You should see:
```
<expected output>
```
> If you see `<error>`, <fix>.

## Step 2: ...

## What You Learned
- ...

## Next Steps
- <how-to guide link>
- <reference link>

## Items to Verify
````

## Quality checklist
- [ ] There is exactly one path with no optional branches or "you could also".
- [ ] Every section ends with a visible, checkable result.
- [ ] Commands, code, outputs and versions are exact or marked `[TBD – verify]`.
- [ ] Explanation is minimal and links out for depth.
- [ ] Prerequisites cover everything the first step needs.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Teaching everything at once: options, flags, alternatives. Pick one path; move choices to how-to guides.
- Steps that only work on the author's machine. Pin versions, provide sample data, state OS differences.
- Ending without a working result, which destroys the learner's confidence.

## Example
Input: "Payments API tutorial: create a test payment and receive the webhook, 30 minutes, developers new to our API."

Excerpt of output:
- Weak: "Payments can be created in several ways (API, SDK, dashboard). You may also want to configure idempotency keys and retries..."
- Strong: "## Step 2: Create your first test payment / Run the command below with your sandbox key. You should see a response with `"status": "pending"` `[TBD – verify field names]`. In Step 3 you will receive the webhook that confirms it."
