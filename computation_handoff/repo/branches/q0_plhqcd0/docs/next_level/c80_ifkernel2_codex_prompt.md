# C80/IFKERNEL2 Codex Work Package

## Title

**Exact source-chain-derived finite-cell four-mode evaluator for the direct instantaneous-fermion contact: operator insertion, inverse-\(\partial^+\) channel, two-gluon spin/polarization numerator, ordered SU(3) color, analytic four-HO overlap, certified public API, and C81 matrix handoff**

## Authoritative baseline

Start from the clean local C79 completion commit:

```text
66e57dfd7d4e5a3f213d085dac2481c4a4ab0a2d
```

Before changing tracked files, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
test "$(git rev-parse HEAD)" = "66e57dfd7d4e5a3f213d085dac2481c4a4ab0a2d"
```

The following pre-existing untracked paths must remain untouched and outside Git:

```text
MSHT20_REP/
docs/next_level/c69_qgembed5_codex_prompt.md
```

Do not add, modify, remove, rename, stage, or consume either path as scientific authority.

Read completely and preserve the committed continuation contract:

```text
docs/next_level/c80_ifkernel2_contract.md
```

This work package supplies the executable derivation and validation plan for
that contract. It must not weaken any scientific boundary frozen there.

The baseline is authoritative only when it contains and reproduces:

```text
C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION
C45_SOURCE_DERIVED_MODE_PROJECTION_READY
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
C77_EXACT_SOURCE_CHAIN_DERIVED_QG_EMBEDDING_READY
C78_SOURCE_DERIVED_IFERM_CONTACT_SUPPORT_READY
C79_IFCONTACT_KERNEL_EVALUATION_INCOMPLETE
```

and the exact C79 finding:

```text
C78 support:
    authenticated and frozen;

C43/C55 source-level W3 coefficient:
    re-closed by both available symbolic routes;

missing object:
    a finite-cell four-mode evaluator for the direct
    b-dagger a-dagger a b contact;

C50:
    a distinct three-mode canonical q-to-qg vertex evaluator;
    not a substitute for the direct contact's measure,
    two-gluon spin/polarization contraction,
    ordered color product, or four-HO integral;

not created:
    contact value;
    sparse or matrix-free contact matrix;
    physical coupling;
    counterterm;
    renormalized operator;
    C53 sequential-propagation substitute;
    C58 self-induced-inertia substitute.
