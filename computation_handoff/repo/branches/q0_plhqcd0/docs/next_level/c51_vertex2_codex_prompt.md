# C51/VERTEX2 Codex Work Package

## Title

**Exhaustive source-derived physical canonical vertex: arbitrary-mode evaluation, count-once sparse assembly, exact SU(3) \(3\otimes8\!\to3\) insertion, generated adjoint, matrix-free closure, and physical-resolution comparison**

## Authoritative baseline

Start from the clean local C50/VSRC completion commit:

```text
ad3adeda99ab1115d07284a9c502c5959f08b6e4
```

Its immediate scientific parent is:

```text
c940136ab9038d9bda91db21650c292a27927506
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor c940136ab9038d9bda91db21650c292a27927506 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE

C49_CANONICAL_SOURCE_CHAIN_INCOMPLETE

C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
```

and the exact C50 scientific boundary:

```text
source-qualified C43/C45 finite-cell color-stripped
canonical P-minus kernel;

exact project sqrt(2) light-front convention map;

proved conversion:
    M^2 = 2 P^+ P^- - P_perp^2;

individual C45/C47 physical-mode evaluator;

three Abelian sources used only as convention/method cross-checks;

historical BLFQ omitted factor of two retained as a required
negative control;

all 3,618 C47 raw canonical tuples diagnostic-only;

no exhaustive vertex matrix assembled.
```

Verify every identity from the committed C50 records rather than relying on this prompt.

The fixed physical architecture remains:

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

longitudinal box:
    L remains symbolic unless C50 proves exact cancellation
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

The C47 raw tuple values remain immutable historical diagnostics and are forbidden as numerical inputs to C51.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C51 consumes the C50 arbitrary-mode evaluator and assembles the complete coupling-factored physical canonical vertex on:

\[
\mathcal H_q
\longrightarrow
\mathcal H_{qg}^{(3,\mathrm{CM}=0)}
\]

at every physical resolution.

C51 must create:

```text
an exhaustive basis-pair and selection-rule ledger;

dimensionally homogeneous color-stripped component matrices;

the complete color-stripped M^2 emission matrix;

the exact open-color SU(3) emission intertwiner;

the complete total-color-triplet q -> qg emission matrix;

the generated qg -> q Hermitian adjoint;

an independent matrix-free action that re-evaluates C50
matrix elements rather than multiplying by the stored sparse matrix;

a Hermitian g_s-linear two-sector block operator;

count-once, unit, convention, source-ancestry, holdout,
and physical-resolution comparison diagnostics.
```

The physical coupling remains factored:

\[
V_{qg\leftarrow q}^{(M^2)}
=
g_s\,\widehat V_{qg\leftarrow q}^{(M^2)}.
\]

Do not choose or fit \(g_s\) or \(\alpha_s\).

The strongest allowed status is:

```text
C51_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

When that gate passes, the exact next package is:

> **C52/HQCD2 — assemble the remaining source-derived local-QCD operator substrate: free, instantaneous, constrained, boundary/zero-mode, and local-counterterm matrices, followed by the projected action identity**

---

# 2. Scientific boundary

C51 is:

```text
canonical q <-> qg vertex specific;
physical-basis exhaustive;
source-derived through C50;
dimensionally typed;
open-color and total-triplet aware;
coupling-factored;
sparse/matrix-free;
deterministic;
validation-only.
```

C51 is not:

```text
a repair or promotion of the C47 raw tuples;
a fit of a coupling or normalization;
a free-Hamiltonian package;
an instantaneous-interaction package;
a dressed-quark eigenproblem;
a JMY Wilson-line package;
a bilocal TMD package;
a one-loop calculation;
a proton or ART25 calculation.
```

Do not extend C51 merely because another local matrix is easy to assemble. The package boundary is the canonical vertex only.

---

# 3. Nonnegotiable authority chain

Every nonzero physical matrix entry must descend through:

```text
locked primary-source canonical QCD interaction
    -> C43 project-convention operator
    -> C45 normalized longitudinal/HO/spinor/polarization modes
    -> C47 physical CM-clean q and qg basis identities
    -> C50 finite-cell P^- kernel
    -> C50 proved P^- to M^2 conversion
    -> C50 arbitrary-mode evaluator
    -> exact SU(3) tensor and triplet isometry
    -> C51 sparse matrix entry.
