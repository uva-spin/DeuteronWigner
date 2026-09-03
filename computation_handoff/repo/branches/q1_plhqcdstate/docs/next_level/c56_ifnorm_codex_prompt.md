# C56/IFNORM Codex Work Package

## Title

**Finite-HO normal-ordering closure for the instantaneous-fermion interaction: one-pair \(a a^\dagger\) self-induced-inertia contraction, regulator ownership, bare/subtracted/counterterm separation, sector lift, and comparison-map diagnostics**

## Authoritative baseline

Start from the clean local C55/IFERM fail-closed completion commit:

```text
12796e04f81158bc90da96cb27d29b33eea6e08e
```

Its immediate scientific parent is:

```text
3717d1a70184c6cc70dfc985534c38f51a7d1476
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 3717d1a70184c6cc70dfc985534c38f51a7d1476 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C54_INSTANTANEOUS_FERMION_ASSEMBLY_INCOMPLETE

C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE
```

and the exact C55 scientific boundary:

```text
source authority:
    Srivastava--Brodsky instantaneous g_s^2 term locked and
    convention mapped;

normal-ordering authority:
    BPP Eq. (2.97) locked and convention mapped;

symbolic g_s^2 coefficient:
    direct expansion and exact second-derivative routes agree;

field-choice inventory:
    16 total choices;
    14 non-vacuum monomials retained in the ledger;

physical block result already proved:
    q <-> qg instantaneous-fermion blocks vanish by exact
    gluon-number parity/operator algebra;

count-once result:
    direct instantaneous contact remains distinct from sequential
    C53 propagation;

unresolved required object:
    the one-pair a a-dagger normal-ordering contraction,
    identified by BPP as a self-induced-inertia term;

missing C45/C47 authority:
    finite-HO contraction regulator;
    subtraction/reference prescription;
    counterterm/operator typing;

consequence:
    no physical instantaneous-fermion matrix was created.
```

Verify every statement from the committed C55 records rather than relying on this prompt.

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
    read-only and not part of the C56 contraction calculation

instantaneous-fermion source:
    C55 source-locked g_s^2 constrained-fermion term
    with exact monomial and normal-ordering ledgers

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

C55 has already closed the action-level \(g_s^2\) operator and the complete monomial inventory. The remaining ambiguity is not whether the \(a a^\dagger\) contraction exists. It is how that required contraction is represented in the selected finite light-front basis.

C56 must distinguish four objects that must not be conflated:

```text
BARE SELF-INDUCED-INERTIA CONTRACTION

    The finite-regulator one-body operator generated directly by
    the exact commutator in the C55 normal-ordering rule.

NORMAL-ORDERING OR REFERENCE SUBTRACTION

    A subtraction applied only when an exact source- and
    regulator-qualified prescription defines it.

LOCAL COUNTERTERM DIRECTION

    An operator or generalized-metric direction whose coefficient
    will later be fixed by a renormalization condition.

PHYSICAL RENORMALIZED SELF-ENERGY

    A later result requiring a complete local renormalization
    condition and, generally, the other same-order local terms.
```

C56 may complete the first and third objects while leaving the second unapplied and the fourth unavailable.

The finite HO basis is a regulator, not a renormalization condition.

A regulator-dependent contraction is not to be:

```text
set to zero;
silently absorbed into the input quark mass;
subtracted by normal ordering a second time;
identified with a fitted C8/C9 mass counterterm;
replaced by a continuum integral;
or inferred from the C53 propagating vertex.
```

---

# 2. Exact purpose

C56 resolves only the one-pair normal-ordering contraction and its operator typing.

C56 must produce:

```text
the exact retained a a-dagger monomial and commutator contraction;

the normal-ordering reference state and commutator convention;

a source-derived finite-HO contraction mode set at every physical
resolution;

an exact shell-, longitudinal-mode-, helicity-, and color-resolved
bare contraction sum;

the finite-cell color-stripped plane-wave self-induced-inertia kernel;

the exact inverse-partial-plus momentum routing and zero-mode status;

the P^- to M^2 conversion for the one-body contraction;

physical one-quark contraction primitive matrices;

the source-supported spectator lift or independently projected
qg-sector contraction primitive;

a mutually exclusive bare/subtraction/counterterm plan;

a typed local counterterm/operator-direction decomposition with
visible residual;

an independent matrix-free contraction action;

regulator fingerprints and physical-resolution comparison diagnostics;

a read-only C57/IFERM2 import contract.
```

The contraction remains coupling factored:

\[
\Sigma_{\mathrm{SII}}
=
g_s^2\,\widehat\Sigma_{\mathrm{SII}}^{(M^2)}.
\]

Do not choose or fit \(g_s\), \(\alpha_s\), a mass counterterm coefficient, a wave-function counterterm coefficient, or a subtraction constant.

C56 must not construct:

```text
the complete direct qg instantaneous-fermion contact matrix;

the complete instantaneous-fermion operator;

the instantaneous color-current/gluon operator;

free q or qg matrices;

the complete local polynomial action;

a projected action/current identity;

the JMY Wilson or bilocal TMD operators;

a one-loop matching coefficient.
```

The strongest allowed status is:

```text
C56_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

When that gate passes, the exact next package is:

> **C57/IFERM2 — assemble the complete instantaneous-fermion operator from the C55 direct-contact contract and the read-only C56 self-induced-inertia contraction**

---

# 3. Scientific scope

The retained normal-ordering object is generated by the exact C55 one-pair contraction.

Its physical action must be audited on:

\[
\mathcal H_q
\oplus
\mathcal H_{qg}^{(3,\mathrm{CM}=0)}.
\]

The contraction is a one-body quark operator before any spectator lift. It may induce:

```text
a q -> q one-body block;

a spectator-lifted qg -> qg block;

a local counterterm direction;

a generalized-metric direction;

a regulator-boundary direction;

or a combination of these.
```

Do not assume it is:

```text
diagonal in the HO basis;

