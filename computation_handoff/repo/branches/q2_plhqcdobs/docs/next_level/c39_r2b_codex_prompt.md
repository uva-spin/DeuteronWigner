# C39/R2B Codex Work Package

## Title

**Execute the finite-basis one-loop spacelike quark correlator, universal soft/overlap subtraction, partonic renormalization, and state-independent light-front-to-selected-scheme matching**

## Authoritative baseline

Start from the clean local C38/M0A completion commit whose abbreviated hash is:

```text
16f7eb1
```

The supplied handoff does not provide the full commit hash. Do not invent it. Resolve and record the authoritative baseline before edits:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor 0ac139f HEAD
git merge-base --is-ancestor bbefd963ea14bf79884ec3a5c1a503581a6dd21e HEAD
```

The resolved clean `HEAD` is the C39 starting commit only when it contains and reproduces:

```text
docs/next_level/c38_implementation_report.md
docs/next_level/c38_c39_prerequisite_gate.json
docs/next_level/c38_capability_matrix.json
docs/next_level/c38_partonic_probe_root.json
docs/next_level/c38_common_ir_plan.json
docs/next_level/c38_spacelike_wilson_insertion.json
docs/next_level/c38_partonic_counterterm_system.json
docs/next_level/c38_discrete_distribution_functional.json
docs/next_level/c38_factorized_resolution_grid.json
handoff/ROADMAP.md
```

Required scientific ancestry includes:

```text
C37/R2:
    resolve full local commit abbreviated 0ac139f

C36/O4:
    resolve full local commit abbreviated dee1dfb

C35/S0C:
    bbefd963ea14bf79884ec3a5c1a503581a6dd21e

C32/R0:
    0d7b94a5e86882b23a56d4c1f11900d554756a18

C28/P1D:
    52678312906bf5cc0bb8664e2486d5d676a6b723
```

Do not use `origin/main` when the local branch is ahead of the remote.

The authoritative Volume XXI source remains:

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

Read and hash-audit it. Preserve its historical two-root, regulator, subtraction, and matching semantics. Add a versioned C39 calculation crosswalk or addendum rather than silently rewriting Volume XXI.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Why C39/R2B is the exact next package

C38 has completed the prerequisite infrastructure and issued:

```text
C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY
```

The following are now available as distinct, versioned objects:

```text
a nonhadronic color-fundamental matching-probe root
normalized one-quark states
normalized quark-gluon states
a common mass IR prescription
a dedicated partonic Hamiltonian
a finite-basis spacelike Wilson path
longitudinal and transverse closure records
instantaneous, constrained, boundary, and zero-mode interfaces
partonic counterterm equations and renormalization conditions
a discrete-to-distributional x functional
a factorized regulator/resolution trajectory interface
tree and first-order Ward/count-once pilots
universal-soft and overlap prerequisites
```

C38 correctly created no one-loop correlator, universal matching kernel, proton TMD, ART25 bridge comparison, fit, inference, or production route.

C39 must now use this fixed infrastructure to perform the actual one-loop calculation.

The physical scheme remains:

```text
O4-SPACELIKE-COLLINS-JMY
```

with:

```text
C36_COLLINEAR_ROOT, B=1
C36_SOFT_ROOT,      B=0
```

The universal soft factor remains outside the hadron tensor network.

The desired matching relation is:

\[
F_q^{\rm selected}(x,b_T;\mu,\zeta_v)
=
\sum_j
Z_{q\leftarrow j}^{\rm FB\to selected}
\otimes_x
F_j^{\rm FB,reg}
+
R_q^{\rm FB\to selected}.
\]

At one loop:

\[
Z_{q\leftarrow j}^{\rm FB\to selected}
=
\delta_{qj}\delta(1-x)
+
a_s Z_{q\leftarrow j}^{(1)}
+
\mathcal O(a_s^2).
\]

The kernel must be extracted from a common-IR partonic difference, not from a hadron-level ratio.

---

# 2. Fixed scientific decisions

The following decisions are immutable in C39:

```text
rapidity/operator scheme:
    O4-SPACELIKE-COLLINS-JMY

matching probes:
    C38 color-fundamental nonhadronic q and qg sectors

common IR:
    the exact C38 mass-regulator plan

soft ownership:
    C36 universal B=0 soft root outside the hadron TTN

microscopic hadron parent:
    C11 remains a separate regulated model density

historical negative control:
    C35 finite-cell modified-delta no-go and Ward defect

tree identity:
    the C36 spacelike operator reduces to all twelve nonzero
    C11 u/d/ubar/dbar parents at g=0

external comparison:
    ART25 remains outside the matching derivation
```

Do not reopen the regulator-family audit.

Do not switch to modified delta, exponential regulation, a finite-length regulator, a dressed-field operator, or a different common-IR prescription after inspecting residuals.

An auxiliary-field representation may remain an independent representation oracle for the selected spacelike Wilson geometry. It is not an additive soft factor.

---

# 3. Primary objective

Execute the chain:

```text
C38 partonic infrastructure
    -> frozen one-loop calculation plan
    -> continuum selected-scheme bare quark correlator
    -> continuum selected-scheme universal soft factor
    -> continuum subtracted and UV-renormalized quark TMD
    -> finite-basis bare partonic quark correlator
    -> finite-basis real qg and virtual q intermediate contributions
    -> finite-basis Wilson, instantaneous, constrained, zero-mode,
       endpoint, and boundary contributions
    -> solution of the partonic counterterm system
    -> finite-basis renormalized collinear object
    -> universal soft/overlap count-once subtraction
    -> discrete-to-distributional x reconstruction
    -> common-IR continuum-minus-finite-basis difference
    -> state-independent LF-to-selected-scheme matching kernel
    -> selected-scheme-to-project conversion
    -> hadron-application readiness decision
