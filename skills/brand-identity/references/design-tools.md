---
kind: research
last-reviewed: 2026-11-03
---

# Design tools: finding and driving the canvas

Shared by `brand-identity` (directions and brand card), `design-system` (the catalogue), `prototype-flows` (key flows) and `product-audit` (a canvas per flow); owned here. It says which canvas tool to use in the current harness and how to do the four things every step needs: **detect it, lay artboards side by side, place images, and get a link to record**. Design tools change monthly — check the tool's current capabilities (its tool list, its own help or usage skill, its docs) before a real brief, rather than relying on anything frozen here.

## Contents

- [Pick the tool, in this order](#pick-the-tool-in-this-order)
- [1. /design in the Claude Code desktop app](#1-design-in-the-claude-code-desktop-app)
- [2. A design tool connected through MCP](#2-a-design-tool-connected-through-mcp)
- [3. HTML canvas fallback](#3-html-canvas-fallback)
- [Writing the brief](#writing-the-brief)
- [Recording the link](#recording-the-link)

## Pick the tool, in this order

1. **`/design`** — in Claude Code in the Claude desktop app, it opens a Claude Design canvas right in the app. Use it whenever the member is working there.
2. **A design tool the member already has connected** — Figma, Paper, MagicPath, Pencil or Stitch. If several are, ask which one they use; otherwise take the first that passes a one-artboard test.
3. **An HTML canvas page** written into the member's `docs/` folder.

Tell the member which you're using in one line. Don't install or sign up for a tool to get a nicer canvas unless the member asks; setting one up is their call, and the fallback is always good enough to choose a direction from.

**One-artboard test (MCP tools).** Before the real brief in a connected design tool, make one small labelled artboard with one placed image, read it back (screenshot or the tool's read call), and get its link. If any of the three fails, drop to the HTML fallback rather than fighting the tool. `/design` doesn't need the test.

## 1. /design in the Claude Code desktop app

`/design` is Claude Code's design command. In the Claude desktop app's Code tab it opens a **Claude Design canvas** inside the app, where the member sees the artboards appear and can react to them on the spot. It's the default for every visual step.

- **Detect:** the member is in Claude Code in the desktop app and `/design` is among the available commands. In the terminal, Codex or Cursor it isn't there — go to tier 2.
- **Invoke:** run `/design` with a plain-language brief (see [Writing the brief](#writing-the-brief)): the artboards, their sizes and order, the content of each, the images to place. One canvas per step; for `product-audit`, one per flow.
- **Artboards side by side:** say it in the brief: "artboards left to right, in this order, labelled …".
- **Images:** name the local files from `docs/` (the saved references, the audit screenshots) in the brief and which artboard each goes on, unaltered.
- **Read back:** `design-system` reads the chosen direction back from the canvas. Ask `/design` for the direction's values, or take a screenshot of it; `docs/3-BRAND.md` also records the hexes and fonts in case the canvas can't be read.
- **Link:** record the canvas link `/design` gives you in the step's document, so the member and later steps can reopen it.

## 2. A design tool connected through MCP

Detect by the tool names in the session (look for the product's name in the available tools) or by a usage skill the server ships. **If the server ships a usage skill or guidelines call, load it first** — several of these fail in confusing ways without it.

| Tool | Detect | Artboards side by side | Place images | Link to record |
|---|---|---|---|---|
| **Figma** | Figma MCP tools in the session (file, design-context, screenshot and write tools) | Frames on one page at fixed x offsets with a gap, or a horizontal auto-layout parent | Upload the image as an asset, then use it as a frame's image fill | The file URL with `?node-id=` for the page or frame |
| **Paper** | Paper tools in the session; the desktop app must be open with a document loaded | Artboards in a row on the open document | Check the current tools for image import; else place as a fill from a local file | The file's share link if the app offers one; otherwise the document name plus exported PNGs saved to `docs/` |
| **MagicPath** | The MagicPath agent skill is installed and logged in | A design per artboard in one project, or one multi-section design | Pass the image files with the request | The project or design URL |
| **Pencil** | Pencil tools in the session; a `.pen` file in the repo | Find empty canvas space, then create frames in a row | Check the current tools for image nodes; export to verify | The `.pen` file path plus exported PNGs in `docs/` |
| **Stitch** | Stitch tools in the session | Screens in one project; generated from text, with variants | Supply references with the generation request where supported | The project URL |

Notes that hold across tools:

- **Generated is not drawn.** Tools that generate screens from text (Stitch, MagicPath) interpret the brief. Check every artboard against the spec — hexes, fonts, copy — and fix drift before showing the member.
- **Design-system handoff.** Some tools accept a DESIGN.md or a token set directly (Stitch can build a design system from one; Figma takes variables). When `design-system` has written `docs/4-DESIGN.md`, push it in so later screens use the tokens.
- **Local-only tools** (Paper, Pencil) have no public link: export each artboard to PNG under `docs/` and record the file path as the link.

## 3. HTML canvas fallback

A single self-contained page in the member's project — `docs/brand/canvas.html` for `brand-identity`; the other steps name their own path. It always works, opens in any browser, and lives next to the docs it illustrates.

- **Layout:** a horizontal row of fixed-width artboards that scrolls sideways, each with a small label above it. States or alternates stack beneath their artboard.
- **Styling:** each direction's artboard styles itself from its own CSS custom properties (`--bg`, `--text`, `--primary`, `--accent`, `--font-heading`, `--font-body`), so a mix is a matter of swapping variables. Fonts load from a Google Fonts `<link>`; everything else inline, no frameworks.
- **Images:** `<img src="references/01-name.png">` with paths relative to the HTML file, so the page works when the folder moves.
- **Read back:** you wrote it, so you can read it; to check how it looks, open it in a browser tool and screenshot it.
- **Link:** the file path. If the harness can publish a page (an artifact or a hosted preview), offer to publish it for a shareable link and record both.

```html
<div class="canvas">  <!-- display:flex; gap:64px; overflow-x:auto; padding:64px -->
  <section class="artboard" style="--w:1200px">
    <p class="label">References</p>
    <!-- images + one-line notes -->
  </section>
  <section class="artboard dir-a" style="--w:1440px">
    <p class="label">A · Field Notes</p>
    <!-- palette, type, wordmark, sample screen, "draws on" -->
  </section>
  <!-- dir-b, dir-c … -->
</div>
```

## Writing the brief

Whatever the tool, the brief says:

1. **Canvas name** — "<product> · brand directions".
2. **Artboards in order**, left to right, each with a label, a size (1440×900 desktop, 390×844 phone, 1200×1200 square cover) and its content.
3. **Exact values** — hexes, font names, real copy in the brand's voice. Never "a warm colour" or lorem ipsum.
4. **Images** — which file goes on which artboard, unaltered.
5. **What not to do** — "no gradients", "no stock photos", the category default to avoid.

## Recording the link

Every canvas link goes into the step's document (`docs/3-BRAND.md` → Canvas, and so on) with one line on what's on it. A link the member can't open is not a link: check it opens, or record the file path instead.
