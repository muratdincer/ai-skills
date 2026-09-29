---
name: docs-information-architecture
description: "Designs or restructures the information architecture of a documentation set using the Diátaxis quadrants (tutorials, how-to guides, reference, explanation): audits existing pages, classifies and splits mixed content, defines navigation, naming and page types, and produces a target site map with a migration plan. Use when docs are hard to navigate, when pages mix learning, tasks, reference and concepts, when a new product or portal needs a documentation structure, or before a docs migration or consolidation."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 12-technical-writing
  role: technical-writer
  area: docs
  title: "Structure documentation"
  related: "tutorial, how-to-guide, user-guide, api-reference-docs, glossary-builder"
  prompt: "Here is our current docs sidebar with 60 pages; propose a restructure so developers can find setup, tasks and API reference faster."
---

# Structure Documentation

## Purpose
Give a documentation set a structure that matches what readers are trying to do (learn, accomplish a task, look something up, understand), so each page has one job, readers find it predictably, and writers know where new content belongs.

## When to use
- Readers or support teams report that docs are hard to navigate or search.
- Pages mix tutorial steps, task recipes, parameter tables and concept explanation.
- A new product, API or developer portal needs its documentation structure defined.
- Before migrating, merging or consolidating multiple doc sites or wikis.

## When not to use
- Writing a single learning path. Use `tutorial`.
- Writing a single task page. Use `how-to-guide`.
- Generating reference content for an API. Use `api-reference-docs`.

## Inputs
Required:
- The current inventory (sidebar, site map, page list with titles, or links) or, for a new product, the product scope and main user tasks.
- The primary audiences (e.g. end users, administrators, integration developers, operators).

Optional, improves quality:
- Analytics or search logs (top pages, failed searches), support ticket themes.
- Product areas and naming, existing style guide or glossary, platform constraints (nav depth, versioning).

If neither an inventory nor a product scope is provided, ask for it. Do not invent page traffic, ticket counts or reader research; mark such claims `[UNKNOWN]` and propose how to gather them.

## Process
1. Build an inventory table: each page with title, current location, audience and apparent purpose; ask for a sample of page contents if titles alone are ambiguous.
2. Classify each page into one Diátaxis type (tutorial, how-to, reference, explanation) by its reader need, not its title; mark pages that mix types as "split" and state which parts go where.
3. Flag problems with evidence: duplicates, orphan pages, outdated or product-internal content, dead ends, titles that do not say what the page does; label inferred judgments `[ASSUMPTION]`.
4. Decide the top-level axis: by Diátaxis type within each product area, or product area within each type; choose based on product breadth and audience overlap, and state the rationale.
5. Draft the target site map with at most three navigation levels, a landing page per section that routes by reader goal, and a clear home for release notes, troubleshooting and glossary.
6. Define naming conventions per page type (tutorials: "Build/Create ...", how-tos: verb-first task, reference: noun, explanation: "About/Understanding ..."), and URL/slug rules that survive renames.
7. Map every existing page to its target: keep, move, split, merge, rewrite, retire; retired and moved pages get redirects.
8. Identify gaps: reader goals with no page (from tickets, search terms or the product scope) and list them as new pages with type and priority.
9. Define ownership and upkeep: an owner per section, review cadence, and the rule for where new content goes.
10. Sequence the migration in waves (highest-traffic or highest-pain areas first) with redirect and link-check steps; list open questions and assumptions.
11. If the user's goal continues, suggest `tutorial`, `how-to-guide` or `api-reference-docs` to fill gaps, or `glossary-builder` to fix inconsistent terminology.

## Output format
```markdown
# Documentation IA: <product / site>
Audiences: <...> | Scope: <sites/sections covered>

## Findings
- <problem> – <evidence / pages> [ASSUMPTION if inferred]

## Structure Decision
Top-level axis: <type-first / area-first> – <rationale>

## Target Site Map
- <Section landing>
  - Tutorials: ...
  - How-to guides: ...
  - Reference: ...
  - Explanation: ...

## Naming and URL Conventions
| Page type | Title pattern | Slug pattern |

## Page Mapping
| Current page | Type | Action (keep/move/split/merge/rewrite/retire) | Target location | Redirect |

## Gaps (New Pages)
| Reader goal | Type | Priority | Source of evidence |

## Ownership and Governance
## Migration Waves
## Assumptions and Open Questions
```

## Quality checklist
- [ ] Every page has exactly one Diátaxis type, or a split plan stating where each part goes.
- [ ] Navigation depth is at most three levels and each section has a goal-based landing page.
- [ ] Every existing page has an action, and every moved or retired page has a redirect.
- [ ] Gaps are tied to evidence (tickets, searches, product scope) or labeled `[ASSUMPTION]`.
- [ ] Naming conventions are defined per page type and applied in the site map.
- [ ] Ownership and the "where does new content go" rule are stated.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Mirroring the org chart or the product's internal module names instead of reader goals. Name sections by what readers want to do or look up.
- Classifying by title ("Getting started" is not automatically a tutorial). Classify by what the content actually does for the reader.
- Restructuring without redirects, which breaks bookmarks, search ranking and in-product links.

## Example
Input: "Sidebar: Overview, Getting Started, Configuration, Webhooks, API, FAQ, Advanced, Misc (60 pages). Audiences: integration developers and admins."

Excerpt of output:
- Finding: "Configuration" (14 pages) mixes admin tasks with a full settings table – split into how-tos and a Settings reference `[ASSUMPTION: based on titles, confirm with page samples]`.
- Finding: "Advanced" and "Misc" say nothing about content; 9 pages redistributed, 3 retired as duplicates of Webhooks pages.
- Page mapping: "Webhooks" → split: "Receive your first webhook" (tutorial), "Verify webhook signatures" (how-to), "Webhook event types" (reference), "About webhook delivery and retries" (explanation).
