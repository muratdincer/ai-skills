---
name: user-guide
description: "Writes a task-based user guide for a product or feature, organized around what users need to accomplish, with prerequisites, numbered steps, expected results, screenshot placeholders, troubleshooting and cross-links. Use when end users or administrators need documentation for a new or changed feature, when a release needs user-facing docs, or when an existing manual is feature-oriented and hard to follow."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 12-technical-writing
  role: technical-writer
  area: docs
  title: "Write a user guide"
  related: "how-to-guide, tutorial, docs-information-architecture, style-guide-check, faq-builder"
  prompt: "Write the user guide section for our new invoice approval workflow for finance approvers, based on these specs and screen names."
---

# Write a User Guide

## Purpose
Give a specific audience the documentation they need to complete real tasks with the product correctly and confidently, organized by their goals rather than by the product's menus.

## When to use
- A new or changed feature needs end-user or administrator documentation.
- An existing manual describes screens and fields but not how to get work done.
- Support tickets show users repeatedly failing at the same tasks.

## When not to use
- Teaching a newcomer through a single guided learning path. Use `tutorial`.
- A single, focused recipe for experienced users. Use `how-to-guide`.
- Organizing a whole documentation set. Use `docs-information-architecture`.

## Inputs
Required:
- The product or feature and its behavior (specs, stories, UI labels, demo notes or access to descriptions of the screens).
- The target audience (role, experience level).

Optional, improves quality:
- Style guide and terminology list, existing docs, support ticket themes.
- Permissions and roles, known limitations, release version.

If the feature behavior or audience is unknown, ask for it. Do not describe UI elements or behavior that the input does not confirm.

## Process
1. Define the audience and their goals; list the top tasks they perform with the feature, ordered by frequency and importance.
2. Build a task outline: overview, prerequisites (access, roles, data), core tasks, advanced tasks, troubleshooting, reference (fields, statuses, limits).
3. For each task, write a title in imperative form that names the goal ("Approve an invoice"), not the screen.
4. Write a one- or two-sentence context: when and why to do this task.
5. List prerequisites specific to the task (permissions, prior steps, required data).
6. Write numbered steps, one action per step, using exact UI labels in bold and the order the user experiences; put the result after the step where it matters ("The invoice moves to Approved").
7. Add screenshot or diagram placeholders only where they reduce ambiguity, with alt text describing the purpose: `[Screenshot: <what it shows>]`.
8. Add notes, warnings and tips sparingly, placed before the step they concern; warnings describe consequence and how to avoid it.
9. Write troubleshooting entries as symptom → cause → fix, from known issues or support themes; mark guesses as `[ASSUMPTION]` for review.
10. Mark any unconfirmed behavior, label or limit `[TBD – confirm with product]` and list them as review questions for the SME.
11. If the user's goal continues, suggest `style-guide-check` before publishing, `faq-builder` for recurring questions or `docs-information-architecture` to place the guide in the doc set.

## Output format
```markdown
# <Feature> User Guide
Audience: <role> | Applies to: <product/version> | Last reviewed: <date or TBD>

## Overview
<what the feature does for this audience, 2-3 sentences>

## Before You Begin
- <access, role, data>

## <Task 1: imperative goal>
<context sentence>
**Prerequisites:** ...
1. Go to **<Menu>** > **<Page>**.
2. Select **<Button>**.
   The <object> opens. [Screenshot: <what it shows>]
3. ...
> **Warning:** <consequence and how to avoid>

**Result:** <what the user sees when done>

## Troubleshooting
| Symptom | Cause | Fix |

## Reference
| Field / status | Meaning | Allowed values |

## Review Questions for SMEs
```

## Quality checklist
- [ ] Tasks are named by user goals, not by screens or features.
- [ ] Each step has one action and uses exact UI labels.
- [ ] Every task states its result so users know they succeeded.
- [ ] Nothing about behavior or UI is invented; unconfirmed items are marked `[TBD]`.
- [ ] Warnings appear before the risky step, not after.
- [ ] The language fits the stated audience and follows the style guide if given.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Documenting the UI field by field ("The Status field shows the status"). Explain what users do and why.
- Mixing conceptual explanation into steps. Keep concepts in the overview or a linked explanation.
- Screenshots for every step; they age fast. Use them only where text is ambiguous.

## Example
Input: "Finance approvers can approve or reject invoices over 10k from the Approvals inbox; rejection requires a reason."

Excerpt of output:
- Weak: "Approvals screen: This screen has an Approve button and a Reject button."
- Strong: "## Reject an invoice / 1. In **Approvals**, open the invoice. 2. Select **Reject**. 3. Enter the reason in **Rejection reason** (required). 4. Select **Confirm**. **Result:** The invoice returns to the submitter with your reason. `[TBD – confirm whether the submitter is notified by email]`"
