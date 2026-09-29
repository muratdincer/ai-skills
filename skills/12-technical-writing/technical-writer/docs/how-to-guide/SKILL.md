---
description: Writes a goal-oriented how-to guide in the Diátaxis sense: a focused recipe that takes a reader who already knows the basics from a stated starting point to one real-world result, with preconditions, numbered action steps, decision points, verification and troubleshooting, and no teaching or background detours. Use when users ask "how do I ...", when a support ticket or recurring question reveals a task without documentation, or when existing docs mix tutorial, reference and explanation for a practical task.
related: tutorial, user-guide, docs-information-architecture, style-guide-check, runbook
prompt: Write a how-to guide for rotating the API signing key in our platform without downtime, for integration developers.
---

# Write a How-to Guide

## Purpose
Help a competent reader complete one specific, real-world task quickly and safely, by giving exactly the steps, conditions and checks needed and nothing else, so the guide can be followed under time pressure.

## When to use
- Users or developers repeatedly ask how to accomplish a specific task.
- A support ticket, incident or release introduces a task that has no documentation.
- An existing page mixes concepts, reference tables and task steps and the task needs its own page.

## When not to use
- The reader is new and needs a first guided success. Use `tutorial`.
- Documenting every task of a feature or product for end users. Use `user-guide`.
- An operational procedure for on-call or production support with alerts and escalation. Use `runbook`.

## Inputs
Required:
- The goal stated as the reader would phrase it ("rotate the signing key", "export invoices to CSV").
- The audience and what they already know or have access to.
- The actual steps or a source of truth for them (SME notes, ticket resolution, code, UI walkthrough).

Optional, improves quality:
- Product version or edition, environment differences (OS, cloud, plan tier).
- Known failure modes, related reference pages, style guide.

If the goal or the source of the steps is missing, ask for it (one question at a time). Never invent commands, parameters, menu labels or outputs; mark any you cannot confirm `[TBD – verify]`.

## Process
1. Restate the goal as a task title starting with a verb in the reader's words ("Rotate the API signing key"); if the request covers several goals, split them into separate guides and say so.
2. Define the starting point and end state: what the reader has before step 1 and what is true after the last step.
3. List preconditions: permissions or roles, versions, required data, backups, maintenance windows; put anything destructive or irreversible in a warning before the steps, not inside them.
4. Separate what the source states from what you infer; label inferred steps `[ASSUMPTION]` and list them for SME confirmation.
5. Write numbered steps, one action per step, in imperative mood, with the exact UI label, command or value; put the condition before the action ("If you use SSO, select ...").
6. Handle real variation with explicit decision points or short tabs per variant (OS, deployment type); do not branch for options that do not change the result.
7. Add verification: how the reader confirms success (expected output, status, UI state) at the end and after any risky step.
8. Add troubleshooting for the 2-4 most likely failures, each as symptom, cause, fix; add rollback or undo if the task changes production state.
9. Strip teaching and background to at most one sentence of context; link to explanation and reference pages instead.
10. Check the guide against the audience: no step assumes knowledge they lack, no step explains what they already know.
11. List every `[TBD – verify]` and `[ASSUMPTION]` item under "Items to verify" with the likely verifier.
12. If the user's goal continues, suggest `style-guide-check` before publishing, `docs-information-architecture` to place the guide, or `tutorial` if readers turn out to be beginners.

## Output format
````markdown
# <Verb-first task title>
Applies to: <product/version/edition or TBD> | Audience: <role> | Time: <~N min or TBD>

<One sentence: what this achieves and when you need it.>

## Before You Begin
- <permission / version / data / backup>
> Warning: <irreversible or disruptive effect, if any>

## Steps
1. <action with exact label, command or value>
   ```<language>
   <command>
   ```
2. If <condition>, <action>. Otherwise, <action>.

## Verify
<expected result / output / state>

## Troubleshooting
| Symptom | Likely cause | Fix |

## Roll Back (if applicable)
1. ...

## Related
- <reference page> · <explanation page>

## Items to Verify
- [TBD – verify] <item> – <who can confirm>
````

## Quality checklist
- [ ] The guide serves exactly one goal, and the title names it with a verb.
- [ ] Preconditions and warnings appear before the steps that need them.
- [ ] Each step contains one action, conditions come before actions, and labels/commands are exact or marked `[TBD – verify]`.
- [ ] The reader can verify success, and risky changes have a rollback path.
- [ ] No tutorial-style teaching or concept explanation beyond one sentence; depth is linked.
- [ ] Inferred steps are labeled `[ASSUMPTION]` and listed for verification.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Writing a tutorial by accident: explaining concepts, adding "let's first understand ...". Keep the reader on the task and link out.
- Burying a warning inside step 6 after the reader has already run step 5. Move warnings to before the first affected step.
- Covering every option "for completeness". Document the variants that change the outcome; put the rest in reference.

## Example
Input: "How-to: rotate the API signing key without downtime, for integration developers. SME notes: create new key, deploy it alongside old, switch signing, remove old key after 24h."

Excerpt of output:
- Weak: "Keys are an important part of security. There are several approaches to key rotation, and you may want to consider ..."
- Strong: "## Before You Begin / - Admin role on the integration project. > Warning: deleting the old key before all clients switch breaks signature verification. ## Steps / 1. In **Settings > Signing keys**, select **Create key** `[TBD – verify label]`. 2. Deploy the new public key to your verifiers alongside the old one. ... ## Verify / New requests show `kid=<new key id>` in the signature header `[TBD – verify header name]`."
- Items to verify: "24-hour overlap is sufficient" `[ASSUMPTION]` – platform team.