```

Every final entry must record or be traceable to:

```text
incoming q basis ID;
outgoing qg basis ID;
resolution and conserved block;
C50 evaluator call identity;
source/operator component IDs;
symbolic parameter signature;
units;
selection-rule decision;
color tensor identity;
triplet-isometry identity;
coupling power;
generator-code hash;
matrix-shard hash.
```

The following are forbidden as physical entry authorities:

```text
C47 raw tuple value;
C47 historical tuple count;
C40 matrix or coefficient;
a color-singlet hadron-model matrix;
a representative C50 holdout substituted for another mode;
a matrix value inferred from desired Hermiticity or continuity.
```

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json

docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_cm_factorization_report.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c50_implementation_report.md
docs/next_level/c50_derivation_authority_manifest.json
docs/next_level/c50_convention_map.json
docs/next_level/c50_finite_volume_state_normalization.json
docs/next_level/c50_finite_box_pminus_kernel.json
docs/next_level/c50_pminus_to_m2_derivation.json
docs/next_level/c50_canonical_component_decomposition.json
docs/next_level/c50_arbitrary_mode_vertex_evaluator.json
docs/next_level/c50_basis_projection_validation.json
docs/next_level/c50_continuum_splitting_crosscheck.json
docs/next_level/c50_abelian_blfq_crosscheck.json
docs/next_level/c50_coordinate_momentum_equivalence.json
docs/next_level/c50_unit_covariance_report.json
docs/next_level/c50_regulator_scaling_report.json
docs/next_level/c50_c51_vertex_assembly_contract.json
docs/next_level/c50_numerical_object_inventory.json
docs/next_level/c50_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c51_derivation_authority_manifest.json
```

---

# 5. Input-fidelity and dependency audit

Before enumerating matrix entries, verify that the C50 evaluator is an actual executable function over physical basis IDs.

For every required dependency classify:

```text
SOURCE_DERIVED_EXECUTABLE;
SOURCE_DERIVED_SYMBOLIC_COMPONENT;
SOURCE_DERIVED_BASIS_IDENTITY;
DIAGNOSTIC_ONLY;
ABSENT_BLOCKING.
```

The positive path may consume only the first three classes.

Explicitly prove that the C51 assembly dependency graph does **not** read the numerical value field of any C47 raw canonical tuple.

Implement both:

```text
a static/import dependency guard;

a runtime poisoning test in which every C47 raw tuple value is replaced
by NaN or a sentinel while the C51 evaluator and matrix remain unchanged.
```

C47 basis IDs, TM/CM transformations, and comparison maps remain valid inputs; only the historical canonical tuple values are prohibited.

Create:

```text
docs/next_level/c51_input_fidelity_audit.json
docs/next_level/c51_raw_tuple_independence_report.json
```

If the evaluator requires any raw tuple value, issue:

```text
C51_C50_EVALUATOR_NOT_INDEPENDENT
```

and stop.

---

# 6. Freeze basis, parameter, and phase identities

For each resolution freeze:

```text
K, Nmax, bHO;
q basis ordering and block labels;
CM-clean triplet qg basis ordering and block labels;
open-color module convention;
triplet-isometry phase;
helicity and polarization phases;
Fourier and HO phases;
mass/IR parameter convention;
symbolic L signature;
P^+ convention;
M^2 units;
comparison maps.
```

Keep distinct:

```text
finite one-fermion support minima:
    1/9, 1/11, 1/13

C7 endpoint regulator:
    1/18
```

The endpoint regulator must not change the basis enumeration.

Do not insert a numerical value for a symbolic parameter that C50 leaves unfixed.

When the C50 evaluator returns a finite linear combination such as:

\[
\widehat V
=
\widehat V_{\perp}
+
m_q\,\widehat V_m
\]

or an equivalent source-derived component decomposition, assemble the component matrices separately and store the exact symbolic assembly rule.

A symbolic component family is acceptable. An element-dependent unit or symbolic signature is not.

Create:

```text
docs/next_level/c51_physical_resolution_manifest.json
docs/next_level/c51_basis_order_manifest.json
docs/next_level/c51_symbolic_parameter_contract.json
```

---

# 7. Resource and sparse-assembly preflight

Enumerate, without evaluating a vertex value:

```text
q dimensions by block;
qg dimensions by block;
all candidate q/qg basis pairs;
pairs rejected by exact conserved quantum numbers;
pairs admitted to C50 evaluation;
expected shard sizes;
memory and runtime estimates.
```

