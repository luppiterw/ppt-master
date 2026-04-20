# Luppiterw Workflow

This document explains how to continue the user's personal PPT production workflow when there is no prior chat context.

For the repository-level summary of this personal workflow, also read [`USER_WORKFLOW.md`](../../USER_WORKFLOW.md).

## Goal

Keep finished, shareable PPT Master outputs in a versioned area that is safe to commit and push to the user's fork.

## Why This Exists

- `projects/*` is ignored by `.gitignore`
- finished projects should be preserved in git
- the user wants future AI sessions to quickly resume the same workflow

## Canonical Working Pattern

1. Generate or edit a deck in `projects/<project_name>`
2. Complete the normal PPT Master pipeline:
   - SVG generation
   - notes generation
   - `total_md_split.py`
   - `finalize_svg.py`
   - `svg_to_pptx.py -s final`
3. Verify exports exist in `exports/`
4. If the project is considered finished or worth sharing, move it to `examples/luppiterw/`
5. Update [PROJECT_INDEX.md](./PROJECT_INDEX.md)
6. Commit on the user's archival branch and push to remote `luppiterw`

## Branch And Remote Convention

- Preferred remote: `luppiterw`
- Preferred remote URL: `git@github.com:luppiterw/ppt-master.git`
- Existing archival branch: `luppiterw`
- Prefer continuing work on branch `luppiterw`

## Directory Convention

Use this structure:

- `examples/luppiterw/<finished-project>/`
- `examples/luppiterw/README.md`
- `examples/luppiterw/PROJECT_INDEX.md`
- `examples/luppiterw/AGENTS.md`

Each archived project should ideally contain:

- `README.md`
- `design_spec.md`
- `sources/`
- `svg_output/`
- `svg_final/`
- `notes/`
- `exports/`
- `templates/` if template-specific assets were part of the finished result

## Style Variant Convention

When the same content is exported in multiple styles:

- keep one project per style
- keep naming explicit enough to identify the style
- treat each finished style as a first-class example

Current examples of this pattern:

- base version
- McKinsey variant
- Anthropic variant
- Pixel Retro variant

## Existing Helper Tool

- [generate_style_variant.py](/D:/Projects/GithubProjects/ppt-master/generate_style_variant.py)

Purpose:

- clones an existing finished project
- rewrites its design spec
- recolors/restyles SVGs into a target style family
- helps produce multiple comparable variants from one source deck

## What Future AI Should Avoid

- Do not archive unfinished work into `examples/luppiterw/`
- Do not leave finished work only in `projects/`
- Do not delete the user's intermediate project attempts unless explicitly asked
- Do not force-push or rewrite archival history unless explicitly asked
- Do not assume all archived examples came from templates; some may be free-design outputs

## Minimal Resume Checklist

When starting without chat context, do this:

1. Read root `AGENTS.md`
2. Read `skills/ppt-master/SKILL.md`
3. Read this file
4. Read [PROJECT_INDEX.md](./PROJECT_INDEX.md)
5. Inspect `git status --short`
6. Inspect `git branch --show-current`
7. Inspect `git remote -v`
