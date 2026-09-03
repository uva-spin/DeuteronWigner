# C81/IFCONTACT3 Codex Work Package

## Title

**Bare direct instantaneous-fermion contact matrix from immutable C78 support and the immutable C80 four-mode evaluator: exact kernel-class aggregation, certified sparse and matrix-free actions, source-derived Hermiticity, and C82 complete-operator handoff**

## Authoritative baseline

Start from the clean local C80 completion commit:

```text
0868a88422380339d9d5e0631830ba7528bd776f
```

Before changing tracked files, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "0868a88422380339d9d5e0631830ba7528bd776f"
```

The following pre-existing untracked paths must remain untouched and outside Git:

```text
MSHT20_REP/
docs/next_level/c69_qgembed5_codex_prompt.md
```

Do not add, modify, remove, rename, stage, or consume either path as scientific authority.

The baseline is authoritative only when it contains and reproduces:

```text
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY

C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY

C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY

C80_EXACT_SOURCE_CHAIN_DERIVED_IFCONTACT_KERNEL_EVALUATOR_READY
```

and the exact inherited C78/C80 results:

```text
C78 physical qg dimensions:
    1,344 / 2,700 / 4,752;

C78 retained-q dimension:
    6 / 6 / 6;

C78 ordered absorption edges:
    312 / 510 / 756;

C78 ordered emission edges:
    312 / 510 / 756;

C78 raw endpoint paths on each side:
    13,056 / 31,450 / 64,464;

C78 supported physical pairs:
    16,224 / 43,350 / 95,256;

C78 factorized kernel-coordinate address spaces:
    28,606,464 / 165,991,250 / 697,394,304;

C78 undecidable, duplicate-witness, and missing-ancestry counts:
    all zero;

C80 raw-coordinate coefficient:
    -delta_K / [4 pi (k_q + k_g)]
    before spin, ordered color, and four-HO factors;

C80 longitudinal result:
    auxiliary L cancels exactly;
    minimum admitted inverse-partial-plus channel is 3/2;
    zero modes remain excluded by the frozen PV/Q0 policy;

C80 transverse result:
    exact finite Laguerre/Gamma four-HO expression;
    independent Gauss-Laguerre validation;
    maximum reported pilot bound approximately 3.6e-15;

C80 spin and ordered-color pilots:
    independent routes close with zero reported residual;

C80 coupling and invariant-mass semantics:
    g_s^2 remains explicitly factored;
    P-minus to M-squared is the exact 2 P-plus P-minus map in the
    fixed P-perp=0 frame;

C80 runtime:
    authenticated deterministic factorized evaluator;
    no physical-pair aggregation;
    no contact matrix.
```

Verify all actual counts, hashes, coordinate schemas, support records,
evaluator statuses, interval conventions, and public APIs from the
repository. This prompt is not numerical authority.

Create a local completion commit. Do not push.

---

# 1. Authority and scientific boundary

C81 is an exact project-derived composition of two already authenticated
scientific objects:

```text
C78:
    exact source-ordered structural coefficients and physical-pair
    support;

C80:
    exact/certified value of every independent raw contact-kernel
    coordinate.
```

No new external authority is required for:

```text
grouping equal authenticated kernel coordinates;
multiplying C78 projected coefficients by C80 kernel values;
performing exact symbolic sums;
assembling a sparse matrix;
constructing a matrix-free action;
assigning canonical matrix-entry IDs;
or serializing the result.
```

External authority would be required only if C81 changed the frozen
operator, regulator, normalization, or physical coupling. C81 must do none
of those things.

C81 must keep \(g_s^2\) explicit and factored. It constructs the bare
matrix coefficient

\[
\widehat M^{2}_{\rm contact,R}
\equiv
\frac{M^{2,\rm bare}_{\rm contact,R}}{g_s^2}.
\]

C81 must not choose:

```text
g_s;
alpha_s;
a renormalization scale;
a subtraction;
a counterterm coefficient;
a fitted normalization;
or a continuum extrapolation.
```

The strongest positive status is:

```text
C81_SOURCE_DERIVED_BARE_IFERM_CONTACT_MATRIX_READY
```

The exact favorable continuation is:

> **C82/IFERM3 — assemble the complete bare instantaneous-fermion operator from the immutable C58 self-induced-inertia block and the immutable C81 direct-contact block, type sector-specific counterterm directions, and issue the next local-HQCD gate**

---

# 2. Exact purpose and stopping point

For every resolution \(R\) and every C78-supported physical pair
\((b,k)\), C81 must evaluate

\[
\left[\widehat M^{2}_{\rm contact,R}\right]_{bk}
=
\sum_{\kappa\in\mathcal K_{bk}}
c_{bk}^{(\kappa)}
\widehat{\mathcal K}^{M^2}_{R,\kappa},
\]

where:

```text
c_bk^(kappa):
    the immutable exact/certified projected coefficient from C78;