```

Verify all actual equations, hashes, conventions, basis identities, and
public APIs from the repository. This prompt is not numerical authority.

Create a local completion commit. Do not push.

---

# 1. Authority policy

C80 must apply the authority hierarchy established in C77.

## 1.1 External primary authority is required for

```text
the light-front QCD instantaneous-fermion operator;
the constrained-field solution from which it follows;
the field order and overall sign;
the inverse-partial-plus prescription;
the physical meaning of the finite longitudinal cell;
the light-front normalization convention.
```

Those authorities are already frozen by C43 and C55. Do not replace them
with a different convention merely because another source is prominent.

## 1.2 Exact project-derived authority is sufficient for

```text
inserting the frozen C45 mode expansions into the frozen operator;
deriving the finite-cell Kronecker factors;
deriving the four-mode transverse-HO integral;
assigning canonical kernel-coordinate IDs;
constructing exact finite sums and recurrence relations;
factorizing and caching primitive values;
serializing the evaluator;
and exposing a safe public API.
```

The repository does **not** need a paper that publishes its exact
finite-HO sparse ordering. The evaluator is a mathematical consequence of
the source-locked operator and source-locked mode basis.

## 1.3 Fail closed only for a physical ambiguity

A no-go is valid when the frozen operator and mode conventions leave a
physically consequential normalization, denominator, gamma ordering, color
ordering, or measure genuinely undetermined, or when two independent
derivations contradict one another.

Do not fail closed merely because a pre-existing evaluator is absent. The
purpose of C80 is to derive and implement it.

---

# 2. Scientific purpose and exact stopping point

C80 must construct an immutable evaluator

\[
\mathcal K^{P^-}_{R,\kappa}
\quad\text{and}\quad
\mathcal K^{M^2}_{R,\kappa}
\]

for each independent direct-contact kernel coordinate \(\kappa\) defined by
C78.

The evaluator must return the coefficient of the explicitly factored
coupling \(g_s^2\) for the normal-ordered monomial

\[
b^\dagger a^\dagger a b.
\]

It must contain:

```text
the exact operator coefficient;
the exact longitudinal conservation and inverse-partial-plus factor;
the two-gluon spin/polarization numerator;
the ordered SU(3) color matrix element;
the local four-mode transverse-HO overlap;
the finite-cell normalization;
the P-minus to M-squared conversion;
a certified numerical enclosure;
and complete ancestry.
```

C80 must not aggregate these kernel values with the C78 projected
coefficients into a physical contact matrix. That is the next package.

C80 must not choose:

```text
a physical g_s or alpha_s;
a renormalization scale;
a subtraction;
a counterterm coefficient;
a fitted normalization;
a sequential C53 propagator;
or a C58 self-induced-inertia value.
```

Preferred positive status:

```text
C80_EXACT_SOURCE_CHAIN_DERIVED_IFCONTACT_KERNEL_EVALUATOR_READY
```

If the committed `c80_ifkernel2_contract.md` freezes a different exact
positive-status spelling, preserve that spelling and record an explicit
alias relation to the status above.

The positive continuation is:

> **C81/IFCONTACT3 — evaluate and assemble the bare direct instantaneous-fermion contact matrix on the immutable C78 support using the immutable C80 evaluator**

---

# 3. Mandatory inputs

Read completely the actual repository equivalents of:

```text
C43:
    G0 light-front-gauge action;
    constrained-fermion solution;
    instantaneous-fermion operator;
    canonical brackets;
    inverse-partial-plus and zero-mode policy;
    finite-volume convention;

C45:
    longitudinal field modes;
    coordinate- and momentum-space 2D-HO modes;
    normalization and Fourier phases;
    spinors and gluon polarization vectors;
    color and zero-mode records;

C47:
    x-weighted qg basis;
    finite-shell truncation;
    exact CM-ground architecture;
    raw/physical basis identities;

C50:
    shared C43/C45 finite-cell convention map;
    exact sqrt(2) conversion;
    P-minus to M-squared convention;
    dimensional and normalization diagnostics;
    three-mode vertex evaluator as a negative-control arity;

C55:
    source locks and exact convention map;
    full instantaneous-fermion operator;
    direct b-dagger a-dagger a b monomial;
    overall g_s-squared coefficient;
    exact distinction from self-induced inertia and C53 propagation;

C57:
    selected finite-HO corresponding-propagating graph regulator;
    mode-support and zero-mode controls;

C77:
    canonical raw qg identities and physical embedding;

C78:
    independent kernel-coordinate vocabulary;
    support and witness ancestry;
    exact projected coefficients;
    C57 reconciliation;
    C53/C58 non-substitution boundaries;

C79:
    fail-closed audit;
    executable gate;
    regression tests;
    c80_ifkernel2_contract.md.
