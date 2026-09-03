# C79/IFCONTACT2 Codex Work Package

## Title

**Source-derived bare direct instantaneous-fermion contact matrix on the immutable C78 support: finite-cell \(P^-\) kernel, inverse-\(\partial^+\) prescription, ordered SU(3) color, exact HO-mode projection, factorized sparse assembly, and C80 complete-operator handoff**

## Authoritative baseline

Start from the clean local C78 completion commit:

```text
1ddf21c230d3a16ee7e52ed09d84140f43781bb8
```

Before changing tracked files, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "1ddf21c230d3a16ee7e52ed09d84140f43781bb8"
```

The following pre-existing untracked paths must remain untouched and outside Git:

```text
MSHT20_REP/
docs/next_level/c69_qgembed5_codex_prompt.md
```

Do not add, modify, remove, rename, stage, or consume either path as scientific authority.

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY
C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
```

and the exact C78 completion:

```text
physical qg dimensions:
    1,344 / 2,700 / 4,752;

retained-q dimension:
    6 at each resolution;

ordered absorption edges:
    312 / 510 / 756;

ordered emission edges:
    312 / 510 / 756;

raw endpoint paths on each side:
    13,056 / 31,450 / 64,464;

witness triples and supported physical pairs:
    16,224 / 43,350 / 95,256;

factorized symbolic kernel-coordinate domains:
    28,606,464 / 165,991,250 / 697,394,304;

undecidable pairs:
    0;

duplicate witnesses:
    0;

missing ancestry:
    0;

C57 reconciliation:
    EXACT_CERTIFICATE_SUPERSESSION_NO_SUPPORT_CHANGE;

C58:
    unchanged and separate;

C53:
    neither numerical values nor propagated sequential vertices were
    used.
```

Verify all actual identities, counts, hashes, formulas, source locks, support
classes, and public operations from the repository. This prompt is not
numerical authority.

Create a local completion commit. Do not push.

---

# 1. Scientific purpose and exact stopping point

C79 must evaluate the **bare direct normal-ordered instantaneous-fermion
contact** arising from the C55 monomial

\[
b^\dagger a^\dagger a b
\]

on the exact physical support established by C78.

For each resolution \(R\), construct the \(g_s^2\)-factored matrix

\[
\left[M^{2,\mathrm{bare}}_{\mathrm{IF,contact},R}\right]_{bk}
=
g_s^2
\sum_{\kappa}
c^{(\kappa)}_{bk}\,
\mathcal K^{M^2}_{R,\kappa},
\]

where:

```text
b:
    physical qg bra identity;

k:
    physical qg ket identity;

kappa:
    one independent C78 source-defined kernel coordinate;

c_bk^(kappa):
    exact C78 projected coefficient and ancestry;

K_R,kappa^(M2):
    the source-derived finite-basis direct-contact kernel value,
    after the exact P-minus to M-squared conversion.
```

Keep \(g_s^2\) explicit and factored. Do not choose a physical coupling or
running scale in C79.

C79 must produce:

```text
the source-derived bare P-minus kernel;

the exact M-squared conversion;

the direct qg-to-qg contact matrix coefficient of g_s^2;

an independently implemented matrix-free action;

certified numerical bounds;

and a complete immutable runtime/API package.
```

C79 must not produce:

```text
a fitted or physical value of g_s;

a subtraction or counterterm coefficient;

a renormalized instantaneous-fermion operator;

the C58 q-sector self-induced-inertia matrix again;

a C53 sequential-vertex or resolvent substitute;

a complete local-QCD Hamiltonian;

a Wilson/TMD, matching, fit, inference, or production object.
```

The strongest positive status is:

```text
C79_SOURCE_DERIVED_BARE_IFERM_CONTACT_MATRIX_READY
```

The exact positive continuation is:

> **C80/IFERM3 — assemble the complete bare instantaneous-fermion operator from the immutable C58 self-induced-inertia and C79 direct-contact blocks, derive sector-specific counterterm directions and the resolution trajectory, and issue the local-HQCD continuation gate**

---

# 2. Authority policy

Apply the authority hierarchy established in C77.

## 2.1 External/source authority is required for

```text
the instantaneous-fermion operator formula;

the normal-ordering and field-order convention;

the inverse-partial-plus operator meaning;

the overall source coefficient and signs;

the light-front action convention;

the P-minus to M-squared relation.
```

