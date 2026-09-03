# C63/QGEMBED2 Codex Work Package

## Title

**Exact CM-ground and color-triplet physical \(qg\) embedding: threshold-free composition of the C62 Talmi–Moshinsky algebra, certified historical-basis adapters, and C52/C53/C57/C58 descendant-impact closure**

## Authoritative baseline

Start from the clean local C62/QGTM completion commit:

```text
cfe1680c381b9531a88e27571e3898a75f6ba784
```

Its immediate scientific parent is:

```text
c22c6ab04e79a591aacc5679efd2b0642c3ad4e8
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor c22c6ab04e79a591aacc5679efd2b0642c3ad4e8 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY

C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY

C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE

C61_EXACT_TM_ALGEBRA_INCOMPLETE

C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY
```

and the exact C62 scientific result:

```text
selected exact representation:
    QGTM-CIRCULAR-LADDER-PRIMARY;

global C45 polar/circular convention:
    |n,m>_polar
      = (-1)^n
        |n + max(m,0), n + max(-m,0)>_circ;

angular momentum:
    L_z = N_+ - N_-;

TM construction:
    exact longitudinal fractions;
    exact x-weighted two-mode binomial brackets;
    threshold-free polar TM coefficients;
    complete finite-shell exact algebra;

historical CM-ground subthreshold residues:
    K = 9/2:   4,032;
    K = 11/2: 15,840;
    K = 13/2: 48,048;

exact residue classification:
    every listed residue is an exact m-selection zero;
    genuine small nonzeros = 0;
    unresolved entries = 0;

historical C47 quadrature and argmax phases:
    diagnostics/holdouts only;

not yet constructed:
    no exact CM-ground physical qg embedding;
    no color-triplet-combined physical qg embedding;
    no final descendant-impact decision;
    no endpoint or witness relation;
    no direct-contact value or matrix.
```

Verify every formula, count, hash, basis order, exact-zero certificate, and numerical-export identity from the committed C62 artifacts rather than relying on this prompt.

The fixed architecture remains:

```text
longitudinal cell:
    -L <= x^- <= L;
    p^+ = pi k/L;
    P^+ = pi K/L;
    L remains symbolic;

physical trajectory:
    (K,Nmax,bHO/GeV)
      = (9/2,8,0.40)
      = (11/2,10,0.45)
      = (13/2,12,0.50);

one-particle transverse basis:
    exact C45 polar two-dimensional HO convention;

two-body transverse basis:
    exact C62 x-weighted relative/CM TM algebra;

physical qg basis:
    C47 finite many-body truncation;
    exact CM-ground sector;
    retained total-color triplet;

color convention:
    exact C53 SU(3) and frozen 24 x 3 triplet isometry.
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All historical C47 canonical tuple values, quadrature-derived phases, and thresholded masks remain diagnostic-only.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C62 proves that the historical subthreshold CM-ground residues do not hide genuine small TM coefficients. They are exact zeros by the angular-momentum selection rule.

This removes the specific threshold ambiguity that blocked C60, but it does not by itself prove that every descendant object is unchanged.

C63 must still distinguish:

```text
EXACT BASIS EQUALITY

    The historical and exact physical bases are identical after one
    explicit phase/permutation adapter.

BASIS-COVARIANT EQUIVALENCE

    The historical matrices remain valid in their historical basis,
    while the exact basis is related by a proved unitary adapter.

SUPPORT-SEMANTICS CORRECTION WITHOUT SUPPORT CHANGE

    Historical threshold language was too weak, but exact support IDs
    and counts are unchanged.

SUPPORT REBUILD

    Exact physical components change canonical reachability or a
    conditional regulator relation.

NUMERICAL OPERATOR REBUILD

    The exact embedding changes a projected C52/C53 operator beyond
    the certified historical quadrature error and basis covariance.

UNRESOLVED IMPACT

    The available comparison does not establish which case applies.
```

A changed phase convention is not automatically changed physics.

Conversely, numerical closeness is not sufficient to prove basis-covariant equality.

Historical artifacts must remain byte-identical. Corrections are descendant supersessions or adapters.

---

# 2. Exact purpose

C63 consumes the exact C62 TM algebra and constructs the complete physical \(qg\) embedding.

C63 must create:

```text
a read-only fidelity import of all C62 exact algebra and support
certificates;

the exact raw single-particle qg basis at every longitudinal
partition and resolution;

the exact relative-plus-CM basis and CM-ground physical kinematic
basis;

the exact CM-ground injection into the raw qg basis;

the exact adjoint projection and CM-ground image projector;

the complete longitudinal, helicity, Jz, OAM, and basis-order
extension of that transverse map;

the exact combination with the frozen C53 24 x 3 color-triplet
isometry;

the full exact/certified physical qg embedding and projection;

a threshold-free support ledger for every physical/raw component;

a certified numerical export for sparse and matrix-free downstream
use;

an explicit exact-to-historical basis adapter;

a complete C47 numerical/quadrature reconciliation;

a complete descendant-impact audit for C52, C53, C57, C58, C59,
and C60;

one exact continuation decision and immutable next-package import
contract.
```

C63 must not construct:

```text
C60 absorption or emission endpoint relations;

a direct-contact intermediate-witness relation;

a direct-contact numerator, denominator, normalization, value, or
matrix;

a new canonical vertex;

a new self-induced-inertia contraction;

a physical counterterm coefficient;

a complete instantaneous-fermion operator.
```

The strongest no-impact status is:

```text
C63_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY
```

When that status passes, the exact next package is:

> **C64/IFSUPPORT2 — reconstruct source-ordered direct-contact endpoint and intermediate-witness support using the immutable C63 exact embedding**

If C63 finds inherited support or operator impact, it must follow the supersession branches in Section 31.

---

# 3. Scientific boundary

C63 is:

```text
physical-basis-embedding specific;
exact CM-ground specific;
exact/certified color-triplet specific;
threshold free;
basis-adapter aware;
descendant-impact aware;
deterministic;
validation only.
```

C63 is not:

```text
a refit of C47 quadrature;

