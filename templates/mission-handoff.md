# Mission handoff

Temporary task state for resuming work across sessions or agents. Not long-term memory. No secrets, raw customer data, or full transcripts.

- Mission ID:
- Scope revision:
- Current candidate (commit / artifact / version):
- Owner, approved outcome, non-goals, approval limits:
- Paths in play and who owns uncommitted changes:
- Completed acceptance evidence (commands, exit codes):
- Required gates still open:
- Long-running processes: owner, PID, start time, completion evidence:
- Rollback and next exact command:
- Budget used / remaining; blocked time separately:

## Worker / result ledger
| Worker | Required gate or optional | Target candidate | Result | Artifact path | Parent verified? | Disposition |
|---|---|---|---|---|---|---|

Dispositions: CURRENT, UNVERIFIED, SUPERSEDED, ALREADY_INCORPORATED, WRONG_MISSION, INVALID. They classify relevance, not approval.

## Rules
- On resume, read current source and this file before old transcripts.
- Classify every late result before acting on it. Match mission, scope, candidate, and worker.
- An old security finding is a signal to reproduce against current code, even if its target was superseded.
- Do not replay completed commands or redispatch unchanged timed-out work.
- Record a result as incorporated only after the parent verifies it.
