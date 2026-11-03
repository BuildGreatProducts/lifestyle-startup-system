#!/usr/bin/env python3
"""Where the member is in the Lifestyle Startup System, in plain English. Read-only.

  python3 scripts/status.py [--repo PATH]          plain summary for the member
  python3 scripts/status.py --json [--repo PATH]   the same, as JSON (for `start`)
  python3 scripts/status.py --greet [--repo PATH]  session-start hook output; silent outside a member's project

Each step's document opens with a `Status:` line (Draft, Done or Extracted). A step is done when
its document says Done. An existing product's path in docs/0-PATH.md, when present, sets the order.
"""
import json
import os
import re
import sys

STEPS = [
    # (number, skill, document, short name, what doing it next gives the member)
    (1, "idea-finder", "1-IDEA.md", "Idea",
     "find the one product idea hiding in your skills, with evidence that people pay"),
    (2, "product-offer", "2-OFFER.md", "Offer",
     "pin down who it's for, what it promises, what form it takes and what it costs"),
    (3, "brand-identity", "3-BRAND.md", "Brand",
     "give it a name, a voice and a visual direction, explored on a canvas from references you like"),
    (4, "design-system", "4-DESIGN.md", "Design system",
     "turn your chosen visual direction into the colours, type and components everything is built with"),
    (5, "prototype-flows", "5-FLOWS.md", "Flows",
     "map the journeys that matter, then design the key screens on a canvas"),
    (6, "build-plan", "6-BUILD-PLAN.md", "Build plan",
     "write the plan your coding agent builds from, phase by phase, each with a test you can run"),
    (7, "security-audit", "7-SECURITY-AUDIT.md", "Security",
     "check the build for security problems before anyone else uses it"),
    (8, "go-live", "8-GO-LIVE.md", "Go live",
     "get it live, one step at a time, ending with a test as a real customer"),
    (9, "go-to-market", "9-GO-TO-MARKET.md", "Go to market",
     "pick your channels and work through a list of actions to get your first customers"),
]
BY_SKILL = {s[1]: s for s in STEPS}
STATUS_RE = re.compile(r"^Status:\s*(\w+)", re.M)


def doc_status(docs, name):
    path = os.path.join(docs, name)
    if not os.path.isfile(path):
        return None
    text = open(path, encoding="utf-8", errors="replace").read()
    # 4-DESIGN.md follows Google's DESIGN.md format: YAML tokens first, then the header.
    fm = re.match(r"\A---\n.*?\n---\n", text, re.S)
    head = text[fm.end() if fm else 0:][:2000]
    m = STATUS_RE.search(head)
    return m.group(1).capitalize() if m else "Draft"


def build_progress(docs):
    """(ticked, total) boxes under ## Build phases in 6-BUILD-PLAN.md, or None."""
    path = os.path.join(docs, "6-BUILD-PLAN.md")
    if not os.path.isfile(path):
        return None
    ticked = total = 0
    inside = False
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith("## "):
            inside = line.strip().lower() == "## build phases"
            continue
        m = re.match(r"^\s*- \[([ xX])\]", line)
        if inside and m:
            total += 1
            ticked += m.group(1) != " "
    return ticked, total


def read_path(docs):
    """Return the existing-product path as [(ticked, skill_or_None, line_text)], or None."""
    path = os.path.join(docs, "0-PATH.md")
    if not os.path.isfile(path):
        return None
    items = []
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.match(r"^\s*- \[([ xX])\]\s*(.+)$", line)
        if not m:
            continue
        text = m.group(2).strip()
        skill = None
        low = text.lower()
        if "product audit" in low or "product-audit" in low:
            skill = "product-audit"
        else:
            for s in STEPS:
                if low.startswith(f"{s[0]}.") or s[3].lower() in low.split(" — ")[0] or s[1] in low:
                    skill = s[1]
                    break
        items.append((m.group(1) != " ", skill, text))
    return items


