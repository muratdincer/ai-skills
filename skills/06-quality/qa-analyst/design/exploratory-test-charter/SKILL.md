---
description: "Writes session-based exploratory test charters with a mission, target areas, resources, risks to probe, test heuristics and oracles, a timebox and a debrief template for notes, bugs and questions. Use when a new or changed feature needs discovery testing, when scripted tests are not yet available or not enough, or when someone asks for exploratory testing ideas."
related: test-scenarios-from-requirements, risk-based-testing, bug-report, heuristic-evaluation, test-summary-report
prompt: "Write exploratory test charters for the new bulk import of product prices from CSV. We have 2 testers for one afternoon."
---

# Write Exploratory Test Charters

## Purpose
Give exploratory testing a clear mission and boundaries so that sessions are focused on risk, results are reportable, and coverage can be discussed, while keeping the tester's freedom to learn and adapt.

## When to use
- A new or significantly changed feature needs fast feedback before or alongside scripted tests.
- Requirements are thin and the team needs to learn the product's real behavior.
- High-risk areas need a different angle than existing regression cases.

## When not to use
- You need repeatable scripted cases for regression. Use `test-case-writing`.
- You need a usability expert review against heuristics. Use `heuristic-evaluation`.
- You need to decide what to test first across the release. Use `risk-based-testing`.

## Inputs
Required:
- The feature or area to explore and what changed.

Optional, improves quality:
- Available people and time, known risks, recent defects, user profiles, environment and data.
- Existing scripted coverage to avoid duplication.

If the area to explore is unknown, ask for it. Everything else can be assumed and marked `[ASSUMPTION]`.

## Process
1. Identify risks and quality characteristics that matter for the area (data integrity, error handling, performance with volume, security, usability).
2. Split the area into charters of 45-120 minutes each, one mission per charter, using the form "Explore <target> with <resources> to discover <information/risk>".
3. For each charter list focus areas and explicit out-of-scope items.
4. Pick heuristics to guide ideas, e.g. SFDIPOT (structure, function, data, interfaces, platform, operations, time), CRUD, boundaries, interruptions, "goldilocks" (too big, too small, just right), variable data (encodings, locales), follow the data.
5. Define oracles: how a tester recognizes a problem (specification, comparable product, consistency with other screens, user expectations, logs, database state).
6. List resources: test accounts, sample files, tools categories (proxy, log viewer), data sets. Use synthetic data only.
7. Assign charters to testers by skill and risk; order by risk.
8. Provide a session notes template: timestamps, what was tested, ideas, bugs, questions, % on-charter vs setup vs bug investigation.
9. Provide debrief questions for after the session: what was covered, what was not, what new risks appeared, should a follow-up charter exist.

## Output format
```markdown
# Exploratory Charters: <feature>
| # | Charter (Explore / with / to discover) | Focus | Out of scope | Heuristics | Oracles | Timebox | Tester |
|---|---|---|---|---|---|---|---|

## Resources and Data
## Session Notes Template
- Charter #, tester, start/end
- Areas covered / not covered
- Bugs (IDs) · Issues/questions · Ideas for new charters
- Time split: setup % / testing % / bug investigation %
## Debrief Questions
```

## Quality checklist
- [ ] Each charter has a single mission and fits the timebox.
- [ ] Charters are ordered by risk and cover the areas that scripted tests do not.
- [ ] Each charter names at least one heuristic and one oracle.
- [ ] Test data is synthetic or masked.
- [ ] The debrief makes coverage and new risks reportable.

## Common pitfalls
- Charters that are too broad ("explore the app"). Narrow to a target and a risk.
- Charters written as step lists. Keep them as missions; steps kill exploration.
- Skipping the debrief, so findings and coverage are lost.

## Example
Input: "Bulk CSV import of product prices; 2 testers, one afternoon."

Excerpt of output:
| 1 | Explore CSV parsing with malformed and edge files to discover data corruption or silent skips | encodings (UTF-8 BOM, Windows-1254), delimiters, quotes, 0/negative prices | UI styling | Goldilocks, variable data | Price in DB equals file value; import summary counts | 90 min | Tester A |
| 2 | Explore partial failure and re-import to discover duplicate or lost price updates | row 5,000 of 10,000 fails, re-upload same file | | Interruptions, follow the data | Audit log, price history | 90 min | Tester B |
