---
kind: curated
last-reviewed: 2026-11-03
---

# UX writing

The rules for every string inside the product — buttons, labels, empty states, errors, confirmations, toasts, notifications, permission asks — and, for screenless shapes, the text an agent or a client reads. The voice comes from `docs/3-BRAND.md` → tone of voice; this file is the fixed layer the voice lives inside. Drawn from Apple's HIG, Material, Shopify Polaris, the Microsoft and Mailchimp guides, GOV.UK content design and NN/g research.

A language model's default is marketing English — the most likely word, rarely the most specific one. Every rule here is a constraint that forces specificity back in.

## Contents

- [The order of priorities](#the-order-of-priorities)
- [Budgets per surface](#budgets-per-surface)
- [The mechanical layer](#the-mechanical-layer)
- [Buttons and the verb dictionary](#buttons-and-the-verb-dictionary)
- [Labels, links and forms](#labels-links-and-forms)
- [Empty states](#empty-states)
- [Loading](#loading)
- [Errors](#errors)
- [Confirmations](#confirmations)
- [Success, milestones, notifications, permissions](#success-milestones-notifications-permissions)
- [Screenless shapes: text a model or a client reads](#screenless-shapes-text-a-model-or-a-client-reads)
- [Named failures](#named-failures)
- [Worked examples](#worked-examples)

## The order of priorities

**Clear beats concise, concise beats consistent, consistent beats voice, voice beats wit** — spend the next level only once the one above is met. The reader is mid-task; the best interface copy is the copy nobody had to read twice.

- People read **20–28%** of the words on a screen (NN/g), scanning down the left edge — so the first two words of every string carry its meaning. "To remove a photo, drag it to the trash", not "Drag a photo to the trash to remove it".
- Comprehension fails past **25 words** a sentence (GOV.UK). Target **US grade 7** (Polaris) / **reading age 9** (GOV.UK) — even for experts, who are just as busy.
- Short common words: help not assist, buy not purchase, turn on not enable, about not approximately.
- If the copy has to explain how the interface works, fix the interface.

## Budgets per surface

| Surface | Budget | Shape |
|---|---|---|
| Button / CTA | 1–3 words, ≤25 characters | {Verb} {noun}, sentence case, no punctuation |
| Field label | 1–3 words | Bare noun, no colon; "(optional)" marks the exception |
| Heading | 3–8 words | Sentence case, front-loaded, no period |
| Empty state | ≤6-word title + 1–2 sentences + 1 CTA | Why it's empty + the next action |
| Error title | 3–4 words | The effect on the user |
| Error body | 1–2 sentences, ≤25 words each | What happened, why, the fix with real numbers |
| Confirmation | 1-line title + 1-line body + 2 buttons | "{Verb} {noun}?" + consequence + verb buttons |
| Toast | 2–5 words | Noun + past participle |
| Tooltip | ≤10 words | Extra info only, never a required instruction |
| Placeholder | 2–5 words | A format example only, never the label |
| Settings description | 1 sentence | What happens when it's **on** |
| Push notification | ~50-character title, ~120-character body | Key noun and verb first; survives truncation |

German and Finnish run **+100–200%** longer than English — a 30-character label breaks a translated layout.

## The mechanical layer

Fixed under any brand voice; the voice lives in word choice and rhythm inside it.

- Sentence case everywhere. No full stops on titles, labels or buttons.
- Active voice, present tense: "Changes apply when you save", not "The changes will be applied". The one exception is the terse result toast ("Message sent").
- Second person ("you"); first person ("my") only for ownership and consent, never mixed in one phrase. Landing-page CTAs are the place first person wins ("Start my trial").
- Numerals, not words: "3 messages".
- Positive framing: "Use only letters", not "Don't use numbers or symbols".
- One exclamation mark per flow at most, never in an error.
- **One name per thing, everywhere.** Keep a lexicon (Concept / We say / Never say) and write every string from it. "Remove photo" in the menu and "Delete photo?" in the dialog reads as two operations.

## Buttons and the verb dictionary

A button says what it does — people act on the label alone. {Verb} + {noun}: "Create invoice", "View shipping settings", "Activate Apple Pay". One-worders (Done, Cancel, Save, Close) only where the context supplies the noun.

> Bad: "Let's do it!" · Good: "Send" (Apple) · Bad: "Try Apple Pay" · Good: "Activate Apple Pay" (Polaris) · Bad: "Add a menu item" · Good: "Add menu item" (Polaris)

| Verb | Means | Not |
|---|---|---|
| Create / Add | make from scratch / bring something existing in | interchangeable |
| Save / Done | writes now / applied when the parent saves | |
| Edit / Manage | change contents / a hub of several actions | |
| Change / Switch | replace with something else / swap accounts, modes, places | |
| Select / Choose | from a closed list / an open, subjective decision | |
| View | a CTA that navigates ("see" is for prose) | |
| Export, Import / Download, Upload | format conversion / same-format copy | |
| OK / Accept / Cancel / Close | acknowledge info / legal terms only / the escape hatch / view-only surfaces | |
| Delete / Remove | destroys / takes out of a list, recoverable | |

Never Submit, Yes, No or a bare "Get started" on a consequential action.

## Labels, links and forms

- A visible label on every field, outside it. Placeholder text vanishes on focus and many screen readers skip it (NN/g).
- Bare nouns, no articles, no colons: "Share with", not "Share with:". "Buy new domain", not "Buy New Domain".
- Mark optional fields "(optional)" rather than starring required ones.
- Links say where they go and stand alone: never "click here" or a bare "Learn more". "Read the [guide to dropshipping]", not "Want to learn more? Click here."

## Empty states

"Empty" means three different things; match the copy to which one it is.

| State | Copy job | Example |
|---|---|---|
| **First run** (never used) | Educate and invite — the one place personality and full sentences earn space | "Add your first product and see how it looks in your store. [Add product]" (Polaris) |
| **User-cleared** (task done) | Acknowledge, briefly | "All caught up" |
| **No results** (search or filter) | Say so, offer the loosening move | "No products match 'winter'. Try a shorter search." |

Every empty state names its reason and carries exactly one CTA. "Your journey starts here!" with no action is a dead end wearing a smile. First-run copy on a no-results state ("Add your first product!" to someone with 400 filtered out) reads as broken. The more often a state recurs, the plainer it gets.

## Loading

Name the wait in the user's world, present progressive: "Preparing video…", not "Buffering…". Past ~10 seconds, state a duration or show progress: "This can take up to 5 minutes." Never explain the infrastructure. AI waits name the step: "Reading your 12 invoices…", "Drafting the summary…".

## Errors

Three parts, in order: **what happened, why (or which item), what to do next** — the fix as a specific imperative with real numbers, limits or the user's own data, and a one-click fix where possible.

> Bad: "That password is too short" · Good: "Choose a password with at least 8 characters" (Apple)
> Bad: "Invalid bank account. Your payout was not deposited. [Next]" · Good: "Couldn't deposit payout — the bank account on file was closed. Update your details and we'll retry automatically. [Update bank account]" (Polaris)
> Bad: "There are 2 errors on this page" · Good: "To save this product, make 2 changes: Enter title · Add weight" (Polaris)

- **No blame:** "Wrong password", never "You entered the wrong password" (GOV.UK).
- **Banned:** invalid, illegal, forbidden, fatal, bad request, oops, uh-oh, raw error codes.
- **The apology budget is one** — for a serious failure the product caused: "Sorry, there is a technical problem. Try again in a few minutes." No "sorry" in validation, no humour under stress.
- Keep everything the user typed through every validation round-trip.
- For AI products, separate the failures: network, usage limit, content filter, model error — each its own recovery path.

## Confirmations

Confirm only what's hard to undo; confirming everything trains people to click through the one that matters. Title = "{Verb} {noun}?", body = the consequence in one line, two buttons that echo the verb and read alone.

> Bad: "Are you sure you want to delete Dark Blue Tee? [Yes] [No]" · Good: "Delete Dark Blue Tee? — This can't be undone. [Cancel] [Delete]" (Polaris)

Standard pairs: deleting → [Cancel] [Delete]; discarding edits → [Keep editing] [Discard]; leaving with unsaved changes → [Stay] [Leave page]. Never "Cancel" as the escape from a dialog about cancelling something — "Cancel subscription? [Keep subscription] [Cancel subscription]".

## Success, milestones, notifications, permissions

- **Toasts are quiet:** "Product saved", not "You successfully added a product!" No "successfully", no exclamation mark.
- **Milestones credit the user**, once, briefly — first launch, first sale, the magic moment: "You launched your store. Nice work." Never "We did it!". Thank people only for something they did for you.
- **Notifications front-load** the noun and verb; meaning survives at 50/120 characters; urgency of delivery matches urgency of content. A marketing message dressed as an alert costs the permission for good.
- **Permission asks come at the moment the feature needs them,** benefit first, postponable: "To remind you at 7:00, allow notifications" — after the user sets a reminder time, never on first launch.

## Screenless shapes: text a model or a client reads

When the shape has no screens, these surfaces replace the screen list. A model reading the text wants precision over personality; the voice shows only where a person reads the output. The error anatomy (what, why, fix) still applies.

| Shape | Surfaces to write rules and good/bad pairs for |
|---|---|
| agent-skill, agent-plugin | skill and command names; descriptions (the text an agent matches to decide whether to load it: what it does, when to use it, when not to); argument hints; the shape of every output it writes; stop and error messages; the README voice |
| mcp-server | tool names (one verb-noun pattern, no synonyms across tools); tool and parameter descriptions with units, formats and an example (agents choose tools from these alone); result formats with a next-step hint; errors an agent can recover from |
| chat-assistant | greeting and conversation starters; clarifying questions; refusal and out-of-scope lines; "I'm not sure" lines; hand-off to a human; the voice rules written as instructions for the system prompt |
| developer-tool | error messages (code, plain cause, fix, docs link); CLI help (usage line, flags, one example per command); command and flag names; progress and log lines; quickstart voice |
| productized-service | client emails (welcome, kickoff, delivery, revision, renewal, payment reminder); intake form questions and help text; delivery notes; status updates |
| digital-product | buy button, what's included, licence line; purchase and download emails; the "start here" page inside the product |

> Bad (tool description): "Gets data." · Good: "Returns open invoices for one client, newest first. Use when the user asks what a client owes. Takes client_id (string, e.g. 'cl_8f2'). Not for paid invoices — use list_payments."

## Named failures

Name the pattern in review so everyone knows the fix.

- **Marketing bleed** — streamline, seamless, powerful, effortless, unlock, elevate, supercharge, empower, "insights" inside the product. Name the object and the action instead: "See which pages get the most visits."
- **Wall of words** — bodies over 2 sentences, restating the title, explaining the mechanism.
- **Apology loop** — oops, uh-oh, unfortunately, "don't worry".
- **Enthusiasm overdose** — "Awesome! You're all set!" for a routine save.
- **Vague error** — "Something went wrong" with no recovery. If the cause is unknown, still give the move: "Refresh the page to try again."
- **Developer leak** — authenticate, credentials, payload, sync conflict, "invalid input".
- **Are-you-sure dialog** with Yes/No.
- **Synonym shuffle** — "workspace" on one screen, "project" on the next.
- **Robot passive** — "Your file has been uploaded" → "File uploaded".
- **Empty empty state** — a bare "No items", or an inspirational line with no action.
- **Blame shift** — "You forgot to add a title" → "Enter title".
- **Permission ambush** — a wall of system dialogs on first launch.
- Also strip: hedges (you can, simply, just, feel free to), padding (in order to, at this time, please be aware that), directional references ("the button below"), and overpromises ("never worry again").

## Worked examples

**Destructive delete** (tone "plain-spoken, but not blunt"): menu "Delete client" → dialog "Delete Maria Chen and 34 invoices?" / "This deletes all invoices and payment history. It can't be undone." / [Cancel] [Delete client] → toast "Client deleted". The model's first draft — "Are you sure you want to permanently delete this client? All data will be lost forever! [Yes] [No]" — breaks four rules at once.

**First-run empty state + permission** (habit tracker, tone "warm, but not chirpy"): "Track your first habit" / "Pick one thing you want to do daily. Stride reminds you at the time you choose." / [Add habit]; then, only after a time is set: "To remind you at 7:00, allow notifications." The draft it replaced: "Welcome to Stride! Your journey to a better you starts here. Enable notifications to unlock the full experience!" — enthusiasm overdose, marketing bleed and a permission ambush, with no next action.
