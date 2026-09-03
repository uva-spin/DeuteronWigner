# C49/VERTEX1 Codex Work Package

## Title

**Dimensionally homogeneous source-derived canonical \(q\!\leftrightarrow qg\) vertex: finite-volume \(P^-\) normalization, \(P^-\!\to M^2\) conversion, transverse-rank scale separation, exact SU(3)/triplet assembly, and exhaustive tuple closure**

## Authoritative baseline

Start from the clean local C48/HQCD fail-closed completion commit:

```text
d237da980274a4d819b8881750fbbd189f0ef469
```

Its immediate scientific parent is:

```text
055f2a3dd5a651cc687f532f4c0ea58d885dd585
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 055f2a3dd5a651cc687f532f4c0ea58d885dd585 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE
```

and the exact C48 preflight result:

```text
C47 runtime/source fidelity:
    11 required hashes matched

physical qg dimensions:
    1,344 / 2,700 / 4,752

raw canonical tuple counts:
    720 / 1,170 / 1,728

blocking unit declaration:
    L^(-1/2) GeV^(1+|m_rel|)

retained transverse sectors:
    |m_rel| = 0 and 1

missing authority:
    source-derived finite-volume canonical P^- normalization
    and canonical P^- to invariant-mass-squared conversion
```

Verify every value from the committed C48 records rather than relying on this prompt.

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

physical basis trajectory:
    K = 9/2, 11/2, 13/2

invariant-mass convention:
    M^2 = 2 P^+ P^- - P_perp^2

longitudinal box:
    L remains symbolic
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

and cannot provide a C49 normalization, coefficient, unit conversion, or matrix element.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C49 resolves only the canonical-vertex obstruction exposed by C48.

The current C47 tuple values cannot be inserted into one linear operator because entries with different \(|m_{\rm rel}|\) carry different declared dimensions. The current records also stop before deriving how the source-normalized finite-box matrix element of the canonical interaction \(P^-_{\rm int}\) becomes an off-diagonal matrix element of the project invariant-mass operator.

C49 must:

```text
audit and decompose every raw C47 canonical tuple;

derive the finite-volume normalized q->qg matrix element of P^-_int
from the C43 source action and C45/C47 state normalizations;

separate mass, transverse-derivative, polarization, and HO/TM factors
so each operator component has an explicit dimensional signature;

derive the exact fixed-block map from the canonical P^- matrix element
to the invariant-mass-squared coefficient;

rebuild an exhaustive dimensionally homogeneous tuple table;

insert exact SU(3) color and the C45/C47 24 x 3 triplet isometry;

assemble the coupling-factored canonical emission matrix;

generate absorption only as its Hermitian adjoint;

validate all tuple, unit, source, symmetry, and symbolic-L identities.
```

C49 must not assemble the free, instantaneous, constrained, boundary, zero-mode, or counterterm matrices that C48 also requested. Those return only after the canonical vertex is qualified.

The strongest allowed status is:

```text
C49_SOURCE_DERIVED_CANONICAL_VERTEX_READY
```

When that gate passes, the exact next package is:

> **C50/HQCD2 — assemble the complete source-derived local-QCD operator substrate and projected action identity using the validated C49 canonical vertex**

---

# 2. Scientific boundary

C49 is:

```text
canonical q<->qg interaction specific;
finite-volume normalization specific;
dimension-analysis specific;
physical CM-clean color-triplet basis specific;
coupling-factored;
source-first;
deterministic;
validation-only.
```

C49 is not:

```text
a fit of a vertex strength;
a choice of physical alpha_s;
a dressed-quark eigenproblem;
an instantaneous-interaction package;
a JMY Wilson-line package;
a bilocal TMD package;
a counterterm solution;
a one-loop calculation;
a proton or ART25 calculation.
```

Do not repair the unit mismatch by multiplying selected entries by a convenient power of \(b_{\rm HO}\), \(L\), \(P^+\), \(K\), or a mass scale unless that factor is derived from the source action, state normalization, and basis transformation.

