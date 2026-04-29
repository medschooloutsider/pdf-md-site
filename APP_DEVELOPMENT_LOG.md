# App Development Log

Updated: 2026-04-29 02:20 CEST

Append new entries at the end of this file.

## Entry Format

- `YYYY-MM-DD HH:MM TZ | scope | factual summary`

## Coordination Rule

- Mirror meaningful site-publish events into `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/APP_DEVELOPMENT_LOG.md`.
- Read `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_logging_contract.md` when the routing or mirroring rule is unclear.

## Entries

- 2026-04-12 13:30 CEST | bootstrap | Created the default development log for utility lane /Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/apps/PDF-MD/publishing/pdf-md-site-publish.
- 2026-04-22 11:27 CEST | trust-copy | Added proof-backed public trust copy to the site proof surfaces using the canonical PDF-MD 2026-04-22 commercial sweep boundaries: unit, headless smoke/stress/soak, strict packaged app-surface with `frontingCount=0`, workflow performance, perf smoke/stress/soak with `retainedOtherArtifactByteCount=0`, and structure-evidence coverage.
- 2026-04-23 16:11 CEST | hub-intake | Moved the clean `pdf-md-site-publish` site repository from AppDev `worktrees/` to `Commercialisation_Hub/apps/PDF-MD/publishing/pdf-md-site-publish` as part of the new Commercialisation Hub scaffold.
- 2026-04-23 16:16 CEST | post-move-gates | AppDev readiness, master-plan, and scope gates passed from the new Commercialisation Hub path after the handoff lane identity was corrected to `pdf-md-site-publish`.
- 2026-04-23 16:58 CEST | homepage-copy | Refined the homepage hero, proof, buy, and legal/support copy to name the HKD138 Personal License, sharpen the commercial sweep proof language, and make checkout/support terms explicit; layout and CSS were unchanged.
- 2026-04-24 01:20 CEST | showcase-dimension-normalization | Normalized the showcase image set in `site-assets/showcase/` to 1600x900 so the image cards match the 16:9 layout used by the public site sections. The current files are `routing-clean.png`, `diagnostics-clean.png`, `markdown-editor-clean.png`, and `export-preview-clean.png`.
- 2026-04-24 00:46 CEST | pages-publication | GitHub Pages was enabled on the public `medschooloutsider/pdf-md-site` repository, resolving the earlier 404 from the private-repo URL. The site root now serves `index.html` from `main`, so the public marketing/support URL is live again.
- 2026-04-24 15:11 CEST | flagship-homepage-rewrite | Rewrote the PDF-MD homepage top section around the 2026-04-24 marketing diagnosis: public-facing `PDF-MD` naming, flagship H1, shorter buyer-facing subhead, routing workspace screenshot as the first visual, above-fold workflow badges, and less internal proof/process language in the primary proof section.
- 2026-04-29 02:20 CEST | mcmaster-three-tab-site-rewrite | Mirrored the GPT-MD McMaster-Carr-inspired three-tab public site structure into PDF-MD using `/Users/siumanshermanchan/Downloads/PDFMD Website Draft.md`: Introduction, Technical Specification, and Sales & Support. Replaced the homepage, refreshed Terms/Privacy/EULA with PDF-MD-specific public copy, reused the cooler white/grey catalogue CSS, kept all page links intercommutable, and wired the Buy CTA to the live Lemon Squeezy checkout URL. Validation passed `git diff --check`, static local-link and new-tab target checks, placeholder/cross-product grep, and local Playwright desktop/mobile render checks with screenshots under `site_visual_review/`.
