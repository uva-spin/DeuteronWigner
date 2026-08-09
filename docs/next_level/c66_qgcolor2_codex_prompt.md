# C66/QGCOLOR2 Codex Work Package

## Title

**Exact SU(3) triplet-isometry artifact completion: source-derived \(3\otimes8\supset3\) intertwiner, frozen \(24\times3\) basis map, normalization and projector equivalence, certified runtime bundle, and read-only import closure**

## Authoritative baseline

Start from the clean local C65/QGEMBED3 fail-closed completion commit:

```text
fd459d8114224de78ba562f904f39ba7d42b6ddc
```

Its immediate positive artifact ancestor is:

```text
C64/QGTM2
6f74663f3a70e853940665c30b1561766b6b75a3
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 6f74663f3a70e853940665c30b1561766b6b75a3 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C64_SOURCE_DERIVED_EXACT_TM_ARTIFACTS_READY

C65_QG_TRIPLET_EMBEDDING_INCOMPLETE
```

and the exact C65 finding:

```text
C64 read-only import:
    passed;

C64 imported objects:
    733 exact TM blocks;
    171,153 coefficient-status records;
    67,920 residue certificates;

required color object:
    frozen C53-convention 24 x 3 triplet isometry U3;

C53 artifact status:
    no C53-owned or descendant-canonical, hash-verified runtime
    artifact exists for that exact 24 x 3 isometry;

available but non-substitutable objects:
    raw_emission_E:
        24 x 3 but differently normalized;
    stored triplet projectors:
        24 x 24 and therefore image projectors, not a
        basis-resolved 24 x 3 isometry;

C65 consequence:
    no CM-ground/triplet physical qg embedding;
    no contact support;
    no descendant-impact audit.
```

Verify every statement from the committed C65 records rather than relying on this prompt.

The C53 scientific result remains intact:

```text
C53 inserted exact SU(3) into the frozen C47 triplet matching module
through two equivalent routes;

the physical canonical q <-> qg vertex is source derived;

absorption is generated only as the Hermitian adjoint;

C53 numerical vertex values are not authority for C66's color basis.
```

The fixed color representation is:

\[
3\otimes 8 = 3 \oplus \overline 6 \oplus 15,
\]

with the exact C45/C47/C53 fundamental, adjoint, product-color, and retained-triplet conventions.

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C65 correctly refused two substitutions.

First, a raw emission map \(E\in\mathbb C^{24\times3}\) is not automatically an isometry. In a common convention one expects schematically

\[
E_{(i,a),j}=(T^a)_{ij},
\]

and then

\[
E^\dagger E=C_F I_3,\qquad C_F=\frac43,
\]

so that a normalized isometry would be

\[
U_3=\frac{1}{\sqrt{C_F}}E.
\]

But C66 must not assume this formula, row ordering, generator orientation, column basis, or normalization. It must derive them from the frozen C53 convention. The exact relation may include a source-owned basis permutation, phase, transpose/conjugation adapter, or a nontrivial positive Gram normalization.

Second, a rank-three projector

\[
P_3\in\mathbb C^{24\times24}
\]

determines a three-dimensional image but does not uniquely determine an ordered, phased \(24\times3\) basis map. Arbitrary numerical eigendecomposition, SVD, QR, or Cholesky choices cannot define the frozen triplet basis.

The required object is a source-derived intertwining isometry:

\[
U_3:\mathbb C^3_{\rm triplet}
\longrightarrow
\mathbb C^3_{\rm fundamental}\otimes\mathbb C^8_{\rm adjoint},
\]

with:

\[
U_3^\dagger U_3=I_3,
\qquad
U_3U_3^\dagger=P_3,
\]

and the exact representation relation

\[
G_{\rm prod}^b\,U_3
=
U_3\,G_{\rm triplet}^b,
\]

in the frozen C53 signs, basis orders, and generator normalization.

C66 must materialize this object as a **C66-owned descendant artifact cryptographically bound to the immutable C53 convention**. Do not edit history or claim that the runtime artifact was already committed by C53.

---

# 2. Exact purpose

C66 resolves only the missing color-isometry artifact and import contract.

C66 must produce:

```text
a complete read-only fidelity audit of the C45/C47/C53 color
conventions;

the exact ordered 24-dimensional product-color basis;

the exact ordered three-dimensional retained-triplet basis;

the exact fundamental and adjoint generators;

the source-derived unnormalized canonical emission/color incidence
map;

its exact Gram matrix, rank, and normalization;

the exact source-owned 24 x 3 triplet isometry U3;

the exact 24 x 24 image projector U3 U3-dagger;

the exact intertwining and representation-equivalence proofs;

the exact relation to raw_emission_E;

the exact relation to every stored C53 24 x 24 triplet projector;

threshold-free exact support and expression records;

certified numerical arrays with error bounds;

deterministic runtime paths and hashes;

a hash-verifying read-only API;

an immutable C67/QGEMBED4 import contract;

a narrow C53 impact audit proving either that C53 remains valid or
that a later supersession is required.
```

C66 must not construct:

```text
the kinematic CM-ground qg embedding;

the full kinematic-times-color physical qg embedding;

C60 absorption/emission endpoint relations;

a direct-contact witness relation;

a contact value or matrix;

a new canonical vertex;

a self-induced-inertia contraction;

a physical counterterm coefficient;

a Wilson/TMD or matching object.
```

