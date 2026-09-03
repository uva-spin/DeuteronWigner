# C57/IFREG Codex Work Package

## Title

**Field-level finite-HO regulator for the instantaneous-fermion self-induced-inertia contraction: projected gauge-field algebra, corresponding-propagating-graph truncation, contracted virtual-gluon mode collection, shell projectors, and physical-basis embedding**

## Authoritative baseline

Start from the clean local C56/IFNORM Branch-B completion commit:

```text
1b49803a7a08d12feb5caca80f4c18b0aab795b6
```

Its immediate scientific parent is:

```text
12796e04f81158bc90da96cb27d29b33eea6e08e
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 12796e04f81158bc90da96cb27d29b33eea6e08e HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C53_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY

C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE

C56_IFNORM_FINITE_HO_REGULATOR_INCOMPLETE
```

and the exact C56 result:

```text
retained source objects:
    exact C55 b-dagger a a-dagger b monomial;
    exact gluon commutator;
    perturbative light-front normal-ordering vacuum;
    BPP requirement to retain the one-pair self-induced-inertia
    contraction;

BPP regulator:
    explicit DLCQ momentum-space self-induced-inertia sum;

C45/C47 status:
    normalized one-particle HO functions and physical CM-clean qg
    bases exist;
    no field-level finite-HO virtual-gluon projector exists;
    no operator-identical DLCQ-to-HO conversion exists;

selected C56 plan:
    IFNORM-UNAVAILABLE;

not created:
    contracted mode collection;
    self-induced-inertia mode sum;
    q or qg contraction matrix;
    subtraction;
    counterterm direction or coefficient;
    direct qg contact;
    C53 sequential substitute.
```

Verify every identity from the committed C56 records rather than relying on this prompt.

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
    K = 9/2, 11/2, 13/2
    Nmax = 8, 10, 12
    bHO = 0.40, 0.45, 0.50 GeV

physical basis:
    C47 x-weighted intrinsic/CM qg basis
    exact CM-ground projection
    exact total-color triplet

canonical local vertex:
    C53 source-derived physical q <-> qg operator
    read-only
    its numerical values are not part of the C57 regulator definition
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

C56 established that the missing object is not the self-induced-inertia formula. It is the **finite-basis contraction projector**.

The following statements must remain distinct:

```text
C45 ONE-PARTICLE HO BASIS EXISTS

    C45 defines normalized longitudinal and transverse one-particle
    modes.

C47 EXTERNAL PHYSICAL qg BASIS EXISTS

    C47 defines an x-weighted, many-body, CM-clean, color-triplet
    qg space.

FIELD-LEVEL VIRTUAL-GLUON PROJECTOR EXISTS

    A projector acting on the gluon field expansion determines the
    commutator kernel used when the a a-dagger pair is contracted.

CORRESPONDING-PROPAGATING INTERMEDIATE PROJECTOR EXISTS

    A projector onto the intermediate qg states retained by the same
    Hamiltonian truncation determines which instantaneous graphs have
    corresponding propagating graphs.

DLCQ-TO-HO CONVERSION EXISTS

    A finite transformation relates the BPP/Tang--Brodsky--Pauli
    momentum regulator to the selected HO regulator with an explicit
    inverse or remainder.
```

The first two do not imply any of the last three.

C57 must decide where the regulator acts and in which order the operations occur:

```text
field projection;
Hamiltonian/Fock projection;
normal ordering;
commutator contraction;
physical-basis projection.
```

These operations need not commute at finite truncation.

C57 may define a new project-specific finite-HO field regulator when it is transparently derived from source-qualified fields, basis functions, Fock truncation, and projector algebra. It may not declare that regulator to be BPP's DLCQ regulator or a continuum-equivalent regulator without a proved conversion.

---

# 2. Exact purpose

C57 resolves only the finite-HO regulator-definition obstruction.

C57 must produce:

```text
an exact source hierarchy for field, Fock-space, and graph-selection
truncation;

a complete audit of projection-versus-normal-ordering operation order;

one selected regulator plan;

a source-derived longitudinal virtual-gluon projector;

a source-derived transverse HO virtual-gluon projector;

the complete one-gluon field-mode collection at each resolution;

the corresponding second-quantized projected gauge field;

the finite-rank projected commutator kernel;

shell-resolved and longitudinal-mode-resolved subprojectors;

a source-derived corresponding-propagating qg intermediate-state
projector where required by the selected plan;

an exact relation between the field projector, intermediate projector,
C47 external physical qg basis, and C53 canonical support;

a zero-mode and residual-boundary regulator contract;

a DLCQ-to-HO conversion audit and visible finite-cutoff remainder;

projector comparison diagnostics across physical resolutions;

a read-only C58/IFNORM2 import contract.
```

C57 must not evaluate the self-induced-inertia mode sum.

C57 must not construct:

```text
a q-sector self-induced-inertia matrix;
a qg-sector self-induced-inertia matrix;
a subtraction;
a mass or metric counterterm direction;
the direct qg instantaneous contact;
the complete instantaneous-fermion operator;
the local HQCD polynomial;
a one-loop TMD or matching coefficient.
```

The strongest allowed status is:

```text
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
```

When that gate passes, the exact next package is:

> **C58/IFNORM2 — execute the self-induced-inertia contraction mode sum, q/qg sector lift, bare/subtraction/counterterm typing, and independent matrix action using the immutable C57 field regulator**

---

# 3. Scientific scope

The regulated one-gluon field space has the abstract form:

\[
\mathcal G_R
=
\mathcal K_{g,R}
\otimes
\mathcal H_{\perp,g,R}
\otimes
\mathbb C^2_{\lambda_g}
\otimes
\mathbb C^8_{\mathrm{adj}},
\]

