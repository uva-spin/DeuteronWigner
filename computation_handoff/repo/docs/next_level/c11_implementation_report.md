# C11/H4 implementation report

## Scope and result

C11 constructs a common microscopic, zero-skewness, nonzero-transverse-
transfer GTMD validation parent from the H3 quark-antiquark-gluon state. The
implementation is finite-basis, Wilson order zero, T-even, and explicitly
unmatched. It preserves the accepted phenomenological model and every C3/C4
analytic benchmark.

The package-specific formal contract is Volume XI,
`references/volume_xi_microscopic_nonzero_transfer_gtmds.tex`, preserved at
SHA-256 `d66450bb7f21bf0464b926a3480594da3be1ed009948a8031f4b4cb2756b915d`.

Both H3 theories are compiled independently. PLAN-A retains owned chiral
pair dynamics; PLAN-B disables that interaction. They share code and
conventions but are never summed. Their state, resolution, recoil, grid,
quadrature, projector, link-order, and scope identities survive every H4
object.

## Kinematics and amplitudes

Incoming and outgoing fibers use the symmetric frame with xi=0 and
transverse momenta minus/plus DeltaT/2. H4 calls the single C3
`SymmetricXiZeroRecoil`; it contains no local active or spectator recoil
formula. Its existing closure checks prove intrinsic closure, unchanged
spectator physical momenta, active transfer DeltaT, unit Jacobian, reversal,
and permutation covariance.

The wave-function evaluator contracts the actual H3 coefficient vector with
the finite longitudinal/transverse mode functions used by this validation
Hamiltonian. Exact-vector and full-bond TTN routes are identical by
construction and test. Low bond removes coefficients rather than
renormalizing the state, so OAM-sensitive loss remains observable.

## Common helicity parent

One typed overlap engine covers the four H3 sectors and yields a 4x4 joint
target-parton helicity matrix for every combination of proton/neutron and
`u`, `d`, `ubar`, `dbar`, or gluon. Flavor weights are distinct; neutron
composition is explicitly transformed and is not copied from the proton.
Antiquarks are direct positive-x slots. The gluon path retains its ordered
adjoint identity even though the Wilson operator is the identity at this
order.

At generic non-collinear kinematics, normalized Pauli tensor products span
the complete joint helicity space. A computed Gram matrix has rank 16 and
generates the dual coefficients. Labels map the quark space to 4 F, 4 G,
and 8 H amplitudes and the gluon space to trace, helicity/circular, and
linear/symmetric-traceless sectors. The maximum reconstruction residual is
2.78e-17. At DeltaT=0 or collinearity, H4 selects a declared rank-8 reduced
basis and refuses a singular inversion; it never presents a pseudoinverse
as coefficient determination.

## Closures

Transfer reversal gives M(-DeltaT)=M(DeltaT)^dagger at operator level. The
light-front parity adapter is declared on fibers and helicities. Future/past
formal alternatives agree at Wilson order zero, and all quark and gluon
link-odd quantities are exactly zero.

Direct forward reduction and both sequential regulated routes consume the
same parent ID and close without named-function normalization. Quarks and
positive-x antiquarks remain separate; the gluon moment convention is
`H_g=xg`. Vector, axial, and EMT diagnostics use the same parent values and
include two nonzero-transfer holdouts per target. The tensor route returns
`LOCAL_TENSOR_OPERATOR_UNAVAILABLE`; no external tensor charge is imposed.
PCAC/pion-pole ownership remains in H3 and is not counted twice.

The Wigner convention is `exp(-i bDelta dot DeltaT)`. Wigner-moment,
transfer-derivative, and H3 ledger routes share an explicit canonical-OAM
adapter. Their algebraic residual is zero and the finite-difference residual
is below 2.4e-9. This is not a claim that canonical and kinetic OAM are
scheme-independent.

Forward matrices are Gram matrices and have minimum eigenvalue above the
declared negative roundoff tolerance. Nonforward matrices are tested with
operator-norm Cauchy bounds, not PSD. Wigner negativity is allowed and no
eigenvalue or named-function clipping exists.

Twelve convergence axes are reported separately: longitudinal resolution,
transverse/UV support, infrared scale, Fock content, OAM support,
exact/Krylov, exact/full-bond, finite bond, kT quadrature, DeltaT derivative,
Wigner quadrature, and Gram conditioning/rank. Representative density,
helicity, chiral-odd, gluon, antiquark, OAM, and EMT observables are present.

## Replacement and readiness

H4 structurally benchmarks the immutable C3 and C4 analytic parents. A
`REPLACES_WITHIN_SCOPE` edge activates only under the C11 H4 validation
root, for supported species at xi=0 and Wilson order zero. It does not force
numerical equality and cannot reach the 216-route production registry.
Rollback is removal of that validation root.

Issued statuses are limited to microscopic parent, projector, T-even
forward, current/EMT, Wigner/OAM, scoped replacement, and nuclear-helicity
interface validation. Physical GTMD/PDF/TMD, Wilson/T-odd, nuclear matching,
LF-to-QCD matching, evolution, process, inference, and production promotion
remain closed.

## Reproduction

```bash
PYTHONPATH=src python scripts/build_c11_manifests.py 893
PYTHONPATH=src python scripts/validate_c11_architecture.py
PYTHONPATH=src python -m pytest -q
```

The manifest builder is deterministic. C11 adds 104 ordered negative
injections and 285 stable requirements.
