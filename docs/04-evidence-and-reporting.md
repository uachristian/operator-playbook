# 04 — Evidence and reporting

Reports are only useful if the owner can trust every claim in them.

## Separate states

Never let one state imply another:

| State | Meaning |
|---|---|
| Planned | Written down, not executed |
| Drafted | Prepared for review, not sent or applied |
| Built | Source changed |
| Tested | Required checks ran and passed on this exact candidate |
| Reviewed | Required reviewer finished on this exact candidate |
| Installed | Artifact placed where it runs |
| Runtime-verified | Observed working in its real runtime |
| Accepted | Owner confirmed the user-visible result |

Never write "executed" before execution or "done" before readback.

## Every claim needs

- source (command, API, file, person);
- observed time;
- identity of what was checked (commit, record ID, version);
- coverage (all, sample, partial);
- unknowns.

Missing or stale evidence is UNKNOWN, not healthy. A job with no recent result is UNKNOWN, not passing.

## Recurring reports

Mark each item:

- **NEW** — first appearance.
- **CHANGED** — seen before; something material changed (say what).
- **UNCHANGED** — seen before; no change. Keep it short or collapse it.
- **HELD** — waiting on an owner decision, approval, or external party. Name who and what.

Include for each actionable item: evidence age, owner, next action. Distinguish a live incident from a repeated report of an old one and from historical errors already resolved.

## Final task reports

End every task with:

1. Outcome in one or two lines.
2. What changed (files, records, systems).
3. How it was verified, with real evidence.
4. What was not verified and why.
5. What needs the owner, as concrete decisions or steps.
6. Rollback status.

## Subagent and third-party results

- A child agent's summary is a claim. Check the actual diff, files, and test runs yourself.
- File existence is not correctness. A green mocked test is not integration proof.
- Late results: match them to the current mission, scope, and candidate before acting. Classify as CURRENT, UNVERIFIED, SUPERSEDED, ALREADY_INCORPORATED, WRONG_MISSION, or INVALID.
- An old security finding still requires reproduction against current code, even if superseded.

## Exit codes and logs

- Preserve true exit codes. No `|| true`, no pipes that hide failure, no cleanup step that turns a failure green.
- Keep logs for required gates. Do not put secrets or customer data into logs.

## Speed claims

No speedup claims without a measured baseline. A small sample does not establish a trend.
