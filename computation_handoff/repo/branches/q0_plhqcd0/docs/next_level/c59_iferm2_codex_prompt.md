# C59/IFERM2 Codex Work Package

## Title

**Complete source-derived instantaneous-fermion operator: normal-ordered \(qg\!\to qg\) contact, corresponding-propagating \(q\)-intermediate support, ordered color/spin kernels, immutable C58 self-induced-inertia import, block assembly, and independent action closure**

## Authoritative baseline

Start from the clean local C58/IFNORM2 completion commit:

```text
43bf2493ec020a130bbf4cb576a851adc5b5e0cf
```

Its immediate scientific parent is:

```text
d9d981459dff8d21d94ef13b0a671e8140b47caa
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor d9d981459dff8d21d94ef13b0a671e8140b47caa HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY

C58_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY
```

and the exact C58 scientific result:

```text
C57 immutable support reproduced:
    support positions:        312 / 510 / 756
    conditional mode unions:  1,216 / 2,320 / 3,936
    candidate envelopes:      2,304 / 4,400 / 7,488

bra-ket support:
    IFNORM2-ORDERED-JOINT-SUPPORT
    source rule Pi_bra delta Pi_ket
    no arbitrary support union or intersection
    no post-hoc Hermitianization

q-sector self-induced-inertia:
    source-derived bare g_s^2 M^2 primitives
    shape 6 x 6 at every physical resolution
    six nonzero diagonal entries
    admitted contracted-mode counts:
        4,216 / 8,330 / 14,484
    independent direct mode-ledger action

qg-sector self-induced-inertia:
    IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY
    corresponding qgg support absent
    no spectator lift
    no false zero full-QCD operator

renormalization plan:
    bare retention
    no reference subtraction
    no physical coupling
    no counterterm coefficient solved

not yet created:
    no direct normal-ordered qg contact
    no complete instantaneous-fermion operator
    no free or instantaneous-current matrix
    no complete local-HQCD polynomial
```

Verify every value, status, expression hash, support hash, basis order, runtime hash, and sector record from the committed C58 artifacts rather than relying on this prompt.

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

physical spaces:
    H_q
    plus
    H_qg^(3,CM=0)

physical q dimension:
    6 at every resolution, subject to manifest verification

physical qg dimensions:
    1,344 / 2,700 / 4,752,
    subject to exact manifest verification

canonical local vertex:
    C53 source-derived physical q <-> qg operator
    read-only
    numerical values and energy denominators are forbidden as
    construction inputs for the direct contact

instantaneous-fermion source:
    C55 exact g_s^2 constrained-fermion operator
    complete normal-ordering and monomial ledger
    q <-> qg exact zero by gluon-number parity

self-induced-inertia:
    C58 source-derived q-sector primitive
    qg highest-sector counterterm-only status
    read-only
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

C59 completes the instantaneous-fermion operator at the declared retained-space scope.

C55 separated the \(a a^\dagger\) monomial into:

```text
a direct normal-ordered a-dagger a contact;

and

the self-induced-inertia commutator contraction.
```

C58 has completed the contraction branch.

C59 must now:

```text
derive and execute every source-required direct normal-ordered
qg -> qg contact term;

derive the corresponding-propagating q-intermediate support without
using C53 numerical matrix values;

construct the finite-cell plane-wave contact kernels;

derive exact inverse-partial-plus routing and zero-mode statuses;

project spin, polarization, ordered SU(3), HO/TM, CM-ground, and
triplet structures into the physical qg basis;

assemble all direct-contact primitive matrices;

import the complete C58 contraction package read-only;

assemble the retained-space instantaneous-fermion block operator;

retain the qg-sector missing self-induced-inertia counterterm-only
direction separately;

implement an independent matrix-free action for the complete operator;

close Hermiticity, count-once, unit, support, topology, isolation,
and physical-resolution diagnostics.
```

The complete retained-space bare coefficient is organized as:

\[
V_{\mathrm{IF,bare}}
=
g_s^2\,
\widehat V_{\mathrm{IF,bare}}^{(M^2)}.
\]

Do not choose, fit, or infer:

```text
g_s;
alpha_s;
a mass counterterm coefficient;
a field/residue coefficient;
a sector counterterm coefficient;
a subtraction constant;
a continuum finite part.
```

The strongest allowed status is:

```text
C59_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

When that gate passes, the exact next package is:

> **C60/HQCD3 — resume complete local-QCD substrate assembly with the immutable C53 canonical vertex and immutable C59 instantaneous-fermion operator**

---

# 2. Scientific boundary

C59 is:

```text
instantaneous-fermion specific;
direct-contact plus normal-ordering-contraction complete;
retained q plus qg space specific;
fixed-K finite-HO regulated;
source ordered;
coupling factored;
sector and counterterm explicit;
sparse and matrix free;
deterministic;
validation only.
```

C59 is not:

```text
a propagating one-loop self-energy calculation;
a product of two C53 numerical vertices;
a physical mass-renormalization calculation;
a free-Hamiltonian calculation;
an instantaneous color-current/gluon calculation;
a complete local-HQCD calculation;
a dressed-parton eigenproblem;
a JMY Wilson or bilocal-TMD calculation;
a matching calculation.
```

Do not broaden C59 into C60 merely because the completed operator can be inserted into a larger block.

---

# 3. Count-once decomposition

The following objects must remain distinct:

## 3.1 Direct normal-ordered instantaneous contact

The retained \(a^\dagger a\) source terms acting in the qg sector.

This is the new C59 calculation.

## 3.2 Self-induced-inertia contraction

The C58 commutator contribution.

Its q-sector primitive is imported read-only. Its qg-sector status remains `IFNORM2-SECTOR-SPECIFIC-COUNTERTERM-ONLY`.

## 3.3 Sequential propagating canonical contribution

The second-order contribution schematically:

\[
V_{\mathrm{C53}}^\dagger
(E-H_0)^{-1}
V_{\mathrm{C53}}.
\]

It is not evaluated and may not be substituted for either contact or contraction.

## 3.4 Local counterterm and metric directions

The unsolved source-derived directions imported from C58 and any direct-contact-specific direction proven necessary in C59.

## 3.5 Boundary and zero-mode completion

Separate local contributions or controls. They may not be hidden inside the contact coefficient.

No contribution ID may occur in more than one category.

Create:

```text
docs/next_level/c59_iferm_count_once_contract.json
```

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

docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_canonical_support_validation.json
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_zero_mode_boundary_regulator.json
docs/next_level/c57_projector_comparison_maps.json
docs/next_level/c57_readiness_report.json

docs/next_level/c58_implementation_report.md
docs/next_level/c58_derivation_authority_manifest.json
docs/next_level/c58_c57_import_report.json
docs/next_level/c58_bra_ket_support_contract.json
docs/next_level/c58_pair_support_decision.json
docs/next_level/c58_qg_sector_scope_decision.json
docs/next_level/c58_q_sector_contraction.json
docs/next_level/c58_qg_sector_contraction.json
docs/next_level/c58_sector_truncation_report.json
docs/next_level/c58_bare_subtraction_counterterm_plan.json
docs/next_level/c58_counterterm_direction_basis.json
docs/next_level/c58_counterterm_typing_report.json
docs/next_level/c58_local_self_energy_count_once.json
docs/next_level/c58_contraction_matrices.json
docs/next_level/c58_matrix_free_report.json
docs/next_level/c58_hermiticity_support_report.json
docs/next_level/c58_c59_import_contract.json
docs/next_level/c58_numerical_object_inventory.json
docs/next_level/c58_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c59_derivation_authority_manifest.json
docs/next_level/c59_input_fidelity_audit.json
```

