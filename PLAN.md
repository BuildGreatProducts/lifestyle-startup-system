# Lifestyle Startup System — restructure plan

A new plugin, built on `~/Products/product-os-public` (ProductOS 2.0.0), for people with a skill who want to turn it into a product they can scale. Nine steps, numbered in order, each run by one skill and writing its own document.

## What changes, in one line

ProductOS runs on three layers (phase checklist → ROUTING.md → orchestrator skill → step skill → worksheet → BONUS playbook, all bent by 12 shape files). The new system has one layer: **the skill is the step**. Each skill carries its own reference docs and writes one file.

| | ProductOS 2.0 | Lifestyle Startup System |
|---|---|---|
| Skills | 45 | 12 (9 step skills + `start`, `path-finder`, `product-audit`) |
| Where reference material lives | ~12,700 lines in phase folders (checklists, worksheets, BONUS, shapes, routing) | Inside each skill's `references/`, trimmed and tagged (see Reference docs). Outside the skills: only README, START-HERE, setup guidelines |
| Outputs in `docs/` | ~25 files | 9 step docs, plus `0-PATH.md` and `audit/` for existing products |
| Shapes | 12 shape files steering every step | One short reference table, read by Offer and Go Live |
| Routing | PLAN.md → shape → checklist | `docs/0-PATH.md` if there is one, else which numbered docs exist |

## The nine steps

| # | Skill | Writes | Built from (ProductOS) |
|---|---|---|---|
| 1 | `idea-finder` | `docs/1-IDEA.md` | `define-idea-finder`, reframed around the member's skill |
| 2 | `product-offer` | `docs/2-OFFER.md` | `define-offer-builder` + `define-product-shape` + `define-customer-persona` + `define-pricing` + `define-offer-review` (as the closing pass) |
| 3 | `brand-identity` | `docs/3-BRAND.md` + canvas | `design-identity-creator` + tone-of-voice part of `design-ux-writing` |
| 4 | `design-system` | `docs/4-DESIGN.md` + `docs/4-DESIGN.html` | `design-design-system` + `design-design-system-from-code` |
| 5 | `prototype-flows` | `docs/5-FLOWS.md` + canvas | `design-magic-moment` + `design-onboarding-flow` + `design-landing-page` + microcopy from `design-ux-writing` |
| 6 | `build-plan` | `docs/6-BUILD-PLAN.md` | Replaces `develop-prd-roadmap`, `develop-build`, `build-loop`, `product-refactor`; modelled on the Chatterbox build plan; has a new-build mode and an existing-code mode |
| 7 | `security-audit` | `docs/7-SECURITY-AUDIT.md` | `develop-security-audit`, run after the build and before go live |
| 8 | `go-live` | `docs/8-GO-LIVE.md` | `develop-golive` + `develop-code-review` as its pre-flight, run as a step-by-step walkthrough |
| 9 | `go-to-market` | `docs/9-GO-TO-MARKET.md` | `distribute-gtm-strategy` + `distribute-growth-experiments` + `distribute-scale-automate` |
| – | `start` | – | `setup` + `continue` merged: installs, then says where you are and runs the next step |
| – | `path-finder` | `docs/0-PATH.md` | `product-audit` (scoring + plan) + the extraction part of `define-from-code` |
| – | `product-audit` | `docs/audit/` + a canvas per flow | `app-teardown`, with `develop-cro-audit`, `develop-design-review`, `develop-design-better` and `distribute-activation-retention-audit` as its references |

Numbered filenames make progress visible at a glance, and "where am I" becomes "which is the highest number that exists" — or, for an existing product, "the next open step in `0-PATH.md`".

`start` asks one question when there's nothing in `docs/` yet: no idea → step 1; an idea → step 2; something already built (code, prototype, live service, store listing) → `path-finder`.

Naming: the old ProductOS `product-audit` (score the project, write a programme) becomes `path-finder`, pairing with `idea-finder`. The name `product-audit` goes to the new teardown skill.

