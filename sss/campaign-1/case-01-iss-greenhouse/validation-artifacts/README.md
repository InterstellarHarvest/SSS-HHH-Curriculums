# Case 01 v1.0 Release-Candidate Validation Artifacts

This directory contains the portable validation harness and machine-readable results for the current v1.0 master.

## Run

From this directory:

```bash
python validate_case01_rc.py
```

The harness resolves all paths relative to its own repository location. It does not contain machine-specific home-directory imports.

## Checks

- Student, Teacher, Answer Key, Accessible, and All Pages role counts
- visible-page overflow
- grayscale and print-preview behavior
- unique DOM IDs and named response fields
- first-page-only Student identification placement
- exact Student/Accessible/Answer Key task headings
- Teacher task-reference emphasis
- required Answer Key exemplar content
- known malformed-text regression
- Teacher production-metadata visibility
- fill/edit keyboard access
- persistence across reload
- selective Student/Accessible clearing
- separate Teacher/Answer Key notes clearing
- reset-to-open-file behavior
- downloaded edited-HTML portability and reset semantics
- five release-candidate PDF builds and page counts

## Outputs

- `CASE01_RC_VALIDATION_RESULTS.json`
- `CASE01_RC_CHECKSUMS.sha256`
- `downloaded-html-portability-test.html` (validation evidence; not a distribution master)
- five role-specific PDFs under `../published/`

All outputs retain **VALIDATION BUILD** status until owner physical print testing passes.
