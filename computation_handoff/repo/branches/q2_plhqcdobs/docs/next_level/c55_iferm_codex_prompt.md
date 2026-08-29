# C55/IFERM Codex Work Package

## Title

**Finite-volume light-front instantaneous-fermion operator: constrained-field derivation, exact normal ordering, inverse-\(\partial^+\) and zero-mode completion, physical \(q/qg\) projection, color-triplet matrix assembly, and independent action closure**

## Authoritative baseline

Start from the clean local C54/HQCD2 fail-closed completion commit:

```text
3717d1a70184c6cc70dfc985534c38f51a7d1476
```

Its immediate scientific parent is:

```text
ec705d02960d3a1a644958d43d35277a85f9825c
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor ec705d02960d3a1a644958d43d35277a85f9825c HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C54_INSTANTANEOUS_FERMION_ASSEMBLY_INCOMPLETE
```

and the exact C54 boundary:

```text
C53 physical canonical vertex:
    verified read-only;
    primitive and generated-adjoint hashes pass;
    executable symbolic coefficient passes;
    basis orders and entry ancestry pass;
    sparse/matrix-free residuals pass;
    historical-tuple and combined-oracle poisoning controls pass.

first missing local contract:
    no source-qualified finite-volume, normal-ordered,
    q/qg instantaneous-fermion matrix-element functional.

not created by C54:
    free local matrices;
    instantaneous matrices;
    constrained/contact matrices;
    boundary/zero-mode matrices;
    polynomial action;
    projected action identity;
    local counterterm directions;
    nonlocal TMD operators.
```

Verify every statement from the committed C54 records rather than relying on this prompt.

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

physical basis:
    K = 9/2, 11/2, 13/2
    C47 CM-clean total-color-triplet qg module

canonical local vertex:
    C53 source-derived physical q <-> qg operator
    imported read-only
    g_s factored
    absorption generated only as the adjoint

invariant-mass convention:
    M^2 = 2 P^+ P^- - P_perp^2

longitudinal cell:
    -L <= x^- <= L
    p^+ = pi k/L
    P^+ = pi K/L
    L remains symbolic
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All historical C47 canonical tuple values and attempted mass/transverse metadata remain diagnostic-only and forbidden as physical numerical inputs.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C54 established that the source-qualified **action-level** instantaneous-fermion term exists, but no executable finite-volume matrix-element functional descends from it.

C55 must not search indefinitely for a publication containing the final custom object:

```text
C43 light-front gauge
+ C45 finite-cell modes
+ C47 CM-clean qg basis
+ C53 triplet convention
= final physical instantaneous-fermion matrix.
```

That matrix is project specific.

C55 must distinguish:

```text
PRIMARY_SOURCE_INPUT
    the constrained-fermion equation;
    the exact action/Hamiltonian term;
    canonical brackets and mode expansions;
    light-front gauge and inverse-derivative prescription.

PROJECT_DERIVED_FROM_SOURCE_INPUTS
    normal-ordering decomposition;
    finite-cell plane-wave matrix elements;
    physical-basis projection;
    triplet-color matrix;
    sparse and matrix-free actions.

ABELIAN_METHOD_CROSSCHECK
    finite-box, operator-ordering, and instantaneous-contact checks
    after an exact QCD-to-QED convention map.

HISTORICAL_METHOD_ORACLE_ONLY
    C40 toy instantaneous matrices;
    earlier reduced finite-gauge benchmarks.

ABSENT_BLOCKING
    any required formula or projection that cannot be derived from
    the source-qualified chain.
```

The final C55 matrix may be a new project calculation. It is acceptable only when every source input, convention conversion, algebraic derivation, normal-ordering decision, matrix element, and independent check is explicit.

---

# 2. Exact purpose

C55 resolves only the instantaneous-fermion obstruction.

It must produce:

```text
the exact C43 constrained-fermion Hamiltonian expression;

the uniquely identified O(g_s^2) instantaneous-fermion operator;

an exhaustive normal-ordering and operator-monomial ledger;

a source-derived block classification on H_q plus H_qg;

a finite-cell color-stripped plane-wave matrix-element kernel;

an exact inverse-partial-plus momentum-routing and zero-mode contract;

a component-wise P^- to M^2 conversion;

an arbitrary physical-basis evaluator;

all source-supported physical instantaneous-fermion matrix blocks;

an independent matrix-free action derived from the operator kernel;

Hermiticity, color covariance, CM/triplet, unit, phase,
normal-ordering, count-once, and physical-resolution diagnostics;

a C56/HQCD3 import contract.
```

The operator must remain coupling factored:

\[
V_{\mathrm{IF}}
=
g_s^2\,\widehat V_{\mathrm{IF}}^{(M^2)}.
\]

Do not choose or fit \(g_s\) or \(\alpha_s\).

C55 must not construct:

```text
the free q or qg matrices;
the instantaneous color-current/gluon matrices;
unrelated constrained/contact matrices;
the complete local polynomial action;
the complete projected action/current identity;
the JMY Wilson or bilocal TMD operators;
a one-loop correlator;
a matching coefficient.
```

The strongest allowed status is:

```text
C55_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

When that gate passes, the exact next package is:

> **C56/HQCD3 — resume complete local-QCD substrate assembly using the read-only C53 canonical vertex and read-only C55 instantaneous-fermion operator**

---

# 3. Scientific scope

The retained physical space is:

\[
\mathcal H_q
\oplus
\mathcal H_{qg}^{(3,\mathrm{CM}=0)}.
\]

The declared operator scope is:

```text
one external quark;
zero or one external transverse gluon;
the normal-ordered local instantaneous-fermion term generated by
eliminating the constrained fermion field;
all direct matrix blocks induced by that term at O(g_s^2);
all normal-ordering contractions required by the selected source
Hamiltonian convention;
all zero-mode and boundary decisions required by 1/partial^+.
```

The following are outside the retained numerical space but must receive explicit operator statuses:

```text
q -> qgg;
qgg -> q;
qg -> qggg;
antiquark and pair-changing monomials;
higher-Fock contractions.
```

“Outside the retained basis” is not synonymous with “zero.” Use:

```text
OUTSIDE_RETAINED_SPACE_NONZERO_OPERATOR
```

when appropriate.

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_gauge_plan.json
docs/next_level/c43_gauge_convention_map.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_boundary_prescription_decision.json
docs/next_level/c43_zero_mode_contract.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_inverse_derivative_mode_functional.json
docs/next_level/c47_boundary_zero_mode_functional.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_physical_resolution_manifest.json
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c54_implementation_report.md
docs/next_level/c54_input_fidelity_audit.json
docs/next_level/c54_local_term_crosswalk.json
docs/next_level/c54_readiness_report.json
docs/next_level/c54_missing_calculation_specification.md
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c55_derivation_authority_manifest.json
docs/next_level/c55_input_fidelity_audit.json
```

---

# 5. Primary-source hierarchy

Reuse the exact C43 source locks, especially:

```text
hep-ph/0011372v2
    Srivastava–Brodsky
    primary light-front-gauge QCD constraint and
    instantaneous-interaction authority

hep-ph/9705477v1
    Brodsky–Pauli–Pinsky
    broad light-front-QCD Hamiltonian, Fock-space,
    and finite-volume authority
```

Reuse the C50 Abelian BLFQ source locks only as method/convention cross-checks where their exact equations support the comparison.

Do not promote:

```text
a QED interaction into QCD color authority;
a color-singlet hadron-model Hamiltonian into the open-triplet module;
a reduced C9/C13/C14 validation term into the C55 physical matrix;
a continuum amplitude into the finite-cell normalization.
```

If the already locked primary sources do not uniquely specify a required action-level sign, factor, ordering, or normal-ordering convention, acquire and hash-lock the exact official primary source needed to close that point.

Do not require a paper to print the final C55 basis matrix.

Create:

```text
docs/next_level/c55_primary_source_manifest.json
docs/next_level/c55_source_role_matrix.json
docs/next_level/c55_source_sufficiency_matrix.json
```

---

# 6. Freeze construction and holdouts

Before deriving the operator, freeze:

```text
the exact C43 fermion constraint;
the exact C43 Hamiltonian sign convention;
the C43/C45 field expansions;
the inverse-partial-plus and PV prescription;
the P0/Q0 projectors;
the finite-cell state normalization;
the C47 physical q and qg basis orders;
the C47 TM/CM transformations;
the C53 SU(3) and triplet phase conventions;
the M^2 conversion convention;
the symbolic L policy.
```

Freeze holdouts before implementation:

```text
one plane-wave qg -> qg matrix element for each independent
gluon-helicity pair;

both quark helicities;

one helicity-conserving and one helicity-changing case;

one smallest allowed gluon fraction;

one largest allowed gluon fraction;

one nontrivial intrinsic-OAM case;

one denominator nearest to zero without being zero;

one exact Q0-forbidden denominator case, if present;

one q -> q normal-ordering contraction candidate;

one q <-> qg candidate expected to be classified by gluon-number
selection rather than assumed zero;

one ordered-color holdout;

one Abelian-limit holdout;

one GeV/MeV holdout;

one symbolic-L holdout;

one physical-resolution comparison holdout.
```

No failed holdout may be moved into construction after inspection.

Create:

```text
docs/next_level/c55_calculation_plan.json
docs/next_level/c55_holdout_plan.json
```

---

# 7. Re-derive the constrained-fermion term

Begin from the exact C43 fermion constraint for:

\[
\psi=\psi_+ + \psi_-.
\]

Transcribe the exact source/project expression for \(\psi_-\), including:

```text
mass term;
transverse derivative;
transverse gauge field;
color generator;
inverse partial-plus;
boundary/zero-mode term;
operator ordering.
```

Substitute it into the source Hamiltonian.

A commonly encountered structure is schematically:

\[
\psi_+^\dagger
\mathcal R^\dagger
\frac{1}{i\partial^+}
\mathcal R
\psi_+,
\]

where \(\mathcal R\) contains the mass, transverse derivative, and \(g_s A_\perp\) terms. This equation is schematic only. Use the exact C43 source expression, factors, signs, Hermitian symmetrization, and derivative action.

Extract the coefficient of \(g_s^2\) algebraically.

Implement two independent symbolic derivations:

```text
direct expansion of the exact constrained-field Hamiltonian;

exact second symbolic derivative with respect to g_s at g_s=0,
with the appropriate factorial convention.
```

Do not use numerical finite differences to define the term.

Create:

```text
docs/next_level/c55_fermion_constraint_rederivation.json
docs/next_level/c55_g2_operator_extraction.json
```

---

