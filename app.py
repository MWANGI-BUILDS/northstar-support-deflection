#!/usr/bin/env python3
"""
Northstar Support Deflection MVP — Flask backend
Provides API endpoints for a rule-based support chatbot
"""

import os
import json
import re
from flask import Flask, request, jsonify
from typing import Dict, Tuple, Optional

app = Flask(__name__)

# ===== Mock data (stand-ins for Northstar's real systems) =====
ORDERS = {
    "NS-10234": {"item": "Trailhead Jacket", "status": "shipped", "carrier": "UPS", "eta": "Aug 13", "tracking": "1Z999AA10123456784", "placed": "Aug 8"},
    "NS-10250": {"item": "Aurora Sneaker", "status": "processing", "carrier": None, "eta": "Aug 15 (pending fulfillment)", "tracking": None, "placed": "Aug 10"},
    "NS-10199": {"item": "Summit Backpack", "status": "delayed", "carrier": "FedEx", "eta": "Aug 16 (was Aug 12)", "tracking": "7712994410", "placed": "Aug 5"},
    "NS-10088": {"item": "Ridge Fleece Pullover", "status": "delivered", "carrier": "UPS", "eta": "Delivered Aug 9", "tracking": "1Z999AA10998877665", "placed": "Aug 2"},
    "NS-10301": {"item": "Alpine Trekking Poles", "status": "shipped", "carrier": "USPS", "eta": "Aug 14", "tracking": "9405511899223344556", "placed": "Aug 9"},
    "NS-10315": {"item": "Cascade Water Bottle", "status": "processing", "carrier": None, "eta": "Aug 16 (pending fulfillment)", "tracking": None, "placed": "Aug 11"},
    "NS-10327": {"item": "Compass Wool Beanie", "status": "delayed", "carrier": "UPS", "eta": "Aug 18 (was Aug 14)", "tracking": "1Z999AA10556677889", "placed": "Aug 6"},
    "NS-10340": {"item": "Thermal Base Layer", "status": "delivered", "carrier": "FedEx", "eta": "Delivered Aug 10", "tracking": "7712994499", "placed": "Aug 3"},
    "NS-10356": {"item": "Trailhead Jacket", "status": "processing", "carrier": None, "eta": "Aug 17 (pending fulfillment)", "tracking": None, "placed": "Aug 12"},
    "NS-10362": {"item": "Aurora Sneaker", "status": "delivered", "carrier": "UPS", "eta": "Delivered Aug 11", "tracking": "1Z999AA10334455667", "placed": "Aug 4"},
    "NS-10378": {"item": "Summit Backpack", "status": "shipped", "carrier": "USPS", "eta": "Aug 15", "tracking": "9405511899667788990", "placed": "Aug 10"},
    "NS-10390": {"item": "Cascade Water Bottle", "status": "delivered", "carrier": "FedEx", "eta": "Delivered Aug 12", "tracking": "7712994512", "placed": "Aug 7"}
}

RETURN_POLICY = {"windowDays": 30, "nonReturnable": ["final sale", "gift card", "personal care"]}

INVENTORY = {
    "trailhead jacket": {"S": 0, "M": 3, "L": 0, "XL": 5, "restock": "Aug 20"},
    "aurora sneaker": {"S": 2, "M": 0, "L": 1, "XL": 0, "restock": "Aug 18"},
    "summit backpack": {"S": 8, "M": 8, "L": 8, "XL": 8, "restock": None},
    "ridge fleece pullover": {"S": 4, "M": 12, "L": 0, "XL": 7, "restock": "Aug 22"},
    "alpine trekking poles": {"STANDARD": 18, "PRO CARBON": 0, "restock": "Aug 28"},
    "cascade water bottle": {"20OZ": 30, "32OZ": 14, "restock": None},
    "compass wool beanie": {"CHARCOAL": 9, "OATMEAL": 0, "FOREST GREEN": 2, "restock": "Sept 05"},
    "thermal base layer": {"S": 0, "M": 10, "L": 6, "restock": "Aug 19"}
}

