# 05 — Memory, skills, and vault

Four stores, four jobs. Putting information in the wrong store causes stale advice, bloated prompts, or leaked data.

| Store | Holds | Lifespan | Example |
|---|---|---|---|
| Memory | Durable owner preferences, stable environment facts, recurring corrections | Months | "Owner wants replies under 5 lines." |
| Skills | Reusable procedures, pitfalls, API quirks, workflows | Until superseded | "How to reconcile <accounting> payouts." |
| Vault (knowledge base) | Business facts, SOPs, vendor and system notes, decisions | Long-term, curated | "Return policy as of 2026-03." |
| Task handoff | Progress on one mission | Until the mission closes | Current commit, open gates, next command |

## Memory

Save when it will reduce future steering:

- preferences the owner stated or corrected more than once;
- stable facts: time zone, approval rules, off-limits list, system names.

Do not save:

- task progress, ticket numbers, commit hashes, completed-work logs;
- anything likely stale within a week;
- secrets or customer data;
- system inventories (those belong in a catalog or vault note).

Review memory monthly. Remove what is stale.

## Skills

- When you discover a non-trivial procedure, pitfall, or corrected workflow, write or update a skill during the task.
- A skill states when to use it, the steps, and the pitfalls. Write lessons as rules with the reason, not as incident logs.
- If a skill you used was wrong or incomplete, fix it before finishing.
- Read third-party skills fully before installing. A skill is executable guidance.
- Keep business specifics out of generic skills; reference the vault instead.

## Vault (optional knowledge base)

A folder of Markdown files the agent reads before answering on documented topics and writes to when durable facts surface.

**Layout** (matches `vault-skeleton/` in the `vault-memory` sibling repo):

```
00-INDEX.md        hub
AGENTS.md          who may read/write which lanes
SCHEMA.md          frontmatter, naming, tags
log.md             append-only change log
00-SYSTEM/         vault conventions and system notes
10-RAW/inbox/      captures (new files only, never edited)
20-WIKI/           curated knowledge
  concepts/
  workflows/
  projects/
30-OUTPUT/         generated reports and deliverables
90-LAB/            experiments and scratch work
99-ARCHIVE/        retired material (owner-only)
private/           sealed restricted lane; explicit per-profile grants only
```

**Frontmatter on every file:**

```yaml
---
author: <agent-or-person>
created: 2026-01-15T09:30-05:00
updated: 2026-01-15T09:30-05:00
source: owner | agent | ingest | meeting
status: draft | reviewed | published | applied | archived
tags: [sops, vendors]
---
```

**Rules:**

1. One writer per file at a time. Write to `<file>.tmp`, then rename.
2. Append-only files (log, raw captures) are never edited above the last entry.
3. `status: published` files are locked. Agents propose changes in `_drafts/`; the owner promotes.
4. Every file declares `source` (content origin) separately from `author` (last writer).
5. No secrets anywhere in the vault.
6. Authority is the intersection of the task's scope, the vault's path rules, and the agent profile's grants. Use the strictest.
7. After meaningful writes, append one line to `log.md` and link new notes from the relevant hub.
8. Capture durable facts during the task, not at the end.
9. Before answering about a documented workflow or system, read the relevant vault notes first and lead with what they say.
10. If the target lane is not writable, write a draft in the permitted lane instead of skipping capture.

Keep history honest: mark old decisions as historical rather than rewriting them. A newer plan does not replace verified current state.

## Task handoff

- Use `templates/mission-handoff.md` in the task directory.
- Update at milestones and before context rollover.
- On resume, read current source and the handoff before old transcripts.
