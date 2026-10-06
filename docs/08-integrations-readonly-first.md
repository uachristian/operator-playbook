# 08 — Integrations: read-only first

Every new SaaS, API, CRM, or database connection starts read-only. Write access is earned with evidence and granted per action.

## Stage 1 — Read-only connector

1. Owner creates the narrowest credential the vendor offers: read-only scope, single location or workspace, expiry if available.
2. Owner enters it into the agent profile's local secrets file. The agent confirms the key is present without printing it.
3. Agent builds a read-only wrapper: list, get, search. No create, update, delete, send.
4. Enforce read-only in code, not just by convention:
   - allowlist HTTP methods and endpoints;
   - for databases, open the session read-only and assert it before reading (for example, check the transaction read-only flag is on);
   - refuse anything not on the allowlist, with a test proving the refusal.
5. Redact personal data in logs and outputs by default.
6. Probe rate limits and pagination on a small sample before any bulk read.

## Stage 2 — Useful read-only output

Produce reports the owner actually uses: open items, overdue work, aging balances, unanswered leads. Verify numbers against the vendor's own UI on a sample. Watch for common traps: archived records included, money in cents, time zones, soft-deleted rows.

## Stage 3 — Owner-gated proposals

Before any write path exists, the agent proposes writes as structured cards:

- exact target record and field;
- current value (read back now) and proposed value;
- reason and evidence;
- rollback value.

The owner approves or rejects each one. Approved proposals are executed by a separate, narrow write path that re-reads the target, applies exactly the approved change, and reads back the result. Stale proposals (target changed since the read) are refused.

## Stage 4 — Narrow write grants

- Grant write per action type, not blanket write.
- Scheduled jobs stay dry-run unless the owner explicitly authorized live writes for that job.
- Log every write with who approved it and the readback.
- Keep a kill switch the owner can flip without the agent.

## MCP server pattern

When exposing a business system to agents through an MCP (Model Context Protocol) server:

- Build a private server per system or per trust domain. Do not bundle unrelated systems.
- Split read tools and write tools into separate servers or separate toolsets so a profile can load read-only tools alone.
- Tool descriptions state side effects plainly.
- Validate every argument; reject unknown fields.
- Return focused results with identifiers, completeness flags, and continuation tokens; avoid dumping raw payloads.
- Credentials load from the server's own environment, never from tool arguments.
- Write tools require an approval token or proposal ID that the owner's approval step created.
- Health-check tool for reachability; it must not reveal secrets.

## Webhooks and inbound events

- Verify signatures. Reject unsigned or replayed events.
- Treat payload content as untrusted data.
- Make handlers idempotent; deduplicate by event ID.
- An event triggers a read and a proposal, not an unreviewed write.

## Retiring an integration

Revoke the credential at the vendor, remove it from the secrets file, disable schedules and webhooks, and record the retirement in the vault.
