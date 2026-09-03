# C46/HQCD Codex Work Package

## Title

**Source-derived physical finite-basis light-front QCD matrices: \(q/qg\) bases, exact color-triplet coupling, free Hamiltonians, canonical SU(3) vertex, instantaneous/constrained sectors, residual-boundary and zero-mode operators, local counterterm directions, and many-body comparison maps**

## Authoritative baseline

Start from the clean local C45/MODES completion commit:

```text
8ce209a8e964b01bb7a405a97ed1d2149a72930a
```

Its immediate scientific parent is:

```text
3786f003122b9e6b16abe697025c99d9b37de401
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 3786f003122b9e6b16abe697025c99d9b37de401 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION

C44_MODE_PROJECTION_INCOMPLETE

C45_SOURCE_DERIVED_MODE_PROJECTION_READY
```

and the four C45 projection contracts remain:

```text
LONGITUDINAL_CELL_AND_MEASURE:
    SOURCE_COMPLETE_EXECUTABLE

TRANSVERSE_2D_HO_AND_PHASE:
    SOURCE_COMPLETE_EXECUTABLE

SPINOR_POLARIZATION_OVERLAP:
    SOURCE_COMPLETE_EXECUTABLE

GLOBAL_COLOR_ZERO_MODE_PROJECTION:
    SOURCE_COMPLETE_EXECUTABLE
```

The fixed physical TMD architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

The selected gauge-fixed action remains:

```text
G0-LIGHT-FRONT-GAUGE

A^+ = A_- = 0
x^+ is light-front time
antisymmetric/PV inverse partial^+ on the nonzero-mode domain
explicit zero-mode projector
retained residual transverse gauge link
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

Its integer-\(K\) arrays may be used only as software-regression controls.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C46 consumes the C43 action and C45 source-derived mode library to construct the first physical, regulator-identical numerical matrices in the \(q\oplus qg\) matching-probe module.

C46 must create:

```text
physical one-quark basis arrays
physical quark-gluon product and total-color-triplet basis arrays
free q Hamiltonian
free qg Hamiltonian
canonical SU(3) q -> qg emission matrix
generated qg -> q absorption matrix
instantaneous-fermion matrices at the declared scope
instantaneous color-current/gluon matrices at the declared scope
all other C43-required constrained/contact matrices
action-owned residual-boundary matrix
C43/C45 zero-mode projectors and any required projected zero-mode operators
local Hamiltonian counterterm-direction matrices
many-body comparison maps between physical resolutions
a projected action-level current/Ward consistency identity
```

C46 does **not** construct the complete nonlocal Ji–Ma–Yuan Wilson-line matrix, the bilocal TMD measurement, nonlocal Wilson/cusp/operator counterterms, a one-loop correlator, or a matching kernel.

The strongest allowed status is:

```text
C46_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

When that gate passes, the exact next package is:

> **C47/WX — source-derived finite-basis Ji–Ma–Yuan Wilson operator, transverse closure, bilocal TMD measurement, nonlocal counterterm directions, and distributional measurement/refinement maps**

Only after C47 closes may the one-loop nonsinglet calculation resume.

---

# 2. Fixed scientific scope

The numerical root is:

```text
NONHADRONIC_COLOR_FUNDAMENTAL_MATCHING_MODULE
```

Use the exact colored-probe plan selected by:

```text
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
```

Do not assume its value from this prompt.

The retained dynamical sectors are:

\[
\mathcal H_q\oplus\mathcal H_{qg}.
\]

The declared action scope is:

```text
one external quark
one quark plus one transverse gluon
rank-zero T-even nonsinglet quark-TMD matching through O(g_s^2)
```

The following remain outside C46 unless the C43 action proves they are required as virtual or constraint partners at this order:

```text
qgg numerical sector
qqbar-pair numerical sector
hadronic qqq sectors
gluon external matching probes
T-odd matching
spin-1 nuclear composition
soft subtraction
one-loop renormalization
phenomenological calibration
```

Every C43 Hamiltonian-ledger term must nevertheless receive an explicit C46 scope decision. A missing Fock sector alone is not a proof that an action term vanishes.

---

# 3. Nonnegotiable evidence standard

Every positive matrix must descend through:

