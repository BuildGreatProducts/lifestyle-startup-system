---
name: go-live
description: >-
  Step 8. Takes a built, audited product live for its shape — deploy and domain, store submission,
  marketplace or registry release, booking page or storefront — walking the member through one step
  at a time: explain it, do the agent's part, say exactly what to click, wait, check it worked.
  Ends with a smoke test as a real customer, and writes docs/8-GO-LIVE.md as checklist and record.
  Use when the member says "get this live", "deploy my app", or "publish it". Not for a security
  check — use security-audit; not for getting customers — use go-to-market.
---

# Go live

The step that turns "it works on my machine" into "a stranger can find it, pay, and get the result." What *live* means depends on the shape — a deployed URL, an approved store listing, a published plugin, a booking page taking payment — and that bar is the finish line. This skill checks the gate, runs a pre-flight review, works out everything between here and live, and then walks the member through it **one step at a time**, doing the agent's part and checking each step before the next.

Many members have never deployed anything. Take the voice of a patient senior engineer sitting beside a capable founder:

- **One step at a time.** Never hand over a wall of instructions. Explain, act, wait, check, move on.
- **Exact clicks.** "In Vercel, open your project → Settings → Environment Variables → Add", not "set your env vars".
- **Every term explained once** in a few words: *DNS (the address book that points your domain at your app)*, *webhook (one service telling another that something happened, like a payment)*.
- **Honest about cost, time and waiting** — store review takes days, DNS can take hours, payment providers verify identity.
- **One path, not a menu.** The build plan chose the stack; this follows it.

## Inputs

- `docs/7-SECURITY-AUDIT.md` — read **first**. Rules in step 1.
- `docs/6-BUILD-PLAN.md` — the stack, hosting, services, the **Only you can set** list and the **Launch requirements**. Unticked build phases: stop and finish the build first. An existing product whose `docs/0-PATH.md` ticks the build plan as Done has no plan: read the stack and hosting from the codebase instead.
- `docs/2-OFFER.md` → `## Product` (`Shape: <slug>`) and pricing; the shape's **Live means** and **Go live** notes in [../product-offer/references/shapes.md](../product-offer/references/shapes.md).
- `docs/5-FLOWS.md` — the front door (landing page, store listing copy) and the magic moment the smoke test must reach.
- **The codebase** — config, environment variables used versus documented, test keys, deploy and packaging files.
- An existing `docs/8-GO-LIVE.md` means the member is resuming: carry on from the first unticked step, re-checking the last ticked one still holds.

## Workflow

### 1. Check the security gate

Shapes that ship code customers run or reach need the audit; a no-code service, storefront or builder site needs it only where there's custom code or stored customer data.

- **No audit** (and the shape needs one) → stop; run `security-audit` first.
- **Not ready** → stop. List the open Critical and High findings and the unrotated keys in plain words, and offer to work the audit's fixes. Go-live does not start.
- **Ready after fixes** → start, and carry the open Medium items into pre-flight.
- **Ready** → start.
- If commits since the audit's `Updated:` date touched sign-in, payments or who-can-see-what, say so and recommend a re-check of that surface before launch.

**Done when:** the verdict is Ready or Ready after fixes, and any open items are listed for pre-flight.

### 2. Pre-flight review

Run [references/code-review-checklist.md](references/code-review-checklist.md) over the code that's about to ship: the repo's own checks, a production build, the release-blockers, and the audit's carried items. Fix must-fix items as agent steps, with the member's go-ahead, before anything is deployed.

**Done when:** the pre-flight verdict is **Ready to ship**.

### 3. Work out the path to live

Read the shape's section of [references/go-live-by-shape.md](references/go-live-by-shape.md) every run — it holds the checklist, the smoke test and dated platform facts. Then audit what stands between here and the bar: accounts and developer programmes, live keys and environment variables, production settings for each service (database, auth on the real domain, payments in live mode with webhooks on production, email sending domain), the go-live route for the shape, the domain, and launch gaps (error tracking, analytics, privacy and terms pages, backups, listing assets). Check current platform rules, fees and review times live, and cite them.

