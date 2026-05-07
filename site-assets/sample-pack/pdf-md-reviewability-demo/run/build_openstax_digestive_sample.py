#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

if Path("/tmp/pdfmd_openstax_deps").exists():
    sys.path.insert(0, "/tmp/pdfmd_openstax_deps")

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


PACK_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PACK_ROOT / "source"
RUN_DIR = PACK_ROOT / "run"
OUT_PDF = SOURCE_DIR / "openstax-digestion-lecture.pdf"
TRANSCRIPT = SOURCE_DIR / "source-transcript.md"
ROUTE_DIAGRAM = SOURCE_DIR / "digestive-route-embedded-labels.png"
CONTROL_DIAGRAM = SOURCE_DIR / "digestive-control-embedded-labels.png"
README = PACK_ROOT / "README.md"
PROFILE = RUN_DIR / "benchmark-profile.json"

PAGE_W = 960
PAGE_H = 540
MARGIN = 52

OPENSTAX_TITLE = "OpenStax Anatomy and Physiology 2e, Chapter 23: The Digestive System"
OPENSTAX_BOOK = "https://openstax.org/books/anatomy-and-physiology-2e/pages/1-introduction"
OPENSTAX_231 = "https://openstax.org/books/anatomy-and-physiology-2e/pages/23-1-overview-of-the-digestive-system"
OPENSTAX_232 = "https://openstax.org/books/anatomy-and-physiology-2e/pages/23-2-digestive-system-processes-and-regulation"
OPENSTAX_LICENSE = "https://creativecommons.org/licenses/by/4.0/"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()


def wrapped_lines(text: str, chars: int) -> list[str]:
    return textwrap.wrap(text, width=chars, break_long_words=False)


def draw_wrapped(c: canvas.Canvas, text: str, x: float, y: float, max_chars: int, leading: float, size: int = 18) -> float:
    c.setFont("Helvetica", size)
    for line in wrapped_lines(text, max_chars):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullets(c: canvas.Canvas, bullets: list[str], x: float, y: float, max_chars: int = 72) -> float:
    c.setFont("Helvetica", 18)
    for item in bullets:
        lines = wrapped_lines(item, max_chars)
        c.drawString(x, y, "-")
        c.drawString(x + 20, y, lines[0])
        y -= 25
        for line in lines[1:]:
            c.drawString(x + 20, y, line)
            y -= 25
        y -= 5
    return y


def start_slide(c: canvas.Canvas, title: str, subtitle: str | None = None) -> None:
    c.setFillColor(colors.HexColor("#fbfbf8"))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#174a3f"))
    c.rect(0, PAGE_H - 14, PAGE_W, 14, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#181c1b"))
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN, PAGE_H - 78, title)
    if subtitle:
        c.setFont("Helvetica", 16)
        c.setFillColor(colors.HexColor("#4d5753"))
        c.drawString(MARGIN, PAGE_H - 106, subtitle)


def footer(c: canvas.Canvas, page: int) -> None:
    c.setStrokeColor(colors.HexColor("#d8ddd8"))
    c.line(MARGIN, 42, PAGE_W - MARGIN, 42)
    c.setFillColor(colors.HexColor("#4d5753"))
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN, 25, "Adapted from OpenStax Anatomy and Physiology 2e, Chapter 23. CC BY 4.0.")
    c.drawRightString(PAGE_W - MARGIN, 25, f"PDF-MD sample lecture - {page}")


