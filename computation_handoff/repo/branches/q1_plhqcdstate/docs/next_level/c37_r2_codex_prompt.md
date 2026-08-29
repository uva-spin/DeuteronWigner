# C37/R2 Codex Work Package

## Title

**Spacelike finite-rapidity partonic quark TMD, universal soft subtraction, and state-independent finite-basis light-front-to-project matching**

## Authoritative baseline

Start from the clean local C36/O4 completion commit whose abbreviated hash is:

```text
dee1dfb
```

The uploaded handoff does not provide the full hash. Do not invent it. Resolve and record it before edits:

```bash
git status --short
git rev-parse HEAD
git show -1 --oneline --stat
git merge-base --is-ancestor bbefd963ea14bf79884ec3a5c1a503581a6dd21e HEAD
```

The resolved `HEAD` is the authoritative C37 baseline only when it contains:

```text
docs/next_level/c36_implementation_report.md
docs/next_level/c36_continuation_gate.json
docs/next_level/c36_regulator_plan_selection.json
docs/next_level/c36_joint_root_identity.json
docs/next_level/c36_future_matching_strategy.json
handoff/ROADMAP.md
```

and the complete C36 baseline reproduces.

Required scientific ancestors include:

```text
C35/S0C:
    bbefd963ea14bf79884ec3a5c1a503581a6dd21e

C34/S0A:
    6bdb44be2afc79e817f69ce0e35813da8a394db7

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

Read and hash-audit it. Preserve its historical meaning. Add a versioned C36/C37 spacelike-regulator crosswalk or addendum rather than silently rewriting the earlier modified-delta implementation history.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git.

Create a local completion commit. Do not push.

---

# 1. Fixed scientific decision

C36 has already completed the regulator-family audit.

The physical regulator plan is frozen as:

```text
O4-SPACELIKE-COLLINS-JMY
```

with:

```text
finite, spacelike, non-lightlike Wilson directions
gauge covariance at finite rapidity
paired B=1 collinear and B=0 universal soft roots
complete transverse closure
source-qualified continuum tree/one-loop structural oracles
exact tree reduction to all twelve nonzero C11 u/d/ubar/dbar parents
```

C37 must not reopen the regulator survey merely because another scheme is easier to calculate.

The following are not competing physical soft factors:

```text
auxiliary-field representation
finite-length representation
exponential-regulator oracle
downstream project/EIS/ART25 convention
```

They are representation, comparison, or conversion records at their source-qualified scope.

C35 remains the immutable no-go certificate for the attempted finite-cell modified-delta microscopic regulator, including its finite-delta Ward defect. Do not overwrite or “repair” it.

C36 is architecture-ready only. It did not create:

```text
finite-basis one-loop matching
a microscopic proton TMD
a bridge calculation
ART25-based tuning
a fit
inference
production
```

C37 performs the first actual partonic matching calculation in the selected spacelike finite-rapidity architecture.

---

# 2. Primary objective

Calculate the same rank-zero quark TMD operator in two regulator realizations:

```text
A. selected continuum spacelike Collins/JMY scheme;

B. the C11/C36 finite-basis light-front collinear regulator,
   with the same finite-rapidity Wilson geometry and common IR prescription.
```

Use the universal B=0 soft factor outside the hadron tensor network.

The calculation chain is:

```text
C36 finite-rapidity operator identities
    -> frozen partonic external states and common IR regulator
    -> continuum unsubtracted spacelike quark correlator
    -> continuum universal spacelike soft factor
    -> continuum subtracted/renormalized quark TMD
    -> finite-basis unsubtracted partonic collinear correlator
    -> finite-basis UV and Hamiltonian/basis counterterms
    -> selected soft subtraction and overlap treatment
    -> distributional difference between the two renormalized objects
    -> state-independent LF-to-selected-scheme matching kernel
    -> selected-scheme-to-project conversion
    -> complete capability and hadron-application gate
```

The desired matching relation is:

\[
F_{q}^{\rm selected}(x,b_T;\mu,\zeta_v)
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

The kernel must be extracted from a common-IR partonic difference. It must never be obtained from:

```text
an ART25/microscopic ratio
a proton-level ratio
the twelve frozen bridge residuals
a fitted x- or b-dependent correction
a free normalization
```

---

# 3. Scope

C37 is:

```text
rank-zero
T-even
quark and positive-x antiquark aware
finite-rapidity spacelike Wilson-line specific
one-loop targeted
partonic
distributional in x
b-space first
gauge and Ward explicit
soft subtraction explicit
finite-basis resolution explicit
state-independence tested
validation only
non-inferential
```

C37 is not:

```text
a new regulator-family survey
a direct phenomenological TMD fit
an ART25 refit
a hadronic normalization fit
a final microscopic proton export by default
a twelve-point bridge comparison
a process calculation
a deuteron prediction
a gluon or T-odd matching package
a production promotion
```

The package may issue a validated **hadron-application gate**. Actual application to the microscopic proton and the frozen ART25 bridge belongs to the next package unless all conditional export requirements in Section 24 close exactly.

---

# 4. Autonomous execution and scientific discipline

Read all relevant C5-C37 operator, state, regulator, soft, matching, evolution, bridge, formal-volume, source, API, manifest, test, ADR, and roadmap files before changing code.

Continue autonomously until every applicable acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository source and git history;
- preserve primary papers and exact ancillaries;
- transcribe exact source equations;
- derive one-loop distributional expressions;
- implement partonic external states;
- construct finite-basis operator matrix elements;
- execute all frozen resolution and IR checks;
- run gauge, Ward, soft, overlap, UV, rapidity, and state-independence tests;
- build deterministic manifests and fault injections.

Do not:

- contact authors;
- alter C11-C36 historical results;
- reselect the physical regulator after seeing residuals;
- use ART25 information in the matching derivation;
- fit counterterms to hadron data;
- use energy convergence as TMD convergence;
- treat an auxiliary representation as an additive soft sector;
- create a likelihood, posterior, reweighting, emulator, or process route;
- push the completion commit.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 5.1 Microscopic state and operator roots

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c8_implementation_report.md
docs/next_level/c9_implementation_report.md
docs/next_level/c10_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
```

