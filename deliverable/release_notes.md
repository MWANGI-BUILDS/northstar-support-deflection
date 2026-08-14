Support Deflection MVP — Release notes

Release: v1.0.0 (feature/support-deflection-mvp)
Date: 2026-08-13

Summary
This release packages the Support Deflection MVP intended for procurement and handoff. It includes a lightweight Flask demo, connector templates for Orders and Ticketing, intent handlers for Order Status and Returns, documentation, smoke tests, and the audit log mapping tasks T1..T10 to commits.

Included artifacts (in this branch)
- app.py — Flask demo entrypoint
- connectors/ — orders_connector.py (template), ticketing.py (webhook connector)
- features/ — t3_order_status.py, t4_returns.py
- tests/smoke_tests.md — manual smoke test matrix
- go_live_note.md — 1-page go-live readiness note
- deliverable/audit_log.csv — final audit trail mapping T1..T10 to commit SHAs
- deliverable/README-deliverable.md — packaging README

Notable commits (T1..T10)
- T1: 5e14003 — feat: add Flask scaffold and run script
- T2: 0c72340 — feat: add orders connector template and demo mocks
- T3: 88d990b — feat: implement order-status intent handler
- T4: e909cdf — feat: implement returns/refunds handler
- T5: dfc7f3b — docs: add integration points & env variables doc
- T6: 9cf6cf4b — docs: add 1-page go-live readiness note
- T7: bdf18a8 — docs: add curl examples and expected outputs
- T8: 4673fe4 — docs: add audit_log_template.csv mapping tasks to commits
- T9: 6a64c02 — test: add smoke test matrix and manual test notes
- T10: e0c6270 — feat: add /deliverable packaging and final commit

How to create the GitHub release (recommended)
Option A: Using GitHub CLI (gh)
1) Install and authenticate gh (https://cli.github.com/)
2) From your local clone:
   git fetch origin
   git checkout feature/support-deflection-mvp
   gh release create v1.0.0 feature/support-deflection-mvp \
     --title "Support Deflection MVP v1.0.0" \
     --notes-file deliverable/release_notes.md
3) Upload the branch zip (if you prefer attaching the archive):
   gh release upload v1.0.0 northstar-support-deflection-feature-support-deflection-mvp.zip --clobber

Option B: Using the GitHub REST API (curl)
1) Create the release (replace $GITHUB_TOKEN):
   curl -X POST -H "Authorization: token $GITHUB_TOKEN" -H "Content-Type: application/json" \
     -d '{"tag_name":"v1.0.0","target_commitish":"feature/support-deflection-mvp","name":"Support Deflection MVP v1.0.0","body":"See deliverable/release_notes.md","draft":false,"prerelease":false}' \
     https://api.github.com/repos/MWANGI-BUILDS/northstar-support-deflection/releases
2) The response will include an upload_url. Use it to upload the zip (replace {upload_url} and $GITHUB_TOKEN):
   curl -X POST -H "Authorization: token $GITHUB_TOKEN" -H "Content-Type: application/zip" --data-binary @northstar-support-deflection-feature-support-deflection-mvp.zip "{upload_url}?name=northstar-support-deflection-feature-support-deflection-mvp.zip
