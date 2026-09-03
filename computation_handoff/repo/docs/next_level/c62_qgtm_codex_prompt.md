# C62/QGTM Codex Work Package

## Title

**Exact two-dimensional harmonic-oscillator and Talmi–Moshinsky algebra: source-locked polar/circular phases, exact Cartesian recoupling, \(x\)-weighted ladder rotations, finite-shell coefficient blocks, and threshold-free zero semantics**

## Authoritative baseline

Start from the clean local C61/IFQGEMBED fail-closed completion commit:

```text
c22c6ab04e79a591aacc5679efd2b0642c3ad4e8
```

Its immediate scientific parent is:

```text
0d74c218e304a9bdb9c13eaaaf8b0abdab2531f6
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 0d74c218e304a9bdb9c13eaaaf8b0abdab2531f6 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C60_IFSUPPORT_QG_EMBEDDING_INCOMPLETE

C61_EXACT_TM_ALGEBRA_INCOMPLETE
```

and the exact C61 scientific result:

```text
the circular-ladder route is viable in principle;

longitudinal fractions are exact and the two-mode rotation may use
    c = sqrt(x_q),
    s = sqrt(x_g);

the inherited C47 polar_to_cart_shell routine is not exact authority;

C47 polar_to_cart_shell:
    evaluates amplitudes through Gauss–Hermite quadrature;
    fixes each row phase through numerical argmax alignment;

there is no source-locked C45 polar-to-circular phase and basis
permutation contract;

forbidden correction:
    fitting an algebraic bracket to the C47 quadrature phases;

not performed:
    no residue classification;
    no exact TM block;
    no exact qg embedding;
    no downstream support or supersession decision.
```

Verify every statement from the committed C61 records rather than relying on this prompt.

The fixed architecture remains:

```text
longitudinal cell:
    -L <= x^- <= L
    p^+ = pi k/L
    P^+ = pi K/L

physical trajectory:
    (K,Nmax,bHO/GeV)
      = (9/2,8,0.40)
      = (11/2,10,0.45)
      = (13/2,12,0.50)

one-particle transverse basis:
    normalized two-dimensional isotropic HO modes
    in the exact C45 coordinate and momentum conventions

two-body transverse variables:
    exact C47 x-weighted qg relative and CM coordinates

historical C47 maps:
    immutable numerical diagnostics only
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All historical C47 canonical tuples, quadrature-derived polar/Cartesian phases, and thresholded support masks remain diagnostic-only.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C61 identified two distinct missing objects:

```text
1. a source-owned phase and permutation map between the C45 polar
   two-dimensional HO states and an exact circular or Cartesian
   oscillator representation;

2. an exact finite-shell two-particle Talmi–Moshinsky coefficient
   generator in that convention.
```

The first object must be established before the second.

A row-by-row phase chosen from:

```text
argmax(abs(quadrature_row))
```

is not a basis convention. It can change under:

```text
quadrature order;
roundoff;
near-degenerate maxima;
basis ordering;
an exact zero becoming numerical noise;
or a small perturbation of the sampled grid.
```

C62 must derive one global analytic convention from the source-qualified C45 wavefunctions and ladder algebra.

The exact convention may contain state-dependent closed-form phases such as powers of \(i\) or \((-1)\), but those phases must follow from one formula. They may not be independently fitted for each row.

C62 must also distinguish:

```text
basis phase;

basis permutation;

coordinate rotation;

Fourier-transform phase;

Talmi–Moshinsky coefficient;

and historical numerical alignment.
```

These are separate maps.

---

# 2. Exact purpose

C62 resolves only the exact HO/TM algebra obstruction.

C62 must produce:

```text
a source-locked analytic C45 polar-HO wavefunction convention;

an exact circular-ladder convention;

an exact polar <-> circular state map;

an exact circular <-> Cartesian state map;

a source-owned basis permutation and phase map for every finite shell;

the exact x-weighted two-mode creation-operator rotation;

an exact one-dimensional normalized two-mode bracket;

an exact two-dimensional polar Talmi–Moshinsky coefficient;

complete exact finite-shell TM blocks for every required
longitudinal partition and physical resolution;

threshold-free exact-zero and exact-nonzero classifications;

an independent exact or analytic reconstruction;

a comparison with the historical quadrature route after, and only
after, the exact convention is fixed;

a coefficient-level reconciliation of the historical subthreshold
TM residues;

an immutable C63/QGEMBED2 import contract.
```

C62 must not construct:

```text
the final CM-ground physical qg embedding;

the color-triplet-combined physical embedding;

C60 absorption or emission endpoint relations;

a direct-contact witness relation;

a contact value or matrix;

a descendant supersession decision beyond a provisional impact
classification.
```

The strongest allowed status is:

```text
C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY
```

When that gate passes, the exact next package is:

> **C63/QGEMBED2 — construct the exact CM-ground and triplet physical \(qg\) embedding, reconcile all descendant support and numerical impacts, and select the required supersession branch**

---

# 3. Scientific boundary

C62 is:

```text
two-dimensional isotropic-HO specific;
finite-shell exact algebra;
longitudinal-partition resolved;
x-weighted coordinate-transform specific;
phase and permutation explicit;
threshold free;
deterministic;
validation only.
```

C62 is not:

```text
a numerical fit to C47;
a quadrature phase calibration;
a change of C45 or C47 basis definitions;
a continuum completeness claim;
a physical Hamiltonian or contact calculation;
a downstream support promotion.
```

The exact TM coefficient may be zero or nonzero independently of whether its historical floating value was small.

---

# 4. Mandatory inputs

Read completely:

```text
docs/next_level/c43_light_front_conventions.json

docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_transverse_ho_validation.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_numerical_object_inventory.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_qg_tm_validation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c60_implementation_report.md
docs/next_level/c60_exact_zero_semantics.json
docs/next_level/c60_missing_calculation_specification.md

docs/next_level/c61_implementation_report.md
docs/next_level/c61_input_fidelity_audit.json
docs/next_level/c61_exact_longitudinal_fraction_manifest.json
docs/next_level/c61_oscillator_scale_contract.json
docs/next_level/c61_coordinate_transform_contract.json
docs/next_level/c61_exact_coefficient_plan.json
docs/next_level/c61_exact_coefficient_plan_decision.json
docs/next_level/c61_missing_calculation_specification.md
docs/next_level/c61_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c62_derivation_authority_manifest.json
docs/next_level/c62_input_fidelity_audit.json
```

---

# 5. Source hierarchy

Reuse the locked C45/C47 BLFQ and light-front-basis sources at their exact scopes.

Audit exact equation locators for:

```text
the coordinate-space 2D HO mode;

the momentum-space 2D HO mode;

normalization;

associated-Laguerre convention;

angular factor exp(+i m phi) or exp(-i m phi);

any explicit (-1)^n or i^N factor;

the Fourier-transform convention;

the one-particle shell definition;

the x-weighted relative/CM coordinate transformation.
```

If the existing source chain does not explicitly fix the polar-state phase, acquire and hash-lock the exact primary source or derive the phase from a source-qualified wavefunction plus source-qualified ladder definitions.

The final phase may be a project derivation. Its inputs must be source qualified.

Classify sources and derivations as:

```text
PRIMARY_POLAR_HO_AUTHORITY;

PRIMARY_LADDER_OPERATOR_AUTHORITY;

PRIMARY_X_WEIGHTED_COORDINATE_AUTHORITY;

PROJECT_DERIVED_POLAR_CIRCULAR_PHASE;

PROJECT_DERIVED_EXACT_TM_BRACKET;

INDEPENDENT_EXACT_RECONSTRUCTION;

HISTORICAL_QUADRATURE_HOLDOUT_ONLY;

NOT_CONVENTION_IDENTICAL.
```

Create:

```text
docs/next_level/c62_primary_source_manifest.json
docs/next_level/c62_source_role_matrix.json
docs/next_level/c62_source_sufficiency_matrix.json
```

---

# 6. Freeze conventions and holdouts

Before deriving a phase, freeze:

```text
metric and transverse-coordinate convention;

coordinate-space Fourier sign;

momentum-space Fourier sign;

dimensionless HO coordinate;

oscillator scale;

polar angular factor;

Laguerre-polynomial convention;

Cartesian creation operators;

circular creation operators;

L_z sign;

vacuum phase;

raw basis order;

relative/CM basis order;

longitudinal fractions;

the C47 coordinate-rotation orientation.
```

Freeze holdouts before construction:

```text
|n=0,m=0>;

|n=0,m=+1>;

|n=0,m=-1>;

|n=1,m=0>;

the complete N=2 shell;

one positive-m and one negative-m high-shell state;

one Cartesian state with multiple circular components;

one coefficient nonzero by a single binomial term;

one coefficient nonzero by multi-term cancellation;

one exact zero by shell mismatch;

one exact zero by m conservation;

one exact zero by algebraic cancellation beyond obvious rules;

one historical row whose argmax index changes under a tiny numerical
perturbation, if such a row exists;

one subthreshold historical TM residue from every resolution;

one highest-shell TM block per physical resolution.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c62_calculation_plan.json
docs/next_level/c62_holdout_plan.json
```

---

# 7. Select the exact representation

Compile mutually exclusive plans.

## 7.1 `QGTM-CIRCULAR-LADDER-PRIMARY`

Use exact circular ladder occupations for both the one-particle polar states and the two-particle relative/CM transformation.

## 7.2 `QGTM-CARTESIAN-PRIMARY`

Use exact Cartesian HO states, exact one-dimensional two-mode brackets in \(x\) and \(y\), and an exact polar/Cartesian recoupling.

## 7.3 `QGTM-GENERATING-FUNCTION-PRIMARY`

Extract exact coefficients from a finite generating function.

## 7.4 `QGTM-EXACT-HYBRID`

Use one exact route for construction and a second exact route for blocks too large for a single representation, with a proved adapter and no numerical phase fitting.

## 7.5 `QGTM-UNAVAILABLE`

No source-owned phase or exact coefficient chain can be completed.

Select one primary route and one independent route.

The preferred route may be circular-ladder algebra, but the decision must follow the actual C45/C47 conventions.

Create:

```text
docs/next_level/c62_exact_representation_plan.json
docs/next_level/c62_exact_representation_decision.json
```

---

# 8. Exact C45 polar wavefunction contract

Transcribe the exact normalized polar 2D-HO wavefunction:

\[
\Phi_{n m}(\rho,\phi)
=
\mathcal N_{n m}
\,\rho^{|m|}
\,e^{-\rho^2/2}
\,L_n^{|m|}(\rho^2)
\,e^{i\,\sigma_m m\phi}
\times
e^{i\varphi_{n m}},
\]

where every sign and phase symbol must be replaced by the actual C45 convention.

Record separately:

```text
radial normalization;

