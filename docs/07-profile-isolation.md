# 07 — Profile isolation

One agent with access to everything is one compromised prompt away from leaking everything. Split trust domains into separate agent profiles.

## What a profile is

A profile is an agent identity with its own persona file, memory, skills, secrets file, tool set, schedules, and channel bindings. Most harnesses support this as separate config directories, workspaces, or projects.

## When to split

Create a separate profile when any of these differ:

- data sensitivity (personal vs business, HR vs operations);
- who may talk to it (owner only vs team vs customers);
- blast radius of its tools (read-only reporting vs live writes vs physical devices);
- the credentials it needs.

Common split for a small business:

| Profile | Purpose | Typical access |
|---|---|---|
| orchestrator | Owner's main agent; coordinates others | Broad read, gated writes |
| ops | Day-to-day operations triage | Business systems read, drafts |
| builder | Experiments and code | Repos and sandboxes, no production credentials |
| personal | Owner's private matters | Personal accounts only |
| devices | Smart building or equipment | Device controls, conservative gates |

## Rules

- No shared credentials. Each profile has its own secrets file with only the keys it needs.
- No cross-profile reads of private memory, history, or vault lanes.
- Minimal tool sets per profile. Do not enable tools a profile does not use.
- Do not copy messaging bot tokens between profiles.
- Specialists report evidence; cross-profile or production-boundary changes route to the orchestrator and the owner.
- When the orchestrator delegates to a specialist, state scope, write paths, tool limits, and whether it may save durable facts.
- Isolation is the design. Do not "fix" it by sharing state for convenience.

## Authority is an intersection

What a profile may do is the intersection of: the owner's current request, the profile's own grants, and any path rules (such as vault permissions). Supervision by an orchestrator does not expand a specialist's access. Use the strictest boundary when they conflict and ask the owner to adjudicate.

## Shared channels

- In group chats, a bot speaks only when addressed or clearly needed.
- Never answer on behalf of another bot.
- Bot-to-bot messages need one packet, a cooldown, and deduplication to prevent loops.
