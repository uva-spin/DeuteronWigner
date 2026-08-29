# C3 implementation report

C3 implements a validation-only analytic common-overlap pilot beside the
accepted model. Starting commit:
`5063c002e763f3d6a0affc774ec6b124a539f0be`.

New package `src/deuteron_wigner/pilot/` provides typed zero-skewness fibers,
intrinsic configurations, the single symmetric recoil map, analytic states,
one diagonal zeroth-rescattering `AMP` kernel and evaluator, a separate C2
reduction bridge, and disjoint provenance.

Benchmarks:

* A: one-body recoil and vector current close exactly at one.
* B: the common evaluator agrees with an independent Gaussian oracle over a
  deterministic grid and satisfies forward/Hermiticity identities.
* C: real amplitudes give exact phase-odd zero, a controlled complex member
  activates algebraic interference, and the 4x4 helicity matrix closes.
* D: `epsilon_abc/sqrt(6)` has unit norm, is annihilated by total SU(3)
  generators, gives proton counts `u=2,d=1`, and maps reversibly to neutron
  counts through represented isospin.

Residual categories and tolerances are separated in
`c3_benchmark_manifest.json`. All 24 required injections are enumerated in
`c3_injection_manifest.json`.

The accepted 216 reductions, C2 graph, default plan, production builder route,
and eight authoritative artifacts remain unchanged. The final suite passes
538/538 tests; all nine builders, 36/36 evidence rows, and 162/162 atlas pages
pass. Counts and hashes are in `c3_regression_report.json`. The local
completion commit is reported operationally after creation because a commit
cannot contain its own hash.

Recommended next package: **C4 — validation-only minimal sea/gluon sectors and
common TMD/GPD/PDF/current route closure (Volume II Benchmarks E–F)**. Keep
these sectors disconnected from accepted production; begin dynamical
Wilson-line work only after common-parent reduction closure passes.
