# Case 02 Validation Artifacts

`validate_case02.py` is the canonical reproducible build and validation harness for the reconciled v1.0 track. It regenerates all five role outputs, validates the approved printable page identity plus balanced-fill behavior, performs static/browser/interaction/PDF checks, writes current checksums and manifest data, and creates direct PDF-rendered contact sheets in `rendered-review/`.

Automated balanced-fill measurements are diagnostic; human design judgment remains final.
