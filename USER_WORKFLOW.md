# User Workflow

This file records the repository owner's personal archival workflow for finished PPT Master outputs.

Use this file when the task is not just "generate a PPT", but specifically "continue luppiterw's local workflow", "archive finished work", or "push my finished examples to my fork".

## Purpose

- keep personal workflow guidance in one additive file
- help future AI sessions resume without prior chat context
- avoid unnecessary edits to upstream-facing project files
- preserve a clean path for future merges from `hugohe3/ppt-master`

## Fast Resume

When resuming the user's personal workflow, read these in order:

1. `AGENTS.md`
2. `skills/ppt-master/SKILL.md`
3. `USER_WORKFLOW.md`
4. `examples/luppiterw/AGENTS.md`
5. `examples/luppiterw/WORKFLOW.md`
6. `examples/luppiterw/PROJECT_INDEX.md`

Then inspect:

1. `git branch --show-current`
2. `git remote -v`
3. `git status --short`

## Canonical Personal Pattern

1. Do normal generation or editing work in `projects/<project_name>/`
2. Finish the standard PPT Master pipeline there
3. Verify the exported PPTX exists under `exports/`
4. If the result is worth preserving, move the whole finished project into `examples/luppiterw/`
5. Update `examples/luppiterw/PROJECT_INDEX.md`
6. Commit on branch `luppiterw`
7. Push to remote `luppiterw`

## Git And Archive Conventions

- preferred branch: `luppiterw`
- preferred remote: `luppiterw`
- preferred remote URL: `git@github.com:luppiterw/ppt-master.git`
- finished, shareable outputs belong in `examples/luppiterw/`
- in-progress work belongs in `projects/`
- `projects/*` is ignored by `.gitignore`, so finished work must not stay there only

## Merge-Friendly Rules

To reduce conflict risk when syncing from upstream:

- prefer adding new files over rewriting upstream files
- keep user-specific workflow docs in `USER_WORKFLOW.md` and `examples/luppiterw/`
- avoid editing root `README.md`, `README_CN.md`, and other upstream-facing docs unless the user explicitly asks
- keep user-specific archive logic out of core scripts unless the user explicitly asks
- treat `examples/luppiterw/` as the main personal extension area

## What Future AI Should Do

- use repository workflow rules first
- use this file only for user-specific continuation rules
- preserve existing archived projects
- keep style variants as separate sibling projects
- report branch, commit SHA, and push target after archival work

## What Future AI Should Avoid

- do not archive unfinished work into `examples/luppiterw/`
- do not leave finished work only in `projects/`
- do not rewrite branch history unless the user explicitly asks
- do not move personal workflow guidance into many scattered root files
- do not assume upstream repository maintainers want personal archive rules mixed into general docs
