"""
Returns/refunds handler helpers (supplementary).
This module contains utilities to summarize return eligibility and compose return instructions.
Included to represent T4 in the audit trail.
"""
from datetime import datetime, timedelta


def item_returnable(item):
    """Return True if item's returnable_until >= today (YYYY-MM-DD)"""
    try:
        ret_by = item.get("returnable_until")
        if not ret_by:
            return False
        today = datetime.utcnow().strftime("%Y-%m-%d")
        return ret_by >= today
    except Exception:
        return False


def summarize_returns(order):
    if not order:
        return None
    items = order.get("items", [])
    lines = []
    any_returnable = False
    for it in items:
        r = item_returnable(it)
        lines.append({
            "sku": it.get("sku"),
            "name": it.get("name"),
            "returnable": r,
            "returnable_until": it.get("returnable_until")
        })
        any_returnable = any_returnable or r

    refund_eta = (datetime.utcnow() + timedelta(days=7)).strftime("%Y-%m-%d") if any_returnable else None
    steps = [
        "Log into your account → Orders → Select the order → Choose 'Return item'.",
        "Print the pre-paid label or bring to a drop-off point.",
        "Ship the item; once we receive it, refunds process in 5-10 business days."
    ] if any_returnable else []

    return {
        "items": lines,
        "any_returnable": any_returnable,
        "refund_eta": refund_eta,
        "steps": steps
    }
