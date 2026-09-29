#!/usr/bin/env python3
"""Render the per-skill usage guides GUIDE.md and GUIDE.tr.md from the skill files."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import parse, skills, ROOT  # noqa: E402
from export import frontmatter, FILES  # noqa: E402

TEXT = {
    "en": {
        "title": "Skill Usage Guide",
        "intro": ("Every skill with when to use it and a ready-to-use example request. Type the example (or your own "
                  "version) in any AI tool where the skill is installed, or paste the skill file first and then the "
                  "request. See [USAGE.md](USAGE.md) for tool setup and [METHODOLOGIES.md](METHODOLOGIES.md) for "
                  "which skills fit which phase."),
        "toc": "Contents", "when": "When", "try": "Try", "related": "Related", "file": "File",
    },
    "tr": {
        "title": "Skill Kullanım Rehberi",
        "intro": ("Her skill için ne zaman kullanılacağı ve hazır bir örnek istek. Örneği (veya kendi versiyonunu) "
                  "skill'in kurulu olduğu herhangi bir YZ aracına yaz ya da önce skill dosyasını, ardından isteği "
                  "yapıştır. Araç kurulumu için [USAGE.tr.md](USAGE.tr.md), hangi skill'in hangi aşamaya uyduğu için "
                  "[METHODOLOGIES.tr.md](METHODOLOGIES.tr.md) dosyasına bak."),
        "toc": "İçindekiler", "when": "Ne zaman", "try": "Örnek istek", "related": "İlgili", "file": "Dosya",
    },
}


def anchor(text):
    keep = "".join(ch for ch in text.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


def render(tree, lang):
    t = TEXT[lang]
    out = [f"# {t['title']}", "", t["intro"], "", f"## {t['toc']}", ""]
    for c in tree:
        out.append(f"- [{c[lang]}](#{anchor(c[lang])})")
        for r in c["children"]:
            out.append(f"  - [{r[lang]}](#{anchor(r[lang])})")
    for c in tree:
        out += ["", f"## {c[lang]}"]
        for r in c["children"]:
            out += ["", f"### {r[lang]}"]
            for a in r["children"]:
                out += ["", f"#### {a[lang]}"]
                for s in a["children"]:
                    rel_path = f"{s['path']}/{FILES[lang]}"
                    src = ROOT / rel_path
                    fm = frontmatter(src.read_text(encoding="utf-8"))[0] if src.exists() else {}
                    out += ["", f"**{s[lang]}** · `{s['id']}`", "",
                            f"- {t['when']}: {fm.get('description', s[lang + '_desc'])}"]
                    if fm.get("prompt"):
                        out.append(f"- {t['try']}: _\"{fm['prompt']}\"_")
                    if fm.get("related"):
                        rel = ", ".join(f"`{x.strip()}`" for x in fm["related"].split(",") if x.strip())
                        out.append(f"- {t['related']}: {rel}")
                    out.append(f"- {t['file']}: [{rel_path}]({rel_path})")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    tree, errors = parse()
    if errors:
        sys.exit("\n".join(errors))
    (ROOT / "GUIDE.md").write_text(render(tree, "en"), encoding="utf-8")
    (ROOT / "GUIDE.tr.md").write_text(render(tree, "tr"), encoding="utf-8")
    print("ok: GUIDE.md, GUIDE.tr.md")