```

C39 is calculation-first.

Do not create new architecture classes, manifests, or source records unless they are required to represent an actual calculated term, counterterm, cancellation, trajectory, or failure mode.

A rigorous no-go is valid, but the package must attempt the complete declared one-loop calculation using the C38 infrastructure.

---

# 4. Scientific scope

C39 is:

```text
rank-zero
T-even
quark and positive-x antiquark aware
one-loop targeted
partonic
finite-basis light-front
spacelike finite-rapidity Wilson-line specific
mass-IR regulated
distributional in x
b-space first
universal-soft subtracted
UV and basis counterterm explicit
state-independence tested
validation only
non-inferential
```

C39 is not:

```text
a regulator survey
a phenomenological fit
an ART25 refit
a proton-level ratio
a free normalization
a direct proton TMD export by default
a bridge comparison
a process calculation
a deuteron prediction
a gluon-TMD calculation
a T-odd matching package
an inference or production package
```

C39 should normally stop at a universal matching and hadron-application gate.

Actual application to the C11/C14 proton state and independent comparison to ART25 belong to a later package.

---

# 5. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C5-C39 Hamiltonian, operator, Wilson, soft, regulator, matching, evolution, bridge, formal-volume, primary-source, API, manifest, test, ADR, and roadmap files before edits.

Continue autonomously until every applicable C39 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository source and git history;
- preserve exact additional source expressions or ancillaries;
- calculate continuum one-loop graphs;
- evaluate finite-basis real and virtual sums;
- solve the partonic counterterm system;
- execute soft and overlap subtractions;
- reconstruct distributional x coefficients;
- run all frozen resolution, IR, gauge, rapidity, and holdout checks;
- rebuild deterministic manifests.

Do not:

- contact authors;
- alter C11-C38 historical results;
- reselect the regulator or common-IR plan;
- use the proton as the matching probe;
- use ART25 members, data, chi2, residuals, or bridge values;
- tune counterterms to a desired matching result;
- infer distributional coefficients from the twelve bridge points;
- equate energy convergence with TMD convergence;
- export a physical proton TMD;
- rerun the ART25 bridge;
- create a likelihood, posterior, optimizer, reweighting, or emulator;
- modify production;
- push the completion commit.

---

# 6. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 6.1 Partonic infrastructure

```text
docs/next_level/c38_implementation_report.md
docs/next_level/c38_api.md
docs/next_level/c38_requirement_coverage.json
docs/next_level/c38_normative_source_integration.json
docs/next_level/c38_primary_source_manifest.json
docs/next_level/c38_derivation_authority_manifest.json

docs/next_level/c38_partonic_probe_root.json
docs/next_level/c38_partonic_probe_scope.json
docs/next_level/c38_probe_plan_selection.json
docs/next_level/c38_common_ir_plan.json
docs/next_level/c38_common_ir_realization_report.json

docs/next_level/c38_one_quark_state_manifest.json
docs/next_level/c38_one_quark_normalization_report.json
docs/next_level/c38_quark_gluon_state_manifest.json
docs/next_level/c38_qg_normalization_report.json

docs/next_level/c38_partonic_hamiltonian_manifest.json
docs/next_level/c38_partonic_hamiltonian_validation.json
docs/next_level/c38_spacelike_wilson_insertion.json
docs/next_level/c38_wilson_emission_vertex.json
docs/next_level/c38_wilson_matrix_element_report.json

docs/next_level/c38_transverse_boundary_operator.json
docs/next_level/c38_endpoint_boundary_report.json
docs/next_level/c38_instantaneous_sector.json
docs/next_level/c38_constraint_sector_report.json
docs/next_level/c38_partonic_zero_mode_sector.json
docs/next_level/c38_zero_mode_decision_report.json

docs/next_level/c38_partonic_counterterm_system.json
docs/next_level/c38_counterterm_renormalization_conditions.json
docs/next_level/c38_counterterm_solvability_report.json

docs/next_level/c38_discrete_distribution_functional.json
docs/next_level/c38_basis_endpoint_distribution.json
docs/next_level/c38_basis_convolution_interface.json
docs/next_level/c38_distribution_refinement_report.json

docs/next_level/c38_factorized_resolution_grid.json
docs/next_level/c38_refinement_map_manifest.json
docs/next_level/c38_partonic_trajectory_plan.json
docs/next_level/c38_trajectory_identifiability_report.json

docs/next_level/c38_tree_partonic_operator_report.json
docs/next_level/c38_qg_vertex_report.json
docs/next_level/c38_wilson_vertex_oracle_report.json
docs/next_level/c38_partonic_ward_pilot.json

docs/next_level/c38_soft_interface_prerequisite.json
docs/next_level/c38_overlap_interface_prerequisite.json
docs/next_level/c38_c39_prerequisite_gate.json
docs/next_level/c38_capability_matrix.json
```

Use the actual filenames when the implementation differs. Do not invent absent files.

## 6.2 Selected scheme and historical matching roots

```text
docs/next_level/c36_implementation_report.md
docs/next_level/c36_spacelike_collinear_definition.json
docs/next_level/c36_spacelike_soft_definition.json
docs/next_level/c36_soft_allocation_convention.json
docs/next_level/c36_finite_rapidity_direction_manifest.json
docs/next_level/c36_joint_regulator_manifest.json
docs/next_level/c36_selected_scheme_soft_oracle.json
docs/next_level/c36_selected_scheme_collinear_oracle.json
docs/next_level/c36_selected_scheme_oracle_validation.json
docs/next_level/c36_selected_to_project_conversion.json
docs/next_level/c36_hard_companion_conversion.json
docs/next_level/c36_overlap_convention.json

docs/next_level/c37_implementation_report.md
docs/next_level/c37_selected_scheme_definition.json
docs/next_level/c37_selected_rapidity_scale_map.json
docs/next_level/c37_selected_soft_allocation.json
docs/next_level/c37_source_sufficiency_decision.json
```

## 6.3 Finite-basis Hamiltonian and Wilson ancestors

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c12_implementation_report.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c5_implementation_report.md
docs/next_level/c6_implementation_report.md
```

These are methodological ancestors only where the operator, external-state, color, normalization, and regulator identities agree.

## 6.4 Distribution, matching, and evolution oracles

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
```

## 6.5 Formal sources

```text
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/volume_xix_source_qualified_process_inputs.tex
references/volume_xx_source_reproducible_bridge_geometry.tex
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Create:

```text
docs/next_level/c39_normative_source_integration.json
docs/next_level/c39_volume_xxi_calculation_crosswalk.json
```