The strongest positive status is:

```text
C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY
```

Its exact continuation is:

> **C67/QGEMBED4 — resume the exact CM-ground and color-triplet physical \(qg\) embedding using immutable C64 and C66 artifacts**

---

# 3. Scientific boundary

C66 is:

```text
SU(3)-representation specific;
basis-order explicit;
normalization explicit;
intertwiner specific;
projector-equivalence specific;
exact-expression and support specific;
numerically certified;
content addressed;
read-only-import enabling;
validation only.
```

C66 is not:

```text
a refit of C53;

a normalization patch applied to a numerical vertex;

an arbitrary factorization of a projector;

a change of the C53 triplet convention;

a physical qg embedding;

a contact or Hamiltonian calculation.
```

The artifact must preserve the distinction among:

```text
unnormalized canonical color-emission map;

normalized triplet isometry;

triplet image projector;

physical canonical vertex;

basis adapter.
```

No two may be aliased.

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json

docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_projection_contract_matrix.json
docs/next_level/c45_numerical_object_inventory.json

docs/next_level/c47_qg_triplet_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json
docs/next_level/c47_c48_matrix_assembly_interface.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c52_component_vocabulary.json
docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_numerical_object_inventory.json
docs/next_level/c52_readiness_report.json

docs/next_level/c53_implementation_report.md
docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_count_once_report.json
docs/next_level/c53_physical_matrix_free_report.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c64_readiness_report.json
docs/next_level/c64_c65_qgembed3_import_contract.json

docs/next_level/c65_implementation_report.md
docs/next_level/c65_c64_import_report.json
docs/next_level/c65_c53_triplet_import_report.json
docs/next_level/c65_missing_calculation_specification.md
docs/next_level/c65_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Read the C53 implementation code under the repository-equivalent color/vertex package, including the exact constructors for:

```text
SU(3) generators;

adjoint generators;

product-color basis;

raw_emission_E;

triplet projector;

full-product and reduced-triplet routes.
```

Create:

```text
docs/next_level/c66_derivation_authority_manifest.json
docs/next_level/c66_input_fidelity_audit.json
```

---

# 5. Freeze source ownership and holdouts

Before constructing a matrix entry, freeze:

```text
the C53 completion commit and source-file hashes;

the exact generator normalization;

the exact fundamental basis order;

the exact adjoint basis order;

the exact product-color row order;

the exact retained-triplet column order;

the adjoint-generator sign convention;

the raw-emission index orientation;

the triplet projector hashes;

the C53 full-product/reduced-route identities;

the coupling and kinematic factorization boundary.
```

Freeze holdouts before construction:

```text
one diagonal-generator entry;

one real off-diagonal-generator entry;

one imaginary off-diagonal-generator entry;

one exact zero entry;

one row from every adjoint color;

one column from every triplet basis state;

one generator-intertwining identity per independent SU(3)
generator class;

one raw_emission_E normalization holdout per column;

one projector row and column;

one nontriplet vector in the anti-sextet complement;

one nontriplet vector in the 15 complement;

one arbitrary triplet-basis rotation;

one C53 full-product physical-vertex holdout;

one C53 reduced-triplet physical-vertex holdout.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c66_calculation_plan.json
docs/next_level/c66_holdout_plan.json
```

---

# 6. Exact SU(3) convention

Materialize exact fundamental generators:

\[
T^a,\qquad a=1,\ldots,8,
\]

in the frozen C53 convention.

Record and verify:

```text
Hermiticity;

tracelessness;

Tr(T^a T^b) normalization;

commutator sign;

anticommutator normalization;

f^{abc};

d^{abc};

quadratic Casimir C_F;

adjoint Casimir C_A;

basis order;

exact expression hashes.
```

Do not import an external Gell-Mann convention by name when its signs or order differ from C53.

Construct the adjoint generators in the exact C53 convention:

\[
(F^b)_{ac}
=
\text{the frozen signed expression in }f^{bac}.
\]

Verify their Hermiticity/anti-Hermiticity convention and commutators.

Create:

```text
docs/next_level/c66_exact_su3_generator_manifest.json
docs/next_level/c66_su3_generator_validation.json
docs/next_level/c66_structure_constant_manifest.json
```

---

# 7. Exact product-color basis

Construct the ordered raw product basis:

\[
\mathcal B_{3\otimes8}
=
\{|i\rangle_{\!3}\otimes|a\rangle_{\!8}\}.
\]

Do not assume whether the row index runs:

```text
fundamental-major;

adjoint-major;

or another frozen C53 order.
```

Each row record retains:

```text
global row index;

fundamental color ID;

adjoint color ID;

basis-order source;

C47/C53 ancestry;

row hash.
```

Construct the total product generator:

\[
G_{\rm prod}^b
=
T^b\otimes I_8
+
I_3\otimes F^b
\]

only after proving the required Kronecker permutations and sign convention.

Create:

```text
docs/next_level/c66_product_color_basis_manifest.json
docs/next_level/c66_product_generator_manifest.json
docs/next_level/c66_product_basis_validation.json
```

---

# 8. Exact retained-triplet basis

Construct the ordered abstract triplet basis:

\[
\mathcal B_{3,\rm retained}
=
\{|r\rangle,\ r=1,2,3\}.
\]

Determine whether its generator action is:

