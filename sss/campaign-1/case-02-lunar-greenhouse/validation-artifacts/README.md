# Case 02 Validation Artifacts

`validate_case02.py` is the canonical reproducible build and validation harness for the reconciled v1.0 track. It regenerates all five role outputs, performs static/browser/interaction/balanced-fill/PDF checks, writes current checksums and manifest data, and creates direct PDF-rendered contact sheets in `rendered-review/`.

Automated balanced-fill measurements are diagnostic; human design judgment remains final.
