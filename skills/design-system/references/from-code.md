---
kind: curated
last-reviewed: 2026-11-03
---

# Design system from code

For `design-system`'s from-code mode, used for existing products (called by `path-finder`). Instead of a direction becoming a new system, the system already living — implicitly and inconsistently — in the codebase is written down as `docs/4-DESIGN.md`. Every shipping codebase has three blues that all mean "primary", button padding forked between components, and a `--color-text` variable half the code ignores. The job: find the de-facto system, surface every internal conflict, let the member pick the canonical value for each role, and document the result.

**Document reality; don't silently improve it.** Capture the real fonts, palette and scale. The only things resolved are internal inconsistencies and banned fonts — always with the member. Quality issues (a pair failing contrast, a paid font, a sprawling type scale) are advisories given outside the file. A design system that lies about the code is worse than none.

## Contents

- [Voice](#voice)
- [Workflow](#workflow)
- [Styling architectures](#styling-architectures)
- [Inconsistency patterns](#inconsistency-patterns)
- [Resolution heuristics](#resolution-heuristics)
- [Advisories](#advisories)

## Voice

A senior design-systems engineer doing a brownfield audit — evidence-led and conflict-precise:

> "`#2563EB` appears in 34 places, `#2D6CDF` in 6 and `#3B82F6` in 2, all as the primary action colour. I'd make `#2563EB` canonical `primary` — it's the most used and the one in `tailwind.config.ts`. Keep it?"

Never "there are some inconsistencies". Where a category has no system at all (elevation as ad-hoc shadows), say so and propose the smallest defensible one, flagged as a proposal, not a discovery.

## Workflow

1. **Set expectations** in one line: scan, inventory, conflicts one at a time, then write. An existing `docs/4-DESIGN.md` makes this a reconciliation — say so.
2. **Map the styling architecture** before extracting any value ([Styling architectures](#styling-architectures)), and state it back: "Tailwind config with a partial theme, plus ~40 arbitrary-value escapes; the conflicts are mostly in the escapes." In a monorepo, ask which app to document — never blend two products.
3. **No UI code** (a pure backend, CLI or MCP server) → there's nothing to extract; run the normal Lite intake from the brand instead. Only a docs site or landing page → extract from that and keep to the Lite set.
4. **Extract the inventory** with counts and locations: every colour literal and variable; every family, size, weight, line height and tracking (and which fonts are actually loaded); every spacing value (detect the base unit); every radius by component type; every shadow, blur and border-as-elevation; every recurring primitive and its values, including forks.
5. **Cluster into conflicts** ([Inconsistency patterns](#inconsistency-patterns)) — one entry per role, with competing values, counts, representative locations and your recommended pick. A banned font is always a conflict. Summarise before resolving: "Clean on radius. 9 conflicts: 3 primary blues, 2 body greys, button padding forked 3 ways, 4 off-grid spacings, two Button components."
6. **Walk the conflicts one at a time**, each with a recommendation from the [heuristics](#resolution-heuristics); the member decides. Values not picked stay in the code as **drift** — the file names the canonical value, and `product-audit` and the build plan fix the code later.
7. **Assemble the file** to [reference-design.md](reference-design.md): canonical tokens under semantic names, the consolidated scales, a component entry per primitive. `Source:` reads "extracted from code". Record consolidation decisions briefly in `## Colors`, `## Typography` and `## Do's and Don'ts` ("Do use `#2563EB` for primary actions — not the legacy `#3B82F6`").
8. **Show it in two passes** — tokens first, then prose — and fold in corrections.
9. **Write both files**, set `Status: Extracted` when `path-finder` called this mode (the member reviews it in a normal run and it becomes `Done`), then give the advisories.

## Styling architectures

Often several layer together:

- **Tailwind** — `tailwind.config.*` → `theme` and `theme.extend`; then grep arbitrary values (`bg-[#…]`, `p-[13px]`, `rounded-[14px]`) — the off-system escapes. Tailwind v4 keeps the theme in CSS (`@theme`).
- **CSS custom properties** — `:root { --… }` plus `[data-theme]` / `.dark` overrides; then grep raw hex and px used instead of the variables.
- **CSS-in-JS** — theme objects, `styled.*` templates, inline `style={{ }}`.
- **Token files** — `tokens.json` (Style Dictionary / W3C DTCG), `theme.ts`, `colors.ts`, `typography.ts`.
- **Component-library themes** — MUI `createTheme`, Chakra, Mantine, shadcn's `globals.css` variables.
- **Native** — SwiftUI `Color`/`Font` extensions and asset catalogs; Android `colors.xml`, `themes.xml`, Compose `Theme.kt`; Flutter `ThemeData`.
- **Raw and scattered** — SCSS variables, plain CSS, values hardcoded inline with no central source (the hardest case).

## Inconsistency patterns

| Pattern | Detect | Resolve |
|---|---|---|
| **Near-duplicate colours** | Cluster by role and closeness (within ~ΔE 5, or rounding to the same name) | Most-used wins; ties go to the value in the central token source |
| **Token defined but bypassed** | For each token, grep its literal value outside the token | The token wins by definition; inline literals are drift |
| **Off-grid spacing** | Infer the base (4 or 8) from the modal values; flag non-multiples | Snap to the nearest step unless the member says it's an optical nudge |
| **Several radii per component type** | Group radii by the component they're on | One radius per component class, mapped to the nearest `rounded` step |
| **Mixed units** | Per property, list units in use | Document the dominant unit; the code may compute in others if the value matches |
| **Font sprawl** | Distinct families, weights and sizes with counts | Collapse to 6–10 levels; keep loaded, most-used families; extra families are advisories |
| **Competing elevation models** | Group treatments by level (resting card, floating menu) | One model per level, from what dominates |
| **Forked components** | Duplicate primitives by name and shape (`Button`, `LegacyButton`) | Document one canonical definition; note the fork |
| **Dead tokens** | Tokens with zero uses | Mention; leave out of the file unless the member keeps them for a known use |

A banned font in the code (Inter, Instrument Serif, Outfit, Plus Jakarta Sans) is a conflict: recommend the closest free substitute from [../../brand-identity/references/image-analysis-patterns.md](../../brand-identity/references/image-analysis-patterns.md) → Fonts and document the family the member picks. The old family left in the code becomes drift.

## Resolution heuristics

In order — but always as a recommendation, never resolved silently:

1. **Frequency** — production usage is the strongest evidence of intent.
2. **Source authority** — a value in the central token source beats scattered literals, even more numerous ones.
3. **Location weight** — shared component and design-system folders beat one-off pages and marketing routes.
4. **Brand tiebreaker** — only when code evidence is genuinely tied: `docs/3-BRAND.md`'s direction, if it exists. Never to override clear evidence.
5. **Accessibility tiebreaker** — among equals, prefer the one meeting WCAG AA.
6. **Recency** — newer code may show the current direction; git history as a last resort.

## Advisories

Given to the member after the files are written, never applied silently:

- **Contrast** — every documented component pair failing WCAG AA (4.5:1 body, 3:1 large), with its ratio and a proposed fix; the member decides whether the token changes.
- **Paid fonts** — a documented family that isn't free for commercial use; keep the real font in the file unless the member asks to switch.
- **Residual sprawl** — anything collapsed hard (24 sizes → 8 levels), so the member knows what got rounded.
- **Brand gap** — when `docs/3-BRAND.md` exists and the code's system contradicts its direction, say where; changing the code to match is a build-plan phase, not something this mode does.
