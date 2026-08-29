# C44/HQCD Codex Work Package

## Title

**Source-derived physical finite-basis light-front QCD Hamiltonians: normalized \(q/qg\) modes, exact SU(3) color-fundamental projection, canonical \(q\leftrightarrow qg\) vertex, instantaneous and constrained operators, residual-boundary terms, and basis-overlap comparison maps**

## Authoritative baseline

Start from the clean local C43/G0 completion commit:

```text
fbcd6ee0cf838db34d4bb1f45396d1435a14cb87
```

Its immediate scientific parent is:

```text
4c8ab287218c185509226d933c9b5585abcc4f45
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 4c8ab287218c185509226d933c9b5585abcc4f45 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL
C42_GAUGE_FIXED_ACTION_INCOMPLETE
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
```

and the exact C43 source/action contract:

```text
gauge:
    G0-LIGHT-FRONT-GAUGE

gauge condition:
    A^+ = A_- = 0

light-front time:
    x^+

inverse derivative:
    antisymmetric/PV inverse partial^+
    on the nonzero-mode domain

zero modes:
    explicit projector and declared-scope contract

residual gauge:
    retained transverse Wilson link

dynamical fields:
    psi_+
    A_perp

constrained fields:
    psi_-
    A^-

physical projection trajectory:
    inherited C32 trajectory
    K = 9/2, 11/2, 13/2
    not the C40 toy integer-K substrate
```

The fixed physical TMD architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

and may be used only for software-regression comparisons.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C44 projects the source-locked C43 gauge-fixed action into the physical finite light-front basis.

C44 must create actual source-derived numerical matrices for the action-owned \(q/qg\) sector:

```text
normalized one-quark basis
normalized quark-gluon basis
free q Hamiltonian
free qg Hamiltonian
canonical SU(3) q -> qg vertex
generated qg -> q adjoint
instantaneous-fermion operator
instantaneous color-current/gluon operator
other declared constrained/contact operators
residual-gauge boundary operator
declared-scope zero-mode operator or exact projected proof
source-derived basis comparison maps
local Hamiltonian counterterm directions
```

C44 does **not** yet project the complete nonlocal Ji–Ma–Yuan Wilson operator or the bilocal TMD measurement. Those consume the C44 field modes and Hamiltonian substrate in the next package.

C44 does **not** calculate a one-loop TMD or matching coefficient.

The strongest allowed status is:

```text
C44_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

When that gate passes, the next package is:

> **C45/WX — source-derived finite-basis Ji–Ma–Yuan Wilson operator, transverse closure, bilocal TMD measurement, nonlocal counterterm directions, and distributional measurement/refinement maps**

Only after C45 closes may a later package resume the one-loop matching calculation.

---

# 2. Fixed scientific scope

The calculation root is:

```text
NONHADRONIC_COLOR_FUNDAMENTAL_MATCHING_PROBE
```

It is not the C11 proton.

The retained Fock sectors are:

\[
\mathcal H_q
\oplus
\mathcal H_{qg}.
\]

The declared perturbative substrate scope is:

```text
one external quark
one quark-plus-one-transverse-gluon sector
terms needed for a rank-zero T-even nonsinglet quark TMD through O(g^2)
```

The following are outside C44’s positive scope unless required by an exact action-level closure:

```text
qgg numerical sector
qqq or hadronic sectors
sea-pair sectors
gluon TMD external probes
T-odd matching
spin-1 nuclear composition
one-loop soft subtraction
phenomenological calibration
```

Three- and four-gluon action terms remain in the C43 ledger and must receive a scope decision. They are not silently discarded.

---

# 3. Nonnegotiable evidence standard

Every positive numerical object must descend through:

```text
C43 primary-source locator
    -> C43 project-convention expression
    -> C44 finite-basis matrix-element formula
    -> deterministic generator
    -> numerical sparse matrix or LinearOperator
    -> application to a nonzero vector
    -> independent check
    -> content hash