a replacement of historical files;

a contact calculation;

a canonical-vertex recalculation unless the audit selects a later
vertex-supersession branch;

a self-energy recalculation;

a physical renormalization calculation.
```

The exact embedding may be dense. Sparsity is an algebraic result, not a requirement.

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_qg_tm_validation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_cm_factorization_report.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_qg_triplet_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_colorless_matrix_free_report.json
docs/next_level/c52_numerical_object_inventory.json
docs/next_level/c52_readiness_report.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_count_once_report.json
docs/next_level/c53_physical_matrix_free_report.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_regulator_plan_decision.json
docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_canonical_support_validation.json
docs/next_level/c57_mode_ancestry_ledger.json
docs/next_level/c57_numerical_object_inventory.json
docs/next_level/c57_readiness_report.json

docs/next_level/c58_c57_import_report.json
docs/next_level/c58_pair_support_decision.json
docs/next_level/c58_mode_contribution_ledger.json
docs/next_level/c58_q_sector_contraction.json
docs/next_level/c58_c53_support_holdout.json
docs/next_level/c58_numerical_object_inventory.json
docs/next_level/c58_readiness_report.json

docs/next_level/c59_implementation_report.md
docs/next_level/c59_readiness_report.json

docs/next_level/c60_implementation_report.md
docs/next_level/c60_input_fidelity_audit.json
docs/next_level/c60_support_layer_contract.json
docs/next_level/c60_exact_zero_semantics.json
docs/next_level/c60_missing_calculation_specification.md
docs/next_level/c60_readiness_report.json

docs/next_level/c62_implementation_report.md
docs/next_level/c62_derivation_authority_manifest.json
docs/next_level/c62_input_fidelity_audit.json
docs/next_level/c62_exact_representation_decision.json
docs/next_level/c62_polar_ho_wavefunction_contract.json
docs/next_level/c62_circular_ladder_contract.json
docs/next_level/c62_polar_circular_phase_contract.json
docs/next_level/c62_exact_polar_cartesian_map.json
docs/next_level/c62_exact_two_mode_rotation.json
docs/next_level/c62_one_dimensional_bracket_contract.json
docs/next_level/c62_exact_polar_tm_contract.json
docs/next_level/c62_exact_tm_block_manifest.json
docs/next_level/c62_exact_tm_block_validation.json
docs/next_level/c62_tm_residue_ledger.json
docs/next_level/c62_tm_residue_reconciliation_report.json
docs/next_level/c62_certified_tm_export.json
docs/next_level/c62_precision_stability_report.json
docs/next_level/c62_provisional_descendant_impact.json
docs/next_level/c62_c63_qgembed2_import_contract.json
docs/next_level/c62_numerical_object_inventory.json
docs/next_level/c62_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c63_derivation_authority_manifest.json
docs/next_level/c63_input_fidelity_audit.json
```

---

# 5. Read-only C62 import gate

Before constructing the CM-ground map, verify:

```text
C62 status and baseline ancestry;

QGTM-CIRCULAR-LADDER-PRIMARY plan ID;

global polar/circular phase formula;

Lz convention;

exact longitudinal-fraction hashes;

exact two-mode-rotation hashes;

exact TM-expression hashes;

exact TM support hashes;

finite-shell block hashes;

certified numerical block hashes and error bounds;

residue-ledger hashes;

4,032 / 15,840 / 48,048 exact-zero counts;

genuine-small-nonzero count = 0;

unresolved count = 0.
```

C63 may not:

```text
change the C62 phase;

change a C62 exact-zero status;

reintroduce a support threshold;

replace an exact block with C47 quadrature;

prune a small exact nonzero;

or change a longitudinal partition.
```

Create:

```text
docs/next_level/c63_c62_import_report.json
```

Any mismatch blocks all downstream construction.

---

# 6. Freeze basis identities and holdouts

Freeze:

```text
exact longitudinal partitions;

raw q/g single-particle basis order;

relative/CM basis order;

CM-ground convention;

physical kinematic qg basis order;

quark and gluon helicity order;

Jz and OAM conventions;

C47 many-body Nmax rule;

C53 product-color and triplet basis order;

C53 triplet phase;

historical C47 basis order and quadrature phase records.
```

Freeze holdouts before assembly:

```text
one ground-shell CM-ground state;

one highest-shell CM-ground state per resolution;

one CM-excited state with exact orthogonality;

positive and negative intrinsic m;

one physical state with a single raw component;

one physical state with multiple exact raw components;

one exact-zero raw component by m selection;

one nonzero component near the smallest numerical magnitude;

one historical phase/permutation adapter row per shell;

one raw/physical round-trip vector;

one color-triplet basis vector;

one basis-rotated triplet vector;

one C52 colorless holdout;

one C53 physical-vertex holdout;

one C57 support holdout;

one C58 admitted-mode holdout;

one adjacent-resolution embedding comparison.
```

No failed holdout may be moved into construction after inspection.

Create:

```text
docs/next_level/c63_calculation_plan.json
docs/next_level/c63_holdout_plan.json
```

---

# 7. Exact raw \(qg\) basis

Construct the exact raw product basis at every resolution:

```text
longitudinal q mode;

longitudinal g mode;

q transverse polar-HO mode;

g transverse polar-HO mode;

q helicity;

g helicity;

fundamental q color;

adjoint g color;

total K;

total Jz;

zero-mode status;

basis-order identity.
```

Keep distinct:

```text
raw kinematic basis;

raw product-color basis;

fixed-K many-body basis;

physical CM-ground basis;

physical triplet basis.
```

Report dimensions and block decompositions.

The expected physical colorless and triplet dimensions are:

```text
K = 9/2:
    colorless physical qg = 448;
    triplet physical qg = 1,344;

K = 11/2:
    colorless physical qg = 900;
    triplet physical qg = 2,700;

K = 13/2:
    colorless physical qg = 1,584;
    triplet physical qg = 4,752.
```

Verify these values from committed manifests. Do not hard-code them when the repository basis differs.

Create:

```text
docs/next_level/c63_raw_qg_basis_manifest.json
docs/next_level/c63_physical_qg_basis_manifest.json
docs/next_level/c63_basis_order_manifest.json
```

---

# 8. Exact CM-ground injection

C62 supplies coefficients in the orientation:

\[
\langle
n_{\rm rel},m_{\rm rel};
n_{\rm CM},m_{\rm CM}
|
n_q,m_q;
n_g,m_g
\rangle_x
\]

or its exact committed equivalent.

Derive the physical-to-raw injection orientation explicitly.

For the orthonormal convention, the raw component of a physical state is the exact conjugate coefficient:

\[
\langle
n_q,m_q;
n_g,m_g
|
n_{\rm rel},m_{\rm rel};
0,0
\rangle_x.
\]

Do not assume this orientation without checking the C62 block convention.

Construct:

\[
J_{\rm CM,R}^{\rm kin}:
\mathcal H_{qg,R}^{\rm rel,CM=0}
\longrightarrow
\mathcal H_{qg,R}^{\rm raw,kin}.
\]

Retain exact coefficient expressions and exact support statuses.

Required checks:

```text
the CM state is exactly n_CM=0,m_CM=0 in the committed convention;

the injection orientation is correct;

all exact m-selection zeros remain literal zeros;

no threshold is used;

the map preserves K, helicities, Jz, and total transverse shell;

the highest retained shell is complete.
```

Create:

```text
docs/next_level/c63_exact_cm_ground_injection.json
docs/next_level/c63_cm_ground_injection_validation.json
```

---

# 9. Exact kinematic projection and image projector

Construct the exact adjoint or metric adjoint:

\[
P_{\rm CM,R}^{\rm kin}.
\]

For orthonormal raw and physical bases require:

\[
P_{\rm CM,R}^{\rm kin}
=
\left(J_{\rm CM,R}^{\rm kin}\right)^\dagger.
\]

When a nontrivial metric is present, use the exact Gram-metric adjoint.

Require:

\[
P_{\rm CM,R}^{\rm kin}
J_{\rm CM,R}^{\rm kin}
=
I_{\rm phys,kin},
\]

and define:

\[
\Pi_{\rm CM,R}^{\rm raw}
=
J_{\rm CM,R}^{\rm kin}
P_{\rm CM,R}^{\rm kin}.
\]

Verify:

\[
\Pi_{\rm CM,R}^{\rm raw}
=
\left(\Pi_{\rm CM,R}^{\rm raw}\right)^\dagger,
\qquad
\left(\Pi_{\rm CM,R}^{\rm raw}\right)^2
=
\Pi_{\rm CM,R}^{\rm raw}.
\]

Also verify exact orthogonality to every retained CM-excited state.

Create:

```text
docs/next_level/c63_exact_cm_ground_projection.json
docs/next_level/c63_cm_ground_projector_validation.json
```

---

# 10. Complete kinematic physical embedding

Extend the transverse CM-ground injection with the exact identities and permutations for:

```text
longitudinal partition;

quark helicity;

gluon helicity;

total Jz;

physical kinematic basis order.
```

Construct:

\[
J_{qg,R}^{\rm kin},
\qquad
P_{qg,R}^{\rm kin}.
\]

Each nonzero component must retain:

```text
physical basis ID;

raw basis ID;

exact TM-expression hash;

exact support status;

longitudinal-partition ID;

helicity identities;

intrinsic/CM ancestry;

basis-order hash.
```

Required checks:

```text
P_kin J_kin = I;

J_kin P_kin = exact CM-ground image projector;

rank and nullity;

K, Jz, helicity, and OAM covariance;

exact support count;

basis-order independence;

matrix-free embed/project agreement.
```

Create:

```text
docs/next_level/c63_exact_kinematic_qg_embedding.json
docs/next_level/c63_kinematic_embedding_validation.json
```

---

# 11. Read-only color-triplet import

Import the C53/C47 color objects read-only:

```text
fundamental and adjoint SU(3) conventions;

product-color basis order;

24 x 3 triplet isometry U3;

triplet projector;

triplet basis phase;

triplet-image and leakage certificates;

basis-rotation contract.
```

Verify all hashes.

The color support and exact-zero semantics must descend from the C53 algebraic certificates, not from a floating threshold on \(U_3\).

Create:

```text
docs/next_level/c63_triplet_import_report.json
```

Any color-hash mismatch blocks full physical assembly.

---

# 12. Exact full physical \(qg\) embedding

Construct the complete map:

\[
J_{qg,R}^{\rm phys}:
\mathcal H_{qg,R}^{\rm CM=0,triplet}
\longrightarrow
\mathcal H_{qg,R}^{\rm raw,kin\otimes(3\otimes8)}.
\]

When kinematic/color factorization is valid, prove the exact permutation-equivalent form:

\[
J_{qg,R}^{\rm phys}
=
\mathcal P_{\rm raw}
\left(
J_{qg,R}^{\rm kin}
\otimes
U_3
\right)
\mathcal P_{\rm phys}^{-1}.
\]

Do not assume the raw Kronecker ordering.

Construct its exact adjoint or metric adjoint:

\[
P_{qg,R}^{\rm phys}.
\]

Required checks:

```text
P_phys J_phys = I_phys;

J_phys P_phys is the exact CM-ground triplet image projector;

rank equals the physical qg dimension;

zero anti-sextet and 15 leakage;

CM and color projectors commute where claimed;

triplet-basis rotation covariance;

K, Jz, helicity, and OAM preservation;

basis-order hashes.
```