---

# 7. Primary-source and derivation authority

Reuse the exact C36-C38 source locks.

Preserve any newly required source or ancillary under:

```text
data/raw/c39_sources/
```

with exact version and SHA-256 identity.

Every calculated contribution must store:

```text
derivation ID
source locator or first-principles derivation
external probe identity
flavor
color
helicity
basis resolution
IR mass
spacelike Wilson direction
finite-rapidity invariant
bT and x representation
Hamiltonian or operator origin
counterterm convention
perturbative order
symbolic-expression hash
generated-code hash
independent check
```

Classify each contribution as:

```text
CONTINUUM_SELECTED_SCHEME_AUTHORITY
FINITE_BASIS_DIRECT_CALCULATION
FINITE_BASIS_HAMILTONIAN_DERIVATION
UNIVERSAL_SOFT_AUTHORITY
OVERLAP_SUBTRACTION_AUTHORITY
COUNTERTERM_AUTHORITY
DISTRIBUTIONAL_RECONSTRUCTION
METHOD_ONLY
NOT_OPERATOR_IDENTICAL
```

Create:

```text
docs/next_level/c39_primary_source_manifest.json
docs/next_level/c39_derivation_authority_manifest.json
```

---

# 8. Immutable C38 baseline

Before edits, reproduce and record:

```text
resolved full C38 completion commit
C38_VALIDATION_PASS
C38 dedicated test suite passing
3,040 deterministic C38 semantic injections

outcome:
    C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY

probe:
    separate, nonhadronic, color-fundamental

sectors:
    normalized q
    normalized qg

IR:
    common mass-regulator plan

operator:
    finite-basis spacelike Wilson path
    endpoints and transverse closure

finite-basis structures:
    instantaneous
    constrained
    boundary
    zero mode
    counterterm
    distributional x
    factorized trajectory

pilots:
    tree operator
    canonical qg vertex
    Wilson first-order vertex
    Ward/count-once infrastructure

nonclaims:
    no one-loop matching kernel
    no microscopic proton TMD
    no ART25 bridge comparison
    no fit or production action

integrity:
    all 642 ART25 identities unchanged
    NO_JOINT_MEASURE
    216 production routes
    eight authoritative artifacts
    MSHT20_REP outside Git
```

Do not proceed if the baseline fails.

C39 must not modify:

- C11-C38 historical roots or statuses;
- the C36 spacelike regulator;
- the C38 probe, IR, path, counterterm, distributional, or trajectory identities in place;
- the C35 finite-delta Ward defect;
- the frozen bridge grid, roles, holdouts, ancestry, or `NO_JOINT_MEASURE`;
- ART25;
- production or authoritative artifacts.

Create versioned C39 calculation descendants only.

---

# 9. Freeze the one-loop calculation plan

Before evaluating a graph or sum, freeze:

```text
selected C36 spacelike scheme
C38 probe representation
C38 common mass IR values
external quark momenta
external helicities
u/d and quark/antiquark probes
gauge convention and checks
finite-rapidity directions and invariant
future/past T-even orientation
mu values
bT points
K, Nmax, bHO and all factorized regulator points
distributional test functions
counterterm conditions
soft allocation
overlap convention
holdouts
```

Use exact C38 identities.

If any required numerical values or comparison maps remain absent, fail closed with the exact missing object rather than substituting convenient values.

Create:

```text
docs/next_level/c39_calculation_plan.json
docs/next_level/c39_external_probe_schedule.json
docs/next_level/c39_holdout_plan.json
```

---

# 10. Continuum selected-scheme calculation

Reconstruct the same rank-zero quark TMD in the selected spacelike scheme using the exact common mass IR prescription.

Calculate and retain separately:

```text
tree term
quark self energy
bilocal quark vertex
real q -> qg emission
spacelike Wilson-line attachment
Wilson-line self energy
endpoint/cusp contribution
transverse-closure contribution
unsubtracted collinear result
universal spacelike soft factor
soft allocation
UV counterterm
subtracted/renormalized TMD
finite-rapidity dependence
```

Represent the result as:

\[
F_{\rm selected}^{(1)}(x,b_T)
=
c_\delta(b_T)\delta(1-x)
+
\sum_n c_n(b_T)
\left[\frac{\ln^n(1-x)}{1-x}\right]_+
+
f_{\rm reg}(x,b_T).
\]

Required checks:

- source transcription;
- independent graph or scalar-integral reconstruction;
- real/virtual count once;
- Mellin moments;
- quark-number moment;
- mass-IR dependence;
- gauge independence of the subtracted object;
- future/past equality;
- finite-rapidity derivative and limit order.

Create:

```text
docs/next_level/c39_continuum_bare_collinear.json
docs/next_level/c39_continuum_soft_execution.json
docs/next_level/c39_continuum_renormalized_tmd.json
docs/next_level/c39_continuum_oracle_validation.json
```

A transcription without an independent reconstruction is not a complete continuum oracle.

---

# 11. Finite-basis bare one-loop correlator

Using the C38 matching probes, calculate the bare finite-basis correlator.

Resolve every applicable contribution:

```text
tree q -> q operator
virtual quark self energy
virtual bilocal operator vertex
real q -> qg emission
virtual qg intermediate-state contribution
spacelike Wilson emission
spacelike Wilson absorption/conjugate contribution
Wilson-line self energy
endpoint/cusp term
transverse closure
instantaneous fermion
instantaneous gluon
constrained gauge component
contact term
basis boundary
zero-mode control
mass counterterm insertion
field counterterm insertion
vertex counterterm insertion
operator counterterm insertion
Wilson/endpoint counterterm insertion
basis/truncation counterterm insertion
```

For each contribution record:

```text
status
value or distributional functional
basis resolution
external probe
IR mass
finite rapidity
x support
bT dependence
UV behavior
IR behavior
gauge behavior
cancellation partners
independent implementation route
```

