---
kind: curated
last-reviewed: 2026-11-03
---

# Identity deep dive

Good and bad calibration for each word-level decision in `brand-identity` step 3, the imagery lanes used in step 5, and the cross-checks run on the brand card in step 7. Read the section for the element in hand. Examples come from teardowns of category-defining brands; the frameworks underneath are April Dunford's positioning, Adam Morgan's challenger brands, Nielsen Norman Group's four dimensions of tone, and Mark and Pearson's archetypes.

## Contents

- [Name](#name)
- [Worldview](#worldview)
- [Contrarian belief](#contrarian-belief)
- [Tone of voice](#tone-of-voice)
- [Imagery lanes and composition](#imagery-lanes-and-composition)
- [How the decisions compose](#how-the-decisions-compose)
- [Lite treatment](#lite-treatment)
- [Going deeper: archetypes](#going-deeper-archetypes)

---

## Name

The bar is a **working name that passes four checks**, not a perfect one. Names appreciate with the product; nobody thought "Notion" or "Stripe" was remarkable on day one.

- **Say it** — "I use ___ for that" out loud, no stumbling, no explaining the pronunciation.
- **Spell it** — a stranger types it correctly after hearing it once. Creative misspellings (Lyft, Tumblr) cost traffic unless you can pay to teach them.
- **Search it** — a sensible domain (the .com or a clean get-/use-/-app variant), the handle where customers spend time, nothing else ranking for it *in this category* (shared with a landscaper is fine; with another coaching app is not).
- **Feel it** — it belongs next to the worldview and tone. A deadpan-punk brand called "FriendlyBot" fights itself.

Choosing fresh: pick **one naming direction** and generate 5–8 candidates only inside it — descriptive (Basecamp), evocative (Notion, Linear), invented (Zapier), compound (Mailchimp), real-word (Stripe, Arc, Slack). For a member selling their own expertise, their own name is a legitimate option when the product *is* their judgment; it caps the exit value, so say so.

| Bad | Good |
|---|---|
| "We're deciding between three names" — for another month | One committed working name, domain noted, revisit only if a check fails |
| A name you spell out on every call | A name a stranger types correctly after hearing it once |
| "AI" bolted on (dates it, crowds it) | A name about the customer's outcome, not the technology |
| The clever pun only the founder gets | The plain word that fits the tone |

## Worldview

The conviction underneath everything — what the brand believes about the world or its customers' lives, beyond any product. It's the belief that survives a pivot, and the one the best customers already hold before they meet you. Patagonia: "the planet can't sustain endless consumption." Basecamp: "work shouldn't be crazy."

Three tests, one sentence:

- **Pivot-proof** — rebuild the product tomorrow and it still stands. If not, it's a product claim.
- **Nod test** — the ideal customer reads it and thinks "finally, someone said it".
- **Argument test** — somebody would disagree. A worldview nobody could argue with is a platitude.

| Brand | Worldview | Why it works |
|---|---|---|
| Patagonia | The planet can't sustain endless consumption. | Bigger than gear; costs them growth; customers already believe it |
| Basecamp | Work shouldn't be crazy. | Polarising in hustle culture; a rallying cry |
| Duolingo | Education should be free and feel like play. | Excludes the credential-first view of learning |

Fails: "we believe in simplicity" (nobody argues for complexity) · "our product is the best way to X" (a product claim in a belief costume) · "AI will change everything" (a tribe of everyone is a tribe of nobody) · "we believe in our users" (excludes no one).

## Contrarian belief

The worldview applied to the category — the deliberately unfashionable position that makes the brand legible against everyone else. Dunford's *differentiated value* in narrative form; Morgan's point that a challenger must take a position the incumbent can't copy.

Structure: **"Most [category] believe [conventional wisdom], but we believe [opposite] — because [reasoning]."** The reasoning carries the weight: a customer truth, a shift, or an insight the incumbents ignore.

Tests: **a named opponent** (vague disagreement is weak) · **provably true** (test the premise against real customers) · **it costs something** (a belief that excludes nobody is marketing copy) · **no competitor could sign it**.

| Brand | Belief | Why it works |
|---|---|---|
| Linear | Most project tools believe more configuration = more value; we believe opinion is the product, because configuration debt slows teams more than it empowers them. | Defies Jira orthodoxy; names the cost |
| Liquid Death | Most water brands believe water should signal wellness; we believe it should be punk, because health brands treat customers like children. | Costs them the wellness segment |
| Patagonia | Most outdoor brands believe more sales = success; we believe buy less and make it last. | Visibly costs growth — which is the proof |
| Mailchimp | Most B2B brands believe buyers are rational; we believe B2B is emotional too. | Justifies the whole playful voice |

| Bad (universal) | Good (defensible) |
|---|---|
| "We believe in great design" | "We believe opinion is the product" |
| "We put the customer first" | "We believe you should buy less" |
| "Unlike legacy tools, we're modern" | What "modern" means, why it's better, and who it excludes |
| "We're like Stripe but for X" | *Why* the X version differs from Stripe |

For a member productizing their own service, the opponent is usually how the work is normally sold ("most agencies sell hours; we sell the finished thing at a fixed price, because clients buy outcomes").

## Tone of voice

How the brand sounds on every surface. Locate it on NN/g's **four dimensions** first — funny ↔ serious, formal ↔ casual, respectful ↔ irreverent, enthusiastic ↔ matter-of-fact — then write three deliverables.

**1. Attributes, 3–5, as "X but not Y".** The Mailchimp convention forces each one to exclude something: "Smart, but not academic. Authentic, but not stuffy. Helpful, but not bossy." Linear: precise, calm, opinionated. Headspace: calm, empathetic, never preachy.

**2. We say / we don't say.** Followable words, not principles: "We say *ship*, never *deploy*. We say *clients*, never *users*. We never say *unlock*, *seamless*, *empower*." "Avoid jargon" is too vague to follow.

**3. One example sentence** nobody could mistake for another brand. Linear: "We rebuilt notifications. They're faster now." Patagonia: "Don't buy this jacket." Test: read it aloud — if it could belong to three competitors, it isn't a voice yet.

**Voice stays; tone bends to the situation.** Write one line each for how the voice reads in an everyday task (invisible, plain), an error (calm specifics, the fix, at most one apology if it's our fault), and a genuine milestone (one brief line crediting the customer). The stressed reader always gets the plainest register. The full copy rules for buttons, errors and empty states come later, in `prototype-flows`.

| Bad | Good |
|---|---|
| "Professional yet friendly" | "Smart, but not academic. Authentic, but not stuffy." |
| "We're approachable but also experts" | "Confident, direct, human." |
| "We leverage best-in-class solutions" | Plain English a stranger would say out loud |
| Playful on the site, formal in the app, chirpy in emails | One voice on every surface, tone bending only to the situation |

## Imagery lanes and composition

Each direction in step 5 commits to **one lane**, following what the product genuinely has to show.

| Lane | When it fits | Example |
|---|---|---|
| Photography | Real people, places, outcomes | Patagonia, Airbnb, Tracksmith |
| Illustration | Warmth on a technical or abstract product | Notion, Mailchimp, Stripe |
| 3D / rendered | The product is an object or a space | Devices, spatial, game-adjacent |
| Type-led / flat graphic | The words are the visual; editorial confidence | The Economist, brutalist landing pages |
| Screenshot-first | The UI is genuinely beautiful and is the story | Linear, Arc, Raycast |

Make the lane specific: "photography" is not a brief; "shot on film, available light, real clients, never models" is. Say what's *not* in the image — Linear's site has no people at all.

Composition rules, 2–3 per direction: symmetric or asymmetric grid · generous or dense · type-led or image-led · centred or off-axis.

Fails: stock photography (even bad custom photos beat it) · "modern and clean" (tells a designer nothing) · the everyone-else moodboard · three lanes mixed across surfaces · "I'll know it when I see it" (the style has to be teachable to the next person and the next tool).

## How the decisions compose

The most common failure is decisions that contradict each other. Run these on the brand card:

- **Worldview → belief.** The belief reads as the worldview applied to this category. Unrelated → one is borrowed.
- **Belief → tone.** A punk belief in a polite corporate voice is a contradiction; so is calm authority with exclamation marks.
- **Tone → look.** "Punk, irreverent" doesn't pair with generous minimal white space; "calm, precise" doesn't pair with maximalist layering.
- **Name → everything.** A playful invented name on a sombre authority brand means one of them moves.
- **Distinctiveness.** The customer could tell this brand from at least 3 of 5 named competitors with the logo covered. If not, name the converging element and change it now.

The test behind all five: describe the brand as a person — name, beliefs, how they talk, what they wear — and a stranger should recognise them from the description alone.

## Lite treatment

For screenless shapes: name, worldview and tone run in full (the tone matters most — it's in every README, prompt and client email); the contrarian belief is one line; the lane is chosen for the surfaces that exist (listing, landing page, cover, deliverables).

## Going deeper: archetypes

Optional — a shorthand for the character behind the tone and look. Pick one primary, at most one secondary, never three.

| Archetype | Tone | Examples |
|---|---|---|
| Sage | Wise, calm, authoritative | The Economist, BBC |
| Explorer | Adventurous, independent | Patagonia, Jeep |
| Outlaw | Rebellious, irreverent | Harley-Davidson, Liquid Death |
| Magician | Visionary, transformative | Apple, Disney |
| Hero | Courageous, determined | Nike |
| Jester | Playful, witty | Old Spice |
| Everyman | Relatable, honest | IKEA, Levi's |
| Caregiver | Nurturing, protective | Volvo |
| Ruler | Premium, in control | Rolex |
| Creator | Imaginative, expressive | Lego, Figma |
| Innocent | Optimistic, simple | Dove |
| Lover | Passionate, refined | Chanel |

Contradictory pairs (Outlaw + Caregiver, Ruler + Jester) confuse the audience. In AI products Magician and Sage are over-represented; Creator, Explorer, Caregiver, Outlaw and Jester differentiate.