but the factors and cutoff correlations must be derived rather than assumed.

C57 must determine whether the finite regulator is:

```text
a universal one-gluon field projector;

a fixed-total-K projector;

a conditional projector depending on the external quark mode;

a qg intermediate-state projector rather than a factorized gluon
projector;

or an exact finite conversion of the BPP DLCQ regulator.
```

A conditional or pair-space projector is scientifically acceptable when it follows from the selected Hamiltonian truncation and is named honestly. It must not be mislabeled as a universal field projector.

C57 must retain separately:

```text
ordinary positive longitudinal gluon modes;

the excluded exact k_g = 0 mode;

residual-boundary modes or functionals;

physical transverse polarizations;

adjoint color;

one-particle HO shells;

many-body Nmax restrictions;

CM projection;

triplet projection;

canonical-reachability restrictions.
```

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_inverse_derivative_contract.json
docs/next_level/c43_zero_mode_contract.json
docs/next_level/c43_boundary_prescription_decision.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_transverse_mode_manifest.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_zero_mode_projection_contract.json
docs/next_level/c45_numerical_object_inventory.json

docs/next_level/c47_qg_longitudinal_partition_manifest.json
docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_many_body_truncation_contract.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_physical_basis_validation.json
docs/next_level/c47_physical_basis_comparison_maps.json
docs/next_level/c47_numerical_object_inventory.json

docs/next_level/c53_su3_convention_manifest.json
docs/next_level/c53_triplet_image_equivalence.json
docs/next_level/c53_triplet_color_intertwiner.json
docs/next_level/c53_physical_entry_ancestry.json
docs/next_level/c53_numerical_object_inventory.json
docs/next_level/c53_readiness_report.json

docs/next_level/c55_normal_ordering_contract.json
docs/next_level/c55_operator_monomial_ledger.json
docs/next_level/c55_contact_propagating_count_once.json
docs/next_level/c55_physical_block_classification.json

docs/next_level/c56_implementation_report.md
docs/next_level/c56_derivation_authority_manifest.json
docs/next_level/c56_primary_source_manifest.json
docs/next_level/c56_source_role_matrix.json
docs/next_level/c56_source_sufficiency_matrix.json
docs/next_level/c56_contraction_identity.json
docs/next_level/c56_normal_ordering_reference.json
docs/next_level/c56_contraction_regulator_plan.json
docs/next_level/c56_regulator_plan_decision.json
docs/next_level/c56_missing_calculation_specification.md
docs/next_level/c56_readiness_report.json
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c57_derivation_authority_manifest.json
docs/next_level/c57_input_fidelity_audit.json
```

---

# 5. Primary-source hierarchy

Reuse the C43--C56 source locks.

Acquire and hash-lock the official arXiv PDF and source archive for:

```text
arXiv:2504.07162v1
    Li, Lappi, Zhao, Salgado,
    Scattering and gluon emission of physical quarks in a
    SU(3) colored field
```

Audit Appendix B and its references for:

```text
the self-induced-inertia operator;

the rule that an instantaneous graph is retained only when the
corresponding propagating graph contributes in the truncated theory;

the finite-volume mode convention;

the transverse regulator;

the sector-dependent mass-renormalization interpretation;

the exact role of the mass counterterm.
```

This source uses a different finite transverse representation unless an exact audit proves otherwise. Classify each usable statement narrowly.

Identify and hash-lock the exact Tang--Brodsky--Pauli primary source cited for the truncation rule. The expected candidate is:

```text
A. C. Tang, S. J. Brodsky, H.-C. Pauli,
Discretized light-cone quantization:
formalism for quantum electrodynamics,
Phys. Rev. D 44, 1842 (1991).
```

Verify the exact bibliographic identity and equation locators.

Reuse the source-locked BLFQ basis authorities, including:

```text
arXiv:0905.1411;
arXiv:1311.2980;
arXiv:1911.10762;
arXiv:2405.16995;
```

at their exact scopes.

Reuse or acquire, for method comparison only:

```text
arXiv:0801.4507
    Fock-sector-dependent renormalization;

arXiv:1402.4195
    finite-basis QED and mass renormalization;

arXiv:1404.6234
    BLFQ regulator dependence and an explicitly omitted
    self-energy sector.
```

Classify source roles as:

```text
ACTION_AND_COMMUTATOR_AUTHORITY;

DLCQ_REGULATOR_AUTHORITY;

CORRESPONDING_PROPAGATING_GRAPH_TRUNCATION_AUTHORITY;

BLFQ_ONE_PARTICLE_BASIS_AUTHORITY;

BLFQ_MANY_BODY_TRUNCATION_AUTHORITY;

SECTOR_RENORMALIZATION_METHOD_COMPARISON;

REGULATOR_CONVERSION_METHOD_COMPARISON;

NOT_OPERATOR_REGULATOR_IDENTICAL.
```

No source may be promoted beyond its exact operator, gauge, state-space, and regulator scope.

Create:

```text
docs/next_level/c57_primary_source_manifest.json
docs/next_level/c57_source_role_matrix.json
docs/next_level/c57_source_sufficiency_matrix.json
```

---

# 6. Freeze construction and holdouts

Before choosing a plan, freeze:

```text
the exact C55/C56 a a-dagger contraction identity;

the normal-ordering vacuum;

the C43 field expansion and canonical commutator;

the C45 longitudinal mode convention;

the C45 transverse HO functions and phases;

the C47 many-body Nmax and CM rules;

the C47 physical q and qg basis orders;

the C53 triplet isometry and canonical-support ancestry;

the exact zero-mode and residual-boundary policies;

