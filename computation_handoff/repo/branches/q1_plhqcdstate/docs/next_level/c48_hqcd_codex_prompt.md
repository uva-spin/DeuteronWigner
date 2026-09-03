# C48/HQCD Codex Work Package

## Title

**Assembly of the source-derived local light-front QCD operator substrate: physical \(q/qg\) free Hamiltonians, exact SU(3) canonical vertex, instantaneous and constrained matrices, boundary/zero-mode completion, local counterterm directions, and projected action identity**

## Authoritative baseline

Start from the clean local C47/BASIS1 completion commit:

```text
055f2a3dd5a651cc687f532f4c0ea58d885dd585
```

Its immediate scientific parent is:

```text
3bf4da30bc672ff933aa3caf66c0c34c387dd08d
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 3bf4da30bc672ff933aa3caf66c0c34c387dd08d HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION

C45_SOURCE_DERIVED_MODE_PROJECTION_READY

C46_PHYSICAL_BASIS_ASSEMBLY_INCOMPLETE

C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY
```

and the exact C47 physical-basis results:

```text
source-locked two-body authority:
    arXiv:1911.10762v1

physical trajectory:
    K = 9/2, 11/2, 13/2

qg CM-clean dimensions:
    1,344 / 2,700 / 4,752

free-operator convention:
    M^2 = 2 P^+ P^- - P_perp^2

longitudinal box:
    L remains symbolic

canonical kinematic tuple counts:
    720 / 1,170 / 1,728

color:
    explicit 24 x 3 triplet isometry

inverse derivative:
    antisymmetric/PV on the nonzero-mode domain

comparison:
    nonnested physical-grid functional
```

Verify every value from the committed C47 records rather than relying on this prompt.

The fixed physical TMD architecture remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

The fixed gauge/action remains:

```text
G0-LIGHT-FRONT-GAUGE

A^+ = A_- = 0
x^+ is light-front time
antisymmetric/PV inverse partial^+ on Q0
explicit zero-mode projector
retained residual transverse gauge link
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

and may not provide any C48 physical coefficient.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C48 consumes the complete C43 action contract, C45 one-particle mode library, and C47 physical CM-clean basis assembly to construct the first source-derived **local QCD matrices** in the colored partonic matching module.

C48 must assemble:

```text
free one-quark invariant-mass matrix;
free CM-clean color-triplet qg invariant-mass matrix;

coupling-factored canonical q -> qg emission matrix;
generated qg -> q absorption adjoint;

all action-required instantaneous-fermion matrices;
all action-required instantaneous color-current/gluon matrices;
all remaining constrained/contact matrices at the declared scope;

action-owned residual-boundary matrices;
projected zero-mode operators and projectors;

local Hamiltonian counterterm-direction matrices;

many-body comparison-map execution on every local operator;

the strongest projected action/current identity supported by C43.
```

Organize the local operator as coefficient blocks in the coupling:

\[
\mathcal M_{\rm local}^2(g_s)
=
\mathcal M_{(0)}^2
+
g_s\,\mathcal M_{(1)}^2
+
g_s^2\,\mathcal M_{(2)}^2
+
\mathcal O(g_s^3),
\]

without choosing or fitting a physical value of \(g_s\).

C48 does **not** construct:

```text
the complete nonlocal Ji–Ma–Yuan Wilson matrix;
the bilocal TMD measurement;
soft subtraction;
nonlocal Wilson/cusp/bilocal counterterm directions;
physical one-loop counterterm coefficients;
a dressed partonic state;
a one-loop correlator;
a matching kernel;
a proton TMD or ART25 bridge.
```

The strongest allowed status is:

```text
C48_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

When that gate passes, the exact next package is:

> **C49/WX — source-derived finite-basis Ji–Ma–Yuan Wilson operator, transverse closure, bilocal TMD measurement, nonlocal counterterm directions, and distributional measurement/refinement maps**

Only after C49 closes may the one-loop nonsinglet calculation resume.

---

# 2. Fixed scientific scope

The numerical root is the exact colored matching-module plan selected by C45 and inherited by C47:

```text
NONHADRONIC_COLOR_FUNDAMENTAL_MATCHING_MODULE
```

Read its exact type and global-Gauss-law semantics from:

```text
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c47_boundary_zero_mode_functional.json
```

