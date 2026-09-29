#!/usr/bin/env python3
"""Parse catalog/catalog.txt, validate it and render CATALOG.md / CATALOG.tr.md."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "catalog" / "catalog.txt"
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse():
    tree, errors, seen = [], [], set()
    cat = role = area = None
    for n, raw in enumerate(SRC.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        m = re.match(r"^(#{1,3}) (.+)$", line)
        if m:
            parts = [p.strip() for p in m.group(2).split("|")]
            node = {"dir": parts[0], "en": parts[1], "tr": parts[2], "children": []}
            level = len(m.group(1))
            if level == 1:
                cat = node; tree.append(cat)
            elif level == 2:
                role = node; cat["children"].append(role)
            else:
                area = node; role["children"].append(area)
            continue
        if line.startswith("- "):
            parts = [p.strip() for p in line[2:].split("|")]
            if len(parts) != 5:
                errors.append(f"line {n}: expected 5 fields, got {len(parts)}"); continue
            sid = parts[0]
            if not ID_RE.match(sid) or len(sid) > 64:
                errors.append(f"line {n}: invalid id {sid}")
            if sid in seen:
                errors.append(f"line {n}: duplicate id {sid}")
            seen.add(sid)
            area["children"].append(dict(zip(["id", "en", "tr", "en_desc", "tr_desc"], parts),
                                         path=f"skills/{cat['dir']}/{role['dir']}/{area['dir']}/{sid}"))
    return tree, errors


def skills(tree):
    for c in tree:
        for r in c["children"]:
            for a in r["children"]:
                for s in a["children"]:
                    yield c, r, a, s


def render(tree, lang):
    tr = lang == "tr"
    total = sum(1 for _ in skills(tree))
    roles = sum(len(c["children"]) for c in tree)
    out = [f"# {'Skill Kataloğu' if tr else 'Skill Catalog'}", "",
           (f"{len(tree)} kategori, {roles} rol/alan, {total} skill." if tr
            else f"{len(tree)} categories, {roles} roles/areas, {total} skills."), "",
           "## " + ("Ağaç" if tr else "Tree"), "", "```"]
    for c in tree:
        out.append(f"{c['dir']}/  ({c[lang]})")
        for r in c["children"]:
            out.append(f"  {r['dir']}/  ({r[lang]})")
            for a in r["children"]:
                out.append(f"    {a['dir']}/  ({a[lang]}, {len(a['children'])})")
    out += ["```", ""]
    for c in tree:
        out += [f"## {c[lang]}", ""]
        for r in c["children"]:
            out += [f"### {r[lang]}", ""]
            for a in r["children"]:
                out += [f"**{a[lang]}**", "", "| ID | " + ("Skill | Açıklama" if tr else "Skill | Description") + " |", "|---|---|---|"]
                for s in a["children"]:
                    fname = "SKILL.tr.md" if tr else "SKILL.md"
                    out.append(f"| [`{s['id']}`]({s['path']}/{fname}) | {s[lang]} | {s[lang + '_desc']} |")
                out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    tree, errors = parse()
    if errors:
        print("\n".join(errors)); sys.exit(1)
    (ROOT / "CATALOG.md").write_text(render(tree, "en"), encoding="utf-8")
    (ROOT / "CATALOG.tr.md").write_text(render(tree, "tr"), encoding="utf-8")
    print(f"ok: {sum(1 for _ in skills(tree))} skills")
