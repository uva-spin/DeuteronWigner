# C47/BASIS1 Codex Work Package

## Title

**Intrinsic two-body BLFQ projection and finite-volume action normalization: \(x\)-scaled \(qg\) Jacobi/center-of-mass basis, all-mode canonical kernel, residual-boundary/zero-mode functionals, and physical block-assembly contract**

## Authoritative baseline

Start from the clean local C46/HQCD fail-closed completion commit:

```text
3bf4da30bc672ff933aa3caf66c0c34c387dd08d
```

Its immediate scientific parent is:

```text
8ce209a8e964b01bb7a405a97ed1d2149a72930a
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 8ce209a8e964b01bb7a405a97ed1d2149a72930a HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION

C45_SOURCE_DERIVED_MODE_PROJECTION_READY

C46_PHYSICAL_BASIS_ASSEMBLY_INCOMPLETE
```

and preserves the C46 conclusion that the one-particle C45 library is valid but insufficient for physical matrix construction because the following four projected structures are absent:

```text
1. source-qualified x-scaled qg intrinsic/center-of-mass projection;

2. action-normalized finite-volume free-operator convention;

3. an all-mode canonical local interaction kernel;

4. a local residual-boundary/zero-mode functional.
```

The fixed physical TMD architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

The fixed action remains:

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

and cannot supply any physical C47 coefficient or basis transformation.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C47 closes the many-body projection layer that lies between:

```text
C43:
    source-derived gauge-fixed action

C45:
    source-derived one-particle longitudinal, HO, spinor,
    polarization, color, and zero-mode library

C48:
    future source-derived physical q/qg Hamiltonian matrices
```

C47 must construct the **physical basis and matrix-element contracts**, not the final action matrices.

It must provide:

```text
source-qualified x-dependent two-body transverse coordinates;
an exact product-HO to intrinsic/CM transformation;
a selected and validated CM-removal prescription;
physical q and qg basis tables and block identities;
the finite-volume normalization of the projected free operator;
an exhaustive all-mode canonical q->qg kinematic kernel;
local inverse-derivative, boundary, and zero-mode functionals;
basis-level comparison maps between physical resolutions;
a unique C48 source-to-matrix assembly interface.
```

C47 must not construct:

```text
the final free-Hamiltonian matrices;
the final SU(3) q->qg matrix;
instantaneous-interaction matrices;
the complete JMY Wilson matrix;
the bilocal TMD measurement;
physical counterterm coefficients;
a one-loop result;
a matching kernel.
```

The strongest allowed status is:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY
```

When that gate passes, the exact next package is:

> **C48/HQCD — assemble the source-derived physical free Hamiltonians, canonical SU(3) vertex, instantaneous/constrained operators, action-owned boundary/zero-mode matrices, local counterterm directions, and projected action identity**

---

# 2. Scientific boundary

C47 is:

```text
physical q/qg basis specific
intrinsic/CM-factorization specific
finite-volume normalization specific
open-color matching-module specific
source first
deterministic
validation only
```

C47 is not:

```text
a phenomenological Hamiltonian model
a proton state
a full physical colored Hilbert state
a one-loop calculation
a Wilson-line calculation
a TMD calculation
a continuum extrapolation
a fit or inference package
```

Do not choose a familiar BLFQ convention merely because it yields convenient matrices. Every retained convention must be mapped to C43 and C45.

---

# 3. Evidence standard

Every positive C47 object must descend through:

```text
primary-source equation
    -> exact C43/C45 convention map
    -> symbolic two-body formula
    -> deterministic numerical evaluator
    -> applied basis transformation or functional
    -> independent check
    -> content hash
