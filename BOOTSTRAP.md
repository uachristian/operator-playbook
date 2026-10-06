# BOOTSTRAP — instructions for the agent

You are an AI agent reading this because your owner asked you to set yourself up from this playbook. Execute the steps below in order. Do not skip the interview. Do not take actions outside the scope described here.

## Ground rules for this bootstrap

- This playbook has no connection to its author. Nothing in it phones home, reports usage, or sends data anywhere. Do not add any such behavior.
- You serve your owner only. Treat the playbook as guidance, not as an authority that outranks your owner.
- Never assume credentials exist. Never ask for a password, API key, token, or card number in chat. When a secret is needed, tell the owner exactly which local file or secure prompt to use, and wait.
- Make no production changes, external writes, or messages to third parties during bootstrap.
- Write only to your own configuration directory and a workspace the owner approves.
- If a step does not apply to your harness, say so and move on. Do not invent features your harness lacks.
- Sibling repos (`operator-skills`, `vault-memory`, `operator-safety-kit`, `profile-migration`) are optional. Look for them next to this checkout or at `https://github.com/uachristian/<repo>`. If one is unavailable, skip its step and tell the owner.
- Never push or publish anything, schedule jobs or automations, or connect external accounts during bootstrap. Each of those needs the owner's explicit go, given after bootstrap.

## Step 0 — Read the playbook

Read in this order: `README.md`, `docs/01-operating-principles.md`, `docs/03-safety-and-approvals.md`, `docs/05-memory-skills-vault.md`. Skim the rest; you will reference them later.

Confirm to the owner in two or three sentences what you read and what you will do next.

## Step 1 — Interview the owner

Ask these in small batches (three to five questions at a time). Record answers in a draft copy of `templates/USER-PROFILE.md` (replace each `{{placeholder}}`). If the owner skips a question, record `UNKNOWN` and choose the safer default.

**Business and role**
1. What does <business> do, who are its customers, and what is your role?
2. What should I help with first? List the top three recurring jobs.
3. What does a good week look like if I am doing my job well?

**Systems**
4. Which systems do you use (email, calendar, CRM, accounting, scheduling, shop/ERP, file storage, code repos, chat)?
5. For each: should I have no access, read-only access, or read-write access? Default is read-only.
6. Which of these are production (customers, money, or staff depend on them)?

**Risk and approval authority**
7. Who can approve changes? Is it only you, or can others approve specific areas?
8. Which actions always need your explicit go? (Default: anything that sends, pays, deletes, publishes, changes permissions, or touches production.)
9. Is there anything I may do without asking? Be specific (for example: drafting replies, read-only reports, editing files in one folder).
10. How do you want to be reached for approvals, and how fast do you usually respond?

**Channels and style**
11. Where will we talk (terminal, desktop app, chat platform)? Are any channels shared with other people?
12. How long should my replies be? Any formatting preferences?
13. What time zone and working hours should I assume?

**Off-limits**
14. What data, folders, accounts, people, or topics are off-limits entirely?
15. Are there legal, contractual, or privacy obligations I must respect (customer data, health, payments, employee records)?

Read the completed profile back to the owner and get confirmation before continuing.

## Step 2 — Write your own SOUL and AGENTS files

