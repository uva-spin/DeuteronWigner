# C34/S0A Codex Work Package

## Title

**One-loop finite-basis eikonal soft function, UV and rapidity counterterms, modified-delta renormalization, and soft-sector continuation closure**

## Authoritative baseline

Start from the clean local C33/S0 completion commit that contains:

```text
docs/next_level/c33_implementation_report.md
```

and reproduces the complete C33 completion record:

```text
1,196 tests
33 builders
39/39 evidence rows
165/165 atlas pages
2,140 C33 requirements
2,040/2,040 C33 negative injections
92 named C33 fault modes
```

The C33 report supplied to this work package does not print the final C33 commit hash. Do not invent one. Resolve and record it before edits:

```bash
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 0d7b94a5e86882b23a56d4c1f11900d554756a18 HEAD
```

The resolved clean local `HEAD` is the authoritative C34 starting commit only when:

1. it contains the C33 report and implementation;
2. the complete C33 baseline reproduces;
3. C32 commit

```text
0d7b94a5e86882b23a56d4c1f11900d554756a18
```

is in its ancestry; and

4. required C28 scientific ancestor

```text
52678312906bf5cc0bb8664e2486d5d676a6b723
```

remains in its ancestry.

Do not use `origin/main` when the local branch is ahead of the remote.

If the authoritative Volume XXI source has been integrated, read and hash-audit:

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
```

and map its requirements. If it is absent, record the absence exactly and do not reconstruct or invent it. The scientific calculation may proceed from the C33/C32 contracts, but no claim of completed Volume XXI integration may be made.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Do not push the final completion commit.

---

# 1. Why C34/S0A is the exact next package

C33 creates a distinct baryon-number-zero root:

```text
C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT
```

which shares neither a state vector nor a probability normalization with the baryon-number-one C32 collinear root:

```text
C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION.
```

The vacuum soft factor is not a component of the C11 proton state.

The selected microscopic realization is frozen as:

```text
S0-FB-EIKONAL-FOCK
```

with:

```text
a unit-normalized B=0 vacuum
vacuum plus one-soft-gluon modes
both n and nbar rapidity regions
transverse mode identity
two physical transverse polarizations
adjoint color
four nondynamical eikonal color sources
fundamental/anti-fundamental line action
P/ANTI_P ordering
future orientation
lightlike and infinity segments
transverse closure
1/Nc singlet trace
modified-delta rapidity-regulator identity
explicit zero-mode status
```

The tree identities close:

\[
S_{\rm FB}^{(0)}(b)
=
\frac{1}{N_c}\operatorname{Tr}\mathbf 1
=
1,
\qquad
C_F=\frac{4}{3}.
\]

The structural soft basis has three nested resolutions:

```text
S0-R1:
    (N_omega,N_y,N_perp) = (4,6,5)
    (omega_min,omega_max,Y_max,L_perp,rho_0) = (0.01,4,3,8,0.001)
    dim(H_soft^(1)) = 3,841

S0-R2:
    (8,12,10)
    (0.005,8,6,16,0.0005)
    dim(H_soft^(1)) = 30,721

S0-R3:
    (12,18,15)
    (0.0033333333333333335,12,9,24,0.0003333333333333333)
    dim(H_soft^(1)) = 103,681
```

with boundary identity:

```text
FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT
```

and zero-mode policy:

```text
EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL
AUDIT_REQUIRED
```

C33 does not calculate a regulator-specific one-loop coefficient. All eighteen one-loop contributions remain:

```text
STRUCTURALLY_UNRESOLVED
NONZERO_UNKNOWN
```

so the strongest status is:

```text
C33_SOFT_TREE_LEVEL_ONLY.
```

The soft UV counterterm, rapidity counterterm, renormalized soft function, rapidity anomalous dimension, Collins-Soper kernel, finite-basis-to-continuum conversion, basis trajectory, soft-collinear compatibility, and zero-bin validation remain unavailable rather than zero.

C34 must perform the first actual one-loop calculation in the finite B=0 root.

---

# 2. Primary objective

Implement the chain:

```text
frozen C33 B=0 vacuum/eikonal root
    -> exact one-gluon eikonal-current operator
    -> cell-integrated finite-basis emission matrix elements
    -> complete one-loop real and virtual soft contributions
    -> line, cusp, endpoint, transverse-closure, zero-mode,
       basis-boundary, gauge, ghost, instantaneous, and vacuum terms
    -> bare finite-basis soft function
    -> UV-counterterm extraction
    -> modified-delta rapidity-counterterm extraction
    -> renormalized finite-basis soft function
    -> rapidity anomalous dimension and Collins-Soper convention
    -> continuum modified-delta target oracle
    -> finite-basis-to-continuum soft conversion
    -> three-resolution regulator trajectory
    -> soft-side zero-bin limit and collinear-continuation contract