---

# 3. Nonnegotiable evidence standard

Every positive canonical matrix element must descend through:

```text
locked primary-source equation
    -> C43 project-convention canonical P^- interaction
    -> C45 normalized field modes/spinors/polarizations
    -> C47 CM-clean basis and exhaustive raw tuple
    -> explicit finite-volume matrix-element derivation
    -> explicit P^- dimensional signature
    -> explicit P^- to M^2 conversion
    -> exact SU(3)/triplet insertion
    -> deterministic sparse matrix
    -> application to nonzero vectors
    -> independent check
    -> deterministic content hash.
```

For every intermediate and final object record:

```text
primary-source locator;
source version;
C43 action-term ID;
C45 mode and phase IDs;
C47 basis/TM/kernel IDs;
incoming and outgoing basis IDs;
operator component;
|m_rel|;
longitudinal normalization;
transverse normalization;
mass, b_HO, P^+, K, and L factors;
formal regulator powers;
total mass dimension;
units before and after conversion;
color tensor;
triplet-isometry row;
coupling power;
generator-code hash;
array hash;
independent residual.
```

An internally consistent unit patch is not a source derivation.

A numerical matrix whose \(|m_{\rm rel}|=0\) and 1 elements have different units is not a linear operator.

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
docs/next_level/c43_finite_basis_projection_contract.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_spinor_polarization_overlap.json
docs/next_level/c45_qg_triplet_projector.json
docs/next_level/c45_c46_projection_interface.json

docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_all_mode_canonical_kernel.json
docs/next_level/c47_all_mode_kernel_validation.json
docs/next_level/c47_c48_matrix_assembly_interface.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c48_implementation_report.md
docs/next_level/c48_input_fidelity_audit.json
docs/next_level/c48_source_sufficiency_decision.json
docs/next_level/c48_missing_calculation_specification.md
```

Use actual filenames when they differ. Do not invent an absent artifact.

Read the exact locked primary sources already preserved for C43, C45, and C47, especially the sources used for:

```text
the canonical light-front QCD interaction;
finite-box state normalization;
BLFQ mode normalization;
the invariant-mass-squared operator;
the physical two-body basis.
```

If those sources do not uniquely determine the canonical vertex normalization, acquire and hash-lock an additional official primary source that does. Do not contact authors and do not infer the missing factor from numerical expectations.

Create:

```text
docs/next_level/c49_derivation_authority_manifest.json
docs/next_level/c49_source_sufficiency_matrix.json
```

---

# 5. Freeze conventions and holdouts

Before modifying a tuple, freeze:

```text
the C43 plus/minus and Fourier conventions;
the C43 canonical interaction density;
the C45 longitudinal box and state normalization;
the C45 HO and Fourier phases;
the C45 spinor and polarization phases;
the C47 x-scaled intrinsic/CM transformation;
the C47 CM-ground basis ordering;
the C47 color-triplet isometry;
the raw C47 tuple table;
the physical resolutions and basis dimensions.
```

Freeze holdouts before deriving the conversion:

```text
at least two |m_rel|=0 tuples per resolution;
at least two |m_rel|=1 tuples per resolution;
one helicity-conserving tuple;
one helicity-changing tuple;
one nontrivial transverse-OAM tuple;
one tuple for each allowed gluon helicity;
one color-generator/triplet entry;
one tuple with the smallest finite x_g;
one tuple with the largest finite x_g;
one exact-zero selection-rule tuple;
one symbolic-L holdout;
one unit-rescaling holdout.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c49_calculation_plan.json
docs/next_level/c49_holdout_plan.json
```

---

# 6. Canonical interaction decomposition

Begin from the exact C43 canonical interaction, schematically:

\[
P^-_{q q g}
=
g_s\int dx^-\,d^2x_\perp\,
\bar\psi(x)\,\Gamma^\mu_{\rm LF}\,T^a\psi(x)\,A^a_\mu(x),
\]

using the exact source-derived light-front operator rather than this schematic form.

Decompose the source expression into separately typed components, for example as actually supported by the source:

```text
mass-dependent spinor term;
transverse-derivative or transverse-momentum term;
helicity-conserving term;
helicity-changing term;
dynamical A_perp contribution;
constrained-field contribution if part of the canonical vertex;
normalization and measure factors.
```

Do not assume that this illustrative list is the exact source decomposition.

Every component must have a homogeneous operator meaning before components are summed.

Create:

```text
docs/next_level/c49_canonical_interaction_decomposition.json
```

---

# 7. Dimensional type system

Implement a machine-checkable dimensional signature for every raw and derived quantity.

At minimum track:

```text
power of L;
power of P^+;
power of b_HO;
power of each explicit mass;
power of dimensionless x, K, and TM brackets;
total natural-unit mass dimension;
target operator type:
    P_MINUS_MATRIX_ELEMENT
    or
    MASS_SQUARED_MATRIX_ELEMENT.