Do not assume the plan name or reinterpret it as a physical colored asymptotic state.

The retained sectors are:

\[
\mathcal H_q\oplus\mathcal H_{qg}^{(3,\mathrm{CM}=0)}.
\]

The declared local-action scope is:

```text
one external quark;
one quark plus one transverse gluon;
rank-zero T-even nonsinglet matching through O(g_s^2);
local action-owned operators only.
```

The following remain outside C48 unless C43 explicitly proves they are required as local closure partners:

```text
qgg numerical states;
qqbar-pair numerical states;
hadronic qqq sectors;
gluon external matching probes;
the nonlocal TMD staple;
the universal soft factor;
one-loop renormalization;
phenomenological calibration.
```

Every C43 Hamiltonian-ledger row must still receive a C48 scope decision. Absence of a retained Fock sector is not by itself an operator-level proof of zero.

---

# 3. Nonnegotiable evidence standard

Every positive matrix must descend through:

```text
locked primary-source equation
    -> C43 project-convention expression
    -> C45 one-particle mode identities
    -> C47 physical-basis/functionals
    -> explicit many-body matrix-element formula
    -> deterministic sparse matrix or LinearOperator
    -> application to nonzero complex vectors
    -> independent check
    -> deterministic content hash
```

For every object record:

```text
primary-source locator;
C43 action-term ID;
C45 mode IDs;
C47 basis/kernel/functional IDs;
gauge and boundary prescription;
zero-mode projector;
colored-module interpretation;
resolution and conserved block;
shape, dtype, nnz, units;
coupling-power factor;
basis-order hash;
generator-code hash;
array hash;
independent residual.
```

The following are not acceptable substitutes:

```text
a scalar expectation list in place of an operator;
a hand-designed sparse texture;
a matrix tuned to close the projected identity;
a C40 method-oracle array with new metadata;
a final matrix assembled from representative rather than exhaustive tuples;
a dense allocation that silently prunes the physical basis.
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
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_global_gauge_constraint_report.json

docs/next_level/c45_projection_contract_matrix.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_basis_assembly_contract_matrix.json
docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_cm_factorization_report.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_all_mode_canonical_kernel.json
docs/next_level/c47_inverse_derivative_mode_functional.json
docs/next_level/c47_boundary_zero_mode_functional.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_c48_matrix_assembly_interface.json
docs/next_level/c47_numerical_object_inventory.json
docs/next_level/c47_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c48_derivation_authority_manifest.json
```

---

# 5. Fidelity and resource preflight

Before assembling a matrix, verify that every consumed C47 object is numerically present and source linked.

Classify each required input as:

```text
SOURCE_DERIVED_EXECUTABLE;
SOURCE_DERIVED_FUNCTIONAL;
METHOD_ORACLE_ONLY;
ABSENT_BLOCKING.
```

Only the first two classes may enter C48.

For each physical resolution report:

```text
q dimension by conserved block;
qg CM-clean triplet dimension by conserved block;
canonical tuple count;
expected free-matrix nnz;
expected canonical-vertex nnz;
expected instantaneous/contact nnz bounds;
memory estimate;
matrix-free cost estimate;
runtime-bundle sharding plan.
```

The expected total qg dimensions are:

```text
1,344 / 2,700 / 4,752
```

but verify them.

Use blockwise sparse matrices, content-addressed shards, and/or genuine `LinearOperator` actions. Do not construct dense \(4752\times4752\) matrices merely for convenience.

Create:

```text
docs/next_level/c48_input_fidelity_audit.json
docs/next_level/c48_dimension_resource_preflight.json
```

If a required C47 object is only metadata, stop with the corresponding targeted no-go.

---

# 6. Freeze basis and units

For every resolution freeze:

```text
K, Nmax, bHO;
q basis ordering;
qg CM-clean color-triplet basis ordering;
total Jz and other block labels;
mass/IR parameters;
symbolic L convention;
M^2 units;
color and helicity phase conventions;
zero-mode projector;
boundary prescription;
comparison maps.
```

Keep distinct:

```text
finite mode minima:
    1/9, 1/11, 1/13

C7 endpoint regulator:
    1/18
```

The endpoint regulator must not alter the physical mode enumeration.

Create:

```text
docs/next_level/c48_physical_resolution_manifest.json
docs/next_level/c48_basis_order_manifest.json
```