```text
locked primary-source equation
    -> C43 project-convention expression
    -> C45 mode/overlap object
    -> explicit many-body matrix-element formula
    -> deterministic sparse-matrix or LinearOperator generator
    -> application to a nonzero complex vector
    -> independent check
    -> deterministic content hash
```

For every numerical object record:

```text
primary-source locator
C43 action-term ID
C45 mode/overlap IDs
gauge convention
boundary prescription
zero-mode projector
basis normalization
color convention
helicity/polarization convention
mass/IR parameter convention
resolution
block quantum numbers
shape
dtype
nnz
units
coupling-power factor
basis-order hash
generator-code hash
array hash
independent residual
```

The following do not constitute physical matrices:

```text
a status record
a symbolic interface
a list of diagonal expectations
a hand-designed sparse texture
a C40 array with renamed labels
a matrix fitted to a desired Ward residual
```

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_gauge_constraint_derivation.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json
docs/next_level/c43_finite_basis_projection_contract.json
docs/next_level/c43_physical_resolution_plan.json

docs/next_level/c45_projection_contract_matrix.json
docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_transverse_overlap_report.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_spinor_polarization_overlap.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_zero_mode_projection_contract.json
docs/next_level/c45_numerical_object_inventory.json
docs/next_level/c45_c46_projection_interface.json
```

Consume the exact source locks retained by C43 and C45. Do not transcribe a replacement formula from memory.

Create:

```text
docs/next_level/c46_derivation_authority_manifest.json
```

---

# 5. Physical regulator and resolution identities

Consume the exact C45 longitudinal convention:

\[
-L\le x^-\le L,\qquad
p^+=\frac{\pi k}{L},\qquad
P^+=\frac{\pi K}{L},\qquad
x=\frac{k}{K}.
\]

Keep \(L\) symbolic.

The physical trajectory is:

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

Verify these identities from C43/C45 before use.

The finite one-fermion support minima are:

```text
1/9
1/11
1/13
```

at the three resolutions.

The inherited:

```text
x_min = 1/18
```

is a separate C7 endpoint-regulator parameter, not the lowest finite-mode fraction. Keep both identities separate in every basis and operator record.

Do not choose a numerical \(L\). When forming invariant-mass or dimensionless matrices, prove the required cancellation or factor the remaining \(L\)-dependence symbolically.

Create:

```text
docs/next_level/c46_physical_resolution_manifest.json
docs/next_level/c46_longitudinal_regulator_separation.json
```

---

# 6. Resource and dimension preflight

Before allocating matrices, enumerate all basis states and conserved blocks.

Report for each resolution:

```text
number of q states
number of full qg product states
number of color-triplet qg states
counts by total Jz
counts by longitudinal partition
counts by transverse excitation
expected sparse-matrix dimensions and nnz bounds
estimated memory and runtime
```

No physically allowed state may be pruned merely to fit a preferred runtime.

Allowed implementation strategies include:

```text
blockwise sparse CSR/CSC matrices
content-addressed block bundles
matrix-free LinearOperators
hybrid assembled/matrix-free representations
```

A positive gate requires deterministic access to every retained block, even when no single monolithic matrix is written.

Create:

```text
docs/next_level/c46_dimension_resource_preflight.json
```

---

# 7. Physical one-quark basis

Construct the one-quark basis from the C45 modes.

Each basis state retains:

```text
flavor-probe label
open fundamental color or selected colored-module label
light-front helicity
positive antiperiodic half-integer k
normalized transverse 2D-HO (n,m)
total Jz
center-of-mass label/policy
mass/IR parameter label
resolution
```

For a one-particle state at fixed total \(K\), enforce the exact longitudinal identity rather than admitting unrelated spectator-like modes.

Generate:

```text
basis table
basis-order hash
Gram matrix
P+ representation
transverse-momentum operators
free invariant-mass ingredients
center-of-mass diagnostics/projectors
deterministic nonzero test vectors
```

Required checks:

```text
Gram Hermiticity
positive definiteness
normalization and orthogonality
longitudinal momentum reconstruction
Jz conservation
color metric
C45 mode-array reproduction
center-of-mass policy
```

Create:

```text
docs/next_level/c46_one_quark_basis_manifest.json
docs/next_level/c46_one_quark_basis_validation.json
```

---

# 8. Physical qg product basis

Construct every allowed partition:

\[
k_q+k_g=K,
\]

where:

```text
k_q is a positive half-integer;
k_g is a positive nonzero integer.
```

Apply the exact C45 many-body \(N_{\max}\) rule and center-of-mass policy.

Every product state retains:

```text
quark and gluon longitudinal modes
quark and gluon transverse HO modes
quark helicity
gluon helicity
fundamental quark color
adjoint gluon color
total Jz
total K
zero-mode status
resolution
```

Generate:

```text
full product-basis table
Gram matrix
kinematic block labels
deterministic comparison with the C45 one-particle modes
```

Required checks:

```text
positive support
exact rational K conservation
Nmax truncation
Jz conservation
orthonormality
no ordinary gluon zero mode
center-of-mass policy
```

Create:

```text
docs/next_level/c46_qg_product_basis_manifest.json
docs/next_level/c46_qg_product_basis_validation.json
```

---

# 9. Total-color triplet basis

Consume the exact C45 color-only projector for:

\[
3\otimes8=3\oplus\bar6\oplus15.
\]

Tensor it with each kinematic qg block and construct the physical matching-module triplet basis.

Do not use:

```text
the full 24-dimensional product color space as the final qg module;
a color singlet;
a fitted Clebsch map.
```

Required checks:

```text
projector Hermiticity and idempotence
rank 3 per color-only copy
C2 = 4/3 on the image
orthogonality to 6bar and 15
total-generator covariance
basis-rotation invariance
compatibility with the selected C45 colored-module plan
```

Generate an explicit normalized triplet Clebsch/isometry:

\[
U_{3\leftarrow3\otimes8},
\]

with a deterministic phase convention.

Create:

```text
docs/next_level/c46_qg_triplet_basis_manifest.json
docs/next_level/c46_qg_triplet_basis_validation.json
```

---

# 10. Source-derived free Hamiltonians

Project the C43 free Hamiltonian into the q and color-triplet qg bases.

Use the exact C43 representation:

```text
P^-
or
the invariant-mass-squared operator
```

as fixed by the projection contract.

Do not replace the transverse kinetic operator by only its diagonal expectation unless the selected HO representation proves that form. Construct the complete retained-basis matrix from analytic HO operators and/or direct quadrature.

Factor all symbolic parameters explicitly:

```text
quark mass or common mass-IR parameter
gluon mass regulator if one exists
L dependence
bHO
K
```

Generate:

```text
assembled sparse matrices
independent matrix-free actions
direct element oracle
block spectra
```

Required checks:

```text
Hermiticity
free dispersion
symbolic/numerical L cancellation or factoring
mass-IR dependence
block conservation
assembled versus matrix-free action
analytic HO-operator versus quadrature agreement
resolution behavior
```

Create:

```text
docs/next_level/c46_free_hamiltonian_matrices.json
docs/next_level/c46_free_hamiltonian_validation.json
```

---

# 11. Canonical SU(3) q -> qg vertex

Project the exact C43 canonical interaction using the C45 local spinor/polarization overlap kernel, longitudinal modes, and transverse HO functions.

Construct the coupling-factored matrix:

\[
\widehat V_{qg\leftarrow q}
=
\frac{1}{g_s}V_{qg\leftarrow q}.
\]

Each matrix element must contain the exact:

```text
longitudinal normalization and conservation delta
source-derived spinor/polarization numerator
three-mode transverse HO overlap
fundamental SU(3) generator
fermionic sign
endpoint-regulator factor only where the C43/C45 contract assigns it
```

The C7 endpoint parameter \(1/18\) must not alter the finite mode list. If it enters a kernel, record its action separately and report whether it is active on the retained support.

Project the qg output into the exact total-color triplet.

Generate absorption solely as:

\[
\widehat V_{q\leftarrow qg}
=
\widehat V_{qg\leftarrow q}^{\dagger}.
\]

Required independent routes:

```text
direct matrix-element evaluation for frozen entries
assembled sparse action
independent transverse quadrature or analytic HO-overlap route
```

Required checks:

```text
all eight SU(3) generator actions
Tr(Ta Tb)=delta_ab/2
CF=4/3
triplet-image residual
total-color covariance
longitudinal conservation
Jz conservation
helicity selection
adjoint residual
nonzero action on normalized q vectors
```

Create:

```text
docs/next_level/c46_canonical_qg_vertex.json
docs/next_level/c46_canonical_qg_vertex_validation.json
```

No physical value of \(g_s\) or \(\alpha_s\) is chosen in C46.

---

# 12. Instantaneous-fermion sector

Project the C43 instantaneous-fermion operator using the same:

```text
PV inverse partial^+
zero-mode projector
boundary prescription
mode normalization
```

as the canonical action.

Factor:

\[
V_{\mathrm{inst},f}
=
g_s^2\widehat V_{\mathrm{inst},f}.
\]

Derive every supported q/q, q/qg, and qg/qg block from the action. Do not force a block to be nonzero or zero from its name.

Allowed block statuses:

```text
REGULATOR_IDENTICAL_EXECUTABLE_NONZERO
REGULATOR_IDENTICAL_EXECUTABLE_ZERO_BY_EXACT_PROOF
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF
ABSENT_BLOCKING
```

Required checks:

```text
inverse-derivative subspace
zero-mode exclusion/control
Hermiticity
longitudinal conservation
Jz conservation
color covariance
direct versus assembled elements
```

Create:

```text
docs/next_level/c46_instantaneous_fermion_matrices.json
```

---

# 13. Instantaneous color-current/gluon sector

Project the C43 Gauss-law-induced instantaneous interaction.

Retain distinct contributions from:

```text
quark color current
gluon color current
mixed current
boundary/zero-mode completion
```

Factor:

\[
V_{\mathrm{inst},g}
=
g_s^2\widehat V_{\mathrm{inst},g}.
\]

Required checks:

```text
same inverse-(partial^+)^2 convention as C43
Hermiticity
SU(3) covariance
triplet-subspace preservation
longitudinal conservation
current identity at declared scope
direct versus assembled matrix elements
```

Create:

```text
docs/next_level/c46_instantaneous_current_matrices.json
```

---

# 14. Remaining constrained and contact terms

Read every C43 Hamiltonian-ledger row marked:

```text
REQUIRED_AT_O_G2
REQUIRED_AS_COUNTERTERM_OR_WARD_PARTNER
```

For each row produce:

```text
a source-derived numerical matrix;
an exact projected zero with proof;
a proved not-applicable status;
or ABSENT_BLOCKING.
```

This includes, as applicable:

```text
fermion-constraint contact terms
gauge-constraint contact terms
normal-ordering/contact terms
action-owned basis-boundary terms
```

Three- and four-gluon action terms must receive an explicit q/qg-scope decision. Do not classify them by omission alone.

Create:

```text
docs/next_level/c46_constrained_operator_ledger.json
```

---

# 15. Residual-boundary and zero-mode projection

Consume the exact C45 colored-module and zero-mode plans.

Project separately:

```text
ordinary nonzero-mode action
gluon k^+=0 control
constrained fermion zero mode
global color/Gauss-law zero mode
residual transverse-gauge zero mode
action-owned boundary term
```

The complete nonlocal JMY transverse link belongs to C47. C46 constructs only action-owned boundary/zero-mode matrices required by the local Hamiltonian and projected action identity.

Every class receives:

```text
projected numerical operator
exact constrained solution
proved exclusion
external-module treatment
cancellation with declared boundary term
or blocking status
```

Create:

```text
docs/next_level/c46_boundary_zero_mode_projection.json
```

---

# 16. Projected action/current identity

Construct the strongest matrix-level identity actually implied by the C43 gauge-fixed action at the C46 \(q/qg\) scope.

Do not call it a full non-Abelian Slavnov–Taylor theorem unless that exact theorem is derived and tested.

The identity must include every required:

```text
canonical propagating term
instantaneous-fermion term
instantaneous-current/gluon term
constrained/contact term
action-owned boundary term
zero-mode contribution
```

Evaluate on multiple deterministic and random nonzero complex vectors in every retained block and resolution.

Report:

```text
full residual
component residuals
color-generator covariance residual
resolution dependence
signed defect when each required term is removed
```

A coefficient may not be tuned to force closure.

Create:

```text
docs/next_level/c46_projected_action_identity_report.json
```

---

# 17. Local Hamiltonian counterterm directions

Construct source-derived local operator directions for later one-loop renormalization:

```text
quark mass
quark field/residue
canonical qg vertex
instantaneous-partner relation
local basis-boundary/regulator direction
```

For each direction generate:

```text
matrix derivative
coupling/order label
source authority
independent finite-difference check
```

Do not solve physical coefficients.

Do not create nonlocal bilocal, Wilson-line, cusp, endpoint, or transverse-link counterterm directions in C46; those belong to C47.

Create:

```text
docs/next_level/c46_local_counterterm_directions.json
```

---

# 18. Many-body physical comparison maps

Use the C45 one-particle transverse overlaps, longitudinal distribution map, color triplet isometry, and zero-mode projectors to construct q and qg comparison maps between adjacent physical resolutions.

The longitudinal grids are nonnested. Do not claim exact embedding.

Construct:

\[
P^q_{r\to r'},\quad R^q_{r'\to r},
\]

\[
P^{qg}_{r\to r'},\quad R^{qg}_{r'\to r}.
\]

Required checks:

```text
Gram-metric adjoint relation
normalization preservation
total K and Jz bookkeeping
color-triplet preservation
reported nonnested longitudinal remainder
free-Hamiltonian consistency
canonical-vertex consistency
instantaneous-operator consistency
boundary/zero-mode consistency
```

These are comparison maps, not a continuum extrapolation or convergence proof.

Create:

```text
docs/next_level/c46_many_body_comparison_maps.json
docs/next_level/c46_many_body_comparison_validation.json
```

---

# 19. Deterministic numerical bundles

For each physical resolution, produce content-addressed runtime bundles containing at least:

```text
q basis table and Gram matrix
qg product-basis table and Gram matrix
qg triplet isometry/projector and triplet basis table
free q Hamiltonian
free qg Hamiltonian
canonical emission and absorption matrices
instantaneous-fermion matrices
instantaneous-current/gluon matrices
all required constrained/contact matrices
action-owned boundary and zero-mode matrices/projectors
local counterterm-direction matrices
many-body comparison-map blocks
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c46_hqcd/
```

Commit an inventory with:

```text
runtime path
shape
dtype
nnz
units
basis-order hash
array hash
generator command
```

Create:

```text
docs/next_level/c46_numerical_object_inventory.json
```

---

# 20. C40 method-oracle isolation

Compare C46 and C40 only as a software-method study.

Report:

```text
dimension differences
sparsity differences
norm and spectrum differences
which C40 serialization and mutation tests remain useful
```

Do not:

```text
fit C46 to C40
rescale C40 into C46
reuse a C40 numerical coefficient
claim source identity from numerical similarity
```

Create:

```text
docs/next_level/c46_c40_method_oracle_comparison.json
```

---

# 21. End-to-end source-to-matrix test

Implement an end-to-end test that starts from the C43 source/action records and C45 mode library, not from prebuilt C46 arrays.

It must:

```text
regenerate physical q and qg mode products
construct the total-color triplet
assemble free Hamiltonians
assemble the canonical SU(3) vertex
assemble instantaneous and constrained matrices
apply boundary and zero-mode contracts
construct local counterterm directions
construct comparison maps
evaluate the projected action identity
reproduce all numerical hashes
```

It must fail when:

```text
the K-to-x convention is changed
x_min=1/18 is used as the finite support minimum
L is assigned arbitrarily
a C45 mode phase changes
a Gell-Mann generator changes
the qg triplet is replaced by the full product or a singlet
a C40 matrix is substituted
an instantaneous term is removed
the inverse-derivative prescription changes
a zero-mode projector changes
the boundary term is omitted
a comparison map is replaced by coordinate interpolation metadata
```

---

# 22. Focused mutation tests

Create at least **192 focused live mutations** of actual derivations or numerical arrays.

Include mutations of:

```text
longitudinal normalization
HO kinetic operator
spinor/polarization numerator
SU(3) generator
triplet isometry
canonical-vertex transverse overlap
instantaneous denominator
zero-mode projector
boundary prescription
basis ordering
matrix adjoint
comparison-map overlap
runtime-array hash
```

Every mutation must fail a concrete normalization, symmetry, action-identity, comparison-map, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 23. Readiness gate

Issue:

```text
C46_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