```

At declared one-loop order:

\[
S_{\rm FB}^{\rm bare}
(b;\Lambda_{\rm soft},\delta^+,\delta^-,\xi_g)
=
1+a_s\,S_{\rm FB}^{(1),\rm bare}
+\mathcal O(a_s^2).
\]

The renormalized object is:

\[
S_{\rm FB}^{\rm ren}
=
Z_S^{\rm UV}\,
R_S^{\rm rap}\,
S_{\rm FB}^{\rm bare}.
\]

The finite-regulator relation is:

\[
S_{\rm cont}^{\rm ren}
=
Z_{\rm FB\to cont}^{S}
\,
S_{\rm FB}^{\rm ren}
+
R_{\rm FB\to cont}^{S}.
\]

C34 must determine rather than assume:

```text
which one-loop line-pair contributions are nonzero in the finite regulator;
which target-scheme scaleless terms become finite-regulator counterterms;
whether the one-gluon finite basis reproduces the complete O(g^2) Wilson expansion;
whether the direct mode sum preserves gauge independence;
whether the modified-delta rapidity logarithms are reproduced;
whether line, cusp, endpoint, and transverse-closure divergences separate;
whether exact-zero-mode exclusion leaves a universal finite remainder;
whether a state-independent soft conversion exists;
whether the three-resolution sequence resolves logarithmic, finite, and
power-suppressed pieces;
whether the C32 off-shell collinear plan can consume the C34 soft limit
without an unproved zero-bin equivalence.
```

A positive result is not assumed.

---

# 3. Scientific boundary

C34 is:

```text
B=0 vacuum specific
quark fundamental soft-function specific
one-loop targeted
direct finite-eikonal-Fock primary
modified-delta rapidity regulated
UV and rapidity explicit
distribution and path-sign explicit
finite-basis and cell-integration explicit
zero-mode explicit
basis-trajectory aware
state and hadron independent
validation only
non-inferential
```

C34 is not:

```text
a modification of the proton state
a completed proton TMD
a completed LF-to-project matching kernel
a fitted soft factor
an ART25 refit
a bridge residual fit
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a process prediction
a deuteron prediction
a gluon-representation soft function
a T-odd process package
a production promotion
```

The continuum result is a target oracle. It is not the finite-basis result.

The auxiliary-field route remains an independent methodological oracle unless C34 proves its exact Minkowski/light-front, path, and modified-delta identity.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all C5-C34 Wilson, soft, cut, regulator, light-front, matching, bridge, source, formal-volume, test, API, manifest, ADR, and roadmap files before changing code.

Continue autonomously until every applicable C34 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect all repository source and git history;
- preserve additional primary sources and ancillaries;
- derive the one-loop Wilson expansion;
- build symbolic eikonal currents and color contractions;
- integrate finite momentum/rapidity cells;
- construct sparse or matrix-free one-gluon operators;
- execute all three soft-basis resolutions;
- derive and fit only source-predicted cutoff structures;
- compute UV and rapidity counterterms;
- run gauge, path, color, regulator, and continuum checks;
- rebuild deterministic manifests.

Do not:

- contact authors;
- alter C11, C32, C33, ARTEMIDE, or ART25;
- insert the vacuum soft state into proton normalization;
- use ART25 members, data, chi2, or bridge residuals;
- tune counterterms to the twelve proton bridge points;
- copy the continuum coefficient as the finite-basis coefficient;
- declare a missing graph scaleless without evaluating its finite-regulator status;
- create a proton TMD export;
- rerun the twelve-point bridge;
- create a likelihood or posterior;
- modify production;
- push the completion commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 5.1 Wilson, cut, sign, and overlap roots

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md
docs/next_level/c5_benchmark_manifest.json

docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c6_benchmark_manifest.json

docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
```

## 5.2 Microscopic collinear/operator roots

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md

docs/next_level/c31_implementation_report.md
docs/next_level/c31_three_layer_identity_manifest.json
docs/next_level/c31_continuum_scheme_equivalence_matrix.json
docs/next_level/c31_source_sufficiency_decision.json

docs/next_level/c32_implementation_report.md
docs/next_level/c32_api.md
docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_regulator_plan_manifest.json
docs/next_level/c32_partonic_external_state_plan.json
docs/next_level/c32_gauge_plan.json
docs/next_level/c32_rapidity_plan.json
docs/next_level/c32_partonic_diagram_ledger.json
docs/next_level/c32_counterterm_ledger.json
docs/next_level/c32_zero_bin_overlap_manifest.json
docs/next_level/c32_source_sufficiency_decision.json
```

## 5.3 C33 structural soft root

```text
docs/next_level/c33_implementation_report.md
docs/next_level/c33_api.md
docs/next_level/c33_requirement_coverage.json
docs/next_level/c33_normative_source_integration.json
docs/next_level/c33_primary_source_manifest.json
docs/next_level/c33_source_relevance_matrix.json

docs/next_level/c33_two_root_tmd_identity.json
docs/next_level/c33_soft_collinear_provenance_graph.json
docs/next_level/c33_soft_sector_plan_manifest.json
docs/next_level/c33_soft_sector_plan_selection.json

docs/next_level/c33_vacuum_hilbert_manifest.json
docs/next_level/c33_soft_basis_manifest.json
docs/next_level/c33_soft_zero_mode_policy.json
docs/next_level/c33_soft_basis_trajectory_plan.json

docs/next_level/c33_eikonal_color_space.json
docs/next_level/c33_four_line_operator_manifest.json
docs/next_level/c33_eikonal_path_reversal_report.json
docs/next_level/c33_soft_rapidity_regulator_manifest.json
docs/next_level/c33_eikonal_denominator_report.json

docs/next_level/c33_soft_diagram_ledger.json
docs/next_level/c33_soft_counterterm_ledger.json
docs/next_level/c33_soft_dependency_graph.json
docs/next_level/c33_bare_soft_factor.json
docs/next_level/c33_bare_soft_oracle_report.json

docs/next_level/c33_soft_collinear_regulator_pair.json
docs/next_level/c33_soft_collinear_compatibility_report.json
docs/next_level/c33_zero_bin_interface_contract.json
docs/next_level/c33_c32_continuation_gate.json

docs/next_level/c33_source_sufficiency_decision.json
docs/next_level/c33_no_go_decision_tree.json
docs/next_level/c33_missing_calculation_specification.md
docs/next_level/c33_unresolved_physics_gaps.md
```

## 5.4 Continuum matching/evolution roots

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
```

## 5.5 Formal sources

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

Use actual filenames when they differ. Never invent an absent source.

Create:

```text
docs/next_level/c34_normative_source_integration.json
```

When Volume XXI is present, create:

```text
docs/next_level/c34_volume_xxi_requirement_crosswalk.json
```

mapping all stable Volume XXI requirements to existing or C34 evidence without changing the scientific meaning of the volume.

---

# 6. Required primary-source and derivation authority

Reuse all C31-C33 source locks. Preserve any new source under:

```text
data/raw/c34_sources/
```

with exact version and SHA-256 identity.

At minimum retain the exact authority classes:

```text
TARGET_MODIFIED_DELTA_SOFT_AUTHORITY
RAPIDITY_RENORMALIZATION_AUTHORITY
ZERO_BIN_AUTHORITY
FINITE_REGULATOR_METHOD_AUTHORITY
LIGHT_FRONT_VACUUM_METHOD_AUTHORITY
AUXILIARY_FIELD_METHOD_AUTHORITY
NOT_OPERATOR_REGULATOR_IDENTICAL
```

Every C34-derived expression must record:

```text
derivation ID
Wilson-line pair
orientation
color action
Fourier convention
momentum flow
i0 and delta signs
gauge
rapidity regulator
UV regulator
finite-cell basis
perturbative order
symbolic-expression hash
generated-code hash
independent oracle
```

Create:

```text
docs/next_level/c34_primary_source_manifest.json
docs/next_level/c34_derivation_authority_manifest.json
```

---

# 7. Immutable C33 baseline

Before edits, reproduce and record:

```text
1,196 tests
33 builders
39/39 evidence rows
165/165 atlas pages
2,140 C33 requirements
2,040/2,040 C33 injections
92 C33 fault modes

C28-C33 validators passing
deterministic C33 regeneration

roots:
    C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION, B=1
    C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT, B=0

selected plan:
    S0-FB-EIKONAL-FOCK

tree:
    S_FB^(0)=1
    C_F=4/3

soft resolutions:
    dimensions 3,841; 30,721; 103,681
    exact C33 resolution tuples and support

boundary:
    FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT

zero mode:
    EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL
    AUDIT_REQUIRED

four Wilson paths:
    S_n^dagger(b)
    S_nbar(b)
    S_nbar^dagger(0)
    S_n(0)

rapidity:
    modified delta
    delta+ and delta- distinct
    signs derived from stored conventions

one-loop:
    18 required classes
    all STRUCTURALLY_UNRESOLVED
    all NONZERO_UNKNOWN

status:
    C33_SOFT_TREE_LEVEL_ONLY
    SOFT_TRAJECTORY_UNAVAILABLE
    SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED
    zero-bin DEFINED_NOT_VALIDATED
    C32 continuation gate false

bridge:
    12 BRIDGE_COMMON_DOMAIN_ONLY
    0 ready
    no microscopic export
    no rerun

integrity:
    all 642 ART25 identities unchanged
    NO_JOINT_MEASURE
    216 production routes
    eight authoritative artifacts
    MSHT20_REP outside Git
```

Do not proceed if this baseline does not reproduce.

C34 must not modify:

- C11;
- the C32 operator-completion root or tree reduction;
- the C33 root, basis identities, path identities, or tree identity;
- the C29-C33 bridge grid, roles, and holdouts;
- any ART25 object;
- historical C33 no-go records in place;
- production registry or authoritative artifacts.

Create versioned C34 one-loop descendants and supersession edges only.

---

# 8. Required C34 architecture

Implement or extend immutable objects equivalent to:

```text
SoftOneLoopPlan
SoftOneLoopOrder
SoftModeCellId
SoftModeQuadrature
SoftModeCompletenessRecord

EikonalCurrent
EikonalEmissionVertex
EikonalAbsorptionVertex
EikonalPairKernel
EikonalSelfKernel
TransverseClosureKernel

SoftVirtualAmplitude
SoftRealAmplitude
SoftCutLedger
SoftRealVirtualAssembly

SoftGaugeContribution
SoftGhostContribution
SoftInstantaneousContribution
SoftZeroModeContribution
SoftBoundaryContribution

SoftBareCoefficient
SoftBareCoefficientDecomposition
SoftUVStructure
SoftRapidityStructure

SoftUVCountertermSolution
SoftRapidityCountertermSolution
SoftRenormalizedCoefficient

SoftRapidityDerivative
SoftCuspConsistency
SoftCSKernelRecord

SoftContinuumTargetRecord
SoftFiniteRegulatorDifference
SoftFiniteRegulatorKernel
SoftRoundTripReport

SoftResolutionSequence
SoftTrajectoryFitPlan
SoftTrajectoryHoldout
SoftTrajectoryResult

SoftSideZeroBinLimit
SoftCollinearContinuationContract
C34SoftCapabilityMatrix
C34ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministically serialized;
- explicit about B=0 root ownership;
- explicit about path and color;
- explicit about mode-cell and quadrature identity;
- explicit about UV, IR, rapidity, gauge, and zero-mode status;
- explicit about first omitted order;
- state and hadron independent;
- independent of ART25;
- unreachable from inference and production.

---

# 9. Freeze the one-loop calculation plan

Before calculating a coefficient, freeze:

```text
primary soft realization:
    S0-FB-EIKONAL-FOCK

perturbative order:
    O(g^2) / O(a_s)

Wilson geometry:
    exact C33 four-line trace order

color:
    SU(3), fundamental quark soft function

gauge:
    covariant xi_g checks at 0, 1, 2

rapidity:
    exact C33 modified-delta plan

UV target:
    declared project/MS-bar soft convention

soft basis:
    exact C33 R1, R2, R3 records

zero mode:
    exact C33 policy

b-space points:
    frozen before results

delta+ and delta- trajectories:
    frozen before results

quadrature:
    source-independent and frozen

trajectory ansatz:
    only source-predicted logs, finite constants, and power terms
