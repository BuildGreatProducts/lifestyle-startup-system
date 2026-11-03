---
kind: curated
last-reviewed: 2026-11-03
---

# Logo types and best practice

The seven logo types with an example of each in this folder, a decision tree, and the rules that make a mark survive every surface. Read in `brand-identity` step 7, where the member gets a **logo direction and a simple wordmark** — a full logo is out of scope for this system. Read again in `design-system` (Lite) for the variant rules.

## Contents

- [The meta-rule](#the-meta-rule)
- [The seven types](#the-seven-types)
- [Decision tree](#decision-tree)
- [The simple wordmark](#the-simple-wordmark)
- [Principles](#principles)
- [Variants](#variants)
- [What kills logos](#what-kills-logos)
- [Calibration](#calibration)

## The meta-rule

A logo is a mark that has to work at every size and in every colour treatment, from a 16px favicon to a billboard, for ten years. A mark that looks great in the deck but fails as an app icon, in dark mode or in one colour costs the brand twice: once to design, again to redesign.

## The seven types

| Type | Example in this folder | When to use it | Failure mode | Pair with |
|---|---|---|---|---|
| **Pictorial** — an image standing for the brand | [Apple](pictorial-1.svg) | Recognition is already earned, or you'll spend 5–10 years earning it | A new brand with a symbol alone is anonymous | A combination mark for the first years |
| **Lettermark** — initials | [IBM](lettermark-1.png), [CNN](lettermark-2.png) | A long or multi-word name people already abbreviate | Three letters with no story are forgettable | Strong custom type — the typeface is the brand |
| **Wordmark** — the name in distinctive type | [Disney](wordmark-1.png) | A short, distinctive name meant to be read | In an off-the-shelf font it's a placeholder, not a logo | A small square mark for favicon and avatar |
| **Combination** — name plus icon | [Amazon](combination-1.webp), [Levi's](combination-2.png) | You want both, with flexibility; the default for most brands | The icon can't stand alone, so it's decoration | A lockup spec (spacing, minimum size, icon-only version) |
| **Emblem** — text inside a badge or crest | [Starbucks](emblem-1.png) | Heritage, authority, institutional credibility | Fine detail turns to mush at small sizes | A simplified digital variant |
| **Abstract** — a meaningful shape | [Airbnb](abstract-1.png), [Nike](abstract-2.svg) | A unique, culture-neutral mark | Needs marketing scale to attach meaning | A clear story for what the shape means |
| **Mascot** — a character | [Mailchimp](mascot-1.webp) | Warmth and personality; consumer, education, food | Detail and personality don't scale down; can date | A face or silhouette avatar for small sizes |

## Decision tree

Stop at the first yes:

1. Willing to spend 5–10 years teaching a symbol? → **Pictorial**.
2. Long multi-word name, or an abbreviation already in use? → **Lettermark**.
3. Short, distinctive name meant to be read as the mark? → **Wordmark** + a small square derivative.
4. Need a name and an icon, flexible across surfaces? → **Combination**.
5. Signalling heritage or authority? → **Emblem** + a digital variant.
6. Global and wanting a culture-neutral mark? → **Abstract** + its story.
7. Consumer brand wanting warmth? → **Mascot** + an avatar version.
8. Stuck → **Combination** with a simple abstract or letter-derived icon. It's the easiest to evolve later.

For a member's first product, the honest answer is nearly always **3 or 4**: a wordmark now, an icon later once there's something to recognise.

## The simple wordmark

What `brand-identity` makes: the name, set in the chosen direction's heading face, with **one deliberate move** so it isn't just typed out:

- **Weight or width** pushed further than the body text uses it.
- **Tracking** opened or tightened beyond default (tight for confident, open for calm).
- **Case** — all lowercase (friendly), all caps (institutional), or one capital doing work.
- **One modified letter** — a cut, a joined pair, a dot replaced by the accent colour. One only.

Then derive the **small square mark** for favicon, app icon and social avatar: the first letter, a monogram, or the modified letter alone, on the primary colour. Check both at 16px and 48px.

Fails: the name in the body font at default settings (that's a heading, not a mark) · three moves at once · a move that only works in colour.

## Principles

1. **Simple** — sketchable from memory in five seconds.
2. **Versatile** — full colour, one colour, reversed, black and white, embroidered, at 16px.
3. **Scalable** — thin lines vanish first; test at the smallest size before approving.
4. **Timeless** — no effect of the moment (long shadows, glows, glass, AI blobs, purple gradients).
5. **Memorable** — one visual hook; "blue circle with a tick" has none.
6. **Relevant** — matches the belief, tone and look in `docs/3-BRAND.md`.
7. **Original** — not a template or a generator's average; logo generators are for exploring, never for the final mark.
8. **Works without colour** — the single most-tested criterion. If the form only works in colour, the form is broken.

## Variants

Every mark ships at least four:

| Variant | Use |
|---|---|
| Full colour | Site, app, packaging |
| One dark colour on light | Print, light mode |
| One light colour on dark | Dark mode, photo overlays |
| Pure black / pure white | Embossing, embroidery, single-colour print |

Design in black first, colour second. No gradients in the one-colour variants. Thicken strokes 5–15% when reversed if thin parts ghost. One or two brand colours plus black and white — never five. Slightly desaturate the primary for dark backgrounds.

## What kills logos

- **The look-alike.** Show the mark beside three competitors' to a stranger; if they can't pick it out, it isn't distinctive.
- **Five fonts, five colours.** Every extra one past two halves recognisability.
- **Designed at one size.** Never tested at 32px or 16px.
- **Relies on colour alone.** A name in a shade of blue is branding instructions, not a logo.
- **The founder's favourite colour.** The palette serves the brand and the category, not taste.
- **No lockup rules.** Without clear space and minimum size, it gets squished and recoloured.
- **Mascot or emblem without a small version.** Dies at favicon size.

## Calibration

| Criterion | Floor | Good |
|---|---|---|
| Recognisable at 16px | "It's something" | Clearly the brand |
| Variants | Colour only | The four above |
| Colours in the mark | 5+ | 1–2 |
| Works in pure black on white | No | Yes, designed for it from the start |
| Small square mark | Scaled-down full logo | Its own derived mark |
| Dark-mode version | Inverted | Designed, primary desaturated |

Below the floor on 16px or black-on-white? The fix is the shape, not the colour or the font.
