# Workspace Handoff

Updated: 2026-04-23 16:16 CEST

## Lane

- Branch: `pdf-md-site-publish`
- Worktree: `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/Commercialisation_Hub/apps/PDF-MD/publishing/pdf-md-site-publish`
- Responsibility: shared static-site publish lane for PDF-MD marketing and checkout pages
- Merge target: `none; shared utility lane`

## Current Objective

- keep static publish work isolated from PDF-MD product and QA changes; current slice adds proof-backed trust copy from the 2026-04-22 PDF-MD commercial sweep

## What Is Already Done

- utility-lane startup and handoff files are now in place
- the PDF-MD root routing docs now explicitly reserve this lane for site-only work
- public proof surfaces now cite the 2026-04-22 commercial sweep boundaries without overclaiming universal PDF correctness
- lane folder moved from AppDev `worktrees/` into `Commercialisation_Hub/apps/PDF-MD/publishing/` so PDF-MD commercialisation material is navigable by app and function

## Left To Do

- keep site-only work isolated here and mirror meaningful site-publish milestones into the PDF-MD app log
- optional: deploy the pushed site revision if the hosting provider does not auto-publish from `main`

## Waiting On

- none recorded yet

## Latest Proof Or Test Evidence

- Site validation for this slice: `git diff --check` plus static text review.
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
