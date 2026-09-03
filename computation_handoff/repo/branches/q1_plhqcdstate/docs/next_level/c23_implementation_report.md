# C23/P0 analytic-validation implementation report

C23 implements only the corrected analytic process compiler. It consumes the
438 `ANALYTIC_PROCESS_ORACLE_ELIGIBLE` identities from C22Q and rejects all 102
`NOT_PROCESS_ELIGIBLE` identities. Source-qualified and physical-input sets are
empty and no API can execute them.

The operational baseline is `5fbb194b...`. Its direct scientific parent is
`a1527fec32c07865de34d14dc1345ca9e816fac8`. The longer hash previously written
as `a1527fef...` was an erroneous expansion of the valid short hash `a1527fe`;
Git ancestry resolves the provenance without changing either commit.

## Implemented analytic process layer

Immutable process, measurement, harmonic, hard, partner, fixed-order, and
factorization/Glauber identities are implemented under
`deuteron_wigner.process.p0`. DY uses past-pointing links and a second analytic
hadron TMD. Current-fragmentation SIDIS uses future-pointing links and an
explicit z-scaled analytic TMD-FF interface. A conditional heavy-quark-pair DIS
record provides the selected gluon-sensitive analytic benchmark with its own
soft/color certificate. Back-to-back colored hadroproduction is a BROKEN
negative control and cannot construct a universal-TMD product.

The 23-function spin-1 kinematic basis is enumerated and classified. T-odd
members remain unavailable. Inclusive b1 and tagged DIS identities are
preserved but operator-specifically unavailable. The nuclear compiler selects
only the NN same-local-operator assumption plan; it does not construct a
matched deuteron total or silently import NNPI, DeltaDelta, six-quark,
transition, hidden-color, or coherent components.

For every rank zero through three, the code supplies an analytic W, its
same-order asymptotic expansion, a fixed-order oracle, and Y=FO-asymptotic.
Only ranks zero and two have eligible input identities and therefore execute as
process oracles; ranks one and three exercise the mathematical oracle while
remaining process-unavailable. Every returned observable is
`VALIDATION_ONLY`. Boundary parameters are not retuned to improve matching.

## Nonclaims

All hard, partner, fragmentation, fixed-order, CS/large-b, and experimental
objects are synthetic. There is no physical covariance, fit, likelihood,
posterior, source-qualified cross section, physical prediction, inference
route, or production route. The production registry remains 216 and the eight
authoritative artifacts are unchanged.
