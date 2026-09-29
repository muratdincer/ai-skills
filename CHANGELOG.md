# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning: [SemVer](https://semver.org/).

## [1.0.0] - 2026-09-28
### Added
- 420 skills in 15 categories and 39 roles, each in English (`SKILL.md`) and Turkish (`SKILL.tr.md`).
- Catalog (`CATALOG.md`, `CATALOG.tr.md`), per-skill usage guide (`GUIDE.md`, `GUIDE.tr.md`), tool setup guide (`USAGE.md`, `USAGE.tr.md`) and methodology guide (`METHODOLOGIES.md`, `METHODOLOGIES.tr.md`).
- Scripts: `catalog.py` (validate + render catalog), `sync.py` (normalize/validate frontmatter), `guide.py` (render guide), `export.py` (skills, zip, bundle, agents-md, cursor-rules).
- CI workflow validating the library on every push.
- Structural contract in `sync.py --check`: section order, 6-14 process steps, 4-9 checklist items, EN/TR parity, 40-200 lines.
- Practices adopted after comparing public skill libraries: self-check loop, hand-off to the next skill, labeled inferences, one-question-at-a-time elicitation, weak-vs-strong examples.
- 10 skills added from that comparison: `requirements-interview`, `edge-case-elicitation`, `bias-check`, `pestle-analysis`, `porters-five-forces`, `competitive-battle-card`, `value-proposition-canvas`, `press-release-faq`, `product-sunset-plan`, `api-deprecation-plan`.