```

Create:

```text
docs/next_level/c80_derivation_authority_manifest.json
docs/next_level/c80_input_fidelity_audit.json
```

---

# 4. Freeze inputs and coordinate vocabulary

Consume C78 through its authenticated public API.

Freeze:

```text
C78 package/root identity;
all independent kernel-coordinate identities;
all coordinate-equivalence classes;
all resolution identities;
all raw q, raw g, and retained-q mode identities;
C43/C55 operator identity;
C45 mode-library identity;
C50 convention-map identity;
C57 regulator identity.
```

Issue:

```text
C80_INPUTS_FROZEN_COMPLETE
```

in:

```text
docs/next_level/c80_input_freeze.json
```

Do not alter or merge C78 kernel coordinates after observing evaluator
values.

Create a complete immutable `ContactKernelCoordinate` record retaining all
fields on which the source kernel can depend, including as applicable:

```text
resolution;
incoming and outgoing quark longitudinal modes;
incoming and outgoing gluon longitudinal modes;
intermediate plus-momentum channel;
incoming and outgoing quark transverse modes;
incoming and outgoing gluon transverse modes;
quark helicities;
gluon polarizations/helicities;
fundamental and adjoint color identities;
ordered color-generator identity;
zero-mode and boundary identity;
finite-HO shell identity;
P-minus/M-squared convention identity.
```

Create:

```text
docs/next_level/c80_kernel_coordinate_manifest.json
docs/next_level/c80_kernel_coordinate_validation.json
```

---

# 5. Derive the four-field finite-cell matrix element

Insert the exact C45 mode expansions for

```text
the outgoing quark field;
the outgoing gluon field;
the incoming gluon field;
the incoming quark field;
```

into the exact C55 direct-contact operator.

Derive the coefficient of

\[
b^\dagger_{\alpha_q'}
a^\dagger_{\alpha_g'}
a_{\alpha_g}
b_{\alpha_q}
\]

without using C50's three-mode numerical value.

Implement two independent derivation routes:

## Route A — coordinate-space insertion

```text
insert the normalized x-minus and x-perp mode expansions;
apply the inverse derivative to the exact source-declared field
product;
integrate x-minus exactly;
integrate the transverse local product;
retain the field-normalization factors and fermion signs.
```

## Route B — momentum-space/functional extraction

Use one independent route, such as:

```text
Fourier-transform the same local operator and evaluate the
momentum-conserving convolution of four mode functions;

or extract the b-dagger a-dagger a b coefficient through ordered
functional derivatives of the frozen finite-cell operator.
```

Route B must not call Route A or consume its assembled result.

Require exact agreement of:

```text
overall sign;
all powers of 2, pi, L, and sqrt(2);
longitudinal Kronecker identity;
inverse-partial-plus channel;
gamma order;
ordered color product;
and transverse overlap definition.
```

Create:

```text
docs/next_level/c80_four_field_operator_insertion.json
docs/next_level/c80_four_field_derivation_comparison.json
```

---

# 6. Longitudinal finite-cell evaluator

Derive the exact longitudinal factor from the frozen field order.

For every coordinate determine:

```text
the incoming and outgoing total plus-momentum relation;
the exact Kronecker conservation rule;
the plus momentum on which 1/(i partial-plus) acts;
the sign under the frozen Fourier convention;
all field-normalization powers;
the finite-cell length dependence;
zero-mode admissibility;
and the minimum allowed denominator magnitude.
```

Do not substitute:

```text
a C53 light-front energy denominator;
a guessed intermediate momentum;
an i-epsilon;
a numerical cutoff;
or a finite value for an excluded zero mode.
```

Use exact `Fraction` arithmetic for discrete longitudinal modes.

Create:

```text
docs/next_level/c80_longitudinal_contact_kernel.json
docs/next_level/c80_inverse_partial_plus_validation.json
```

A singular coordinate that survives all frozen support rules is a concrete
no-go and must be identified exactly.

---

# 7. Two-gluon spin/polarization numerator

Evaluate the exact spin/polarization structure in the source gamma order.

Implement two independent routes:

```text
direct four-component gamma-matrix/spinor/polarization contraction;

source-reduced two-component light-front helicity expression.
```

Retain:

```text
incoming and outgoing quark helicities;
incoming and outgoing gluon polarizations;
gamma-plus/projector identity;
polarization phase convention;
exact symbolic numerator when feasible;
certified numerical value and bound;
selection-rule status.
```

Validate:

```text
helicity selection;
polarization-basis covariance;
Hermitian-conjugate relation;
zero-polarization and wrong-gamma-order negative controls;
agreement of both routes.
```

Create:

```text
docs/next_level/c80_two_gluon_spin_kernel.json
docs/next_level/c80_two_gluon_spin_validation.json
```

---

# 8. Ordered SU(3) color evaluator

Evaluate the exact ordered color matrix element inherited from the direct
contact.

Keep the source order of the two generators explicit. Do not replace the
general result by \(C_F\) unless the specific contracted identity proves
that reduction.

Implement two independent routes:

```text
direct multiplication in the fundamental/product-color basis;

