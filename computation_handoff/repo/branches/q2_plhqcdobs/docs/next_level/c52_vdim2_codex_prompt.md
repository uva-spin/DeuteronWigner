# C52/VDIM2 Codex Work Package

## Title

**Executable source-component decomposition for the canonical vertex: exact symbolic coefficients, per-entry mass/transverse outputs, dimensionally homogeneous colorless component matrices, and recomposition closure**

## Authoritative baseline

Start from the clean local C51/VERTEX2 fail-closed completion commit:

```text
d074e45e68f04994a4fc8b7979b33d0a99fc0c42
```

Its immediate scientific parent is:

```text
ad3adeda99ab1115d07284a9c502c5959f08b6e4
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor ad3adeda99ab1115d07284a9c502c5959f08b6e4 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY

C51_VERTEX_DIMENSIONAL_ASSEMBLY_INCOMPLETE
```

and the exact C51 findings:

```text
C50 evaluator independence from C47 raw tuple values:
    proved statically;
    proved with runtime sentinel poisoning;

C50 executable return values:
    combined pminus_GeV;
    combined m2_GeV2;

C50 named component information:
    metadata only;

missing:
    executable per-entry component values;
    exact symbolic component coefficients;
    a source-derived homogeneous component-matrix decomposition;

C51 consequence:
    no colorless component matrix;
    no complete colorless vertex;
    no SU(3)/triplet insertion;
    no physical emission matrix;
    no adjoint;
    no matrix-free vertex action.
```

Verify these statements from the committed C51 records rather than relying on this prompt.

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
    C47 CM-clean qg total-color-triplet module

canonical convention:
    C50 finite-cell color-stripped P^- kernel
    M^2 = 2 P^+ P^- - P_perp^2
    L symbolic
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

All 3,618 C47 raw canonical tuple values remain immutable diagnostic-only data and are forbidden as physical numerical inputs.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact purpose

C52 resolves only the dimensional/component interface obstruction exposed by C51.

C50 derived a valid combined arbitrary-mode canonical matrix element, but its executable API does not expose the source-owned terms whose sum produces that value. C52 must promote the source decomposition from prose/metadata into executable mathematics.

C52 must create:

```text
an exact source-component basis for the C50 canonical kernel;

executable symbolic coefficient objects for every component;

executable per-basis-pair component evaluations for P^- and M^2;

a typed dimensional signature for every coefficient, primitive
matrix element, and completed component;

dimensionally homogeneous color-stripped component matrices at
all physical resolutions;

an exact symbolic assembly rule for the complete color-stripped
canonical vertex;

entrywise and matrix-level proof that the component sum reproduces
the existing C50 combined evaluator;

independent component-level holdouts, unit tests, parameter tests,
and raw-tuple-independence tests;

a complete C53 physical-vertex assembly contract.
```

C52 must not insert SU(3) color into a final physical vertex matrix.

C52 must not construct the triplet emission matrix, absorption adjoint, or full matrix-free physical vertex action.

The strongest allowed status is:

```text
C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY
```

When that gate passes, the exact next package is:

> **C53/VERTEX2 — exhaustive physical-basis evaluation, exact SU(3)/triplet insertion, physical emission-matrix assembly, independent matrix-free action, and adjoint closure**

---

# 2. Scientific boundary

C52 is:

```text
canonical-component specific;
color stripped;
source-derived through C43/C45/C47/C50;
symbolically typed;
dimensionally homogeneous;
physical-basis exhaustive at the component level;
coupling factored;
deterministic;
validation only.
```

C52 is not:

```text
a numerical decomposition inferred from the combined evaluator;
a fit in quark mass, bHO, L, or momentum;
a finite-difference separation of unnamed terms;
a promotion of C47 raw tuple values;
a final SU(3) vertex;
a free or instantaneous Hamiltonian package;
a JMY Wilson or bilocal-TMD package;
a one-loop calculation;
a proton or ART25 calculation.
```

