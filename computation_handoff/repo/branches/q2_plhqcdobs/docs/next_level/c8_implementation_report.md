# C8/H1 implementation report

## Result and scope

C8 solves the first interacting microscopic eigenproblem in the project. It
extends, rather than duplicates, the exact C7 resolution identities and
retains only the color-singlet antisymmetric \(qqq\) sector. The package is a
finite valence-sector Hamiltonian-EFT validation benchmark. It is isolated
from every accepted phenomenological production root.

The primary proton/neutron, \(J^z=\pm\tfrac12\) tower has dimensions 4, 7,
and 10 at three distinct \(K,N_{\max},b\) resolutions. Its states carry exact
longitudinal partitions, radial index, \(L_z=-1,0,1\), light-front spin,
pair-spin, color-singlet, permutation, CM, target, and resolution identity.
Comparison maps are explicit isometries.

## Hamiltonian and assumption branches

The finite mass-squared operator contains typed free, induced Jacobi-IR
confinement, effective color-spin, shared light-quark mass counterterm, and
truncation-discrepancy blocks. Three immutable plans are compiled:

- H1-PLAN-A: resolution-refitted confinement plus effective color-spin;
- H1-PLAN-B: zero confinement plus effective color-spin;
- H1-PLAN-C: resolution-refitted confinement without color-spin.

Their identities are distinct and mutually exclusive. The color-spin term is
explicitly `ALTERNATIVE_TO_EXPLICIT_QQQG_DYNAMICS`; no overlap subtraction
exists yet, so both routes cannot be selected. Omitted \(qqqg\), sea,
higher-orbital, zero-mode, instantaneous, and basis-tail terms are recorded
as unimplemented rather than assigned zero.

At every resolution the shared mass condition fixes the benchmark ground
mass to \(M^2=0.88^2\ {\rm GeV}^2\) through a resolution-dependent mass
counterterm. Induced coefficients are independently refitted and their
Jacobian, Hessian spectrum, naturalness combinations, residuals, and
comparison-map identities are exported. Fitting this validation reference
does not establish a physical nucleon or continuum trajectory.

## Current and holdouts

The vector current is owned by the exact Hamiltonian identity. It uses exact
quark flavor charges and one shared block normalization, never a
transfer- or component-specific factor. Proton \(F_1(0)=1\) closes;
neutron \(F_1(0)=0\) is a correlated isospin-partner prediction. Nonzero
transfer proton and neutron matrix elements and a second current-component
extraction remain holdouts. The component defect is reported, not fitted
away.

## Solvers, state tracking, and tensor network

Every block is solved by dense Hermitian diagonalization and a matrix-free
Krylov operator. Eigenpair and current-matrix-element agreement are recorded.
State identities across resolutions use exact quantum numbers, comparison
overlaps, current fingerprints, principal angles, and a largest-component
real-positive phase convention.

Benchmark H-J contains a controlled avoided crossing. Eigenvalue-order
tracking follows the wrong branch, while overlap tracking recovers the
intended state.

The TTN uses the three-quark coupling tree
`((q1,q2)->(Rc,Rf,S,Lz,alpha),q3)->(I,Jz,color singlet)`. Every index carries
physical mode, helicity, flavor/isospin, color, permutation, \(J^z\), and
resolution data. Forbidden blocks are absent. Full-bond tensorization
reconstructs the exact state, and a genuine nested Rayleigh--Ritz
optimization supplies the fixed-bond variational solutions. Energy is
nonincreasing with bond capacity, full bond agrees with the exact oracle, and
the deliberately low-rank state misses a measurable OAM/current feature.
This finite \(qqq\) result is not evidence that the full QCD Fock state has
low entanglement.

## Benchmarks and validation

H-D verifies exact pole-mass and charge invariance in a two-/three-sector
self-energy toy while bare and counterterm values flow. H-H reports the
current-component defect across the tower. H-J validates state tracking. H-K
compares confinement routes. H-TN validates exact representation,
variational convergence, recoupling, and tensor-operator application.
H-PLAN compiles and executes all three assumption branches.

Machine-readable evidence covers 104 requirements and 56 deliberate fault
injections. Numerical tolerances and residuals are centralized in
`c8_tolerance_manifest.json`; immutable regression evidence is in
`c8_regression_report.json`.

## Readiness

C8 issues only qualified H1 validation statuses for the basis tower,
Hamiltonian, flow, current, state tracking, TTN representation/optimization,
and assumption compiler. It does not issue physical-nucleon, production
current, GTMD, Wilson, nuclear, LF-to-QCD, inference, or TMD readiness.

The exact next package is C9/H2: introduce the dynamical \(qqqg\) sector,
sector-dependent renormalization, instantaneous partners, Ward closure,
gluon/OAM exports, and a controlled microscopic reconnection boundary to the
C5/C6 Wilson engine.