```text
the fundamental T^b;

a phase/permutation-conjugate fundamental representation;

the conjugate representation;

or another declared adapter.
```

Do not infer the column basis from a numerical eigensolver.

Construct the exact basis adapter \(A_3\) when the retained basis differs from the canonical fundamental basis:

\[
G_{\rm triplet}^b
=
A_3^\dagger T^b A_3,
\]

or the exact committed orientation.

Required checks:

```text
unitarity/isometry of A3;

basis IDs;

phase and permutation;

generator covariance;

complex conjugation;

hash stability.
```

Create:

```text
docs/next_level/c66_retained_triplet_basis_manifest.json
docs/next_level/c66_triplet_basis_adapter.json
docs/next_level/c66_triplet_basis_validation.json
```

---

# 9. Reconstruct the unnormalized canonical color map

Reconstruct the source-owned color-only map:

\[
E_{\rm src}:
\mathbb C^3_{\rm source}
\longrightarrow
\mathbb C^{24}_{3\otimes8}.
\]

Determine the exact index relation from the C53 canonical emission operator. Candidate forms include:

\[
(E_{\rm src})_{(i,a),j}
=
(T^a)_{ij},
\]

\[
(T^a)_{ji},
\qquad
(T^a)^*_{ij},
\qquad
-(T^a)^T_{ij},
\]

possibly combined with frozen basis permutations.

Do not choose among them by whichever one numerically resembles `raw_emission_E`.

For every entry retain:

```text
row and column basis IDs;

generator ID;

exact expression;

index orientation;

source-term identity;

coupling-factored status;

kinematic-factor-free status;

exact-zero reason;

expression hash.
```

Create:

```text
docs/next_level/c66_source_color_emission_map.json
docs/next_level/c66_source_color_emission_validation.json
```

---

# 10. Exact Gram matrix and rank

Compute exactly:

\[
G_E=E_{\rm src}^\dagger E_{\rm src}.
\]

Report:

```text
shape;

rank;

nullity;

eigenvalue/minimal-polynomial structure;

exact determinant;

condition number as a diagnostic;

commutation with the retained-triplet generators.
```

Allowed outcomes include:

```text
G_E = C_F I_3;

G_E = scalar times a basis metric;

G_E = positive definite non-scalar source metric;

G_E rank deficient;

Gram relation incomplete.
```

Do not replace \(G_E\) with \(C_F I\) by expectation.

Create:

```text
docs/next_level/c66_color_emission_gram.json
docs/next_level/c66_color_emission_gram_validation.json
```

A positive isometry gate requires rank three and a source-qualified positive normalization.

---

# 11. Select the normalization plan

Compile mutually exclusive plans before constructing \(U_3\).

## 11.1 `QGCOLOR2-CASIMIR-NORMALIZATION`

When the exact Gram relation is:

\[
G_E=C_F I_3,
\]

construct:

\[
U_{\rm canonical}=E_{\rm src}/\sqrt{C_F}.
\]

## 11.2 `QGCOLOR2-POLAR-NORMALIZATION`

For a source-qualified positive non-scalar Gram matrix, construct:

\[
U_{\rm canonical}
=
E_{\rm src}G_E^{-1/2}
\]

using an exact algebraic positive square root.

## 11.3 `QGCOLOR2-SOURCE-EXPLICIT-ISOMETRY`

Consume a source-explicit exact triplet-basis map independent of \(E_{\rm src}\), then prove its relation to \(E_{\rm src}\).

## 11.4 `QGCOLOR2-UNAVAILABLE`

No exact normalization and column-basis relation can be established.

Select one plan.

A numerical QR/SVD normalization is a holdout only. It cannot define the phase or column ordering.

Create:

```text
docs/next_level/c66_triplet_normalization_plan.json
docs/next_level/c66_triplet_normalization_decision.json
```

---

# 12. Construct the frozen \(24\times3\) isometry

Construct the C53-convention isometry:

\[
U_3
=
U_{\rm canonical}A_3
\]

or the exact orientation derived from the retained-triplet basis adapter.

Each entry must retain:

```text
row product-color basis ID;

column retained-triplet basis ID;

exact expression;

exact support status;

normalization ancestry;

basis-adapter ancestry;

expression hash.
```

Require:

\[
U_3^\dagger U_3=I_3
\]

exactly.

Do not repair orthonormality by numerical reorthogonalization.

Create:

```text
docs/next_level/c66_exact_triplet_isometry.json
docs/next_level/c66_triplet_isometry_validation.json
```

---

# 13. Intertwiner identity

For every adjoint label \(b\), verify exactly:

\[
G_{\rm prod}^b U_3
=
U_3 G_{\rm triplet}^b.
\]

Record:

```text
left and right expression hashes;

exact residual;

basis-permutation ancestry;

generator sign;

representation identity.
```

Also verify finite group-action covariance for declared holdout transformations when implemented:

\[
D_{3\otimes8}(g)U_3
=
U_3D_3(g).
\]

Create:

```text
docs/next_level/c66_triplet_intertwiner_contract.json
docs/next_level/c66_triplet_intertwiner_validation.json
```

This is the primary proof that the image is the retained triplet rather than an arbitrary rank-three subspace.

---

# 14. Exact image projector

Construct:

\[
P_3=U_3U_3^\dagger.
\]

Require exactly:

\[
P_3^\dagger=P_3,
\qquad
P_3^2=P_3,
\qquad
\operatorname{rank}P_3=3,
\qquad
\operatorname{Tr}P_3=3.
\]

Verify:

```text
P3 commutes with all product generators;

P3 U3 = U3;

U3-dagger P3 = U3-dagger;

the complement has dimension 21;

anti-sextet and 15 holdouts are annihilated;

triplet holdouts are preserved.
```

Create:

```text
docs/next_level/c66_exact_triplet_projector.json
docs/next_level/c66_triplet_projector_validation.json
```

---

# 15. Relation to stored C53 projectors

Inventory every C53-owned \(24\times24\) projector-like object.

For each object report:

```text
artifact ID;

basis order;

rank;

Hermiticity;

idempotence;

generator commutator;

exact or certified relation to P3;

whether it is the triplet image projector, another projector, or an
operator-dependent object.
```

Allowed relation statuses:

```text
EXACTLY_EQUAL_TO_U3_U3_DAGGER;

PERMUTATION_EQUIVALENT;

BASIS_ADAPTER_EQUIVALENT;

DISTINCT_DECLARED_PROJECTOR;

NOT_PROJECTOR;

IMPACT_UNRESOLVED_BLOCKING.
```

Do not use projector equality alone to set the columns of \(U_3\).

Create:

```text
docs/next_level/c66_c53_projector_inventory.json
docs/next_level/c66_c53_projector_equivalence_report.json
```

---

# 16. Relation to `raw_emission_E`

Load `raw_emission_E` only after \(E_{\rm src}\), \(G_E\), \(A_3\), and \(U_3\) are frozen.

Determine whether:

\[
E_{\rm raw}
=
U_3 N,
\]

for an exact source-owned normalization/column adapter \(N\), or the exact orientation.

Report:

```text
shape;

basis order;

coupling/kinematic content;

rank;

Gram matrix;

exact normalization relation;

column phase/permutation;

residual;

support difference.
```

Allowed statuses:

```text
RAW_EMISSION_EQUALS_SOURCE_MAP;

RAW_EMISSION_EQUALS_SQRT_CF_TIMES_U3;

RAW_EMISSION_EQUALS_U3_TIMES_EXACT_NORMALIZER;

RAW_EMISSION_CONTAINS_ADDITIONAL_FACTORS;

RAW_EMISSION_RELATION_INCOMPLETE.
```

C65's refusal to substitute `raw_emission_E` remains historically correct even when C66 later proves a normalization relation.

Create:

```text
docs/next_level/c66_raw_emission_relation.json
docs/next_level/c66_raw_emission_relation_validation.json
```

---

# 17. Threshold-free support and expression records

For every \(24\times3\) entry assign:

```text
ZERO_BY_EXACT_GENERATOR_STRUCTURE;

ZERO_BY_EXACT_BASIS_SELECTION;

NONZERO_EXACT_RATIONAL;

NONZERO_EXACT_RADICAL;

NONZERO_EXACT_IMAGINARY_RADICAL;

UNDECIDABLE_BLOCKING.
```

A positive gate requires:

```text
UNDECIDABLE_BLOCKING = 0.
```

Materialize:

```text
the complete status array;

a derived Boolean support mask;

canonical exact expressions for every nonzero;

exact-zero certificates;

row/column basis manifests;

per-entry ancestry.
```

Compute:

```text
row_basis_sha256;

column_basis_sha256;

expression_sha256;

status_sha256;

support_sha256;

zero_certificate_sha256;

aggregate package hash.
```

Create:

```text
docs/next_level/c66_triplet_expression_manifest.json
docs/next_level/c66_triplet_support_manifest.json
docs/next_level/c66_triplet_hash_manifest.json
```

---

# 18. Certified numerical artifact

Export certified numerical arrays for:

```text
U3;

U3-dagger;

P3;

E_src;

G_E;

A3;

all required basis permutations.
```

Because the entries are exact rational/radical/\(i\) combinations, use a rigorous directed-rounding or exact-radical enclosure plan.

For each stored value retain:

```text
exact-expression hash;

rounded complex midpoint;

absolute error bound;

working precision;

rounding convention;

basis IDs.
```

Required checks:

```text
exact value lies inside every interval;

claimed nonzero intervals exclude zero;

exact zeros remain literal zeros;

precision doubling preserves support;

U3-dagger U3 identity closes within propagated bounds;

P3 invariants close within propagated bounds;

intertwiner residuals close within propagated bounds.
```

Create:

```text
docs/next_level/c66_numerical_certification_plan.json
docs/next_level/c66_certified_triplet_export.json
docs/next_level/c66_error_bound_validation.json
docs/next_level/c66_precision_stability_report.json
```

---

# 19. Deterministic runtime bundle

Use:

```text
data/runtime/c66_qgcolor2/
```

Materialize deterministic files for:

```text
row_basis.json;

column_basis.json;

status.npy or equivalent;

support.npy or equivalent;

exact_expressions.jsonl or equivalent;

U3_real.npy;

U3_imag.npy;

U3_abs_error.npy;

P3_real.npy;

P3_imag.npy;

P3_abs_error.npy;

source_emission arrays;

basis adapters and permutations;

metadata.json.
```

Use actual repository conventions when different.

Commit an inventory containing:

```text
relative path;

schema;

shape;

dtype;

nnz;

basis hashes;

expression/status/support hashes;

array hashes;

error-bound hashes;

generator command;

source fingerprint.
```