---

# 5. Read-only C58 import

Before deriving a direct contact, verify the full C58 import contract.

At minimum verify:

```text
C58 readiness status;
q-sector primitive hashes;
q-sector symbolic-expression hashes;
q-sector basis-order hashes;
q-sector mode-ledger and shell hashes;
q-sector sparse/matrix-free residuals;
pair-support-plan ID;
qg-sector-plan ID;
bare-retention-plan ID;
qg-sector counterterm-only status or direction hashes;
counterterm-direction-basis hashes;
zero-mode and boundary-status hashes;
count-once hashes;
Hermiticity hashes;
comparison-map hashes.
```

Reproduce:

```text
q primitive shape:
    6 x 6 at every resolution;

q primitive nnz:
    6 at every resolution;

admitted contraction modes:
    4,216 / 8,330 / 14,484.
```

C59 may not:

```text
resum the C58 contraction;
change the pair support;
change the qg-sector decision;
apply a subtraction;
absorb the contraction into a mass;
fit a coefficient;
lift the q contraction into qg;
replace the C58 matrix-free route;
reclassify a C58 counterterm direction.
```

Create:

```text
docs/next_level/c59_c58_import_report.json
```

Any mismatch blocks all C59 assembly.

---

# 6. Freeze construction and holdouts

Before deriving the contact, freeze:

```text
the exact C55 direct-contact monomial IDs;
the exact normal-ordering source order;
the C43/C45 field normalization;
the C43 inverse-partial-plus prescription;
the zero-mode and residual-boundary policy;
the C47 physical qg basis order;
the C53 SU(3) and triplet conventions;
the source corresponding-propagating graph rule;
the M^2 conversion convention;
the symbolic L policy;
the read-only C58 package.
```

Freeze holdouts:

```text
at least one nonzero direct-contact matrix element for every
source-ordered contact term;

both quark helicities;

both incoming and outgoing gluon helicities;

every input/output triplet color label or an exact complete color
holdout;

smallest and largest external gluon longitudinal modes;

one diagonal and one off-diagonal qg basis pair;

one pair with a common intermediate q state;

one pair with no common intermediate q state;

one source-Hermitian partner pair;

one nearest-zero nonzero inverse denominator;

one exact zero-mode control;

one nontrivial intrinsic-OAM transition;

one full-product versus triplet color holdout;

one single-particle-HO versus intrinsic/CM projection holdout;

one GeV/MeV holdout;

one symbolic-L holdout;

one adjacent-resolution comparison holdout.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c59_calculation_plan.json
docs/next_level/c59_holdout_plan.json
```

---

# 7. Identify every direct-contact source term

Read the C55 normal-ordering and monomial ledgers.

Identify every source term contributing to the retained normal-ordered qg-preserving contact.

The expected source may contain contributions from:

```text
an original a-dagger a ordering;

the normal-ordered descendant of an a a-dagger ordering;

Hermitian-conjugate field orderings;

distinct ordered color products;

distinct inverse-derivative placements.
```

This list is illustrative only.

For every source term record:

```text
C55 monomial ID;
field ordering;
fermion ordering;
gluon-number change;
normal-order ancestry;
color ordering;
derivative placement;
Hermitian partner;
retained physical block;
coupling order;
mass dimension.
```

Allowed statuses:

```text
DIRECT_QG_CONTACT_REQUIRED;
DIRECT_QG_CONTACT_EXACT_ZERO_BY_SOURCE_ALGEBRA;
OUTSIDE_RETAINED_SPACE_NONZERO_OPERATOR;
NOT_APPLICABLE_WITH_SOURCE_PROOF;
ABSENT_BLOCKING.
```

The positive gate requires no required `ABSENT_BLOCKING` source term.

Create:

```text
docs/next_level/c59_direct_contact_source_ledger.json
docs/next_level/c59_direct_contact_component_contract.json
```

---

# 8. Exact corresponding-propagating support for the direct contact

The TBP rule that selected the C57 regulator must be applied to the direct contact at its own topology.

For qg bra and ket states, derive the retained support through the corresponding propagating intermediate state or exact source equivalent.

A typical topology is:

\[
qg_{\rm ket}
\longrightarrow
q_{\rm int}
\longrightarrow
qg_{\rm bra},
\]

but use the exact C55 ordered source terms.

Compile mutually exclusive support plans.

## 8.1 `IFERM2-SOURCE-ORDERED-Q-INTERMEDIATE-SUPPORT`

Each ordered contact term carries an explicit intermediate-q support derived from the canonical source selection rules.

The source-defined sum of ordered terms produces the contact.

