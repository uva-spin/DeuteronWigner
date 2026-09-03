# C54/HQCD2 Codex Work Package

## Title

**Complete source-derived local light-front QCD operator substrate: free invariant-mass blocks, instantaneous fermion and color-current matrices, constrained/contact and boundary/zero-mode completion, local counterterm directions, coupling-ordered assembly, and projected action identity**

## Authoritative baseline

Start from the clean local C53/VERTEX2 completion commit:

```text
ec705d02960d3a1a644958d43d35277a85f9825c
```

Its immediate scientific parent is:

```text
949af3ad83ea4a384c9142784251dfd06254b5fd
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 949af3ad83ea4a384c9142784251dfd06254b5fd HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION

C45_SOURCE_DERIVED_MODE_PROJECTION_READY

C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY

C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY

C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

and the exact C53 scientific boundary:

```text
canonical interaction:
    one additive C43 covariant b-dagger a-dagger b bilinear

physical q -> qg color vertex:
    exact SU(3);
    exact 3 tensor 8 -> 3 triplet image;
    reduced and full-product assembly routes equivalent;
    g_s factored;
    executable SymPy coefficient retained separately;
    absorption generated only as the Hermitian adjoint;
    independent C52-driven matrix-free actions;
    complete entry ancestry and count-once closure;

historical inputs:
    C47 raw canonical tuples poisoned;
    C50 combined values poisoned in the assembly path;

not yet constructed:
    physical free q or qg matrices;
    instantaneous-fermion matrices;
    instantaneous color-current/gluon matrices;
    remaining constrained/contact matrices;
    action-owned boundary/zero-mode matrices;
    local counterterm directions;
    complete local-QCD block operator;
    projected action identity.
```

Verify every identity from the committed C53 records rather than relying on this prompt.

The fixed architecture remains:

```text
TMD scheme:
    O4-SPACELIKE-COLLINS-JMY

gauge/action:
    G0-LIGHT-FRONT-GAUGE
    A^+ = A_- = 0
    x^+ is light-front time
    antisymmetric/PV inverse partial^+ on Q0
    explicit zero-mode projector
    retained residual transverse gauge link

physical basis:
    K = 9/2, 11/2, 13/2
    C47 CM-clean total-color-triplet qg module

invariant-mass convention:
    M^2 = 2 P^+ P^- - P_perp^2

coupling organization:
    g_s remains symbolic and factored

longitudinal box:
    L remains symbolic unless an inherited source-derived cancellation
    has already been proved.
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All C47 raw canonical tuple values and attempted historical component metadata remain diagnostic-only and forbidden as physical numerical inputs.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C54 completes the **local action-owned operator substrate** on

\[
\mathcal H_q
\oplus
\mathcal H_{qg}^{(3,\mathrm{CM}=0)}
\]

using the C53 physical canonical vertex as an immutable \(g_s^1\) input.

C54 must construct:

```text
the source-derived free q invariant-mass matrix;

the source-derived free CM-clean triplet-qg invariant-mass matrix;

all action-required instantaneous-fermion matrices;

all action-required instantaneous color-current/gluon matrices;

every remaining local constrained/contact matrix required at the
declared q/qg scope;

all action-owned local residual-boundary and zero-mode matrices
or exact projected proofs;

source-derived local counterterm-direction operators and,
where required, generalized-metric directions;

the immutable coupling-ordered coefficient blocks
    M_(0)^2,
    M_(1)^2,
    M_(2)^2;

an assembled and independently matrix-free local polynomial action;

the strongest projected local action/current identity actually
supported by the C43 source contract;

operator-by-operator physical-resolution comparison diagnostics.
```

The canonical \(g_s^1\) block must be imported from C53 read-only. It must not be re-derived, renormalized, rescaled, or refitted in C54.

C54 must not construct:

```text
the complete nonlocal Ji–Ma–Yuan Wilson line;
the transverse staple closure as a nonlocal TMD operator;
the bilocal quark TMD measurement;
the universal B=0 soft factor;
nonlocal Wilson/cusp/bilocal counterterms;
physical one-loop counterterm coefficients;
a dressed partonic eigenstate;
a one-loop correlator;
a matching kernel;
a microscopic proton TMD;
an ART25 bridge.
```

The strongest allowed status is:

```text
C54_SOURCE_DERIVED_LOCAL_HQCD_SUBSTRATE_READY
```

When that gate passes, the exact next package is:

> **C55/WX — source-derived finite-basis Ji–Ma–Yuan Wilson operator, transverse closure, bilocal TMD measurement, nonlocal counterterm directions, and distributional/refinement maps**

---

# 2. Scientific boundary

C54 is:

```text
local gauge-fixed QCD action specific;
q plus qg sector specific;
physical CM-clean triplet-basis specific;
coupling-order resolved;
source derived;
sparse and matrix free;
deterministic;
validation only.
```

