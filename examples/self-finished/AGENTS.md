# AGENTS.md

This subtree stores the user's finalized and shareable presentation projects.

Before making changes under `examples/self-finished/`, the agent must:

1. Read the repository root `AGENTS.md`
2. Read `skills/ppt-master/SKILL.md`
3. Read [WORKFLOW.md](./WORKFLOW.md)
4. Read [PROJECT_INDEX.md](./PROJECT_INDEX.md)

## User-Specific Rules

- The user's fork remote is `luppiterw` -> `git@github.com:luppiterw/ppt-master.git`
- The existing archival branch is `self-finished-20260420`
- New work may continue on that branch or on a new branch named like `self-finished-YYYYMMDD`
- Keep in-progress work under `projects/`
- Once a presentation project is finished and worth preserving, move it from `projects/` to `examples/self-finished/`
- Do not keep finalized examples only in `projects/`, because `.gitignore` excludes `projects/*`
- Preserve the full finished project structure:
  - `design_spec.md`
  - `sources/`
  - `svg_output/`
  - `svg_final/`
  - `notes/`
  - `exports/`
  - `templates/` when style/template-specific work was used
- Prefer adding a short `README.md` inside each finished project directory
- If multiple style variants are generated from the same content, keep them as separate sibling projects

## Preferred Archival Pattern

- Use `examples/self-finished/` as the permanent, versioned archive area
- Add or update [PROJECT_INDEX.md](./PROJECT_INDEX.md) whenever a new finished project is archived
- If helper tooling was created to produce style variants or perform user-specific packaging, keep it versioned in the repository and mention it in the index

## Git Expectations

- Do not rewrite the user's history unless explicitly asked
- Prefer normal commits over amend/rebase
- Push archival branches to remote `luppiterw`
- After pushing, report:
  - branch name
  - commit SHA
  - push destination
  - PR URL if available

## Fast Path For Future Sessions

If the user asks for "continue my self-finished workflow" or similar, start from this sequence:

1. Inspect `examples/self-finished/PROJECT_INDEX.md`
2. Inspect `git branch --show-current` and `git remote -v`
3. If generating a new deck, work in `projects/` first
4. After export is complete, move the finished project into `examples/self-finished/`
5. Update the index and commit/push to `luppiterw`