Create:

```text
docs/next_level/c66_runtime_path_manifest.json
docs/next_level/c66_numerical_object_inventory.json
docs/next_level/c66_runtime_completeness_report.json
```

A positive gate requires zero missing, duplicate, orphaned, or unhashed artifacts.

---

# 20. Hash-verifying read-only API

Create APIs equivalent to:

```python
load_triplet_basis_manifest()

load_exact_triplet_isometry() -> ExactTripletIsometry

load_certified_triplet_isometry() -> CertifiedMatrix

load_triplet_projector() -> CertifiedMatrix

load_source_emission_relation()

embed_triplet_color_to_product(
    triplet_vector,
    precision=None,
) -> CertifiedVectorResult

project_product_color_to_triplet(
    product_vector,
    precision=None,
) -> CertifiedVectorResult
```

The loader must:

```text
verify all hashes before returning data;

return immutable arrays;

expose exact statuses separately from numerical values;

expose row/column basis orders;

expose error bounds;

call no C52/C53 physical vertex generator;

regenerate no missing artifact.
```

Create:

```text
docs/next_level/c66_api_contract.json
docs/next_level/c66_api_validation.json
```

---

# 21. Independent reconstruction

Implement two genuinely independent construction routes.

## Route A: source-emission normalization

Construct \(E_{\rm src}\), its exact Gram matrix, and the selected normalization.

## Route B: representation-nullspace/intertwiner construction

Solve the exact finite linear system:

\[
G_{\rm prod}^b U-U G_{\rm triplet}^b=0
\]

for all \(b\), impose the frozen column basis/phase convention, and normalize exactly.

Route B must not call Route A's matrix constructor.

Compare:

```text
exact U3 expressions;

support;

basis order;

projector;

intertwiner residuals;

normalization.
```

A numerical SVD nullspace is a diagnostic only unless converted into an exact certified solution through an independent exact algebra step.

Create:

```text
docs/next_level/c66_independent_isometry_reconstruction.json
docs/next_level/c66_two_route_equivalence_report.json
```

---

# 22. C53 impact audit

C66 must not reopen C53 physics, but it must prove the new artifact is compatible with C53.

Audit:

```text
the full-product color route;

the reduced-triplet color route;

the physical emission map;

the generated absorption adjoint;

basis ordering;

support ancestry;

coupling factorization;

matrix-free action.
```

Reconstruct frozen C53 color holdouts using the C66 \(U_3\) while poisoning stored C53 physical matrix values during construction.

Classify C53:

```text
UNCHANGED_EXACTLY_ARTIFACT_GAP_ONLY;

READ_ONLY_IMPORT_ADAPTER_REQUIRED_NO_OPERATOR_REBUILD;

SUPPORT_CERTIFICATE_SUPERSEDED_VALUES_VALID;

NUMERICAL_OPERATOR_REBUILD_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

A numerical-operator rebuild status blocks direct return to QGEMBED4 and requires the supersession branch.

Create:

```text
docs/next_level/c66_c53_impact_audit.json
docs/next_level/c66_c53_basis_covariance_report.json
```

---

# 23. C67/QGEMBED4 import contract

When C53 does not require numerical rebuilding, define the immutable contract by which C67 consumes:

```text
the C66 package aggregate hash;

the exact row and column basis manifests;

the exact U3 expression/status/support records;

the certified U3 and error bounds;

the exact P3 projector;

the kinematic/color ordering adapter contract;

the triplet basis adapter;

the raw_emission_E relation;

the C53 impact decision;

the hash-verifying read-only API.
```

C67 must verify every hash before combining \(U_3\) with a C64 CM-ground kinematic embedding.

C67 may not:

```text
renormalize raw_emission_E itself;

factor a 24 x 24 projector itself;

choose new column phases;

change a basis order;

regenerate C66;

or call C53 numerical vertex code to obtain U3.
```

Create:

```text
docs/next_level/c66_c67_qgembed4_import_contract.json
```

When C53 requires rebuilding, create instead:

```text
docs/next_level/c66_c67_vertex5_import_contract.json
```

---

# 24. Deterministic reconstruction

Run:

```text
two consecutive complete builds;

one clean-runtime build;

one serial build;

one declared parallel build if supported;

one restart/resume build.
```

Require byte-identical final artifacts.

A restart may reuse a runtime object only after all source, basis, expression, support, and numerical hashes pass.

Create:

```text
docs/next_level/c66_deterministic_reconstruction_report.json
docs/next_level/c66_restart_parallel_report.json
docs/next_level/c66_environment_manifest.json
```

---

# 25. Count-once and provenance

Report:

```text
expected U3 entry count = 72;

materialized status count;

exact-zero count by class;

exact-nonzero count by class;

expression count;

certified numerical count;

projector entry count;

basis record count;

runtime artifact count;

missing count;

duplicate count;

orphan count;

hash mismatch count;

unresolved impact count.
```

Do not hard-code nonzero counts.

Every \(U_3\) entry must have one ancestry path:

```text
C53 SU(3) convention
    ->
source color map or intertwiner equation
    ->
normalization
    ->
triplet basis adapter
    ->
exact U3 entry
    ->
support/expression certificate
    ->
