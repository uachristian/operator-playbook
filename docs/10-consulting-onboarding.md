# 10 — Consulting onboarding

How a consultant uses this playbook to stand up an agent for a client. The client owns everything; the consultant leaves nothing behind that phones home.

## Principles

- The client owns their data, credentials, accounts, agent configuration, and outputs.
- The consultant never holds client secrets. The client creates credentials and enters them locally.
- The agent has no connection to the consultant or to the playbook's author after setup.
- Everything installed is readable text the client can inspect.

## Engagement steps

1. **Scope call.** Agree on the first three jobs, the systems involved, and what is off-limits. Write it down.
2. **Environment.** The client provides the machine or account the agent runs on. The consultant does not host it unless separately contracted, with its own data agreement.
3. **Bootstrap session.** With the client present, tell the agent: "Read BOOTSTRAP.md from https://github.com/uachristian/operator-playbook and follow it." Prefer a local checkout: `git clone` the repos, then tell the agent to read BOOTSTRAP.md from the checkout. The client answers the interview.
4. **Credential entry.** For each system, the client creates the narrowest credential and enters it into the local secrets file or password manager. The consultant may point at the vendor's settings page; the client types the value.
5. **Read-only first.** Connect systems read-only (`08-integrations-readonly-first.md`). Deliver one useful report per system before discussing writes.
6. **Approvals.** Configure the approval channel so the client, not the consultant, approves gated actions.
7. **First-week checklist.** Run it with the client. Fix the operating files based on what they correct.
8. **Handover.** Give the client a one-page summary: files created, systems connected and access level, actions that need approval, how to revoke each credential, how to stop scheduled jobs.

## Consultant access

- Prefer screen-share sessions over standing remote access.
- If standing access is needed, use a separate named account the client can revoke, with least privilege and an expiry.
- Revoke consultant access at handover unless a support contract says otherwise.

## Customizing for a client

- Fork or copy this playbook into the client's own account if they want to track changes.
- Put client-specific facts in their vault and operating files, never in a shared public fork.
- Keep reusable improvements generic and contribute them back without client details.

## Data handling

- No client data in the consultant's notes, prompts, or demos. Use synthetic examples.
- If the client needs data moved between systems, the client approves the plan (`templates/change-plan.md`) and the migration runs read-only on source with verified readback on target.

## Offboarding checklist

- [ ] Consultant credentials and remote access revoked.
- [ ] Client knows how to rotate every credential the agent uses.
- [ ] Client knows how to disable schedules, webhooks, and integrations.
- [ ] Backups of operating files exist in the client's control.
- [ ] Open `TODO(owner)` items handed over in writing.
