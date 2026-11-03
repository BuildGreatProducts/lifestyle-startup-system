---
kind: curated
last-reviewed: 2026-11-03
---

# Visual references

How `brand-identity` step 4 collects references and turns "I like this" into notes the directions can be built from. The references are the visual half of the brief; the brand words are the other. Saved references are inspiration for the member's own direction — never copied into the product.

## Contents

- [What makes a useful reference](#what-makes-a-useful-reference)
- [How to ask](#how-to-ask)
- [Capturing what they like](#capturing-what-they-like)
- [Turning "I like this" into notes](#turning-i-like-this-into-notes)
- [Saving them](#saving-them)
- [From references to three directions](#from-references-to-three-directions)
- [Why references fail](#why-references-fail)

## What makes a useful reference

| Useful | Not useful |
|---|---|
| A real thing the member has seen and reacted to | A trend roundup or "best websites of the year" list |
| Something with one clear quality to take (the type, the colour, the restraint) | A screenshot liked for "everything" |
| At least one from **outside the category** — packaging, a magazine, a shop sign, a book cover, an album | Five direct competitors |
| A mix of kinds: one screen, one non-screen, one mood | Five near-identical SaaS hero sections |
| Specific: *this* page, *this* label | "Apple" or "something like Notion" with no page in mind |

A good set of 3–5 usually has one reference for **type**, one for **colour**, one for **layout or density**, and one for **mood**. They can overlap; the point is that every visual decision has something to aim at.

## How to ask

One question, with examples of what counts:

> "Now the fun part. Share a few things whose look you love — websites, apps, brands, packaging, posters, book covers, a screenshot, a Figma frame or a Pinterest board. Three to five is ideal, and at least one from outside your industry. They don't have to look like what you're building. Earlier you mentioned [admired brand] — that's a great first one."

- Accept anything: a URL, an image, a file path, a Figma link, a description of something they can't find ("the Aesop shop I walked past").
- A described reference → find the image yourself and check it's the one they mean.
- One reference arrives → ask for one more from outside the category before moving on; don't demand five.
- Member is stuck → offer candidates ([reference-finding.md](reference-finding.md)). Never start the directions with none.

## Capturing what they like

For each reference, one at a time: **"What do you like about this one — the type, the colours, the layout, the mood, or something else?"** Then one follow-up that forces a specific:

- Type → "The big headline, or the small text?" "Is it the serif, or how much space it gets?"
- Colour → "The cream background, or the one orange button?" "Would you want it this dark?"
- Layout → "How empty it is, or how it's arranged?"
- Mood → "If this were a person, what would they do for a living?"

Also ask what they **don't** like about it. "I like the type but it's too cold" is the most useful sentence in the step.

## Turning "I like this" into notes

Read the image ([image-analysis-patterns.md](image-analysis-patterns.md)), then write the member's words and your translation side by side. Read the translation back for a yes or a correction.

| The member says | The note |
|---|---|
| "I love how calm Aesop feels" | Warm low-saturation palette (amber `#8A6A3B`-ish on cream `#F6F1E7`); serif-led, small sizes, wide tracking on labels; dense text blocks with large margins; no photography of people; type-led. Takes: *palette temperature, label treatment* |
| "The Stripe homepage, the colours" | Saturated gradient accent on white; the gradient is the *only* saturated element; neutral grey type. Takes: *one saturated accent against neutrals* — not the gradient itself, which is now a category default |
| "This poster — it just pops" | Two flat colours at full saturation, heavy condensed sans set huge, tight leading, edge-to-edge type. Takes: *headline scale and weight* |
| "I like that it's simple" (a minimal app) | Ask which simple: one accent colour? few elements per screen? no borders? Here: one accent, flat surfaces, 8px corners, 24px+ gaps. Takes: *density and restraint* |
| "The vibe of this Instagram account" | The photography: film grain, natural light, warm shadows, candid subjects. Takes: *imagery lane and photo style*, nothing about the interface |

Each note ends with **Takes:** — the one or two qualities this reference supplies. That's the line the directions cite.

## Saving them

- Save each to `docs/brand/references/NN-short-name.<ext>` (`01-aesop-shop.png`). Number in the order received.
- Live site → screenshot the part they mean (above the fold, or the specific page), not the whole site. No browser tool → ask the member for a screenshot.
- Figma frame → export or screenshot through the connected tool; otherwise ask for a screenshot.
- Downloading an image from the web → ask the member first; a screenshot is usually enough.
- Keep the source URL, the member's words and your note for each — they go into `docs/3-BRAND.md` → Visual references.

## From references to three directions

Build a small matrix before drawing anything: references down the side, **type · colour · layout · mood** across, each cell the quality that reference could supply. Then assign:

- Each direction **leads with a different reference** — its strongest quality sets the direction's character.
- Each direction **borrows from one or two others** for the elements its lead doesn't cover.
- The brand words decide what can't come from a reference: a "calm, precise" tone rules out the poster's maximalism for body layout even if the member loves the poster's headlines.

| | Lead | Type from | Colour from | Layout from |
|---|---|---|---|---|
| A | 01 Aesop | 01 | 01 | 03 |
| B | 03 poster | 03 | 02 (one accent) | 03 |
| C | 04 film photos | 01 (labels) | 04 | 02 |

One reference only → the three directions push it in three ways (its type with a different palette; its palette with a different layout; its mood in a different lane), and say so.

## Why references fail

- **The competitor clone.** All references are direct competitors → the directions converge on the category default. Fix: ask for one from outside the category, or find it.
- **The Dribbble shot.** A concept nobody shipped, liked for its polish. Fine for mood; never the lead for layout, because it was never built for real content.
- **Vibe only.** "I like the feel" with no specific. Fix: the follow-up questions above until one quality is named.
- **The photo, not the design.** The member likes the picture on the page. Fix: separate the imagery note from the interface note.
- **References that fight.** One dark and dense, one light and airy. Don't average them into grey; give each its own direction and let the member choose.
- **The member's own old site.** Useful as a "not this" — ask what they want to keep from it, if anything.