Do not infer components by evaluating the combined function at specially chosen parameter values and solving a linear system. Such evaluations may be holdouts only after the component formulas have been derived independently from the source expression.

---

# 3. Nonnegotiable authority chain

Every executable component must descend through:

```text
locked primary-source canonical QCD interaction
    -> C43 project-convention operator term
    -> C50 plane-wave operator decomposition
    -> C50 finite-cell state normalization
    -> C50 P^- to M^2 conversion
    -> explicit component symbolic formula
    -> C45/C47 physical-basis projection
    -> C52 per-entry component evaluator
    -> C52 color-stripped component matrix.
```

For every component retain:

```text
component ID;
primary-source locator;
C43 action-term ID;
C50 derivation ID;
operator ordering;
helicity tensor;
transverse rank;
explicit mass dependence;
explicit transverse-momentum/derivative dependence;
longitudinal-fraction dependence;
finite-cell normalization;
symbolic L, P^+, bHO, and mass powers;
P^- dimensional signature;
M^2 dimensional signature;
selection rule;
phase convention;
basis-projection formula;
generator-code hash;
runtime-object hash.
```

The following are forbidden as component authority:

```text
the combined C50 numerical output;
a C50 metadata label by itself;
a C47 raw tuple value;
a component obtained by subtraction from the combined result;
a component obtained by fitting parameter dependence;
a representative holdout reused for another basis pair;
a hand-selected bHO or mass factor inserted to repair units.
```

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_action_derivation_manifest.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json

docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_cm_factorization_report.json
docs/next_level/c47_physical_basis_comparison_maps.json

docs/next_level/c50_plane_wave_operator_derivation.json
docs/next_level/c50_finite_volume_state_normalization.json
docs/next_level/c50_finite_box_pminus_kernel.json
docs/next_level/c50_pminus_dimensional_ledger.json
docs/next_level/c50_pminus_to_m2_derivation.json
docs/next_level/c50_canonical_component_decomposition.json
docs/next_level/c50_transverse_rank_dimensional_closure.json
docs/next_level/c50_arbitrary_mode_vertex_evaluator.json
docs/next_level/c50_basis_projection_validation.json
docs/next_level/c50_unit_covariance_report.json
docs/next_level/c50_regulator_scaling_report.json
docs/next_level/c50_c51_vertex_assembly_contract.json
docs/next_level/c50_readiness_report.json