```

A C43 symbolic formula is not a matrix.

A C40 matrix with changed labels is not a source-derived C44 matrix.

A numerical matrix is not source-derived merely because its symmetry checks pass.

For every generated object record:

```text
source locator
C43 derivation ID
gauge convention
field normalization
basis normalization
color convention
helicity/polarization convention
IR mass convention
resolution
shape
dtype
nnz
basis-order hash
generator-code hash
array hash
units
coupling-power convention
independent residual
```

---

# 4. Mandatory C43 inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_primary_source_manifest.json
docs/next_level/c43_source_sufficiency_matrix.json
docs/next_level/c43_gauge_plan.json
docs/next_level/c43_gauge_convention_map.json
docs/next_level/c43_light_front_conventions.json

docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_gauge_constraint_derivation.json

docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_free_propagator_checks.json

docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_residual_gauge_derivation.json
docs/next_level/c43_transverse_link_derivation.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json

docs/next_level/c43_jmy_action_compatibility.json
docs/next_level/c43_bilocal_operator_compatibility.json
docs/next_level/c43_finite_basis_projection_contract.json
docs/next_level/c43_physical_resolution_plan.json
```

Read the exact locked source TeX/PDF records for:

```text
BPP hep-ph/9705477v1
Srivastava-Brodsky hep-ph/0011372v2
BJY hep-ph/0208038v2
JMY hep-ph/0404183v1
```

Do not derive numerical formulas from memory when a source/C43 locator exists.

Create:

```text
docs/next_level/c44_derivation_authority_manifest.json
```

---

# 5. Physical resolution plan

Consume the exact C43 projection contract.

The expected inherited C32 trajectory is:

```text
R1:
    K = 9/2
    Nmax = 8
    bHO = 0.40 GeV

R2:
    K = 11/2
    Nmax = 10
    bHO = 0.45 GeV

R3:
    K = 13/2
    Nmax = 12
    bHO = 0.50 GeV
```

with the inherited declarations:

```text
fermion longitudinal modes:
    positive antiperiodic half-integers

gluon longitudinal modes:
    positive periodic nonzero integers

gluon zero mode:
    excluded from the ordinary basis
    retained through the explicit C43 zero-mode contract

transverse basis:
    normalized two-dimensional oscillator modes

mass/IR convention:
    exact C43 projection contract

center-of-mass policy:
    exact C43 projection contract
```

Verify these values from the repository before use.

If the C43 contract differs, use the C43 record and document the discrepancy. Do not silently force this prompt’s expected values.

The C40 integer-\(K\) resolutions remain separate method oracles and cannot be labeled physical refinement points.

Create:

```text
docs/next_level/c44_physical_resolution_manifest.json
```

---

# 6. Source-derived field-mode library

Implement project-normalized finite-basis mode functions for:

```text
good quark field psi_+
transverse gluon field A_perp
```

The mode library must include:

```text
longitudinal plane-wave mode
2D harmonic-oscillator transverse mode
light-front quark spinor
physical transverse gluon polarization
fundamental quark color
adjoint gluon color
creation/annihilation normalization
integration measure
```

Numerically validate:

```text
longitudinal orthogonality
transverse oscillator orthogonality
spinor normalization
polarization completeness at the selected gauge scope
canonical anticommutator
canonical commutator
resolution-specific completeness on the retained subspace
```

Create:

```text
docs/next_level/c44_mode_library_derivation.json
docs/next_level/c44_mode_library_validation.json
```

If the mode expansions cannot be made compatible with the C43 brackets, issue:

```text
C44_MODE_PROJECTION_INCOMPLETE
```

---

# 7. One-quark basis

Construct the actual color-fundamental one-quark basis at each physical resolution.

Each state retains:

```text
flavor probe label
fundamental color c = 1,2,3
light-front helicity
positive half-integer longitudinal mode
transverse radial n
transverse angular m
total Jz block
IR-mass label
resolution
```

