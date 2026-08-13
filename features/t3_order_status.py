"""
Order-status handler module (supplementary).
This module contains helper utilities extracted from the main app to support the order-status intent.
Included to create an audit-friendly commit representing T3.
"""
from datetime import datetime


def summarize_order_status(order):
    if not order:
        return None
    status = order.get("status")
    if status == "shipped":
        return {
            "message": f"Order {order['order_id']} shipped via {order.get('carrier','Unknown')}. Tracking: {order.get('tracking','N/A')}",
            "status": "shipped"
        }
    if status == "processing":
        return {"message": f"Order {order['order_id']} is processing. Estimated ship date: {order.get('estimated_ship_date','N/A')}", "status": "processing"}
    if status == "delivered":
        return {"message": f"Order {order['order_id']} was delivered on {order.get('delivered_at','N/A')}", "status": "delivered"}
    return {"message": f"Order {order['order_id']} status: {status}", "status": status}
