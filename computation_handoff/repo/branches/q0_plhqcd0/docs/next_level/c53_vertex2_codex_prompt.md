# C53/VERTEX2 Codex Work Package

## Title

**Exact SU(3)/triplet physical canonical vertex: source-derived color intertwiner, physical sparse emission matrix, independent matrix-free action, generated adjoint, count-once closure, and regulator-resolution comparison**

## Authoritative baseline

Start from the clean local C52/VDIM2 completion commit:

```text
949af3ad83ea4a384c9142784251dfd06254b5fd
```

Its immediate scientific parent is:

```text
d074e45e68f04994a4fc8b7979b33d0a99fc0c42
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor d074e45e68f04994a4fc8b7979b33d0a99fc0c42 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY

C51_VERTEX_DIMENSIONAL_ASSEMBLY_INCOMPLETE

C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY
```

and the exact C52 scientific result:

```text
authoritative additive source component:
    one C43 canonical b-dagger a-dagger b covariant bilinear

C50 labels "mass" and "transverse":
    inseparable spinor subterms;
    not independent additive operator components

C52 executable content:
    immutable SymPy coefficient;
    direct C45/C47 physical-basis primitive;
    component-wise P-minus to M-squared conversion;
    exhaustive color-stripped primitive matrices;
    independent direct color-stripped matrix-free action

color-stripped primitive matrices:
    K = 9/2:   shape 448 x 2,   nnz 104
    K = 11/2:  shape 900 x 2,   nnz 170
    K = 13/2:  shape 1584 x 2,  nnz 252

C50 holdout recomposition:
    maximum P-minus residual 1.11e-16
    maximum M-squared residual 8.89e-16

historical C47 canonical tuples:
    static and runtime poisoning independence passed

physical color insertion:
    not yet performed
```

Verify every identity from the committed C52 records rather than relying on this prompt.

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
    C47 CM-clean qg total-color-triplet module

canonical operator convention:
    M^2 = 2 P^+ P^- - P_perp^2
    physical coupling g_s remains factored
    L remains symbolic according to C50/C52
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All C47 raw canonical tuple values and attempted historical component metadata remain immutable diagnostic-only objects and are forbidden as physical numerical inputs.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C53 consumes the complete C52 color-stripped symbolic vertex family and inserts the exact QCD color structure.

C53 must create:

```text
the raw fundamental-to-product-color emission map
    E: 3 -> 3 tensor 8;

a proof that the canonical emission image equals the retained
total-color-triplet subspace;

the exact reduced 3 x 3 color intertwiner in the frozen C45/C47
triplet basis;

the complete coupling-factored physical q -> qg emission matrix
at every physical resolution;

an independent physical matrix-free emission action that consumes
the C52 direct color-stripped action, not the stored C53 matrix;

the qg -> q absorption matrix generated only as the Hermitian adjoint;

the Hermitian g_s-linear two-sector block operator;

entry ancestry, count-once, exact-zero, unit, phase, holdout,
raw-tuple-independence, and physical-resolution comparison records.
```

The physical canonical interaction is:

\[
V^{(M^2)}_{qg\leftarrow q}
=
g_s\,\widehat V^{(M^2)}_{qg\leftarrow q}.
\]

Do not choose, fit, or infer a physical value of \(g_s\) or \(\alpha_s\).

The strongest allowed status is:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

When that gate passes, the exact next package is:

> **C54/HQCD2 — assemble the remaining source-derived local-QCD operator substrate: free, instantaneous, constrained, boundary/zero-mode, and local-counterterm matrices, followed by the projected action identity**

---

# 2. Scientific boundary

C53 is:

```text
canonical q <-> qg vertex specific;
exact-SU(3) specific;
open-color matching-module specific;
total-color-triplet specific;
source-derived through C43/C45/C47/C50/C52;
coupling factored;
sparse and matrix free;
deterministic;
validation only.
```

C53 is not:

```text
a new decomposition of the covariant spinor bilinear;
a fit or normalization adjustment;
a physical coupling selection;
a free-Hamiltonian package;
an instantaneous/constrained-operator package;
a dressed-quark eigenproblem;
a JMY Wilson-line package;
a bilocal TMD package;
a one-loop calculation;
a proton or ART25 calculation.
```