proportional to the identity;

proportional to the free mass direction;

identical in the q and qg sectors;

universal across resolutions;

or removable by one scalar counterterm.
```

These properties must be tested.

The already proved exact zeros remain:

```text
q -> qg = 0;
qg -> q = 0
```

for the instantaneous-fermion operator by gluon-number parity. C56 must preserve that proof and must not reopen it without a source-level contradiction.

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
docs/next_level/c45_numerical_object_inventory.json

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
docs/next_level/c53_basis_order_manifest.json
docs/next_level/c53_numerical_object_inventory.json

docs/next_level/c54_implementation_report.md
docs/next_level/c54_local_term_crosswalk.json
docs/next_level/c54_readiness_report.json

docs/next_level/c55_implementation_report.md
docs/next_level/c55_derivation_authority_manifest.json
docs/next_level/c55_source_sufficiency_matrix.json
docs/next_level/c55_fermion_constraint_rederivation.json
docs/next_level/c55_g2_operator_extraction.json
docs/next_level/c55_instantaneous_fermion_operator_contract.json
docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
docs/next_level/c55_physical_block_classification.json
docs/next_level/c55_contact_propagating_count_once.json
docs/next_level/c55_missing_calculation_specification.md
docs/next_level/c55_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c56_derivation_authority_manifest.json
docs/next_level/c56_input_fidelity_audit.json
```

---

# 5. Primary-source hierarchy

Reuse the C55 source locks:

```text
Srivastava--Brodsky:
    exact constrained-fermion and instantaneous g_s^2 operator authority;

Brodsky--Pauli--Pinsky:
    exact normal-ordering and self-induced-inertia retention authority.
```

The following may be acquired and hash locked only as renormalization-method comparisons when not already present:

```text
arXiv:0801.4507
    Fock-sector-dependent renormalization methodology;

arXiv:1612.09331
    sector-dependent self-energy/mass consequences of Fock truncation
    in a scalar light-front model;

arXiv:1402.4195
    BLFQ finite-basis mass-renormalization methodology in QED;

hep-th/9708054
    normal-ordering and second-order Hamiltonian-renormalization
    methodology.
```

Classify all such additions as:

```text
RENORMALIZATION_METHOD_COMPARISON_ONLY
```

unless an exact equation is demonstrably operator-, gauge-, regulator-, and convention-identical to C56.

These comparison sources may motivate diagnostics. They may not determine:

```text
the C56 contraction mode set;

the C56 subtraction constant;

the C56 QCD color tensor;

the C56 finite-HO matrix;

or a physical counterterm coefficient.
```

Create:

```text
docs/next_level/c56_primary_source_manifest.json
docs/next_level/c56_source_role_matrix.json
docs/next_level/c56_source_sufficiency_matrix.json
```

---

# 6. Freeze construction and holdouts

Before evaluating the contraction, freeze:

```text
the exact C55 a a-dagger monomial ID;

the exact commutator convention;

the normal-ordering reference state;

the C43/C45 field normalization;

the inverse-partial-plus routing;

the finite longitudinal cell;

the C45 one-gluon mode ordering;

the C47 q and qg physical basis orders;

the C47 TM/CM projectors;

the C53 triplet phase and color convention;

the M^2 conversion convention;

the symbolic L policy.
```

Freeze holdouts before construction:

```text
one contraction contribution from every gluon helicity;

one contribution from every adjoint color class or an exact
color-summed holdout;

smallest and largest retained gluon longitudinal mode;

lowest and highest included transverse HO shell;

one exact Q0-excluded candidate;

one nonzero inverse-derivative denominator nearest zero;

both quark helicities;

one off-diagonal transverse-HO matrix element candidate;

one q-sector matrix element;

one qg-sector spectator-lift matrix element;

one mass-direction comparison;

one residual-operator comparison;

one GeV/MeV holdout;

one symbolic-L holdout;

one adjacent-resolution comparison holdout.
```

No failed holdout may be moved into construction after inspection.

Create:

```text
docs/next_level/c56_calculation_plan.json
docs/next_level/c56_holdout_plan.json
```

---

# 7. Identify the exact contraction

Read the C55 monomial ledger and identify the unique retained one-pair ordering:

```text
a_\nu a^\dagger_{\nu'}
```

or the exact source-equivalent ordering.

Apply:

\[
a_\nu a^\dagger_{\nu'}
=
a^\dagger_{\nu'} a_\nu
+
[a_\nu,a^\dagger_{\nu'}].
\]

The commutator term must be derived from the exact finite-cell field normalization.

Create one immutable record:

```text
SelfInducedInertiaContraction
```

containing:

```text
C55 monomial ancestry;

field ordering;

commutator;

summed contracted indices;

fermion bilinear;

inverse-derivative placement;

color ordering;

polarization ordering;

coupling power;

normal-ordering reference;

zero-mode domain;

mass dimension.
```

Do not identify the contraction with the direct normal-ordered qg contact.

Do not identify it with the propagating C53 second-order self-energy.

Create:

```text
docs/next_level/c56_contraction_identity.json
docs/next_level/c56_normal_ordering_reduction.json
```

---

# 8. Normal-ordering reference state

Specify exactly with respect to which state the fields are normal ordered.

The contract must distinguish:

```text
the perturbative light-front vacuum;

the B=0 soft vacuum root;

the open-color one-quark external module;

the physical qg basis;

the historical C11 proton.
```

The self-induced-inertia contraction must use the source-defined normal-ordering vacuum. It must not use a hadron expectation value or ART25 ensemble average.

Record:

```text
vacuum identity;

annihilation conditions;

zero-mode exclusion/control;

boundary conditions;

commutator normalization;

whether constrained zero modes are part of the vacuum algebra.
```

Create:

```text
docs/next_level/c56_normal_ordering_reference.json
```

---

# 9. Finite-HO contraction-regulator plans

Compile mutually exclusive plans before summing a mode.

## 9.1 `IFNORM-PROJECTED-FIELD-MODE-REGULATOR`

Normal order the already regulated C45 field expansion. Sum over the complete retained one-gluon field-mode collection at each resolution, then project the resulting one-body operator into the C47 physical spaces.

## 9.2 `IFNORM-EXTERNAL-QG-EMBEDDABLE-REGULATOR`

Sum only contracted gluon modes that can occur in an external retained qg basis state.

This plan is permitted only if the source/project projection contract proves that the normal-order contraction is regulated by the external many-body truncation rather than by the field-mode cutoff.

## 9.3 `IFNORM-SOURCE-DEFINED-REFERENCE-SUBTRACTION`

Use a source-defined finite-basis reference subtraction before projection.

The exact reference, mode pairing, and counterterm relation must be source qualified.

## 9.4 `IFNORM-REGULATOR-MATCHED-CONVERSION`

Convert a contraction from another regulator only through an operator-identical finite conversion with declared order and remainder.

## 9.5 `IFNORM-UNAVAILABLE`

No unique regulator ownership can be established.

Select exactly one primary regulator plan.

Do not choose the plan that gives the smallest matrix or smoothest trajectory.

Create:

```text
docs/next_level/c56_contraction_regulator_plan.json
docs/next_level/c56_regulator_plan_decision.json
```

---

# 10. Materialize the contracted gluon mode set

For the selected plan, generate the exact contracted mode collection at:

```text
K = 9/2;
K = 11/2;
K = 13/2.
```

Each mode record must retain:

```text
longitudinal mode k_g;

momentum fraction where applicable;

transverse HO n and m;

gluon helicity;

adjoint color;

zero-mode status;

boundary phase;

normalization;

resolution;

shell label;

mode hash.
```

Report:

```text
total mode count;

counts by longitudinal mode;

counts by transverse shell;

counts by helicity and color;

excluded zero modes;

modes rejected by the selected regulator rule.
```

The mode collection must be generated independently of the external basis pair being evaluated unless the selected plan proves otherwise.

Create:

```text
docs/next_level/c56_contracted_gluon_mode_manifest.json
docs/next_level/c56_contracted_mode_validation.json
```

---

# 11. Exact shell and mode contribution ledger

For every contracted mode \(\nu\), define its contribution to the color-stripped one-body kernel:

\[
\Sigma_{\alpha'\alpha}^{(\nu)}
\]

before summing.

The complete bare contraction is schematically:

\[
\widehat\Sigma_{\alpha'\alpha}^{(-)}
=
\sum_{\nu\in\mathcal G_R}
\Sigma_{\alpha'\alpha}^{(\nu)}.
\]

This formula is schematic. Use the exact C55 operator ordering and denominator.

Retain:

```text
mode identity;

fermion basis identities;

inverse-derivative denominator;

spin/polarization tensor;

transverse overlap;

color factor before and after summation;

finite-cell normalization;

P^- contribution;

M^2 contribution;

exact-zero reason.
```

Construct partial sums by:

```text
longitudinal mode;

transverse shell;

helicity;

color;

combined shell.
```

Create:

```text
docs/next_level/c56_mode_contribution_ledger.json
docs/next_level/c56_shell_partial_sum_report.json
```

---

# 12. Inverse-\(\partial^+\) routing and zero modes

Use the exact routing proved or specified by C55.

For the contracted pair, determine the mode on which:

\[
\frac{1}{i\partial^+}
\]

acts after the commutator is applied.

Do not assume that the denominator is simply the external quark momentum or contracted gluon momentum.

Record:

```text
pre-contraction product mode;

post-contraction fermion mode;

denominator mode;

sign;

PV prescription;

P0/Q0 status;

boundary partner;

resolution.
```

Every zero denominator must be classified as:

```text
EXCLUDED_BY_Q0_WITH_SOURCE_PROOF;

CANCELS_WITH_DECLARED_BOUNDARY_TERM;

RETAINED_ZERO_MODE_CONTROL;

ABSENT_BLOCKING.
```

Never use epsilon, clipping, a pseudoinverse, or deleted entries.

Create:

```text
docs/next_level/c56_contraction_inverse_derivative_routing.json
docs/next_level/c56_contraction_zero_mode_ledger.json
docs/next_level/c56_inverse_derivative_validation.json
```

---

# 13. Spin, polarization, and color sums

Derive the contraction sums without assuming their final form.

## 13.1 Polarization

Sum over the exact retained physical transverse-gluon polarization basis.

Verify the source-supported completeness relation at the declared light-front-gauge scope.

Any omitted constrained or boundary polarization contribution must remain visible.

## 13.2 Color

Retain the ordered color product inherited from the C55 monomial.

Only after exact contraction over the adjoint label test whether:

\[
\sum_a T^aT^a=C_F I_3
\]

applies in the stored convention.

Do not hard-code \(C_F\) before the ordered color calculation.

## 13.3 Spin

Evaluate the good-component fermion tensor and an independent four-component route.

Do not assume helicity diagonality.

Required checks:

```text
polarization-basis completeness;

ordered-color sum;

C_F residual where applicable;

quark-helicity selection;

phase convention;

good-component/four-component equality;

Abelian limit.
```

Create:

```text
docs/next_level/c56_spin_polarization_contraction.json
docs/next_level/c56_color_contraction.json
docs/next_level/c56_spin_color_validation.json
```

---

# 14. Finite-cell normalization

Derive every factor in the one-pair contraction from:

```text
the two gauge-field mode expansions;

the commutator;

the quark field normalization;

the x-minus and transverse integrations;

the finite-cell state normalization;

the contracted-mode sum.
```

Keep \(L\) symbolic.

Determine whether the complete bare contraction:

```text
is L independent;

contains one block-common factored L power;

or retains a source-defined finite-volume dependence.
```

An entry-dependent \(L\) signature is blocking.

Create:

```text
docs/next_level/c56_finite_volume_contraction_normalization.json
docs/next_level/c56_normalization_validation.json
```

---

# 15. \(P^-\!\to M^2\) conversion

Derive the one-body contraction in both forms:

\[
\widehat\Sigma^{(-)}
\]

and:

\[
\widehat\Sigma^{(M^2)}.
\]

Use:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Prove separately for the q and qg sector representations:

```text
same total P^+ on bra and ket;

the relevant total transverse frame;

whether P_perp^2 has a contraction-related contribution;

state-normalization compatibility;

the factor of two.
```

Every completed \(M^2\) primitive must have uniform mass-squared units.

Create:

```text
docs/next_level/c56_contraction_pminus_to_m2_contract.json
docs/next_level/c56_contraction_pminus_to_m2_validation.json
```

---

# 16. Physical q-sector projection

Project the color-stripped one-body contraction into the complete physical one-quark basis.

Construct:

```text
the primitive sparse matrix;

the executable symbolic coefficient;

an independent direct matrix-free action;

selected direct integral holdouts.
```

Do not assume the matrix is diagonal.

Report:

```text
shape;

nnz;

Hermiticity;

helicity blocks;

transverse-HO off-diagonal support;

longitudinal-mode dependence;

eigenvalue or spectral-bound diagnostics;

symbolic signature.
```

Create:

```text
docs/next_level/c56_q_sector_contraction.json
docs/next_level/c56_q_sector_validation.json
```

---

# 17. qg-sector spectator lift and independent projection

Compile two routes.

## 17.1 Spectator-lift route

Lift the one-body quark operator into the full qg product basis with the external gluon as spectator, then apply:

```text
the C47 TM/Jacobi map;

CM-ground projection;

triplet color reduction.
```

## 17.2 Direct qg projection route

Evaluate the contraction directly between physical qg states from the field operator and basis expansions.

Require equality if the source/operator algebra predicts a pure spectator lift.

If additional external-gluon ordering or truncation terms survive, retain them as separately sourced contributions.

Do not force equality by definition.

Required checks:

```text
spectator identity;

CM-ground preservation;

triplet preservation;

Jz and K conservation;

full-product versus triplet route;

spectator-lift/direct residual;

sector-dependent remainder.
```

Create:

```text
docs/next_level/c56_qg_sector_contraction.json
docs/next_level/c56_sector_lift_validation.json
```

---

# 18. Bare, subtraction, and counterterm plan

Compile mutually exclusive renormalization plans after the bare matrices exist.

## 18.1 `IFNORM-BARE-RETAINED-SEPARATE-CT`

Retain the complete finite-regulator contraction in the bare/direct \(g_s^2\) operator and define separate local counterterm directions with unsolved coefficients.

No reference subtraction is applied at C56.

## 18.2 `IFNORM-SOURCE-REFERENCE-SUBTRACTED`

Apply an exact source-defined reference subtraction, while preserving both the unsubtracted and subtracted operators and their counterterm relation.

## 18.3 `IFNORM-REGULATOR-CONVERTED`

Apply an exact finite conversion from a regulator-identical calculation, with order, inverse, round trip, and remainder.

## 18.4 `IFNORM-UNAVAILABLE`

No scientifically complete separation is supported.

Select exactly one plan.

The preferred minimal bare-substrate route is permitted only when the source Hamiltonian and later counterterm architecture clearly separate the bare contraction from the renormalization condition.

Create:

```text
docs/next_level/c56_bare_subtraction_counterterm_plan.json
docs/next_level/c56_renormalization_plan_decision.json
```

---

# 19. Counterterm and operator typing

Construct a source-owned candidate direction basis.

Audit at least:

```text
quark mass-squared direction;

quark field/residue or generalized-metric direction;

sector-specific mass direction;

local basis-boundary direction;

zero-mode direction;

self-induced-inertia operator direction.
```

For each sector and resolution, test whether the bare contraction lies in the span of the pre-existing directions.

Use the correct basis metric and report:

```text
direction Gram matrix;

rank;

condition number;

projection coefficients as diagnostics only;

parallel component;

orthogonal residual;

operator-norm residual;

comparison-map behavior.
```

Do not interpret diagnostic projection coefficients as physical counterterm coefficients.

Allowed typing outcomes:

```text
PURE_MASS_DIRECTION;

MASS_PLUS_METRIC_DIRECTION;

SECTOR_DEPENDENT_EXISTING_DIRECTIONS;

NEW_LOCAL_SELF_INDUCED_INERTIA_DIRECTION_REQUIRED;

UNRESOLVED_BLOCKING.
```

If a new direction is required, define it from the source-derived contraction itself and keep its coefficient unsolved.

Do not force a nonzero residual into the mass direction.

Create:

```text
docs/next_level/c56_counterterm_direction_basis.json
docs/next_level/c56_counterterm_typing_report.json
docs/next_level/c56_sector_dependence_report.json
```

---

# 20. Fock-sector and spectator universality

Test rather than assume whether the same counterterm direction and eventual coefficient can act in the q and qg sectors.

Separate:

```text
operator universality;

matrix-representation differences caused by the spectator and CM projection;

Fock-truncation-induced sector dependence;

basis-boundary dependence;

physical renormalization-condition dependence.
```

The following are distinct claims:

```text
the same source one-body operator lifts to both sectors;

the finite matrices are related by spectator lift;

one scalar counterterm coefficient renormalizes both sectors;

the renormalized physical self-energy is sector independent.
```

C56 may establish the first two without establishing the last two.

Create:

```text
docs/next_level/c56_fock_sector_universality_contract.json
docs/next_level/c56_fock_sector_universality_validation.json
```

---

# 21. Count-once relation to other local terms

Extend the C55 count-once ledger.

Keep distinct:

```text
direct normal-ordered qg contact;

self-induced-inertia contraction;

C53 propagating second-order self-energy;

free mass direction;

mass counterterm direction;

field/residue direction;

boundary and zero-mode completion;

instantaneous color-current self-energy;

future loop/matching self-energy.
```

The contraction may share a renormalization condition with another term without being the same operator contribution.

No object may be added twice under two names.

Create:

```text
docs/next_level/c56_local_self_energy_count_once.json
```

---

# 22. Arbitrary-mode contraction evaluator

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

basis identities;

contracted-mode contribution count;

shell partial sums;

inverse-derivative routing;

zero-mode status;

spin/polarization sum;

color sum;

P^- value;

M^2 value;

units;

symbolic signature;

counterterm typing;

source ancestry;

exact-zero reason.
```

The evaluator must not consume:

```text
C40 instantaneous values;

C47 raw canonical tuple values;

C53 physical vertex values;

a fitted mass shift;

a continuum self-energy number.
```

Create:

```text
docs/next_level/c56_contraction_evaluator_api.json
docs/next_level/c56_contraction_evaluator_validation.json
```

---

# 23. Exhaustive domain and matrix assembly

Enumerate all q/q and qg/qg basis pairs allowed by the contraction.

Every pair receives one status:

```text
PRESELECTION_FORBIDDEN_EXACT;

EVALUATED_EXACT_ZERO;

EVALUATED_NONZERO;

EVALUATOR_UNAVAILABLE_BLOCKING;

DUPLICATE_BLOCKING.
```

Assemble the q and qg contraction primitive matrices only.

Do not assemble the direct qg instantaneous contact.

Report:

```text
Cartesian pair count;

preselection count;

evaluator calls;

exact zeros;

nonzeros;

duplicates;

missing entries;

blocking entries;

matrix nnz.
```

A positive gate requires:

```text
duplicate = 0;

missing = 0;

blocking = 0.
```

Create:

```text
docs/next_level/c56_physical_domain_ledger.json
docs/next_level/c56_contraction_matrices.json
docs/next_level/c56_count_once_report.json
```

---

# 24. Independent matrix-free action

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
regenerate or iterate over contracted gluon modes;

evaluate the mode-resolved kernel;

accumulate q and qg sector actions separately;

retain shell and counterterm-direction diagnostics.
```

It must not:

```text
multiply by stored C56 sparse matrices;

load a matrix-entry table as numerical authority;

construct the contraction from C53 V-dagger D-inverse V;

consume historical coefficients.
```

Compare sparse and matrix-free actions on:

```text
basis vectors;

deterministic complex superpositions;

random normalized complex vectors;

all physical resolutions;

multiple diagnostic symbolic substitutions.
```

Create:

```text
docs/next_level/c56_matrix_free_report.json
```

---

# 25. Hermiticity and positivity diagnostics

Verify Hermiticity from the source contraction.

Do not repair the matrix by post-hoc averaging.

Report:

```text
Hermiticity residual;

ordering-reversal residual;

denominator-conjugation residual;

color-order residual;

basis-phase covariance.
```

The contraction need not be positive semidefinite unless the source structure proves it.

Report its Hermitian spectrum or rigorous bounds without clipping negative eigenvalues.

Create:

```text
docs/next_level/c56_hermiticity_spectrum_report.json
```

---

# 26. Regulator fingerprints

The three physical points change \(K\), \(N_{\max}\), and \(b_{\rm HO}\) together. They are not a factorized continuum trajectory.

Report the bare contraction through:

```text
shell partial sums;

longitudinal-mode partial sums;

UV-shell sensitivity;

small-k_g sensitivity;

bHO scaling;

symbolic-L behavior;

q versus qg sector comparison;

direction-decomposition residuals.
```

Do not fit away the regulator dependence.

Do not claim convergence from three correlated resolution points.

A diagnostic factorized scan may be added only when it uses the same source-qualified mode generator and is labeled:

```text
NONPHYSICAL_REGULATOR_DIAGNOSTIC
```

It must not define a subtraction or physical coefficient.

Create:

```text
docs/next_level/c56_regulator_fingerprint_report.json
docs/next_level/c56_shell_asymptotic_diagnostics.json
```

---

# 27. Physical-resolution comparison

Use the C47 comparison maps to evaluate:

\[
R\,\widehat\Sigma_{\mathrm{SII},r'}\,P
\quad\text{versus}\quad
\widehat\Sigma_{\mathrm{SII},r}.
\]

Execute separately for:

```text
q-sector contraction;

qg-sector contraction;

mass-direction component;

metric/direction component;

orthogonal self-induced-inertia residual.
```

Separate:

```text
nonnested longitudinal remainder;

transverse truncation remainder;

CM-projection remainder;

triplet-basis remainder;

contracted-mode-set remainder;

zero-mode/boundary remainder;

symbolic normalization remainder;

numerical error.
```

Do not tune a subtraction or counterterm coefficient to reduce the comparison residual.

Create:

```text
docs/next_level/c56_operator_comparison_report.json
docs/next_level/c56_comparison_remainder_ledger.json
```

---

# 28. Independent checks

## 28.1 Direct commutator versus explicit vacuum contraction

Evaluate frozen holdouts by both:

```text
the normal-order commutator;

an explicit vacuum matrix element of the two gluon fields.
```

## 28.2 Full mode sum versus shell sum

Require exact recomposition.

## 28.3 Abelian limit

Remove QCD color while preserving the same finite-cell and normal-ordering conventions.

Use QED/BLFQ sources only as method checks.

## 28.4 Continuum asymptotic comparison

Where a primary source provides the leading regulator behavior, compare only the asymptotic structure after mapping conventions.

Do not import a continuum finite part as a C56 subtraction.

## 28.5 Spectator-lift equality

Compare direct and lifted qg-sector routes.

Create:

```text
docs/next_level/c56_vacuum_commutator_crosscheck.json
docs/next_level/c56_shell_recomposition_report.json
docs/next_level/c56_abelian_crosscheck.json
docs/next_level/c56_asymptotic_method_comparison.json
docs/next_level/c56_spectator_lift_crosscheck.json
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

normal-ordering reference controls;

wrong SU(3) controls;

omitted/duplicated contraction controls.
```

Require:

```text
every completed M^2 primitive scales as mass squared;

all symbolic signatures are sector consistent;

dimensionless residuals are invariant;

wrong conventions fail explicitly.
```

Create:

```text
docs/next_level/c56_unit_regulator_convention_report.json
```

---

# 30. Isolation and poisoning controls

Prove that C56 is unchanged when:

```text
all C40 instantaneous matrices are poisoned;

all C47 raw canonical tuples and component metadata are poisoned;

all C50 combined canonical values are poisoned;

all C53 physical canonical vertex values are poisoned;

historical C8/C9 mass and instantaneous coefficients are poisoned;

ART25 data and members are inaccessible.
```

The build must fail when:

```text
the C55 contraction monomial changes;

the normal-ordering reference changes;

the C45 contracted-mode collection changes;

the inverse-derivative prescription changes;

the zero-mode projector changes;

the C47 physical basis hash changes;

the C53 triplet-isometry hash changes;

the selected regulator plan changes without supersession.
```

Create:

```text
docs/next_level/c56_isolation_report.json
```

---

# 31. C57/IFERM2 import contract

Define the read-only contract by which C57 will consume:

```text
the q and qg self-induced-inertia primitive matrices;

the executable symbolic coefficient;

the g_s^2 order label;

the regulator-plan identity;

the bare/subtraction/counterterm decision;

the counterterm/operator-direction typing;

the normal-order contraction ancestry;

the zero-mode and boundary statuses;

the independent matrix-free action;

the count-once and comparison ledgers.
```

C57 must verify hashes before assembling the direct qg contact.

C57 may not rederive, rescale, subtract, or fit C56.

Create:

```text
docs/next_level/c56_c57_import_contract.json
```

---

# 32. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
contracted gluon mode collection;

mode contribution ledger;

shell partial sums;

q-sector primitive matrix;

qg-sector primitive matrix;

symbolic coefficient;

counterterm-direction records;

matrix-free reconstruction metadata;

domain and count-once ledgers;

holdout and comparison records.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c56_ifnorm/
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

regulator-plan ID;

basis-order hash;

expression hash;

array hash;

generator command.
```

Create:

```text
docs/next_level/c56_numerical_object_inventory.json
```

All JSON, expressions, and arrays must regenerate byte-for-byte.

---

# 33. End-to-end source-to-contraction test

Implement an end-to-end test that begins from the C43/C45/C47/C55 contracts—not from prebuilt C56 matrices.

It must:

```text
load the exact a a-dagger monomial;

derive the commutator contraction;

select the source-supported regulator plan;

generate the contracted gluon mode collection;

derive every mode contribution;

apply inverse-derivative and zero-mode rules;

sum spin, polarization, and color;

derive finite-cell normalization;

convert P^- to M^2;

project into q and qg physical sectors;

classify counterterm/operator directions;

assemble primitive matrices;

apply the independent matrix-free action;

run shell, holdout, unit, poisoning, and comparison tests;

reproduce every hash.
```

It must fail when:

```text
the contraction is dropped;

the contraction is subtracted without an exact plan;

the contraction is silently absorbed into the input mass;

the contracted mode set is restricted to external qg states without
source authority;

a zero denominator is clipped;

a continuum finite part is imported;

a C53 propagating self-energy is substituted;

a mass counterterm coefficient is fitted;

a q/qg sector difference is hidden;

a post-hoc Hermitian average is applied;

a runtime hash changes.
```

---

# 34. Focused mutation tests

Create at least **224 focused live mutations** of actual contractions, modes, denominators, direction records, or matrices.

Include mutations of:

```text
a a-dagger monomial identity;

commutator sign;

normal-ordering vacuum;

contracted mode inclusion;

longitudinal mode;

transverse shell;

gluon helicity;

adjoint color;

polarization completeness;

color ordering;

inverse-derivative denominator;

PV prescription;

zero-mode projector;

finite-cell normalization;

L power;

P^+ power;

P^- to M^2 factor;

q-sector primitive;

qg spectator lift;

CM projector;

triplet isometry;

counterterm direction;

sector-universality status;

matrix entry;

matrix-free accumulation;

shell recomposition;

comparison map;

runtime hash.
```

Every mutation must fail a concrete source, normal-ordering, regulator, zero-mode, color, Hermiticity, typing, count-once, matrix-free, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 35. Readiness gate

Issue:

```text
C56_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

only when:

```text
the full C55 baseline reproduces;

the exact one-pair contraction is identified;

the normal-ordering reference is explicit;

one source-supported finite-HO regulator plan is selected;

the contracted gluon mode set is complete;

every mode contribution is source derived;

shell and full-sum recomposition closes;

inverse-derivative routing is explicit;

all zero denominators have typed statuses;

spin, polarization, and color sums close;

finite-cell normalization is complete;

P^- to M^2 conversion closes;

q-sector contraction matrices exist;

qg-sector direct and spectator-lift routes close or retain a typed
source-derived remainder;

one bare/subtraction/counterterm plan is selected;

the bare contraction is not silently removed;

counterterm/operator typing is complete with visible residual;

Fock-sector universality claims are no stronger than the calculation;

count-once separation from contact, propagation, and future loop terms closes;

the arbitrary-mode evaluator covers every admitted pair;

duplicate, missing, and blocking domain counts are zero;

sparse and independent matrix-free contraction actions agree;

Hermiticity follows without post-hoc repair;

regulator fingerprints and physical-resolution comparisons execute;

independent commutator, vacuum, shell, Abelian, and lift checks pass;

unit, regulator, phase, zero-mode, and poisoning tests pass;

the C57 import contract is complete;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-contraction test passes.
```

Do not issue:

```text
C56_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C56_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C56_PHYSICAL_MASS_RENORMALIZATION_SOLVED;

C56_PROJECTED_ACTION_IDENTITY_READY;

C56_JMY_WILSON_MATRIX_VALIDATED;

C56_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 36. Exact no-go branches

## A. Normal-ordering source or contraction identity remains incomplete

```text
C56_IFNORM_SOURCE_RULE_INCOMPLETE
```

Next:

> **C57/IFRULE — exact BPP/SB commutator, ordering, and contraction identity completion**

## B. Finite-HO regulator ownership remains incomplete

```text
C56_IFNORM_FINITE_HO_REGULATOR_INCOMPLETE
```

Next:

> **C57/IFREG — contracted field-mode collection, truncation projector, and shell regulator completion**

## C. Inverse derivative or zero-mode treatment remains incomplete

```text
C56_IFNORM_ZERO_MODE_ROUTING_INCOMPLETE
```

Next:

> **C57/IFZERO2 — contraction denominator, PV, boundary, and zero-mode completion**

## D. Bare/subtraction separation remains incomplete

```text
C56_IFNORM_SUBTRACTION_PLAN_INCOMPLETE
```

Next:

> **C57/IFSUB — bare contraction, reference subtraction, and regulator-conversion decision**

## E. Counterterm/operator typing remains incomplete

```text
C56_IFNORM_COUNTERTERM_TYPING_INCOMPLETE
```

Next:

> **C57/IFCT — mass, metric, sector, boundary, and self-induced-inertia direction completion**

## F. qg-sector lift remains incomplete

```text
C56_IFNORM_SECTOR_LIFT_INCOMPLETE
```

Next:

> **C57/IFLIFT — spectator lift, CM/triplet projection, and sector-dependence completion**

## G. Sparse and matrix-free actions disagree

```text
C56_IFNORM_MATRIX_ACTION_CLOSURE_FAILED
```

Next:

> **C57/IFACT2 — independent contraction sparse/matrix-free action completion**

## H. Normal-ordering contraction closes

```text
C56_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

Next:

> **C57/IFERM2 — assemble the complete instantaneous-fermion operator**

---

# 37. Required deliverables

Create at least:

```text
docs/next_level/c56_implementation_report.md
docs/next_level/c56_api.md
docs/next_level/c56_derivation_authority_manifest.json
docs/next_level/c56_input_fidelity_audit.json

docs/next_level/c56_primary_source_manifest.json
docs/next_level/c56_source_role_matrix.json
docs/next_level/c56_source_sufficiency_matrix.json
docs/next_level/c56_calculation_plan.json
docs/next_level/c56_holdout_plan.json

docs/next_level/c56_contraction_identity.json
docs/next_level/c56_normal_ordering_reduction.json
docs/next_level/c56_normal_ordering_reference.json

docs/next_level/c56_contraction_regulator_plan.json
docs/next_level/c56_regulator_plan_decision.json
docs/next_level/c56_contracted_gluon_mode_manifest.json
docs/next_level/c56_contracted_mode_validation.json

docs/next_level/c56_mode_contribution_ledger.json
docs/next_level/c56_shell_partial_sum_report.json

docs/next_level/c56_contraction_inverse_derivative_routing.json
docs/next_level/c56_contraction_zero_mode_ledger.json
docs/next_level/c56_inverse_derivative_validation.json

docs/next_level/c56_spin_polarization_contraction.json
docs/next_level/c56_color_contraction.json
docs/next_level/c56_spin_color_validation.json

docs/next_level/c56_finite_volume_contraction_normalization.json
docs/next_level/c56_normalization_validation.json
docs/next_level/c56_contraction_pminus_to_m2_contract.json
docs/next_level/c56_contraction_pminus_to_m2_validation.json

docs/next_level/c56_q_sector_contraction.json
docs/next_level/c56_q_sector_validation.json
docs/next_level/c56_qg_sector_contraction.json
docs/next_level/c56_sector_lift_validation.json

docs/next_level/c56_bare_subtraction_counterterm_plan.json
docs/next_level/c56_renormalization_plan_decision.json
docs/next_level/c56_counterterm_direction_basis.json
docs/next_level/c56_counterterm_typing_report.json
docs/next_level/c56_sector_dependence_report.json
docs/next_level/c56_fock_sector_universality_contract.json
docs/next_level/c56_fock_sector_universality_validation.json
docs/next_level/c56_local_self_energy_count_once.json

docs/next_level/c56_contraction_evaluator_api.json
docs/next_level/c56_contraction_evaluator_validation.json
docs/next_level/c56_physical_domain_ledger.json
docs/next_level/c56_contraction_matrices.json
docs/next_level/c56_count_once_report.json
docs/next_level/c56_matrix_free_report.json
docs/next_level/c56_hermiticity_spectrum_report.json

docs/next_level/c56_regulator_fingerprint_report.json
docs/next_level/c56_shell_asymptotic_diagnostics.json
docs/next_level/c56_operator_comparison_report.json
docs/next_level/c56_comparison_remainder_ledger.json

docs/next_level/c56_vacuum_commutator_crosscheck.json
docs/next_level/c56_shell_recomposition_report.json
docs/next_level/c56_abelian_crosscheck.json
docs/next_level/c56_asymptotic_method_comparison.json
docs/next_level/c56_spectator_lift_crosscheck.json

docs/next_level/c56_unit_regulator_convention_report.json
docs/next_level/c56_isolation_report.json
docs/next_level/c56_c57_import_contract.json

docs/next_level/c56_numerical_object_inventory.json
docs/next_level/c56_readiness_report.json
docs/next_level/c56_source_sufficiency_decision.json
docs/next_level/c56_no_go_decision_tree.json
docs/next_level/c56_missing_calculation_specification.md
docs/next_level/c56_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/ifnorm/
```

or the repository-equivalent package.

Add focused tests for:

```text
contraction identity;
normal-ordering reference;
finite-HO regulator plan;
contracted mode collection;
shell recomposition;
inverse derivative and zero modes;
spin/polarization/color sums;
finite-cell normalization;
P^- to M^2 conversion;
q-sector projection;
qg spectator lift;
bare/subtraction/counterterm separation;
counterterm typing;
sector universality;
count once;
arbitrary evaluator;
sparse/matrix-free action;
Hermiticity and spectrum;
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

C56 is complete only when:

1. The full C55 baseline reproduces.
2. The C55 no-go remains explicit.
3. The C53 physical canonical vertex remains immutable.
4. The C43 action, C45 modes, and C47 physical basis remain unchanged.
5. C40 remains method-oracle only.
6. Historical C47 tuple values and metadata remain diagnostic-only.
7. No historical mass or instantaneous coefficient enters.
8. No physical \(g_s\), \(\alpha_s\), mass shift, or subtraction coefficient is chosen.
9. No arbitrary numerical \(L\) is introduced.
10. The exact \(a a^\dagger\) monomial is identified.
11. The commutator contraction is derived exactly.
12. The normal-ordering reference state is explicit.
13. The contraction remains distinct from the direct qg contact.
14. The contraction remains distinct from C53 propagation.
15. One finite-HO regulator plan is selected from source/project authority.
16. The contracted gluon mode collection is materialized.
17. The collection includes every required longitudinal, transverse, helicity, and color mode.
18. Exact zero modes remain separate controls.
19. Every mode contribution has complete ancestry.
20. Shell and full-sum recomposition closes.
21. Every inverse denominator follows exact operator routing.
22. No epsilon, clipping, pseudoinverse, or silent deletion is used.
23. Polarization completeness closes at the declared gauge scope.
24. Ordered color contraction closes.
25. Good-component and four-component spin routes agree.
26. Finite-cell normalization is complete.
27. Symbolic \(L\) dependence is common, factored, or canceled.
28. The \(P^-\!\to M^2\) map closes for q and qg representations.
29. Every completed primitive has mass-squared units.
30. The q-sector matrix exists at all resolutions.
31. The qg direct and spectator-lift routes close or retain a source-derived remainder.
32. CM and triplet identities are preserved.
33. One bare/subtraction/counterterm plan is selected.
34. The bare contraction is never silently removed.
35. No source-free reference subtraction is applied.
36. Counterterm/operator directions are source derived.
37. A nonzero residual is not forced into the mass direction.
38. Sector universality is not inferred from operator naming.
39. Direct, contraction, propagating, counterterm, boundary, zero-mode, and future loop terms are count-once distinct.
40. The arbitrary evaluator is independent of historical values.
41. Every admitted q/q and qg/qg pair is evaluated.
42. Duplicate, missing, and blocking counts are zero.
43. Sparse and independent matrix-free actions agree.
44. Hermiticity follows without post-hoc averaging.
45. Negative eigenvalues are not clipped.
46. Regulator fingerprints remain visible.
47. Three correlated physical resolutions are not mislabeled as a continuum extrapolation.
48. Physical-resolution comparisons retain all separated remainders.
49. Vacuum/commutator, shell, Abelian, asymptotic, and spectator-lift checks pass.
50. GeV/MeV, \(L\), \(P^+\), \(b_{\rm HO}\), mass, phase, PV, zero-mode, normal-ordering, and SU(3) controls pass.
51. Static and runtime poisoning controls pass.
52. The C57 import contract is complete.
53. Runtime bundles contain actual mode sums, expressions, matrices, and independent action metadata.
54. End-to-end reconstruction passes.
55. At least 224 focused live mutations are detected.
56. No complete direct instantaneous-fermion contact matrix is claimed.
57. No complete instantaneous-fermion operator status is issued.
58. No free or instantaneous-current matrix is claimed complete.
59. No complete local-HQCD status is issued.
60. No projected action/current identity is claimed complete.
61. No JMY Wilson or bilocal TMD matrix is created.
62. No soft subtraction or nonlocal counterterm system is created.
63. No physical counterterm coefficient is solved.
64. No one-loop coefficient or matching kernel is created.
65. No proton TMD or ART25 bridge is created.
66. No fit, inference, process, or production route is created.
67. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
68. `MSHT20_REP/` remains untouched and outside Git.
69. The working tree is clean except for the pre-existing untracked directory.
70. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken regulator ownership, normal-ordering retention, bare/subtraction separation, counterterm typing, sector dependence, or matrix-free independence to open the gate.

---

# 39. Final Codex response

Report:

- full starting and final commits;
- exact primary and method-comparison sources and role classifications;
- exact contraction monomial and commutator;
- normal-ordering reference state;
- selected finite-HO regulator plan and rejected alternatives;
- contracted mode counts by longitudinal mode, shell, helicity, and color;
- mode- and shell-resolved contribution ranges;
- inverse-derivative routing and zero-mode statuses;
- spin/polarization/color residuals;
- finite-cell normalization and symbolic-\(L\) behavior;
- \(P^-\!\to M^2\) conversion residuals;
- q-sector primitive shape, nnz, norm/spectrum, units, and symbolic signature;
- qg-sector primitive shape, nnz, spectator-lift/direct residual, units, and symbolic signature;
- selected bare/subtraction/counterterm plan;
- counterterm-direction basis, rank, condition number, typing, and orthogonal residual;
- q/qg sector-universality result;
- direct/contact/propagating/contraction/counterterm/boundary/zero-mode count-once decisions;
- physical-domain counts;
- sparse/matrix-free residuals;
- Hermiticity and spectrum diagnostics;
- regulator fingerprints and shell partial sums;
- physical-resolution comparison residuals and separated remainders;
- independent vacuum, shell, Abelian, asymptotic, and spectator-lift checks;
- unit, regulator, phase, normal-ordering, zero-mode, wrong-color, and poisoning controls;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no complete direct instantaneous contact, complete instantaneous-fermion operator, free/current/local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-counterterm, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an omitted contraction, an external-state-limited mode sum without authority, a continuum subtraction imported into the finite HO regulator, a fitted mass shift, a contraction hidden inside the input mass, or a sector-dependent residual forced into one universal scalar counterterm as a completed normal-ordering contract.