The qg total dimensions are expected to be:

```text
1,344 / 2,700 / 4,752
```

but verify them from C47.

Do not allocate a dense matrix merely for convenience.

Use:

```text
blockwise CSR/CSC sparse matrices;
content-addressed shards;
and an independent matrix-free evaluator.
```

No physically allowed pair may be pruned to meet a runtime target.

Create:

```text
docs/next_level/c51_dimension_resource_preflight.json
```

---

# 8. Exhaustive basis-pair ledger

Construct the exhaustive Cartesian basis-pair domain:

\[
(\beta,\alpha)
\in
\mathcal B_{qg}^{\rm phys}
\times
\mathcal B_q.
\]

Apply only exact, source-owned pre-evaluation selection rules:

```text
resolution identity;
total K;
total transverse momentum/CM frame;
total Jz;
flavor conservation;
allowed helicity/polarization domain;
zero-mode domain;
colored-module domain.
```

Every candidate pair receives exactly one status:

```text
PRESELECTION_FORBIDDEN_EXACT;
EVALUATED_EXACT_ZERO;
EVALUATED_NONZERO;
EVALUATOR_UNAVAILABLE_BLOCKING;
DUPLICATE_BLOCKING.
```

For every evaluated pair, call the C50 arbitrary-mode evaluator. Do not infer a value by symmetry from another pair except through an explicitly stored exact relation that is independently checked.

The historical C47 counts:

```text
720 / 1,170 / 1,728
```

are diagnostic comparisons only. They are not expected nonzero counts and may not control enumeration.

Create:

```text
docs/next_level/c51_exhaustive_basis_pair_ledger.json
docs/next_level/c51_selection_rule_report.json
```

A positive gate requires:

```text
EVALUATOR_UNAVAILABLE_BLOCKING = 0
DUPLICATE_BLOCKING = 0.
```

---

# 9. Evaluate and assemble source-derived component matrices

Use the exact C50 component decomposition.

For every source-derived component, assemble a color-stripped sparse matrix:

\[
\widehat V_{\rm kin}^{(r,c)}
\]

where \(r\) labels resolution and \(c\) labels the source-owned operator component.

Examples may include mass and transverse structures, but use the actual C50 component IDs.

Each component matrix must have:

```text
one uniform unit/signature;
one declared symbolic factor;
one coupling power;
one source/operator identity.
```

Then construct the complete color-stripped coefficient matrix:

\[
\widehat V_{\rm kin}^{(M^2)}
=
\sum_c s_c(\text{declared parameters})
\,\widehat V_{\rm kin}^{(c)}.
\]

Required checks:

```text
every evaluated pair consumed once;
component sum equals direct C50 evaluator;
uniform mass-squared output;
symbolic-L cancellation or one common factored signature;
GeV/MeV covariance;
coordinate/momentum holdout reproduction;
C50 frozen-holdout reproduction.
```

Create:

```text
docs/next_level/c51_colorless_component_matrices.json
docs/next_level/c51_colorless_vertex_matrix.json
docs/next_level/c51_colorless_vertex_validation.json
```

---

# 10. Exact SU(3) emission intertwiner

Construct the color-product emission tensor:

\[
E_{(c',a),c}
=
(T^a)_{c'c},
\qquad
T^a=\frac{\lambda^a}{2}.
\]

Let:

\[
U_3:
\mathbb C^3
\longrightarrow
\mathbb C^3\otimes\mathbb C^8
\]

be the exact C45/C47 \(24\times3\) triplet isometry in its frozen phase convention.

Construct the triplet emission intertwiner:

\[
C_{\rho c}
=
\sum_{c',a}
(U_3)_{(c',a),\rho}^{*}
(T^a)_{c'c}.
\]

Do not assume that \(C_{\rho c}\) is literally diagonal before accounting for the frozen input/output triplet phase and basis convention.

Required checks:

```text
Tr(T^a T^b)=delta^{ab}/2;
C_F=4/3;
U_3^\dagger U_3=I_3;
the raw emission tensor lies entirely in the triplet image;
C^\dagger C=C_F I_3;
rank(C)=3;
total-generator intertwining/covariance;
basis-rotation invariance;
no 6bar or 15 leakage;
no singlet substitution.
```

Create:

```text
docs/next_level/c51_color_emission_intertwiner.json
docs/next_level/c51_color_intertwiner_validation.json
```

If the canonical emission tensor does not lie completely in the retained triplet image, issue the exact color no-go rather than projecting away a nonzero remainder silently.

---

# 11. Assemble the physical emission matrix

Insert the exact color intertwiner into the color-stripped kinematic matrix according to the frozen C47 basis order.

Construct:

\[
\widehat V_{qg\leftarrow q}^{(M^2)}
=
\frac{1}{g_s}
V_{qg\leftarrow q}^{(M^2)}.
\]

Every nonzero entry must retain ancestry to:

```text
physical basis pair;
C50 evaluator result;
component decomposition;
color-intertwiner entry;
triplet-isometry identity.
```

Required checks:

```text
shape;
nnz;
mass-squared units;
basis-order compatibility;
triplet-image identity;
color covariance;
K, Jz, helicity, and flavor rules;
nonzero action on normalized q vectors;
direct frozen-entry reconstruction;
blockwise sparse action.
```

Create:

```text
docs/next_level/c51_physical_canonical_emission_matrix.json
docs/next_level/c51_physical_emission_validation.json
```

---

# 12. Independent matrix-free action

Implement a matrix-free action:

```python
apply_canonical_emission(vector_q, resolution, parameters)
```

that:

```text
enumerates the exact admitted basis-pair domain;
calls the C50 evaluator directly;
inserts the exact color intertwiner;
accumulates the qg vector.
```

It must not:

```text
multiply by the stored C51 sparse matrix;
load the C51 tuple-value table as its numerical authority;
load any C47 raw tuple value.
```

Compare sparse and matrix-free actions on:

```text
every basis vector in small blocks;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions.
```

Create:

```text
docs/next_level/c51_matrix_free_emission_report.json
```

---

# 13. Generate absorption only as the adjoint

Define:

\[
\widehat V_{q\leftarrow qg}^{(M^2)}
=
\left(
\widehat V_{qg\leftarrow q}^{(M^2)}
\right)^\dagger.
\]

Do not independently evaluate, fit, or phase-adjust absorption entries.

Construct the coupling-linear two-sector block:

\[
\mathcal M_{(1)}^2
=
\begin{pmatrix}
0 & \widehat V_{q\leftarrow qg}^{(M^2)}
\\[1mm]
\widehat V_{qg\leftarrow q}^{(M^2)} & 0
\end{pmatrix}.
\]

Required checks:

```text
adjoint residual;
block Hermiticity;
basis-order identity;
sparse/matrix-free equality;
nonzero action in both directions;
phase-convention stability.
```

Create:

```text
docs/next_level/c51_vertex_adjoint_report.json
docs/next_level/c51_linear_block_operator_validation.json
```

Do not diagonalize this block as a dressed physical quark state.

---

# 14. Count-once and completeness audit

Report for every resolution:

```text
total Cartesian basis pairs;
exact preselection rejections;
C50 evaluator calls;
evaluated exact zeros;
evaluated nonzeros;
component records;
final sparse nnz;
duplicate records;
missing records;
blocking records.
```

Distinguish:

```text
multiple source components contributing to one matrix entry;

from

duplicate evaluation of the same source component.
```

A positive gate requires:

```text
duplicate source-component count = 0;
missing admitted-pair count = 0;
blocking count = 0.
```

Create:

```text
docs/next_level/c51_count_once_report.json
docs/next_level/c51_matrix_completeness_report.json
```

---

# 15. Holdouts and independent reconstruction

Freeze C51 holdouts before complete assembly, including:

```text
at least four nonzero entries per resolution;
both independent C50 operator-component types where present;
both quark helicities;
both gluon helicities;
smallest and largest allowed x_g;
nontrivial intrinsic OAM;
one exact-zero entry;
one color-phase entry;
one symbolic-parameter entry;
one coordinate/momentum route entry;
one Abelian-limit entry.
```

Evaluate every holdout through at least two independent routes.

No failed holdout may be moved into construction or excluded after inspection.

Create:

```text
docs/next_level/c51_holdout_plan.json
docs/next_level/c51_holdout_validation.json
```

---

# 16. Unit, symbolic-parameter, and convention covariance

Re-execute C50’s checks at full-matrix level.

## 16.1 GeV/MeV conversion

All physical emission-matrix entries must scale as mass squared.

## 16.2 Symbolic \(L\)

Verify the C50-predicted cancellation or block-common factor. No element-dependent \(L\) signature is allowed.

## 16.3 \(P^+\) and fixed-\(x\) rescaling

Verify the exact C50 conversion law.

## 16.4 \(b_{\rm HO}\) and basis changes

Test the analytic component scaling and the physical comparison map. Do not require entrywise invariance across different bases.

## 16.5 Fourier, helicity, and triplet phase conventions

Round-trip all frozen phase conventions.

## 16.6 Historical factor-of-two control

The omitted or duplicated BLFQ factor of two must fail the full-matrix convention test.

Create:

```text
docs/next_level/c51_unit_convention_covariance_report.json
```

---

# 17. Physical-resolution comparison

Use the C47 physical comparison maps to evaluate:

\[
R_{qg}\,
\widehat V_{r'}\,
P_q
\quad\text{versus}\quad
\widehat V_r.
\]

Separate:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
color-triplet remainder;
symbolic-parameter/normalization remainder;
numerical error.
```

This is a regulator comparison diagnostic, not a continuum extrapolation or fit.

Do not tune the vertex to reduce the comparison residual.

Create:

```text
docs/next_level/c51_vertex_comparison_report.json
docs/next_level/c51_vertex_remainder_ledger.json
```

---

# 18. Historical C47 tuple comparison

Preserve the C50 diagnostic classifications.

After the C51 matrix exists, compare the historical C47 tuples only diagnostically.

Allowed statuses remain:

```text
AGREES_AFTER_EXPLICIT_REFACTORIZATION;
DIFFERS_BY_IDENTIFIED_OMITTED_FACTOR;
DIFFERS_BY_CONVENTION_MAP;
AMBIGUOUS_HISTORICAL_ORACLE;
EXACT_ZERO_CONSISTENT.
```

No C47 tuple becomes a matrix authority through agreement.

The new C51 nonzero count is not required to equal the C47 raw tuple count.

Create:

```text
docs/next_level/c51_c47_historical_comparison.json
```

---

# 19. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
basis-pair ledger;
component sparse matrices;
colorless complete matrix;
color emission intertwiner;
physical emission matrix;
generated absorption adjoint;
linear block operator shards;
matrix-free evaluation metadata;
holdout records;
comparison-map execution blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c51_vertex2/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
symbolic-factor signature;
coupling power;
basis-order hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c51_numerical_object_inventory.json
```

All bundles must regenerate byte-for-byte.

---

# 20. End-to-end source-to-matrix test

Implement an end-to-end test that begins with the C43/C45/C47/C50 contracts—not with a prebuilt C51 matrix.

It must:

```text
load the physical bases;
enumerate every basis pair;
apply exact selection rules;
evaluate every admitted pair with C50;
assemble source-component matrices;
construct the exact color intertwiner;
assemble the physical emission matrix;
generate the adjoint;
compare sparse and matrix-free actions;
run count-once, holdout, unit, phase, and comparison tests;
reproduce all hashes.
```

It must fail when:

```text
a C47 raw tuple value is consumed;
a C50 representative holdout is reused for another mode;
an admitted pair is skipped;
a pair is duplicated;
an exact-zero rule is changed;
an operator component is omitted;
an unproved symbolic factor is inserted;
a Gell-Mann generator changes;
the triplet isometry changes;
6bar or 15 leakage is projected away silently;
the absorption matrix is independently altered;
the BLFQ factor-of-two error is reintroduced;
a C40 matrix is substituted;
a runtime hash changes.
```

---

# 21. Focused mutation tests

Create at least **224 focused live mutations** of actual domains, evaluator calls, component records, color tensors, or matrices.

Include mutations of:

```text
basis ordering;
selection-rule status;
C50 evaluator input;
C50 evaluator output unit;
source-component ancestry;
symbolic L/P+/mass/bHO signature;
pair count;
duplicate source component;
exact-zero status;
SU(3) generator;
triplet isometry;
color intertwiner;
matrix entry;
matrix-free accumulation;
adjoint;
unit conversion;
phase convention;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, count-once, dimensional, color, adjoint, matrix-free, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 22. Readiness gate

Issue:

```text
C51_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

only when:

```text
the full C50 baseline reproduces;
the C50 evaluator is independent of C47 raw tuple values;
all physical basis pairs receive one exact status;
every admitted pair is evaluated successfully;
all component matrices have homogeneous units;
the complete colorless M^2 matrix closes;
the exact SU(3) emission tensor lies in the retained triplet;
the color intertwiner has the required rank, Casimir, and covariance;
the complete physical emission matrix exists at all resolutions;
the matrix-free action is independent and agrees;
absorption is the generated adjoint;
the g_s-linear block is Hermitian;
count-once and completeness audits close;
all frozen holdouts pass;
matrix-level unit and convention covariance passes;
physical-resolution comparisons execute;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-matrix test passes.
```

Do not issue:

```text
C51_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C51_FREE_HAMILTONIAN_VALIDATED;
C51_INSTANTANEOUS_OPERATOR_VALIDATED;
C51_JMY_WILSON_MATRIX_VALIDATED;
C51_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C51_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 23. Exact no-go branches

## A. C50 evaluator cannot cover the complete physical basis

```text
C51_EVALUATOR_DOMAIN_INCOMPLETE
```

Next:

> **C52/PROJ3 — complete the source-derived arbitrary-mode physical-basis evaluator**

## B. C51 depends on C47 raw tuple values

```text
C51_C50_EVALUATOR_NOT_INDEPENDENT
```

Next:

> **C52/INDEP1 — remove historical-tuple dependence from the canonical evaluator and assembly chain**

## C. Exhaustive pair enumeration or count-once closure fails

```text
C51_EXHAUSTIVE_VERTEX_ENUMERATION_INCOMPLETE
```

Next:

> **C52/ENUM1 — physical basis-pair domain, selection-rule, and count-once completion**

## D. Dimensional or symbolic-parameter homogeneity fails

```text
C51_VERTEX_DIMENSIONAL_ASSEMBLY_INCOMPLETE
```

Next:

> **C52/VDIM2 — component-matrix units and symbolic-factor assembly completion**

## E. SU(3)/triplet insertion fails

```text
C51_COLOR_TRIPLET_VERTEX_INCOMPLETE
```

Next:

> **C52/COLORV2 — exact emission intertwiner and triplet-image completion**

## F. Sparse and matrix-free routes disagree

```text
C51_VERTEX_ACTION_CLOSURE_FAILED
```

Next:

> **C52/VACT1 — independent sparse/matrix-free canonical-action completion**

## G. Physical canonical vertex closes

```text
C51_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

Next:

> **C52/HQCD2 — assemble the remaining local-QCD operator substrate and projected action identity**

---

# 24. Required deliverables

Create at least:

```text
docs/next_level/c51_implementation_report.md
docs/next_level/c51_api.md
docs/next_level/c51_derivation_authority_manifest.json

docs/next_level/c51_input_fidelity_audit.json
docs/next_level/c51_raw_tuple_independence_report.json
docs/next_level/c51_physical_resolution_manifest.json
docs/next_level/c51_basis_order_manifest.json
docs/next_level/c51_symbolic_parameter_contract.json
docs/next_level/c51_dimension_resource_preflight.json

docs/next_level/c51_exhaustive_basis_pair_ledger.json
docs/next_level/c51_selection_rule_report.json

docs/next_level/c51_colorless_component_matrices.json
docs/next_level/c51_colorless_vertex_matrix.json
docs/next_level/c51_colorless_vertex_validation.json

docs/next_level/c51_color_emission_intertwiner.json
docs/next_level/c51_color_intertwiner_validation.json

docs/next_level/c51_physical_canonical_emission_matrix.json
docs/next_level/c51_physical_emission_validation.json
docs/next_level/c51_matrix_free_emission_report.json

docs/next_level/c51_vertex_adjoint_report.json
docs/next_level/c51_linear_block_operator_validation.json

docs/next_level/c51_count_once_report.json
docs/next_level/c51_matrix_completeness_report.json
docs/next_level/c51_holdout_plan.json
docs/next_level/c51_holdout_validation.json

docs/next_level/c51_unit_convention_covariance_report.json
docs/next_level/c51_vertex_comparison_report.json
docs/next_level/c51_vertex_remainder_ledger.json
docs/next_level/c51_c47_historical_comparison.json

docs/next_level/c51_numerical_object_inventory.json
docs/next_level/c51_readiness_report.json
docs/next_level/c51_source_sufficiency_decision.json
docs/next_level/c51_no_go_decision_tree.json
docs/next_level/c51_missing_calculation_specification.md
docs/next_level/c51_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/vertex2/
```

or the repository-equivalent package.

Add focused tests for:

```text
raw-tuple independence;
basis-pair enumeration;
C50 evaluator coverage;
component assembly;
dimensional homogeneity;
SU(3)/triplet intertwiner;
sparse and matrix-free action;
adjoint and block Hermiticity;
count once;
holdouts;
unit and phase covariance;
resolution comparison;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 25. Acceptance criteria

C51 is complete only when:

1. The full C50 baseline reproduces.
2. The C49 no-go remains explicit.
3. The C43 action, C45 mode, and C47 basis contracts remain unchanged.
4. C40 remains method-oracle only.
5. C47 raw tuple files remain byte-identical.
6. C47 raw tuple values are never consumed by C51.
7. The runtime poisoning test proves raw-tuple independence.
8. No arbitrary numerical \(L\) is introduced.
9. No physical coupling is chosen.
10. All symbolic parameters remain typed and source owned.
11. Every physical basis pair receives one status.
12. Exact preselection rules are source owned.
13. Every admitted pair is evaluated by C50.
14. No representative value is reused for another mode.
15. Blocking and duplicate pair counts are zero.
16. Every source component has homogeneous units.
17. The component sum reproduces direct C50 evaluation.
18. The complete colorless matrix has mass-squared units.
19. Symbolic-\(L\) behavior is common or canceled.
20. Exact SU(3) normalization closes.
21. The raw color-emission tensor lies in the triplet image.
22. The triplet intertwiner has rank three.
23. \(C^\dagger C=C_F I_3\) closes.
24. No \(\bar6\) or \(15\) leakage is hidden.
25. The physical emission matrix exists at all resolutions.
26. The sparse and independent matrix-free actions agree.
27. Absorption is generated only as the adjoint.
28. The \(g_s\)-linear block is Hermitian.
29. Count-once and completeness ledgers close.
30. All frozen holdouts pass.
31. GeV/MeV covariance passes.
32. \(L\), \(P^+\), \(b_{\rm HO}\), Fourier, helicity, and triplet-phase checks pass.
33. The historical factor-of-two error is detected.
34. Resolution comparisons retain all nonnested/truncation remainders.
35. Runtime bundles contain actual sparse matrices and independent action metadata.
36. End-to-end reconstruction passes.
37. At least 224 focused live mutations are detected.
38. No free, instantaneous, constrained, boundary, or zero-mode matrix is claimed complete.
39. No complete local-HQCD status is issued.
40. No JMY Wilson or bilocal TMD matrix is created.
41. No physical counterterm coefficient is solved.
42. No one-loop coefficient or matching kernel is created.
43. No proton TMD or ART25 bridge is created.
44. No fit, inference, process, or production route is created.
45. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
46. `MSHT20_REP/` remains untouched and outside Git.
47. The working tree is clean except for the pre-existing untracked directory.
48. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken exhaustive evaluation, raw-tuple independence, dimensional homogeneity, color-triplet closure, or matrix-free independence to open the gate.

---

# 26. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C50 inputs consumed;
- input-fidelity classifications;
- raw-tuple independence and poisoning-test result;
- physical q and qg dimensions by block;
- Cartesian pair counts and selection-rule partitions;
- C50 evaluator call, exact-zero, nonzero, duplicate, missing, and blocking counts;
- component-matrix shapes, nnz, units, and symbolic factors;
- complete colorless matrix shapes, nnz, norms, and validation residuals;
- color-intertwiner matrix, rank, \(C_F\), covariance, and leakage residuals;
- physical emission-matrix shapes, nnz, norms, and triplet residuals;
- matrix-free residuals;
- absorption-adjoint and linear-block Hermiticity residuals;
- count-once and completeness results;
- holdout results;
- unit, \(L\), \(P^+\), \(b_{\rm HO}\), Fourier, helicity, triplet-phase, and factor-of-two checks;
- physical-resolution comparison residuals and separated remainders;
- historical C47 tuple diagnostic classifications;
- runtime-bundle hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no remaining local-QCD matrices, JMY Wilson/bilocal matrix, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a partial basis-pair sample, a matrix using C47 tuple values, a component mixture with inconsistent units, a color projection with hidden leakage, or an adjoint independently retuned from emission as the exhaustive source-derived physical canonical vertex.
