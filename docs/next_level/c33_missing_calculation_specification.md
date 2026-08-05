# Missing C33 finite-basis one-loop soft calculation

## Exact obstruction

C33 closes the distinct B=0 root, direct-Fock plan, vacuum normalization,
four-line color/path identity, and `S_FB^(0)=1`. It does not calculate any
regulator-specific one-loop coefficient. The exact typed outcome is

```text
C33_SOFT_TREE_LEVEL_ONLY
```

and the exact continuation is

```text
C34/S0A — one-loop soft diagram, counterterm, and rapidity-renormalization completion
```

The missing result is not a fit parameter and is not zero. It is

\[
S_{\rm FB}^{\rm bare}(b;\Lambda_{\rm soft},\delta^\pm,\xi_g)
=1+a_s S_{\rm FB}^{(1),\rm bare}
+\mathcal O(a_s^2),
\qquad
S_{\rm FB}^{(1),\rm bare}=\mathrm{NONZERO\_UNKNOWN}.
\]

## Regulator identity that must be frozen

C34/S0A must use the selected `S0-FB-EIKONAL-FOCK` root without modifying C11
or C32. Before evaluating a graph, it must freeze and hash:

- the complete vacuum plus one-gluon basis at three or more nested resolutions,
  including normalization and completeness relations;
- both `n` and `nbar` rapidity regions, transverse modes, polarizations, all
  eight adjoint colors, boundary conditions, endpoints, and the retained/tested
  zero-mode policy;
- the four fundamental/conjugate Wilson paths, trace order, future/past
  orientation, path ordering, transverse closure, b-space measurement, and
  Fourier phase/normalization;
- the modified-delta `delta+` and `delta-` prescription, its ordered eikonal
  denominators, line-conjugation rule, regulator-removal order, and relation to
  the rapidity scale;
- the finite-basis UV regulator and target MSbar convention, with logarithmic
  and linear/power divergences kept separate;
- covariant gauge and the frozen `xi_g=0,1,2` holdouts;
- a common partonic IR prescription compatible with the C32 spacelike
  off-shell checks at `p^2=-0.04,-0.09 GeV^2` and momenta 5 and 10 GeV, or a
  proved conversion that retains the same overlap limit.

The basis cutoff must not be relabeled as the rapidity regulator, and a finite
numerical epsilon must not become physical support.

## Required bare contributions

Calculate in the finite basis, rather than copying from the continuum, every
coefficient in the following ledger:

```text
N_NBAR_EXCHANGE
CONJUGATE_LINE_EXCHANGE
SAME_DIRECTION_LINE_EXCHANGE
REAL_ONE_SOFT_GLUON
VIRTUAL_ONE_SOFT_GLUON
WILSON_LINE_SELF_ENERGY
CUSP_ENDPOINT
TRANSVERSE_CLOSURE
AUXILIARY_FIELD_SELF_ENERGY
SOFT_VACUUM_ENERGY
LIGHT_FRONT_INSTANTANEOUS
GAUGE_FIXING
GHOST
ZERO_MODE
BASIS_BOUNDARY
RAPIDITY_COUNTERTERM
UV_COUNTERTERM
RESIDUAL_LINE_MASS_COUNTERTERM
```

For each entry provide the line pair, cut/virtual classification, color factor,
gauge dependence, UV/IR/rapidity/basis and b dependence, symbolic derivation,
numerical implementation, cancellation partners, and holdout. An absent graph
may be assigned zero only with a regulator- and gauge-specific proof.

The sum must demonstrate Hermitian conjugation, exact color-singlet
normalization, T-even future/past equality, transverse-rotation covariance,
real/virtual count-once behavior, b-to-zero behavior in the declared source
convention, and basis completeness at each resolution.

## UV and rapidity renormalization

Derive, in the same finite basis, the Wilson-line self-energy, cusp, endpoint,
transverse-link, vacuum-energy, and any auxiliary residual-line-mass
counterterms. Separate cutoff logarithms from linear/power divergences and show
that the state-independent UV factor produces the target soft anomalous
dimension.

Next derive the modified-delta rapidity counterterm and form

\[
S_{\rm FB}^{\rm ren}=Z_S^{\rm UV}R_S^{\rm rap}S_{\rm FB}^{\rm bare}.
\]