Khat_R,kappa^(M2):
    the immutable coefficient of g_s^2 returned by C80;

K_bk:
    the exact source-ordered coordinate set attached to the
    physical pair by C78.
```

C81 must produce:

```text
a terminal value status for every C78-supported physical pair;

a deterministic sparse P-minus contact matrix coefficient;

a deterministic sparse M-squared contact matrix coefficient;

an independent factorized matrix-free action;

certified numerical bounds;

source-derived Hermiticity closure;

a public immutable runtime/API package;

and a C82 import contract.
```

C81 must not:

```text
change C78 structural support after evaluating values;

materialize the full C78 coordinate Cartesian domains;

replace the contact by C53 sequential propagation;

replace or add the C58 self-induced-inertia block;

select a physical coupling;

solve a counterterm;

assemble the complete instantaneous-fermion operator;

or create a TMD, matching, fit, inference, or production object.
```

---

# 3. Mandatory inputs

Read completely the actual repository equivalents of:

```text
C58:
    q-sector bare self-induced-inertia matrix;
    IFNORM2-ORDERED-JOINT-SUPPORT;
    admitted-mode ledgers;
    qg counterterm-only scope;
    separation from the direct contact;

C77:
    physical qg basis;
    physical-to-raw embedding;
    raw-to-physical projection;
    canonical basis IDs and ordering;

C78:
    physical-pair support;
    endpoint and witness relations;
    independent kernel-coordinate IDs;
    exact projected coefficient vectors;
    exact projected-cancellation records;
    support ancestry;
    public support API;

C80:
    kernel-coordinate schema;
    factor-level primitive tables;
    exact/certified P-minus and M-squared evaluator;
    interval convention;
    exact-zero statuses;
    public API;
    runtime root;
    deterministic reconstruction;

C53:
    read-only canonical-vertex result for post-construction
    non-substitution controls only.
```

Create:

```text
docs/next_level/c81_derivation_authority_manifest.json
docs/next_level/c81_input_fidelity_audit.json
```

---

# 4. Freeze C78 and C80 before aggregation

Consume C78 and C80 only through their authenticated immutable public APIs.

Verify and freeze:

```text
C78 package/root;
C80 package/root;

all three resolution identities;

physical qg basis order;

all supported physical-pair IDs;

all witness and kernel-coordinate IDs;

all projected coefficient values, exact records, and bounds;

all C80 terminal coordinate statuses;

all C80 P-minus and M-squared values and bounds;