# ===== Helper functions =====
def find_order(order_id: str) -> Optional[Dict]:
    """Look up an order and return details"""
    normalized_id = order_id.upper().replace('NS ', 'NS-')
    if not normalized_id.startswith('NS-'):
        normalized_id = 'NS-' + normalized_id.replace('NS', '')
    return ORDERS.get(normalized_id)

def handle_free_text(message: str) -> Tuple[str, float, Optional[Dict]]:
    """Route user message to appropriate handler"""
    lower = message.lower()
    
    # Extract order number: NS-10234, NS 10234, order #1001, etc.
    order_match = re.search(r'(?:NS\s*-?\s*)?(\d{5})', lower)
    if order_match and 'order' in lower:
        order_id = f"NS-{order_match.group(1)}"
        order = find_order(order_id)
        if order:
            status_messages = {
                "processing": f"Order {order_id} ({order['item']}) is being prepared. ETA: {order['eta']}.",
                "shipped": f"Order {order_id} ({order['item']}) shipped via {order['carrier']}. Tracking: {order['tracking']}. ETA: {order['eta']}.",
                "delayed": f"Order {order_id} ({order['item']}) is running late via {order['carrier']}. New ETA: {order['eta']}.",
                "delivered": f"Order {order_id} ({order['item']}) delivered {order['eta']} via {order['carrier']}."
            }
            reply = status_messages.get(order["status"], "Order status unknown.")
            return reply, 0.95, {
                "order_id": order_id,
                "status": order["status"],
                "tracking": order.get("tracking"),
                "carrier": order.get("carrier"),
                "items": [{"sku": "UNKNOWN", "name": order["item"], "returnable_until": "2026-09-09"}]
            }
    
    # NS-XXXXX format
    ns_match = re.search(r'NS-?\s*(\d{5})', lower)
    if ns_match:
        order_id = f"NS-{ns_match.group(1)}"
        order = find_order(order_id)
        if order:
            status_messages = {
                "processing": f"Order {order_id} ({order['item']}) is being prepared. ETA: {order['eta']}.",
                "shipped": f"Order {order_id} ({order['item']}) shipped via {order['carrier']}. Tracking: {order['tracking']}. ETA: {order['eta']}.",
                "delayed": f"Order {order_id} ({order['item']}) is running late via {order['carrier']}. New ETA: {order['eta']}.",
                "delivered": f"Order {order_id} ({order['item']}) delivered {order['eta']} via {order['carrier']}."
            }
            reply = status_messages.get(order["status"], "Order status unknown.")
            return reply, 0.95, {
                "order_id": order_id,
                "status": order["status"],
                "tracking": order.get("tracking"),
                "carrier": order.get("carrier"),
                "items": [{"sku": "UNKNOWN", "name": order["item"], "returnable_until": "2026-09-09"}]
            }
    
    # Returns & refunds
    if re.search(r'\b(return|refund|exchange|send.*back)\b', lower):
        reply = "What category is the item? Apparel (30-day return window) or Electronics?"
        return reply, 0.85, None
    
    # Stock availability
    product_match = next((p for p in INVENTORY.keys() if p in lower), None)
    if product_match:
        options = ', '.join(k for k in INVENTORY[product_match].keys() if k != 'restock')
        reply = f"Which size/option for {product_match.title()}? Options: {options}"
        return reply, 0.85, None
    
    # Default
    reply = "I can help with order status, returns/refunds, or stock availability. What's your question?"
    return reply, 0.5, None

# ===== API Endpoints =====
@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({"error": "No message provided"}), 400
        
        reply, confidence, chat_data = handle_free_text(message)
        
        return jsonify({
            "reply": reply,
            "confidence": confidence,
            "data": chat_data
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "service": "northstar-support-deflection"})

if __name__ == '__main__':
    # Get port from environment or use 5000
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Northstar Support Deflection MVP on port {port}...")
    app.run(debug=True, host='0.0.0.0', port=port)