```

Treat:

```text
[L] = mass^(-1);
[b_HO] = mass;
[P^+] = mass;
[g_s] = mass^0 in four-dimensional QCD.
```

Verify these assignments against the project convention and source.

The ledger must distinguish:

```text
formal regulator dependence;
physical mass dimension;
basis-function normalization;
operator dimension.
```

For every final \(P^-\) entry, all nonzero components must share one operator-level dimensional signature.

For every final \(M^2\) entry, all nonzero components must have total mass dimension two and a common factored finite-volume signature.

Create:

```text
docs/next_level/c49_dimensional_type_system.json
docs/next_level/c49_dimensional_audit.json
```

The gate must fail before matrix assembly when dimensions are incompatible.

---

# 8. Audit and supersede the raw C47 tuple semantics

Preserve the C47 tuple table byte-for-byte as historical input.

For each of the:

```text
720 / 1,170 / 1,728
```

raw tuples, determine whether its stored value is:

```text
a dimensionless TM/HO bracket;
a transverse momentum moment;
a spinor/polarization numerator;
a partially normalized P^- component;
a composite object with mixed factors;
or unavailable for unique interpretation.
```

Create a one-to-one or explicit one-to-many descendant mapping:

```text
raw tuple ID
    -> normalized component IDs
    -> recomposed P^- tuple ID
    -> M^2 tuple ID.
