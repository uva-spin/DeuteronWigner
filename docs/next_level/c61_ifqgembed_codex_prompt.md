# C61/IFQGEMBED Codex Work Package

## Title

**Exact raw-to-physical \(qg\) embedding: algebraic \(x\)-weighted two-dimensional Talmi–Moshinsky maps, certified zero/nonzero semantics, exact CM-ground and triplet projection, quadrature-residue reconciliation, and inherited-support impact audit**

## Authoritative baseline

Start from the clean local C60/IFSUPPORT fail-closed completion commit:

```text
0d74c218e304a9bdb9c13eaaaf8b0abdab2531f6
```

Its immediate scientific parent is:

```text
3174722ee1fc2d0045ee10273b4338f335b262b9
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 3174722ee1fc2d0045ee10273b4338f335b262b9 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY

C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY

C59_IFERM_CONTACT_SUPPORT_INCOMPLETE

C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE
```

and the exact C60 result:

```text
C58:
    unchanged and read-only;

C47 TM/CM embedding:
    quadrature derived;
    contains nonzero floating residues below the C57 support threshold
    of 1e-12;

subthreshold residue counts:
    K = 9/2:   4,032
    K = 11/2: 15,840
    K = 13/2: 48,048

C60 requirement:
    exact raw-path support;
    exact projected-cancellation semantics;
    no threshold-promoted exact zero;

consequence:
    no absorption endpoint relation;
    no emission endpoint relation;
    no intermediate-witness relation;
    no Boolean pair adjacency;
    no direct-contact value or matrix.
```

Verify these values and every consumed hash from the committed C60 records rather than relying on this prompt.

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

longitudinal cell:
    -L <= x^- <= L
    p^+ = pi k/L
    P^+ = pi K/L
    L remains symbolic

physical trajectory:
    (K,Nmax,bHO/GeV)
      = (9/2,8,0.40)
      = (11/2,10,0.45)
      = (13/2,12,0.50)

one-particle transverse basis:
    normalized C45 two-dimensional HO modes
    in the committed phase convention

two-body qg basis:
    exact longitudinal fractions;
    x-weighted Jacobi/intrinsic and CM coordinates;
    finite many-body Nmax;
    CM-ground projection;
    retained total-color triplet

historical C47 embedding:
    immutable quadrature-derived diagnostic and numerical holdout;
    not exact support authority in C61
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All historical C47 canonical tuple values and attempted mass/transverse metadata remain diagnostic-only.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

A floating coefficient satisfying:

```text
abs(value) < 1e-12
```

is not an exact zero.

The C47 quadrature result may contain three scientifically different classes:

```text
QUADRATURE_NOISE_AROUND_AN_EXACT_ZERO

    The exact Talmi–Moshinsky coefficient is zero by a selection rule
    or exact algebraic cancellation.

GENUINE_SMALL_NONZERO_COEFFICIENT

    The exact coefficient is nonzero even though its magnitude is
    below the historical threshold.

UNRESOLVED_NUMERICAL_RESIDUE

    Available calculations do not prove either exact zero or
    certified nonzero.
```

C61 must classify every historical subthreshold residue.

A genuine small coefficient must remain in the embedding support regardless of magnitude.

An exact zero requires one of:

```text
an exact quantum-number selection rule;

an exact finite symbolic cancellation;

an exact algebraic-number identity;

or a theorem-backed zero of the analytic coefficient.
```

A high-precision floating value near zero is not an exact-zero proof.

A rigorous interval excluding zero may certify nonzero. An interval containing zero may not certify zero.

---

# 2. Exact purpose

C61 resolves only the raw-product-to-physical-\(qg\) embedding obstruction.

C61 must create:

```text
the exact C47 transverse-coordinate transformation in the project
convention;

an executable exact arithmetic representation of every finite-shell
two-dimensional Talmi–Moshinsky coefficient;

an exact or rigorously certified support classification for every
raw/intrinsic/CM coefficient;

a complete exact raw product -> intrinsic/CM transformation at every
physical longitudinal partition and resolution;

an exact CM-ground injection/projection;

an exact kinematic raw product <-> physical CM-ground qg embedding;

an exact combination with the read-only color-triplet isometry,
including basis permutations and phases;

an exact adjoint/inverse/isometry contract;

a certified high-precision numerical export for downstream sparse
linear algebra;

a full reconciliation of the 4,032 / 15,840 / 48,048 historical
subthreshold residues;

a dependency and supersession audit covering C47, C52, C53, C57,
C58, C59, and C60;

an immutable next-package import contract.
```

C61 must not construct:

```text
C60 absorption or emission endpoint relations;

a direct-contact witness relation;

a direct-contact numerator, denominator, normalization, or matrix;

a new canonical vertex;

a new self-induced-inertia contraction;

a physical counterterm coefficient;

a one-loop TMD or matching result.
```

The strongest no-impact status is:

```text
C61_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY
```

When that gate passes **and** no inherited support or matrix object requires rebuilding, the exact next package is:

> **C62/IFSUPPORT2 — rerun source-ordered direct-contact endpoint and witness support using the immutable exact C61 embedding**

If the exact embedding changes inherited support or numerical operators, follow the impact branches in Section 33 instead.

---

# 3. Scientific boundary

C61 is:

```text
embedding specific;
finite-shell exact-algebra specific;
longitudinal-partition resolved;
x-weighted TM/CM specific;
support-semantic;
CM-ground and triplet aware;
deterministic;
validation only.
```