Use the exact source locks and equation chain already frozen by C43, C50,
and C55. Do not import a different convention merely because another source
is prominent.

## 2.2 Exact project-derived authority is sufficient for

```text
mode enumeration;

finite-HO overlap evaluation under the already selected project
regulator;

canonical kernel-coordinate identities;

factorized contractions;

basis ordering;

sparse assembly;

matrix-free actions;

runtime serialization and hashes.
```

No external paper is required to publish the project's exact sparse-matrix
ordering or kernel-coordinate IDs.

## 2.3 Existing project regulator status

C57 already selected:

```text
IFREG-CORRESPONDING-PROPAGATING-SUPPORT
CORRESPONDING_PROPAGATING_GRAPH_PROJECT
```

as a fixed-\(K\), incoming-quark-indexed conditional finite-HO graph
regulator. Preserve its declared limitations. Do not relabel it as a
universal field projector or BPP DLCQ.

A new external-authority no-go is valid only when the source-locked
instantaneous operator, the frozen finite-cell convention, and the exact
project mode realization are genuinely contradictory or leave a
physically consequential coefficient undefined.

---

# 3. Mandatory inputs

Read completely the actual repository equivalents of:

```text
C43:
    selected light-front gauge action;
    light-front normalization;
    constrained-fermion solution;
    instantaneous-fermion action term;
    inverse-partial-plus and zero-mode policy;
    canonical brackets and finite-volume convention;

C45:
    longitudinal modes;
    normalized 2D-HO modes;
    spinors and polarizations;
    phase convention;
    zero-mode projectors;

C47:
    x-weighted product/relative-CM basis;
    finite-shell truncation;
    physical q and qg basis identities;
    CM-ground projection;

C50:
    finite-cell P-minus convention;
    exact sqrt(2) convention map;
    M-squared = 2 P-plus P-minus - P-perp-squared conversion;
    units and normalization contracts;

C55:
    exact source lock for the instantaneous-fermion term;
    C43/source convention map;
    g_s-squared coefficient;
    all normal-ordered monomials;
    direct b-dagger a-dagger a b term;
    distinction from C53 sequential propagation;

C57:
    conditional finite-HO field regulator;
    corresponding-propagating graph selection;
    field-mode support;
    zero-mode and boundary controls;

C58:
    ordered Pi-bra delta Pi-ket self-induced-inertia block;
    bare-retention decision;
    q-sector result;
    qg counterterm-only scope;

C77:
    exact physical qg embedding and projectors;
    canonical raw and physical identities;
    certified component values and bounds;

C78:
    absorption and emission endpoints;
    retained-q witnesses;
    independent symbolic kernel coordinates;
    exact projected coefficients;
    physical support statuses;
    C57 reconciliation;
    C58 separation;
    C53 non-substitution.
```

Use C53 only as a post-construction non-substitution and support holdout.

Create:

```text
docs/next_level/c79_derivation_authority_manifest.json
docs/next_level/c79_input_fidelity_audit.json
```

---

# 4. Freeze all inputs before kernel evaluation

Consume C78 through its authenticated public support API.

Freeze:

```text
C78 package/root identity;

the 16,224 / 43,350 / 95,256 supported physical-pair identities;

all witness identities;

all independent kernel-coordinate identities;

all exact projected coefficients c_bk^(kappa);

all C77 embedding and bound identities used by C78;

the C43/C50/C55 operator and convention chain;

the C57 regulator identity;

the C58 self-induced-inertia separation record.
```

Issue:

```text
C79_INPUTS_FROZEN_COMPLETE
```

in:

```text
docs/next_level/c79_input_freeze.json
```

After this freeze, do not alter support to make the evaluated matrix more
sparse, more Hermitian, or numerically convenient.

---

# 5. Freeze the exact operator-level contact formula

Transcribe the exact C55 source-mapped direct-contact formula into one
canonical C79 operator record.

The record must expose:

```text
source equation identities and hashes;

project light-front convention;

field order b-dagger a-dagger a b;

overall sign;

all factors of g_s, 2, sqrt(2), and i;

gamma-matrix order;

the field product on which 1/(i partial-plus) acts;

the ordered color-generator product;

integration measure;

normal-ordering sign;

zero-mode prescription;

the declared P-minus units.
```