```

Every decomposition must preserve signs and phases.

No raw tuple may be silently dropped, duplicated, or reinterpreted.

Allowed raw-tuple statuses:

```text
SOURCE_DECOMPOSED_AND_NORMALIZED;
SOURCE_DECOMPOSED_REQUIRES_SHARED_FACTOR;
AMBIGUOUS_BLOCKING;
EXACT_ZERO_BY_SELECTION_RULE.
```

Create:

```text
docs/next_level/c49_c47_tuple_semantics_audit.json
docs/next_level/c49_tuple_supersession_map.json
```

Any required `AMBIGUOUS_BLOCKING` tuple prevents the positive gate.

---

# 9. Resolve the \(|m_{\rm rel}|=0,1\) unit mismatch

Derive how the source canonical numerator and the C45/C47 HO/TM integrals combine in each transverse-angular sector.

For every retained component identify explicitly:

```text
the number of transverse derivatives or momenta;
whether the momentum factor is contained in the spinor numerator,
the HO overlap, or both;
the power of b_HO generated by changing to a dimensionless HO variable;
any mass term carrying the missing dimension;
the TM/Jacobi bracket normalization;
the angular phase and OAM selection rule.
```

The current declaration:

\[
L^{-1/2}\,\mathrm{GeV}^{\,1+|m_{\rm rel}|}
\]

must be superseded by a source-derived factorization in which the full \(P^-\) matrix element has one dimension independent of \(|m_{\rm rel}|\).

Do not force homogeneity by multiplying all \(|m_{\rm rel}|=1\) entries by \(1/b_{\rm HO}\), or the \(|m_{\rm rel}|=0\) entries by \(b_{\rm HO}\), unless that factor follows from the source-normalized integral.

Required independent checks:

```text
direct physical-momentum integration;
dimensionless-HO-variable integration with explicit b_HO factors;
coordinate-space derivative evaluation where available;
momentum-space evaluation;
frozen tuple holdouts;
controlled b_HO rescaling.
```

Create:

```text
docs/next_level/c49_mrel_scale_factorization.json
docs/next_level/c49_mrel_unit_closure_report.json
```

---

# 10. Finite-volume normalized \(P^-\) matrix element

Derive the complete finite-box matrix element:

\[
\langle qg,\beta|P^-_{q q g}|q,\alpha\rangle
\]

using:

```text
the C43 field expansion;
the C43/C45 canonical brackets;
the finite interval -L <= x^- <= L;
p^+ = pi k/L;
the finite-box Kronecker normalization;
the C45 transverse measure;
the C47 normalized physical states;
the selected open-color matching-module convention.
```

Retain every factor from:

```text
the x^- integration;
the transverse integration;
creation/annihilation normalization;
external-state normalization;
longitudinal conservation;
spinor and polarization normalization;
CM/TM transformation;
identical-particle conventions where applicable.
```

Keep \(L\) symbolic.

Determine whether the finite-volume matrix element:

```text
is independent of L;
contains a block-common factored power of L;
or retains a source-defined regulator dependence.
```

An element-dependent \(L\) power is forbidden unless the source operator itself has different dimensions in different components, in which case the components cannot be summed into one vertex and the package must fail closed.

Create:

```text
docs/next_level/c49_finite_volume_pminus_normalization.json
docs/next_level/c49_pminus_tuple_table.json
docs/next_level/c49_pminus_validation.json
```

---

# 11. Derive the \(P^-\!\to M^2\) conversion

Use the fixed project identity:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Derive the off-diagonal q-to-qg conversion between normalized states at fixed total momentum.

Do not simply multiply by \(2P^+\) without proving:

```text
the q and qg states share the same total P^+;
the finite-box normalization is consistent on both sectors;
the total P_perp^2 operator has no off-diagonal q<->qg contribution
at the declared scope;
the basis is in the declared total-transverse-momentum/CM frame;
the factor of two follows from the C43 metric convention;
no additional state-rescaling factor appears.
```

Compile and decide among:

```text
VERTEX1-DIRECT-M2-PROJECTION;

VERTEX1-PMINUS-THEN-M2;

VERTEX1-TWO-ROUTE-EQUIVALENT;

