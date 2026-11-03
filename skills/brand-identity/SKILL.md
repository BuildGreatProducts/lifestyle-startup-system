---
name: brand-identity
description: >-
  Step 3. Gives the product a brand: name, worldview, contrarian belief and tone of voice in words,
  then gathers the member's visual references, explores three distinct visual directions side by
  side on a canvas, and refines the chosen one into a brand card (logo direction and wordmark,
  palette, type, mood). Writes docs/3-BRAND.md and saves the references to docs/brand/references/.
  Use when the member says "name my product", "build my brand", or "what should it look like". Not
  for tokens and components — use design-system; not without an offer — use product-offer.
---

# Brand identity

The step that gives the product one recognisable character: what it's called, what it believes, how it sounds and what it looks like. It runs in two halves. First the brand **in words** — the decisions everything else has to agree with. Then the brand **in pictures** — real references the member likes, three distinct directions on a canvas, and one chosen direction refined into a brand card. The next step turns that direction into tokens, so a vague look here becomes a generic product later.

Take the voice of a senior brand strategist and design director:

- **Opinionated and specific.** "Every coaching site in your niche is sage green and a script font — the wedge is to look like none of them" beats "have you considered other colours?"
- **Pattern-match** against real brands: "That's a Granola shape — calm, prosumer — not a Liquid Death shape."
- **Artifacts or it didn't happen.** Every element ends on something concrete: a name you can register, a sentence in the brand's voice, a hex, a typeface.
- **Show, don't describe.** Visual choices go on the canvas side by side, never as paragraphs of adjectives.
- **Blunt but kind** about generic drafts.

## Inputs

- `docs/2-OFFER.md` — **required**. The Summary, Customer and Offer feed the worldview, belief and tone; `## Product` → the `Shape:` line decides what the directions show. Missing or still a placeholder → run `product-offer` first; never improvise an offer.
- `docs/3-BRAND.md` and `docs/brand/references/` if they exist — a re-run. Carry the answers over, show what would change, and ask before overwriting a `Done` document.
- `docs/3-BRAND.md` with `Status: Extracted` — `path-finder` pulled it from an existing product. **Review mode:** walk each part with the member and sharpen it; run the visual references and the three directions only if they want a new look. Set `Done` when reviewed.
- [../product-offer/references/shapes.md](../product-offer/references/shapes.md) — the shape's row and its **Brand identity** note, which says full or lite. **Lite** shapes (an agent skill, MCP server or developer tool; a chat assistant, productized service or digital product runs the brand full) get: name, worldview and tone in full; the belief in one line; at least one reference; the three directions shown as a landing hero, listing tile, cover or client deliverable rather than an app screen. The brand card is still built.

## Workflow

The session takes 60–90 minutes. All research is yours; the member reacts to proposals and says what they like.

### 1. Read the offer and form a hypothesis

Read `docs/2-OFFER.md` in full. Then ask two questions, one at a time:

1. **"What's a brand you admire, in any category — and what exactly do you admire about it?"**
2. **"Do you have a working name already, and how attached are you to it?"**

State a three-sentence **working hypothesis** — a candidate worldview (from the offer's pain and mechanism), a tone direction (from the customer's world) and a visual lane (from what the product has to show) — and check it with the member.

**Done when:** the member has confirmed or corrected the hypothesis.

### 2. Research the category's defaults (live)

Know what the category looks and sounds like so every choice can deliberately differ. Read [references/brand-patterns.md](references/brand-patterns.md), then search for:

- **3–5 named competitors or alternatives** from the offer: their naming style, tone, stated beliefs (usually none — that's the opening) and visual lane.
- **The category default.** If five of five look the same, name that look out loud — it's what the directions must not become.
- **Adjacent-category breakthroughs** — brands outside the category with a distinctive identity. They become candidate references in step 4.
- **Name availability** for the working name or top candidates: a sensible domain, the handle where customers spend time, anything else ranking for the name in this category, and — for store, marketplace or registry shapes — the listing name and the host's trademark rules.

Collect 5–8 data points with links. No web search → say so, ask the member for comparables, and mark those claims unverified.

**Done when:** the category default is named in one line and the name candidates have availability results.

### 3. The brand in words

Go in order — **Name → Worldview → Contrarian belief → Tone of voice** — because each constrains the next. Read the matching section of [references/identity-deep-dive.md](references/identity-deep-dive.md) as you reach each one. For each:

1. **Propose a draft artifact** from the offer and the research — not "your worldview is about simplicity" but a sentence the member can nod at or argue with.
2. **Ask 1–3 sharp questions** to test it ("if you rebuilt the product tomorrow, would this belief survive?").
3. **Name drift** the moment an answer matches the category default, and offer the sharper version.
4. **Lock it** before moving on. A member who can't decide can take your research-backed pick, tagged `[recommended; revisit after first customers]` — that counts as done.

A working name the member is attached to gets a confirmation pass (the four checks), not a naming workshop.

**Done when:** a committed name with its checks, one-sentence worldview, one-sentence belief, and a tone with 3–5 "X but not Y" attributes, we-say/we-don't-say words and one example sentence nobody else could write.

### 4. Visual references

Without references the directions have nothing to aim at and drift to the average. Follow [references/visual-references.md](references/visual-references.md):

1. **Ask for them.** One or more sites, apps, brands, packaging, posters, screenshots, a Figma frame or a moodboard — **recommend 3–5**, at least one from outside the category. Remind the member of the brand they named in step 1.
2. **For each, ask what they like** — the type, the colour, the layout, the mood, or something else. One reference at a time.
3. **Read every image yourself** ([references/image-analysis-patterns.md](references/image-analysis-patterns.md)) and turn "I like it" into specific notes: approximate hexes, type classification and closest free font, density, corners, composition. Read the notes back so the member can say "yes, that" or "no, it's the other thing".
4. **No references?** Find candidates with [references/reference-finding.md](references/reference-finding.md): 6–9 across adjacent categories and the brand words, shown side by side; the member picks from those.
5. **Push for at least one.** Don't start the directions with zero. If the member still has none after seeing candidates, pick the two closest to the brand words, say they're your picks, and move on.
6. **Save them** to `docs/brand/references/` as `NN-short-name.<ext>` (screenshot a live site rather than linking it). Keep the source link and the member's words for each.

**Done when:** at least one reference (ideally 3–5) is saved, each with what the member likes and your translated notes.

### 5. Three directions on a canvas

Find and drive the canvas tool with [references/design-tools.md](references/design-tools.md) — `/design` first, then a connected design tool, then the HTML fallback. Lay out, left to right: a **references** artboard (every saved image with its one-line note), then **three direction artboards** side by side. Each direction shows:

- A short name and its idea in one line, in the brand's voice.
- **Palette** — 4–6 hexes with roles (background, text, primary, accent).
- **Type** — a heading and a body face, free for commercial use, never the banned defaults (rules in [references/image-analysis-patterns.md](references/image-analysis-patterns.md) → Fonts).
- **Mood** in three words, and the imagery lane.
- **The name set as a wordmark** in the direction's type.
- **A sample screen or cover** with real copy in the brand's voice — the home or hero screen for screen shapes; a landing hero, listing tile, cover or deliverable page for screenless ones.
- **Draws on** — which references it uses and exactly what it takes from each ("type from 02, palette temperature from 04").

The three must be **distinct blends, not three takes on one image**: each leads with a different reference, and they differ on at least two of type classification, colour temperature or value, and density or layout. None may match the category default from step 2 unless the member asks for it.

**Done when:** the canvas shows the references and three directions side by side, and you have its link.

### 6. Pick or mix

Walk the member through the three in two or three sentences each, then recommend one ("I'd go with B, because it's the only one that looks unlike your competitors and still feels like the tone"). The member picks one, or mixes: take one direction as the **base** and borrow named elements from another ("B, with A's serif headlines"). Redraw a mix on the canvas as its own artboard before going on — a mix that only exists in words falls apart when it becomes tokens.

**Done when:** one direction (or one redrawn mix) is chosen.

### 7. Brand card

Refine the chosen direction into a **brand card** artboard on the same canvas:

- **Logo direction.** Pick the logo type with the decision tree in [references/logo-types/logo-types.md](references/logo-types/logo-types.md) — almost always a wordmark or a combination mark at this stage — and make a **simple wordmark**: the name in the chosen type with one deliberate move (weight, tracking, case, or one modified letter). Show it in black on white, white on black, and as a small square mark at app-icon and favicon size. A full logo is out of scope; say so if the member asks.
- **Palette** final, each hex with its role; text colours checked for contrast on their backgrounds.
- **Type** pair with what each face is for.
- **Mood** — three words, the lane, and 2–3 composition rules ("type-led, generous white space, one accent per screen").

Then run the whole-identity checks from [references/identity-deep-dive.md](references/identity-deep-dive.md) → How the decisions compose (worldview → belief → tone → look → name agree; the customer could tell it apart from 3 of 5 competitors without the logo). Read the card back as one brand.

**Done when:** the brand card is on the canvas and every check passes, or the failing element was changed.

## Write docs/3-BRAND.md

```markdown
# Brand: <product name>

Status: Done
Updated: <YYYY-MM-DD>

## Brand card
| | |
|---|---|
| Name | <name> |
| Worldview | <one line> |
| We believe | <one line> |
| We sound | <3 words> |
| Look | <direction name> — <top reference> |
| Logo | <type> — <wordmark rule in a clause> |

## Name
<The name, the four checks one line each, the domain and handles to use.>

## Worldview
<One sentence.>

## Contrarian belief
<One sentence: most <category> believe…, we believe… because…>

## Tone of voice
<3–5 "X but not Y" attributes; we say / we don't say; one example sentence; how the tone bends for an everyday task, an error and a milestone.>

## Visual references
| File | Source | What the member likes | What it's for |
|---|---|---|---|
<One row per file in docs/brand/references/, linked; "what it's for" names the element it supplies to the chosen direction.>

## Visual direction
<Direction name and its idea in one line. Lane. Palette table (hex, role). Type (heading, body, why). Mood words. Composition rules. Draws on: reference → what it takes. One line each on the two directions not chosen, and why.>

## Logo direction
<Logo type and why; the wordmark rule; the small-size mark; the black-only and white-only check.>

## Canvas
<Link to the canvas, and what's on it: references, three directions, brand card.>

## Sources
<Competitors, category research and availability checks, with links.>
```

Use `Status: Draft` until the brand card passes.

## Verify before delivering

- [ ] Name, worldview, belief and tone are each a concrete artifact; the belief names a real opponent and no competitor could sign it.
- [ ] At least one reference is saved in `docs/brand/references/`, each with the member's words and your notes, and listed in the doc.
- [ ] The canvas shows three directions that lead with different references and differ on at least two visual axes; each says what it draws from which reference.
- [ ] Fonts are free for commercial use and off the banned list.
- [ ] The chosen direction has hexes with roles and named typefaces, so the design system can start without asking again.
- [ ] The brand card passes the whole-identity checks.
- [ ] The canvas link and every researched fact are in the doc.

## Next

**Build the design system** — `design-system`. It opens the chosen direction on this canvas and reads `docs/3-BRAND.md` and the saved references, so the member doesn't have to bring anything new.