all source, operator, regulator, and convention identities.
```

Issue:

```text
C81_INPUTS_FROZEN_COMPLETE
```

in:

```text
docs/next_level/c81_input_freeze.json
```

After this freeze:

```text
do not change support;
do not merge or split C78 coordinates based on evaluated values;
do not change the C80 evaluator;
do not repair Hermiticity by changing entries;
do not introduce a physical coupling.
```

---

# 5. Canonical matrix-entry domain

Create an immutable matrix-entry record for every C78-supported pair.

Each record must retain:

```text
resolution;
physical bra ID;
physical ket ID;
row and column indices;
C78 structural-support status;
ordered witness IDs;
ordered kernel-coordinate IDs;
projected-coefficient identities;
C80 evaluator identities;
factored-coupling identity;
P-minus/M-squared convention;
canonical matrix-entry ID.
```

Do not construct entries for structurally unsupported pairs merely to
store numerical zeros. Unsupported pairs remain represented by the C78
support API.

Create:

```text
docs/next_level/c81_contact_matrix_entry_manifest.json
docs/next_level/c81_contact_matrix_entry_validation.json
```

Require:

```text
entry counts reproduce the C78 supported-pair counts;
no duplicate pair;
no missing supported pair;
no unsupported pair promoted into the sparse domain.
```

---

# 6. Exact kernel-equivalence aggregation

The C78 coordinate domains are factorized address spaces. C81 must not
iterate or materialize them as dense Cartesian arrays.

Construct exact equivalence classes using the immutable C80 kernel-value
identity:

\[
\kappa_1\sim\kappa_2
\quad\Longleftrightarrow\quad
\text{C80 proves they share one exact kernel object}.
\]

For each physical pair define the exact class coefficient

\[
C_{bk}^{[\lambda]}
=
\sum_{\kappa\in\lambda\cap\mathcal K_{bk}}
c_{bk}^{(\kappa)}.
\]

Then evaluate

\[
\left[\widehat M^2_{\rm contact}\right]_{bk}
=
\sum_{\lambda}
C_{bk}^{[\lambda]}
\widehat{\mathcal K}^{M^2}_{\lambda}.
\]

Requirements:

```text
equivalence classes descend from C80 identity, never floating
equality;

projected coefficients are summed exactly or through their
authenticated symbolic representation before numerical evaluation;

source-distinct kernel classes remain distinct even when their
current numerical values coincide;

exactly identical kernel classes are not reevaluated per witness;

all class and entry ancestries remain reversible.
```

Create:

```text
docs/next_level/c81_kernel_class_aggregation_plan.json
docs/next_level/c81_kernel_class_inventory.json
docs/next_level/c81_kernel_class_aggregation_validation.json
```

Report:

```text
raw coordinate counts;
unique C80 kernel-class counts;
pair-local nonempty class counts;
compression factors;
cache-hit rates;
peak memory;
deterministic shard strategy.
```

---

# 7. Exact and certified arithmetic

For each term with projected coefficient
\(c\pm\delta c\) and kernel value \(K\pm\delta K\), propagate a rigorous
product bound at least as conservative as

\[
\delta(cK)
\le
|c|\,\delta K
+
|K|\,\delta c
+
\delta c\,\delta K.
\]

For each matrix entry, propagate the sum bound using a rigorous accumulated
enclosure. Do not use observed cancellation to reduce the bound unless an
exact symbolic cancellation has already been proved.

Where exact symbolic forms are available:

```text
combine exact expressions first;
simplify only through declared algebraic identities;
then evaluate numerically with directed or certified bounds.
```

Where only certified values are available:

```text
retain the interval result;
do not call an interval-overlapping-zero entry an exact zero.
```

Create:

```text
docs/next_level/c81_contact_arithmetic_contract.json
docs/next_level/c81_contact_bound_propagation_report.json
```

---

# 8. Terminal value semantics

Assign exactly one terminal value status to every C78-supported pair:

```text
NONZERO_EXACT_SOURCE_DERIVED_CONTACT_VALUE;

NONZERO_CERTIFIED_CONTACT_VALUE_INTERVAL_EXCLUDES_ZERO;

NONZERO_SYMBOLIC_CONTACT_VALUE_INTERVAL_INCLUDES_ZERO;

ZERO_BY_EXACT_KERNEL_VALUE;

ZERO_BY_EXACT_EVALUATED_PAIR_CANCELLATION;

CERTIFIED_NUMERICAL_VALUE_INTERVAL_INCLUDES_ZERO_NO_EXACT_ZERO;

UNAVAILABLE_BLOCKING.
```

Interpretation:

```text
structural support remains the immutable C78 status;

value status describes the result of applying C80;

a structurally supported pair may evaluate to exact zero;

an interval containing zero is not an exact-zero certificate;