---

# 7. Free one-quark invariant-mass matrix

Consume the C47 free-operator normalization contract:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Construct the complete one-quark matrix:

\[
M_{q,0}^2.
\]

Use the exact physical one-quark basis and C45/C47 HO operator algebra.

Required outputs:

```text
assembled sparse matrix;
independent matrix-free action;
direct diagonal and selected off-diagonal oracle;
block spectra or rigorous spectral bounds;
symbolic-L factorization record.
```

Required checks:

```text
Hermiticity;
units of GeV^2;
free dispersion;
mass/IR dependence;
Jz, color, helicity, and K block conservation;
assembled versus matrix-free action;
analytic HO operator versus direct quadrature;
no arbitrary numerical L.
```

Create:

```text
docs/next_level/c48_free_q_matrix.json
docs/next_level/c48_free_q_validation.json
```

---

# 8. Free qg invariant-mass matrix

Construct:

\[
M_{qg,0}^2
\]

in the exact CM-ground, total-color-triplet qg basis.

Begin from the source-derived intrinsic free functional. Transform through the C47 TM/Jacobi isometry and CM projector rather than summing unrelated one-particle expectation values.

Required checks:

```text
Hermiticity;
CM-ground preservation;
color-triplet preservation;
intrinsic/CM separation;
units and symbolic-L treatment;
mass/IR dependence;
K and Jz block conservation;
assembled versus matrix-free action;
direct intrinsic-functional agreement;
TM forward/inverse consistency.
```

Create:

```text
docs/next_level/c48_free_qg_matrix.json
docs/next_level/c48_free_qg_validation.json
```

---

# 9. Canonical SU(3) emission matrix

Consume every entry of the exhaustive C47 all-mode kinematic tuple table.

Insert the exact fundamental color tensor and C45/C47 triplet isometry to construct:

\[
\widehat V_{qg\leftarrow q}
=
\frac{1}{g_s}V_{qg\leftarrow q}.
\]

The matrix is a coefficient of \(g_s\) in the invariant-mass operator and must have the corresponding project units.

No physical value of \(g_s\) or \(\alpha_s\) is chosen.

Every nonzero matrix element must be traceable to:

```text
incoming q basis ID;
outgoing physical qg basis ID;
C47 kinematic tuple ID;
SU(3) generator/color-isometry entry;
longitudinal conservation;
helicity and Jz selection;
normalization factor;
source derivation.
```

Generate absorption solely as:

\[
\widehat V_{q\leftarrow qg}
=
\widehat V_{qg\leftarrow q}^{\dagger}.
\]

Required checks:

```text
all exhaustive tuples consumed exactly once;
no allowed tuple dropped;
no forbidden tuple activated;
Tr(T^aT^b)=delta^{ab}/2;
C_F=4/3;
triplet-image residual;
total-color covariance;
longitudinal conservation;
Jz and helicity rules;
direct frozen-element reconstruction;
sparse action versus independent tuple-sum action;
adjoint residual;
nonzero action on normalized q probes.
```

Create:

```text
docs/next_level/c48_canonical_qg_matrix.json
docs/next_level/c48_canonical_qg_validation.json
```

---

# 10. Instantaneous-fermion matrices

Use the exact C43 instantaneous-fermion action and C47 PV inverse-derivative functional.

Factor:

\[
V_{\mathrm{inst},f}
=
g_s^2\widehat V_{\mathrm{inst},f}.
\]

Audit and assemble every action-supported block among:

```text
q -> q;
q -> qg;
qg -> q;
qg -> qg.
```

Do not assume a block is nonzero or zero from its name.

Allowed block statuses:

```text
SOURCE_DERIVED_EXECUTABLE_NONZERO;
SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF;
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF;
ABSENT_BLOCKING.
```

Required checks:

```text
PV inverse-derivative domain;
P0/Q0 consistency;
Hermiticity or exact paired-adjoint relation;
K and Jz conservation;
color covariance;
CM-ground preservation;
direct matrix element versus assembled action;
boundary-prescription dependence.
```

Create:

```text
docs/next_level/c48_instantaneous_fermion_matrices.json
```

---

# 11. Instantaneous color-current/gluon matrices

Project the C43 Gauss-law-induced interaction using the C47 inverse-derivative and boundary/zero-mode functionals.

