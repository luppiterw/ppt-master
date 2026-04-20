from __future__ import annotations

import argparse
import copy
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


SVG_NS = "http://www.w3.org/2000/svg"
NS = {"svg": SVG_NS}
ET.register_namespace("", SVG_NS)


@dataclass(frozen=True)
class Theme:
    key: str
    display_name: str
    template_name: str
    design_style: str
    theme_mode: str
    bg: str
    alt_bg: str
    primary: str
    accent: str
    accent_2: str
    text: str
    secondary_text: str
    tertiary_text: str
    border: str
    success: str
    warning: str
    title_font: str
    body_font: str
    dark_cover: bool = False
    dark_cover_bg_1: str = ""
    dark_cover_bg_2: str = ""


THEMES: dict[str, Theme] = {
    "mckinsey": Theme(
        key="mckinsey",
        display_name="McKinsey Style",
        template_name="mckinsey",
        design_style="McKinsey-style consulting deck",
        theme_mode="Light theme",
        bg="#FFFFFF",
        alt_bg="#ECF0F1",
        primary="#005587",
        accent="#0076A8",
        accent_2="#F5A623",
        text="#2C3E50",
        secondary_text="#5D6D7E",
        tertiary_text="#7F8C8D",
        border="#D8E0E5",
        success="#27AE60",
        warning="#E74C3C",
        title_font='Arial, "Helvetica Neue", "Segoe UI", sans-serif',
        body_font='Arial, "Helvetica Neue", "Segoe UI", sans-serif',
    ),
    "anthropic": Theme(
        key="anthropic",
        display_name="Anthropic Style",
        template_name="anthropic",
        design_style="Anthropic-style AI product deck",
        theme_mode="Mixed theme",
        bg="#FFFFFF",
        alt_bg="#F8FAFC",
        primary="#D97757",
        accent="#4A90D9",
        accent_2="#10B981",
        text="#1A1A2E",
        secondary_text="#64748B",
        tertiary_text="#94A3B8",
        border="#E2E8F0",
        success="#10B981",
        warning="#EF4444",
        title_font='Arial, "Helvetica Neue", "Segoe UI", sans-serif',
        body_font='Arial, "Helvetica Neue", "Segoe UI", sans-serif',
        dark_cover=True,
        dark_cover_bg_1="#1A1A2E",
        dark_cover_bg_2="#0F172A",
    ),
    "pixel_retro": Theme(
        key="pixel_retro",
        display_name="Pixel Retro Style",
        template_name="pixel_retro",
        design_style="Pixel retro neon deck",
        theme_mode="Dark theme",
        bg="#0D1117",
        alt_bg="#161B22",
        primary="#39FF14",
        accent="#00D4FF",
        accent_2="#FF2E97",
        text="#E6EDF3",
        secondary_text="#8B949E",
        tertiary_text="#6E7681",
        border="#30363D",
        success="#39FF14",
        warning="#FFD700",
        title_font='"Consolas", "Monaco", "Courier New", monospace',
        body_font='"Segoe UI", "Microsoft YaHei", sans-serif',
    ),
}


OLD_COLORS = {
    "#f7f9fc": "bg",
    "#eaf0f8": "alt_bg",
    "#1565c0": "primary",
    "#00acc1": "accent",
    "#7c4dff": "accent_2",
    "#1f2937": "text",
    "#5b6472": "secondary_text",
    "#8b95a7": "tertiary_text",
    "#d6deea": "border",
    "#2e7d32": "success",
    "#d84315": "warning",
}


SLIDE_LABELS = {
    "slide_01_cover": "DECK OVERVIEW",
    "slide_02_core_claim": "CORE CLAIM",
    "slide_03_market_tradeoffs": "MARKET TRADEOFFS",
    "slide_04_value_grid": "VALUE FRAME",
    "slide_05_system_architecture": "SYSTEM LOGIC",
    "slide_06_three_stages": "THREE STAGES",
    "slide_07_why_svg": "SVG STRATEGY",
    "slide_08_design_philosophy": "DESIGN RULES",
    "slide_09_faq_snapshot": "FAQ SNAPSHOT",
    "slide_10_quality_expectations": "QUALITY BAR",
    "slide_11_windows_setup": "WINDOWS SETUP",
    "slide_12_troubleshooting": "TROUBLESHOOTING",
    "slide_13_closing_fit": "BEST FIT",
}