def draw_process_table(c: canvas.Canvas) -> None:
    x = MARGIN
    y = 365
    row_h = 38
    col_w = [170, 610]
    rows = [
        ("Ingestion", "Food enters the mouth and is prepared for movement."),
        ("Propulsion", "Swallowing and peristalsis move contents along the tract."),
        ("Mechanical digestion", "Chewing, churning, and segmentation increase surface area."),
        ("Chemical digestion", "Enzymes and acid break macromolecules into absorbable units."),
        ("Absorption", "Nutrients cross the intestinal mucosa into blood or lymph."),
        ("Defecation", "Indigestible material leaves the body."),
    ]
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#e9eee9"))
    c.rect(x, y, sum(col_w), row_h, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#181c1b"))
    c.drawString(x + 14, y + 13, "Process")
    c.drawString(x + col_w[0] + 14, y + 13, "Study cue")
    y -= row_h
    c.setFont("Helvetica", 13)
    for name, cue in rows:
        c.setStrokeColor(colors.HexColor("#cfd6cf"))
        c.rect(x, y, sum(col_w), row_h, fill=0, stroke=1)
        c.line(x + col_w[0], y, x + col_w[0], y + row_h)
        c.setFillColor(colors.HexColor("#174a3f"))
        c.setFont("Helvetica-Bold", 13)
        c.drawString(x + 14, y + 13, name)
        c.setFillColor(colors.HexColor("#181c1b"))
        c.setFont("Helvetica", 13)
        c.drawString(x + col_w[0] + 14, y + 13, cue)
        y -= row_h


def create_route_diagram(path: Path) -> None:
    img = Image.new("RGB", (1500, 820), "#f7f5ef")
    d = ImageDraw.Draw(img)
    title_font = font(44, True)
    label_font = font(30, True)
    small_font = font(24)
    d.text((52, 38), "Embedded-label route map", fill="#173f36", font=title_font)
    d.text((54, 96), "The labels in this diagram are pixels, not selectable PDF text.", fill="#4d5753", font=small_font)
    nodes = [
        ("Mouth", 135, 250),
        ("Pharynx", 355, 250),
        ("Esophagus", 610, 250),
        ("Stomach", 905, 250),
        ("Small intestine", 730, 520),
        ("Large intestine", 430, 520),
        ("Rectum / anus", 180, 520),
    ]
    for index, (label, x, y) in enumerate(nodes):
        d.rounded_rectangle((x - 95, y - 55, x + 95, y + 55), radius=24, fill="#ffffff", outline="#174a3f", width=5)
        text_w = d.textlength(label, font=label_font)
        d.text((x - text_w / 2, y - 18), label, fill="#181c1b", font=label_font)
        if index < 3:
            next_x = nodes[index + 1][1]
            d.line((x + 100, y, next_x - 100, y), fill="#174a3f", width=7)
            d.polygon([(next_x - 100, y), (next_x - 120, y - 14), (next_x - 120, y + 14)], fill="#174a3f")
    d.line((1005, 295, 805, 475), fill="#174a3f", width=7)
    d.polygon([(805, 475), (826, 466), (817, 447)], fill="#174a3f")
    d.line((635, 520, 525, 520), fill="#174a3f", width=7)
    d.polygon([(525, 520), (545, 506), (545, 534)], fill="#174a3f")
    d.line((335, 520, 280, 520), fill="#174a3f", width=7)
    d.polygon([(280, 520), (300, 506), (300, 534)], fill="#174a3f")
    d.rounded_rectangle((1070, 340, 1430, 650), radius=28, fill="#e9eee9", outline="#174a3f", width=4)
    d.text((1100, 372), "Accessory organs", fill="#173f36", font=label_font)
    for i, label in enumerate(["Liver", "Gallbladder", "Pancreas", "Salivary glands"]):
        d.text((1120, 432 + i * 48), f"- {label}", fill="#181c1b", font=small_font)
    img.save(path)


def create_control_diagram(path: Path) -> None:
    img = Image.new("RGB", (1500, 820), "#f7f5ef")
    d = ImageDraw.Draw(img)
    title_font = font(44, True)
    label_font = font(31, True)
    small_font = font(25)
    d.text((52, 38), "Embedded-label control map", fill="#173f36", font=title_font)
    d.text((54, 96), "Neural and hormonal labels are intentionally embedded in the image.", fill="#4d5753", font=small_font)
    centers = {
        "Food in lumen": (260, 380),
        "Stretch sensors": (560, 230),
        "Chemoreceptors": (560, 530),
        "Enteric plexuses": (875, 380),
        "Secretions + motility": (1220, 380),
    }
    for label, (x, y) in centers.items():
        d.rounded_rectangle((x - 150, y - 65, x + 150, y + 65), radius=28, fill="#ffffff", outline="#174a3f", width=5)
        lines = textwrap.wrap(label, 16)
        for i, line in enumerate(lines):
            text_w = d.textlength(line, font=label_font)
            d.text((x - text_w / 2, y - 20 + i * 36), line, fill="#181c1b", font=label_font)
    arrows = [
        ((410, 360), (410, 260), (560, 260)),
        ((410, 400), (410, 500), (560, 500)),
        ((710, 230), (875, 320)),
        ((710, 530), (875, 440)),
        ((1025, 380), (1070, 380)),
    ]
    for points in arrows:
        d.line(points, fill="#174a3f", width=7, joint="curve")
        end = points[-1]
        d.polygon([(end[0], end[1]), (end[0] - 22, end[1] - 14), (end[0] - 22, end[1] + 14)], fill="#174a3f")
    d.rounded_rectangle((70, 650, 1430, 760), radius=22, fill="#e9eee9", outline="#c2cac2", width=3)
    d.text((100, 676), "Study point: regulation is local plus systemic; reflexes and gut hormones tune digestion.", fill="#181c1b", font=small_font)
    img.save(path)


SLIDES = [
    {
        "title": "Introduction to digestion",
        "subtitle": "A rights-clean lecture PDF for PDF-MD extraction testing",
        "bullets": [
            "Digestion breaks food into absorbable molecules while moving material through the alimentary canal.",
            "The sample includes selectable text plus diagrams whose labels are embedded as image pixels.",
            "Source basis: OpenStax Anatomy and Physiology 2e, Chapter 23, adapted under CC BY 4.0.",
        ],
    },
    {
        "title": "System map",
        "subtitle": "Alimentary canal plus accessory organs",
        "bullets": [
            "Alimentary canal: mouth, pharynx, esophagus, stomach, small intestine, large intestine, rectum, anus.",
            "Accessory organs: teeth, tongue, salivary glands, liver, gallbladder, and pancreas.",
            "The core job is to release nutrients and absorb them into the body while eliminating indigestible residue.",
        ],
    },
    {
        "title": "Six digestive processes",
        "subtitle": "Text-table extraction target",
        "table": True,
    },
    {
        "title": "Route map with embedded labels",
        "subtitle": "Image OCR target",
        "image": ROUTE_DIAGRAM,
        "caption": "The diagram labels are part of a PNG, so PDF-MD must use image OCR to recover them.",
    },
    {
        "title": "Wall layers of the alimentary canal",
        "subtitle": "What students should keep straight",
        "bullets": [
            "Mucosa: epithelium and connective tissue at the lumen-facing surface.",
            "Submucosa: connective tissue, vessels, glands, and local nerve plexus.",
            "Muscularis: smooth muscle layers that drive mixing and propulsion.",
            "Serosa or adventitia: outer covering depending on organ position.",
        ],
    },
    {
        "title": "Control map with embedded labels",
        "subtitle": "Second image OCR target",
        "image": CONTROL_DIAGRAM,
        "caption": "This image tests whether the exported Markdown makes embedded labels visible enough to inspect.",
    },
    {
        "title": "Why the small intestine matters",
        "subtitle": "Absorption surface area and final digestion",
        "bullets": [
            "Most absorption occurs in the small intestine.",
            "Circular folds, villi, and microvilli increase mucosal surface area.",
            "Brush border enzymes complete parts of carbohydrate and protein digestion.",
            "Absorbed nutrients enter blood or lymph depending on the molecule type.",
        ],
    },
    {
        "title": "Attribution and sample boundary",
        "subtitle": "Public redistribution note",
        "bullets": [
            "Adapted from OpenStax Anatomy and Physiology 2e, Chapter 23: The Digestive System.",
            "Original OpenStax text is licensed under Creative Commons Attribution 4.0 International.",
            "This sample is not medical advice. It is a PDF-MD extraction demo for lecture-slide material.",
            "The test intentionally mixes selectable slide text with embedded text inside diagrams.",
        ],
    },
]


def create_pdf() -> None:
    c = canvas.Canvas(str(OUT_PDF), pagesize=(PAGE_W, PAGE_H))
    for page, slide in enumerate(SLIDES, 1):
        start_slide(c, slide["title"], slide.get("subtitle"))
        if slide.get("table"):
            draw_process_table(c)
        elif "image" in slide:
            img_path = slide["image"]
            c.drawImage(ImageReader(str(img_path)), MARGIN, 118, width=570, height=312, preserveAspectRatio=True, mask="auto")
            c.setFillColor(colors.HexColor("#181c1b"))
            y = draw_wrapped(c, slide["caption"], 665, 365, 24, 24, size=18)
            c.setFillColor(colors.HexColor("#4d5753"))
            draw_wrapped(c, "Normal slide text remains selectable; labels inside the diagram are embedded image text.", 665, y - 18, 25, 20, size=14)
        else:
            draw_bullets(c, slide["bullets"], MARGIN, 360)
        footer(c, page)
        c.showPage()
    c.save()


def write_transcript() -> None:
    lines = [
        "# OpenStax Digestion Lecture Sample",
        "",
        "This transcript describes the intended source PDF content. It is not PDF-MD output.",
        "",
    ]
    for i, slide in enumerate(SLIDES, 1):
        lines.append(f"## Slide {i}: {slide['title']}")
        if slide.get("subtitle"):
            lines.append(slide["subtitle"])
        if slide.get("bullets"):
            lines.extend([f"- {b}" for b in slide["bullets"]])
        if slide.get("table"):
            lines.append("- Ingestion: food enters the mouth.")
            lines.append("- Propulsion: swallowing and peristalsis move contents.")
            lines.append("- Mechanical digestion: chewing, churning, and segmentation increase surface area.")
            lines.append("- Chemical digestion: enzymes and acid break macromolecules.")
            lines.append("- Absorption: nutrients cross into blood or lymph.")
            lines.append("- Defecation: indigestible material leaves the body.")
        if slide.get("image") == ROUTE_DIAGRAM:
            lines.append("- Embedded image labels: Mouth, Pharynx, Esophagus, Stomach, Small intestine, Large intestine, Rectum / anus, Liver, Gallbladder, Pancreas, Salivary glands.")
        if slide.get("image") == CONTROL_DIAGRAM:
            lines.append("- Embedded image labels: Food in lumen, Stretch sensors, Chemoreceptors, Enteric plexuses, Secretions + motility.")
        lines.append("")
    lines.extend([
        "## Attribution",
        f"Adapted from {OPENSTAX_TITLE}.",
        f"Book URL: {OPENSTAX_BOOK}",
        f"Section 23.1: {OPENSTAX_231}",
        f"Section 23.2: {OPENSTAX_232}",
        f"License: {OPENSTAX_LICENSE}",
    ])
    TRANSCRIPT.write_text("\n".join(lines) + "\n")


def write_readme() -> None:
    README.write_text(
        "\n".join(
            [
                "# PDF-MD OpenStax Digestion Lecture Sample",
                "",
                "This pack is a rights-clean public sample for PDF-MD. It uses a short lecture-style PDF adapted from OpenStax Anatomy and Physiology 2e, Chapter 23 under CC BY 4.0.",
                "",
                "## What is inside",
                "",
                "- `source/openstax-digestion-lecture.pdf` - generated lecture-slide PDF with selectable text and embedded-label diagrams.",
                "- `source/digestive-route-embedded-labels.png` - PNG diagram whose labels are embedded image text.",
                "- `source/digestive-control-embedded-labels.png` - second PNG diagram for image OCR.",
                "- `source/source-transcript.md` - intended source content and attribution.",
                "- `output/openstax-digestion-lecture_Hybrid_norm.md` - Markdown generated through the PDF-MD benchmark/export harness.",
                "- `audit/openstax-digestion-lecture_Hybrid_norm.audit.json` - audit sidecar generated by PDF-MD for the same run.",
                "- `run/benchmark-profile.json` and `run/summary.json` - bounded proof profile and run summary.",
                "",
                "## Source and license",
                "",
                f"Adapted from {OPENSTAX_TITLE}.",
                f"Book: {OPENSTAX_BOOK}",
                f"Section 23.1: {OPENSTAX_231}",
                f"Section 23.2: {OPENSTAX_232}",
                f"License: {OPENSTAX_LICENSE}",
                "",
                "This sample is an extraction demo, not medical advice.",
            ]
        )
        + "\n"
    )


def write_profile() -> None:
    PROFILE.write_text(
        json.dumps(
            {
                "id": "pdf-md-openstax-digestion-lecture",
                "name": "PDF-MD OpenStax digestion lecture sample",
                "sourcePDFPath": str(OUT_PDF),
                "referenceAuditJSONPath": None,
                "referenceAuditJSONPaths": None,
                "ocrMode": "balanced",
                "ocrLanguageMode": "automatic",
                "ocrLanguages": [],
                "suites": [
                    {
                        "id": "openstax-digestion-pass",
                        "title": "OpenStax digestion lecture pass",
                        "description": "A bounded Hybrid export over a rights-clean digestion lecture PDF with selectable text plus embedded-label diagrams.",
                        "rangeExpression": "1-8",
                        "combinations": [
                            {
                                "exportMode": "hybrid",
                                "normalization": "on",
                                "expectation": "success",
                            }
                        ],
                    }
                ],
            },
            indent=2,
        )
        + "\n"
    )


def main() -> None:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    (PACK_ROOT / "output").mkdir(parents=True, exist_ok=True)
    (PACK_ROOT / "audit").mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    create_route_diagram(ROUTE_DIAGRAM)
    create_control_diagram(CONTROL_DIAGRAM)
    create_pdf()
    write_transcript()
    write_readme()
    write_profile()
    print(OUT_PDF)


if __name__ == "__main__":
    main()