The basis must be partitioned into conserved blocks.

Generate:

```text
basis table
Gram matrix
free P+ array
free P_perp array
free invariant-mass or P- array
deterministic coordinate vectors
```

Required checks:

```text
Gram Hermiticity
positive definiteness
normalization
orthogonality
free momentum reconstruction
Jz conservation
color metric
resolution identity
```

Create:

```text
docs/next_level/c44_one_quark_basis_manifest.json
docs/next_level/c44_one_quark_basis_validation.json
```

---

# 8. Quark-gluon basis and exact color-fundamental irrep

Construct the product basis:

\[
3\otimes 8
=
3\oplus\bar 6\oplus 15.
\]

The physical matching-probe qg sector must transform in the unique total-color triplet reached by the canonical emission vertex.

Construct the total generators:

\[
T_{\rm tot}^a
=
T_q^a\otimes I_8
+
I_3\otimes F_g^a,
\]

and derive the projector onto:

\[
C_2=\frac43.
\]

Do not impose a color singlet.

Every qg state retains:

```text
quark longitudinal and transverse modes
gluon longitudinal and transverse modes
quark helicity
gluon transverse polarization/helicity
quark fundamental color
gluon adjoint color
total-color irrep
total longitudinal momentum
total transverse/OAM label
total Jz block
zero-mode status
resolution
```

Generate:

```text
full product-basis table
triplet-projector matrix
triplet-basis vectors
qg Gram matrix
free qg kinematic arrays
```

Required checks:

```text
3 tensor 8 decomposition dimensions
triplet-projector Hermiticity and idempotence
total-generator covariance
C2 = 4/3 on the retained triplet
orthogonality to 6bar and 15
basis normalization
positive longitudinal support
total K conservation
total Jz conservation
```

Create:

```text
docs/next_level/c44_qg_color_projection.json
docs/next_level/c44_qg_basis_manifest.json
docs/next_level/c44_qg_basis_validation.json
```

---

# 9. Free Hamiltonians

Project the C43 free Hamiltonian onto the physical q and qg bases.

Construct:

\[
P^-_{0,q},
\qquad
P^-_{0,qg},
\]

and the exact project invariant-mass representation where applicable.

Factor no unphysical phenomenological interaction into these matrices.

Provide:

```text
assembled sparse matrices
independent matrix-free actions
diagonal-element direct oracle
block labels
spectra
```

Required checks:

```text
Hermiticity
free dispersion relation
mass-IR dependence
block conservation
assembled/matrix-free equality on deterministic complex vectors
direct diagonal-element agreement
resolution behavior
```

Create:

```text
docs/next_level/c44_free_hamiltonian_matrices.json
docs/next_level/c44_free_hamiltonian_validation.json
```

---

# 10. Canonical SU(3) q -> qg vertex

Project the source-derived canonical interaction onto the physical bases.

Construct the coupling-factored matrix:

\[
\widehat V_{qg\leftarrow q}
\equiv
\frac{1}{g_s}V_{qg\leftarrow q}.
\]

Do not choose or fit a physical value of \(\alpha_s\) in C44.

Each matrix element must include the exact C43-derived:

```text
spinor numerator
transverse polarization
longitudinal normalization
transverse oscillator overlap
fundamental SU(3) generator
momentum conservation
fermionic sign
```

The emission matrix must map into the total-color triplet subspace.

Generate absorption by:

\[
\widehat V_{q\leftarrow qg}
=
\widehat V_{qg\leftarrow q}^{\dagger}.
\]

Required checks:

```text
all eight Gell-Mann generator actions
Tr(Ta Tb)=delta_ab/2
CF=4/3
total-color covariance
triplet-image residual
longitudinal conservation
Jz conservation
helicity-selection rules
transverse-overlap quadrature
direct element versus assembled matrix
adjoint residual
nonzero action on a normalized q state
```

Create:

```text
docs/next_level/c44_canonical_qg_vertex.json
docs/next_level/c44_canonical_qg_vertex_validation.json
```

---

# 11. Instantaneous-fermion operator

Project the C43 instantaneous-fermion term at the declared q/qg scope.

Factor the explicit coupling power:

\[
V_{\rm inst,f}
=
g_s^2\widehat V_{\rm inst,f}.
\]

Determine the supported blocks from the action rather than from desired sparsity.

For every block, assign:

```text
REGULATOR_IDENTICAL_EXECUTABLE_NONZERO
REGULATOR_IDENTICAL_EXECUTABLE_ZERO_BY_EXACT_PROOF
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF
ABSENT_BLOCKING
```

Required checks:

```text
inverse-partial-plus prescription
zero-mode projector
Hermiticity
color covariance
longitudinal conservation
direct matrix element versus assembled matrix
```

Create:

```text
docs/next_level/c44_instantaneous_fermion_matrix.json
```

---

# 12. Instantaneous color-current/gluon operator

Project the C43 Gauss-law-induced instantaneous interaction.

Retain separately:

```text
quark-current contribution
gluon-current contribution
mixed current contribution
boundary/zero-mode term
```

Factor:

\[
V_{\rm inst,g}
=
g_s^2\widehat V_{\rm inst,g}.
\]

Required checks:

```text
same inverse-partial-plus-squared prescription as C43
Hermiticity
SU(3) covariance
current conservation at declared scope
triplet-subspace preservation
direct versus assembled matrix elements
```

Create:

```text
docs/next_level/c44_instantaneous_current_matrix.json
```

---

# 13. Other constrained and contact operators

Project every C43 Hamiltonian-ledger term marked:

```text
REQUIRED_AT_O_G2
REQUIRED_AS_COUNTERTERM_OR_WARD_PARTNER
```

This may include:

```text
fermion-constraint contact term
gauge-constraint contact term
residual boundary term
declared zero-mode control
```

Every term must have:

```text
source expression
projected matrix-element formula
numerical matrix or exact no-applicability proof
coupling power
scope
```

Create:

```text
docs/next_level/c44_constrained_operator_ledger.json
```

If any required action-owned term remains `ABSENT_BLOCKING`, the final gate is false.

---

# 14. Residual-gauge boundary operator

Project the C43 residual transverse gauge field at light-cone infinity into the declared q/qg scope.

C44 does not yet build the full JMY Wilson line. It must construct the action-owned boundary field/operator needed by C45.

Record:

```text
boundary prescription
future/past orientation
transverse field mode content
zero-mode relation
color action
matrix blocks
```

Required checks:

```text
residual-gauge transformation
Hermiticity/conjugation
boundary-prescription dependence
nontrivial ablation in the projected gauge identity
```

Create:

```text
docs/next_level/c44_residual_boundary_matrix.json
```

---

# 15. Zero-mode projection

Apply the exact C43 zero-mode contract.

For each zero-mode class, produce one of:

```text
projected numerical operator
exact constrained contribution
proved exclusion with a tested projector
blocking unresolved contribution
```

At minimum retain separate decisions for:

```text
gluon longitudinal k+ = 0
fermion constrained zero mode
residual transverse gauge zero mode
global color-constraint zero mode
```

A projector that removes the ordinary-basis zero mode is not by itself a proof that the operator contribution vanishes.

Create:

```text
docs/next_level/c44_zero_mode_projection.json
```

---

# 16. Matrix-level gauge/current identity

Construct the exact projected identity supported by the C43 action.

Do not label it a full non-Abelian Slavnov–Taylor theorem unless the source and calculation actually establish that scope.

The identity must include every required projected term:

```text
canonical propagating vertex
instantaneous fermion
instantaneous current/gluon
constrained/contact terms
residual boundary term
zero-mode contribution
```

Evaluate it on multiple nonzero complex vectors in every supported resolution/block.

Required output:

```text
full residual
component residuals
signed defect when each required term is removed
gauge-convention identity
color-generator covariance residual
```

