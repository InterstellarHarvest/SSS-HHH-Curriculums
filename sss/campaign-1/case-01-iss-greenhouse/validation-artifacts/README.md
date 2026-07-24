# Case 01 v1.0 Validation Artifacts

This directory contains the portable validation harness and machine-readable results for the current v1.0 master.

## Validation environment setup

The Case 01 validation harness requires Python 3 and the packages listed in
`requirements.txt`.

From the repository root:

```bash
python3 -m venv .venv-case01-validation
source .venv-case01-validation/bin/activate
python -m pip install --upgrade pip
python -m pip install -r \
  sss/campaign-1/case-01-iss-greenhouse/validation-artifacts/requirements.txt
python -m playwright install chromium
```

On Linux CI or a minimal Linux workstation, Playwright may also require:

```bash
python -m playwright install --with-deps chromium
```

Run the validation harness using the command documented below. The generated
virtual environment is local tooling and must not be committed.

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
- five approved v1.0 PDF builds and page counts

## Outputs

- `CASE01_RC_VALIDATION_RESULTS.json`
- `CASE01_RC_CHECKSUMS.sha256`
- `downloaded-html-portability-test.html` (validation evidence; not a distribution master)
- five role-specific PDFs under `../published/`

All outputs are part of the approved stable v1.0 release; owner physical print testing passed on 2026-07-24.
