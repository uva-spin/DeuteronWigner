# C50/VSRC Codex Work Package

## Title

**First-principles finite-volume canonical-vertex derivation: exact light-front convention map, normalized plane-wave \(q\!\to qg\) matrix element, \(P^-\!\to M^2\) conversion, Abelian BLFQ cross-checks, and a source-qualified arbitrary-mode evaluator**

## Authoritative baseline

Start from the clean local C49/VERTEX1 fail-closed completion commit:

```text
c940136ab9038d9bda91db21650c292a27927506
```

Its immediate scientific parent is:

```text
d237da980274a4d819b8881750fbbd189f0ef469
```

Before changing code, run and record:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor d237da980274a4d819b8881750fbbd189f0ef469 HEAD
```

The baseline is authoritative only when it contains and reproduces:

```text
C47_SOURCE_DERIVED_PHYSICAL_BASIS_ASSEMBLY_READY

C48_CANONICAL_VERTEX_ASSEMBLY_INCOMPLETE

C49_CANONICAL_SOURCE_CHAIN_INCOMPLETE
```

and the exact C49 audit:

```text
raw C47 tuples audited:
    3,618

raw tuple status:
    3,618 AMBIGUOUS_BLOCKING

source additions:
    arXiv:2503.21372v1
    arXiv:2401.03480v1

source decision:
    effective color-singlet hadron Hamiltonians with incompatible
    conventions and model/fitted terms;
    not regulator-identical authority for the C43/C45/C47
    open-triplet canonical matrix element.
```

Verify every value from the committed C49 records rather than relying on this prompt.

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

project light-front convention:
    v^\pm = (v^0 +/- v^3)/sqrt(2)
    v^2 = 2 v^+ v^- - v_perp^2
    M^2 = 2 P^+ P^- - P_perp^2

physical basis:
    C45/C47 half-integer-K trajectory
    K = 9/2, 11/2, 13/2
    L symbolic
    CM-clean color-triplet qg module
```

C40 remains:

```text
EXECUTABLE_METHOD_ORACLE_ONLY
```

The C47 raw canonical tuple tables remain immutable historical artifacts, but they are no longer permitted as authoritative numerical inputs to the physical canonical vertex.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Exact scientific correction

C49 established that no audited publication supplies the final custom object:

```text
the C43-normalized;
C45-mode-projected;
C47-CM-clean;
open-color-triplet;
finite-box;
q -> qg canonical matrix element.
```

That final matrix is project specific. It need not appear verbatim in a paper.

C50 must therefore distinguish two forms of authority:

## 1.1 Source authority

Primary sources must determine:

```text
the canonical QCD interaction operator;
the light-front gauge and field decomposition;
the field-mode expansions and canonical brackets;
the finite longitudinal box and boundary phases;
the one-particle state normalization;
the transverse HO and TM/Jacobi normalization;
the spinor and polarization conventions;
the open-color external-module interpretation;
the SU(3) generator normalization;
the invariant-mass convention.
```

## 1.2 Project derivation authority

The final finite-box matrix element may be a new project calculation when it is derived transparently from the source-qualified ingredients.

The acceptable chain is:

```text
source-qualified operator and modes
    -> explicit symbolic substitution
    -> finite-volume plane-wave matrix element
    -> convention conversion
    -> physical-basis projection formula
    -> independent cross-checks
    -> deterministic evaluator.
```

Do not require a publication to print the final C50 formula.

Do not call a formula source qualified merely because it resembles a published BLFQ model vertex.

Create the authority classes:

```text
PRIMARY_SOURCE_INPUT
PROJECT_DERIVED_FROM_SOURCE_INPUTS
ABELIAN_METHOD_CROSSCHECK
MODEL_HAMILTONIAN_COMPARISON_ONLY
AMBIGUOUS_HISTORICAL_ORACLE
ABSENT_BLOCKING
```

Every positive C50 formula must be either:

```text
PRIMARY_SOURCE_INPUT
```

or:

```text
PROJECT_DERIVED_FROM_SOURCE_INPUTS.
```

---

# 2. Exact purpose