Do not reopen the C52 component decision. The authoritative additive canonical operator contains one inseparable covariant bilinear.

---

# 3. Nonnegotiable authority chain

Every nonzero physical matrix entry must descend through:

```text
locked primary-source canonical QCD interaction
    -> C43 project-convention b-dagger a-dagger b operator
    -> C45 normalized modes and exact SU(3) conventions
    -> C47 CM-clean physical q/qg bases and 24 x 3 triplet isometry
    -> C50 finite-cell P-minus kernel and M-squared conversion
    -> C52 executable SymPy coefficient and color-stripped primitive
    -> exact C53 SU(3) emission tensor
    -> exact C53 triplet intertwiner
    -> C53 physical sparse matrix entry.
```

Every physical entry must retain or be traceable to:

```text
incoming physical q basis ID;
outgoing physical qg basis ID;
color-stripped primitive row and column;
C52 symbolic-expression hash;
C52 primitive-matrix hash;
input fundamental color;
output triplet-color label;
raw SU(3) tensor ancestry;
triplet-isometry ancestry;
coupling power;
units and symbolic signature;
basis-order hash;
matrix-shard hash.
```

The following are forbidden as physical entry authorities:

```text
a C47 raw canonical tuple value;
C47 historical component metadata;
a C40 method-oracle coefficient;
a color-singlet hadron-model matrix;
a fitted color normalization;
a projection that silently discards nontriplet leakage;
an absorption value independently adjusted from emission.
```

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json

docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_qg_triplet_validation.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_qg_triplet_basis_manifest.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_cm_factorization_report.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c50_convention_map.json
docs/next_level/c50_pminus_to_m2_derivation.json
docs/next_level/c50_arbitrary_mode_vertex_evaluator.json

docs/next_level/c51_input_fidelity_audit.json
docs/next_level/c51_raw_tuple_independence_report.json
docs/next_level/c51_missing_calculation_specification.md

docs/next_level/c52_implementation_report.md
docs/next_level/c52_derivation_authority_manifest.json
docs/next_level/c52_component_vocabulary.json
docs/next_level/c52_symbol_registry.json
docs/next_level/c52_symbolic_expression_contract.json
docs/next_level/c52_component_factorization.json
docs/next_level/c52_component_pminus_to_m2_map.json
docs/next_level/c52_component_evaluator_api.json
docs/next_level/c52_component_domain_ledger.json
docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_colorless_symbolic_vertex.json
docs/next_level/c52_colorless_component_validation.json
docs/next_level/c52_colorless_matrix_free_report.json
docs/next_level/c52_raw_tuple_independence_report.json
docs/next_level/c52_component_unit_covariance_report.json
docs/next_level/c52_c53_vertex_assembly_contract.json
docs/next_level/c52_numerical_object_inventory.json
docs/next_level/c52_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c53_derivation_authority_manifest.json
docs/next_level/c53_input_fidelity_audit.json
```

---

# 5. Freeze basis, symbolic, and phase identities

Before constructing a color tensor, freeze for every resolution:

```text
K, Nmax, bHO;
color-stripped q basis ordering;
color-stripped qg kinematic basis ordering;
physical q basis ordering after fundamental color is attached;
physical qg basis ordering after triplet color is attached;
C52 primitive matrix and expression hashes;
open-color matching-module semantics;
fundamental generator convention;
adjoint generator convention;
24 x 3 triplet-isometry phase;
zero-mode and global-Gauss-law treatment;
M-squared units;
symbolic L, P^+, bHO, and mass signatures;
physical comparison maps.
```

The C52 color-stripped shapes imply the expected physical dimensions:

```text
K = 9/2:
    expected 1344 x 6

K = 11/2:
    expected 2700 x 6

K = 13/2:
    expected 4752 x 6
```

These are inferred by attaching a three-dimensional input fundamental color and a three-dimensional output triplet color. Verify them from the committed basis manifests and C52/C53 contract. Do not hard-code them when the exact repository ordering differs.

Create:

```text
docs/next_level/c53_physical_resolution_manifest.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_symbolic_parameter_contract.json
```

---

# 6. Dependency and raw-tuple isolation

Retain and strengthen the C51/C52 guards.

The C53 construction may consume:

```text
C47 physical basis identities;
C47 triplet isometry;
C47 comparison maps;
C52 primitive matrices;
C52 executable symbolic coefficient;
C52 direct color-stripped matrix-free action.
```

It may not consume:

```text
C47 raw canonical tuple values;
C47 attempted mass/transverse metadata;
C50 combined values as primitive matrix entries;
C40 numerical coefficients.
```

Implement:

```text
a static dependency/import guard;