Retain separately:

```text
quark-current contribution;
gluon-current contribution;
mixed-current contribution;
local boundary/zero-mode completion.
```

Factor:

\[
V_{\mathrm{inst},g}
=
g_s^2\widehat V_{\mathrm{inst},g}.
\]

Required checks:

```text
same PV inverse-(partial^+)^2 convention as C43/C47;
Hermiticity;
SU(3) covariance;
triplet-subspace preservation;
K and Jz conservation;
CM-ground preservation;
direct versus matrix-free action;
current-source bookkeeping.
```

Create:

```text
docs/next_level/c48_instantaneous_current_matrices.json
```

---

# 12. Remaining constrained and contact matrices

Read every C43 Hamiltonian-ledger row marked:

```text
REQUIRED_AT_O_G2;
REQUIRED_AS_COUNTERTERM_OR_WARD_PARTNER.
```

For each row produce:

```text
a source-derived numerical matrix;
an exact projected zero with proof;
a proved not-applicable status;
or ABSENT_BLOCKING.
```

This includes, where applicable:

```text
fermion-constraint contact terms;
gauge-constraint contact terms;
normal-ordering/contact terms;
local basis-boundary terms;
three-/four-gluon terms required as virtual or current partners.
```

Do not classify three- or four-gluon terms solely by the absence of a qgg external basis. Use operator counting and the exact declared matrix block.

Create:

```text
docs/next_level/c48_constrained_contact_ledger.json
```

Any required `ABSENT_BLOCKING` row prevents the positive gate.

---

# 13. Residual-boundary and zero-mode matrices

Consume the exact C47 local functionals to construct action-owned matrices for:

```text
residual transverse gauge boundary field;
constrained fermion zero-mode completion;
longitudinal-gluon zero-mode control;
global Gauss-law zero-mode treatment;
local boundary/contact completion.
```

Do not construct the complete nonlocal JMY transverse link; that belongs to C49.

For each class record:

```text
matrix block;
colored-module interpretation;
P0/Q0 action;
boundary prescription;
cancellation partner;
status;
norm or exact-zero proof.
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

Create:

```text
docs/next_level/c48_boundary_zero_mode_matrices.json
```

---

# 14. Coupling-ordered block operator

Assemble immutable coefficient blocks:

\[
\mathcal M_{(0)}^2,\qquad
\mathcal M_{(1)}^2,\qquad
\mathcal M_{(2)}^2,
\]

on:

\[
\mathcal H_q\oplus\mathcal H_{qg}^{(3,\mathrm{CM}=0)}.
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

\[
\mathcal M_{(1)}^2
=
\begin{pmatrix}
0 & \widehat V_{q\leftarrow qg}\\
\widehat V_{qg\leftarrow q} & 0
\end{pmatrix},
\]

with \(\mathcal M_{(2)}^2\) containing every required instantaneous, constrained, boundary, zero-mode, and local counterterm-direction block, while keeping physical counterterm coefficients unset.

Do not diagonalize this as a physical dressed quark Hamiltonian in C48.

A deterministic dimensionless test coupling may be used only for algebraic polynomial-action checks and must never be stored as a physical parameter or result.

Create:

```text
docs/next_level/c48_local_operator_block_manifest.json
docs/next_level/c48_polynomial_action_validation.json
```

---

# 15. Projected action/current identity

Construct the strongest matrix-level identity actually derived from C43 at the \(q\oplus qg\) local-action scope.

Do not call it a full Slavnov–Taylor identity unless the exact theorem, ghost content, and source derivation support that name.

The identity must include every required contribution:

```text
canonical propagating vertex;
instantaneous fermion;
instantaneous color current/gluon;
constraint/contact terms;
local boundary term;
zero-mode completion.
```

Evaluate it:

```text
block by block;
at every physical resolution;
on deterministic basis vectors;
on random normalized complex vectors;
through assembled and matrix-free routes.
```

Report:

```text
full residual;
component residuals;
color-generator covariance residual;
resolution dependence;
signed nonzero defect after removing each required term.
```

No coefficient may be tuned to force closure.

Create:

```text
docs/next_level/c48_projected_action_identity_report.json
```

---

# 16. Local counterterm-direction matrices

Construct the source-derived local directions required by the later one-loop renormalization problem.

Audit at least:

```text
quark mass direction;
quark field/residue or metric direction;
canonical qg vertex direction;
instantaneous-partner direction;
local basis-boundary/regulator direction.
```

When a field/residue variation changes the generalized metric rather than only the operator matrix, store the correct matrix pair or generalized-eigenproblem direction. Do not force every counterterm into an additive Hamiltonian matrix.

For each direction provide:

```text
source/action authority;
parameter definition;
operator or metric derivative;
coupling/order label;
matrix blocks;
independent finite-difference check;
rank and linear-independence diagnostics.
```

Do not solve physical coefficients.

Do not create nonlocal Wilson, cusp, endpoint, transverse-link, or bilocal counterterm directions; those belong to C49.

Create:

```text
docs/next_level/c48_local_counterterm_directions.json
docs/next_level/c48_local_counterterm_rank_report.json
```

---

# 17. Execute physical comparison maps

Consume the C47 q and qg comparison maps.

Test every C48 local operator under adjacent-resolution comparison.

For each operator \(O\), evaluate the exact supported relation, schematically:

\[
R\,O_{r'}\,P
\quad\text{versus}\quad
O_r.
\]

Retain separately:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
color-triplet remainder;
zero-mode/boundary remainder;
numerical error.
```