the physical resolution records.
```

Freeze holdouts:

```text
the lowest positive gluon longitudinal mode;

the highest candidate longitudinal mode;

the lowest HO shell;

the highest candidate HO shell;

both gluon helicities;

all adjoint colors or one exact color-completeness holdout;

one mode allowed by the one-particle HO cutoff but forbidden by the
many-body qg cutoff;

one mode allowed in the external qg basis but unreachable by the
canonical operator;

one mode canonically reachable but removed by CM projection;

one exact zero-mode candidate;

one projector-kernel coordinate-space value;

one momentum-space projector value;

one operation-order noncommutativity holdout;

one DLCQ-to-HO overlap holdout;

one adjacent-resolution projector comparison.
```

No failed holdout may be moved into construction.

Create:

```text
docs/next_level/c57_calculation_plan.json
docs/next_level/c57_holdout_plan.json
```

---

# 7. Projection and normal-ordering operation order

Compile the following operation sequences explicitly.

## 7.1 `FIELD_PROJECT_THEN_NORMAL_ORDER`

Define a regulated field:

\[
A_{\perp,R}
=
\Pi_{g,R} A_\perp,
\]

or the exact two-sided field-map equivalent, then normal order products of \(A_{\perp,R}\).

The contraction kernel is the finite-rank projector kernel.

## 7.2 `NORMAL_ORDER_THEN_FOCK_PROJECT`

Normal order the source field product before applying the retained-Fock-space projector to the Hamiltonian.

The commutator is the source commutator; the later Fock projection determines the retained operator block.

## 7.3 `CORRESPONDING_PROPAGATING_GRAPH_PROJECT`

Apply the Tang--Brodsky--Pauli graph-selection rule: retain the instantaneous contribution only on the intermediate-state support of the corresponding propagating graph in the same truncated theory.

## 7.4 `DLCQ_REGULATE_THEN_CONVERT_TO_HO`

Evaluate or define the BPP/TBP-regulated operator in its momentum regulator, then transform it to the HO representation through an exact finite conversion.

## 7.5 `OPERATION_ORDER_UNAVAILABLE`

No unique operation sequence is supported.

For every pair of nonidentical sequences, derive the formal difference. In particular, record:

\[
\mathcal N(\Pi A\,\Pi A)
-
\Pi\,\mathcal N(AA)\,\Pi,
\]

or the exact project expression, including the commutator-projector term.

Do not assume projection and normal ordering commute.

Create:

```text
docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_projection_normal_ordering_commutator.json
```

---

# 8. Regulator plans

Compile mutually exclusive regulator plans before generating a mode.

## 8.1 `IFREG-UNIVERSAL-PROJECTED-HO-FIELD`

Construct a universal one-gluon projector from the C45 field modes. Normal order the projected field.

This plan requires a source-derived longitudinal upper support and transverse shell cutoff independent of an external basis pair.

## 8.2 `IFREG-FIXED-K-FOCK-PROJECTED-FIELD`

Define the regulated Hamiltonian at each fixed total \(K\) through a Fock-space projector. The effective contracted mode support may depend on the fixed sector and on the incoming quark mode.

This plan must name the result a fixed-\(K\) conditional regulator, not a universal field regulator.

## 8.3 `IFREG-CORRESPONDING-PROPAGATING-SUPPORT`

Use the source-qualified graph-selection rule. Construct the intermediate qg support from the same source canonical operator and the same Fock/basis truncation, without using C53 numerical values or energy denominators.

The C53 nonzero support may be a holdout, not the construction authority.

## 8.4 `IFREG-DLCQ-LONGITUDINAL-HO-TRANSVERSE-HYBRID`

Retain the source DLCQ longitudinal regulator and define a new project transverse HO regulator. This is a new hybrid regulator and must not be called BPP DLCQ or C45/C47 external regulation without qualification.

## 8.5 `IFREG-EXACT-DLCQ-TO-HO-CONVERSION`

Use an exact finite conversion with an inverse or a declared nonzero remainder.

## 8.6 `IFREG-UNAVAILABLE`

No unique finite-HO contraction regulator is supported.

Select exactly one primary plan.

Do not choose by matrix size, smoothness, or expected cancellation with a future counterterm.

Create:

```text
docs/next_level/c57_field_regulator_plan.json
docs/next_level/c57_regulator_plan_decision.json
```

---

# 9. Longitudinal field-mode projector

Derive the longitudinal one-gluon mode space from:

```text
the finite cell;
periodic nonzero gluon modes;
fixed total K where applicable;
positive quark modes;
the selected operation order;
the selected graph/Fock truncation.
```

Do not assume:

```text
1 <= k_g <= K;

1 <= k_g <= K - 1/2;

or

the set of k_g values appearing in external qg states
```

without derivation.

Construct the exact projector or conditional projector:

\[
\Pi^{\parallel}_{g,R}
=
\sum_{k_g\in\mathcal K_{g,R}}
|k_g\rangle\langle k_g|,
\]

or:

\[
\Pi^{\parallel}_{g,R|\alpha}
\]

when the support is external-state dependent.

Required checks:

```text
Hermiticity;

idempotence where the object is a true projector;

positive support;

zero-mode exclusion/control;

compatibility with total-K conservation;

compatibility with the corresponding-propagating support;

exact Fraction arithmetic;

basis-order hash.
```

Create:

```text
docs/next_level/c57_longitudinal_field_projector.json
docs/next_level/c57_longitudinal_projector_validation.json
```

---

# 10. Transverse HO field projector

Start from the exact C45 normalized two-dimensional HO modes.

Define the one-particle shell label:

\[
N_g=2n_g+|m_g|+1
\]

only if this is the committed C45 convention.

Determine the field-level transverse cutoff from the source/project contract.

Audit separately:

```text
one-particle shell cutoff;