projection through the immutable C74 retained-triplet authority.
```

Validate:

```text
generator order;
conjugation relation;
triplet closure;
zero anti-sextet and 15 leakage after projection;
agreement of both routes;
a reversed-generator negative control.
```

Create:

```text
docs/next_level/c80_ordered_color_kernel.json
docs/next_level/c80_ordered_color_validation.json
```

---

# 9. Exact local four-HO overlap

Derive the transverse local integral from the operator insertion. In the
common-scale case it will have the structural form

\[
I_{\alpha_q'\alpha_g';\alpha_g\alpha_q}
=
\int d^2x_\perp\,
\Phi_{\alpha_q'}^*(x_\perp)
\Phi_{\alpha_g'}^*(x_\perp)
\Phi_{\alpha_g}(x_\perp)
\Phi_{\alpha_q}(x_\perp),
\]

but the exact C45 field normalization and ordering are authoritative.

Do not assume equal oscillator scales unless the mode records prove it.

Implement two independent routes:

## Route A — analytic finite polynomial/Gaussian evaluator

Use the exact C45 2D-HO functions to derive a finite expression through one
of:

```text
Laguerre-polynomial expansion and exact radial moments;

circular-ladder polynomial algebra;

Cartesian-HO product algebra with an exact polar/circular adapter;