## 5.2 Continuum matching/evolution roots

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
```

These are validation and source infrastructures. They are not a substitute for the C37 regulator-specific partonic calculation.

## 5.3 Bridge history

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c30_implementation_report.md
docs/next_level/c31_implementation_report.md
docs/next_level/c32_implementation_report.md
```

## 5.4 Regulator and soft history

```text
docs/next_level/c33_implementation_report.md
docs/next_level/c34_implementation_report.md
docs/next_level/c35_implementation_report.md

docs/next_level/c36_implementation_report.md
docs/next_level/c36_api.md
docs/next_level/c36_requirement_coverage.json
docs/next_level/c36_normative_source_integration.json
docs/next_level/c36_primary_source_manifest.json
docs/next_level/c36_source_relevance_matrix.json
docs/next_level/c36_regulator_plan_manifest.json
docs/next_level/c36_regulator_plan_selection.json
docs/next_level/c36_plan_exclusion_graph.json
docs/next_level/c36_regulator_selection_scorecard.json
docs/next_level/c36_joint_root_identity.json
docs/next_level/c36_finite_rapidity_direction_manifest.json
docs/next_level/c36_joint_regulator_manifest.json
docs/next_level/c36_finite_regulator_gauge_report.json
docs/next_level/c36_transverse_link_report.json
docs/next_level/c36_ward_benchmark.json
docs/next_level/c36_spacelike_soft_definition.json
docs/next_level/c36_spacelike_collinear_definition.json
docs/next_level/c36_soft_allocation_convention.json
docs/next_level/c36_selected_scheme_soft_oracle.json
docs/next_level/c36_selected_scheme_collinear_oracle.json
docs/next_level/c36_selected_scheme_oracle_validation.json
docs/next_level/c36_rapidity_coordinate_manifest.json
docs/next_level/c36_rapidity_evolution_report.json
docs/next_level/c36_regulator_limit_order.json
docs/next_level/c36_selected_to_project_conversion.json
docs/next_level/c36_conversion_roundtrip_report.json
docs/next_level/c36_hard_companion_conversion.json
docs/next_level/c36_c11_tree_reduction_report.json
docs/next_level/c36_microscopic_implementation_plan.json
docs/next_level/c36_state_operator_soft_separation.json
docs/next_level/c36_finite_basis_compatibility.json
docs/next_level/c36_future_matching_strategy.json
docs/next_level/c36_overlap_convention.json
docs/next_level/c36_zero_bin_compatibility.json
docs/next_level/c36_continuation_gate.json
docs/next_level/c36_capability_matrix.json
docs/next_level/c36_unresolved_physics_gaps.md
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

Create:

```text
docs/next_level/c37_normative_source_integration.json
docs/next_level/c37_volume_xxi_spacelike_addendum_crosswalk.json
```

---

# 6. Primary-source authority

Reuse the exact C36 source locks. Preserve any newly needed source or ancillary under:

```text
data/raw/c37_sources/
```

with exact version and SHA-256 identity.

At minimum, distinguish the roles of:

```text
hep-ph/0404183:
    selected finite-rapidity JMY quark TMD, soft subtraction,
    one-loop factorization, Collins-Soper evolution

arXiv:1210.2100:
    continuum relation between Collins and EIS definitions;
    not finite-basis matching

arXiv:2312.04315:
    auxiliary-field representation of spacelike Wilson lines and
    one-loop soft methodology

arXiv:2603.03814:
    current preliminary auxiliary-field Collins-Soper methodology;
    not a project matching coefficient

arXiv:2002.09408:
    auxiliary-line residual mass, endpoints, piecewise paths, and
    scheme-conversion methodology

arXiv:1911.03840:
    regulator-specific matching methodology and finite-length links;
    not operator-identical to the C11 basis by default

arXiv:1111.4996:
    downstream on-light-cone project/EIS target and gauge/soft checks

transverse-link sources retained by C36:
    exact gauge completion at infinity
