# SSS Case 01 v1.0 RC Repository Handoff

**Repository base inspected:** `InterstellarHarvest/SSS-HHH-Curriculums` `main` at `c68f05d964c828297d6d9c6ca00d77253a9d78fe`  
**Prepared:** 2026-07-24

## Apply

Extract the repository overlay at the root of a checkout at the inspected base, then review the replacements with `git diff`. The overlay contains only new or replaced approved v1.0 release files; historical v0.2/v0.3 files already in the repository remain untouched.

Run:

```bash
cd sss/campaign-1/case-01-iss-greenhouse/validation-artifacts
python validate_case01_rc.py
```

The harness discovers Chromium through `CHROMIUM_PATH`, `chromium`, or `chromium-browser`; paths in results and documentation are repository-relative.

## Result

Automated validation passed and the owner completed physical 100% scale print testing on 2026-07-24. Case 01 is the approved stable v1.0 release.

## Publishing note

The connected GitHub integration provided read access to current HEAD but rejected branch and file writes with HTTP 403. This handoff is therefore packaged as a repository-ready overlay rather than a pushed commit or pull request.