```

Freeze at least one resolution, one \(b\) point, one rapidity-regulator point, and one gauge point as holdouts not used in any counterterm/trajectory determination.

Create:

```text
docs/next_level/c34_one_loop_plan.json
docs/next_level/c34_mode_quadrature_plan.json
docs/next_level/c34_trajectory_fit_plan.json
```

---

# 10. Eikonal current and one-gluon matrix elements

Construct the one-gluon eikonal emission current from the four stored lines.

Schematically:

\[
J_a^\mu(k;b)
=
g\sum_{\ell=1}^{4}
\mathcal T_\ell^a\,
\sigma_\ell\,
v_\ell^\mu\,
e^{i\bm k_T\cdot\bm x_{\ell T}}\,
D_\ell(k;\delta^\pm,i0),
\]

where every factor is derived from the stored line record.

For every line retain:

```text
fundamental or anti-fundamental action
orientation
P or ANTI_P order
direction n or nbar
transverse position 0 or b
momentum-flow convention
emission/absorption convention
delta+ or delta-
i0 sign
complex conjugation
```

Calculate cell-integrated matrix elements:

\[
\langle g_{\lambda,\nu}^a|
J\cdot A
|\Omega\rangle
\]

rather than evaluating a singular integrand only at cell centers.

Required checks:

- zero-coupling limit;
- line conjugation;
- path reversal;
- color trace;
- Ward contraction;
- direct matrix and sparse/matrix-free action;
- cell-normalization completeness;
- regulator-sign derivation;
- no physical numerical epsilon.

Create:

```text
docs/next_level/c34_eikonal_current_manifest.json
docs/next_level/c34_one_gluon_vertex_manifest.json
docs/next_level/c34_mode_cell_integration_report.json
```

---

# 11. Complete one-loop contribution calculation

Resolve every C33 one-loop slot.

At minimum calculate or prove non-applicability for:

```text
N_NBAR_EXCHANGE
CONJUGATE_LINE_EXCHANGE
SAME_DIRECTION_LINE_EXCHANGE
REAL_ONE_SOFT_GLUON
VIRTUAL_ONE_SOFT_GLUON
WILSON_LINE_SELF_ENERGY
CUSP_ENDPOINT
TRANSVERSE_CLOSURE
AUXILIARY_FIELD_SELF_ENERGY
SOFT_VACUUM_ENERGY
LIGHT_FRONT_INSTANTANEOUS
GAUGE_FIXING
GHOST
ZERO_MODE
BASIS_BOUNDARY
RAPIDITY_COUNTERTERM
UV_COUNTERTERM
RESIDUAL_LINE_MASS_COUNTERTERM
```

A target-scheme graph that is scaleless in dimensional regularization may still produce a finite-regulator logarithm, power divergence, or counterterm. Its C34 status must be calculated.

Allowed contribution statuses:

```text
CALCULATED_NONZERO
CALCULATED_ZERO_BY_EXACT_IDENTITY
CANCELS_WITH_DECLARED_PARTNER
TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO
NOT_APPLICABLE_WITH_PROOF
UNRESOLVED_BLOCKING
```

Create:

```text
docs/next_level/c34_soft_diagram_results.json
docs/next_level/c34_soft_counterterm_results.json
docs/next_level/c34_one_loop_dependency_closure.json
```

No one-loop readiness status may be issued while a required contribution remains `UNRESOLVED_BLOCKING`.

---

# 12. Real, virtual, and count-once assembly

Construct the one-loop coefficient independently through:

1. Wilson-operator expansion and vacuum contraction;
2. one-gluon mode-sum/cut assembly.

Retain:

```text
real support
virtual support
line-pair identity
cut identity
mode-cell identity
b-dependent phase
delta-regulator identity
```

The authoritative assembly must prevent:

```text
real/virtual double counting
conjugate-line double counting
line-self-energy duplication
soft/cusp duplication
numerical epsilon as support
```

Required checks:

- direct versus mode-sum equality;
- missing-real residual;
- missing-virtual residual;
- duplicate-cut residual;
- future/past equality;
- Hermitian conjugation;
- \(b\)-rotation covariance.

Create:

```text
docs/next_level/c34_real_virtual_assembly.json
docs/next_level/c34_soft_cut_ledger.json
docs/next_level/c34_count_once_report.json
```

---

# 13. Bare finite-basis soft coefficient

Construct:

\[
S_{\rm FB}^{(1),\rm bare}
=
S_{\rm exchange}
+
S_{\rm real}
+
S_{\rm virtual}
+
S_{\rm line}
+
S_{\rm cusp}
+
S_{\rm transverse}
+
S_{\rm inst}
+
S_{\rm zero}
+
S_{\rm boundary}
+
S_{\rm vacuum}.
\]

Report every component separately as a function of:

```text
b
mu reference
delta+
delta-
xi_g
soft resolution
UV support
IR support
rapidity support
zero-mode policy
```

Do not force \(S(b=0)=1\) beyond the exact source convention. Record the controlled \(b\to0\) behavior instead.

Create:

```text
docs/next_level/c34_bare_soft_coefficient.json
docs/next_level/c34_bare_soft_decomposition.json
docs/next_level/c34_bare_soft_validation_report.json
```

---

# 14. Continuum modified-delta target oracle

Reconstruct the source-qualified one-loop continuum soft coefficient in the exact target convention.

Retain analytically and separately:

```text
UV poles/logs
rapidity logs
b-space logarithms
finite constants
color factor
gauge status
line/cusp decomposition where source-defined
```

Use two independent routes:

```text
source expression transcription
direct symbolic/integral reconstruction
```

Required checks:

- expression hash;
- source locator;
- convention alignment;
- derivative checks;
- known anomalous dimensions;
- no use of C19-C22 validation polynomials as a substitute.

Create:

```text
docs/next_level/c34_continuum_soft_target.json
docs/next_level/c34_continuum_soft_oracle_report.json
```

---

# 15. UV structure and counterterms

Separate finite-regulator behavior into:

\[
S_{\rm FB}^{(1),\rm bare}
=
A_{\rm power}(\Lambda_{\rm soft})
+
A_{\log}\ln\Lambda_{\rm soft}
+
A_{\rm cusp}\ln^2(\mu b)
+
A_{\rm rap}\ln(\delta^+\delta^-)
+
A_{\rm finite}
+
R_{\rm power}.
\]

The exact decomposition may differ, but all distinct structures must remain visible.

Solve state-independent counterterms for:

```text
Wilson-line self energy
cusp/endpoint
transverse closure
residual line mass
vacuum energy where applicable
soft operator UV factor
```

Do not hide a linear or power divergence inside a logarithmic MS counterterm.

Required checks:

- source-predicted UV coefficient;
- gauge independence after assembly;
- resolution behavior;
- holdout resolution;
- inverse counterterm;
- first omitted order.

Create:

```text
docs/next_level/c34_soft_uv_structure.json
docs/next_level/c34_soft_uv_counterterm_solution.json
docs/next_level/c34_soft_uv_closure_report.json
```

---

# 16. Modified-delta rapidity renormalization

Retain \(\delta^+\) and \(\delta^-\) independently through the bare calculation.

Extract the rapidity counterterm in the declared convention:

\[
S_{\rm FB}^{\rm ren}
=
Z_S^{\rm UV}
R_S^{\rm rap}
S_{\rm FB}^{\rm bare}.
\]

Required checks:

- correct line-conjugation behavior;
- future/past equality;
- cancellation of regulator dependence at declared order;
- regulator-removal order;
- derivative with respect to the exact rapidity variable;
- gauge independence;
- no fitted nonperturbative CS term;
- no identification of finite basis with the rapidity regulator.

Create:

```text
docs/next_level/c34_soft_rapidity_structure.json
docs/next_level/c34_soft_rapidity_counterterm_solution.json
docs/next_level/c34_rapidity_renormalization_closure.json
```

---

# 17. Rapidity anomalous dimension and cusp consistency

Extract the source-convention rapidity anomalous dimension only after UV and rapidity closure.

Record the exact derivative convention.

Test the consistency relation between the \(\mu\) derivative of the rapidity anomalous dimension and the quark cusp anomalous dimension.

Keep distinct:

```text
soft rapidity anomalous dimension
TMD rapidity anomalous dimension
Collins-Soper D convention
ART25 nonperturbative CS model
```

No ART25 fit value may enter the calculation.

Create:

```text
docs/next_level/c34_soft_rapidity_anomalous_dimension.json
docs/next_level/c34_cusp_consistency_report.json
docs/next_level/c34_soft_cs_kernel_convention.json
```

---

# 18. Finite-basis-to-continuum soft conversion

Calculate:

\[
Z_{\rm FB\to cont}^{S,(1)}
=
S_{\rm cont}^{(1),\rm ren}
-
S_{\rm FB}^{(1),\rm ren}
\]

in the exact finite-regulator relation appropriate to the selected representation.

The conversion must be:

```text
vacuum-state independent
hadron independent
flavor independent for the quark fundamental soft sector where proved
ART25-member independent
gauge independent
explicit in resolution and regulator
explicit in first omitted order
```

Separate:

```text
logarithmic conversion
finite constant
power correction
zero-mode remainder
endpoint remainder
transverse-closure remainder
numerical remainder
```

Required checks:

- inverse map;
- round trip;
- continuum-oracle recovery;
- gauge closure;
- rapidity-anomalous-dimension closure;
- holdout resolution;
- no target-data fitting.

Create:

```text
docs/next_level/c34_soft_regulator_conversion.json
docs/next_level/c34_soft_regulator_roundtrip.json
docs/next_level/c34_soft_conversion_remainder.json
```

---

# 19. Three-resolution trajectory

Execute the exact C33 resolutions R1-R3.

If a fit contains more free trajectory coefficients than can be determined by the three points, reduce the ansatz using source-predicted structure or add a fourth independently frozen resolution before fitting. Do not overfit three points.

Separate:

```text
UV logarithm
rapidity-window dependence
IR/fixed-volume dependence
transverse discretization
finite constant
power correction
zero-mode control
endpoint/junction effect
quadrature error
```

At least one resolution or one regulator combination must remain a holdout.

Allowed statuses:

```text
SOFT_CONTINUUM_TRAJECTORY_RESOLVED
SOFT_LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
SOFT_FINITE_BASIS_ONLY
SOFT_NONUNIVERSAL_TRAJECTORY
SOFT_TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c34_soft_basis_trajectory.json
docs/next_level/c34_soft_trajectory_holdout_report.json
docs/next_level/c34_soft_continuum_extrapolation.json
```

---

# 20. Zero modes, endpoints, and transverse closure

The C33 zero-mode policy remains immutable.

Evaluate the separate zero-mode control sufficiently to determine whether it contributes to:

```text
line self energy
rapidity logarithm
cusp/endpoint term
Ward identity
continuum finite constant
```

A missing zero-mode calculation cannot be called zero.

Audit transverse closure and infinity-junction contributions separately from lightlike segments.

Create:

```text
docs/next_level/c34_zero_mode_contribution_report.json
docs/next_level/c34_endpoint_transverse_closure_report.json
```

---

# 21. Auxiliary-field cross-check

The auxiliary-field route remains:

```text
SOURCE_ORACLE_ONLY
```

unless C34 implements and proves the necessary conversion.

When available, compare:

```text
path composition
line orientation
endpoint renormalization
residual-line-mass term
one-loop coefficient
```

Do not add direct and auxiliary results.

Create:

```text
docs/next_level/c34_auxiliary_soft_crosscheck.json
```

---

# 22. Soft-side zero-bin limit and C32 continuation contract

C34 does not calculate the full C32 collinear one-loop correlator.

It must, however, construct an executable soft-side limit object suitable for a later zero-bin comparison.

Define:

\[
\operatorname{SOFT\_LIMIT}_{\rm C34}
\]

with the same:

```text
measurement
b coordinate
rapidity convention
UV target
gauge convention
off-shell IR variables where meaningful
regulator-removal order
```

as the frozen C32 collinear plan, or provide an explicit conversion contract.

Because Idilbi–Mehen does not establish automatic soft/zero-bin equivalence for the frozen off-shell IR plan, do not issue zero-bin validation from citation alone.

Allowed interface statuses:

```text
SOFT_SIDE_ZERO_BIN_OBJECT_READY
SOFT_COLLINEAR_EXACT_CONVERSION_READY
SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST
SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED
SOFT_COLLINEAR_INCOMPATIBLE
```

Create:

```text
docs/next_level/c34_soft_side_zero_bin_limit.json
docs/next_level/c34_soft_collinear_continuation_contract.json
docs/next_level/c34_c32_continuation_gate.json
```

The C32 continuation gate may become true only for starting the subsequent collinear calculation. It does not validate the collinear zero-bin equality in advance.

---

# 23. Tensor-network and quantum representation

Instantiate the C33 soft tensor-network contract where useful.

The network must preserve:

```text
vacuum root
one-gluon mode
rapidity region
transverse cell
polarization
adjoint color
four eikonal color legs
singlet trace
real/virtual branch
```

Compare full contraction and any compressed representation on the soft coefficient itself.

Bond dimension is a deterministic numerical axis, not a statistical member.

Update the future PennyLane/QTN interface contract without executing a fit.

Create:

```text
docs/next_level/c34_soft_tensor_network_execution.json
docs/next_level/c34_soft_quantum_interface_update.json
```

---

# 24. Uncertainty and remainder separation

Keep separate:

```text
first omitted perturbative order
UV-counterterm truncation
rapidity-counterterm truncation
finite-basis UV remainder
finite-basis IR remainder
rapidity-window remainder
zero-mode remainder
endpoint/cusp remainder
transverse-closure remainder
residual-line-mass remainder
basis-boundary remainder
finite-basis-to-continuum conversion remainder
soft-collinear compatibility remainder
zero-bin-interface remainder
auxiliary-field representation remainder
quadrature and floating-point error
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No soft uncertainty may be absorbed into:

```text
ART25 covariance
the proton state
a fitted TMD normalization
the future LF-to-project matching kernel
```

Create:

```text
docs/next_level/c34_soft_uncertainty_budget.json
docs/next_level/c34_soft_remainder_separation.json
```

---

# 25. Scientifically valid no-go outcomes

C34 must support rigorous negative outcomes.

## 25.1 One-loop diagram incompleteness

```text
C34_SOFT_ONE_LOOP_INCOMPLETE
```

when a required graph or counterterm remains unresolved.

## 25.2 Gauge obstruction

```text
C34_SOFT_GAUGE_CLOSURE_FAILED
```

when the assembled coefficient retains gauge dependence beyond the declared remainder.

## 25.3 Rapidity obstruction

```text
C34_SOFT_RAPIDITY_RENORMALIZATION_UNRESOLVED
```

when modified-delta dependence cannot be removed consistently.

## 25.4 Zero-mode obstruction

```text
C34_SOFT_ZERO_MODE_COMPLETION_REQUIRED
```

when the excluded control contributes to required closure.

## 25.5 Trajectory obstruction

```text
C34_SOFT_CONTINUUM_TRAJECTORY_UNRESOLVED
```

when logarithmic, finite, and power pieces cannot be separated.

## 25.6 Regulator-conversion obstruction

