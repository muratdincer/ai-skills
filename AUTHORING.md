# Authoring Guide

How to write and maintain skills in this library. Every skill must follow these rules so that it works in any AI tool and both language versions stay consistent.

## 1. Location and files

```
skills/<category>/<role>/<area>/<skill-id>/
├── SKILL.md      # English
└── SKILL.tr.md   # Turkish
```

- `catalog/catalog.txt` is the single source of truth for categories, roles, areas, skill IDs and titles. Add a skill there first.
- The skill ID is globally unique, lowercase, hyphenated, at most 64 characters, and equals the folder name.
- Reference example: `skills/01-business-analysis/business-analyst/intake/request-intake-document/`.

## 2. Frontmatter

Authors write only three fields. `python3 scripts/sync.py` adds `name`, `license` and `metadata` (version, language, category, role, area, title) from the catalog.

```yaml
---
description: <What it does, one or two sentences>. Use when <triggers: situations, phrases, inputs>.
related: <comma-separated skill IDs that exist in the catalog>
prompt: <one realistic example request a user would type>
---
```

- `description` is the most important line: tools decide from it when to load the skill. Write it in the third person, state what the skill does and when to use it, and keep it at most 1024 characters (aim for 250-450).
- The Turkish file has a Turkish `description` and `prompt`. `related` is identical in both files.
- Only link skills that exist in the catalog.

## 3. Body structure

The body starts with an H1 title (the catalog title in that language, in title case) and uses these sections in this order:

| English | Türkçe | Content |
|---|---|---|
| Purpose | Amaç | 1-3 sentences: what outcome the skill produces and why it matters |
| When to use | Ne zaman kullanılır | 2-4 concrete situations |
| When not to use | Ne zaman kullanılmaz | 1-3 cases, each pointing to the better skill by ID in backticks |
| Inputs | Girdiler | "Required:" and "Optional:" lists; what to do if a required input is missing |
| Process | Süreç | 6-12 numbered, concrete steps an AI can follow |
| Output format | Çıktı formatı | A fenced markdown template of the deliverable |
| Quality checklist | Kalite kontrol listesi | 4-7 `- [ ]` checks the AI runs before answering |
| Common pitfalls | Sık yapılan hatalar | 2-4 domain mistakes and how to avoid them |
| Example | Örnek | A short input and an excerpt of output |

Target length: 60-130 lines per file. Dense and specific beats long and generic.

## 4. Content rules

1. **Tool-agnostic.** Never mention a specific AI product, model, tool call, file system access or slash command. Write instructions any chat model can follow with only the conversation as input. "Ask the user" is fine; "use the Read tool" is not.
2. **Methodology-independent.** Do not assume Scrum, Kanban, SAFe or Waterfall. Use neutral terms ("iteration/sprint", "backlog", "work item"). If a step differs by methodology, say "if the team works in fixed iterations..." rather than naming a framework as a requirement.
3. **No fabrication.** When information is missing, the skill must mark it (`[UNKNOWN]`, `[ASSUMPTION]`, `[TBD]`; Turkish: `[BİLİNMİYOR]`, `[VARSAYIM]`, `[TBD]`) or ask, never invent names, numbers, dates or money.
4. **Ask only what blocks.** Skills ask for required inputs only; everything else becomes an open question in the output.
5. **Name standards precisely** where they are the common reference (ISO/IEC/IEEE 29148, ISO 29119, WCAG 2.2, OWASP ASVS, KVKK/GDPR, BPMN 2.0, C4, arc42, DORA). Do not quote paid standards verbatim.
6. **Senior audience.** Do not explain basic concepts; give expert-level steps, heuristics and checks.
7. **Privacy.** Skills that handle personal data must remind to mask or minimize it.
8. **Separate what was said from what is inferred.** Every inference is labeled as such and ends up in assumptions or open questions, so the reader knows what the output rests on.
9. **Self-check loop.** The last quality-checklist item tells the AI to revise and re-run the checklist when any check fails, before answering.
10. **Hand off.** The last process step suggests the next skill from `related` when the user's goal continues beyond this skill. Skills stay independently usable; chaining is a suggestion, not a dependency.
11. **Interactive elicitation.** When a skill has to gather information from the user, it asks one focused question at a time (or a short numbered batch of at most 5), and uses anything the user already supplied instead of asking again.
12. **Contrast examples.** Where quality is subtle (stories, criteria, messages, review comments), the Example shows a weak version next to the strong one.
13. **No time-sensitive statements** ("as of this year...", tool versions). Name stable standards instead.

## 5. Language rules

- The Turkish file is written in natural, professional Turkish, not a word-for-word translation. Keep the same structure, steps, template fields and checks.
- Keep widely used English industry terms where Turkish teams use them (backlog, sprint, pull request, commit, pipeline, deployment, rollback, SLA, KPI, OKR, stakeholder may be "paydaş"). On first use, a Turkish equivalent can be added in parentheses.
- Use the Turkish characters ç, ğ, ı, İ, ö, ş, ü correctly.
- Section headings must be exactly the ones in the table above.

## 6. Structural contract (enforced by `sync.py --check`)

- Both files contain all nine section headings of section 3, in order.
- The Process section is a numbered list with 6-14 steps, and both languages have the same number of steps.
- The Quality checklist has 4-9 `- [ ]` items, the same number in both languages.
- Each file is 40-200 lines.
- `name` never contains reserved vendor words; `description` has no XML tags and is at most 1024 characters.

## 7. Validation

```bash
python3 scripts/catalog.py        # validate catalog, regenerate CATALOG.md / CATALOG.tr.md
python3 scripts/sync.py           # normalize frontmatter of all skills
python3 scripts/sync.py --check   # CI mode: fail on missing files, bad links, unnormalized files
```

## 8. Versioning

Bump `metadata.version` in both files (SemVer) when a skill's behavior or output format changes, and note it in `CHANGELOG.md`.
