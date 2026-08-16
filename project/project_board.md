# Project Board — Support Deflection MVP

Set this up as the literal board (Trello / GitHub Projects / Notion — team's choice; columns:
**Backlog → In Progress → Review → Done**). This file is the board's source-of-truth export so it's
auditable outside whatever tool is used. Every task obeys the anti-black-box rule: ≤4 hours, and the DoD
is one checkable sentence. Status must be moved the same day work happens — no batching.

Priority key: **P0** = blocks the demo · **P1** = required for the 2-category minimum · **P2** = stretch
(3rd category / polish).

| ID | Task | Owner | Priority | Est. | Definition of Done | Status |
|---|---|---|---|---|---|---|
| T1 | Draft Team Charter from workshop discussion and post for sign-off | Michael | P0 | 1h | Charter doc exists in repo with all 5 names in the signature table | Done |
| T2 | Set up project board with columns + this task list, tag owners/priority | Michael | P0 | 1h | Board is live and contains ≥10 tasks each with owner + priority + DoD | Done |
| T3 | Draft mock data set: 8 sample orders with status/tracking fields | Victor | P0 | 2h | `orders.js` contains 8 orders covering states: processing, shipped, delivered, delayed | Done |
| T4 | Draft mock data set: 6 sample products with stock levels and sizes | Sandisiwe | P1 | 2h | `stock.js` contains 6 products with size/quantity fields, at least 2 out-of-stock | Done |
| T5 | Define commit/edit message convention and pin it in the audit log doc | Esther | P0 | 1h | `AUDIT_LOG.md` states the `<type>: <what> — <why>` convention with 3 worked examples | Done |
| T6 | Build Order Status decision-tree logic (order-number lookup → status → next step) | Michael | P1 | 4h | Entering any of the 8 mock order numbers returns the correct status and an accurate next-step message | Done |
| T7 | Build Returns & Refunds decision-tree logic (eligibility check → instructions → refund timeline) | Victor | P1 | 4h | For a delivered order within/outside the return window, the flow returns the correct eligibility and refund-timeline message | Done |
| T8 | Build Stock Availability lookup logic (product/size search → in-stock or restock message) | Sandisiwe | P2 | 3h | Searching any of the 6 mock products by name returns correct stock status per size | Done |
| T9 | Build the chat-style UI shell (input box, message thread, category buttons) | Sandisiwe | P1 | 4h | UI renders in-browser with no console errors and routes input to the correct module | Done |
| T10 | Write escalation fallback copy ("I can't help with that — here's how to reach a human") for all 3 modules | Ann | P1 | 1h | Every unmatched query returns the fallback message instead of a blank/broken response | Done |
| T11 | Wire all 3 modules into a single entry point + basic input router (keyword match to category) | Michael | P0 | 3h | Typing a natural question ("where's my order", "how do I return this", "is this back in stock") routes to the correct module ≥90% of a 10-question test set | Done |
| T12 | End-to-end manual test pass across all 3 categories + log bugs found | Victor + Esther | P0 | 2h | A written test log exists showing ≥10 test queries run with pass/fail noted | Done |
| T13 | Write the 1-page go-live readiness note (what works / known-broken / handover needs) | Ann | P0 | 2h | `GO_LIVE_NOTE.md` fits on one page and covers all 3 required sections | Done |
| T14 | Pull raw commit/edit + board timestamp log for Day 4 checkpoint and flag any imbalance | Esther | P0 | 1h | `AUDIT_LOG.md` mid-sprint snapshot table is filled in with real per-member counts by Day 4 | Done |
| T15 | Compile final submission package (repo + audit export + go-live note) and circulate for sign-off | Ann | P0 | 2h | All 5 members confirm in-channel that their work is represented before Day 5 submission | Done |

**Total tasks: 15** (exceeds the 10+ minimum). No single task exceeds 4 hours. Every DoD is a single
checkable sentence — nothing on this board is a "black box."

## Column view (for the actual board tool)

- **Backlog:** empty by Day 3 (everything should have moved at least to In Progress)
- **In Progress:** update same-day when a task starts
- **Review:** owner moves here when they believe DoD is met; one other member checks it against the DoD
  before moving to Done
- **Done:** only after the DoD sentence has been verified true, not just "code written"