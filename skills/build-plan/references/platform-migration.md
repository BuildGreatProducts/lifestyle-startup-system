---
kind: checklist
last-reviewed: 2026-11-03
---

# Moving off a prompt-to-app platform

When the app lives on Lovable, Bolt, v0, Base44, Replit Agent or similar, the move into the member's own repo, stack and coding agent is **phase 0** of the build plan, in place of the usual "safe to change" phase. Work every item; confirm the platform specifics live.

## Contents

- [Two rules](#two-rules)
- [Inventory what the platform does](#inventory-what-the-platform-does)
- [Check the export mechanics live](#check-the-export-mechanics-live)
- [Phase 0: the move](#phase-0-the-move)
- [Platform notes](#platform-notes)

## Two rules

1. **Moving is not improving.** Phase 0 moves and rewires what exists; it doesn't restructure it. Cleanup of the generated code is later phases, planned in existing-code mode once the app runs from the repo. Keeping them apart keeps each one checkable.
2. **Clean break.** Once exported, the platform's editor is retired — exports are snapshots, and anything changed on the platform afterwards is silently lost. Tell the member before exporting.

## Inventory what the platform does

Check each item concretely with the member; "sort of" hides the thing that breaks in production. Record each as a row: *item · where it lives now · where it's going · action · how we check it*. That table becomes phase 0's boxes.

- [ ] **Code and export path** — GitHub sync (often a paid plan — check; it may be the one platform charge that can't be avoided) or a zip. Is the synced repo current?
- [ ] **Hosting and deploys** — the platform URL, build pipeline, preview environments.
- [ ] **Database** — platform-managed (e.g. Lovable Cloud) or a service the member owns (their own Supabase). This one answer sets how hard the move is.
- [ ] **Auth** — platform-managed users, or an external provider. OAuth apps configured platform-side (client IDs, secrets, redirect URLs).
- [ ] **Secrets and environment variables** — every one listed **by name**. Secrets never export; each is re-entered, and rotated where the platform held it.
- [ ] **Storage** — buckets, uploaded files, and anywhere the app stores signed URLs (they change after the move; stale ones break silently).
- [ ] **Server functions and scheduled jobs** — edge functions, crons, and the platform URLs they call.
- [ ] **Webhooks pointing in** — Stripe, OAuth callbacks, email providers targeting platform URLs. These break the moment the platform is paused, not when the code moves.
- [ ] **Domain and DNS** — where DNS points today. Cutover is the last step, never an early one.
- [ ] **Everything else** — email, analytics, error tracking, payments.

**Target:** keep what the member already owns (their Supabase, Stripe or Clerk move by re-pointing, not rebuilding); replace only what the platform owns, from [stack-options.md](stack-options.md). The common result: a GitHub repo as source of truth, Vercel for hosting, the member's own database project, and their coding agent.

## Check the export mechanics live

Export features change fast. Search the platform's current docs and changelog for: what the export includes (schema, data, access policies, auth users — and whether password hashes come along so logins survive), what it leaves out (usually secrets, OAuth configs, storage files), and known traps. Fold what you find into the boxes, cited. No web search → say so, ask the member what their export screen offers, and mark those boxes unverified.

## Phase 0: the move

Adapt to the inventory; cut what doesn't apply.

- [ ] **Export and baseline** — sync or export to GitHub; tag `pre-rebuild-<date>`; record a baseline of the working app (core flows walked, screenshots, user count, storage file count) for the gate to compare against.
- [ ] **Secrets** — `.env.example` with every variable by name; values entered at the destination; rotated where the platform held them; nothing committed.
- [ ] **Backend** *(only if the platform owns it)* — database dump and restore into the member's project; auth users restored (log in with a real pre-move password); storage files copied; functions redeployed from the repo; crons recreated, old platform URLs hunted out of the code; OAuth apps recreated.
- [ ] **Re-point the world** — every webhook and callback (payments first), API base URLs, regenerated signed URLs.
- [ ] **Deploy** — hosting project, variables set, build green, preview and production deploys working. DNS cutover prepared, **not run**.
- [ ] **Agent workflow** — root guidelines in place, platform-only files and shims removed, dependencies install cleanly from the lockfile.
- [ ] **You:** run the gate with the agent (below), then the DNS cutover.

Done when: every core flow passes against the baseline on the new deploy — a pre-move account logs in, a test-mode payment completes, uploads and old file links load, each scheduled job fires once — and DNS points at the new host. Anything red: stop, the platform stays untouched.

Add one box to the **last** phase: **You:** after a few quiet days on the new host, pause the platform project, then remove it. Never pause or delete it before the gate is green.

## Platform notes

Last reviewed October 2026 — starting points for the live check, not answers.

- **Lovable** — GitHub sync is a paid-plan feature (source not recorded; check the pricing page). Lovable Cloud is its managed backend (database, auth, storage, functions); an app on it is the harder class. Official backend Export / Pause / Remove controls shipped in mid-2026 (check the docs and changelog). The backend export is a `pg_dump` carrying schema, data, RLS policies, triggers, sequences and auth users with password hashes, so logins survive; it leaves out secrets, OAuth configs and storage files.
- **Bolt, v0, Base44, Replit Agent** — no notes yet; rely on the live check.