C50 must derive an arbitrary-mode canonical-vertex evaluator from first principles.

It must produce:

```text
an exact convention map among the C43 project convention and
the convention of every comparison source;

a source-derived momentum-space canonical q-q-g operator;

normalized finite-volume one-quark and qg plane-wave states;

the complete finite-box color-stripped matrix element of P^-_qqg;

a machine-checkable dimensional decomposition into mass and
transverse-momentum structures;

the exact off-diagonal conversion from P^- to M^2;

a direct continuum/light-front splitting-amplitude oracle;

an Abelian QED/BLFQ convention cross-check;

a project-derived arbitrary-mode evaluator that consumes C45/C47
mode identities without consuming C47's ambiguous tuple values;

a frozen set of independently evaluated physical-basis matrix-element
holdouts for C51.
```

C50 must not assemble the complete 3,618-entry physical vertex matrix.

C50 must not insert the full SU(3)/triplet structure into a production vertex matrix, although it may validate the color factor separately.

The strongest allowed status is:

```text
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
```

When that gate passes, the exact next package is:

> **C51/VERTEX2 — exhaustive source-derived physical-basis tuple regeneration, exact SU(3)/triplet insertion, emission-matrix assembly, and adjoint closure**

---

# 3. Scientific boundary

C50 is:

```text
canonical-interaction specific;
finite-volume normalization specific;
convention-conversion specific;
arbitrary-mode evaluator specific;
source-first;
project-derivation explicit;
coupling-factored;
validation-only.
```

C50 is not:

```text
another search for a paper containing the final custom matrix;
a repair of the C47 raw tuple values;
a fit of vertex coefficients;
a physical alpha_s choice;
a complete local-HQCD matrix package;
an instantaneous-interaction package;
a JMY Wilson-line package;
a one-loop calculation;
a proton or ART25 calculation.
```

---

# 4. Mandatory inputs

Read completely:

```text
references/c43_light_front_qcd_gauge_action.tex

docs/next_level/c43_light_front_conventions.json
docs/next_level/c43_gauge_convention_map.json
docs/next_level/c43_action_derivation_manifest.json
docs/next_level/c43_hamiltonian_term_ledger.json
docs/next_level/c43_canonical_brackets.json
docs/next_level/c43_mode_expansion_contract.json
docs/next_level/c43_finite_basis_projection_contract.json

docs/next_level/c45_longitudinal_cell_contract.json
docs/next_level/c45_longitudinal_mode_manifest.json
docs/next_level/c45_transverse_ho_contract.json
docs/next_level/c45_light_front_spinor_contract.json
docs/next_level/c45_gluon_polarization_contract.json
docs/next_level/c45_spinor_polarization_overlap.json
docs/next_level/c45_colored_probe_plan.json
docs/next_level/c45_global_gauss_law_contract.json
docs/next_level/c45_qg_triplet_projector.json

docs/next_level/c47_x_scaled_coordinate_contract.json
docs/next_level/c47_qg_tm_transformation.json
docs/next_level/c47_cm_plan.json
docs/next_level/c47_physical_q_basis_manifest.json
docs/next_level/c47_physical_qg_basis_manifest.json
docs/next_level/c47_free_operator_normalization_contract.json
docs/next_level/c47_c48_matrix_assembly_interface.json

docs/next_level/c48_implementation_report.md
docs/next_level/c48_missing_calculation_specification.md

docs/next_level/c49_implementation_report.md
docs/next_level/c49_c47_tuple_semantics_audit.json
docs/next_level/c49_source_sufficiency_matrix.json
docs/next_level/c49_missing_calculation_specification.md
```

Use actual filenames when they differ. Do not invent an absent artifact.

Preserve the C47 raw tuple files byte-for-byte.

---

# 5. Primary-source hierarchy

Reuse the exact C43-C49 source locks.

The canonical QCD operator authority remains the C43 chain based on the source-locked light-front-QCD action.

Obtain and hash-lock official arXiv PDF and source archives, when not already present, for the following Abelian method and convention cross-checks:

```text
arXiv:1402.4195v1
    Electron g-2 in Light-Front Quantization

role:
    explicit BLFQ field expansions;
    discrete box normalization;
    canonical QED vertex operator;
    creation/annihilation normalization;
    warning concerning a historical factor-of-two error;
    convention comparison only.

arXiv:1110.0553
    Electron Anomalous Magnetic Moment in Basis Light-Front
    Quantization Approach

role:
    analytic HO/Talmi-Moshinsky vertex methodology;
    independent warning about the corrected interaction factor;
    method cross-check only.

arXiv:2405.16995
    Electron form factors in Basis Light-front Quantization

role:
    modern x-dependent transverse basis;
    finite-box longitudinal mode convention;
    explicit QED Hamiltonian and basis normalization;
    comparison to light-front perturbation theory;
    Abelian cross-check only.
```

These QED papers are not QCD color authority and their plus/minus convention must not be imported directly.

Audit one source-qualified continuum light-front \(q\to qg\) splitting-amplitude or light-front-wave-function formula as an independent helicity/kinematic cross-check. It need not share the finite-box regulator.

Classify the new sources as:

```text
ABELIAN_FINITE_BOX_NORMALIZATION_CROSSCHECK
ABELIAN_VERTEX_METHOD_CROSSCHECK
CONTINUUM_Q_TO_QG_HELICITY_CROSSCHECK
MODEL_HAMILTONIAN_COMPARISON_ONLY
```

Create:

```text
docs/next_level/c50_primary_source_manifest.json
docs/next_level/c50_source_role_matrix.json
docs/next_level/c50_derivation_authority_manifest.json
```

---

# 6. Freeze construction and holdouts

Before performing the derivation, freeze:

```text
the exact C43 canonical q-q-g operator;
the C43 project plus/minus convention;
the C45 box, Fourier, spinor, polarization, and HO phases;
the C47 CM-clean physical basis definitions;
the open-color external-module interpretation;
the SU(3) normalization;
the symbolic L policy;
the P^- and M^2 operator definitions.
```

Freeze holdouts that are not used to simplify the derivation:

```text
two helicity-conserving plane-wave points;
two helicity-changing plane-wave points;
one massless-quark limit;
one finite-mass point;
one nonzero transverse-momentum point in each independent direction;
one smallest-x_g point;
one largest-x_g point;
one exact-zero helicity/selection-rule point;
one C45 HO ground-state projection;
one nontrivial HO/TM projection;
one GeV/MeV unit-conversion point;
one symbolic-L point;
one Abelian-limit point;
one C47 raw-tuple comparison point from each |m_rel| class.
```

Create:

```text
docs/next_level/c50_calculation_plan.json
docs/next_level/c50_holdout_plan.json
```

---

# 7. Complete convention map

Build an exact map among:

```text
C43 project convention:
    v^\pm = (v^0 +/- v^3)/sqrt(2)
    p dot x = p^+ x^- + p^- x^+ - p_perp dot x_perp
    M^2 = 2 P^+ P^- - P_perp^2

the no-sqrt(2) convention used in relevant BLFQ QED papers:
    x^\pm = x^0 +/- x^3
    p dot x contains p^+ x^- / 2
    M^2 = P^+ P^- - P_perp^2

the convention of every continuum q->qg cross-check.
```

Derive explicitly:

```text
coordinate rescaling;
momentum rescaling;
delta-function rescaling;
box-length and mode-label mapping;
field normalization mapping;
creation/annihilation mapping;
P^- mapping;
M^2 mapping;
spinor and polarization mapping.
```

A quoted factor of two is not a conversion proof.

Machine-check:

```text
metric identities;
Fourier-phase equality;
canonical-bracket equality;
one-particle state-normalization equality;
free-dispersion equality.
```

Create:

```text
docs/next_level/c50_convention_map.json
docs/next_level/c50_convention_roundtrip_report.json
```

---

# 8. Re-derive the canonical momentum-space operator

Begin from the exact C43 interaction density.

Insert the C43/C45 source-normalized quark and gluon mode expansions symbolically.

Retain only the operator ordering that maps:

\[
|q\rangle \longrightarrow |qg\rangle.
\]