angular convention;

state phase;

coordinate-space expression;

momentum-space expression;

Fourier phase;

oscillator scale;

basis-order ID.
```

Required checks:

```text
normalization;

orthogonality;

L_z eigenvalue;

ground-state positivity or declared phase;

radial-node convention;

coordinate/momentum Fourier relation;

creation/annihilation recurrence.
```

Create:

```text
docs/next_level/c62_polar_ho_wavefunction_contract.json
docs/next_level/c62_polar_ho_wavefunction_validation.json
```

---

# 9. Exact circular-ladder convention

Define exact circular operators from the Cartesian operators.

Do not hard-code:

\[
a_\pm^\dagger
=
\frac{a_x^\dagger \mp i a_y^\dagger}{\sqrt2}
\]

until the sign is derived from the committed \(L_z\) and Fourier conventions.

Record:

```text
a_plus and a_minus definitions;

commutators;

L_z in number-operator form;

vacuum convention;

occupation ordering;

state normalization;

complex-conjugation rule.
```

For each polar state define exact occupations satisfying the committed equivalents of:

\[
n_+ + n_- = 2n+|m|,
\qquad
n_+ - n_- = m.
\]

Allowed status:

```text
POLAR_TO_CIRCULAR_BIJECTION_VALIDATED;

POLAR_TO_CIRCULAR_SIGN_ADAPTER_REQUIRED;

POLAR_TO_CIRCULAR_INCOMPLETE.
```

Create:

```text
docs/next_level/c62_circular_ladder_contract.json
docs/next_level/c62_circular_ladder_validation.json
```

---

# 10. Derive the polar-to-circular phase

Define:

\[
|n,m\rangle_{\rm polar}
=
e^{i\phi_{n,m}}
\,
|n_+(n,m),n_-(n,m)\rangle_{\rm circ}.
\]

Derive \(e^{i\phi_{n,m}}\) from the analytic C45 wavefunction and the circular-ladder coordinate representation.

The result must be one closed formula or one deterministic recurrence with a source-owned base state.

The following are forbidden:

```text
row-by-row argmax alignment;

least-squares phase fitting;

using C47 quadrature signs;

choosing phases to maximize agreement with historical arrays;

fixing each degenerate shell independently without a global rule.
```

Required checks:

```text
exact equality of analytic wavefunctions;

L_z eigenvalue;

radial raising recurrence;

complex conjugation m <-> -m;

Fourier-transform phase;

shellwise unitarity;

global phase consistency across shells.
```

Create:

```text
docs/next_level/c62_polar_circular_phase_contract.json
docs/next_level/c62_polar_circular_phase_validation.json
```

---

# 11. Exact circular-to-Cartesian map

Construct the normalized exact map between:

```text
|n_plus,n_minus>_circ

and

|n_x,n_y>_cart.
```

Use exact binomial expansion of the source-qualified ladder definitions.

Every coefficient must be represented by:

```text
exact rational factors;

factorial square roots;

powers of i;

one canonical expression;

one exact-zero status.
```

Construct shellwise matrices:

\[
U_{\rm cart\leftarrow circ}^{(N)}.
\]

Required checks:

\[
U^\dagger U=I,
\qquad
UU^\dagger=I
\]

exactly or through exact symbolic reduction.

Also verify:

```text
total shell;

L_z representation;

basis permutation;

complex conjugation;

inverse map;

coordinate-space polynomial equality.
```

Create:

```text
docs/next_level/c62_circular_cartesian_contract.json
docs/next_level/c62_circular_cartesian_validation.json
```

---

# 12. Exact polar-to-Cartesian map

Compose:

\[
U_{\rm cart\leftarrow polar}^{(N)}
=
U_{\rm cart\leftarrow circ}^{(N)}
\,
U_{\rm circ\leftarrow polar}^{(N)}.
\]

This matrix replaces the historical numerical `polar_to_cart_shell` as the exact descendant authority.

Historical C47 output remains immutable.

Required checks:

```text
exact shellwise unitarity;

analytic wavefunction equality;

basis-order permutation;

phase formula;

no rowwise fitting;

independent Cartesian integration holdouts.
```

Create:

```text
docs/next_level/c62_exact_polar_cartesian_map.json
docs/next_level/c62_exact_polar_cartesian_validation.json
```

---

# 13. Historical argmax alignment audit

Load the immutable C47 `polar_to_cart_shell` route.

For every row record:

```text
historical quadrature row;

historical argmax index;

historical chosen phase;

exact row;

exact basis permutation;

one global analytic phase;

quadrature residual after applying only the global exact convention.
```

Classify rows as:

```text
AGREES_WITH_EXACT_GLOBAL_CONVENTION;

QUADRATURE_NOISE_ONLY;

ARGMAX_PHASE_UNSTABLE;

BASIS_PERMUTATION_MISMATCH;

FOURIER_PHASE_MISMATCH;

IMPLEMENTATION_DISCREPANCY;