```

Classify each record as:

```text
SELECTED_OPERATOR_AUTHORITY
SELECTED_ONE_LOOP_AUTHORITY
SELECTED_SOFT_AUTHORITY
SELECTED_EVOLUTION_AUTHORITY
CONTINUUM_CONVERSION_AUTHORITY
AUXILIARY_REPRESENTATION_AUTHORITY
FINITE_BASIS_METHOD_AUTHORITY
DOWNSTREAM_TARGET_AUTHORITY
NOT_FINITE_BASIS_OPERATOR_IDENTICAL
```

Every new equation or generated array must store:

```text
source locator
operator identity
Wilson directions
rapidity convention
soft allocation
UV convention
external state
IR regulator
gauge
perturbative order
transcription or derivation hash
independent check
```

Create:

```text
docs/next_level/c37_primary_source_manifest.json
docs/next_level/c37_derivation_authority_manifest.json
```

---

# 7. Immutable C36 baseline

Before edits, reproduce and record at least:

```text
resolved full C36 commit
1,265 tests collected
C35 and C36 validators passing
C33-C36 focused suite: 98 passed
C-prefixed inherited suite: 849 passed
2,640 C36 semantic injections
15 C36 primary-source records
12 C36 ADRs
deterministic manifest reconstruction

selected physical plan:
    O4-SPACELIKE-COLLINS-JMY

paired roots:
    C36_COLLINEAR_ROOT, B=1
    C36_SOFT_ROOT, B=0

historical negative control:
    C35 modified-delta no-go
    finite-delta Ward defect 0.2143273

tree reduction:
    all twelve nonzero C11 u/d/ubar/dbar parents pass

soft ownership:
    universal soft factor outside the hadron TTN

readiness:
    architecture ready
    no one-loop finite-basis matching
    no microscopic proton TMD
    no bridge rerun

integrity:
    all 642 ART25 identities unchanged
    NO_JOINT_MEASURE
    216 production routes
    eight authoritative artifacts
    MSHT20_REP outside Git
```

Do not proceed if the baseline fails.

C37 must not modify:

- C11-C36 historical roots or statuses;
- the C35 Ward defect;
- the C36 selected regulator;
- the C36 tree reduction;
- the frozen bridge grid, roles, holdouts, ancestry, or `NO_JOINT_MEASURE`;
- ART25;
- production or authoritative artifacts.

Create versioned C37 calculation descendants only.

---

# 8. Required architecture

Implement or extend immutable objects equivalent to:

```text
C37PartonicCalculationId
C37PartonicOrder
C37PartonicChannel

PartonicExternalState
CommonIRRegulator
ExternalMomentumPlan
ExternalSpinPlan
ExternalFlavorPlan

SelectedUnsubtractedCollinear
SelectedBareSoft
SelectedSubtractedTMD
SelectedUVCounterterm
SelectedRapidityCoordinate

FiniteBasisPartonicCollinear
FiniteBasisWilsonInsertion
FiniteBasisInstantaneousTerm
FiniteBasisBoundaryTerm
FiniteBasisCounterterm

DistributionalCoefficient
EndpointDeltaTerm
PlusDistributionTerm
RegularXTerm
DiscreteBasisConvolution

SoftAllocationRecord
OverlapSubtractionRecord
CountOnceReport

PartonicDifference
LFToSelectedMatchingKernel
MatchingChannelMatrix
MatchingRemainder

GaugeCancellationReport
IRCancellationReport
UVCancellationReport
RapidityEvolutionReport
StateIndependenceReport
BasisTrajectoryReport

SelectedToProjectExecution
ProjectToART25ReadOnlyExecution

