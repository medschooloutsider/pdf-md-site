# Workspace Handoff

Updated: 2026-04-24 16:09 CEST

## Lane

- Branch: `pdf-md-site-publish`
- Worktree: `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/apps/PDF-MD/publishing/pdf-md-site-publish`
- Responsibility: shared static-site publish lane for PDF-MD marketing and checkout pages
- Merge target: `none; shared utility lane`

## Current Objective

- keep static publish work isolated from PDF-MD product and QA changes; current slice keeps the public homepage aligned with the 2026-04-24 marketing diagnosis and treats PDF-MD as the flagship native Mac Markdown product

## What Is Already Done

- utility-lane startup and handoff files are now in place
- the PDF-MD root routing docs now explicitly reserve this lane for site-only work
- public proof surfaces now cite the 2026-04-22 commercial sweep boundaries without overclaiming universal PDF correctness
- lane folder moved from AppDev `worktrees/` into `Commercialisation_Hub/apps/PDF-MD/publishing/` so PDF-MD commercialisation material is navigable by app and function
- homepage top section now uses public-facing `PDF-MD` naming, a flagship document-to-Markdown promise, routing workspace screenshot as the first visual, buyer-facing feature badges, and less internal proof/process language
- harvested generated image assets from the 2026-04-24 PDF-MD image-heavy dispatch are now copied into `site-assets/generated/`; the homepage hero uses the primary backplate, the Advantage strip uses the secondary backplate, and the How section uses the workflow transformation visual instead of the older four-image collage
- `Commercialisation_Hub/apps/PDF-MD/distribution/app-store-metadata.md` now records a four-step App Store screenshot storyboard keyed to `site-assets/generated/pdfmd-app-store-backplate-set.png`

## Left To Do

- keep site-only work isolated here and mirror meaningful site-publish milestones into the PDF-MD app log
- optionally adjust generated-visual cropping after final stakeholder/deployment review
- feed any future generated visuals back into the homepage only after real app screenshots are used as prompt inputs
- optional: deploy the pushed site revision if the hosting provider does not auto-publish from `main`

## Waiting On

- none recorded yet

## Latest Proof Or Test Evidence

- Site validation for the 16:09 CEST visual-wiring slice: `git diff --check`; generated asset file existence and dimensions checked with `sips` at 1586x992 for all four copied PNGs; local browser pass served `index.html` from `127.0.0.1:8765` and captured `site_visual_review/pdf-md-generated-visual-wiring-1440.png`.
- Site validation for the 15:11 CEST rewrite slice: `git diff --check` plus static text review.
- 2026-04-24 flagship homepage rewrite followed the marketing diagnosis from `2026-04-24_gptmd_pdfmd_marketing_diagnosis_from_chatgpt_pro_extended.md` and reused `site-assets/showcase/routing-clean.png` as the first product visual.
- Source evidence remains in canonical PDF-MD `main`: final commercial sweep evidence under `QA/runs/*/20260422-*`, strict app-surface `QA/runs/app-surface/20260422-022358`, structure evidence `QA/runs/structure-evidence/20260422-020138`.
- Post-move AppDev readiness, master-plan, and scope gates passed from the new Commercialisation Hub path on 2026-04-23 16:16 CEST.

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
