# The Northstar Sprint — Team Pod Submission

**Client:** Northstar Retail Co.
**Engagement:** 1-week Support Deflection MVP
**Pod:** Michael · Victor · Sandisiwe · Esther · Ann
**Sprint window:** Day 1–5 (as defined in the brief)

This repository is the single paper trail for all three assessed deliverables. It is organized so that
an evaluator (or Northstar's procurement office) can walk in cold and verify, in order: (1) that the team
set itself up correctly, (2) that the work was genuinely collaborative and traceable, and (3) that the
prototype actually does what it claims.

## Folder map

| Folder | Maps to | Contains |
|---|---|---|
| `01-team-charter/` | Assignment 1 | Signed Team Charter — communication, deadlines, conflict resolution, escalation path |
| `02-project-board/` | Assignment 1 | 12-task board, each ≤4 hrs, owner + priority + Definition of Done |
| `03-prototype/` | Assignment 2 | The working Support Deflection MVP (runnable, single file) |
| `04-audit-log/` | Assignment 2 | Commit/edit convention, raw activity log, mid-sprint audit snapshot |
| `05-go-live-note/` | Product deliverable (ships with prototype) | 1-page go-live readiness note for Northstar's team |
| `06-individual-assessments/` | Assignment 3 | Day 1 baseline diagnostic template, self-assessment template, confidential Peer Reliability Index |

## How the three assignments map to what's inside

### Assignment 1 — Team Working Agreement & Board Setup (Team submission)
- `01-team-charter/TEAM_CHARTER.md` — signed by all 5 members, with an explicit escalation rule (0 visible
  activity for 2+ days → auto-flagged).
- `02-project-board/PROJECT_BOARD.md` — 12 granular tasks (>10 required), none over 4 hours, each with an
  owner, priority, and a single-sentence Definition of Done, satisfying the anti–black-box rule.

### Assignment 2 — Collaborative Delivery & Audit Log (Pair/small group submission)
- `03-prototype/` — the multi-author artifact: a decision-tree Support Deflection MVP covering **Order
  Status** and **Returns & Refunds** (2 of 3 required categories), with Stock Availability included as a
  stretch third category.
- `04-audit-log/AUDIT_LOG.md` — the commit/edit convention used (`<type>: <what changed> — <why it
  matters>`), plus the raw log template and the Day 4 mid-sprint audit snapshot showing contribution
  balance and task-to-commit traceability.
- `05-go-live-note/GO_LIVE_NOTE.md` — the 1-page note Northstar's own team needs to run this without the
  pod in the room.

### Assignment 3 — Individual Baseline & Peer Diagnostic (Individual submission, one per member)
- `06-individual-assessments/DAY1_BASELINE_DIAGNOSTIC.md` — the 30-minute solo diagnostic each member
  completes alone on Day 1 AM, before any team collaboration.
- `06-individual-assessments/SELF_ASSESSMENT_TEMPLATE.md` — Day 5 self-assessment vs. Day 1 baseline.
- `06-individual-assessments/PEER_RELIABILITY_INDEX.md` — the confidential 5-question peer rating. Each
  member fills out **one copy per teammate**, submits it individually and privately; only aggregate
  patterns are ever shared back to the team.

## Task allocation at a glance

| Member | Primary lane | Board tasks owned |
|---|---|---|
| **Michael** | Team lead, Order Status module, board/charter setup | T1, T2, T6, T11 |
| **Victor** | Returns & Refunds module, backend logic + testing | T3, T7, T12 |
| **Sandisiwe** | Stock Availability module, frontend/UI build | T4, T8 |
| **Esther** | Audit log discipline, QA, commit-message policing | T5, T9 |
| **Ann** | Go-live note, documentation, demo script, assessment compilation | T10, T13 |

(Full task detail with priorities and Definitions of Done is in `02-project-board/PROJECT_BOARD.md`.)

## Day-by-day status (fill in live, don't batch)

| Day | Phase | Owner of the update | Status |
|---|---|---|---|
| Day 1 AM | Solo baseline diagnostic (all 5, independently) | Each member | ☐ |
| Day 1 PM | Charter + Board workshop (90 min, all 5) | Michael (facilitator) | ☐ |
| Day 2–3 | Build against the board | All (see task table) | ☐ |
| Day 4 | Mid-sprint audit pull + escalation check | Esther | ☐ |
| Day 5 | Package + submit all three assignments | Ann (compiler), all sign off | ☐ |

## Quick start — running the prototype

```
cd 03-prototype
open index.html      # or double-click it — no build step, no server required
```

See `03-prototype/README.md` for the full walkthrough and demo script.