certified numerical artifact.
```

Create:

```text
docs/next_level/c66_artifact_ancestry_ledger.json
docs/next_level/c66_count_once_report.json
```

A positive gate requires all error and unresolved counts to be zero.

---

# 26. Isolation and poisoning controls

Prove C66 construction is unchanged when:

```text
C53 physical vertex numerical values are poisoned;

raw_emission_E numerical values are poisoned after its identity is
reserved as a holdout;

stored 24 x 24 projector numerical values are poisoned after their
identities are reserved as holdouts;

all C47 raw canonical tuple values are poisoned;

all C50/C52 combined/physical values are poisoned;

all C57/C58 numerical objects are poisoned;

all C64 TM arrays are inaccessible except for inherited regression
verification;

ART25 files are inaccessible.
```

The build must fail when:

```text
a C53 generator changes;

the generator normalization changes;

the adjoint sign changes;

the product basis order changes;

the retained-triplet column order changes;

the normalizer changes;

a column phase changes without an adapter update;

an exact nonzero is pruned;

an exact zero is inferred from magnitude;

a projector factorization is substituted for source columns;

a runtime path is absent;

an array or expression hash changes;

the loader regenerates missing data.
```

Create:

```text
docs/next_level/c66_isolation_report.json
```

---

# 27. End-to-end source-to-isometry test

Implement an end-to-end test that begins from the frozen C45/C47/C53 color contracts, not from prebuilt C66 arrays.

It must:

```text
verify source fingerprints;

construct exact fundamental and adjoint generators;

construct the product basis and product generators;

construct the retained-triplet basis;

derive E_src;

compute the exact Gram matrix;

select the normalization plan;

construct U3;

verify U3-dagger U3;

verify the intertwiner identities;

construct P3;

compare all stored C53 projectors;

compare raw_emission_E only as a holdout;

construct exact support and expressions;

export certified numerical arrays;

load them through the read-only API;

run the independent intertwiner-nullspace route;

run C53 impact tests;

rebuild every artifact byte-for-byte.
```

It must fail when:

```text
raw_emission_E is directly relabeled U3;

a 24 x 24 projector is numerically factored to define U3;

a numerical SVD chooses column phases;

the source generator order is changed;

the product basis order is guessed;

the Casimir normalization is assumed rather than derived;

the full/reduced C53 route is used as construction authority through
stored numerical values;

a support threshold is used;

a required artifact is missing;

a hash changes.
```

---

# 28. Focused mutation tests

Create at least **256 focused live mutations** of actual source, basis, expression, normalization, isometry, projector, array, or import objects.

Include mutations of:

```text
generator entry;

generator order;

Tr(Ta Tb) normalization;

f^{abc} sign;

adjoint-generator sign;

product basis row order;

triplet column order;

raw-emission index orientation;

Gram entry;

Casimir value;

normalization-plan ID;

inverse square-root factor;

column phase;

column permutation;

U3 exact entry;

U3 support status;

intertwiner equation;

projector entry;

projector rank;

raw_emission relation;

stored-projector relation;

certified numerical value;

error bound;

runtime path;

expression hash;

support hash;

package aggregate hash;

read-only array flag;

C53 impact status;

continuation branch.
```

Every mutation must fail a concrete source, representation, normalization, basis, exact-support, intertwiner, projector, certification, import, impact, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 29. Readiness gate

Issue:

```text
C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY
```

only when:

```text
the full C65 baseline reproduces;

the C65 no-go remains explicit;

C53 positive scientific status remains unchanged;

the C53 color source fingerprints are complete;

fundamental and adjoint generators are exact;

the product-color basis is exact and ordered;

the retained-triplet basis is exact and ordered;

E_src is source derived;

its Gram matrix and rank are exact;

one normalization plan is selected;

U3 exists as an exact 24 x 3 map;

U3-dagger U3 = I exactly;

all intertwiner identities close exactly;

P3 = U3 U3-dagger closes exactly;

P3 is Hermitian, idempotent, rank three, trace three;

anti-sextet and 15 leakage are zero;

every stored C53 projector has a complete relation status;

raw_emission_E has a complete normalization relation;

every U3 entry has an exact terminal status;

no entry remains undecidable;

all expressions and basis orders are hashed;

certified numerical arrays and bounds exist;

the runtime inventory is complete;

the read-only API verifies hashes and regenerates nothing;

the independent reconstruction agrees;

the C53 impact audit is fully typed;

the correct C67 contract exists;

deterministic reconstruction passes;

count-once and provenance close;

poisoning controls pass;

the end-to-end test passes.
```

Do not issue:

```text
C66_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY;

C66_IFERM_CONTACT_SUPPORT_READY;

C66_DIRECT_IFERM_CONTACT_READY;

C66_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C66_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY.
```

---

# 30. Exact continuation decision

Select exactly one branch.

## 30.1 Isometry artifact ready; C53 remains valid

Issue:

```text
C66_SOURCE_DERIVED_TRIPLET_ISOMETRY_ARTIFACT_READY
```

Required C53 status:

```text
UNCHANGED_EXACTLY_ARTIFACT_GAP_ONLY;

READ_ONLY_IMPORT_ADAPTER_REQUIRED_NO_OPERATOR_REBUILD;

or