C61 is not:

```text
a change of regulator trajectory;

a fit of quadrature tolerances;

a blanket declaration that all tiny entries are zero;

a dense replacement chosen for convenience;

a continuum HO completeness theorem;

a physical contact or Hamiltonian calculation.
```

The exact embedding may be sparse or dense. Density is a result, not a design target.

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_transverse_ho_validation.json
docs/next_level/c45_numerical_object_inventory.json

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
docs/next_level/c52_numerical_object_inventory.json
docs/next_level/c52_readiness_report.json

docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_canonical_support_validation.json
docs/next_level/c57_numerical_object_inventory.json
docs/next_level/c57_readiness_report.json

docs/next_level/c58_c57_import_report.json
docs/next_level/c58_c53_support_holdout.json
docs/next_level/c58_numerical_object_inventory.json
docs/next_level/c58_readiness_report.json

docs/next_level/c59_implementation_report.md
docs/next_level/c59_missing_calculation_specification.md

docs/next_level/c60_implementation_report.md
docs/next_level/c60_input_fidelity_audit.json
docs/next_level/c60_support_layer_contract.json
docs/next_level/c60_exact_zero_semantics.json
docs/next_level/c60_missing_calculation_specification.md
docs/next_level/c60_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c61_derivation_authority_manifest.json
docs/next_level/c61_input_fidelity_audit.json
```

---

# 5. Source and derivation authority

Reuse the source locks that established the C45/C47 BLFQ basis and x-weighted Jacobi coordinates.

Audit exact equation locators for:

```text
normalized two-dimensional HO modes;

single-particle shell convention;

x-weighted qg Jacobi and CM coordinates;

finite-shell Talmi–Moshinsky transformation;

CM-ground projection;

basis phases and Fourier convention.
```

The final exact coefficients may be a project derivation from these source-qualified definitions.

Classify inputs as:

```text
PRIMARY_BASIS_AUTHORITY;

PRIMARY_COORDINATE_TRANSFORM_AUTHORITY;

PROJECT_DERIVED_EXACT_TM_COEFFICIENT;

INDEPENDENT_ANALYTIC_CROSSCHECK;

HIGH_PRECISION_NUMERICAL_HOLDOUT;

HISTORICAL_QUADRATURE_DIAGNOSTIC_ONLY;

NOT_REGULATOR_OR_CONVENTION_IDENTICAL.
```

Do not require a paper to print the final project matrix.

If an exact formula, phase, scale, or coordinate map is missing, acquire and hash-lock the exact primary source needed to close that point.

Create:

```text
docs/next_level/c61_primary_source_manifest.json
docs/next_level/c61_source_role_matrix.json
docs/next_level/c61_source_sufficiency_matrix.json
```

---

# 6. Freeze construction and holdouts

Before deriving a coefficient, freeze:

```text
all longitudinal fractions as exact Fraction objects;

the raw single-particle q and g HO labels;

the intrinsic and CM HO labels;

the C45 polar-HO phase convention;

the C47 x-weighted coordinate transformation;

the many-body Nmax rule;

the CM-ground convention;

the raw product basis order;

the intrinsic/CM basis order;

the physical qg basis order;

the C53 triplet isometry and phase;

the historical C47 quadrature arrays and 1e-12 threshold as
diagnostic-only objects.
```

Freeze holdouts:

```text
the lowest nontrivial shell block;

the highest shell block at every resolution;

m = 0 and nonzero-m sectors;

positive and negative m;

one coefficient nonzero by a single term;

one coefficient nonzero by cancellation among several terms;

one exact zero by total-shell mismatch;

one exact zero by angular-momentum mismatch;

one exact zero by finite symbolic cancellation;

one genuine small nonzero coefficient, if one exists;

one historical subthreshold residue from each resolution;

one CM-ground row;

one CM-excited row;

one raw/physical round-trip state;

one triplet-phase holdout;

one adjacent-resolution map holdout.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c61_calculation_plan.json
docs/next_level/c61_holdout_plan.json
```

---

# 7. Exact longitudinal and scale identities

For every qg longitudinal partition, record exactly:

```text
K;

k_q and k_g;

x_q = k_q/K;

x_g = k_g/K;

x_q + x_g = 1;

the exact oscillator-scale parameters used by the raw modes;

the exact intrinsic scale;

the exact CM scale;

all dimensionless coordinate rescalings.
```

Use exact rationals for declared regulator decimals only when the committed input defines them as exact decimal parameters.

Do not reconstruct exact rational values from arbitrary binary floats.

Audit whether the transverse transformation is:

```text
an orthogonal rotation with coefficients generated by x_q and x_g;

a scaled symplectic transformation;

a biorthogonal map;

