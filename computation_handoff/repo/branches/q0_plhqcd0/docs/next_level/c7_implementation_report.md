# C7/H0 implementation report

## Scope and scientific boundary

C7 introduces a validation-only microscopic light-front Hamiltonian spine. It
does not replace, tune, or feed the accepted phenomenological production
model. The implementation realizes the finite H0 basis, free invariant-mass
operator, and one reduced canonical \(qqq\leftrightarrow qqqg\) vertex needed
to test whether the proposed formal architecture can carry exact discrete
quantum numbers and complete color structure.

It makes no claim to a physical nucleon eigenstate, continuum or
renormalized QCD, a GTMD overlap, a microscopic Wilson line, nuclear
matching, or inference. Those capabilities remain fail-closed.

## Implemented physics

- `HamiltonianResolution` stores exact longitudinal resolution \(K\), BLFQ
  \(N_{\max}\), oscillator scale \(b\), Hamiltonian scale, endpoint regulator,
  boundary conditions, and a deterministic identity. Scale types cannot be
  silently interchanged.
- Fermion longitudinal modes are positive half-integers; boson modes are
  positive integers. Exact `Fraction` arithmetic enforces total \(K\), total
  \(J^z\), transverse cutoff, charge, parton content, and excluded gluon zero
  modes.
- The retained sectors are \(qqq\), \(qqqg\), and \(qqqq\bar q\), with
  proton/neutron and \(J^z=\pm\tfrac12\) blocks kept distinct.
- Complete SU(3) invariant subspaces are computed as common nullspaces of the
  total generators, including the anti-fundamental action
  \(-T^{a\,T}\). Their singlet multiplicities are exactly 1, 2, and 3.
- Fermion exchange uses an exact signed permutation representation and an
  idempotent Hermitian antisymmetrizer before operator assembly.
- The H-A free operator evaluates
  \(M_0^2=\sum_i(\langle k_{\perp i}^2\rangle+m_i^2)/x_i\), with the
  two-dimensional oscillator expectation and an independent Gauss--Laguerre
  quadrature oracle. Matrix-free and assembled actions agree.
- The H-B reduced vertex uses a shared coupling, explicit \(t^a\) color
  action, longitudinal conservation, transverse/helicity factors, the
  declared endpoint regulator, normalization, and fermion sign. Absorption
  is generated as the adjoint of emission.
- Center-of-mass factorization and Lawson diagnostics are explicit gates, not
  assumed properties.

The reference basis is deliberately small: dimensions \(1,2,3\) for the
three sectors at each of the three benchmark resolutions
\((N_{\max},b/{\rm GeV})=(8,0.40),(8,0.45),(10,0.50)\). These are architecture
benchmarks, not convergence claims.

## Quantitative validation

The generated manifests cover 74 stable requirements and 48 deliberate
negative injections. The color multiplicities are \(1,2,3\); all exact
selection rules are tested exactly. Numerical residuals and the common
declared tolerance are recorded in
`c7_tolerance_manifest.json`. H-A covers nine free blocks and H-B covers 12
proton/neutron and helicity vertex blocks, including random complex
superpositions. The complete repository regression, legacy builders,
evidence matrix, atlas, immutable-output hashes, and C5/C6 hashes are recorded
in `c7_regression_report.json`.

## Provenance and isolation

The H0 provenance graph has no path to production, nuclear, evolution,
process, or inference roots. Its nodes have the scope
`C7_H0_VALIDATION_ONLY`. No TMD-specific coefficient, accepted parent,
registry entry, production artifact, or Volume 0--VII source was changed.
Volumes VI and VII are preserved byte-for-byte with pinned source hashes and
are indexed alongside Volumes 0--V.

## Readiness and next work

Validated now: basis types, color multiplicities, permutation basis,
center-of-mass gate, free operator, and term interface.

Unavailable now: physical nucleon eigenstates, renormalization trajectories,
currents, GTMD overlaps, microscopic Wilson lines, nuclear matching,
light-front-to-QCD matching, and inference.

The next package is **C8/H1: valence-sector Hamiltonian and
renormalization-flow benchmark**. It must add controlled \(qqq\)
interactions/induced confinement, current operators, small-tower
diagonalization, state tracking, and mass/current flow while remaining
explicitly valence-only.
