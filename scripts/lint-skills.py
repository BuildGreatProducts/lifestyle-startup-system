#!/usr/bin/env python3
"""Lint the Lifestyle Startup System's skills and references (rules in AUTHORING.md).

Run from the repo root:  python3 scripts/lint-skills.py
Exit code 1 if any ERROR is found; WARNings never fail the run.

Skills
  ERROR  name: present, <=64 chars, a-z/0-9/hyphen, matches the folder, no reserved words
  ERROR  description: present, <=1024 chars, no XML tags, has a "Not for" line
  WARN   description over 700 chars (descriptions load into every session)
  ERROR  SKILL.md body over 500 lines;  WARN over 250
References (skills/*/references/**/*.md)
  ERROR  no frontmatter, or kind not curated | checklist | research, or no last-reviewed date
  WARN   a checklist or research reference more than 183 days past last-reviewed
  WARN   over 100 lines with no contents list near the top
  WARN   not linked from any SKILL.md or reference (an orphan)
Everywhere (skills, setup, README, START-HERE)
  ERROR  a relative Markdown link that doesn't resolve
  ERROR  a ProductOS leftover: productos/ paths, retired skill or document names
  ERROR  a backticked name that looks like a skill but isn't one
  ERROR  setup/CLAUDE.md and setup/AGENTS.md differ below their title line
  ERROR  a computer:// link
"""
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
DESC_MAX, DESC_WARN = 1024, 700
BODY_MAX, BODY_WARN = 500, 250
TOC_MIN_LINES, TOC_SCAN_LINES = 100, 40
STALE_DAYS = 183
KINDS = {"curated", "checklist", "research"}
SHAPES = {"web-app", "mobile-app", "desktop-app", "browser-extension", "agent-plugin", "agent-skill",
          "mcp-server", "chat-assistant", "developer-tool", "productized-service", "website", "digital-product"}

# Leftovers from ProductOS that must not appear in the new system.
LEFTOVERS = [
    (r"productos/", "a productos/ path"),
    (r"\bProductOS\b", "the ProductOS name"),
    (r"`(?!design-system`)(?:define|design|develop|distribute)-[a-z0-9-]+`", "a retired ProductOS skill name"),
    (r"(?<![\w-])(?:DEFINE|PRD|ROADMAP|PATH|COPY|DEPLOY|MAGIC-MOMENT|ONBOARDING|LANDING-PAGE|GROWTH-TRACKER)\.md\b",
     "a retired document name"),
    (r"\bBONUS-[A-Za-z-]+\.md\b", "a retired BONUS doc name"),
]

errors, warnings = [], []


def rel(path):
    return os.path.relpath(path, ROOT)


def parse_frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields, key, block = {}, None, []
    for line in m.group(1).split("\n"):
        top = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if top:
            if key and block:
                fields[key] = " ".join(block)
            key, value, block = top.group(1), top.group(2).strip(), []
            if value in (">", ">-", "|", "|-"):
                continue
            fields[key] = value.strip("'\"")
            key = None
        elif key is not None:
            block.append(line.strip())
    if key and block:
        fields[key] = " ".join(block)
    return fields, text[m.end():]


def skill_names():
    return sorted(d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))


def check_skill(name):
    path = os.path.join(SKILLS, name, "SKILL.md")
    fields, body = parse_frontmatter(open(path, encoding="utf-8").read())
    if fields is None:
        errors.append(f"{rel(path)}: no YAML frontmatter")
        return
    n = fields.get("name", "")
    if not n:
        errors.append(f"{rel(path)}: missing name")
    elif len(n) > 64 or not re.fullmatch(r"[a-z0-9-]+", n):
        errors.append(f"{rel(path)}: name '{n}' must be <=64 chars of a-z, 0-9, hyphen")
    elif n != name:
        errors.append(f"{rel(path)}: name '{n}' doesn't match folder '{name}'")
    if re.search(r"anthropic|claude", n):
        errors.append(f"{rel(path)}: name uses a reserved word")
    d = fields.get("description", "")
    if not d:
        errors.append(f"{rel(path)}: missing description")
    else:
        if len(d) > DESC_MAX:
            errors.append(f"{rel(path)}: description is {len(d)} chars (max {DESC_MAX})")
        elif len(d) > DESC_WARN:
            warnings.append(f"{rel(path)}: description is {len(d)} chars (aim for <={DESC_WARN})")
        if re.search(r"<[A-Za-z/][^>]*>", d):
            errors.append(f"{rel(path)}: description contains an XML tag")
        if "Not for" not in d:
            errors.append(f"{rel(path)}: description has no 'Not for X — use Y' line")
    lines = body.count("\n")
    if lines > BODY_MAX:
        errors.append(f"{rel(path)}: body is {lines} lines (max {BODY_MAX})")
    elif lines > BODY_WARN:
        warnings.append(f"{rel(path)}: body is {lines} lines (aim for <={BODY_WARN})")