many-body sum-of-quanta Nmax cutoff;

x-scaled intrinsic qg cutoff;

CM-ground projection;

canonical-reachability restriction.
```

Do not equate them.

Construct:

\[
\Pi^\perp_{g,R}
=
\sum_{\nu_\perp\in\mathcal H_{\perp,g,R}}
|\nu_\perp\rangle\langle\nu_\perp|,
\]

or the exact conditional/pair-space equivalent.

Resolve the oscillator-scale question:

```text
fixed one-particle bHO;

x_g-dependent one-particle scale;

intrinsic qg scale;

or a source-derived transformation among them.
```

Do not assign the C47 intrinsic scale directly to a field mode without proving the map.

Required checks:

```text
Hermiticity and idempotence;

rank and trace;

HO normalization;

coordinate/momentum Fourier equality;

shell decomposition;

rotational/OAM covariance;

scale and units;

direct quadrature;

relation to the C47 TM/Jacobi map.
```

Create:

```text
docs/next_level/c57_transverse_field_projector.json
docs/next_level/c57_transverse_projector_validation.json
```

---

# 11. Full one-gluon field projector

Construct the full field projector or typed conditional operator:

\[
\Pi_{g,R}
=
\Pi^{\parallel}_{g,R}
\otimes
\Pi^\perp_{g,R}
\otimes
I_{\lambda_g}
\otimes
I_{\mathrm{adj}},
\]

only when factorization is proved.

If longitudinal and transverse restrictions are correlated through the many-body truncation, store the nonfactorized projector explicitly.

Every mode record retains:

```text
k_g;

n_g and m_g;

HO shell;

gluon helicity;

adjoint color;

zero-mode status;

boundary identity;

normalization;

oscillator scale;

resolution;

mode hash;

regulator-plan ancestry.
```

Create:

```text
docs/next_level/c57_gluon_field_projector.json
docs/next_level/c57_gluon_field_projector_validation.json
```

---

# 12. Projected field and commutator kernel

Construct the projected transverse gauge field from the C43/C45 expansion.

Derive the exact finite-rank commutator:

\[
[a_{R,\nu},a^\dagger_{R,\nu'}]
=
(\Pi_{g,R})_{\nu\nu'},
\]

or the exact conditional/generalized relation.

In coordinate space, define the truncated completeness kernel:

\[
\Delta_{g,R}(x,y)
=
\sum_{\nu\in\mathcal G_R}
u_\nu(x)u_\nu^*(y),
\]

with all polarization, color, and normalization factors explicit.

Do not call:

\[
\Delta_{g,R}(x,y)
\]

a Dirac delta at finite truncation.

Required checks:

```text
canonical projected algebra;

projector-kernel Hermiticity;

reproducing property on the retained mode space;

failure outside the retained space;

coordinate/momentum equality;

equal-point shell decomposition;

color and polarization completeness;

symbolic-L behavior;

zero-mode separation.
```

Create:

```text
docs/next_level/c57_projected_field_expansion.json
docs/next_level/c57_projected_commutator_kernel.json
docs/next_level/c57_projected_commutator_validation.json
```

---

# 13. Corresponding-propagating intermediate projector

When required by the selected plan, construct the intermediate qg support from:

```text
the C43 canonical q -> qg operator;

C45 normalized modes;

C47 fixed-K, Nmax, TM/CM, and triplet basis;

exact source selection rules.
```

Do not use:

```text
C53 numerical matrix values;

C53 singular values;

a C53 energy denominator;

or C53-adjoint times C53.
```

The C53 entry-ancestry and nonzero-support records may be used only as independent holdouts.

Define:

\[
\Pi^{\mathrm{can}}_{qg,R}
\]

on the reachable intermediate qg subspace.

Report its relation to:

```text
the complete C47 physical qg projector;

the C53 canonical emission image;

the full product-color qg space;

the CM-excited qg space;

the anti-sextet and 15 color spaces.
```

Required checks:

```text
projector Hermiticity and idempotence;

rank;

K and Jz conservation;

CM-ground status;

triplet status;

canonical reachability;

source-selection count once;

agreement with C53 support as a holdout.
```

Create:

```text
docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_canonical_support_validation.json
```

---

# 14. Conditional contracted-mode support

If the selected plan is conditional on an incoming quark basis state, define:

\[
\mathcal G_R(\alpha)
\]

or a pair-space support:

\[
\mathcal I_R(\alpha)
\subset
\mathcal H_{qg,R}.
\]

Do not force a conditional support into a universal tensor-product projector.

For every incoming quark state report:

```text
candidate gluon modes;

allowed intermediate qg states;

rejected modes and exact reasons;

support rank;

dependence on quark longitudinal mode;

dependence on quark HO shell;

dependence on helicity and Jz;

dependence on CM projection;

dependence on color/triplet reachability.
```

Test whether two quark states with identical conserved quantum numbers but different HO labels have the same or different support.

Create:

```text
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_conditional_support_validation.json
```

---

# 15. Second-quantized Fock-space projector

Construct the retained Fock-space projector:

\[
\mathbb P_R
=
\mathbb P_{q,R}
\oplus
\mathbb P_{qg,R},
\]

with the exact physical or intermediate spaces required by the selected plan.

Derive the relation among:

```text
projected field algebra;

projected Hamiltonian;

normal-ordered instantaneous operator;

corresponding propagating graph;