only when:

```text
the complete C43 and C45 baselines reproduce;
the physical q and qg bases exist at every resolution;
the total-color qg triplet is exact;
the free Hamiltonians are source derived;
the canonical SU(3) vertex is source derived;
absorption is the generated adjoint;
every required instantaneous/constrained/contact term has an executable or proved status;
the action-owned boundary and zero-mode contracts are projected;
the projected action/current identity closes;
local counterterm directions exist;
many-body physical comparison maps exist;
all numerical bundles reproduce byte-for-byte;
the end-to-end source-to-matrix test passes.
```

Do not issue:

```text
C46_JMY_WILSON_MATRIX_VALIDATED
C46_BILOCAL_TMD_MEASUREMENT_VALIDATED
C46_ONE_LOOP_TMD_VALIDATED
C46_MATCHING_KERNEL_VALIDATED
C46_MICROSCOPIC_PROTON_TMD_EXPORTED
```

---

# 24. Exact no-go branches

## A. Many-body basis construction fails

```text
C46_PHYSICAL_BASIS_ASSEMBLY_INCOMPLETE
```

Next:

> **C47/BASIS1 — physical \(q/qg\) many-body truncation, center-of-mass, and block-assembly completion**

## B. Color-triplet coupling fails

```text
C46_QG_COLOR_TRIPLET_COUPLING_INCOMPLETE
```