```text
C34_SOFT_REGULATOR_CONVERSION_UNAVAILABLE
```

when a finite-basis result exists but no universal continuum conversion closes.

## 25.7 Soft-collinear incompatibility

```text
C34_SOFT_COLLINEAR_REGULATORS_INCOMPATIBLE
```

when no operator-identical overlap test can be formulated.

Every no-go result must specify the exact missing calculation.

Create:

```text
docs/next_level/c34_source_sufficiency_decision.json
docs/next_level/c34_no_go_decision_tree.json
docs/next_level/c34_missing_calculation_specification.md
```

---

# 26. Holdouts

Freeze holdouts before symbolic simplification, counterterm solution, trajectory fitting, or regulator conversion.

Reserve at least:

```text
one n-nbar line-pair coefficient
one conjugate-line coefficient
one same-direction contribution
one real contribution
one virtual contribution
one Wilson self-energy coefficient
one cusp/endpoint coefficient
one transverse-closure coefficient
one gauge xi value
one delta+ variation
one delta- variation
one b point
one b-to-zero controlled point
one zero-mode control
one basis-boundary coefficient
one UV-counterterm coefficient
one rapidity-counterterm coefficient
one rapidity-anomalous-dimension coefficient
one continuum-oracle finite constant
one finite-regulator round trip
one soft resolution
one auxiliary/direct comparison
one soft-side zero-bin object
one ART25-independence control
```

No failed holdout may be moved into construction or fitting.

---

# 27. Required benchmark families

Implement at least:

## S0A-A: immutable C33 root and plan

- B=0/B=1 separation;
- exact plan;
- no state mixing.

## S0A-B: eikonal current

- all four lines;
- color;
- signs;
- cell-integrated matrix elements.

## S0A-C: mode basis and quadrature

- normalization;
- completeness;
- singular-cell treatment;
- resolution identity.

## S0A-D: line-pair contribution closure

- n-nbar;
- conjugate;
- same-direction;
- self energies.

## S0A-E: real/virtual count once

- direct Wilson expansion;
- mode-sum route;
- cut ledger.

## S0A-F: cusp, endpoint, and transverse closure

- separate identities;
- no duplicate counterterm.

## S0A-G: gauge, ghost, and instantaneous terms

- explicit decisions;
- gauge closure.

## S0A-H: zero mode and basis boundary

- explicit control;
- no silent zero.

## S0A-I: bare soft coefficient

- component decomposition;
- b and regulator dependence.

## S0A-J: continuum modified-delta oracle

- source expression;
- independent reconstruction.

## S0A-K: UV renormalization

- power/log separation;
- counterterms;
- anomalous dimension.

## S0A-L: rapidity renormalization

- delta dependence;
- counterterm;
- removal order.

## S0A-M: cusp and CS consistency

- rapidity derivative;
- mu derivative;
- convention identity.

## S0A-N: finite-regulator conversion

- inverse;
- round trip;
- state independence.

## S0A-O: basis trajectory

- R1-R3;
- holdout;
- no overfit.

## S0A-P: soft-side zero-bin readiness

- common measurement;
- exact interface;
- no premature equality.

## S0A-Q: continuation/no-go decision

- exact status;
- exact next branch;
- no proton export.

## S0A-R: deterministic isolation

- no ART25 use;
- no fit;
- no production mutation.

---

# 28. Negative injections

Create at least **2,240 ordered C34 negative injections** with stable IDs and deterministic diagnostics.

Include:

## Baseline and root identity

- invented C33 commit;
- C33 baseline not reproduced;
- B=0 soft state inserted into proton normalization;
- C33 path record modified;
- C33 tree identity overwritten.

## Eikonal current

- line omitted;
- conjugate action wrong;
- path order lost;
- transverse position lost;
- wrong delta regulator assigned;
- i0 sign inserted manually;
- color action transposed incorrectly;
- cell center used across a singular cell without integration.

## Mode basis

- one-gluon normalization wrong;
- rapidity regions aliased;
- polarization dropped;
- adjoint color dropped;
- zero mode silently included;
- zero mode silently discarded;
- basis completeness inferred from one resolution.

## One-loop diagrams

- real graph omitted;
- virtual graph omitted;
- same-direction graph declared scaleless by continuum analogy;
- self energy omitted;
- cusp omitted;
- endpoint omitted;
- transverse closure omitted;
- ghost/gauge term omitted;
- instantaneous term omitted;
- vacuum energy omitted;
- basis-boundary term omitted.

## Count once

- real contribution duplicated;
- virtual contribution duplicated;
- conjugate pair double counted;
- cut support duplicated;
- soft factor squared accidentally;
- inverse square root applied twice.

## UV renormalization

- power divergence hidden in log;
- linear divergence dropped;
- line-mass counterterm omitted;
- cusp counterterm duplicated;
- UV factor tuned to continuum finite constant;
- holdout resolution used in counterterm determination.