docs/next_level/c51_implementation_report.md
docs/next_level/c51_input_fidelity_audit.json
docs/next_level/c51_raw_tuple_independence_report.json
docs/next_level/c51_missing_calculation_specification.md
```

Use actual repository filenames when they differ. Do not invent an absent artifact.

Create:

```text
docs/next_level/c52_derivation_authority_manifest.json
docs/next_level/c52_input_fidelity_audit.json
```

---

# 5. Freeze the component vocabulary from the source

Read the exact C50 component decomposition.

Do not assume that the source components are literally named:

```text
MASS
TRANSVERSE
```

even though C50 metadata may use those shorthand labels.

Construct the authoritative component list from the actual source-derived operator terms.

Every component must correspond to one additive term before basis projection and before numerical parameter evaluation.

For each candidate term decide:

```text
INDEPENDENT_SOURCE_COMPONENT;
SHARED_SYMBOLIC_COEFFICIENT;
SUBTERM_NOT_SEPARATELY_GAUGE_OR_OPERATOR_MEANINGFUL;
EXACT_ZERO_AT_DECLARED_SCOPE;
ABSENT_BLOCKING.
```

Only `INDEPENDENT_SOURCE_COMPONENT` terms become component evaluators.

Terms that must remain combined for operator-level reasons must be represented by one common component rather than artificially split.

Create:

```text
docs/next_level/c52_component_vocabulary.json
docs/next_level/c52_component_scope_decision.json
```

A positive gate requires no required `ABSENT_BLOCKING` term.

---

# 6. Executable symbolic algebra contract

Implement executable symbolic coefficient objects rather than descriptive strings.

An acceptable implementation may use:

```text
a content-addressed SymPy expression;
or
a project-native immutable symbolic-expression AST with exact rational
powers and deterministic evaluation.
```

The object must support:

```text
canonical serialization;
free-symbol inventory;
exact rational coefficients;
complex phases;
addition and multiplication;
substitution;
unit/dimension evaluation;
numerical evaluation;
symbolic differentiation where relevant;
expression hashing;
equivalence testing under simplification.
```

At minimum the symbol registry must audit:

```text
quark mass or common mass-IR parameter;
P^+;
L;
bHO;
longitudinal fractions;
transverse momenta or dimensionless HO variables;
helicity/polarization phases;
any source-owned normalization constants.
```

Do not introduce a symbol absent from the C50 derivation.

Create:

```text
docs/next_level/c52_symbol_registry.json
docs/next_level/c52_symbolic_expression_contract.json
```

---

# 7. Factor each component into coefficient and primitive

For each source-owned component \(c\), derive an exact factorization of the form

\[
V_c^{(-)}(\beta,\alpha)
=
S_c^{(-)}(\mathcal P)\,
I_c(\beta,\alpha;\mathcal P_{\rm basis}),
\]

and

\[
V_c^{(M^2)}(\beta,\alpha)
=
S_c^{(M^2)}(\mathcal P)\,
I_c(\beta,\alpha;\mathcal P_{\rm basis}),
\]

or the exact more general factorization required by the source.

Here:

```text
S_c:
    executable symbolic coefficient;

I_c:
    executable source-derived basis primitive;
```

A component may require a finite sum of primitives, but each term must be explicit and count-once.

The factorization must identify:

```text
which transverse momentum or derivative factor belongs in S_c;
which power of bHO comes from dimensionless HO variables;
which mass factor is explicit;
which factors belong to finite-cell state normalization;
which factors belong to the TM/CM transformation;
which factors belong to the spinor/polarization tensor.
```

Do not transfer a factor between \(S_c\) and \(I_c\) merely to make dimensions convenient. Any alternative factoring must be proved equivalent.

Create:

```text
docs/next_level/c52_component_factorization.json
docs/next_level/c52_component_primitive_contract.json
```

---

# 8. Dimensional type system

Extend or supersede the C50 dimensional ledger with executable types.

For every symbol, primitive, coefficient, component value, and sum track:

```text
power of mass;
power of L;
power of P^+;
power of bHO;
formal regulator signature;
operator type:
    P_MINUS_COMPONENT
    M2_COMPONENT
    DIMENSIONLESS_PRIMITIVE;
component transverse rank;
complex phase type.
```

Require:

```text
every completed P^- component has the same operator-level mass dimension;

every completed M^2 component has mass dimension two;

all components summed into one matrix have identical formal regulator
and symbolic-factor signatures after common factors are extracted;

