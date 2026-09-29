#!/usr/bin/env python3
"""Normalize every skill's frontmatter from catalog/catalog.txt and validate the tree.

Authors only write `description`, `related` and `prompt` in a skill's frontmatter;
name, license and metadata are derived from the catalog so both languages stay in sync.

Usage: python3 scripts/sync.py [--check]
"""
import re, sys
from pathlib import Path
from catalog import parse, skills, ROOT

LANGS = {"en": "SKILL.md", "tr": "SKILL.tr.md"}
LICENSE = "MIT"
SECTIONS = {
    "en": ["Purpose", "When to use", "When not to use", "Inputs", "Process", "Output format",
           "Quality checklist", "Common pitfalls", "Example"],
    "tr": ["Amaç", "Ne zaman kullanılır", "Ne zaman kullanılmaz", "Girdiler", "Süreç", "Çıktı formatı",
           "Kalite kontrol listesi", "Sık yapılan hatalar", "Örnek"],
}
RESERVED = ("anthropic", "claude", "openai", "gemini", "copilot")
VERSION = "1.0.0"


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^\s*([A-Za-z_-]+):\s*(.*)$", line)
        if kv and kv.group(2):
            fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm, m.group(2).lstrip("\n")


def quote(v):
    return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render(s, c, r, a, lang, fm, body):
    lines = ["---", f"name: {s['id']}", f"description: {quote(fm['description'])}", f"license: {LICENSE}",
             "metadata:", f'  version: "{fm.get("version", VERSION)}"', f"  language: {lang}",
             f"  category: {c['dir']}", f"  role: {r['dir']}", f"  area: {a['dir']}",
             f"  title: {quote(s[lang])}"]
    if fm.get("related"):
        lines.append(f"  related: {quote(fm['related'])}")
    if fm.get("prompt"):
        lines.append(f"  prompt: {quote(fm['prompt'])}")
    return "\n".join(lines + ["---", "", body.rstrip() + "\n"])


def sections(body):
    """Return {heading: text} for H2 sections, ignoring headings inside fenced code blocks."""
    out, current, fence = {}, None, False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            current = line[3:].strip(); out[current] = []; continue
        if current:
            out[current].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def contract(body, lang):
    """Structural contract; returns (problems, step_count, check_count)."""
    probs, secs = [], sections(body)
    names = [h for h in secs if h in SECTIONS[lang]]
    if names != SECTIONS[lang]:
        missing = [h for h in SECTIONS[lang] if h not in secs]
        probs.append(f"sections missing/out of order: {missing or names}")
    steps = len(re.findall(r"^\d+\. ", secs.get(SECTIONS[lang][4], ""), re.M))
    checks = len(re.findall(r"^- \[ \]", secs.get(SECTIONS[lang][6], ""), re.M))
    if not 6 <= steps <= 14:
        probs.append(f"process has {steps} steps (6-14)")
    if not 4 <= checks <= 9:
        probs.append(f"quality checklist has {checks} items (4-9)")
    n = body.count("\n") + 1
    if not 40 <= n <= 200:
        probs.append(f"{n} lines (40-200)")
    return probs, steps, checks


def main(check):
    tree, errors = parse()
    ids = {s["id"] for *_, s in skills(tree)}
    problems, changed, shape = list(errors), 0, {}
    problems += [f"reserved word in id: {i}" for i in ids if any(w in i for w in RESERVED)]
    for c, r, a, s in skills(tree):
        for lang, fname in LANGS.items():
            p = ROOT / s["path"] / fname
            if not p.exists():
                problems.append(f"missing: {p.relative_to(ROOT)}"); continue
            fm, body = split_frontmatter(p.read_text(encoding="utf-8"))
            fm.setdefault("related", fm.get("related", ""))
            if not fm.get("description"):
                problems.append(f"no description: {p.relative_to(ROOT)}"); continue
            if len(fm["description"]) > 1024:
                problems.append(f"description > 1024 chars: {p.relative_to(ROOT)}")
            for rel in filter(None, (x.strip() for x in fm.get("related", "").split(","))):
                if rel not in ids:
                    problems.append(f"unknown related '{rel}' in {p.relative_to(ROOT)}")
            if not body.startswith("# "):
                problems.append(f"body must start with an H1: {p.relative_to(ROOT)}")
            if "<" in fm["description"] and re.search(r"<[a-zA-Z/]", fm["description"]):
                problems.append(f"description contains a tag: {p.relative_to(ROOT)}")
            probs, steps, checks = contract(body, lang)
            problems += [f"contract: {p.relative_to(ROOT)}: {x}" for x in probs]
            shape.setdefault(s["id"], {})[lang] = (steps, checks)
            new = render(s, c, r, a, lang, fm, body)
            if new != p.read_text(encoding="utf-8"):
                changed += 1
                if not check:
                    p.write_text(new, encoding="utf-8")
    for sid, langs in shape.items():
        if len(langs) == 2 and langs["en"] != langs["tr"]:
            problems.append(f"contract: {sid}: EN/TR mismatch (steps, checks) {langs['en']} vs {langs['tr']}")
    # orphan skill folders
    for p in (ROOT / "skills").rglob("SKILL.md"):
        if p.parent.name not in ids:
            problems.append(f"orphan skill folder: {p.parent.relative_to(ROOT)}")
    print("\n".join(problems) if problems else "ok")
    print(f"{'would change' if check else 'normalized'}: {changed} files")
    return 1 if problems or (check and changed) else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
