# Workspace Handoff

Updated: 2026-04-29 02:20 CEST

## Lane

- Branch: `main`
- Worktree: `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/apps/PDF-MD/publishing/pdf-md-site-publish`
- Responsibility: shared static-site publish lane for PDF-MD marketing and checkout pages
- Merge target: `none; shared utility lane`

## Current Objective

- keep static publish work isolated from PDF-MD product and QA changes; current slice mirrors the GPT-MD three-tab catalogue website model into PDF-MD and prepares the static site for GitHub Pages publication from `main`

## What Is Already Done

- utility-lane startup and handoff files are now in place
- the PDF-MD root routing docs now explicitly reserve this lane for site-only work
- public proof surfaces now cite the 2026-04-22 commercial sweep boundaries without overclaiming universal PDF correctness
- lane folder moved from AppDev `worktrees/` into `Commercialisation_Hub/apps/PDF-MD/publishing/` so PDF-MD commercialisation material is navigable by app and function
- homepage top section now uses public-facing `PDF-MD` naming, a flagship document-to-Markdown promise, routing workspace screenshot as the first visual, buyer-facing feature badges, and less internal proof/process language
- harvested generated image assets from the 2026-04-24 PDF-MD image-heavy dispatch are now copied into `site-assets/generated/`; the homepage hero uses the primary backplate, the Advantage strip uses the secondary backplate, and the How section uses the workflow transformation visual instead of the older four-image collage
- `Commercialisation_Hub/apps/PDF-MD/distribution/app-store-metadata.md` now records a four-step App Store screenshot storyboard keyed to `site-assets/generated/pdfmd-app-store-backplate-set.png`
- the PDF-MD public site now uses the same clean three-tab structure as GPT-MD: Introduction, Technical Specification, and Sales & Support
- the homepage `Buy pdf.md` CTA is wired to the live Lemon Squeezy checkout URL `https://medout.lemonsqueezy.com/checkout/buy/4a9b9138-736f-4a98-afc2-48488fbf12ee`
- Terms, Privacy, and EULA pages are refreshed with PDF-MD-specific public-facing copy and cross-page navigation

## Left To Do

- keep site-only work isolated here and mirror meaningful site-publish milestones into the PDF-MD app log
- confirm GitHub Pages has picked up the latest pushed `main` revision after publication

## Waiting On

- none recorded yet

## Latest Proof Or Test Evidence

- Site validation for the 16:09 CEST visual-wiring slice: `git diff --check`; generated asset file existence and dimensions checked with `sips` at 1586x992 for all four copied PNGs; local browser pass served `index.html` from `127.0.0.1:8765` and captured `site_visual_review/pdf-md-generated-visual-wiring-1440.png`.
- Site validation for the 15:11 CEST rewrite slice: `git diff --check` plus static text review.
- 2026-04-24 flagship homepage rewrite followed the marketing diagnosis from `2026-04-24_gptmd_pdfmd_marketing_diagnosis_from_chatgpt_pro_extended.md` and reused `site-assets/showcase/routing-clean.png` as the first product visual.
- Source evidence remains in canonical PDF-MD `main`: final commercial sweep evidence under `QA/runs/*/20260422-*`, strict app-surface `QA/runs/app-surface/20260422-022358`, structure evidence `QA/runs/structure-evidence/20260422-020138`.
- Post-move AppDev readiness, master-plan, and scope gates passed from the new Commercialisation Hub path on 2026-04-23 16:16 CEST.
- 2026-04-29 three-tab rewrite validation: AppDev coordination, master-plan, and scope gates passed from the dedicated `pdf-md-site-publish` lane; `git diff --check` passed; static local-link and target checks returned no missing links and no non-anchor links lacking `target="_blank"`; placeholder/cross-product grep returned no matches; local Playwright render confirmed three primary tabs, the live Lemon checkout href, and no desktop/mobile horizontal overflow. Screenshots were written to `site_visual_review/pdf-md-three-tab-1440.png` and `site_visual_review/pdf-md-eula-390.png`.
- 2026-04-29 gallery update: the five selected `10_3*_ AM` images were identified as pdf.md images and added as a no-title/no-caption gallery under the Introduction panel. Final gallery assets are exact 2880x1800 PNGs under `site-assets/gallery/pdf-md/` with numbered descriptive filenames. Local checks confirmed five gallery images, no missing references, and no horizontal overflow.

## Risks To Other Lanes

- none recorded yet

## Relevant Handoff Or Contract Files

- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/MASTER_PLAN.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/WORKSPACE_HANDOFF.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/APP_WIDE_CONCERN_ROUTING.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/APP_DEVELOPMENT_LOG.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/docs/coordination/MASTER_PLAN.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/WORKSPACE_HANDOFF.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/APP_DEV_PORTFOLIO_LEDGER.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_ledger_contract.md`
