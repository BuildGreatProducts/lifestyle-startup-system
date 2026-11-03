---
kind: checklist
last-reviewed: 2026-11-03
---

# Capture

How to screenshot every screen and state in the screen map without touching the app's code or any real account. Tools and flags change — check the current Playwright, Xcode and emulator docs before relying on a command here.

## Contents

- [Ground rules](#ground-rules)
- [Run the app](#run-the-app)
- [Web: Playwright at phone and desktop sizes](#web-playwright-at-phone-and-desktop-sizes)
- [iOS and Expo: the simulator](#ios-and-expo-the-simulator)
- [Android](#android)
- [Reaching every state](#reaching-every-state)
- [Files](#files)
- [Check before critiquing](#check-before-critiquing)

## Ground rules

- [ ] **Never edit the app's code, config or dependencies.** Don't add Playwright to its `package.json`; run it from a scratch folder outside the project, or use a browser tool already connected to the session. If the app won't run without a change, stop and ask the member.
- [ ] **Test accounts and seed data only.** Use the project's seed, fixture or example-config files, or create a throwaway account on the local app. Never the member's real credentials, never a customer's account, never production services.
- [ ] **Payments in test mode only**, with the provider's published test cards. If checkout points at live keys, don't capture past the checkout screen — log it as Not captured and flag the live key to the member.
- [ ] Don't send real email, SMS or push. If the app would, note the screen and move on.
- [ ] Keep any secrets you read (local env files) out of the report and the screenshots.

## Run the app

- [ ] Read the README and the package scripts for the dev command; start it locally.
- [ ] Seed the database with the project's seed script if there is one, so populated states look like real use.
- [ ] Note the local URL and the commit you're capturing, for the report's Sources.

## Web: Playwright at phone and desktop sizes

- [ ] Capture at **390×844** (phone) and **1440×900** (desktop), unless the app is clearly phone-only or desktop-only. Full-page for screens that scroll; the viewport alone for the above-the-fold view of the front door.
- [ ] Sign in once and save the session state, so every capture after it starts signed in.
- [ ] Wait for the network to go idle and fonts to load before each shot; hide the dev overlay if the framework shows one.
- [ ] Capture the front door in both light and dark if there's a theme toggle.
- [ ] If Playwright isn't available and can't be installed outside the project, use a connected browser tool at the same two sizes, and say which in the report.

## iOS and Expo: the simulator

- [ ] Boot a current iPhone simulator; build and launch the app with the project's own scripts (an Expo dev build, or Xcode).
- [ ] Navigate by deep link where the app defines them (`xcrun simctl openurl booted <url>`), otherwise drive it with the simulator tools in the session.
- [ ] Capture with `xcrun simctl io booted screenshot <file>`.
- [ ] Set appearance (light and dark) and text size if the app supports them, for one sample screen each.
- [ ] Screens you can't drive to (system sheets, in-app purchase sheets, push) go on the Not captured list for the member to grab by hand.

## Android

- [ ] An emulator with the project's build; capture with `adb exec-out screencap -p > <file>`. Same rules for deep links and Not captured.

## Reaching every state

| State | How to get it without changing code |
|---|---|
| First run / empty | A brand-new test account |
| Populated | The seed script, or a few minutes of real use on a test account |
| Returning | The populated account, signed out and back in |
| Loading | Throttle the network in the browser tool, or intercept the request and delay it |
| Error | Intercept a request and return an error, go offline, or submit an invalid form |
| Free vs paid | A seeded paid test user, or a test-mode checkout |
| Paywall / limit hit | Use up a free allowance on a test account, or a seeded account at its limit |

A state you can't reach this way goes on the Not captured list with the reason.

## Files

- [ ] Save as `docs/audit/screens/<flow>/<NN>-<screen>-<state>-<phone|desktop>.png`, numbered in flow order.
- [ ] Compress each to **300 KB or less** (a PNG optimiser, or high-quality JPEG for long full-page shots) so canvases stay light.
- [ ] Capture the store listing too, for store-front shapes: the search-result row and the listing page.

## Check before critiquing

- [ ] Every screen and state in the screen map has a file, or a logged reason it doesn't.
- [ ] Open a sample from every flow: no blank page, error overlay, dev toolbar, half-loaded fonts or seed text like "test test".
- [ ] Phone captures are actually phone layouts, not a squeezed desktop.