Execute for:

```text
free q matrix;
free qg matrix;
canonical vertex;
instantaneous matrices;
constraint/contact matrices;
boundary/zero-mode matrices;
local counterterm directions.
```

These are comparison diagnostics, not a continuum extrapolation.

Create:

```text
docs/next_level/c48_operator_comparison_report.json
docs/next_level/c48_comparison_remainder_ledger.json
```

---

# 18. Deterministic runtime bundles

For every physical resolution produce content-addressed runtime bundles containing:

```text
basis-order identities;
free q and qg matrices;
canonical emission and absorption matrices;
instantaneous-fermion matrices;
instantaneous-current/gluon matrices;
all constrained/contact matrices;
boundary/zero-mode matrices and projectors;
coupling-ordered block matrices;
local counterterm directions;
comparison-map execution blocks;
matrix-free reconstruction metadata.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c48_hqcd/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
coupling power;
basis-order hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c48_numerical_object_inventory.json
```

All bundles must regenerate byte-for-byte.

---

# 19. C40 isolation

Compare C48 with C40 only as a method-oracle regression.

Report:

```text
dimension and block-structure differences;
norm and sparsity differences;
which C40 serialization, matrix-free, and mutation tests remain reusable.
```

Do not:

```text
fit C48 to C40;
reuse C40 coefficients;
rescale C40 arrays;
use numerical similarity as evidence of source identity.
```

Create:

```text
docs/next_level/c48_c40_method_oracle_comparison.json
```

---

# 20. End-to-end source-to-local-matrix test

Implement an end-to-end test that begins from C43 source/action records, C45 mode records, and C47 physical-basis records—not from prebuilt C48 arrays.

It must:

```text
regenerate physical basis identities;
assemble free q and qg matrices;
consume all canonical tuples and insert exact SU(3);
generate the absorption adjoint;
assemble instantaneous and constrained matrices;
assemble boundary/zero-mode matrices;
construct coupling-ordered blocks;
construct local counterterm directions;
execute the projected action identity;
execute comparison-map checks;
reproduce all numerical hashes.
```

It must fail when:

```text
a C47 basis row is removed;
the CM projector is omitted;
the free-operator factor is changed;
L is assigned arbitrarily;
a canonical tuple is dropped or duplicated;
a Gell-Mann generator changes;
the triplet isometry is replaced;
a C40 matrix is substituted;
an instantaneous term is removed;
the PV prescription changes;
a zero-mode projector changes;
the local boundary term is omitted;
a field counterterm is forced into the wrong additive form;
a runtime hash is altered.
```

---

# 21. Focused mutation tests

Create at least **224 focused live mutations** of actual source-to-matrix inputs and arrays.

Include mutations of:

```text
free-operator normalization;
intrinsic free functional;
CM projector;
canonical tuple value;
tuple multiplicity;
SU(3) generator;
triplet isometry;
vertex adjoint;
instantaneous denominator;
current color factor;
constraint/contact term;
boundary functional;
zero-mode projector;
operator block ordering;
counterterm derivative;
comparison map;
matrix-free action;
runtime-array hash.
```