C54 is not:

```text
a phenomenological Hamiltonian model;
a fit of local operator strengths;
a physical coupling determination;
a dressed-quark calculation;
a nonlocal TMD-operator calculation;
a soft-function calculation;
a one-loop matching calculation;
a proton or deuteron prediction.
```

Do not insert a numerical \(g_s\), \(\alpha_s\), counterterm coefficient, box length, or regulator trajectory point merely to obtain a matrix.

---

# 3. Nonnegotiable authority chain

Every positive local matrix must descend through:

```text
locked primary-source equation
    -> C43 project-convention action term
    -> C45 normalized modes and zero-mode projectors
    -> C47 CM-clean physical basis and local functionals
    -> explicit C54 many-body matrix-element derivation
    -> deterministic sparse matrix or LinearOperator
    -> application to nonzero vectors
    -> independent check
    -> deterministic content hash.
```

The canonical block has the separate immutable chain:

```text
C43 action
    -> C45 modes/color
    -> C47 physical basis
    -> C50 finite-cell kernel
    -> C52 executable colorless primitive
    -> C53 exact SU(3)/triplet physical vertex.
```

For every local object record:

```text
primary-source locator;
C43 action-term ID;
C45 mode/projector IDs;
C47 basis/functional IDs;
C53 vertex ID where relevant;
gauge and boundary prescription;
zero-mode domain;
colored-module interpretation;
resolution and conserved block;
shape, dtype, nnz, units;
coupling order;
symbolic parameter signature;
basis-order hash;
generator-code hash;
array hash;
independent residual.
```

The following are forbidden:

```text
a C40 toy coefficient;
a C47 raw canonical tuple value;
a source label without an executable formula;
a hand-designed sparse texture;
a block set to zero only because a Fock sector is absent;
a coefficient tuned to close the projected identity;
a numerical matrix inferred from desired Hermiticity.
```

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_gauge_constraint_derivation.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json
docs/next_level/c43_finite_basis_projection_contract.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_free_operator_functional_validation.json
docs/next_level/c47_inverse_derivative_mode_functional.json
docs/next_level/c47_boundary_zero_mode_functional.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_c48_matrix_assembly_interface.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c53_implementation_report.md
docs/next_level/c53_derivation_authority_manifest.json
docs/next_level/c53_physical_resolution_manifest.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_symbolic_parameter_contract.json
docs/next_level/c53_physical_vertex_primitive_matrices.json
docs/next_level/c53_physical_symbolic_vertex.json
docs/next_level/c53_physical_emission_validation.json
docs/next_level/c53_physical_matrix_free_report.json
docs/next_level/c53_vertex_adjoint_report.json
docs/next_level/c53_linear_block_operator_validation.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c54_derivation_authority_manifest.json
docs/next_level/c54_input_fidelity_audit.json
```

---

# 5. Input-fidelity audit

Before assembling a matrix, classify every required input as:

```text
SOURCE_DERIVED_EXECUTABLE;
SOURCE_DERIVED_SYMBOLIC;
SOURCE_DERIVED_FUNCTIONAL;
SOURCE_DERIVED_BASIS_IDENTITY;
METHOD_ORACLE_ONLY;
ABSENT_BLOCKING.
```

Only the first four classes may enter C54.

The audit must verify that:

```text
the C47 free functionals are executable over every physical basis row;

the inverse-derivative and boundary/zero-mode functionals expose
actual mode-index actions rather than status metadata;

the C53 physical primitive and symbolic coefficient are present,
content-addressed, and independently reconstructible;

every C43 action term required at O(g_s^0) or O(g_s^2) has an
explicit projection formula or a source-qualified exact
non-applicability proof.
```

If a required local input is metadata-only, stop at the corresponding targeted branch. Do not recreate the C40 mistake.

Create a one-to-one local term crosswalk:

```text
C43 term ID
C43 declared scope
C47 functional/input
C54 matrix block
coupling order
source status
projection status
identity role
```

Create:

```text
docs/next_level/c54_local_term_crosswalk.json
```

---

# 6. Freeze basis, units, and symbolic parameters

For every physical resolution freeze:

```text
K, Nmax, bHO;
q physical basis ordering;
CM-clean triplet-qg basis ordering;
total Jz and other conserved blocks;
open-color module semantics;
mass/IR parameter convention;
symbolic L convention;
zero-mode projectors;
boundary prescription;
M^2 units;
C53 physical-vertex primitive and expression hashes;
physical comparison maps.
```

Keep distinct:

```text
finite one-fermion support minima:
    1/9, 1/11, 1/13

historical C7 endpoint regulator:
    1/18
