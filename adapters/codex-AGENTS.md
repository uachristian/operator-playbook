# AGENTS.md — adapter for Codex

Codex reads `AGENTS.md` files from the repository root and nested directories.

## Setup

1. Complete `../BOOTSTRAP.md` to produce your filled `AGENTS.md` from `../templates/AGENTS.md`.
2. Copy it to your repository root as `AGENTS.md`. Add short nested `AGENTS.md` files only for directories with different rules.
3. Add a "Persona" section at the top with the key rules from your filled `SOUL.md`: tool discipline, approval gates, evidence states, secrets policy.
4. Keep secrets in environment variables or a local `.env` excluded by `.gitignore`.

## Notes

- Use the strictest sandbox and approval mode that still lets the task run. Network and writes outside the workspace should require approval.
- Codex runs may be unattended; keep gated actions as proposals in files for the owner to approve.
- Use `../templates/build-contract.md` and `../templates/build-closeout.md` for substantial tasks.