HadronApplicationPrerequisite
HadronApplicationGate
C37CapabilityMatrix
C37ClosureReport
```

Every object must be immutable, content addressed, deterministic, and explicit about:

```text
root ownership
partonic channel
external state
IR regulator
finite-rapidity directions
soft allocation
gauge
UV scheme
x-distribution structure
basis resolution
first omitted order
remainder
```

No universal kernel may depend on a hadron state or ART25 member.

---

# 9. Freeze the calculation plan

Before one-loop evaluation, freeze:

```text
selected C36 physical scheme
selected C36 microscopic implementation relation
selected C36 future matching strategy
finite-rapidity vectors and source-defined invariant
future/past orientation for the T-even pilot
transverse closure
soft allocation
UV target
common IR regulator
external momenta
external off-shellness or mass
gauge values
mu values
finite-rapidity values
bT points
x-space test functions
C7/C11 finite-basis resolutions
holdouts
```

Use the exact C36 manifests. Do not silently substitute a new strategy.

If C36 did not select an executable partonic-difference strategy, fail closed and report the exact missing decision.

Create:

```text
docs/next_level/c37_calculation_plan.json
docs/next_level/c37_external_state_plan.json
docs/next_level/c37_holdout_plan.json
```

---

# 10. Exact selected-scheme definitions

Transcribe the exact selected-source definitions of:

```text
unsubtracted quark TMD correlator
universal soft factor
subtracted quark TMD
finite-rapidity invariant
zeta or equivalent scale
soft allocation
UV renormalization
rapidity evolution
order of the lightlike/large-rapidity limit
```

Do not hard-code a remembered \(\rho\), \(\zeta\), or soft-factor power.

The machine-readable definition must include:

```text
path order
anti-path order
future/past direction
spacelike vectors
transverse closure
endpoint identities
Fourier convention
normalization
quark/antiquark convention
```

Create:

```text
docs/next_level/c37_selected_scheme_definition.json
docs/next_level/c37_selected_rapidity_scale_map.json
docs/next_level/c37_selected_soft_allocation.json
```

---

# 11. Common partonic external states and IR regulator

Use the same external-state IR prescription on the continuum and finite-basis sides, or construct a separately proved conversion.

At minimum retain:

```text
two external quark momenta
two IR-regulator values
u and d labels
quark and charge-conjugate antiquark states
two helicities
one primary and one holdout gauge value
```

The external state is a matching probe, not the proton.

Required checks:

- same momentum and normalization;
- same spin projector;
- same IR regulator;
- same color normalization;
- same Fourier and \(x\)-support convention;
- charge conjugation;
- independence of the eventual kernel from the probe choice.

Create:

```text
docs/next_level/c37_partonic_external_states.json
docs/next_level/c37_common_ir_contract.json
```

---

# 12. Continuum selected-scheme one-loop calculation

Reproduce the source-qualified selected-scheme partonic quark TMD.

Calculate or independently reconstruct:

```text
tree term
quark self energy
bilocal quark vertex
real quark emission
spacelike Wilson-line attachment
Wilson-line self energy
endpoint/cusp contribution
transverse closure contribution where required
unsubtracted collinear result
universal soft factor
soft-subtracted result
UV counterterm
finite-rapidity dependence
```

Represent the result distributionally:

\[
F^{(1)}(x,b_T)
=
c_\delta(b_T)\delta(1-x)
+
\sum_n c_n(b_T)
\left[\frac{\ln^n(1-x)}{1-x}\right]_+
+
f_{\rm reg}(x,b_T).
\]

Required independent checks:

- source transcription;
- graph-level or direct-integral reconstruction;
- Mellin moments;
- quark-number moment;
- gauge independence of the subtracted object;
- finite-rapidity evolution;
- lightlike/large-rapidity limit order;
- future/past equality for the T-even channel.

Create:

```text
docs/next_level/c37_continuum_unsubtracted_collinear.json
docs/next_level/c37_continuum_soft_factor.json
docs/next_level/c37_continuum_subtracted_tmd.json
docs/next_level/c37_continuum_oracle_validation.json
```

---

# 13. Finite-basis partonic collinear operator

Evaluate the C36 spacelike collinear operator in the finite light-front regulator.

The calculation must use partonic external states, not the proton wave function.

Retain all required contributions, including where applicable:

```text
tree overlap
quark self energy
operator vertex
real emission
spacelike Wilson insertion
transverse closure
instantaneous-fermion term
instantaneous-gluon term
basis-boundary term
endpoint-regulator term
zero-mode control
Hamiltonian mass counterterm
Hamiltonian vertex counterterm
operator counterterm
```

For each term record:

```text
source or derivation
basis resolution
longitudinal mode
transverse/OAM mode
color
spin
x support
bT dependence
UV behavior
IR behavior
finite-rapidity behavior
gauge dependence
cancellation partners
```

No continuum scaleless result may determine a finite-basis term without a regulator-specific proof.

Create:

```text
docs/next_level/c37_finite_basis_partonic_collinear.json
docs/next_level/c37_finite_basis_contribution_ledger.json
docs/next_level/c37_finite_basis_counterterm_ledger.json
```

---

# 14. Discrete-to-distributional \(x\) map

The finite light-front basis has discrete longitudinal support, while the target matching kernel is distributional.

Define an exact regulated map among:

```text
discrete K/mode support
cell or basis test functions
continuum x distributions
convolutions
Mellin moments
the continuum trajectory
```

Do not infer a continuous distribution from only the twelve hadronic bridge points.

Require:

- partition/completeness on the regulated x domain;
- exact number moment;
- support \(0<x\le1\);
- endpoint treatment;
- independent test-function action;
- refinement across at least three resolutions;
- no fitted interpolation to ART25.

Create:

```text
docs/next_level/c37_discrete_x_distribution_map.json
docs/next_level/c37_distributional_convolution_report.json
```

---

# 15. Universal soft subtraction and overlap

Use the C36 universal soft root outside the hadron TTN.

The finite-basis collinear result must be combined with the selected soft subtraction according to the exact source convention.

Keep separate:

```text
soft factor
soft allocation
zero-bin or equivalent overlap subtraction
finite-rapidity dependence
IR regulator
UV renormalization
```

Do not subtract the soft factor twice.

Do not assume that the historical C32 off-shell zero-bin contract carries over automatically.

Required controls:

- missing-soft defect;
- duplicate-soft defect;
- missing-overlap defect;
- duplicate-overlap defect;
- count-once closure;
- gauge cancellation;
- finite-rapidity consistency.

Create:

```text
docs/next_level/c37_soft_subtraction_execution.json
docs/next_level/c37_overlap_execution.json
docs/next_level/c37_count_once_report.json
```

---

# 16. Extract the finite-basis matching kernel

After both sides are renormalized and use the same IR prescription, extract:

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
explicit in the finite-basis regulator
explicit in finite rapidity
explicit in mu
explicit in first omitted order
```

Create:

```text
docs/next_level/c37_lf_to_selected_matching_library.json
docs/next_level/c37_matching_remainder.json
```

If any required cancellation is unavailable, retain the kernel as empty-not-zero.

---

# 17. Channel matrix and singlet discipline

Decide explicitly at the declared order:

```text
q <- q
q <- qbar
q <- g
nonsinglet
quark singlet
```

Do not assume off-diagonal channels vanish.

A nonsinglet-only result may issue:

```text
C37_NONSINGLET_MATCHING_VALIDATED
```

but it cannot produce separate full physical \(u,d,\bar u,\bar d\) TMDs when unresolved singlet/gluon mixing contributes at the selected order.

Create:

```text
docs/next_level/c37_matching_channel_matrix.json
docs/next_level/c37_singlet_mixing_decision.json
```

