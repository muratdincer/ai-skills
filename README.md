# AI Skills for Software Teams

[Türkçe](README.tr.md)

A tool-agnostic library of **420 AI skills** covering every role in a software department, from request intake and meeting summaries to architecture decisions, test design, incident postmortems and hiring. Each skill is a small, focused job definition that any AI assistant can follow, in **English and Turkish**.

- **Portable:** plain Markdown in the open Agent Skills format (`SKILL.md` + YAML header). Works as a native skill, a rule file, a knowledge file, a system prompt or a pasted prompt.
- **Granular:** one skill = one job ("find gaps in requirements", "extract action items", "write a rollback plan"), so skills can be chained.
- **Reliable output:** every skill has inputs, numbered steps, an output template, a quality checklist and common pitfalls. Missing information is marked, never invented.
- **Methodology-independent:** usable in Waterfall, Scrum, Kanban, SAFe or hybrid setups. See [METHODOLOGIES.md](METHODOLOGIES.md).

## Structure

```
skills/<category>/<role>/<area>/<skill-id>/
├── SKILL.md      English
└── SKILL.tr.md   Turkish
```

| # | Category | Roles |
|---|---|---|
| 00 | Shared (cross-role) | Meetings, Communication, Documentation, Problem solving & decisions, Knowledge management |
| 01 | Business Analysis | Business Analyst, System Analyst |
| 02 | Product Management | Product Manager, Product Owner |
| 03 | Project & Delivery Management | Project Manager, Scrum Master / Agile Coach, Program Manager / PMO |
| 04 | Architecture | Enterprise, Solution and Software Architect |
| 05 | Software Engineering | Developer (backend/frontend/mobile), Tech Lead |
| 06 | Quality Assurance & Testing | QA Analyst, Test Automation Engineer, Performance Test Engineer |
| 07 | DevOps, SRE & Platform | DevOps/Platform Engineer, Release Manager, SRE |
| 08 | Data & AI | Data Architect, Data Engineer, DBA, Data/BI Analyst, Data Scientist / ML & AI Engineer |
| 09 | Security & Compliance | Security Architect / AppSec Engineer, GRC / Compliance |
| 10 | UX / UI Design | UX Researcher, UX/UI Designer, UX Writer |
| 11 | Support & IT Operations | Support Engineer (L1-L3), IT Service Management |
| 12 | Technical Writing | Technical Writer |
| 13 | Engineering Management & Leadership | Engineering Manager, CTO / VP / Director |
| 14 | Presales & Consulting | Presales / Solution Consultant |

Full tree with every skill: [CATALOG.md](CATALOG.md).

## Quick start

```bash
git clone https://github.com/muratdincer/ai-skills.git && cd ai-skills

# Agent Skills compatible tools: copy skills into the tool's skills folder
python3 scripts/export.py skills --dest ~/.claude/skills            # English
python3 scripts/export.py skills --lang tr --dest ~/.claude/skills  # Turkish

# Chat assistants: one knowledge file per role
python3 scripts/export.py bundle --role business-analyst --dest dist/business-analyst.md
```

Then just ask: *"Here is a request from sales, create an intake document and list what is missing."*

No setup at all? Open any `SKILL.md`, paste it into a chat, then write your request.

## Documentation

| Document | Content |
|---|---|
| [USAGE.md](USAGE.md) | Installing in different AI tools, export formats, invoking and chaining skills |
| [GUIDE.md](GUIDE.md) | Every skill with when to use it and an example request |
| [CATALOG.md](CATALOG.md) | The full category / role / area / skill tree |
| [METHODOLOGIES.md](METHODOLOGIES.md) | Which skills to use at each step of Waterfall, V-Model, Scrum, Kanban, XP, Lean, SAFe, DevOps, design thinking |
| [AUTHORING.md](AUTHORING.md) | Rules for writing and maintaining skills |

## Contributing

1. Add the skill to `catalog/catalog.txt`.
2. Write `SKILL.md` and `SKILL.tr.md` following [AUTHORING.md](AUTHORING.md).
3. Run `python3 scripts/catalog.py && python3 scripts/sync.py && python3 scripts/guide.py`.
4. Open a pull request; CI runs `sync.py --check`.

## Acknowledgements

Structure and practices were compared with, and partly inspired by, these public skill libraries and guides:
[Anthropic skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills),
[obra/superpowers](https://github.com/obra/superpowers),
[deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills),
[product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills),
[phuryn/pm-skills](https://github.com/phuryn/pm-skills),
[45ck/business-analysis-skills](https://github.com/45ck/business-analysis-skills).
No content was copied; ideas such as self-check loops, severity labels, separating the literal ask from the underlying need, and absent/weak/deferred gap classification were rewritten in this library's format.

## License

[MIT](LICENSE)