UNRESOLVED_BLOCKING.
```

Demonstrate that perturbing the quadrature row cannot alter the exact phase.

Create:

```text
docs/next_level/c62_historical_argmax_phase_audit.json
docs/next_level/c62_polar_cartesian_reconciliation_report.json
```

---

# 14. Exact x-weighted two-mode rotation

For each exact longitudinal partition, construct the source-owned rotation:

\[
\begin{pmatrix}
a^\dagger_{\mathrm{rel},\sigma}\\
a^\dagger_{\mathrm{CM},\sigma}
\end{pmatrix}
=
R(x_q,x_g)
\begin{pmatrix}
a^\dagger_{q,\sigma}\\
a^\dagger_{g,\sigma}
\end{pmatrix},
\qquad
\sigma\in\{+,-\},
\]

or the exact inverse orientation used by C47.

Use:

\[
x_q=\frac{k_q}{K},
\qquad
x_g=\frac{k_g}{K},
\qquad
x_q+x_g=1,
\]

with exact rational arithmetic.

Represent the rotation entries using exact algebraic objects such as:

```text
sqrt(x_q);

sqrt(x_g);

exact signs;

exact rational factors.
```

Prove:

```text
the preserved metric;

determinant and orientation;

inverse;

canonical commutators;

the same rotation in both circular sectors;

compatibility with the C47 coordinate map.
```

Create:

```text
docs/next_level/c62_exact_two_mode_rotation.json
docs/next_level/c62_two_mode_rotation_validation.json
```

---

# 15. Exact normalized one-dimensional bracket

For normalized occupation states, derive the exact coefficient:

\[
B_R(r,c;q,g)
=
\langle r,c|
\widehat U(R)
|q,g\rangle.
\]

Use finite coefficient extraction from the source-owned creation-operator polynomial.

One acceptable form is:

\[
B_R(r,c;q,g)
=
\sqrt{\frac{r!\,c!}{q!\,g!}}
\,
[z^r w^c]
(R_{11}z+R_{21}w)^q
(R_{12}z+R_{22}w)^g,
\]

subject to verification of orientation and normalization.

Implement the coefficient as a canonical sparse exact sum.

Required checks:

```text
q+g = r+c selection;

exact normalization;

orthogonality;

inverse rotation;

composition of rotations;

reflection and sign controls;

single-term and multi-term holdouts.
```

Create:

```text
docs/next_level/c62_one_dimensional_bracket_contract.json
docs/next_level/c62_one_dimensional_bracket_validation.json
```

---

# 16. Exact two-dimensional circular TM coefficient

For each circular sector construct:

\[
B_+,
\qquad
B_-.
\]

The complete circular coefficient is:

\[
\mathrm{TM}_{\rm circ}
=
B_+ B_-.
\]

Retain:

```text
incoming q/g circular occupations;

outgoing relative/CM circular occupations;

longitudinal-partition ID;

exact expression;

selection-rule ancestry;

normalization;

phase.
```

Required exact rules include:

```text
conservation of total plus-sector occupation;

conservation of total minus-sector occupation;

therefore conservation of total transverse shell;

therefore conservation of total m.
```

Additional exact cancellations must be detected algebraically rather than assumed absent.

Create:

```text
docs/next_level/c62_exact_circular_tm_contract.json
docs/next_level/c62_exact_circular_tm_validation.json
```

---

# 17. Exact polar TM coefficient

Apply the exact input and output polar/circular phase maps:

\[
\mathrm{TM}_{\rm polar}
=
U_{\rm polar\leftarrow circ}^{\rm out}
\,
\mathrm{TM}_{\rm circ}
\,
U_{\rm circ\leftarrow polar}^{\rm in}.
\]

For every coefficient return one terminal status:

```text
ZERO_BY_EXACT_SHELL_RULE;

ZERO_BY_EXACT_M_RULE;

ZERO_BY_EXACT_ALGEBRAIC_CANCELLATION;

NONZERO_EXACT_ALGEBRAIC;

UNDECIDABLE_BLOCKING.
```

A positive gate requires:

```text
UNDECIDABLE_BLOCKING = 0
```

over every coefficient required by the physical trajectory.

Do not introduce a numerical tolerance into this API.

Create:

```text
docs/next_level/c62_exact_polar_tm_contract.json
docs/next_level/c62_exact_polar_tm_validation.json
```

---

# 18. Canonical exact-expression representation

Use an exact expression system capable of deterministic serialization.

An acceptable implementation may use:

```text
SymPy Rational, Integer, I, sqrt, factorial, binomial, and
AlgebraicNumber;

or

a project-native sparse polynomial/radical AST with exact reduction.
```

For each exact longitudinal partition, reduce coefficient expressions in an exact algebraic field containing the required square roots and \(i\).

The representation must support:

```text
canonical ordering;

exact addition and multiplication;

exact zero testing;

high-precision evaluation;

expression hashing;

free-symbol inventory;

basis-independent equality.
```

Do not treat `sympy.N(expr)` or a high-precision float as the expression authority.

Create:

```text
docs/next_level/c62_exact_expression_contract.json
docs/next_level/c62_algebraic_field_manifest.json
```

---

# 19. Complete finite-shell TM blocks

For every longitudinal partition and physical resolution, construct exact block matrices between:

```text
the raw q/g polar single-particle basis;

the relative/CM polar basis.
```

Construct blocks shell by shell before assembling the full finite map.

Report:

```text
shape;

shell decomposition;

m decomposition;

rank;

nullity;

exact nonzero count;

exact-zero-by-rule count;

exact-zero-by-cancellation count;