---

# 18. Closure tests

A positive matching status requires all applicable tests.

## 18.1 Infrared closure

Report the IR dependence of:

```text
continuum selected-scheme object
finite-basis object
their difference
```

## 18.2 Gauge and Ward closure

Test the complete subtracted objects and their difference, not isolated gauge-dependent pieces.

The C35 finite-delta Ward defect remains a negative control.

## 18.3 UV closure

Separate:

```text
continuum UV renormalization
finite-basis Hamiltonian/basis counterterms
operator counterterms
matching-kernel UV dependence
```

## 18.4 Finite-rapidity evolution

Test the selected rapidity derivative and cusp consistency at the declared order.

## 18.5 Sum rules

Test:

```text
quark number
charge conjugation
flavor universality where proved
tree limit
small-b behavior
```

Create:

```text
docs/next_level/c37_ir_cancellation_report.json
docs/next_level/c37_gauge_ward_report.json
docs/next_level/c37_uv_closure_report.json
docs/next_level/c37_rapidity_cusp_report.json
docs/next_level/c37_sum_rule_report.json
```

Do not fabricate unavailable residuals.

---

# 19. Basis and regulator trajectory

Execute at least the frozen C7/C11 three-resolution sequence.

Separate, to the extent the repository supports:

```text
longitudinal resolution
transverse basis
oscillator scale
basis UV behavior
basis IR behavior
endpoint regulation
zero-mode policy
quadrature
finite-rapidity value
external-state IR regulator
```

Do not fit more trajectory parameters than the available independent points support.

Add an independently frozen fourth point when required for identifiability.

Allowed statuses:

```text
MATCHING_TRAJECTORY_RESOLVED
LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN
FINITE_BASIS_MATCHING_ONLY
NONUNIVERSAL_TRAJECTORY
TRAJECTORY_UNAVAILABLE
```

Create:

```text
docs/next_level/c37_basis_regulator_trajectory.json
docs/next_level/c37_trajectory_holdout_report.json
docs/next_level/c37_continuum_trajectory_decision.json
```

---

# 20. State-independence tests

Test the extracted kernel across:

```text
two external momenta
two IR-regulator values
two quark helicities
u and d labels
quark and positive-x antiquark charge-conjugate probes
at least two finite-basis resolutions
```

Where possible, apply the kernel to a simple composite toy state not used in extraction.

If it depends irreducibly on a proton coefficient or external probe, issue:

```text
STATE_DEPENDENT_MODEL_MAP
```

and do not call it matching.

Create:

```text
docs/next_level/c37_state_independence_report.json
docs/next_level/c37_flavor_antiquark_report.json
```

---

# 21. Execute the selected-to-project conversion

Use the C36 conversion as a read-only source contract.

Once a selected-scheme partonic TMD exists, execute and validate:

```text
selected finite-rapidity scheme
    -> project renormalized TMD scheme
    -> read-only project-to-ART25 convention
```

Keep separate:

```text
finite operator conversion
soft allocation
rapidity convention
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
docs/next_level/c37_selected_to_project_execution.json
docs/next_level/c37_conversion_roundtrip_report.json
docs/next_level/c37_hard_companion_report.json
docs/next_level/c37_downstream_art25_execution_contract.json
```

Do not apply a continuum conversion directly to the unmatched historical C11 density.

---

# 22. Hadron-application prerequisite

C37 should normally stop at a validated universal matching kernel.

Define the exact requirements for applying it to the microscopic proton state:

```text
complete required channel matrix
distributional x convolution on the finite basis
basis trajectory
matching remainder
project conversion
two-scale evolution
operator identity
C11/C14 parent relation
TTN convergence on the TMD operator
common x-b-Q domain
```

Create:

```text
docs/next_level/c37_hadron_application_prerequisite.json
docs/next_level/c37_hadron_application_gate.json
```

A successful partonic calculation may issue:

```text
C37_HADRON_APPLICATION_READY
```

without yet issuing a microscopic proton TMD or bridge result.

---

# 23. Conditional validation-only microscopic export

Only when **all** of the following close:

```text
full channel matrix needed for u/d/ubar/dbar
state-independent matching
distributional finite-basis convolution
basis trajectory
selected-to-project conversion
evolution identity
TMD-specific TTN convergence
complete common domain
```

C37 may create a versioned validation-only microscopic export on the immutable twelve-point grid.

Every row must retain:

```text
microscopic parent
resolution
Fock content
Wilson/operator identity
matching kernel
channel/mixing identity
finite-rapidity value
project conversion
evolution
x/b/Q
all remainders
```

No free normalization is permitted.

Even when this export exists, C37 must not perform the ART25 residual, whitening, percentile, or null-space comparison. That comparison belongs to the next bridge package.

Create only when the gate passes:

```text
docs/next_level/c37_conditional_microscopic_tmd_export.json
docs/next_level/c37_conditional_export_report.json
```

When the gate fails, serialize deterministic empty coordinates, not numerical zeros.

---

# 24. Bridge preservation

C37 does not rerun the frozen ART25 bridge.

Preserve:

```text
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
all 642 ART25 member identities
external covariance rank and null space
eight calibration-candidate and four holdout roles
NO_JOINT_MEASURE
data ancestry
no-double-counting alternatives
```

If a conditional microscopic export closes, issue only:

```text
BRIDGE_INPUT_VECTOR_READY_FOR_INDEPENDENT_COMPARISON
```

