"""
Support Deflection MVP - Flask chatbot with connectors and fallback ticketing.

Behavior:
- Intent detection: order-status or returns/refunds (simple keyword-based)
- Confidence scoring: 0..1; configurable threshold via CONFIDENCE_THRESHOLD
- Uses connectors/orders_connector.get_order(order_id) to fetch normalized order dict.
- Falls back to connectors/ticketing.create_ticket when confidence < threshold or order not found.
- If no ORDERS_API_BASE_URL is provided, connectors use demo mock data so the app is runnable for demo.
"""
import os
import re
import logging
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

from connectors import orders_connector, ticketing

# Config
CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.6"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
TICKET_ON_FALLBACK = os.getenv("TICKET_ON_FALLBACK", "true").lower() in ("1", "true", "yes")

# Logging
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("support-deflection")

app = Flask(__name__)

# Simple demo fallback dataset (only used when ORDERS_API_BASE_URL not configured)
# orders_connector will use its own mock if needed; kept here for compatibility if needed.
DEMO_ORDERS = {
    "1001": {
        "order_id": "1001",
        "status": "shipped",
        "shipped_at": "2026-08-10T09:12:00Z",
        "carrier": "FastShip",
        "tracking": "FS123456789",
        "items": [{"sku": "TS-RED-M", "name": "T-Shirt Red M", "returnable_until": "2026-09-09"}],
        "total": 29.99
    },
    "1002": {
        "order_id": "1002",
        "status": "processing",
        "estimated_ship_date": "2026-08-15",
        "items": [{"sku": "SH-BLK-9", "name": "Sneakers Black 9", "returnable_until": "2026-09-14"}],
        "total": 79.99
    },
    "1003": {
        "order_id": "1003",
        "order_id": "1003",
        "status": "delivered",
        "delivered_at": "2026-08-05T16:30:00Z",
        "items": [{"sku": "JKT-GRY-L", "name": "Jacket Gray L", "returnable_until": "2026-09-04"}],
        "total": 129.99
    }
}

# Helper: find order id like #1001 or 1001
def find_order_id(text):
    m = re.search(r"#?(\d{3,8})", text)
    return m.group(1) if m else None

# Intent detection (very simple)
def detect_intent(message):
    msg = message.lower()
    if any(kw in msg for kw in ("where is my order", "where", "has this shipped", "status", "tracking")):
        return "order_status"
    if any(kw in msg for kw in ("return", "refund", "how do i return", "when will i get my refund")):
        return "returns"
    # fallback: keywords
    if "order" in msg and "where" in msg:
        return "order_status"
    if "return" in msg or "refund" in msg:
        return "returns"
    return "unknown"

# Simple confidence scoring:
# - base score for keyword match: 0.6
# - +0.25 if order id present
# - +0.15 if explicit phrase matched (e.g., "where is my order")
def compute_confidence(message, intent):
    base = 0.0
    msg = message.lower()
    if intent == "order_status":
        if any(kw in msg for kw in ("where is my order", "has this shipped", "tracking", "where")):
            base = 0.6
        elif "status" in msg:
            base = 0.55
    elif intent == "returns":
        if any(kw in msg for kw in ("how do i return", "refund", "return", "when will i get my refund")):
            base = 0.6
        else:
            base = 0.5
    else:
        base = 0.2

    order_id = find_order_id(msg)
    if order_id:
        base += 0.25
    # clamp
    return min(1.0, base)

def format_order_status_reply(order):
    if not order:
        return "I couldn't find that order. Please confirm the order number or contact support."
    status = order.get("status")
    if status == "shipped":
        return f"Order {order['order_id']} shipped via {order.get('carrier','Unknown')}. Tracking: {order.get('tracking','N/A')}."
    if status == "processing":
        return f"Order {order['order_id']} is processing. Estimated ship date: {order.get('estimated_ship_date','N/A')}."
    if status == "delivered":
        return f"Order {order['order_id']} was delivered on {order.get('delivered_at','N/A')}."
    return f"Order {order['order_id']} status: {status}"

