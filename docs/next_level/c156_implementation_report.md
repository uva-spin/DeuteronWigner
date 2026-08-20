# C156/HQCDMATCHGRID2 implementation report

Status: `C156_HQCDMATCHGRID2_COMMON_IR_NUMERICAL_INCOMPLETE`.

Plan `MATCHGRID2-D` is selected. The immutable evaluator requires an explicit
grid record and exactly one parameter record or C144 fixture. It freezes gate
thresholds, returns complete gate vectors, preserves disconnected intervals,
and rejects unadmitted caller scales.

C153 exposes symbolic common-IR cancellation and perturbative-order records,
but no numerical common-IR residual/remainder evaluator or authority-derived
positive scale bracket. Consequently K9, K11, and K13 component windows and
their signed-mass/coupling intersection are empty. No 2 GeV, mZ, physical
scale, threshold, PDG input, inverse conversion, or physical target is used.

C155 proves exact u/d window covariance by block identity; no flavor average
is performed. The narrow continuation is `C157/HQCDMATCHIR2`.
