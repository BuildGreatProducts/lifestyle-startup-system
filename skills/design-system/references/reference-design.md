---
kind: curated
last-reviewed: 2026-11-03
---

# Reference DESIGN.md

The format rules for `docs/4-DESIGN.md` — Google's open [DESIGN.md format](https://github.com/google-labs-code/design.md), YAML tokens plus prose — the Lite token set, and one complete worked example. Use the example for **structure only**: never copy its design choices into a member's system.

## Contents

- [File shape](#file-shape)
- [Token rules](#token-rules)
- [The eight sections](#the-eight-sections)
- [Lite set](#lite-set)
- [The HTML style guide](#the-html-style-guide)
- [Worked example: Editorial Calm](#worked-example-editorial-calm)

## File shape

1. **YAML frontmatter** first — the format requires it: `version: alpha`, `name`, `description`, then `colors`, `typography`, `rounded`, `spacing`, `components`.
2. The step header: `# Design system: <product>`, then `Status:` and `Updated:` lines, then a `Source:` line (the chosen direction and canvas link, any adjusting image, or "extracted from code") and a `Brand:` line linking `3-BRAND.md`.
3. The **eight sections**, in order, as `##` headings. No duplicate `##` headings anywhere — the format rejects them; use `###` inside a section.

The brand's words (name, worldview, tone) live in `docs/3-BRAND.md`, not here. `## Brand & Style` summarises them in a sentence and links there.

## Token rules

- Hexes are quoted strings: `"#1A1A1A"`. Dimensions in `px`, `em` or `rem`; letter-spacing may be negative `em`.
- **Semantic names, never appearance names:** `primary`, `on-primary`, `secondary`, `tertiary`, `neutral`, `surface`, `surface-container`, `surface-container-high`, `on-surface`, `on-surface-variant`, `outline`, `outline-variant`, `inverse-surface`, `inverse-on-surface`, `error`, `on-error`, `success`, `warning`, `info`. Not `blue`, `lightGray`. Add a role only when something uses it.
- **Typography levels:** `display-lg`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-md`, `label-sm` (plus `code-md` for developer-facing products). Aim for 6–10; never more than 15. Each level has `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, optional `letterSpacing`.
- **Rounded:** `none`, `sm`, `md`, `lg`, `xl`, `full`. **Spacing:** `xs`–`xl`, plus `gutter` and `margin` when the layout repeats them.
- **Components reference tokens** as `"{colors.primary}"`, `"{typography.label-md}"`, `"{rounded.sm}"` — braces, dot path, exact name, always quoted (unquoted, YAML reads braces as a map). Literal values only where no token fits.
- **Variants are siblings:** `button-primary` and `button-primary-hover`, never nested.
- **Valid component properties:** `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Anything else triggers parser warnings.
- **Contrast:** every component's `backgroundColor` + `textColor` pair meets WCAG AA — 4.5:1 for body text, 3:1 for large text. Compute it; don't eyeball it.
- **Fonts:** free for commercial use and off the banned list — rules and substitutions in [../../brand-identity/references/image-analysis-patterns.md](../../brand-identity/references/image-analysis-patterns.md) → Fonts. The direction from `brand-identity` has already chosen them; carry them over unless the member asks otherwise.
- **Light and dark:** when both exist, the YAML holds the primary mode; describe the other's values in `## Colors` and give the HTML both token sets.

## The eight sections

Each 3–8 tight sentences (bullets of per-role values don't count against it). Explain the *why* so a coding agent can decide where the tokens are silent; don't restate the YAML.

| Section | Holds |
|---|---|
| `## Brand & Style` | The aesthetic in one phrase, the feeling the UI should create, one or two anti-patterns, a link to `3-BRAND.md`. When an image adjusted the direction, a `### What the reference changed` list |
| `## Colors` | What each role does and why that value; the one accent's job; contrast intent |
| `## Typography` | The pairing's character, what each level is for, treatment rules (uppercase labels, tabular numbers) |
| `## Layout & Spacing` | Grid, max content widths, density, how spacing tokens map to layout |
| `## Elevation & Depth` | The depth model and why it fits the brand |
| `## Shapes` | Corner philosophy and deliberate differences by component class |
| `## Components` | How each component behaves, variants and states. Every YAML component appears here, and vice versa |
| `## Do's and Don'ts` | 4–6 of each, specific and enforceable, from the member's anti-patterns and the brand |

## Lite set

For screenless shapes, whose surfaces are a listing, landing page, docs, README, social images and deliverables. Same file, same format, less of it:

- **Colors:** `primary`, `on-primary`, `surface`, `on-surface`, `on-surface-variant`, `outline`, at most one accent; `error`/`success` only if docs or output show states.
- **Typography:** 4–6 levels — `display-lg`, `headline-md`, `body-md`, `label-md`, plus `code-md` in a mono face for developer-facing shapes.
- **Rounded and spacing:** 3–4 steps each.
- **Components:** 5–6 entries, variants included — `button-primary`, `link`, `card`, `badge`, and `code-block` (agent and developer shapes) or `screenshot-frame` (when listings show a host app, chat or terminal). For a productized service or digital product, `document-page` (a deliverable or proposal page) may replace one of them.
- **Logo use:** a `### Logo use` subsection in `## Brand & Style` — light and dark versions, clear space, minimum size, the square avatar crop listings need, two don'ts — from `3-BRAND.md` → Logo direction and [../../brand-identity/references/logo-types/logo-types.md](../../brand-identity/references/logo-types/logo-types.md) → Variants.
- **Prose:** all eight sections stay; Layout, Elevation and Shapes may be one or two sentences.
- **Marked Lite:** the YAML `description` ends "(Lite — brand tokens for listings, landing pages and docs)" and the HTML header says the same. If the product later gains screens, re-run in full and extend the Lite tokens — never discard them.

## The HTML style guide

`docs/4-DESIGN.html`, generated from the tokens just written:

- One self-contained file: CSS inline, no frameworks, no external JS; fonts from a Google Fonts `<link>`.
- Every YAML token declared as a CSS custom property in `:root` (`--color-primary`, `--type-headline-lg-size`, `--rounded-md`, `--space-md`), and every swatch, specimen and component styled from those variables, with values matching the YAML exactly.
- Sections in this order: **Header** (name, description, source direction, "live mirror of 4-DESIGN.md") → **Colors** (swatch, name, hex, a line in its `on-` colour, the contrast ratio) → **Typography** (each level as a live specimen with its spec) → **Spacing** (labelled bars) → **Radius** (sample boxes) → **Elevation** (a card per level) → **Components** (every entry rendered live, variants grouped; hover and focus as labelled static copies) → **Do's and Don'ts** (two columns, with small visual examples where they help).
- Both modes → a small vanilla-JS toggle flipping `data-theme`, with both token sets defined.
- Neutral chrome: a reference page, not a marketing page.

## Worked example: Editorial Calm

A complete light-mode system: warm neutrals, generous white space, a serif and sans pair. In a member's file the header block and a link to `3-BRAND.md` follow the title.

```markdown
---
version: alpha
name: Editorial Calm
description: A light-mode, editorial design system anchored in warm neutrals, generous whitespace and a refined serif/sans pairing.
colors:
  primary: "#1A1A1A"
  secondary: "#6B6660"
  tertiary: "#B23A2E"
  neutral: "#F8F5F0"
  surface: "#FFFFFF"
  surface-container: "#F2EEE7"
  surface-container-high: "#E8E3D9"
  on-surface: "#1A1A1A"
  on-surface-variant: "#6B6660"
  outline: "#B8B0A4"
  outline-variant: "#E0D9CC"
  inverse-surface: "#1A1A1A"
  inverse-on-surface: "#F8F5F0"
  error: "#B23A2E"
  on-error: "#FFFFFF"
  error-container: "#F4DAD5"
  on-error-container: "#7A1F16"
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
rounded:
  none: 0
  sm: 2px
  md: 4px
  lg: 8px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.surface-container}"
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  card-paper:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 24px
  list-item:
    backgroundColor: transparent
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    padding: 16px 0
  list-item-hover:
    backgroundColor: "{colors.surface-container}"
  chip:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 6px 12px
---

# Design system: Editorial Calm

## Brand & Style

A long-form, type-led system drawn from independent magazines and contemporary book design. Patient, considered, quietly authoritative: the UI gets out of the reader's way. The intent is "read it twice" — pages feel composed rather than packed, and negative space does structural work. The feeling is opening a thoughtful magazine, not scrolling a feed. Never a dashboard grid; never a second accent.

## Colors

A warm-neutral foundation with one earthy accent.

- **Primary (#1A1A1A):** deep ink for headlines, body and primary buttons.
- **Secondary (#6B6660):** warm grey for metadata, captions and hover states.
- **Tertiary (#B23A2E):** terracotta, used for the single most important action on a screen and editorial flourishes only.
- **Neutral (#F8F5F0):** warm cream page background — softer than white without losing brightness.
- **Surface (#FFFFFF):** paper white for cards, modals and inputs sitting on the page.
- **Outline / outline-variant:** 1px hairlines; the variant inside content, the standard on component edges.

## Typography

Newsreader for narrative, Public Sans for interface — both free on Google Fonts. Display and headlines are Newsreader Medium with negative tracking, italics allowed for character. Body is Public Sans 400 at 16–18px with 1.55–1.6 line height. The smallest label is uppercase with 0.08em tracking, echoing magazine mastheads. Numbers in tables use tabular figures.

## Layout & Spacing

Measured-prose model: narrow text columns in a generous canvas. Body text maxes at 680px; components at a 1080px frame; outer margins start at 48px. An 8px base governs everything (`xs 4 · sm 8 · md 16 · lg 32 · xl 64`, `gutter 24`, `margin 48`). Cards have 24px padding and 32px gaps; sections break with 64px. If a layout starts to feel like a dashboard, return to one column.

## Elevation & Depth

Depth comes from paper on paper and hairlines, not shadows. The page is cream with no border; cards and modals are white with one 1px outline-variant edge; floating menus alone get a faint `0 1px 3px rgba(26,26,26,0.06)` shadow, always with the border. Anything heavier breaks the calm.

## Shapes

Restrained and precise: buttons and inputs 2px, cards 4px, chips fully rounded to mark them as a separate kind of thing. Small enough to feel architectural, never toy-like. Sharp 0px corners only for rules and full-bleed images.

## Components

### Buttons
Primary is solid ink on cream, once per screen; hover shifts to the warm grey. Ghost is transparent with ink text and a surface-container hover, for secondary and destructive-confirm actions. Both 44px tall for touch targets.

### Inputs
Paper white with a 1px outline-variant border that becomes `outline` on focus. Label above; helper text below in `body-sm`. Errors swap the border to `error`.

### Cards and lists
Cards are paper white, 24px padding, `rounded-md`, with an optional uppercase metadata strip. List items are borderless with hairline dividers; hover shows surface-container.

### Chips
Fully rounded, `label-sm` on surface-container — tags, filters and statuses, never actions.

## Do's and Don'ts

- **Do** reserve the terracotta for one element per screen.
- **Don't** use shadows for hierarchy where a hairline will do.
- **Do** keep body columns at 680px or less.
- **Don't** mix Newsreader and Public Sans in one headline.
- **Do** use italic Newsreader for emphasis in headlines.
- **Don't** add a second accent colour.
```
