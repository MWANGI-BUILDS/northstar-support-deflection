"""
Generic ticketing webhook connector template.

- Reads TICKET_WEBHOOK_URL from env.
- If not set, logs and returns a mocked response (so local demo continues).
- Keeps payload generic: subject, body, metadata.
"""
import os
import requests
import logging
from datetime import datetime

logger = logging.getLogger("ticketing-connector")
TICKET_WEBHOOK_URL = os.getenv("TICKET_WEBHOOK_URL")
TICKET_WEBHOOK_AUTH = os.getenv("TICKET_WEBHOOK_AUTH")  # optional
REQUEST_TIMEOUT = float(os.getenv("TICKET_REQUEST_TIMEOUT", "5"))

def create_ticket(payload):
    """
    payload: dict containing at least subject and body. Additional metadata accepted.
    Returns the webhook response (or a mock dict if no webhook configured).
    """
    if not TICKET_WEBHOOK_URL:
        logger.info("TICKET_WEBHOOK_URL not configured. Returning mock ticket response.")
        return {"status": "mock", "created_at": datetime.utcnow().isoformat(), "payload": payload}

    headers = {"Content-Type": "application/json"}
    if TICKET_WEBHOOK_AUTH:
        headers["Authorization"] = TICKET_WEBHOOK_AUTH

    try:
        resp = requests.post(TICKET_WEBHOOK_URL, json=payload, headers=headers, timeout=REQUEST_TIMEOUT)
        try:
            resp_json = resp.json()
        except Exception:
            resp_json = {"status_code": resp.status_code, "text": resp.text}
        if resp.status_code >= 200 and resp.status_code < 300:
            logger.info("Ticket created via webhook: %s", resp_json)
            return {"status": "ok", "response": resp_json}
        logger.warning("Ticketing webhook returned %s: %s", resp.status_code, resp.text)
        return {"status": "error", "status_code": resp.status_code, "response": resp_json}
    except Exception as e:
        logger.exception("Error calling ticketing webhook: %s", e)
        raise