VERTEX1-CONVERSION-UNAVAILABLE.
```

Prefer a two-route equality when the sources permit:

```text
direct projection of the mass-squared operator;
finite-volume P^- matrix element followed by the derived conversion.
```

The final coupling-factored canonical matrix must have uniform units of mass squared.

Create:

```text
docs/next_level/c49_pminus_to_m2_contract.json
docs/next_level/c49_pminus_to_m2_validation.json
```

---

# 12. Rebuild the exhaustive canonical tuple table

Create a new dimensionally homogeneous C49 table for each resolution.

Every tuple must record:

```text
incoming q basis ID;
outgoing CM-clean triplet qg basis ID;
raw C47 tuple ancestry;
operator component ancestry;
dimensionless overlap;
explicit scale factors;
finite-volume P^- value and units;
M^2 value and units;
selection-rule identity;
holdout role;
source/derivation ID.
```

Required counts:

```text
every allowed C47 tuple consumed exactly once;
every exact-zero tuple preserved as an exact-zero decision;
no duplicate basis-pair contribution unless distinct source components
are explicitly summed;
all component sums auditable.
```

Report separately:

```text
raw tuple count;
normalized component count;
recomposed P^- tuple count;
M^2 tuple count;
exact-zero count;
duplicate count;
missing count;
ambiguous count.
```

The required missing, duplicate, and ambiguous counts are zero for a positive gate.

Create:

```text
docs/next_level/c49_dimensionally_homogeneous_tuple_table.json
docs/next_level/c49_tuple_count_once_report.json
```

---

# 13. Assemble the colorless kinematic matrices

Before inserting color, assemble a color-stripped kinematic matrix at each resolution:

\[
\widehat V_{\rm kin}^{(-)}
\]

for \(P^-\), and:

\[
\widehat V_{\rm kin}^{(M^2)}
\]

for the invariant-mass-squared coefficient.

Required checks:

```text
uniform dimensions;
sparse tuple action versus direct tuple sum;
frozen element reconstruction;
selection-rule closure;
resolution identity;
symbolic-L factorization;
b_HO-rescaling law;
P^- and M^2 conversion equality.
```

Create:

```text
docs/next_level/c49_colorless_kinematic_vertex.json
docs/next_level/c49_colorless_vertex_validation.json
```

---

# 14. Insert exact SU(3) and the triplet isometry

Only after the colorless kinematic matrix is dimensionally and source qualified, insert:

```text
T^a = lambda^a/2;
the adjoint color label;
the exact C45/C47 24 x 3 triplet isometry;
the selected open-color module normalization.
```

Construct the coupling-factored emission matrix:

\[
\widehat V^{(M^2)}_{qg\leftarrow q}
=
\frac{1}{g_s}
V^{(M^2)}_{qg\leftarrow q}.
\]

Required checks:

```text
Tr(T^aT^b)=delta^{ab}/2;
C_F=4/3;
triplet-image residual;
total-generator covariance;
rank-three color map;
basis-rotation invariance;
direct color-tensor reconstruction;
no color singlet substitution;
no full-product color leakage.
```

Create:

```text
docs/next_level/c49_canonical_qg_vertex_matrix.json
docs/next_level/c49_color_triplet_validation.json
```

---

# 15. Generate the absorption adjoint

Define:

\[
\widehat V^{(M^2)}_{q\leftarrow qg}
=
\left(
\widehat V^{(M^2)}_{qg\leftarrow q}
\right)^\dagger.
\]

Do not independently re-evaluate or fit the absorption matrix.

Required checks:

```text
shape;
basis ordering;
phase convention;
adjoint residual;
nonzero action on normalized q and qg vectors;
block-Hermiticity of the g_s-linear two-sector operator.
```

Create:

```text
docs/next_level/c49_vertex_adjoint_report.json
```

---

# 16. Unit and convention covariance tests

Execute at least the following independent tests:

## 16.1 GeV/MeV unit conversion

Convert all dimensional inputs coherently and verify that:

```text
P^- entries scale with the derived mass dimension;
M^2 entries scale quadratically;
dimensionless observables and residuals are invariant.
```

## 16.2 Symbolic-\(L\) test

Vary the symbolic representation of \(L\) or evaluate at two diagnostic \(L\) values only after factoring the source expression.

Verify the predicted common scaling or exact cancellation.

Do not treat either value as physical.

## 16.3 \(b_{\rm HO}\) scaling

Evaluate source-predicted scaling of the separate mass and transverse structures.

Do not demand numerical invariance when the physical basis genuinely changes with \(b_{\rm HO}\); test the analytic factorization and transformed matrix element.

## 16.4 Phase and Fourier convention

Verify the C43/C45 Fourier and HO phases through direct coordinate- and momentum-space routes.

## 16.5 \(P^-\) versus \(M^2\)

Verify the selected conversion on all frozen holdouts and representative entries from every block.

Create:

```text
docs/next_level/c49_unit_covariance_report.json
docs/next_level/c49_convention_roundtrip_report.json
```

---

# 17. Physical-resolution comparison diagnostics

Use the C47 physical basis comparison maps to compare the completed canonical matrix across adjacent resolutions.

Evaluate the exact supported relation:

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
transverse-basis truncation;
CM-projection remainder;
color-triplet remainder;
unit/normalization remainder;
numerical error.
```

Do not fit a trajectory or call this continuum convergence.