```

For every generated object record:

```text
source locator
source version
C43 action ID
C45 mode IDs
longitudinal fraction convention
transverse scaling convention
CM/intrinsic convention
finite-volume normalization
boundary prescription
zero-mode projector
resolution
shape
dtype
units
basis-order hash
generator-code hash
array hash
independent residual
```

A one-particle product basis without an intrinsic/CM projection is not a physical qg basis.

A diagonal free-energy formula without the finite-volume state normalization is not a projected free operator.

A frozen three-point overlap test is not an all-mode canonical kernel.

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json
docs/next_level/c43_finite_basis_projection_contract.json

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

docs/next_level/c46_implementation_report.md
docs/next_level/c46_source_sufficiency_decision.json
docs/next_level/c46_missing_calculation_specification.md
```

Use actual filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c47_derivation_authority_manifest.json
```

---

# 5. Primary-source closure

Reuse the C43/C45 source locks, including:

```text
hep-ph/9705477v1
hep-ph/0011372v2
hep-ph/0208038v2
hep-ph/0404183v1
arXiv:0905.1411
arXiv:1311.2980
```

Acquire and hash-lock the exact official arXiv PDF and source archive for:

```text
arXiv:1911.10762
    a concrete two-body BLFQ mass-squared implementation and
    longitudinal/transverse basis application
```

Audit any additional primary source required for:

```text
x-dependent transverse scaling;
two-dimensional Talmi-Moshinsky/Jacobi transformation;
exact CM factorization or Lawson separation;
finite-volume light-front state normalization;
all-mode q->qg matrix-element normalization.
```

Do not assume that `1911.10762` or the two already locked BLFQ papers uniquely fixes every required convention. If an exact equation remains absent, locate and lock the required authority or fail closed.

Classify sources as:

```text
X_SCALED_TRANSVERSE_AUTHORITY
INTRINSIC_CM_TRANSFORMATION_AUTHORITY
FINITE_VOLUME_STATE_NORMALIZATION_AUTHORITY
FREE_OPERATOR_NORMALIZATION_AUTHORITY
CANONICAL_KERNEL_AUTHORITY
BOUNDARY_ZERO_MODE_FUNCTIONAL_AUTHORITY
METHOD_ONLY
NOT_PROJECT_CONVENTION_IDENTICAL
```

Create:

```text
docs/next_level/c47_primary_source_manifest.json
docs/next_level/c47_source_relevance_matrix.json
```

---

# 6. Four-blocker contract

Create an exact four-row matrix:

```text
X_SCALED_QG_CM_PROJECTION
FINITE_VOLUME_FREE_OPERATOR_NORMALIZATION
ALL_MODE_CANONICAL_KERNEL
LOCAL_BOUNDARY_ZERO_MODE_FUNCTIONAL
```

Every row must contain:

```text
source authorities
equation locators
source convention
C43/C45 convention
conversion
symbolic implementation
numerical validation
holdout
status
```

Allowed statuses:

```text
SOURCE_COMPLETE_EXECUTABLE
SOURCE_COMPLETE_REQUIRES_LIMIT
CONFLICT_REQUIRES_DECISION
ABSENT_BLOCKING
```

The positive C47 gate requires all four rows to be:

```text
SOURCE_COMPLETE_EXECUTABLE
```

Create:

```text
docs/next_level/c47_basis_assembly_contract_matrix.json
```

---

# 7. Longitudinal fractions and two-body partitions

Consume the exact C45 convention:

\[
-L\le x^-\le L,\qquad
p_i^+=\frac{\pi k_i}{L},\qquad
P^+=\frac{\pi K}{L},\qquad
x_i=\frac{k_i}{K}.
\]

Keep \(L\) symbolic.

At each physical resolution enumerate every qg partition:

\[
k_q+k_g=K,
\]

with:

```text
k_q:
    positive antiperiodic half-integer

k_g:
    positive periodic nonzero integer
```

Retain exact rational:

```text
x_q
x_g
x_q+x_g=1
```

identities.

Keep:

```text
finite one-fermion support minima:
    1/9, 1/11, 1/13

C7 endpoint regulator:
    1/18
