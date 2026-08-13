Manual smoke test matrix (run these locally)

1) Order status - shipped
Request:
POST /chat { "message":"Where is my order #1001?" }
Expected:
- reply mentions "shipped" and includes a tracking code when demo mock used.

2) Order status - processing
Request:
POST /chat { "message":"Has order #1002 shipped yet?" }
Expected:
- reply says "processing" and includes estimated ship date.

3) Returns - returnable item
Request:
POST /chat { "message":"How do I return order #1001?" }
Expected:
- reply lists return steps and shows refund ETA.

4) Missing order
Request:
POST /chat { "message":"Where is order #9999?" }
Expected:
- reply that order not found and (if TICKET_WEBHOOK_URL is set) a ticket is created by connector.

5) Low-confidence fallback
Request:
POST /chat { "message":"I need help" }
Expected:
- reply asks for more info; if TICKET_ON_FALLBACK true and webhook configured, a ticket gets created.

Record results and associated commits in the audit log.
