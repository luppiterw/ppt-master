# docs_overview_ppt169_anthropic_20260420_2 - Design Spec

> This document is the unified handoff artifact for the Anthropic Style variant. It keeps the same narrative and slide outline while switching the visual system to the selected template family.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | docs_overview_ppt169_anthropic_20260420_2 |
| **Canvas Format** | PPT 16:9 (1280x720) |
| **Page Count** | 13 |
| **Design Style** | Anthropic-style AI product deck |
| **Target Audience** | Developers, AI IDE users, open-source adopters, technical teams, internal demo viewers |
| **Use Case** | Product introduction, technical overview, community sharing, internal onboarding |
| **Created Date** | 2026-04-20 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280x720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 60px, top 50px, bottom 40px |
| **Content Area** | 1160x590 inside the safe area |

---

## III. Visual Theme

### Theme Style

- **Style**: Anthropic Style
- **Theme**: Mixed theme
- **Tone**: consistent with the repository template family `anthropic`

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | Main page background |
| **Secondary bg** | `#F8FAFC` | Cards, panels, quiet surfaces |
| **Primary** | `#D97757` | Titles, key accents, structural highlights |
| **Accent** | `#4A90D9` | Connectors, secondary emphasis |
| **Secondary accent** | `#10B981` | Callouts, alternative emphasis |
| **Body text** | `#1A1A2E` | Primary text |
| **Secondary text** | `#64748B` | Supporting copy |
| **Tertiary text** | `#94A3B8` | Footers and low-priority notes |
| **Border/divider** | `#E2E8F0` | Borders and separators |
| **Success** | `#10B981` | Positive states |
| **Warning** | `#EF4444` | Risks, cautions, issue markers |

---

## IV. Typography System

### Font Plan

| Role | Font |
| ---- | ---- |
| **Title** | `Arial, "Helvetica Neue", "Segoe UI", sans-serif` |
| **Body** | `Arial, "Helvetica Neue", "Segoe UI", sans-serif` |
| **Code** | `"Consolas", "Monaco", monospace` |
| **Emphasis** | `Arial, "Helvetica Neue", "Segoe UI", sans-serif` |

### Font Size Hierarchy

| Purpose | Suggested Size | Weight |
| ------- | -------------- | ------ |
| Cover title | 52-56px | Bold |
| Content title | 32-36px | Bold |
| Card title | 20-24px | Bold |
| Body content | 16-18px | Regular |
| Annotation | 12-14px | Regular |
| Page number/date | 12-14px | Regular |

---

## V. Layout Principles


### Page Structure

- **Header area**: 84-104px high; contains page title, section label, and optional small metadata
- **Content area**: 520-560px high; main cards, diagrams, lists, and comparison modules
- **Footer area**: 28-36px high; page index, project name, or short source note

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | Cover, conclusion, key takeaway pages |
| **Left-right split (5:5)** | Comparisons, promise vs limitation |
| **Left-right split (4:6)** | Architecture and explanation pages |
| **Top-bottom split** | Pipeline plus notes, setup plus command validation |
| **Three/four column cards** | Value propositions, feature lists |
| **Matrix grid** | FAQ grouping and decision framing |

### Spacing Specification

