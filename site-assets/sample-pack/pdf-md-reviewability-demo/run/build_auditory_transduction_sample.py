#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


PACK_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PACK_ROOT / "source"
RUN_DIR = PACK_ROOT / "run"

SOURCE_LOCAL_PDF = Path(
    "/Users/siumanshermanchan/Documents/01_Academic_Core/01_Rome_Italy_2025_2030/"
    "MD_UCSC/03_Year_2_2025_2026/02_Spring_2026/01_Required_Courses/"
    "01_Fahb_3_Endocrine_Nervous_MR000011/01_Part_A_Endocrine_Nervous/"
    "02_Nervous/04_Physiology/009-Auditory transduction .pdf"
)

SELECTED_ORIGINAL_PAGES = [5, 8, 10, 11, 15, 20, 30, 40]

OUT_PDF = SOURCE_DIR / "auditory-transduction-lecture-excerpt.pdf"
TRANSCRIPT = SOURCE_DIR / "source-transcript.md"
PREVIEW_IMAGE = SOURCE_DIR / "auditory-transduction-embedded-labels.png"
README = PACK_ROOT / "README.md"
PROFILE = RUN_DIR / "benchmark-profile.json"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"Required tool not found: {name}")
    return path


def build_excerpt_pdf() -> None:
    qpdf = require_tool("qpdf")
    page_spec = ",".join(str(page) for page in SELECTED_ORIGINAL_PAGES)
    run([qpdf, "--empty", "--pages", str(SOURCE_LOCAL_PDF), page_spec, "--", str(OUT_PDF)])


def build_preview_image() -> None:
    pdftoppm = require_tool("pdftoppm")
    preview_stem = PREVIEW_IMAGE.with_suffix("")
    run([
        pdftoppm,
        "-png",
        "-r",
        "180",
        "-f",
        "8",
        "-l",
        "8",
        "-singlefile",
        str(OUT_PDF),
        str(preview_stem),
    ])


def extracted_text() -> str:
    pdftotext = require_tool("pdftotext")
    result = subprocess.run(
        [pdftotext, "-layout", str(OUT_PDF), "-"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def write_transcript() -> None:
    pages = ", ".join(str(page) for page in SELECTED_ORIGINAL_PAGES)
    text = extracted_text()
    TRANSCRIPT.write_text(
        "\n".join([
            "# Source Transcript",
            "",
            "This transcript was extracted from the representative auditory transduction",
            "lecture excerpt used in the public PDF-MD sample pack.",
            "",
            f"Original slide pages selected: {pages}.",
            "",
            "The transcript records the selectable PDF text layer only. Labels that exist",
            "inside rasterized figures are represented in the generated PDF-MD output",
            "when the Hybrid pass routes those pages through OCR.",
            "",
            "```text",
            text,
            "```",
            "",
        ]),
        encoding="utf-8",
    )


def write_profile() -> None:
    PROFILE.write_text(
        json.dumps(
            {
                "id": "pdf-md-auditory-transduction-lecture",
                "name": "PDF-MD auditory transduction lecture sample",
                "sourcePDFPath": str(OUT_PDF),
                "referenceAuditJSONPath": None,
                "referenceAuditJSONPaths": None,
                "ocrMode": "balanced",
                "ocrLanguageMode": "automatic",
                "ocrLanguages": [],
                "suites": [
                    {
                        "id": "auditory-transduction-pass",
                        "title": "Auditory transduction lecture pass",
                        "description": (
                            "A bounded Hybrid export over a user-confirmed "
                            "rights-cleared medical-school auditory transduction "
                            "lecture excerpt with selectable slide text and "
                            "embedded-label diagrams."
                        ),
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
        + "\n",
        encoding="utf-8",
    )


def write_readme() -> None:
    README.write_text(
        "\n".join([
            "# PDF-MD Auditory Transduction Sample Pack",
            "",
            "This sample pack lets prospective PDF-MD buyers inspect a real",
            "medical-school lecture excerpt before purchasing.",
            "",
            "The source PDF is a representative eight-slide excerpt from a",
            "user-confirmed rights-cleared auditory transduction lecture. It mixes",
            "normal selectable slide text with image-heavy anatomy and physiology",
            "figures whose labels are embedded in the figure images.",
            "",
            "## Files",
            "",
            "- `source/auditory-transduction-lecture-excerpt.pdf` - source excerpt",
            "- `source/auditory-transduction-embedded-labels.png` - rendered preview slide",
            "- `source/source-transcript.md` - selectable PDF text layer",
            "- `output/auditory-transduction-lecture-excerpt_Hybrid_norm.md` - generated Markdown",
            "- `audit/auditory-transduction-lecture-excerpt_Hybrid_norm.audit.json` - audit sidecar",
            "- OCR uncertainty notes are included inline in the Markdown and in the audit JSON when slide labels are spatially ambiguous.",
            "- `run/benchmark-profile.json` - benchmark profile used to regenerate output",
            "- `run/pdf-md-benchmark-output/` - retained benchmark output copy",
            "",
            "The sample is not medical advice. It is an extraction proof package for",
            "lecture-slide material.",
            "",
        ]),
        encoding="utf-8",
    )


def main() -> None:
    if not SOURCE_LOCAL_PDF.exists():
        raise FileNotFoundError(SOURCE_LOCAL_PDF)

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    build_excerpt_pdf()
    build_preview_image()
    write_transcript()
    write_profile()
    write_readme()


if __name__ == "__main__":
    main()