# 8. Exact instantaneous-fermion operator contract

Define one immutable operator object:

```text
InstantaneousFermionOperator
```

It must record:

```text
source equation and locator;
project-convention expression;
all field factors;
which derivative acts on which product;
Hermitian ordering;
color ordering;
coupling power;
inverse-derivative prescription;
zero-mode domain;
normal-ordering convention;
mass dimension;
local/nonlocal-in-x-minus status;
local-in-x-plus status.
```

A schematic target may resemble:

\[
P^-_{\mathrm{IF}}
\sim
g_s^2
\int dx^-\,d^2x_\perp\,
\psi_+^\dagger
(\alpha_\perp\!\cdot A_\perp)
\frac{1}{i\partial^+}
(\alpha_\perp\!\cdot A_\perp)
\psi_+,
\]

but do not hard-code this schematic expression when the exact C43 formula differs in factors, adjoints, derivative placement, color order, or boundary terms.

Create:

```text
docs/next_level/c55_instantaneous_fermion_operator_contract.json
```

---

# 9. Normal-ordering and operator-monomial ledger

Insert the exact quark and gluon mode expansions before projecting onto Fock sectors.

Enumerate all operator monomials generated by the two gauge fields and the fermion bilinear.

At minimum audit the source equivalents of:

```text
b-dagger a-dagger a b;
b-dagger a a-dagger b;
b-dagger a-dagger a-dagger b;
b-dagger a a b;

antiquark-preserving terms;
pair-creation and pair-annihilation terms;
normal-ordering contractions.
```

Do not assume this illustrative list is complete.

For every monomial record:

```text
operator order;
fermion-number change;
gluon-number change;
color ordering;
longitudinal momentum routing;
inverse-derivative argument;
normal-ordering contraction;
retained physical block;
status.
```

Allowed statuses:

```text
DIRECT_RETAINED_OPERATOR;
NORMAL_ORDER_CONTRACTION_RETAINED;
OUTSIDE_RETAINED_SPACE_NONZERO_OPERATOR;
EXACT_ZERO_BY_OPERATOR_ALGEBRA;
NOT_APPLICABLE_WITH_SOURCE_PROOF;
ABSENT_BLOCKING.
```

Normal ordering must be exact.

If an \(a a^\dagger\) term produces both:

```text
a normal-ordered a-dagger a contribution;
and
a commutator contraction,
```

store them separately.

Do not silently drop the contraction as a vacuum constant. In a fermion bilinear it may be a one-body self-induced-inertia or counterterm-like operator.

Create:

```text
docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
```

---

# 10. Retained-block classification

Compile the exact physical block matrix:

```text
q -> q;
q -> qg;
qg -> q;
qg -> qg.
```

Each block receives exactly one of:

```text
SOURCE_DERIVED_EXECUTABLE_NONZERO;
SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF;
NORMAL_ORDER_CONTRACTION_DIRECTION;
NOT_APPLICABLE_WITH_ACTION_LEVEL_PROOF;
ABSENT_BLOCKING.
```

Do not infer:

```text
q <-> qg = 0
```

merely from the phrase “two-gluon contact.” Prove the result from the normal-ordered monomial ledger and zero-mode/boundary policy.

Do not infer:

```text
q -> q = 0
```

merely because the direct normal-ordered term contains \(a^\dagger a\). Resolve the normal-ordering contraction and its relation to mass, field, and sector counterterm directions.

Create:

```text
docs/next_level/c55_physical_block_classification.json
```

---

# 11. Count-once relation to propagating canonical dynamics

The instantaneous-fermion contact is not the same object as second-order propagation through two C53 canonical vertices.

Create an explicit relation ledger separating:

```text
direct instantaneous-fermion contact;

second-order propagating canonical contribution
    V^\dagger (E-H_0)^{-1} V;

normal-ordering contraction/self-induced inertia;

local counterterm direction;

zero-mode/boundary completion.
```

Do not construct the propagating second-order matrix numerically in C55.

Do not generate the instantaneous operator from:

```text
C53 adjoint times an energy denominator times C53 emission.
```

Use that structure only as a topology/count-once negative control.

Create:

```text
docs/next_level/c55_contact_propagating_count_once.json
```

---

# 12. Finite-cell state and field normalization

Derive the finite-volume plane-wave matrix element from the C43/C45 mode expansions.

Retain every factor from:

```text
-L <= x^- <= L;
p^+ = pi k/L;
fermion antiperiodic modes;
gluon periodic nonzero modes;
creation/annihilation brackets;
one-quark state normalization;
qg state normalization;
transverse field normalization;
two gauge-field factors;
x-minus integration;
transverse integration;
open-color module normalization.
```

Keep \(L\) symbolic.

Prove whether:

```text
L cancels;
a common block-level power remains;
or a source-defined regulator dependence remains.
```

No entry-dependent \(L\) signature may survive in one matrix block.

Create:

```text
docs/next_level/c55_finite_volume_normalization.json
docs/next_level/c55_state_normalization_validation.json
```

---

# 13. Inverse-\(\partial^+\) momentum routing

For every monomial, derive the exact longitudinal momentum on which:

\[
\frac{1}{i\partial^+}
\]

acts.

Do not assign the denominator from a remembered light-front time-ordering rule.

Record:

```text
incoming quark mode;
incoming gluon mode;
outgoing quark mode;
outgoing gluon mode;
operator ordering;
intermediate product mode;
denominator sign;
PV prescription;
P0/Q0 status;
boundary term.
```