UNAVAILABLE_BLOCKING is reserved for a genuine evaluator or
aggregation failure.
```

A favorable C81 gate requires:

```text
UNAVAILABLE_BLOCKING = 0.
```

Create:

```text
docs/next_level/c81_contact_matrix_value_status.json
docs/next_level/c81_contact_value_status_validation.json
```

---

# 9. Low-shell direct-aggregation pilot

Before full assembly, evaluate a frozen low-shell set containing:

```text
one diagonal supported pair;
one off-diagonal supported pair;
one pair with multiple witness paths;
one pair whose kernel contribution is exactly zero;
one pair with exact evaluated cancellation when available;
one Hermitian-conjugate pair;
one pair at each resolution.
```

For every pilot report:

```text
C78 witness and projected-coefficient records;
C80 kernel-coordinate values;
class aggregation;
exact/symbolic expression;
P-minus result;
M-squared result;
certified bound;
terminal value status.
```

Create:

```text
docs/next_level/c81_low_shell_contact_matrix_pilot.json
```

---

# 10. Independent raw-space reconstruction holdouts

Implement an independent validation route for frozen low- and mid-shell
pairs.

The route must:

```text
load the physical bra and ket from C77;
expand them independently into raw components;
apply the C80 four-mode kernel directly to source-ordered raw paths;
sum over retained-q witnesses without consuming the C81 aggregated
entry;
project back to the physical pair;
compare with the C81 pair result.
```

It may consume C78 only to select frozen physical pairs after construction;
it must not consume the C78 pair coefficient vector as its numerical
aggregation input.

Create:

```text
docs/next_level/c81_independent_raw_space_reconstruction.json
```

This route is a matrix-value oracle, not a redefinition of support.

---

# 11. Sparse P-minus and M-squared matrices

Assemble deterministic sparse matrices for the coefficient of \(g_s^2\):

\[
\widehat P^-_{\rm contact,R},
\qquad
\widehat M^2_{\rm contact,R}.
\]

Store:

```text
physical qg row/column basis IDs;
CSR or equivalent deterministic sparse arrays;
entry values;
entry bounds;
entry value statuses;
C78 support hashes;
C80 kernel hashes;
factored-coupling identity;
units;
P-plus and P-perp frame identities.
```

Verify entrywise:

\[
\widehat M^2_{\rm contact,R}
=
2P_R^+\widehat P^-_{\rm contact,R}
\]

in the fixed \(P_\perp=0\) frame under the exact C80 convention.

Do not store a matrix with \(g_s^2\) numerically multiplied in.

Create:

```text
docs/next_level/c81_sparse_contact_matrix_manifest.json
docs/next_level/c81_pminus_m2_matrix_conversion_report.json
```

---

# 12. Independent matrix-free action

Implement:

```python
apply_bare_iferm_contact_coefficient(
    vector,
    resolution,
)
```

that evaluates the C78 witness/kernel contraction through C80 primitives
without multiplying by the stored C81 sparse matrix.

The matrix-free route must use an independently organized execution path,
for example:

```text
endpoint/witness streaming;
kernel-class lookup;
pair-local exact coefficient accumulation;
direct output-vector scatter.
```

Compare sparse and matrix-free actions on:

```text
all frozen basis-vector holdouts;
deterministic complex superpositions;
random normalized complex vectors;
small exact dense subblocks;
all three resolutions.
```

Create:

```text
docs/next_level/c81_matrix_free_contact_validation.json
```

---

# 13. Hermiticity and diagonal reality without repair

The direct contact must inherit Hermiticity from:

```text
the source operator;
the independent C78 absorption/emission relations;
the C80 conjugation identities;
the C77 physical embedding.
```

Prove the exact pair map

\[
(b,k,\lambda)
\longleftrightarrow
(k,b,\bar\lambda)
\]

with the appropriate conjugation of projected coefficients and kernel
values.

Validate:

\[
\widehat M^{2\dagger}_{\rm contact}
=
\widehat M^2_{\rm contact}.
\]

Report:

```text
exact conjugation-pair closure;
maximum numerical Hermiticity residual;
certified Hermiticity bound;
maximum imaginary diagonal residual;
largest offending entry if any bound fails.
```

Do not:

```text
replace M by (M+M-dagger)/2;
copy one triangle into the other;
discard imaginary parts;
clip entries;
or tune a factor.
```

Create:

```text
docs/next_level/c81_contact_hermiticity_report.json
```

A favorable status requires Hermiticity to close without repair.

---

# 14. Matrix diagnostics without false physical claims

For each resolution report:

```text
matrix dimension;
C78 structural-support count;
evaluated exact-nonzero count;
certified nonzero count;
exact evaluated-kernel-zero count;
exact evaluated-cancellation count;
interval-includes-zero count;
sparse nnz;
density;
Frobenius norm;
operator-norm estimate;
maximum diagonal magnitude;
maximum off-diagonal magnitude;
Hermiticity residual;
matrix-free residual.
```

Compute selected eigenvalue diagnostics only as finite-resolution bare
operator diagnostics. Do not claim positivity, boundedness below, a
physical spectrum, or a continuum limit.

Create:

```text
docs/next_level/c81_contact_matrix_diagnostics.json
docs/next_level/c81_contact_resolution_comparison.json
```

The resolution comparison must separate changes in:

```text
K;
Nmax;
b_HO;
physical basis dimension;
support;
kernel primitives;
and numerical certification.
```

Do not fit a continuum value from three jointly changing resolutions.

---

# 15. C53 and C58 non-substitution/separation

After the C81 matrices and hashes are frozen:

## C53

Poison all C53 numerical values and any propagator/resolvent interfaces.

Prove that C81 is not:

\[
V^\dagger G V,
\]

not a sequential pair of canonical vertices, and not a zero-denominator
limit of C53.

## C58

Preserve C58 byte-identically as the separate self-induced-inertia block.

Verify:

```text
C58 acts on the retained q sector;
C81 acts on the physical qg sector;
the monomial ancestries differ;
the support identities differ;
no value, entry, mode, or future counterterm direction is counted
twice.
```

Create:

```text
docs/next_level/c81_c53_non_substitution_report.json
docs/next_level/c81_c58_separation_report.json
```

---

# 16. Public API and runtime package

Use:

```text
src/deuteron_wigner/bridge/ifcontact3/
data/runtime/c81_ifcontact3/
```

or exact repository-equivalent paths.

Provide immutable public operations equivalent to:

```python
load_bare_iferm_contact_matrix_package(resolution)

