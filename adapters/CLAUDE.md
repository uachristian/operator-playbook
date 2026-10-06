# CLAUDE.md — adapter for Claude Code

Claude Code loads `CLAUDE.md` from the project root (and a user-level copy) at session start.

## Setup

1. Complete `../BOOTSTRAP.md` to produce your filled `AGENTS.md` from `../templates/AGENTS.md`.
2. In your project root, create `CLAUDE.md` containing either:
   - the full text of your filled `AGENTS.md`, or
   - one line importing it: `@AGENTS.md` (Claude Code supports `@path` imports).
3. Put persona-level rules from your filled `SOUL.md` into the user-level `CLAUDE.md` so they apply across projects.
4. Store secrets in your shell environment or a local `.env` excluded by `.gitignore`. Never in `CLAUDE.md`.

## Notes

- Configure tool permissions so writes, network calls, and shell commands that touch production require approval.
- Use subagents per `../docs/06-delegation-and-parallel-work.md`.
- Keep `CLAUDE.md` stable within a session; edits take effect next session.
