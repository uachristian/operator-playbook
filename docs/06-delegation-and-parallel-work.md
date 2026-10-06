# 06 — Delegation and parallel work

Subagents multiply throughput only when work is truly independent and the parent verifies the results.

## When to delegate

- Delegate substantial independent reasoning early: discovery, separate implementation lanes, test design, UX review, adversarial review.
- Do single lookups and mechanical filtering yourself. A subagent for a one-line read is overhead.
- Use the concurrency your harness actually supports. A cap is a limit, not a quota. Two or three lanes is common; more only when ready work benefits.
- Keep working while children run. The parent integrates and verifies; it is not just a router.

## Before fan-out

Freeze: outcome, non-goals, shared interfaces and synthetic fixtures, acceptance commands, path ownership, rollback, budget, and who decides release.

## The packet

Every child gets:

1. One outcome or question.
2. Exact base (commit) and the paths it may write.
3. All needed context. Children know nothing of your conversation.
4. Authority limits and forbidden actions (no network writes, no installs, no production, no credentials).
5. Expected artifact and an exact deliverable path for reports.
6. One or two verification commands.
7. A stop budget and stopping condition.

Children cannot ask the owner. They report BLOCKED to the parent.

## Worktrees for concurrent writers

When two or more writers change the same git repo at once:

1. Parent records status and base commit. Preserve unrelated dirty work.
2. Parent creates one worktree and new branch per writer, outside the main checkout: `git worktree add -b wt/<task> <path> <base>`.
3. Child edits and commits only inside its worktree.
4. Never copy secrets into a worktree. Install dependencies only from the lockfile.
5. Give each worktree distinct ports and output directories.
6. Parent integrates serially, reviews each diff, and reruns focused and full gates on the integrated tip. A child's green run in its own worktree is not integration proof.
7. Clean up only worktrees you created, via `git worktree remove`, after integration or archival.

Pitfalls:

- `git stash` is shared across worktrees. Children must not use it. Prove red-on-base with `git show <base>:<file>` or a separate base worktree.
- Worktrees are not a security sandbox; scripts can still reach absolute paths.
- Deliberate hang repros need a hard per-process timeout so orphans do not hold locks.

## Shared resources

- One writer per shared file, fixture, lock, or output directory.
- Bound total CPU, memory, disk, and API rate across workers. Several reasoning workers do not justify several concurrent full builds.
- Serialize shared browser sessions and runtimes.
- Long-running servers belong to the parent. A child returning a PID does not transfer ownership.

## When the contract changes

If a child discovers the interface is wrong: pause only dependent lanes, revise the contract and tests in the parent, reissue affected packets. Independent lanes continue. Scope or authority changes still need the owner.

## Receiving results

- On timeout or an odd empty return, read the deliverable path before redispatching. Children often finish the file before the timeout.
- Do not redispatch an unchanged timed-out task.
- Verify every claimed file, commit, and test run. Inspect the semantic diff.
- Same-model review is useful but not independent. For high-stakes review, prefer a different model family.