```

The endpoint regulator must not alter the physical mode enumeration.

Create:

```text
docs/next_level/c54_physical_resolution_manifest.json
docs/next_level/c54_basis_order_manifest.json
docs/next_level/c54_symbolic_parameter_contract.json
```

---

# 7. Resource and block preflight

Report for every resolution:

```text
q dimension and conserved blocks;
qg dimension and conserved blocks;
combined local-space dimension;
expected free-matrix nnz;
expected instantaneous/contact nnz bounds;
expected boundary/zero-mode nnz bounds;
memory estimate;
matrix-free cost estimate;
runtime sharding plan.
```

Verify the physical dimensions from C53 rather than hard-coding them.

Use:

```text
blockwise CSR/CSC matrices;
content-addressed sparse shards;
genuine independent LinearOperator actions.
```

No physically allowed state may be removed for runtime convenience.

Create:

```text
docs/next_level/c54_dimension_resource_preflight.json
```

---

# 8. Free one-quark invariant-mass matrix

Construct:

\[
M_{q,0}^2
\]

from the C43 free action and the C47 finite-volume normalization contract.

Use the exact project identity:

\[
M^2=2P^+P^- - P_\perp^2.
\]

The matrix must act on the physical one-quark basis including fundamental color, but its kinematic part must remain color diagonal and source derived.

Required outputs:

```text
assembled sparse matrix;
independent matrix-free action;
direct analytic element oracle;
block spectra or rigorous spectral bounds;
symbolic-L factorization record.
```

Required checks:

```text
Hermiticity;
GeV^2 units;
free dispersion;
mass/IR dependence;
color, helicity, Jz, and K conservation;
assembled versus matrix-free equality;
analytic HO-operator versus direct quadrature;
no arbitrary numerical L.
```

Create:

```text
docs/next_level/c54_free_q_matrix.json
docs/next_level/c54_free_q_validation.json
```

---

# 9. Free CM-clean triplet-qg invariant-mass matrix

Construct:

\[
M_{qg,0}^2
\]

in the C47 CM-ground, total-color-triplet physical basis.

Begin from the source-derived intrinsic free functional and transform through:

```text
the x-weighted Jacobi/TM map;
the exact CM-ground projector;
the physical triplet isometry.
```

Do not approximate the result by unrelated one-particle expectation values unless the source-derived transformation proves equality.

Required checks:

```text
Hermiticity;
GeV^2 units;
CM-ground preservation;
triplet preservation;
intrinsic/CM separation;
mass/IR dependence;
K and Jz conservation;
assembled versus matrix-free equality;
direct intrinsic-functional agreement;
symbolic-L cancellation or factoring;
TM forward/inverse consistency.
```

Create:

```text
docs/next_level/c54_free_qg_matrix.json
docs/next_level/c54_free_qg_validation.json
```

---

# 10. Import the C53 canonical block read-only

Import:

\[
\widehat V_{qg\leftarrow q}^{(M^2)}
\]

and its generated adjoint from C53.

The C54 builder must verify:

```text
C53 primitive hash;
C53 executable-expression hash;
C53 physical basis-order hash;
C53 entry-ancestry hash;
C53 adjoint identity;
C53 sparse/matrix-free residual;
C53 raw-tuple poisoning identity.
```

C54 may not:

```text
recompute color insertion;
change the triplet phase;
rescale the primitive;
change the symbolic coefficient;
insert a physical g_s;
independently evaluate absorption.
```

Create:

```text
docs/next_level/c54_c53_vertex_import_report.json
```

Any mismatch blocks all downstream assembly.

---

# 11. Instantaneous-fermion matrices

Project the exact C43 instantaneous-fermion operator using:

```text
the C43 antisymmetric/PV inverse derivative;
the C45/C47 Q0 projector;
the C47 physical basis;
the same field and state normalization used by C53.
```

Factor:

\[
V_{\mathrm{inst},f}
=
g_s^2\widehat V_{\mathrm{inst},f}^{(M^2)}.
\]

Audit every action-supported block among:

```text
q -> q;
q -> qg;
qg -> q;
qg -> qg.
```

Do not presume a block is zero from its name.

Allowed statuses:

```text
SOURCE_DERIVED_EXECUTABLE_NONZERO;
SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF;
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF;
ABSENT_BLOCKING.
```

For every nonzero block retain:

```text
operator ordering;
inverse-derivative denominator;
zero-mode-domain statement;
color tensor;
basis-element derivation;
coupling power;
units.
```

Required checks:

```text
P0/Q0 consistency;
PV prescription;
Hermiticity or exact paired-adjoint relation;
K and Jz conservation;
color covariance;
triplet preservation where applicable;
CM-ground preservation;
direct element versus sparse action;
independent matrix-free action.
```

Create:

```text
docs/next_level/c54_instantaneous_fermion_matrices.json
docs/next_level/c54_instantaneous_fermion_validation.json
```

---

# 12. Instantaneous color-current/gluon matrices

Project the C43 Gauss-law-induced interaction.

Retain distinct source-owned pieces:

```text
quark color current;
gluon color current;
mixed current;
local boundary/zero-mode completion.
```

Factor:

\[
V_{\mathrm{inst},g}
=
g_s^2\widehat V_{\mathrm{inst},g}^{(M^2)}.
\]

The source decomposition must remain explicit through assembly.

Required checks:

```text
same inverse-(partial^+)^2 convention as C43/C47;
Hermiticity;
fundamental and adjoint SU(3) covariance;
triplet-subspace preservation;
K and Jz conservation;
CM-ground preservation;
current-source count once;
direct element versus sparse action;
independent matrix-free action.
```

Create:

```text
docs/next_level/c54_instantaneous_current_matrices.json
docs/next_level/c54_instantaneous_current_validation.json
```

---

# 13. Remaining constrained and contact terms

Read every C43 Hamiltonian-ledger row marked:

```text
REQUIRED_AT_O_G2;
REQUIRED_AS_COUNTERTERM_OR_WARD_PARTNER.
```

For each row produce exactly one of:

```text
a source-derived numerical matrix;