a runtime poisoning test replacing every C47 raw canonical tuple value
and component metadata field with NaN/sentinels;

a C50-combined-value poisoning test proving that the C53 sparse assembly
is driven by the C52 primitive and symbolic expression, while C50 remains
a validation holdout only.
```

The physical vertex and its hashes must remain unchanged under these poisonings.

Create:

```text
docs/next_level/c53_dependency_isolation_report.json
docs/next_level/c53_raw_tuple_poisoning_report.json
```

---

# 7. Exact SU(3) conventions

Use the frozen project convention:

\[
T^a=\frac{\lambda^a}{2},
\qquad
\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab},
\qquad
C_F=\frac43.
\]

Construct the adjoint generators using the exact project sign convention:

\[
(F^b)_{ac}
=
-i f^{bac}
\]

or the exact equivalent stored in the project.

Machine-check:

```text
Hermiticity of every T^a;
tracelessness;
commutator and anticommutator identities;
f and d tensor identities;
fundamental quadratic Casimir;
adjoint generator algebra;
basis ordering and phase.
```

Create:

```text
docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_su3_validation.json
```

---

# 8. Raw canonical color-emission map

Construct the unprojected color map:

\[
E:
\mathbb C^3
\longrightarrow
\mathbb C^3\otimes\mathbb C^8,
\]

with entries:

\[
E_{(c',a),c}
=
(T^a)_{c'c}.
\]

The product-color ordering \((c',a)\) must be explicit and frozen.

Required checks:

\[
E^\dagger E=C_F I_3.
\]

Construct the total final-state generators:

\[
G_{\rm tot}^b
=
T^b\otimes I_8
+
I_3\otimes F^b.
\]

Verify the intertwining identity in the exact stored convention:

\[
G_{\rm tot}^b E
=
E T^b.
\]

Report:

```text
shape;
rank;
singular values;
norm;
Casimir residual;
intertwining residual;
basis-order identity.
```

Create:

```text
docs/next_level/c53_raw_color_emission_map.json
docs/next_level/c53_raw_color_emission_validation.json
```

---

# 9. Prove equality of the emission image and retained triplet

Let:

\[
U_3:
\mathbb C^3
\longrightarrow
\mathbb C^{24}
\]

be the frozen C45/C47 \(24\times3\) triplet isometry.

Define:

\[
P_3^{(U)}
=
U_3U_3^\dagger.
\]

Independently derive the canonical-emission projector:

\[
P_3^{(E)}
=
\frac{1}{C_F}EE^\dagger.
\]

Require:

\[
P_3^{(U)}=P_3^{(E)}
\]

within declared numerical tolerance.

Also require:

```text
Hermiticity and idempotence of both projectors;
rank three;
C2 = 4/3 on the image;
orthogonality to the anti-sextet and 15;
zero canonical-emission leakage:
    (I_24 - P3) E = 0.
