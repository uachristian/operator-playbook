# 09 — Efficiency

Spend fewer calls and less of the owner's time without lowering safety or accuracy. Safety and verified completion always come first.

## Before you look anything up

- Define the exact question and the evidence that would answer it.
- Batch independent reads into one step. Serialize only real dependencies and approval gates.
- Stop when the question is answered. Do not widen a narrow check into an investigation.

## Choosing the tool

- Single lookup: direct tool call.
- Three or more calls with filtering, branching, or aggregation: a script that does the mechanical work and returns only the result.
- Substantial independent reasoning: delegate early with a bounded packet.
- Parallelize only work that is independent and rate-safe.

## Output size

- Return focused evidence: identifiers, relevant context, errors, completeness flags, continuation paths.
- Do not hide missing results or truncation to save space.
- Do not over-shrink and then repeat the lookup.

## Reuse

- Reuse verified results within the same scope until freshness or a new decision requires a recheck.
- Search existing docs, issues, and skills before running a new experiment or writing a diagnostic tool.

## Missions

- One owning session and one handoff per active mission. Check ownership before resuming or editing shared artifacts.
- Continue already-approved scope to completion or a specific blocker instead of asking for another generic go.
- Identify the real finish line early: installation, activation, rollback, and the owner-visible acceptance step.
- At major context compaction or repeated same-cause failures, write an exact handoff and start a fresh session.

## Builds

- Optimize for verified quality per useful call, not total calls or diff size.
- Default cycle for big work: one implementation pass, one adversarial review, one remediation pass, one final review. Extra cycles need a concrete reason.
- Give reviewers a frozen candidate, one subsystem, one question, and bounded commands. Do not run review swarms after you have enough evidence to decide.
- Do lightweight independent work during long builds, backups, or installs.

## What not to change for speed

Do not silently change models, reasoning levels, context compression, retention, streaming, paid tiers, or profile boundaries as a speed tactic. Do not remove required gates. Never claim a speedup without a measured baseline.

## Prompt stability

Keep stable instruction prefixes stable. Do not rewrite persona or rules mid-conversation; many harnesses cache the prompt prefix, and changing it raises cost on every call.