no entry-dependent unit signature survives.
```

Create:

```text
docs/next_level/c52_dimensional_type_system.json
docs/next_level/c52_component_dimensional_audit.json
```

The evaluator must reject a component sum before numerical evaluation when the signatures are incompatible.

---

# 9. Component-wise \(P^-\!\to M^2\) conversion

Apply the proved C50 conversion to each source component separately.

For each component record:

```text
P^- expression;
fixed-total-P^+ factor;
off-diagonal P_perp^2 status;
state-normalization factor;
M^2 expression;
conversion residual.
```

If the conversion is a common multiplication by \(2P^+\), prove that it acts identically on every component.

If a component has a distinct \(P_\perp^2\) contribution, represent it explicitly rather than absorbing it into metadata.

Create:

```text
docs/next_level/c52_component_pminus_to_m2_map.json
docs/next_level/c52_component_conversion_validation.json
```

---

# 10. Descendant arbitrary-mode component API

Create a new descendant API, for example:

```python
evaluate_canonical_vertex_components(
    incoming_q_basis_id,
    outgoing_qg_basis_id,
    resolution,
    symbolic_parameters,
) -> CanonicalVertexComponentEvaluation
```

The return object must contain:

```text
ordered component records;
exact symbolic coefficient per component;
primitive value per component;
P^- component value;
M^2 component value;
units and dimensional signature;
selection-rule or exact-zero reason;
source ancestry;
combined P^- value;
combined M^2 value.
```

The existing C50 combined evaluator remains immutable as a historical API.

The descendant API must be derived from the source formulas, not implemented by calling C50 once and splitting its result.

Allowed exact-zero statuses:

```text
ZERO_BY_HELICITY_SELECTION;
ZERO_BY_OAM_SELECTION;
ZERO_BY_LONGITUDINAL_SELECTION;
ZERO_BY_SOURCE_COMPONENT_IDENTITY;
ZERO_BY_BASIS_ORTHOGONALITY.
```

Create:

```text
docs/next_level/c52_component_evaluator_api.json
docs/next_level/c52_component_evaluator_validation.json
```

---

# 11. Recomposition against the C50 combined evaluator

Use the C50 combined evaluator strictly as an independent descendant holdout.

For every tested basis pair require:

\[
\sum_c V_c^{(-)}(\beta,\alpha)
=
V_{\rm C50}^{(-)}(\beta,\alpha),
\]

and

\[
\sum_c V_c^{(M^2)}(\beta,\alpha)
=
V_{\rm C50}^{(M^2)}(\beta,\alpha).
\]

Test:

```text
all C50 frozen holdouts;
all C51 attempted holdouts;
every exact nonzero operator-component class;
both quark helicities;
both gluon helicities;
small and large x_g;
nontrivial intrinsic OAM;
massless and finite-mass points;
at least two diagnostic parameter substitutions;
a deterministic broad physical-basis sample;
the full admitted physical-basis domain when computationally practical.
```

The parameter substitutions are validation only. They may not define the decomposition.

Create:

```text
docs/next_level/c52_recomposition_report.json
docs/next_level/c52_combined_evaluator_holdout_report.json
```

Any unexplained recomposition residual blocks readiness.

---

# 12. Direct component-level independent checks

For each source component provide at least two routes among:

```text
direct plane-wave source expression;
coordinate-space field-mode integration;
momentum-space HO/TM projection;
good-component reduced spinor route;
full four-component spinor route;
analytic low-mode integral;
independent quadrature.
```

The exact pair of routes may differ by component.

The combined C50 evaluator does not count as one of the two component-level derivations.

Create:

```text
docs/next_level/c52_component_independent_checks.json
```

---

# 13. Exhaustive component-domain ledger

Reuse the exact physical basis-pair domain and selection rules from C51.

Every pair/component combination receives one status:

```text
PRESELECTION_FORBIDDEN_EXACT;
COMPONENT_EXACT_ZERO;
COMPONENT_NONZERO;
COMPONENT_EVALUATOR_UNAVAILABLE_BLOCKING;
DUPLICATE_COMPONENT_BLOCKING.
```

Report for every resolution:

```text
Cartesian basis-pair count;
component-domain count;
preselection count;
exact-zero component count;
nonzero component count;
unavailable count;
duplicate count.
```

The positive gate requires:

```text
unavailable = 0;
duplicate = 0.
```

Create:

```text
docs/next_level/c52_component_domain_ledger.json
docs/next_level/c52_component_count_once_report.json
```

---

# 14. Assemble color-stripped component matrices

For every source-owned component and every resolution, assemble a sparse color-stripped matrix:

\[
\widehat V_{\rm kin}^{(c)}.
\]

Each component matrix must have:

```text
one component ID;
one source identity;
one dimensional signature;
one symbolic coefficient contract;
one primitive-matrix unit;
one basis ordering;
one coupling power.
```

Store separately:

```text
the primitive matrix;
the symbolic coefficient;
the evaluated diagnostic matrix at frozen nonphysical test parameters,
when needed for numerical validation.
```

Do not freeze an unfixed physical parameter into the authoritative matrix.

Construct the symbolic color-stripped assembly:

\[
\widehat V_{\rm kin}^{(M^2)}
=
\sum_c
S_c^{(M^2)}
\widehat I_c.
\]

C52 may create this **color-stripped symbolic matrix family**.

C52 must not insert SU(3) or the triplet isometry.

Required checks:

```text
component sparse action versus direct component evaluator;
symbolic sum versus direct C50 combined evaluator;
uniform M^2 dimensions;
common symbolic-L signature;
basis-order consistency;
count-once closure.
```

Create:

```text
docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_colorless_symbolic_vertex.json
docs/next_level/c52_colorless_component_validation.json
```

---

# 15. Independent matrix-free colorless action

Implement:

```python
apply_colorless_vertex_components(
    vector_q,
    resolution,
    symbolic_parameters,
)
```

that:

```text
enumerates admitted basis pairs;
calls the new component evaluator;
accumulates each component separately;
returns component qg vectors and their exact sum.
```

It must not multiply by stored component matrices.

Compare sparse and matrix-free component actions on:

```text
basis vectors;
deterministic complex superpositions;
random normalized complex vectors;
all physical resolutions;
multiple diagnostic parameter substitutions.
```

Create:

```text
docs/next_level/c52_colorless_matrix_free_report.json
```

---

# 16. Raw-tuple independence

Retain the C51 static and poisoning guards.

Strengthen them so that:

```text
all C47 raw canonical tuple values may be replaced by NaN;
all C47 raw tuple component metadata may be altered;
the C52 source-derived component evaluator and matrices remain unchanged.
```

C47 basis identities and TM/CM transformations remain legitimate inputs.

Create:

```text
docs/next_level/c52_raw_tuple_independence_report.json
```

---

# 17. Unit and parameter covariance

Run component-level and summed tests under:

```text
GeV/MeV conversion;
symbolic L scaling or cancellation;
fixed-x P^+ rescaling;
bHO basis transformation;
quark-mass rescaling;
massless limit;
Fourier phase;
helicity phase;
coordinate/momentum route;
historical factor-of-two negative control.
```

Require:

```text
each component scales according to its source-derived coefficient;