Next:

> **C47/COLOR3 — exact color-fundamental \(qg\) isometry and canonical-emission image completion**

## C. Free Hamiltonian projection fails

```text
C46_FREE_HAMILTONIAN_PROJECTION_INCOMPLETE
```

Next:

> **C47/HFREE — source-derived HO kinetic and light-front free-Hamiltonian matrix completion**

## D. Canonical vertex fails

```text
C46_CANONICAL_QG_VERTEX_INCOMPLETE
```

Next:

> **C47/VERTEX1 — source-derived light-front spinor/HO/SU(3) canonical-vertex completion**

## E. Instantaneous, constrained, boundary, or zero-mode projection fails

```text
C46_CONSTRAINED_OPERATOR_PROJECTION_INCOMPLETE
```

Next:

> **C47/Z2 — action-derived instantaneous, constrained, boundary, and zero-mode matrix completion**

## F. Projected action identity fails

```text
C46_PROJECTED_ACTION_IDENTITY_FAILED
```

Next:

> **C47/G3 — missing-term and projected light-front current/Ward identity completion**

## G. Comparison maps fail

```text
C46_MANY_BODY_COMPARISON_MAP_INCOMPLETE
```

Next:

> **C47/R1D — source-overlap many-body comparison-map completion**

## H. All local QCD matrix gates close