SUPPORT_CERTIFICATE_SUPERSEDED_VALUES_VALID.
```

Next:

> **C67/QGEMBED4 — resume exact physical \(qg\) embedding using C64 and C66**

## 30.2 C53 numerical vertex rebuild required

Issue:

```text
C66_TRIPLET_ISOMETRY_READY_C53_VERTEX_SUPERSESSION_REQUIRED
```

Next:

> **C67/VERTEX5 — rebuild the physical canonical vertex using the exact C66 isometry before downstream embedding**

## 30.3 C53 impact unresolved

Issue:

```text
C66_QGCOLOR_C53_IMPACT_INCOMPLETE
```

Next:

> **C67/QGCOLOR-IMPACT — complete full/reduced route, basis covariance, and vertex-impact closure**

Do not proceed to QGEMBED4 if a C53 numerical rebuild is required.

---

# 31. Exact no-go branches

## A. SU(3) convention or basis order incomplete

```text
C66_QGCOLOR_SU3_BASIS_CONTRACT_INCOMPLETE
```

Next:

> **C67/QGCOLOR-SRC — fundamental/adjoint generators, product ordering, and retained-triplet basis completion**

## B. Source color map orientation incomplete

```text
C66_QGCOLOR_EMISSION_MAP_INCOMPLETE
```

Next:

> **C67/QGCOLOR-MAP — source canonical color-index orientation and factorization completion**

## C. Normalization incomplete

```text
C66_QGCOLOR_NORMALIZATION_INCOMPLETE
```

Next:

> **C67/QGCOLOR-NORM — exact Gram, Casimir, positive square root, and column-basis normalization completion**

## D. Intertwiner or projector equivalence fails

```text
C66_QGCOLOR_INTERTWINER_PROJECTOR_FAILED
```

Next:

> **C67/QGCOLOR-XCHECK — representation identity, projector, complement, and basis-adapter reconciliation**

## E. Numerical/runtime artifact integrity incomplete

```text
C66_QGCOLOR_RUNTIME_INTEGRITY_INCOMPLETE
```

Next:

> **C67/QGCOLOR-RUNTIME — exact-expression, certified-array, path, hash, and import closure**

## F. Isometry closes

Use one of the continuation statuses in Section 30.

---

# 32. Required deliverables

Create at least:

```text
docs/next_level/c66_implementation_report.md
docs/next_level/c66_api.md
docs/next_level/c66_derivation_authority_manifest.json
docs/next_level/c66_input_fidelity_audit.json

docs/next_level/c66_calculation_plan.json
docs/next_level/c66_holdout_plan.json

docs/next_level/c66_exact_su3_generator_manifest.json
docs/next_level/c66_su3_generator_validation.json
docs/next_level/c66_structure_constant_manifest.json

docs/next_level/c66_product_color_basis_manifest.json
docs/next_level/c66_product_generator_manifest.json
docs/next_level/c66_product_basis_validation.json

docs/next_level/c66_retained_triplet_basis_manifest.json
docs/next_level/c66_triplet_basis_adapter.json
docs/next_level/c66_triplet_basis_validation.json

docs/next_level/c66_source_color_emission_map.json
docs/next_level/c66_source_color_emission_validation.json
docs/next_level/c66_color_emission_gram.json
docs/next_level/c66_color_emission_gram_validation.json

docs/next_level/c66_triplet_normalization_plan.json
docs/next_level/c66_triplet_normalization_decision.json
docs/next_level/c66_exact_triplet_isometry.json
docs/next_level/c66_triplet_isometry_validation.json

docs/next_level/c66_triplet_intertwiner_contract.json
docs/next_level/c66_triplet_intertwiner_validation.json
docs/next_level/c66_exact_triplet_projector.json
docs/next_level/c66_triplet_projector_validation.json

docs/next_level/c66_c53_projector_inventory.json
docs/next_level/c66_c53_projector_equivalence_report.json
docs/next_level/c66_raw_emission_relation.json
docs/next_level/c66_raw_emission_relation_validation.json

docs/next_level/c66_triplet_expression_manifest.json
docs/next_level/c66_triplet_support_manifest.json
docs/next_level/c66_triplet_hash_manifest.json

docs/next_level/c66_numerical_certification_plan.json
docs/next_level/c66_certified_triplet_export.json
docs/next_level/c66_error_bound_validation.json
docs/next_level/c66_precision_stability_report.json

docs/next_level/c66_runtime_path_manifest.json
docs/next_level/c66_numerical_object_inventory.json
docs/next_level/c66_runtime_completeness_report.json

docs/next_level/c66_api_contract.json
docs/next_level/c66_api_validation.json
docs/next_level/c66_independent_isometry_reconstruction.json
docs/next_level/c66_two_route_equivalence_report.json

docs/next_level/c66_c53_impact_audit.json
docs/next_level/c66_c53_basis_covariance_report.json

docs/next_level/c66_deterministic_reconstruction_report.json
docs/next_level/c66_restart_parallel_report.json
docs/next_level/c66_environment_manifest.json
docs/next_level/c66_artifact_ancestry_ledger.json
docs/next_level/c66_count_once_report.json
docs/next_level/c66_isolation_report.json

docs/next_level/c66_readiness_report.json
docs/next_level/c66_source_sufficiency_decision.json
docs/next_level/c66_no_go_decision_tree.json
docs/next_level/c66_missing_calculation_specification.md
docs/next_level/c66_regression_report.json
```

Create exactly one next-package import contract:

```text
docs/next_level/c66_c67_qgembed4_import_contract.json

or