a source-derived generalized-metric/operator pair;

an exact projected zero with proof;

a proved not-applicable status;

ABSENT_BLOCKING.
```

Audit, as applicable:

```text
fermion-constraint contact terms;
gauge-constraint contact terms;
normal-ordering/contact terms;
local basis-boundary terms;
local regulator terms;
three-gluon action terms;
four-gluon action terms.
```

The absence of qgg or higher external basis states is not by itself a proof of non-applicability. Use operator ordering, normal ordering, retained matrix block, and the declared perturbative scope.

Create:

```text
docs/next_level/c54_constrained_contact_ledger.json
```

Any required `ABSENT_BLOCKING` row prevents the positive gate.

---

# 14. Action-owned boundary and zero-mode matrices

Consume the C43/C45/C47 local contracts to construct the local matrices or exact projected statuses for:

```text
residual transverse gauge boundary field;
constrained fermion zero-mode completion;
longitudinal-gluon zero-mode control;
global Gauss-law zero-mode treatment;
local basis-boundary/contact completion.
```

Do not construct the complete nonlocal JMY transverse link. That belongs to C55.

For every class record:

```text
physical matrix block;
P0/Q0 action;
colored-module interpretation;
boundary prescription;
cancellation partner;
coupling order;
norm or exact-zero proof;
status.
```

Allowed statuses:

```text
SOURCE_DERIVED_EXECUTABLE_NONZERO;
SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF;
EXTERNAL_MODULE_LABEL_WITH_PROVED_FACTORING;
CANCELS_WITH_DECLARED_LOCAL_PARTNER;
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF;
ABSENT_BLOCKING.
```

Required checks:

```text
global-color/Gauss-law compatibility;
residual-gauge transformation at local-action scope;
P0/Q0 identities;
boundary-prescription dependence;
Hermiticity/paired adjoint;
CM/triplet preservation.
```

Create:

```text
docs/next_level/c54_boundary_zero_mode_matrices.json
docs/next_level/c54_boundary_zero_mode_validation.json
```

---

# 15. Local counterterm-direction operators

Construct source-derived **directions**, not fitted coefficients.

Audit at least:

```text
quark mass direction;
quark field/residue direction;
qg canonical-vertex direction;
instantaneous-partner direction;
local basis-boundary/regulator direction;
local zero-mode direction where source required.
```

For each direction decide whether it is represented by:

```text
an additive operator matrix;
a generalized-metric derivative;
a coupled operator/metric pair;
an exact constraint direction;
not applicable with proof;
or blocking.
```

Do not force a field-strength or state-normalization variation into an additive matrix when the source structure changes the metric or basis normalization.

For every positive direction provide:

```text
parameter definition;
source authority;
operator/metric derivative;
coupling/order label;
physical matrix blocks;
independent finite-difference check;
rank and linear-independence diagnostics.
```

No physical counterterm coefficient is solved.

Nonlocal Wilson-line, cusp, endpoint, transverse-link, soft, and bilocal counterterm directions remain outside C54.

Create:

```text
docs/next_level/c54_local_counterterm_directions.json
docs/next_level/c54_local_counterterm_rank_report.json
```

---

# 16. Coupling-ordered local operator

Assemble immutable coefficient blocks:

\[
\mathcal M_{\rm local}^2(g_s)
=
\mathcal M_{(0)}^2
+
g_s\mathcal M_{(1)}^2
+
g_s^2\mathcal M_{(2)}^2
+
\mathcal O(g_s^3).
\]

At minimum:

\[
\mathcal M_{(0)}^2
=
\begin{pmatrix}
M_{q,0}^2 & 0\\
0 & M_{qg,0}^2
\end{pmatrix},
\]

and the read-only C53 block:

\[
\mathcal M_{(1)}^2
=
\begin{pmatrix}
0 &
\widehat V_{q\leftarrow qg}^{(M^2)}
\\
\widehat V_{qg\leftarrow q}^{(M^2)}
&
0
\end{pmatrix}.
\]

The \(g_s^2\) coefficient block must contain every direct local instantaneous, constrained, contact, boundary, and zero-mode contribution at the declared scope.

Counterterm **directions** are stored separately from the bare/direct \(\mathcal M_{(2)}^2\) block unless the exact project convention requires an explicitly symbolic coefficient family. No physical coefficient is inserted.

Create:

```text
docs/next_level/c54_local_operator_block_manifest.json
docs/next_level/c54_local_polynomial_action_contract.json
```

---

# 17. Independent matrix-free polynomial action

Implement:

```python
apply_local_hqcd_polynomial(
    vector_q,
    vector_qg,
    resolution,
    symbolic_parameters,
    diagnostic_gs=None,
)
```

The authoritative route returns coupling-order-separated vectors:

```text
order_0_action;
order_1_action;
order_2_direct_action;
counterterm_direction_actions;
```

A diagnostic nonphysical \(g_s\) may be accepted only for algebraic recomposition tests. It must never be stored as a physical parameter or result.

The matrix-free route must:

```text
apply free actions directly from source functionals;
call the independent C53 matrix-free canonical action;
apply instantaneous/constrained/boundary/zero-mode actions
through independently generated kernels;
not multiply by the stored combined block matrices.
```

Compare assembled and matrix-free actions on:

```text
every basis vector in tractable blocks;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions;
multiple diagnostic symbolic substitutions.
```

Create:

```text
docs/next_level/c54_local_matrix_free_report.json
docs/next_level/c54_polynomial_action_validation.json
```

---

# 18. Projected local action/current identity

Compile the strongest identity actually supported by the C43 source contract.

Do not invent an identity from the desired matrix sum.

Do not call the result a full non-Abelian Slavnov–Taylor identity unless the exact source derivation, ghost content, and retained state space support that theorem.

The identity record must state:

```text
its source equation or derivation;
its external-state domain;
its coupling order;
its current or gauge-transformation insertion;
every required propagating, instantaneous, constrained,
boundary, zero-mode, and counterterm-direction term;
its exact non-applicability limits.
```

Evaluate the identity:

```text
block by block;
at every resolution;
on deterministic basis vectors;
on random normalized complex vectors;
through assembled and independent matrix-free routes.
```

Report:

```text
full residual;
residual by coupling order;
residual by source term;
color-generator covariance residual;
resolution dependence;
signed defect when every required term is ablated.
```

No coefficient may be tuned to force closure.

If C43 supplies no explicit action/current identity beyond a term ledger, issue:

```text
C54_PROJECTED_ACTION_IDENTITY_UNDEFINED
```

rather than inventing one.

Create:

```text
docs/next_level/c54_projected_action_identity_contract.json
docs/next_level/c54_projected_action_identity_report.json
```

---

# 19. Operator comparison across physical resolutions

Consume the C47 comparison maps.

For every local operator \(O\), evaluate the exact supported relation:

\[
R\,O_{r'}\,P
\quad\text{versus}\quad
O_r.
\]

Execute for:

```text
free q;
free qg;
C53 canonical emission and absorption;
every instantaneous block;
every constrained/contact block;
every boundary/zero-mode block;
every local counterterm direction;
the coupling-ordered coefficient blocks.
```

Separate:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
triplet-basis remainder;
zero-mode/boundary remainder;
symbolic-parameter remainder;
numerical error.
```

