# C58/IFNORM2 Codex Work Package

## Title

**Execution of the instantaneous-fermion self-induced-inertia contraction: immutable conditional-support import, source-ordered bra–ket support, finite-cell mode sums, sector-dependent q/qg representation, bare/counterterm separation, and independent matrix action**

## Authoritative baseline

Start from the clean local C57/IFREG completion commit:

```text
d9d981459dff8d21d94ef13b0a671e8140b47caa
```

Its immediate scientific parent is:

```text
1b49803a7a08d12feb5caca80f4c18b0aab795b6
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 1b49803a7a08d12feb5caca80f4c18b0aab795b6 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE

C56_IFNORM_FINITE_HO_REGULATOR_INCOMPLETE

C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
```

and the exact C57 regulator decision:

```text
operation order:
    CORRESPONDING_PROPAGATING_GRAPH_PROJECT

regulator plan:
    IFREG-CORRESPONDING-PROPAGATING-SUPPORT

regulator type:
    source-derived;
    fixed-K;
    incoming-quark-indexed;
    conditional;
    finite-HO;
    not universal;
    not BPP DLCQ;

source use:
    Tang--Brodsky--Pauli graph-selection logic;
    C45 field modes;
    C47 Fock/CM/triplet projections;

C53 role:
    support-position holdout only;
    no C53 numerical value used in construction;

C53-support holdout positions:
    K=9/2:  312
    K=11/2: 510
    K=13/2: 756

conditional field-mode union counts:
    K=9/2:  1,216
    K=11/2: 2,320
    K=13/2: 3,936

candidate mode-envelope counts:
    K=9/2:  2,304
    K=11/2: 4,400
    K=13/2: 7,488

DLCQ-to-HO conversion:
    CONVERSION_UNAVAILABLE;
    no BPP finite part imported;
    conversion not required by the selected project regulator;

not yet executed:
    no contraction contribution;
    no mode sum;
    no q or qg contraction matrix;
    no subtraction;
    no counterterm direction or coefficient;
    no direct qg contact;
    no complete instantaneous-fermion operator.
```

Verify every value, hash, basis order, support identity, and count from the committed C57 artifacts rather than relying on this prompt.

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

physical basis:
    C47 x-weighted intrinsic/CM qg basis
    exact CM-ground projection
    exact total-color triplet

instantaneous-fermion source:
    C55 source-locked g_s^2 constrained-fermion operator
    exact b-dagger a a-dagger b contraction identity
    BPP normal-ordering rule
    q <-> qg exact zero by gluon-number parity

canonical local vertex:
    C53 source-derived physical q <-> qg operator
    read-only;
    support may be used only through the independent C57 contract;
    numerical values and energy denominators are forbidden in C58.
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

# 1. Exact purpose

C58 executes the one-pair normal-ordering contraction that C55 identified and C57 regulated.

C58 must construct:

```text
a read-only import and fidelity audit of the complete C57 regulator;

the source-ordered bra–ket support rule required to turn an
incoming-quark-indexed conditional regulator into Hermitian matrix
elements;

the exact mode-resolved self-induced-inertia contribution for every
admitted contracted mode;

the complete finite-cell q-sector bare contraction sum;

the declared-scope qg-sector representation:
    spectator lift,
    sectorwise corresponding-propagating exclusion,
    sector-specific direct calculation,
    or explicit blocker;

the exact spin, polarization, color, inverse-derivative, zero-mode,
normalization, and P-minus-to-M-squared factors;

the complete bare/subtraction/counterterm decision;

source-derived local counterterm/operator directions with all
physical coefficients unsolved;

sparse primitive matrices and independent direct mode-sum actions;

Hermiticity, count-once, shell, regulator, sector, unit, phase,
poisoning, and physical-resolution diagnostics;

an immutable C59/IFERM2 import contract.
```

The contraction remains coupling factored:

\[
\Sigma_{\mathrm{SII}}
=
g_s^2\,
\widehat\Sigma_{\mathrm{SII}}^{(M^2)}.
\]

Do not choose, fit, or infer:

```text
g_s;
alpha_s;
a mass counterterm coefficient;
a wave-function counterterm coefficient;
a sector counterterm coefficient;
a subtraction constant;
a continuum finite part.
```

C58 must not construct:

```text
the direct normal-ordered qg -> qg instantaneous contact;
the complete instantaneous-fermion operator;
the free q or qg matrices;
the instantaneous color-current/gluon matrices;
the complete local-HQCD polynomial;
a projected action/current identity;
the JMY Wilson or bilocal TMD operators;
a one-loop TMD or matching coefficient.
```

The strongest allowed status is:

```text
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

When that gate passes, the exact next package is:

> **C59/IFERM2 — assemble the complete instantaneous-fermion operator from the source-derived direct contact and the immutable C58 self-induced-inertia contraction**

---

# 2. Scientific boundary

C58 is:

```text
one-pair normal-ordering-contraction specific;
fixed-K conditional-regulator specific;
source ordered;
finite-HO regulated;
bare-operator and counterterm-direction aware;
sector explicit;
coupling factored;
sparse and matrix free;
deterministic;
validation only.
```

C58 is not:

```text
a propagating one-loop self-energy calculation;
a reconstruction from two C53 vertices;
a physical mass renormalization;
a universal-field-regulator calculation;
a BPP-DLCQ numerical import;
a continuum subtraction;
a dressed-state diagonalization;
a complete instantaneous-interaction calculation.
```

The C57 regulator is a project-specific corresponding-propagating-support regulator. It must retain that name and scope.

---

# 3. Four objects that must remain distinct

C58 must preserve the following count-once separation:

## 3.1 Direct normal-ordered contact

The retained \(a^\dagger a\) part of the C55 instantaneous-fermion operator. Its physical \(qg\to qg\) matrix is deferred to C59.

## 3.2 Self-induced-inertia contraction

The commutator contribution generated by:

\[
a_\nu a^\dagger_{\nu'}
=
a^\dagger_{\nu'}a_\nu
+
[a_\nu,a^\dagger_{\nu'}].
\]

This is the C58 object.

## 3.3 Sequential propagating self-energy

The second-order canonical contribution schematically involving:

\[
V_{\rm C53}^\dagger
(E-H_0)^{-1}
V_{\rm C53}.
\]

It is not evaluated in C58 and may not define a C58 matrix element.

## 3.4 Counterterm or subtraction contribution

A separate local operator or generalized-metric direction with an unsolved coefficient, unless an exact source-defined reference subtraction is independently established.

No two of these objects may share the same contribution ID.

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_fermion_constraint_derivation.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_boundary_prescription_decision.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_zero_mode_projection_contract.json

docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c55_fermion_constraint_rederivation.json
docs/next_level/c55_g2_operator_extraction.json
docs/next_level/c55_instantaneous_fermion_operator_contract.json
docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
docs/next_level/c55_physical_block_classification.json
docs/next_level/c55_contact_propagating_count_once.json

docs/next_level/c56_contraction_identity.json
docs/next_level/c56_normal_ordering_reference.json
docs/next_level/c56_contraction_regulator_plan.json
docs/next_level/c56_regulator_plan_decision.json

docs/next_level/c57_implementation_report.md
docs/next_level/c57_derivation_authority_manifest.json
docs/next_level/c57_source_role_matrix.json
docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_field_regulator_plan.json
docs/next_level/c57_regulator_plan_decision.json
docs/next_level/c57_longitudinal_field_projector.json
docs/next_level/c57_transverse_field_projector.json
docs/next_level/c57_gluon_field_projector.json
docs/next_level/c57_projected_commutator_kernel.json
docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_fock_space_projector.json
docs/next_level/c57_shell_projector_manifest.json
docs/next_level/c57_contracted_field_mode_manifest.json
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_zero_mode_boundary_regulator.json
docs/next_level/c57_projector_comparison_maps.json
docs/next_level/c57_mode_ancestry_ledger.json
docs/next_level/c57_count_once_report.json
docs/next_level/c57_c58_import_contract.json
docs/next_level/c57_numerical_object_inventory.json
docs/next_level/c57_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c58_derivation_authority_manifest.json
docs/next_level/c58_input_fidelity_audit.json
```