```

Do not project away a nonzero leakage remainder. Any unexplained mismatch is blocking.

Create:

```text
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_leakage_report.json
```

---

# 10. Reduced triplet color intertwiner

Construct:

\[
C
=
U_3^\dagger E.
\]

This is a \(3\times3\) map from the incoming fundamental-color basis to the retained outgoing triplet basis.

Do not assume \(C\) is diagonal. The frozen triplet basis may differ from the canonical-emission basis by a unitary phase/basis rotation.

Define:

\[
W
=
\frac{1}{\sqrt{C_F}}C.
\]

Require:

\[
W^\dagger W=I_3,
\qquad
WW^\dagger=I_3,
\]

equivalently:

\[
C^\dagger C=C_FI_3,
\qquad
CC^\dagger=C_FI_3.
\]

Verify the reduced generator covariance:

\[
(U_3^\dagger G_{\rm tot}^b U_3)C
=
CT^b.
\]

Required outputs:

```text
C entries;
rank;
singular values;
determinant phase;
unitary W;
Casimir residual;
left/right unitarity residuals;
generator-covariance residual;
phase-convention identity.
```

Create:

```text
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_color_intertwiner_validation.json
```

---

# 11. Basis-rotation covariance

Choose deterministic nontrivial unitary rotations \(R\) of the retained triplet basis as validation-only holdouts.

Under:

\[
U_3\to U_3R,
\]

the reduced intertwiner must transform as:

\[
C\to R^\dagger C.
\]

The physical emission operator represented in the rotated output basis must transform covariantly, while basis-independent norms and the Hermitian two-sector spectrum at diagnostic coupling remain unchanged.

Do not replace the authoritative frozen triplet basis.

Create:

```text
docs/next_level/c53_triplet_basis_rotation_report.json
```

---

# 12. Two independent color-assembly routes

Construct the physical color insertion through two independent routes.

## 12.1 Reduced-intertwiner route

Combine the C52 color-stripped primitive matrix \(I_{\rm kin}\) with \(C\), respecting the exact basis ordering.

When the ordering factorizes, the result is permutation-equivalent to:

\[
I_{\rm kin}\otimes C.
\]

Do not assume a raw Kronecker order without proving the permutation map.

## 12.2 Full-product-then-project route

First construct the raw product-color map:

\[
I_{\rm kin}\otimes E
\]

in the full \(3\otimes8\) output color space.

Then project with:

\[
I_{\rm kin,out}\otimes U_3^\dagger.
\]

After the exact basis permutations, require equality with the reduced-intertwiner route.

## 12.3 Explicit entry route

For frozen entries, independently evaluate:

\[
V_{(\beta,\rho),(\alpha,c)}
=
I_{\beta\alpha}
\sum_{c',a}
(U_3)^*_{(c',a),\rho}
(T^a)_{c'c}.
\]

Create:

```text
docs/next_level/c53_color_assembly_routes.json
docs/next_level/c53_color_assembly_equivalence.json
```

---

# 13. Assemble the physical symbolic emission family

Consume the authoritative C52 family:

\[
\widehat V_{\rm kin}^{(M^2)}
=
S_{\rm can}^{(M^2)}
\widehat I_{\rm can},
\]

or the exact equivalent stored by C52.

Construct the physical family:

\[
\widehat V_{qg\leftarrow q}^{(M^2)}
=
S_{\rm can}^{(M^2)}
\widehat I_{\rm phys},
\]

where \(\widehat I_{\rm phys}\) contains the exact color intertwiner.

Keep separate:

```text
the physical primitive sparse matrix;
the executable SymPy coefficient;
diagnostic evaluated matrices at frozen nonphysical test substitutions;
the physical coupling factor g_s.
```

Do not freeze an unfixed mass, \(L\), \(P^+\), \(b_{\rm HO}\), or physical \(g_s\) into the authoritative primitive.

Required checks:

```text
physical shape;
nnz;
basis order;
uniform M-squared units after coefficient application;
common symbolic signature;
triplet-image identity;
source-expression ancestry;
nonzero action on normalized physical q vectors.
```

Create:

```text
docs/next_level/c53_physical_vertex_primitive_matrices.json
docs/next_level/c53_physical_symbolic_vertex.json
docs/next_level/c53_physical_emission_validation.json
```

---

# 14. Entry ancestry and count-once ledger

For every nonzero physical primitive entry record:

```text
physical row and column;
qg kinematic row;
q kinematic column;
output triplet label;
input fundamental-color label;
C52 primitive entry ancestry;
C52 expression hash;
color-intertwiner entry;
source/operator ID;
basis-order identity.
```

Report for every resolution:

```text
color-stripped primitive nnz;
color-intertwiner nnz;
candidate tensor-product entries;
physical nonzero entries;
exact zeros from the color intertwiner;
duplicate entries;
missing ancestry entries;
blocking entries.
```

Multiple color contributions inside the definition of one intertwiner entry are not duplicate physical matrix entries; retain their internal sum ancestry.

A positive gate requires:

```text
duplicate physical entry count = 0;
missing ancestry count = 0;
blocking count = 0.
```

Create:

```text
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_count_once_report.json
```

---

# 15. Independent physical matrix-free emission action

Implement:

```python
apply_physical_canonical_emission(
    vector_q,
    resolution,
    symbolic_parameters,
)
```

The independent route must:

```text
reshape the input according to the frozen q kinematic/color basis;
apply the C52 direct color-stripped matrix-free primitive action;
apply the reduced color intertwiner or the full-product color map
followed by U3-dagger;
apply the executable C52 symbolic coefficient;
return the physical qg triplet vector.
```

It must not:

```text
multiply by the stored C53 sparse physical matrix;
load the C53 physical entry table as numerical authority;
consume a C47 raw tuple value;
consume a C40 matrix.
```

Implement both reduced-color and full-product-color matrix-free routes and compare them.

Compare sparse and matrix-free actions on:

```text
every physical q basis vector;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions;
multiple diagnostic symbolic substitutions.
```

Create:

```text
docs/next_level/c53_physical_matrix_free_report.json
```

---

# 16. Generate absorption only as the adjoint

Define:

\[
\widehat V_{q\leftarrow qg}^{(M^2)}
=
\left(
\widehat V_{qg\leftarrow q}^{(M^2)}
\right)^\dagger.
\]

Do not independently evaluate, fit, normalize, or phase-adjust absorption.

Construct the coupling-linear two-sector block:

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

Keep \(g_s\) factored outside this coefficient block.

Required checks:

```text
adjoint residual;
block Hermiticity;
basis-order compatibility;
sparse versus matrix-free action in both directions;
nonzero forward and reverse action;
triplet-phase covariance;
diagnostic polynomial action at nonphysical test coupling.
```

Do not diagonalize the block as a physical dressed-quark state.

Create:

```text
docs/next_level/c53_vertex_adjoint_report.json
docs/next_level/c53_linear_block_operator_validation.json
```

---

# 17. Frozen holdouts

Freeze before final assembly:

```text
at least four nonzero kinematic primitive entries per resolution;
at least one zero primitive entry;
at least one nonzero off-diagonal color-intertwiner entry when present;
every input fundamental color;
every output triplet color;
both quark helicities;
both gluon helicities represented by the C52 basis;
smallest and largest allowed x_g;
nontrivial intrinsic OAM;
one triplet-basis phase holdout;
one full-product-versus-reduced-color holdout;
one symbolic-parameter holdout;
one GeV/MeV holdout.
```

Evaluate every holdout through:

```text
explicit entry sum;
reduced-intertwiner assembly;
full-product-then-project assembly;
physical matrix-free action.
```

No failed holdout may be moved into construction after inspection.

Create:

```text
docs/next_level/c53_holdout_plan.json
docs/next_level/c53_holdout_validation.json
```

---

# 18. Unit, symbolic, and convention covariance

Re-execute C52’s checks after color insertion.

## 18.1 GeV/MeV conversion

Color factors are dimensionless. The physical matrix must inherit the exact mass-squared scaling of the C52 family.

## 18.2 Symbolic \(L\), \(P^+\), \(b_{\rm HO}\), and mass

Color insertion must not alter the symbolic signature or create an entry-dependent factor.

## 18.3 Fourier and helicity phase

The physical operator must reproduce the C52 phase behavior.

## 18.4 Triplet phase

A frozen triplet-basis phase change must transform the output basis covariantly.

## 18.5 Historical factor-of-two negative control

The C50/C52 omitted or duplicated factor-of-two mutation must still fail after color insertion.

## 18.6 SU(3) normalization negative controls

The following must fail:

```text
T^a = lambda^a;
wrong adjoint-generator sign;
C_F = 1;
singlet projection;
full-product output mislabeled as triplet;
silent anti-sextet or 15 removal.
```

Create:

```text
docs/next_level/c53_unit_color_convention_report.json
```

---

# 19. Physical-resolution comparison

Use the C47 physical comparison maps and the C52 colorless comparison contract.

Evaluate:

\[
R_{qg}^{\rm phys}
\widehat V_{r'}^{\rm phys}
P_q^{\rm phys}
\quad\text{versus}\quad
\widehat V_r^{\rm phys}.
\]

Separate:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
kinematic primitive remainder;
color-triplet basis remainder;
symbolic coefficient/normalization remainder;
numerical error.
```