Do not fit any coefficient to reduce the comparison residual.

Create:

```text
docs/next_level/c54_operator_comparison_report.json
docs/next_level/c54_comparison_remainder_ledger.json
```

---

# 20. Count-once and ancestry ledgers

Every nonzero local matrix entry must retain ancestry to:

```text
C43 action term;
C45/C47 mode and basis IDs;
source-owned operator ordering;
inverse-derivative/boundary functional where applicable;
color tensor;
physical block;
coupling order;
matrix shard.
```

Report separately:

```text
source term count;
projected block count;
nonzero entry count;
exact-zero decision count;
not-applicable count;
duplicate source-component count;
missing required entry count;
blocking entry count.
```

Multiple source terms contributing to one matrix entry are not duplicates when their ancestry remains distinct and their sum is explicit.

A positive gate requires:

```text
duplicate source-component count = 0;
missing required entry count = 0;
blocking required entry count = 0.
```

Create:

```text
docs/next_level/c54_local_entry_ancestry.json
docs/next_level/c54_count_once_report.json
```

---

# 21. Unit, parameter, and convention covariance

Run matrix-level tests under:

```text
GeV/MeV conversion;
symbolic L scaling or cancellation;
fixed-x P^+ rescaling;
bHO basis transformations;
mass/IR variation;
Fourier phase;
helicity and polarization phase;
triplet phase;
PV boundary prescription controls;
zero-mode-projector controls;
historical factor-of-two negative control;
wrong SU(3) controls inherited from C53.
```

