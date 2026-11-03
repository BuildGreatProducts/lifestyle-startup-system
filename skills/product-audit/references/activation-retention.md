---
kind: curated
last-reviewed: 2026-10-01
---

# Activation and retention

The leaks between "a customer arrives" and "a customer stays": the path from signup (or install, or payment) to the magic moment, and the loop that brings them back. Conversion surfaces — signup forms, pricing, checkout — are in [audit-areas.md](audit-areas.md); this file starts where they end, so don't count a finding twice. **Figures last reviewed October 2026**; re-verify before quoting.

## Contents

- [Set the retention model first](#set-the-retention-model-first)
- [Map the as-built path and loop](#map-the-as-built-path-and-loop)
- [Activation areas](#activation-areas)
- [Retention areas](#retention-areas)
- [Severity calibration](#severity-calibration)
- [Shapes without screens](#shapes-without-screens)
- [Benchmarks](#benchmarks)

## Set the retention model first

How often *should* this product be used? It sets the bar, and judging a transactional product against daily benchmarks is the most common audit mistake.

| Model | Products | Needs | Judge against |
|---|---|---|---|
| **Daily / habit** | social, habit, health, daily productivity | an active trigger: push, streaks, digests | day 1 / 7 / 30 retention |
| **Weekly** | most B2B SaaS, creator tools | lifecycle email and a recurring reason to log in | weekly active use, feature adoption |
| **Occasional / transactional** | tax, travel, events, one-off utilities | return-to-purchase, not daily use | repeat rate and reactivation; no penalty for missing daily mechanics |
| **Renewal cycle** | productized services, annual plans | visible delivery and reporting | renewal rate |

State it back with the magic moment before scoring: "Weekly product; the magic moment is the first ranked list of late payers."

## Map the as-built path and loop

From the screenshots and the code, trace:

- **The activation path** — every screen, gate and required action from account created (or install, or payment) to the magic moment. Count them. This is the spine of the activation findings.
- **The return loop** — what, if anything, brings the customer back: emails, push, scheduled jobs, stored value. If nothing does, that is the headline finding.

## Activation areas

**A. Time to value**
- [ ] Actions from account created to the magic moment — flag more than 3–5, or any setup before the first win.
- [ ] The magic moment from `docs/5-FLOWS.md` actually built into the first-run path, not left for the customer to find.
- [ ] Setup tax: mandatory profile, workspace config or integration before anything useful.

**B. Walls before value**
- [ ] Account required before any demo, sample or try-it.
- [ ] Permission prompts (push, location, contacts, camera) on first launch before any value.
- [ ] A hard paywall before the magic moment, for a product meant to let people feel it first.
- [ ] An email-verification gate blocking first use.

**C. Empty states and first run**
- [ ] The first screen after signup: blank, or seeded with sample data, a template or the thing they just made?
- [ ] Every empty state names its reason and has one CTA toward the magic moment.
- [ ] Progressive disclosure: the first action guided, not the whole UI at once.

**D. Onboarding friction**
- [ ] More than 3–5 onboarding screens; forced tours with no skip; no progress shown.
- [ ] Onboarding ends **at** the magic moment, not at a dashboard short of it. Check against `docs/5-FLOWS.md`.

## Retention areas

**E. Re-engagement — the most common leak**
- [ ] Code: lifecycle email beyond transactional (welcome series, nudges for unfinished work, milestones, win-back).
- [ ] Push: wired up, asked for *after* first value, and actually sent — for daily and weekly products.
- [ ] Calibrate: occasional products lean on email and can skip push.

**F. Return loop and stored value**
- [ ] A recurring trigger (digest, reminder, scheduled job) for habit products.
- [ ] Stored value: history, data or setup that builds up and would be lost by leaving.
- [ ] Does the product look any different on day 30 than on day 1?
- [ ] What a returning customer sees first: their work, or a blank or marketing screen.

**G. Churn and win-back**
- [ ] The cancel flow: a pause, downgrade or save offer — or one click into the void, or impossible to find.
- [ ] Failed-payment recovery: smart retries and dunning emails, not just the payment provider's defaults.
- [ ] A reason captured on cancel; a win-back offer after.

**H. Instrumentation**
- [ ] The magic-moment event fires to analytics.
- [ ] The funnel (signup → activated → retained) and churn events (cancel, payment failed, reactivated) are tracked.
- [ ] Analytics that can cut cohorts, not just page views.

## Severity calibration

- **Critical** — a wall before any value; a dead-end blank first screen; no way back at all for a daily or weekly product; the magic moment untracked.
- **Major** — a 7-step forced onboarding; no welcome series; no dunning; the magic moment reachable but buried.
- **Minor** — no milestone emails; no exit survey; a weak empty-state CTA.
- **Polish** — a streak missing on a weekly product.

## Shapes without screens

Product audit is for products with screens. When a screenless shape ships some (a developer tool's dashboard, an MCP server's account page, a service's intake form or portal, a digital product's sales page), audit those screens with the areas above and read activation and retention this way:

| Shape | Activation | Retention | Where the evidence is |
|---|---|---|---|
| agent-plugin, agent-skill | installed, triggered, first promised output | invoked again in later sessions; still installed at 30 days | the skill and command files, README, any licence or opt-in telemetry |
| mcp-server | client connected; a tool call returned something useful | tool calls per account, week over week | server logs, auth |
| chat-assistant | a conversation that finished the job | returning conversations or workspace users | the platform's analytics |
| developer-tool | first successful call or command | calls per key, week over week | API logs |
| productized-service | first deliverable accepted | renewal or repeat order | delivery records, billing |
| digital-product | downloaded and used (template opened, module one done) | repeat purchase, low refund rate | checkout platform, delivery emails |

Telemetry that leaves a customer's machine must be opt-in, disclosed, and never include prompts, files or customer data — hidden or default-on telemetry is a Critical trust finding.

## Benchmarks

- Reaching the aha in the first session (or within 48 hours) is markedly more likely to lead to paid; ~3.4× is often quoted but no primary study was traced — directional only.
- 3-step tours complete at ~72%, 7-step at ~16% — Chameleon benchmark (other editions report ~66% for 3-step).
- Day-1 retention baseline ~26%, optimised 40%+ — no source recorded; verify.
- Most consumer apps lose the majority of users in week one; the curve should flatten to a stable core, not trend to zero. Healthy B2B SaaS annual logo retention is 90%+ — general industry pattern; find a category figure before quoting.
- Failed payments are often 20–40% of subscription churn, and the cheapest to recover — a commonly repeated range from billing vendors; PYMNTS has reported up to ~50%.
- A welcome series is the highest-leverage first lifecycle send — practitioner consensus, no single figure.
