---
name: ux-map
description: Build a verified UX map of a website's path from first visit to its goal — a purchase for commercial sites, or a completed task for free, public-information, government, nonprofit and data/dashboard sites (find a record, understand it, apply, donate, report) — with personas, journey stages, flowcharts, a journey map, prioritized findings, metrics, and a list of what is still unverified, by actually walking the site in the browser, then delivering it as a shareable doc. Use this whenever the user asks for a UX map, user journey, customer journey, conversion funnel, signup/checkout flow review, "how do users get from landing to buying", a funnel audit, a usability walk-through of a public tool or dashboard, or wants to know where visitors drop off or get stuck on a website, even if they don't say "UX map".
---

# UX map: first visit to goal

Produce a UX map that is grounded in what the site *actually* does, not in what such sites usually do. The value of this skill is the verification: every claim in the final map is tagged as **verified** (you saw it in the browser) or **assumed** (you could not reach it). A map built from assumptions looks just as confident as a verified one, and that is exactly what makes it dangerous — so the walk comes first and the writing comes second.

## Inputs

- A URL (required). If missing, ask for it.
- Whether a logged-in walk is wanted. Default: do the public walk, then offer the logged-in walk.
- Optional: the business's buyer context (who uses vs. who pays). If unknown, infer from the site and say so.

## Step 0 — Identify the goal before walking

A funnel needs an end point, and not every site sells something. Spend one look (homepage text + a visible-links read, Phase 1 steps 2–3) deciding which kind of site this is:

- **Commercial** (pricing, plans, checkout, "Buy", "Upgrade", "Start free trial"): the goal is purchase. Follow the method as written.
- **Non-commercial** (free public tool, government service, data dashboard or map, nonprofit, research portal, content site): there is no purchase, so the map traces a **task** instead. Infer the most likely primary task from the site's own copy, then confirm it with the user in one question before the full walk — the right end point changes every stage after it. Offer 2–3 options with your recommendation first, e.g.:
  - *Find and understand* — locate a record (a factory, a school, a clinic) and grasp what its data means. The usual goal for maps and dashboards.
  - *Act* — apply, register, report a problem, donate, contact an office, download data.
  - *Per-audience journeys* — separate paths for the public, journalists/researchers and officials. Broader, more of it inferred.
- **Mixed** (free tool with a paid tier, nonprofit with donations): map the main task, then the step toward the paid/donation action as the final stage.

How the method changes for non-commercial sites:

- **Personas** split by *who needs the information* vs. *who can act on it* (resident vs. regulator, patient vs. clinic, citizen vs. office), instead of user vs. payer. Note literacy, language and device: a public-interest site's most important audience is often on a phone, reading a local language.
- **Stages** run arrive → wait/load → orient → narrow/search → find → understand → learn more → act. The "understand" stage is where these sites usually break: numbers, codes and scores shown without a scale or plain-language meaning.
- **"Purchase" in diagrams** becomes the act the visitor can take (get directions, download, share, apply). If no action exists, that is itself a gap.
- **Phase 2** applies only if the site has a login (admin, contributor, or citizen account). Many don't; say so and skip it.
- **Metrics** track task completion (share who filter, open a record, open the explanation, take the act) instead of conversion to paid.
- **Findings priority**: anything that stops a visitor understanding or acting on the information outranks speed and cosmetics.

## Safety boundaries (these shape the whole method)

The map needs signup, onboarding and checkout screens, but you must not create accounts, type passwords, or pay on a live site. So:

- **Logged-out**: read pages and follow links/buttons freely. Stop at the signup form; record what it says and where its `next=`/redirect parameters point.
- **Logged-in**: ask the user to log in themselves in the built-in browser pane (they type credentials or use "Continue with Google"). Then walk read-only.
- **Read-only means**: don't create forms/projects/records, don't type into editors or checkout fields, don't click Submit/Publish/Pay. Opening a checkout page is fine; continuing to the payment processor is not.
- **Prove you changed nothing**: note a counter on the dashboard (forms, projects, items) before the walk and re-check it after. Report the result.
- If the user's logged-in session is in a browser you can't reach (e.g. Edge), say so and offer: log in in the built-in pane, use Claude in Chrome, or send screenshots.

