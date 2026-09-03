# C43/G0 API

`deuteron_wigner.bridge.g0.source_manifest()` regenerates hashes and metadata
for the locked local C43 sources. `conventions()` and `action_contract()`
return the action-level gauge, constraint, interaction, boundary, and
zero-mode contracts. `validate_contract()` rejects deviations from the
source-locked action contract.

Run `PYTHONPATH=src python3 scripts/build_c43_action_artifacts.py` to
regenerate all C43 records. The API contains no finite-basis numerical QCD
matrix generator; that work is reserved for C44/HQCD.
