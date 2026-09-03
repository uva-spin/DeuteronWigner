# C262/HQCDC117CONTLOOP1 Codex Work Package

## Mission

Evaluate and independently reduce the C261 eight-topology D-dimensional
one-loop program for `PROJECT_C117_RI_SMOM_V1`. Produce projected bare
amplitudes, UV poles and finite parts, RI/SMOM and MSbar-NDR renormalization
matrices, evanescent finite subtraction, the RI/SMOM-to-MSbar conversion
matrix, anomalous dimensions, and declared uncertainties.

Do not evaluate the finite-C43 adapter or solve C117 coefficients.

## Baseline and provenance

Start from the C261 completion commit in AUTOPILOT_STATE.json. Frozen C261
package root:

```text
b8326f78014113be619c70f2c6f8a8174d55c80b11892a4cd9ef2b41b762b4b2
```

Read and hash-verify the committed C261→C262 contract, C261 source-locator,
tensor-basis, diagram inventory, symbolic-program, amplitude, matrix, RG,
uncertainty, release/runtime manifests, every C260 scheme-definition record,
and the exact C259 source archives.

## Frozen authority

Preserve `PROJECT_C117_RI_SMOM_V1`, Landau gauge, symmetric Euclidean
nonexceptional kinematics, C260 operator/projector ordering, NDR
anticommuting-gamma5 nonsinglet scope, MSbar target convention, all eight C261
topologies, and the exact formulas `C=Z_MSbar (Z_RISMOM)^-1` and
`gamma=-mu dZ/dmu Z^-1`.

Keep physical/EOM/BRST-exact/evanescent sectors, source/color order, flavors,
orientations, units, boundaries, links, holonomies, Abel topology,
K9/K11/K13, C166, and Q0/Q1/Q2 separate. Never push.

## Strict claim boundary

Every nonzero or zero loop entry requires an explicit algebraic or symmetry
derivation. Absence in related bilinear/four-quark literature is not a zero.
Published RI/SMOM matrices for other bases are method/check authorities, not
C117 numerical data.

No finite-C43 coefficient, physical observable target, physical Hamiltonian,
PennyLane activation, spectrum, TMD, or production object is created.

## Mutually exclusive plans

Select exactly one:

```text
C117CONTLOOP1-A  complete one-loop conversion matrix and uncertainty ready
C117CONTLOOP1-B  master-integral reduction ready; exact master evaluation remains
C117CONTLOOP1-C  tensor/color/evanescent reduction ready; IBP reduction remains
C117CONTLOOP1-D  additional EOM/BRST/evanescent operator required
C117CONTLOOP1-E  two valid reduction routes contradict after convention audit
C117CONTLOOP1-F  no lawful standard conversion exists
```

Plans B/C/D are positive continuations when they publish a smaller exact
executable frontier. They are not blockers.

## Construction

Materialize each C261 topology with explicit momentum routing, D-dimensional
measure, denominators, C117 numerator tensor, ordered SU(3) color, Landau
propagator, source/sink orientation, symmetry factor, dual projector and
counterterm ownership. Demonstrate count-once completeness.

Implement two independent routes:

```text
Route A: Feynman parameters, tensor decomposition, symmetric master integrals;
Route B: algebraic tensor/color projection followed by IBP/basis reduction or
         an independent momentum-routing/basis-reversal calculation.
```

Perform exact D-dimensional Dirac/color algebra and retain O(epsilon) terms
that multiply UV poles. Include quark/source wavefunction factors,
EOM/BRST-exact nuisance subtraction and the C260 evanescent finite convention.

Publish, order by order:

```text
A_bare = I + a_s(A_pole/epsilon + A_finite);
Z_RISMOM;
Z_MSbar;
C_MSbar<-RISMOM;
gamma;
Sigma composition interface;
Ward/ST and alternate-projector residuals;
gauge-parameter cancellation/scope;
scale, scheme, evanescent and integration uncertainties.
```

Verify UV-pole cancellation in the conversion matrix and route parity entry by
entry. If master values cannot be lawfully completed, preserve them as named
exact integrals with contours/prescriptions and select the smallest B/C
continuation. Never insert remembered constants.

## Public API, validation, and continuation

Provide immutable safe-loading records with separate input, topology,
algebra, reduction, master, amplitude, pole, finite, Z, conversion, gamma,
Ward/ST, uncertainty, residual, release, scope and package roots.

Run all C250-C261 adjacent tests and C262 tests; source hashes/locators; two
route inventories and reductions; routing reversal; basis reversal; UV and IR
classification; pole cancellation; evanescent changes; gauge/BRST/ST checks;
RG composition/reversal; flavor and threshold separation; nonconsumption of
finite-C43/K9/K11/K13; safe loading; restart/sharding/paging/query order; two
deterministic builds; protected paths; and at least 384 live mutations.

Create exactly one local completion commit and never push. If plan A succeeds,
continue to the finite-C43 adapter. Otherwise create exactly one smallest
calculation continuation. Generate its full prompt, atomically update state,
and continue immediately. Stop only for a schema-certified real math/physics
blocker, exceptional infrastructure blocker, or PENNYLANE_PHYSICAL_ACTIVE.
