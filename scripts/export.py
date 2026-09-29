#!/usr/bin/env python3
"""Export skills for any AI tool.

Formats
  skills        Flat Agent Skills layout: <dest>/<skill-id>/SKILL.md (in the chosen language).
                For tools that read SKILL.md folders (skills directories of coding agents and chat apps).
  zip           One <skill-id>.zip per skill, for tools that upload skills through a UI.
  bundle        One Markdown file with an index and the full text of every selected skill.
                For custom assistants, projects, knowledge files or a system prompt.
  agents-md     An AGENTS.md index (name, description, path) so any agent that reads AGENTS.md
                can open the right skill file on demand. Use together with `skills`.
  cursor-rules  One .mdc rule per skill (description + agent-requested), for rule-based editors.

Filters
  --lang en|tr            language of the exported content (default en)
  --category 01-...       repeatable; category directory name
  --role business-analyst repeatable; role directory name
  --skill <id>            repeatable; single skills

Examples
  python3 scripts/export.py skills --lang tr --dest ~/.agent-skills
  python3 scripts/export.py bundle --role business-analyst --dest dist/ba.md
  python3 scripts/export.py agents-md --dest AGENTS.md --skills-root .agent-skills
"""
import argparse, re, shutil, sys, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import parse, skills, ROOT  # noqa: E402

FILES = {"en": "SKILL.md", "tr": "SKILL.tr.md"}



def unquote(value):
    """Parse a YAML scalar written by sync.py; collapse any stray escaping left by hand edits."""
    v = value.strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        v = v[1:-1]
    while '\\"' in v or '\\\\' in v:
        v = v.replace('\\\\', '\\').replace('\\"', '"')
    return v

def selected(args):
    tree, errors = parse()
    if errors:
        sys.exit("\n".join(errors))
    for c, r, a, s in skills(tree):
        if args.category and c["dir"] not in args.category:
            continue
        if args.role and r["dir"] not in args.role:
            continue
        if args.skill and s["id"] not in args.skill:
            continue
        src = ROOT / s["path"] / FILES[args.lang]
        if src.exists():
            yield c, r, a, s, src


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    fm = {}
    for line in (m.group(1) if m else "").splitlines():
        kv = re.match(r"^\s*([A-Za-z_-]+):\s*(.*)$", line)
        if kv and kv.group(2):
            fm[kv.group(1)] = unquote(kv.group(2))
    return fm, (m.group(2) if m else text).lstrip("\n")


def export_skills(items, dest):
    for *_, s, src in items:
        out = dest / s["id"]
        out.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, out / "SKILL.md")


def export_zip(items, dest):
    dest.mkdir(parents=True, exist_ok=True)
    for *_, s, src in items:
        with zipfile.ZipFile(dest / f"{s['id']}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            z.write(src, f"{s['id']}/SKILL.md")


def export_bundle(items, dest, lang):
    items = list(items)
    title = "Yapay Zeka Skill Paketi" if lang == "tr" else "AI Skill Bundle"
    intro = ("Aşağıdaki skill'ler bir iş tanımıdır. Kullanıcının isteğine uyan skill'i açıklamasına göre seç, "
             "Süreç adımlarını uygula ve Çıktı formatını kullan. Hiçbiri uymuyorsa normal yanıt ver."
             if lang == "tr" else
             "Each skill below is a job definition. Pick the skill whose description matches the user's request, "
             "follow its Process and use its Output format. If none matches, answer normally.")
    lines = [f"# {title}", "", intro, "", "## Index" if lang == "en" else "## Dizin", ""]
    bodies = []
    for c, r, a, s, src in items:
        fm, body = frontmatter(src.read_text(encoding="utf-8"))
        lines.append(f"- `{s['id']}`: {fm.get('description', '')}")
        body = re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + 2) + " ", body, flags=re.M)
        bodies += ["", "---", "", f"## Skill: `{s['id']}`", "", body.rstrip()]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines + bodies) + "\n", encoding="utf-8")


def export_agents_md(items, dest, lang, skills_root):
    head = ("# Skill'ler\n\nBir görev aşağıdaki açıklamalardan birine uyuyorsa, başlamadan önce ilgili SKILL.md dosyasını "
            "oku ve talimatlarını uygula.\n" if lang == "tr" else
            "# Skills\n\nWhen a task matches one of the descriptions below, read that SKILL.md before starting "
            "and follow its instructions.\n")
    lines, current = [head], None
    for c, r, a, s, src in items:
        if (c["dir"], r["dir"]) != current:
            current = (c["dir"], r["dir"])
            lines.append(f"\n## {c[lang]} / {r[lang]}\n")
        fm, _ = frontmatter(src.read_text(encoding="utf-8"))
        lines.append(f"- `{skills_root}/{s['id']}/SKILL.md` – {fm.get('description', '')}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_cursor(items, dest):
    dest.mkdir(parents=True, exist_ok=True)
    for *_, s, src in items:
        fm, body = frontmatter(src.read_text(encoding="utf-8"))
        desc = fm.get("description", "").replace('"', "'")
        (dest / f"{s['id']}.mdc").write_text(
            f'---\ndescription: "{desc}"\nalwaysApply: false\n---\n\n{body}', encoding="utf-8")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("format", choices=["skills", "zip", "bundle", "agents-md", "cursor-rules"])
    p.add_argument("--dest", required=True, type=Path)
    p.add_argument("--lang", choices=FILES, default="en")
    p.add_argument("--category", action="append")
    p.add_argument("--role", action="append")
    p.add_argument("--skill", action="append")
    p.add_argument("--skills-root", default=".agent-skills", help="path prefix used in agents-md links")
    args = p.parse_args()
    items = list(selected(args))
    if not items:
        sys.exit("no skills matched the filters")
    dest = args.dest.expanduser()
    {"skills": lambda: export_skills(items, dest),
     "zip": lambda: export_zip(items, dest),
     "bundle": lambda: export_bundle(items, dest, args.lang),
     "agents-md": lambda: export_agents_md(items, dest, args.lang, args.skills_root),
     "cursor-rules": lambda: export_cursor(items, dest)}[args.format]()
    print(f"exported {len(items)} skills ({args.lang}) as {args.format} -> {dest}")


if __name__ == "__main__":
    main()