Allowed statuses:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_IDENTITY
CANCELS_WITH_DECLARED_PARTNER
NOT_APPLICABLE_WITH_PROOF
UNRESOLVED_BLOCKING
```

No complete matching status may be issued while a required contribution remains `UNRESOLVED_BLOCKING`.

Create:

```text
docs/next_level/c39_finite_basis_bare_correlator.json
docs/next_level/c39_finite_basis_contribution_results.json
docs/next_level/c39_finite_basis_one_loop_closure_matrix.json
```

---

# 12. Real and virtual calculations

## 12.1 Real \(qg\) sector

Use the normalized C38 qg states and the exact finite-basis phase-space/completeness relation.

Calculate:

```text
canonical q -> qg emission
operator emission
spacelike Wilson emission
interference terms
measurement delta/functionals
endpoint behavior
```

## 12.2 Virtual sector

Use the finite-basis Hamiltonian and intermediate-state sum or equivalent matrix-free resolvent.

Calculate:

```text
self energy
operator vertex
Wilson virtual terms
instantaneous partners
counterterm insertions
```

Required checks:

- assembled versus matrix-free;
- direct sum versus resolvent;
- real/virtual support;
- Hermitian conjugation;
- energy-denominator prescription;
- mass-IR dependence;
- no numerical epsilon as physical support;
- cut and virtual terms counted once.

Create:

```text
docs/next_level/c39_real_qg_execution.json
docs/next_level/c39_virtual_q_execution.json
docs/next_level/c39_real_virtual_count_once_report.json
```

---

# 13. Execute the counterterm system

Solve the C38 partonic counterterm system only after the corresponding bare structures exist.

Retain separate solutions for:

```text
quark mass
quark field
canonical q<->qg vertex
instantaneous partners
bilocal operator
spacelike Wilson line
endpoint/cusp
transverse closure
basis boundary
sector truncation
```

Every solution must be fixed by partonic renormalization conditions.

Required outputs:

```text
equation matrix
rank
null directions
condition number
solution
holdout residuals
resolution dependence
IR independence
finite-rapidity dependence
first omitted order
```

Do not use:

```text
proton mass
proton current
proton TMD
ART25
bridge values
desired continuum finite constants
```

to close the partonic counterterm system.

Create:

```text
docs/next_level/c39_counterterm_solution.json
docs/next_level/c39_counterterm_rank_report.json
docs/next_level/c39_counterterm_holdout_report.json
```

If the system is underdetermined, keep the unresolved directions explicit and fail closed.

---

# 14. Renormalized finite-basis collinear object

Construct:

\[
F_{\rm FB}^{\rm ren}
=
Z_{\rm field}
Z_{\rm op}
Z_{\rm Wilson}
\left[
F_{\rm FB}^{\rm bare}
+
F_{\rm inst}
+
F_{\rm boundary}
+
F_{\rm zero}
+
F_{\rm CT}
\right].
\]

The exact factorization may differ according to the selected finite-basis convention; preserve the actual operator ordering.

Required checks:

- UV/cutoff closure;
- mass-IR dependence remains only in the common physical IR structure;
- gauge/Ward closure;
- quark-number normalization;
- finite-rapidity identity;
- basis-resolution behavior;
- endpoint and zero-mode accounting;
- no hidden state-dependent normalization.

Create:

```text
docs/next_level/c39_finite_basis_renormalized_collinear.json
docs/next_level/c39_finite_basis_uv_closure.json
docs/next_level/c39_finite_basis_ward_closure.json
```

---

# 15. Discrete-to-distributional reconstruction

Use the exact C38 distribution functional.

For every resolution, calculate the action on the frozen test-function basis:

\[
\langle F_K,\varphi_r\rangle.
\]

Reconstruct, only when the linear system is identifiable:

```text
delta endpoint coefficient
plus-distribution coefficients
regular-support representation
Mellin moments
convolution action
```

A closed-form coefficient decomposition is not required when the finite-resolution authority is better represented as a distribution functional. In that case, issue a typed functional result and do not invent a unique analytic decomposition.

Required checks:

- rank and nullspace of the reconstruction;
- endpoint action;
- quark-number moment;
- test-function holdouts;
- K refinement;
- agreement with the direct finite-basis measurement;
- no spline or ART25-based interpolation.

Create:

```text
docs/next_level/c39_distributional_reconstruction.json
docs/next_level/c39_distributional_rank_report.json
docs/next_level/c39_distributional_holdout_report.json
```

---

# 16. Universal soft and overlap subtraction

Use the C36 universal spacelike soft root outside the hadron TTN.

Execute the selected soft allocation and overlap convention exactly once.

Retain separately:

```text
unsubtracted finite-basis collinear object
universal soft factor
soft allocation power
overlap/zero-bin object
UV conversion
finite-rapidity dependence
```

Required negative controls:

```text
missing soft
duplicate soft
missing overlap
duplicate overlap
wrong soft power
wrong rapidity value
wrong bT convention
```

Required positive checks:

- count-once closure;
- gauge/Ward closure after subtraction;
- mass-IR consistency;
- finite-rapidity consistency;
- source-convention identity.

Create:

```text
docs/next_level/c39_soft_subtraction_execution.json
docs/next_level/c39_overlap_subtraction_execution.json
docs/next_level/c39_soft_overlap_count_once_report.json
```

If the soft/overlap relation cannot be executed with the common mass IR plan, issue the exact overlap branch rather than forcing cancellation.

---

# 17. Extract the matching kernel

Only after both sides are renormalized and use the same IR prescription, calculate:

\[
Z_{\rm FB\to selected}^{(1)}
=
F_{\rm selected}^{(1),\rm ren}
-
F_{\rm FB}^{(1),\rm ren},
\]

with the exact distributional inverse/convolution relation.

The kernel must be:

```text
IR finite
gauge independent
state independent
hadron independent
ART25 independent
explicit in K, Nmax, bHO and the finite-basis regulator
explicit in finite rapidity
explicit in mu
distributionally well defined
accompanied by first omitted order and remainder
```

Create:

```text
docs/next_level/c39_lf_to_selected_matching_library.json
docs/next_level/c39_matching_kernel_rank_report.json
docs/next_level/c39_matching_remainder.json
```

If any required cancellation fails, serialize an empty-not-zero kernel.

---

# 18. Matching-channel discipline

Decide explicitly:

```text
q <- q
q <- qbar
q <- g
nonsinglet
quark singlet
```

The C38 q and qg probe infrastructure does not automatically prove the full singlet matrix.

A positive `q <- q` nonsinglet result may issue:

```text
C39_NONSINGLET_MATCHING_VALIDATED
```

but must not be promoted to complete independent \(u,d,\bar u,\bar d\) matching while unresolved \(q\leftarrow g\) or singlet mixing contributes at the declared order.

If an off-diagonal channel is zero at the selected order, provide a source- or calculation-backed proof.

Create:

```text
docs/next_level/c39_matching_channel_matrix.json
docs/next_level/c39_singlet_mixing_report.json
```

---

# 19. Closure tests

## 19.1 IR closure

Evaluate at all frozen and holdout IR masses.

Report:

```text
continuum mass-IR dependence
finite-basis mass-IR dependence
matching-difference mass-IR dependence
```

## 19.2 Gauge and Ward closure

Test:

```text
continuum subtracted object
finite-basis renormalized/subtracted object
matching difference
```

The C35 finite-delta Ward defect remains a negative control and must not contaminate the selected spacelike scheme.

## 19.3 UV closure

Separate:

```text
continuum UV renormalization
finite-basis Hamiltonian/basis UV renormalization
operator/Wilson counterterms
matching-kernel UV dependence
```

## 19.4 Rapidity and cusp closure

Test the selected finite-rapidity derivative, cusp relation, and limit order.

## 19.5 Sum-rule closure

Test:

```text
tree limit
quark number
charge conjugation
flavor universality where proved
small-b behavior
```

Create:

```text
docs/next_level/c39_ir_cancellation_report.json
docs/next_level/c39_gauge_ward_report.json
docs/next_level/c39_uv_closure_report.json
docs/next_level/c39_rapidity_cusp_report.json
docs/next_level/c39_sum_rule_report.json
```

Do not fabricate unavailable residuals.

---

# 20. State-independence tests

Test the extracted kernel across:

```text
at least two external momenta
at least two IR masses
both quark helicities
u and d labels
quark and positive-x antiquark charge-conjugate probes
at least three valid finite-basis resolutions
one wave-packet or alternate probe realization when available
one simple composite toy state not used in extraction
```

A universal kernel may depend on the regulator, not on the external probe or hadron state.

If irreducible probe dependence remains, issue:

```text
STATE_DEPENDENT_MODEL_MAP
```

and do not call the result matching.

Create:

```text
docs/next_level/c39_state_independence_report.json
docs/next_level/c39_flavor_antiquark_report.json
```

---

# 21. Factorized regulator trajectory

Execute the C38 factorized grid.

Separate:

```text
K dependence
Nmax dependence
bHO dependence
basis UV support
basis IR support
endpoint/boundary dependence
zero-mode dependence
IR-mass dependence
finite-rapidity dependence
quadrature dependence
```

Use only source- or derivation-predicted fit structures.

Require:

```text
more independent points than fitted coefficients
at least one holdout per fitted family
operator-specific convergence
matching-kernel convergence
```

Allowed statuses:

```text
MATCHING_TRAJECTORY_RESOLVED
LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
FINITE_BASIS_MATCHING_ONLY
NONIDENTIFIABLE_TRAJECTORY
TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c39_matching_trajectory.json
docs/next_level/c39_trajectory_holdout_report.json
docs/next_level/c39_trajectory_decision.json
```

Energy convergence is not a TMD or matching convergence criterion.

---

# 22. Selected-scheme-to-project conversion

Use the C36 conversion as a read-only source contract.

Execute:

```text
finite-basis -> selected spacelike scheme
selected spacelike scheme -> project renormalized scheme
project scheme -> read-only ART25 convention
```

Keep separate:

```text
operator conversion
UV convention
rapidity convention
soft allocation
finite factor
hard-factor companion
scale relocation
two-scale evolution
threshold map
```

Required checks:

- inverse;
- round trip;
- hard × TMD × TMD invariance;
- \(\mu\) RG;
- rapidity RG;
- member/data independence;
- first omitted order.

Create:

```text
docs/next_level/c39_selected_to_project_execution.json
docs/next_level/c39_conversion_roundtrip_report.json
docs/next_level/c39_hard_companion_report.json
docs/next_level/c39_downstream_art25_contract.json
```

Do not use ART25 fit parameters or covariance in the conversion.

---

# 23. Hadron-application gate

C39 normally stops at a universal partonic matching result.

Issue:

```text
C39_HADRON_APPLICATION_READY
```

only when:

```text
all required matching channels for the intended u/d/ubar/dbar application close
the matching kernel is state independent
the distributional convolution is executable
the regulator trajectory is sufficient
the selected-to-project conversion closes
the first omitted order and all remainders are explicit
the C11/C14 operator application identity is explicit
TMD-specific TTN convergence requirements are specified
the common x-b-Q domain is defined
```

Create:

```text
docs/next_level/c39_hadron_application_prerequisite.json
docs/next_level/c39_hadron_application_gate.json
docs/next_level/c39_bridge_prerequisite_delta.json
```

Do not apply the kernel to the proton or calculate ART25 residuals in C39.

The bridge remains:

```text
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
```

unless and until an independent hadron-application/bridge package is executed.

---

# 24. Tensor-network and quantum interface

Use the C38 partonic tensor-network interface for calculation and validation where useful.

Compare:

```text
explicit basis sums
matrix-free resolvent action
partonic tensor-network contraction
```

on:

```text
real qg contribution
virtual qg contribution
Wilson insertion
instantaneous terms
distributional measurement
```

Bond dimension is a deterministic numerical axis.

Do not train a QDNN or quantum circuit.

Update:

```text
docs/next_level/c39_partonic_tensor_network_execution.json
docs/next_level/c39_quantum_operator_interface_update.json
```

---

# 25. Uncertainty and remainder separation

Keep separate:

```text
continuum source/transcription
continuum numerical integration
common mass-IR residual
finite-basis longitudinal truncation
finite-basis transverse truncation
basis UV remainder
basis IR remainder
endpoint/boundary remainder
zero-mode remainder
instantaneous-sector remainder
counterterm null directions
distributional reconstruction remainder
soft-allocation remainder
overlap/zero-bin remainder
finite-rapidity power correction
matching-channel incompleteness
trajectory remainder
selected-to-project conversion
two-scale evolution
tensor-network truncation
floating-point error
first omitted perturbative order
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No matching remainder may be absorbed into ART25 covariance, a proton normalization, or a free TMD width.