def has_toc(lines):
    head = lines[:TOC_SCAN_LINES]
    if any(re.match(r"^#+\s*(table of )?contents\b", l, re.I) for l in head):
        return True
    return sum(bool(re.search(r"\]\(#", l)) for l in head) >= 3


def reference_files():
    for name in skill_names():
        top = os.path.join(SKILLS, name, "references")
        for dirpath, _, files in os.walk(top):
            for f in files:
                if f.endswith(".md"):
                    yield os.path.join(dirpath, f)


def check_references():
    today = datetime.date.today()
    for path in reference_files():
        text = open(path, encoding="utf-8").read()
        fields, _ = parse_frontmatter(text)
        if fields is None:
            errors.append(f"{rel(path)}: no frontmatter (kind, last-reviewed)")
            continue
        kind = fields.get("kind", "")
        if kind not in KINDS:
            errors.append(f"{rel(path)}: kind '{kind}' is not one of {', '.join(sorted(KINDS))}")
        try:
            reviewed = datetime.date.fromisoformat(fields.get("last-reviewed", ""))
        except ValueError:
            errors.append(f"{rel(path)}: last-reviewed must be a YYYY-MM-DD date")
            reviewed = None
        if reviewed and kind in ("checklist", "research") and (today - reviewed).days > STALE_DAYS:
            warnings.append(f"{rel(path)}: {kind} last reviewed {reviewed} — over {STALE_DAYS} days ago")
        lines = text.split("\n")
        if len(lines) > TOC_MIN_LINES and not has_toc(lines):
            warnings.append(f"{rel(path)}: {len(lines)} lines with no contents list near the top")


def checked_files():
    files = [os.path.join(ROOT, f) for f in ("README.md", "START-HERE.md")]
    files += [os.path.join(ROOT, "setup", f) for f in ("CLAUDE.md", "AGENTS.md")]
    for dirpath, _, names in os.walk(SKILLS):
        files += [os.path.join(dirpath, n) for n in names if n.endswith((".md", ".html"))]
    return [f for f in files if os.path.isfile(f)]


def check_text():
    known = set(skill_names())
    link_targets = set()
    looks_like_skill = re.compile(
        r"`((?:idea|product|brand|design|prototype|build|security|go|path|start)[a-z-]*)`")
    for path in checked_files():
        text = open(path, encoding="utf-8").read()
        here = os.path.dirname(path)
        if "computer://" in text:
            errors.append(f"{rel(path)}: contains a computer:// link — give the file path instead")
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", text):
            target = m.group(1)
            if re.match(r"[a-z]+:", target):
                continue
            full = os.path.normpath(os.path.join(here, target))
            link_targets.add(full)
            if not os.path.exists(full):
                errors.append(f"{rel(path)}: link to {target} doesn't resolve")
        for n, line in enumerate(text.split("\n"), 1):
            for pattern, what in LEFTOVERS:
                if re.search(pattern, line):
                    errors.append(f"{rel(path)}:{n}: {what}")
            for name in looks_like_skill.findall(line):
                if "-" in name and name not in known and name not in SHAPES and not name.endswith((".md", "-")):
                    errors.append(f"{rel(path)}:{n}: `{name}` looks like a skill name but isn't one")
    for path in reference_files():
        if os.path.normpath(path) not in link_targets:
            warnings.append(f"{rel(path)}: not linked from any skill or reference")


def check_setup_twins():
    a, b = (os.path.join(ROOT, "setup", f) for f in ("CLAUDE.md", "AGENTS.md"))
    if not (os.path.isfile(a) and os.path.isfile(b)):
        warnings.append("setup/CLAUDE.md or setup/AGENTS.md is missing")
        return
    if open(a, encoding="utf-8").read().split("\n")[1:] != open(b, encoding="utf-8").read().split("\n")[1:]:
        errors.append("setup/CLAUDE.md and setup/AGENTS.md differ below their title line — keep the twins identical")


def main():
    names = skill_names()
    for name in names:
        check_skill(name)
    check_references()
    check_text()
    check_setup_twins()
    for w in warnings:
        print(f"WARN   {w}")
    for e in errors:
        print(f"ERROR  {e}")
    print(f"\n{len(names)} skills checked: {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