Do not use an approximate formula copied from this prompt. The committed
C55/C43 source chain is authoritative.

Implement two independent symbolic derivations of the overall coefficient:

```text
direct transcription/convention map;

reduction from the constrained-fermion action.
```

Require exact agreement.

Create:

```text
docs/next_level/c79_contact_operator_contract.json
docs/next_level/c79_contact_operator_coefficient_validation.json
```

---

# 6. Define the independent kernel-coordinate vocabulary

Each C78 coordinate \(\kappa\) must identify every variable on which the
contact kernel can depend.

At minimum, where present in the source chain, retain:

```text
resolution;

incoming and outgoing quark longitudinal modes;

incoming and outgoing gluon longitudinal modes;

retained intermediate quark plus momentum;

incoming and outgoing quark transverse modes;

incoming and outgoing gluon transverse modes;

quark helicities;

gluon polarizations/helicities;

incoming and outgoing fundamental colors;

incoming and outgoing adjoint colors;

ordered color-generator identity;

inverse-partial-plus channel;

zero-mode and boundary identity;

finite-HO shell/truncation identity;

source-order sign;

P-minus/M-squared normalization identity.
```

Two coordinates may share one evaluated kernel value only when exact
source and basis symmetries prove that equivalence.

Do not merge coordinates because their floating values happen to agree.

Do not split source-identical coordinates merely to avoid cancellation.

Create:

```text
docs/next_level/c79_kernel_coordinate_vocabulary.json
docs/next_level/c79_kernel_coordinate_equivalence_report.json
```

---

# 7. Longitudinal kernel and inverse-\(\partial^+\)

Derive the exact longitudinal factor from the source-ordered field product.

For every kernel coordinate determine:

```text
which plus momentum appears in the inverse derivative;

its sign under the frozen Fourier convention;

the exact half-integer/integer finite-cell value;

longitudinal Kronecker conservation;

normalization powers of L and P-plus;

whether the channel is excluded by the zero-mode policy;

whether a principal-value prescription is relevant on the retained
positive-mode support.
```

Requirements:

```text
do not replace the source denominator with a sequential C53 energy
denominator;

do not add an i-epsilon absent from the instantaneous operator;

do not use the C57 support threshold;

do not silently assign a zero-mode denominator a finite value.
```

Prove whether the retained C78 support excludes every singular denominator.
If a singular allowed coordinate exists, fail closed with its exact
identity rather than clipping it.

Create:

```text
docs/next_level/c79_inverse_partial_plus_contract.json
docs/next_level/c79_longitudinal_kernel_validation.json
```

---

# 8. Spinor and polarization numerator

Evaluate the source-ordered numerator using the frozen C45 spinors,
polarizations, gamma matrices, and light-front normalization.

Construct two independent routes:

```text
direct gamma-matrix contraction;

source-reduced light-front helicity expression.
```

For each coordinate retain:

```text
incoming/outgoing quark helicities;

incoming/outgoing gluon polarizations;

intermediate gamma-plus projector identity;

exact or canonical symbolic numerator;

certified numerical value and bound;

selection-rule status.
```

Validate:

```text
helicity selection;

polarization-basis covariance;

conjugation/adjoint relation;

light-front normalization;

negative controls for reversed gamma ordering and omitted gamma-plus.
```

Create:

```text
docs/next_level/c79_spinor_polarization_kernel.json
docs/next_level/c79_spinor_polarization_validation.json
```

---

# 9. Exact ordered SU(3) color kernel

Evaluate the ordered color action required by the direct contact.

Preserve the source order of the two generators. Do not replace the general
matrix element by \(C_F\) unless the exact summed diagonal contraction being
evaluated proves that reduction.

Construct independently:

```text
direct ordered fundamental-generator multiplication;

C74 product-color/triplet projection route.
```

Verify:

```text
generator order;

Hermitian-conjugate relation;

triplet closure;

zero anti-sextet and 15 leakage after projection;

agreement of the two routes;

failure of a reversed-generator mutation when the generators do not
commute.
```

Create:

```text
docs/next_level/c79_ordered_color_kernel.json
docs/next_level/c79_ordered_color_validation.json
```

---