basis orders;

expression hashes.
```

Classify each block as:

```text
EXACT_UNITARY_BLOCK;

EXACT_ISOMETRIC_BLOCK_WITH_COMPLEMENT;

NONNESTED_BLOCK_WITH_EXPLICIT_COMPLEMENT;

BLOCK_INCOMPLETE.
```

Required checks:

```text
exact or algebraically certified U-dagger U;

exact or algebraically certified U U-dagger;

inverse map;

shell count;

m count;

basis-order independence;

composition with the exact polar/Cartesian maps.
```

Create:

```text
docs/next_level/c62_exact_tm_block_manifest.json
docs/next_level/c62_exact_tm_block_validation.json
```

---

# 20. Independent exact reconstruction

Implement a second route that does not call the primary TM generator.

Preferred independent routes are:

```text
exact Cartesian factorization into two one-dimensional HO rotations,
followed by exact polar/Cartesian recoupling;

or

exact generating-function coefficient extraction.
```

Use analytic coordinate- or momentum-space integration for low-shell holdouts.

High-precision quadrature remains a third, non-authoritative diagnostic.

Compare:

```text
exact expressions;

support classifications;

finite-shell block actions;

low-shell analytic values.
```

Create:

```text
docs/next_level/c62_independent_tm_reconstruction.json
docs/next_level/c62_analytic_low_shell_holdouts.json
docs/next_level/c62_high_precision_quadrature_holdouts.json
```

---

# 21. Coefficient-level historical residue reconciliation

Load the historical C47 TM/CM quadrature coefficients associated with the C60 subthreshold counts:

```text
4,032 / 15,840 / 48,048.
```

C62 must classify residues at the **TM-coefficient algebra level**.

For every residue record:

```text
resolution;

longitudinal partition;

raw polar basis IDs;

relative/CM polar basis IDs;

historical value;

historical threshold decision;

exact TM status;

exact expression hash;

high-precision value;

quadrature discrepancy;

phase/permutation adapter;

provisional support-impact flag.
```

Aggregate:

```text
EXACT_ZERO_QUADRATURE_NOISE;

GENUINE_SMALL_EXACT_NONZERO;

PHASE_OR_PERMUTATION_MISMATCH;

HISTORICAL_INDEXING_MISMATCH;

UNRESOLVED_BLOCKING.
```

A positive C62 gate requires:

```text
UNRESOLVED_BLOCKING = 0
```

for every residue that lies inside the exact TM blocks constructed in C62.

Do not yet issue final descendant supersession decisions. C63 owns the complete CM-ground, triplet, and descendant-impact audit.

Create:

```text
docs/next_level/c62_tm_residue_ledger.json
docs/next_level/c62_tm_residue_reconciliation_report.json
```

---

# 22. Certified numerical export

Export exact TM blocks to numerical arrays for downstream use.

Each numerical entry must carry or inherit:

```text
exact-expression hash;

exact support status;

working precision;

rounded value;

absolute error bound;

basis IDs.
```

Exact zeros may be stored as literal zero only after proof.

Exact nonzeros may not be removed by magnitude.

Run multiple precision levels and require stable:

```text
support;

basis order;

rounded values within bounds;

unitarity residuals within propagated bounds.
```

Create:

```text
docs/next_level/c62_certified_tm_export.json
docs/next_level/c62_precision_stability_report.json
```

---

# 23. Exact TM APIs

Create APIs equivalent to:

```python
polar_to_circular_state(
    n: int,
    m: int,
) -> ExactPolarCircularState

polar_to_cartesian_shell(
    shell: int,
) -> ExactShellTransform

one_dimensional_tm_bracket(
    incoming_1: int,
    incoming_2: int,
    outgoing_1: int,
    outgoing_2: int,
    longitudinal_partition_id: str,
) -> ExactBracket

polar_tm_coefficient(
    raw_q_mode_id: str,
    raw_g_mode_id: str,
    relative_mode_id: str,
    cm_mode_id: str,
    longitudinal_partition_id: str,
) -> ExactTMCoefficient

exact_tm_block(
    resolution_id: str,
    longitudinal_partition_id: str,
)
```

Return objects must expose:

```text
exact status;

exact expression;

expression hash;

selection-rule proof;

basis and phase ancestry;

certified numerical value and bound.
```

Do not expose:

```text
a phase-fit option;

an argmax alignment option;

a support threshold;

a prune-small-values option.
```

Create:

```text
docs/next_level/c62_api_contract.json
docs/next_level/c62_api_validation.json
```

---

# 24. Provisional inherited-impact audit

C62 must identify, but not yet execute, downstream consequences.

Trace whether exact TM coefficients provisionally affect:

```text
C47 raw/CM support identities;

C52 colorless basis projections;

C53 canonical support ancestry;

C57 corresponding-propagating support;

C58 admitted mode supports;

C59/C60 direct-contact preflight.
```

Allowed provisional statuses:

```text
NO_TM_LEVEL_CHANGE;

TM_SUPPORT_SEMANTICS_CHANGED_ONLY;

TM_NUMERICAL_VALUES_CHANGED_WITHIN_HISTORICAL_ERROR;

TM_NUMERICAL_REBUILD_CANDIDATE;

FULL_PHYSICAL_EMBEDDING_AUDIT_REQUIRED;