```text
C46_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

Next:

> **C47/WX — source-derived finite-basis JMY Wilson operator, bilocal TMD measurement, nonlocal counterterm directions, and distributional/refinement maps**

---

# 25. Required deliverables

Create at least:

```text
docs/next_level/c46_implementation_report.md
docs/next_level/c46_api.md
docs/next_level/c46_derivation_authority_manifest.json
docs/next_level/c46_physical_resolution_manifest.json
docs/next_level/c46_longitudinal_regulator_separation.json
docs/next_level/c46_dimension_resource_preflight.json

docs/next_level/c46_one_quark_basis_manifest.json
docs/next_level/c46_one_quark_basis_validation.json
docs/next_level/c46_qg_product_basis_manifest.json
docs/next_level/c46_qg_product_basis_validation.json
docs/next_level/c46_qg_triplet_basis_manifest.json
docs/next_level/c46_qg_triplet_basis_validation.json

docs/next_level/c46_free_hamiltonian_matrices.json
docs/next_level/c46_free_hamiltonian_validation.json

docs/next_level/c46_canonical_qg_vertex.json
docs/next_level/c46_canonical_qg_vertex_validation.json

docs/next_level/c46_instantaneous_fermion_matrices.json
docs/next_level/c46_instantaneous_current_matrices.json
docs/next_level/c46_constrained_operator_ledger.json
docs/next_level/c46_boundary_zero_mode_projection.json
docs/next_level/c46_projected_action_identity_report.json

