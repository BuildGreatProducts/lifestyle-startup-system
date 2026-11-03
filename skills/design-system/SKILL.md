---
name: design-system
description: >-
  Step 4. Turns the visual direction chosen in brand-identity into the tokens and components
  everything is built with — colours, type, spacing, radii, elevation, components — and writes
  docs/4-DESIGN.md in Google's DESIGN.md format (YAML tokens plus prose) and docs/4-DESIGN.html, a
  live style guide. Can adjust the direction from an image, or extract the system from an existing
  codebase. Use when the member says "build my design system", "turn my brand into tokens", or "use
  this screenshot's look". Not for naming or the visual direction — use brand-identity.
---

# Design system

Turns a visual source into the tokens and components every later step builds with: `prototype-flows` designs screens with them, and the build plan's design-catalogue phase codes them before any feature. Two mirrored files: `docs/4-DESIGN.md` is the source of truth a coding agent implements from; `docs/4-DESIGN.html` renders every token and component live for the member. They are always written together so they never drift.

The visual decisions were made in `brand-identity`. This step makes them **exact and complete** — the hexes, the scale, the states, the rules for everything the direction didn't show — not a second round of taste.

Take the voice of a senior design director who is also a systems engineer:

- **Observant.** Describe what's on the canvas, not what you assume.
- **Token-fluent.** Every recommendation lands as a token: not "a soft red" but `error: "#B23A2E"`.
- **Decisive.** When the member is unsure, recommend with a one-line reason.
- **Strict to the format.** Section order, YAML schema and token-reference syntax are fixed.

## Inputs

- `docs/3-BRAND.md` — **required** on the normal path: the chosen direction (palette with roles, type, mood, composition rules), the logo direction, the canvas link and the reference list.
- **The brand canvas** — the chosen direction's artboards and the brand card, opened with [../brand-identity/references/design-tools.md](../brand-identity/references/design-tools.md). Unreadable → work from `3-BRAND.md` and say so.
- `docs/brand/references/` — the saved images, read alongside the direction.
- `docs/2-OFFER.md` — what the product is and who uses it, and `## Product` → the `Shape:` line. Read that shape's row in [../product-offer/references/shapes.md](../product-offer/references/shapes.md): **Full** (screen shapes), **Adapted** (scoped to the surfaces the row names, such as an extension's popup and injected UI) or **Lite** — brand tokens only — for screenless shapes such as an agent skill, MCP server or productized service.
- `docs/4-DESIGN.md` with `Status: Extracted` — the from-code run `path-finder` started. **Review mode:** walk the tokens and components with the member, settle open values, write the `.html` if it's missing, and set `Done`. No brand canvas is needed.
- `docs/4-DESIGN.md` and `.html` if they exist (not `Extracted`) — a re-run. Ask whether to refine specific tokens, rebuild from a new source, or merge; show what would change before overwriting.

Missing `2-OFFER.md` → run `product-offer` first.

## Workflow

### 1. Choose the intake

Take the first that applies; tell the member which in one line.

1. **Primary — the chosen direction.** `3-BRAND.md` names a direction and the canvas shows it. Build from that and the references. This is the normal path; ask nothing.
2. **Secondary — an image reference.** The member shares a screenshot, Figma frame or live site they want to pull in. With a chosen direction, the image **adjusts** it — it never replaces it — and you say exactly what changed. With no direction (rare: an older project), the image is the source, read against the brand words in `3-BRAND.md`.
3. **From code — existing products only**, when `path-finder` calls this step or the member asks to document the system already in their app. Follow [references/from-code.md](references/from-code.md) instead of steps 2–3 below, then rejoin at step 4.

**No direction and no image → stop** (unless the source is code, or the document is `Extracted`). Send the member back to `brand-identity`: "The look gets decided there, from references you like, on a canvas. Inventing a style here would give you the category average."

**Done when:** the intake is named and its source is open.

### 2. Read the source

Open the chosen direction on the canvas and read `3-BRAND.md` → Visual direction, then every saved reference, using [../brand-identity/references/image-analysis-patterns.md](../brand-identity/references/image-analysis-patterns.md). Capture what the direction already fixes (palette, type pair, mood, composition rules) and what it leaves open (states, secondary text, borders, elevation, the scale between the sizes it showed).

**An adjusting image:** read it the same way, then list what it changes as a short table — token, direction value, new value, why — and what it leaves alone. Get a yes before going on. An image that contradicts the brand's tone or a composition rule in `3-BRAND.md` loses on strategy and wins only on tactics (exact hexes, radii, component rhythm); say which applies.

Summarise back in 5–8 bullets.

**Done when:** the member has confirmed the summary (and the change table, if there is one).