or another exact source-owned linear transformation.
```

Prove the metric preserved by the transformation.

Create:

```text
docs/next_level/c61_exact_longitudinal_fraction_manifest.json
docs/next_level/c61_oscillator_scale_contract.json
docs/next_level/c61_coordinate_transform_contract.json
docs/next_level/c61_coordinate_transform_validation.json
```

---

# 8. Select an exact coefficient representation

Compile mutually exclusive implementation plans.

## 8.1 `QGEMBED-CIRCULAR-LADDER-ALGEBRA`

Represent each polar 2D-HO state by exact circular-ladder occupations:

\[
n_+ = n+\max(m,0),
\qquad
n_- = n+\max(-m,0).
\]

Apply the exact two-mode coordinate rotation independently to the \(+\) and \(-\) ladder operators. Construct every coefficient as a finite sum of exact binomial/factorial factors and exact powers of the transformation entries.

## 8.2 `QGEMBED-CARTESIAN-FACTORIZE-AND-RECOUPLE`

Factor the 2D transformation into two exact one-dimensional HO brackets, then apply exact Cartesian-to-polar recoupling.

## 8.3 `QGEMBED-GENERATING-FUNCTION`

Use an exact finite generating-function coefficient extraction.

## 8.4 `QGEMBED-ALGEBRAIC-INTERVAL-HYBRID`

Use exact analytic selection rules and exact symbolic formulas where feasible, plus rigorous arbitrary-precision interval certification for coefficients whose exact algebraic simplification is computationally prohibitive.

This plan may certify nonzero with an interval excluding zero. It may not certify zero from an interval containing zero.

## 8.5 `QGEMBED-UNAVAILABLE`

No complete exact/certified representation can be constructed.

Select one primary construction route and one genuinely independent holdout route.

Do not use ordinary floating quadrature as the primary construction.

Create:

```text
docs/next_level/c61_exact_coefficient_plan.json
docs/next_level/c61_exact_coefficient_plan_decision.json
```

---

# 9. Exact polar-HO state encoding

Construct a bijective exact map among:

```text
polar labels (n,m);

circular-ladder occupations (n_plus,n_minus);

total transverse quanta;

angular momentum;

Cartesian labels where used.
```

Verify:

\[
n_+ + n_- = 2n+|m|,
\qquad
n_+ - n_- = m,
\]

or the exact sign convention committed by C45.

Retain:

```text
normalization;

phase;

Fourier transform phase;

creation/annihilation ordering;

basis order.
```

Create:

```text
docs/next_level/c61_polar_circular_basis_contract.json
docs/next_level/c61_polar_circular_basis_validation.json
```

---

# 10. Exact one-dimensional rotation coefficients

For each circular sector, derive the exact coefficient generated by the two-mode ladder transformation.

A coefficient may be represented schematically by a finite sum of the form

\[
\sum_r
(-1)^{\sigma(r)}
\binom{N_1}{r}
\binom{N_2}{N'_1-r}
c^{p(r)}
s^{q(r)}
\sqrt{
\frac{N'_1!N'_2!}{N_1!N_2!}
},
\]

but use the exact C47 transformation, signs, powers, and normalization.

Every expression must support:

```text
canonical serialization;

exact simplification;

free-symbol inventory;

exact substitution of x_q and x_g;

high-precision evaluation;

exact-zero test where algebraically decidable;

content hashing.
```

Create:

```text
docs/next_level/c61_one_dimensional_tm_formula.json
docs/next_level/c61_one_dimensional_tm_validation.json
```

---

# 11. Exact two-dimensional TM coefficient

Construct the complete polar-basis coefficient:

\[
\langle n_{\rm rel},m_{\rm rel};
        n_{\rm CM},m_{\rm CM}
|
n_q,m_q;
n_g,m_g
\rangle_x
\]

through the selected exact route.

Retain exact selection rules, including the source equivalents of:

```text
total transverse-quanta conservation;

total angular-momentum conservation;

shell and parity restrictions;

finite-basis membership;

longitudinal-partition identity.
```

Do not assume those rules are sufficient; exact algebraic cancellations may create additional zeros.

Each coefficient receives one terminal status:

```text
ZERO_BY_EXACT_QUANTUM_NUMBER_RULE;

ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION;

NONZERO_EXACT_ALGEBRAIC;

NONZERO_CERTIFIED_INTERVAL;

UNDECIDABLE_BLOCKING.
```

Create:

```text
docs/next_level/c61_exact_tm_coefficient_contract.json
docs/next_level/c61_exact_tm_coefficient_validation.json
```

A positive gate requires:

```text
UNDECIDABLE_BLOCKING = 0
```

over every coefficient needed by the physical trajectory.

---

# 12. Independent exact/analytic reconstruction

Implement a second route that does not call the primary coefficient generator.

Allowed independent routes include:

```text
Cartesian-factorized coefficient reconstruction;

generating-function coefficient extraction;

analytic low-shell coordinate-space integration;

analytic momentum-space integration;

high-precision interval quadrature as a non-authoritative holdout.
```

Compare exact expressions where both routes are symbolic.

For numerical holdouts, use sufficient precision and rigorous error bounds to distinguish:

```text
agreement with a nonzero exact coefficient;

quadrature noise around an exact zero;

or unresolved failure.
```

Create:

```text
docs/next_level/c61_independent_tm_reconstruction.json
docs/next_level/c61_high_precision_holdout_report.json
```

---

# 13. Finite-shell block construction

For each exact longitudinal partition and resolution, construct complete TM blocks between:

```text
the raw single-particle qg HO basis;

the intrinsic-plus-CM HO basis.
```

The block must preserve the complete finite total-quanta sector required by the C47 truncation.

Audit whether the raw and transformed finite subspaces are exactly equal.

Allowed statuses:

```text
FINITE_BLOCK_UNITARY;

FINITE_BLOCK_ISOMETRIC_WITH_EXPLICIT_COMPLEMENT;

NONNESTED_FINITE_BLOCK_WITH_EXPLICIT_REMAINDER;

FINITE_BLOCK_INCOMPLETE.
```

Required checks:

```text
shape;

rank and nullity;

exact row and column norms;

exact orthogonality;

exact inverse or adjoint relation;

total-shell block decomposition;

angular-momentum block decomposition;