or an equivalent exact recurrence.
```

The evaluator must expose exact angular and shell selection rules and
canonical factorial/rational/square-root expressions.

## Route B — independent numerical holdout

Use high-order two-dimensional quadrature, or an independently transformed
momentum-space convolution, with a certified convergence envelope.

Required validation:

```text
normalization holdouts;
lowest-shell closed form;
positive- and negative-m cases;
angular-momentum selection;
complex-conjugation symmetry;
permutation relations allowed by the operator;
scale dependence;
precision doubling;
exact-zero classification without a threshold.
```

Create:

```text
docs/next_level/c80_four_ho_contact_integral.json
docs/next_level/c80_four_ho_analytic_validation.json
docs/next_level/c80_four_ho_quadrature_validation.json
```

C50's three-mode integral is a required negative control: its arity and
measure must fail if passed off as the four-mode contact integral.

---

# 10. Finite-cell normalization and units

Combine the source coefficient, longitudinal factor, spin/polarization
numerator, ordered color factor, and four-HO overlap into the coefficient
of \(g_s^2\) in \(P^-\).

Track explicitly:

```text
L;
P-plus;
b_HO;
all powers of GeV;
field normalizations;
finite-cell Kronecker factors;
sqrt(2) conventions;
and any transverse-area dimension.
```

Then apply the frozen C43/C50 invariant-mass convention:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Prove the treatment of \(P_\perp^2\) in the selected total-transverse
frame.

Determine analytically whether the auxiliary box length cancels. Do not set
\(L=1\), hide it in a coupling, or repair units numerically.

Create:

```text
docs/next_level/c80_finite_cell_contact_normalization.json
docs/next_level/c80_pminus_to_m2_contact_conversion.json
docs/next_level/c80_dimensional_validation.json
```

---

# 11. Immutable factorized evaluator

Implement a public evaluator equivalent to:

```python
evaluate_bare_contact_kernel(
    kernel_coordinate_id: str,
    resolution: str,
    precision: int | None = None,
) -> CertifiedContactKernel
```

The returned frozen record must expose:

```text
kernel-coordinate identity;
coefficient of g_s squared in P-minus;
coefficient of g_s squared in M-squared;
certified absolute bounds;
units;
longitudinal factor and ancestry;
spin/polarization factor and ancestry;
ordered color factor and ancestry;
four-HO factor and ancestry;
normalization and conversion identities;
terminal evaluator status.
```

Also expose factor-level APIs equivalent to:

```python
longitudinal_contact_factor(...)
spin_polarization_contact_factor(...)
ordered_color_contact_factor(...)
four_ho_contact_overlap(...)
```

The evaluator must:

```text
load only authenticated immutable inputs;
use allow_pickle=False for every NumPy load;
reject object-dtype, unsafe, or unindexed files;
return non-writeable arrays and frozen records;
call no C50 value evaluator as a substitute;
call no C53/C58 construction route;
choose no physical coupling.
```

Create:

```text
docs/next_level/c80_api_contract.json
docs/next_level/c80_api_validation.json
```

---

# 12. Factorization and computational scope

The C78 kernel-coordinate address spaces are extremely large. C80 must not
materialize dense arrays over them.

Construct exact equivalence classes and content-addressed primitive tables
for:

```text
longitudinal factors;
spin/polarization factors;
ordered color factors;
four-HO overlaps;
normalization/conversion factors.
```

Requirements:

```text
evaluate each unique primitive once;
preserve exact coordinate ancestry;
stream coordinate queries;
record cache and compression ratios;
record peak memory;
reconstruct frozen full-coordinate holdouts directly;
and never use floating equality to merge classes.
```

C80 need not aggregate over C78 physical bra/ket pairs. It must demonstrate
that every C78 coordinate can be evaluated by the factorized API and that
all frozen holdouts return terminal values.

Create:

```text
docs/next_level/c80_factorization_plan.json
docs/next_level/c80_primitive_inventory.json
docs/next_level/c80_scaling_and_resource_report.json
```

---

# 13. Executable pilots and closure

Before declaring evaluator readiness, execute:

```text
one lowest-shell diagonal coordinate;
one lowest-shell off-diagonal nonzero coordinate;
one angular-selection exact zero;
one helicity/polarization exact zero;
one color-order-sensitive coordinate;
one coordinate at each of the three resolutions;
one smallest-certified nonzero holdout;
one Hermitian-conjugate coordinate pair.
```

For each pilot compare:

```text
Route A versus Route B operator derivation;
direct versus reduced spin route;
direct versus projected color route;
analytic versus quadrature four-HO route;
P-minus versus independently converted M-squared result.
```

Create:

```text
docs/next_level/c80_low_shell_kernel_pilot.json
docs/next_level/c80_kernel_holdout_report.json
```

---

# 14. Runtime package and deterministic reconstruction

Use:

```text
src/deuteron_wigner/bridge/ifkernel2/
data/runtime/c80_ifkernel2/
```

or repository-equivalent paths.

Create one authenticated runtime index/root containing:

```text
source and API fingerprints;
coordinate schema;
primitive tables;
exact-expression records;
certified numerical values and bounds;
factorization metadata;
holdouts;
and deterministic reconstruction commands.
```

Run:

```text
two consecutive builds;
one clean build;
one serial build;
one supported parallel/sharded build;
one restart build.
```

Require byte-identical runtime and tracked artifacts.

Create:

```text
docs/next_level/c80_runtime_inventory.json
docs/next_level/c80_deterministic_reconstruction_report.json
```

---

# 15. Isolation and negative controls

Prove C80 construction is independent of:

```text
C50 three-mode numerical values;
C53 vertex values and propagators;
C58 self-induced-inertia values;
C78 physical-pair aggregation;
a chosen physical g_s or alpha_s;
a counterterm;
the historical C57 threshold;
C47 quadrature residues;
ART25 files.
```

Required failures include mutations of:

```text
operator coefficient;
field order;
gamma order;
inverse-partial-plus channel;
longitudinal Fourier sign;
zero-mode admission;
field normalization;
four-mode arity;
HO phase;
angular selection;
ordered color product;
P-minus to M-squared factor;
units;
bound propagation;
unsafe NumPy loading;
mutable return;
C50-value substitution;
C53/C58 substitution;
physical-coupling insertion.
```

Create at least **320 focused live mutations** of actual operator,
coordinate, factor, evaluator, and runtime objects.

Create:

```text
docs/next_level/c80_isolation_report.json
docs/next_level/c80_regression_report.json
```

---

# 16. Readiness and continuation decisions

Select exactly one branch.

## 16.1 Favorable branch

Issue the exact positive status frozen by the committed C80 contract, with
preferred semantic identity:

```text
C80_EXACT_SOURCE_CHAIN_DERIVED_IFCONTACT_KERNEL_EVALUATOR_READY
```

Required:

```text
both operator-insertion routes agree;
the longitudinal denominator and zero-mode policy close;
the spin/polarization routes agree;
the ordered-color routes agree;
the analytic and numerical four-HO routes agree;
finite-cell normalization and units close;
P-minus to M-squared conversion closes;
every frozen coordinate holdout has a terminal value;
the factorized public evaluator is immutable and deterministic;
no physical-pair matrix is assembled;
all isolation and mutation tests pass.
```

Next:

> **C81/IFCONTACT3 — bare direct-contact matrix evaluation and sparse/matrix-free assembly on the immutable C78 support**

## 16.2 Operator insertion incomplete

```text
C80_IFKERNEL_OPERATOR_INSERTION_INCOMPLETE
```

Next:

> **C81/IFOPINSERT — repair only the specifically identified field-expansion, sign, gamma-order, or coefficient contradiction**

## 16.3 Longitudinal evaluator incomplete

```text
C80_IFKERNEL_LONGITUDINAL_INCOMPLETE
```

Next:

> **C81/IFLONG — repair only the specifically identified finite-cell, inverse-derivative, or zero-mode defect**

## 16.4 Spin/color evaluator incomplete

```text
C80_IFKERNEL_SPIN_COLOR_INCOMPLETE
```

Next:

> **C81/IFSPINCOLOR — repair only the specifically identified spinor, polarization, or ordered-color defect**

## 16.5 Four-HO evaluator incomplete

```text
C80_IFKERNEL_FOUR_HO_INCOMPLETE
```

Next:

> **C81/IFHO4 — repair only the specifically identified analytic overlap, phase, scale, or quadrature defect**

## 16.6 Normalization/conversion incomplete

```text
C80_IFKERNEL_NORMALIZATION_INCOMPLETE
```

Next:

> **C81/IFKERNELNORM — repair only the specifically identified field normalization, box-length, units, or P-minus-to-M-squared defect**

## 16.7 Public evaluator incomplete

```text
C80_IFKERNEL_PUBLIC_EVALUATOR_INCOMPLETE
```

Next:

> **C81/IFKERNELAPI — repair only the specifically identified factorization, certification, loader, runtime, or determinism defect**

Do not issue a contact-matrix, complete-instantaneous-fermion,
renormalized, TMD, matching, inference, or production status.

---

# 17. Essential deliverables

Create at least:

```text
docs/next_level/c80_implementation_report.md
docs/next_level/c80_derivation_authority_manifest.json
docs/next_level/c80_input_fidelity_audit.json
docs/next_level/c80_input_freeze.json

