"""
Orders connector template.

Behavior:
- If ORDERS_API_BASE_URL is configured, call GET {ORDERS_API_BASE_URL}/orders/{order_id}
  (supports API key via ORDERS_API_KEY header or ORDERS_API_KEY_HEADER_NAME).
- Otherwise, falls back to demo mock orders for local demo/testing.
- Normalizes the response into a dict with keys used by app.py.
"""
import os
import requests
import logging

logger = logging.getLogger("orders-connector")
ORDERS_API_BASE_URL = os.getenv("ORDERS_API_BASE_URL")
ORDERS_API_KEY = os.getenv("ORDERS_API_KEY")
ORDERS_API_KEY_HEADER_NAME = os.getenv("ORDERS_API_KEY_HEADER_NAME", "X-API-KEY")
REQUEST_TIMEOUT = float(os.getenv("ORDERS_REQUEST_TIMEOUT", "5"))

# Demo fallback dataset (kept small)
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
        "status": "delivered",
        "delivered_at": "2026-08-05T16:30:00Z",
        "items": [{"sku": "JKT-GRY-L", "name": "Jacket Gray L", "returnable_until": "2026-09-04"}],
        "total": 129.99
    }
}

def normalize_order(resp_json):
    """
    Convert a provider-specific order JSON into the normalized shape used by app.py.
    If your Orders API already matches this shape, return identity mapping.
    """
    # Basic normalization for typical JSON shapes (adapt as needed)
    if not resp_json:
        return None
    # If the API already returns order_id, status, items etc. we pass through.
    if "order_id" in resp_json:
        return resp_json
    # Example normalization when API returns 'id' field
    order = {}
    order["order_id"] = resp_json.get("id") or resp_json.get("order_number")
    order["status"] = resp_json.get("status")
    order["shipped_at"] = resp_json.get("shipped_at")
    order["carrier"] = resp_json.get("carrier")
    order["tracking"] = resp_json.get("tracking_number") or resp_json.get("tracking")
    order["items"] = resp_json.get("items", [])
    return order

def get_order(order_id):
    if not order_id:
        return None
    if not ORDERS_API_BASE_URL:
        # Demo fallback
        logger.info("ORDERS_API_BASE_URL not configured — using demo mock orders for %s", order_id)
        return DEMO_ORDERS.get(order_id)
    url = f"{ORDERS_API_BASE_URL.rstrip('/')}/orders/{order_id}"
    headers = {}
    if ORDERS_API_KEY:
        headers[ORDERS_API_KEY_HEADER_NAME] = ORDERS_API_KEY
    try:
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        if resp.status_code == 200:
            return normalize_order(resp.json())
        if resp.status_code == 404:
            logger.info("Order %s not found (404)", order_id)
            return None
        logger.warning("Orders API returned %s for %s: %s", resp.status_code, order_id, resp.text)
        return None
    except Exception as e:
        logger.exception("Error calling Orders API: %s", e)
        raise