docs/next_level/c46_local_counterterm_directions.json
docs/next_level/c46_many_body_comparison_maps.json
docs/next_level/c46_many_body_comparison_validation.json

docs/next_level/c46_numerical_object_inventory.json
docs/next_level/c46_c40_method_oracle_comparison.json

docs/next_level/c46_readiness_report.json
docs/next_level/c46_source_sufficiency_decision.json
docs/next_level/c46_no_go_decision_tree.json
docs/next_level/c46_missing_calculation_specification.md
docs/next_level/c46_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/hqcd/
```

or the repository-equivalent package.

Add focused tests for:

```text
physical basis construction
color-triplet projection
free Hamiltonians
canonical vertex
instantaneous/constrained sectors
boundary/zero modes
projected action identity
many-body comparison maps
end-to-end source-to-matrix reconstruction
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C46 is complete only when:

1. The full C45 baseline reproduces.
2. The C44 no-go remains explicit.
3. The C43 gauge/action contract remains unchanged.
4. C40 remains method-oracle only.
5. The physical half-integer-\(K\) trajectory is used.
6. The finite support minima and endpoint regulator remain separate.
7. No arbitrary numerical \(L\) is introduced.
8. Physical q bases exist at all resolutions.
9. Physical qg product bases exist at all resolutions.
10. The exact total-color triplet basis exists.
11. The colored-module interpretation matches C45.
12. Gram and center-of-mass identities close.
13. Free q Hamiltonians are source derived.
14. Free qg Hamiltonians are source derived.
15. Assembled and matrix-free actions agree.
16. The canonical q->qg vertex is source derived.
17. Its image lies in the qg triplet.
18. Absorption is the generated adjoint.
19. Longitudinal, Jz, helicity, and color rules close.
20. Every required instantaneous-fermion block has an executable/proved status.
21. Every required instantaneous-current/gluon block has an executable/proved status.
22. Every required constrained/contact term has an executable/proved status.
23. Action-owned boundary terms are projected.
24. C43/C45 zero-mode statuses are implemented.
25. The projected action/current identity closes at its declared scope.
26. Removing every required term gives a nonzero defect.
27. Local counterterm directions are source derived.
28. Many-body comparison maps descend from C45 overlaps/functionals.
29. Nonnested longitudinal remainders remain visible.
30. Hamiltonian, vertex, and constrained-operator map residuals are reported.
31. Numerical bundles contain actual arrays, not metadata substitutes.
32. End-to-end source-to-matrix reconstruction passes.
33. At least 192 live mutations are detected.
34. No complete JMY Wilson matrix is claimed.
35. No bilocal TMD measurement is claimed.
36. No one-loop coefficient or physical counterterm solution is created.
37. No matching kernel is created.
38. No proton TMD or ART25 bridge is created.
39. No fit, inference, process, or production route is created.
40. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
41. `MSHT20_REP/` remains untouched and outside Git.
42. The working tree is clean except for the pre-existing untracked directory.
43. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken the physical basis, color representation, constrained-sector completeness, zero-mode contract, or projected action identity to open the gate.

---

# 27. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45 inputs consumed;
- physical resolution identities and resource estimates;
- q and qg dimensions by conserved block;
- color-triplet isometry/projector residuals;
- Gram and center-of-mass residuals;
- free-Hamiltonian shapes, nnz, spectra, symbolic-parameter treatment, and matrix-free residuals;
- canonical-vertex shapes, nnz, norms, color/Casimir residuals, triplet-image residual, and adjoint residual;
- instantaneous and constrained operator shapes, norms, and statuses;
- boundary and zero-mode statuses;
- projected action/current residual and every ablation defect;
- local counterterm-direction matrices;
- many-body comparison-map shapes and consistency residuals;
- runtime bundle hashes;
- C40 method-oracle comparison;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no complete JMY Wilson matrix, bilocal TMD measurement, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe source-qualified modes alone, a full \(3\otimes8\) product basis without the triplet reduction, a matrix passing only internal checks, or a projected identity with omitted required terms as source-derived finite-basis QCD.