The calculation must show cancellation of the bare delta dependence, gauge
parameter independence, basis independence up to a declared remainder,
future/past equality, and path independence of the rapidity evolution. Extract
the rapidity anomalous dimension and Collins-Soper/D-function only from this
renormalized result and test its mu derivative against the cusp anomalous
dimension in the selected source convention. Do not fit a nonperturbative
Collins-Soper model.

## Continuum oracle and finite-basis conversion

Reconstruct the one-loop continuum modified-delta soft function through two
independent routes: the source expression and an independent symbolic or direct
integral. Align Wilson geometry, color representation, b and Fourier
conventions, MSbar normalization, modified-delta prescription, and rapidity
derivative convention. Retain logarithms and finite constants separately.

The continuum result is an oracle. It becomes a conversion only after the
finite-basis result exists. Determine

\[
S_{\rm cont}^{\rm ren}
=Z_{\rm FB\to cont}^{S}S_{\rm FB}^{\rm ren}
+R_{\rm FB\to cont}^{S}
\]

with separate logarithmic, finite, power-suppressed, endpoint, zero-mode, and
numerical pieces. Validate the inverse, round trip, UV and rapidity anomalous
dimensions, gauge independence, b dependence, state/hadron/ART25 independence,
and resolution trajectory. Three plan records without calculated observables do
not satisfy this requirement.

The auxiliary-field papers permit an independent methodological oracle. To use
that route as more than an oracle, prove the Euclidean/spacelike-to-Minkowski
map, lightlike/modified-delta identity, endpoint/cusp and residual-mass
renormalization, transverse segment composition, and agreement with the direct
finite-Fock calculation. Never add the direct and auxiliary results.

## C32 compatibility and zero-bin closure

Construct an explicit compatibility matrix for gauge group/representation,
four-line geometry, b measurement, Fourier convention, UV target scheme,
modified-delta convention, IR prescription, boundary/zero-mode treatment,
overlap region, and regulator-removal order.

Evaluate the C32 collinear operator's soft limit with the same IR and rapidity
prescriptions and validate

\[
\operatorname{ZERO\_BIN}:\operatorname{COLL}_{\rm C32}
\rightarrow\operatorname{SOFT\_LIMIT}_{\rm C33}.
\]

Show both the missing-subtraction and duplicate-subtraction residuals and
establish count-once placement before inverse-square-root soft allocation. The
typed `DEFINED_NOT_VALIDATED` interface is not enough.

This calculation must address the source limitation directly:
arXiv:hep-ph/0702022 establishes the compared soft/zero-bin equivalence with DR
as the IR regulator and states that off-shellness is not a suitable automatic
equivalence regulator. The frozen C32 off-shell plan therefore needs an
operator-identical derivation or proved conversion; citation to the DR result
cannot validate compatibility.

## Closure gates

Only calculated quantities may populate numerical residuals. To issue
`C33_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING`, all of the following must pass:

- complete B=0 vacuum basis and four-line operator;
- exact tree normalization;
- one-loop bare soft sum;
- UV and rapidity renormalization;
- gauge and future/past closure;
- source-qualified continuum oracle;
- three-or-more-point finite-basis trajectory;
- finite-basis-to-continuum conversion and round trip;
- C32/C33 regulator compatibility;
- validated zero-bin interface.

Until then, all one-loop coefficients, counterterms, anomalous dimensions,
conversion coefficients, residuals, and trajectory corrections remain
`NONZERO_UNKNOWN`; compatibility remains
`SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED`; and the continuation gate remains
false.

## Scope exclusions

C34/S0A must not use ART25 members, data, chi2 values, bridge residuals, or a
hadron-level ratio to select or tune a coefficient. It must not mutate the C11
proton state, export a microscopic proton TMD, rerun the twelve-point bridge,
or create a fit, calibration, likelihood, posterior, optimization, reweighting,
emulator, process bridge, physical claim, inference status, or production
status.

The implementation points to extend are
`src/deuteron_wigner/bridge/s0/core.py`, `tests/test_c33_s0.py`,
`scripts/build_c33_manifests.py`, and `scripts/validate_c33.py`.