external physical basis.
```

Explicitly test whether:

\[
\mathbb P_R A_\perp \mathbb P_R
\]

is sufficient to define the contraction or whether a separate intermediate-space map is required.

Create:

```text
docs/next_level/c57_fock_space_projector.json
docs/next_level/c57_fock_field_compatibility_report.json
```

---

# 16. DLCQ-to-HO conversion audit

Preserve the BPP/TBP DLCQ regulator as a distinct source object.

Construct the exact overlap map between the source transverse momentum modes or cells and the C45 HO modes when the source supplies enough information:

\[
U_{\mathrm{HO}\leftarrow\mathrm{DLCQ}}.
\]

Report:

```text
source momentum-domain cutoff;

source UV/IR regulator;

source cell or quadrature measure;

HO shell cutoff;

overlap-matrix shape;

rank;

singular values;

forward map;

candidate inverse;

round-trip residual;

unmapped source subspace;

unmapped HO subspace;

operator conversion remainder.
```

At finite cutoff, do not assume a rectangular momentum cutoff and an HO-shell projector are unitarily equivalent.

Allowed decisions:

```text
EXACT_FINITE_CONVERSION;

ISOMETRIC_CONVERSION_WITH_VISIBLE_REMAINDER;

METHOD_COMPARISON_ONLY;

CONVERSION_UNAVAILABLE.
```

A method comparison cannot open the positive regulator gate by itself.

Create:

```text
docs/next_level/c57_dlcq_ho_conversion_contract.json
docs/next_level/c57_dlcq_ho_conversion_report.json
```

---

# 17. Projector shell decomposition

Construct orthogonal shell projectors:

\[
\Pi_{g,R}
=
\sum_s \Pi_{g,R}^{(s)}
\]

for the selected field or conditional regulator.

Keep separately:

```text
longitudinal-mode projectors;

transverse HO-shell projectors;

helicity projectors;

color projectors;

zero-mode controls;

boundary controls.
```

Required checks:

```text
orthogonality;

sum to the complete selected projector;

rank recomposition;

kernel recomposition;

basis-order independence;

no missing or duplicate mode.
```

Create:

```text
docs/next_level/c57_shell_projector_manifest.json
docs/next_level/c57_shell_projector_validation.json
```

---

# 18. Materialized contracted field-mode collection

Materialize the complete mode collection or conditional support tables at all physical resolutions.

Report:

```text
total field modes;

total conditional pair states where applicable;

counts by k_g;

counts by HO shell;

counts by m_g;

counts by helicity;

counts by adjoint color;

zero-mode controls;

CM-excluded states;

canonical-unreachable states;

triplet-excluded states.
```

No contraction coefficient is evaluated in C57.

Create:

```text
docs/next_level/c57_contracted_field_mode_manifest.json
docs/next_level/c57_contracted_field_mode_validation.json
```

---

# 19. External-basis embedding

Define exact maps among:

```text
the field-mode space;

the raw qg product basis;

the intrinsic/CM qg basis;

the CM-ground qg basis;

the total-color-triplet qg basis;

the canonically reachable qg subspace.
```

Construct explicit embeddings, projections, or typed nonfactorized relations.

Do not treat an external qg basis row as a field mode.

Required checks:

```text
Gram-metric adjoint relations;

normalization;

K and Jz bookkeeping;

CM projection;

triplet projection;

canonical support;

rank and nullity;

basis-rotation covariance.
```

Create:

```text
docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_external_basis_embedding_validation.json
```

---

# 20. Zero-mode and residual-boundary regulator contract

The exact positive gluon mode collection excludes \(k_g=0\), but that does not assign all zero-mode effects to zero.

For the field regulator, classify:

```text
ordinary positive mode;

exact longitudinal zero mode;

residual transverse-gauge mode;

global Gauss-law zero mode;

boundary mode or functional;

constrained polarization contribution.
```

Each receives:

```text
included in primary field projector;

excluded with source proof;

retained as separate control;

represented by a boundary functional;

or ABSENT_BLOCKING.
```

The projected commutator kernel and corresponding-propagating projector must use the same zero-mode policy.

Create:

```text
docs/next_level/c57_zero_mode_boundary_regulator.json
docs/next_level/c57_zero_mode_boundary_validation.json
```

---

# 21. Regulator fingerprints

C57 does not evaluate a self-energy, but it must expose the regulator geometry.

Report for each resolution:

```text
longitudinal support;

transverse shell support;

effective HO UV and IR diagnostic scales;

projector rank;

equal-point kernel trace;

conditional-support rank distribution;

CM-removal fraction;

canonical-reachability fraction;

triplet fraction;

zero-mode and boundary controls.
```

The quantities:

```text
bHO*sqrt(Nmax);

bHO/sqrt(Nmax)
```

remain diagnostics unless the source defines exact cutoffs.

Do not claim a continuum trajectory from the three correlated physical points.

Create:

```text
docs/next_level/c57_regulator_fingerprint_report.json
```

---

# 22. Physical-resolution comparison maps

Construct comparison maps between the selected field/intermediate projectors at adjacent physical resolutions.

The longitudinal spaces and HO scales are nonnested. Do not claim exact inclusion.

Evaluate:

\[
R_g\Pi_{g,R'}P_g
\quad\text{versus}\quad
\Pi_{g,R},
\]

or the exact conditional/pair-space equivalent.

Separate:

```text
longitudinal nonnesting;

HO-shell truncation;

bHO scale change;

CM projection;

canonical-support change;

triplet representation;

zero-mode/boundary change;

numerical error.
```

Do not tune the projector to improve the comparison.

Create:

```text
docs/next_level/c57_projector_comparison_maps.json
docs/next_level/c57_projector_comparison_report.json
docs/next_level/c57_comparison_remainder_ledger.json
```

---

# 23. Count-once and provenance ledger

Every retained field or intermediate state must have one ancestry path.

Report:

```text
candidate modes;