### 0. Path finder (existing products)
- Looks at what exists — codebase, live site, landing page, store listing, prior docs — and scores it against the nine steps with evidence.
- For each step, marks it **Do** (missing or weak), **Fast-track** (extract a draft from what exists, then review it with the member) or **Done** (good enough to build on), with one line of why.
- Fast-track drafts are written straight into the step's doc, marked as extracted, so the step skill only has to review them: the offer from the landing page into `docs/2-OFFER.md`; the design system from the code via `design-system`'s from-code mode.
- Where the product has screens a member can reach, the path includes `product-audit` before `build-plan`, so the plan's phases fix what the audit found.
- `docs/0-PATH.md`: the scorecard, then the path — the steps in order with their mark, as checkboxes. `start` follows it.
- References: `scorecard.md`, `extract-offer.md`.

### 1. Idea finder
- Starts from the member's skill (craft, profession, service they already sell), not "what should I build".
- Keeps: inventory, 3–5 candidates, willingness-to-pay gate, live research, converge on one.
- Output: the chosen idea, who pays, why now, and the runners-up. Short.
- References: `idea-audit.md`, `validation-cheat-sheet.md`, `patterns.md`.

### 2. Product offer (one skill, one doc)
Sections, in this order, each a short conversation with live research:
1. **Customer** — who, their situation, where they hang out (persona, trimmed to what later steps use).
2. **Offer** — pain, outcome, mechanism, guarantee, proof.
3. **Product shape** — what form it takes (app, digital product, service, agent skill…), picked from one table.
4. **Pricing** — model, 2–3 real anchors, launch price, the price line.
5. **Review** — the failure-pattern check from `define-offer-review`, applied before writing.

References (loaded only for the section in hand): `offer-examples.md`, `offer-failure-patterns.md`, `ai-era-patterns.md`, `customer-examples.md`, `shapes.md`, `pricing-models.md`, `business-models.md` (trimmed from 538 lines).

### 3. Brand identity / visual direction (canvas)
1. Brand in words: name, worldview, contrarian belief, tone of voice (from identity-creator).
2. **Visual references.** The skill asks the member for one or more visual references: sites, apps, brands, packaging, posters, screenshots, a Figma frame or a moodboard. It recommends 3–5. For each, the member says what they like about it (the type, the colour, the layout, the mood), and the skill reads each image to pin that down. A member with none is shown a short set of candidates the skill has found from adjacent categories and the brand words, and picks from those. References are saved to `docs/brand/references/`. Without references the explorations have nothing visual to aim at, so the skill pushes for at least one before moving on.
3. Style exploration on a canvas: 3 distinct visual directions (type, colour, mood, a sample screen or cover each), side by side, built from the brand words **and** the references. Each direction names which references it draws on and what it takes from each, so the three are distinct blends rather than three takes on one image.
4. Member picks one (or mixes); refine into a brand card: logo direction and wordmark, palette, type, mood.
5. Write `docs/3-BRAND.md`: the words, the references with what each is for, the chosen direction, and a link to the canvas. Hands straight on to `design-system`, which reads the same references.

Canvas tool, detected in this order: `/design` in Claude Code → Figma / Paper / MagicPath / Pencil / Stitch via MCP → an HTML canvas page as fallback. One reference file says how to drive each; `brand-identity`, `design-system`, `prototype-flows` and `product-audit` all share it.

References: `identity-deep-dive.md`, `brand-patterns.md`, `logo-types/` (with the images), `visual-references.md` (what makes a useful reference, how to ask for them, how to turn "I like this" into specific type, colour and layout notes), `image-analysis-patterns.md`, `design-tools.md`.

### 4. Design system
Turns a visual source into the tokens and components every later step builds with. The skill takes its intake in this order:
1. **Primary: the chosen direction on the brand-identity canvas.** The skill opens the step 3 canvas, reads the picked direction (or the mix the member chose) and `docs/3-BRAND.md`, and builds the system from that. This is the normal path, with no question asked.
2. **Secondary: an image reference.** The step 3 references in `docs/brand/references/` come along with the direction, so this is for when there's no chosen direction yet, or the member wants to pull in something specific (a screenshot, Figma frame or live site they love). When there is a chosen direction, the image adjusts it rather than replacing it, and the skill says what changed.
3. **From code, for existing products only.** Called by `path-finder`: colours, type, spacing, radii and components read from CSS variables, Tailwind config and theme files, with competing values settled with the member.

