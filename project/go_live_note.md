# Go-Live Readiness Note — Support Deflection MVP
*For: Northstar Retail Co. support team · From: the pod (Michael, Victor, Sandisiwe, Esther, Ann) · Day 5*

## What works

- Deflects all 3 of your top ticket types end-to-end in a single interface: *order status*, **returns &
  refunds*, and **stock availability* — the brief only required 2; we shipped the 3rd as a bonus.
- Natural-language input is routed automatically to the right module (keyword + order-number matching),
  tested at ≥90% accuracy on a 10-question set (see 04-audit-log T12 test log).
- Every dead end has a human-handoff message instead of a broken or blank reply — customers are never
  stuck talking to a wall.
- Zero infrastructure: it's a single HTML file. No server, no hosting cost, no install. Your team can open
  it, read it, and edit it without any of us in the room.

## What's known-broken / not yet real

- *Mock data only.* Order and stock data is hardcoded in the file (ORDERS and STOCK objects in
  index.html) — it is not connected to your real order management or inventory systems. This is the #1
  thing to fix before real customers touch it.
- *Keyword-based routing, not AI.* It will mis-route genuinely ambiguous phrasing it wasn't tested
  against. It does not learn from mistakes on its own.
- *No conversation memory across sessions* — refreshing the page loses the thread. No login, no per-
  customer history.
- *English only*, and return-window logic assumes a flat 30-day policy — if your real policy varies by
  category, that's a single constant to change (RETURN_WINDOW_DAYS), not a redesign.
- *No ticket creation on handoff.* The "talk to a human" path currently just says so — it doesn't yet
  file a ticket in your real system.

## What your team needs to pick this up without us

1. *Swap mock data for real data.* Replace the ORDERS and STOCK JavaScript objects in index.html
   with calls to your order-management and inventory APIs. Everything downstream (the eligibility logic,
   the messages) already expects the same field shapes — see the module comments in the file.
2. *Wire the handoff.* Replace the placeholder message in the human/agent branch of routeMessage()
   with your real ticketing system's create-ticket call.
3. *Expand the test set.* 03-prototype/README.md has the demo script we used; before wider rollout,
   run a larger set of real historical ticket phrasings through it and tune the keyword lists in
   routeMessage() for anything that mis-routes.
4. *Decide on hosting.* As a static file it can be dropped onto any web host, embedded in an existing
   help-center page, or wrapped into your app — no framework lock-in.
5. *Owner on your side:* whoever owns your help-center/FAQ content is best placed to maintain the
   fallback copy and expand categories over time; whoever owns integrations should own the data wiring in
   step 1.

One page, as required — full technical detail lives in 03-prototype/README.md and the code comments.