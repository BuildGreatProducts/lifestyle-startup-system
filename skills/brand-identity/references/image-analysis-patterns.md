---
kind: curated
last-reviewed: 2026-11-03
---

# Image analysis patterns

How to read a visual reference and turn what you see into specific notes and, later, tokens. Owned by `brand-identity` (step 4, reading the member's references; step 5, choosing type and colour for the directions); used by `design-system` when it reads the chosen direction and any new image. Always open the image itself — a page's CSS, a file name or the member's description is a supplementary signal, never the source.

## Contents

- [Reading a reference](#reading-a-reference)
- [Colour](#colour)
- [Typography](#typography)
- [Spacing, shape and depth](#spacing-shape-and-depth)
- [Layout and composition](#layout-and-composition)
- [Calibration shapes](#calibration-shapes)
- [Fonts](#fonts)
- [Pitfalls](#pitfalls)

## Reading a reference

Per image, extract in this order and write each as a note you could hand to a designer:

1. **What it is** — site, app screen, packaging, poster, photo — and light or dark.
2. **Colour** — approximate hexes with roles; dominant vs accent.
3. **Type** — classification, closest free font, hierarchy, case, tracking.
4. **Density and shape** — spacing feel, corner radii, borders vs shadows.
5. **Composition** — grid, alignment, type-led or image-led, how much empty space.
6. **Mood** — three concrete adjectives, not "clean" or "modern".

Then summarise back in 5–8 tight bullets. Where two references conflict (one dark and dense, one light and airy), name the conflict instead of averaging it.

## Colour

- Dominant background → `surface` (or `neutral`); dominant text → `on-surface`.
- The single non-neutral that pulls the eye → the accent or `primary`. Two strong accents → ask which is the hero.
- Muted secondary text → `on-surface-variant`; stacked neutral tints → `surface-container`, `surface-container-high`.
- Note **temperature** (warm cream vs cool grey), **value** (light, mid, dark) and **saturation** — these three are what make directions feel different, more than hue.
- In photography, separate the photo's colours from the interface's. The member who likes "the colour" of a photo-led site usually means the photo.

## Typography

- Classify before naming: geometric sans · grotesque/neo-grotesque · humanist sans · transitional or old-style serif · didone · slab · display/decorative · mono · script.
- **Tells:** x-height (tall reads friendly and screen-first; short reads bookish), terminals (flat, angled, ball), apertures (open humanist vs closed grotesque), contrast between thick and thin strokes.
- Say how sure you are: "a tight grotesque, probably Söhne — closest free: Hanken Grotesk".
- Largest text → `display` or `headline-lg`; body → `body-md`; small caps labels → `label-sm`.
- A serif in a reference is almost always for headlines, not body. Two distinct faces → the system is a pair.

## Spacing, shape and depth

- Smallest repeated gap → `xs`/`sm`; gap between unrelated blocks → `lg`/`xl`; button padding is usually 12–16px vertical, 16–24px horizontal.
- **Corners:** 0–2px architectural or brutalist · 4–8px modern professional · 12–16px consumer, friendly · 24px+ playful · pills on small controls contemporary consumer.
- **Depth:** soft large shadows → shadow elevation · backdrop blur → glass · stacked tints → tonal layering · 1px hairlines → border elevation · contrast only → flat.
- **Density:** count how much fits above the fold. Dashboard-dense, comfortable, or gallery-generous.

## Layout and composition

- Grid: single column, 12-column, asymmetric split, bento.
- Alignment: centred (ceremonial, simple) or left-aligned (editorial, scannable).
- Lead: type-led (headline is the hero), image-led, or product-led (a screenshot is the hero).
- Rhythm: is spacing even, or does it vary deliberately between sections?

These become the direction's composition rules, and later `## Layout & Spacing`.

## Calibration shapes

Recognised shapes to anchor a direction or name what a reference adds up to:

- **Editorial Calm** — warm neutrals, serif and sans pair, hairline borders, paper on paper. Calm-authority and expert brands. Full worked example: [../../design-system/references/reference-design.md](../../design-system/references/reference-design.md).
- **Atmospheric Glass** — dark surface, vivid gradient, blurred cards. Dramatic, transformative brands.
- **Dashboard Precision** — cool neutrals, geometric or grotesque sans, 2–4px corners, flat tonal layers. Linear and Vercel shape.
- **Friendly Workspace** — warm whites, humanist sans, medium rounding, soft hairlines. Warm tool-for-thinking brands.
- **Brutalist Editorial** — high-contrast monochrome, serif display, sharp corners, heavy weights. Defiant or authority-led brands.
- **Soft Consumer** — pastel or warm mid-tones, rounded sans, 16px+ corners, gentle shadows. Habit, wellness and family products.

Three directions on one canvas should rarely share a calibration shape.

## Fonts

- **Free for commercial use only** — Google Fonts, Fontshare, or Vercel's Geist family. Check the licence page when unsure.
- **Banned** as the vibe-coded defaults: **Inter, Instrument Serif, Outfit, Plus Jakarta Sans.**
- **Substitutions** when a reference uses a paid or banned face, surfaced to the member: Söhne → Hanken Grotesk or Public Sans · GT America → Schibsted Grotesk · Tiempos → Newsreader · Suisse Int'l or Helvetica Now → Public Sans · Inter → Public Sans or Manrope · Canela → Fraunces · Graphik → Albert Sans.
- **Distinctive free picks** to start from: Fraunces, Newsreader, Source Serif 4, Spectral, Cormorant Garamond, DM Serif Display, Bricolage Grotesque, Schibsted Grotesk, Hanken Grotesk, Public Sans, Manrope, Albert Sans, Onest, Funnel Sans and Display, Satoshi, General Sans, Switzer, Geist, JetBrains Mono, DM Mono, Geist Mono.

## Pitfalls

- **Compression shifts colour.** JPEG screenshots drift hexes; sample flat areas, not edges or gradients.
- **Rendering artifacts aren't palette.** Anti-aliasing fringes and photo highlights aren't colours to keep.
- **Dark-mode screenshot, light-mode brand.** Ask which the member means before deriving a dark system.
- **Liking the content, not the design.** A beautiful photo of a beach on a plain site is a photography note, not a layout note. Ask.
- **One reference doing everything.** If a direction's palette, type and layout all come from one image, it's a copy, not a direction.