Create:

```text
docs/next_level/c49_vertex_comparison_report.json
docs/next_level/c49_vertex_remainder_ledger.json
```

---

# 18. Deterministic runtime bundle

For every physical resolution, produce a content-addressed runtime bundle containing:

```text
normalized component table;
P^- tuple table;
M^2 tuple table;
colorless P^- matrix;
colorless M^2 matrix;
SU(3)/triplet emission matrix;
generated absorption adjoint;
basis-order identities;
dimension/unit ledger;
matrix-free tuple-action metadata;
comparison-map execution blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c49_vertex1/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
formal L/b_HO/P^+ factors;
coupling power;
basis-order hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c49_numerical_object_inventory.json
```

All bundles must regenerate byte-for-byte.

---

# 19. End-to-end source-to-vertex test

Implement an end-to-end test that begins from the C43 source/action records, C45 normalized modes, and C47 physical basis—not from prebuilt C49 matrices.

It must:

```text
load and audit every raw C47 tuple;
derive the component decomposition;
derive the finite-volume P^- normalization;
derive the P^- to M^2 map;
rebuild the homogeneous tuple table;
assemble the colorless matrices;
insert exact SU(3) and the triplet isometry;
generate the absorption adjoint;
run unit and convention tests;
run physical-resolution comparisons;
reproduce every hash.
```

It must fail when:

```text
an |m_rel|=1 entry is patched by an unproved power of b_HO;
an |m_rel|=0 entry is patched by an unproved mass;
the P^- to M^2 factor is hard-coded without its contract;
the factor of two is removed or duplicated;
P_perp^2 is ignored without proof;
L is assigned an arbitrary physical value;
one raw tuple is dropped or duplicated;
a C40 matrix is substituted;
a Gell-Mann generator changes;
the triplet isometry changes;
the absorption matrix is independently altered;
a runtime hash changes.
```

---

# 20. Focused mutation tests

Create at least **192 focused live mutations** of actual derivations, tuple records, units, or matrices.

Include mutations of:

```text
raw tuple dimensional signature;
|m_rel| label;
transverse derivative count;
mass-term factor;
b_HO power;
L power;
P^+ power;
finite-box state normalization;
Fourier phase;
P^- to M^2 conversion;
factor of two;
P_perp block decision;
tuple count-once map;
SU(3) generator;
triplet isometry;
basis ordering;
vertex adjoint;
comparison map;
runtime-array hash.
```

Every mutation must fail a concrete source, dimension, count-once, covariance, adjoint, or deterministic-reconstruction check.

Do not inflate the count with identifier-only dispatch.

---

# 21. Readiness gate

Issue:

```text
C49_SOURCE_DERIVED_CANONICAL_VERTEX_READY
```

only when:

```text
the full C48 baseline reproduces;
the source-sufficiency matrix has no required absent row;
all raw tuples have unambiguous source semantics;
the |m_rel|=0 and 1 components are dimensionally homogeneous after
source-derived factorization;
the finite-volume P^- normalization is complete;
the symbolic-L dependence is common and explicit or cancels;
the P^- to M^2 conversion is derived and validated;
every raw tuple is consumed exactly once;
the final M^2 tuple table has uniform mass-squared units;
the colorless matrices close;
the exact SU(3)/triplet insertion closes;
absorption is the generated adjoint;
unit/convention covariance tests pass;
comparison diagnostics execute;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-vertex test passes.
```

Do not issue:

```text
C49_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C49_INSTANTANEOUS_OPERATOR_VALIDATED;
C49_JMY_WILSON_MATRIX_VALIDATED;
C49_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C49_ONE_LOOP_TMD_VALIDATED;
C49_MATCHING_KERNEL_VALIDATED.
```

---

# 22. Exact no-go branches

## A. Canonical source chain remains incomplete

```text
C49_CANONICAL_SOURCE_CHAIN_INCOMPLETE
```

Next:

> **C50/VSRC — exact finite-volume light-front canonical-vertex source and convention closure**

