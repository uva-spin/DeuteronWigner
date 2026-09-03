# WP12 scientific inspection before item 6

Decision: **ready for item 6**.

The inspected canonical boundary is `outputs/parent_tmds/wp12_canonical_composed_quark.csv` and `outputs/parent_tmds/wp12_canonical_composed_gluon.csv`. Legacy coefficient responses are not carried into evolution: ordered joint-spin CP maps replace shadowing, antishadowing, and off-shell blocks, while the sourced NNpi correlator is included once.

## Quantitative findings

- All 18 quark and 18 gluon TMDs are finite and nonzero somewhere away from the kinematic origin on all five x nodes.
- Minimum density eigenvalues: quark 0.000412612, gluon 0.020881.
- Maximum rank-weighted ratios to f1: quark 1, gluon 1.
- Maximum CP recomposition shifts: quark 2.7259% and gluon 2.9080% of the local f1 reference.
- Staple-reversal residuals: quark 0.000e+00, gluon 1.285e-09 GeV^-2.
- No final positivity contraction was required after the canonical composition; the common completion scale is exactly one.

## Scientific interpretation

Close u/d curves are expected for a dominantly isoscalar deuteron; the implementation nevertheless preserves distinct u, d, ubar, dbar inputs and interfaces. Bare high-rank coefficients are not compared directly because their tensors contain explicit powers of kT/M; all acceptance bounds use rank-weighted combinations.

## Remaining model dependence entering item 6

- CP polarized/tensor response strengths are phenomenological, not globally fitted.
- Shared Fock/OAM and DeltaDelta/hidden-color/SRC parents are correlated zero-centered alternatives.
- Gluon f/d universal components still require observable-specific hard-color weights.
- The boundary is fixed at Q=5 GeV; complete rank-aware evolution is precisely item 6.
- Available fit/lattice covariance remains heterogeneous and must stay as named axes.

These are named evolution/fit uncertainties, not unresolved WP12 composition defects.
