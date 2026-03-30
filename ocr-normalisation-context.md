# OCR Normalisation Context

Updated: 2026-03-12

## Goal

Make OCR normalisation behave like a conservative structural enhancement layer, not a lossy compression pass.

The target is:

- Preserve semantic content from raw OCR whenever possible.
- Improve structure only when the transform is low-risk.
- Keep enough audit data to explain why a page was normalised the way it was.

## Practical Feasibility

This is practical, with limits.

What is realistically achievable:

- Prevent most self-inflicted information loss caused by post-processing.
- Recover better reading order on figure-heavy pages by using OCR layout geometry.
- Separate figure labels from captions more reliably than plain text heuristics alone.
- Expose OCR geometry in audit output so failures can be debugged visually.

What is not realistically guaranteed from plain OCR text alone:

- Perfect semantic reconstruction of dense figures.
- Perfect caption/label classification on all pages.
- Reliable recovery when Vision recognition itself is wrong or incomplete.

## Current Design Decisions

### 1. Normalisation must be conservative

Normalisation is allowed to:

- clean whitespace
- promote obvious headings
- preserve figure-label clusters as structured bullets

Normalisation is not allowed to:

- replace original label lines with a shorter synthetic summary if that loses content
- remove figure captions just because they look noisy
- bias OCR candidate selection toward outputs that are shorter but less faithful

### 2. OCR candidate scoring happens before normalisation

The DPI selection logic now scores pre-normalised OCR text, then applies normalisation to the winning candidate.

Reason:

- a destructive normaliser should not influence which OCR result is considered "best"

### 3. Layout information is now retained during OCR assembly

Vision `VNRecognizedTextObservation` bounding boxes are now preserved long enough to:

- group words into rows
- order rows spatially
- join fragments that belong on the same row
- insert paragraph breaks before likely figure captions

This is the first real step beyond text-only heuristics.

### 4. Audit output must include OCR geometry

Heavy Audit now exposes OCR observation boxes in:

- JSON sidecar: `sections[].ocrObservations`
- HTML audit viewer: blue overlays on the rendered page

Reason:

- OCR quality work is not credible if the app hides what Vision actually saw

### 5. Metrics must be comparable across export modes

All export modes now write audit JSON.

The shared audit schema separates:

- `metrics.extraction`
- `metrics.normalization`

Reason:

- `Fast Text` cannot match OCR content coverage on raster-heavy pages
- but it can still be compared on normalization behavior using the same metric schema

## Changes Landed

### OCR engine

File: `Sources/PDFMD/OCREngine.swift`

- `PageExtraction` and `PageResult` now carry OCR observations.
- OCR recognition now returns both assembled text and observation geometry.
- Cropped region OCR remaps observation boxes back into page coordinates.
- OCR assembly is layout-aware instead of plain newline concatenation.
- Full-page OCR candidate scoring uses raw OCR before normalisation.
- Destructive normalisation falls back to precleaned OCR.

### Normaliser

File: `Sources/PDFMD/Resources/normalize_ocr_text.sh`

- Figure-label clusters are preserved as bullet lists instead of a semicolon summary line.

### Tests

File: `Tests/PDFMDTests/PDFMDTests.swift`

Added regression coverage for:

- the brainstem `Figure 3.3` caption-loss example
- layout-aware caption separation from label bands
- Heavy Audit JSON persistence of OCR observation geometry
- Fast Text audit JSON persistence of shared extraction/normalization metrics

## Known Failure That Triggered This Work

Example page:

- raw OCR preserved both label lines and the `Figure 3.3` caption
- normalised OCR collapsed labels into a synthetic `Figure labels: ...` line
- the caption block was dropped entirely

This was a normaliser failure, not primarily an OCR-recognition failure.

## How To Test Now

### App bundle

Built app:

- `dist/PDF-MD.app`

### Recommended manual test

1. Launch `dist/PDF-MD.app`.
2. Export the target PDF in `Heavy Audit` mode.
3. Inspect:
   - markdown output
   - `.audit.json`
   - `.audit.html`

### What to look for

- Figure captions should survive normalisation if they were present in raw OCR.
- Figure labels should remain structured, not rewritten into a shorter synthetic sentence.
- All modes should write `stem.audit.json`.
- Audit JSON should include `metrics.extraction` and `metrics.normalization`.
- `.audit.json` should include `ocrObservations` per section.
- `.audit.html` should show blue OCR line boxes over the rendered page.

## Relevant Artifacts

- App bundle: `dist/PDF-MD.app`
- OCR engine: `Sources/PDFMD/OCREngine.swift`
- OCR normaliser: `Sources/PDFMD/Resources/normalize_ocr_text.sh`
- Tests: `Tests/PDFMDTests/PDFMDTests.swift`

## Remaining Gaps

### 1. Normaliser still reasons mostly from text

The OCR assembly step is layout-aware, but the shell normaliser still mostly sees text only.

Good next move:

- move more structure decisions out of the shell script and into Swift where geometry is available

### 2. No explicit caption classifier yet

Current caption handling is heuristic:

- paragraph gap
- spatial order
- `Figure <number>` detection

Good next move:

- introduce a caption classifier based on geometry, prefix patterns, and line width

### 3. OCR observations are audit-only

The geometry is now exported, but not yet fully used for:

- label clustering
- list reconstruction
- side-note isolation
- multi-column detection

### 4. No side-by-side raw vs normalised audit view

Good next move:

- persist both raw OCR assembly and final normalised OCR in the audit sidecar for direct comparison

### 5. No corpus benchmark yet

We still need a stable evaluation set of difficult PDFs with expected failure categories:

- figure-heavy lecture slides
- anatomical atlases
- scanned notes with mixed prose and diagrams
- multi-column scientific pages

## Suggested Next Iteration

1. Add raw assembled OCR to audit JSON next to normalised OCR.
2. Tag each OCR observation with source:
   - full-page OCR
   - region OCR
   - slide fallback OCR
3. Add a caption classifier in Swift.
4. Reduce shell normaliser responsibility to low-risk cleanup only.
5. Build a small regression corpus and score token retention plus caption retention.

## Current Status

The pipeline is materially better than the original text-only normalisation pass.

It now:

- preserves more content
- uses layout during OCR assembly
- exposes OCR geometry for debugging
- reports shared extraction/normalization metrics across all export modes
- has regression coverage for the failure that started this thread

It is not finished, but it is now on a sounder architecture.