IMPACT_UNRESOLVED_BLOCKING.
```

C63 must make the final CM-ground/triplet/descendant decision.

Create:

```text
docs/next_level/c62_provisional_descendant_impact.json
```

---

# 25. Isolation and poisoning controls

Prove that C62 is unchanged when:

```text
all C40 arrays are poisoned;

all historical C47 quadrature values are poisoned after holdout IDs
are loaded;

all historical argmax phases are poisoned;

the historical 1e-12 threshold is changed;

all C47 canonical tuple values are poisoned;

all C50/C52/C53 numerical values are poisoned;

all C57/C58 numerical values are poisoned;

ART25 files are inaccessible.
```

The build must fail when:

```text
the C45 polar wavefunction convention changes;

the Fourier phase changes;

the circular-ladder definition changes;

the polar/circular phase formula changes;

the C47 coordinate rotation changes;

an exact fraction is replaced by binary-float inference;

a row-by-row phase fit is introduced;

an exact nonzero is pruned;

an exact zero is assigned by tolerance;

the exact-representation plan changes without supersession.
```

Create:

```text
docs/next_level/c62_isolation_report.json
```

---

# 26. C63/QGEMBED2 import contract

Define the immutable contract by which C63 will consume:

```text
the exact polar wavefunction convention;

the circular-ladder convention;

the exact polar/circular phase map;

the exact polar/Cartesian map;

the exact two-mode rotation;

the exact one-dimensional bracket;

the exact polar TM coefficient generator;

the complete exact finite-shell TM blocks;

the exact support classifications;

the certified numerical arrays;

the residue-reconciliation ledger;

the provisional impact record;

all basis-order and expression hashes.
```

C63 may not:

```text
refit phases;

reintroduce a threshold;

change exact-zero statuses;

or replace the exact blocks with historical quadrature arrays.
```

Create:

```text
docs/next_level/c62_c63_qgembed2_import_contract.json
```

---

# 27. Deterministic runtime bundles

For every resolution and longitudinal partition produce content-addressed bundles containing:

```text
polar/circular phase records;

circular/Cartesian shell maps;

polar/Cartesian shell maps;

exact two-mode rotation;

exact one-dimensional bracket tables;

exact polar TM coefficient records;

exact finite-shell blocks;

exact support masks;

certified numerical blocks;

historical comparison and residue records.
```

Heavy exact-expression tables and numerical arrays may remain outside Git under:

```text
data/runtime/c62_qgtm/
```

Commit an inventory containing:

```text
runtime path;

object type;

shell or partition;

shape or record count;

exact-expression format;

working precision;

error bound;

basis-order hash;

phase-map hash;

expression hash;

support hash;

array hash;

generator command.
```

Create:

```text
docs/next_level/c62_numerical_object_inventory.json
```

All JSON, exact expressions, and numerical arrays must regenerate byte-for-byte.

---

# 28. End-to-end source-to-TM-algebra test

Implement an end-to-end test that starts from the C45/C47 source contracts—not from prebuilt C62 arrays.

It must:

```text
load the analytic polar HO convention;

derive the circular ladder operators;

derive the polar/circular occupations and phase;

derive exact circular/Cartesian and polar/Cartesian shell maps;

derive the exact x-weighted two-mode rotation;

derive one-dimensional brackets;

derive two-dimensional circular and polar TM coefficients;

classify exact zeros and nonzeros;

assemble complete finite-shell blocks;

run the independent exact reconstruction;

export certified numerical blocks;

reconcile historical argmax phases and TM residues;

run isolation, count-once, precision, and provisional-impact tests;

reproduce every hash.
```

It must fail when:

```text
a C47 quadrature row defines a phase;

argmax alignment enters construction;

a support threshold is used;

a genuine exact nonzero is pruned;

a numerical near-zero is labeled exact zero;

a binary float is guessed to be a source rational;

the rotation orientation is inferred from historical agreement;

the independent route calls the primary generator;

a runtime hash changes.
```

---

# 29. Focused mutation tests

Create at least **256 focused live mutations** of actual phases, operators, expressions, coefficients, blocks, or residue records.

Include mutations of:

```text
polar angular sign;

Laguerre phase;

Fourier phase;

circular-operator sign;

L_z sign;

occupation permutation;

polar/circular phase;

Cartesian recoupling phase;

factorial normalization;

binomial coefficient;

rotation entry;

rotation orientation;

longitudinal fraction;

one-dimensional bracket summation bound;

plus-sector coefficient;

minus-sector coefficient;

shell rule;

m rule;

algebraic-cancellation term;

coefficient status;

exact support entry;

historical argmax adapter;

residue classification;

certified numerical bound;

provisional-impact status;

expression hash;

runtime-array hash.
```

Every mutation must fail a concrete source, phase, ladder, exact-zero, unitarity, support, residue, certification, impact, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 30. Readiness gate

Issue:

```text
C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY
```

only when:

```text
the full C61 baseline reproduces;

the C61 no-go remains explicit;

one source-owned analytic polar convention is fixed;

one exact circular-ladder convention is fixed;

the polar/circular bijection closes;

the polar/circular phase follows one analytic formula or recurrence;

no row-by-row phase fit is used;

the circular/Cartesian map closes exactly;

the polar/Cartesian map closes exactly;

the historical argmax phase audit is complete;

the exact x-weighted two-mode rotation closes;

the one-dimensional bracket closes;

the two-dimensional circular coefficient closes;

