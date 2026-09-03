# C6 active-gluon implementation report

## Declared scope

C6 is a validation-only active-gluon, one-Wilson-order extension of C5. It is
not a gluon TMD extraction, physical soft-subtracted correlator, evolution
input, nuclear object, inference model, or process prediction.

The implemented chain is:

`C4 qqqg state and positive-x gluon slot -> C5 paths/poles/resolvent/cuts ->
ordered adjoint link pair -> common active-gluon tensor -> explicit
three-adjoint color ordering -> independent f/d RED maps -> C4 transverse
polarization RED maps -> full pair reversal -> analytic MATCH-class
half-soft subtraction`.

## Dynamical phase

Each leg has the C5 convention-derived distribution

`1/(v·l-i0 eta) = PV(1/(v·l)) + i eta pi delta(v·l)`.

The active-gluon absorptive contribution requires nonzero coupling, declared
cut support, the explicit ordered color coupler, `Lz=0`/`|Lz|=1`
interference, and all active-field/left-link/right-link/spectator
attachments. Removing coupling, cut support, or OAM produces exact zero.
Finite epsilon remains a numerical convergence oracle inherited from C5 and
does not occur in a C6 result identity.

## Color and polarization

Explicit ordered traces give

`2[Tr(Ta Tb Tc)-Tr(Tb Ta Tc)] = i f^{abc}`

and

`2[Tr(Ta Tb Tc)+Tr(Tb Ta Tc)] = d^{abc}`.

The measured norms are 24 and 40/3, with zero `f·d`. Normalized projections
reconstruct the declared `f/d` subspace, while an injected tensor outside
that subspace retains a nonzero orthogonal residual. There is no default
`f+d` mixture or process color weight.

One tensor parent supplies trace, helicity-antisymmetric, and
symmetric-traceless projections in both color channels. Exact reconstruction
is checked independently for `f` and `d`.

## Soft and rapidity benchmark

For an explicit shared overlap coefficient `A`, the benchmark uses

`W_unsub = W_finite + A L_rap`,

`S^(1) = 2 A L_rap`,

and `W_sub = W_unsub - S^(1)/2`.

Thus `d W_sub / d L_rap = 0`. Omitting the half-soft subtraction gives `+A`;
duplicating it gives `-A`. UV finite matching remains
`UNRESOLVED_NOT_ZERO`. Only `BOUNDARY_ONLY_RESCATTERING` is executable;
`JOINT_MICROSCOPIC_SOFT_SECTOR` is explicitly unimplemented and mutually
exclusive.

## Boundaries

The finite cut and overlap two-cells do not complete the general Volume 0
`Provenance2Complex`. Remaining Volume III work includes second and higher
Wilson orders, strict non-Abelian ordering convergence, all-sector Ward
closure, a complete continuum rapidity/soft scheme, and LF-to-QCD matching.
Volumes IV, V, and VI remain fail-closed.

Machine-readable residuals and identities are in
`c6_benchmark_manifest.json`; immutable regression evidence is in
`c6_regression_report.json`.
