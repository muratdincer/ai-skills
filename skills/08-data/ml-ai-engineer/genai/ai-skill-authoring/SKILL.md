---
name: ai-skill-authoring
description: "Writes a new portable, bilingual skill (SKILL.md in English and SKILL.tr.md in Turkish) that follows this library's authoring guide, including catalog line, three-field frontmatter, the nine fixed sections, structural limits and content rules. Use when someone wants to add a skill to the library, turn a repeatable task or checklist into a skill, or review a draft skill for conformance."
license: MIT
metadata:
  version: "1.0.0"
  language: en
  category: 08-data
  role: ml-ai-engineer
  area: genai
  title: "Author a new AI skill"
  related: "prompt-design, llm-eval-set, document-review, technical-translation, style-guide-check"
  prompt: "Write a new skill for our library that helps a support engineer write a customer outage notice; give me the catalog line and both language files."
---

# Author a New AI Skill

## Purpose
Produce a skill that any chat model can follow with only the conversation as input, loads at the right moment because of a precise description, and passes the library's structural check in both languages on the first try.

## When to use
- A team has a repeatable task (a document, analysis or review) worth standardizing as a skill.
- A draft skill must be checked against the authoring guide before it is merged.
- An existing prompt or checklist should be converted into the library's skill format.

## When not to use
- It is a one-off instruction for a single feature. Use `prompt-design`.
- Only the Turkish or English text needs polishing without structural change. Use `technical-translation` or `document-review`.

## Inputs
Required:
- The task the skill performs, its target role, and 2-3 real situations in which it is used.
- The deliverable the skill produces (document, table, message, review).

Optional, improves quality:
- A good real example of the deliverable, known mistakes practitioners make, relevant standards.
- The intended category, role and area in the catalog; related existing skill IDs.

If the task or deliverable is unclear, ask one question at a time (at most 5 in a batch). Do not ask for optional inputs; list them as open questions.

## Process
1. Check for overlap: if an existing skill covers most of the task, propose extending it instead; otherwise pick a globally unique, lowercase, hyphenated ID (at most 64 characters) that equals the folder name.
2. Draft the catalog line: `- <id> | <EN title> | <TR title> | <EN one-liner> | <TR one-liner>` under the right `# category`, `## role`, `### area`; the folder is `skills/<category>/<role>/<area>/<id>/`.
3. Write frontmatter with only `description`, `related` and `prompt` (tooling adds name, license and metadata). The description is third person, states what it does and then "Use when ..." with triggers, has no XML tags, stays at most 1024 characters (aim for 250-450). `related` lists 2-5 IDs that exist in the catalog, identical in both files. `prompt` is one realistic user request.
4. Start the body with an H1 equal to the catalog title in title case, then the nine sections in order: Purpose, When to use, When not to use, Inputs, Process, Output format, Quality checklist, Common pitfalls, Example (Turkish: Amaç, Ne zaman kullanılır, Ne zaman kullanılmaz, Girdiler, Süreç, Çıktı formatı, Kalite kontrol listesi, Sık yapılan hatalar, Örnek).
5. Write Purpose (1-3 sentences on outcome and why it matters), When to use (2-4 concrete situations) and When not to use (1-3 cases, each naming a better skill by ID in backticks).
6. Write Inputs as "Required:" and "Optional:" lists, plus what to do when a required input is missing: ask only what blocks, one focused question at a time, reuse what the user already gave.
7. Write the Process as 6-14 numbered, concrete, expert-level steps; include marking unsupported items as `[UNKNOWN]`, `[ASSUMPTION]` or `[TBD]` (Turkish `[BİLİNMİYOR]`, `[VARSAYIM]`, `[TBD]`), separating stated facts from inferences, privacy masking when personal data is involved, and a last step that suggests the next skill from `related`.
8. Write the Output format as a fenced markdown template of the deliverable with placeholders, and a Quality checklist of 4-9 `- [ ]` items whose last item is the self-check loop ("All checks pass; if any fails, revise the output and re-run this checklist before answering.").
9. Write 2-4 Common pitfalls (domain mistake plus how to avoid it) and a short Example (input plus an output excerpt); when quality is subtle, show a weak version next to the strong one.
10. Apply the content rules: no AI product, tool call, file access or slash command; no methodology assumed (say "iteration/sprint", "backlog"); standards named precisely, never quoted verbatim; no time-sensitive statements; senior audience, no basics.
11. Write the Turkish file as natural professional Turkish, not word-for-word: same sections, same step count, same checklist count, same template fields, correct ç, ğ, ı, İ, ö, ş, ü, common English industry terms kept where Turkish teams use them.
12. Verify against the structural contract (each file 40-200 lines, target 60-130; identical step and checklist counts; valid related IDs), list open questions, and suggest `llm-eval-set` to test the skill on realistic prompts.

## Output format
```markdown
Catalog line:
- <id> | <EN title> | <TR title> | <EN one-liner> | <TR one-liner>
Path: skills/<category>/<role>/<area>/<id>/

--- SKILL.md ---
---
description: <what it does>. Use when <triggers>.
related: <id-1>, <id-2>, <id-3>
prompt: <realistic request>
---

# <EN Title In Title Case>
## Purpose
## When to use
## When not to use
## Inputs
## Process
## Output format
## Quality checklist
## Common pitfalls
## Example

--- SKILL.tr.md ---
<same frontmatter keys in Turkish except identical `related`; Turkish headings>

Conformance notes: <step count EN/TR, checklist count EN/TR, line counts, open questions>
```

## Quality checklist
- [ ] The description says what the skill does and when to use it, in third person, at most 1024 characters.
- [ ] All nine headings appear in order in both files, with the exact wording of the guide.
- [ ] Process has 6-14 steps and the checklist 4-9 items, with identical counts in both languages.
- [ ] Every `related` and "when not to use" ID exists in the catalog; `related` is identical in both files.
- [ ] No tool names, product names, methodology assumptions or time-sensitive claims; missing data is marked, never invented.
- [ ] The last process step hands off to a related skill and the last checklist item is the self-check loop.
- [ ] All checks pass; if any fails, revise the output and re-run this checklist before answering.

## Common pitfalls
- A vague description ("Helps with documents"). Tools load skills from this line; name the deliverable and concrete triggers.
- Generic steps ("Analyze the input", "Write the output"). Each step should contain a domain heuristic a junior would not know.
- Translating Turkish word for word, or letting the two files drift in structure. Keep structure identical, phrasing natural.

## Example
Input: "Skill for writing a customer outage notice."

Weak description: "Outage notice skill. Helps write notices."

Strong description: "Writes a customer-facing outage notice with impact, affected services, current status, next update time and workaround, in plain language without internal jargon. Use when an incident affects customers and a first or follow-up notice must be published."

Conformance notes excerpt: Process 9/9 steps, checklist 6/6 items, related `incident-communication, incident-response, customer-outage-notice` checked against the catalog.