docs/next_level/c80_kernel_coordinate_manifest.json
docs/next_level/c80_kernel_coordinate_validation.json
docs/next_level/c80_four_field_operator_insertion.json
docs/next_level/c80_four_field_derivation_comparison.json

docs/next_level/c80_longitudinal_contact_kernel.json
docs/next_level/c80_inverse_partial_plus_validation.json
docs/next_level/c80_two_gluon_spin_kernel.json
docs/next_level/c80_two_gluon_spin_validation.json
docs/next_level/c80_ordered_color_kernel.json
docs/next_level/c80_ordered_color_validation.json

docs/next_level/c80_four_ho_contact_integral.json
docs/next_level/c80_four_ho_analytic_validation.json
docs/next_level/c80_four_ho_quadrature_validation.json

docs/next_level/c80_finite_cell_contact_normalization.json
docs/next_level/c80_pminus_to_m2_contact_conversion.json
docs/next_level/c80_dimensional_validation.json

docs/next_level/c80_factorization_plan.json
docs/next_level/c80_primitive_inventory.json
docs/next_level/c80_scaling_and_resource_report.json
docs/next_level/c80_low_shell_kernel_pilot.json
docs/next_level/c80_kernel_holdout_report.json

docs/next_level/c80_api_contract.json
docs/next_level/c80_api_validation.json
docs/next_level/c80_runtime_inventory.json
docs/next_level/c80_deterministic_reconstruction_report.json
docs/next_level/c80_isolation_report.json
docs/next_level/c80_readiness_report.json
docs/next_level/c80_regression_report.json
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