Construct exact rational mode-index denominators before floating-point evaluation.

For every possible zero denominator, issue one of:

```text
EXCLUDED_BY_Q0_WITH_SOURCE_PROOF;
CANCELS_WITH_DECLARED_BOUNDARY_TERM;
RETAINED_ZERO_MODE_CONTROL;
ABSENT_BLOCKING.
```

A zero denominator is never replaced by:

```text
epsilon;
a clipped value;
a pseudoinverse;
a deleted matrix entry.
```

Create:

```text
docs/next_level/c55_inverse_derivative_routing.json
docs/next_level/c55_zero_denominator_ledger.json
docs/next_level/c55_inverse_derivative_validation.json
```

---

# 14. Plane-wave color-stripped kernel

Derive the finite-cell color-stripped plane-wave matrix element for every retained direct monomial.

For the qg-preserving contact, construct a kernel of the form:

\[
\mathcal I_{\lambda' h';\lambda h}
(p'_q,k'_g;p_q,k_g),
\]

with exact source-dependent:

```text
spinor/good-component tensor;
incoming and outgoing gluon polarizations;
inverse-derivative denominator;
longitudinal Kronecker delta;
transverse momentum conservation;
normalization factors;
phase;
operator ordering.
```

The notation is schematic. Use the exact C43/C45 conventions.

Implement two spin routes:

```text
good-component/constrained-field route;

full four-component source expression reduced with the C43 projectors.
```

Require agreement.

Create:

```text
docs/next_level/c55_plane_wave_kernel.json
docs/next_level/c55_spin_polarization_validation.json
```

---

# 15. Color algebra

For each retained qg-preserving operator ordering, derive the exact color tensor.

Possible source structures include ordered products such as:

\[
T^aT^b
\quad\text{or}\quad
T^bT^a,
\]

but use the actual normal-ordering and momentum-flow result.

Construct the operator first in the full product-color space:

\[
\mathbb C^3\otimes\mathbb C^8
\longrightarrow
\mathbb C^3\otimes\mathbb C^8.
\]

Then reduce to the frozen C47 triplet by:

\[
U_3^\dagger
\,\mathcal C_{\mathrm{IF}}\,
U_3.
\]

Do not assume the reduced \(3\times3\) color operator is proportional to the identity before calculation.

Required checks:

```text
Hermiticity after summing required orderings;
fundamental and adjoint SU(3) covariance;
triplet-subspace preservation;
zero anti-sextet and 15 leakage for the retained map;
full-product versus reduced-triplet route equality;
basis-rotation covariance;
Abelian limit.
```

Create:

```text
docs/next_level/c55_color_operator.json
docs/next_level/c55_color_triplet_validation.json
```

---

# 16. \(P^-\!\to M^2\) conversion

Apply the project identity:

\[
M^2=2P^+P^- - P_\perp^2
\]

to every retained instantaneous-fermion block.

Prove separately:

```text
same total P^+ on bra and ket;
same total transverse/CM frame;
whether P_perp^2 has an O(g_s^2) off-diagonal/contact term;
state-normalization compatibility;
factor of two in the C43 convention.
```

Do not copy the C50 canonical conversion without confirming its applicability to a qg-preserving contact and any q-preserving contraction.

Every completed \(\widehat V_{\mathrm{IF}}^{(M^2)}\) block must have uniform mass-squared units.

Create:

```text
docs/next_level/c55_pminus_to_m2_contract.json
docs/next_level/c55_pminus_to_m2_validation.json
```

---

# 17. Physical HO/TM/CM projection

Project the plane-wave kernel into the C47 physical basis.

The direct qg-preserving term generally requires a local four-mode transverse overlap and the exact x-weighted TM/CM transformations.

Derive, do not guess:

```text
the transverse integration measure;
HO phase;
incoming and outgoing x-scaled variables;
TM/Jacobi brackets;
CM-ground projectors;
OAM and Jz selection;
basis normalization.
```

Implement at least two independent routes:

```text
direct single-particle HO integration followed by CM projection;

intrinsic/CM basis evaluation using the C47 TM maps.
```

Use independent quadrature or analytic low-mode integrals as holdouts.

Create:

```text
docs/next_level/c55_physical_projection_contract.json
docs/next_level/c55_ho_tm_projection_validation.json
```

---

# 18. Arbitrary-mode evaluator

Create:

```python
evaluate_instantaneous_fermion(
    incoming_basis_id,
    outgoing_basis_id,
    resolution,
    symbolic_parameters,
) -> InstantaneousFermionEvaluation
```

The result must contain:

```text
physical block;
normal-ordered monomial ancestry;
plane-wave kernel components;
inverse-derivative mode and denominator;
zero-mode status;
transverse primitive;
color primitive;
P^- value;
M^2 value;
units;
exact-zero reason;
source ancestry;
symbolic signature.
```

The evaluator must not consume:

```text
C40 instantaneous matrices;
C47 raw canonical tuple values;
C53 physical vertex values;
a fitted or hand-entered contact coefficient.
```

C53 basis identities and color conventions remain valid inputs.

Create:

```text
docs/next_level/c55_evaluator_api.json
docs/next_level/c55_evaluator_validation.json
```

---

# 19. Exhaustive physical-domain ledger

Enumerate the complete retained Cartesian domains for every classified block.

