# Authoring guide

How every skill and reference in the Lifestyle Startup System is written. For maintainers and for agents editing the system — not for members. `PLAN.md` holds the design decisions behind it.

## The system in one paragraph

Nine steps, one skill each, numbered in order. Each step writes one document to the member's `docs/` folder, named for its step: `1-IDEA.md`, `2-OFFER.md`, `3-BRAND.md`, `4-DESIGN.md` (+ `4-DESIGN.html`), `5-FLOWS.md`, `6-BUILD-PLAN.md`, `7-SECURITY-AUDIT.md`, `8-GO-LIVE.md`, `9-GO-TO-MARKET.md`. Three skills sit outside the sequence: `start` (install and route), `path-finder` (existing products → `0-PATH.md`) and `product-audit` (teardown → `docs/audit/`). There are no phase folders, checklists, worksheets or routing files: **the skill is the step**.

| # | Skill | Writes | Reads first |
|---|---|---|---|
| 1 | `idea-finder` | `docs/1-IDEA.md` | — |
| 2 | `product-offer` | `docs/2-OFFER.md` | `1-IDEA.md` if present |
| 3 | `brand-identity` | `docs/3-BRAND.md`, `docs/brand/references/`, canvas | `2-OFFER.md` |
| 4 | `design-system` | `docs/4-DESIGN.md`, `docs/4-DESIGN.html` | `3-BRAND.md` + its canvas |
| 5 | `prototype-flows` | `docs/5-FLOWS.md`, canvas | `2-OFFER.md`, `3-BRAND.md`, `4-DESIGN.md` |
| 6 | `build-plan` | `docs/6-BUILD-PLAN.md` | `2`–`5`, and the codebase if one exists |
| 7 | `security-audit` | `docs/7-SECURITY-AUDIT.md` | the codebase, `6-BUILD-PLAN.md` |
| 8 | `go-live` | `docs/8-GO-LIVE.md` | `7-SECURITY-AUDIT.md`, the codebase |
| 9 | `go-to-market` | `docs/9-GO-TO-MARKET.md` | `2-OFFER.md`, `8-GO-LIVE.md` |
| – | `start` | root `CLAUDE.md` / `AGENTS.md` block | everything in `docs/` |
| – | `path-finder` | `docs/0-PATH.md` (+ extracted drafts) | the existing product |
| – | `product-audit` | `docs/audit/` + a canvas per flow | the running product, `2`–`5` |

## SKILL.md

**Frontmatter.** `name` matches the folder (lowercase, hyphens). `description` is under 700 characters, written as: what it does and what it writes · `Use when` + two or three phrases a member would actually say · `Not for` + the neighbouring skill to use instead. Descriptions load into every session, so every word earns its place.

**Length.** Aim for 120–200 lines; 500 is the hard limit (`scripts/lint-skills.py`). Push detail into references.

**Shape.** Use these sections, in this order:

1. `# <Step name>` and a short paragraph: what this step produces and why it matters for the member's product. Then the voice, in 3–5 bullets, when the step needs a particular stance.
2. `## Inputs` — which `docs/` files it reads, and what to do when one is missing (run the step that writes it; never improvise its content).
3. `## Workflow` — numbered `###` steps. Each ends with a one-line **Done when:** the member or the agent can check.
4. `## Write docs/N-NAME.md` — the exact sections of the output document, in order.
5. `## Verify before delivering` — a short checkbox list.
6. `## Next` — the next step in plain words, and its skill name.

**Talking to the member.** Many members aren't technical. Plain English, one question at a time, a recommendation with every choice ("I'd go with B, because…"), and options shown side by side when they're visual. Do the mechanical work yourself and say what you did in one line. Never show a skill name, file path or command unless the member has to act on it.

**Research.** When a step needs facts that change (competitors, prices, communities, platform rules, tools), research them live and cite them in the member's document. If web search isn't available, say so, ask the member, and mark those claims unverified.

**Canvas.** Steps that design visually (`brand-identity`, `prototype-flows`, `product-audit`, and `design-system`'s catalogue) follow [skills/brand-identity/references/design-tools.md](skills/brand-identity/references/design-tools.md) to find and drive the canvas tool: `/design` first (in the Claude Code desktop app it opens a Claude Design canvas in the app), then Figma, Paper, MagicPath, Pencil or Stitch through MCP, then an HTML canvas page as the fallback. Record every canvas link in the step's document.

**Product.** The product's shape (web app, mobile app, digital product, productized service, agent skill…) is chosen in step 2 and recorded in `docs/2-OFFER.md` → `## Product`. Skills that adapt to it read [skills/product-offer/references/shapes.md](skills/product-offer/references/shapes.md).

## Output documents

Every step document opens with:

```markdown
# <Step name>: <product name>

Status: Draft
Updated: 2026-11-03
```

- `docs/4-DESIGN.md` is the one exception to the opening: Google's DESIGN.md format puts the YAML token block first, so its header comes straight after that block. `scripts/status.py` skips a leading `---` block before looking for `Status:`.
- `Status` is `Draft` while the step is in progress, `Done` when the step's verify list passes, and `Extracted` for a draft `path-finder` pulled from an existing product (the step skill reviews it with the member and sets `Done`). `start` and `scripts/status.py` read only this line, so keep it exactly in this form.
- Write only your own document. Never edit another step's document except to read it — if it's wrong, say so and offer to re-run that step.
- Re-running a step on a `Done` document shows the member what would change and asks before overwriting.

## References

Each skill's references live in its own `references/` folder and are linked from the SKILL.md at the step that needs them, by relative path: `[references/offer-examples.md](references/offer-examples.md)`. A reference shared by several skills lives in its **owner** skill's folder and is linked from the others by relative path (`../brand-identity/references/design-tools.md`); never copy it.

Every reference opens with frontmatter:

```markdown
---
kind: curated
last-reviewed: 2026-11-03
---
```

| `kind` | Holds | The skill… |
|---|---|---|
| `curated` | Judgment the agent can't research: good/bad calibration, worked examples, failure patterns, rubrics, scorecards, document shapes | Follows it |
| `checklist` | What must be checked, where a missed check is the expensive failure | Works every item; confirms current specifics live |
| `research` | How to look up something that goes stale: what to search, which sources to trust, what to bring back, how to cite it | Runs it fresh every time; holds no frozen lists of tools, prices or competitors |

Rules:

1. **Trim what the model already knows; keep what changes its output.** Generic best-practice explanation goes. Examples, patterns, numbers with sources, and "why this one fails" notes stay.
2. A reference over 100 lines opens with a contents list.
3. A `checklist` or `research` reference more than 6 months past `last-reviewed` is flagged by the lint; the skill tells the member it is leaning on fresh research for that part.
4. No ProductOS names, paths (`productos/…`), phase names (Define, Design, Develop, Distribute) or old document names (`DEFINE.md`, `PRD.md`, `ROADMAP.md`) anywhere. Use the step names and document names above.

## Root guidelines

`start` wires `setup/CLAUDE.md` (and its twin `setup/AGENTS.md`, identical below the title line) into the member's project root, between `<!-- BEGIN LIFESTYLE STARTUP SYSTEM -->` and `<!-- END LIFESTYLE STARTUP SYSTEM -->`, appended — never overwriting an existing file. Those guidelines tell the coding agent that `docs/6-BUILD-PLAN.md` is the build plan, `docs/4-DESIGN.md` is the design law, `docs/5-FLOWS.md` holds the copy rules, and how to work the build phases.
