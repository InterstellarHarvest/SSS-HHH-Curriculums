# Repository Agent Instructions

## Scope and authority

These instructions govern agent-assisted work in the `SSS-HHH-Curriculums` repository.

They apply to:

- Codex
- Claude
- ChatGPT-directed implementation agents
- other automated coding assistants
- human-directed agent workflows

Project-specific curriculum and visual standards remain authoritative within their own scope. This file governs repository work practices, validation discipline, release protection, and implementation behavior.

## Frozen release protection

Approved and released curriculum work must be treated as frozen unless the owner explicitly reopens it.

For a frozen release:

- do not revise curriculum content merely because a tooling or unrelated shared-system change is being made;
- do not regenerate, rewrite, normalize, or reformat frozen case sources without explicit authorization;
- do not alter approved lifecycle records, release records, case-package versions, or accepted baselines unless the task specifically requires it;
- absence of changes to frozen curriculum files is itself important regression evidence;
- tooling work does not reopen a frozen curriculum release.

SSS is a regression baseline once marked complete and `APPROVED_STABLE`.

The same rule applies to HHH cases as they become approved and frozen.

## Branch and worktree discipline

For nontrivial implementation work:

- begin from the exact authorized baseline;
- use an isolated feature branch or worktree when practical;
- do not mix unrelated changes;
- do not amend, squash, rebase, force-push, or rewrite approved history unless explicitly authorized;
- preserve a clean and attributable diff;
- report the starting SHA, branch, changed files, validation performed, and final commit SHA.

Do not modify `main` directly unless the owner explicitly authorizes it.

## Proportional Validation and Runtime Discipline

### Core rule

Validation must be proportional to the files and systems changed.

Do not run the repository's most expensive full-system, mutation, historical-release, or all-case validation suites merely because they exist.

The purpose of validation is to establish confidence in the affected system, not to maximize the number of checks executed.

### Change classification

Before running validation, classify the diff.

#### Tooling-only changes

Examples:

- `apps/curriculum-editor/**`
- launchers
- local development servers
- editor chrome
- editor-only tests
- developer documentation
- tooling scripts that do not alter canonical curriculum output

For tooling-only changes:

1. run focused unit/integration tests for the changed tooling;
2. run the editor/browser regression suite if editor behavior changed;
3. run narrowly relevant shared contracts where the tooling interfaces with them;
4. verify the diff contains no curriculum-package changes;
5. run `git diff --check`.

Do **not** run full all-case curriculum mutation suites, exhaustive release reconstruction, or multi-hour static validation unless the changed tooling can alter canonical curriculum output and narrower tests cannot establish safety.

#### Shared rendering or production-system changes

If shared code can alter rendered Student, Teacher, Answer Key, or Accessible curriculum output:

- run affected shared-system tests;
- run representative cases covering the changed behavior;
- expand to all cases only when the change genuinely has repo-wide output impact or representative testing exposes uncertainty.

#### Case-specific curriculum changes

Run:

- that case's required validation;
- directly relevant shared validators;
- targeted regression against preserved cases when a modified shared dependency can affect them.

Do not automatically rerun unrelated campaigns.

#### Release-wide or governing-system changes

Full-system validation is appropriate when the change actually modifies:

- canonical shared curriculum architecture;
- package schema;
- universal rendering behavior;
- release-integrity logic;
- shared source generation;
- governing validation behavior;
- every case or a substantial cross-case dependency.

### Expensive validators

Any validator known to take tens of minutes or hours must not be run automatically unless:

1. its coverage is materially relevant to the diff;
2. a faster targeted validator cannot establish the same confidence;
3. the expected value justifies the runtime.

Mutation suites that intentionally rewrite cases and rerun full validators are **special-purpose release-validation tools**, not routine post-change checks.

Do not run them for unrelated tooling-only changes.

### Runtime discipline

Before starting a potentially long validation command:

- inspect what it runs;
- determine whether it recursively invokes case validators or mutation suites;
- prefer a targeted subcommand or constituent test when available.

If a validation path unexpectedly becomes long-running, stop and reassess rather than allowing it to continue solely because it was started.

Do not spend hours proving that untouched frozen curriculum files remain untouched when Git diff scope plus appropriate regression tests already establish that fact.

### Frozen release baseline

Once SSS is `APPROVED_STABLE` and frozen:

- untouched SSS curriculum files are regression baselines;
- tooling work does not reopen SSS;
- absence of SSS source changes is important evidence;
- SSS-wide validation is required only when changed shared behavior could actually affect SSS output.

The same principle applies to HHH once portions of it become frozen.

### Reporting

Report:

- diff scope;
- validation chosen;
- why those checks were sufficient;
- any intentionally omitted expensive suites and why they were not relevant.

Do not describe an irrelevant unrun mega-suite as a validation deficiency.

Prefer:

**small relevant test set + clear reasoning**

over:

**largest possible test set + excessive runtime**.

## Mutation-suite restrictions

Mutation suites are not routine checks.

Do not run a mutation suite unless the current task changes:

- validation logic the mutation suite is intended to test;
- release-integrity behavior;
- shared curriculum architecture materially exercised by the mutation suite;
- or another system where the mutation coverage is directly necessary.

If a mutation suite temporarily rewrites repository files, run it only in an isolated and controlled context.

Never run other validators concurrently against files while a mutation suite is intentionally changing them.

Restore and verify repository state before continuing.

## Generated artifact policy

Generated editable copies, role HTML, routine screenshots, temporary validation output, and PDFs are not canonical curriculum artifacts unless a governing project rule explicitly says otherwise.

Do not commit generated outputs merely because validation or review created them.

Canonical curriculum production remains package-source based.

## Tooling and editor changes

Changes to the Curriculum Editor, launcher, local server, editor tests, or developer workflow are tooling changes unless they alter canonical curriculum output.

For tooling-only work:

- keep curriculum case packages untouched;
- preserve existing authoring and rendering contracts;
- test the changed tooling directly;
- avoid reopening frozen curriculum releases;
- prefer targeted lifecycle, authoring, browser, and interface tests over all-case curriculum validation.

## Validation concurrency

Do not run validators concurrently when either validator:

- mutates repository files;
- uses shared temporary paths;
- rewrites fixtures in place;
- depends on a pristine working tree;
- or can observe another validator's transient state.

When in doubt, run validation serially.

## Commit and integration discipline

Before committing:

- confirm the diff is limited to intended files;
- run `git diff --check`;
- verify no temporary output or machine-local path has been introduced;
- verify frozen case sources remain untouched when the task does not authorize changes to them.

Before integration:

- report the exact commit being proposed;
- report validation results;
- identify any known caveat that materially affects confidence;
- do not merge or push to `main` unless authorized.

## Reporting requirements

A completion report should be concise and decision-useful.

Include:

- starting SHA;
- branch/worktree;
- files changed;
- what behavior changed;
- validation actually run;
- relevant pass/fail counts;
- `git diff --check` result;
- final commit SHA;
- whether the change is pushed, merged, held, or awaiting owner review.

Do not inflate reports with irrelevant validator output.

Do not present hours of unnecessary validation as evidence of quality when a smaller relevant test set would have established the same confidence.
