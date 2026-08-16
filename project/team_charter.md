# Team Working Agreement — The Northstar Sprint

**Pod members:** Michael, Victor, Sandisiwe, Esther, Ann
**Client engagement:** Northstar Retail Co. — Support Deflection MVP
**Effective:** Day 1, PM workshop · **Applies for:** full 5-day sprint

By adding their name in the signature table at the bottom, each member confirms they were present at the
Day 1 charter workshop, understand these norms, and agree to be held to them.

## 1. Purpose

We are a 5-person pod delivering one MVP artifact plus its audit trail for Northstar Retail Co. in one
week. This charter exists so that (a) decisions get made quickly without a manager in the room, and
(b) every member's contribution is visible and checkable, because procurement will not release payment
without a credible collaboration audit trail.

## 2. Communication rules

- **Primary channel:** shared team chat (Slack/WhatsApp group — named on Day 1) for day-to-day updates.
- **Daily check-in:** one asynchronous update per member per working day, posted by 6pm local time,
  answering: *what I did today, what's blocking me, what I'm doing next.* This is not a meeting — it's a
  2–3 line message.
- **Synchronous check-ins:** Day 1 PM (charter + board workshop, 90 min), Day 4 (checkpoint, 20 min), Day
  5 (delivery wrap, 20 min). All other syncs are opt-in, called by whoever is blocked.
- **Response time:** a direct question/tag gets a response (even "seen, will answer properly by X") within
  4 working hours during the sprint window.
- **No silent scope changes.** If a task's scope or estimate changes, the owner posts it in-channel before
  changing the board — not after.

## 3. Deadlines & ways of working

- Every board task carries an owner, a priority, and a Definition of Done (DoD) that is a single checkable
  sentence — per the anti–black-box rule, no task may represent more than 4 hours of work. If a task
  can't be described as one checkable sentence, it gets split before work starts.
- **Board status moves the same day the work happens.** Batching updates to the end of the week defeats
  the audit log's purpose and is treated as a charter violation.
- **Commit/edit message convention (mandatory for all contributions — code, docs, board edits):**
  `<type>: <what changed> — <why it matters>`
  Examples: `feat: add returns decision-tree branch — covers refund-eligibility question type`,
  `docs: draft go-live note section 2 — Northstar needs known-issues list before handover`.
  `wip` / `updates` / `fix stuff` are not acceptable and will be asked to be redone.
- **Branch naming (if using version control):** `<member-initials>/<task-id>-<short-desc>`, e.g.
  `mn/t6-order-status-api`.

## 4. Decision-making & conflict resolution

- Default: the task **owner** decides implementation details within their lane.
- Cross-lane decisions (affecting 2+ members' work): raised in the team channel, decided by simple
  majority if not resolved by discussion within 24 hours.
- Disagreements about quality or scope: the person raising the concern states it in one message
  (what's wrong, what they'd prefer instead); the owner responds within 24 hours; if unresolved after
  one round, Michael (facilitator) makes the final call so the sprint doesn't stall.
- We assume good faith by default — a missed update is treated as a logistics problem to solve, not a
  character judgment, unless the escalation path below is triggered.

## 5. Escalation path (non-negotiable)

- **Trigger:** zero visible activity (no commit/edit, no board movement, no check-in message) from a
  member for **2 consecutive days**.
- **Step 1 (Day of detection):** whoever notices posts a direct, non-accusatory check-in tag in the team
  channel ("hey [name], haven't seen movement on [task] since [date] — everything okay? need anything
  reassigned?"). This happens immediately, not at the Day 4 checkpoint or the deadline.
- **Step 2 (within 24 hrs, no response):** Michael reaches out 1:1 directly (call/DM) to understand the
  blocker.
- **Step 3 (still unresolved):** at the Day 4 checkpoint this is logged in the mid-sprint audit snapshot
  as an open flag, the affected tasks are reassigned or descoped so the deliverable still ships, and it is
  noted (factually, without blame language) in the final audit log.
- This path exists to protect the deliverable and the team, not to punish — the goal is always to unblock
  early enough that Day 5 delivery isn't at risk.

## 6. Confidentiality

- The Day 5 Peer Reliability Index is **confidential**: each member's individual ratings of teammates are
  never shared verbatim with the person being rated. Only aggregate patterns (e.g., "communication
  clarity trended lower across 3 of 4 raters") may be surfaced back to the team, and only in aggregate.

## 7. Definition of Done for the sprint overall

The sprint is "done" when: the prototype demoably handles ≥2 of the 3 ticket categories end-to-end, the
go-live note is written, the audit log is exported and covers the full week with no unexplained gaps, and
all 5 members have submitted their individual Assignment 3 components.

## Signatures

| Member | Role/lane this sprint | Signed (initials) | Date |
|---|---|---|---|
| Michael | Team lead / facilitator, Order Status module | | Day 1 |
| Victor | Returns & Refunds module | | Day 1 |
| Sandisiwe | Stock Availability module, UI build | | Day 1 |
| Esther | Audit log & QA discipline | | Day 1 |
| Ann | Documentation, go-live note, demo | | Day 1 |