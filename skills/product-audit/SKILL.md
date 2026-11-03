---
name: product-audit
description: >-
  Tears down a built product the way a senior product designer tears down a competitor: maps every
  screen from the code, runs it locally and screenshots every screen and state, critiques each
  through UX, conversion, retention and product, checks it against the member's own flows, tokens
  and voice, lays each flow on a canvas with findings beside the screens, and writes
  docs/audit/REPORT.md. Never edits app code. Use when the member says "audit my app", "tear down
  my product", "why aren't people sticking". Not for planning the fixes — use build-plan; not for
  security — use security-audit.
---

# Product audit

A teardown of the product as it actually renders. Every screen is captured, every flow is laid out on a canvas, and every finding points at something visible in a screenshot — so the member sees their product the way a new customer does, with a senior designer's notes beside it. It reads, runs, captures and reports; it **never edits the app's code**. Its top fixes become phases in the build plan, and its conversion and retention findings become go-to-market experiments.

Run it after go live once real people are using the product, before each growth push, and — for an existing product — before the build plan, so the plan fixes what the audit found.

Take the voice of a senior product designer doing a teardown for a client who's paying for honesty:

- **Evidence first.** The screenshots are the evidence. A finding without a screen behind it is an opinion.
- **Specific to this product.** "Add social proof" fits any app; "the pricing screen has no proof within a scroll of the Pro plan" fits this one.
- **Honest about severity, kind about the work.** Name what's working in every flow before what's broken.
- **Ranked, not listed.** Ten fixes in order of impact against effort beat fifty in a pile.

## Inputs

- **The product, runnable.** The codebase on the member's machine, or a local build. A live product with no local copy can be audited for its public screens only; signed-in screens then need the member's own screenshots or a local or test environment. Never sign in to production with real credentials.
- `docs/2-OFFER.md` — the customer, the job, the shape and the pricing. Missing: read the code, the front door and the README, then confirm audience, job and business model with the member in one question.
- `docs/5-FLOWS.md`, `docs/4-DESIGN.md`, `docs/3-BRAND.md` — optional. When each exists, the audit checks the product against it; when one is missing, say which check was skipped.
- `docs/audit/REPORT.md` if it exists — a re-run. Keep the old report for comparison and say which findings are fixed, still open, or new.

Product audit is for products with screens. For a screenless shape, audit only the screens it ships (a sales page, a key dashboard, an intake form) and say the rest is out of scope.

## Workflow

### 1. Understand the product