retained modes;

exactly excluded modes;

zero-mode controls;

conditional duplicates;

shell duplicates;

basis-map duplicates;

missing mode identities;

blocking identities.
```

Keep distinct:

```text
field-mode support;

intermediate qg support;

external qg basis support;

canonical-emission support;

future self-induced-inertia contribution support.
```

A state may appear in more than one relation, but it may not be counted twice inside one projector.

Create:

```text
docs/next_level/c57_mode_ancestry_ledger.json
docs/next_level/c57_count_once_report.json
```

---

# 24. Independence and poisoning controls

Prove that C57 is unchanged when:

```text
all C40 arrays are poisoned;

all historical C47 canonical tuple values and metadata are poisoned;

all C50 combined values are poisoned;

all C53 canonical matrix values are poisoned;

all C56 unavailable placeholder values are poisoned;

ART25 files are inaccessible.
```

C53 basis, triplet, and support identities may remain available as holdouts.

The build must fail when:

```text
the C43 field expansion changes;

the C45 HO mode hash changes;

the C47 many-body truncation rule changes;

the normal-ordering vacuum changes;

the selected operation order changes without supersession;

the selected regulator plan changes without supersession;

the zero-mode policy changes;

the field projector loses Hermiticity or idempotence;

a conditional projector is relabeled universal.
```

Create:

```text
docs/next_level/c57_isolation_report.json
```

---

# 25. C58/IFNORM2 import contract

Define the immutable contract by which C58 will consume:

```text
the selected regulator-plan ID;

the operation-order contract;

the complete field-mode or conditional intermediate support;

longitudinal and transverse projectors;

shell projectors;

projected commutator kernel;

zero-mode and boundary statuses;

field-to-qg embedding maps;

comparison maps;

basis-order and mode hashes;

count-once and provenance ledgers.
```

C58 must verify all hashes before evaluating one contraction contribution.

C58 may not:

```text
change the regulator;

restrict the mode set after seeing the sum;

insert a subtraction;

use C53 values;

or import the BPP finite sum without the selected conversion.
```

Create:

```text
docs/next_level/c57_c58_import_contract.json
```

---

# 26. Deterministic runtime bundles

For every resolution produce content-addressed bundles containing:

```text
longitudinal projector;

transverse HO projector;

full field or conditional projector;

projected commutator kernel;

shell projectors;

materialized mode collection;

corresponding-propagating projector where applicable;

field-to-qg embeddings;

zero-mode/boundary records;

comparison-map blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c57_ifreg/
```

Commit an inventory containing:

```text
runtime path;

shape;

dtype;

nnz;

units;

projector type;

conditional-domain identity;

regulator-plan ID;

operation-order ID;

basis-order hash;

mode-set hash;

array hash;

generator command.
```

Create:

```text
docs/next_level/c57_numerical_object_inventory.json
```

All JSON and arrays must regenerate byte-for-byte.

---

# 27. End-to-end source-to-projector test

Implement an end-to-end test that starts from the C43/C45/C47/C55/C56 contracts—not from prebuilt C57 arrays.

It must:

```text
load and classify the primary sources;

derive the operation-order alternatives;

select the regulator plan;

construct the longitudinal projector;

construct the transverse HO projector;

construct the full or conditional field/intermediate projector;

construct the projected field and commutator kernel;

construct shell projectors;

construct the corresponding-propagating support where required;

construct field-to-qg embeddings;

apply zero-mode and boundary policies;

run DLCQ-to-HO conversion diagnostics;

run comparison, count-once, and poisoning tests;

reproduce all hashes.
```

It must fail when:

```text
the external qg basis is silently used as the field-mode collection;

a one-particle Nmax cutoff is substituted for the many-body cutoff
without proof;

the intrinsic qg oscillator scale is assigned to a field mode without
a derived map;

projection and normal ordering are assumed to commute;

the corresponding-propagating rule uses C53 numerical values;

the BPP DLCQ sum is relabeled HO regulated;

a finite momentum cutoff is declared unitarily equivalent to a finite
HO shell without a conversion proof;

a zero mode is deleted;

a conditional projector is serialized as universal;

a mode is omitted or duplicated;

a runtime hash changes.
```

---

# 28. Focused mutation tests

Create at least **224 focused live mutations** of actual source decisions, projectors, modes, kernels, or maps.

Include mutations of:

```text
operation order;

regulator-plan ID;

longitudinal support;

k_g upper bound;

zero-mode inclusion;

HO shell rule;

Nmax relation;

bHO scale;

x_g scale map;

projector entry;

projector rank;

projector idempotence;

mode normalization;

helicity identity;

adjoint color identity;

projected commutator;

kernel phase;

shell assignment;

canonical-reachability status;

CM projection;

triplet projection;

DLCQ-to-HO overlap;

conditional-support domain;

embedding map;

comparison map;

mode hash;

runtime-array hash.
```

Every mutation must fail a concrete source, algebra, projector, normalization, support, zero-mode, count-once, comparison, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 29. Readiness gate

Issue:

```text
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
```

only when:

```text
the full C56 baseline reproduces;

the source hierarchy is complete;

the field/Fock/graph truncation distinction is explicit;

projection and normal-ordering operation order is selected;

one regulator plan is selected;

the longitudinal projector is source derived;

the transverse HO projector is source derived;

the field scale and Nmax relation are resolved;

the full field or conditional projector exists at every resolution;

the projected field expansion exists;

the finite-rank commutator kernel closes;

shell projectors recompose exactly;