The exact color intertwiner should introduce no physical regulator dependence. Any color remainder must be explained by basis representation/phase and close under the exact comparison map.

Do not tune the vertex or color normalization to reduce the comparison residual.

Create:

```text
docs/next_level/c53_vertex_comparison_report.json
docs/next_level/c53_vertex_remainder_ledger.json
```

---

# 20. Historical C47 and C40 comparisons

Preserve all historical classifications.

The C53 result may be compared diagnostically with:

```text
C47 raw canonical tuples;
C40 toy canonical matrix.
```

Allowed conclusions include:

```text
historical diagnostic agrees after explicit refactorization;
historical diagnostic differs by a known omitted factor;
historical diagnostic remains ambiguous;
method-oracle sparsity test remains reusable.
```

No historical object becomes source authority through numerical agreement.

Create:

```text
docs/next_level/c53_historical_oracle_comparison.json
```

---

# 21. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
raw 24 x 3 emission map E;
triplet projector from U3;
triplet projector from E;
reduced 3 x 3 color intertwiner C;
unitary phase map W;
physical primitive sparse matrix;
executable symbolic coefficient record;
diagnostic evaluated physical matrices;
generated absorption adjoint;
linear block operator shards;
physical matrix-free metadata;
entry-ancestry ledger;
holdout and comparison records.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c53_vertex2/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
symbolic signature;
coupling power;
basis-order hash;
expression hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c53_numerical_object_inventory.json
```

All symbolic expressions and arrays must regenerate byte-for-byte.

---

# 22. End-to-end source-to-physical-vertex test

Implement an end-to-end test that begins with the C43/C45/C47/C50/C52 contracts—not with a prebuilt C53 matrix.

It must:

```text
load the physical bases and C52 primitive;
regenerate exact SU(3) generators;
construct the raw emission map E;
prove the emission image equals the frozen triplet;
construct the reduced color intertwiner;
assemble the physical primitive by two routes;
apply the executable symbolic coefficient;
generate absorption as the adjoint;
compare sparse and independent matrix-free actions;
run count-once, holdout, unit, phase, poisoning,
and comparison tests;
reproduce all hashes.
```

It must fail when:

```text
a C47 raw tuple value or component metadata enters;
a C40 coefficient enters;
the C52 primitive hash changes;
the C52 symbolic coefficient is replaced by text;
a Gell-Mann generator changes;
the adjoint-generator sign changes;
the triplet isometry changes without the covariance transform;
a nontriplet remainder is silently projected away;
a singlet or full-product color basis is substituted;
the reduced and full-product assembly routes disagree;
absorption is independently altered;
the physical matrix-free route multiplies by the stored matrix;
the historical factor-of-two error is reintroduced;
a runtime hash changes.
```

---

# 23. Focused mutation tests

Create at least **224 focused live mutations** of actual color tensors, basis maps, symbolic records, physical entries, or actions.

Include mutations of:

```text
fundamental generator;
adjoint generator;
f-tensor sign;
product-color ordering;
raw emission tensor;
triplet projector;
triplet isometry;
intertwiner rank;
intertwiner phase;
Casimir normalization;
anti-sextet leakage;
15-dimensional-irrep leakage;
C52 primitive entry;
C52 expression hash;
physical basis ordering;
physical matrix entry;
entry ancestry;
matrix-free color accumulation;
adjoint;
linear block;
unit conversion;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, algebra, color-covariance, leakage, count-once, adjoint, matrix-free, unit, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 24. Readiness gate