contact_matrix_value_status(bra_id, ket_id, resolution)

contact_matrix_element_coefficient(bra_id, ket_id, resolution)

contact_matrix_row_coefficient(bra_id, resolution)

apply_bare_iferm_contact_coefficient(vector, resolution)

load_sparse_contact_matrix_coefficient(resolution)
```

Every returned result must expose:

```text
coefficient-of-g_s^2 status;
P-minus and M-squared values;
certified bounds;
units;
C78 structural-support ancestry;
C80 kernel ancestry;
matrix-entry identity;
terminal value status.
```

All NumPy loads must explicitly use:

```python
allow_pickle=False
```

Reject object dtype, unsafe paths, unindexed files, writable arrays, and
mutable records.

Create one authenticated C81 runtime index/root in this package.

Create:

```text
docs/next_level/c81_api_contract.json
docs/next_level/c81_api_validation.json
docs/next_level/c81_runtime_inventory.json
docs/next_level/c81_deterministic_reconstruction_report.json
```

---

# 17. C82 import contract

Define the exact immutable contract by which C82 consumes:

```text
the C58 self-induced-inertia package;
the C81 direct-contact package;
their sector domains;
their basis orders;
their g_s^2-factor conventions;
their P-minus/M-squared conventions;
their sparse and matrix-free actions;
their bounds;
their monomial and support ancestry;
their non-overlap certificate.
```

C82 must not:

```text
recompute C58 or C81;
choose a physical coupling;
identify a counterterm coefficient;
lift the q block into qg;
lift the qg block into q;
or add a sequential C53 contribution.
```

Create:

```text
docs/next_level/c81_c82_iferm3_import_contract.json
```

---

# 18. Deterministic execution and scaling

The assembly must remain sparse and factorized.

Requirements:

```text
never materialize the full C78 coordinate domains;
never materialize a dense physical matrix except tiny holdout
subblocks;
evaluate unique C80 kernel classes once;
use deterministic pair and coordinate order;
use stable exact or certified accumulation;
support serial, deterministic sharded, and restart execution;
record peak memory and runtime scaling.
```

Run:

```text
two consecutive complete builds;
one clean build;
one serial build;
one supported parallel/sharded build;
one restart build.
```

Require byte-identical runtime and tracked artifacts.

Create:

```text
docs/next_level/c81_resource_and_scaling_report.json
```

---

# 19. Isolation and negative controls

Prove C81 construction is independent of:

```text
a physical g_s or alpha_s;
a counterterm;
C53 numerical values and propagators;
C58 numerical values;
the historical C57 1e-12 threshold;
C47 quadrature residues;
ART25 files.
```

Required failures include mutations of:

```text
C78 pair support;
C78 projected coefficient;
C78 kernel-coordinate identity;
C80 kernel value;
C80 bound;
kernel-equivalence class;
pair-local class coefficient;
P-minus/M-squared conversion;
basis order;
row/column ID;
exact-zero classification;
bound accumulation;
deterministic accumulation order;
Hermitian-conjugate mapping;
post-hoc symmetrization;
physical-coupling insertion;
C53 substitution;
C58 substitution;
unsafe NumPy loading;
mutable return.
```

Create at least **384 focused live mutations** of actual pair, class,
matrix, bound, sparse, matrix-free, and runtime objects.

Create:

```text
docs/next_level/c81_isolation_report.json
docs/next_level/c81_regression_report.json
```

---

# 20. Readiness and continuation decisions

Select exactly one branch.

## 20.1 Favorable branch

Issue:

```text
C81_SOURCE_DERIVED_BARE_IFERM_CONTACT_MATRIX_READY
```

Required:

```text
all C78-supported pairs are imported exactly once;
all C80 coordinates needed by those pairs have terminal evaluator
values;
kernel classes are exact and complete;
every pair has a terminal value status;
UNAVAILABLE_BLOCKING = 0;
P-minus and M-squared matrices close under the C80 conversion;
sparse and independent matrix-free actions agree;
independent raw-space holdouts agree;
Hermiticity and diagonal reality close without repair;
C53 non-substitution passes;
C58 separation passes;
runtime/API/determinism/mutations pass.
```

Next:

> **C82/IFERM3 — complete bare instantaneous-fermion operator assembly, sector-specific counterterm-direction typing, and local-HQCD continuation gate**

## 20.2 Pair aggregation incomplete

```text
C81_IFCONTACT_PAIR_AGGREGATION_INCOMPLETE
```

Next:

> **C82/IFAGG — repair only the specifically identified C78 coefficient, C80 coordinate, kernel-class, or pair-value aggregation defect**

## 20.3 Numerical certification incomplete

```text
C81_IFCONTACT_MATRIX_CERTIFICATION_INCOMPLETE
```

Next:

> **C82/IFMATCERT — repair only the specifically identified interval, bound, exact-zero, sparse/matrix-free, or precision defect**

## 20.4 Hermiticity incomplete

```text
C81_IFCONTACT_HERMITICITY_INCOMPLETE
```

Next:

> **C82/IFHERMIT — repair only the specifically identified conjugation, endpoint, kernel, phase, or matrix-assembly defect**

## 20.5 Runtime/API incomplete

```text
C81_IFCONTACT_PUBLIC_MATRIX_INCOMPLETE
```

Next:

> **C82/IFMATRIXAPI — repair only the specifically identified sparse storage, loader, API, determinism, or restart defect**

Do not issue a complete-instantaneous-fermion, counterterm-solved,
renormalized, local-QCD, TMD, matching, inference, or production status.

---

# 21. Essential deliverables

Create at least:

```text
docs/next_level/c81_implementation_report.md
docs/next_level/c81_derivation_authority_manifest.json
docs/next_level/c81_input_fidelity_audit.json
docs/next_level/c81_input_freeze.json