docs/next_level/c66_c67_vertex5_import_contract.json

or

docs/next_level/c66_c67_qgcolor_impact_import_contract.json.
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgcolor2/
```

or the repository-equivalent package.

Add focused tests for:

```text
SU(3) generators and structure constants;
product and triplet basis orders;
source color-emission map;
Gram and normalization;
exact U3;
intertwiner identities;
projector equivalence;
raw_emission relation;
exact support and expressions;
certified numerical arrays;
runtime hashes;
read-only API;
independent reconstruction;
C53 impact;
deterministic reconstruction;
end-to-end closure.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All committed JSON and every runtime artifact must reconstruct byte-for-byte.

---

# 33. Acceptance criteria

C66 is complete only when:

1. The full C65 baseline reproduces.
2. The C65 fail-closed status remains explicit.
3. C53 remains historically byte-identical.
4. C64 remains historically byte-identical and read-only.
5. C40 remains method-oracle only.
6. No C53 physical vertex numerical value defines \(U_3\).
7. `raw_emission_E` is not relabeled \(U_3\).
8. A \(24\times24\) projector is not factored numerically to define columns.
9. No numerical SVD/QR phase convention defines the triplet basis.
10. Fundamental generators are exact and hash locked.
11. Adjoint generators are exact and hash locked.
12. Generator normalization and signs are explicit.
13. The product-color basis order is explicit.
14. The retained-triplet basis order is explicit.
15. Any basis adapter is exact.
16. The source color map is independently derived.
17. Its coupling/kinematic factorization is explicit.
18. Its Gram matrix is exact.
19. Its rank is three.
20. One exact normalization plan is selected.
21. \(U_3\) is exactly \(24\times3\).
22. Every \(U_3\) entry has one terminal exact status.
23. No \(U_3\) entry remains undecidable.
24. \(U_3^\dagger U_3=I_3\) closes exactly.
25. Every generator intertwiner identity closes exactly.
26. \(P_3=U_3U_3^\dagger\) closes exactly.
27. \(P_3\) is Hermitian and idempotent.
28. \(P_3\) has rank and trace three.
29. Anti-sextet and 15 leakage are zero.
30. Every stored C53 projector has a complete relation status.
31. The relation to `raw_emission_E` is exact and typed.
32. C65's historical refusal to substitute remains valid.
33. Exact expressions, zeros, and support are materialized.
34. Row and column basis hashes are committed.
35. Certified numerical arrays have rigorous bounds.
36. Exact zeros remain literal zero.
37. Exact nonzeros are not pruned.
38. Precision changes do not alter support.
39. Runtime paths and hashes are complete.
40. The read-only API verifies every hash.
41. Imported arrays are immutable.
42. The loader regenerates nothing.
43. The independent intertwiner route agrees.
44. The C53 impact audit is complete.
45. Exactly one continuation branch is selected.
46. Deterministic serial/parallel/restart reconstruction passes.
47. Every entry and artifact has complete ancestry.
48. Duplicate, missing, orphan, hash-mismatch, undecidable, and unresolved-impact counts are zero.
49. Static and runtime poisoning controls pass.
50. At least 256 focused live mutations are detected.
51. No CM-ground/full physical \(qg\) embedding is created.
52. No endpoint/witness relation or contact object is created.
53. No canonical vertex is rebuilt inside the positive artifact branch.
54. No complete instantaneous-fermion or local-HQCD status is issued.
55. No Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
56. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
57. `MSHT20_REP/` remains untouched and outside Git.
58. The working tree is clean except for the pre-existing untracked directory.
59. A local completion commit is created and not pushed.

A rigorous no-go or supersession branch is valid. Do not weaken generator authority, basis ordering, exact normalization, intertwiner closure, projector equivalence, numerical certification, or C53-impact accounting to open the positive gate.

---

# 34. Final Codex response

Report:

- full starting and final commits;
- exact C53 source/API fingerprints;
- fundamental and adjoint generator conventions and hashes;
- \(\operatorname{Tr}(T^aT^b)\), \(C_F\), \(C_A\), \(f\), and \(d\) checks;
- product-color and retained-triplet basis orders and hashes;
- source color-emission map shape, rank, nnz, and expression hash;
- exact Gram matrix and normalization plan;
- exact basis adapter;
- exact \(U_3\) shape, nnz, support counts, and expression/status hashes;
- \(U_3^\dagger U_3\) residual;
- all generator-intertwiner residuals;
- \(P_3\) shape, rank, trace, Hermiticity, and idempotence residuals;
- anti-sextet and 15 leakage results;
- relation of every C53 projector to \(P_3\);
- exact relation to `raw_emission_E`;
- certified numerical precision and maximum error bounds;
- runtime paths and array hashes;
- read-only API validation;
- independent-reconstruction residuals;
- C53 impact decision;
- deterministic serial/parallel/restart results;
- ancestry, duplicate, missing, orphan, undecidable, and unresolved-impact counts;
- isolation and poisoning results;
- focused mutation results;
- exact readiness/no-go/supersession status;
- exact next branch;
- confirmation that no CM-ground/full physical \(qg\) embedding, endpoint/witness support, contact value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a differently normalized emission map, an arbitrary projector factorization, a numerically chosen triplet basis, an unverified column phase, or a non-hash-verified in-memory object as the frozen \(24\times3\) C53-convention triplet isometry.