With no canvas direction and no image, the skill sends the member back to `brand-identity` rather than inventing a style.

Writes `docs/4-DESIGN.md` in Google's DESIGN.md format (YAML tokens + prose) and `docs/4-DESIGN.html`, a live style guide. Lite mode (brand tokens only) for screenless shapes like agent skills and services. `prototype-flows` designs with these tokens; the build plan's design-catalogue phase builds them.

References: `reference-design.md`, `from-code.md` (extraction rules from `design-design-system-from-code`); uses `image-analysis-patterns.md` from `brand-identity`.

### 5. Prototype flows (journeys first, then screens)
1. **User journeys** — the 3–5 journeys that matter (discover → sign up → magic moment → pay → come back), as a diagram and a short list. Magic moment named here.
2. **Key flows on canvas** — full screens for each key flow in the brand and design system from steps 3 and 4: landing page, onboarding to the magic moment, the core loop, paywall/checkout, settings/account. Real copy, not lorem.
3. `docs/5-FLOWS.md`: the journeys, the screen list per flow with canvas links, and the copy rules (voice in practice: buttons, errors, empty states).

References: `magic-moment-benchmarks.md`, `onboarding-best-practice.md` (one file, folding the 13 per-shape files into sections), `landing-page-best-practice.md`, `ux-writing.md`, `design-heuristics.md`.

### 6. Build plan (lean on how Opus plans)
The skill is short: inputs, the doc's shape, a handful of rules, and the Chatterbox plan as a worked example. No PRD, no separate roadmap.

The doc's shape (taken from Chatterbox):
1. One-paragraph summary: what it is, platform, stack in a clause.
2. **Stack** — table: layer, choice, why.
3. **Key choices** — each with the choice, how it works, and the alternative considered.
4. **Architecture** — one diagram, one paragraph.
5. **Data model** — table of tables/collections, plus storage and access rules.
6. **Core logic** — one short section per subsystem (the parts an agent would get wrong).
7. **Build phases** — numbered from 0, each a checklist ending in **"Done when:"** with a test a person can run. Phase 0 = accounts and empty app on device; phase 1 = design catalogue matching the canvas; then local core loop, first run, accounts, payments…; last = launch.
8. **Launch requirements** — store / platform rules and a test checklist.
9. **Open questions** — checkboxes.

Rules: every phase ends runnable; the design catalogue phase comes before features; payments get their own phase; settings only the member can set are listed separately. Building itself = "work the phases in order, tick the boxes, commit at each phase" — carried by the root `CLAUDE.md`/`AGENTS.md` that `start` wires in.

**Existing-code mode (the old refactor).** When there's already a codebase, the skill baselines it first (what's there, what works, what the stack is), then writes the same doc with three differences:
- The Stack and Data model sections show **current → target**, with keep / change / remove on each row.
- A **Keep or remove** section lists each existing feature against the flows from step 5, with the member's decision.
- Phase 0 is "safe to change": version history on, the app runs locally, a smoke test passes. Later phases close the gap from current to target, each still ending in "Done when".
Moving off a prompt-to-app platform (Lovable, Bolt, Replit…) is a phase 0 variant, not a separate skill.

References: `example-build-plan.md` (Chatterbox, cleaned up), `stack-options.md` (trimmed from 581 lines), `existing-codebase.md` (baseline and gap rules, from `develop-prd-roadmap`), `platform-migration.md` (from `develop-migrate`).