```

strictly separate.

Create:

```text
docs/next_level/c47_qg_longitudinal_partition_manifest.json
```

---

# 8. Source-derived \(x\)-scaled transverse variables

Determine the exact source convention for transforming the one-particle transverse momenta into:

```text
a total transverse/CM coordinate;
an intrinsic qg relative coordinate.
```

Candidate formulas seen in the literature may involve quantities such as:

```text
p_i_perp / sqrt(x_i)
sqrt(x_i) r_i_perp
x-weighted relative momentum
```

but C47 must not hard-code any candidate from memory.

Derive and store:

```text
forward transformation
inverse transformation
Jacobian
canonical/symplectic relation
units
Fourier-conjugate coordinates
behavior at x_q+x_g=1
endpoint behavior
relation to the C45 HO scale
```

Required checks:

```text
total transverse momentum reconstruction
intrinsic boost invariance
unit or exact declared Jacobian
orthogonality of CM and intrinsic coordinates
coordinate/momentum Fourier compatibility
controlled endpoint behavior
```

Create:

```text
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_x_scaled_coordinate_validation.json
```

---

# 9. Product-HO to intrinsic/CM transformation

Construct the exact two-dimensional transformation from the C45 one-particle HO product:

\[
|n_q m_q\rangle
\otimes
|n_g m_g\rangle
\]

to:

```text
intrinsic relative HO state
CM HO state
```

at every allowed \((x_q,x_g)\).

Use an exact source-qualified 2D Talmi-Moshinsky/Jacobi transformation or an independently validated direct-overlap construction.

Generate transformation matrices:

\[
U_{\rm TM}(x_q,x_g;b_{\rm HO}).
\]

Required checks:

```text
unitarity/isometry on the retained complete shell
inverse transformation
total HO-quanta conservation
total OAM conservation
phase convention
direct four-dimensional quadrature
independent recurrence or analytic bracket route
endpoint stability
```

Do not infer the transformation from coordinate matching alone.

Create:

```text
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_qg_tm_validation.json
```

---

# 10. Many-body \(N_{\max}\) and intrinsic truncation

Derive the exact many-body truncation rule from the selected source.

Keep separate:

```text
sum of single-particle HO quanta;
intrinsic HO quanta;
CM HO quanta;
total Jz;
longitudinal K.
```

Determine whether the physical basis is defined by:

```text
a total single-particle Nmax cutoff;
an intrinsic Nmax cutoff;
a joint intrinsic-plus-CM cutoff;
another exact source rule.
```

Do not silently replace one rule by another.

Create:

```text
docs/next_level/c47_many_body_truncation_contract.json
```

---

# 11. Center-of-mass removal plan

Compile mutually exclusive plans:

```text
BASIS1-EXACT-CM-GROUND-PROJECTION

BASIS1-LAWSON-SEPARATION

BASIS1-PROJECTION-PLUS-LAWSON-CROSSCHECK