| Element | Recommended Range | Current Project |
| ------- | ---------------- | --------------- |
| Card gap | 20-32px | 24px |
| Content block gap | 24-40px | 28px |
| Card padding | 20-32px | 24px |
| Card border radius | 8-16px | 14px |
| Icon-text gap | 8-16px | 12px |
| Single-row card height | 530-600px | 548px |
| Double-row card height | 265-295px each | 272px |
| Three-column card width | 360-380px each | 368px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/chunk/`
- **Usage method**: Placeholder format `{{icon:chunk/icon-name}}`
- **Locked library**: `chunk`

### Recommended Icon List (fill as needed)

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Product promise | `{{icon:chunk/rocket}}` | Slide 01 |
| Editable output | `{{icon:chunk/layers}}` | Slide 02 |
| Comparison/chart cue | `{{icon:chunk/chart-bar}}` | Slide 03 |
| Cost value | `{{icon:chunk/dollar}}` | Slide 04 |
| Privacy/local | `{{icon:chunk/shield-check}}` | Slide 04 |
| Open workflow | `{{icon:chunk/plug}}` | Slide 04 |
| Pipeline/system | `{{icon:chunk/code}}` | Slide 05 |
| Source formats | `{{icon:chunk/folder-open}}` | Slide 09 |
| Validation/setup success | `{{icon:chunk/circle-checkmark}}` | Slide 11 |
| Windows environment | `{{icon:chunk/window}}` | Slide 11 |
| User workflow | `{{icon:chunk/user}}` | Slide 12 |
| Team or audience | `{{icon:chunk/users}}` | Slide 13 |

---

## VII. Visualization Reference List (if needed)

| Visualization Type | Reference Template | Used In |
| ------------------ | ------------------ | ------- |
| process_flow | `templates/charts/process_flow.svg` | Slide 05 |
| numbered_steps | `templates/charts/numbered_steps.svg` | Slide 06, Slide 11 |
| comparison_table | `templates/charts/comparison_table.svg` | Slide 07, Slide 09 |
| comparison_columns | `templates/charts/comparison_columns.svg` | Slide 03 |
| icon_grid | `templates/charts/icon_grid.svg` | Slide 04 |
| vertical_list | `templates/charts/vertical_list.svg` | Slide 02, Slide 08, Slide 10, Slide 12 |
| chevron_process | `templates/charts/chevron_process.svg` | Slide 12 |
| pros_cons_chart | `templates/charts/pros_cons_chart.svg` | Slide 13 |

---

## VIII. Image Resource List (if needed)

| Filename | Dimensions | Ratio | Purpose | Type | Status | Generation Description |
| -------- | --------- | ----- | ------- | ---- | ------ | --------------------- |
| N/A | N/A | N/A | No external images are required for this deck | Decorative | Not used | Use abstract geometric backgrounds, iconography, and native SVG diagrams only |

**Status descriptions**:

- **Pending** - Needs AI generation, provide detailed description
- **Existing** - User already has image, place in `images/`
- **Placeholder** - Not yet processed, use dashed border placeholder in SVG

---

## IX. Content Outline

### Part 1: Product Positioning

#### Slide 01 - Cover

- **Layout**: Single column centered with large title and geometric background
- **Title**: PPT Master
- **Subtitle**: Product, Architecture, and Setup Overview
- **Info**: docs synthesis deck | generated from project documentation | 2026-04-20

#### Slide 02 - The Core Claim

- **Layout**: Left-right split (4:6)
- **Title**: A real PowerPoint workflow, not a screenshot export
- **Visualization**: vertical_list
- **Content**:
  - The product promise is native editable PPTX, not flattened images or browser captures
  - Every shape, text block, gradient, and shadow is intended to remain clickable and editable
  - The value proposition is reducing blank-page work while preserving final-mile editing in PowerPoint

#### Slide 03 - Why Existing AI PPT Paths Break Down

- **Layout**: Comparison columns
- **Title**: Four approaches, four different trade-offs
- **Visualization**: comparison_columns
- **Content**:
  - Image embedding looks polished but kills editability
  - HTML/CSS exports render well on the web but do not map cleanly to slide canvas semantics
  - Direct python-pptx generation keeps objects editable but usually produces weak visual design
  - PPT Master positions SVG-to-DrawingML as the middle path between design quality and editability

#### Slide 04 - Why PPT Master Is Different

- **Layout**: Four-card grid
- **Title**: The framework is optimized for usable output
- **Visualization**: icon_grid
- **Content**:
  - Real PowerPoint output with native shapes
  - Predictable cost with no SaaS subscription dependency
  - Local-first handling of files and exports
  - No lock-in on editors or models

### Part 2: Architecture and Technical Logic

#### Slide 05 - End-to-End System Architecture

- **Layout**: Wide process page
- **Title**: The workflow is a serial design-to-engineering pipeline
- **Visualization**: process_flow
- **Content**:
  - Source documents are normalized into structured text
  - Strategist defines the slide plan and design specification
  - Executor generates SVG pages and notes
  - Post-processing and export convert the SVG set into editable DrawingML PPTX

#### Slide 06 - The Three Technical Stages

- **Layout**: Top-bottom split
- **Title**: Understand, generate, convert
- **Visualization**: numbered_steps
- **Content**:
  - Stage 1: content understanding and design planning
  - Stage 2: AI visual generation in SVG
  - Stage 3: engineering conversion into native PowerPoint objects

#### Slide 07 - Why SVG Wins

- **Layout**: Comparison table with explanation panel
- **Title**: SVG is the practical bridge format
- **Visualization**: comparison_table
- **Content**:
  - DrawingML is too verbose for reliable direct AI authoring
  - HTML/CSS describes document flow, not independent slide objects
  - WMF/EMF lacks useful model training support
  - SVG shares the same absolute-coordinate worldview as DrawingML and keeps conversion understandable

#### Slide 08 - Design Philosophy and Honest Limits

- **Layout**: Left-right split (5:5)
- **Title**: AI is the designer, not the finisher
- **Visualization**: vertical_list
- **Content**:
  - The generated deck is a design draft and starting point, not a fully polished final artifact
  - Good output still depends on human taste, judgment, and finishing work
  - The system prioritizes removing 90 percent of layout labor, not replacing final editorial control
  - Setup cost and slower serial generation are accepted trade-offs for editability and quality

### Part 3: FAQ and Practical Use

#### Slide 09 - FAQ Snapshot

- **Layout**: Matrix grid
- **Title**: What users usually ask first
- **Visualization**: comparison_table
- **Content**:
  - Input coverage: PDF, DOCX, PPTX, EPUB, HTML, LaTeX, RST, URLs, Markdown, plain text
  - Output coverage: standard PPT plus multiple non-standard canvases
  - Editability: native `.pptx` plus `_svg.pptx` backup
  - Charts: visually editable shapes, but not Excel-bound chart objects

#### Slide 10 - Quality Expectations and Model Choice

- **Layout**: Left-right split (4:6)
- **Title**: Output quality depends on both the model and the review loop
- **Visualization**: vertical_list
- **Content**:
  - Claude is positioned as the most reliable model for layout-heavy SVG generation
  - Overflow and alignment issues are framed as model capability limits more than script bugs
  - Users are expected to review, regenerate specific pages, and fix coordinates when needed
  - Serial generation is intentional because parallel generation reduced cross-slide consistency

### Part 4: Windows Setup and Onboarding

#### Slide 11 - Windows Quick Start

- **Layout**: Full-width numbered steps
- **Title**: The minimum Windows setup path
- **Visualization**: numbered_steps
- **Content**:
  - Install Python 3.10+ and add it to PATH
  - Download or clone the repository
  - Install dependencies from `requirements.txt`
  - Verify core imports and run a minimal sample deck

#### Slide 12 - Troubleshooting and First-Run Workflow

- **Layout**: Wide process with side notes
- **Title**: Most setup problems are environment-path issues, not product logic issues
- **Visualization**: chevron_process
- **Content**:
  - Common failure modes include missing PATH entries, mismatched pip targets, blocked PowerShell scripts, and network-limited installs
  - The recommended first-run path is verify Python, install dependencies, test imports, then run a tiny deck
  - Optional enhancements like CairoSVG, Node.js fallback, and Pandoc are edge-case extras, not hard requirements

### Part 5: Closing

#### Slide 13 - Who Should Use It

- **Layout**: Left-right split (5:5)
- **Title**: Choose PPT Master when editability matters more than instant browser output
- **Visualization**: pros_cons_chart
- **Content**:
  - Best fit: users who want native editability, local workflows, transparent cost, and model/editor flexibility
  - Not the right fit: users who want instant browser UI, zero setup, collaborative canvases, or data-bound spreadsheet charts
  - Closing message: PPT Master is a serious engineering workflow for serious slide users

---

## X. Speaker Notes Requirements

Generate corresponding speaker note files for each page, saved to the `notes/` directory:

- **File naming**: Match SVG names, e.g. `slide_01_cover.md`
- **Presentation duration**: 12-15 minutes
- **Notes style**: concise, presenter-friendly, explanatory, no marketing fluff
- **Presentation purpose**: inform and persuade
- **Content includes**: main talking point, transition sentence, and one short interpretation layer beyond visible bullets
- **Master notes file**: `notes/total.md` uses `#` headings matching slide filenames
- **Split note files**: per-slide markdown files must not contain heading markers

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` and not `<foreignObject>`
4. Transparency uses `fill-opacity` and `stroke-opacity`; `rgba()` is forbidden
5. No `<style>`, `class`, `mask`, external CSS, `foreignObject`, `textPath`, `animate*`, `script`, or `iframe`
6. One presentation, one icon library: `chunk`
7. Keep each slide within the design system defined above, even when layout motifs vary
8. Use native geometric decoration and avoid raster-image dependence

### PPT Compatibility Rules:

- Group opacity is forbidden; apply opacity per child element
- Text and shapes must remain inside safe margins unless intentionally full-bleed
- Rounded cards should be PowerPoint-safe and compatible with the finalize step
- Export must use `svg_final/` after post-processing, not raw `svg_output/`

