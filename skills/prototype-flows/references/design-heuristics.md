---
kind: curated
last-reviewed: 2026-11-03
---

# Design heuristics (H1–H50)

The craft rules that separate "shipped" from "designed", drawn from Nielsen Norman Group, Laws of UX, Shneiderman, Refactoring UI, WCAG 2.2, Don Norman, Apple's HIG, Material 3 and established AI-product patterns. Owned by `prototype-flows`, which designs with them; `product-audit` critiques with them.

**Style-neutral throughout.** Every visual value — colour, type size, spacing, radius, elevation, motion duration — is a token from `docs/4-DESIGN.md`, named in the form `{colors.primary}`. When a screen needs a value the tokens don't have, it's a **new pattern**: note it (prototype-flows lists it under the flows doc's design-system gaps; product-audit reports it), never invent a hex or a pixel value inline.

**Cite by number** in notes and findings ("H22: the submit button should be disabled until the form is valid"). Heuristics marked **(code)** can't be judged from a screenshot alone — in an audit, check them in the code or mark them unchecked.

## Contents

- [Visual hierarchy and emphasis](#visual-hierarchy-and-emphasis) — H1–H6
- [Layout and alignment](#layout-and-alignment) — H7–H10
- [Typography craft](#typography-craft) — H11–H13
- [Colour and contrast](#colour-and-contrast) — H14–H16
- [Interaction and feedback](#interaction-and-feedback) — H17–H22
- [Forms](#forms) — H23–H27
- [States: empty, loading, error, success](#states-empty-loading-error-success) — H28–H32
- [Motion](#motion) — H33–H36
- [Accessibility (WCAG 2.2 AA)](#accessibility-wcag-22-aa) — H37–H42
- [Mobile and touch](#mobile-and-touch) — H43–H46
- [Cognitive load and navigation](#cognitive-load-and-navigation) — H47–H48
- [AI-product specifics](#ai-product-specifics) — H49–H50
- [Which heuristics dominate which screen](#which-heuristics-dominate-which-screen)

## Visual hierarchy and emphasis

**H1. One primary action per view (Von Restorff).** The primary CTA is the single visually distinct element — the most prominent colour token and the largest button size. Secondary actions use quieter tokens.

**H2. Hierarchy from size + weight + colour, not size alone (Refactoring UI).** De-emphasise secondary text with weight or a secondary text-colour token before shrinking it.

**H3. Proximity groups, white space separates (Gestalt).** Related fields sit on a small gap token; unrelated groups on a larger one.

**H4. Common region bounds groups (Gestalt).** When proximity isn't enough, bound with a card, divider or tinted surface from the elevation and surface tokens.

**H5. White space is a tool — default to too much (Refactoring UI).** Generous padding reads as confident; tightening is deliberate, never the default.

**H6. Snap to the spacing scale; nothing one pixel off.** Every margin, padding and gap is a token. Grid alignment is the difference between designed and drafted.

## Layout and alignment

**H7. Semantic structure before generic containers (WCAG 1.3.1). (code)** `main`, `nav`, `header`, `section`, `button`, `label`; ARIA roles only when no native element fits.

**H8. Reading line length 50–75 characters.** Cap prose containers around 65ch.

**H9. Reflow at 320 px (WCAG 1.4.10).** Every view works 320 px wide with no horizontal scroll.

**H10. Text spacing tolerance (WCAG 1.4.12). (code)** Layout survives user overrides of line-height ≥1.5×, letter-spacing ≥0.12em, word-spacing ≥0.16em.

## Typography craft

**H11. Only documented type levels.** Every size and weight is a typography token.

**H12. Tabular figures in data.** Numbers in tables, dashboards and ledgers align vertically.

**H13. Balanced headlines, no orphans.** Headlines wrap balanced; body paragraphs avoid one-word last lines.

## Colour and contrast

**H14. Body text contrast ≥4.5:1 (WCAG 1.4.3).** Large text (≥18.66 px bold or ≥24 px) needs ≥3:1. Check every text/background token pair, in light and dark.

**H15. UI component contrast ≥3:1 (WCAG 1.4.11).** Field borders, icon-only buttons, focus rings, chart strokes.

**H16. Colour is never the only signal.** Pair every colour-coded state with an icon, label or pattern.

## Interaction and feedback

**H17. Feedback within 100 ms (Doherty, Norman).** Every action shows a press state, optimistic update or skeleton at once.

**H18. Every interactive element has its states.** Default, hover or focus-visible, active, disabled — and loading where it's async. On a canvas, draw the ones that matter.

**H19. Affordances signal interactivity.** Buttons look pressable; links visibly differ from body text.

**H20. Discoverable over hidden.** Critical actions are visible by default, never behind hover, long-press or an undisclosed gesture.

**H21. Easy reversal (Shneiderman).** Undo on destructive actions, Cancel on every modal, Back without losing data, soft delete with restore.

**H22. Constraints prevent errors (Norman).** Disable invalid options, constrain inputs, gate submit on validity — rather than erroring after submit.

## Forms

**H23. Single column, labels on top.** Never placeholder-as-label.

**H24. The right mobile keyboard. (code)** Email, numeric, decimal, phone and URL input types.

**H25. Autocomplete. (code)** email, name, new-password, one-time-code, postal-code — respects password managers and saves ~30 seconds.

**H26. Validate on blur, clear on change.** Validating every keystroke punishes typos.

**H27. Smart defaults absorb complexity (Tesler).** Detect timezone, locale and currency; preselect the safe option; parse "tomorrow 3pm"; prefill from earlier answers.

## States: empty, loading, error, success

**H28. Four states for every data view.** Empty, loading, error, success — each designed with tokens, and the success state with as much care as the rest.

**H29. Skeletons over spinners for content (NN/g).** Placeholders shaped like the final layout, so nothing jumps.

**H30. Optimistic UI for low-risk actions.** Likes, toggles and follows update at once and roll back with a toast on failure.

**H31. Empty states are first impressions.** One line on what belongs here and one primary CTA — the copy patterns are in [ux-writing.md](ux-writing.md#empty-states).

**H32. Errors say what, why and how to fix,** with a retry or recovery path — anatomy in [ux-writing.md](ux-writing.md#errors).

## Motion

**H33. UI motion in the 150–400 ms band (NN/g, Material 3).** Micro 100–150 ms (hover, toggle); standard 200–300 ms (menu, modal); large 300–400 ms (page transition). Repeated UI never animates past 500 ms.

**H34. Easing matches direction.** Ease-out entering, ease-in exiting, ease-in-out moving between two on-screen states.

**H35. Animate transform and opacity only. (code)** Never width, height, top or left.

**H36. Honour reduced motion. (code)** Swap transforms for instant changes or short fades — never remove the feedback itself.

## Accessibility (WCAG 2.2 AA)

**H37. Everything works from the keyboard (2.1.1). (code)** Tab, Shift+Tab, Enter, Space, arrows; focus traps in modals work.

**H38. Visible focus rings (2.4.7).** ≥2 px at ≥3:1 contrast, from a focus token if there is one.

**H39. Targets ≥24×24 px (2.5.8);** on touch aim for 44×44 (Apple) or 48×48 (Material).

**H40. Labels tied to their inputs (3.3.2). (code)**

**H41. Focus not hidden (2.4.11).** Sticky headers and footers never cover the focused element.

**H42. Accessible sign-in (3.3.8).** No puzzles to log in; paste allowed in password fields; one-time codes autofill.

## Mobile and touch

**H43. Primary actions in the thumb zone.** Bottom half of the screen; never the top corners for frequent actions.

**H44. Respect safe areas.** Fixed bottom bars and full-bleed headers clear the notch and the home indicator.

**H45. No hover-only critical information.** Hover doesn't exist on touch.

**H46. Every drag has a tap alternative (2.5.7).**

## Cognitive load and navigation

**H47. Navigation within 5–9 items (Miller).** The rest goes in a menu, command palette or settings.

**H48. Recognition over recall (NN/g).** Show selected filters, the current page, breadcrumbs, recent items; never make people remember a value from an earlier screen.

## AI-product specifics

**H49. Stream, with Stop as a primary control.** Responses stream as they generate; a visible Stop at primary weight aborts the real request; tool calls, searching and thinking show as labelled steps.

**H50. AI output is an editable draft.** Edit, accept in part, regenerate or reject; sources cited inline and one click to open; each failure type (network, limit, content filter, model error) has its own recovery path.

## Which heuristics dominate which screen

| Screen | Lean on |
|---|---|
| Landing page, store listing | H1, H2, H5, H8, H13, H14, H43 |
| Signup, onboarding, checkout | H1, H22–H27, H31, H32, H39, H42 |
| Core loop, dashboard | H2–H6, H12, H17, H28–H30, H47, H48 |
| AI chat or generation | H17, H29, H49, H50, H32 |
| Settings, account | H3, H4, H21, H23, H47 |
| Paywall | H1, H2, H16, H21 (an obvious way out) |