# 10. Local transverse-HO contact integral

Derive the finite-HO transverse matrix element of the local contact from the
normalized C45 mode functions and the fixed C57/C77 truncation.

The kernel generally contains the local four-mode overlap appropriate to
the exact C55 operator. Derive its form from the operator rather than
assuming a pair of C53 vertex overlaps.

Implement two independent routes:

```text
factorized analytic/recurrence or exact-mode route;

direct high-order two-dimensional quadrature holdout route.
```

Retain:

```text
all four transverse mode identities;

angular-momentum selection;

shell selection;

phase convention;

exact zero certificate or evaluated nonzero;

quadrature/error certificate;

resolution and b_HO dependence.
```

No numerical threshold may define support.

Create:

```text
docs/next_level/c79_transverse_contact_kernel.json
docs/next_level/c79_transverse_contact_validation.json
```

---

# 11. Finite-cell normalization and \(P^-\to M^2\) conversion

Assemble the longitudinal normalization, transverse integral, spinor
numerator, color factor, and source coefficient first as a bare \(P^-\)
kernel.

Then apply the exact C43/C50 convention:

\[
M^2=2P^+P^- - P_\perp^2.
\]

For the declared total-transverse frame, prove the treatment of
\(P_\perp^2\).

Track all powers and units of:

```text
L;

P-plus;

b_HO;

GeV;

mode-normalization factors;

finite-cell delta functions.
```

Determine analytically whether the auxiliary box length \(L\) cancels from
the \(M^2\) primitive.

Do not set \(L=1\) or absorb a residual length dependence into \(g_s\).

Require the final coefficient of \(g_s^2\) to have the declared
mass-squared units.

Create:

```text
docs/next_level/c79_finite_cell_normalization_contract.json
docs/next_level/c79_pminus_to_m2_conversion_report.json
docs/next_level/c79_dimensional_validation.json
```

---

# 12. Factorized evaluation of the large coordinate domains

The C78 coordinate domains are:

```text
28,606,464;
165,991,250;
697,394,304.
```

These are factorized address spaces, not authorization to allocate three
dense arrays of those lengths.

C79 must:

```text
derive exact factorization by longitudinal, spin/polarization,
transverse, color, and normalization coordinates;

evaluate unique primitive factors once;

cache only content-addressed unique values;

stream or shard the contraction deterministically;

avoid materializing the full Cartesian coordinate domain;

record compression factors and peak memory;

reconstruct selected coordinates directly as holdouts.
```

The physical supported-pair domains are only:

```text
16,224;
43,350;
95,256.
```

The final sparse physical matrix should therefore be assembled over
supported pairs, not over all physical matrix pairs and not over a dense
raw-coordinate tensor.

Create:

```text
docs/next_level/c79_factorized_kernel_plan.json
docs/next_level/c79_kernel_compression_report.json
docs/next_level/c79_resource_and_scaling_report.json
```

A full-domain materialization is a failed implementation, not a readiness
requirement.

---

# 13. Assemble the bare physical contact matrix

For every C78-supported pair \((b,k)\), evaluate:

\[
\left[\widehat M^2_{\mathrm{contact}}\right]_{bk}
=
\sum_\kappa
c_{bk}^{(\kappa)}
\mathcal K^{M^2}_{\kappa},
\]

where \(\widehat M^2_{\mathrm{contact}}\) denotes the coefficient of
\(g_s^2\).

Classify each pair as:

```text
NONZERO_SOURCE_DERIVED_CONTACT_VALUE;

ZERO_BY_EXACT_EVALUATED_KERNEL;

ZERO_BY_EXACT_EVALUATED_CANCELLATION;

UNAVAILABLE_BLOCKING.
```

Do not alter the C78 structural-support status. A C78-supported pair that
evaluates to exact zero remains a structurally supported pair with an
evaluated-zero value status.

Store a deterministic sparse representation with:

```text
row and column physical IDs;

matrix value;

certified absolute bound;

all contributing kernel-coordinate hashes;

C78 support and witness ancestry;

units;

factored-coupling identity.
```

Create:

```text
docs/next_level/c79_contact_matrix_manifest.json
docs/next_level/c79_contact_matrix_value_status.json
```

---

# 14. Independent matrix-free action

Implement an independent action:

```python
apply_bare_iferm_contact(vector, resolution)
```

that evaluates the factorized endpoint/witness/kernel contraction without
multiplying by the stored C79 sparse matrix.

Compare on:

```text
all basis-vector holdouts;

deterministic complex superpositions;

random normalized vectors;

small exact dense subblocks;

all three resolutions.
```

Require agreement within propagated certified bounds.

Create:

```text
docs/next_level/c79_matrix_free_validation.json
```

---

# 15. Hermiticity without post-hoc repair

The direct contact is required to inherit Hermiticity from the source
operator and the independently derived absorption/emission endpoint
relations.

Validate:

\[
M_{\mathrm{contact}}^{2\dagger}
=
M_{\mathrm{contact}}^2
\]

within the declared exact/numerical semantics.

Do not:

```text
replace M by (M+M-dagger)/2;

copy one triangle into the other;

clip imaginary diagonal parts;

or tune a normalization to improve Hermiticity.
```

Report separately:

```text
exact conjugation identities;

numerical Hermiticity residual;

certified Hermiticity bound;

largest offending entry if the bound fails.
```

Create:

```text
docs/next_level/c79_hermiticity_report.json
```

---

# 16. Separate C53 and C58 holdouts

After the C79 matrix and hashes are frozen:

## C53

Prove that C79 is not:

\[
V^\dagger G V,
\]

a sequential two-vertex propagation, or a zero-energy-denominator limit of
C53.

Poison C53 numerical values during C79 construction.

## C58

Preserve the C58 q-sector self-induced-inertia matrix unchanged and
separate.

Verify:

```text
different sector/domain;

different normal-ordered monomial ancestry;

different support identity;

no value or counterterm double counting.
```

Create:

```text
docs/next_level/c79_c53_non_substitution_report.json
docs/next_level/c79_c58_separation_report.json
```

---

# 17. Resolution trajectory and convergence diagnostics

Compare the three bare \(g_s^2\)-factored contact matrices without claiming
a continuum limit.

Report:

```text
matrix dimensions;

structural-support counts;

evaluated nonzero counts;

exact evaluated-zero counts;

Frobenius and operator norms;

selected diagonal/off-diagonal holdouts;

adjacent-resolution comparison-map residuals;

separate longitudinal, shell, b_HO, and numerical-bound effects.
```

Do not fit a continuum constant from three jointly changing resolutions.

Create:

```text
docs/next_level/c79_contact_resolution_report.json
```

---

# 18. Public API and runtime package

Use:

```text
src/deuteron_wigner/bridge/ifcontact2/
data/runtime/c79_ifcontact2/
```

or repository-equivalent paths.

Provide immutable public operations equivalent to:

```python
load_bare_iferm_contact_package(resolution)

contact_kernel_coordinate(kernel_id, resolution)

contact_matrix_element(bra_id, ket_id, resolution)

contact_matrix_row(bra_id, resolution)

apply_bare_iferm_contact(vector, resolution)

contact_value_status(bra_id, ket_id, resolution)
```

Every return must expose:

```text
factored g_s-squared identity;

P-minus and M-squared convention;

units;

value and certified bound;

C78 support ancestry;

kernel-coordinate ancestry;

exact value status.
```

Create one authenticated C79 runtime index/root in this package.

Create:

```text
docs/next_level/c79_api_contract.json
docs/next_level/c79_api_validation.json
docs/next_level/c79_runtime_inventory.json
docs/next_level/c79_deterministic_reconstruction_report.json
```

---

# 19. Isolation and negative controls

Prove C79 construction is independent of:

```text
C53 numerical matrices and propagators;

C58 numerical self-induced-inertia values;

a chosen physical g_s or alpha_s;

a counterterm coefficient;

the historical C57 1e-12 threshold;

historical C47 quadrature residues;

ART25 files.
```

Required failures include mutations of:

```text
overall source coefficient;

field order;

gamma-matrix order;

inverse-partial-plus momentum;

denominator sign;

zero-mode admission;

finite-cell normalization;

P-minus to M-squared factor;

transverse-HO phase;

ordered color-generator product;

fermion sign;

kernel-coordinate equivalence class;

C78 projected coefficient;

C78 support identity;

bound propagation;

post-hoc Hermitianization;

C53 sequential substitution;

C58 self-energy substitution;

physical-coupling insertion.
```