basis-order independence.
```

Create:

```text
docs/next_level/c61_exact_tm_block_manifest.json
docs/next_level/c61_exact_tm_block_validation.json
```

---

# 14. Exact CM-ground projection

Define the exact CM-ground state from the committed C47 convention.

Construct:

```text
the CM-ground injection into intrinsic/CM space;

the CM-ground projector;

the exact raw-product embedding of every CM-ground intrinsic state;

the exact adjoint projection back to the physical kinematic basis.
```

Do not classify a CM-excited coefficient as zero merely because its quadrature value is small.

Required checks:

```text
projector Hermiticity and idempotence;

rank;

exact CM quantum numbers;

orthogonality to every retained CM-excited state;

raw/intrinsic/CM round trip;

Lawson/CM diagnostic compatibility.
```

Create:

```text
docs/next_level/c61_exact_cm_ground_projector.json
docs/next_level/c61_cm_ground_embedding_validation.json
```

---

# 15. Exact kinematic physical-qg embedding

Construct the exact kinematic embedding:

\[
J^{\rm kin}_{qg,R}:
\mathcal H^{\rm phys,kin}_{qg,R}
\longrightarrow
\mathcal H^{\rm raw,kin}_{qg,R}.
\]

Construct the exact adjoint/projection:

\[
P^{\rm kin}_{qg,R}.
\]

Retain:

```text
longitudinal partition;

quark and gluon helicities;

Jz;

raw single-particle transverse labels;

intrinsic and CM labels;

CM-ground identity;

basis order;

exact coefficient expression or certified interval.
```

Required checks:

```text
P J = I on the physical kinematic space;

J P equals the exact CM-ground image projector on the raw space;

Gram-metric compatibility;

rank and nullity;

basis-rotation covariance;

no thresholded sparsification.
```

Create:

```text
docs/next_level/c61_exact_kinematic_qg_embedding.json
docs/next_level/c61_kinematic_embedding_validation.json
```

---

# 16. Color-triplet combination

Import the C53/C47 \(24\times3\) triplet isometry read-only.

Construct the full physical embedding through the exact basis-order map.

When factorization is valid, prove the exact permutation-equivalent form:

\[
J^{\rm phys}_{qg,R}
\sim
J^{\rm kin}_{qg,R}
\otimes
U_3.
\]

Do not assume factorization before verifying:

```text
color/kinematic basis ordering;

triplet phase;

global-color projection;

CM/color independence;

zero-mode policy.
```

Required checks:

```text
exact or certified isometry;

triplet-image identity;

zero anti-sextet and 15 leakage;

basis-rotation covariance;

read-only triplet hash.
```

Create:

```text
docs/next_level/c61_exact_physical_qg_embedding.json
docs/next_level/c61_color_triplet_embedding_validation.json
```

---

# 17. Exact support semantics

Derive support solely from coefficient status.

A raw component belongs to the physical embedding support only when its exact/certified coefficient status is:

```text
NONZERO_EXACT_ALGEBRAIC
```

or:

```text
NONZERO_CERTIFIED_INTERVAL.
```

It does not belong when the status is one of the two exact-zero classes.

Never derive support from:

```text
abs(float_value) > threshold;

sparse-matrix storage after numeric pruning;

C53 nonzero values;

historical C47 masks.
```

Construct support records retaining:

```text
physical basis ID;

raw basis ID;

coefficient status;

exact expression hash;

interval certificate where used;

selection-rule ancestry;

CM and triplet ancestry.
```

Create:

```text
docs/next_level/c61_exact_embedding_support.json
docs/next_level/c61_exact_support_validation.json
```

---

# 18. Reconcile every historical subthreshold residue

Load the immutable C47 quadrature arrays.

For every historical nonzero residue below \(10^{-12}\), report:

```text
resolution;

raw and transformed basis IDs;

historical complex value;

historical threshold decision;

exact/certified coefficient status;

exact expression or zero proof;

high-precision numerical value;

quadrature discrepancy;

whether support changes;

which descendants consumed the old threshold decision.
```

Aggregate counts into:

```text
EXACT_ZERO_QUADRATURE_NOISE;

GENUINE_SMALL_NONZERO;

UNRESOLVED_BLOCKING;

DUPLICATE_OR_MISINDEXED;

BASIS_CONVENTION_MISMATCH.
```

The aggregate count must equal exactly:

```text
4,032 / 15,840 / 48,048
```

unless the C60 manifest proves a more refined partition. Any mismatch must be resolved, not ignored.

Create:

```text
docs/next_level/c61_c47_subthreshold_residue_ledger.json
docs/next_level/c61_c47_residue_reconciliation_report.json
```

---

# 19. Certified numerical export

Downstream sparse and matrix-free code may consume numerical arrays, but those arrays must descend from the exact/certified coefficient objects.

For each coefficient export:

```text
exact-expression hash;

working precision;

rounded complex value;

rigorous absolute error bound;

exact support status.
```

The support mask must be serialized independently of numerical magnitude.

Run convergence at multiple arbitrary precisions.

Required checks:

```text
rounding stability;

support stability;

exact-zero export as literal zero only after proof;

nonzero interval excludes zero;

matrix isometry residual compatible with the stored error bounds;

no threshold pruning.
```

Create:

```text
docs/next_level/c61_certified_numerical_export.json
docs/next_level/c61_precision_stability_report.json
```

---

# 20. Historical C47 quadrature comparison

The C47 quadrature route remains a numerical holdout.

Compare:

```text
exact/certified coefficients;