# 18. Acceptance criteria

C80 is complete only when:

1. Baseline `66e57dfd7d4e5a3f213d085dac2481c4a4ab0a2d` reproduces.
2. Both protected untracked paths remain untouched.
3. C43/C45/C47/C50/C55/C57/C77/C78/C79 historical artifacts remain unchanged.
4. `c80_ifkernel2_contract.md` is consumed and preserved.
5. C78 coordinate identities freeze before evaluator construction.
6. No external paper is demanded for project-owned finite-HO sparse ordering.
7. The four-field coefficient is derived by two independent routes.
8. All signs and normalization factors agree between routes.
9. The inverse-\(\partial^+\) channel is exact.
10. Every admitted denominator is nonsingular or explicitly excluded.
11. Spin/polarization evaluation closes by two routes.
12. Ordered color evaluation closes by two routes.
13. General color is not improperly reduced to \(C_F\).
14. The four-HO integral is derived from the operator.
15. The analytic four-HO evaluator closes against an independent numerical route.
16. Exact zeros use no numerical threshold.
17. C50's three-mode evaluator is rejected as a four-mode substitute.
18. Finite-cell normalization and units close.
19. Any auxiliary \(L\) dependence is derived, not set by convention.
20. The \(P^-\to M^2\) conversion is exact.
21. \(g_s^2\) remains explicit and factored.
22. No physical coupling or counterterm is selected.
23. Large coordinate domains remain factorized.
24. Every frozen holdout has a terminal evaluator result.
25. The public evaluator is immutable, safe, and deterministic.
26. At least 320 focused live mutations pass.
27. No physical contact matrix, C53/C58 substitute, complete instantaneous-fermion operator, TMD/matching, fit, inference, or production object is created.
28. `NO_JOINT_MEASURE`, 216 routes, 642 ART25 identities, and authoritative artifacts remain unchanged.
29. The working tree is clean except for the two protected untracked paths.
30. A local completion commit is created and not pushed.

Do not weaken operator insertion, inverse-derivative identity, spin/color
ordering, four-mode overlap, dimensional closure, certification, or
no-substitution boundaries to open the gate.

---

# 19. Final Codex response

Report:

- starting and final commits;
- untouched untracked paths;
- consumed C80 contract identity;
- C78 package/root and coordinate counts;
- source/operator identities;
- four-field derivation-route agreement;
- longitudinal conservation and denominator rule;
- minimum admitted denominator;
- spin/polarization route agreement;
- ordered-color route agreement;
- four-HO analytic formula class, exact-zero counts, and quadrature residuals;
- finite-cell normalization and \(L\)-dependence status;
- \(P^-\to M^2\) conversion and final units;
- unique primitive counts and compression factors;
- peak memory and execution strategy;
- low-shell and full-coordinate holdout results;
- public evaluator/API and runtime-root hashes;
- deterministic reconstruction;
- isolation and mutation results;
- exact readiness/no-go status;
- exact next branch;
- confirmation that no physical coupling, contact matrix, counterterm, complete instantaneous-fermion operator, TMD/matching, fit, inference, or production object was created;
- confirmation that nothing was pushed.