## Phase 1 — Public walk (logged out)

Goal: know every door into the funnel and where each one leads.

1. Dismiss any cookie banner with the most privacy-preserving option ("Reject all" / "Necessary only").
2. `get_page_text` on the homepage. Note the value proposition, products/plans, prices, free tier limits, social proof (who the testimonials are from — users or buyers?), FAQ answers about billing.
3. List visible links with their full destination in one call, rather than clicking around. Include the host — signup and checkout often live on another domain (`app.`, `kf.`, regional hosts), and that is itself a finding. Wait ~1.5 s first: many sites add `next=`/redirect parameters to links with JavaScript after load, and reading too early produces a false "plan lost" finding.
   ```js
   await new Promise(r => setTimeout(r, 1500)); [...new Set([...(document.querySelector('main') || document.body).querySelectorAll('a')].filter(a => a.offsetParent && a.innerText.trim()).map(a => a.innerText.trim().slice(0,40) + ' => ' + a.host + a.pathname + a.search + a.hash))].join('\n')
   ```
   Run it on the header/nav separately if `main` misses the nav CTAs.
4. **Pricing pages hide card sets behind toggles** (monthly/annual, segment tabs like nonprofit/business). Click each toggle combination, then re-run the visible-links read above. Never map a CTA to a plan by reading surrounding HTML of hidden cards — labels get crossed.
5. Most CTAs are plain links — read their hrefs first. Only for real `<button>`s (e.g. "Choose plan") click via JS. A click that navigates kills the script — and so does a client-side redirect on the page you just opened — so defer the click and read `location.href` in a *second* call:
   ```js
   setTimeout(() => [...document.querySelectorAll('button,a')].find(b => b.innerText.trim() === 'Choose Starter').click(), 50); 'clicked'
   ```
   then `await new Promise(r => setTimeout(r, 2000)); location.href`.