Create:

```text
docs/next_level/c44_projected_ward_current_report.json
```

---

# 17. Local Hamiltonian counterterm directions

Construct source-derived operator directions needed for later partonic renormalization:

```text
quark mass direction
quark field/residue direction
canonical vertex direction
instantaneous-partner direction
basis-boundary/local regulator direction
```

C44 does not determine their physical one-loop coefficients.

For each direction provide:

```text
operator derivative
matrix
source/action authority
coupling/order
independent finite-difference check
```

Do not include the nonlocal bilocal, Wilson-line, cusp, or transverse-link counterterms; those belong to C45.

Create:

```text
docs/next_level/c44_local_counterterm_directions.json
```

---

# 18. Physical basis comparison maps

Construct comparison maps from actual normalized mode overlaps.

For adjacent physical resolutions:

\[
P_{r\to r'},
\qquad
R_{r'\to r},
\]

provide maps for:

```text
q basis
qg triplet basis
```

The longitudinal grids are generally nonnested. Do not assert exact embedding unless proved.

For the transverse oscillator basis, calculate the overlap integrals at differing \(N_{\max}\) and \(b_{\rm HO}\).

Required checks:

```text
Gram-metric adjoint relation
normalization preservation
K-support map
reported nonnested remainder
free-Hamiltonian consistency
canonical-vertex consistency
instantaneous-operator consistency
boundary-operator consistency
```

Create:

```text
docs/next_level/c44_basis_comparison_maps.json
docs/next_level/c44_basis_comparison_validation.json
```

---

# 19. Deterministic numerical bundles

For every physical resolution, produce a deterministic runtime bundle containing at least:

```text
q basis table and Gram matrix
qg product and triplet basis tables
qg triplet projector and Gram matrix
free q Hamiltonian
free qg Hamiltonian
canonical emission and absorption matrices
instantaneous-fermion matrix
instantaneous-current/gluon matrix
other required constrained/contact matrices
residual-boundary matrix
zero-mode projectors/operators
local counterterm-direction matrices
```

Store heavy arrays under a content-addressed runtime directory.

Commit a numerical inventory containing:

```text
runtime path
shape
dtype
nnz
basis-order hash
array hash
generator command
```

Create:

```text
docs/next_level/c44_numerical_object_inventory.json
```

---

# 20. C40 method-oracle comparison

Compare the physical C44 matrices with C40 only as a software-method audit.

Report:

```text
shape differences
norm differences
spectrum differences
sparsity differences
which C40 tests remain reusable
```

Do not:

```text
fit C44 to C40
rescale C40 into C44
use numerical similarity as source identity
```

Create:

```text
docs/next_level/c44_c40_method_oracle_comparison.json
```

---

# 21. End-to-end source-to-matrix test

Implement an end-to-end test that begins from the C43 source/action records and regenerates the C44 matrices.

It must:

```text
load source and convention identities
generate physical modes
construct q and qg bases
project the qg color triplet
assemble free Hamiltonians
assemble the canonical vertex
assemble instantaneous/constrained operators
assemble the residual-boundary and zero-mode objects
apply the projected gauge/current identity
construct comparison maps
verify numerical hashes
```

It must fail when:

```text
a C43 source locator is removed
a plus/minus convention changes
a mode normalization changes
a Gell-Mann generator changes
the qg triplet projector is replaced by a singlet or full-product identity
a C40 toy matrix is substituted
an instantaneous term is removed
the inverse-derivative prescription changes
the boundary term is removed
a zero-mode projector changes
a comparison map is replaced by coordinate interpolation metadata
```

---

# 22. Focused mutation tests

Create at least 192 focused source-to-matrix mutations.

Mutate actual formulas or arrays, including:

```text
spinor normalization
polarization vector
longitudinal mode weight
oscillator normalization
SU(3) generator
triplet projector
mass-IR term
canonical vertex numerator
instantaneous denominator
zero-mode projector
boundary prescription
matrix adjoint
basis-order hash
comparison-map overlap
```

Every mutation must fail a concrete derivation, symmetry, current, or deterministic-hash test.

Do not inflate the count with identifier-only dispatch.

---

# 23. Readiness gate

Issue:

```text
C44_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

only when:

```text
the C43 action/source baseline reproduces;
all physical modes are source normalized;
the q and qg bases exist at all physical resolutions;
the qg total-color triplet is exact;
the free Hamiltonians are source derived;
the canonical SU(3) vertex is source derived;
all required instantaneous and constrained operators are projected;
the boundary and zero-mode contracts are projected;
the matrix-level gauge/current identity closes;
local counterterm directions exist;
physical basis comparison maps exist;
all numerical bundles reproduce byte-for-byte;
the end-to-end source-to-matrix test passes.
```

Do not issue:

```text
C44_JMY_WILSON_MATRIX_VALIDATED
C44_BILOCAL_TMD_MEASUREMENT_VALIDATED
C44_ONE_LOOP_TMD_VALIDATED
C44_MATCHING_KERNEL_VALIDATED
C44_MICROSCOPIC_PROTON_TMD_EXPORTED
```

---

# 24. Exact no-go branches

## A. Physical mode projection fails

```text
C44_MODE_PROJECTION_INCOMPLETE
```

Next:

> **C45/MODES — source-normalized longitudinal/transverse light-front mode completion**

## B. qg color-fundamental projection fails

```text
C44_QG_COLOR_TRIPLET_INCOMPLETE
```

Next:

> **C45/COLOR3 — exact \(3\otimes8\to3\) light-front color-coupling completion**

## C. Free Hamiltonians or canonical vertex fail

```text
C44_HQCD_CANONICAL_SECTOR_INCOMPLETE
```

Next:

> **C45/HQCD1 — source-derived free and canonical \(q\leftrightarrow qg\) matrix completion**

## D. Instantaneous or constrained sectors fail

```text
C44_CONSTRAINED_OPERATOR_PROJECTION_INCOMPLETE
```

Next:

> **C45/Z2 — instantaneous, constrained, boundary, and zero-mode matrix completion**

## E. Gauge/current identity fails

```text
C44_PROJECTED_GAUGE_IDENTITY_FAILED
```

Next:

> **C45/G3 — projected light-front Ward/current identity and missing-term completion**

## F. Comparison maps fail

```text
C44_BASIS_COMPARISON_MAP_INCOMPLETE
```

Next:

> **C45/R1D — source-overlap physical basis comparison-map completion**

## G. All gates close

```text
C44_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

Next:

> **C45/WX — source-derived finite-basis Ji–Ma–Yuan Wilson operator, bilocal TMD measurement, nonlocal counterterm directions, and distributional/refinement maps**

---

# 25. Required deliverables

Create at least:

```text
docs/next_level/c44_implementation_report.md
docs/next_level/c44_api.md
docs/next_level/c44_derivation_authority_manifest.json
docs/next_level/c44_physical_resolution_manifest.json

docs/next_level/c44_mode_library_derivation.json
docs/next_level/c44_mode_library_validation.json

docs/next_level/c44_one_quark_basis_manifest.json
docs/next_level/c44_one_quark_basis_validation.json
docs/next_level/c44_qg_color_projection.json
docs/next_level/c44_qg_basis_manifest.json
docs/next_level/c44_qg_basis_validation.json

docs/next_level/c44_free_hamiltonian_matrices.json
docs/next_level/c44_free_hamiltonian_validation.json

docs/next_level/c44_canonical_qg_vertex.json
docs/next_level/c44_canonical_qg_vertex_validation.json

docs/next_level/c44_instantaneous_fermion_matrix.json
docs/next_level/c44_instantaneous_current_matrix.json
docs/next_level/c44_constrained_operator_ledger.json
docs/next_level/c44_residual_boundary_matrix.json
docs/next_level/c44_zero_mode_projection.json

docs/next_level/c44_projected_ward_current_report.json
docs/next_level/c44_local_counterterm_directions.json

docs/next_level/c44_basis_comparison_maps.json
docs/next_level/c44_basis_comparison_validation.json

docs/next_level/c44_numerical_object_inventory.json
docs/next_level/c44_c40_method_oracle_comparison.json

docs/next_level/c44_readiness_report.json
docs/next_level/c44_source_sufficiency_decision.json
docs/next_level/c44_no_go_decision_tree.json
docs/next_level/c44_missing_calculation_specification.md
docs/next_level/c44_regression_report.json
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and numerical bundles must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C44 is complete only when:

1. The full C43 baseline reproduces.
2. The C43 gauge/action/source contract remains unchanged.
3. C40 remains method-oracle only.
4. The physical C32/C43 half-integer-\(K\) trajectory is used.
5. Source-normalized quark modes are generated.
6. Source-normalized transverse-gluon modes are generated.
7. Canonical brackets are reproduced on the retained subspace.
8. Physical q bases exist at all declared resolutions.
9. Physical qg product bases exist at all declared resolutions.
10. The exact \(3\otimes8\to3\) projector is constructed.
11. The retained qg states have \(C_F=4/3\).
12. Free q Hamiltonians are source derived.
13. Free qg Hamiltonians are source derived.
14. Assembled and matrix-free actions agree.
15. The canonical q->qg vertex is source derived.
16. Its image lies in the total-color triplet.
17. Absorption is the generated adjoint.
18. Helicity, momentum, color, and Jz rules close.
19. Instantaneous-fermion blocks receive executable/proved statuses.
20. Instantaneous-current/gluon blocks receive executable/proved statuses.
21. Every required constrained/contact term receives an executable/proved status.
22. Residual-boundary terms are projected.
23. Zero-mode statuses implement the C43 contract.
24. The projected gauge/current identity closes at its declared scope.
25. Removing every required term gives a nonzero defect.
26. Local Hamiltonian counterterm directions are source derived.
27. Physical comparison maps descend from mode overlaps.
28. Nonnested longitudinal remainders remain visible.
29. Hamiltonian and vertex comparison-map residuals are reported.
30. Numerical bundles contain actual arrays, not metadata substitutes.
31. End-to-end source-to-matrix reconstruction passes.
32. At least 192 focused live mutations are detected.
33. No JMY Wilson matrix or bilocal TMD matrix is claimed.
34. No one-loop coefficient or physical counterterm solution is created.
35. No matching kernel is created.
36. No proton TMD or ART25 bridge is created.
37. No fit, inference, process, or production route is created.
38. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
39. `MSHT20_REP/` remains untouched and outside Git.
40. The working tree is clean except for the pre-existing untracked directory.
41. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken source normalization, color representation, constrained-sector completeness, zero-mode ownership, or gauge/current closure to open the gate.

---

# 27. Final Codex response

Report:

- full starting and final commits;
- exact C43 source/action inputs consumed;
- physical resolution identities;
- mode-library formulas and normalization residuals;
- q and qg dimensions by conserved block;
- \(3\otimes8\) decomposition and triplet-projector residuals;
- Gram residuals;
- free-Hamiltonian shapes, nnz, spectra, and matrix-free residuals;
- canonical-vertex shapes, nnz, norms, color/Casimir residuals, and adjoint residuals;
- instantaneous and constrained operator shapes, norms, and statuses;
- residual-boundary and zero-mode statuses;
- projected gauge/current residual and every ablation defect;
- local counterterm-direction matrices;
- comparison-map shapes and consistency residuals;
- numerical bundle hashes;
- C40 method-oracle comparison;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no complete JMY Wilson matrix, bilocal TMD measurement, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an action contract, a C40 toy matrix, a color-product basis without the triplet projection, or a matrix passing internal checks as source-derived finite-basis QCD.