Every mutation must fail a concrete source, Hermiticity, covariance, action-identity, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 22. Readiness gate

Issue:

```text
C48_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

only when:

```text
the complete C43, C45, and C47 baselines reproduce;
every consumed C47 object passes the fidelity audit;
free q and qg matrices exist at all physical resolutions;
the canonical SU(3) emission matrix consumes every allowed tuple exactly once;
absorption is the generated adjoint;
all required instantaneous matrices have executable/proved statuses;
all required constraint/contact matrices have executable/proved statuses;
the local boundary and zero-mode contracts are assembled;
the coupling-ordered block operator is complete at declared scope;
the projected action/current identity closes;
each required-term ablation produces a nonzero defect;
local counterterm directions exist and are correctly typed;
comparison-map diagnostics are executed;
all runtime bundles reproduce byte-for-byte;
the end-to-end source-to-local-matrix test passes.
```

Do not issue:

```text
C48_JMY_WILSON_MATRIX_VALIDATED;
C48_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C48_ONE_LOOP_TMD_VALIDATED;
C48_MATCHING_KERNEL_VALIDATED;
C48_MICROSCOPIC_PROTON_TMD_EXPORTED.
```

---

# 23. Exact no-go branches

## A. C47 basis/functionals are incomplete in execution

```text
C48_PHYSICAL_BASIS_CONSUMPTION_INCOMPLETE
```

Next:

> **C49/BASIS2 — targeted physical-basis/runtime-functional completion**

## B. Free matrices cannot be assembled

```text
C48_FREE_HAMILTONIAN_ASSEMBLY_INCOMPLETE
```

Next:

> **C49/HFREE — source-derived invariant-mass matrix completion**

## C. Canonical vertex cannot be assembled

```text
C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE
```

Next:

> **C49/VERTEX1 — exhaustive tuple/SU(3)/triplet canonical-matrix completion**

## D. Instantaneous, constrained, boundary, or zero-mode matrices remain incomplete

```text
C48_CONSTRAINED_OPERATOR_ASSEMBLY_INCOMPLETE
```

Next:

> **C49/Z2 — local instantaneous, constrained, boundary, and zero-mode matrix completion**

## E. Projected action identity fails

```text
C48_PROJECTED_ACTION_IDENTITY_FAILED
```

Next:

> **C49/G3 — missing local term and projected action/current identity completion**

## F. Local counterterm directions remain incomplete

```text
C48_LOCAL_COUNTERTERM_DIRECTIONS_INCOMPLETE
```

Next:

> **C49/CTLOCAL — source-derived local partonic counterterm-direction completion**

## G. Physical comparison execution remains incomplete

```text
C48_OPERATOR_COMPARISON_INCOMPLETE
```

Next:

> **C49/R1E — local-operator comparison-map and nonnested-remainder completion**

## H. All local-QCD matrix gates close

```text
C48_SOURCE_DERIVED_HQCD_OPERATOR_SUBSTRATE_READY
```

Next:

> **C49/WX — source-derived finite-basis JMY Wilson operator, bilocal TMD measurement, nonlocal counterterm directions, and distributional/refinement maps**

---

# 24. Required deliverables

Create at least:

```text
docs/next_level/c48_implementation_report.md
docs/next_level/c48_api.md
docs/next_level/c48_derivation_authority_manifest.json
docs/next_level/c48_input_fidelity_audit.json
docs/next_level/c48_dimension_resource_preflight.json
docs/next_level/c48_physical_resolution_manifest.json
docs/next_level/c48_basis_order_manifest.json

docs/next_level/c48_free_q_matrix.json
docs/next_level/c48_free_q_validation.json
docs/next_level/c48_free_qg_matrix.json
docs/next_level/c48_free_qg_validation.json

docs/next_level/c48_canonical_qg_matrix.json
docs/next_level/c48_canonical_qg_validation.json

docs/next_level/c48_instantaneous_fermion_matrices.json
docs/next_level/c48_instantaneous_current_matrices.json
docs/next_level/c48_constrained_contact_ledger.json
docs/next_level/c48_boundary_zero_mode_matrices.json

docs/next_level/c48_local_operator_block_manifest.json
docs/next_level/c48_polynomial_action_validation.json
docs/next_level/c48_projected_action_identity_report.json