## 8.2 `IFERM2-COMMON-Q-INTERMEDIATE-PROJECTOR`

A qg pair contributes when bra and ket connect to at least one common retained q intermediate state under the exact source ordering.

This plan may be selected only if derived, not assumed.

## 8.3 `IFERM2-FULL-EXTERNAL-QG-SUPPORT`

The direct contact acts on the entire source-allowed physical qg block without a corresponding-propagating restriction.

This plan requires an explicit source-level exemption from the graph-selection rule.

## 8.4 `IFERM2-DIRECT-CONTACT-SUPPORT-UNAVAILABLE`

No unique support can be derived.

Do not use:

```text
C53 numerical nonzero values;
C53 singular values;
C53 energy denominators;
an arbitrary support union or intersection;
a support selected after inspecting Hermiticity;
the complete external qg basis merely because it exists.
```

The C53 support and entry ancestry may be used only as independent holdouts after construction.

Create:

```text
docs/next_level/c59_direct_contact_support_contract.json
docs/next_level/c59_direct_contact_support_decision.json
docs/next_level/c59_direct_contact_support_validation.json
```

---

# 9. Plane-wave direct-contact kernel

Insert the exact C43/C45 field expansions into every required C55 direct-contact term.

Derive the finite-cell plane-wave kernel:

\[
\mathcal C_{\lambda'_q h'_g;\lambda_q h_g}
(p'_q,k'_g;p_q,k_g)
\]

or the exact source-equivalent object.

Retain:

```text
incoming and outgoing quark modes;
incoming and outgoing gluon modes;
source-ordered contact-term ID;
intermediate-q support identity;
longitudinal Kronecker constraints;
transverse momentum structure;
spin tensor;
polarization vectors;
ordered SU(3) tensor;
inverse-partial-plus denominator;
finite-cell normalization;
phase;
P^- units.
```

Do not derive the value by multiplying two C53 matrix elements.

Implement at least two spinor routes:

```text
good-component/constrained-field route;

four-component source expression reduced with the C43 projectors.
```

Create:

```text
docs/next_level/c59_plane_wave_contact_kernel.json
docs/next_level/c59_spin_polarization_contact_validation.json
```

---

# 10. Inverse-\(\partial^+\) routing and zero modes

For every ordered direct-contact term, derive the exact product on which:

\[
\frac{1}{i\partial^+}
\]

acts.

Record:

```text
incoming q and g modes;
outgoing q and g modes;
source field order;
intermediate product mode;
intermediate q support ID;
exact rational denominator;
denominator sign;
PV prescription;
P0/Q0 status;
boundary partner;
Hermitian-conjugate routing.
```

Do not replace the inverse derivative by a propagating light-front energy denominator.

Every zero denominator must have one status:

```text
EXCLUDED_BY_Q0_WITH_SOURCE_PROOF;
CANCELS_WITH_DECLARED_BOUNDARY_TERM;
RETAINED_ZERO_MODE_CONTROL;
ABSENT_BLOCKING.
```

Never use:

```text
epsilon;
clipping;
pseudoinverse;
silent entry deletion.
```

Create:

```text
docs/next_level/c59_contact_inverse_derivative_routing.json
docs/next_level/c59_contact_zero_denominator_ledger.json
docs/next_level/c59_contact_inverse_derivative_validation.json
```

---

# 11. Ordered SU(3) color operator

For each source-ordered contact term, construct the full product-color operator:

\[
\mathcal C_{\rm color}:
\mathbb C^3\otimes\mathbb C^8
\longrightarrow
\mathbb C^3\otimes\mathbb C^8.
\]

Retain the exact ordered products, for example \(T^aT^b\) or \(T^bT^a\), only as actually derived.

Do not replace the ordered tensor by \(C_F I\) before external gluon colors are evaluated.

Reduce independently with the frozen C53 triplet isometry:

\[
\mathcal C_{\rm color}^{(3)}
=
U_3^\dagger
\mathcal C_{\rm color}
U_3.
\]

Required checks:

```text
full-product versus triplet-route equality;
fundamental and adjoint SU(3) covariance;
triplet preservation;
zero anti-sextet and 15 leakage;
source-order Hermiticity after required terms are summed;
triplet-basis rotation covariance;
Abelian limit;
wrong-generator negative controls.
```

Create:

```text
docs/next_level/c59_direct_contact_color_operator.json
docs/next_level/c59_direct_contact_color_validation.json
```

---

# 12. Finite-cell normalization

Derive every normalization factor from:

```text
the quark field expansions;
the two external-gluon field expansions;
the finite-cell creation/annihilation brackets;
the qg state normalization;
the x^- integration;
the transverse integration;
the source-ordered intermediate-q support;
the C47 physical basis normalization.
```

Keep \(L\) symbolic.

For every direct-contact source component determine whether:

```text
L cancels;
one block-common L power remains;
or a source-defined finite-volume dependence remains.
```

No element-dependent \(L\) signature may survive in one matrix block.

Create:

```text
docs/next_level/c59_direct_contact_finite_volume_normalization.json
docs/next_level/c59_direct_contact_normalization_validation.json
```

---

# 13. \(P^-\!\to M^2\) conversion

Derive the direct-contact contribution in both forms:

\[
\widehat V_{\mathrm{contact}}^{(-)}
\]

and:

\[
\widehat V_{\mathrm{contact}}^{(M^2)}.
\]

Use:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Prove:

```text
same total P^+ on qg bra and ket;
same total transverse/CM frame;
the O(g_s^2) P_perp^2 contact status;
state-normalization compatibility;
the factor of two in the project convention.
```

Do not copy the C50 or C58 conversion without checking the qg-preserving contact.

Every completed primitive must have uniform mass-squared units.

Create:

```text
docs/next_level/c59_direct_contact_pminus_to_m2_contract.json
docs/next_level/c59_direct_contact_pminus_to_m2_validation.json
```

---

# 14. Physical HO/TM/CM projection

Project every source-ordered plane-wave contact term into the physical qg basis.

The local contact generally requires a four-mode transverse integral.

Derive:

```text
single-particle HO integration measure;
incoming and outgoing x-scaled variables;
Fourier and HO phases;
Talmi--Moshinsky/Jacobi maps;
CM-ground projections;
intrinsic OAM selection;
K and Jz selection;
triplet color reduction;
basis normalization.
```

Implement two independent routes:

## 14.1 Single-particle route

Evaluate the finite four-mode HO integral and then apply the C47 physical-basis maps.

## 14.2 Intrinsic/CM route

Transform the operator into the C47 intrinsic/CM basis and evaluate directly in the CM-ground subspace.

Require agreement on all holdouts and a broad deterministic sample.

Do not use C47 raw canonical tuple values.

Create:

```text
docs/next_level/c59_direct_contact_projection_contract.json
docs/next_level/c59_direct_contact_projection_validation.json
```

---

# 15. Arbitrary-mode direct-contact evaluator

Create:

```python
evaluate_direct_iferm_contact(
    incoming_qg_basis_id,
    outgoing_qg_basis_id,
    resolution,
    symbolic_parameters,
) -> DirectIFermContactEvaluation
```

The result must contain:

```text
basis IDs;
ordered source-term records;
intermediate-q support IDs;
plane-wave kernel components;
inverse-derivative routing;
zero-mode status;
spin/polarization values;
full-product and triplet color values;
transverse primitive;
P^- value;
M^2 value;
units;
symbolic signature;
source ancestry;
exact-zero or truncation reason.
```

The evaluator must not consume:

```text
C40 values;
C47 raw canonical tuples;
C50 combined values;
C53 numerical vertex values;
C53 energy denominators;
C58 contraction values;
a fitted contact coefficient.
```

C58 is imported only later during final block assembly.

Create:

```text
docs/next_level/c59_direct_contact_evaluator_api.json
docs/next_level/c59_direct_contact_evaluator_validation.json
```

---

# 16. Exhaustive qg contact domain

Enumerate the complete physical qg/qg Cartesian domain by exact conserved blocks.

Every pair receives one status:

```text
PRESELECTION_FORBIDDEN_EXACT;
EXCLUDED_BY_CORRESPONDING_PROPAGATING_RULE;
EVALUATED_EXACT_ZERO;
EVALUATED_NONZERO;
OUTSIDE_DECLARED_CONTACT_SCOPE;
EVALUATOR_UNAVAILABLE_BLOCKING;
DUPLICATE_BLOCKING.
```

Preselection may use only:

```text
resolution;
K;
Jz;
flavor;
gluon number;
CM-ground identity;
triplet identity;
source-ordered support;
zero-mode domain.
```

Report:

```text
Cartesian pair count;
preselection count;
support-exclusion count;
evaluator calls;
exact-zero count;
nonzero count;
outside-scope count;
duplicates;
missing entries;
blocking entries.
```

A positive gate requires:

```text
duplicates = 0;
missing = 0;
blocking = 0.
```

Create:

```text
docs/next_level/c59_direct_contact_domain_ledger.json
docs/next_level/c59_direct_contact_count_once_report.json
```

---

# 17. Assemble direct-contact primitive matrices

For every physical resolution assemble:

\[
\widehat V_{\mathrm{contact},qg}^{(M^2)}.
\]

Store separately:

```text
source-component primitive matrices;
source symbolic coefficients;
complete direct-contact primitive;
g_s^2 coupling-order label;
diagnostic evaluated matrices at explicitly nonphysical substitutions;
entry ancestry.
```

Do not insert a physical \(g_s\).

Expected physical shapes are:

```text
1,344 x 1,344;
2,700 x 2,700;
4,752 x 4,752;
```

subject to exact manifest verification.

Use blockwise sparse shards. Do not allocate a dense fine-resolution matrix.

Required checks:

```text
shape and basis order;
nnz derived rather than assumed;
mass-squared units;
source-term sum;
intermediate-support identity;
K and Jz conservation;
CM-ground preservation;
triplet preservation;
source Hermiticity;
direct-element holdouts.
```

Create:

```text
docs/next_level/c59_direct_contact_matrices.json
docs/next_level/c59_direct_contact_entry_ancestry.json
docs/next_level/c59_direct_contact_matrix_validation.json
```

---

# 18. Independent direct-contact matrix-free action

Implement:

```python
apply_direct_iferm_contact(
    vector_qg,
    resolution,
    symbolic_parameters,
)
```

The independent route must:

```text
reconstruct the source-ordered q-intermediate support;
enumerate admitted qg pairs;
call the direct-contact evaluator;
accumulate every ordered source term;
retain support and source-component diagnostics.
```

It must not:

```text
multiply by the stored direct-contact matrix;
load an entry ledger as numerical authority;
construct the contact from C53 V-dagger D-inverse V;
consume C53 numerical values;
consume C58 contraction values.
```

Compare sparse and matrix-free actions on:

```text
every basis vector in tractable conserved blocks;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions;
multiple diagnostic symbolic substitutions.
```

Create:

```text
docs/next_level/c59_direct_contact_matrix_free_report.json
```

---

# 19. Import the C58 sector package

Import read-only:

```text
the q-sector self-induced-inertia primitive;
its executable symbolic coefficient;
its independent matrix-free action;
its pair-support and shell ancestry;
its qg-sector counterterm-only status or direction;
its bare-retention plan;
its counterterm/operator-direction typing;
its zero-mode and boundary statuses.
```

Do not recompute the C58 contraction during normal C59 assembly.

For the end-to-end reconstruction test, C58 may be independently rebuilt only through its authoritative builder and hashes.

Create:

```text
docs/next_level/c59_c58_sector_import_report.json
```

---

# 20. Complete retained-space block classification

Finalize the instantaneous-fermion physical blocks:

```text
q -> q;
q -> qg;
qg -> q;
qg -> qg.
```

The expected pattern from inherited source decisions is:

```text
q -> q:
    C58 bare self-induced-inertia primitive;

q -> qg:
    exact zero by C55 gluon-number parity;

qg -> q:
    exact zero by C55 gluon-number parity;

qg -> qg:
    C59 direct normal-ordered contact primitive;
    no qg bare self-induced-inertia loop under the selected
    corresponding-propagating highest-sector truncation;
    separate C58 sector-specific counterterm-only direction.
```