docs/next_level/c81_contact_matrix_entry_manifest.json
docs/next_level/c81_contact_matrix_entry_validation.json
docs/next_level/c81_kernel_class_aggregation_plan.json
docs/next_level/c81_kernel_class_inventory.json
docs/next_level/c81_kernel_class_aggregation_validation.json

docs/next_level/c81_contact_arithmetic_contract.json
docs/next_level/c81_contact_bound_propagation_report.json
docs/next_level/c81_contact_matrix_value_status.json
docs/next_level/c81_contact_value_status_validation.json
docs/next_level/c81_low_shell_contact_matrix_pilot.json
docs/next_level/c81_independent_raw_space_reconstruction.json

docs/next_level/c81_sparse_contact_matrix_manifest.json
docs/next_level/c81_pminus_m2_matrix_conversion_report.json
docs/next_level/c81_matrix_free_contact_validation.json
docs/next_level/c81_contact_hermiticity_report.json
docs/next_level/c81_contact_matrix_diagnostics.json
docs/next_level/c81_contact_resolution_comparison.json

docs/next_level/c81_c53_non_substitution_report.json
docs/next_level/c81_c58_separation_report.json
docs/next_level/c81_api_contract.json
docs/next_level/c81_api_validation.json
docs/next_level/c81_runtime_inventory.json
docs/next_level/c81_deterministic_reconstruction_report.json
docs/next_level/c81_resource_and_scaling_report.json
docs/next_level/c81_c82_iferm3_import_contract.json

