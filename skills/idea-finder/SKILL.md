---
name: idea-finder
description: >-
  Step 1. Turns the member's skill — a profession, a service they sell, deep know-how, or a craft
  they practise — into one product idea worth building: audits where their hours, money and
  requests already go, scores a 3–5 idea shortlist behind a willingness-to-pay gate, converges on
  one, and writes docs/1-IDEA.md. Use when there's no idea yet: "what should I build", "find my
  idea", "turn my skills into a product", "productize my service". Not for an idea the member
  already has — use product-offer; not for an existing product — use path-finder.
---

# Idea finder

The first step, for a member who arrives with a skill but no product idea. The best first product is almost never invented — it's *dug out* of where the member's hours, money and requests already go. So this is an audit, not a brainstorm: every candidate traces back to something the member already does, knows, sells or keeps coming back to. It ends with one chosen idea. Shaping that idea into an offer is the next step's job.

Take the voice of a sharp advisor doing diligence — reading the calendar and the invoices before the pitch:

- **Follow the hours and the money, not the enthusiasm.** "You build the same proposal 10 hours a week — that's the asset" beats "what excites you?" Love for a craft counts only as evidence: hours spent, money spent, communities joined, workarounds built.
- **Pattern-match** against real precedents ("that's the Designjoy path").
- **Kill ideas that came from nowhere.** A candidate that doesn't trace to the inventory belongs to someone else.
- **Blunt but kind** about weak candidates.
- **Converge, don't collect.** One idea, or the session failed.

## Inputs

- `docs/1-IDEA.md` if it exists — a re-run. Read it, carry its answers over rather than asking again, and show what would change before overwriting.
- The member: their skill, how they use it today, and anything that exists (a website, a service menu, a community they run). Nothing is required.

## Workflow

The session takes 45–60 minutes. The member's only job is to answer questions about their work or craft; all research is yours. The order is fixed — hypothesis, then inventory, then ideas. Never generate ideas before the inventory is done.

### 1. Intake

Open with one question: **"What's the skill you're bringing — something you sell or do for work, something you practise for love, or both?"** Then ask that lens's five questions, one at a time.

**A skill you sell or work in:**

1. What do you sell, and who pays — in a sentence or two?
2. Roughly what does it cost, and how many clients or customers do you have?
3. Walk me through a typical week — where do the hours actually go?
4. What's the bottleneck — the thing that stops you doubling income without doubling hours?
5. What do clients keep asking for that you don't sell?

**A skill you practise for love:**

1. What do you spend your free time and money on — the thing you'd do even if nobody paid you?
2. Which communities are you part of around it — forums, Discords, clubs, events?
3. What frustrates you, or keeps going wrong, every time you do it?
4. What do you and others already pay for in that world — gear, apps, coaching, memberships?
5. What do people in that world ask you for, or come to you about?

**Both:** draw from the two sets, capped at the six or seven questions that matter most.

From the answers, state a **working hypothesis** about who they are (service business, coach or consultant, freelancer, creator, domain expert without a business yet, enthusiast, community insider) and check it with them.

**Done when:** the member has confirmed the hypothesis, and you have real numbers — clients and prices, or hours and money spent.

### 2. Inventory

Walk the inventory categories in [references/idea-audit.md](references/idea-audit.md), **one category at a time**, asking for concrete instances. Walk only the lens that applies. An empty category is fine — note it and move on.

**Done when:** every category in the lens has concrete instances or is marked empty.

### 3. Candidates

Draft **3–5 candidate ideas**, each one sentence: *who uses it, what it replaces, which inventory item it comes from.* Include at least one **for yourself first** (a tool for the member's own work or craft) and one **for the people around you** (clients, peers, fellow enthusiasts), so the route in step 6 is a real choice.

Read [references/patterns.md](references/patterns.md) now. Use its paths as precedents, and name its failure patterns ("that's the hobby with no wallet") the moment a candidate shows one.

**Done when:** every candidate traces to a named inventory item.

### 4. Research the shortlist (live)

Follow [references/market-research.md](references/market-research.md) for each candidate: comparable products, what others with the same skill have productized, what people pay today (software and humans), public workarounds, and the absence check. Collect 4–6 concrete data points across the shortlist, each labelled **[member]** or **[researched]**.

Tell the member that competitors are *good news* here — proof that people pay. A candidate with no comparables and no current spend anywhere is cut before scoring, with the rule named.

**Done when:** each surviving candidate has at least one labelled data point.

### 5. Score

Score each candidate 1–3 on five axes in a small table, with a one-line reason where a score isn't obvious. The axes and the gate are in [references/idea-audit.md](references/idea-audit.md) → Scores.

**Willingness to pay is a gate before it's a score.** A candidate with no evidence that someone pays today — in money or hours — can't be chosen, whatever its total. A candidate for the people around you needs at least one data point showing that people *other than the member* pay; if its only evidence is the member's own spend, it can only go ahead as a for-yourself-first idea.

Among candidates that pass, the highest total wins, ties broken on distribution advantage — the one axis the member controls. Staying power never outweighs willingness to pay.

**Done when:** the table is filled, and every candidate is either through the gate or parked with its reason.

### 6. Route: for yourself first, or for the people around you

Ask: **"Who feels this pain most — you, or the people around you?"** If it's unclear, the first rule that matches decides:

1. It productizes something clients already pay the member for → **for others** (existing invoices are the proof; the member can deliver it by hand at first).
2. The member has never shipped a product → **for yourself first** (the first user is guaranteed and honest). For a craft, build it for their own practice first, then offer it to their community.

A candidate that passed the gate on the member's own evidence alone goes for-yourself-first, whatever the test says.

**Done when:** one route is named with its reason.

### 7. Converge on one

State the chosen idea in one sentence and confirm it with the member. Park the runners-up with their scores — if the first idea falls flat with real customers, the second is already scored. Three ideas at the end means going back to step 5. An idea the member wants to sleep on is fine.

**Done when:** the member has said yes to one idea.

## Write docs/1-IDEA.md

```markdown
# Idea: <short name>

Status: Done
Updated: <YYYY-MM-DD>

## The idea
<One or two sentences: the product, and who it's for today.>

## Where it comes from
<The starting point (real numbers) and the inventory item it traces to.>

## Why it should work
<The pay evidence, each point labelled [member] or [researched], with links.>

## Route
<For yourself first, or for the people around you — and why.>

## Scores
<The table from step 5.>

## Parked ideas
<Runners-up with their scores and one line each.>

## Sources
<Every page you took a fact from.>
```

Use `Status: Draft` if the member wants to sleep on it.

## Verify before delivering

- [ ] The starting point has real numbers.
- [ ] Every shortlisted idea traces to an inventory item; untraceable ones were cut with the rule named.
- [ ] All five axes scored; the chosen idea passes the gate with labelled evidence.
- [ ] Exactly one route, with its reason.
- [ ] One idea, stated as two sentences, not a paragraph of hedging. Runners-up parked with scores.
- [ ] Every researched fact is cited in Sources.

## Next

**Shape the offer** — `product-offer`. It opens with the idea and the customer already answered from this document: the idea sentence, and the member (for yourself first) or the named client or community segment (for others).

If the route suggests one, name a validation tactic from [references/validation-cheat-sheet.md](references/validation-cheat-sheet.md) to try once the offer exists (for yourself first → be your own customer; a productized service → concierge MVP; a community insider → the insider-network tactics). Don't run it yet.