Do not force this pattern when an exact C59 source calculation contradicts it.

Distinguish:

```text
zero full operator;
zero retained matrix block;
excluded bare loop by truncation;
counterterm-direction-only status;
outside retained space.
```

Create:

```text
docs/next_level/c59_complete_block_classification.json
```

---

# 21. Assemble the complete instantaneous-fermion operator

Construct the bare retained-space coefficient:

\[
\widehat V_{\mathrm{IF,bare}}^{(M^2)}
=
\begin{pmatrix}
\widehat\Sigma_{q,\mathrm{SII}}^{(M^2)}
&
0
\\[1mm]
0
&
\widehat V_{\mathrm{contact},qg}^{(M^2)}
\end{pmatrix}.
\]

This expression is the expected structure. Use the exact source-derived block result.

Keep separately:

```text
qg highest-sector self-induced-inertia counterterm direction;
q-sector and qg-sector mass directions;
metric/residue directions;
boundary and zero-mode directions;
any independent C58 self-induced-inertia direction.
```

The complete coupling-factored interaction is:

\[
V_{\mathrm{IF,bare}}
=
g_s^2
\widehat V_{\mathrm{IF,bare}}^{(M^2)}.
\]

No physical counterterm coefficient is inserted.

Create:

```text
docs/next_level/c59_complete_iferm_operator.json
docs/next_level/c59_iferm_counterterm_direction_manifest.json
```

---

# 22. Independent complete matrix-free action

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
call the immutable C58 direct mode-sum action for q;
call the independent C59 direct-contact action for qg;
return block-separated bare actions;
return counterterm-direction actions separately;
preserve exact-zero off-diagonal blocks.
```

It must not multiply by the assembled complete block matrix.

Compare assembled and matrix-free actions on:

```text
q basis vectors;
qg basis vectors in tractable blocks;
mixed q plus qg deterministic vectors;
random normalized complex vectors;
all resolutions;
multiple diagnostic substitutions.
```

Create:

```text
docs/next_level/c59_complete_iferm_matrix_free_report.json
docs/next_level/c59_complete_iferm_action_validation.json
```

---

# 23. Source Hermiticity

Hermiticity must follow from:

```text
the C58 ordered-joint-support contraction;
the C55 direct-contact source ordering;
the C59 q-intermediate support contract;
mode-level conjugation;
inverse-denominator conjugation;
spin and polarization conjugation;
ordered color conjugation;
physical basis phases.
```

Do not apply:

\[
M\to\frac12(M+M^\dagger)
\]

after assembly.

Report:

```text
direct-contact source-term pairing residual;
intermediate-support conjugation residual;
mode-level residual;
q-block residual;
qg-block residual;
complete block residual;
matrix-free conjugation residual;
basis-phase covariance.
```

Create:

```text
docs/next_level/c59_iferm_hermiticity_report.json
docs/next_level/c59_iferm_spectrum_report.json
```

Do not clip negative eigenvalues. Positivity is not required unless the source proves it.

---

# 24. Topology and graph-selection checks

Execute independent checks that distinguish:

```text
direct contact;
C58 contraction;
C53 sequential propagation;
qg highest-sector omitted contraction;
counterterm-only direction.
```

At frozen plane-wave holdouts, compare the source contact topology with the corresponding propagating support identity without using propagating numerical values.

Where the source supplies a local cancellation or covariant-equivalence identity, test only its declared term combination.

Do not claim a full Ward or Slavnov--Taylor identity.

Create:

```text
docs/next_level/c59_contact_propagating_topology_report.json
docs/next_level/c59_corresponding_graph_support_report.json
```

---

# 25. Counterterm and sector typing

Preserve the C58 bare-retention plan.

Audit whether the completed direct contact introduces any additional local direction beyond the imported C58 basis.

At minimum retain:

```text
q mass-squared direction;
q field/residue or metric direction;
q-sector self-induced-inertia direction;
qg sector-specific mass direction;
qg highest-sector counterterm-only direction;
local basis-boundary direction;
zero-mode direction;
direct-contact operator direction where independent.
```

Report:

```text
direction Gram or generalized-metric matrix;
rank;
nullity;
condition number;
diagnostic projection coefficients;
orthogonal residual;
sector dependence;
comparison-map behavior.
```

Diagnostic coefficients are not physical renormalization coefficients.

Do not force the direct contact or omitted qg contraction into a universal scalar mass direction.

Create:

```text
docs/next_level/c59_iferm_counterterm_typing_report.json
docs/next_level/c59_iferm_sector_dependence_report.json
```

---

# 26. Unit, regulator, and convention covariance

Execute:

```text
GeV/MeV conversion;
symbolic-L scaling or cancellation;
fixed-x P^+ rescaling;
bHO scaling and basis transformation;
quark-mass variation where applicable;
Fourier phase;
quark-helicity phase;
gluon-polarization phase;
triplet phase;
PV prescription controls;
zero-mode-projector controls;
normal-ordering controls;
corresponding-support controls;
factor-of-two M^2 control;
wrong SU(3) controls;
omitted/duplicated contact controls.
```

Require:

```text
every completed M^2 block scales as mass squared;
all symbolic signatures are block consistent;
color factors change no units;
dimensionless residuals are invariant;
wrong conventions fail explicitly.
```

Create:

```text
docs/next_level/c59_unit_regulator_convention_report.json
```

---

# 27. Physical-resolution comparisons

Use the C47/C57/C58 comparison maps.

Evaluate separately:

```text
C58 q-sector self-induced-inertia primitive;
C59 qg direct-contact primitive;
complete bare instantaneous-fermion block;
every imported or new counterterm direction.
```

For each operator evaluate the exact supported comparison:

\[
R\,O_{R'}\,P
\quad\text{versus}\quad
O_R.
\]

Separate:

```text
longitudinal nonnesting;
HO-shell truncation;
bHO scale change;
corresponding-support change;
CM projection;
triplet representation;
highest-sector truncation;
zero-mode/boundary change;
symbolic normalization;
numerical error.
```

Do not tune any coefficient to reduce a comparison residual.

Create:

```text
docs/next_level/c59_iferm_comparison_report.json
docs/next_level/c59_iferm_comparison_remainder_ledger.json
```

---

# 28. Isolation and poisoning controls

Prove that C59 is unchanged when:

```text
all C40 arrays are poisoned;
all historical C47 canonical tuple values and metadata are poisoned;
all C50 combined values are poisoned;
all C53 numerical matrix values and energy denominators are poisoned;
all BPP DLCQ finite sums are unavailable;
all ART25 files are inaccessible.
```

The build must fail when:

```text
a C58 import hash changes;
the C55 direct-contact monomial ledger changes;
the C57/C59 corresponding-support rule changes;
the inverse-derivative prescription changes;
the zero-mode policy changes;
the C47 qg basis order changes;
the C53 triplet-isometry hash changes;
a direct-contact source term is omitted or duplicated;
the qg counterterm-only status is silently promoted to a bare loop;
a conditional support is relabeled universal.
```

Create:

```text
docs/next_level/c59_isolation_report.json
```

---

# 29. C60/HQCD3 import contract

Define the immutable contract by which C60 will consume:

```text
the complete bare instantaneous-fermion block;
the q and qg block classifications;
the qg sector-specific counterterm-only direction;
all other local counterterm/metric directions;
the g_s^2 coupling-order label;
the exact-zero off-diagonal blocks;
the source-support and zero-mode statuses;
the independent complete matrix-free action;
the count-once, Hermiticity, ancestry, and comparison ledgers.
```

C60 must verify all hashes before assembling free or instantaneous-current matrices.

C60 may not:

```text
rederive the direct contact;
recompute the C58 contraction;
change the highest-sector status;
rescale the operator;
apply a subtraction;
fit a coefficient;
replace any block by C53 propagation.
```

Create:

```text
docs/next_level/c59_c60_import_contract.json
```

---

# 30. Deterministic runtime bundles

For every physical resolution produce content-addressed bundles containing:

```text
direct-contact support tables;
ordered source-component ledgers;
direct-contact primitive matrices;
read-only C58 q-sector identities;
complete instantaneous-fermion block;
counterterm/operator-direction records;
matrix-free reconstruction metadata;
block-classification records;
entry ancestry;
count-once ledgers;
Hermiticity records;
holdout and comparison records.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c59_iferm2/
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
C58 import hash;
support-plan ID;
basis-order hash;
expression hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c59_numerical_object_inventory.json
```

All JSON, symbolic expressions, and arrays must regenerate byte-for-byte.

---

# 31. End-to-end source-to-complete-operator test

Implement an end-to-end test that begins from the C43/C45/C47/C55/C57/C58 contracts—not from prebuilt C59 matrices.

It must:

```text
verify and import C58;
identify every direct-contact source term;
derive corresponding q-intermediate support;
derive plane-wave contact kernels;
derive inverse-derivative routing;
evaluate spin, polarization, and ordered color;
derive finite-cell normalization;
convert P^- to M^2;
project into the physical qg basis;
enumerate every admitted qg pair;
assemble direct-contact matrices;
assemble the complete retained-space operator;
apply the independent complete matrix-free action;
run Hermiticity, topology, unit, poisoning, count-once,
and comparison tests;
reproduce every hash.
```

It must fail when:

```text
a C58 matrix is altered or rescaled;
the C58 contraction is lifted into qg;
a C53 numerical value or energy denominator enters;
the direct contact is constructed as V-dagger D-inverse V;
an ordered contact source term is omitted;
a source term is counted both before and after normal ordering;
an arbitrary support union or intersection is used;
the contact is post-hoc Hermitianized;
a zero denominator is clipped;
a nontriplet remainder is silently removed;
a qg omitted contraction is serialized as a zero full-QCD operator;
a counterterm coefficient is fitted;
a physical g_s is inserted;
a runtime hash changes.
```

---

# 32. Focused mutation tests

Create at least **256 focused live mutations** of actual source terms, supports, kernels, matrices, or directions.

Include mutations of:

```text
C58 import hash;
C58 q primitive entry;
C58 qg sector status;
direct-contact monomial ID;
normal-order ancestry;
source-term order;
q-intermediate support;
incoming or outgoing qg basis ID;
inverse-derivative denominator;
PV prescription;
zero-mode status;
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
direct-contact matrix entry;
matrix-free accumulation;
exact-zero off-diagonal block;
counterterm direction;
count-once identity;
Hermitian partner;
comparison map;
runtime hash.
```

Every mutation must fail a concrete source, support, normal-ordering, zero-mode, dimension, color, Hermiticity, typing, count-once, matrix-free, holdout, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 33. Readiness gate

Issue:

```text
C59_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