---

# 5. Read-only C57 regulator import

Before evaluating one mode, verify the complete C57 import contract.

At minimum verify:

```text
operation-order ID;
regulator-plan ID;
resolution IDs;
longitudinal-projector hashes;
transverse-projector hashes;
conditional-support hashes;
projected-commutator-kernel hashes;
shell-projector hashes;
mode-manifest hashes;
field-to-qg embedding hashes;
zero-mode/boundary hashes;
comparison-map hashes;
basis-order hashes;
mode-ancestry hashes.
```

Verify the committed aggregate identities:

```text
C53 support-position holdout:
    312 / 510 / 756;

conditional field-mode union:
    1,216 / 2,320 / 3,936;

candidate envelopes:
    2,304 / 4,400 / 7,488.
```

C58 may not:

```text
add a virtual mode;
remove a virtual mode;
change the conditional support;
replace the support by the full C47 external qg basis;
replace the support by C53 nonzero values;
change a shell assignment;
change the zero-mode policy;
change the projector operation order;
change the regulator plan.
```

Create:

```text
docs/next_level/c58_c57_import_report.json
```

Any mismatch blocks all contraction evaluation.

---

# 6. Freeze construction and holdouts

Before calculating a contribution, freeze:

```text
the exact C55 contraction monomial and commutator;
the perturbative light-front normal-ordering vacuum;
the C57 conditional support for every incoming quark state;
the C57 shell decomposition;
the inverse-partial-plus prescription;
the zero-mode and residual-boundary policy;
the C45/C47 physical basis order;
the C53 SU(3) and triplet conventions;
the M^2 conversion convention;
the symbolic L policy.
```

Freeze holdouts:

```text
one contribution from each physical gluon helicity;

one exact color-completeness holdout;

smallest and largest retained k_g;

lowest and highest retained HO shell;

one conditionally rejected envelope mode;

one exact zero-mode control;

one denominator nearest zero without being zero;

both quark helicities;

one diagonal and one off-diagonal q-basis pair;

one pair with different incoming and outgoing conditional supports;

one source-Hermitian partner pair;

one q-sector full-sum holdout;

one qg-sector representation holdout;

one shell-recomposition holdout;

one GeV/MeV holdout;

one symbolic-L holdout;

one adjacent-resolution comparison holdout.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c58_calculation_plan.json
docs/next_level/c58_holdout_plan.json
```

---

# 7. The central bra–ket support problem

C57 stores an incoming-quark-indexed conditional support. A matrix element is labeled by both:

\[
\langle\alpha'|
\widehat\Sigma_{\mathrm{SII}}
|\alpha\rangle.
\]

C58 must derive, from the exact C55 operator ordering and the TBP corresponding-propagating rule, the contracted support:

\[
\mathcal I_R(\alpha',\alpha).
\]

Compile mutually exclusive support plans before evaluating a mode.

## 7.1 `IFNORM2-ORDERED-JOINT-SUPPORT`

The source operator supplies an ordered pair of canonical reachability conditions. A virtual state contributes only when it is supported by the incoming and outgoing operator attachments in their exact ordering.

The resulting set may be an intersection, but do not call it an intersection unless the derivation proves that identity.

## 7.2 `IFNORM2-HERMITIAN-ORDERED-PAIR-SUM`

The source Hamiltonian contains two ordered terms whose conditional supports are conjugate. Their source-defined sum produces the Hermitian matrix element.

This is not post-hoc averaging.

## 7.3 `IFNORM2-INCOMING-ONLY-SUPPORT`

Use the incoming support alone only if the source operator proves that the complete matrix remains Hermitian through another exact identity.

## 7.4 `IFNORM2-PAIR-SUPPORT-UNAVAILABLE`

No unique pairwise support can be derived from the C57 contract and C55 ordering.

The following are forbidden:

```text
arbitrary support union;
arbitrary support intersection;
support selected after inspecting numerical residuals;
post-hoc matrix symmetrization;
support chosen to match C53 values.
```

Create:

```text
docs/next_level/c58_bra_ket_support_contract.json
docs/next_level/c58_pair_support_decision.json
docs/next_level/c58_pair_support_validation.json
```

A positive gate requires a source-derived conjugation relation:

\[
\mathcal I_R(\alpha',\alpha)
\longleftrightarrow
\mathcal I_R(\alpha,\alpha')
\]

that supports Hermiticity term by term or by exact ordered pairing.

---

# 8. Sectorwise corresponding-propagating rule

The q-sector contraction is associated with retained \(q\to qg\to q\) support.

The qg-sector representation requires an independent scope decision. A spectator lift of the q-sector one-body operator and a sectorwise application of the corresponding-propagating rule are not automatically identical.

Compile:

## 8.1 `IFNORM2-ONE-BODY-SPECTATOR-LIFT`

The source contraction defines a universal one-body quark operator that lifts into qg with the external gluon as an exact spectator.

This plan requires direct operator and basis proof.

## 8.2 `IFNORM2-SECTORWISE-CORRESPONDING-SUPPORT`

Apply the graph-selection rule separately in each Fock sector. A qg-sector self-induced-inertia loop requires the corresponding retained intermediate sector, potentially qgg.

If that sector is absent, the qg bare contraction may be excluded with a source-qualified truncation status rather than assigned zero as an operator.

## 8.3 `IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY`

The q-sector bare contraction is retained, while the highest retained qg sector receives a separately typed renormalization direction but no bare loop contraction because its corresponding higher intermediate sector is absent.

This plan requires source-qualified Fock-sector-dependent renormalization logic.

## 8.4 `IFNORM2-DIRECT-QG-CONTRACTION`

Evaluate the C55 contraction directly between physical qg states using a separately defined conditional virtual support.

## 8.5 `IFNORM2-QG-SECTOR-UNAVAILABLE`

The q-sector contraction can be calculated, but the qg-sector representation remains unresolved.

Select exactly one primary qg-sector plan.

Do not call an absent corresponding qgg graph a vanishing full-QCD operator.

Create:

```text
docs/next_level/c58_sector_support_plan.json
docs/next_level/c58_qg_sector_scope_decision.json
```

---

# 9. Exact mode-resolved contribution

For each admitted pair support and contracted mode \(\nu\), derive:

\[
\Sigma_{\alpha'\alpha}^{(\nu,-)}
\]

directly from the C55 commutator operator.

Each record must contain:

```text
incoming and outgoing basis IDs;
pair-support ID;
contracted field-mode ID;
shell ID;
longitudinal mode;
HO mode;
gluon helicity;
adjoint color;
commutator normalization;
inverse-derivative routing;
zero-mode status;
spin/polarization tensor;
ordered color tensor;
transverse primitive;
finite-cell normalization;
P^- contribution;
M^2 contribution;
units;
symbolic signature;
source ancestry;
exact-zero reason.
```

The contribution must not be obtained from:

```text
a C53 vertex product;
a C53 energy denominator;
a C40 matrix;
a continuum self-energy formula;
a fitted shell coefficient.
```

Create:

```text
docs/next_level/c58_mode_contribution_ledger.json
```

---

# 10. Inverse-\(\partial^+\) routing and zero modes

For every contribution, inherit the C57 support but rederive the actual denominator from the C55 operator.

Record:

```text
pre-contraction field product;
post-contraction fermion product;
incoming and outgoing longitudinal modes;
contracted gluon mode;
operator ordering;
denominator mode;
exact rational denominator;
sign;
PV prescription;
P0/Q0 status;
boundary partner.
```

Every zero denominator must have one of:

```text
EXCLUDED_BY_C57_Q0_WITH_SOURCE_PROOF;

CANCELS_WITH_DECLARED_BOUNDARY_TERM;

RETAINED_ZERO_MODE_CONTROL;

ABSENT_BLOCKING.
```

Never use:

```text
epsilon;
clipping;
pseudoinverse;
deleted entries;
a finite denominator copied from a propagating graph.
```

Create:

```text
docs/next_level/c58_inverse_derivative_routing.json
docs/next_level/c58_zero_denominator_ledger.json
docs/next_level/c58_inverse_derivative_validation.json
```

---

# 11. Spin, polarization, and color contraction

## 11.1 Spin

Evaluate the fermion tensor through:

```text
the good-component constrained-field route;

an independent four-component source expression reduced by the C43
projectors.
```

Require agreement.

## 11.2 Polarization

Use the exact C57 retained physical transverse-polarization space.

Verify its projected completeness at the declared light-front-gauge scope. Keep any boundary or constrained-polarization remainder separate.

## 11.3 Color

Preserve the ordered color product from the C55 monomial.

Only after the adjoint-color contraction test whether:

\[
\sum_a T^aT^a=C_F I_3,
\qquad
C_F=\frac43,
\]

applies.

For a qg-sector representation, verify the full product-color and reduced-triplet routes independently.

Required checks:

```text
good-component/four-component equality;
polarization completeness;
ordered-color identity;
fundamental/adjoint covariance;
triplet preservation;
basis-rotation covariance;
Abelian limit;
no hidden nontriplet leakage.
```

Create:

```text
docs/next_level/c58_spin_polarization_contraction.json
docs/next_level/c58_color_contraction.json
docs/next_level/c58_spin_color_validation.json
```

---

# 12. Finite-cell normalization

Derive every factor from:

```text
the two C45 gauge-field expansions;
the projected C57 commutator;
the C43 quark fields;
the finite-cell canonical brackets;
the x^- integration;
the transverse integration;
the q or qg state normalization;
the conditional support.
```

Keep \(L\) symbolic.

Determine whether each physical block:

```text
is L independent;

has one block-common factored L power;

or retains a source-defined finite-volume dependence.
```

An element-dependent \(L\) signature is blocking.

Create:

```text
docs/next_level/c58_finite_volume_normalization.json
docs/next_level/c58_normalization_validation.json
```

---

# 13. Component-wise \(P^-\!\to M^2\) conversion

Construct:

\[
\widehat\Sigma_{\mathrm{SII}}^{(-)}
\]

and:

\[
\widehat\Sigma_{\mathrm{SII}}^{(M^2)}.
\]

Use:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Prove separately for every retained sector:

```text
same total P^+ on bra and ket;
same total transverse/CM frame;
off-diagonal P_perp^2 status;
state-normalization compatibility;
factor of two in the project convention.
```

Do not reuse the C50 conversion merely by label.

Every completed \(M^2\) primitive must have uniform mass-squared units.

Create:

```text
docs/next_level/c58_pminus_to_m2_contract.json
docs/next_level/c58_pminus_to_m2_validation.json
```

---

# 14. Shell and mode sums

For every matrix element, sum only over the immutable C57 pair support:

\[
\widehat\Sigma_{\alpha'\alpha}^{(M^2)}
=
\sum_{\nu\in\mathcal I_R(\alpha',\alpha)}
\Sigma_{\alpha'\alpha}^{(\nu,M^2)}.
\]

Retain partial sums by:

```text
longitudinal mode;
HO shell;
gluon helicity;
adjoint color;
zero-mode/boundary class;
ordered source term.
```

Require:

```text
mode contributions sum to shell contributions;
shell contributions sum to the full pair result;
support-union accounting closes;
no envelope-only mode contributes;
no admitted conditional mode is omitted;
no mode is duplicated.
```

Create:

```text
docs/next_level/c58_shell_partial_sum_report.json
docs/next_level/c58_mode_sum_recomposition.json
```

---

# 15. q-sector bare contraction

Assemble the complete physical q-sector primitive:

\[
\widehat\Sigma_{q,R}^{(M^2)}.
\]

Do not assume that it is:

```text
diagonal;
helicity independent;
HO diagonal;
longitudinal-mode independent;
proportional to the identity;
proportional to the free mass direction.
```

Required outputs:

```text
sparse primitive matrix;
executable symbolic coefficient;
independent direct mode-sum action;
basis-element ancestry;
shell-resolved diagnostics;
Hermitian spectrum or rigorous bounds.
```

Required checks:

```text
source Hermiticity;
K, Jz, helicity, and color rules;
mass-squared units;
symbolic-L behavior;
direct versus matrix-free action;
pair-support conjugation;
no post-hoc symmetrization.
```

Create:

```text
docs/next_level/c58_q_sector_contraction.json
docs/next_level/c58_q_sector_validation.json
```

---

# 16. qg-sector representation

Execute the selected qg-sector plan.

If spectator lift is selected, construct the one-body lift in the raw qg product basis and then apply:

```text
the C47 x-weighted TM/Jacobi map;
the exact CM-ground projector;
the C53 triplet convention.
```

Also evaluate an independent direct qg matrix-element route.

If sectorwise exclusion is selected, retain:

```text
the nonzero full-QCD operator identity;
the absent corresponding qgg support;
the exact truncation status;
the required sector counterterm direction;
the first omitted Fock sector.
```

Do not serialize an excluded truncated contribution as a zero full-QCD operator.

Required checks, as applicable:

```text
spectator identity;
direct/lift equality;
CM preservation;
triplet preservation;
K and Jz conservation;
sector-support ownership;
source Hermiticity;
sector-dependent remainder.
```

Create:

```text
docs/next_level/c58_qg_sector_contraction.json
docs/next_level/c58_sector_lift_validation.json
docs/next_level/c58_sector_truncation_report.json
```

---

# 17. Bare, subtraction, and counterterm plans

After the bare sums exist, compile mutually exclusive plans.

## 17.1 `IFNORM2-BARE-RETAINED-SEPARATE-CT`

Retain the complete C57-regulated contraction in the bare local \(g_s^2\) operator. Define local counterterm directions separately. Apply no reference subtraction.

## 17.2 `IFNORM2-SOURCE-REFERENCE-SUBTRACTED`

Apply an exact source-defined subtraction with a specified reference state, regulator, finite part, and counterterm relation.

Preserve both unsubtracted and subtracted operators.

## 17.3 `IFNORM2-REGULATOR-CONVERTED`

Use an exact operator-identical finite conversion from another regulator, with inverse or visible remainder.

C57's `CONVERSION_UNAVAILABLE` prevents this plan unless a new source-qualified conversion is actually constructed and supersedes that record.

## 17.4 `IFNORM2-SECTOR-DEPENDENT-BARE-AND-CT`

Retain sectorwise bare contributions according to corresponding-propagating support and define distinct sector counterterm directions.

## 17.5 `IFNORM2-SUBTRACTION-PLAN-UNAVAILABLE`

The bare result exists, but its placement in the local Hamiltonian cannot be typed consistently.

Select exactly one plan.

The finite HO mode sum is a regulator-dependent bare operator, not a physical renormalized mass.

Create:

```text
docs/next_level/c58_bare_subtraction_counterterm_plan.json
docs/next_level/c58_renormalization_plan_decision.json
```

---

# 18. Counterterm and operator-direction typing

Construct a source-owned direction basis containing at least:

```text
quark mass-squared direction;
quark field/residue or generalized-metric direction;
q-sector-specific mass direction;
qg-sector-specific mass direction;
local basis-boundary direction;
zero-mode direction;
self-induced-inertia direction.
```

For every sector and resolution, evaluate the contraction against this direction basis using the correct Gram or generalized metric.

Report:

```text
direction Gram matrix;
rank;
nullity;
condition number;
diagnostic projection coefficients;
parallel component;
orthogonal residual;
operator-norm residual;
comparison-map behavior.
```

Diagnostic projection coefficients are not physical counterterm coefficients.

Allowed outcomes:

```text
PURE_MASS_DIRECTION;

MASS_PLUS_METRIC_DIRECTION;

SECTOR_DEPENDENT_EXISTING_DIRECTIONS;

NEW_LOCAL_SELF_INDUCED_INERTIA_DIRECTION_REQUIRED;

TRUNCATED_HIGHEST_SECTOR_CT_DIRECTION_ONLY;

UNRESOLVED_BLOCKING.
```

Do not force a nonzero residual into one universal scalar mass term.

Create:

```text
docs/next_level/c58_counterterm_direction_basis.json
docs/next_level/c58_counterterm_typing_report.json
docs/next_level/c58_sector_dependence_report.json
```

---

# 19. Fock-sector universality audit

Keep separate the claims:

```text
the same source one-body operator exists in every sector;

the C57 regulator gives the same virtual support in every sector;

the qg matrix is a spectator lift of the q matrix;

one scalar counterterm coefficient works in both sectors;

the renormalized physical self-energy is sector independent.
```

C58 may establish the first or third without establishing the fourth or fifth.

Create:

```text
docs/next_level/c58_fock_sector_universality_contract.json
docs/next_level/c58_fock_sector_universality_validation.json
```

---

# 20. Count-once relation to all local self-energy objects

Extend the C55/C56/C57 ledgers.

Keep distinct:

```text
direct normal-ordered instantaneous contact;
C58 self-induced-inertia contraction;
C53 sequential propagating self-energy;
free quark mass;
mass counterterm direction;
field/residue direction;
sector counterterm direction;
boundary and zero-mode completion;
instantaneous color-current self-energy;
future loop/matching self-energy.
```

No object may enter twice under different names.

Create:

```text
docs/next_level/c58_local_self_energy_count_once.json
```

---

# 21. Arbitrary-mode evaluator

Create:

```python
evaluate_self_induced_inertia(
    incoming_basis_id,
    outgoing_basis_id,
    sector,
    resolution,
    symbolic_parameters,
) -> SelfInducedInertiaEvaluation
```

The result must include:

```text
sector;
basis IDs;
pair-support ID;
contracted-mode count;
mode and shell partial sums;
inverse-derivative routing;
zero-mode status;
spin/polarization result;
color result;
P^- value;
M^2 value;
units;
symbolic signature;
counterterm typing;
source ancestry;
exact-zero or truncation reason.
```

The evaluator must not consume:

```text
C40 instantaneous values;
C47 raw canonical tuple values;
C50 combined canonical values;
C53 physical vertex values;
a C53 energy denominator;
a BPP DLCQ finite sum;
a fitted mass shift.
```

Create:

```text
docs/next_level/c58_evaluator_api.json
docs/next_level/c58_evaluator_validation.json
```

---

# 22. Exhaustive physical-domain ledger

Enumerate every q/q pair and every qg/qg pair required by the selected sector plan.

Each receives exactly one status:

```text
PRESELECTION_FORBIDDEN_EXACT;

EVALUATED_EXACT_ZERO;

EVALUATED_NONZERO;

EXCLUDED_BY_CORRESPONDING_PROPAGATING_RULE;

COUNTERTERM_DIRECTION_ONLY;

EVALUATOR_UNAVAILABLE_BLOCKING;

DUPLICATE_BLOCKING.
```

Report:

```text
Cartesian pair count;
preselection count;
pair-support count;
evaluator calls;
exact-zero count;
nonzero count;
truncation-exclusion count;
counterterm-only count;
duplicate count;
missing count;
blocking count.
```

A positive gate requires:

```text
duplicate = 0;
missing = 0;
blocking = 0.
```

Create:

```text
docs/next_level/c58_physical_domain_ledger.json
docs/next_level/c58_count_once_report.json
```

---

# 23. Sparse primitive matrices

Assemble only the self-induced-inertia primitive matrices authorized by the sector plan.

Store separately:

```text
primitive sparse matrix;
executable symbolic coefficient;
g_s^2 coupling-order label;
sector status;
counterterm/operator-direction records;
diagnostic evaluated matrices at explicitly nonphysical substitutions.
```

Do not insert a physical \(g_s\).

Create:

```text
docs/next_level/c58_contraction_matrices.json
docs/next_level/c58_matrix_validation.json
```

---

# 24. Independent direct mode-sum action

Implement:

```python
apply_self_induced_inertia(
    vector_q,
    vector_qg,
    resolution,
    symbolic_parameters,
)
```

The independent route must:

```text
reconstruct pair supports from the immutable C57 contract;
iterate the exact contracted modes;
evaluate the C55 source kernel;
accumulate q and qg actions according to the selected sector plan;
retain shell and counterterm diagnostics.
```

It must not:

```text
multiply by the stored C58 matrices;
load the C58 entry ledger as numerical authority;
construct the contraction from C53 V-dagger D-inverse V;
load C53 numerical values;
consume historical coefficients.
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
docs/next_level/c58_matrix_free_report.json
```

---

# 25. Hermiticity and conditional-support closure

Hermiticity must follow from:

```text
the source Hamiltonian ordering;
the pair-support contract;
mode-level conjugation;
denominator conjugation;
spin/polarization conjugation;
ordered color conjugation.
```

Do not repair the matrix with:

\[
M\to\frac12(M+M^\dagger).
\]

Report:

```text
mode-level conjugation residual;
pair-support conjugation residual;
shell-level residual;
full-matrix Hermiticity residual;
ordered-term pairing residual;
basis-phase covariance.
```

If the incoming-indexed conditional regulator cannot produce a source-Hermitian pair support, issue:

```text
C58_IFNORM_CONDITIONAL_SUPPORT_HERMITICITY_INCOMPLETE
```

rather than symmetrizing.

Create:

```text
docs/next_level/c58_hermiticity_support_report.json
docs/next_level/c58_spectrum_report.json
```

Do not clip negative eigenvalues. Positivity is not required unless the source proves it.

---

# 26. Regulator fingerprints

Report the bare contraction through:

```text
conditional-support-size distribution;
mode-union fraction relative to the C57 envelope;
longitudinal-mode partial sums;
HO-shell partial sums;
small-k_g sensitivity;
highest-shell sensitivity;
bHO scaling;
symbolic-L behavior;
q-sector versus qg-sector behavior;
counterterm-direction residuals.
```

The three physical points change \(K\), \(N_{\max}\), and \(b_{\rm HO}\) together. Do not call them a continuum trajectory.

A factorized diagnostic scan is permitted only when it uses the immutable C57 generator and is labeled:

```text
NONPHYSICAL_REGULATOR_DIAGNOSTIC
```

It may not define a subtraction or counterterm coefficient.

Create:

```text
docs/next_level/c58_regulator_fingerprint_report.json
docs/next_level/c58_shell_asymptotic_diagnostics.json
```

---

# 27. Physical-resolution comparison

Use the C57/C47 comparison maps to evaluate:

\[
R\,\widehat\Sigma_{\mathrm{SII},R'}\,P
\quad\text{versus}\quad
\widehat\Sigma_{\mathrm{SII},R}.
\]

Execute separately for:

```text
q-sector bare contraction;
qg-sector representation;
mass-direction component;
metric component;
sector-specific direction;
orthogonal self-induced-inertia residual.
```

Separate:

```text
longitudinal nonnesting;
HO-shell truncation;
bHO scale change;
conditional-support change;
CM projection;
triplet representation;
zero-mode/boundary change;
symbolic normalization;
numerical error.
```

Do not tune a subtraction or direction coefficient to reduce the residual.

Create:

```text
docs/next_level/c58_operator_comparison_report.json
docs/next_level/c58_comparison_remainder_ledger.json
```

---

# 28. Independent checks

## 28.1 Commutator versus explicit vacuum contraction

Evaluate frozen holdouts by both routes.

## 28.2 Mode sum versus shell sum

Require exact recomposition.

## 28.3 Source support versus C53 support holdout

The independently constructed C57 support must continue to match the C53 support positions:

```text
312 / 510 / 756
```

without using C53 numerical values in the contraction.

## 28.4 Good-component versus four-component spin route

Require agreement.

## 28.5 Full color sum versus reduced color result

Require agreement.

## 28.6 Abelian limit

Remove QCD color while preserving the same finite-cell and conditional support.

## 28.7 Sector representation

Compare direct and spectator-lift routes where the selected qg plan requires both.

Create:

```text
docs/next_level/c58_vacuum_commutator_crosscheck.json
docs/next_level/c58_shell_recomposition_report.json
docs/next_level/c58_c53_support_holdout.json
docs/next_level/c58_spin_route_crosscheck.json
docs/next_level/c58_color_route_crosscheck.json
docs/next_level/c58_abelian_crosscheck.json
docs/next_level/c58_sector_representation_crosscheck.json
```

---

# 29. Unit, regulator, and convention covariance

Execute:

```text
GeV/MeV conversion;
symbolic-L scaling or cancellation;
fixed-x P^+ rescaling;
bHO scaling and basis transformation;
quark-mass variation;
Fourier phase;
gluon-polarization phase;
triplet phase;
PV prescription controls;
zero-mode-projector controls;
normal-ordering-vacuum controls;
pair-support controls;
omitted/duplicated contraction controls;
wrong SU(3) controls;
factor-of-two M^2 control.
```

Require:

```text
every completed M^2 primitive scales as mass squared;
all symbolic signatures are block consistent;
dimensionless residuals are invariant;
wrong conventions fail explicitly.
```

Create:

```text
docs/next_level/c58_unit_regulator_convention_report.json
```

---

# 30. Isolation and poisoning controls

Prove that C58 is unchanged when:

```text
all C40 arrays are poisoned;
all historical C47 tuple values and metadata are poisoned;
all C50 combined values are poisoned;
all C53 physical matrix values are poisoned;
all BPP DLCQ finite-sum values are inaccessible;
all ART25 files are inaccessible.
```

The build must fail when:

```text
a C57 support hash changes;
a C57 shell assignment changes;
the C57 operation order changes;
the C57 regulator-plan ID changes;
the C55 contraction monomial changes;
the normal-ordering vacuum changes;
the inverse-derivative prescription changes;
the zero-mode policy changes;
the pair-support rule changes without supersession;
a conditional support is relabeled universal.
```

Create:

```text
docs/next_level/c58_isolation_report.json
```

---

# 31. C59/IFERM2 import contract

Define the immutable contract by which C59 will consume:

```text
the selected pair-support plan;
the selected qg-sector plan;
the q and qg contraction primitive matrices or exact truncation statuses;
the executable symbolic coefficient;
the g_s^2 coupling-order label;
the bare/subtraction/counterterm plan;
the counterterm/operator-direction typing;
the conditional-support and shell ancestry;
the zero-mode and boundary statuses;
the independent matrix-free action;
the count-once, Hermiticity, and comparison ledgers.
```

C59 must verify every hash before constructing the direct qg contact.

C59 may not:

```text
change the C57 regulator;
change pair support;
rescale the contraction;
apply a new subtraction;
fit a counterterm coefficient;
replace the contraction by C53 propagation.
```

Create:

```text
docs/next_level/c58_c59_import_contract.json
```

---

# 32. Deterministic runtime bundles

For every resolution produce content-addressed bundles containing:

```text
pair-support tables;
mode contribution ledger;
shell partial sums;
q-sector primitive matrix;
qg-sector primitive matrix or exact sector-status object;
symbolic coefficient;
counterterm-direction records;
matrix-free reconstruction metadata;
domain and count-once ledgers;
Hermiticity records;
holdout and comparison records.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c58_ifnorm2/
```

Commit an inventory containing:

```text
runtime path;
shape;
dtype;
nnz;
units;
coupling order;
symbolic signature;
C57 regulator-plan ID;
pair-support-plan ID;
qg-sector-plan ID;
basis-order hash;
support hash;
expression hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c58_numerical_object_inventory.json
```

All JSON, expressions, and arrays must regenerate byte-for-byte.

---

# 33. End-to-end source-to-contraction test

Implement an end-to-end test that starts from the C43/C45/C47/C55/C57 contracts—not from prebuilt C58 matrices.

It must:

```text
verify the C57 import;
derive the pair-support rule;
select the qg-sector plan;
iterate every admitted conditional mode;
derive inverse-derivative routing;
evaluate spin, polarization, and color;
derive finite-cell normalization;
convert P^- to M^2;
sum modes and shells;
assemble the q-sector result;
construct or classify the qg-sector representation;
select the bare/subtraction/counterterm plan;
type counterterm directions;
assemble primitive matrices;
apply the independent matrix-free action;
run Hermiticity, shell, holdout, unit, poisoning, and comparison tests;
reproduce every hash.
```

It must fail when:

```text
a C57 mode is added or removed;
an arbitrary support union or intersection is used;
the matrix is symmetrized after construction;
a C53 numerical value or energy denominator enters;
the contraction is replaced by V-dagger D-inverse V;
a BPP DLCQ finite part is imported;
a zero denominator is clipped;
the bare sum is hidden in the input mass;
a subtraction is applied without a source plan;
a qg spectator lift is assumed without sector proof;
a sector-dependent residual is forced into one universal counterterm;
a physical g_s or counterterm coefficient is inserted;
a runtime hash changes.
```

---

# 34. Focused mutation tests

Create at least **256 focused live mutations** of actual supports, contributions, sums, directions, or matrices.

Include mutations of:

```text
C57 support identity;
incoming-quark index;
bra–ket support relation;
ordered support term;
contracted mode;
longitudinal mode;
HO shell;
gluon helicity;
adjoint color;
commutator sign;
normal-ordering vacuum;
inverse-derivative denominator;
PV prescription;
zero-mode status;
spin tensor;
polarization vector;
color ordering;
finite-cell normalization;
L power;
P^+ power;
P^- to M^2 factor;
q-sector matrix entry;
qg-sector plan;
spectator lift;
CM projector;
triplet map;
bare/subtraction plan;
counterterm direction;
sector-universality status;
matrix-free accumulation;
Hermitian partner;
shell recomposition;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, support, normal-ordering, zero-mode, dimension, color, Hermiticity, typing, count-once, matrix-free, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 35. Readiness gate

Issue:

```text
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

only when:

```text
the full C57 baseline reproduces;

all C57 regulator objects import read-only;

the 312/510/756 support holdout remains closed;

the 1,216/2,320/3,936 mode unions and
2,304/4,400/7,488 envelopes reproduce;

the exact source-derived bra–ket support rule is selected;

conditional support produces source Hermiticity without post-hoc repair;

the qg-sector representation receives a complete source-qualified
status;

every admitted mode contribution is evaluated;

inverse-derivative routing is explicit;

every zero denominator has a typed status;

spin, polarization, and color sums close;

finite-cell normalization closes;

P^- to M^2 conversion closes;

mode, shell, and full sums recompose;

the q-sector bare contraction exists at all resolutions;

the qg-sector matrix or exact truncation/counterterm-only status is complete;

one bare/subtraction/counterterm plan is selected;

the bare contraction is never silently removed;

counterterm/operator typing is complete with visible residual;

Fock-sector universality claims are no stronger than the calculation;

direct contact, propagation, contraction, counterterm, boundary,
zero-mode, and future loop objects remain count-once distinct;

the exhaustive domain has no duplicate, missing, or blocking row;

sparse and independent direct mode-sum actions agree;

Hermiticity follows from source ordering and support;

regulator fingerprints and physical-resolution comparisons execute;

independent vacuum, shell, support, spin, color, Abelian, and sector
checks pass;

unit, regulator, phase, zero-mode, support, and poisoning tests pass;

the C59 import contract is complete;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-contraction test passes.
```

Do not issue:

```text
C58_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C58_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C58_PHYSICAL_MASS_RENORMALIZATION_SOLVED;

C58_PROJECTED_ACTION_IDENTITY_READY;

C58_JMY_WILSON_MATRIX_VALIDATED;

C58_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 36. Exact no-go branches

## A. C57 import or support identity fails

```text
C58_IFNORM_C57_IMPORT_INCOMPLETE
```

Next:

> **C59/IFREG2 — regulator artifact, support, shell, and embedding integrity completion**

## B. Bra–ket support remains ambiguous

```text
C58_IFNORM_PAIR_SUPPORT_INCOMPLETE
```

Next:

> **C59/IFPAIR — source-ordered joint support and Hermitian conditional-regulator completion**

## C. Mode kernel or normalization remains incomplete

```text
C58_IFNORM_MODE_KERNEL_INCOMPLETE
```

Next:

> **C59/IFKERNEL — commutator contribution, spin/color, finite-cell normalization, and M-squared completion**

## D. Inverse derivative or zero modes remain incomplete

```text
C58_IFNORM_ZERO_MODE_ROUTING_INCOMPLETE
```

Next:

> **C59/IFZERO4 — contracted-mode denominator, PV, boundary, and zero-mode completion**

## E. Conditional support cannot produce source Hermiticity

```text
C58_IFNORM_CONDITIONAL_SUPPORT_HERMITICITY_INCOMPLETE
```

Next:

> **C59/IFHERM — ordered conditional-support and source-Hermitian operator completion**

## F. qg-sector representation remains incomplete

```text
C58_IFNORM_SECTOR_REPRESENTATION_INCOMPLETE
```

Next:

> **C59/IFSECTOR — spectator lift, qgg truncation, and sector-dependent renormalization completion**

## G. Bare/subtraction plan remains incomplete

```text
C58_IFNORM_SUBTRACTION_PLAN_INCOMPLETE
```

Next:

> **C59/IFSUB2 — bare contraction, reference subtraction, and regulator-conversion decision**

## H. Counterterm typing remains incomplete

```text
C58_IFNORM_COUNTERTERM_TYPING_INCOMPLETE
```

Next:

> **C59/IFCT2 — mass, metric, sector, boundary, and independent self-induced-inertia direction completion**

## I. Sparse and matrix-free actions disagree

```text
C58_IFNORM_MATRIX_ACTION_CLOSURE_FAILED
```

Next:

> **C59/IFACT3 — independent conditional mode-sum sparse/matrix-free action completion**

## J. Self-induced-inertia contraction closes

```text
C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

Next:

> **C59/IFERM2 — assemble the complete instantaneous-fermion operator**

---

# 37. Required deliverables

Create at least:

```text
docs/next_level/c58_implementation_report.md
docs/next_level/c58_api.md
docs/next_level/c58_derivation_authority_manifest.json
docs/next_level/c58_input_fidelity_audit.json

docs/next_level/c58_c57_import_report.json
docs/next_level/c58_calculation_plan.json
docs/next_level/c58_holdout_plan.json

docs/next_level/c58_bra_ket_support_contract.json
docs/next_level/c58_pair_support_decision.json
docs/next_level/c58_pair_support_validation.json
docs/next_level/c58_sector_support_plan.json
docs/next_level/c58_qg_sector_scope_decision.json

docs/next_level/c58_mode_contribution_ledger.json
docs/next_level/c58_inverse_derivative_routing.json
docs/next_level/c58_zero_denominator_ledger.json
docs/next_level/c58_inverse_derivative_validation.json

docs/next_level/c58_spin_polarization_contraction.json
docs/next_level/c58_color_contraction.json
docs/next_level/c58_spin_color_validation.json

docs/next_level/c58_finite_volume_normalization.json
docs/next_level/c58_normalization_validation.json
docs/next_level/c58_pminus_to_m2_contract.json
docs/next_level/c58_pminus_to_m2_validation.json

docs/next_level/c58_shell_partial_sum_report.json
docs/next_level/c58_mode_sum_recomposition.json

docs/next_level/c58_q_sector_contraction.json
docs/next_level/c58_q_sector_validation.json
docs/next_level/c58_qg_sector_contraction.json
docs/next_level/c58_sector_lift_validation.json
docs/next_level/c58_sector_truncation_report.json

docs/next_level/c58_bare_subtraction_counterterm_plan.json
docs/next_level/c58_renormalization_plan_decision.json
docs/next_level/c58_counterterm_direction_basis.json
docs/next_level/c58_counterterm_typing_report.json
docs/next_level/c58_sector_dependence_report.json
docs/next_level/c58_fock_sector_universality_contract.json
docs/next_level/c58_fock_sector_universality_validation.json
docs/next_level/c58_local_self_energy_count_once.json

docs/next_level/c58_evaluator_api.json
docs/next_level/c58_evaluator_validation.json
docs/next_level/c58_physical_domain_ledger.json
docs/next_level/c58_count_once_report.json
docs/next_level/c58_contraction_matrices.json
docs/next_level/c58_matrix_validation.json
docs/next_level/c58_matrix_free_report.json
docs/next_level/c58_hermiticity_support_report.json
docs/next_level/c58_spectrum_report.json

docs/next_level/c58_regulator_fingerprint_report.json
docs/next_level/c58_shell_asymptotic_diagnostics.json
docs/next_level/c58_operator_comparison_report.json
docs/next_level/c58_comparison_remainder_ledger.json

docs/next_level/c58_vacuum_commutator_crosscheck.json
docs/next_level/c58_shell_recomposition_report.json
docs/next_level/c58_c53_support_holdout.json
docs/next_level/c58_spin_route_crosscheck.json
docs/next_level/c58_color_route_crosscheck.json
docs/next_level/c58_abelian_crosscheck.json
docs/next_level/c58_sector_representation_crosscheck.json

docs/next_level/c58_unit_regulator_convention_report.json
docs/next_level/c58_isolation_report.json
docs/next_level/c58_c59_import_contract.json

docs/next_level/c58_numerical_object_inventory.json
docs/next_level/c58_readiness_report.json
docs/next_level/c58_source_sufficiency_decision.json
docs/next_level/c58_no_go_decision_tree.json
docs/next_level/c58_missing_calculation_specification.md
docs/next_level/c58_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/ifnorm2/
```

or the repository-equivalent package.

Add focused tests for:

```text
C57 import;
pair-support derivation;
sector-support plan;
mode contributions;
inverse derivative and zero modes;
spin/polarization/color sums;
finite-cell normalization;
P^- to M^2 conversion;
shell recomposition;
q-sector assembly;
qg-sector representation;
bare/subtraction decision;
counterterm typing;
sector universality;
count once;
arbitrary evaluator;
sparse/matrix-free action;
Hermiticity;
unit/poisoning controls;
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

# 38. Acceptance criteria

C58 is complete only when:

1. The full C57 baseline reproduces.
2. The C57 positive gate remains explicit.
3. The C55 contraction identity and normal-ordering vacuum remain unchanged.
4. The C53 canonical vertex remains read-only.
5. The C43 action, C45 modes, and C47 physical basis remain unchanged.
6. C40 remains method-oracle only.
7. Historical C47 tuple values and metadata remain diagnostic-only.
8. No C53 numerical value or energy denominator enters.
9. No BPP DLCQ finite sum is imported.
10. No physical \(g_s\), \(\alpha_s\), subtraction, or counterterm coefficient is chosen.
11. No arbitrary numerical \(L\) is introduced.
12. Every C57 import hash passes.
13. The C57 operation order and regulator plan are immutable.
14. The 312/510/756 support holdout reproduces.
15. The 1,216/2,320/3,936 mode unions reproduce.
16. The 2,304/4,400/7,488 envelopes reproduce.
17. A source-derived bra–ket pair-support rule is selected.
18. No ad hoc union or intersection is used.
19. Pair support obeys the exact conjugation relation.
20. Hermiticity is not repaired post hoc.
21. A complete qg-sector plan is selected.
22. Highest-sector truncation is not mislabeled as a zero full-QCD operator.
23. Every admitted contracted mode is evaluated.
24. Every mode contribution has complete ancestry.
25. No envelope-only mode contributes.
26. No admitted conditional mode is omitted.
27. Every inverse denominator follows exact operator routing.
28. No epsilon, clipping, pseudoinverse, or deletion is used.
29. Every zero denominator has a typed status.
30. Good-component and four-component spin routes agree.
31. Polarization completeness closes at the declared scope.
32. Ordered color contraction closes.
33. No nontriplet leakage is hidden.
34. Finite-cell normalization is complete.
35. Symbolic \(L\) dependence is common, factored, or canceled.
36. \(P^-\!\to M^2\) conversion closes in every retained sector.
37. Every completed primitive has mass-squared units.
38. Mode, shell, and full-sum recomposition closes.
39. The q-sector bare contraction exists at every resolution.
40. The qg-sector matrix or exact truncation/counterterm-only status is complete.
41. One bare/subtraction/counterterm plan is selected.
42. The bare contraction is never silently removed.
43. No source-free reference subtraction is applied.
44. Counterterm/operator directions are source derived.
45. A nonzero residual is not forced into a universal mass direction.
46. Fock-sector universality claims remain separated.
47. Direct contact, propagation, contraction, counterterm, boundary, zero-mode, and future loop terms are count-once distinct.
48. Every admitted physical pair is evaluated or exactly classified.
49. Duplicate, missing, and blocking counts are zero.
50. Sparse and independent direct mode-sum actions agree.
51. Hermiticity follows from source ordering and pair support.
52. Negative eigenvalues are not clipped.
53. Regulator fingerprints remain visible.
54. Three correlated physical resolutions are not called a continuum extrapolation.
55. Comparison maps retain all separated remainders.
56. Vacuum, shell, support, spin, color, Abelian, and sector checks pass.
57. GeV/MeV, \(L\), \(P^+\), \(b_{\rm HO}\), mass, phase, PV, zero-mode, support, factor-of-two, and SU(3) controls pass.
58. Static and runtime poisoning controls pass.
59. The C59 import contract is complete.
60. Runtime bundles contain actual mode contributions, expressions, matrices/statuses, and independent action metadata.
61. End-to-end reconstruction passes.
62. At least 256 focused live mutations are detected.
63. No direct qg contact matrix is claimed complete.
64. No complete instantaneous-fermion status is issued.
65. No free or instantaneous-current matrix is claimed complete.
66. No complete local-HQCD status is issued.
67. No projected action/current identity is claimed complete.
68. No JMY Wilson or bilocal TMD matrix is created.
69. No soft subtraction or nonlocal counterterm system is created.
70. No physical mass-renormalization result is claimed.
71. No one-loop TMD coefficient or matching kernel is created.
72. No proton TMD or ART25 bridge is created.
73. No fit, inference, process, or production route is created.
74. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
75. `MSHT20_REP/` remains untouched and outside Git.
76. The working tree is clean except for the pre-existing untracked directory.
77. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken pair-support ownership, sectorwise graph selection, inverse-derivative routing, bare/subtraction separation, counterterm typing, source Hermiticity, or independent mode-sum action to open the gate.

---

# 39. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C55/C57 inputs consumed;
- C57 import hashes and reproduced support/mode counts;
- selected bra–ket support plan and rejected alternatives;
- pair-support conjugation and Hermiticity logic;
- selected qg-sector plan and rejected alternatives;
- mode contribution counts and ranges by \(k_g\), shell, helicity, and color;
- inverse-derivative denominator ranges and zero-mode statuses;
- spin, polarization, and color residuals;
- finite-cell normalization and symbolic-\(L\) behavior;
- \(P^-\!\to M^2\) residuals;
- shell and full-sum recomposition residuals;
- q-sector primitive shape, nnz, norm/spectrum, units, and symbolic signature;
- qg-sector primitive or exact truncation/counterterm-only status;
- direct/spectator-lift or sectorwise-support residuals;
- selected bare/subtraction/counterterm plan;
- counterterm-direction basis, rank, condition number, typing, and orthogonal residual;
- Fock-sector universality result;
- direct/contact/propagating/contraction/counterterm/boundary/zero-mode count-once decisions;
- physical-domain counts;
- sparse/direct-mode-sum matrix-free residuals;
- source-Hermiticity residuals;
- regulator fingerprints and partial sums;
- physical-resolution comparison residuals and separated remainders;
- independent vacuum, shell, support, spin, color, Abelian, and sector checks;
- unit, regulator, phase, support, zero-mode, wrong-color, and poisoning controls;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no direct contact, complete instantaneous-fermion operator, free/current/local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop TMD, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an arbitrary support intersection, a post-hoc Hermitianized matrix, a qg spectator lift without sector proof, a contraction built from C53 values, a BPP DLCQ finite sum relabeled as HO, a hidden bare mass shift, or a fitted counterterm coefficient as the completed source-derived normal-ordering contraction.