Derive the coefficient multiplying:

```text
b^\dagger_{q'} a^\dagger_g b_q
```

with all:

```text
longitudinal measures;
transverse measures;
spinor and polarization factors;
SU(3) generator left symbolic;
Fourier phases;
operator-order signs;
box-normalization factors.
```

Do not begin from the C47 tuple value.

Create an exact symbolic object:

```text
CanonicalQQGPlaneWaveKernel
```

with component decomposition into the actual C43 source-supported structures.

Create:

```text
docs/next_level/c50_plane_wave_operator_derivation.json
docs/next_level/c50_operator_ordering_report.json
```

---

# 9. Normalized finite-volume states

Construct the finite-box states directly from the C43/C45 canonical brackets:

\[
|q;\alpha\rangle,
\qquad
|qg;\beta\rangle.
\]

Derive their normalization rather than assuming continuum normalization.

Record:

```text
longitudinal mode normalization;
transverse basis normalization;
open-color label normalization;
helicity normalization;
qg product-state normalization;
CM-clean isometry normalization;
zero-mode domain.
```

Prove:

```text
one-quark orthonormality;
qg orthonormality;
compatibility of the plane-wave and HO basis normalizations;
compatibility of q and qg total-P^+ normalization.
```

Create:

```text
docs/next_level/c50_finite_volume_state_normalization.json
docs/next_level/c50_state_normalization_validation.json
```

---

# 10. Finite-box plane-wave \(P^-\) matrix element

Evaluate from first principles:

\[
\langle q(p',\lambda',c');g(k,h,a)|
P^-_{qqg}
|q(p,\lambda,c)\rangle.
\]

Perform the \(x^-\) and \(x_\perp\) integrals explicitly.

Derive:

```text
the longitudinal Kronecker delta;
the transverse momentum delta or finite-basis projection kernel;
every power of L;
every power of P^+;
every square-root state-normalization factor;
the spinor/polarization numerator;
the color tensor T^a_{c'c};
the uniform P^- mass dimension.
```

Keep \(L\) symbolic.

Separate the color-stripped result:

\[
\mathcal V^{(-)}_{\lambda'h;\lambda}(p',k;p)
\]

from the SU(3) tensor.

All nonzero helicity/OAM components must have one common operator dimension.

Create:

```text
docs/next_level/c50_finite_box_pminus_kernel.json
docs/next_level/c50_pminus_dimensional_ledger.json
docs/next_level/c50_pminus_validation.json
```

---

# 11. Derive the \(P^-\!\to M^2\) map

For the off-diagonal transition between fixed-total-momentum sectors, derive:

\[
\langle qg|M^2|q\rangle
\]

from:

\[
M^2=2P^+P^- - P_\perp^2.
\]

Prove separately:

```text
same total P^+ in the two sectors;
same total transverse-momentum/CM frame;
orthogonality of different Fock sectors under P_perp^2;
absence or presence of any off-diagonal P_perp^2 term;
state-normalization compatibility;
the exact factor of two in the C43 convention.
```

Implement two routes when possible:

```text
direct project-convention M^2 derivation;

P^- matrix element followed by the derived conversion.
```

Allowed decisions:

```text
C50_DIRECT_AND_CONVERTED_M2_EQUIVALENT
C50_PMINUS_TO_M2_ONLY
C50_DIRECT_M2_ONLY
C50_M2_CONVERSION_UNRESOLVED
```

Create:

```text
docs/next_level/c50_pminus_to_m2_derivation.json
docs/next_level/c50_pminus_to_m2_validation.json
```

---

# 12. Dimensional decomposition of mass and transverse structures

Express the plane-wave and \(M^2\) kernels as a sum of independently homogeneous components.

For example, only if derived from the source:

```text
mass-dependent helicity-flip structure;
transverse-momentum helicity structure;
other constrained canonical structure.
```

For every component record:

```text
spin/helicity tensor;
transverse rank;
explicit mass factors;
explicit transverse momentum factors;
longitudinal fractions;
operator dimension;
phase.
```

Demonstrate that the complete matrix element has uniform units independent of the later HO angular label.

This derivation must explain why the C47 raw tuples appeared to scale as:

```text
GeV^(1+|m_rel|)
```

without treating that raw declaration as authoritative.

Create:

```text
docs/next_level/c50_canonical_component_decomposition.json
docs/next_level/c50_transverse_rank_dimensional_closure.json
```

---

# 13. Project the arbitrary plane-wave kernel into the C45/C47 basis

Construct an evaluator:

```text
evaluate_canonical_vertex(
    incoming_q_basis_id,
    outgoing_qg_basis_id,
    resolution,
    symbolic_parameters
)
```

It must compute the matrix element from:

```text
the new C50 plane-wave kernel;
the C45 normalized HO functions;
the C47 x-scaled TM/Jacobi transform;
the C47 CM-ground projector;
the C47 physical basis isometries.
```

It must not consume the numerical value of any C47 raw canonical tuple.

The evaluator may consume C47 basis IDs and transformation matrices.

Evaluate all frozen holdouts and a deterministic sparse sample at every resolution.

Do not assemble the complete vertex matrix.

Create:

```text
docs/next_level/c50_arbitrary_mode_vertex_evaluator.json
docs/next_level/c50_basis_projection_validation.json
```

---

# 14. Independent cross-checks

## 14.1 Continuum light-front splitting amplitude

Compare the color-stripped C50 plane-wave kernel, after convention mapping, with a source-qualified continuum \(q\to qg\) light-front helicity amplitude.

Compare:

```text
helicity zeros;
relative phases;
mass terms;
transverse-momentum terms;
longitudinal-fraction dependence.
```

Do not compare finite-box normalization factors before removing/mapping them.

## 14.2 Abelian limit

Take:

```text
T^a -> 1;
open-color factor -> 1;
QCD self-interaction absent.
```

Map the C50 convention into the locked BLFQ QED convention.

Compare the finite-box vertex normalization and the \(P^-\)/\(M^2\) relation.

The QED source's historical factor-of-two correction must be an explicit negative control.

## 14.3 Direct coordinate-space integration

For frozen low-mode holdouts, evaluate the matrix element directly in coordinate space from the field modes.

## 14.4 Momentum-space integration

Evaluate the same holdouts through the momentum-space kernel and HO/TM projection.

Require independent agreement.

Create:

```text
docs/next_level/c50_continuum_splitting_crosscheck.json
docs/next_level/c50_abelian_blfq_crosscheck.json
docs/next_level/c50_coordinate_momentum_equivalence.json
```

---

# 15. Reclassify the C47 raw tuples

Preserve all 3,618 raw tuples and the C49 audit.

Do not attempt to repair them in place.

Compare each raw tuple only after the C50 evaluator exists.

Allowed comparison statuses:

```text
AGREES_AFTER_EXPLICIT_REFACTORIZATION
DIFFERS_BY_IDENTIFIED_OMITTED_FACTOR
DIFFERS_BY_CONVENTION_MAP
AMBIGUOUS_HISTORICAL_ORACLE
EXACT_ZERO_CONSISTENT
```

No raw tuple becomes physical authority through numerical agreement alone.

Create:

```text
docs/next_level/c50_c47_tuple_comparison.json
docs/next_level/c50_historical_tuple_status.json
```

A positive C50 gate does not require all raw tuples to agree. It requires the new source-derived evaluator to be complete and the differences to remain explicit.

---

# 16. Unit and regulator tests

Execute:

```text
GeV/MeV conversion;
symbolic-L scaling or cancellation;
P^+ rescaling with fixed x;
b_HO scaling under the exact basis transformation;
Fourier-phase reversal;
helicity-phase convention;
project/no-sqrt(2) convention round trip;
massless and finite-mass limits.
```

Dimensionless residuals must remain invariant.

Dimensional values must scale with their derived units.

Create:

```text
docs/next_level/c50_unit_covariance_report.json
docs/next_level/c50_regulator_scaling_report.json
```

---

# 17. C51 assembly contract

Define the unique contract by which C51 will:

```text
evaluate every allowed physical basis pair;
build the exhaustive new tuple table;
insert exact SU(3);
apply the 24 x 3 triplet isometry;
assemble the sparse emission matrix;
generate the absorption adjoint;
execute count-once and comparison-map tests.
```

The contract must specify:

```text
input basis IDs;
output units;
symbolic parameters;
coupling-power factoring;
selection-rule semantics;
zero-value semantics;
source ancestry;
error and remainder propagation;
matrix-free evaluation.
```

Create:

```text
docs/next_level/c50_c51_vertex_assembly_contract.json
```

---

# 18. Deterministic runtime bundle

Create a content-addressed runtime bundle containing:

```text
symbolic canonical operator components;
finite-box state-normalization tables;
plane-wave P^- kernel holdouts;
plane-wave M^2 kernel holdouts;
arbitrary-mode evaluator holdouts;
continuum splitting cross-checks;
Abelian BLFQ cross-checks;
coordinate/momentum integration holdouts;
unit and convention round-trip arrays.
```

Heavy arrays may remain outside Git under:

```text
data/runtime/c50_vsrc/
```

Commit an inventory with:

```text
runtime path;
shape;
dtype;
units;
symbolic-factor signature;
basis-order hash;
array hash;
generator command.
```

Create:

```text
docs/next_level/c50_numerical_object_inventory.json
```

---

# 19. End-to-end derivation test

Implement a test that starts from the C43 action and C45/C47 modes, not from C47 tuple values.

It must:

```text
load the source/convention chain;
derive the momentum-space operator coefficient;
construct finite-volume normalized states;
evaluate the P^- plane-wave kernel;
derive the M^2 kernel;
project frozen physical-basis holdouts;
execute continuum and Abelian cross-checks;
execute unit and regulator tests;
reproduce every hash.
```

It must fail when:

```text
a C47 raw tuple value is used as an input;
a model-hadron BLFQ vertex is substituted;
the no-sqrt(2) QED convention is imported without conversion;
the historical factor-of-two error is reintroduced;
L is fixed arbitrarily;
the P^- to M^2 factor is hard-coded;
the P_perp^2 decision is omitted;
a transverse momentum or mass factor is inserted for convenience;
the coordinate- and momentum-space routes disagree;
a runtime hash changes.
```

---

# 20. Focused mutations

Create at least **192 focused live mutations** of actual source expressions, convention maps, state normalizations, or evaluators.

Include mutations of:

```text
plus/minus rescaling;
Fourier factor of one-half;
box normalization;
creation/annihilation normalization;
spinor normalization;
polarization vector;
mass term;
transverse-momentum term;
helicity phase;
Kronecker delta;
P^+ factor;
factor of two in M^2;
P_perp^2 decision;
L power;
b_HO factor;
TM phase;
open-color normalization;
Abelian limit;
holdout basis ID;
runtime hash.
```

Every mutation must fail a concrete convention, dimensional, source, normalization, cross-check, or deterministic-reconstruction test.

Do not inflate the count with identifier-only dispatch.

---

# 21. Readiness gate

Issue:

```text
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
```

only when:

```text
the full C49 baseline reproduces;
the source/project-derivation distinction is explicit;
the complete convention map closes;
the canonical momentum-space operator is re-derived from C43;
the finite-volume states are normalized from C43/C45 brackets;
the plane-wave P^- matrix element is complete;
all nonzero P^- components have common operator units;
the P^- to M^2 conversion is derived;
all nonzero M^2 components have mass-squared units;
the arbitrary-mode evaluator is independent of C47 tuple values;
continuum splitting checks close at their scope;
the Abelian BLFQ cross-check closes after convention mapping;
coordinate- and momentum-space holdouts agree;
unit and regulator tests pass;
the C51 assembly contract is complete;
runtime objects reproduce byte-for-byte;
the end-to-end derivation test passes.
```

Do not issue:

```text
C50_PHYSICAL_CANONICAL_VERTEX_MATRIX_READY;
C50_COMPLETE_LOCAL_HQCD_SUBSTRATE_READY;
C50_INSTANTANEOUS_OPERATOR_VALIDATED;
C50_JMY_WILSON_MATRIX_VALIDATED;
C50_ONE_LOOP_MATCHING_VALIDATED.
```

---

# 22. Exact no-go branches

## A. The source action or mode normalization is still insufficient

```text
C50_PRIMARY_INPUT_CHAIN_INCOMPLETE
```

Next:

> **C51/SRC1 — targeted canonical action, field expansion, or finite-box normalization closure**

## B. The project/QED convention map does not close

```text
C50_LIGHT_FRONT_CONVENTION_MAP_INCOMPLETE
```

Next:

> **C51/CONV2 — exact sqrt(2), Fourier, state-normalization, and mass-operator convention closure**

## C. The finite-box plane-wave matrix element remains incomplete

```text
C50_FINITE_BOX_PMINUS_DERIVATION_INCOMPLETE
```

Next:

> **C51/PMINUS1 — direct canonical-operator insertion and finite-volume state-normalization completion**

## D. The \(P^-\!\to M^2\) map remains incomplete

```text
C50_PMINUS_TO_M2_DERIVATION_INCOMPLETE
```

Next:

> **C51/M2MAP2 — fixed-total-momentum invariant-mass conversion completion**

## E. The physical-basis evaluator remains incomplete

```text
C50_ARBITRARY_MODE_EVALUATOR_INCOMPLETE
```

Next:

> **C51/PROJ2 — HO/TM/CM projection of the source-derived plane-wave kernel**

## F. All source/convention gates close

```text
C50_CANONICAL_VERTEX_SOURCE_CONVENTION_READY
```

Next:

> **C51/VERTEX2 — exhaustive physical canonical-vertex matrix assembly**

---

# 23. Required deliverables

Create at least:

```text
docs/next_level/c50_implementation_report.md
docs/next_level/c50_api.md

docs/next_level/c50_primary_source_manifest.json
docs/next_level/c50_source_role_matrix.json
docs/next_level/c50_derivation_authority_manifest.json
docs/next_level/c50_calculation_plan.json
docs/next_level/c50_holdout_plan.json

docs/next_level/c50_convention_map.json
docs/next_level/c50_convention_roundtrip_report.json

docs/next_level/c50_plane_wave_operator_derivation.json
docs/next_level/c50_operator_ordering_report.json

docs/next_level/c50_finite_volume_state_normalization.json
docs/next_level/c50_state_normalization_validation.json

docs/next_level/c50_finite_box_pminus_kernel.json
docs/next_level/c50_pminus_dimensional_ledger.json
docs/next_level/c50_pminus_validation.json

docs/next_level/c50_pminus_to_m2_derivation.json
docs/next_level/c50_pminus_to_m2_validation.json

docs/next_level/c50_canonical_component_decomposition.json
docs/next_level/c50_transverse_rank_dimensional_closure.json

docs/next_level/c50_arbitrary_mode_vertex_evaluator.json
docs/next_level/c50_basis_projection_validation.json

docs/next_level/c50_continuum_splitting_crosscheck.json
docs/next_level/c50_abelian_blfq_crosscheck.json
docs/next_level/c50_coordinate_momentum_equivalence.json

docs/next_level/c50_c47_tuple_comparison.json
docs/next_level/c50_historical_tuple_status.json

docs/next_level/c50_unit_covariance_report.json
docs/next_level/c50_regulator_scaling_report.json

docs/next_level/c50_c51_vertex_assembly_contract.json
docs/next_level/c50_numerical_object_inventory.json

docs/next_level/c50_readiness_report.json
docs/next_level/c50_source_sufficiency_decision.json
docs/next_level/c50_no_go_decision_tree.json
docs/next_level/c50_missing_calculation_specification.md
docs/next_level/c50_regression_report.json
```

Add source code under:

```text
src/deuteron_wigner/bridge/vsrc/
```

or the repository-equivalent package.

Add focused tests for:

```text
light-front convention conversion;
operator substitution;
finite-volume state normalization;
plane-wave P^- kernel;
P^- to M^2 conversion;
dimensional decomposition;
arbitrary-mode projection;
continuum and Abelian cross-checks;
unit/regulator covariance;
end-to-end derivation.
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON and runtime arrays must reproduce byte-for-byte.

---

# 24. Acceptance criteria

C50 is complete only when:

1. The full C49 baseline reproduces.
2. The C49 no-go remains explicit.
3. The C43 action, C45 mode, and C47 basis contracts remain unchanged.
4. C40 remains method-oracle only.
5. C47 raw tuple values are not consumed as physical inputs.
6. Model-hadron BLFQ sources remain comparison-only.
7. Source inputs and project-derived results are clearly distinguished.
8. The C43/no-sqrt(2) convention map is exact.
9. Fourier phases and box modes map consistently.
10. State normalizations map consistently.
11. The canonical operator ordering is derived.
12. The finite-volume q and qg states are normalized.
13. The plane-wave P^- matrix element is derived directly.
14. Its Kronecker and momentum-conservation factors are explicit.
15. Its symbolic-L dependence is explicit.
16. Its mass and transverse components have common P^- units.
17. No convenient mass or b_HO patch is introduced.
18. The P^- to M^2 conversion is derived.
19. The factor of two is proved in the project convention.
20. The off-diagonal P_perp^2 decision is proved.
21. All M^2 components have mass-squared units.
22. The arbitrary-mode evaluator is independent of raw tuple values.
23. Coordinate- and momentum-space holdouts agree.
24. The continuum q->qg cross-check closes at its scope.
25. The Abelian BLFQ cross-check closes after convention conversion.
26. The historical BLFQ factor-of-two error is detected as a negative control.
27. GeV/MeV covariance passes.
28. Symbolic-L scaling passes.
29. P^+ and b_HO scaling tests pass at their declared scope.
30. C47 tuple comparisons remain diagnostic only.
31. The C51 assembly contract is complete.
32. Runtime objects contain actual symbolic/numerical evaluators.
33. End-to-end derivation passes.
34. At least 192 focused live mutations are detected.
35. No exhaustive physical vertex matrix is assembled.
36. No SU(3)/triplet production matrix is claimed.
37. No remaining local-HQCD matrices are claimed.
38. No JMY Wilson or bilocal TMD matrix is created.
39. No physical counterterm coefficient is solved.
40. No one-loop coefficient or matching kernel is created.
41. No proton TMD or ART25 bridge is created.
42. No fit, inference, process, or production route is created.
43. Historical roots, `NO_JOINT_MEASURE`, 216 routes, ART25 identities, and authoritative artifacts remain unchanged.
44. `MSHT20_REP/` remains untouched and outside Git.
45. The working tree is clean except for the pre-existing untracked directory.
46. A local completion commit is created and not pushed.

A rigorous no-go is valid. Do not weaken convention equivalence, finite-volume normalization, dimensional homogeneity, or independent derivation to open the gate.

---

# 25. Final Codex response

Report:

- full starting and final commits;
- exact source hierarchy and role classifications;
- exact distinction between source-transcribed and project-derived formulas;
- convention-map equations and residuals;
- canonical operator decomposition;
- finite-volume state normalizations;
- plane-wave P^- kernel components, dimensions, and symbolic-L behavior;
- P^- to M^2 route and residuals;
- mass/transverse dimensional closure;
- arbitrary-mode evaluator holdouts and residuals;
- continuum q->qg helicity/kinematic comparison;
- Abelian BLFQ convention and factor-of-two comparison;
- coordinate/momentum-space residuals;
- unit and regulator covariance results;
- C47 historical-tuple comparison classifications;
- runtime-bundle hashes;
- focused mutation results;
- exact readiness or no-go status;
- exact next branch;
- confirmation that no exhaustive canonical matrix, remaining local-QCD matrices, JMY Wilson/bilocal matrix, physical counterterm solution, one-loop result, matching kernel, proton TMD, ART25 bridge, fit, inference, process, or production action occurred;
- integrity and deterministic-reconstruction status;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a literature search, a model-hadron Hamiltonian, an unconverted QED formula, a repaired C47 tuple, or a hard-coded \(2P^+\) multiplier as the source-qualified finite-box QCD canonical vertex.
