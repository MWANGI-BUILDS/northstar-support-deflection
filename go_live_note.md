Support Deflection MVP — Go-Live Readiness (1 page)

What works (demo-validated)
- Order Status intent: Given an order number (#1001) the bot returns shipped/processing/delivered states and tracking when shipped.
- Returns & Refunds intent: Given an order number, the bot reports item returnability, step-by-step return instructions, and an estimated refund ETA.
- Demoable end-to-end locally via POST /chat (see README).

Known / accepted limitations (what's broken)
- No authentication: Prototype uses demo mock data when ORDERS_API_BASE_URL is not set.
- No production Orders/Returns API integration by default — connectors are templates.
- No rate-limiting, session/context store, or advanced NLU.
- Minimal logging/observability in this MVP.
- No ticketing SLA or escalation rules configured.

Operational pickup checklist (what Northstar must do)
1. Integrate real Orders API:
   - Provide API base URL, API key, and response contract.
   - Replace demo fallback or set ORDERS_API_BASE_URL + ORDERS_API_KEY.
2. Authentication & account linking:
   - Implement SSO/OAuth or session token scheme to map user → orders.
3. Returns flow wiring:
   - Provide returns API or return-label generation endpoint.
4. Hosting & scaling:
   - Deploy behind API gateway, add rate limiting and TLS.
5. Monitoring & logging:
   - Integrate logs/metrics and implement deflection monitoring.
6. Ticketing integration:
   - Add webhook or direct integration to ticketing system for fallback tickets.
7. Playbook & staff training:
   - Provide 1-page playbook to Customer Support.

Minimum effort to go-live (estimate)
- Integration + Auth + logging + ticketing webhook: ~2–3 developer-weeks + 1 week testing & CS training.

Contact for handover
- Michael (PM/Lead): michael@example.com
