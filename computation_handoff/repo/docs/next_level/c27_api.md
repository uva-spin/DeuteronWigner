# C27/P1C validation API

`deuteron_wigner.process.p1c` provides immutable identities for the direct
author transfer of `MSHT20_REP`, its members, and indivisible ART25 joint
members. Resolution is fail-closed: indices are neither wrapped, clipped,
renamed, converted, nor replaced.

`scripts/run_c27_art25.py` initializes the unchanged ARTEMIDE v3.01 engine and
executes content-addressed member ranges. Independent processes are the only
parallel unit because ARTEMIDE's selected PDF and FF replicas are global
runtime state. `scripts/build_c27_manifests.py` reconstructs the complete
source locks, execution summaries, covariance, gates, and regression records.
`scripts/validate_c27.py` checks their scientific invariants.

These interfaces are research-validation infrastructure. They create no fit,
posterior, likelihood, deuteron prediction, or production route.