Issue:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

only when:

```text
the full C52 baseline reproduces;
all dependency and poisoning guards pass;
the exact SU(3) conventions close;
the raw emission map E closes;
E-dagger E = C_F I;
the total-generator intertwining identity closes;
the emission image equals the frozen triplet subspace;
nontriplet leakage is zero;
the reduced color intertwiner has rank three;
C-dagger C = C_F I and C C-dagger = C_F I;
reduced-color and full-product assembly routes agree;
the physical primitive matrices exist at all resolutions;
the executable symbolic family preserves C52 dimensions and units;
entry ancestry and count-once ledgers close;
the independent physical matrix-free routes agree with the sparse matrices;
absorption is generated only as the adjoint;
the g_s-linear block is Hermitian;
all frozen holdouts pass;
unit, symbolic, phase, and color convention tests pass;
physical-resolution comparisons execute;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-physical-vertex test passes.
```

Do not issue:

```text
C53_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C53_FREE_HAMILTONIAN_VALIDATED;
C53_INSTANTANEOUS_OPERATOR_VALIDATED;
C53_PROJECTED_ACTION_IDENTITY_VALIDATED;
C53_JMY_WILSON_MATRIX_VALIDATED;
C53_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C53_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 25. Exact no-go branches

## A. SU(3) convention or raw emission map fails

```text
C53_SU3_EMISSION_MAP_INCOMPLETE
```

Next:

> **C54/COLORALG — exact fundamental/adjoint convention and canonical emission-map completion**

## B. The canonical emission image does not equal the retained triplet

```text
C53_COLOR_TRIPLET_IMAGE_MISMATCH
```

Next:

> **C54/COLORV3 — reconcile the C45/C47 triplet basis with the source-derived emission intertwiner**

## C. Reduced and full-product color assembly disagree

```text
C53_PHYSICAL_VERTEX_ASSEMBLY_INCOMPLETE
```

Next:

> **C54/VASM1 — physical basis ordering, color insertion, and entry-ancestry completion**

## D. Independent matrix-free action fails

```text
C53_PHYSICAL_MATRIX_FREE_CLOSURE_FAILED
```

Next:

> **C54/VACT2 — independent physical sparse/matrix-free canonical-action completion**

## E. Adjoint or linear-block closure fails

```text
C53_VERTEX_ADJOINT_CLOSURE_FAILED
```

Next:

> **C54/ADJ1 — phase, basis-order, and generated-adjoint completion**

## F. Physical-resolution comparison remains incomplete

```text
C53_VERTEX_COMPARISON_INCOMPLETE
```

Next:

> **C54/R1F — physical canonical-vertex comparison-map and remainder completion**

## G. Physical canonical vertex closes

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY
```