the two-dimensional polar coefficient closes;

every required coefficient has an exact zero or exact nonzero status;

no required coefficient remains undecidable;

complete finite-shell blocks exist for all physical partitions;

the independent exact reconstruction agrees;

all in-scope historical TM residues are reconciled;

certified numerical exports are stable;

the provisional descendant-impact audit is complete;

count-once and provenance close;

poisoning controls pass;

the C63 import contract is complete;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-TM-algebra test passes.
```

Do not issue:

```text
C62_SOURCE_DERIVED_EXACT_QG_EMBEDDING_READY;

C62_IFERM_CONTACT_SUPPORT_READY;

C62_DIRECT_IFERM_CONTACT_READY;

C62_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C62_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY.
```

---

# 31. Exact no-go branches

## A. The analytic polar-HO phase remains incomplete

```text
C62_POLAR_HO_PHASE_CONTRACT_INCOMPLETE
```

Next:

> **C63/QGPHASE — source-locked polar wavefunction, circular ladder, Fourier phase, and shell permutation completion**

## B. The circular/Cartesian recoupling remains incomplete

```text
C62_POLAR_CARTESIAN_ALGEBRA_INCOMPLETE
```

Next:

> **C63/QGCART — exact circular/Cartesian and polar/Cartesian shell-map completion**

## C. The x-weighted two-mode rotation remains incomplete

```text
C62_QG_ROTATION_CONTRACT_INCOMPLETE
```

Next:

> **C63/QGROT — exact longitudinal-fraction, coordinate, scale, and ladder-rotation completion**

## D. The one-dimensional bracket remains incomplete

```text
C62_ONE_DIMENSIONAL_TM_BRACKET_INCOMPLETE
```

Next:

> **C63/QG1D — exact normalized two-mode coefficient-extraction completion**

## E. The polar TM coefficients remain incomplete

```text
C62_EXACT_POLAR_TM_COEFFICIENT_INCOMPLETE
```

Next:

> **C63/QG2D — exact plus/minus-sector composition, phase adapters, and polar-bracket completion**

## F. Exact and independent routes disagree

```text
C62_EXACT_TM_RECONSTRUCTION_FAILED
```

Next:

> **C63/QGXCHECK — circular, Cartesian, generating-function, and analytic-integral reconciliation**

## G. Historical residues remain unresolved

```text
C62_TM_RESIDUE_RECONCILIATION_INCOMPLETE
```

Next:

> **C63/QGRESIDUE2 — phase, basis-order, exact-zero, and quadrature-residue reconciliation**

## H. Exact TM algebra closes

```text
C62_SOURCE_DERIVED_EXACT_TM_ALGEBRA_READY
```

Next:

> **C63/QGEMBED2 — exact physical qg embedding and descendant-impact closure**

---

# 32. Required deliverables

Create at least:

```text
docs/next_level/c62_implementation_report.md
docs/next_level/c62_api.md
docs/next_level/c62_derivation_authority_manifest.json
docs/next_level/c62_input_fidelity_audit.json

docs/next_level/c62_primary_source_manifest.json
docs/next_level/c62_source_role_matrix.json
docs/next_level/c62_source_sufficiency_matrix.json
docs/next_level/c62_calculation_plan.json
docs/next_level/c62_holdout_plan.json

docs/next_level/c62_exact_representation_plan.json
docs/next_level/c62_exact_representation_decision.json

docs/next_level/c62_polar_ho_wavefunction_contract.json
docs/next_level/c62_polar_ho_wavefunction_validation.json
docs/next_level/c62_circular_ladder_contract.json
docs/next_level/c62_circular_ladder_validation.json
docs/next_level/c62_polar_circular_phase_contract.json
docs/next_level/c62_polar_circular_phase_validation.json

docs/next_level/c62_circular_cartesian_contract.json
docs/next_level/c62_circular_cartesian_validation.json
docs/next_level/c62_exact_polar_cartesian_map.json
docs/next_level/c62_exact_polar_cartesian_validation.json
docs/next_level/c62_historical_argmax_phase_audit.json
docs/next_level/c62_polar_cartesian_reconciliation_report.json

docs/next_level/c62_exact_two_mode_rotation.json
docs/next_level/c62_two_mode_rotation_validation.json
docs/next_level/c62_one_dimensional_bracket_contract.json
docs/next_level/c62_one_dimensional_bracket_validation.json
docs/next_level/c62_exact_circular_tm_contract.json
docs/next_level/c62_exact_circular_tm_validation.json
docs/next_level/c62_exact_polar_tm_contract.json
docs/next_level/c62_exact_polar_tm_validation.json

docs/next_level/c62_exact_expression_contract.json
docs/next_level/c62_algebraic_field_manifest.json
docs/next_level/c62_exact_tm_block_manifest.json
docs/next_level/c62_exact_tm_block_validation.json

docs/next_level/c62_independent_tm_reconstruction.json
docs/next_level/c62_analytic_low_shell_holdouts.json
docs/next_level/c62_high_precision_quadrature_holdouts.json

docs/next_level/c62_tm_residue_ledger.json
docs/next_level/c62_tm_residue_reconciliation_report.json
docs/next_level/c62_certified_tm_export.json
docs/next_level/c62_precision_stability_report.json