docs/next_level/c81_isolation_report.json
docs/next_level/c81_readiness_report.json
docs/next_level/c81_regression_report.json
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

C81 is complete only when:

1. Baseline `0868a88422380339d9d5e0631830ba7528bd776f` reproduces.
2. Both protected untracked paths remain untouched.
3. C58/C77/C78/C80 historical artifacts remain unchanged.
4. C78 and C80 package roots verify and freeze before aggregation.
5. Every C78-supported pair appears exactly once.
6. No unsupported pair is added to the sparse domain.
7. Kernel equivalence is based only on C80 exact identity.
8. No floating-value equality defines a kernel class.
9. Exact projected coefficients are aggregated before numerical evaluation where available.
10. All C80 values remain coefficients of factored \(g_s^2\).
11. No physical coupling is selected.
12. Product and sum bounds are propagated rigorously.
13. Exact zeros are distinguished from intervals containing zero.
14. Every supported pair has one terminal value status.
15. `UNAVAILABLE_BLOCKING` is zero in the favorable branch.
16. The low-shell aggregation pilot closes.
17. Independent raw-space holdouts agree.
18. Sparse P-minus and M-squared matrices are constructed.
19. Their exact \(2P^+\) conversion closes.
20. The full coordinate domains are never materialized densely.
21. Dense physical matrices are not required.
22. Sparse and independent matrix-free actions agree.
23. Hermiticity closes without repair.
24. Diagonal reality closes within certified bounds.
25. C53 is not used as a sequential substitute.
26. C58 remains unchanged and separate.
27. Resolution diagnostics make no continuum claim.
28. The public API returns immutable safe objects.
29. Deterministic serial, clean, sharded, and restart builds agree.
30. At least 384 focused live mutations pass.
31. No counterterm, complete instantaneous-fermion operator, local-QCD Hamiltonian, TMD/matching, fit, inference, or production object is created.
32. `NO_JOINT_MEASURE`, 216 routes, 642 ART25 identities, and authoritative artifacts remain unchanged.
33. The working tree is clean except for the two protected untracked paths.
34. A local completion commit is created and not pushed.

Do not weaken exact class identity, pairwise source ancestry, interval
arithmetic, P-minus/M-squared conversion, sparse/matrix-free independence,
or Hermiticity to open the gate.

---

# 23. Final Codex response

Report:

- starting and final commits;
- untouched untracked paths;
- C78 and C80 package/root identities;
- imported supported-pair and coordinate counts;
- unique kernel-class counts and compression factors;
- peak memory and execution strategy;
- physical matrix shapes;
- structural-support counts;
- exact nonzero, certified nonzero, exact kernel-zero, exact cancellation, and interval-includes-zero counts;
- sparse nnz and density;
- P-minus/M-squared conversion residual;
- maximum matrix-entry bound;
- independent raw-space holdout residuals;
- sparse-versus-matrix-free residuals and bounds;
- Hermiticity and diagonal-reality residuals and bounds;
- matrix norms and finite-resolution diagnostics;
- C53 non-substitution and C58 separation;
- runtime/API and deterministic-reconstruction hashes;
- isolation and mutation results;
- exact readiness/no-go status;
- exact next branch;
- confirmation that \(g_s^2\) remains factored and no physical coupling, counterterm, complete instantaneous-fermion operator, local-QCD Hamiltonian, TMD/matching, fit, inference, or production object was created;
- confirmation that nothing was pushed.