### 7. Security audit (between build and go live)
Runs once the build plan's phases are done, before anything goes live. Same core as `develop-security-audit`:
- Audits the whole app, worst risks first: secrets in code, database access control, unprotected routes, one customer reading another's data (IDOR), exposed keys; then agent-tool risks such as prompt injection for AI products.
- Verifies each finding down to a concrete way it could be exploited, so nothing is a guess.
- `docs/7-SECURITY-AUDIT.md`: a launch verdict (**Ready**, **Ready after fixes**, **Not ready**) and a checkbox fix plan split into **agent fixes** and **only you can do this** (rotating keys, dashboard settings).
- Never fixes on its own. After the member has read the plan, it offers to work the agent fixes, then re-checks each one and updates the verdict.
- `go-live` won't start while the verdict is **Not ready**.

References: `security-checklist.md`, `agent-tools-tier.md`, `security-audit-template.md`.

### 8. Go live (walk-through)
- Same audit and `go-live-by-shape` content as `develop-golive`, with a short code-review pass as its pre-flight. It reads the security verdict first and stops if there are open blockers.
- Behaviour change: the agent walks the member through one step at a time — explains it, does its part, tells the member exactly what to click, waits for "done", checks it worked, moves on. Ends with a real-customer smoke test.
- `docs/8-GO-LIVE.md` doubles as the checklist and the record.

References: `go-live-by-shape.md`, `code-review-checklist.md`.

### 9. Go to market (actions, not strategy docs)
Same three stages, each written as a list of actions the member ticks off:
1. **Strategy** — 3 ranked channels, each with 5–10 concrete actions for the first 30 days.
2. **Experiments** — 3 experiments at a time, each: action, metric, how long, what counts as a win. A tracker table in the same doc.
3. **Scale and automate** — for each proven winner: do more, do better, automate (with the human check).

The skill opens at whichever stage the doc shows is next, and is meant to be re-run.

References: `distribution-channels.md`, `experiments-library.md`, `ai-distribution-tools.md`, `measurement.md`.

### Product audit (any time there are screens)
A teardown of the built product, the way a senior product designer tears down a competitor. It never edits app code; it reads, runs, captures and reports.

1. **Understand the product** — audience, job and business model from `docs/2-OFFER.md` (or the code and the member).
2. **Map every screen** — from the code (routes, screens, views, modals, paywalls), grouped into flows, with the states worth capturing (empty, populated, loading, error, first-run, free vs paid).
3. **Capture** — run the app locally and screenshot every screen and state (Playwright for web at phone and desktop sizes; the iOS simulator for native). Test accounts and seed data only.
4. **Critique** — every screen, every flow, then the whole product, through four lenses: **UX, Conversion, Retention, Product**. Each finding: where, lens, problem, recommendation, severity (Critical / Major / Minor / Polish), effort (S / M / L). Findings point at pixels, one problem per finding, nothing generic, and each flow names what's working.
5. **Lay each flow on a canvas** — one artboard per screen in flow order, states stacked beneath, the screenshot unaltered, a findings card beside each screen, and a closing artboard with the flow's verdict and top fixes.
6. **Report** — `docs/audit/REPORT.md`: verdict, top 10 by impact against effort, per-flow findings with canvas links, product recommendations, and what couldn't be captured.

Where it fits: recommended after go live once real people are using it, re-run before each growth push, and placed by `path-finder` before `build-plan` for existing products. Its top fixes feed straight into `build-plan` (existing-code mode) as phases, and its retention and conversion findings feed `go-to-market` experiments.

The lenses also check the work against the member's own docs: does the onboarding reach the magic moment in `5-FLOWS.md`, do the screens use `4-DESIGN.md` tokens, does the copy match `3-BRAND.md`'s voice.

References: `lenses.md` (the four lenses, expanded from `app-teardown`), `conversion-benchmarks.md` and `audit-areas.md` (from `develop-cro-audit`), `activation-retention.md` (from `distribute-activation-retention-audit`), `design-heuristics.md` (shared with `prototype-flows`), `capture.md` (web and iOS capture recipes).

## Reference docs

The reference docs are kept: each moves into the skill that uses it, under `skills/<skill>/references/`. Each skill names the file at the point it needs it, so the agent loads a file only when it reaches that part. The references carry the judgment, and live research covers whatever changes.