The next package must execute the actual bridge diagnostics independently.

Create:

```text
docs/next_level/c37_bridge_prerequisite_delta.json
docs/next_level/c37_bridge_integrity_regression.json
```

---

# 25. Uncertainty and remainder separation

Keep separate:

```text
selected-scheme perturbative truncation
continuum-oracle transcription
common-IR conversion
finite-basis UV remainder
finite-basis IR remainder
longitudinal/basis truncation
endpoint and zero-mode remainder
Wilson insertion remainder
instantaneous-term remainder
soft-allocation remainder
overlap/zero-bin remainder
finite-rapidity power correction
matching-channel incompleteness
basis trajectory
selected-to-project conversion
two-scale evolution
TTN truncation
numerical quadrature
external ART25 covariance
```

Unknown remains:

```text
NONZERO_UNKNOWN
```

No matching uncertainty may be absorbed into ART25 covariance or a fitted hadron normalization.

Create:

```text
docs/next_level/c37_matching_uncertainty_budget.json
docs/next_level/c37_remainder_separation.json
```

---

# 26. Scientifically valid no-go outcomes

## 26.1 Continuum source reconstruction fails

```text
C37_SELECTED_SCHEME_ONE_LOOP_ORACLE_INCOMPLETE
```

Next:

> **C38/R2S — selected-scheme source expression and independent one-loop oracle completion**

## 26.2 Finite-basis collinear calculation is not executable

```text
C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE
```

Next:

> **C38/M0A — finite-basis spacelike Wilson insertion, partonic states, and counterterm construction**

## 26.3 Soft/overlap count-once closure fails

```text
C37_SOFT_OVERLAP_CLOSURE_FAILED
```

Next:

> **C38/Z1 — spacelike soft/collinear overlap and zero-bin completion**

## 26.4 Matching is state dependent

```text
C37_STATE_INDEPENDENT_MATCHING_UNAVAILABLE
```

Next:

> **C38/O2B — finite-basis collinear operator/regulator redesign for universal matching**

## 26.5 Only nonsinglet matching closes

```text
C37_NONSINGLET_ONLY
```

Next:

> **C38/MIX0 — singlet and q<-g/q<-qbar matching-channel completion**

## 26.6 Basis trajectory remains unresolved

```text
C37_MATCHING_TRAJECTORY_UNRESOLVED
```

Next:

> **C38/R1 — finite-basis regulator trajectory and power-correction completion**

## 26.7 Project conversion remains unresolved

```text
C37_PROJECT_CONVERSION_UNAVAILABLE
```

Next:

> **C38/C0 — selected-spacelike-to-project one-loop conversion completion**

## 26.8 Full matching closes

```text
C37_HADRON_APPLICATION_READY
```

Next:

> **C38/B1E — apply the validated matching kernel to microscopic proton states, close TMD convergence, and execute the frozen ART25 bridge**

Every no-go must identify the exact missing graph, counterterm, source expression, channel, trajectory, or conversion.

Create:

```text
docs/next_level/c37_source_sufficiency_decision.json
docs/next_level/c37_no_go_decision_tree.json
docs/next_level/c37_missing_calculation_specification.md
```

---

# 27. Holdouts

Freeze before calculation:

```text
one continuum delta-endpoint coefficient
one continuum plus-distribution coefficient
one regular x term
one Mellin moment
one soft coefficient
one quark self-energy term
one spacelike Wilson-attachment term
one transverse-closure term
one finite-basis instantaneous term
one basis counterterm
one gauge value
one external momentum
one IR-regulator value
one finite-rapidity value
one bT point
one basis resolution
one q<-g decision
one antiquark charge-conjugation check
one selected-to-project round trip
one hard-companion point
one toy-state independence check
one ART25-independence control
```

No failed holdout may be moved into derivation or tuning.

---

# 28. Required benchmark families

Implement at least:

```text
R2-A  immutable C36 architecture and C35 negative control
R2-B  exact selected-scheme definitions
R2-C  common external states and IR regulator
R2-D  continuum unsubtracted collinear calculation
R2-E  continuum universal soft factor
R2-F  continuum subtracted TMD
R2-G  finite-basis partonic collinear calculation
R2-H  discrete-to-distributional x map
R2-I  soft/overlap count-once closure
R2-J  matching-kernel extraction
R2-K  q<-q/q<-qbar/q<-g channel matrix
R2-L  IR, UV, gauge, and Ward closure
R2-M  finite-rapidity and cusp evolution
R2-N  basis trajectory
R2-O  state independence and charge conjugation
R2-P  selected-to-project conversion
R2-Q  hadron-application and bridge prerequisites
R2-R  deterministic isolation and no readiness leakage
```

---

# 29. Negative injections

Create at least **2,840 ordered C37 semantic fault injections** with stable IDs and deterministic diagnostics.

Include:

## Regulator and source identity

- regulator family reopened after C36;
- modified-delta finite-cell root restored as primary;
- auxiliary representation added as a second soft factor;
- remembered \(\rho\) formula substituted for source definition;
- finite-rapidity limit order changed.

## External states and IR

- different IR regulators on two sides;
- external normalization mismatch;
- quark/antiquark alias;
- external momentum changed after holdout freeze;
- proton state used as a matching probe.

## Continuum calculation

