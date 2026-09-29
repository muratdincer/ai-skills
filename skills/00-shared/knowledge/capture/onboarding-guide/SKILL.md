---
description: Writes an onboarding guide that takes a newcomer to a team, department or project through context, ways of working, tools and access, key people, vocabulary and a sequenced set of first tasks with clear "you are ready when" milestones. Use when a team expects new members, contractors or transfers, when existing onboarding is scattered across wikis and chats, or when someone asks to "write an onboarding guide" for a role or team.
related: onboarding-plan-30-60-90, technical-onboarding, handover-document, glossary-builder, kb-article
prompt: Write an onboarding guide for new business analysts joining our payments team.
---

# Write an Onboarding Guide

## Purpose
Shorten the time until a newcomer contributes independently, and make it independent of who happens to be available to explain things. The guide gives a reusable path: what to understand, whom to meet, what to set up, and what to do first, in order.

## When to use
- A team expects new members, contractors or internal transfers.
- Onboarding knowledge is scattered across wikis, chats and people.
- Newcomers repeatedly ask the same questions or take long to become productive.

## When not to use
- A personal plan with goals for one specific hire's first three months. Use `onboarding-plan-30-60-90`.
- Setting up a developer environment and codebase walkthrough in depth. Use `technical-onboarding`.
- Transferring ownership of a specific system or project. Use `handover-document`.

## Inputs
Required:
- The team or project, and the role(s) the guide is for.

Optional, improves quality:
- Team mission, products/systems, stakeholders, working agreements, meeting cadence.
- Tool list and access request process, existing docs, glossary, org chart.
- Typical first tasks and what "productive" means for this role.

If the team or role is missing, ask. Gather the rest with focused questions in batches of at most 5, reusing anything already provided; leave unanswered items as `[TBD]` for the guide owner.

## Process
1. Define the audience (role, seniority, internal or external) and the target: what the newcomer should be able to do independently, and by when. Mark a proposed target `[ASSUMPTION]` if not given.
2. Write the context layer: why the team exists, whom it serves, what it owns, how it fits in the organization, and current priorities. Keep it to what a newcomer needs in week one.
3. Describe ways of working: planning cadence, recurring meetings and their purpose, how work items flow, definitions of ready/done if used, decision and escalation paths, communication norms (which channel for what, response expectations).
4. List tools and access as a checklist: tool, purpose, how to request, typical lead time, who approves. Order by what blocks the first tasks. Never include credentials.
5. Build the people map: key contacts by role (manager, buddy, product/business counterpart, tech lead, operations, key stakeholders) and what to go to each for. Use roles where names are unknown.
6. Collect the vocabulary: team-specific terms, acronyms and system names with one-line definitions, or point to the glossary.
7. Sequence the first tasks from low-risk to real contribution (read, shadow, pair, do with review, do alone), each with its learning goal and a "done" signal.
8. Define milestones as observable readiness checks per phase (for example first week, first month), not only a list of activities.
9. Add a feedback loop: when the newcomer and buddy check in, and how the newcomer reports gaps in the guide so it is updated.
10. Assign guide ownership and a review interval; mark any information that changes often so it links to a source instead of being copied.
11. If the goal continues, suggest the next skill: `onboarding-plan-30-60-90` for a personal plan, `technical-onboarding` for engineering setup, or `glossary-builder` if the vocabulary section is large.

## Output format
```markdown
# Onboarding Guide: <team/project> — <role>
For: <audience> · Goal: independent on <capability> by <time or TBD> · Owner: <role> · Review: <interval>

## 1. Why We Exist and What We Own
## 2. How We Work
- Cadence and meetings: ... · Work flow: ... · Decisions and escalation: ... · Communication norms: ...
## 3. Tools and Access
| Tool | Purpose | How to request | Lead time | Approver | Done |
|---|---|---|---|---|---|
## 4. People to Meet
| Role / name | Go to them for | When to meet |
|---|---|---|
## 5. Vocabulary
- <term>: <definition>
## 6. First Tasks
| # | Task | Mode (read/shadow/pair/review/alone) | Learning goal | Done when |
|---|---|---|---|---|
## 7. Milestones
- End of week 1: <observable readiness check>
- End of month 1: ...
## 8. Feedback and Help
- Buddy check-ins: ... · Report guide gaps to: ...
## Open Items for the Guide Owner
- [TBD] ...
```

## Quality checklist
- [ ] The guide states what "independent" means for the role and by when (or marks it `[ASSUMPTION]`/`[TBD]`).
- [ ] Access items are ordered by what blocks the first tasks and include lead times or `[TBD]`.
- [ ] First tasks progress from observing to doing alone, each with a done signal.
- [ ] Milestones are observable checks, not activity lists.
- [ ] No credentials or unnecessary personal data; frequently changing facts link to a source.
- [ ] Nothing about the team is invented; gaps are listed for the guide owner.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Dumping every link on day one. Sequence information by when it is needed; week one is context, access and people.
- Forgetting access lead times, so the newcomer waits idle for a week. Request blocking access before the start date.
- No owner for the guide. It becomes outdated after the first reorganization; assign an owner and ask each newcomer to fix one gap.

## Example
Input: "New business analysts joining the payments team. They need to understand card flows, our backlog tool and the fraud team."

Excerpt of output:
- Goal: writes and refines a work item for a card payment change with only review support by end of month 1 `[ASSUMPTION]`.
- Access: backlog tool — for work items — request via `[UNKNOWN: access process]` — lead time `[TBD]`.
- First task 2: shadow a refinement session with the fraud team — learning goal: understand chargeback rules — done when: can explain the chargeback flow in own words to the buddy.