docs/next_level/c48_local_counterterm_directions.json
docs/next_level/c48_local_counterterm_rank_report.json

docs/next_level/c48_operator_comparison_report.json
docs/next_level/c48_comparison_remainder_ledger.json

docs/next_level/c48_numerical_object_inventory.json
docs/next_level/c48_c40_method_oracle_comparison.json

docs/next_level/c48_readiness_report.json
docs/next_level/c48_source_sufficiency_decision.json
docs/next_level/c48_no_go_decision_tree.json
docs/next_level/c48_missing_calculation_specification.md
docs/next_level/c48_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/hqcd2/
```

or the repository-equivalent package.

Add focused tests for:

```text
free matrices;
canonical vertex;
instantaneous and constrained matrices;
boundary/zero-mode assembly;
coupling-ordered blocks;
projected action identity;
counterterm directions;
operator comparison;
end-to-end source-to-matrix reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 25. Acceptance criteria

C48 is complete only when:

1. The full C47 baseline reproduces.
2. The C46 no-go remains explicit.
3. The C43 gauge/action contract remains unchanged.
4. The C45 mode contract remains unchanged.
5. C40 remains method-oracle only.
6. The physical half-integer-\(K\) trajectory is used.
7. The finite support minima remain distinct from the endpoint regulator.
8. \(L\) remains symbolic or its cancellation is proved.
9. Every C47 basis/function consumed is numerically present and source linked.
10. No physical basis state is pruned for runtime convenience.
11. Free q matrices exist at all resolutions.
12. Free qg matrices exist at all resolutions.
13. Free matrices preserve the CM-ground triplet module.
14. Assembled and matrix-free free actions agree.
15. The canonical emission matrix consumes every exhaustive tuple once.
16. Its color insertion is exact SU(3).
17. Its image lies in the qg triplet.
18. Absorption is the generated adjoint.
19. Longitudinal, Jz, helicity, color, and CM rules close.
20. Every required instantaneous-fermion block has an executable/proved status.
21. Every required instantaneous-current block has an executable/proved status.
22. Every required constrained/contact row has an executable/proved status.
23. Local boundary and zero-mode matrices implement C43/C47.
24. The coupling-ordered local block operator is complete at declared scope.
25. The projected action/current identity closes.
26. Removing every required term gives a nonzero defect.
27. Local counterterm directions are source derived.
28. Metric directions are not misrepresented as additive matrices.
29. No physical counterterm coefficient is solved.
30. Operator comparison maps are executed.
31. Nonnested-grid and truncation remainders remain visible.
32. Numerical bundles contain actual arrays and operators.
33. End-to-end reconstruction passes.
34. At least 224 live mutations are detected.
35. No complete JMY Wilson matrix is claimed.
36. No bilocal TMD measurement is claimed.
37. No one-loop coefficient or matching kernel is created.
38. No proton TMD or ART25 bridge is created.
39. No fit, inference, process, or production route is created.
40. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
41. `MSHT20_REP/` remains untouched and outside Git.
42. The working tree is clean except for the pre-existing untracked directory.
43. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken exhaustive tuple consumption, constrained-sector completeness, zero-mode ownership, or the projected action identity to open the gate.

---

# 26. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47 inputs consumed;
- fidelity-audit counts;
- physical dimensions and resource strategy;
- free q and qg matrix shapes, nnz, units, spectra/bounds, symbolic-\(L\) treatment, and matrix-free residuals;
- canonical matrix shape, nnz, norm, exhaustive tuple accounting, SU(3)/Casimir/triplet residuals, and adjoint residual;
- instantaneous matrix shapes, norms, block statuses, and direct-check residuals;
- constrained/contact ledger statuses;
- boundary and zero-mode matrix statuses and norms;
- coupling-ordered block shapes and polynomial-action residuals;
- projected action/current residual and every ablation defect;
- local counterterm-direction shapes, rank, and finite-difference residuals;
- operator-comparison residuals and separated remainders;
- runtime-bundle hashes;
- C40 method-oracle comparison;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no complete JMY Wilson matrix, bilocal TMD measurement, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe the C47 basis/functionals alone, a partially consumed tuple table, a matrix with omitted action-owned terms, or an identity closed by fitted coefficients as a source-derived local QCD operator substrate.