Create at least **384 focused live mutations** of actual operator, kernel,
coordinate, sparse-matrix, and matrix-free objects.

Create:

```text
docs/next_level/c79_isolation_report.json
docs/next_level/c79_regression_report.json
```

---

# 20. Readiness and continuation decisions

Select exactly one branch.

## 20.1 Favorable branch

Issue:

```text
C79_SOURCE_DERIVED_BARE_IFERM_CONTACT_MATRIX_READY
```

Required:

```text
operator coefficient closes by two routes;

inverse-partial-plus prescription closes;

all retained denominators are valid or explicitly excluded;

spinor/polarization numerator closes by two routes;

ordered color kernel closes by two routes;

transverse-HO kernel closes against independent quadrature;

finite-cell normalization and M-squared units close;

large coordinate domains are evaluated factorwise;

all supported physical pairs have terminal value status;

no unavailable entry remains;

sparse and independent matrix-free actions agree;

Hermiticity closes without repair;

C53 non-substitution and C58 separation pass;

deterministic reconstruction and mutations pass.
```

Next:

> **C80/IFERM3 — complete bare instantaneous-fermion operator assembly, sector-specific counterterm directions, and resolution-trajectory closure**

## 20.2 Operator/source convention incomplete

Issue:

```text
C79_IFCONTACT_OPERATOR_CONVENTION_INCOMPLETE
```

Next:

> **C80/IFKERNEL-SRC — repair only the specifically identified source coefficient, field order, gamma order, or convention-map defect**

## 20.3 Inverse derivative or zero-mode incomplete

Issue:

```text
C79_IFCONTACT_INVERSE_DERIVATIVE_INCOMPLETE
```

Next:

> **C80/IFDENOM — repair only the specifically identified \(1/\partial^+\), singular-mode, or boundary defect**

## 20.4 Finite-cell normalization incomplete

Issue:

```text
C79_IFCONTACT_FINITE_CELL_NORMALIZATION_INCOMPLETE
```

Next:

> **C80/IFNORM3 — repair only the specifically identified mode-normalization, box-length, units, or \(P^-\to M^2\) conversion defect**

## 20.5 Kernel evaluation incomplete

Issue:

```text
C79_IFCONTACT_KERNEL_EVALUATION_INCOMPLETE
```

Next:

> **C80/IFKERNEL2 — repair only the spinor, polarization, color, transverse-HO, factorization, or certification defect**

## 20.6 Matrix assembly incomplete

Issue:

```text
C79_IFCONTACT_MATRIX_ASSEMBLY_INCOMPLETE
```

Next:

> **C80/IFMATRIX2 — repair only the sparse aggregation, matrix-free, Hermiticity, or runtime-package defect**

Do not issue a renormalized, complete instantaneous-fermion, local-QCD,
TMD, matching, inference, or production status.

---

# 21. Essential deliverables

Create at least:

```text
docs/next_level/c79_implementation_report.md
docs/next_level/c79_derivation_authority_manifest.json
docs/next_level/c79_input_fidelity_audit.json
docs/next_level/c79_input_freeze.json

docs/next_level/c79_contact_operator_contract.json
docs/next_level/c79_contact_operator_coefficient_validation.json
docs/next_level/c79_kernel_coordinate_vocabulary.json
docs/next_level/c79_kernel_coordinate_equivalence_report.json

docs/next_level/c79_inverse_partial_plus_contract.json
docs/next_level/c79_longitudinal_kernel_validation.json
docs/next_level/c79_spinor_polarization_kernel.json
docs/next_level/c79_spinor_polarization_validation.json
docs/next_level/c79_ordered_color_kernel.json
docs/next_level/c79_ordered_color_validation.json
docs/next_level/c79_transverse_contact_kernel.json
docs/next_level/c79_transverse_contact_validation.json

docs/next_level/c79_finite_cell_normalization_contract.json
docs/next_level/c79_pminus_to_m2_conversion_report.json
docs/next_level/c79_dimensional_validation.json

docs/next_level/c79_factorized_kernel_plan.json
docs/next_level/c79_kernel_compression_report.json
docs/next_level/c79_resource_and_scaling_report.json

docs/next_level/c79_contact_matrix_manifest.json
docs/next_level/c79_contact_matrix_value_status.json
docs/next_level/c79_matrix_free_validation.json
docs/next_level/c79_hermiticity_report.json

docs/next_level/c79_c53_non_substitution_report.json
docs/next_level/c79_c58_separation_report.json
docs/next_level/c79_contact_resolution_report.json

docs/next_level/c79_api_contract.json
docs/next_level/c79_api_validation.json
docs/next_level/c79_runtime_inventory.json
docs/next_level/c79_deterministic_reconstruction_report.json
docs/next_level/c79_isolation_report.json
docs/next_level/c79_readiness_report.json
docs/next_level/c79_regression_report.json
```

