---
kind: curated
last-reviewed: 2026-11-03
---

# The four lenses

Every screen, every flow and then the whole product gets looked at through all four: **UX, Conversion, Retention, Product**. This file holds the questions each lens asks, what "good" looks like, the findings each lens most often produces, and the finding format and severity scale the report uses. The detailed checks live elsewhere — [audit-areas.md](audit-areas.md) for conversion surfaces and token adherence, [activation-retention.md](activation-retention.md) for the path to the magic moment and back, [../../prototype-flows/references/design-heuristics.md](../../prototype-flows/references/design-heuristics.md) for craft.

## Contents

- [Writing a finding](#writing-a-finding)
- [Severity and effort](#severity-and-effort)
- [UX](#ux)
- [Conversion](#conversion)
- [Retention](#retention)
- [Product](#product)
- [Checks against the member's own docs](#checks-against-the-members-own-docs)
- [Flow verdicts](#flow-verdicts)
- [Why findings fail](#why-findings-fail)

## Writing a finding

| Field | What goes in it |
|---|---|
| **Where** | flow › screen › element, plus the screenshot file |
| **Lens** | UX, Conversion, Retention or Product |
| **Problem** | what the customer experiences — not what the code does |
| **Recommendation** | the specific change, buildable as written |
| **Severity** | Critical / Major / Minor / Polish |
| **Effort** | S (under half a day) / M (1–2 days) / L (more) |

Rules:

- **Point at pixels.** Every finding cites something visible in a screenshot. A finding about something missing names where it should be ("no price anywhere on the pricing screen above the fold").
- **One problem per finding.** The same problem on six screens is one pattern finding listing all six locations.
- **Nothing generic.** "Improve the onboarding" or "add social proof" would fit any app — make it about this one or cut it.
- **Name what's working** in each flow, so the fixes don't break it.

> Good: "Onboarding › 03 Plan picker › plan cards — three plans shown before the customer has seen any output; the free option is grey 12px text under the cards. Move the plan picker after the first report is generated, and make 'Continue free' a secondary button. Conversion · Critical · S."
>
> Bad: "The onboarding could be smoother and the pricing page should be more compelling." — no screen, no element, no change, no severity.

## Severity and effort

- **Critical** — blocks the job or the revenue: a signup wall before any value, a paywall with no way to try, a dead-end empty first screen, checkout that errors, the magic moment unreachable in the first session.
- **Major** — a meaningful leak most customers hit: a forced 7-screen tour, a generic CTA on the main conversion screen, no reason to return, copy that contradicts the offer.
- **Minor** — friction some customers hit: a weak empty-state CTA, an unclear label, a missing loading state.
- **Polish** — craft: off-scale spacing, an inconsistent radius, a widow in a headline.

Rank the top 10 by impact on the job and the business **against** effort — a Critical S beats a Critical L, and a Major S often beats both.

## UX

**Asks:** can the customer tell where they are, what to do next, and what just happened?

- Hierarchy: one primary action per screen; secondary text quieter (H1, H2).
- Copy clarity: buttons say what they do; errors say what, why and the fix; no marketing bleed inside the product.
- Feedback and states: loading, empty, error and success each designed (H28–H32).
- Friction: taps, fields and decisions between the customer and their goal.
- Consistency: one name per thing; one look per component.
- Accessibility basics visible in a screenshot: contrast, tap-target size, text size (H14, H39).

**Typical findings:** placeholder-as-label forms; three equal-weight buttons; spinner with no words; "Something went wrong" with no way out; a modal with no close.

## Conversion

**Asks:** how fast does a new customer reach value, and what is asked of them before they get it?

- Time-to-value: screens and actions from first touch to the first real output.
- Wall placement: signup, email verification, permissions and paywall — before or after the customer feels anything?
- Paywall timing and framing: trial clear, annual and trial as default where the pricing intends it, a visible way to continue free if the plan allows.
- Plan clarity: what's in each plan, the one it steers buyers to, the price visible.
- CTA strength: one CTA, first person on the front door, benefit-led.
- Trust: real proof near the decision, the guarantee from the offer, privacy and terms linked.
- Form friction: fields beyond what the first output needs.

**Typical findings:** account required to see anything; pricing hidden behind "Contact us"; checkout opening in a new tab that loses the plan; a hero that promises something onboarding doesn't deliver.

## Retention

**Asks:** why would they come back tomorrow — or next week, or at renewal, for this product's natural rhythm?

- A trigger to return: email, push, digest, reminder, a scheduled job — set to the product's retention model, not to "daily" by default.
- Stored value: data, history or progress that builds up and would be lost by leaving.
- The core loop's payoff: does each use end with something worth having?
- What a returning customer sees first: their work, or a blank dashboard?
- Empty states that lead into the loop rather than dead-ending.
- The way out: cancel flow, pause or downgrade, failed-payment recovery.

**Typical findings:** nothing brings anyone back; the home screen is identical on day 30 and day 1; a returning customer lands on a marketing page; cancel is one click into the void, or impossible to find.

## Product

**Asks:** is this the right product for the job?

- Positioning visible inside the product — does it feel like the thing the front door sold?
- The magic moment reachable in the first session, and marked as the high point.
- Features earning their place, or diluting the core loop.
- Difference from the obvious alternative (a spreadsheet, a general chatbot, the incumbent) visible on screen.
- The business model fitting how it's actually used — a monthly plan on a once-a-year job, a free plan that already does everything.

**Typical findings:** three half-built features competing with the core loop; settings richer than the product; nothing on screen a general chatbot couldn't do.

## Checks against the member's own docs

Run these whenever the doc exists; a gap between the documented plan and what shipped is a Major finding by default — the thinking was done, the build drifted.

| Doc | Check |
|---|---|
| `docs/5-FLOWS.md` | Does the shipped onboarding reach the named magic moment, inside its time-to-aha target? Do the shipped flows match the canvas flows, screen for screen? Do buttons, errors and empty states follow its copy rules and lexicon? |
| `docs/4-DESIGN.md` | Do the screens use its colours, type levels, radii and spacing? Anything off-token is an inconsistency or a new pattern — see [audit-areas.md](audit-areas.md#l-design-system-adherence). |
| `docs/3-BRAND.md` | Does the copy sound like its tone of voice? Does any screen use a word on its "we don't say" list? Does the look match the chosen direction? |
| `docs/2-OFFER.md` | Does the front door promise the offer's outcome, show its price exactly, and carry its guarantee and real proof? |

## Flow verdicts

Close every flow with: **steps to value** (screens and actions to the payoff), **where people will drop** (the one or two screens), **what's working** (one or two lines), and **what to fix first** (up to three findings).

## Why findings fail

- **The redesign in disguise.** "Rebuild the dashboard" is a project, not a finding. Name the one problem and the smallest change that fixes it.
- **The taste note.** "I'd use a different font" with no customer cost. Cut it, or tie it to a heuristic or a token.
- **The code finding.** "The component re-renders" — the customer doesn't experience that. Leave it to the build plan unless it shows on screen.
- **Severity inflation.** Everything Critical means nothing is. Reserve Critical for the job or the revenue.
- **The wrong rhythm.** Faulting a tax tool for having no daily streak. Judge retention against the product's own retention model.