docs/next_level/c62_api_contract.json
docs/next_level/c62_api_validation.json
docs/next_level/c62_provisional_descendant_impact.json
docs/next_level/c62_isolation_report.json
docs/next_level/c62_c63_qgembed2_import_contract.json

docs/next_level/c62_numerical_object_inventory.json
docs/next_level/c62_readiness_report.json
docs/next_level/c62_source_sufficiency_decision.json
docs/next_level/c62_no_go_decision_tree.json
docs/next_level/c62_missing_calculation_specification.md
docs/next_level/c62_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/qgtm/
```

or the repository-equivalent package.

Add focused tests for:

```text
polar wavefunction;
circular ladders;
polar/circular phase;
circular/Cartesian map;
polar/Cartesian map;
historical argmax audit;
exact two-mode rotation;
one-dimensional bracket;
two-dimensional circular and polar coefficients;
exact-zero semantics;
finite-shell blocks;
independent reconstruction;
residue reconciliation;
certified export;
isolation;
provisional impact;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON, exact expressions, and runtime arrays must reproduce byte-for-byte.

---

# 33. Acceptance criteria

C62 is complete only when:

1. The full C61 baseline reproduces.
2. The C61 fail-closed status remains explicit.
3. C43/C45/C47 historical files remain unchanged.
4. C40 remains method-oracle only.
5. Historical quadrature phases remain diagnostic-only.
6. No historical numerical matrix defines an exact phase.
7. No support threshold enters the exact API.
8. No physical coupling or contact coefficient is chosen.
9. No endpoint or witness relation is constructed.
10. The C45 polar wavefunction convention is explicit.
11. The coordinate and momentum wavefunctions have a fixed Fourier relation.
12. The circular ladder signs are source derived.
13. The \(L_z\) number-operator relation closes.
14. The polar/circular occupation map is bijective.
15. The polar/circular phase follows one global rule.
16. No row-by-row argmax phase is used.
17. The circular/Cartesian shell map is exact.
18. The polar/Cartesian shell map is exact.
19. Shellwise unitarity closes.
20. Historical argmax phases are fully audited.
21. Exact longitudinal fractions are preserved.
22. The two-mode rotation preserves the declared metric and commutators.
23. The one-dimensional bracket has exact normalization.
24. The plus and minus circular sectors are independent and exact.
25. The complete polar TM coefficient is exact.
26. Every required coefficient has one terminal exact status.
27. No exact nonzero is pruned.
28. No numerical near-zero is labeled exact zero.
29. No coefficient remains undecidable.
30. Complete finite-shell blocks exist for every required partition.
31. Their rank, nullity, shell, and \(m\) structure are complete.
32. The independent exact route agrees.
33. Analytic low-shell holdouts agree.
34. High-precision quadrature is used only as a holdout.
35. Every in-scope historical subthreshold residue is classified.
36. Residue counts close.
37. Certified numerical exports carry error bounds.
38. Precision changes do not alter exact support.
39. Exact APIs expose no phase-fit or threshold option.
40. Provisional descendant impacts are typed.
41. Historical descendants are not superseded prematurely.
42. Duplicate, missing, and unresolved counts are zero.
43. Static and runtime poisoning controls pass.
44. The C63 import contract is complete.
45. Runtime bundles contain exact expressions, support statuses, and numerical arrays.
46. End-to-end reconstruction passes.
47. At least 256 focused live mutations are detected.
48. No exact physical qg embedding is claimed complete.
49. No contact support, value, or matrix is created.
50. No complete instantaneous-fermion or local-HQCD status is issued.
51. No JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
52. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
53. `MSHT20_REP/` remains untouched and outside Git.
54. The working tree is clean except for the pre-existing untracked directory.
55. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken phase authority, exact-zero semantics, finite-shell algebra, independent reconstruction, or residue accounting to open the gate.

---

# 34. Final Codex response

Report:

- full starting and final commits;
- exact source hierarchy and role classifications;
- selected exact representation and independent route;
- C45 coordinate- and momentum-space polar wavefunctions;
- circular ladder definitions and \(L_z\) relation;
- the exact polar/circular occupation and phase formula;
- circular/Cartesian and polar/Cartesian shell-map shapes and exact residuals;
- the historical argmax-phase audit counts;
- exact longitudinal fractions and two-mode rotation matrices;
- one-dimensional bracket formula and residuals;
- circular and polar two-dimensional TM formulas;
- coefficient counts by exact shell zero, exact \(m\) zero, exact cancellation zero, exact nonzero, and undecidable status;
- finite-shell block shapes, ranks, nullities, nonzero counts, and exact/certified unitarity residuals;
- independent reconstruction residuals;
- analytic and high-precision holdout results;
- classification of the historical 4,032 / 15,840 / 48,048 subthreshold residues at the TM-algebra level;
- counts of exact-zero quadrature noise, genuine small nonzeros, phase/permutation mismatches, indexing mismatches, and unresolved records;
- certified numerical precisions and error bounds;
- provisional descendant-impact statuses;
- ancestry, duplicate, missing, and unresolved counts;
- isolation and poisoning results;
- runtime expression, support, and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no CM-ground/triplet physical embedding, endpoint relation, witness relation, contact support/value/matrix, complete instantaneous-fermion operator, local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a quadrature-fitted phase, a rowwise argmax convention, a thresholded near-zero, a pruned exact nonzero, or an exact TM block without an independent reconstruction as completed exact HO/Talmi–Moshinsky algebra.