Create:

```text
docs/next_level/c63_exact_physical_qg_embedding.json
docs/next_level/c63_physical_embedding_validation.json
docs/next_level/c63_color_cm_factorization_report.json
```

---

# 13. Threshold-free physical support ledger

A physical/raw component belongs to support only when:

```text
the C62 TM coefficient is exact nonzero;

the longitudinal/helicity/Jz identity permits it;

the C53 triplet coefficient has exact nonzero support;

the basis permutation maps the pair.
```

Each pair receives one status:

```text
ZERO_BY_EXACT_TM_RULE;

ZERO_BY_EXACT_TM_CANCELLATION;

ZERO_BY_EXACT_COLOR_RULE;

ZERO_BY_CM_OR_BASIS_SELECTION;

NONZERO_EXACT_ALGEBRAIC;

NONZERO_CERTIFIED_NUMERICAL_COLOR_FACTOR;

UNDECIDABLE_BLOCKING.
```

A positive gate requires:

```text
UNDECIDABLE_BLOCKING = 0.
```

Never derive support from:

```text
abs(value) > tolerance;

historical sparse storage;

the C57 1e-12 mask;

or C53 evaluated matrix values.
```

Create:

```text
docs/next_level/c63_exact_physical_embedding_support.json
docs/next_level/c63_exact_support_validation.json
```

---

# 14. Exact-to-historical basis adapter

Construct explicit adapters between:

```text
the exact C62/C63 physical kinematic basis;

the historical C47 quadrature/argmax physical basis.
```

Separate:

```text
basis permutation;

diagonal or block-unitary phase;

quadrature residual;

possible basis-subspace mismatch.
```

Define the adapter orientation explicitly, for example:

\[
J_{\rm hist}
=
J_{\rm exact}
A_{\rm exact\leftarrow hist}
+
\Delta_{\rm quad},
\]

or the exact committed equivalent.

Do not choose the adapter by fitting the full historical matrix.

It must descend from:

```text
the C62 global polar phase;

the historical recorded row phases;

the exact basis permutations;

and the common source basis definitions.
```

Required checks:

```text
unitarity or exact isometry of the adapter;

shell and m block structure;

global consistency across longitudinal partitions;

no support-changing phase;

historical-to-exact and exact-to-historical round trips;

quadrature residual bounded by the historical numerical method.
```

Create:

```text
docs/next_level/c63_historical_basis_adapter.json
docs/next_level/c63_historical_basis_adapter_validation.json
```

---

# 15. Historical C47 embedding reconciliation

Compare the exact embedding with the immutable C47 quadrature embedding after applying only the proved adapter.

Separate:

```text
exact-zero quadrature noise;

ordinary quadrature error on nonzero entries;

historical phase convention;

basis permutation;

scale or normalization mismatch;

implementation discrepancy.
```

Reconfirm that all:

```text
4,032 / 15,840 / 48,048
```

subthreshold residues are exact zeros and do not enter exact support.

Also audit every historical above-threshold support entry.

Report:

```text
historical support count;

exact support count;

symmetric difference after adapter;

maximum and distribution of certified numerical discrepancies;

row and column Gram residuals;

unexplained discrepancies.
```

Create:

```text
docs/next_level/c63_c47_embedding_reconciliation.json
docs/next_level/c63_c47_support_reconciliation.json
```

A positive gate requires no unexplained support discrepancy.

---

# 16. Certified numerical export

Export the exact physical embeddings to numerical sparse and matrix-free representations.

For every nonzero entry store or inherit:

```text
exact TM-expression hash;

exact color-certificate hash;

working precision;

rounded complex value;

rigorous or conservatively propagated absolute error bound;

exact support status;

basis IDs.
```

Support is serialized independently from magnitude.

Required checks:

```text
precision stability;

support stability;

P J = I within propagated bounds;

image-projector idempotence within propagated bounds;

exact zeros remain literal zero;

no magnitude pruning;

sparse and matrix-free embed/project agreement.
```

Create:

```text
docs/next_level/c63_certified_numerical_embedding_export.json
docs/next_level/c63_precision_stability_report.json
docs/next_level/c63_matrix_free_embedding_report.json
```

---

# 17. C47 basis-status decision

Historical C47 artifacts remain immutable.

Classify the relationship between C47 and C63 as one of:

```text
C47_NUMERICAL_EMBEDDING_VALID_IN_HISTORICAL_BASIS;

C47_VALUES_VALID_BUT_EXACT_SUPPORT_CERTIFICATE_SUPERSEDED;

C47_BASIS_ADAPTER_REQUIRED_NO_PHYSICS_CHANGE;

C47_NUMERICAL_EMBEDDING_SUPERSESSION_REQUIRED;

C47_IMPACT_UNRESOLVED_BLOCKING.
```

The classification must state whether future packages should consume:

```text
C63 exact basis directly;

C47 historical basis plus the C63 adapter;

or a rebuilt descendant operator.
```

Create:

```text
docs/next_level/c63_c47_basis_status_decision.json
```

---

# 18. C52/C53 impact audit

Do not silently rebuild or overwrite C52/C53.

Audit them through three independent layers.

## 18.1 Basis-covariance proof

Derive how colorless and physical canonical vertices transform under the C63 historical-basis adapter.

## 18.2 Frozen holdout reconstruction

Recompute frozen C52/C53 matrix elements from source primitives and the exact embedding without consuming stored matrix values.

## 18.3 Complete transformed comparison where tractable

Transform the immutable historical matrices into the exact basis and compare their support, values, adjoints, and matrix-free actions.

Poison C52/C53 stored values during the construction route.

Classify each package as:

```text
UNCHANGED_EXACTLY;

BASIS_ADAPTER_ONLY_NO_OPERATOR_REBUILD;

SUPPORT_ANCESTRY_CERTIFICATE_SUPERSEDED_VALUES_VALID;

NUMERICAL_OPERATOR_REBUILD_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

Create:

```text
docs/next_level/c63_c52_impact_audit.json
docs/next_level/c63_c53_impact_audit.json
docs/next_level/c63_vertex_basis_covariance_report.json
```

A vertex-rebuild branch takes precedence over every downstream support branch.

---

# 19. C57 support-impact audit

Reconstruct canonical reachability from:

```text
the source canonical endpoint rules;

the exact C63 embedding;

the fixed C57 operation order;

the fixed C57 corresponding-propagating-support plan.
```

Do not consume C53 numerical values.

Compare exact identities and counts with:

```text
C53 support-position holdout:
    312 / 510 / 756;

C57 conditional field-mode unions:
    1,216 / 2,320 / 3,936;

C57 candidate envelopes:
    2,304 / 4,400 / 7,488.
```

Report:

```text
exact support counts;

symmetric differences;

basis-adapter-only differences;

new or removed exact support edges;

mode-union changes;

envelope changes;

zero-mode and CM/triplet causes.
```

Classify C57 as:

```text
UNCHANGED_EXACTLY;

BASIS_ID_ADAPTER_ONLY;

SUPPORT_SEMANTICS_CERTIFICATE_SUPERSEDED_NO_SUPPORT_CHANGE;

SUPPORT_REBUILD_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

Create:

```text
docs/next_level/c63_c57_support_impact_audit.json
```

---

# 20. C58 impact audit

Audit the immutable C58 ordered-joint support and q-sector self-induced-inertia result.

Reproduce or compare:

```text
ordered-joint support identities;

admitted contraction-mode counts:
    4,216 / 8,330 / 14,484;

q-sector primitive shape:
    6 x 6;

q-sector nonzero count:
    6;

qg status:
    IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY.
```

If the C57 support is unchanged exactly or through a bijective basis-ID adapter, prove whether the C58 mode ledger and q primitive remain unchanged.

Do not preserve C58 by threshold tuning.

Classify C58 as:

```text
UNCHANGED_EXACTLY;

BASIS_ID_ADAPTER_ONLY;

SUPPORT_LEDGER_REBUILD_REQUIRED_VALUES_UNCHANGED;

NUMERICAL_CONTRACTION_REBUILD_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

Create:

```text
docs/next_level/c63_c58_impact_audit.json
```

---

# 21. C59/C60 continuation audit

C59 and C60 created no direct-contact value or matrix.

Audit whether the exact C63 embedding resolves C60's sole blocker:

```text
exact raw/physical qg components;

exact projected-cancellation semantics;

threshold-free endpoint-support input.
```

Classify:

```text
C60_BLOCKER_RESOLVED_READY_FOR_IFSUPPORT2;

ADDITIONAL_ENDPOINT_INPUT_BLOCKING;

UPSTREAM_SUPERSESSION_MUST_RUN_FIRST.
```

Create:

```text
docs/next_level/c63_c59_c60_continuation_audit.json
```

---

# 22. Complete descendant dependency graph

Trace:

```text
C47 quadrature embedding;

C52 colorless vertex;

C53 physical vertex;

C57 conditional regulator;

C58 self-induced inertia;

C59 direct-contact preflight;

C60 support no-go.
```

For every consumed object record:

```text
historical hash;

exact C63 dependency;

basis adapter;

support impact;

numerical impact;

required supersession;

next authorized consumer.
```

Create:

```text
docs/next_level/c63_descendant_dependency_graph.json
docs/next_level/c63_inherited_impact_summary.json
docs/next_level/c63_supersession_plan.json
```

No positive descendant may be preserved by narrative assertion alone.

---

# 23. Exact embedding APIs

Create APIs equivalent to:

```python
physical_qg_raw_components(
    physical_qg_basis_id,
    resolution,
) -> tuple[ExactPhysicalEmbeddingComponent, ...]

embed_physical_qg_to_raw(
    physical_vector,
    resolution,
    precision=None,
)

project_raw_qg_to_physical(
    raw_vector,
    resolution,
    precision=None,
)

cm_ground_image_projector(
    resolution,
    precision=None,
)

historical_exact_basis_adapter(
    resolution,
    precision=None,
)
```

Return records must expose:

```text
exact support status;

TM expression hash;

color certificate hash;

certified numerical value and bound;

basis ancestry;

CM ancestry;

triplet ancestry;

historical-adapter identity.
```

Do not expose:

```text
a support threshold;

a prune-small option;

an argmax phase option;

a fit-to-C47 option.
```

Create:

```text
docs/next_level/c63_api_contract.json
docs/next_level/c63_api_validation.json
```

---

# 24. Physical-resolution comparison

Construct exact/certified comparison maps between adjacent resolutions.

Because \(K\), \(N_{\max}\), and \(b_{\rm HO}\) all change, do not claim literal inclusion.

Compare:

\[
R_{\rm raw}
J^{\rm phys}_{R'}
P_{\rm phys}
\quad\text{versus}\quad
J^{\rm phys}_{R}.
\]

Separate:

```text
longitudinal nonnesting;

finite-shell change;

bHO scale change;

exact TM-block change;

CM-ground change;

triplet-basis adapter;

basis-order adapter;

certified numerical rounding;

exact support change.
```

Create:

```text
docs/next_level/c63_embedding_comparison_maps.json
docs/next_level/c63_embedding_comparison_report.json
docs/next_level/c63_comparison_remainder_ledger.json
```

---

# 25. Count-once and provenance

Every nonzero physical/raw component must have one exact ancestry path.

Report:

```text
candidate physical/raw pair count;

exact TM-zero count;

exact color-zero count;

other exact selection-zero count;

exact nonzero count;

certified color-nonzero count;

undecidable count;

duplicate component count;

missing component count;

CM-ground component count;

triplet-combined component count.
```

For descendant impact also report:

```text
basis-adapter records;

support-changed records;