historical quadrature coefficients;

independent high-precision quadrature.
```

Separate:

```text
quadrature truncation;

quadrature roundoff;

basis-phase mismatch;

basis-order mismatch;

scale mismatch;

genuine implementation discrepancy.
```

Do not refit a threshold to make the maps agree.

Create:

```text
docs/next_level/c61_historical_quadrature_comparison.json
```

---

# 21. Descendant dependency and supersession audit

Trace every descendant use of:

```text
C47 floating embedding coefficients;

C47 thresholded embedding support;

C57 1e-12 support decisions;

C58 conditional support;

C52/C53 numerical matrices and support ancestry;

C59/C60 preflight support logic.
```

For every affected artifact classify:

```text
UNCHANGED_EXACTLY;

NUMERICAL_VALUES_UNCHANGED_SUPPORT_SEMANTICS_CORRECTED;

SUPPORT_REBUILD_REQUIRED;

NUMERICAL_OPERATOR_REBUILD_REQUIRED;

STATUS_SUPERSESSION_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

At minimum audit:

```text
C47 physical qg basis identities;

C52 colorless primitive matrices;

C53 physical canonical vertex and support ancestry;

C57 corresponding-propagating regulator;

C58 self-induced-inertia mode support and q-sector primitive;

C59 direct-contact preflight;

C60 failed support audit.
```

Historical artifacts remain byte-identical. Any correction is a descendant supersession, not an edit of historical outputs.

Create:

```text
docs/next_level/c61_descendant_dependency_graph.json
docs/next_level/c61_inherited_support_impact_report.json
docs/next_level/c61_supersession_plan.json
```

---

# 22. C52/C53 numerical holdout audit

Do not rebuild C52 or C53 in C61.

Use the exact embedding to reconstruct a frozen set of their basis-projection holdouts without consuming their stored numerical entries as construction inputs.

Determine whether:

```text
the exact map reproduces C52/C53 values within certified quadrature
and rounding errors;

their numerical values remain valid but support ancestry requires
supersession;

or their numerical operators require rebuilding.
```

Poison C52/C53 stored values during construction.

Create:

```text
docs/next_level/c61_c52_c53_embedding_impact_audit.json
```

---

# 23. C57/C58 support-impact audit

Reconstruct the source-owned canonical reachability support using the exact embedding and the existing source selection rules.

Compare with the C57 support counts and identities.

Determine whether the exact embedding changes:

```text
the 312 / 510 / 756 canonical support positions;

the 1,216 / 2,320 / 3,936 conditional unions;

the 2,304 / 4,400 / 7,488 candidate envelopes;

the C58 ordered-joint supports;

the 4,216 / 8,330 / 14,484 C58 admitted contraction modes;

the C58 q-sector primitive.
```

Do not preserve those numbers by threshold tuning.

Create:

```text
docs/next_level/c61_c57_c58_support_impact_audit.json
```

---

# 24. Exact embedding API

Create APIs equivalent to:

```python
exact_tm_coefficient(
    raw_q_mode_id,
    raw_g_mode_id,
    intrinsic_mode_id,
    cm_mode_id,
    longitudinal_partition_id,
) -> ExactTMCoefficient

physical_qg_raw_components(
    physical_qg_basis_id,
    resolution,
) -> tuple[ExactEmbeddingComponent, ...]

project_raw_qg_to_physical(
    raw_vector,
    resolution,
    precision=None,
)

embed_physical_qg_to_raw(
    physical_vector,
    resolution,
    precision=None,
)
```

Return objects must expose:

```text
exact status;

exact expression hash;

selection-rule proof;

certified numerical value and error;

basis ancestry;

CM and triplet ancestry.
```

Do not expose a threshold argument that changes exact support.

Create:

```text
docs/next_level/c61_api_contract.json
docs/next_level/c61_api_validation.json
```

---

# 25. Physical-resolution comparison

Construct typed comparison maps for the exact embeddings at adjacent resolutions.

Because \(K\), \(N_{\max}\), and \(b_{\rm HO}\) all change, do not claim literal inclusion.

Compare:

\[
R_{\rm raw}\,
J^{\rm phys}_{R'}
\,P_{\rm phys}
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

triplet-basis change;

certified numerical rounding;

support change.
```

Create:

```text
docs/next_level/c61_embedding_comparison_maps.json
docs/next_level/c61_embedding_comparison_report.json
docs/next_level/c61_comparison_remainder_ledger.json
```

---

# 26. Count-once and provenance

Every exact coefficient and embedding support entry must have one ancestry path.

Report:

```text
candidate raw/transformed coefficient count;

exact-zero-by-rule count;

exact-zero-by-cancellation count;

exact nonzero count;

interval-certified nonzero count;

undecidable count;

duplicate coefficient count;

missing coefficient count;

physical support-entry count;

CM-ground entry count;

triplet-combined entry count.
```

A positive gate requires:

```text
undecidable = 0;

duplicate = 0;

missing = 0.
```

Create:

```text
docs/next_level/c61_coefficient_ancestry_ledger.json
docs/next_level/c61_count_once_report.json
```

---

# 27. Isolation and poisoning controls

Prove that C61 is unchanged when:

```text
all C40 arrays are poisoned;

all C47 quadrature values are poisoned after their basis IDs and
historical holdout roles are loaded;

the historical 1e-12 threshold is changed;

all C47 canonical tuple values and metadata are poisoned;

all C50 combined values are poisoned;

all C52/C53 numerical matrix values are poisoned;

all C57/C58 numerical operator values are poisoned;

ART25 files are inaccessible.
```

The build must fail when:

```text
the C45 HO phase changes;

the C47 coordinate transformation changes;

an exact longitudinal fraction is replaced by binary-float inference;

the oscillator-scale contract changes;

the polar/circular map changes;

the many-body Nmax rule changes;

the CM-ground convention changes;

the triplet isometry changes;

an exact nonzero is removed by threshold;

an exact zero is declared from a numerical tolerance;

the selected exact-coefficient plan changes without supersession.
```

Create:

```text
docs/next_level/c61_isolation_report.json
```

---

# 28. Runtime bundles

For every resolution produce content-addressed bundles containing:

```text
exact longitudinal-partition records;

exact coordinate-transform records;

exact coefficient-expression records;

exact support masks;

certified numerical TM blocks;

CM-ground injection/projection;

kinematic physical-qg embedding;

full triplet physical-qg embedding;

residue-reconciliation ledgers;

descendant-impact records;

comparison-map blocks.
```

Heavy exact-expression tables and numerical arrays may remain outside Git under:

```text
data/runtime/c61_ifqgembed/
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

support hash;

expression hash;

array hash;

generator command.
```

Create:

```text
docs/next_level/c61_numerical_object_inventory.json
```

All JSON, exact expressions, and numerical arrays must regenerate byte-for-byte.

---

# 29. End-to-end source-to-embedding test

Implement an end-to-end test that begins from the C45/C47 source contracts—not from prebuilt C61 arrays.

It must:

```text
load exact fractions and scales;

derive the exact coordinate transform;

construct the polar/circular basis map;

derive one-dimensional rotation coefficients;

derive two-dimensional TM coefficients;

classify exact zeros and nonzeros;

construct complete finite-shell blocks;

construct the CM-ground projector;

construct kinematic and triplet physical embeddings;

export certified numerical arrays;

reconcile every C47 subthreshold residue;

run C52/C53 and C57/C58 impact audits;

run exact isometry, holdout, comparison, count-once, and poisoning tests;

reproduce every hash.
```

It must fail when:

```text
ordinary floating quadrature is used as primary authority;

abs(value) < threshold defines an exact zero;

a genuine small nonzero is pruned;

an interval containing zero is labeled exact zero;

a binary float is guessed to be a rational source value;

one-particle and many-body shell rules are conflated;

a CM-excited component is silently deleted;

the color-triplet map is rederived with a different phase;

historical descendants are declared unchanged without the impact audit;

a runtime hash changes.
```

---

# 30. Focused mutation tests

Create at least **256 focused live mutations** of actual coordinate, coefficient, support, embedding, or impact objects.

Include mutations of:

```text
x_q or x_g;

coordinate-transform sign;

oscillator scale;

polar/circular occupation map;

factorial normalization;

binomial summation bound;

rotation power;

phase;

total-shell rule;

angular-momentum rule;

exact-cancellation term;

coefficient status;

interval bound;

historical residue classification;

CM-ground label;

CM projector;

raw basis order;

physical basis order;

triplet isometry;

support entry;

certified numerical value;

error bound;

descendant-impact status;

comparison map;

expression hash;

runtime-array hash.
```

Every mutation must fail a concrete source, algebra, exact-zero, isometry, support, CM, triplet, certification, impact, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 31. Readiness gate

Issue:

```text
C61_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY
```

only when:

```text
the full C60 baseline reproduces;

the C60 no-go remains explicit;

the C58 package remains read-only;

the exact coordinate and scale contracts are complete;

one exact/certified coefficient plan is selected;

the polar/circular basis map closes;

the exact one-dimensional formulas close;

the exact two-dimensional TM coefficients close;

every required coefficient has an exact-zero or certified-nonzero
status;

no coefficient remains undecidable;

the independent reconstruction agrees;

finite-shell blocks have complete rank/isometry statuses;

the exact CM-ground projector closes;

the exact kinematic embedding closes;

the exact triplet physical embedding closes;

support is derived without numerical thresholds;

all 4,032 / 15,840 / 48,048 historical subthreshold residues are
reconciled;

the certified numerical export is stable;

the historical quadrature comparison is explained;

the descendant dependency and supersession audit is complete;

C52/C53 and C57/C58 impact is fully typed;

count-once and provenance close;

comparison maps execute;

poisoning controls pass;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-embedding test passes.
```

Do not issue:

```text
C61_IFERM_CONTACT_SUPPORT_READY;

C61_DIRECT_IFERM_CONTACT_READY;

C61_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C61_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C61_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 32. Exact next-package decision

After the exact embedding closes, select exactly one continuation.

## 32.1 No inherited support or value impact

Conditions:

```text
all historical subthreshold residues are exact zeros
or genuine small nonzeros already retained in every numerical operator;

C52/C53 numerical values and support ancestry remain valid;

C57/C58 support identities and mode counts remain valid.
```

Next:

> **C62/IFSUPPORT2 — rerun direct-contact endpoint and witness support using C61**

## 32.2 C57/C58 support impact, but C52/C53 values remain valid

Conditions:

```text
the exact embedding changes canonical reachability or conditional
support used by C57/C58;

the physical canonical vertex numerical values do not require rebuild.
```

Status:

```text
C61_EXACT_QG_EMBEDDING_READY_IFREG_SUPERSESSION_REQUIRED
```

Next:

> **C62/IFREG3 — rebuild the corresponding-propagating regulator and self-induced-inertia support from the exact embedding**

## 32.3 C52/C53 physical-vertex numerical or support ancestry impact

Status:

```text
C61_EXACT_QG_EMBEDDING_READY_VERTEX_SUPERSESSION_REQUIRED
```

Next:

> **C62/VERTEX4 — rebuild the colorless and physical canonical vertex from the exact embedding before downstream instantaneous work**

## 32.4 Impact unresolved

Status:

```text
C61_QG_EMBEDDING_DESCENDANT_IMPACT_INCOMPLETE
```

Next:

> **C62/QGIMPACT — complete the descendant dependency and numerical/support impact audit**

Do not proceed directly to C60 support reconstruction when an inherited support or operator object requires supersession.

---

# 33. Exact no-go branches

## A. Coordinate or scale convention remains incomplete

```text
C61_QG_COORDINATE_SCALE_CONTRACT_INCOMPLETE
```

Next:

> **C62/QGCOORD — exact x-weighted coordinate, oscillator-scale, and phase completion**

## B. Exact TM formula remains incomplete

```text
C61_EXACT_TM_ALGEBRA_INCOMPLETE
```

Next:

> **C62/QGTM — circular-ladder, Cartesian, or generating-function coefficient completion**

## C. Some coefficient statuses remain undecidable

```text
C61_EXACT_SUPPORT_CLASSIFICATION_INCOMPLETE
```

Next:

> **C62/QGCERT — exact selection-rule and rigorous interval certification completion**

## D. CM-ground or physical embedding remains incomplete

```text
C61_QG_CM_PHYSICAL_EMBEDDING_INCOMPLETE
```

Next:

> **C62/QGCM — exact CM-ground, raw/physical, and triplet embedding completion**

## E. Historical residues cannot be reconciled

```text
C61_C47_RESIDUE_RECONCILIATION_INCOMPLETE
```

Next:

> **C62/QGRESIDUE — basis-order, phase, scale, and quadrature-residue reconciliation**

## F. Exact and certified numerical routes disagree

```text
C61_QG_EMBEDDING_NUMERICAL_CERTIFICATION_FAILED
```

Next:

> **C62/QGNUM — high-precision export, interval bounds, and independent reconstruction closure**

## G. Exact embedding closes

Use one of the continuation statuses in Section 32.

---

# 34. Required deliverables

Create at least:

```text
docs/next_level/c61_implementation_report.md
docs/next_level/c61_api.md
docs/next_level/c61_derivation_authority_manifest.json
docs/next_level/c61_input_fidelity_audit.json

docs/next_level/c61_primary_source_manifest.json
docs/next_level/c61_source_role_matrix.json
docs/next_level/c61_source_sufficiency_matrix.json
docs/next_level/c61_calculation_plan.json
docs/next_level/c61_holdout_plan.json

docs/next_level/c61_exact_longitudinal_fraction_manifest.json
docs/next_level/c61_oscillator_scale_contract.json
docs/next_level/c61_coordinate_transform_contract.json
docs/next_level/c61_coordinate_transform_validation.json

docs/next_level/c61_exact_coefficient_plan.json
docs/next_level/c61_exact_coefficient_plan_decision.json
docs/next_level/c61_polar_circular_basis_contract.json
docs/next_level/c61_polar_circular_basis_validation.json
docs/next_level/c61_one_dimensional_tm_formula.json
docs/next_level/c61_one_dimensional_tm_validation.json
docs/next_level/c61_exact_tm_coefficient_contract.json
docs/next_level/c61_exact_tm_coefficient_validation.json
docs/next_level/c61_independent_tm_reconstruction.json
docs/next_level/c61_high_precision_holdout_report.json

docs/next_level/c61_exact_tm_block_manifest.json
docs/next_level/c61_exact_tm_block_validation.json
docs/next_level/c61_exact_cm_ground_projector.json
docs/next_level/c61_cm_ground_embedding_validation.json
docs/next_level/c61_exact_kinematic_qg_embedding.json
docs/next_level/c61_kinematic_embedding_validation.json
docs/next_level/c61_exact_physical_qg_embedding.json
docs/next_level/c61_color_triplet_embedding_validation.json

docs/next_level/c61_exact_embedding_support.json
docs/next_level/c61_exact_support_validation.json
docs/next_level/c61_c47_subthreshold_residue_ledger.json
docs/next_level/c61_c47_residue_reconciliation_report.json
docs/next_level/c61_certified_numerical_export.json
docs/next_level/c61_precision_stability_report.json
docs/next_level/c61_historical_quadrature_comparison.json

docs/next_level/c61_descendant_dependency_graph.json
docs/next_level/c61_inherited_support_impact_report.json
docs/next_level/c61_supersession_plan.json
docs/next_level/c61_c52_c53_embedding_impact_audit.json
docs/next_level/c61_c57_c58_support_impact_audit.json

docs/next_level/c61_api_contract.json
docs/next_level/c61_api_validation.json
docs/next_level/c61_embedding_comparison_maps.json
docs/next_level/c61_embedding_comparison_report.json
docs/next_level/c61_comparison_remainder_ledger.json

docs/next_level/c61_coefficient_ancestry_ledger.json
docs/next_level/c61_count_once_report.json
docs/next_level/c61_isolation_report.json

docs/next_level/c61_numerical_object_inventory.json
docs/next_level/c61_readiness_report.json
docs/next_level/c61_source_sufficiency_decision.json
docs/next_level/c61_no_go_decision_tree.json
docs/next_level/c61_missing_calculation_specification.md
docs/next_level/c61_regression_report.json
```

Create the appropriate immutable next-package import contract after the impact decision:

```text
docs/next_level/c61_c62_ifsupport2_import_contract.json

or

docs/next_level/c61_c62_ifreg3_import_contract.json

or

docs/next_level/c61_c62_vertex4_import_contract.json.
```

Add source code under:

```text
src/deuteron_wigner/bridge/ifqgembed/
```

or the repository-equivalent package.

Add focused tests for:

```text
exact fractions and scales;
coordinate transform;
polar/circular encoding;
one-dimensional coefficients;
two-dimensional TM coefficients;
exact-zero and certified-nonzero semantics;
independent reconstruction;
finite-shell blocks;
CM-ground projector;
kinematic and triplet embeddings;
subthreshold-residue reconciliation;
certified numerical export;
descendant-impact audit;
count once;
poisoning isolation;
comparison maps;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON, exact expressions, and runtime arrays must reproduce byte-for-byte.

---

# 35. Acceptance criteria

C61 is complete only when:

1. The full C60 baseline reproduces.
2. The C60 no-go remains explicit.
3. C58 remains read-only.
4. C43/C45/C47 historical files remain unchanged.
5. C40 remains method-oracle only.
6. Historical C47 tuple values remain diagnostic-only.
7. C47 quadrature values are not exact support authority.
8. The historical \(10^{-12}\) threshold cannot change exact support.
9. No physical coupling or counterterm coefficient is chosen.
10. No direct-contact value or matrix is evaluated.
11. Longitudinal fractions are exact.
12. Oscillator scales and coordinate maps are source qualified.
13. The metric preserved by the coordinate transform is proved.
14. One exact/certified coefficient plan is selected.
15. The polar/circular basis map is bijective.
16. Ladder and phase conventions are explicit.
17. One-dimensional coefficients are exact.
18. Two-dimensional coefficients are exact or rigorously certified.
19. Every coefficient has one terminal status.
20. No interval containing zero is labeled exact zero.
21. No tiny exact nonzero is pruned.
22. No coefficient remains undecidable.
23. The independent reconstruction agrees.
24. Finite-shell block rank/isometry is complete.
25. Raw and transformed basis orders are explicit.
26. The exact CM-ground projector is Hermitian and idempotent.
27. CM-excited components are not removed by threshold.
28. The kinematic physical embedding closes.
29. The triplet physical embedding closes.
30. No nontriplet leakage is hidden.
31. Exact support descends from coefficient status only.
32. All 4,032 / 15,840 / 48,048 historical residues are classified.
33. Aggregate residue counts close.
34. Genuine small nonzeros remain visible.
35. Certified numerical exports carry error bounds.
36. Exact zeros are exported as zero only after proof.
37. Precision changes do not alter support.
38. Historical quadrature discrepancies are separated by cause.
39. Descendant dependency tracing is complete.
40. C52/C53 numerical and support impact is typed.
41. C57/C58 support and mode-count impact is typed.
42. Historical artifacts are superseded only through descendant records.
43. No downstream status is preserved by threshold tuning.
44. Exact embedding APIs expose no support-changing tolerance.
45. Comparison maps retain all nonnested and scale remainders.
46. Duplicate, missing, and undecidable counts are zero.
47. Static and runtime poisoning controls pass.
48. Runtime bundles contain exact expressions, support certificates, and numerical arrays.
49. End-to-end reconstruction passes.
50. At least 256 focused live mutations are detected.
51. The exact next branch follows the inherited-impact decision.
52. No endpoint relation, witness relation, contact support, contact matrix, complete instantaneous operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
53. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
54. `MSHT20_REP/` remains untouched and outside Git.
55. The working tree is clean except for the pre-existing untracked directory.
56. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken exact-zero semantics, algebraic coefficient construction, CM projection, support certification, or descendant-impact accounting to open the gate.

---

# 36. Final Codex response

Report:

- full starting and final commits;
- exact source hierarchy and role classifications;
- exact longitudinal fractions and oscillator-scale decisions;
- coordinate-transform matrix, preserved metric, and residuals;
- selected exact-coefficient plan and independent route;
- polar/circular basis identities;
- one-dimensional and two-dimensional coefficient formulas;
- coefficient counts by exact-zero, exact-nonzero, interval-nonzero, and undecidable status;
- finite-shell block shapes, ranks, nullities, and exact/certified isometry residuals;
- CM-ground projector shape, rank, and exact residuals;
- kinematic and full triplet embedding shapes, ranks, nullities, and round-trip residuals;
- exact support counts;
- complete classification of the 4,032 / 15,840 / 48,048 historical subthreshold residues;
- counts of exact quadrature-noise zeros and genuine small nonzeros;
- certified numerical precisions and error bounds;
- historical quadrature discrepancy categories;
- C52/C53 impact status;
- C57/C58 support and mode-count impact status;
- supersession decisions;
- comparison-map residuals and separated remainders;
- ancestry, duplicate, missing, and undecidable counts;
- isolation and poisoning results;
- runtime expression, support, and array hashes;
- focused mutation results;
- exact readiness/no-go and inherited-impact status;
- exact next branch;
- confirmation that no endpoint/witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe thresholded quadrature support, a high-precision near-zero, an interval containing zero, a pruned exact nonzero, an unproved CM projection, or an unaudited descendant dependency as the exact physical \(qg\) embedding.