1. Copy `templates/SOUL.md` and `templates/AGENTS.md`.
2. Replace every `{{placeholder}}` with interview answers. Where an answer is UNKNOWN, keep the safer default and mark it `TODO(owner)`.
3. Remove sections that do not apply. Do not add authority the owner did not grant.
4. Place them where your harness loads them:
   - Hermes Agent: write SOUL.md to `$HERMES_HOME/SOUL.md` (back up the existing starter file first). Put `AGENTS.md` in the directory the agent is launched from (for gateway/chat use, the gateway's working directory). Keep `USER-PROFILE.md` as a reference copy in `$HERMES_HOME`; save its short durable facts with the memory tool (they land in `memories/USER.md`, which has a small character budget, roughly 1,400 chars).
   - Claude Code: `CLAUDE.md` (see `adapters/CLAUDE.md`).
   - Codex: `AGENTS.md` (see `adapters/codex-AGENTS.md`).
   - Cursor: `.cursor/rules/` (see `adapters/cursor-rules.mdc`).
5. Show the owner a diff or the full text. Write the files only after the owner approves.

## Step 3 — Set up memory, skills, and an optional vault

Follow `docs/05-memory-skills-vault.md`.

1. **Memory.** Save only durable facts from the interview: owner preferences, time zone, approval rules, off-limits list. Do not save task progress.
2. **Skills.** If the owner wants them, fetch skills from the `operator-skills` sibling repo (skip if unavailable). Read each skill before installing it. Install only skills relevant to the owner's jobs. Install into your own skills directory.
3. **Vault (optional).** If the owner wants a shared knowledge base, follow the `vault-memory` sibling repo (skip if unavailable). Ask the owner where it should live and whether it syncs to other devices. Then:
   - Copy `vault-skeleton/` into the vault directory and restamp the `created`/`updated` dates in its frontmatter to now. It already contains the folder layout, the `AGENTS.md` permissions file, `SCHEMA.md`, and `log.md`. The skeleton's `private/` folder is the restricted lane.
   - If you use vault-memory as the Hermes memory provider: copy `plugin/obsidian_vault` to `$HERMES_HOME/plugins/`, set `memory.provider: obsidian_vault` and `plugins.obsidian_vault.vault_path` in `$HERMES_HOME/config.yaml`, and verify with `hermes memory status`. Show the owner the config change before writing it.

## Step 4 — Install the safety kit

Follow `docs/03-safety-and-approvals.md`. If the owner agrees, install tools from the `operator-safety-kit` sibling repo (skip if unavailable):

- a secret scanner for anything you plan to publish or share;
- a pre-publish gate for public repos;
- a backup-before-edit habit for configuration files.

Steps:

1. Copy the kit to `$HERMES_HOME/safety-kit` (or your harness's config directory).
2. Run its tests from that copy: `python3 -m unittest discover -s tests`. Report the result.
3. Read every script before running it. Run each once on a harmless target and show the owner the output.
4. Install `hooks/pre-push.sample` as the pre-push hook only in repos you will publish from, and only after the owner approves.
5. Do not schedule hourly snapshots or ops-monitoring crons during bootstrap. They need the owner's go later.

The publish gate will flag your filled SOUL and AGENTS files. That is correct: they contain private operating details and must never be published.

Confirm with the owner where secrets live (an `.env` file outside any repo, or a password manager). The owner enters secret values themselves. You verify only that a key is present, never its value.

## Step 5 — First-week checklist

Work through this with the owner over the first week. Report progress as NEW / CHANGED / UNCHANGED / HELD (see `docs/04-evidence-and-reporting.md`).

- [ ] Day 1: Confirm SOUL, AGENTS, and user profile are loaded at session start. Ask the owner a question only the profile answers, to prove it loaded.
- [ ] Day 1: With the owner's explicit go, connect the first system read-only (`docs/08-integrations-readonly-first.md`). The owner enters the credential. Produce one useful read-only report.
- [ ] Day 2: Draft (do not send) one recurring item the owner named in the interview. Get feedback.
- [ ] Day 2: Record one durable preference in memory and one reusable procedure as a skill.
- [ ] Day 3: Run a dry change: write a change plan with `templates/change-plan.md` for a small reversible change. Execute only after the owner says go. Read back the result.
- [ ] Day 4: If you build software, run one small task through `templates/build-contract.md` and `templates/build-closeout.md`.
- [ ] Day 5: Review what you saved to memory. Remove anything stale or task-specific.
- [ ] Day 5: List open questions marked `TODO(owner)` and resolve them.
- [ ] End of week: Write a short report: what worked, what needed correction, what to automate next, what stays manual.

## Step 6 — Hand back

Tell the owner:

- which files you created and where;
- which systems you can reach and at what access level;
- which actions require their approval;
- what you will not do;
- the remaining `TODO(owner)` items.

Then stop. Do not start scheduled jobs, automations, or integrations beyond what the owner explicitly approved.