Require:

```text
every local M^2 block has mass-squared units;
color insertion changes no units;
all symbolic signatures are block consistent;
dimensionless residuals are invariant;
wrong conventions fail explicitly.
```

Create:

```text
docs/next_level/c54_unit_parameter_convention_report.json
```

---

# 22. Isolation and poisoning controls

Retain all C53 guards.

Additionally prove that:

```text
replacing C40 arrays with sentinels changes no C54 physical object;

replacing all C47 raw canonical tuple values and component metadata
changes no C54 object;

replacing C50 combined evaluator values changes no C54 assembly input;

altering the C53 physical primitive or expression hash fails before
any C54 action is assembled;

removing one required instantaneous, constrained, boundary, or
zero-mode term creates the prescribed failure.
```

Create:

```text
docs/next_level/c54_isolation_report.json
```

---

# 23. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
free q matrix;
free qg matrix;
read-only imported C53 vertex identities;
instantaneous-fermion matrices;
instantaneous-current/gluon matrices;
remaining constrained/contact matrices;
boundary/zero-mode matrices and projectors;
coupling-order coefficient blocks;
local counterterm-direction operator/metric records;
matrix-free reconstruction metadata;
entry-ancestry and count-once records;
projected-identity action records;
comparison-map execution blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c54_hqcd2/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
coupling order;
symbolic signature;
basis-order hash;
expression hash where applicable;
array hash;
generator command.
```

Create:

```text
docs/next_level/c54_numerical_object_inventory.json
```

All JSON, symbolic records, and arrays must regenerate byte-for-byte.

---

# 24. End-to-end source-to-local-substrate test

Implement an end-to-end test that begins with the C43/C45/C47/C53 contracts—not with prebuilt C54 matrices.

It must:

```text
regenerate the physical basis identities;
assemble free q and qg matrices;
verify and import the C53 canonical block;
assemble every instantaneous matrix;
assemble every constrained/contact matrix;
assemble boundary/zero-mode matrices;
construct local counterterm directions;
construct coupling-order blocks;
apply the independent polynomial action;
evaluate the projected action identity;
execute comparison maps;
run count-once, unit, poisoning, and holdout tests;
reproduce every hash.
```

It must fail when:

```text
a C40 coefficient enters;
a C47 raw tuple value enters;
the C53 vertex is rederived or rescaled;
the free-operator normalization changes;
L is assigned arbitrarily;
an instantaneous denominator changes;
a current color factor changes;
a constrained/contact term is omitted;
a zero-mode projector changes;
a boundary term is omitted;
a metric direction is forced into an additive matrix;
a required source term is duplicated;
an identity coefficient is tuned;
a matrix-free route multiplies by the stored combined matrix;
a runtime hash changes.
```

---

# 25. Focused mutation tests

Create at least **256 focused live mutations** of actual action terms, functionals, matrices, directions, or identities.

Include mutations of:

```text
free-operator normalization;
intrinsic free functional;
CM projector;
C53 vertex hash;
instantaneous-fermion denominator;
instantaneous-current color tensor;
inverse-derivative prescription;
constraint/contact term;
boundary functional;
zero-mode projector;
global-color treatment;
coupling-order label;
operator block order;
counterterm derivative;
metric direction;
entry ancestry;
count-once record;
projected-identity term;
matrix-free action;
unit signature;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, Hermiticity, covariance, count-once, identity, matrix-free, unit, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 26. Readiness gate

Issue:

```text
C54_SOURCE_DERIVED_LOCAL_HQCD_SUBSTRATE_READY
```

only when:

```text
the full C53 baseline reproduces;
every required input passes the fidelity audit;
free q and qg matrices exist at all resolutions;
the C53 canonical block is imported unchanged;
all required instantaneous-fermion blocks have executable/proved statuses;
all required instantaneous-current blocks have executable/proved statuses;
all required constrained/contact rows have executable/proved statuses;
all local boundary and zero-mode rows have executable/proved statuses;
the coupling-ordered local coefficient blocks are complete at declared scope;
local counterterm directions are source derived and correctly typed;
the independent polynomial action agrees with assembled blocks;
the strongest source-supported projected local action/current identity closes;
every required-term ablation produces a nonzero signed defect;
operator comparisons execute with separated remainders;
entry ancestry and count-once ledgers close;
unit, parameter, convention, and poisoning tests pass;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-local-substrate test passes.
```

Do not issue:

```text
C54_JMY_WILSON_MATRIX_VALIDATED;
C54_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C54_SOFT_SUBTRACTION_VALIDATED;
C54_PHYSICAL_COUNTERTERM_SOLUTION;
C54_ONE_LOOP_TMD_VALIDATED;
C54_MATCHING_KERNEL_VALIDATED;
C54_MICROSCOPIC_PROTON_TMD_EXPORTED.
```

---

# 27. Exact no-go branches

## A. Free operator assembly remains incomplete

```text
C54_FREE_OPERATOR_ASSEMBLY_INCOMPLETE
```

Next:

> **C55/HFREE2 — source-derived physical q/qg invariant-mass matrix completion**

## B. Instantaneous-fermion projection remains incomplete

```text
C54_INSTANTANEOUS_FERMION_ASSEMBLY_INCOMPLETE
```

Next:

> **C55/IFERM — finite-volume light-front instantaneous-fermion matrix completion**

## C. Instantaneous color-current/gluon projection remains incomplete

```text
C54_INSTANTANEOUS_CURRENT_ASSEMBLY_INCOMPLETE
```

Next:

> **C55/ICURR — Gauss-law current, inverse-derivative, and SU(3) matrix completion**

## D. Constrained, contact, boundary, or zero-mode projection remains incomplete

```text
C54_LOCAL_CONSTRAINT_BOUNDARY_ZERO_MODE_INCOMPLETE
```

Next:

> **C55/ZLOCAL — local constrained/contact, residual-boundary, and zero-mode completion**

## E. Local counterterm directions remain incomplete

```text
C54_LOCAL_COUNTERTERM_DIRECTIONS_INCOMPLETE
```

Next:

> **C55/CTLOCAL2 — source-derived local operator/metric counterterm-direction completion**

## F. No explicit projected identity exists

```text
C54_PROJECTED_ACTION_IDENTITY_UNDEFINED
```

Next:

> **C55/G4 — derive the declared-scope projected local action/current identity from the C43 source action**

## G. The projected identity exists but fails

```text
C54_PROJECTED_ACTION_IDENTITY_FAILED
```

Next:

> **C55/G5 — identify and complete missing local action-owned terms**

## H. Operator comparison remains incomplete

```text
C54_OPERATOR_COMPARISON_INCOMPLETE
```

Next:

> **C55/R1G — local-operator comparison-map and nonnested-remainder completion**

## I. All local-QCD gates close

```text
C54_SOURCE_DERIVED_LOCAL_HQCD_SUBSTRATE_READY
```

Next:

> **C55/WX — source-derived finite-basis JMY Wilson operator, bilocal TMD measurement, nonlocal counterterm directions, and distributional/refinement maps**

---

# 28. Required deliverables

Create at least:

```text
docs/next_level/c54_implementation_report.md
docs/next_level/c54_api.md
docs/next_level/c54_derivation_authority_manifest.json
docs/next_level/c54_input_fidelity_audit.json
docs/next_level/c54_local_term_crosswalk.json

docs/next_level/c54_physical_resolution_manifest.json
docs/next_level/c54_basis_order_manifest.json
docs/next_level/c54_symbolic_parameter_contract.json
docs/next_level/c54_dimension_resource_preflight.json

docs/next_level/c54_free_q_matrix.json
docs/next_level/c54_free_q_validation.json
docs/next_level/c54_free_qg_matrix.json
docs/next_level/c54_free_qg_validation.json

docs/next_level/c54_c53_vertex_import_report.json

docs/next_level/c54_instantaneous_fermion_matrices.json
docs/next_level/c54_instantaneous_fermion_validation.json
docs/next_level/c54_instantaneous_current_matrices.json
docs/next_level/c54_instantaneous_current_validation.json

docs/next_level/c54_constrained_contact_ledger.json
docs/next_level/c54_boundary_zero_mode_matrices.json
docs/next_level/c54_boundary_zero_mode_validation.json

docs/next_level/c54_local_counterterm_directions.json
docs/next_level/c54_local_counterterm_rank_report.json

docs/next_level/c54_local_operator_block_manifest.json
docs/next_level/c54_local_polynomial_action_contract.json
docs/next_level/c54_local_matrix_free_report.json
docs/next_level/c54_polynomial_action_validation.json

docs/next_level/c54_projected_action_identity_contract.json
docs/next_level/c54_projected_action_identity_report.json

docs/next_level/c54_operator_comparison_report.json
docs/next_level/c54_comparison_remainder_ledger.json

docs/next_level/c54_local_entry_ancestry.json
docs/next_level/c54_count_once_report.json
docs/next_level/c54_unit_parameter_convention_report.json
docs/next_level/c54_isolation_report.json

docs/next_level/c54_numerical_object_inventory.json
docs/next_level/c54_readiness_report.json
docs/next_level/c54_source_sufficiency_decision.json
docs/next_level/c54_no_go_decision_tree.json
docs/next_level/c54_missing_calculation_specification.md
docs/next_level/c54_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/hqcd3/
```

