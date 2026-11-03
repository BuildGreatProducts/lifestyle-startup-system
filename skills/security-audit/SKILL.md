---
name: security-audit
description: >-
  Step 7. Audits the built product before it goes live — committed secrets, database access rules,
  unprotected routes, one customer reaching another's data, keys shipped to the browser, then
  agent-tool risks like prompt injection — verifies each finding to a concrete exploit, and writes
  docs/7-SECURITY-AUDIT.md: a verdict (Ready, Ready after fixes, Not ready) and a fix plan split
  into agent fixes and what only the member can do. Never fixes on its own. Use when the member
  says "is my app secure", "security check", or "am I safe to launch". Not for going live — use
  go-live.
---

# Security audit

The gate between building and going live. Apps built fast with coding agents fail in a short, predictable list of ways — a key committed to git, a table anyone can read, a route that never checks who's asking, user A editing user B's data by changing an ID. This step checks that list first and in depth, proves every finding with a concrete way in, and writes a verdict the member can act on and a fix plan the agent can work. `go-live` won't start while the verdict is **Not ready**.

It never fixes anything on its own. A wrong fix to sign-in can lock the member out of their own app. It reports; fixing is a separate step the member chooses, after reading the plan.

Take the voice of a senior application-security engineer auditing a small production app:

- **Exploitability, not best practice.** Every finding names who the attacker is, what they send and what they get. "Not best practice" doesn't ship.
- **The stack decides what applies.** "Password hashing: N/A, Clerk manages credentials" is a correct audit line, not a gap.
- **Quiet reports get read.** Drop anything below roughly 8/10 confidence; a noisy report teaches the member to ignore reports.
- **Plain words for the member.** "Anyone with the link can read every customer's orders", not "IDOR on `/api/orders/[id]`" — the technical form goes in the table.

## Inputs

- **The codebase** — the whole thing by default.
- `docs/6-BUILD-PLAN.md` — the stack, data model and access rules the build was meant to follow. Unticked phases mean the build isn't finished: say so, and offer to audit what exists now and re-run once the build is done. The verdict covers only what's built.
- `docs/2-OFFER.md` → `## Product` (`Shape: <slug>`). Shapes without custom code or stored customer data (a no-code `productized-service`, `digital-product` or `website`) need the audit only for the custom surface — scripts touching client files, a custom intake or portal, a buyer database. None at all: say so in one line, write a short `Ready` document saying why, and hand on.
- An existing `docs/7-SECURITY-AUDIT.md` means a re-run: re-check every open fix first, then audit what changed since its date.

## Workflow

### 1. Scope and stack

Ask one question: **the whole product, or just the changes since the last commit?** Default whole product. Then detect the stack from the code before judging anything — framework, database and its access model (row-level security, rules, or checks in server functions), auth provider, payments provider, hosting and build config.

**Done when:** you can name the stack, and which checklist categories it makes N/A and why.

### 2. Map the attack surface

Enumerate before judging; the map is the audit's evidence and goes in the document:

- Every route, endpoint or server function: whether auth runs before the handler, whether it takes a resource ID.
- Every table or collection and its access rule.
- Every environment variable and where it's read — especially behind public prefixes (`NEXT_PUBLIC_`, `VITE_`, `EXPO_PUBLIC_`, `REACT_APP_`) or bundled into a mobile app or extension.
- Every webhook receiver and whether it verifies signatures.
- Every user-input entry point and file-upload path.
- For products where a model calls tools: every tool with its permissions, every hook and bundled script, every manifest and config, every place fetched content enters a prompt, every place model output renders as links or images.

**Done when:** the map covers every route, table, variable and webhook in the repo.

### 3. Audit, worst risks first

Work [references/security-checklist.md](references/security-checklist.md) in tier order, one category at a time, never sampled. Classify each **Critical / High / Medium / Low / Pass / N/A**, with a reason for every N/A. Apply its key-identity rules before flagging any key.

For agent skills, agent plugins, MCP servers, chat assistants, and any app where a model calls tools, read [references/agent-tools-tier.md](references/agent-tools-tier.md) and audit that tier straight after Tier 1.

**Done when:** every category in every tier that applies is classified.

### 4. Prove every finding

Detection is generous; the report is not. Re-read each candidate in the code and write its exploit path — who, what they send, what they get. If you can't, drop it. Judge against this codebase's own patterns. Apply the checklist's never-report and always-report lists.

For the most likely real finding — one customer reaching another's data — trace it in code (the ownership check on reads and writes, by ID), and add the user A / user B test to the member's list so it's proved in the running app too.

**Done when:** every finding has a location, an exploit path and a severity, and nothing from the never-report list is left.

### 5. Set the verdict

- **Not ready** — any open Critical or High finding, or a leaked credential not yet rotated. `go-live` won't start.
- **Ready after fixes** — no Critical or High; Medium findings to fix before launch. `go-live` can start and carries them in its pre-flight.
- **Ready** — nothing above Low.

**Done when:** the verdict follows from the findings by these rules, in one honest line.

### 6. Write the document and walk the member through it

Get the date with `date +%Y-%m-%d`. Write `docs/7-SECURITY-AUDIT.md` (below). Then, in conversation: the verdict, the count by severity, and the **Do this right now** items if any — rotating a leaked key outranks every code fix, because the key is in git history whatever the code says now. Explain each "only you can do this" item in plain words, with where to click.

**Done when:** the member has read the verdict and the right-now items.

### 7. Offer the fixes, then re-check

Only after the member has read the plan, offer: "Want me to work through the agent fixes now, top to bottom?" On a yes, take each fix in order: make the change, run its **Verify** line, tick it. Run the tests the fix touched. Then re-check each finding against its exploit path, update the Findings table, and re-set the verdict. Commit with `Security fixes: <range>`.

Never tick an "only you can do this" item yourself — ask the member to do it, then check what you can from your side (the old key no longer works, the setting is visible in config) and tick it when they confirm.

**Done when:** every fix the member asked for is ticked with its Verify passing, and the verdict and `Updated:` date reflect the re-check.

## Write docs/7-SECURITY-AUDIT.md

Follow [references/security-audit-template.md](references/security-audit-template.md) exactly: header, Verdict, Do this right now (only when a credential leaked), Findings, What's already secure, Attack surface, Agent fixes, Only you can do this, Not covered.

Set `Status: Done` once the document passes the verify list, whatever the verdict — the verdict, not the status, gates `go-live`.

## Verify before delivering

- [ ] The verdict follows the rules in step 5 and reads as one line a non-technical founder can act on.
- [ ] Every category in every tier that applies is classified; every N/A says why.
- [ ] Every finding has a location, a named attacker capability and an exploit path; nothing from the never-report list made it in.
- [ ] The anon-key / service-key distinction was applied correctly.
- [ ] Agent fixes are severity-ordered checkboxes, one concern each, each with a Verify line an agent can check unattended.
- [ ] Only-you items are specific (where, what, in what order — rotation first) and include the user A / user B test.
- [ ] Nothing was fixed before the member asked.

## Next

**Not ready** → the fixes first: offer to work the agent fixes (step 7), then re-check. The member's own items are theirs.

**Ready** or **Ready after fixes** → **go live** — `go-live`. It reads this verdict before it starts.

Re-run this audit after any significant change to sign-in, payments or who can see what.