Create:

```text
docs/next_level/c39_uncertainty_budget.json
docs/next_level/c39_remainder_separation.json
```

---

# 26. Scientifically valid outcomes and next branches

## 26.1 Continuum selected-scheme oracle incomplete

```text
C39_CONTINUUM_ONE_LOOP_ORACLE_INCOMPLETE
```

Next:

> **C40/R2S — selected spacelike continuum graph and integral reconstruction completion**

## 26.2 Finite-basis bare calculation incomplete

```text
C39_FINITE_BASIS_ONE_LOOP_INCOMPLETE
```

Next:

> **C40/R2C — targeted finite-basis real, virtual, Wilson, instantaneous, and counterterm completion**

## 26.3 Counterterm system unresolved

```text
C39_PARTONIC_COUNTERTERM_SYSTEM_UNRESOLVED
```

Next:

> **C40/CT1 — one-loop partonic renormalization conditions and counterterm closure**

## 26.4 Soft/overlap closure fails

```text
C39_SOFT_OVERLAP_CLOSURE_FAILED
```

Next:

> **C40/Z1 — spacelike soft/collinear overlap and zero-bin completion**

## 26.5 Distributional reconstruction fails

```text
C39_DISTRIBUTIONAL_MATCHING_UNRESOLVED
```

Next:

> **C40/X1 — finite-K endpoint, plus-distribution, and convolution reconstruction**

## 26.6 Matching is state dependent

```text
C39_STATE_INDEPENDENT_MATCHING_UNAVAILABLE
```

Next:

> **C40/O2B — finite-basis partonic operator/regulator redesign for universal matching**

## 26.7 Only nonsinglet closes

```text
C39_NONSINGLET_ONLY
```

Next:

> **C40/MIX0 — singlet and q<-g/q<-qbar matching-channel completion**

## 26.8 Trajectory unresolved

```text
C39_MATCHING_TRAJECTORY_UNRESOLVED
```

Next:

> **C40/R1B — factorized matching trajectory and power-correction completion**

## 26.9 Project conversion unresolved

```text
C39_PROJECT_CONVERSION_UNAVAILABLE
```

Next:

> **C40/C0 — selected-spacelike-to-project conversion completion**

## 26.10 Full universal matching closes

```text
C39_HADRON_APPLICATION_READY
```

Next:

> **C40/B1E — apply the validated kernel to microscopic proton states, close TMD-specific convergence, and execute the frozen ART25 bridge**

Every no-go must identify the exact missing graph, counterterm, channel, cancellation, trajectory, or conversion.

Create:

```text
docs/next_level/c39_source_sufficiency_decision.json
docs/next_level/c39_no_go_decision_tree.json
docs/next_level/c39_missing_calculation_specification.md
```

---

# 27. Holdouts

Freeze before calculation:

```text
one continuum delta-endpoint coefficient
one continuum plus-distribution coefficient
one continuum regular term
one finite-basis real qg contribution
one finite-basis virtual contribution
one Wilson-emission contribution
one Wilson virtual/self-energy contribution
one instantaneous-fermion term
one instantaneous-gluon term
one zero-mode control
one endpoint/boundary contribution
one mass counterterm condition
one field counterterm condition
one vertex counterterm condition
one operator/Wilson counterterm condition
one IR mass
one external momentum
one helicity
one bT point
one finite-rapidity point
one K resolution
one Nmax resolution
one distributional test function
one Mellin moment
one matching-channel decision
one state-independence probe
one selected-to-project round trip
one ART25-independence control
```

No failed holdout may be moved into construction or tuning.

---

# 28. Required benchmark families

Implement at least:

```text
R2B-A  immutable C38 infrastructure and fixed C36 scheme
R2B-B  frozen calculation and external probes
R2B-C  continuum bare collinear calculation
R2B-D  continuum universal soft and subtraction
R2B-E  finite-basis real qg calculation
R2B-F  finite-basis virtual q calculation
R2B-G  Wilson, endpoint, and transverse contributions
R2B-H  instantaneous, constrained, and zero-mode contributions
R2B-I  counterterm solution
R2B-J  renormalized finite-basis collinear object
R2B-K  distributional reconstruction
R2B-L  soft/overlap count-once closure
R2B-M  matching-kernel extraction
R2B-N  IR, UV, gauge, Ward, rapidity, and sum-rule closure
R2B-O  channel matrix and state independence
R2B-P  factorized regulator trajectory
R2B-Q  selected-to-project and hadron-application gates
R2B-R  deterministic isolation and no bridge/readiness leakage
```

---

# 29. Semantic fault injections

Create at least **3,240 ordered C39 semantic fault injections** with stable IDs and deterministic diagnostics.

The injections must test actual calculated structures, not merely identifier dispatch.

Include:

## Baseline and plan

- wrong C38 baseline;
- C36 scheme changed;
- C38 probe root aliased to proton;
- common IR plan changed;
- holdout moved after inspection.

## Continuum calculation

- soft factor omitted;
- soft factor duplicated;
- graph contribution omitted;
- source transcription used without independent check;
- endpoint distribution binned;
- quark-number failure hidden;
- finite-rapidity limit order changed.

## Finite-basis real/virtual calculation

- qg normalization changed;
- virtual denominator sign changed;
- Wilson emission omitted;
- Wilson conjugate omitted;
- instantaneous term omitted;
- boundary term omitted;
- zero mode set to zero without proof;
- counterterm inserted twice;
- numerical epsilon treated as support.

## Counterterms

- proton observable used;
- ART25 used;
- IR dependence absorbed into UV counterterm;
- Wilson and operator counterterms aliased;
- null direction hidden;
- desired continuum constant used as a fit target.

## Distributional reconstruction

- twelve bridge points used as x grid;
- delta endpoint dropped;
- plus distribution replaced by cutoff;
- unsupported analytic decomposition forced from a rank-deficient functional;
- number moment violated;
- spline introduced.