def normalize_hex(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip().lower()
    if re.fullmatch(r"#[0-9a-f]{6}", value):
        return value
    return None


def parse_font_size(value: str | None) -> float:
    if not value:
        return 0.0
    match = re.search(r"[\d.]+", value)
    return float(match.group(0)) if match else 0.0


def is_full_background_rect(elem: ET.Element) -> bool:
    return (
        elem.tag == f"{{{SVG_NS}}}rect"
        and elem.get("x", "0") == "0"
        and elem.get("y", "0") == "0"
        and elem.get("width") == "1280"
        and elem.get("height") == "720"
    )


def map_shape_color(color: str | None, theme: Theme) -> str | None:
    hex_value = normalize_hex(color)
    if not hex_value:
        return color
    role = OLD_COLORS.get(hex_value)
    if not role:
        if hex_value == "#ffffff":
            return theme.alt_bg
        return color
    return getattr(theme, role)


def map_text_color(color: str | None, theme: Theme, slide_name: str, y_value: float, font_size: float) -> str | None:
    if isinstance(color, str) and color.startswith("url("):
        return theme.primary
    hex_value = normalize_hex(color)
    if not hex_value:
        return color
    if theme.key == "pixel_retro":
        if hex_value == "#ffffff":
            return "#FFFFFF"
        role = OLD_COLORS.get(hex_value)
        if role in {"text", "secondary_text", "tertiary_text"}:
            if y_value <= 130 and font_size >= 24:
                return theme.primary
            if role == "text":
                return theme.text
            return theme.secondary_text
        if role:
            return getattr(theme, role)
        return theme.text
    if theme.dark_cover and slide_name in {"slide_01_cover", "slide_13_closing_fit"}:
        if hex_value in {"#ffffff", "#1f2937", "#5b6472", "#8b95a7"}:
            if y_value <= 140 and font_size >= 24:
                return "#FFFFFF"
            if hex_value == "#1f2937":
                return "#FFFFFF"
            if hex_value == "#5b6472":
                return "#CBD5E1"
            return "#94A3B8"
    if hex_value == "#ffffff":
        return "#FFFFFF"
    role = OLD_COLORS.get(hex_value)
    return getattr(theme, role) if role else color


def set_font(elem: ET.Element, theme: Theme, title_like: bool) -> None:
    elem.set("font-family", theme.title_font if title_like else theme.body_font)


def add_snippet(root: ET.Element, index: int, snippet: str) -> int:
    wrapped = f'<wrapper xmlns="{SVG_NS}">{snippet}</wrapper>'
    wrapper = ET.fromstring(wrapped)
    for child in list(wrapper):
        root.insert(index, child)
        index += 1
    return index


def ensure_defs(root: ET.Element) -> ET.Element:
    defs = root.find("svg:defs", NS)
    if defs is None:
        defs = ET.Element(f"{{{SVG_NS}}}defs")
        root.insert(0, defs)
    return defs


def find_insert_after_background(root: ET.Element) -> int:
    index = 0
    for child in list(root):
        if child.tag == f"{{{SVG_NS}}}defs":
            index += 1
            continue
        if is_full_background_rect(child):
            index += 1
            continue
        break
    return index


def add_mckinsey_frame(root: ET.Element, slide_name: str) -> None:
    index = find_insert_after_background(root)
    index = add_snippet(root, index, '<rect x="0" y="0" width="1280" height="4" fill="#005587"/>')
    if slide_name == "slide_01_cover":
        add_snippet(root, index, '<rect x="44" y="56" width="8" height="590" fill="#005587"/>')


def add_anthropic_frame(root: ET.Element, slide_name: str) -> None:
    index = find_insert_after_background(root)
    index = add_snippet(root, index, '<rect x="0" y="0" width="1280" height="6" fill="#D97757"/>')
    if slide_name not in {"slide_01_cover", "slide_13_closing_fit"}:
        label = SLIDE_LABELS.get(slide_name, slide_name.replace("_", " ").upper())
        add_snippet(
            root,
            index,
            f'<text x="60" y="52" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" letter-spacing="2" fill="#D97757">{label}</text>',
        )


def add_pixel_frame(root: ET.Element, slide_name: str) -> None:
    index = find_insert_after_background(root)
    index = add_snippet(
        root,
        index,
        (
            '<rect x="0" y="0" width="1280" height="4" fill="#39FF14" fill-opacity="0.65"/>'
            '<rect x="0" y="6" width="640" height="2" fill="#00D4FF" fill-opacity="0.45"/>'
            '<rect x="0" y="714" width="1280" height="2" fill="#00D4FF" fill-opacity="0.45"/>'
            '<rect x="0" y="716" width="1280" height="4" fill="#39FF14" fill-opacity="0.65"/>'
        ),
    )
    if slide_name == "slide_01_cover":
        add_snippet(
            root,
            index,
            (
                '<rect x="1048" y="80" width="18" height="18" fill="#39FF14" fill-opacity="0.90"/>'
                '<rect x="1072" y="80" width="18" height="18" fill="#00D4FF" fill-opacity="0.70"/>'
                '<rect x="1096" y="80" width="18" height="18" fill="#FF2E97" fill-opacity="0.90"/>'
            ),
        )


def apply_dark_cover(root: ET.Element, theme: Theme) -> None:
    defs = ensure_defs(root)
    gradient = ET.fromstring(
        f'''
        <linearGradient xmlns="{SVG_NS}" id="variantDarkBg" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="{theme.dark_cover_bg_1}"/>
          <stop offset="100%" stop-color="{theme.dark_cover_bg_2}"/>
        </linearGradient>
        '''
    )
    defs.append(gradient)

    first_background = True
    for elem in root:
        if is_full_background_rect(elem):
            if first_background:
                elem.set("fill", "url(#variantDarkBg)")
                first_background = False
            else:
                elem.set("fill", "none")

    grid_snippet = """
    <g>
      <rect x="0" y="0" width="1280" height="720" fill="none" stroke="#FFFFFF" stroke-opacity="0.04" stroke-width="1"/>
      <path d="M0 180 H1280 M0 360 H1280 M0 540 H1280 M320 0 V720 M640 0 V720 M960 0 V720"
            fill="none" stroke="#FFFFFF" stroke-opacity="0.03" stroke-width="1"/>
      <circle cx="1060" cy="120" r="160" fill="#D97757" fill-opacity="0.10"/>
      <circle cx="930" cy="600" r="210" fill="#4A90D9" fill-opacity="0.08"/>
    </g>
    """
    add_snippet(root, find_insert_after_background(root), grid_snippet)


def restyle_svg(svg_path: Path, theme: Theme) -> None:
    tree = ET.parse(svg_path)
    root = tree.getroot()
    slide_name = svg_path.stem

    for elem in root.iter():
        tag = elem.tag
        if tag == f"{{{SVG_NS}}}text":
            font_size = parse_font_size(elem.get("font-size"))
            y_value = float(re.search(r"[\d.]+", elem.get("y", "0")).group(0)) if re.search(r"[\d.]+", elem.get("y", "0")) else 0.0
            title_like = font_size >= 24 or (y_value <= 140 and font_size >= 18)
            set_font(elem, theme, title_like)
            fill = elem.get("fill")
            mapped_fill = map_text_color(fill, theme, slide_name, y_value, font_size)
            if mapped_fill:
                elem.set("fill", mapped_fill)
            if theme.key == "pixel_retro" and title_like and y_value <= 130:
                elem.set("font-weight", "700")
            continue

        if tag in {
            f"{{{SVG_NS}}}rect",
            f"{{{SVG_NS}}}circle",
            f"{{{SVG_NS}}}ellipse",
            f"{{{SVG_NS}}}path",
            f"{{{SVG_NS}}}polygon",
            f"{{{SVG_NS}}}use",
        }:
            if is_full_background_rect(elem):
                elem.set("fill", theme.bg)
            else:
                fill = elem.get("fill")
                if fill and not fill.startswith("url("):
                    mapped_fill = map_shape_color(fill, theme)
                    if mapped_fill:
                        elem.set("fill", mapped_fill)
                stroke = elem.get("stroke")
                if stroke and not stroke.startswith("url("):
                    mapped_stroke = map_shape_color(stroke, theme)
                    if mapped_stroke:
                        elem.set("stroke", mapped_stroke)
                if theme.key == "pixel_retro" and tag == f"{{{SVG_NS}}}rect" and elem.get("rx") and elem.get("width"):
                    try:
                        width = float(elem.get("width", "0"))
                    except ValueError:
                        width = 0
                    if width >= 120 and elem.get("fill") == theme.alt_bg:
                        elem.set("stroke", theme.border)
                        elem.set("stroke-width", "2")
                        elem.set("rx", "6")
            continue

        if tag == f"{{{SVG_NS}}}stop":
            stop_color = elem.get("stop-color")
            if stop_color and not stop_color.startswith("url("):
                mapped = map_shape_color(stop_color, theme)
                if mapped:
                    elem.set("stop-color", mapped)

    if theme.key == "mckinsey":
        add_mckinsey_frame(root, slide_name)
    elif theme.key == "anthropic":
        if slide_name in {"slide_01_cover", "slide_13_closing_fit"}:
            apply_dark_cover(root, theme)
        add_anthropic_frame(root, slide_name)
    elif theme.key == "pixel_retro":
        add_pixel_frame(root, slide_name)

    tree.write(svg_path, encoding="utf-8", xml_declaration=False)


def build_design_spec(theme: Theme, original_spec: str, project_name: str, date_text: str) -> str:
    _, remainder = original_spec.split("## V. Layout Principles", 1)
    header = f"""# {project_name} - Design Spec

> This document is the unified handoff artifact for the {theme.display_name} variant. It keeps the same narrative and slide outline while switching the visual system to the selected template family.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | {project_name} |
| **Canvas Format** | PPT 16:9 (1280x720) |
| **Page Count** | 13 |
| **Design Style** | {theme.design_style} |
| **Target Audience** | Developers, AI IDE users, open-source adopters, technical teams, internal demo viewers |
| **Use Case** | Product introduction, technical overview, community sharing, internal onboarding |
| **Created Date** | {date_text} |

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

- **Style**: {theme.display_name}
- **Theme**: {theme.theme_mode}
- **Tone**: consistent with the repository template family `{theme.template_name}`

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `{theme.bg}` | Main page background |
| **Secondary bg** | `{theme.alt_bg}` | Cards, panels, quiet surfaces |
| **Primary** | `{theme.primary}` | Titles, key accents, structural highlights |
| **Accent** | `{theme.accent}` | Connectors, secondary emphasis |
| **Secondary accent** | `{theme.accent_2}` | Callouts, alternative emphasis |
| **Body text** | `{theme.text}` | Primary text |
| **Secondary text** | `{theme.secondary_text}` | Supporting copy |
| **Tertiary text** | `{theme.tertiary_text}` | Footers and low-priority notes |
| **Border/divider** | `{theme.border}` | Borders and separators |
| **Success** | `{theme.success}` | Positive states |
| **Warning** | `{theme.warning}` | Risks, cautions, issue markers |

---

## IV. Typography System

### Font Plan

| Role | Font |
| ---- | ---- |
| **Title** | `{theme.title_font}` |
| **Body** | `{theme.body_font}` |
| **Code** | `"Consolas", "Monaco", monospace` |
| **Emphasis** | `{theme.title_font}` |

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
"""
    return header + remainder


def safe_variant_name(base_project: Path, theme_key: str) -> Path:
    root = base_project.parent
    match = re.match(r"^(.*)_(\d{8})$", base_project.name)
    if match:
        base_name = f"{match.group(1)}_{theme_key}_{match.group(2)}"
    else:
        base_name = f"{base_project.name}_{theme_key}"
    candidate = root / base_name
    suffix = 2
    while candidate.exists():
        candidate = root / f"{base_name}_{suffix}"
        suffix += 1
    return candidate


def copy_project_structure(source_project: Path, destination_project: Path, template_dir: Path) -> None:
    shutil.copytree(source_project, destination_project)
    for dirname in ("exports", "svg_final"):
        target = destination_project / dirname
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)

    project_templates = destination_project / "templates"
    if project_templates.exists():
        shutil.rmtree(project_templates)
    project_templates.mkdir(parents=True, exist_ok=True)

    for asset in template_dir.iterdir():
        if asset.is_file():
            shutil.copy2(asset, project_templates / asset.name)


def generate_variant(source_project: Path, theme: Theme) -> Path:
    date_text = datetime.now().strftime("%Y-%m-%d")
    destination_project = safe_variant_name(source_project, theme.key)
    template_dir = source_project.parents[1] / "skills" / "ppt-master" / "templates" / "layouts" / theme.template_name
    copy_project_structure(source_project, destination_project, template_dir)

    original_spec = (source_project / "design_spec.md").read_text(encoding="utf-8")
    new_spec = build_design_spec(theme, original_spec, destination_project.name, date_text)
    (destination_project / "design_spec.md").write_text(new_spec, encoding="utf-8")

    for svg_path in sorted((destination_project / "svg_output").glob("*.svg")):
        restyle_svg(svg_path, theme)

    return destination_project


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a themed variant project from an existing PPT Master project.")
    parser.add_argument("source_project", type=Path)
    parser.add_argument("--theme", choices=sorted(THEMES), required=True)
    args = parser.parse_args()

    source_project = args.source_project.resolve()
    theme = THEMES[args.theme]
    destination = generate_variant(source_project, theme)
    print(destination)


if __name__ == "__main__":
    main()