Confirm the picture with the member in one message: the shape and its Live-means bar, the steps ahead (count, and which ones are theirs), the monthly cost, the time, and any questions only they can answer (do they own a domain, is there a deadline).

**Done when:** the member has agreed the path.

### 4. Write docs/8-GO-LIVE.md

Write the whole checklist (below) before starting the first step, so the member can see the full road and resume any time.

**Done when:** every step has an owner, a time, and a "You'll know it worked when" line.

### 5. Walk through it, one step at a time

For each unticked step, in order:

1. **Explain** what it is and why, in two or three sentences.
2. **Do the agent's part** — config, code, commands, preparing the exact values.
3. **Tell the member exactly what to do** — where to go, what to click, what they'll be asked for, what it costs. Secrets go straight from the provider's dashboard into the host's settings; never ask for them in chat, and never write them into the repo or this document.
4. **Wait** for the member to say "done". Don't stack the next step on top.
5. **Check it worked** from your side wherever you can — the URL loads over HTTPS, the variable exists by name, the build is green, a test webhook arrives, the listing shows "Waiting for review". If you can't check, ask for what they see.
6. **Tick it and record** the result on the step's Record line (date, URL, ID, plan chosen — never a secret value). Commit any code or config change.

Then the next step. If something fails, fix it before moving on. If the member stops, the document shows exactly where they are. Where a review stands between submission and live, say how long it usually takes, and what to do if it comes back with fixes.

**Done when:** every step before the smoke test is ticked and recorded.

### 6. Smoke test as a real customer

Run the shape's smoke test from [references/go-live-by-shape.md](references/go-live-by-shape.md) against its Live-means bar: through the real front door, on the device the customer uses, on production — find it, sign up or install or book, reach the magic moment, pay for real, then refund. The member does what needs their hands; you check what you can (the payment reached the backend, the event reached analytics, the error tracker is quiet).

**Done when:** every line of the smoke test passes and the Live-means bar is met. Anything less isn't live: record what failed and fix it.

## Write docs/8-GO-LIVE.md

```markdown
# Go live: <product name>

Status: Draft
Updated: <YYYY-MM-DD>

## Live means
<The shape's bar, from shapes.md, in one or two sentences.>
Live at: <the link, listing or booking page a customer uses>

## Pre-flight
- Security audit: <verdict, date>. Carried items: <list or "none">.
- Code review: <Ready to ship, date>.

## Steps
### <Phase: Accounts | Keys and settings | Production services | Ship it | Domain | After launch>
- [ ] **<Step>** — <You | Agent | Together> · <time> · <cost if any>
  <What it is, in a sentence.>
  You'll know it worked when: <what the member or agent can see>.
  Record: <filled in when done — date, URL, ID; never a secret>

## Smoke test
- [ ] <Each line of the shape's smoke test, as a real customer>
Result: <date, pass/fail, what was seen>

## Record
| What | Where | Monthly cost |
<Every account, service, domain and listing created, so the member knows what they're paying for.>

## Open issues
<Anything deferred, with the reason.>
```

Set `Status: Done` only when the smoke test passes against the Live-means bar.

## Verify before delivering

- [ ] The security verdict was read first; go-live didn't start on Not ready, and carried items were cleared or deferred with a reason.
- [ ] The pre-flight verdict is Ready to ship.
- [ ] Every step has an owner, a time, a "You'll know it worked when" line and a filled Record line; each was checked before the next began.
- [ ] No secret value appears in chat, the repo, or this document.
- [ ] Platform facts (fees, review times, rules) were checked live and are dated.
- [ ] The smoke test passed as a real customer, on production, against the shape's Live-means bar — and the Record table lists every monthly cost.

## Next

**Get customers** — `go-to-market`. It opens with the live front door from this document. Recommend a teardown with `product-audit` once real people have used it for a couple of weeks.