operator-rebuild records;

unresolved impact records.
```

A positive gate requires:

```text
undecidable = 0;

duplicate = 0;

missing = 0;

unresolved impact = 0.
```

Create:

```text
docs/next_level/c63_component_ancestry_ledger.json
docs/next_level/c63_count_once_report.json
```

---

# 26. Isolation and poisoning controls

Prove that C63 construction is unchanged when:

```text
all C40 arrays are poisoned;

all C47 quadrature values are poisoned after historical basis IDs
and holdout roles are loaded;

the historical 1e-12 threshold changes;

all historical C47 argmax phases are poisoned after the exact
adapter source records are frozen;

all C47 canonical tuples are poisoned;

all C50 combined values are poisoned;

all C52/C53 numerical matrices are poisoned during exact embedding
construction;

all C57/C58 numerical operator values are poisoned during exact
embedding construction;

ART25 files are inaccessible.
```

Impact-audit comparison stages may load immutable descendant outputs only after the construction objects and hashes are complete.

The build must fail when:

```text
a C62 exact block changes;

a C62 exact-zero status changes;

the CM-ground convention changes;

the physical basis order changes;

the triplet isometry changes;

a numerical threshold enters support;

a genuine nonzero is pruned;

an exact zero is inferred from magnitude;

the historical adapter is fitted rather than derived;

an impact status is promoted without its required comparison.
```

Create:

```text
docs/next_level/c63_isolation_report.json
```

---

# 27. Deterministic runtime bundles

For every resolution produce content-addressed bundles containing:

```text
raw qg basis records;

physical kinematic qg basis records;

exact CM-ground injection;

exact kinematic projection and image projector;

full triplet physical embedding and projection;

exact support ledger;

certified numerical sparse arrays;

matrix-free reconstruction metadata;

historical basis adapter;

C47 reconciliation records;

C52/C53/C57/C58 impact records;

comparison-map blocks.
```

Heavy exact-expression tables and numerical arrays may remain outside Git under:

```text
data/runtime/c63_qgembed2/
```

Commit an inventory containing:

```text
runtime path;

object type;

shape or record count;

exact-expression format;

working precision;

error bound;

basis-order hash;

CM-projector hash;

triplet hash;

support hash;

adapter hash;

array hash;

generator command.
```

Create:

```text
docs/next_level/c63_numerical_object_inventory.json
```

All JSON, exact expressions, certificates, and numerical arrays must regenerate byte-for-byte.

---

# 28. End-to-end source-to-physical-embedding test

Implement an end-to-end test that begins from C45, C47 basis definitions, C53 color certificates, and C62 exact algebra—not from prebuilt C63 arrays.

It must:

```text
verify the C62 import;

construct raw and physical kinematic basis identities;

construct the exact CM-ground injection;

construct its adjoint and image projector;

extend longitudinal/helicity/Jz identities;

import and verify the triplet isometry;

construct the full physical embedding;

derive exact support;

export certified numerical arrays;

construct the historical basis adapter;

reconcile C47;

run C52/C53/C57/C58 impact audits;

select the exact continuation branch;

run comparison, count-once, poisoning, and precision tests;

reproduce every hash.
```

It must fail when:

```text
C47 quadrature is used as construction authority;

the 1e-12 threshold changes exact support;

a C62 zero is made nonzero or vice versa;

the TM orientation is reversed without the adjoint proof;

a CM-excited state enters the physical basis;

a nontriplet color path is retained;

the raw Kronecker ordering is assumed without permutation proof;

the historical adapter is fitted;

C52/C53 values enter embedding construction;

C57/C58 counts are preserved by tuning;

an impact branch is skipped;

a runtime hash changes.
```

---

# 29. Focused mutation tests

Create at least **256 focused live mutations** of actual basis, embedding, support, adapter, or impact objects.

Include mutations of:

```text
C62 import hash;

TM coefficient status;

TM orientation;

longitudinal partition;

raw q mode;

raw g mode;

intrinsic mode;

CM label;

CM-ground injection;

metric adjoint;

image projector;

quark helicity;

gluon helicity;

Jz;

OAM;

raw basis order;

physical basis order;

triplet isometry;

triplet phase;

kinematic/color permutation;

exact support entry;

certified numerical value;

error bound;

historical basis adapter;

C47 reconciliation status;

C52 impact status;

C53 impact status;

C57 support edge;

C58 mode-ledger status;

continuation branch;

comparison map;

runtime hash.
```

Every mutation must fail a concrete source, exact-zero, isometry, CM, color, support, certification, adapter, impact, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 30. Readiness and impact gates

The exact physical embedding gate requires:

```text
the full C62 baseline reproduces;

the C62 positive status remains explicit;

all exact TM blocks import read-only;

the raw and physical basis manifests are complete;

the exact CM-ground injection exists;

the exact projection and image projector close;

the kinematic embedding closes;

the triplet import closes;

the full physical embedding closes;

support is threshold free;

no component remains undecidable;

certified numerical arrays are stable;

the historical basis adapter closes;

C47 reconciliation has no unexplained discrepancy;

C52/C53 impact is fully typed;

C57/C58 impact is fully typed;

C59/C60 continuation is fully typed;

count-once and provenance close;

comparison maps execute;

poisoning controls pass;

runtime bundles reproduce byte-for-byte;

the end-to-end test passes.
```

After those conditions pass, issue exactly one status from Section 31.

Do not issue:

```text
C63_IFERM_CONTACT_SUPPORT_READY;

C63_DIRECT_IFERM_CONTACT_READY;

C63_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C63_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C63_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 31. Exact continuation decision

Select exactly one branch.

## 31.1 Exact embedding ready; no upstream rebuild

Issue:

```text
C63_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY
```

Required impact decisions:

```text
C52/C53:
    unchanged exactly,
    basis-adapter only,
    or support-certificate supersession with valid values;

C57:
    unchanged exactly,
    basis-ID adapter only,
    or exact support-certificate supersession with no support change;

C58:
    unchanged exactly or basis-ID adapter only;

C60 blocker:
    resolved.
```

Next:

> **C64/IFSUPPORT2 — source-ordered direct-contact endpoint and witness support using the exact C63 embedding**

## 31.2 C57/C58 support supersession required

Issue:

```text
C63_EXACT_QG_EMBEDDING_READY_IFREG_SUPERSESSION_REQUIRED
```

Conditions:

```text
the exact physical embedding is complete;

C52/C53 do not require a numerical operator rebuild;

C57 or C58 support identities or mode ledgers change.
```

Next:

> **C64/IFREG3 — rebuild corresponding-propagating regulator and self-induced-inertia support from the exact C63 embedding**

## 31.3 C52/C53 vertex supersession required

Issue:

```text
C63_EXACT_QG_EMBEDDING_READY_VERTEX_SUPERSESSION_REQUIRED
```

Conditions:

```text
the exact physical embedding is complete;

a C52/C53 numerical operator or indispensable support ancestry
requires rebuilding.
```

This branch takes precedence over the IFREG branch.

Next:

> **C64/VERTEX4 — rebuild the colorless and physical canonical vertex in the exact C63 basis, then revalidate downstream support**

## 31.4 Descendant impact unresolved

Issue:

```text
C63_QG_EMBEDDING_DESCENDANT_IMPACT_INCOMPLETE
```

Next:

> **C64/QGIMPACT — complete basis-adapter, operator-covariance, and support/mode-ledger impact closure**

Do not proceed to IFSUPPORT2 when an upstream positive package requires supersession.

---

# 32. Exact no-go branches

## A. C62 import fails

```text
C63_QGEMBED_C62_IMPORT_INCOMPLETE
```

Next:

> **C64/QGTM2 — exact TM artifact and support-certificate integrity completion**

## B. CM-ground injection or projector remains incomplete

```text
C63_QG_CM_GROUND_EMBEDDING_INCOMPLETE
```

Next:

> **C64/QGCM2 — exact CM-ground orientation, adjoint, image-projector, and basis completion**

## C. Full triplet embedding remains incomplete

```text
C63_QG_TRIPLET_EMBEDDING_INCOMPLETE
```

Next:

> **C64/QGCOLOR — exact kinematic/color ordering, triplet isometry, and leakage completion**

## D. Certified numerical export fails

```text
C63_QG_EMBEDDING_NUMERICAL_CERTIFICATION_FAILED
```

Next:

> **C64/QGNUM2 — precision, error-bound, sparse, and matrix-free embedding closure**

## E. Historical basis adapter remains incomplete

```text
C63_QG_HISTORICAL_BASIS_ADAPTER_INCOMPLETE
```

Next:

> **C64/QGADAPT — exact phase/permutation adapter and C47 quadrature reconciliation**

## F. Exact physical embedding closes

Use one of the four continuation statuses in Section 31.

---

# 33. Required deliverables

Create at least:

```text
docs/next_level/c63_implementation_report.md
docs/next_level/c63_api.md
docs/next_level/c63_derivation_authority_manifest.json
docs/next_level/c63_input_fidelity_audit.json
docs/next_level/c63_c62_import_report.json

docs/next_level/c63_calculation_plan.json
docs/next_level/c63_holdout_plan.json
docs/next_level/c63_raw_qg_basis_manifest.json
docs/next_level/c63_physical_qg_basis_manifest.json
docs/next_level/c63_basis_order_manifest.json

docs/next_level/c63_exact_cm_ground_injection.json
docs/next_level/c63_cm_ground_injection_validation.json
docs/next_level/c63_exact_cm_ground_projection.json
docs/next_level/c63_cm_ground_projector_validation.json

docs/next_level/c63_exact_kinematic_qg_embedding.json
docs/next_level/c63_kinematic_embedding_validation.json
docs/next_level/c63_triplet_import_report.json
docs/next_level/c63_exact_physical_qg_embedding.json
docs/next_level/c63_physical_embedding_validation.json
docs/next_level/c63_color_cm_factorization_report.json

docs/next_level/c63_exact_physical_embedding_support.json
docs/next_level/c63_exact_support_validation.json
docs/next_level/c63_historical_basis_adapter.json
docs/next_level/c63_historical_basis_adapter_validation.json
docs/next_level/c63_c47_embedding_reconciliation.json
docs/next_level/c63_c47_support_reconciliation.json
docs/next_level/c63_c47_basis_status_decision.json

docs/next_level/c63_certified_numerical_embedding_export.json
docs/next_level/c63_precision_stability_report.json
docs/next_level/c63_matrix_free_embedding_report.json

docs/next_level/c63_c52_impact_audit.json
docs/next_level/c63_c53_impact_audit.json
docs/next_level/c63_vertex_basis_covariance_report.json
docs/next_level/c63_c57_support_impact_audit.json
docs/next_level/c63_c58_impact_audit.json
docs/next_level/c63_c59_c60_continuation_audit.json

docs/next_level/c63_descendant_dependency_graph.json
docs/next_level/c63_inherited_impact_summary.json
docs/next_level/c63_supersession_plan.json

docs/next_level/c63_api_contract.json
docs/next_level/c63_api_validation.json
docs/next_level/c63_embedding_comparison_maps.json
docs/next_level/c63_embedding_comparison_report.json
docs/next_level/c63_comparison_remainder_ledger.json
docs/next_level/c63_component_ancestry_ledger.json
docs/next_level/c63_count_once_report.json
docs/next_level/c63_isolation_report.json

docs/next_level/c63_numerical_object_inventory.json
docs/next_level/c63_readiness_report.json
docs/next_level/c63_source_sufficiency_decision.json
docs/next_level/c63_no_go_decision_tree.json
docs/next_level/c63_missing_calculation_specification.md
docs/next_level/c63_regression_report.json
```