- soft factor omitted;
- soft factor counted twice;
- transverse link omitted;
- graph-level check replaced by source transcription;
- endpoint distribution binned;
- Mellin/quark-number failure hidden;
- gauge-dependent unsubtracted result called physical.

## Finite-basis calculation

- continuum scaleless term copied as zero;
- instantaneous term omitted;
- basis boundary omitted;
- zero-mode silently zeroed;
- Hamiltonian counterterm omitted;
- one basis point called continuum;
- energy convergence used as TMD convergence.

## Distributional map

- twelve bridge points used as an x convolution grid;
- arbitrary interpolation;
- support outside \(0<x\le1\);
- delta term dropped;
- plus distribution replaced by cutoff;
- partition/completeness omitted.

## Matching

- hadron-level ratio used;
- ART25 member used;
- state-dependent map called universal;
- IR dependence left in kernel;
- gauge dependence left in kernel;
- q<-g assumed zero;
- first omitted order set to zero.

## Conversion

- selected-to-project conversion applied directly to C11;
- hard companion omitted;
- scale evolution absorbed into finite factor;
- inverse absent;
- round-trip failure hidden;
- ART25 CS model used.

## Export and bridge

- export before full channel closure;
- free normalization introduced;
- failed point imputed;
- empty export treated as zero;
- bridge residual calculated in C37;
- likelihood, p-value, or reweighting created.

## Integrity

- historical C35 defect changed;
- C36 tree reduction changed;
- frozen roles or holdouts changed;
- `NO_JOINT_MEASURE` changed;
- production registry changed;
- authoritative artifact changed;
- raw MSHT files committed;
- nondeterministic manifest.

---

# 30. Deliverables

Create at least:

```text
docs/next_level/c37_implementation_report.md
docs/next_level/c37_api.md
docs/next_level/c37_requirement_coverage.json
docs/next_level/c37_normative_source_integration.json
docs/next_level/c37_volume_xxi_spacelike_addendum_crosswalk.json
docs/next_level/c37_primary_source_manifest.json
docs/next_level/c37_derivation_authority_manifest.json

docs/next_level/c37_calculation_plan.json
docs/next_level/c37_external_state_plan.json
docs/next_level/c37_holdout_plan.json

docs/next_level/c37_selected_scheme_definition.json
docs/next_level/c37_selected_rapidity_scale_map.json
docs/next_level/c37_selected_soft_allocation.json

docs/next_level/c37_partonic_external_states.json
docs/next_level/c37_common_ir_contract.json

docs/next_level/c37_continuum_unsubtracted_collinear.json
docs/next_level/c37_continuum_soft_factor.json
docs/next_level/c37_continuum_subtracted_tmd.json
docs/next_level/c37_continuum_oracle_validation.json

docs/next_level/c37_finite_basis_partonic_collinear.json
docs/next_level/c37_finite_basis_contribution_ledger.json
docs/next_level/c37_finite_basis_counterterm_ledger.json

docs/next_level/c37_discrete_x_distribution_map.json
docs/next_level/c37_distributional_convolution_report.json

docs/next_level/c37_soft_subtraction_execution.json
docs/next_level/c37_overlap_execution.json
docs/next_level/c37_count_once_report.json

docs/next_level/c37_lf_to_selected_matching_library.json
docs/next_level/c37_matching_remainder.json
docs/next_level/c37_matching_channel_matrix.json
docs/next_level/c37_singlet_mixing_decision.json

docs/next_level/c37_ir_cancellation_report.json
docs/next_level/c37_gauge_ward_report.json
docs/next_level/c37_uv_closure_report.json
docs/next_level/c37_rapidity_cusp_report.json
docs/next_level/c37_sum_rule_report.json

docs/next_level/c37_basis_regulator_trajectory.json
docs/next_level/c37_trajectory_holdout_report.json
docs/next_level/c37_continuum_trajectory_decision.json
docs/next_level/c37_state_independence_report.json
docs/next_level/c37_flavor_antiquark_report.json

docs/next_level/c37_selected_to_project_execution.json
docs/next_level/c37_conversion_roundtrip_report.json
docs/next_level/c37_hard_companion_report.json
docs/next_level/c37_downstream_art25_execution_contract.json

docs/next_level/c37_hadron_application_prerequisite.json
docs/next_level/c37_hadron_application_gate.json
docs/next_level/c37_bridge_prerequisite_delta.json
docs/next_level/c37_bridge_integrity_regression.json

docs/next_level/c37_matching_uncertainty_budget.json
docs/next_level/c37_remainder_separation.json

docs/next_level/c37_source_sufficiency_decision.json
docs/next_level/c37_no_go_decision_tree.json
docs/next_level/c37_missing_calculation_specification.md

docs/next_level/c37_holdout_report.json
docs/next_level/c37_injection_manifest.json
docs/next_level/c37_regression_report.json
docs/next_level/c37_unresolved_physics_gaps.md
```

Create conditional export files only if every Section 23 gate passes.

Add ADRs for:

- fixed C36 spacelike scheme ownership;
- common partonic IR regulator;
- universal soft outside the hadron TTN;
- discrete-to-distributional x authority;
- finite-basis Wilson insertion and counterterms;
- singlet/mixing discipline;
- state-independent matching;
- selected-to-project conversion;
- hadron-application gate;
- bridge execution deferred to an independent package.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy distribution grids, basis matrices, loop arrays, and convolution tables may remain outside Git under content-addressed runtime directories. Commit their schemas, hashes, dimensions, coordinate order, and deterministic reconstruction commands.