### 3. Settle what's still open

Ask only what the direction and `3-BRAND.md` don't answer — usually two or three questions, one at a time, each with a recommendation from the canvas:

1. **Colour roles** beyond the palette — semantic states, secondary text, borders; light, dark or both.
2. **Density** — tight, comfortable or generous.
3. **Shape language** and **elevation** — corners by component class; shadows, hairlines, tonal layers or flat.
4. **Components** that matter for the first version — 6–10 including variants, from the offer's core loop (Lite: the fixed set).
5. **Three things this must never look like** — they become the Don'ts.

A vague answer gets a recommendation, not another open question.

**Done when:** every token group has a decided source.

### 4. Derive the tokens

Compose the YAML to [references/reference-design.md](references/reference-design.md) → Token rules, or its Lite set. Carry the direction's hexes and fonts over exactly unless step 2 changed them. Derive what the canvas didn't show (hover states, `on-` colours, the full type scale) from what it did, and compute contrast for every component pair; fix failures now by adjusting the derived colour, not the brand's primary, and say so.

**Done when:** the YAML parses, every component references tokens, and every pair meets WCAG AA.

### 5. Draft the prose

Write the eight sections in order ([references/reference-design.md](references/reference-design.md) → The eight sections), 3–8 sentences each. `## Brand & Style` links `3-BRAND.md` rather than repeating it, and carries `### What the reference changed` when an image adjusted the direction. Lite: also `### Logo use`.

**Done when:** every YAML component is explained in prose, and every prose component has a YAML entry.

### 6. Confirm, then write both files

Show a short outline first — the colour tokens, type levels, scales, component list, one line per section. Fold in edits. Then write `docs/4-DESIGN.md`, check it saved, and generate `docs/4-DESIGN.html` **from the tokens just written** ([references/reference-design.md](references/reference-design.md) → The HTML style guide), not from a fresh look at the images.

**Done when:** both files exist and the HTML's custom properties match the YAML exactly.

### 7. Put the catalogue on the canvas

Add a **catalogue** to the brand canvas, beside the chosen direction: colour swatches, type specimens and every component with its states, drawn from the tokens. `prototype-flows` designs its screens from this. Where the canvas tool accepts a DESIGN.md or token set directly, push the file in so later screens use the tokens ([../brand-identity/references/design-tools.md](../brand-identity/references/design-tools.md)). Lite: a single artboard is enough.

**Done when:** the catalogue is on the canvas and its link is in `docs/4-DESIGN.md` → `Source:`.

## Write docs/4-DESIGN.md

Google's format puts the YAML first, so the step header follows it:

```markdown
---
version: alpha
name: <Design system name>
description: <one sentence; Lite adds "(Lite — brand tokens for listings, landing pages and docs)">
colors: …
typography: …
rounded: …
spacing: …
components: …
---

# Design system: <product name>

Status: Done
Updated: <YYYY-MM-DD>
Source: <direction "<name>" on the brand canvas (<link>); catalogue (<link>)> [adjusted by <image>] | extracted from code
Brand: <link to 3-BRAND.md>

## Brand & Style
## Colors
## Typography
## Layout & Spacing
## Elevation & Depth
## Shapes
## Components
## Do's and Don'ts
```

Use `Status: Draft` while open questions remain, and `Status: Extracted` for a from-code run that `path-finder` started. `docs/4-DESIGN.html` mirrors it: header, colours, type, spacing, radius, elevation, components, do's and don'ts.

**Editing later.** Any token change goes to the YAML, the prose that mentions it and the matching CSS property in the HTML, in one edit. A hand edit to the HTML gets folded back into the YAML. Changes to the brand itself go through `brand-identity`.

## Verify before delivering

- [ ] The YAML parses (quoted hexes and `{…}` references, consistent indentation) and follows the schema; the header sits after it with `Status:` and `Source:`.
- [ ] The direction's palette and fonts carried over exactly, or every change is listed with its reason.
- [ ] All eight sections are present, in order, no duplicate `##` headings; components match one-for-one between YAML and prose.
- [ ] Fonts are free for commercial use and off the banned list.
- [ ] Every component pair meets WCAG AA, computed.
- [ ] The HTML renders every token and component live, its values match the YAML, and both files were written in the same pass.
- [ ] The catalogue is on the canvas and linked.
- [ ] Lite only: within the Lite set, `### Logo use` filled, both files marked Lite.

Tell the member in two lines: the design system is the rulebook any coding agent builds from, and the style guide opens in a browser to show it.

## Next

**Design the key flows** — `prototype-flows`. It designs the journeys and screens on the canvas with these tokens and the brand's voice. For a screenless shape, it maps the steps from install or purchase to first result instead.