Create exactly one next-package import contract:

```text
docs/next_level/c63_c64_ifsupport2_import_contract.json

or

docs/next_level/c63_c64_ifreg3_import_contract.json

or

docs/next_level/c63_c64_vertex4_import_contract.json

or

docs/next_level/c63_c64_qgimpact_import_contract.json.
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgembed2/
```

or the repository-equivalent package.

Add focused tests for:

```text
C62 import;
raw and physical basis identities;
CM-ground injection and projector;
kinematic embedding;
triplet import and full embedding;
exact support;
certified numerical export;
historical basis adapter;
C47 reconciliation;
C52/C53 basis covariance and impact;
C57/C58 support and mode-ledger impact;
C59/C60 continuation;
count once;
isolation;
comparison maps;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON, exact expressions, certificates, and runtime arrays must reproduce byte-for-byte.

---

# 34. Acceptance criteria

C63 is complete only when:

1. The full C62 baseline reproduces.
2. The C62 positive gate remains explicit.
3. C43/C45/C47 historical files remain unchanged.
4. C52/C53/C57/C58 historical artifacts remain unchanged.
5. C40 remains method-oracle only.
6. Historical quadrature remains diagnostic-only.
7. The historical \(10^{-12}\) threshold cannot change exact support.
8. No physical coupling, subtraction, or counterterm coefficient is chosen.
9. No direct-contact value or matrix is evaluated.
10. Every C62 import hash passes.
11. The global polar/circular phase remains unchanged.
12. All 4,032/15,840/48,048 residues remain exact zeros.
13. The raw qg basis is explicit.
14. The physical kinematic qg basis is explicit.
15. Expected dimensions are verified rather than assumed.
16. The TM orientation for physical-to-raw injection is proved.
17. The exact CM-ground injection exists.
18. The exact adjoint or metric adjoint exists.
19. \(P_{\rm kin}J_{\rm kin}=I\) closes.
20. The raw CM-ground image projector is Hermitian and idempotent.
21. Every retained CM-excited state is orthogonal to the image.
22. Longitudinal, helicity, Jz, and OAM identities are preserved.
23. The C53 triplet isometry imports read-only.
24. The raw color/kinematic ordering is explicit.
25. The full physical embedding exists.
26. \(P_{\rm phys}J_{\rm phys}=I\) closes.
27. No anti-sextet or 15 leakage is hidden.
28. CM/color factorization is proved where claimed.
29. Exact support uses no numerical threshold.
30. No component remains undecidable.
31. Certified numerical arrays carry error bounds.
32. Precision changes do not alter support.
33. Sparse and matrix-free embed/project routes agree.
34. The exact-to-historical basis adapter is source derived.
35. The adapter is not fitted to C47.
36. The historical and exact basis relation has a complete status.
37. C47 support reconciliation has no unexplained discrepancy.
38. C52 impact is fully typed.
39. C53 impact is fully typed.
40. C57 support counts and identities are independently audited.
41. C58 support, mode counts, and primitive impact are independently audited.
42. C59/C60 continuation has a complete status.
43. No positive descendant is preserved by threshold tuning.
44. Any basis-only change is distinguished from an operator rebuild.
45. Vertex supersession takes precedence over IFREG supersession.
46. The exact next branch follows the impact decision.
47. Every component has complete ancestry.
48. Duplicate, missing, undecidable, and unresolved-impact counts are zero.
49. Comparison maps retain all nonnested and basis-adapter remainders.
50. Static and runtime poisoning controls pass.
51. Runtime bundles contain actual exact/certified embeddings and impact records.
52. End-to-end reconstruction passes.
53. At least 256 focused live mutations are detected.
54. No endpoint relation, witness relation, contact support, contact value, or contact matrix is created.
55. No complete instantaneous-fermion or local-HQCD status is issued.
56. No JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
57. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
58. `MSHT20_REP/` remains untouched and outside Git.
59. The working tree is clean except for the pre-existing untracked directory.
60. A local completion commit is created and not pushed.

A rigorous no-go or supersession branch is valid. Do not weaken exact CM projection, triplet leakage, threshold-free support, basis-covariance proof, certified numerical export, or descendant-impact accounting to open the no-impact gate.

---

# 35. Final Codex response

Report:

- full starting and final commits;
- exact C62 import hashes and reproduced residue counts;
- raw and physical qg dimensions and block decompositions;
- CM-ground injection and projection shapes, ranks, nnz, and exact/certified residuals;
- CM-image projector rank, Hermiticity, idempotence, and CM-excited orthogonality;
- kinematic embedding shapes, ranks, nullities, support counts, and round-trip residuals;
- triplet import hashes;
- full physical embedding shapes, ranks, nullities, support counts, and round-trip residuals;
- color leakage and basis-rotation residuals;
- certified numerical precisions and error bounds;
- historical basis-adapter formula, shape, phase/permutation content, and residuals;
- C47 support and numerical reconciliation;
- C47 basis-status decision;
- C52 impact status and basis-covariance residuals;
- C53 impact status and basis-covariance residuals;
- exact C57 support positions, union/envelope counts, and symmetric differences;
- exact C58 ordered-joint/admitted-mode counts and primitive-impact status;
- C59/C60 continuation status;
- complete descendant supersession decision;
- comparison-map residuals and separated remainders;
- ancestry, duplicate, missing, undecidable, and unresolved-impact counts;
- isolation and poisoning results;
- runtime expression, support, adapter, and array hashes;
- focused mutation results;
- exact readiness/no-go/supersession status;
- exact next branch;
- confirmation that no endpoint/witness relation, direct-contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a thresholded embedding, an unproved TM orientation, a CM projector inferred from small values, a raw Kronecker ordering assumed without a permutation proof, a fitted historical adapter, or an unaudited descendant as the exact physical \(qg\) embedding.