Next:

> **C54/HQCD2 — assemble the remaining local-QCD operator substrate and projected action identity**

---

# 26. Required deliverables

Create at least:

```text
docs/next_level/c53_implementation_report.md
docs/next_level/c53_api.md
docs/next_level/c53_derivation_authority_manifest.json
docs/next_level/c53_input_fidelity_audit.json

docs/next_level/c53_physical_resolution_manifest.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_symbolic_parameter_contract.json
docs/next_level/c53_dependency_isolation_report.json
docs/next_level/c53_raw_tuple_poisoning_report.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_su3_validation.json
docs/next_level/c53_raw_color_emission_map.json
docs/next_level/c53_raw_color_emission_validation.json

docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_leakage_report.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_color_intertwiner_validation.json
docs/next_level/c53_triplet_basis_rotation_report.json

docs/next_level/c53_color_assembly_routes.json
docs/next_level/c53_color_assembly_equivalence.json

docs/next_level/c53_physical_vertex_primitive_matrices.json
docs/next_level/c53_physical_symbolic_vertex.json
docs/next_level/c53_physical_emission_validation.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_count_once_report.json
docs/next_level/c53_physical_matrix_free_report.json

docs/next_level/c53_vertex_adjoint_report.json
docs/next_level/c53_linear_block_operator_validation.json
docs/next_level/c53_holdout_plan.json
docs/next_level/c53_holdout_validation.json

docs/next_level/c53_unit_color_convention_report.json
docs/next_level/c53_vertex_comparison_report.json
docs/next_level/c53_vertex_remainder_ledger.json
docs/next_level/c53_historical_oracle_comparison.json

docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json
docs/next_level/c53_source_sufficiency_decision.json
docs/next_level/c53_no_go_decision_tree.json
docs/next_level/c53_missing_calculation_specification.md
docs/next_level/c53_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/vertex3/
```

or the repository-equivalent package.

Add focused tests for:

```text
SU(3) algebra;
raw emission map;
triplet-image equivalence;
color intertwiner;
basis-rotation covariance;
two-route physical assembly;
entry ancestry and count once;
physical sparse/matrix-free action;
generated adjoint and linear-block Hermiticity;
poisoning isolation;
unit and phase covariance;
resolution comparison;
end-to-end source-to-physical-vertex reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON, symbolic expressions, and runtime arrays must reproduce byte-for-byte.

---

# 27. Acceptance criteria

C53 is complete only when:

1. The full C52 baseline reproduces.
2. The C51 no-go remains explicit.
3. The C52 single-component source decision remains unchanged.
4. The C43 action, C45 modes/color, and C47 basis remain unchanged.
5. C40 remains method-oracle only.
6. C47 raw tuple values and metadata remain diagnostic-only.
7. C50 combined values remain holdouts, not primitive inputs.
8. Static and runtime poisoning guards pass.
9. No arbitrary numerical \(L\) is introduced.
10. No physical coupling is chosen.
11. The exact fundamental generators close.
12. The exact adjoint generators close.
13. The raw emission map has rank three.
14. \(E^\dagger E=C_FI_3\) closes.
15. The total-generator intertwining identity closes.
16. The emission projector equals the frozen triplet projector.
17. No \(\bar6\) or \(15\) leakage is hidden.
18. The reduced color intertwiner has rank three.
19. \(C^\dagger C=C_FI_3\) closes.
20. \(CC^\dagger=C_FI_3\) closes.
21. Triplet-basis rotation covariance closes.
22. Reduced and full-product color-assembly routes agree.
23. Explicit-entry holdouts agree.
24. Physical primitive matrices exist at all resolutions.
25. Their shapes and basis orders match the physical manifests.
26. Their nnz counts are derived rather than assumed.
27. Every physical entry has complete ancestry.
28. Duplicate, missing, and blocking counts are zero.
29. The executable symbolic coefficient remains separate from the primitive.
30. Physical outputs retain uniform mass-squared units.
31. Color insertion changes no dimensional or regulator signature.
32. Independent reduced and full-product matrix-free actions agree.
33. Sparse and matrix-free physical actions agree.
34. Absorption is generated only as the adjoint.
35. The \(g_s\)-linear block is Hermitian.
36. No physical dressed-state diagonalization is performed.
37. All frozen holdouts pass.
38. GeV/MeV covariance passes.
39. \(L\), \(P^+\), \(b_{\rm HO}\), mass, Fourier, helicity, and triplet-phase checks pass.
40. The historical factor-of-two negative control fails as required.
41. Wrong SU(3), singlet, full-product, and leakage controls fail.
42. Physical-resolution comparisons retain all remainders.
43. Runtime bundles contain actual sparse matrices and independent action metadata.
44. End-to-end reconstruction passes.
45. At least 224 focused live mutations are detected.
46. No free, instantaneous, constrained, boundary, or zero-mode matrix is claimed complete.
47. No complete local-HQCD status is issued.
48. No JMY Wilson or bilocal TMD matrix is created.
49. No physical counterterm coefficient is solved.
50. No one-loop coefficient or matching kernel is created.
51. No proton TMD or ART25 bridge is created.
52. No fit, inference, process, or production route is created.
53. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
54. `MSHT20_REP/` remains untouched and outside Git.
55. The working tree is clean except for the pre-existing untracked directory.
56. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken the emission-image proof, triplet leakage test, exact SU(3) normalization, physical matrix-free independence, or generated-adjoint requirement to open the gate.

---

# 28. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C50/C52 inputs consumed;
- dependency and poisoning results;
- physical q and qg dimensions and expected/actual matrix shapes;
- fundamental and adjoint SU(3) residuals;
- raw emission-map shape, rank, singular values, norm, Casimir, and intertwining residuals;
- frozen-triplet and emission-projector residuals;
- \(\bar6\)/15 leakage residuals;
- reduced color-intertwiner entries, rank, singular values, phase, \(C_F\), and covariance residuals;
- basis-rotation covariance residuals;
- reduced/full-product/explicit-entry assembly residuals;
- physical primitive-matrix shapes, nnz, norms, units, and symbolic signatures;
- entry-ancestry, duplicate, missing, and blocking counts;
- physical sparse/matrix-free residuals for both color routes;
- absorption-adjoint and linear-block Hermiticity residuals;
- holdout results;
- unit, symbolic-\(L\), \(P^+\), \(b_{\rm HO}\), mass, Fourier, helicity, triplet-phase, factor-of-two, and wrong-color controls;
- physical-resolution comparison residuals and separated remainders;
- historical-oracle comparison classifications;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no remaining local-QCD matrices, JMY Wilson/bilocal matrix, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a colorless symbolic family, a projected color map with unexplained leakage, a physical matrix assembled from C47 raw tuples, a matrix-free route that multiplies by the stored sparse matrix, or an independently retuned absorption matrix as the exact physical canonical vertex.