### Three kinds

| Kind | What it holds | How the skill uses it |
|---|---|---|
| **Curated** | Judgment the agent can't research: good/bad calibration, worked examples, failure patterns, rubrics and scorecards, the shape of each output doc | Follows it. This is the system's IP and what keeps output consistent between members |
| **Checklist** | What must be checked, where missing a check is the expensive failure (security, go-live, platform rules) | Works through every item, and confirms the current specifics live (today's App Store rules, a provider's current key-rotation steps) |
| **Research** | How to look something up that goes stale: what to search, which sources to trust, what to bring back | Runs the research fresh each time and cites what it found in the member's doc. Holds no frozen lists of tools, prices or competitors |

### Rules

1. Every reference opens with frontmatter: `kind: curated | checklist | research` and `last-reviewed: YYYY-MM-DD`.
2. **Trim what Opus already knows, keep what changes its output.** Generic best-practice explanation goes; examples, patterns and "why this one fails" notes stay. So `business-models.md` shrinks a lot from 538 lines, and `offer-examples.md` stays almost whole.
3. When a checklist or research reference is more than 6 months past `last-reviewed`, the skill tells the member it's leaning on fresh research for that part. `lint-skills.py` flags those files for the maintainer.
4. A reference shared by several skills (`design-tools.md`, `design-heuristics.md`) has one owner skill. The others point to it, so no copies drift apart.

### Every reference, tagged

| Skill | Curated | Checklist | Research |
|---|---|---|---|
| `path-finder` | `scorecard.md`, `extract-offer.md` | | |
| `idea-finder` | `idea-audit.md`, `validation-cheat-sheet.md`, `patterns.md` | | `market-research.md` (demand, competitors, where buyers gather) |
| `product-offer` | `offer-examples.md`, `offer-failure-patterns.md`, `ai-era-patterns.md`, `customer-examples.md`, `shapes.md`, `pricing-models.md`, `business-models.md` | | `pricing-research.md` (real price anchors), `customer-research.md` (communities, language, alternatives) |
| `brand-identity` | `identity-deep-dive.md`, `brand-patterns.md`, `logo-types/`, `visual-references.md`, `image-analysis-patterns.md` (owner) | | `design-tools.md` (owner; how to find and drive the canvas tool in this harness), `reference-finding.md` (where to find candidate references when the member has none) |
| `design-system` | `reference-design.md`, `from-code.md` (uses `image-analysis-patterns.md` from `brand-identity`) | | |
| `prototype-flows` | `magic-moment-benchmarks.md`, `onboarding-best-practice.md`, `landing-page-best-practice.md`, `store-listing-best-practice.md` (confirm current store rules live), `ux-writing.md`, `design-heuristics.md` (owner) | | |
| `build-plan` | `example-build-plan.md`, `existing-codebase.md` | `platform-migration.md` | `stack-options.md` (how to pick and verify a current stack, replacing the 581-line list) |
| `security-audit` | `security-audit-template.md` | `security-checklist.md`, `agent-tools-tier.md` | |
| `go-live` | | `go-live-by-shape.md`, `code-review-checklist.md` | |
| `go-to-market` | `experiments-library.md`, `measurement.md`, `channel-playbooks.md` (how each channel type works) | | `channel-research.md` (named communities and directories for this niche), `ai-distribution-tools.md` |
| `product-audit` | `lenses.md`, `activation-retention.md`, `conversion-benchmarks.md` | `audit-areas.md`, `capture.md` | |

`distribution-channels.md` (506 lines) splits in two: how each channel type works stays curated as `channel-playbooks.md`; the named lists become `channel-research.md`.

## What gets dropped (or parked)