def format_returns_reply(order):
    if not order:
        return "I couldn't find that order. Please confirm the order number or contact support."
    items = order.get("items", [])
    any_returnable = False
    item_lines = []
    for it in items:
        try:
            ret_by = it.get("returnable_until")
            returnable = ret_by is not None and ret_by >= datetime.utcnow().strftime("%Y-%m-%d")
        except Exception:
            returnable = False
        item_lines.append(f"- {it.get('name')} (SKU {it.get('sku')}): {'returnable' if returnable else 'not returnable'}")
        any_returnable = any_returnable or returnable
    if any_returnable:
        refund_eta = (datetime.utcnow() + timedelta(days=7)).strftime("%Y-%m-%d")
        steps = [
            "Log into your account → Orders → Select the order → Choose 'Return item'.",
            "Print the pre-paid label or bring to a drop-off point.",
            "Ship the item; once we receive it, refunds process in 5-10 business days."
        ]
        return f"Items:\n" + "\n".join(item_lines) + f"\n\nReturn steps:\n" + "\n".join(steps) + f"\nEstimated refund completion by ~{refund_eta}."
    else:
        return f"Items:\n" + "\n".join(item_lines) + "\n\nNo items are currently within the return window."

@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True)
    msg = (payload.get("message") or "").strip()
    if not msg:
        return jsonify({"error": "message required"}), 400

    intent = detect_intent(msg)
    confidence = compute_confidence(msg, intent)
    logger.info("Detected intent=%s confidence=%.2f message=%s", intent, confidence, msg)

    order_id = find_order_id(msg)

    # If not confident enough, create ticket (optional) and ask for clarification
    if confidence < CONFIDENCE_THRESHOLD:
        reply = "I didn't get enough information to help. Could you share your order number (e.g. #1001) or provide more detail?"
        # create ticket if configured and allowed
        if TICKET_ON_FALLBACK:
            ticket_payload = {
                "subject": f"Support deflection fallback: unclear intent",
                "body": msg,
                "intent": intent,
                "confidence": confidence,
                "order_id": order_id
            }
            try:
                ticket_resp = ticketing.create_ticket(ticket_payload)
                logger.info("Created fallback ticket: %s", ticket_resp)
            except Exception as e:
                logger.exception("Failed to create fallback ticket: %s", e)
        return jsonify({"reply": reply, "confidence": confidence})

    # For known intents, require order_id to proceed
    if intent in ("order_status", "returns") and not order_id:
        return jsonify({"reply": "Please provide your order number (e.g. #1001) so I can check it.", "confidence": confidence})

    # Try to fetch order
    order = None
    try:
        order = orders_connector.get_order(order_id)
    except Exception as e:
        logger.exception("Orders connector error: %s", e)
        order = None

    if not order:
        # create ticket if configured
        if TICKET_ON_FALLBACK:
            ticket_payload = {
                "subject": f"Support deflection fallback: order not found #{order_id}",
                "body": msg,
                "intent": intent,
                "confidence": confidence,
                "order_id": order_id
            }
            try:
                ticket_resp = ticketing.create_ticket(ticket_payload)
                logger.info("Created ticket for missing order: %s", ticket_resp)
            except Exception as e:
                logger.exception("Failed to create ticket for missing order: %s", e)
        return jsonify({"reply": f"I couldn't find order {order_id}. Please confirm the number or contact support.", "confidence": confidence})

    # Build response
    if intent == "order_status":
        reply = format_order_status_reply(order)
        return jsonify({"reply": reply, "confidence": confidence, "data": order})
    if intent == "returns":
        reply = format_returns_reply(order)
        return jsonify({"reply": reply, "confidence": confidence, "data": order})

    # fallback
    return jsonify({"reply": "I can help with order status and returns/refunds. Try: 'Where is my order #1001?' or 'How do I return order #1001?'.", "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=(os.getenv("FLASK_DEBUG", "false").lower() in ("1","true")))
