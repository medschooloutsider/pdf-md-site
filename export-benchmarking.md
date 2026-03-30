# Export Benchmarking

The representative benchmark profile for `ALL Past Papers Biopath 2.pdf` lives in `docs/biopath-export-benchmark-profile.json`.

It is intentionally small and tuned to the route map seen in the full-document hybrid exports:

- `17-21`: first transition into OCR fallback and back to mixed extraction
- `180-184`: OCR fallback pages plus the slow late mixed-content cluster
- `203-210`: late-document route mix where normalization changes route selection
- `204,206,210,213-214`: Fast Text probe pages that still appear incompatible because raster content is present

Run the benchmark from the repo root with:

- `./scripts/run_export_benchmark.sh`

Artifacts are written under `dist/benchmarks/<timestamp>/`:

- `summary.json`: machine-readable results for every suite and mode combination
- `summary.md`: readable report with timings, route mix, slowest page, reference drift, and failure reasons
- one folder per suite and mode, containing the generated markdown and audit artifacts

The Biopath profile points norm-on runs at the saved `_OCR_norm.audit.json` export and norm-off runs at `_OCR_raw.audit.json`, so each benchmark row reports:

- route drift against the matching reference export
- text drift count against the matching reference export

The profile keeps OCR concurrency at `Balanced`, matching the current machine recommendation for the M1 Max test system.
