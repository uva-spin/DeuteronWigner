# C158/HQCDFBNUM implementation report

The C158 authority is source-derived from the public C144 sparse polynomial
and exact derivative APIs, with C131 retained-term ownership as the explicit
coupling-power authority. It constructs immutable data-only coefficient DAGs,
algebraic degree components, sparse two-by-two projected resolvent series,
source/contact ledgers, quantity-specific coefficients, and componentwise
numerical enclosures.

The package intentionally publishes finite-basis values only. It does not
evaluate a continuum target, a common-IR difference, a perturbative
remainder, a scale bracket, a physical input, running, thresholds, a
counterterm, or a matching window. Missing q-qbar, gg, qgg, zero-mode,
boundary, and full-QCD 1PI sectors remain explicitly unavailable rather than
being assigned zero.

The selected plan is FBNUM-A. The sole continuation is C159/HQCDMATCHIR3.