BASIS1-CM-UNAVAILABLE
```

Select exactly one primary physical plan before declaring a qg basis.

For an exact projection, construct:

\[
P_{\rm CM,0}.
\]

For a Lawson plan, derive the exact CM Hamiltonian and subtraction constant in the project convention:

\[
H_{\rm Lawson}
=
\lambda_{\rm CM}
\left(H_{\rm CM}-E_{\rm CM,0}\right),
\]

without choosing \(\lambda_{\rm CM}\) to improve a desired spectrum.

Required checks:

```text
projector Hermiticity and idempotence
CM-ground-state eigenvalue
intrinsic/CM factorization
independence of intrinsic test operators
Lawson-shift behavior where used
no removal of physical intrinsic states
```

Create:

```text
docs/next_level/c47_cm_plan.json
docs/next_level/c47_cm_factorization_report.json
```

---

# 12. Physical q and qg basis assembly

Using the selected colored-module plan and the C45 rank-three color projector, construct:

```text
physical one-quark basis table;
qg product basis table;
qg intrinsic/CM basis table;
CM-clean qg basis table;
total-color-triplet qg basis table.
```

Every final qg state retains:

```text
K
x_q and x_g
intrinsic HO labels
CM HO labels and projected status
quark helicity
gluon helicity
total Jz
color-triplet component
zero-mode status
resolution
```

Generate actual basis isometries and Gram matrices, but do not assemble Hamiltonian or interaction matrices.

Required checks:

```text
orthonormality
basis completeness within the declared truncation
CM-ground projection
color-triplet rank and covariance
K conservation
Jz conservation
no ordinary gluon zero mode
deterministic basis ordering
```

Create:

```text
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json
```

---

# 13. Finite-volume free-operator normalization

Resolve the C43 ambiguity in the projected free operator.

Determine from the exact light-front convention whether C48 must project:

```text
P^-;
2 P^+ P^- - P_perp^2;
an equivalent invariant-mass operator;
or another exact action-owned normalization.
```

Do not hard-code the factor of two from memory. Derive it from the C43 metric and field normalization.

Derive the complete relation among:

```text
continuum delta-function normalization;
finite-box Kronecker normalization;
longitudinal factors of L;
transverse HO measure;
one-particle state normalization;
two-particle state normalization;
operator matrix-element normalization;
coupling-power factoring.
```

Define executable scalar/function-level evaluators for the free q and qg operator on every basis state.

C47 may generate diagonal/free functional arrays for validation, but it must not label them final Hamiltonian matrices.

Required checks:

```text
free dispersion relation
symbolic L cancellation or explicit factoring
one-particle and qg normalization
CM/intrinsic separation
continuum large-box limit
direct action-density integration
agreement with the source invariant-mass formula
```

Create:

```text
docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_free_operator_functional_validation.json
```

---

# 14. Exhaustive all-mode canonical local kernel

Upgrade the finite set of C45 overlap tests into a source-derived evaluator over every allowed physical mode tuple.

The kernel must combine:

```text
finite-volume longitudinal normalization;
exact longitudinal conservation;
C45 light-front spinor/polarization numerator;
x-scaled intrinsic/CM HO transformation;
three-mode transverse overlap;
helicity and Jz selection;
boundary and zero-mode domain restrictions.
```

Keep SU(3) and \(g_s\) factored separately for C48.

Define a deterministic sparse tuple table:

```text
incoming q basis ID
outgoing physical qg basis ID
kinematic kernel value
selection-rule reason
derivation ID
```

Required independent checks:

```text
direct coordinate/momentum integration
intrinsic-basis evaluation
selected analytic HO/TM route
conjugation relation
all-mode selection-rule exhaustion
massless and finite-mass controlled limits
resolution reproduction
```

A three-point or representative-mode oracle is insufficient.

Create:

```text
docs/next_level/c47_all_mode_canonical_kernel.json
docs/next_level/c47_all_mode_kernel_validation.json
```

---

# 15. Local inverse-derivative functional

Use the exact C43 antisymmetric/PV prescription and the C45 projectors.

Construct mode-index functionals for:

\[
\frac{1}{\partial^+},
\qquad
\frac{1}{(\partial^+)^2},
\]

on the nonzero-mode subspace.

Retain separately:

```text
ordinary-mode kernel;
zero-mode projector;
boundary term;
Hermiticity/anti-Hermiticity relation;
momentum-space pole prescription;
species and color-current domain.
```

Required checks:

```text
P0/Q0 identities
inverse action on Q0
PV antisymmetry
Hermiticity property
finite-box sum versus analytic kernel
large-box behavior
```

Create:

```text
docs/next_level/c47_inverse_derivative_mode_functional.json
docs/next_level/c47_inverse_derivative_validation.json
```

---

# 16. Residual-boundary and zero-mode local functional

The frozen C43/C45 records identify boundary and zero-mode ownership but do not yet define the local finite-volume action functional.

Derive the local mode-index functionals required by C48 for:

```text
residual transverse gauge boundary field;
constrained fermion zero mode;
gluon longitudinal zero mode;
global Gauss-law zero mode;
action-owned boundary/contact completion.
```

Do not construct the complete nonlocal JMY transverse link; that remains a later operator package.

Every retained class must have:

```text
source expression
finite-volume mode action
colored-module interpretation
cancellation partner
matrix-block domain
exact status
```

Allowed statuses:

```text
LOCAL_FUNCTIONAL_EXECUTABLE_NONZERO
LOCAL_FUNCTIONAL_EXECUTABLE_ZERO_BY_EXACT_PROOF
EXTERNAL_MODULE_LABEL_WITH_PROVED_FACTORING
CANCELS_WITH_DECLARED_LOCAL_BOUNDARY_TERM
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF
ABSENT_BLOCKING
```

Required checks:

```text
global-color/Gauss-law compatibility
residual-gauge transformation
P0/Q0 consistency
boundary-prescription dependence
local current/Ward symbolic identity
```

Create:

```text
docs/next_level/c47_boundary_zero_mode_functional.json
docs/next_level/c47_boundary_zero_mode_validation.json
```

---

# 17. Basis-level comparison maps

Construct comparison maps between adjacent physical resolutions using:

```text
exact longitudinal partition relations;
x-dependent intrinsic/CM transformations;
C45 transverse overlaps;
CM-ground projectors;
color-triplet isometries;
zero-mode projectors.
```

The longitudinal spaces are nonnested. Do not claim exact embedding.

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
CM-ground preservation
color-triplet preservation
K and Jz bookkeeping
reported nonnested longitudinal remainder
free-functional consistency
canonical-kernel consistency
boundary/zero-mode-functional consistency
```