Every basis pair receives exactly one status:

```text
PRESELECTION_FORBIDDEN_EXACT;
EVALUATED_EXACT_ZERO;
EVALUATED_NONZERO;
NORMAL_ORDER_CONTRACTION;
EVALUATOR_UNAVAILABLE_BLOCKING;
DUPLICATE_BLOCKING.
```

Preselection may use only exact source-owned rules:

```text
resolution;
K;
Jz;
fermion number;
gluon-number change;
CM-ground status;
triplet status;
zero-mode domain;
operator ordering.
```

Report:

```text
Cartesian pair count;
preselection count;
evaluator-call count;
exact-zero count;
nonzero count;
normal-order contraction count;
duplicate count;
missing count;
blocking count.
```

For a positive gate:

```text
duplicate = 0;
missing = 0;
blocking = 0.
```

Create:

```text
docs/next_level/c55_physical_domain_ledger.json
docs/next_level/c55_count_once_report.json
```

---

# 20. Assemble physical matrices

For every retained physical block with executable status, assemble sparse primitive matrices.

At minimum audit whether the final positive set contains:

```text
qg -> qg direct contact primitive;

q -> q normal-order contraction primitive or a separately typed
counterterm/self-induced-inertia direction;

q <-> qg exact-zero blocks with proof.
```

Do not force this anticipated pattern when the source derivation gives another result.

Store separately:

```text
primitive sparse matrix;
executable symbolic coefficient;
g_s^2 factor;
normal-ordering/contraction direction;
diagnostic evaluated matrix at nonphysical test substitutions.
```

Do not insert a physical \(g_s\).

Create:

```text
docs/next_level/c55_physical_matrices.json
docs/next_level/c55_normal_order_contraction_report.json
docs/next_level/c55_matrix_validation.json
```

---

# 21. Independent matrix-free action

Implement:

```python
apply_instantaneous_fermion(
    vector_q,
    vector_qg,
    resolution,
    symbolic_parameters,
)
```

The independent route must:

```text
enumerate the exact admitted domain;
call the C55 arbitrary-mode evaluator;
accumulate direct and contraction actions separately;
return block-separated outputs.
```

It must not:

```text
multiply by the stored C55 sparse matrices;
load a matrix-entry ledger as numerical authority;
construct the contact from C53 V-dagger D-inverse V;
consume C40 arrays or C47 tuple values.
```

Compare sparse and matrix-free actions on:

```text
every basis vector in tractable blocks;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions;
multiple diagnostic symbolic substitutions.
```

Create:

```text
docs/next_level/c55_matrix_free_report.json
```

---

# 22. Hermiticity and ordering closure

The complete retained instantaneous-fermion operator must satisfy the exact source-required Hermiticity relation.

Verify:

```text
direct Hermiticity of qg -> qg;
paired-adjoint relation for any off-diagonal block;
normal-order contraction Hermiticity;
operator-order reversal;
color-order reversal;
inverse-denominator conjugation;
basis-phase covariance.
```

Do not repair Hermiticity by averaging:

\[
M\to\frac12(M+M^\dagger)
\]

unless that symmetrization is itself the exact source operator definition and is applied before evaluation.

Create:

```text
docs/next_level/c55_hermiticity_ordering_report.json
```

---

# 23. Independent physics checks

## 23.1 Constraint-substitution equality

Compare the explicit C55 operator with the exact \(g_s^2\) coefficient extracted from the constrained-field Hamiltonian before normal ordering.

## 23.2 Abelian limit

Set the QCD color tensor to the exact Abelian limit and map conventions to the locked BLFQ/QED sources where their scope supports the comparison.

Do not use QED to determine QCD color or normal-ordering choices.

## 23.3 Propagating-versus-contact topology

At plane-wave holdouts, verify the source-owned distinction between the instantaneous contact and sequential propagating canonical contributions.

Where the primary source supplies a covariant/light-front equivalence identity, test the declared combination without tuning.

## 23.4 Direct coordinate/momentum routes

Compare direct coordinate-space field-mode integration with momentum/HO/TM evaluation for frozen low modes.

Create:

```text
docs/next_level/c55_constraint_substitution_report.json
docs/next_level/c55_abelian_crosscheck.json
docs/next_level/c55_contact_topology_crosscheck.json
docs/next_level/c55_coordinate_momentum_equivalence.json
```

---

# 24. Unit, regulator, and convention covariance

Execute:

```text
GeV/MeV conversion;
symbolic-L scaling or cancellation;
fixed-x P^+ rescaling;
bHO basis transformation;
mass/IR variation where the operator depends on it;
Fourier phase;
helicity/polarization phase;
triplet phase;
PV prescription controls;
zero-mode-projector controls;
normal-ordering convention controls;
factor-of-two M^2 control;
wrong SU(3) controls.
```

Require:

```text
every completed M^2 block scales as mass squared;
all symbolic signatures are block consistent;
dimensionless residuals are invariant;
wrong conventions fail explicitly.
```

Create:

```text
docs/next_level/c55_unit_regulator_convention_report.json
```

---

# 25. Physical-resolution comparison

Use the C47 comparison maps to evaluate:

\[
R\,\widehat V_{\mathrm{IF},r'}\,P
\quad\text{versus}\quad
\widehat V_{\mathrm{IF},r}.
\]

Execute separately for:

```text
direct qg contact;
normal-order contraction/direction;
every other retained block.
```

Separate:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
triplet-basis remainder;
zero-mode/boundary remainder;
normal-ordering remainder;
symbolic normalization remainder;
numerical error.
```

Do not tune a contact coefficient to reduce the comparison residual.

Create:

```text
docs/next_level/c55_operator_comparison_report.json
docs/next_level/c55_comparison_remainder_ledger.json
```

---

# 26. Isolation and poisoning controls

Prove that C55 is unchanged when:

```text
all C40 instantaneous matrices are poisoned;

all C47 raw canonical tuple values and component metadata are poisoned;

C50 combined canonical values are poisoned;

C53 physical canonical primitive entries are poisoned in paths
not needed for basis/color identity;

historical C9/C13/C14 instantaneous benchmark coefficients are poisoned.
```

The C55 result may consume source-derived basis, mode, and color identities, but not historical physical values.

The C55 build must fail when:

```text
the C43 instantaneous-fermion source expression changes;
the inverse-derivative prescription changes;
the zero-mode projector changes;
the normal-ordering contract changes;
the C47 physical basis hash changes;
the C53 triplet-isometry hash changes.
```

Create:

```text
docs/next_level/c55_isolation_report.json
```

---

# 27. C56/HQCD3 import contract

Define the read-only contract by which C56 will consume:

```text
the physical instantaneous-fermion primitive matrices;
their executable symbolic coefficient;
the g_s^2 coupling-order label;
normal-order contraction/counterterm-direction records;
physical basis-order hashes;
zero-mode and boundary statuses;
independent matrix-free action;
entry ancestry and count-once ledgers;
comparison diagnostics.
```

C56 must verify hashes before assembling any other local matrix.

C56 may not rederive or rescale C55.

Create:

```text
docs/next_level/c55_c56_import_contract.json
```

---

# 28. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
operator-monomial ledger;
inverse-derivative routing records;
plane-wave kernel holdouts;
color operators;
physical projection primitives;
domain ledger;
direct physical matrices;
normal-order contraction/direction objects;
matrix-free reconstruction metadata;
entry ancestry;
holdout records;
comparison-map execution blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c55_iferm/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
units;
coupling order;
symbolic signature;
basis-order hash;
expression hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c55_numerical_object_inventory.json
```

All JSON, expressions, and arrays must regenerate byte-for-byte.

---

# 29. End-to-end source-to-operator test

Implement an end-to-end test that begins from the C43/C45/C47/C53 contracts—not from prebuilt C55 matrices.

It must:

```text
rederive the constrained-fermion g_s^2 term;
normal order every monomial;
classify every physical block;
derive finite-cell normalization;
derive inverse-derivative routing;
derive plane-wave spin and color kernels;
apply P^- to M^2 conversion;
project into the CM-clean triplet basis;
evaluate every admitted basis pair;
assemble physical matrices;
apply the independent matrix-free action;
run Hermiticity, holdout, unit, poisoning, and comparison tests;
reproduce all hashes.
```

It must fail when:

```text
a C40 or historical instantaneous coefficient enters;
a C47 raw tuple value enters;
the contact is built as V-dagger D-inverse V;
an a a-dagger contraction is silently dropped;
a contraction is counted both as direct contact and counterterm;
a q <-> qg block is assumed zero without the monomial proof;
an inverse-derivative denominator is clipped or regularized by epsilon;
a zero mode is deleted;
the color order is reversed;
the triplet projection discards nonzero leakage silently;
Hermiticity is repaired after assembly;
a physical g_s is inserted;
a runtime hash changes.
```

---

# 30. Focused mutation tests

Create at least **224 focused live mutations** of actual source terms, monomials, denominators, kernels, color tensors, or matrices.

Include mutations of:

```text
fermion constraint;
g_s^2 extraction factor;
operator ordering;
normal-ordering contraction;
gluon-number change;
longitudinal momentum routing;
inverse-derivative sign;
PV prescription;
zero-mode projector;
boundary term;
spin tensor;
polarization vector;
color ordering;
SU(3) generator;
triplet isometry;
finite-cell normalization;
L power;
P^+ power;
P^- to M^2 factor;
HO/TM phase;
CM projector;
matrix entry;
matrix-free accumulation;
Hermitian partner;
entry ancestry;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, normal-ordering, dimension, zero-mode, color, Hermiticity, count-once, matrix-free, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 31. Readiness gate

Issue:

```text
C55_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

only when:

```text
the full C54 baseline reproduces;
the source/project-derivation distinction is explicit;
the C43 constrained-fermion equation is rederived;
the exact g_s^2 operator is extracted by two symbolic routes;
the normal-ordering and monomial ledger is complete;
every physical block has an executable/proved status;
all normal-order contractions are retained or excluded with proof;
contact and propagating topologies are count-once separated;
finite-cell normalization is complete;
inverse-derivative routing is explicit for every term;
zero denominators and zero modes have resolved statuses;
the plane-wave spin/polarization kernel closes;
the full-product and triplet color routes close;
the P^- to M^2 conversion closes;
physical HO/TM/CM projection closes;
the arbitrary-mode evaluator covers every admitted pair;
the exhaustive domain has no duplicate, missing, or blocking row;
all retained physical matrices exist;
the independent matrix-free action agrees;
Hermiticity follows from the source ordering without post-hoc repair;
constraint, Abelian, topology, and coordinate/momentum checks pass;
unit, regulator, phase, normal-ordering, and poisoning tests pass;
physical-resolution comparisons execute;
the C56 import contract is complete;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-operator test passes.
```

Do not issue:

```text
C55_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C55_INSTANTANEOUS_CURRENT_READY;
C55_PROJECTED_ACTION_IDENTITY_READY;
C55_JMY_WILSON_MATRIX_VALIDATED;
C55_BILOCAL_TMD_MEASUREMENT_VALIDATED;
C55_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 32. Exact no-go branches

## A. The action-level instantaneous-fermion source chain is incomplete

```text
C55_IFERM_SOURCE_OPERATOR_CHAIN_INCOMPLETE
```

Next:

> **C56/IFSRC — exact constrained-fermion Hamiltonian and \(g_s^2\) operator closure**

## B. Normal ordering or retained-block classification is incomplete

```text
C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE
```

Next:

> **C56/IFNORM — operator-monomial, contraction, self-induced-inertia, and block-scope completion**

## C. Inverse derivative or zero-mode routing is incomplete

```text
C55_IFERM_INVERSE_DERIVATIVE_ZERO_MODE_INCOMPLETE
```

Next:

> **C56/IFZERO — exact mode routing, PV kernel, zero denominator, boundary, and zero-mode completion**

## D. Finite-volume normalization is incomplete

```text
C55_IFERM_FINITE_VOLUME_NORMALIZATION_INCOMPLETE
```

Next:

> **C56/IFVOL — finite-cell field/state normalization and \(P^-\!\to M^2\) completion**

## E. Physical HO/TM/color projection is incomplete

```text
C55_IFERM_PHYSICAL_PROJECTION_INCOMPLETE
```

Next:

> **C56/IFPROJ — all-mode spin/HO/TM/CM/SU(3)-triplet projection completion**

## F. Sparse and matrix-free actions disagree

```text
C55_IFERM_MATRIX_ACTION_CLOSURE_FAILED
```

Next:

> **C56/IFACT — independent instantaneous-fermion sparse/matrix-free action completion**

## G. The instantaneous-fermion operator closes

```text
C55_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

Next:

> **C56/HQCD3 — resume complete local-QCD substrate assembly**

---

# 33. Required deliverables

Create at least:

```text
docs/next_level/c55_implementation_report.md
docs/next_level/c55_api.md
docs/next_level/c55_derivation_authority_manifest.json
docs/next_level/c55_input_fidelity_audit.json

docs/next_level/c55_primary_source_manifest.json
docs/next_level/c55_source_role_matrix.json
docs/next_level/c55_source_sufficiency_matrix.json
docs/next_level/c55_calculation_plan.json
docs/next_level/c55_holdout_plan.json

docs/next_level/c55_fermion_constraint_rederivation.json
docs/next_level/c55_g2_operator_extraction.json
docs/next_level/c55_instantaneous_fermion_operator_contract.json

docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
docs/next_level/c55_physical_block_classification.json
docs/next_level/c55_contact_propagating_count_once.json

docs/next_level/c55_finite_volume_normalization.json
docs/next_level/c55_state_normalization_validation.json
docs/next_level/c55_inverse_derivative_routing.json
docs/next_level/c55_zero_denominator_ledger.json
docs/next_level/c55_inverse_derivative_validation.json

docs/next_level/c55_plane_wave_kernel.json
docs/next_level/c55_spin_polarization_validation.json
docs/next_level/c55_color_operator.json
docs/next_level/c55_color_triplet_validation.json

docs/next_level/c55_pminus_to_m2_contract.json
docs/next_level/c55_pminus_to_m2_validation.json
docs/next_level/c55_physical_projection_contract.json
docs/next_level/c55_ho_tm_projection_validation.json

docs/next_level/c55_evaluator_api.json
docs/next_level/c55_evaluator_validation.json
docs/next_level/c55_physical_domain_ledger.json
docs/next_level/c55_count_once_report.json

docs/next_level/c55_physical_matrices.json
docs/next_level/c55_normal_order_contraction_report.json
docs/next_level/c55_matrix_validation.json
docs/next_level/c55_matrix_free_report.json
docs/next_level/c55_hermiticity_ordering_report.json

docs/next_level/c55_constraint_substitution_report.json
docs/next_level/c55_abelian_crosscheck.json
docs/next_level/c55_contact_topology_crosscheck.json
docs/next_level/c55_coordinate_momentum_equivalence.json

docs/next_level/c55_unit_regulator_convention_report.json
docs/next_level/c55_operator_comparison_report.json
docs/next_level/c55_comparison_remainder_ledger.json
docs/next_level/c55_isolation_report.json
docs/next_level/c55_c56_import_contract.json

docs/next_level/c55_numerical_object_inventory.json
docs/next_level/c55_readiness_report.json
docs/next_level/c55_source_sufficiency_decision.json
docs/next_level/c55_no_go_decision_tree.json
docs/next_level/c55_missing_calculation_specification.md
docs/next_level/c55_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/iferm/
```

or the repository-equivalent package.

Add focused tests for:

```text
constraint rederivation;
g_s^2 extraction;
normal ordering and monomial classification;
finite-volume normalization;
inverse derivative and zero modes;
spin/polarization kernel;
color/triplet projection;
P^- to M^2 conversion;
HO/TM/CM projection;
arbitrary-mode evaluator;
domain and count once;
sparse/matrix-free action;
Hermiticity;
independent physics checks;
unit/phase/poisoning controls;
resolution comparison;
end-to-end reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON, symbolic expressions, and runtime arrays must reproduce byte-for-byte.

---

# 34. Acceptance criteria

C55 is complete only when:

1. The full C54 baseline reproduces.
2. The C54 no-go remains explicit.
3. The C53 physical canonical vertex remains byte-identical.
4. The C43 action, C45 modes, and C47 physical basis remain unchanged.
5. C40 remains method-oracle only.
6. C47 raw canonical tuple values and metadata remain diagnostic-only.
7. No historical instantaneous coefficient enters the calculation.
8. No physical \(g_s\) or \(\alpha_s\) is chosen.
9. No arbitrary numerical \(L\) is introduced.
10. The constrained-fermion equation is transcribed exactly.
11. The \(g_s^2\) operator is extracted by two symbolic routes.
12. The exact derivative placement is retained.
13. The normal-ordering convention is source qualified.
14. Every operator monomial is enumerated.
15. Every normal-order contraction is explicit.
16. Every outside-space nonzero monomial is labeled honestly.
17. Every physical block has an executable/proved status.
18. No q-to-q or q-to-qg zero is assumed from topology language.
19. Direct contact and propagating canonical dynamics are not double counted.
20. Finite-cell field and state normalization is complete.
21. Symbolic \(L\) dependence is common, factored, or canceled.
22. Every inverse-derivative denominator is derived from operator routing.
23. No denominator uses epsilon, clipping, or a pseudoinverse.
24. Every zero denominator has a typed zero-mode/boundary status.
25. The plane-wave spin/polarization kernel is source derived.
26. Good-component and four-component routes agree.
27. Ordered SU(3) color factors are source derived.
28. Full-product and reduced-triplet routes agree.
29. No nontriplet leakage is silently discarded.
30. Every retained \(M^2\) block has mass-squared units.
31. The \(P^-\!\to M^2\) map is proved for each block.
32. The physical HO/TM/CM projection closes.
33. The arbitrary-mode evaluator is independent of historical values.
34. Every admitted basis pair is evaluated.
35. Duplicate, missing, and blocking counts are zero.
36. Direct and contraction matrices remain distinct.
37. Sparse and independent matrix-free actions agree.
38. Hermiticity follows from source ordering without post-hoc averaging.
39. Constraint-substitution equality passes.
40. Abelian, topology, and coordinate/momentum checks pass.
41. GeV/MeV, \(L\), \(P^+\), \(b_{\rm HO}\), mass, phase, PV, zero-mode, normal-ordering, and SU(3) controls pass.
42. Physical-resolution comparisons retain all remainders.
43. Static and runtime poisoning controls pass.
44. The C56 import contract is complete.
45. Runtime bundles contain actual expressions, matrices, and independent action metadata.
46. End-to-end reconstruction passes.
47. At least 224 focused live mutations are detected.
48. No free or instantaneous-current matrix is claimed complete.
49. No complete local-HQCD status is issued.
50. No projected action/current identity is claimed complete.
51. No JMY Wilson or bilocal TMD matrix is created.
52. No soft subtraction or nonlocal counterterm system is created.
53. No physical counterterm coefficient is solved.
54. No one-loop coefficient or matching kernel is created.
55. No proton TMD or ART25 bridge is created.
56. No fit, inference, process, or production route is created.
57. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
58. `MSHT20_REP/` remains untouched and outside Git.
59. The working tree is clean except for the pre-existing untracked directory.
60. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken normal ordering, inverse-derivative routing, zero-mode ownership, direct-versus-propagating count once, or physical matrix-free independence to open the gate.

---

# 35. Final Codex response

Report:

- full starting and final commits;
- exact source hierarchy and role classifications;
- source-versus-project-derived distinctions;
- constrained-fermion equation and \(g_s^2\) extraction residual;
- exact instantaneous-fermion operator expression and derivative placement;
- normal-ordering convention and every operator-monomial status;
- q/q, q/qg, qg/q, and qg/qg block decisions;
- direct-contact, propagating, contraction, counterterm, boundary, and zero-mode count-once decisions;
- finite-cell normalization and symbolic-\(L\) behavior;
- inverse-derivative routing, denominator ranges, and zero-mode statuses;
- plane-wave spin/polarization kernel residuals;
- full-product and triplet color residuals;
- \(P^-\!\to M^2\) route and residuals;
- physical HO/TM/CM projection residuals;
- exhaustive domain counts;
- physical matrix shapes, nnz, norms, units, and symbolic signatures;
- normal-order contraction/direction records;
- sparse/matrix-free residuals;
- Hermiticity and ordering residuals;
- constraint, Abelian, topology, and coordinate/momentum check residuals;
- unit, regulator, phase, normal-ordering, and wrong-color controls;
- physical-resolution comparison residuals and separated remainders;
- isolation and poisoning results;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no free, instantaneous-current, remaining constrained/contact, full local-HQCD, projected-identity, JMY Wilson/bilocal, soft, physical-counterterm, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an action-level term without finite-cell matrix elements, a normal-ordering contraction that was dropped silently, a contact matrix built from two propagating vertices, a clipped inverse denominator, or a post-hoc Hermitianized matrix as the source-derived instantaneous-fermion operator.