def state(repo):
    docs = os.path.join(repo, "docs")
    statuses = {s[1]: doc_status(docs, s[2]) for s in STEPS}
    audit_done = os.path.isfile(os.path.join(docs, "audit", "REPORT.md"))
    path = read_path(docs)

    build = build_progress(docs)
    building = statuses.get("build-plan") == "Done" and build is not None and build[0] < build[1]

    def done(skill):
        if skill == "product-audit":
            return audit_done
        if skill == "build-plan" and building:
            return False
        if skill == "idea-finder" and statuses.get("product-offer"):
            return True  # a member who came with an idea skips step 1
        return statuses.get(skill) == "Done"

    nxt, mode = None, "steps"
    if path is not None:
        mode = "path"
        for ticked, skill, text in path:
            if skill is None:
                continue  # a line we can't map to a step never blocks or ends the path
            if skill == "build-plan" and building:
                nxt = skill
                break
            if not ticked and not done(skill):
                nxt = skill
                break
    else:
        for s in STEPS:
            if not done(s[1]):
                nxt = s[1]
                break
    started = any(statuses.values()) or path is not None
    return {
        "started": started,
        "mode": mode,
        "steps": [{"step": s[0], "skill": s[1], "doc": f"docs/{s[2]}", "name": s[3],
                   "status": statuses[s[1]] or "Not started"} for s in STEPS],
        "audit": "Done" if audit_done else "Not run",
        "next": nxt,
        "building": {"ticked": build[0], "total": build[1]} if building else None,
        "all_done": nxt is None and started,
    }


def summary(st):
    if not st["started"]:
        return ("Nothing started yet. Say \"continue\" and your agent will ask one question — "
                "find an idea, start from an idea you have, or start from something you've already built — "
                "and take you from there.")
    done = [s for s in st["steps"] if s["status"] == "Done"]
    line = f"{len(done)} of 9 steps done" + (f" (last: {done[-1]['name']})" if done else "")
    if st["mode"] == "path":
        line += ", following your product's path"
    if st["all_done"]:
        return (line + ". Every step is done — say \"continue\" to run your next round of growth "
                "actions, or ask for a product audit of what's live.")
    nxt = st["next"]
    if nxt == "product-audit":
        what = "review every screen of your product for UX, conversion and retention problems, laid out on a canvas"
        name = "Product audit"
    else:
        s = BY_SKILL[nxt]
        what, name = s[4], s[3]
        if nxt == "build-plan" and st["building"]:
            b = st["building"]
            return (f"{line}. You're building: {b['ticked']} of {b['total']} build tasks done. "
                    "Say \"continue\" to carry on with the next one; you can stop after any phase.")
        status = next(x["status"] for x in st["steps"] if x["skill"] == nxt)
        if status in ("Draft", "Extracted"):
            what = "carry on with it — " + what if status == "Draft" else "review the draft pulled from your product, then " + what
    return f"{line}. Next up, {name}: {what}. Say \"continue\" to start; you can stop after any step."


def is_member_project(repo):
    docs = os.path.join(repo, "docs")
    if os.path.isfile(os.path.join(docs, "0-PATH.md")):
        return True
    if any(os.path.isfile(os.path.join(docs, s[2])) for s in STEPS):
        return True
    for f in ("CLAUDE.md", "AGENTS.md"):
        p = os.path.join(repo, f)
        if os.path.isfile(p) and "BEGIN LIFESTYLE STARTUP SYSTEM" in open(p, encoding="utf-8", errors="replace").read():
            return True
    return False


def main():
    args = sys.argv[1:]
    repo = os.getcwd()
    if "--repo" in args:
        repo = os.path.abspath(args[args.index("--repo") + 1])
    st = state(repo)
    if "--greet" in args:
        if not is_member_project(repo):
            return
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "The Lifestyle Startup System is set up in this folder. Where the member is: "
                + summary(st)
                + "\n\nIf the member's first message doesn't ask for something specific, open with a short, "
                "plain-English welcome back (two or three lines): where they are and what saying \"continue\" "
                "will do. Don't start a step until they say so."),
        }}))
    elif "--json" in args:
        print(json.dumps(st, indent=2))
    else:
        print(summary(st))


if __name__ == "__main__":
    main()