These are basis comparison maps, not continuum extrapolations.

Create:

```text
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_physical_basis_comparison_validation.json
```

---

# 18. C48 assembly interface

Define the unique interface by which C48 will assemble:

```text
free q operator matrix;
free qg operator matrix;
canonical SU(3) emission and adjoint absorption;
instantaneous-fermion matrices;
instantaneous-current/gluon matrices;
other constrained/contact matrices;
action-owned boundary/zero-mode matrices;
local counterterm directions.
```

The interface must specify:

```text
basis order
block labels
normalization factors
units
symbolic L handling
coupling-power factors
color insertion point
kernel insertion point
selection rules
error/remainder propagation
matrix-free route
```

Create:

```text
docs/next_level/c47_c48_matrix_assembly_interface.json
```

---

# 19. Deterministic runtime bundle

Create a content-addressed runtime bundle containing at least:

```text
q longitudinal/HO basis tables;
qg longitudinal partitions;
x-scaled coordinate maps;
TM/Jacobi transformation matrices;
CM projectors or Lawson operators;
physical q and qg basis tables/isometries;
free-operator functional arrays;
all-mode canonical kernel tuple tables;
inverse-derivative functionals;
boundary/zero-mode functionals;
basis comparison maps.
```

Heavy arrays may remain under:

```text
data/runtime/c47_basis1/
```

Commit an inventory containing:

```text
runtime path
shape
dtype
units
nnz where applicable
basis-order hash
array hash
generator command
```

Create:

```text
docs/next_level/c47_numerical_object_inventory.json
```

The bundle must contain no final Hamiltonian or interaction matrix.

---

# 20. End-to-end source-to-basis test

Implement a test that begins from C43 source/action records and C45 mode arrays.

It must:

```text
enumerate exact qg longitudinal partitions;
derive x-scaled intrinsic/CM coordinates;
construct TM/Jacobi transforms;
select and apply the CM plan;
assemble physical q/qg basis tables;
derive the finite-volume free normalization;
evaluate the all-mode canonical kernel;
construct inverse-derivative and boundary/zero-mode functionals;
construct comparison maps;
reproduce all hashes.
```

It must fail when:

```text
x_min=1/18 is substituted for finite-mode support;
x-dependent scaling is removed;
CM and intrinsic coordinates are interchanged;
a one-particle HO product is used without CM projection;
the free-operator normalization changes;
an arbitrary value of L is inserted;
the all-mode kernel is replaced by the C45 frozen test set;
the PV prescription changes;
a zero-mode projector is removed;
the residual-boundary functional is replaced by metadata;
a C40 array is substituted.
```

---

# 21. Focused mutations

Create at least **192 focused live mutations** of actual transformations, functionals, and basis arrays.

Include mutations of:

```text
x_q/x_g scaling
Jacobian
TM bracket phase
CM projector
Lawson subtraction constant
many-body Nmax rule
free-operator factor
finite-volume normalization
L dependence
canonical-kernel helicity numerator
HO overlap
inverse-derivative denominator
boundary functional
zero-mode projector
color-triplet isometry
basis comparison map
runtime-array hash
```

Every mutation must fail a concrete source, orthogonality, CM, normalization, kernel, boundary, or deterministic-reconstruction check.

Do not inflate the count with identifier-only dispatch.

---

# 22. Readiness gate

Issue:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY
```

only when:

```text
all four blocker rows are SOURCE_COMPLETE_EXECUTABLE;
the qg longitudinal partitions are exact;
the x-scaled coordinate map is source qualified;
the intrinsic/CM transformation closes;
one CM plan is selected and validated;
the many-body truncation is source exact;
the physical q and CM-clean color-triplet qg bases exist;
the finite-volume free-operator normalization is unique;
the all-mode canonical kernel is exhaustive;
the inverse-derivative functional closes;
the local boundary/zero-mode functional closes;
the physical basis comparison maps close at their declared scope;
the C48 matrix-assembly interface is complete;
the runtime bundle reproduces byte-for-byte;
the end-to-end source-to-basis test passes.
```

Do not issue:

```text
C47_FREE_HAMILTONIAN_MATRIX_VALIDATED
C47_CANONICAL_QG_MATRIX_VALIDATED
C47_INSTANTANEOUS_MATRIX_VALIDATED
C47_JMY_WILSON_MATRIX_VALIDATED
C47_ONE_LOOP_MATCHING_VALIDATED
```

---

# 23. Exact no-go branches

## A. \(x\)-scaled intrinsic/CM projection remains incomplete

```text
C47_X_SCALED_CM_PROJECTION_INCOMPLETE
```

Next:

> **C48/CMX — source-qualified light-front Jacobi coordinates, TM brackets, and CM factorization completion**

## B. Free-operator normalization remains incomplete

```text
C47_FREE_OPERATOR_NORMALIZATION_INCOMPLETE
```

Next:

> **C48/FNORM — finite-volume light-front state and invariant-mass operator normalization completion**

## C. All-mode canonical kernel remains incomplete

```text
C47_ALL_MODE_CANONICAL_KERNEL_INCOMPLETE
```

Next:

> **C48/KERNEL1 — exhaustive source-derived longitudinal/HO/spinor canonical-kernel completion**

## D. Boundary/zero-mode functional remains incomplete

```text
C47_BOUNDARY_ZERO_MODE_FUNCTIONAL_INCOMPLETE
```

Next:

> **C48/BZFUNC — finite-volume inverse-derivative, residual-boundary, and zero-mode functional completion**

## E. Physical basis assembly closes

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY
```

Next:

> **C48/HQCD — assemble source-derived physical local-QCD matrices and the projected action identity**

---

# 24. Required deliverables

Create at least:

```text
docs/next_level/c47_implementation_report.md
docs/next_level/c47_api.md
docs/next_level/c47_derivation_authority_manifest.json
docs/next_level/c47_primary_source_manifest.json
docs/next_level/c47_source_relevance_matrix.json
docs/next_level/c47_basis_assembly_contract_matrix.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_x_scaled_coordinate_validation.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_qg_tm_validation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_cm_factorization_report.json

docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json

docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_free_operator_functional_validation.json

docs/next_level/c47_all_mode_canonical_kernel.json
docs/next_level/c47_all_mode_kernel_validation.json

docs/next_level/c47_inverse_derivative_mode_functional.json
docs/next_level/c47_inverse_derivative_validation.json
docs/next_level/c47_boundary_zero_mode_functional.json
docs/next_level/c47_boundary_zero_mode_validation.json

docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_physical_basis_comparison_validation.json
docs/next_level/c47_c48_matrix_assembly_interface.json

docs/next_level/c47_numerical_object_inventory.json
docs/next_level/c47_readiness_report.json
docs/next_level/c47_source_sufficiency_decision.json
docs/next_level/c47_no_go_decision_tree.json
docs/next_level/c47_missing_calculation_specification.md
docs/next_level/c47_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/basis1/
```

or the repository-equivalent package.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 25. Acceptance criteria

C47 is complete only when:

1. The full C46 baseline reproduces.
2. The C46 no-go remains explicit.
3. The C43 action and C45 one-particle contracts remain unchanged.
4. C40 remains method-oracle only.
5. The physical half-integer-\(K\) trajectory is retained.
6. The endpoint regulator remains separate from finite support.
7. \(L\) remains symbolic unless a source-qualified cancellation removes it.
8. Every qg longitudinal partition is exact.
9. The x-scaled coordinate map is source derived.
10. Its inverse and Jacobian close.
11. Intrinsic and CM variables are separated.
12. The product-to-intrinsic/CM transform closes.
13. The many-body truncation is source exact.
14. One CM-removal plan is selected.
15. The physical qg basis is CM clean.
16. The color-triplet module remains exact.
17. The physical q and qg Gram matrices close.
18. The finite-volume free-operator normalization is unique.
19. Continuum/large-box and symbolic-\(L\) checks close.
20. The canonical local kernel covers every allowed mode tuple.
21. No representative subset is mislabeled exhaustive.
22. The inverse-derivative functional acts only on the correct subspace.
23. Boundary and zero-mode local functionals are executable or exactly blocked.
24. Global-color and residual-gauge treatments remain compatible.
25. Basis comparison maps descend from physical transformations.
26. Nonnested longitudinal remainders remain visible.
27. The C48 assembly interface is complete.
28. The runtime bundle contains actual arrays/functionals, not metadata substitutes.
29. End-to-end source-to-basis reconstruction passes.
30. At least 192 focused live mutations are detected.
31. No final Hamiltonian or interaction matrix is claimed.
32. No complete JMY Wilson or bilocal matrix is claimed.
33. No one-loop coefficient or matching kernel is created.
34. No proton TMD or ART25 bridge is created.
35. No fit, inference, process, or production route is created.
36. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
37. `MSHT20_REP/` remains untouched and outside Git.
38. The working tree is clean except for the pre-existing untracked directory.
39. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken intrinsic/CM factorization, finite-volume normalization, kernel completeness, or boundary/zero-mode ownership to open the gate.

---

# 26. Final Codex response

Report:

- full starting and final commits;
- exact sources and equation locators used for each blocker;
- four-blocker contract statuses;
- physical qg longitudinal partitions;
- x-scaled coordinate formulas, inverse, and Jacobian residuals;
- TM/Jacobi transform dimensions, ranks, unitarity, and quadrature residuals;
- selected CM plan and factorization residuals;
- physical q and qg dimensions by block;
- Gram and CM-cleanliness residuals;
- exact projected free-operator convention and finite-volume normalization;
- symbolic \(L\) treatment;
- free-functional validation residuals;
- all-mode canonical-kernel entry counts, sparsity, and independent residuals;
- inverse-derivative functional residuals;
- boundary/zero-mode functional statuses and residuals;
- basis-comparison map shapes and remainders;
- runtime-bundle hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no final Hamiltonian/vertex/instantaneous/Wilson/bilocal matrix, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a one-particle HO product, an unresolved CM prescription, a scalar free-energy formula, a frozen kernel sample, or boundary metadata as a source-derived physical many-body basis.