the component sum scales as the C50 combined evaluator;

dimensionless residuals are invariant;

no component changes its declared unit across entries.
```

Create:

```text
docs/next_level/c52_component_unit_covariance_report.json
docs/next_level/c52_symbolic_parameter_validation.json
```

---

# 18. Physical-resolution comparison

Use the C47 comparison maps on every color-stripped component matrix.

Evaluate:

\[
R_{qg}\,
\widehat V^{(c)}_{r'}\,
P_q
\quad\text{versus}\quad
\widehat V^{(c)}_r.
\]

Separate:

```text
nonnested longitudinal remainder;
transverse truncation remainder;
CM-projection remainder;
symbolic-coefficient remainder;
normalization remainder;
numerical error.
```

Also compare the complete symbolic colorless sum.

Do not tune component coefficients to improve these comparisons.

Create:

```text
docs/next_level/c52_component_comparison_report.json
docs/next_level/c52_component_remainder_ledger.json
```

---

# 19. C53 physical-vertex assembly contract

Define the unique contract by which C53 will:

```text
consume the C52 color-stripped component matrices and symbolic coefficients;

construct the exact SU(3) emission tensor;

apply the frozen 24 x 3 triplet isometry;

assemble the physical emission matrix;

generate absorption only as the adjoint;

implement an independent physical matrix-free route;