## Soft and overlap

- wrong soft power;
- missing overlap;
- duplicate overlap;
- different rapidity value;
- different bT convention;
- common mass IR contract broken.

## Matching

- hadron-level ratio used;
- ART25 member used;
- IR-dependent difference called matching;
- gauge-dependent difference called matching;
- state-dependent difference called universal;
- q<-g assumed zero;
- first omitted order set to zero.

## Conversion and readiness

- hard companion omitted;
- conversion applied directly to C11;
- inverse absent;
- round-trip failure hidden;
- proton export created in C39;
- bridge residual calculated;
- likelihood, p-value, calibration, reweighting, or emulator created.

## Integrity

- C35 Ward defect changed;
- C36 tree reduction changed;
- bridge roles or holdouts changed;
- `NO_JOINT_MEASURE` changed;
- production registry changed;
- authoritative artifact changed;
- raw MSHT files committed;
- nondeterministic manifest.

---

# 30. Deliverables

Create at least:

```text
docs/next_level/c39_implementation_report.md
docs/next_level/c39_api.md
docs/next_level/c39_requirement_coverage.json
docs/next_level/c39_normative_source_integration.json
docs/next_level/c39_volume_xxi_calculation_crosswalk.json
docs/next_level/c39_primary_source_manifest.json
docs/next_level/c39_derivation_authority_manifest.json

docs/next_level/c39_calculation_plan.json
docs/next_level/c39_external_probe_schedule.json
docs/next_level/c39_holdout_plan.json

docs/next_level/c39_continuum_bare_collinear.json
docs/next_level/c39_continuum_soft_execution.json
docs/next_level/c39_continuum_renormalized_tmd.json
docs/next_level/c39_continuum_oracle_validation.json

docs/next_level/c39_finite_basis_bare_correlator.json
docs/next_level/c39_finite_basis_contribution_results.json
docs/next_level/c39_finite_basis_one_loop_closure_matrix.json
docs/next_level/c39_real_qg_execution.json
docs/next_level/c39_virtual_q_execution.json
docs/next_level/c39_real_virtual_count_once_report.json

docs/next_level/c39_counterterm_solution.json
docs/next_level/c39_counterterm_rank_report.json
docs/next_level/c39_counterterm_holdout_report.json

docs/next_level/c39_finite_basis_renormalized_collinear.json
docs/next_level/c39_finite_basis_uv_closure.json
docs/next_level/c39_finite_basis_ward_closure.json

docs/next_level/c39_distributional_reconstruction.json
docs/next_level/c39_distributional_rank_report.json
docs/next_level/c39_distributional_holdout_report.json

docs/next_level/c39_soft_subtraction_execution.json
docs/next_level/c39_overlap_subtraction_execution.json
docs/next_level/c39_soft_overlap_count_once_report.json

docs/next_level/c39_lf_to_selected_matching_library.json
docs/next_level/c39_matching_kernel_rank_report.json
docs/next_level/c39_matching_remainder.json
docs/next_level/c39_matching_channel_matrix.json
docs/next_level/c39_singlet_mixing_report.json

docs/next_level/c39_ir_cancellation_report.json
docs/next_level/c39_gauge_ward_report.json
docs/next_level/c39_uv_closure_report.json
docs/next_level/c39_rapidity_cusp_report.json
docs/next_level/c39_sum_rule_report.json

docs/next_level/c39_state_independence_report.json
docs/next_level/c39_flavor_antiquark_report.json

docs/next_level/c39_matching_trajectory.json
docs/next_level/c39_trajectory_holdout_report.json
docs/next_level/c39_trajectory_decision.json

docs/next_level/c39_selected_to_project_execution.json
docs/next_level/c39_conversion_roundtrip_report.json
docs/next_level/c39_hard_companion_report.json
docs/next_level/c39_downstream_art25_contract.json

docs/next_level/c39_hadron_application_prerequisite.json
docs/next_level/c39_hadron_application_gate.json
docs/next_level/c39_bridge_prerequisite_delta.json

docs/next_level/c39_partonic_tensor_network_execution.json
docs/next_level/c39_quantum_operator_interface_update.json

docs/next_level/c39_uncertainty_budget.json
docs/next_level/c39_remainder_separation.json

docs/next_level/c39_source_sufficiency_decision.json
docs/next_level/c39_no_go_decision_tree.json
docs/next_level/c39_missing_calculation_specification.md

docs/next_level/c39_injection_manifest.json
docs/next_level/c39_regression_report.json
docs/next_level/c39_unresolved_physics_gaps.md
```

Add ADRs for:

- C39 calculation-first scope;
- continuum selected-scheme reconstruction;
- finite-basis real and virtual authority;
- counterterm solution ordering;
- distributional reconstruction and rank-deficient functionals;
- universal-soft/overlap count once;
- matching-channel discipline;
- state-independent matching;
- factorized trajectory;
- independent hadron-application and bridge package.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy basis sums, resolvent arrays, loop tables, distributional matrices, and trajectory arrays may remain outside Git under content-addressed runtime directories. Commit their schemas, hashes, dimensions, coordinate order, and deterministic reconstruction commands.

---

# 31. Acceptance criteria

C39/R2B is complete only when:

1. The full C38 baseline commit is resolved rather than invented.
2. The complete C38 baseline reproduces.
3. The C36 spacelike scheme remains fixed.
4. The C38 probe and common-IR identities remain fixed.
5. The calculation plan and holdouts are frozen before evaluation.
6. The continuum bare collinear object is calculated or fails closed.
7. The continuum universal soft factor is executed or fails closed.
8. The continuum subtracted TMD has an independent check.
9. Endpoint distributions are exact.
10. Mellin and quark-number checks close where claimed.
11. Every required finite-basis one-loop contribution receives an explicit status.
12. No continuum scalelessness is copied to the finite basis without proof.
13. Real qg contributions are calculated or fail closed.
14. Virtual q contributions are calculated or fail closed.
15. Wilson, endpoint, and transverse terms are explicit.
16. Instantaneous, constrained, boundary, and zero-mode terms are explicit.
17. Counterterms are solved only after their bare structures exist.
18. Counterterms use partonic conditions.
19. Counterterm rank and null directions are reported.
20. The renormalized finite-basis object closes UV identities when claimed.
21. The distributional reconstruction reports its rank and nullspace.
22. A rank-deficient functional is not forced into a unique analytic form.
23. The twelve bridge points are never used as an x grid.
24. Soft and overlap subtractions are placed exactly once.
25. The continuum and finite-basis sides use the same mass IR prescription.
26. The matching difference is IR finite when claimed.
27. The matching difference is gauge independent when claimed.
28. The matching result is state independent when called universal.
29. q<-q, q<-qbar, q<-g, nonsinglet, and singlet statuses are explicit.
30. Nonsinglet-only closure is not promoted to full flavor closure.
31. The factorized trajectory is executed at enough independent points.
32. No trajectory is overfit.
33. Energy convergence is not used as TMD convergence.
34. The selected-to-project conversion is source audited.
35. Hard-factor companion transformations are explicit.
36. Inverse and round-trip conversion are tested.
37. ART25 information does not enter the derivation.
38. C39 normally stops at the hadron-application gate.
39. C39 does not execute the ART25 bridge comparison.
40. No free normalization is introduced.
41. Failed kernels remain empty-not-zero.
42. All 642 ART25 identities and covariance remain unchanged.
43. `NO_JOINT_MEASURE`, ancestry, roles, and holdouts remain unchanged.
44. No fit, likelihood, posterior, optimization, reweighting, or emulator is created.
45. No process, deuteron, gluon, T-odd, inference, or production status is promoted.
46. Every no-go includes an exact missing-calculation specification.
47. All inherited tests, validators, requirements, injections, and manifests remain passing.
48. The production registry remains exactly 216 routes.
49. All eight authoritative artifacts remain byte-identical.
50. `MSHT20_REP/` remains outside Git.
51. At least 3,240 C39 semantic fault injections produce the expected diagnostics.
52. All C39 manifests reproduce byte-for-byte.
53. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
54. A local completion commit is created and not pushed.

A rigorous one-loop, channel, trajectory, or overlap no-go is valid. Do not weaken universality, gauge closure, common-IR identity, or distributional reconstruction to obtain a matching kernel.

---

# 32. Allowed and forbidden statuses

The strongest generally permitted statuses include:

```text
C39_CALCULATION_PLAN_FROZEN
C39_CONTINUUM_SELECTED_SCHEME_ORACLE_VALIDATED
C39_FINITE_BASIS_ONE_LOOP_AUDITED
C39_COUNTERTERM_SYSTEM_SOLVED_OR_DECIDED
C39_DISTRIBUTIONAL_RECONSTRUCTION_AUDITED
C39_SOFT_OVERLAP_COUNT_ONCE_DECIDED
C39_MATCHING_CHANNEL_MATRIX_COMPLETE
C39_STATE_INDEPENDENCE_DECIDED
C39_MATCHING_TRAJECTORY_DECIDED
C39_SELECTED_TO_PROJECT_CONVERSION_AUDITED
C39_HADRON_APPLICATION_GATE_DECIDED
C39_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when every corresponding gate passes:

```text
C39_CONTINUUM_SELECTED_SCHEME_ONE_LOOP_VALIDATED
C39_FINITE_BASIS_COLLINEAR_ONE_LOOP_VALIDATED
C39_PARTONIC_COUNTERTERM_SYSTEM_VALIDATED
C39_SOFT_OVERLAP_CLOSURE_VALIDATED
C39_LF_TO_SELECTED_MATCHING_VALIDATED
C39_NONSINGLET_MATCHING_VALIDATED
C39_FULL_QUARK_SINGLET_MATCHING_VALIDATED
C39_STATE_INDEPENDENT_MATCHING_VALIDATED
C39_MATCHING_TRAJECTORY_RESOLVED
C39_SELECTED_TO_PROJECT_CONVERSION_VALIDATED
C39_HADRON_APPLICATION_READY
```

The following remain forbidden throughout C39:

```text
C39_MICROSCOPIC_PROTON_TMD_EXPORTED
BRIDGE_DISTRIBUTION_COMPARISON_READY
MICROSCOPIC_MODEL_CALIBRATED
ART25_CONSTRAINED_MICROSCOPIC_POSTERIOR
GLOBAL_LIKELIHOOD_READY
GLOBAL_INFERENCE_READY
REPLICA_REWEIGHTED
PARAMETERS_OPTIMIZED
EMULATOR_TRAINED
BRIDGE_PROCESS_READY
SOURCE_PROCESS_PROMOTED
PHYSICAL_INPUT_PROMOTED
PHYSICAL_DEUTERON_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
PHYSICAL_TODD_PROCESS_READY
PRODUCTION_READY
```

---

# 33. Final Codex response

Report:

- resolved full starting and final commits;
- test, validator, builder, evidence, atlas, requirement, injection, and fault-mode counts;
- exact source identities and hashes;
- frozen calculation, probe, common-IR, and holdout plans;
- continuum bare collinear, universal soft, and subtracted-TMD results;
- continuum distributional coefficients and Mellin residuals;
- every finite-basis contribution status and calculated value;
- real/virtual count-once results;
- counterterm system rank, null directions, solution, and holdouts;
- renormalized finite-basis collinear results;
- distributional reconstruction rank, coefficients/functionals, and holdouts;
- soft/overlap subtraction residuals;
- matching-kernel values or exact empty status;
- q<-q, q<-qbar, q<-g, nonsinglet, and singlet decisions;
- IR, UV, gauge, Ward, rapidity, cusp, and sum-rule residuals;
- state-independence and charge-conjugation results;
- factorized trajectory and holdout results;
- selected-to-project conversion and hard-companion results;
- hadron-application gate;
- bridge prerequisite delta, confirming no bridge comparison ran;
- exact no-go and next branch where blocked;
- confirmation that no ART25 member, data, chi2, residual, bridge point, or proton-level ratio entered the derivation;
- confirmation that no proton TMD export, bridge comparison, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe prerequisite infrastructure, an incomplete continuum transcription, a rank-deficient distribution functional, a nonsinglet-only result, or a state-dependent map as a complete microscopic proton TMD matching result.