Create exactly one next-package contract corresponding to the selected
branch.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

Do not add or modify the old untracked C69 prompt.

---

# 22. Acceptance criteria

C79 is complete only when:

1. Baseline `1ddf21c230d3a16ee7e52ed09d84140f43781bb8` reproduces.
2. Both required untracked paths remain untouched.
3. C43/C50/C55/C57/C58/C77/C78 historical artifacts remain unchanged.
4. C78 support imports and freezes before values are evaluated.
5. The exact direct-contact operator coefficient closes by two routes.
6. \(g_s^2\) remains factored.
7. No physical coupling is selected.
8. The inverse-\(\partial^+\) momentum and sign are source derived.
9. Singular and zero-mode channels are handled exactly.
10. No sequential C53 energy denominator is used.
11. Spinor/polarization numerators close by two routes.
12. Ordered color closes by two routes.
13. General color is not reduced improperly to \(C_F\).
14. Transverse-HO integrals close against independent quadrature.
15. Exact zeros use no numerical threshold.
16. Finite-cell normalization and units close.
17. Any auxiliary \(L\) dependence is derived, not set by convention.
18. The \(P^-\to M^2\) conversion is exact.
19. The enormous coordinate domains remain factorized.
20. No full coordinate-domain dense array is materialized.
21. Every C78-supported physical pair has a terminal evaluated-value status.
22. No unavailable pair remains in the favorable branch.
23. Sparse and independent matrix-free actions agree.
24. Hermiticity closes without post-hoc repair.
25. C53 numerical values and propagators are absent from construction.
26. C58 remains unchanged and separate.
27. Resolution comparisons do not claim a continuum limit.
28. Runtime package and API reconstruct deterministically.
29. At least 384 focused live mutations pass.
30. No counterterm, renormalized operator, complete instantaneous-fermion operator, local-QCD Hamiltonian, TMD/matching, fit, inference, or production object is created.
31. `NO_JOINT_MEASURE`, 216 routes, 642 ART25 identities, and authoritative artifacts remain unchanged.
32. The working tree is clean except for the two pre-existing untracked paths.
33. A local completion commit is created and not pushed.

Do not weaken source ordering, denominator identity, finite-cell
normalization, ordered color, exact transverse projection, bound
propagation, factorized assembly, or Hermiticity to open the gate.

---

# 23. Final Codex response

Report:

- starting and final commits;
- untouched untracked paths;
- C78 package/root identity and imported support counts;
- operator/source identities;
- overall \(g_s^2\)-factored coefficient result;
- inverse-\(\partial^+\) prescription and minimum denominator magnitude;
- longitudinal-kernel identities;
- spinor/polarization route agreement;
- ordered-color route agreement;
- transverse-HO route agreement and maximum quadrature bound;
- finite-cell normalization and box-length cancellation/status;
- \(P^-\to M^2\) conversion and final units;
- raw coordinate-domain, unique-factor, and compression counts;
- peak-memory and streaming/sharding results;
- physical matrix shapes;
- structural-support, evaluated-nonzero, exact-kernel-zero, and exact-cancellation counts;
- sparse nnz;
- matrix norms;
- sparse-versus-matrix-free residuals and bounds;
- Hermiticity residual and bound;
- C53 non-substitution and C58 separation;
- adjacent-resolution diagnostics;
- deterministic reconstruction;
- isolation and mutation results;
- exact readiness/no-go status;
- exact next branch;
- confirmation that no physical coupling, counterterm, renormalized or complete instantaneous-fermion operator, TMD/matching, fit, inference, or production object was created;
- confirmation that nothing was pushed.