run full color, count-once, unit, holdout, and comparison tests.
```

Specify:

```text
component ordering;
symbol substitution;
basis ordering;
units;
coupling factoring;
color insertion point;
triplet phase;
exact-zero semantics;
error/remainder propagation.
```

Create:

```text
docs/next_level/c52_c53_vertex_assembly_contract.json
```

---

# 20. Deterministic runtime bundles

For every resolution produce content-addressed bundles containing:

```text
symbol registry;
component symbolic expressions;
component-domain ledger;
primitive component matrices;
symbolic coefficient records;
diagnostic evaluated component matrices;
symbolic colorless vertex family;
component matrix-free metadata;
holdout and recomposition records;
comparison-map execution blocks.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c52_vdim2/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
nnz;
primitive units;
coefficient dimensional signature;
coupling power;
basis-order hash;
expression hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c52_numerical_object_inventory.json
```

All objects must regenerate byte-for-byte.

---

# 21. End-to-end source-to-component test

Implement an end-to-end test that begins from the C43/C45/C47/C50 source contracts—not from C50 combined values or C47 raw tuples.

It must:

```text
derive the component vocabulary;
construct executable symbolic coefficients;
construct component primitives;
apply component-wise P^- to M^2 conversion;
evaluate arbitrary physical basis pairs;
recompose the C50 combined evaluator as a holdout;
assemble component matrices;
compare sparse and matrix-free component actions;
run unit/parameter and comparison tests;
reproduce every hash.
```

It must fail when:

```text
a component is produced by subtracting from the combined C50 value;
a component coefficient is stored only as text;
a symbolic coefficient is fitted from parameter probes;
a mass or bHO factor is inserted without source ancestry;
a component is omitted or duplicated;
two components with different units are summed;
the combined C50 result is used as a primitive input;
a C47 raw tuple value is consumed;
the component-wise M^2 conversion is skipped;
a runtime hash changes.
```

---

# 22. Focused mutation tests

Create at least **224 focused live mutations** of actual component formulas, symbolic coefficients, dimensional types, domain records, or matrices.

Include mutations of:

```text
component ID;
source ancestry;
operator-component boundary;
symbolic coefficient;
mass power;
L power;
P^+ power;
bHO power;
transverse rank;
helicity tensor;
phase;
primitive value;
P^- to M^2 factor;
exact-zero reason;
component count;
duplicate component;
component matrix entry;
matrix-free accumulation;
recomposition sum;
comparison map;
expression hash;
runtime-array hash.
```

Every mutation must fail a concrete source, dimension, recomposition, count-once, matrix-free, unit, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 23. Readiness gate

Issue:

```text
C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY
```

only when:

```text
the full C51 baseline reproduces;
C50 and C51 raw-tuple independence remains intact;
the source component vocabulary is complete;
every component has an executable symbolic coefficient;
every component has an executable basis primitive;
component-wise P^- and M^2 outputs exist;
all component outputs are dimensionally homogeneous;
the component sum reproduces C50 independently;
component-level independent checks pass;
the exhaustive component-domain ledger has no unavailable or duplicate row;
color-stripped component matrices exist at all resolutions;
the symbolic colorless vertex family is complete;
sparse and independent matrix-free component actions agree;
unit and symbolic-parameter covariance passes;
physical-resolution comparisons execute;
the C53 assembly contract is complete;
runtime bundles reproduce byte-for-byte;
the end-to-end source-to-component test passes.
```

Do not issue:

```text
C52_SOURCE_DERIVED_PHYSICAL_CANONICAL_VERTEX_READY;
C52_COLOR_TRIPLET_VERTEX_READY;
C52_VERTEX_ADJOINT_READY;
C52_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C52_JMY_WILSON_MATRIX_VALIDATED;
C52_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 24. Exact no-go branches

## A. Source component formulas remain incomplete

```text
C52_SOURCE_COMPONENT_FORMULAS_INCOMPLETE
```

Next:

> **C53/COMP1 — exact canonical operator-term decomposition and component formula completion**

## B. Executable symbolic coefficients remain incomplete

```text
C52_SYMBOLIC_COEFFICIENT_CONTRACT_INCOMPLETE
```

Next:

> **C53/SYM1 — immutable executable symbolic algebra and coefficient completion**

## C. Component dimensional closure fails

```text
C52_COMPONENT_UNIT_CLOSURE_FAILED
```

Next:

> **C53/UDIM — source-derived mass, transverse, finite-cell, and invariant-mass dimensional closure**

## D. Component recomposition fails

```text
C52_COMPONENT_RECOMPOSITION_FAILED
```

Next:

> **C53/RECOMP — component boundary, phase, normalization, and count-once correction**

## E. Component evaluator domain remains incomplete

```text
C52_COMPONENT_DOMAIN_INCOMPLETE
```

Next:

> **C53/DOMAIN2 — complete arbitrary-mode component evaluator and physical-domain closure**

## F. Component matrices and symbolic assembly close

```text
C52_SOURCE_DERIVED_VERTEX_COMPONENT_ASSEMBLY_READY
```

Next:

> **C53/VERTEX2 — exact SU(3)/triplet physical canonical-vertex assembly and adjoint closure**

---

# 25. Required deliverables

Create at least:

```text
docs/next_level/c52_implementation_report.md
docs/next_level/c52_api.md
docs/next_level/c52_derivation_authority_manifest.json
docs/next_level/c52_input_fidelity_audit.json

docs/next_level/c52_component_vocabulary.json
docs/next_level/c52_component_scope_decision.json
docs/next_level/c52_symbol_registry.json
docs/next_level/c52_symbolic_expression_contract.json

docs/next_level/c52_component_factorization.json
docs/next_level/c52_component_primitive_contract.json
docs/next_level/c52_dimensional_type_system.json
docs/next_level/c52_component_dimensional_audit.json

docs/next_level/c52_component_pminus_to_m2_map.json
docs/next_level/c52_component_conversion_validation.json
docs/next_level/c52_component_evaluator_api.json
docs/next_level/c52_component_evaluator_validation.json

docs/next_level/c52_recomposition_report.json
docs/next_level/c52_combined_evaluator_holdout_report.json
docs/next_level/c52_component_independent_checks.json

docs/next_level/c52_component_domain_ledger.json
docs/next_level/c52_component_count_once_report.json

docs/next_level/c52_colorless_component_matrices.json
docs/next_level/c52_colorless_symbolic_vertex.json
docs/next_level/c52_colorless_component_validation.json
docs/next_level/c52_colorless_matrix_free_report.json

docs/next_level/c52_raw_tuple_independence_report.json
docs/next_level/c52_component_unit_covariance_report.json
docs/next_level/c52_symbolic_parameter_validation.json

docs/next_level/c52_component_comparison_report.json
docs/next_level/c52_component_remainder_ledger.json
docs/next_level/c52_c53_vertex_assembly_contract.json

docs/next_level/c52_numerical_object_inventory.json
docs/next_level/c52_readiness_report.json
docs/next_level/c52_source_sufficiency_decision.json
docs/next_level/c52_no_go_decision_tree.json
docs/next_level/c52_missing_calculation_specification.md
docs/next_level/c52_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/vdim2/
```

or the repository-equivalent package.

Add focused tests for:

```text
component vocabulary;
symbolic coefficients;
dimensional types;
component evaluator;
component-wise conversion;
recomposition;
component-domain count once;
colorless component matrices;
independent matrix-free action;
raw-tuple independence;
unit/parameter covariance;
resolution comparison;
end-to-end source-to-component reconstruction.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON, symbolic expressions, and runtime arrays must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C52 is complete only when:

1. The full C51 baseline reproduces.
2. The C51 no-go remains explicit.
3. The C50 combined evaluator remains unchanged.
4. The C43 action, C45 modes, and C47 basis remain unchanged.
5. C40 remains method-oracle only.
6. C47 raw tuple values remain diagnostic-only.
7. Static and poisoning tests prove raw-tuple independence.
8. No component is inferred by subtraction from the combined result.
9. No component is fitted from parameter probes.
10. The source-owned component vocabulary is explicit.
11. Every independent component has a source locator and operator meaning.
12. Components that cannot be separated physically remain combined.
13. Every symbolic coefficient is executable.
14. Symbolic expressions serialize deterministically.
15. Free symbols are source owned.
16. Every component has a primitive evaluator.
17. Coefficient/primitive factorization is source derived.
18. Every P^- component has the correct common operator dimension.
19. Every M^2 component has mass-squared dimension.
20. Formal regulator signatures remain distinct from mass dimension.
21. Component-wise P^- to M^2 conversion is explicit.
22. No element-dependent unit signature remains.
23. The descendant component evaluator returns actual component values.
24. Exact-zero reasons are typed and tested.
25. Component sums reproduce the C50 combined evaluator.
26. Component-level independent routes agree.
27. The exhaustive component-domain ledger closes.
28. Unavailable and duplicate component counts are zero.
29. Color-stripped component matrices exist at all resolutions.
30. The symbolic colorless assembly is complete.
31. No SU(3) or triplet physical matrix is assembled.
32. Sparse and independent matrix-free colorless actions agree.
33. GeV/MeV covariance passes.
34. Symbolic \(L\), \(P^+\), \(b_{\rm HO}\), mass, Fourier, and helicity checks pass.
35. The historical factor-of-two negative control fails as required.
36. Physical-resolution comparison diagnostics execute.
37. The C53 assembly contract is complete.
38. Runtime bundles contain executable expressions and actual arrays.
39. End-to-end reconstruction passes.
40. At least 224 focused live mutations are detected.
41. No physical color vertex or adjoint is claimed.
42. No free, instantaneous, constrained, boundary, or zero-mode matrix is claimed complete.
43. No JMY Wilson or bilocal TMD matrix is created.
44. No physical counterterm coefficient is solved.
45. No one-loop coefficient or matching kernel is created.
46. No proton TMD or ART25 bridge is created.
47. No fit, inference, process, or production route is created.
48. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
49. `MSHT20_REP/` remains untouched and outside Git.
50. The working tree is clean except for the pre-existing untracked directory.
51. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken source-component identity, executable symbolic coefficients, dimensional homogeneity, independent recomposition, or raw-tuple independence to open the gate.

---

# 27. Final Codex response

Report:

- full starting and final commits;
- exact C43/C45/C47/C50/C51 inputs consumed;
- input-fidelity classifications;
- authoritative source component IDs and meanings;
- symbolic coefficient expressions and free-symbol inventories;
- coefficient/primitive factorizations;
- dimensional signatures for every component;
- component-wise P^- and M^2 conversion residuals;
- component evaluator outputs and exact-zero classifications;
- recomposition residuals against C50;
- independent component-level check residuals;
- component-domain counts, unavailable counts, duplicates, and count-once status;
- color-stripped component-matrix shapes, nnz, primitive units, and symbolic coefficients;
- complete symbolic colorless-vertex contract;
- sparse/matrix-free component-action residuals;
- raw-tuple poisoning results;
- unit, symbolic-\(L\), \(P^+\), \(b_{\rm HO}\), mass, Fourier, helicity, and factor-of-two checks;
- physical-resolution comparison residuals and separated remainders;
- runtime expression and array hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no SU(3)/triplet physical vertex, adjoint, remaining local-QCD matrices, JMY Wilson/bilocal matrix, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe metadata component names, a numerical subtraction of the combined evaluator, parameter-fitted pieces, component matrices with inconsistent units, or a colorless symbolic family as the completed physical canonical vertex.