---

# 31. Acceptance criteria

C37/R2 is complete only when:

1. The full C36 baseline commit is resolved rather than invented.
2. The complete C36 baseline reproduces.
3. The C36 spacelike regulator remains fixed.
4. The C35 modified-delta no-go remains explicit.
5. Continuum selected-scheme definitions are source exact.
6. The finite-rapidity scale and limit order are explicit.
7. Common partonic external states and IR regulator are frozen.
8. The continuum unsubtracted collinear object is calculated or fails closed.
9. The continuum universal soft factor is calculated or fails closed.
10. The continuum subtracted TMD is independently validated.
11. Endpoint distributions are exact.
12. Mellin and quark-number checks close where claimed.
13. The finite-basis partonic collinear object is calculated or fails closed.
14. Every required finite-basis contribution receives an explicit status.
15. No continuum scalelessness is copied to the finite regulator without proof.
16. The discrete-to-distributional x map is explicit.
17. The finite-basis convolution is not inferred from twelve hadron points.
18. Soft and overlap subtractions are count-once.
19. The matching difference uses the same IR prescription.
20. The kernel is IR finite when claimed.
21. The kernel is gauge independent when claimed.
22. The kernel is state independent when called matching.
23. q<-q, q<-qbar, and q<-g receive explicit decisions.
24. Nonsinglet-only closure is not promoted to full flavor closure.
25. The basis trajectory is executed at three or more valid points.
26. No trajectory is overfit.
27. UV, rapidity, basis, and numerical remainders remain separate.
28. The selected-to-project conversion is source audited.
29. Hard-factor companion transformations are explicit.
30. Inverse and round-trip conversions are tested.
31. ART25 information does not enter the derivation.
32. Hadron application occurs only after every required channel and convolution gate passes.
33. No free normalization is introduced.
34. Failed exports remain empty, not zero.
35. C37 does not perform the ART25 bridge comparison.
36. All 642 ART25 identities and covariance remain unchanged.
37. Frozen roles, holdouts, ancestry, and `NO_JOINT_MEASURE` remain unchanged.
38. No fit, likelihood, posterior, optimization, reweighting, or emulator is created.
39. No process, deuteron, gluon, T-odd, inference, or production status is promoted.
40. Every no-go contains an exact missing-calculation specification.
41. All inherited tests, validators, builders, requirements, injections, and manifests remain passing.
42. The production registry remains exactly 216 routes.
43. All eight authoritative artifacts remain byte-identical.
44. `MSHT20_REP/` remains outside Git.
45. At least 2,840 C37 semantic fault injections produce the expected diagnostics.
46. All C37 manifests reproduce byte-for-byte.
47. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
48. A local completion commit is created and not pushed.

A rigorous no-go or nonsinglet-only result is valid. Do not weaken universality, gauge closure, channel completeness, or distributional identity to obtain a matching kernel.

---

# 32. Allowed and forbidden statuses

The strongest generally permitted statuses include:

```text
C37_CALCULATION_PLAN_FROZEN
C37_SELECTED_SCHEME_CONTINUUM_ORACLE_VALIDATED
C37_FINITE_BASIS_COLLINEAR_AUDITED
C37_DISTRIBUTIONAL_X_MAP_AUDITED
C37_SOFT_OVERLAP_COUNT_ONCE_DECIDED
C37_MATCHING_CHANNEL_MATRIX_COMPLETE
C37_BASIS_TRAJECTORY_AUDITED
C37_SELECTED_TO_PROJECT_CONVERSION_AUDITED
C37_HADRON_APPLICATION_GATE_DECIDED
C37_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when exact gates pass:

```text
C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_VALIDATED
C37_LF_TO_SELECTED_MATCHING_VALIDATED
C37_NONSINGLET_MATCHING_VALIDATED
C37_FULL_QUARK_SINGLET_MATCHING_VALIDATED
C37_STATE_INDEPENDENT_MATCHING_VALIDATED
C37_SELECTED_TO_PROJECT_CONVERSION_VALIDATED
C37_HADRON_APPLICATION_READY
```

The following remain forbidden unless the conditional export gates close exactly:

```text
C37_MICROSCOPIC_PROTON_TMD_EXPORTED
```

The following remain forbidden throughout C37:

```text
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
- exact selected-scheme source identities and hashes;
- frozen external-state and IR plan;
- finite-rapidity directions, invariant, and limit order;
- continuum collinear, soft, and subtracted-TMD results;
- distributional coefficients and Mellin residuals;
- finite-basis contribution statuses and values;
- discrete-to-distributional map and convergence;
- soft/overlap count-once residuals;
- matching channel matrix;
- IR, UV, gauge, Ward, rapidity, cusp, and sum-rule residuals;
- basis trajectory and holdout results;
- state-independence and charge-conjugation results;
- selected-to-project conversion and hard-companion results;
- hadron-application gate;
- conditional export count and hashes, if any;
- bridge prerequisite delta, with confirmation that no comparison ran;
- exact no-go and next branch where blocked;
- confirmation that no ART25 member, data, chi2, residual, or proton-level ratio entered the derivation;
- confirmation that no bridge comparison, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe an architecture-ready scheme, a continuum-only result, a nonsinglet-only kernel, or a state-dependent conversion as a complete microscopic proton TMD matching result.
