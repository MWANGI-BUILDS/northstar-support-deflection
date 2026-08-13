# Northstar Support Deflection MVP

Contents:
- app.py — Flask rule-based chatbot
- connectors/ — connector templates for Orders and Ticketing
- config/.env.example — environment variables
- charter_board.md, go_live_note.md, audit_log_template.csv — deliverables
- scripts/ — helper scripts to create branch and per-task commits, and to generate the audit CSV

Important notes:
- No secrets are committed. Provide credentials via environment variables or GitHub Secrets.
- The connectors use demo mock data if ORDERS_API_BASE_URL is not set so you can demo locally without credentials.

Quick start (local demo)
1. Install
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Optional: copy config/.env.example to .env and adjust values.

3. Run the app
   python app.py

4. Demo via curl

Order status (shipped):
curl -s -X POST http://localhost:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Where is my order #1001?"}' | jq

Expected sample reply (demo mock):
{
  "reply": "Order 1001 shipped via FastShip. Tracking: FS123456789.",
  "confidence": 0.85,
  "data": {
    "order_id": "1001",
    "status": "shipped",
    "tracking": "FS123456789",
    "carrier": "FastShip",
    "items": [
      {"sku": "TS-RED-M", "name": "T-Shirt Red M", "returnable_until": "2026-09-09"}
    ]
  }
}

Order status (processing):
curl -s -X POST http://localhost:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Has order #1002 shipped yet?"}' | jq

Expected sample reply (demo mock):
{
  "reply": "Order 1002 is processing. Estimated ship date: 2026-08-15.",
  "confidence": 0.8,
  "data": { "order_id": "1002", "status": "processing" }
}

Returns/refunds:
curl -s -X POST http://localhost:5000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"How do I return order #1001?"}' | jq

Expected sample reply (demo mock):
{
  "reply": "Items:\n- T-Shirt Red M (SKU TS-RED-M): returnable\n\nReturn steps:\nLog into your account → Orders → Select the order → Choose 'Return item'.\nPrint the pre-paid label or bring to a drop-off point.\nShip the item; once we receive it, refunds process in 5-10 business days.\nEstimated refund completion by ~2026-08-20.",
  "confidence": 0.85,
  "data": { "order_id": "1001", "items": [ {"sku":"TS-RED-M"} ] }
}

Preparing the Git history & push (one commit per Charter task)
- This repo includes scripts/push_commits.sh which will:
  - create and checkout branch feature/support-deflection-mvp
  - make one commit per Charter task (T1..T10) with required commit messages
  - push the branch to origin

Usage:
1. Create an empty repo on GitHub at MWANGI-BUILDS/northstar-support-deflection (or ensure the remote origin is set locally).
2. Clone it locally:
   git clone git@github.com:MWANGI-BUILDS/northstar-support-deflection.git
   cd northstar-support-deflection
3. Copy these files into the repo (or extract this package here).
4. Make scripts executable:
   chmod +x scripts/*.sh
5. Run:
   ./scripts/push_commits.sh

After push:
- Run ./scripts/generate_audit_log.sh to create audit_log.csv with actual commit SHAs and timestamps.
- Deliver audit_log.csv to procurement along with the branch.

Security:
- Do not commit real credentials. Use GitHub Secrets or environment variables on your runner.

If you want, I can:
- Walk you through running the push script, or
- After you push, fetch the branch and verify the commit history and produce the final audit CSV for you.