| Dropped | Why |
|---|---|
| 4 phase orchestrators, `ROUTING.md`, 4 checklists, numbered worksheets | The skill is the step; `start` does the routing |
| 12 shape files | One table in `shapes.md` |
| `product-refactor`, `define-from-code`, `design-design-system-from-code`, `develop-migrate` | Folded into `path-finder` (extraction), `design-system` (from-code mode) and `build-plan` (existing-code mode) |
| `develop-cro-audit`, `develop-design-review`, `develop-design-better`, `distribute-activation-retention-audit` | Become `product-audit`'s references |
| `ship-in-7`, `sell-in-30` | Challenges removed |
| Coach-composed `PLAN.md` | `start` asks where you are; `path-finder` writes the path for existing products |
| `design-app-listing`, `design-marketplace-listing` | Folded into `prototype-flows`: for store-first shapes the front-door flow is the store listing (`store-listing-best-practice.md`) |
| `design-prompt-generator`, `develop-agent-evals`, `develop-feature-finder`, `define-business-strategy` | Out of scope for v1 |
| `GLOSSARY.md`, `status.py` checklist parsing | Plain words in the skills; status = which docs exist |

## New repo layout

```
lifestyle-startup-system/
├── .claude-plugin/  .codex-plugin/  .cursor-plugin/  .agents/
├── README.md  START-HERE.md  CHANGELOG.md  LICENSE.md
├── hooks/                session-start greeting (simplified)
├── setup/                CLAUDE.md, AGENTS.md wired into the member's root
├── scripts/              lint-skills.py (kept), status.py (rewritten, tiny)
└── skills/
    ├── start/
    ├── path-finder/
    ├── product-audit/
    ├── idea-finder/        SKILL.md + references/
    ├── product-offer/
    ├── brand-identity/
    ├── design-system/
    ├── prototype-flows/
    ├── build-plan/
    ├── security-audit/
    ├── go-live/
    └── go-to-market/
```

## How we build it

1. **Scaffold** — copy manifests, hooks, setup, scripts and licence from product-os-public into this folder; rename to `lifestyle-startup-system`; `git init`.
2. **Port references** — move each BONUS doc, worksheet and skill reference into the skill that uses it; trim, split and merge as listed above; add the `kind` and `last-reviewed` frontmatter; add the staleness check to `lint-skills.py`.
3. **Write the twelve skills** — the nine step skills in order, then `product-audit`, `path-finder` and `start`; each under ~200 lines, run through `lint-skills.py`.
4. **Rewrite the front door** — README, START-HERE, setup guidelines, session-start hook, status script.
5. **Dry run** — take one real skill (e.g. a sample service business) through all nine steps in a scratch folder, in Claude Code and one other harness; then run `path-finder` and `product-audit` on an existing project (e.g. Chatterbox) and follow the path into existing-code mode; fix what breaks.

## Decisions (settled 2026-11-03)

1. **Shapes** — all 12 kept as rows in one table; flows and go-live guidance written mainly for web app, mobile app, digital product and productized service.
2. **Existing products** — `path-finder` plots a path through the steps; refactor lives inside `build-plan` as existing-code mode; the challenges are removed.
3. **Coach-composed `PLAN.md`** — dropped.
4. **Build plan location** — markdown in the repo; optionally mirrored to a Claude Doc in Claude Code.
5. **Logo** — direction and a simple wordmark in step 3; a full logo is out of scope.
6. **Names** — no prefix; the plugin namespace `lifestyle-startup-system:` keeps them apart from ProductOS.
7. **Design system** — kept as its own skill (step 4), after brand identity. Its primary intake is the chosen direction on the brand-identity canvas, then an image reference; from code only for existing products.
8. **Product audit** — a teardown skill reviewing UX, conversion, retention and product, with a canvas per flow; usable any time there are screens.
9. **Security audit** — kept as its own skill (step 7), between the build and go live; its verdict gates `go-live`.
10. **Numbering** — steps run 1–9 in order, no a/b sub-steps; each doc's number is its step.
11. **Reference docs** — kept inside each skill, tagged curated, checklist or research; anything that goes stale is researched live instead of stored.
12. **Visual references in brand identity** — the skill asks for one or more visual references (3–5 recommended) and builds the explorations from them plus the brand words; it finds candidates when the member has none.
13. **Offer summary** — the pitch at the top of `docs/2-OFFER.md` includes the price, so it reads as a complete offer.
