---
name: information-architecture
description: "Structures the information architecture of a product or site, producing a content inventory, organization scheme, sitemap hierarchy, navigation model, labeling system and a card sort or tree test plan to validate it. Use when a product, portal or documentation site is being created or restructured, when users \"can't find things\", or when navigation and menu labels must be decided."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Structure information architecture"
  related: "user-flow, wireframe-spec, docs-information-architecture, research-plan, persona"
  prompt: "Restructure the navigation of our HR self-service portal; employees can't find leave, payroll and expense pages."
---

# Structure Information Architecture

## Purpose
Organize content and functions so users can predict where things are and what labels mean, and validate that structure with users before it is built, reducing findability failures and support load.

## When to use
- A new product, portal or site is being designed and needs a sitemap and navigation.
- Users report they cannot find features or content, or search is used as a workaround.
- Two products or sections are being merged and structures must be reconciled.

## When not to use
- The need is the step sequence for one task. Use `user-flow`.
- The structure is for technical documentation (tutorials, how-tos, reference). Use `docs-information-architecture`.
- The IA is settled and a single screen must be specified. Use `wireframe-spec`.

## Inputs
Required:
- The product or site scope and its main user groups.

Optional, improves quality:
- Current sitemap or menu, content inventory, analytics (top pages, search terms, exits), support tickets, personas, business priorities, platform constraints (mobile tab bar limits).

If scope or user groups are missing, ask for them. Missing inventory or analytics becomes a listed gap, not invented data.

## Process
1. Define user groups and their top tasks (aim for the 5-10 tasks that drive most visits); note tasks from evidence vs. `[ASSUMPTION]`.
2. Build or review the content inventory: each item with type, owner, audience, frequency of use and status (keep, merge, remove, create).
3. Choose the organization scheme per level: task-based, audience-based, topic-based, or exact (alphabetical, chronological). Avoid org-chart structure unless users think in departments.
4. Draft the hierarchy (sitemap) at most 3 levels deep where possible, with 5-9 items per level in primary navigation and the top tasks reachable within 2 clicks/taps.
5. Define the navigation model: global, local, contextual, utility, footer, search and mobile adaptation; state which items appear where.
6. Write labels in the users' vocabulary (use search logs and interview language), consistent in grammar, mutually exclusive and without internal jargon; list synonyms for search.
7. Plan validation: an open or hybrid card sort to discover mental models (15-30 participants for quantitative patterns), then a tree test on the draft hierarchy with task scenarios and success targets.
8. Define tree-test tasks and success metrics: direct success, indirect success, first-click correctness, time; set a target (e.g. 70% success per task `[ASSUMPTION]`).
9. Record governance: who owns each section, how new content is placed, and when labels may change.
10. List assumptions, risks and open questions, and suggest `user-flow` and `wireframe-spec` for the next step, or `research-plan` to schedule the validation study.

## Output format
```markdown
# Information Architecture: <product / site>
User groups: <...> · Scope: <...>

## Top Tasks
| # | Task | User group | Evidence |
|---|---|---|---|

## Content Inventory (summary)
| Item | Type | Audience | Use | Action |
|---|---|---|---|---|

## Organization Scheme
<scheme per level and rationale>

## Sitemap
- 1 <Label>
  - 1.1 <Label>

## Navigation Model
<global, local, contextual, utility, search, mobile>

## Labeling
| Label | Meaning / contents | Rejected alternatives | Search synonyms |
|---|---|---|---|

## Validation Plan
- Card sort: <type, participants, analysis>
- Tree test: <tasks, correct paths, success target>

## Governance, Assumptions and Open Questions
- ...
```

## Quality checklist
- [ ] Top tasks are identified and each is reachable within two levels.
- [ ] The organization scheme reflects users' mental models, not the org chart.
- [ ] Labels are user vocabulary, consistent and non-overlapping.
- [ ] Depth and breadth are balanced; no level is a "misc" or "other" bucket.
- [ ] A card sort and/or tree test with success targets is planned before build.
- [ ] Evidence-based tasks and labels are distinguished from assumptions.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mirroring departments ("HR Operations", "Finance Services"). Users think "Request leave", "My payslip".
- Clever or branded labels. Plain words beat creative ones for findability.
- Validating IA with a visual prototype. Tree-test the hierarchy alone so visuals do not mask structure problems.

## Example
Input: "Employees can't find leave, payroll and expense pages in the HR portal."

Excerpt of output:
- Top tasks (from search logs `[ASSUMPTION: logs not yet provided]`): request leave, view payslip, submit expense, update bank details.
- Before: HR Operations > Time Management > Absence Requests. After: Time off > Request time off.
- Tree test task: "You want to take next Friday off. Where would you go?" Correct path: Time off > Request time off. Target: 80% direct success.