6. For each distinct entry path, record: entry CTA → landing URL → signup copy → `next=` target (or hidden `input[name=next]`). Check whether the signup copy and plan summary change per path, and whether the plan, billing cycle and segment survive into the `next=` target (they often don't — a common finding).
7. Visit the key product/pricing subpages linked from the footer and nav. Look for free-tier limits stated only there, no-signup tools, comparison guides, payment methods mentioned only in FAQs, and how "Talk to Sales" is implemented (form, calendar, or just `mailto:`). Embedded forms (HubSpot etc.) sit in iframes that `get_page_text` can't see; read their fields with `[...document.querySelectorAll('iframe')].map(f => { try { return [...f.contentDocument.querySelectorAll('label,input,select')].map(e => e.innerText || e.name).join(', ') } catch { return 'cross-origin' } })`.
8. Try a deep checkout/plan link while logged out. Does the login redirect keep the plan? (Commercial sites only.)
9. **Use the core features, not just the links.** On tools, maps and dashboards the journey happens inside one page: apply a filter, open a record, open every dialog and help button, and read what the visitor actually learns. Custom dropdowns often don't respond to scripted clicks — use real clicks from a screenshot. Count results yourself (e.g. table rows) and check whether the page states the count. Note what stays in the URL after filtering (shareability).
10. **Repeat the key path at phone width** (`resize_window` preset `mobile`, reload). Layouts often hide features on phones or swap them for different behaviour — a row tap that opens directions instead of the map, a separate map page without a legend. Reset to `desktop` when done.
11. **Note load cost** when a page shows a spinner: `performance.getEntriesByType('navigation')` and the largest `resource` entries. Report what you measured and on what connection; real mobile networks will be slower — put that in "Not yet verified".
12. Read help/explanation content wherever it lives. If it's a PDF in an iframe and the pane renders it blank, check the file with a `HEAD` fetch before calling it broken.

## Phase 2 — Logged-in walk (with permission)

Ask first. Once the user says they're logged in:

1. Dashboard: onboarding checklist (list every step and which are done — does it ever lead to the paid product?), empty states, persistent upgrade CTAs, counters (note them for the before/after check).
2. The core product's first screen for a new user: blank canvas or guided start? Are starter prompts/templates shown where the user actually works?
3. Every checkout variant reachable from in-app CTAs: what's pre-selected, bundle/upsell offers, required fields, disabled states, order summary clarity, payment methods named (card only? invoice? bank transfer?).
4. Empty states for paid features (e.g. "No servers yet") — copy and pagination quirks.
5. Re-check the counter. Confirm nothing was created.

Use `get_page_text` / JS `innerText` as the primary reader. Screenshots of SPAs sometimes show loading skeletons even after content has loaded; trust the DOM text and only report a "slow loading" finding if the DOM is also empty.

## Phase 3 — Write the map

Deliver it as a shareable doc using the docs connector (load its skill/guide first and follow its rules: skeleton first, one section per call). If no docs tool is available, or the user asks for a file, write markdown to the path they give (default `ux-map-<site>.md` in the working directory) and say so.

**Tagging claims**: "Yes" = you saw it happen in the browser. "Stated" = the site says it (FAQ, pricing copy) but you didn't see it in action — e.g. "invoice available on annual plans". "No" = not reached. Stated claims are useful but go in "Not yet verified" if a finding depends on them.

Use this section order. Keep each section's first sentence as its point.

1. **Summary** — the one-sentence diagnosis, how the map was built (date, logged-out + logged-in, nothing created), what was not tested, and the top 3 fixes as a numbered list.
2. **Personas** — table: persona · role · wants · blocked by. Always separate the *user* from the *payer/approver* when they differ (B2B, research, NGOs, schools, agencies); that split is where many funnels leak.
3. **Funnel stages** — numbered list from aware → expand (usually 8–11), each with one concrete line about this site. Stages are about the user's progress, not the site's pages, so many entry paths don't mean more stages.
4. **Flow 1: public site to checkout** — diagram (see below). Non-commercial: the desktop task flow.
5. **Flow 2: dashboard to payment** — diagram, only if the logged-in walk happened; otherwise a pending note. Non-commercial without login: the phone task flow, when it differs from desktop (it usually does).
6. **Journey map** — table: stage · what the user meets · mood · friction · fix · checked (Yes/No). The "checked" column is the verified/assumed tag.
7. **Findings and fixes** — table sorted by priority: priority · finding · fix · effort (Low/Medium/High). Priority = impact on reaching purchase first, effort second. Dead ends (a path with no next step toward paying) and missing buyer routes outrank cosmetic issues.
8. **Metrics to track** — table: stage · one metric that shows the leak.
9. **Not yet verified** — a task list of exactly what wasn't tested and why (would consume a free quota, would start a payment, needed login).

### Diagrams

Each flow is a top-down flowchart: a title stating the finding (e.g. "Every path funnels into one generic signup page"), a one-line color key, neutral boxes for normal steps, amber for friction, dashed red for confirmed gaps, accent for the purchase. Each box = a bold name + one short line of evidence (a price, a limit, a copy quote). Tie gap boxes to the step they hang off with a dashed connector so nothing floats. Keep to ~10–12 boxes per diagram; when there are many entry paths, group similar ones into one box (e.g. "3 paid plans → plain /sign-up") rather than cram or drop them. If the renderer gives you a screenshot, look at it and fix overlaps.

In a markdown fallback, draw the flow as an ASCII flowchart in a code block and mark states with text tags instead of colours: `[FRICTION]`, `[GAP]`, `[PURCHASE]`.

### Writing rules

- Every number, price, limit and quote comes from the walk. If you didn't see it, it goes in "Not yet verified", not in a box.
- Quote the site's own copy when it's the problem (e.g. a signup heading that promises the wrong product for the path the visitor came from).
- Findings name the exact screen/URL so the team can find it.
- After the doc is done, reply in chat with one short line and the link — no recap.

## Reference

Read the example matching the site type to calibrate depth and tone, not to copy content:

- `references/example-saas.md` — commercial SaaS: public + logged-in walk to checkout.
- `references/example-public-map.md` — non-commercial public data map: find-and-understand task, desktop vs. phone flows.
