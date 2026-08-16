# Commit / Edit Audit Log — Support Deflection MVP

This is the audit trail Northstar's procurement office requires before releasing payment. It has three
parts: (1) the convention every contribution followed, (2) the raw log itself, (3) the Day 4 mid-sprint
snapshot that checked contribution balance before it was too late to fix.

## 1. Convention (set Day 1, enforced by Esther)

Every commit, tracked-document edit, or board-status change uses:

```
<type>: <what changed> — <why it matters>
```

`type` is one of: `feat`, `fix`, `docs`, `test`, `chore`, `refactor`.
`wip` and `updates` are rejected — the reviewer asks for a rewrite before it counts toward the log.

**Branch naming (if using git):** `<initials>/<task-id>-<short-desc>`, e.g. `vc/t7-returns-logic`.

### Worked examples actually used this sprint

- `feat: implement returns eligibility check — enforces 30-day window per client requirement`
- `feat: add stock lookup by size — covers the 3rd deflection category as a stretch goal`
- `docs: write go-live known-issues section — Northstar needs this before they run it unsupervised`
- `fix: correct order/returns keyword collision in router — "return order" was mis-routing to order status`
- `test: run 10-question routing accuracy pass — confirms T11 Definition of Done is met`
- `chore: set up board columns and 15 tasks — satisfies Assignment 1 granularity requirement`

## 2. Raw log (export format)

Export this directly from git (`git log --pretty=format:'%h | %an | %ad | %s' --date=short`) or from the
board tool's activity feed. Template below — replace with the real export before submission.

| Timestamp | Member | Type | Message | Task ID | Board column moved to |
|---|---|---|---|---|---|
| Day 1, 14:20 | Michael | chore | Set up board columns and 15 tasks — satisfies Assignment 1 granularity requirement | T2 | Done |
| Day 1, 15:05 | Michael | docs | Draft charter from workshop notes — captures escalation path agreed live | T1 | Done |
| Day 1, 16:40 | Esther | docs | Define commit convention with 3 examples — sets audit standard before build starts | T5 | Done |
| Day 2, 09:15 | Victor | feat | Add 8-order mock data set — covers processing/shipped/delivered/delayed states | T3 | Done |
| Day 2, 10:30 | Sandisiwe | feat | Add 6-product mock stock data set — 2 items deliberately out of stock for testing | T4 | Done |
| Day 2, 13:00 | Michael | feat | Implement order-status lookup logic — returns correct status for all 8 mock orders | T6 | Done |
| Day 2, 16:20 | Sandisiwe | feat | Build chat UI shell with quick-reply buttons — routes input to module stubs | T9 | In Progress |
| Day 3, 09:40 | Victor | feat | Implement returns eligibility check — enforces 30-day window | T7 | Done |
| Day 3, 11:15 | Sandisiwe | feat | Implement stock-by-size lookup — covers stretch 3rd category | T8 | Done |
| Day 3, 14:00 | Michael | feat | Wire router across all 3 modules — keyword-match with order-ID extraction | T11 | Review |
| Day 3, 15:30 | Ann | docs | Draft fallback + handoff copy for all 3 modules — no dead ends in the flow | T10 | Done |
| Day 3, 17:10 | Esther | fix | Correct order/returns keyword collision in router — "return order" mis-routed | T11 | Done |
| Day 4, 09:00 | Esther | chore | Pull commit + board timestamp log for checkpoint — no members show 2-day gaps | T14 | Done |
| Day 4, 10:00 | Victor | test | Run 10-question routing accuracy test, log results | T12 | Done |
| Day 4, 10:00 | Esther | test | Cross-check Victor's test log against router source | T12 | Done |
| Day 4, 15:00 | Ann | docs | Draft 1-page go-live note — what works / known-broken / handover sections | T13 | Done |
| Day 5, 10:00 | Ann | chore | Compile final submission package, circulate for team sign-off | T15 | Done |

*(Replace with the pod's actual timestamps/messages before submission — this table is the required shape,
not a substitute for the real export.)*

## 3. Mid-sprint audit snapshot (Day 4 — self-correction checkpoint)

Pulled by Esther per the Charter. This is checked **before** the deadline specifically so imbalance can be
fixed while there's still time, not discovered after the fact.

| Member | Commits/edits (Day 1–4) | Board tasks moved to Done | Longest activity gap | Flag? |
|---|---|---|---|---|
| Michael | | | | |
| Victor | | | | |
| Sandisiwe | | | | |
| Esther | | | | |
| Ann | | | | |

**Escalation check:** did any member show 0 visible activity for 2+ consecutive days? ☐ Yes ☐ No
If yes — record which Charter escalation step was taken and the outcome:

> _(fill in — e.g. "Step 1 check-in posted Day 3, resolved same day; no reassignment needed.")_

## 4. Traceability check

Every task on the board (`02-project-board/PROJECT_BOARD.md`) should be traceable to at least one log
entry above by Task ID. Before submission, confirm: ☐ every Done task has ≥1 matching log row · ☐ every
log row references a real Task ID · ☐ no member's contribution is limited to a single day.