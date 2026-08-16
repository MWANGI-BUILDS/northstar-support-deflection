# Prototype — Support Deflection MVP

**What it is:** a single-file, client-side decision-tree chatbot that deflects the three ticket types
Northstar's support team is drowning in. No backend, no build step, no dependencies — deliberately, so
Northstar's team can pick it up without the pod in the room (see the go-live note).

## Run it

```
open index.html
```
or just double-click `index.html`. It opens in any modern browser. No server, no install, no internet
connection required — all data is mocked and embedded in the file.

## Categories covered

| Category | Required? | Status |
|---|---|---|
| Order status | Yes (part of the 2-minimum) | ✅ Implemented |
| Returns & refunds | Yes (part of the 2-minimum) | ✅ Implemented |
| Stock availability | Stretch (3rd category) | ✅ Implemented |

This satisfies "reduce manual ticket handling for at least 2 of the 3 categories" with a 3rd shipped as a
bonus.

## Demo script (for the client walkthrough)

1. **Order status, happy path:** click "Where is order NR1042?" → shows shipped status, carrier, tracking
   number, ETA.
2. **Order status, delayed:** type `has NR1004 shipped yet` → shows a delayed order with the hub note and
   revised ETA — demonstrates it isn't just a happy-path demo.
3. **Returns, eligible:** click "How do I return order NR1005?" → shows eligibility, instructions, and
   refund timeline.
4. **Returns, ineligible order not yet delivered:** type `refund for NR1003` → explains it can't be
   returned yet because it hasn't shipped.
5. **Stock, in stock:** click "Is the Trail Runner back in stock in size 9?" → shows quantity available.
6. **Stock, out of stock:** type `do you have the trail runner in size 8` → shows out-of-stock + restock
   ETA.
7. **Escalation:** click "Talk to a human" → shows the human-handoff message (this is the seam where a
   real ticketing system would create a ticket).
8. **Fallback:** type something unrelated (`what's your return policy on pets`) → shows the fallback
   message instead of breaking or hallucinating an answer.

## How the routing works

`routeMessage()` in `index.html` keyword-matches free-text input against three signal sets (order/returns/
stock), extracts an order number with a regex (`NR\d{3,5}`) when present, and calls the matching module.
This is intentionally simple (no ML, no external API) so it's auditable and so Northstar's team can extend
it without needing an ML background — see the go-live note for what a v2 would add.

## Known limitations (see go-live note for the full list)

- Mock data only — 8 orders, 6 products. Not wired to Northstar's real order/inventory systems.
- Keyword-based routing, not a language model — ambiguous phrasing can mis-route (test set: ≥90% accuracy
  on a 10-question set, see `02-project-board/PROJECT_BOARD.md` task T11 and T12's test log).
- No persistence — refreshing the page clears the conversation.
- Single language (English) only.