# Luppiterw Project Index

This index records the user's archived, versioned PPT Master outputs under `examples/luppiterw/`.

## Current Archive

### 1. Base Overview Deck

- Project: `docs_overview_ppt169_20260420`
- Type: free-design base version
- Source set:
  - `docs/why-ppt-master.md`
  - `docs/technical-design.md`
  - `docs/faq.md`
  - `docs/windows-installation.md`
- Output summary:
  - 13 pages
  - editable native PPTX
  - SVG backup PPTX

### 2. McKinsey Variant

- Project: `docs_overview_ppt169_mckinsey_20260420_2`
- Type: style variant
- Source deck: `docs_overview_ppt169_20260420`
- Style family: `mckinsey`

### 3. Anthropic Variant

- Project: `docs_overview_ppt169_anthropic_20260420_2`
- Type: style variant
- Source deck: `docs_overview_ppt169_20260420`
- Style family: `anthropic`

### 4. Pixel Retro Variant

- Project: `docs_overview_ppt169_pixel_retro_20260420`
- Type: style variant
- Source deck: `docs_overview_ppt169_20260420`
- Style family: `pixel_retro`

## Current User Preferences Captured In This Archive

- finished projects should be moved from `projects/` to `examples/luppiterw/`
- style variants should be preserved as separate projects
- archival work should be committed on branch `luppiterw` and pushed to the user's fork
- future AI sessions should be able to resume from repository-local documentation without prior chat context

## Maintenance Rule

When a new finished project is archived:

1. add a new entry here
2. append it at the end of `## Current Archive`
3. use one of the fixed templates below
4. keep the numbered heading continuous
5. mention whether it is a base deck or a style variant
6. mention the source material or source deck
7. mention the style family if applicable

## Fixed Entry Templates

Copy one of the following blocks and replace the placeholders directly.

### Template A. Base Deck

```md
### <N>. <Short Display Name>

- Project: `<project_directory_name>`
- Type: base deck
- Source set:
  - `<source_file_or_url_1>`
  - `<source_file_or_url_2>`
- Output summary:
  - `<page_count> pages`
  - editable native PPTX
  - SVG backup PPTX
```

### Template B. Style Variant

```md
### <N>. <Short Display Name>

- Project: `<project_directory_name>`
- Type: style variant
- Source deck: `<base_project_directory_name>`
- Style family: `<style_family>`
- Output summary:
  - `<page_count> pages`
  - editable native PPTX
  - SVG backup PPTX
```

### Template Notes

- For base decks, keep `Source set` as the original source files or URLs actually used.
- For style variants, use `Source deck` to point back to the archived base project.
- If page count is not yet confirmed, replace `<page_count>` before committing instead of leaving the placeholder.
- Keep labels and field order unchanged so future AI can continue appending entries in the same format.