the complete mode collection is materialized;

the corresponding-propagating support exists when required;

its construction is independent of C53 numerical values;

the relation to the C47 external basis is explicit;

the DLCQ-to-HO decision has an exact status and visible remainder;

zero-mode and boundary statuses are complete;

comparison maps execute with separated remainders;

mode ancestry and count-once ledgers close;

duplicate, missing, and blocking required identities are zero;

poisoning controls pass;

the C58 import contract is complete;

runtime bundles reproduce byte-for-byte;

the end-to-end source-to-projector test passes.
```

Do not issue:

```text
C57_SOURCE_DERIVED_IFERM_NORMAL_ORDERING_READY;

C57_SELF_INDUCED_INERTIA_MATRIX_READY;

C57_SOURCE_DERIVED_INSTANTANEOUS_FERMION_READY;

C57_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;

C57_PHYSICAL_MASS_RENORMALIZATION_SOLVED;

C57_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 30. Exact no-go branches

## A. Operation order remains ambiguous

```text
C57_IFREG_OPERATION_ORDER_INCOMPLETE
```

Next:

> **C58/IFORDER — projection, normal-ordering, commutator, and Fock-projection ordering closure**

## B. Longitudinal field support remains incomplete

```text
C57_IFREG_LONGITUDINAL_PROJECTOR_INCOMPLETE
```

Next:

> **C58/IFLONG — fixed-cell gluon mode support, total-K relation, and zero-mode closure**

## C. Transverse HO field projector remains incomplete

```text
C57_IFREG_TRANSVERSE_HO_PROJECTOR_INCOMPLETE
```

Next:

> **C58/IFHO — one-particle shell, many-body Nmax, x-scaled basis, and HO projector closure**

## D. Corresponding-propagating support remains incomplete

```text
C57_IFREG_PROPAGATING_SUPPORT_INCOMPLETE
```

Next:

> **C58/IFPROP — Tang--Brodsky--Pauli graph-selection and canonical intermediate-space completion**

## E. Field-to-external-basis embedding remains incomplete

```text
C57_IFREG_EXTERNAL_EMBEDDING_INCOMPLETE
```

Next:

> **C58/IFEMBED — field, product-qg, intrinsic/CM, triplet, and canonical-support map completion**

## F. DLCQ-to-HO conversion is required but incomplete

```text
C57_IFREG_DLCQ_HO_CONVERSION_INCOMPLETE
```

Next:

> **C58/IFCONV — finite regulator overlap, inverse/remainder, and operator-conversion completion**

## G. Zero-mode or boundary regulator remains incomplete

```text
C57_IFREG_ZERO_MODE_BOUNDARY_INCOMPLETE
```

Next:

> **C58/IFZERO3 — field-projector zero-mode, residual-gauge, and boundary completion**

## H. Field regulator closes

```text
C57_SOURCE_DERIVED_IFERM_FIELD_REGULATOR_READY
```

Next:

> **C58/IFNORM2 — execute the self-induced-inertia contraction**

---

# 31. Required deliverables

Create at least:

```text
docs/next_level/c57_implementation_report.md
docs/next_level/c57_api.md
docs/next_level/c57_derivation_authority_manifest.json
docs/next_level/c57_input_fidelity_audit.json

docs/next_level/c57_primary_source_manifest.json
docs/next_level/c57_source_role_matrix.json
docs/next_level/c57_source_sufficiency_matrix.json
docs/next_level/c57_calculation_plan.json
docs/next_level/c57_holdout_plan.json

docs/next_level/c57_operation_order_contract.json
docs/next_level/c57_projection_normal_ordering_commutator.json
docs/next_level/c57_field_regulator_plan.json
docs/next_level/c57_regulator_plan_decision.json

docs/next_level/c57_longitudinal_field_projector.json
docs/next_level/c57_longitudinal_projector_validation.json
docs/next_level/c57_transverse_field_projector.json
docs/next_level/c57_transverse_projector_validation.json
docs/next_level/c57_gluon_field_projector.json
docs/next_level/c57_gluon_field_projector_validation.json

docs/next_level/c57_projected_field_expansion.json
docs/next_level/c57_projected_commutator_kernel.json
docs/next_level/c57_projected_commutator_validation.json

docs/next_level/c57_corresponding_propagating_projector.json
docs/next_level/c57_canonical_support_validation.json
docs/next_level/c57_conditional_mode_support.json
docs/next_level/c57_conditional_support_validation.json

docs/next_level/c57_fock_space_projector.json
docs/next_level/c57_fock_field_compatibility_report.json

docs/next_level/c57_dlcq_ho_conversion_contract.json
docs/next_level/c57_dlcq_ho_conversion_report.json

docs/next_level/c57_shell_projector_manifest.json
docs/next_level/c57_shell_projector_validation.json
docs/next_level/c57_contracted_field_mode_manifest.json
docs/next_level/c57_contracted_field_mode_validation.json

docs/next_level/c57_field_to_qg_embedding.json
docs/next_level/c57_external_basis_embedding_validation.json
docs/next_level/c57_zero_mode_boundary_regulator.json
docs/next_level/c57_zero_mode_boundary_validation.json

docs/next_level/c57_regulator_fingerprint_report.json
docs/next_level/c57_projector_comparison_maps.json
docs/next_level/c57_projector_comparison_report.json
docs/next_level/c57_comparison_remainder_ledger.json

docs/next_level/c57_mode_ancestry_ledger.json
docs/next_level/c57_count_once_report.json
docs/next_level/c57_isolation_report.json
docs/next_level/c57_c58_import_contract.json

docs/next_level/c57_numerical_object_inventory.json
docs/next_level/c57_readiness_report.json
docs/next_level/c57_source_sufficiency_decision.json
docs/next_level/c57_no_go_decision_tree.json
docs/next_level/c57_missing_calculation_specification.md
docs/next_level/c57_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/ifreg/
```

