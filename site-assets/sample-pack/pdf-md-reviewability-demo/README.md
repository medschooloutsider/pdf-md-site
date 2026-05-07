# PDF-MD Auditory Transduction Sample Pack

This sample pack lets prospective PDF-MD buyers inspect a real
medical-school lecture excerpt before purchasing.

The source PDF is a representative eight-slide excerpt from a
user-confirmed rights-cleared auditory transduction lecture. It mixes
normal selectable slide text with image-heavy anatomy and physiology
figures whose labels are embedded in the figure images.

## Files

- `source/auditory-transduction-lecture-excerpt.pdf` - source excerpt
- `source/auditory-transduction-embedded-labels.png` - rendered preview slide
- `source/source-transcript.md` - selectable PDF text layer
- `output/auditory-transduction-lecture-excerpt_Hybrid_norm.md` - generated Markdown
- `audit/auditory-transduction-lecture-excerpt_Hybrid_norm.audit.json` - audit sidecar
- OCR uncertainty notes are included inline in the Markdown and in the audit JSON when slide labels are spatially ambiguous.
- `run/benchmark-profile.json` - benchmark profile used to regenerate output
- `run/pdf-md-benchmark-output/` - retained benchmark output copy

The sample is not medical advice. It is an extraction proof package for
lecture-slide material.