## Rapidity renormalization

- delta+ and delta- aliased;
- regulator removed before assembly;
- rapidity log absorbed into UV factor;
- zeta prescription confused with bare regulator;
- CS model imported from ART25;
- gauge dependence hidden in rapidity counterterm.

## Continuum conversion

- continuum result copied as finite result;
- finite constant fitted to ART25;
- inverse map absent;
- round-trip failure hidden;
- one resolution called continuum;
- arbitrary polynomial trajectory;
- first omitted order set to zero.

## Zero modes and endpoints

- zero-mode control ignored;
- endpoint contribution merged with cusp without identity;
- transverse junction omitted;
- zero-mode sensitivity called numerical noise.

## Soft-collinear interface

- zero-bin equality claimed from citation alone;
- off-shell IR issue ignored;
- different measurements accepted;
- different b conventions accepted;
- collinear one-loop coefficients fabricated;
- valid soft sector called complete TMD.

## Scope leakage

- microscopic proton TMD exported;
- twelve-point bridge rerun;
- residual called likelihood;
- p-value reported;
- calibration performed;
- member reweighted;
- emulator trained;
- process/deuteron/gluon/T-odd status promoted.

## Integrity

- ART25 member used;
- ART25 data or chi2 used;
- raw MSHT files committed;
- production registry changed;
- authoritative artifact changed;
- nondeterministic manifest.

---

# 29. Deliverables

Create at least:

```text
docs/next_level/c34_implementation_report.md
docs/next_level/c34_api.md
docs/next_level/c34_requirement_coverage.json
docs/next_level/c34_normative_source_integration.json
docs/next_level/c34_primary_source_manifest.json
docs/next_level/c34_derivation_authority_manifest.json

docs/next_level/c34_one_loop_plan.json
docs/next_level/c34_mode_quadrature_plan.json
docs/next_level/c34_trajectory_fit_plan.json

docs/next_level/c34_eikonal_current_manifest.json
docs/next_level/c34_one_gluon_vertex_manifest.json
docs/next_level/c34_mode_cell_integration_report.json

docs/next_level/c34_soft_diagram_results.json
docs/next_level/c34_soft_counterterm_results.json
docs/next_level/c34_one_loop_dependency_closure.json

docs/next_level/c34_real_virtual_assembly.json
docs/next_level/c34_soft_cut_ledger.json
docs/next_level/c34_count_once_report.json

docs/next_level/c34_bare_soft_coefficient.json
docs/next_level/c34_bare_soft_decomposition.json
docs/next_level/c34_bare_soft_validation_report.json

docs/next_level/c34_continuum_soft_target.json
docs/next_level/c34_continuum_soft_oracle_report.json

docs/next_level/c34_soft_uv_structure.json
docs/next_level/c34_soft_uv_counterterm_solution.json
docs/next_level/c34_soft_uv_closure_report.json

docs/next_level/c34_soft_rapidity_structure.json
docs/next_level/c34_soft_rapidity_counterterm_solution.json
docs/next_level/c34_rapidity_renormalization_closure.json

docs/next_level/c34_soft_rapidity_anomalous_dimension.json
docs/next_level/c34_cusp_consistency_report.json
docs/next_level/c34_soft_cs_kernel_convention.json

docs/next_level/c34_soft_regulator_conversion.json
docs/next_level/c34_soft_regulator_roundtrip.json
docs/next_level/c34_soft_conversion_remainder.json

docs/next_level/c34_soft_basis_trajectory.json
docs/next_level/c34_soft_trajectory_holdout_report.json
docs/next_level/c34_soft_continuum_extrapolation.json

docs/next_level/c34_zero_mode_contribution_report.json
docs/next_level/c34_endpoint_transverse_closure_report.json
docs/next_level/c34_auxiliary_soft_crosscheck.json

docs/next_level/c34_soft_side_zero_bin_limit.json
docs/next_level/c34_soft_collinear_continuation_contract.json
docs/next_level/c34_c32_continuation_gate.json

docs/next_level/c34_soft_tensor_network_execution.json
docs/next_level/c34_soft_quantum_interface_update.json

docs/next_level/c34_soft_uncertainty_budget.json
docs/next_level/c34_soft_remainder_separation.json

docs/next_level/c34_source_sufficiency_decision.json
docs/next_level/c34_no_go_decision_tree.json
docs/next_level/c34_missing_calculation_specification.md

docs/next_level/c34_holdout_report.json
docs/next_level/c34_injection_manifest.json
docs/next_level/c34_regression_report.json
docs/next_level/c34_unresolved_physics_gaps.md
```

When Volume XXI is present, also create:

```text
docs/next_level/c34_volume_xxi_requirement_crosswalk.json
docs/next_level/architecture_decisions/<next>_c34_volume_xxi_integration.md
```

Add ADRs for:

- eikonal-current and cell-integration authority;
- finite-regulator scaleless-versus-nonzero decisions;
- real/virtual count-once assembly;
- UV power/log separation;
- modified-delta rapidity-counterterm authority;
- zero-mode and transverse-closure ownership;
- finite-basis soft conversion;
- trajectory fitting and holdout discipline;
- soft-side zero-bin readiness;
- exact C32 continuation and no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy mode-cell matrices, symbolic expressions, per-resolution arrays, and tensor-network tensors may remain outside Git under a declared content-addressed runtime directory. Commit their schemas, hashes, dimensions, resolution order, and deterministic reconstruction commands.

---

# 30. Acceptance criteria

C34/S0A is complete only when:

1. The actual clean C33 completion commit is resolved and recorded rather than invented.
2. The complete C33 baseline reproduces before edits.
3. The B=0 soft and B=1 collinear roots remain disjoint.
4. The C33 basis, path, rapidity, and tree identities remain unchanged.
5. The one-loop plan is frozen before results.
6. The quadrature/cell-integration plan is frozen before results.
7. Every eikonal line contributes through a typed current.
8. Singular cells are integrated rather than sampled naively.
9. Every required one-loop contribution receives a calculated or proved status.
10. No required finite-regulator contribution is called scaleless by continuum analogy alone.
11. Real and virtual contributions are counted once.
12. Color-trace normalization closes.
13. Future/past T-even equality closes when claimed.
14. Gauge dependence cancels when claimed.
15. The bare coefficient retains all regulator identities.
16. UV power and logarithmic structures remain separate.
17. UV counterterms are state independent.
18. Rapidity dependence is retained until the rapidity counterterm is applied.
19. Modified-delta regulator dependence cancels when claimed.
20. The rapidity anomalous dimension is extracted only from a closed calculation.
21. Cusp consistency is tested.
22. The continuum target oracle is independently reconstructed.
23. The continuum coefficient is not substituted for the finite-basis coefficient.
24. The finite-regulator conversion is hadron and ART25 independent.
25. Inverse and round-trip conversion are tested.
26. All three C33 resolutions are executed for any trajectory claim.
27. No trajectory is overfit.
28. At least one trajectory/regulator combination remains a holdout.
29. Zero-mode status is calculated or remains blocking.
30. Endpoint, cusp, and transverse-closure pieces remain separately auditable.
31. Auxiliary and direct routes remain alternatives.
32. The soft-side zero-bin object is explicit.
33. Off-shell soft/zero-bin equivalence is not assumed from citation.
34. A valid soft function is not called a completed microscopic TMD.
35. C34 creates no microscopic proton export.
36. C34 does not rerun the twelve-point bridge.
37. The C32 continuation gate is issued only at its exact supported scope.
38. All remainder classes remain separate.
39. Unknown remainder remains nonzero-unknown.
40. No ART25 object enters the derivation.
41. C29-C33 roles, holdouts, ancestry, and `NO_JOINT_MEASURE` remain unchanged.
42. All 642 ART25 identities and source covariance remain unchanged.
43. No fit, calibration, likelihood, posterior, optimization, reweighting, or emulator is created.
44. No process, deuteron, spin-1, gluon, T-odd, inference, or production status is promoted.
45. Every no-go result contains an exact missing-calculation specification.
46. All inherited tests, builders, requirements, injections, and manifests remain passing.
47. The production registry remains exactly 216 routes.
48. All eight authoritative artifacts remain byte-identical.
49. Raw transferred source files remain outside Git absent permission.
50. Every C34 negative injection yields the expected diagnostic.
51. All C34 manifests reproduce byte-for-byte.
52. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
53. A local completion commit is created and not pushed.

A rigorous negative result is valid. Do not weaken the soft-sector definition to obtain a positive continuation gate.

---

# 31. Outcome branches

## Branch A: one-loop soft sector closes

When:

```text
C34_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED
C34_SOFT_UV_RENORMALIZATION_VALIDATED
C34_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C34_SOFT_REGULATOR_CONVERSION_VALIDATED
C34_SOFT_SIDE_ZERO_BIN_OBJECT_READY
```

the exact next package is:

> **C35/R0B — microscopic one-loop collinear correlator, zero-bin comparison, UV/rapidity combination, and LF-to-project matching closure**

## Branch B: one-loop coefficient closes but trajectory remains unresolved

The exact next package is:

> **C35/S1 — soft-basis continuum trajectory, zero-mode, endpoint, and power-correction completion**

## Branch C: direct finite-Fock route fails but auxiliary route closes

The exact next package is:

> **C35/S2 — auxiliary-eikonal soft root validation and conversion to the finite-basis project regulator**

## Branch D: rapidity closure fails

The exact next package is:

> **C35/S0B — modified-delta rapidity-counterterm and gauge-closure completion**

## Branch E: zero-mode completion is required

The exact next package is:

> **C35/Z0 — finite-basis soft zero-mode and boundary-sector construction**

## Branch F: soft and collinear regulators are incompatible

The exact next package is:

> **C35/O3 — redesign of the microscopic collinear/soft regulator pair and overlap architecture**

## Branch G: required one-loop contributions remain incomplete

The exact next package is:

> **C35/S0C — targeted unresolved soft-diagram and counterterm completion**

No branch automatically authorizes fitting or inference.

---

# 32. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C34_ONE_LOOP_SOFT_PLAN_FROZEN
C34_EIKONAL_CURRENT_VALIDATED
C34_MODE_CELL_INTEGRATION_VALIDATED
C34_ONE_LOOP_SOFT_LEDGER_COMPLETE
C34_CONTINUUM_SOFT_ORACLE_VALIDATED
C34_SOFT_TRAJECTORY_AUDITED
C34_SOFT_SIDE_ZERO_BIN_OBJECT_DEFINED
C34_C32_CONTINUATION_GATE_DECIDED
C34_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when every exact gate passes:

```text
C34_FINITE_BASIS_SOFT_ONE_LOOP_VALIDATED
C34_SOFT_UV_RENORMALIZATION_VALIDATED
C34_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED
C34_SOFT_REGULATOR_CONVERSION_VALIDATED
C34_SOFT_CONTINUUM_TRAJECTORY_RESOLVED
C34_SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST
C34_SOFT_SECTOR_READY_FOR_COLLINEAR_MATCHING
```

The following remain forbidden:

```text
C34_MICROSCOPIC_PROTON_TMD_EXPORTED
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

- resolved C33 starting commit and final C34 commit;
- test, builder, evidence, atlas, requirement, injection, and fault-mode counts;
- Volume XXI presence and integration status;
- frozen one-loop and quadrature plans;
- eikonal-current identities;
- mode-cell and resolution dimensions;
- every one-loop contribution status;
- real/virtual and count-once residuals;
- bare soft coefficient and component values;
- UV power/log structure;
- UV-counterterm solution and residuals;
- modified-delta rapidity structure;
- rapidity-counterterm solution and residuals;
- gauge and future/past residuals;
- rapidity anomalous dimension and cusp-consistency status;
- continuum target-oracle residuals;
- finite-regulator conversion and round-trip residuals;
- basis-trajectory and holdout status;
- zero-mode, endpoint, cusp, and transverse-closure status;
- auxiliary-route comparison status;
- soft-side zero-bin status;
- soft-collinear continuation status;
- C32 continuation-gate status;
- exact no-go status when blocked;
- exact next-package branch;
- confirmation that no ART25 member, data, chi2, bridge residual, or proton-level ratio entered the calculation;
- confirmation that no microscopic TMD export, bridge rerun, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a continuum target coefficient, a structurally complete diagram ledger, or a tree-level identity as a completed one-loop finite-basis soft function.