or the repository-equivalent package.

Add focused tests for:

```text
source roles;
operation order;
regulator-plan exclusion;
longitudinal projector;
transverse HO projector;
full/conditional projector;
projected commutator kernel;
shell decomposition;
corresponding-propagating support;
DLCQ-to-HO conversion audit;
field-to-qg embedding;
zero modes and boundary;
mode ancestry and count once;
poisoning isolation;
physical-resolution comparison;
end-to-end source-to-projector reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All JSON and runtime arrays must reproduce byte-for-byte.

---

# 32. Acceptance criteria

C57 is complete only when:

1. The full C56 baseline reproduces.
2. The C56 no-go remains explicit.
3. The exact C55/C56 contraction identity remains unchanged.
4. The C53 canonical vertex remains read-only.
5. The C43 action, C45 modes, and C47 physical basis remain unchanged.
6. C40 remains method-oracle only.
7. Historical C47 tuple values and metadata remain diagnostic-only.
8. No physical coupling or counterterm coefficient is chosen.
9. No arbitrary numerical \(L\) is introduced.
10. The exact primary source for the TBP truncation rule is identified.
11. arXiv:2504.07162 Appendix B is audited at its exact scope.
12. Its transverse regulator is not silently identified with HO.
13. Field, Fock-space, and graph-selection projectors remain distinct.
14. Projection and normal ordering are not assumed to commute.
15. One operation order is selected.
16. One regulator plan is selected.
17. A universal and a conditional projector are never conflated.
18. The longitudinal support is derived.
19. The transverse HO support is derived.
20. One-particle and many-body Nmax rules are not conflated.
21. The field oscillator scale is resolved.
22. The full field or conditional projector exists.
23. Every true projector is Hermitian and idempotent.
24. The projected field expansion exists.
25. The commutator is the finite projector kernel, not an asserted delta.
26. Coordinate- and momentum-space kernels agree.
27. Shell projectors are orthogonal.
28. Shells recompose the complete selected projector.
29. The mode collection includes every required longitudinal, HO, helicity, and color identity.
30. Exact zero modes remain separate controls.
31. No external qg basis is silently substituted for the field-mode set.
32. Corresponding-propagating support is derived where required.
33. That support does not use C53 numerical values.
34. C53 support agrees only as a holdout.
35. Field-to-qg embedding maps are explicit.
36. CM and triplet projections are retained.
37. No nontriplet or CM-excited remainder is silently removed.
38. The DLCQ-to-HO decision has a typed status.
39. A finite conversion remainder remains visible.
40. Regulator fingerprints are reported.
41. The three physical resolutions are not called a continuum trajectory.
42. Comparison maps retain all nonnested remainders.
43. Every mode/projector entry has complete ancestry.
44. Duplicate, missing, and blocking required identities are zero.
45. Static and runtime poisoning controls pass.
46. No self-induced-inertia mode sum is evaluated.
47. No q or qg contraction matrix is created.
48. No subtraction or counterterm direction is created.
49. No direct contact or complete instantaneous-fermion operator is created.
50. No free/current/local-HQCD matrix is created.
51. No JMY Wilson, bilocal TMD, soft, one-loop, matching, proton, ART25, fit, inference, process, or production object is created.
52. The C58 import contract is complete.
53. Runtime bundles contain actual projectors, kernels, mode tables, and maps.
54. End-to-end reconstruction passes.
55. At least 224 focused live mutations are detected.
56. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
57. `MSHT20_REP/` remains untouched and outside Git.
58. The working tree is clean except for the pre-existing untracked directory.
59. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken operation-order ownership, field-versus-Fock projector identity, longitudinal support, HO truncation, corresponding-propagating support, DLCQ-to-HO conversion, or zero-mode treatment to open the gate.

---

# 33. Final Codex response

Report:

- full starting and final commits;
- exact primary sources and role classifications;
- the audited TBP truncation rule and exact source locator;
- the audited arXiv:2504.07162 Appendix-B statements and regulator differences;
- selected operation order and rejected alternatives;
- selected regulator plan and rejected alternatives;
- longitudinal projector formulas, support, rank, and zero-mode status;
- transverse HO projector formulas, shell rule, scale, rank, and residuals;
- whether the full regulator is factorized, nonfactorized, or conditional;
- projected-field and commutator-kernel residuals;
- shell-projector ranks and recomposition residuals;
- materialized mode counts by longitudinal mode, shell, helicity, and color;
- corresponding-propagating projector rank and support decisions;
- C53 support holdout residuals;
- conditional-support distributions where applicable;
- field/Fock/external-qg embedding ranks and nullities;
- DLCQ-to-HO conversion status, rank, singular values, and remainder;
- zero-mode and boundary statuses;
- regulator fingerprints;
- physical-resolution comparison residuals and separated remainders;
- ancestry, duplicate, missing, and blocking counts;
- poisoning and isolation results;
- runtime array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no contraction sum, q/qg contraction matrix, subtraction, counterterm direction, direct contact, complete instantaneous-fermion operator, local-HQCD matrix, JMY Wilson/bilocal, soft, one-loop, matching, proton, ART25, fit, inference, process, or production object was created;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe the external qg basis as a field projector, a many-body Nmax rule as a one-particle HO cutoff, a conditional support as universal, a finite HO kernel as a Dirac delta, a momentum-box cutoff as HO-equivalent without conversion, or a C53 nonzero pattern as the source derivation of the regulator.