only when:

```text
the full C58 baseline reproduces;
all C58 objects import read-only;
the complete direct-contact source ledger has no required blocker;
one source-derived corresponding-propagating support plan is selected;
the direct-contact plane-wave kernels close;
inverse-derivative routing is explicit;
every zero denominator has a typed status;
spin and polarization routes agree;
ordered full-product and triplet color routes agree;
finite-cell normalization closes;
P^- to M^2 conversion closes;
single-particle and intrinsic/CM projection routes agree;
the direct-contact evaluator covers every admitted pair;
the qg contact domain has no duplicate, missing, or blocking row;
direct-contact matrices exist at every physical resolution;
the independent direct-contact matrix-free action agrees;
the C58 q-sector contraction remains immutable;
the qg highest-sector counterterm-only status remains explicit;
the complete q/q, q/qg, qg/q, and qg/qg block classification closes;
the complete bare instantaneous-fermion block exists;
the independent complete matrix-free action agrees;
Hermiticity follows from source ordering without post-hoc repair;
contact, contraction, propagation, counterterm, boundary, and zero-mode
objects remain count-once distinct;
counterterm and sector typing is complete with visible residuals;
unit, convention, support, zero-mode, color, and poisoning tests pass;
physical-resolution comparisons execute;
the C60 import contract is complete;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-complete-operator test passes.
```

Do not issue:

```text
C59_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C59_INSTANTANEOUS_CURRENT_READY;
C59_PROJECTED_ACTION_IDENTITY_READY;
C59_PHYSICAL_MASS_RENORMALIZATION_SOLVED;
C59_JMY_WILSON_MATRIX_VALIDATED;
C59_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 34. Exact no-go branches

## A. C58 import fails

```text
C59_IFERM_C58_IMPORT_INCOMPLETE
```

Next:

> **C60/IFNORM3 — contraction-package integrity, sector status, and import closure**

## B. Direct-contact source ledger remains incomplete

```text
C59_IFERM_DIRECT_CONTACT_SOURCE_INCOMPLETE
```

Next:

> **C60/IFCONTACT — exact normal-ordered qg-contact source-term completion**

## C. Corresponding-propagating support remains incomplete

```text
C59_IFERM_CONTACT_SUPPORT_INCOMPLETE
```

Next:

> **C60/IFSUPPORT — source-ordered q-intermediate support and graph-selection closure**

## D. Kernel or finite-volume normalization remains incomplete

```text
C59_IFERM_CONTACT_KERNEL_INCOMPLETE
```

Next:

> **C60/IFKERNEL2 — spin, polarization, color, finite-cell normalization, and M-squared completion**

## E. Inverse derivative or zero modes remain incomplete

```text
C59_IFERM_CONTACT_ZERO_MODE_INCOMPLETE
```

Next:

> **C60/IFZERO5 — direct-contact denominator, PV, boundary, and zero-mode completion**

## F. Physical HO/TM/CM or triplet projection remains incomplete

```text
C59_IFERM_CONTACT_PHYSICAL_PROJECTION_INCOMPLETE
```

Next:

> **C60/IFPROJ2 — all-mode qg contact projection and triplet closure**

## G. Source Hermiticity fails

```text
C59_IFERM_HERMITICITY_INCOMPLETE
```

Next:

> **C60/IFHERM2 — ordered contact-term support, conjugation, and Hermitian closure**

## H. qg sector counterterm-only direction remains incomplete

```text
C59_IFERM_QG_SECTOR_DIRECTION_INCOMPLETE
```

Next:

> **C60/IFSECTOR2 — highest-sector truncation and counterterm-direction completion**

## I. Sparse and matrix-free actions disagree

```text
C59_IFERM_MATRIX_ACTION_CLOSURE_FAILED
```

Next:

> **C60/IFACT4 — independent complete instantaneous-fermion action closure**

## J. Complete instantaneous-fermion operator closes

```text
C59_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY
```

Next:

> **C60/HQCD3 — resume complete local-QCD substrate assembly**

---

# 35. Required deliverables

Create at least:

```text
docs/next_level/c59_implementation_report.md
docs/next_level/c59_api.md
docs/next_level/c59_derivation_authority_manifest.json
docs/next_level/c59_input_fidelity_audit.json
docs/next_level/c59_iferm_count_once_contract.json

docs/next_level/c59_c58_import_report.json
docs/next_level/c59_calculation_plan.json
docs/next_level/c59_holdout_plan.json

docs/next_level/c59_direct_contact_source_ledger.json
docs/next_level/c59_direct_contact_component_contract.json
docs/next_level/c59_direct_contact_support_contract.json
docs/next_level/c59_direct_contact_support_decision.json
docs/next_level/c59_direct_contact_support_validation.json

docs/next_level/c59_plane_wave_contact_kernel.json
docs/next_level/c59_spin_polarization_contact_validation.json
docs/next_level/c59_contact_inverse_derivative_routing.json
docs/next_level/c59_contact_zero_denominator_ledger.json
docs/next_level/c59_contact_inverse_derivative_validation.json

docs/next_level/c59_direct_contact_color_operator.json
docs/next_level/c59_direct_contact_color_validation.json
docs/next_level/c59_direct_contact_finite_volume_normalization.json
docs/next_level/c59_direct_contact_normalization_validation.json
docs/next_level/c59_direct_contact_pminus_to_m2_contract.json
docs/next_level/c59_direct_contact_pminus_to_m2_validation.json

docs/next_level/c59_direct_contact_projection_contract.json
docs/next_level/c59_direct_contact_projection_validation.json
docs/next_level/c59_direct_contact_evaluator_api.json
docs/next_level/c59_direct_contact_evaluator_validation.json

docs/next_level/c59_direct_contact_domain_ledger.json
docs/next_level/c59_direct_contact_count_once_report.json
docs/next_level/c59_direct_contact_matrices.json
docs/next_level/c59_direct_contact_entry_ancestry.json
docs/next_level/c59_direct_contact_matrix_validation.json
docs/next_level/c59_direct_contact_matrix_free_report.json

docs/next_level/c59_c58_sector_import_report.json
docs/next_level/c59_complete_block_classification.json
docs/next_level/c59_complete_iferm_operator.json
docs/next_level/c59_iferm_counterterm_direction_manifest.json
docs/next_level/c59_complete_iferm_matrix_free_report.json
docs/next_level/c59_complete_iferm_action_validation.json

docs/next_level/c59_iferm_hermiticity_report.json
docs/next_level/c59_iferm_spectrum_report.json
docs/next_level/c59_contact_propagating_topology_report.json
docs/next_level/c59_corresponding_graph_support_report.json
docs/next_level/c59_iferm_counterterm_typing_report.json
docs/next_level/c59_iferm_sector_dependence_report.json

docs/next_level/c59_unit_regulator_convention_report.json
docs/next_level/c59_iferm_comparison_report.json
docs/next_level/c59_iferm_comparison_remainder_ledger.json
docs/next_level/c59_isolation_report.json
docs/next_level/c59_c60_import_contract.json

docs/next_level/c59_numerical_object_inventory.json
docs/next_level/c59_readiness_report.json
docs/next_level/c59_source_sufficiency_decision.json
docs/next_level/c59_no_go_decision_tree.json
docs/next_level/c59_missing_calculation_specification.md
docs/next_level/c59_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/iferm2/
```

or the repository-equivalent package.

Add focused tests for:

```text
C58 read-only import;
direct-contact source-term inventory;
corresponding q-intermediate support;
plane-wave contact kernel;
inverse derivative and zero modes;
spin/polarization/color;
finite-cell normalization;
P^- to M^2 conversion;
HO/TM/CM/triplet projection;
arbitrary evaluator;
qg domain and count once;
direct-contact sparse/matrix-free action;
complete block assembly;
complete matrix-free action;
Hermiticity;
counterterm/sector typing;
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

