# Workspace Start Here

Read these files in order before starting meaningful work:

1. `WORKSPACE_HANDOFF.md`
2. `APP_DEVELOPMENT_LOG.md`
3. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/MASTER_PLAN.md`
4. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/WORKSPACE_HANDOFF.md`
5. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/APP_WIDE_CONCERN_ROUTING.md`
6. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/APP_DEVELOPMENT_LOG.md`
7. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/APP_DEV_PORTFOLIO_LEDGER.md`
8. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_logging_contract.md`
9. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_master_plan_contract.md`
10. `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/AGENTS.md`

Scope companion:

- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_scope_contract.md`
- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/docs/app_dev_master_plan_contract.md`

If the task touches packaged-app QA, exact-bundle smoke, frontmost monitoring, or any claim that a lane is headless or nonfronting, also read:

- `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/HEADLESS_NONFRONTING_SMOKE_LESSONS.md`

## Startup Gate

- run `python3 "/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/scripts/check_appdev_coordination_readiness.py" --surface-root "."` from this directory before meaningful work
- if the check fails, restore or re-scaffold the missing coordination files before continuing
- do not stay in the current lane by habit; use the app strategy docs and the logging contract to decide whether to stay, move to verification, move to core, or create a new lane

## Master Plan Gate

- run `python3 "/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/scripts/check_appdev_master_plan.py" --surface-root "."` from this directory before meaningful work
- read `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/MASTER_PLAN.md` before site work that could affect product positioning, routing, or publish strategy
- reread that master plan after the task outcome is known and before user-facing closeout

## Scope Gate

- run `python3 "/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/scripts/check_appdev_scope.py" --surface-root "."` from this directory before meaningful work
- if the current request is broad, cross-lane, or sounds like it belongs elsewhere, rerun the scope gate with `--task-text "brief request summary"`
- if the scope gate or the app strategy points to a better-home lane, warn the user, name the better home, and ask for confirmation before continuing here

## Operating Rule

- keep this lane site-only: checkout pages, static copy, site assets, and published CSS
- do not mix product-code, OCR, export, or packaged-QA work into this publish lane by habit

## Stay Or Move Rule

- stay here when the work is site-only or publish-only
- move back to the PDF-MD app root when the work is export behavior, diagnostics, OCR, or packaged QA
- mirror meaningful site-publish events into `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/APP_DEVELOPMENT_LOG.md`

## Update Rule

- Append `APP_DEVELOPMENT_LOG.md` before substantial work, after outcome, and before user-facing closeout.
- Reread `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/docs/coordination/MASTER_PLAN.md` after the outcome is known and before closeout.
- Update `WORKSPACE_HANDOFF.md` first.
- Mirror meaningful lane notes into `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/apps/PDF-MD/APP_DEVELOPMENT_LOG.md`.
- Update `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/APP_DEV_PORTFOLIO_LEDGER.md` if lane status, proof truth, or next-slice truth changed.
- Append `/Volumes/DATA_ARCHIVE/Hub_Network/20_App_And_Tool_Hubs/AppDev_Hub/APP_DEV_ACTIVITY_LOG.md` if the event matters in chronology for future threads.
