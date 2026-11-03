---
name: start
description: >-
  The front door of the Lifestyle Startup System. Sets it up in the member's product folder (root
  CLAUDE.md / AGENTS.md guidelines, version history when the build starts), then reads docs/, tells
  the member in plain words where they are and what the next step does for them, and runs that
  step. Use when the member says "start", "set up the Lifestyle Startup System", "continue", "what's
  next", "where was I" or "pick up where I left off". Not for carrying on a task already under way
  in this conversation — just keep going with it.
---

# Start

One word for the member to remember: **"continue"**. This skill sets the system up the first time, and every time after that it works out where the member is and runs the next step. It decides nothing about the product itself — each step's skill does that.

## Workflow

### 1. Check the setup

Find the member's **product folder** — the folder that holds everything for this product: `docs/`, the root guidelines, and later any code.

- The current folder is the Lifestyle Startup System's own folder (it has `AUTHORING.md` and `skills/` at the top) → this isn't the product folder. Ask whether the product already has a folder; if not, make one next to it named after the product (default `my-product`). If the system isn't installed as a plugin, copy this folder into the product folder as `lifestyle-startup-system/`. Ask the member to reopen their agent in the product folder, in one plain line, and stop.
- A general folder (home, Desktop, Downloads, Documents) isn't a product folder either: ask the same question.

Then, in the product folder:

1. **Root guidelines.** No root `CLAUDE.md` / `AGENTS.md` → copy them whole from this system's `setup/` folder. They exist → never overwrite: append the block between `<!-- BEGIN LIFESTYLE STARTUP SYSTEM -->` and `<!-- END LIFESTYLE STARTUP SYSTEM -->` from the matching file in `setup/`, or, on a re-run, replace everything between those markers with the fresh block. Wire whichever files match the member's coding agent; the default is both.
2. **A copied-in system stays out of history.** If the system lives in the product folder as `lifestyle-startup-system/`, make sure `.gitignore` has that line. The member's own documents in `docs/` are theirs and stay tracked.

Tell the member what you did in one line: *"I've set up your product folder; everything we write together goes in `docs/`."*

**Done when:** the root guidelines carry exactly one Lifestyle Startup System block.

### 2. Read where they are

Run `python3 <this skill's folder>/../../scripts/status.py --json --repo .` from the product folder. Without Python, read the `Status:` line at the top of each numbered document in `docs/` and the checkboxes in `docs/0-PATH.md`.

If `docs/0-PATH.md` exists, tick every unticked line whose step document now says `Status: Done` (product audit: once `docs/audit/REPORT.md` exists; build plan: only once every box under `## Build phases` is ticked), so the path stays true.

**Done when:** you know the next step.

### 3. Pick the next step

The first match wins:

| The state | Next |
|---|---|
| Nothing in `docs/` yet | Ask the one question below |
| `docs/0-PATH.md` exists | The first unticked line on the path |
| A step document says `Draft` or `Extracted` | That step — carry on or review it |
| `docs/6-BUILD-PLAN.md` says `Done` but boxes under `## Build phases` are unticked | Keep building: the next unticked box, working as the root guidelines say |
| Otherwise | The first step whose document doesn't exist yet, in order 1–9 (step 1 counts as done once `docs/2-OFFER.md` exists — the member came with an idea) |
| All nine are `Done` | `go-to-market` again (its next stage or a fresh round of experiments), and offer a `product-audit` of what's live |

**The one question**, asked as a three-way choice. Look before you ask: code beyond `docs/`, a platform export, a live URL in a README. If the folder points to an answer, put it first and say why.

> **Where would you like to start?**
> 1. **Find an idea** — you have a skill, a service or a craft, but no product idea yet. → `idea-finder`
> 2. **Start from an idea you have** — you know what you want to make, and nothing's built yet. → `product-offer`
> 3. **Start from something you've built** — code, a prototype, an app on Lovable or Bolt, a live site, service or listing. → `path-finder`

**Done when:** one next step is chosen.

### 4. Tell the member, in plain words

Two or three lines, with no step numbers, file names or skill names unless they ask:

- where they are — how many of the nine steps are done, or that they're following their product's path;
- what the next step does for them, in one sentence (the status script's plain summary has the wording);
- that they can stop after any step, and "continue" picks up from there next time.

> You've shaped your offer and set your brand. Next, we'll turn your chosen look into the colours, type and building blocks everything else is made from. Ready?

Wait for a yes, or a different request, before running it.

### 5. Run the step

Run the next step's skill from its first step and follow it.

## Version history

When the build starts (the build plan's phase 0, or any time the member asks), the product folder needs version history if the product is built from code here. Already a git repository → nothing to do. Otherwise run `git init`, check `.gitignore` (step 1), and save everything as the first commit, *Start version history*. Tell the member in one line: *"I've turned on version history: every change from here is saved and can be undone."* No git on the machine → say so plainly and give the one thing to do (on a Mac, accept the developer-tools prompt; on Windows, install Git from git-scm.com).

## Rules

- **Route only.** The order lives in this skill's table and `docs/0-PATH.md`; the steps' skills own everything else.
- **Plain words.** Say what a step does, not what it's called. Explain a technical term in a few words the first time it comes up.
- **The member's request wins.** If they ask for something specific, do that; "continue" is the default, not a gate.

## Verify before handing over

- [ ] The root guidelines carry exactly one Lifestyle Startup System block.
- [ ] The member heard where they are and what's next, in plain words.
- [ ] The next step is the first match in the table, and it ran from its first step.
