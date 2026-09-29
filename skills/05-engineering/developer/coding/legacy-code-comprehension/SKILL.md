---
description: "Builds a working map of unfamiliar or legacy code: entry points, modules and their responsibilities, main runtime flows, data stores, external integrations, hidden business rules, dead or risky areas and safe places to change, with every conclusion tied to evidence in the code. Use when a developer inherits a system, must change code nobody fully understands, plans a modernization, or asks how an old codebase works."
related: "code-explanation, refactoring, tech-debt-assessment, modernization-assessment, business-rules-catalog"
prompt: "I inherited this billing module with no documentation. Here is the folder structure and the main classes; help me understand how an invoice gets created."
---

# Understand Legacy Code

## Purpose
Turn an unfamiliar codebase into a map a developer can act on: where things happen, which rules live where, what is dangerous to touch and where to start, while keeping clear what was seen in the code and what is still a guess.

## When to use
- A team inherits a system or module without reliable documentation or original authors.
- A change must be made in code whose flow and rules are not understood.
- A modernization, migration or rewrite needs an inventory of current behavior and hidden rules.

## When not to use
- A single function or file needs explaining. Use `code-explanation`.
- The goal is to improve the code structure step by step. Use `refactoring`.
- The goal is a prioritized debt inventory for decision makers. Use `tech-debt-assessment`.

## Inputs
Required:
- Access to code excerpts: folder tree, entry points or the files around the area of interest.
- The question or change that drives the exploration (for example "how is an invoice created").

Optional, improves quality:
- Build and deployment files, database schema, configuration, logs, commit history highlights, existing tickets, anyone who remembers the system.

If only part of the code is available, map what is visible, mark gaps `[NOT SEEN]`, and ask for the next most informative files one small batch at a time.

## Process
1. Anchor on the driving question; comprehension without a goal expands forever.
2. Identify the tech stack and entry points: main programs, HTTP routes, scheduled jobs, message consumers, UI screens, stored procedures and triggers.
3. Sketch the module map: each package or component with a one-line responsibility inferred from names, dependencies and code, and its inbound/outbound dependencies.
4. Trace the main flow for the driving question from entry point to persistence and outbound calls; record file and function names at each hop.
5. Inventory data: tables or files touched, who writes them, and data that other systems read directly.
6. Extract hidden business rules: conditionals on status codes, magic numbers, date cut-offs, special customers, configuration flags; record each with its location.
7. Mark risk zones: no tests, high churn or complexity, reflection or dynamic dispatch, shared global state, copy-pasted variants, code that looks dead (confirm with usage search or logs before deleting).
8. Identify seams: places where behavior can be observed or substituted for testing (interfaces, configuration, boundaries), and the safest point to make the requested change.
9. Propose characterization tests that pin current behavior before changes.
10. Label every conclusion as `[SEEN in <file>]` or `[INFERRED]`, and list open questions with who or what (logs, database, business owner) can answer them.
11. If the goal continues, suggest `refactoring` to improve the area safely, `business-rules-catalog` to document the extracted rules or `tech-debt-assessment` to prioritize the risks found.

## Output format
```markdown
# Legacy Code Map: <system/module>
Driving question: <...> · Coverage: <what was seen / not seen>

## Entry Points
| Type | Name | Location |

## Module Map
| Module | Responsibility | Depends on | Evidence |

## Main Flow: <question>
1. <hop> — <file:function> — [SEEN/INFERRED]

## Data Touched
| Store/table | Read/Write | By | Shared with |

## Hidden Business Rules
| Rule | Location | Evidence | Confirm with |

## Risk Zones
## Seams and Safe Change Point
## Characterization Tests to Add
## Open Questions
```

## Quality checklist
- [ ] The map answers the driving question with a traceable flow.
- [ ] Every statement is tagged `[SEEN in ...]` or `[INFERRED]`; unseen areas are marked `[NOT SEEN]`.
- [ ] Hidden business rules include location and a way to confirm them.
- [ ] "Dead code" is only claimed with evidence or marked as suspected.
- [ ] A concrete safe change point and characterization tests are proposed.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- Reading top-down through every file instead of following one flow from an entry point.
- Trusting names and comments over behavior; legacy names often lie after years of changes.
- Deleting "unused" code that is called via reflection, configuration, scheduled jobs or another system reading the database.
- Missing logic that lives outside the application: stored procedures, triggers, cron scripts, ETL jobs.

## Example
Input: "Billing module, folders `jobs/`, `core/`, `db/procs/`. How is an invoice created?"

Excerpt of output:
1. `jobs/NightlyBilling.run()` selects contracts with `status IN (2,5)` `[SEEN in NightlyBilling.java]`
2. Calls stored procedure `sp_create_invoice` `[SEEN]`; its body `[NOT SEEN]`, request `db/procs/sp_create_invoice.sql` next.
- Hidden rule: contracts with `customer_type = 'K'` skip VAT `[SEEN in TaxCalc.java:88]` — confirm meaning of `'K'` with the finance owner.
