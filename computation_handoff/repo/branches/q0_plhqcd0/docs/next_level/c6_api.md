# C6 validation-only active-gluon API

The package `deuteron_wigner.pilot.active_gluon` extends, rather than
duplicates, the C1–C5 type spine.

## Ordered operator identity

- `OrderedAdjointLinkPair` stores the left and right C5
  `BareWilsonSegment`s in exact order, their independent transverse closures,
  endpoint fibers, orientations, adjoint representation, and trace closure.
  Pair swapping and one-leg reversal create different identities.
- `ActiveGluonOperatorId` decorates the pair with the two field-strength
  indices, `GLUON` species, `DIAGONAL_ADJOINT` status, Wilson order, regulator,
  soft route, scheme status, and C4 state-member identity.

Four link words are supported as separate validation identities:
`[+,+]`, `[-,-]`, `[+,-]`, and `[-,+]`. No word implies an `f` or `d` color
class.

## Common tensor and dynamics

- `ActiveGluonKernelInput` retains the C4 `qqqg` state ancestry, the explicit
  positive-x active-gluon slot, C5 resolvent and cut ledger, both link
  attachments, color ordering, OAM blocks, exchanged-gluon identity, and the
  full restricted Ward attachment set.
- `ActiveGluonRescatteringKernel` derives both pole signs from the paths and
  creates one first-order absorptive tensor. Coupling, cut support, color
  coupling, OAM interference, and the complete attachment set are mandatory.
- `ActiveGluonTensorParent` stores one AMP-class tensor with axes for target
  helicities, active-gluon helicities, transverse indices, and three adjoint
  color indices. It exists before all color and polarization RED maps.

## Color and polarization reductions

- `ThreeAdjointColorKernel` is built from explicit forward/reversed ordered
  fundamental-generator traces. Their difference produces `i f^{abc}` and
  their sum produces `d^{abc}`.
- `ColorChannel.F_TYPE` and `D_TYPE` use normalized projections `1/24` and
  `1/(40/3)`. `decompose()` always returns the orthogonal residual.
- `GluonPolarizationView` reuses the C4 trace, helicity-antisymmetric, and
  symmetric-traceless projectors. All six color/polarization views descend
  from one tensor parent.

## Reversal, matching, and status

- `OrderedPairAntiunitaryReversal` transforms both paths, endpoints,
  momentum fibers, target/gluon helicity phases, color ordering, transverse
  indices, and projection identity before forming link-even or link-odd
  combinations.
- `AnalyticSoftOverlap` is a MATCH-class boundary-only first-order benchmark.
  It records shared collinear/soft ancestry and performs exactly one
  half-soft subtraction. Missing and duplicate subtraction have opposite
  nonzero rapidity derivatives.
- `C6OverlapLedger` records finite cut-equivalence, overlap-subtraction,
  alternative-route, additive, and remainder relations.
- `ActiveGluonResultEnvelope` carries all validation and unresolved matching
  statuses and rejects production, Volume IV, Volume V, and Volume VI use.

Every registry and result record is deterministically serialized by
`scripts/build_c6_manifests.py`.
