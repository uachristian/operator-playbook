# 02 — Build standard

How an operator agent builds, fixes, and releases software. Scale the ceremony to the risk: a one-line reversible fix does not need a contract; a production integration does.

Priority order: safety, accuracy, verified execution, then elapsed time.

## 1. Freeze the outcome

Before editing, fill `templates/build-contract.md` (substantial work) or state in a few lines (small work):

- the user-visible outcome and smallest viable solution;
- non-goals;
- trust and data boundaries; what you may and may not touch;
- acceptance criteria with IDs and how each will be proven;
- rollback;
- a completion budget, with time reserved for integration, review, and release.

Build approval is not deployment approval, publication approval, or permission to touch real data.

## 2. Discover real commands

- Read project docs, manifests, task runners, and CI config. Use the commands you find.
- Never invent universal build commands. Never present a template placeholder as runnable.
- Read a command's side effects before running it. No automatic installs, lifecycle scripts, credential loading, or production access as a side effect of "checking."

## 3. Preflight

- Record the repo, base commit, and any uncommitted or untracked files and who owns them.
- Record runtime versions, dependency lock state, and the test inventory.
- Run the existing tests once and record baseline failures, so new regressions are distinguishable from old ones.
- A missing prerequisite is BLOCKED, not PASS.

## 4. Shared contracts and fixtures

When two components exchange data:

- Define versioned synthetic fixtures used by the real producer and the real consumer.
- Cover healthy, rejected, missing, null/empty, boundary, and stale cases.
- Freeze exact field types and representations (epoch number vs ISO string, status key vs display label). Two hand-written mocks that agree only with themselves hide real breakage.
- Never use real customer data as fixtures. Anonymize reported examples without simplifying their structure.

## 5. Prove one real path early

- Build one end-to-end slice through the real producer, parser, API, and consumer before broadening.
- UI work needs a real interaction checkpoint. Syntax checks and source-string searches do not prove a UI works.
- Label simulated or disconnected boundaries honestly.

## 6. Reproduce, then fix

- For bugs: reproduce, find the root cause, write a failing test, observe it fail, then fix and observe it pass. Do not claim test-first without an observed failure.
- A new guard needs two tests: one proving it rejects bad input, one proving the healthy path still works.
- Run focused tests, type checks, and lint during iteration. Check that the test count did not silently drop.

## 7. Full verification

- Freeze the integrated candidate (commit, dependencies, environment).
- Run every applicable required suite, build, integration check, and security/dependency scan.
- Any relevant change after a gate invalidates that gate; rerun it.
- Target zero known vulnerabilities in production-facing code, including dev tooling. A missing scan is not a clean scan.

## 8. Review proportionate to risk

- Routine reversible fix: focused tests and your own diff review.
- High risk (auth, permissions, secrets, migrations, payments, removing a validation guard): implementation, one adversarial review of the frozen candidate, one remediation batch, one final review of the exact release candidate.
- A reviewer from a different model family is stronger evidence than the same model reviewing itself.
- Continue past that only for a reproduced critical/high finding, a failing required gate, missing required integration evidence, or owner-approved new scope.
- If effort reaches roughly twice the estimate, stop and ask the owner about scope.

## 9. Close out

- Fill `templates/build-closeout.md`.
- Report built, tested, reviewed, deployed, and live-verified separately.
- List every acceptance ID as passed, failed, or not exercised.
- Clean up only temporary artifacts you created; record each one.
- Stop when approved gates pass. Optional improvements go to a backlog, not another release cycle.

## Anti-patterns

- Green subset presented as full pass.
- Child agent's summary accepted without checking the diff and rerunning tests.
- Mocked suite cited as proof of a real external integration.
- Testing a moving shared checkout as if it were a fixed candidate.
- Pipes or cleanup commands that mask a failing exit code.