Pin down who it's for, the job it does for them and how it makes money, each sourced to a doc, a file or the member. Read the shape's row in [../product-offer/references/shapes.md](../product-offer/references/shapes.md) for its front door and what its magic moment looks like, and set the retention model with [references/activation-retention.md](references/activation-retention.md#set-the-retention-model-first). Critique without the job is decoration.

**Done when:** audience, job, business model, shape, retention model and the magic moment are stated and sourced.

### 2. Map every screen

Inventory screens **from the code**, not by clicking around: routes and pages, navigators and views, plus modals, sheets, dialogs, paywalls and emails the product sends. Group them into flows — the sequence a customer walks to get one thing done: the front door, sign-up and sign-in, onboarding to the magic moment, the core loop, create and edit, upgrade and checkout, settings and account, cancel. A screen can sit in more than one flow. For each screen, list the states worth capturing: first run and empty, populated, loading, error, returning, free and paid.

Write `docs/audit/screen-map.md`: every flow with its screens in order and their states. Every route or screen file in the code is in a flow or under **Not captured** with a reason.

**Done when:** the screen map covers every screen in the code, and the member has confirmed the flows.

### 3. Capture

Run the app locally and screenshot every screen and state in the map, following [references/capture.md](references/capture.md): Playwright for web at 390×844 and 1440×900, the simulator for iOS, test accounts and seed data only, nothing installed into the app's project. Say what you're doing in one line ("I'm running your app locally and capturing 46 screens at phone and desktop sizes — about ten minutes").

**Done when:** every screen and state has a file or a logged reason it doesn't, and a sample from every flow has been opened to confirm it rendered.

### 4. Critique

Look at every screenshot. Review each screen, then each flow end to end, then the product as a whole, through all four lenses in [references/lenses.md](references/lenses.md) — it holds the finding format, the severity scale and what each lens asks. Work the checks while you look:

- [references/audit-areas.md](references/audit-areas.md) — the conversion surfaces, design-system adherence and copy, item by item; numbers to cite from [references/conversion-benchmarks.md](references/conversion-benchmarks.md).
- [references/activation-retention.md](references/activation-retention.md) — the as-built path to the magic moment and the loop back.
- [../prototype-flows/references/design-heuristics.md](../prototype-flows/references/design-heuristics.md) — craft, cited by number.

Every finding: where, lens, problem, recommendation, severity, effort. One problem per finding; the same problem on several screens is one pattern finding. Each flow gets a verdict: steps to value, where people will drop, what's working, what to fix first.

**Done when:** every screen has been reviewed against all four lenses (a screen with no findings says so), and every flow has a verdict.

### 5. Check against the member's own docs

Run the doc checks in [references/lenses.md](references/lenses.md#checks-against-the-members-own-docs): does the shipped onboarding reach the magic moment named in `5-FLOWS.md` inside its target; do the screens use the `4-DESIGN.md` tokens; does the copy match `3-BRAND.md`'s voice and the flows doc's copy rules; does the front door keep the offer's promise and price. Drift between the plan and what shipped is Major by default.

**Done when:** each doc that exists has been checked, and each missing one is named as a skipped check.

### 6. Lay each flow on a canvas

Find and drive the canvas with [../brand-identity/references/design-tools.md](../brand-identity/references/design-tools.md) — `/design` first, then a connected design tool, then the HTML fallback at `docs/audit/canvas-<flow>.html`. **One canvas per flow.** The brief:

- One artboard per screen, sized to its capture, in flow order left to right, labelled `<NN> · <screen>`.
- Alternate states stacked beneath their screen; phone and desktop side by side where both were captured.
- The screenshot placed unaltered. This is a wall of evidence, not a redesign.
- Beside each screen, a card with its findings, severity-tagged, Critical first.
- A closing artboard: the flow's verdict, what's working, the top fixes.

**Done when:** every flow has a canvas that opens, and each link is recorded in the screen map.

### 7. Walk the member through it

Give the verdict and the top three fixes first, then open the canvases flow by flow. Ask about anything you couldn't judge alone — a constraint, a fix already in flight, a feature that's there on purpose — and adjust the ranking before writing the report.

**Done when:** the member has seen every canvas and agreed the top 10.

## Write docs/audit/REPORT.md

```markdown
# Product audit: <product name>

Status: Done
Updated: <YYYY-MM-DD>

## Verdict
<Three sentences: the product's biggest opportunity, the biggest leak, what to do first.>

## The product
<Audience, job, business model, shape, retention model, magic moment — each with its source. Commit captured.>

## Top 10
| # | Finding | Where | Lens | Severity | Effort |
<Ranked by impact on the job and the business against effort.>

## Flows
### <Flow> — <canvas link>
<Verdict: steps to value, where people drop, what's working. Then the findings table.>

## Against your docs
<Magic moment reached? Tokens used? Voice and copy rules followed? Offer kept? Each a line, or "skipped — no doc".>

## Product recommendations
<Positioning, magic moment, retention loop, monetisation — a short paragraph each.>

## For the build plan
<The fixes that need code, grouped into phase-sized chunks, in order.>

## For go to market
<The conversion and retention findings worth testing as experiments, each with the metric it moves.>

## Not captured
<Screens and states that couldn't be reached, and why.>

## Sources
<Commit, local URL, capture sizes and tools, benchmarks cited with their sources.>
```

## Verify before delivering

- [ ] Every route or screen in the code is in the screen map or under Not captured with a reason.
- [ ] Every screen and state has a screenshot, and samples were checked for blank or broken renders.
- [ ] Every finding points at a screen, has all six fields, and is specific to this product.
- [ ] Every flow has a verdict that names what's working, and a canvas link that opens.
- [ ] The doc checks ran for every doc that exists; skipped ones are named.
- [ ] Severities are honest; the top 10 is ranked by impact against effort.
- [ ] No app code was changed, and only test accounts, seed data and test-mode payments were used.

## Next

**Fix what it found** — `build-plan`, in existing-code mode: the "For the build plan" fixes become its phases. Once those ship, the "For go to market" findings become experiments in `go-to-market`. Re-run the audit before each growth push.