# 36. Acceptance criteria

C59 is complete only when:

1. The full C58 baseline reproduces.
2. The C58 positive gate remains explicit.
3. The C53 physical canonical vertex remains read-only.
4. The C43 action, C45 modes, and C47 basis remain unchanged.
5. C40 remains method-oracle only.
6. Historical C47 tuple values and metadata remain diagnostic-only.
7. No C53 numerical value or energy denominator enters.
8. No BPP DLCQ finite sum enters.
9. No physical \(g_s\), \(\alpha_s\), subtraction, or counterterm coefficient is chosen.
10. No arbitrary numerical \(L\) is introduced.
11. Every C58 import hash passes.
12. The C58 q primitive remains byte-identical.
13. The C58 qg counterterm-only status remains explicit.
14. Every required direct-contact source term is identified.
15. Normal-order ancestry remains explicit.
16. No source term is omitted or duplicated.
17. One source-derived direct-contact support plan is selected.
18. No arbitrary support union or intersection is used.
19. C53 support is a holdout only.
20. Every direct-contact inverse denominator follows exact operator routing.
21. No epsilon, clipping, pseudoinverse, or deletion is used.
22. Every zero denominator has a typed status.
23. Good-component and four-component spin routes agree.
24. Polarization identities close at the declared scope.
25. Ordered SU(3) color factors are source derived.
26. Full-product and triplet color routes agree.
27. No nontriplet leakage is hidden.
28. Finite-cell normalization is complete.
29. Symbolic \(L\) dependence is common, factored, or canceled.
30. The direct-contact \(P^-\!\to M^2\) conversion closes.
31. Every completed primitive has mass-squared units.
32. Single-particle and intrinsic/CM projection routes agree.
33. The direct-contact evaluator is independent of historical values.
34. Every admitted qg pair is evaluated.
35. Duplicate, missing, and blocking contact counts are zero.
36. Direct-contact matrices exist at every resolution.
37. Their shapes and basis orders match the physical manifests.
38. Their nnz counts are derived rather than assumed.
39. Sparse and independent direct-contact actions agree.
40. q/q is the immutable C58 contraction or exact source-derived descendant.
41. q/qg and qg/q exact-zero proofs remain intact.
42. qg/qg contains the direct contact without a fabricated qg bare loop contraction.
43. Highest-sector counterterm-only status is not serialized as zero full QCD.
44. The complete bare instantaneous-fermion block exists.
45. Counterterm directions remain separate from the bare operator.
46. The independent complete matrix-free action agrees.
47. Hermiticity follows without post-hoc averaging.
48. Negative eigenvalues are not clipped.
49. Direct contact, contraction, propagation, counterterm, boundary, and zero-mode contributions are count-once distinct.
50. Counterterm and sector typing retains visible residuals.
51. GeV/MeV, \(L\), \(P^+\), \(b_{\rm HO}\), mass, phase, PV, zero-mode, support, factor-of-two, and SU(3) controls pass.
52. Physical-resolution comparisons retain all separated remainders.
53. Static and runtime poisoning controls pass.
54. The C60 import contract is complete.
55. Runtime bundles contain actual kernels, matrices, statuses, and independent action metadata.
56. End-to-end reconstruction passes.
57. At least 256 focused live mutations are detected.
58. No free matrix is claimed complete.
59. No instantaneous-current matrix is claimed complete.
60. No complete local-HQCD status is issued.
61. No projected action/current identity is claimed complete.
62. No JMY Wilson or bilocal TMD matrix is created.
63. No soft subtraction or nonlocal counterterm system is created.
64. No physical mass-renormalization result is claimed.
65. No one-loop TMD coefficient or matching kernel is created.
66. No proton TMD or ART25 bridge is created.
67. No fit, inference, process, or production route is created.
68. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
69. `MSHT20_REP/` remains untouched and outside Git.
70. The working tree is clean except for the pre-existing untracked directory.
71. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken direct-contact source completeness, corresponding-propagating support, inverse-derivative routing, source Hermiticity, highest-sector typing, count-once separation, or independent matrix-free action to open the gate.

---

# 37. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C55/C57/C58 inputs consumed;
- C58 import hashes, q primitive shape/nnz, admitted-mode counts, and qg-sector status;
- complete direct-contact source-term inventory and normal-order ancestry;
- selected direct-contact support plan and rejected alternatives;
- intermediate-q support counts and C53 support holdout residuals;
- plane-wave kernel components;
- inverse-derivative denominator ranges and zero-mode statuses;
- spin and polarization residuals;
- ordered full-product and triplet color residuals;
- finite-cell normalization and symbolic-\(L\) behavior;
- \(P^-\!\to M^2\) residuals;
- single-particle and intrinsic/CM projection residuals;
- qg contact domain counts;
- direct-contact matrix shapes, nnz, norms/spectra, units, and symbolic signatures;
- direct-contact sparse/matrix-free residuals;
- final q/q, q/qg, qg/q, and qg/qg block statuses;
- complete instantaneous-fermion block shapes, nnz, units, and coupling label;
- complete sparse/matrix-free residuals;
- source-Hermiticity residuals;
- topology and count-once decisions;
- counterterm-direction basis, rank, condition number, typing, and orthogonal residual;
- sector-dependence result;
- unit, regulator, phase, support, zero-mode, wrong-color, and poisoning controls;
- physical-resolution comparison residuals and separated remainders;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no free/current/local-HQCD matrix, projected identity, JMY Wilson/bilocal, soft, physical-renormalization, one-loop TMD, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a direct contact inferred from two C53 vertices, a contact with arbitrary qg support, an inverse denominator replaced by a propagating energy denominator, a post-hoc Hermitianized matrix, a qg missing loop mislabeled zero, a counterterm coefficient fitted to cancel the bare block, or a block assembly that rederives C58 as the complete source-derived instantaneous-fermion operator.
