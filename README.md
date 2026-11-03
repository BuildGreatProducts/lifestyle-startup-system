# Lifestyle Startup System

**Turn your skill into a product you can scale — with an AI agent doing the heavy lifting.**

> **Want 1-1 support?** Join the **Product Studio** for 1-1 support through the system: **[go.buildgreatproducts.com](https://go.buildgreatproducts.com)**

You already have something people pay for, or would: a profession, a service you sell, deep know-how, a craft. The Lifestyle Startup System takes that skill through nine steps to a live product and its first customers. Each step is one skill your agent runs with you, and each writes one document to your product folder's `docs/`. You can stop after any step and say **"continue"** next time.

| # | Step | What you get | Document |
|---|---|---|---|
| 1 | **Idea finder** | The one product idea hiding in your skills, with evidence that people pay | `docs/1-IDEA.md` |
| 2 | **Product offer** | Who it's for, what it promises, what form it takes, what it costs — in one document | `docs/2-OFFER.md` |
| 3 | **Brand identity** | A name, a voice and a visual direction, explored side by side on a canvas from references you love | `docs/3-BRAND.md` + canvas |
| 4 | **Design system** | Your chosen direction turned into the colours, type and components everything is built with | `docs/4-DESIGN.md` + `4-DESIGN.html` |
| 5 | **Prototype flows** | The journeys that matter, then the key screens designed on a canvas with real copy | `docs/5-FLOWS.md` + canvas |
| 6 | **Build plan** | A plan your coding agent builds from, phase by phase, each ending in a test you can run | `docs/6-BUILD-PLAN.md` |
| 7 | **Security audit** | A check of the build before anyone else uses it, with a launch verdict and a fix list | `docs/7-SECURITY-AUDIT.md` |
| 8 | **Go live** | Your product live, walked through one step at a time, ending with a test as a real customer | `docs/8-GO-LIVE.md` |
| 9 | **Go to market** | Your channels and a list of actions for the first customers, then experiments, then scale | `docs/9-GO-TO-MARKET.md` |

Already built something? **Path finder** scores it against the nine steps and writes the path for your product (`docs/0-PATH.md`): which steps to do, which to fast-track from what already exists, and which are done. **Product audit** tears down a working product screen by screen for UX, conversion, retention and product problems, with each flow laid out on a canvas (`docs/audit/`).

It works for any shape of product — web, mobile or desktop app, browser extension, agent plugin or skill, MCP server, chat assistant, developer tool, productized service, website or digital product. You pick the shape in step 2, and the later steps adapt to it.

## Install

### Claude Code

```bash
claude plugin install ./lifestyle-startup-system
```

Run it from your product folder, with this folder inside it or next to it.

### Codex

```bash
codex plugin marketplace add ./lifestyle-startup-system
```

```bash
codex plugin add lifestyle-startup-system@lifestyle-startup-system
```

### Cursor

`/add-plugin` needs a git clone (a folder with at least one commit), not a ZIP extract. Point it at this folder. Without git, copy the folder to `~/.cursor/plugins/local/lifestyle-startup-system` and reload the window.

### Claude Desktop / Cowork (no install)

Copy this folder into your product folder as `lifestyle-startup-system/`, and open your **product folder** as the project. The skills are picked up from there.

## Get started

Open your agent in your product folder — an empty folder is fine — and say **"start"**. It sets up your folder (adding a short guidelines block to `CLAUDE.md` / `AGENTS.md`, never overwriting what's there) and asks one question:

1. **Find an idea** — you have a skill but no product idea yet.
2. **Start from an idea you have.**
3. **Start from something you've built** — code, a prototype, an app on Lovable or Bolt, a live site or listing.

From then on, say **"continue"** in any session. It tells you where you are and runs the next step. In Claude Code, the plugin greets you with the same summary when a session starts.

## How it's organized

- **`skills/`** — the twelve skills: the nine steps, plus `start`, `path-finder` and `product-audit`. Each folder holds a `SKILL.md` and the `references/` it loads only when it needs them — worked examples, failure patterns, checklists and research guides.
- **`setup/`** — the guidelines `start` wires into your product folder's root `CLAUDE.md` / `AGENTS.md`, so your coding agent follows your design system, copy rules and build plan.
- **`scripts/status.py`** — where you are, in plain English (`python3 scripts/status.py --repo <your product folder>`). `scripts/lint-skills.py` is the maintainer's check of every skill and reference.
- **`hooks/`** — the session-start greeting.
- **`AUTHORING.md`** — how the skills and references are written, for maintainers.

Everything the system writes for you lives in your product folder's `docs/`. It's yours — share it, commit it, point anyone new at it.

## Requirements

- Claude Code, Codex, Cursor, Claude Desktop or Cowork.
- Web search turned on — several steps do live research.
- A canvas for steps 3, 4, 5 and the product audit. Best: Claude Code in the Claude desktop app, where `/design` opens a Claude Design canvas right in the app. Elsewhere: Figma, Paper, MagicPath, Pencil or Stitch connected through MCP. Without either, the agent builds an HTML canvas page instead.

## Version

**1.0.0** — see `CHANGELOG.md`. Licensed for individual commercial use — see `LICENSE.md`.