or the repository-equivalent package.

Add focused tests for:

```text
input fidelity;
free q/qg matrices;
C53 read-only import;
instantaneous fermion;
instantaneous current;
constrained/contact terms;
boundary and zero modes;
counterterm directions;
coupling-order blocks;
independent polynomial action;
projected action identity;
count once and ancestry;
unit and poisoning controls;
operator comparison;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON, symbolic expressions, and runtime arrays must reproduce byte-for-byte.

---

# 29. Acceptance criteria

C54 is complete only when:

1. The full C53 baseline reproduces.
2. The C52 and C53 positive gates remain explicit.
3. The C43 action, C45 mode/color, and C47 basis/functionals remain unchanged.
4. C40 remains method-oracle only.
5. C47 raw tuple values and metadata remain diagnostic-only.
6. C50 combined values remain holdouts, not assembly inputs.
7. The C53 physical vertex remains byte-identical.
8. No arbitrary numerical \(L\) is introduced.
9. No physical \(g_s\) or \(\alpha_s\) is chosen.
10. No physical counterterm coefficient is solved.
11. Every required input passes the source/executable fidelity audit.
12. Free q matrices exist at all resolutions.
13. Free qg matrices exist at all resolutions.
14. Free matrices preserve CM and triplet identities.
15. Assembled and independent matrix-free free actions agree.
16. The C53 canonical block is imported without modification.
17. Every required instantaneous-fermion block has an executable/proved status.
18. Every required instantaneous-current block has an executable/proved status.
19. Every required constrained/contact row has an executable/proved status.
20. Three-/four-gluon scope decisions are source and operator based.
21. Every local boundary/zero-mode row has an executable/proved status.
22. P0/Q0 and boundary-prescription identities close.
23. Local counterterm directions are source derived.
24. Metric directions are not misrepresented as additive matrices.
25. The coupling-order coefficient blocks are complete at declared scope.
26. The independent polynomial action agrees with assembled blocks.
27. A source-supported projected local action/current identity is explicitly defined.
28. The projected identity closes at every resolution and supported block.
29. Every required-term ablation gives a signed nonzero defect.
30. No coefficient is tuned to close the identity.
31. Operator comparison maps execute.
32. Nonnested, transverse, CM, color, boundary, symbolic, and numerical remainders remain separate.
33. Every nonzero local entry has complete ancestry.
34. Duplicate, missing, and blocking required-entry counts are zero.
35. Every local M^2 block has uniform mass-squared units.
36. GeV/MeV, \(L\), \(P^+\), \(b_{\rm HO}\), mass, phase, PV, zero-mode, and color controls pass.
37. Static and runtime poisoning controls pass.
38. Runtime bundles contain actual sparse matrices/operators and independent action metadata.
39. End-to-end reconstruction passes.
40. At least 256 focused live mutations are detected.
41. No complete JMY Wilson matrix is claimed.
42. No bilocal TMD measurement is claimed.
43. No soft subtraction or nonlocal counterterm system is claimed.
44. No dressed-state diagonalization is performed.
45. No one-loop coefficient or matching kernel is created.
46. No proton TMD or ART25 bridge is created.
47. No fit, inference, process, or production route is created.
48. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
49. `MSHT20_REP/` remains untouched and outside Git.
50. The working tree is clean except for the pre-existing untracked directory.
51. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken local-term completeness, inverse-derivative and zero-mode ownership, counterterm typing, or the projected action identity to open the gate.

---

# 30. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C53 inputs consumed;
- input-fidelity classifications and local-term crosswalk counts;
- physical dimensions, blocks, and resource strategy;
- free q and qg matrix shapes, nnz, norms/spectra, units, symbolic-\(L\) treatment, and matrix-free residuals;
- C53 import hashes and immutability checks;
- instantaneous-fermion shapes, norms, block statuses, and residuals;
- instantaneous-current shapes, norms, source-piece statuses, and residuals;
- constrained/contact ledger statuses;
- boundary and zero-mode matrix statuses, norms, and cancellation identities;
- local counterterm-direction types, shapes, ranks, and finite-difference residuals;
- coupling-order block shapes and polynomial-action residuals;
- projected action/current identity source, domain, residuals, and every ablation defect;
- operator-comparison residuals and separated remainders;
- entry-ancestry, duplicate, missing, exact-zero, not-applicable, and blocking counts;
- unit, symbolic, phase, PV, zero-mode, color, and poisoning results;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no JMY Wilson/bilocal matrix, soft subtraction, physical counterterm solution, dressed-state result, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a C53 vertex plus incomplete \(g_s^2\) blocks, a term ledger without matrices, a zero-mode omission, a metric counterterm forced into an additive matrix, or an identity closed by fitted coefficients as the complete source-derived local QCD substrate.