## B. \(|m_{\rm rel}|\) dimensional factorization remains incomplete

```text
C49_MREL_UNIT_FACTORIZATION_INCOMPLETE
```

Next:

> **C50/MREL — transverse-rank HO/spinor dimensional-factorization completion**

## C. Finite-volume or symbolic-\(L\) normalization remains incomplete

```text
C49_FINITE_VOLUME_VERTEX_NORMALIZATION_INCOMPLETE
```

Next:

> **C50/VNORM — finite-box state, measure, and canonical \(P^-\) normalization completion**

## D. \(P^-\!\to M^2\) conversion remains incomplete

```text
C49_PMINUS_TO_M2_CONVERSION_INCOMPLETE
```

Next:

> **C50/M2MAP — direct and converted invariant-mass vertex normalization completion**

## E. Tuple reconstruction remains incomplete

```text
C49_EXHAUSTIVE_TUPLE_RECONSTRUCTION_INCOMPLETE
```

Next:

> **C50/TUPLE1 — raw-component semantics, count-once, and exhaustive tuple completion**

## F. SU(3)/triplet assembly fails

```text
C49_COLOR_TRIPLET_VERTEX_INCOMPLETE
```

Next:

> **C50/COLORV — exact SU(3) color insertion and \(3\otimes8\to3\) vertex completion**

## G. Canonical vertex closes

```text
C49_SOURCE_DERIVED_CANONICAL_VERTEX_READY
```

Next:

> **C50/HQCD2 — assemble the remaining local-QCD operator substrate and projected action identity**

---

# 23. Required deliverables

Create at least:

```text
docs/next_level/c49_implementation_report.md
docs/next_level/c49_api.md
docs/next_level/c49_derivation_authority_manifest.json
docs/next_level/c49_source_sufficiency_matrix.json
docs/next_level/c49_calculation_plan.json
docs/next_level/c49_holdout_plan.json

docs/next_level/c49_canonical_interaction_decomposition.json
docs/next_level/c49_dimensional_type_system.json
docs/next_level/c49_dimensional_audit.json

docs/next_level/c49_c47_tuple_semantics_audit.json
docs/next_level/c49_tuple_supersession_map.json
docs/next_level/c49_mrel_scale_factorization.json
docs/next_level/c49_mrel_unit_closure_report.json

docs/next_level/c49_finite_volume_pminus_normalization.json
docs/next_level/c49_pminus_tuple_table.json
docs/next_level/c49_pminus_validation.json
docs/next_level/c49_pminus_to_m2_contract.json
docs/next_level/c49_pminus_to_m2_validation.json

docs/next_level/c49_dimensionally_homogeneous_tuple_table.json
docs/next_level/c49_tuple_count_once_report.json
docs/next_level/c49_colorless_kinematic_vertex.json
docs/next_level/c49_colorless_vertex_validation.json

docs/next_level/c49_canonical_qg_vertex_matrix.json
docs/next_level/c49_color_triplet_validation.json
docs/next_level/c49_vertex_adjoint_report.json

docs/next_level/c49_unit_covariance_report.json
docs/next_level/c49_convention_roundtrip_report.json
docs/next_level/c49_vertex_comparison_report.json
docs/next_level/c49_vertex_remainder_ledger.json

docs/next_level/c49_numerical_object_inventory.json
docs/next_level/c49_readiness_report.json
docs/next_level/c49_source_sufficiency_decision.json
docs/next_level/c49_no_go_decision_tree.json
docs/next_level/c49_missing_calculation_specification.md
docs/next_level/c49_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/vertex1/
```

or the repository-equivalent package.

Add focused tests for:

```text
dimensional type checking;
raw tuple semantics;
m_rel scale factorization;
finite-volume P^- normalization;
P^- to M^2 conversion;
tuple count once;
colorless matrix assembly;
SU(3)/triplet insertion;
adjoint generation;
unit/convention covariance;
comparison diagnostics;
end-to-end source-to-vertex reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 24. Acceptance criteria

C49 is complete only when:

1. The full C48 baseline reproduces.
2. The C48 fail-closed result remains explicit.
3. The C43 action, C45 mode, and C47 basis contracts remain unchanged.
4. C40 remains method-oracle only.
5. No arbitrary numerical \(L\) is introduced.
6. No physical coupling is chosen.
7. The canonical source decomposition is explicit.
8. Every raw tuple receives a source-semantic status.
9. Every raw tuple has a machine-checkable dimensional signature.
10. Formal regulator powers and total mass dimension remain separate.
11. The \(|m_{\rm rel}|=0\) components are normalized from source formulas.
12. The \(|m_{\rm rel}|=1\) components are normalized from source formulas.
13. No \(b_{\rm HO}\) or mass patch is introduced for convenience.
14. Direct physical-momentum and dimensionless-HO routes agree.
15. The finite-volume \(P^-\) matrix element is derived.
16. External-state and mode normalizations are explicit.
17. Symbolic \(L\) dependence is common, factored, or canceled.
18. The \(P^-\!\to M^2\) conversion is derived.
19. The \(P_\perp^2\) off-diagonal decision is proved.
20. Every raw tuple is consumed exactly once.
21. Missing, duplicate, and ambiguous tuple counts are zero.
22. Every final \(P^-\) entry has uniform operator units.
23. Every final \(M^2\) entry has uniform mass-squared units.
24. Colorless tuple and sparse-matrix actions agree.
25. Exact SU(3) insertion closes.
26. The emission image lies in the total-color triplet.
27. Absorption is the generated adjoint.
28. GeV/MeV unit covariance passes.
29. Symbolic-\(L\) tests pass.
30. \(b_{\rm HO}\) factorization tests pass.
31. Coordinate- and momentum-space phase checks pass.
32. Physical-resolution comparison diagnostics execute.
33. Runtime bundles contain actual arrays and typed units.
34. End-to-end source-to-vertex reconstruction passes.
35. At least 192 focused live mutations are detected.
36. No free, instantaneous, constrained, boundary, or zero-mode matrix is claimed complete.
37. No complete local-QCD substrate status is issued.
38. No JMY Wilson or bilocal TMD matrix is created.
39. No physical counterterm coefficient is solved.
40. No one-loop coefficient or matching kernel is created.
41. No proton TMD or ART25 bridge is created.
42. No fit, inference, process, or production route is created.
43. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
44. `MSHT20_REP/` remains untouched and outside Git.
45. The working tree is clean except for the pre-existing untracked directory.
46. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken dimensional homogeneity, finite-volume normalization, exhaustive tuple accounting, or the \(P^-\!\to M^2\) derivation to obtain a matrix.

---

# 25. Final Codex response

Report:

- full starting and final commits;
- exact source and convention authorities used;
- source-sufficiency counts;
- raw tuple counts and semantic classifications;
- normalized component counts;
- \(|m_{\rm rel}|=0,1\) scale factorizations;
- dimensional signatures before and after correction;
- finite-volume state and \(P^-\) normalization;
- symbolic \(L\) treatment;
- selected \(P^-\!\to M^2\) route and residuals;
- final homogeneous tuple counts and count-once residuals;
- colorless \(P^-\) and \(M^2\) matrix shapes, nnz, norms, and unit checks;
- SU(3)/triplet emission-matrix shape, nnz, norm, Casimir/covariance/triplet residuals;
- absorption-adjoint residual;
- GeV/MeV, \(L\), \(b_{\rm HO}\), phase, and conversion checks;
- physical-resolution comparison residuals and separated remainders;
- runtime-bundle hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no remaining local-QCD matrices, JMY Wilson/bilocal matrix, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a dimensionally mixed tuple table, an unproved \(2P^+\) multiplier, a convenient \(b_{\rm HO}\) repair, a partially consumed tuple set, or a color matrix without the triplet-image proof as a source-derived canonical vertex.
