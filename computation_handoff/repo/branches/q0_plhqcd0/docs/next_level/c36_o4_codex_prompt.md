# C36/O4 Codex Work Package

## Title

**Gauge-invariant finite-rapidity replacement regulator for the microscopic TMD root: spacelike Wilson-line collinear/soft operators, auxiliary-field realization, and conversion to the project/ART25 scheme**

## Authoritative baseline

Start from the local C35/S0C completion commit:

```text
bbefd963ea14bf79884ec3a5c1a503581a6dd21e
```

Required ancestors include:

```text
C34/S0A:
    6bdb44be2afc79e817f69ce0e35813da8a394db7

C33/S0:
    e0b34c74e8f39c9d42cf49cc598f1533d9353a7e

C32/R0:
    0d7b94a5e86882b23a56d4c1f11900d554756a18

C28/P1D:
    52678312906bf5cc0bb8664e2486d5d676a6b723
```

A documentation-only descendant is acceptable only when these commits remain in its ancestry and the complete C35 baseline reproduces before any scientific change.

Do not use `origin/main` when the local branch is ahead of the remote.

The authoritative Volume XXI source remains:

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

Read and hash-audit it. Volume XXI remains authoritative for the distinction among the microscopic state, completed operator, soft sector, renormalized project TMD, and downstream ART25-aligned TMD. C36 may add a versioned regulator-architecture correction or requirement crosswalk, but it must not silently rewrite the historical volume.

The pre-existing untracked directory:

```text
MSHT20_REP/
```

must remain untouched and outside Git while redistribution permission remains unresolved.

Create a local completion commit. Do not push.

---

# 1. Why C36/O4 is the exact next package

C35 reaches the rigorous Branch-G result:

```text
selected plan:
    S0C-UNAVAILABLE

primary no-go:
    C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE

secondary no-go:
    C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE

exact continuation:
    C36/O4 — replacement regulator architecture for the microscopic TMD soft root
```

The result is source supported and is not a numerical failure or a zero soft correction.

C35 establishes several useful exact records:

```text
v^\pm = (v^0 +/- v^3)/sqrt(2)
n^2 = nbar^2 = 0
n.nbar = 1
n.k = k^-
nbar.k = k^+
k^2 = 2 k^+ k^- - k_T^2

delta^- -> lambda delta^-
delta^+ -> lambda^-1 delta^+
under n -> lambda n, nbar -> lambda^-1 nbar

exact real on-shell coordinate chart and phase-space measure
exact virtual geometric coordinate chart
scalar-cell normalization oracle
principal-value/cut/analytic singular-integral oracles
finite-segment modified-delta damping operator
```

C35 also executes an explicit finite-delta Ward diagnostic. The damped scalar path identity closes analytically, but the finite-delta Wilson operator retains a nonzero gauge defect. No finite-cell BRST/Krein completion, complete light-front physical-gauge completion, or regulator-identical auxiliary-field completion exists in the repository.

Therefore:

```text
all eighteen one-loop contribution classes:
    UNRESOLVED_BLOCKING / NONZERO_UNKNOWN

finite-basis one-loop coefficient:
    undefined

UV and rapidity counterterms:
    empty-not-zero

finite-basis-to-continuum conversion:
    unavailable

soft-side zero-bin value:
    empty-not-zero

C32 continuation gate:
    false
```

C36 must not keep filling slots inside this incompatible regulator descriptor.

It must replace the rapidity-regulator architecture with one that preserves the relevant Wilson-line gauge covariance at every finite regulator value and that admits a source-audited collinear/soft pair.

---

# 2. Central scientific correction

The historical chain is preserved:

```text
C11:
    regulated finite-basis model density

C32:
    completed lightlike-staple operator with exact C11 tree reduction

C33:
    structurally distinct B=0 vacuum/eikonal root

C34-C35:
    modified-delta finite-cell realization audits
```

The C35 descendant is not deleted. It remains the exact no-go certificate for the attempted finite-cell modified-delta realization.

C36 creates a new versioned root:

```text
C36_GAUGE_INVARIANT_FINITE_RAPIDITY_TMD_ROOT
```

with two descendants over one common rapidity architecture:

```text
C36_COLLINEAR_ROOT, B=1
C36_SOFT_ROOT,      B=0
```

The shared regulator record is:

\[
\mathfrak R_{36}
=
\left(
\mathcal U_{\rm finite\ rapidity},
\mathcal R_{\rm UV},
\mathcal R_{\rm IR},
\mathcal M_{b_T},
\mathcal C_{\rm soft/coll},
\mathcal C_{\rm scheme}
\right).
\]

The replacement architecture must preserve gauge covariance through the operator definition rather than attempt to restore it only after evaluating a gauge-defective finite regulator.

The modified-delta/EIS convention remains available only as:

```text
DOWNSTREAM_CONTINUUM_TARGET_SCHEME
```

for an already-renormalized TMD. It is no longer the finite microscopic regulator.

---

# 3. Primary objective

Implement the chain:

```text
C35 no-go and exact convention records
    -> audit gauge-invariant rapidity-regulator families
    -> select one finite-rapidity operator scheme
    -> create paired B=1 collinear and B=0 soft roots
    -> define exact finite-regulator Wilson geometry
    -> prove gauge covariance at finite regulator
    -> define UV, rapidity, soft, and overlap conventions
    -> construct source-qualified continuum tree and one-loop oracles
    -> establish conversion to the project/ART25 convention
    -> prove exact tree reduction to the C11 microscopic density
    -> decide the finite-basis collinear matching strategy
    -> define the executable next-calculation gate
```

The preferred scientific form is a finite-rapidity, non-lightlike Wilson geometry:

\[
v^2<0,\qquad
\bar v^2<0,
\]

with source-defined rapidity variables and a source-defined invariant such as \(\rho\) or an equivalent Collins-Soper parameter.

The collinear and soft operators must use the same finite-rapidity geometry or an exact proved conversion.

The package must determine rather than assume:

```text
whether off-light-cone/spacelike Wilson lines provide the correct
gauge-invariant microscopic project scheme;

whether an auxiliary one-dimensional field representation can realize the
same spacelike Wilson paths and their endpoint/cusp renormalization;

whether an exponential or finite-length soft regulator is a more suitable
primary architecture;

whether the finite-basis hadron state can be coupled to the new collinear
operator without introducing a gauge-field vacuum into the proton state;

whether the universal soft factor should remain a continuum/auxiliary
operator root rather than a finite-cell Fock root;

whether a state-independent finite-basis collinear matching calculation can
be formulated in the selected scheme;

whether the selected scheme can be converted to the downstream
project/ART25 convention with hard-factor and evolution identities preserved.
```

A positive architecture is not assumed.

---

# 4. Scientific boundary

C36 is:

```text
regulator-architecture replacement
operator-definition first
finite-rapidity
gauge-covariant at finite regulator
paired collinear/soft
quark fundamental representation
T-even rank-zero pilot scope
source audited
scheme conversion explicit
tree-reduction explicit
validation only
non-inferential
```

C36 is not:

```text
a continuation of the gauge-defective modified-delta finite-cell root
a numerical soft coefficient fit
a microscopic proton TMD export
a completed LF-to-project matching kernel
an ART25 refit
a likelihood
a posterior
replica reweighting
parameter optimization
an emulator
a process prediction
a deuteron prediction
a gluon or T-odd regulator generalization
a production promotion
```

C36 may construct continuum and auxiliary-field one-loop oracles. It must not label those as a completed finite-basis hadronic calculation.

---

# 5. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C5-C36 Wilson, regulator, soft, collinear, Hamiltonian, matching, evolution, bridge, formal-volume, primary-source, test, API, manifest, ADR, and roadmap files before edits.

Continue autonomously until every applicable C36 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository source and complete git history;
- preserve newly relevant primary papers and ancillaries;
- audit alternative rapidity regulators;
- construct exact off-light-cone/spacelike Wilson paths;
- implement auxiliary-field representations;
- derive finite-rapidity tree and one-loop continuum oracles;
- construct scheme-conversion records;
- perform gauge-transformation and Ward tests;
- build tree-reduction tests against C11/C32;
- freeze a future partonic matching plan;
- generate deterministic manifests.

Do not:

- contact authors;
- alter C11-C35 historical results;
- use ART25 members, data, chi2, or bridge residuals;
- fit a regulator conversion;
- fit a rapidity kernel;
- call the downstream modified-delta target the new microscopic regulator;
- create a microscopic proton TMD;
- rerun the twelve-point bridge;
- create inference or production routes;
- push the completion commit.

---

# 6. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

## 6.1 Historical microscopic and Wilson roots

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c6_implementation_report.md
docs/next_level/c11_implementation_report.md
docs/next_level/c12_implementation_report.md
docs/next_level/c13_implementation_report.md
docs/next_level/c14_implementation_report.md
```

## 6.2 Matching and evolution roots

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c20_implementation_report.md
docs/next_level/c21_implementation_report.md
docs/next_level/c22_implementation_report.md
```

## 6.3 Bridge and regulator history

```text
docs/next_level/c29_implementation_report.md
docs/next_level/c30_implementation_report.md
docs/next_level/c31_implementation_report.md

docs/next_level/c32_implementation_report.md
docs/next_level/c32_operator_completion_manifest.json
docs/next_level/c32_c11_tree_reduction_report.json
docs/next_level/c32_regulator_plan_manifest.json

docs/next_level/c33_implementation_report.md
docs/next_level/c33_two_root_tmd_identity.json
docs/next_level/c33_four_line_operator_manifest.json

docs/next_level/c34_implementation_report.md
docs/next_level/c34_continuum_soft_target.json

docs/next_level/c35_implementation_report.md
docs/next_level/c35_api.md
docs/next_level/c35_requirement_coverage.json
docs/next_level/c35_normative_source_integration.json
docs/next_level/c35_primary_source_manifest.json
docs/next_level/c35_derivation_authority_manifest.json
docs/next_level/c35_gauge_complete_plan_manifest.json
docs/next_level/c35_gauge_complete_plan_selection.json
docs/next_level/c35_light_front_convention.json
docs/next_level/c35_null_vector_regulator_rescaling.json
docs/next_level/c35_real_coordinate_chart.json
docs/next_level/c35_virtual_coordinate_chart.json
docs/next_level/c35_modified_delta_operator.json
docs/next_level/c35_modified_delta_mode_action_report.json
docs/next_level/c35_source_sufficiency_decision.json
docs/next_level/c35_no_go_decision_tree.json
docs/next_level/c35_missing_calculation_specification.md
docs/next_level/c35_regression_report.json
docs/next_level/c35_unresolved_physics_gaps.md
```

## 6.4 Formal sources

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

Use actual filenames when they differ. Do not invent absent sources.

Create:

```text
docs/next_level/c36_normative_source_integration.json
docs/next_level/c36_volume_xxi_requirement_crosswalk.json
```

---

# 7. Required primary-source audit

Reuse all relevant C31-C35 source locks. Preserve additional sources under:

```text
data/raw/c36_sources/
```

with exact version and SHA-256 identity.

Audit at least:

```text
hep-ph/0404183
    Ji-Ma-Yuan off-light-cone gauge links, soft subtraction, and
    one-loop/all-orders factorization scope

arXiv:1210.2100
    Collins/EIS definition equivalence and MSbar-convention alignment

arXiv:1511.05590
    modified-delta continuum target and its finite-regulator gauge caveat

arXiv:1604.00392
    exponential rapidity regulator and RRG-compatible soft construction

arXiv:2312.05957
    all-orders analytic relations among off-light-cone, finite-length,
    and exponential soft factors

arXiv:2312.04315
    auxiliary-field representation and spacelike Minkowski Wilson directions

arXiv:2412.12645
    exploratory auxiliary-field lattice soft-function realization

arXiv:2603.03814
    current auxiliary-field Collins-Soper-kernel methodology in the
    spacelike/Collins region

arXiv:2002.09408
    auxiliary-field Wilson-line renormalization, residual mass, endpoints,
    and piecewise paths

arXiv:1711.00543
    finite-cutoff Wilson-line renormalization structures

arXiv:1009.2776
arXiv:1104.0686
    transverse Wilson lines and gauge invariance in singular gauges

arXiv:1910.11415
arXiv:1911.03840
    spacelike/large-momentum TMD soft and matching methodology

arXiv:2311.01391
    gauge-invariant dressed-field/Coulomb-gauge quasi-TMD alternative
```

Classify every source as:

```text
FINITE_RAPIDITY_OPERATOR_AUTHORITY
GAUGE_INVARIANT_SOFT_AUTHORITY
CONTINUUM_SCHEME_EQUIVALENCE_AUTHORITY
AUXILIARY_FIELD_REALIZATION_AUTHORITY
EXPONENTIAL_REGULATOR_AUTHORITY
TRANSVERSE_LINK_AUTHORITY
FINITE_CUTOFF_RENORMALIZATION_AUTHORITY
DRESSED_FIELD_ALTERNATIVE_AUTHORITY
METHOD_ONLY
NOT_OPERATOR_REGULATOR_IDENTICAL
```

The 2026 auxiliary-field result is current and relevant, but its preliminary lattice extraction cannot be promoted into the project’s microscopic soft factor without an exact operator and scheme map.

Create:

```text
docs/next_level/c36_primary_source_manifest.json
docs/next_level/c36_source_relevance_matrix.json
```

---

# 8. Immutable C35 baseline

Before edits, reproduce and record:

```text
starting commit:
    6bdb44be2afc79e817f69ce0e35813da8a394db7

C35 completion:
    bbefd963ea14bf79884ec3a5c1a503581a6dd21e

tests:
    1,257 passed

focused C33-C35:
    90 passed

validators:
    C28-C35 pass

C35 manifests:
    61 deterministic JSON records

coverage:
    326 records

fault modes:
    93

semantic injections:
    2,511

selected C35 plan:
    S0C-UNAVAILABLE

primary no-go:
    C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE

secondary no-go:
    C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE

finite-delta Ward defect:
    0.2143273

analytic damped-identity residual:
    approximately 1.01e-16

one-loop contribution slots:
    18 UNRESOLVED_BLOCKING / NONZERO_UNKNOWN

tree:
    S_FB^(0)=1

failed projection:
    642 x 0, empty-not-zero

cross-root relation:
    NO_JOINT_MEASURE

integrity:
    216 production routes
    eight authoritative artifacts unchanged
    642 ART25 identities and covariance unchanged
    MSHT20_REP outside Git
```

Do not proceed if this baseline does not reproduce.

C36 must not modify:

- C11;
- the exact C32 tree reduction;
- the C33/C34/C35 historical soft roots and no-go results;
- the C35 finite-delta Ward defect;
- the bridge grid, roles, holdouts, ancestry, or `NO_JOINT_MEASURE`;
- ART25;
- production registry or authoritative artifacts.

Create new regulator roots and typed supersession edges only.

---

# 9. Required C36 architecture

Implement or extend immutable objects equivalent to:

```text
ReplacementRegulatorRootId
ReplacementRegulatorFamily
ReplacementRegulatorPlan
ReplacementRegulatorSelection

FiniteRapidityDirection
FiniteRapidityPair
FiniteRapidityInvariant
RapidityLimitOrder
RapidityEvolutionCoordinate

GaugeCovariantWilsonPath
SpacelikeWilsonSegment
FiniteLengthWilsonSegment
TransverseClosureSegment
WilsonEndpointRecord
WilsonCuspRecord

ReplacementCollinearRoot
ReplacementSoftRoot
ReplacementJointRegulator
ReplacementOverlapConvention

AuxiliaryFieldDirection
AuxiliaryFieldAction
AuxiliaryFieldPropagator
AuxiliaryResidualMass
AuxiliaryEndpointOperator
AuxiliaryPathJunction

ExponentialMeasurementRegulator
CoordinateShiftRegulator
FiniteLengthRegulator

FiniteRapidityBareSoft
FiniteRapidityRenormalizedSoft
FiniteRapidityCollinearOperator
FiniteRapidityProjectTMD

FiniteRapidityGaugeReport
FiniteRapidityWardReport
FiniteRapidityCuspReport
FiniteRapidityCSReport

ContinuumSchemeConversion
HardCompanionConversion
RapiditySchemeConversion
SchemeRoundTripReport

MicroscopicTreeReduction
FiniteBasisCompatibilityDecision
FiniteBasisMatchingStrategy

C36ContinuationGate
C36CapabilityMatrix
C36ClosureReport
```

Every object must be:

- immutable;
- content addressed;
- deterministic;
- explicit about source and target operators;
- explicit about gauge transformation;
- explicit about finite rapidity;
- explicit about path, endpoint, and transverse closure;
- explicit about UV, rapidity, and soft conventions;
- explicit about perturbative order and first omitted order;
- state and ART25 independent where labeled universal;
- unreachable from inference and production.

---

# 10. Compile mutually exclusive regulator plans

Compile and decide among:

## 10.1 `O4-SPACELIKE-COLLINS-JMY`

A finite-rapidity, gauge-covariant operator using genuine non-lightlike Wilson lines with source-defined spacelike directions:

```text
v^2 < 0
vbar^2 < 0
```

and a source-defined rapidity invariant.

Requirements:

```text
exact gauge covariance at finite rapidity
complete transverse closure
source-defined soft subtraction
one-loop continuum authority
Collins-Soper evolution
conversion to the project/ART25 convention
```

## 10.2 `O4-AUXILIARY-SPACELIKE`

A local one-dimensional auxiliary-field realization of the same spacelike Wilson geometry.

Requirements:

```text
exact Minkowski spacelike-direction map
auxiliary action and propagator
color representation
residual-mass/line renormalization
endpoint and cusp operators
piecewise transverse closure
finite-length and infinite-length relation
conversion to the selected continuum soft scheme
```

This may be the implementation of Plan 10.1 rather than a different physical soft factor. Do not add both.

## 10.3 `O4-EXPONENTIAL`

A gauge-invariant exponential/coordinate-shift regulator acting on the complete soft measurement or Wilson geometry.

Requirements:

```text
operator-level gauge invariance
source-defined measurement deformation
collinear/soft consistency
rapidity-renormalization convention
all-order or declared-order relation to a spacelike soft form factor
conversion to the project/ART25 scheme
finite-basis compatibility
```

## 10.4 `O4-FINITE-LENGTH-SPACELIKE`

A finite-length spacelike Wilson-line architecture with gauge-covariant endpoint closure and a source-supported infinite-length/rapidity limit.

## 10.5 `O4-DRESSED-FIELD`

A gauge-invariant dressed-field or Coulomb-gauge-equivalent T-even operator architecture, only if its large-momentum matching and relation to the project TMD are sufficiently explicit for the present light-front microscopic state.

## 10.6 `O4-UNAVAILABLE`

No candidate closes the required finite-regulator and matching identities.

Select exactly one physical primary plan before evaluating a numerical coefficient.

An auxiliary representation of the selected physical plan is a representation choice, not an additive second soft sector.

Create:

```text
docs/next_level/c36_regulator_plan_manifest.json
docs/next_level/c36_regulator_plan_selection.json
docs/next_level/c36_plan_exclusion_graph.json
```

---

# 11. Selection criteria

The selected plan must maximize scientific closure, not convenience.

Evaluate:

```text
finite-regulator gauge covariance
operator identity
soft/collinear pair completeness
transverse-link completeness
one-loop source authority
all-order factorization/evolution authority
finite-cutoff renormalization
auxiliary or tensor-network realizability
microscopic-state compatibility
tree reduction to C11
state-independent matching strategy
conversion to project/ART25
regulator-removal order
numerical realizability
minimum synthetic content
```

A plan fails if it requires a gauge-restoring counterterm that is fitted from the desired answer without an operator theorem.

Do not choose the plan by which one gives the smallest future ART25 residual.

Create:

```text
docs/next_level/c36_regulator_selection_scorecard.json
```

---

# 12. New joint collinear/soft root

The replacement regulator applies to both roots.

Define:

```text
C36_COLLINEAR_ROOT, B=1
C36_SOFT_ROOT,      B=0
```

with a common finite-rapidity pair.

For an off-light-cone plan, store exact direction records:

```text
v^mu
vbar^mu
v^2
vbar^2
v.vbar
orientation
future/past
normalization
rapidity values
source-defined invariant
lightlike-limit order
```

Do not hard-code a \(\rho\) formula from memory; transcribe and test the exact selected-source convention.

The roots share:

```text
gauge group
fundamental representation
Wilson directions
transverse displacement
path closure
rapidity parameter
UV target
soft-allocation convention
overlap convention
Fourier convention
```

They do not share a state vector or probability normalization.

Create:

```text
docs/next_level/c36_joint_root_identity.json
docs/next_level/c36_finite_rapidity_direction_manifest.json
docs/next_level/c36_joint_regulator_manifest.json
```

---

# 13. Gauge covariance at finite regulator

Prove at operator level that the selected finite-regulator paths transform as genuine Wilson lines or gauge-covariantly dressed fields.

For the closed soft trace, require gauge invariance at finite regulator before taking a rapidity limit.

Audit:

```text
endpoint transformations
transverse closure
junction transformations
path ordering
anti-path ordering
fundamental/anti-fundamental action
future/past reversal
singular-gauge transverse links
BRST or Ward identity at the selected scope
```

Required negative control:

```text
the inherited finite-delta modified-delta operator retains its C35 Ward
defect and fails this gate.
```

Create:

```text
docs/next_level/c36_finite_regulator_gauge_report.json
docs/next_level/c36_transverse_link_report.json
docs/next_level/c36_ward_benchmark.json
```

---

# 14. Spacelike/off-light-cone operator definition

When the spacelike plan is selected, define the bare soft factor and collinear correlator with the exact source path geometry.

Schematically:

\[
S_{v,\bar v}^{\rm bare}(b_T)
=
\frac{1}{N_c}
\langle 0|
\mathrm{Tr}
\left[
W_v^\dagger(b_T)
W_{\bar v}(b_T)
W_{\bar v}^\dagger(0)
W_v(0)
\right]
|0\rangle ,
\]

and:

\[
\Phi_{q,v}^{\rm unsub}(x,b_T)
=
\langle P|
\bar q(b)
W_v^\dagger(b)
\Gamma
W_v(0)
q(0)
|P\rangle ,
\]

with exact endpoint and transverse-closure conventions.

Do not treat these schematic equations as the source definition. The machine-readable records must follow the selected paper’s exact ordering, normalization, and subtraction convention.

Create:

```text
docs/next_level/c36_spacelike_soft_definition.json
docs/next_level/c36_spacelike_collinear_definition.json
docs/next_level/c36_soft_allocation_convention.json
```

---

# 15. Auxiliary-field realization

When used, formulate each Wilson segment through a one-dimensional auxiliary field.

Record:

```text
field statistics
color representation
direction vector
Minkowski/Euclidean identity
action
propagator
boundary conditions
residual mass
endpoint operators
piecewise-path junctions
cusp operators
finite-line ratio
infinite-line limit
renormalization scheme
```

Test:

```text
auxiliary propagator equals the selected Wilson segment
path composition
line reversal
endpoint transformation
color transport
finite-rapidity identity
one-loop coefficient at source scope
```

The recent auxiliary-field Collins-Soper extraction is a methodology and data source, not a project result. Preserve its current preliminary status.

Create:

```text
docs/next_level/c36_auxiliary_field_realization.json
docs/next_level/c36_auxiliary_wilson_equivalence.json
docs/next_level/c36_auxiliary_renormalization_report.json
```

---

# 16. Exponential and finite-length alternatives

When either is selected or retained as an oracle, define its operator action exactly.

For the exponential regulator, record whether the deformation acts on:

```text
the measurement
coordinate separation
total soft energy
Wilson endpoints
another source-defined object
```

For the finite-length regulator, record:

```text
segment lengths
endpoint closure
path geometry
large-length limit
rapidity relation
power corrections
```

Use the all-orders analytic relation among off-light-cone, finite-length, and exponential soft factors only at the exact scope supported by the source.

Create:

```text
docs/next_level/c36_exponential_regulator_manifest.json
docs/next_level/c36_finite_length_regulator_manifest.json
docs/next_level/c36_regulator_equivalence_matrix.json
```

---

# 17. Continuum tree and one-loop oracles

For every retained candidate, compile source-qualified continuum records at tree level and one loop where available.

Record separately:

```text
bare soft coefficient
UV poles/logs
rapidity logs
finite constants
cusp terms
endpoint/line terms
rapidity anomalous dimension
Collins-Soper convention
hard-factor companion
first omitted order
```

Require at least two independent checks for the selected plan:

```text
source expression
independent symbolic or direct-integral reconstruction
```

Create:

```text
docs/next_level/c36_selected_scheme_soft_oracle.json
docs/next_level/c36_selected_scheme_collinear_oracle.json
docs/next_level/c36_selected_scheme_oracle_validation.json
```

These are continuum/operator oracles, not a microscopic proton result.

---

# 18. Rapidity evolution and regulator limit

Define the selected finite-rapidity variable and its evolution derivative exactly.

Keep separate:

```text
finite-rapidity regulator value
Collins-Soper evolution variable
UV scale mu
rapidity scale zeta
lightlike limit
infinite-line limit
large-momentum limit where applicable
```

Test:

```text
rescaling invariance
rapidity derivative
cusp consistency
path transitivity
limit order
threshold independence at the operator level
```

No nonperturbative ART25 Collins-Soper fit parameter enters this calculation.

Create:

```text
docs/next_level/c36_rapidity_coordinate_manifest.json
docs/next_level/c36_rapidity_evolution_report.json
docs/next_level/c36_regulator_limit_order.json
```

---

# 19. Conversion to the project and ART25 conventions

Once both sides are already renormalized TMD objects, construct the finite conversion:

\[
F^{\rm project}
=
Z_{\rm selected\to project}
\otimes
F^{\rm selected}
+
R_{\rm selected\to project}.
\]

Then preserve the existing read-only project-to-ART25 alignment.

Factor the conversion into:

```text
operator-definition conversion
UV convention
rapidity convention
soft allocation
finite TMD factor
hard-factor companion
scale relocation
ordinary two-scale evolution
threshold map
```

Required checks:

- inverse;
- round trip;
- cross-section-level hard/TMD invariance;
- \(\mu\) RG;
- rapidity RG;
- flavor/antiquark relation;
- source/member independence;
- first omitted order.

Create:

```text
docs/next_level/c36_selected_to_project_conversion.json
docs/next_level/c36_conversion_roundtrip_report.json
docs/next_level/c36_hard_companion_conversion.json
docs/next_level/c36_downstream_art25_contract.json
```

Do not apply this conversion directly to the historical C11 density.

---

# 20. Exact tree reduction to C11

Construct the C36 collinear operator descendant and test its zero-coupling, finite-rapidity tree limit against the twelve nonzero C11 parents:

```text
u, d, ubar, dbar
x = 0.03, 0.10, 0.30
```

Require:

```text
matrix equality
forward scalar equality
quark/antiquark identity
future/past T-even equality
link-odd zero
normalization equality
```

The finite-rapidity Wilson line reduces to identity at tree level, but this does not by itself validate one-loop matching.

Create:

```text
docs/next_level/c36_c11_tree_reduction_report.json
docs/next_level/c36_operator_supersession_report.json
```

If the selected operator does not reduce to C11, issue the exact operator-replacement branch.

---

# 21. Decide the microscopic implementation architecture

Compile mutually exclusive implementation relations:

## 21.1 `CONTINUUM_UNIVERSAL_SOFT_PLUS_FINITE_BASIS_COLLINEAR_MATCHING`

The soft factor is an independent universal continuum/auxiliary finite-rapidity operator. The finite-basis microscopic state enters only through the collinear matrix element and a regulator-specific matching calculation.

## 21.2 `AUXILIARY_SPACELIKE_SOFT_PLUS_FINITE_BASIS_COLLINEAR_MATCHING`

The selected soft operator is realized through auxiliary fields, while the hadronic state remains the existing finite-basis TTN root.

## 21.3 `JOINT_FINITE_BASIS_FINITE_RAPIDITY`

Both collinear and soft sectors receive compatible finite-basis realizations with a proved matching to the selected continuum scheme.

## 21.4 `DRESSED_FIELD_MICROSCOPIC_OPERATOR`

The hadron operator is reformulated using a gauge-invariant dressed field and later matched to the physical TMD.

## 21.5 `IMPLEMENTATION_UNAVAILABLE`

No scientifically complete relation exists.

Select one before designing the next calculation.

The universal soft factor is not required to be represented as a probability amplitude in the hadron TTN.

Create:

```text
docs/next_level/c36_microscopic_implementation_plan.json
docs/next_level/c36_state_operator_soft_separation.json
```

---

# 22. Finite-basis compatibility and matching strategy

Audit whether the selected C36 collinear operator can be evaluated using the C11-C14 microscopic state.

Record:

```text
active quark operator
finite-basis state support
Wilson insertion support
spectator treatment
UV regulator
endpoint regulator
finite-rapidity direction
off-shell or mass IR plan
zero-bin/soft overlap convention
required Fock sectors
required counterterms
```

Select a future matching strategy:

```text
M36-A:
    direct source-identical matching

M36-B:
    proved regulator equivalence

M36-C:
    partonic difference in the selected finite-rapidity scheme

M36-D:
    auxiliary-field matching

M36-E:
    large-momentum/dressed-field matching

M36-F:
    unavailable
```

Do not calculate a hadron-level ratio.

Create:

```text
docs/next_level/c36_finite_basis_compatibility.json
docs/next_level/c36_future_matching_strategy.json
docs/next_level/c36_missing_partonic_calculation.md
```

---

# 23. Soft–collinear overlap and zero-bin convention

Define the selected scheme’s count-once relation.

Record:

```text
soft subtraction
zero-bin or equivalent overlap
measurement identity
IR regulator
finite-rapidity variables
UV convention
order of limits
```

Do not assume that the historical C32 spacelike-off-shell zero-bin contract automatically carries into the new regulator.

Allowed statuses:

```text
OVERLAP_DEFINITION_SOURCE_QUALIFIED
OVERLAP_OPERATOR_IDENTICAL_TEST_READY
OVERLAP_CONVERSION_REQUIRED
OVERLAP_UNRESOLVED
OVERLAP_INCOMPATIBLE
```

Create:

```text
docs/next_level/c36_overlap_convention.json
docs/next_level/c36_zero_bin_compatibility.json
```

---

# 24. Tensor-network and quantum interface

Preserve:

```text
TTN_hadron:
    microscopic B=1 state

soft/operator compiler:
    universal finite-rapidity Wilson operator or auxiliary-field root
```

Do not force the universal soft factor into the hadron-state probability tensor.

For an auxiliary-field plan, define a future QTN register and circuit contract for:

```text
direction
color
path segment
endpoint
cusp
auxiliary propagation
```

The circuit remains a nontrainable operator representation unless a later package explicitly authorizes trainable microscopic Hamiltonian parameters.

Create:

```text
docs/next_level/c36_tensor_network_interface.json
docs/next_level/c36_quantum_operator_interface.json
```

---

# 25. C36 continuation gate

C36 does not export a proton TMD and does not rerun the bridge.

It may issue:

```text
C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY
```

only when:

```text
one physical regulator plan is selected
finite-regulator gauge covariance closes
paired collinear/soft definitions exist
tree reduction to C11 closes
continuum tree/one-loop oracles are source qualified
rapidity evolution is defined
conversion to the project scheme is defined
finite-basis implementation relation is selected
future partonic matching strategy is executable
overlap/zero-bin convention is explicit
```

Create:

```text
docs/next_level/c36_continuation_gate.json
docs/next_level/c36_capability_matrix.json
```

The twelve bridge coordinates remain:

```text
12 BRIDGE_COMMON_DOMAIN_ONLY
0 BRIDGE_DISTRIBUTION_COMPARISON_READY
```

until a later regulator-specific microscopic calculation exports a renormalized TMD.

---

# 26. Remainder and uncertainty separation

Keep separate:

```text
selected-regulator perturbative truncation
off-light-cone/finite-rapidity power corrections
finite-length corrections
auxiliary-field conversion
endpoint/cusp renormalization
Wilson-line residual mass
UV-scheme conversion
rapidity-scheme conversion
soft-allocation conversion
hard-factor companion
finite-basis collinear matching
microscopic basis truncation
Fock/Wilson truncation
overlap/zero-bin uncertainty
two-scale evolution
downstream ART25 model covariance
numerical error
```

Unknown remains:

```text
NONZERO_UNKNOWN.
```

No remainder may be absorbed into ART25 covariance or a fitted proton normalization.

Create:

```text
docs/next_level/c36_uncertainty_budget.json
docs/next_level/c36_remainder_separation.json
```

---

# 27. Scientifically valid no-go outcomes

C36 must support rigorous negative results.

## 27.1 No finite-regulator gauge-invariant operator family closes

```text
C36_GAUGE_INVARIANT_RAPIDITY_REGULATOR_UNAVAILABLE
```

Next:

> **C37/O5 — non-Wilson or dressed-field microscopic TMD operator redesign**

## 27.2 Spacelike operator closes but auxiliary realization does not

```text
C36_SPACELIKE_CONTINUUM_ONLY
```

Next:

> **C37/R2 — continuum-spacelike soft plus finite-basis collinear partonic matching**

## 27.3 Auxiliary spacelike realization closes

```text
C36_AUXILIARY_SPACELIKE_ARCHITECTURE_READY
```

Next:

> **C37/A0 — auxiliary-field finite-rapidity soft calculation and finite-basis collinear interface**

## 27.4 Exponential architecture is selected

```text
C36_EXPONENTIAL_ARCHITECTURE_READY
```

Next:

> **C37/E0 — exponential-regulator microscopic collinear/soft matching pilot**

## 27.5 Tree reduction fails

```text
C36_REPLACEMENT_OPERATOR_INCOMPATIBLE_WITH_C11
```

Next:

> **C37/O1B — new microscopic collinear TMD operator root independent of C11**

## 27.6 Conversion to the project scheme is unavailable

```text
C36_PROJECT_SCHEME_CONVERSION_UNAVAILABLE
```

Next:

> **C37/C0 — selected-regulator-to-project continuum conversion completion**

Every no-go must specify the exact missing source, theorem, operator, or calculation.

Create:

```text
docs/next_level/c36_source_sufficiency_decision.json
docs/next_level/c36_no_go_decision_tree.json
docs/next_level/c36_missing_calculation_specification.md
```

---

# 28. Holdouts

Freeze holdouts before plan selection or conversion construction.

Reserve at least:

```text
one finite-regulator gauge transformation
one transverse-link transformation
one future/past reversal
one finite-rapidity value
one rapidity derivative
one one-loop finite constant
one cusp coefficient
one endpoint coefficient
one auxiliary residual-mass coefficient
one finite-length correction
one exponential/off-light-cone equivalence point
one conversion inverse
one conversion round trip
one hard-factor companion point
one u tree-reduction point
one d tree-reduction point
one ubar tree-reduction point
one dbar tree-reduction point
one finite-basis compatibility decision
one overlap/zero-bin decision
one current 2026 auxiliary-field result not used in construction
one ART25-independence control
```

Do not move failed holdouts into construction.

---

# 29. Required benchmark families

Implement at least:

## O4-A: immutable C35 no-go and supersession

## O4-B: primary-source regulator audit

## O4-C: regulator-plan selection

## O4-D: paired collinear/soft root identity

## O4-E: finite-rapidity direction and normalization

## O4-F: finite-regulator gauge covariance

## O4-G: transverse closure and singular-gauge completeness

## O4-H: selected soft and collinear operator definitions

## O4-I: auxiliary-field or alternative representation

## O4-J: continuum tree and one-loop oracles

## O4-K: rapidity evolution and limit order

## O4-L: selected-to-project scheme conversion

## O4-M: hard/TMD companion invariance

## O4-N: exact C11 tree reduction

## O4-O: finite-basis implementation strategy

## O4-P: overlap and zero-bin convention

## O4-Q: continuation/no-go decision

## O4-R: deterministic isolation and no readiness leakage

---

# 30. Negative injections

Create at least **2,640 ordered C36 semantic fault injections** with stable IDs and deterministic diagnostics.

Include:

## Baseline and supersession

- wrong C35 commit;
- C35 Ward defect overwritten;
- historical modified-delta root relabeled successful;
- C36 root aliases C33;
- B=0 state inserted into proton normalization.

## Plan selection

- two physical regulator plans selected;
- auxiliary and physical soft factors added;
- plan selected by ART25 residual;
- unsupported current paper promoted to exact authority;
- finite-delta modified-delta retained as microscopic primary.

## Finite-rapidity geometry

- timelike vector accepted where source requires spacelike;
- \(v^2\) sign lost;
- rapidity invariant hard-coded incorrectly;
- normalization changed without rapidity rescaling;
- lightlike limit taken before renormalization;
- future/past orientation lost.

## Gauge covariance

- transverse link omitted;
- endpoint transformations ignored;
- finite-regulator Ward defect hidden;
- gauge-restoring term fitted;
- singular-gauge completeness assumed;
- BRST closure claimed without action.

## Auxiliary fields

- Euclidean direction treated as identical Minkowski authority without map;
- residual mass omitted;
- endpoint operator omitted;
- cusp/junction omitted;
- finite-line and infinite-line objects aliased;
- preliminary CS extraction treated as project output.

## Exponential/finite-length plans

- measurement deformation applied after integration;
- finite length called rapidity evolution;
- all-order equality applied outside source scope;
- power corrections set to zero;
- gauge invariance assumed from name.

## Continuum oracles

- one transcription called two independent routes;
- source convention mismatch;
- UV and rapidity logs conflated;
- hard companion omitted;
- first omitted order hidden.

## Scheme conversion

- continuum conversion applied directly to C11;
- inverse absent;
- round-trip failure hidden;
- scale evolution absorbed into finite factor;
- ART25 CS model used in the conversion;
- flavor dependence invented.

## Tree reduction and microscopic compatibility

- tree normalization fitted;
- quark/antiquark alias;
- C11 and C36 operators added;
- failed tree point imputed;
- hadron-level ratio called matching;
- finite-basis regulator identity omitted.

## Overlap and readiness

- historical off-shell zero-bin citation reused automatically;
- overlap counted twice;
- soft factor called complete TMD;
- proton export created;
- twelve-point bridge rerun;
- likelihood or p-value created.

## Integrity

- ART25 member/data/chi2 used;
- bridge role changed;
- `NO_JOINT_MEASURE` changed;
- production registry changed;
- authoritative artifact changed;
- raw MSHT files committed;
- nondeterministic manifest.

---

# 31. Deliverables

Create at least:

```text
docs/next_level/c36_implementation_report.md
docs/next_level/c36_api.md
docs/next_level/c36_requirement_coverage.json
docs/next_level/c36_normative_source_integration.json
docs/next_level/c36_volume_xxi_requirement_crosswalk.json
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

docs/next_level/c36_auxiliary_field_realization.json
docs/next_level/c36_auxiliary_wilson_equivalence.json
docs/next_level/c36_auxiliary_renormalization_report.json

docs/next_level/c36_exponential_regulator_manifest.json
docs/next_level/c36_finite_length_regulator_manifest.json
docs/next_level/c36_regulator_equivalence_matrix.json

docs/next_level/c36_selected_scheme_soft_oracle.json
docs/next_level/c36_selected_scheme_collinear_oracle.json
docs/next_level/c36_selected_scheme_oracle_validation.json

docs/next_level/c36_rapidity_coordinate_manifest.json
docs/next_level/c36_rapidity_evolution_report.json
docs/next_level/c36_regulator_limit_order.json

docs/next_level/c36_selected_to_project_conversion.json
docs/next_level/c36_conversion_roundtrip_report.json
docs/next_level/c36_hard_companion_conversion.json
docs/next_level/c36_downstream_art25_contract.json

docs/next_level/c36_c11_tree_reduction_report.json
docs/next_level/c36_operator_supersession_report.json

docs/next_level/c36_microscopic_implementation_plan.json
docs/next_level/c36_state_operator_soft_separation.json
docs/next_level/c36_finite_basis_compatibility.json
docs/next_level/c36_future_matching_strategy.json
docs/next_level/c36_missing_partonic_calculation.md

docs/next_level/c36_overlap_convention.json
docs/next_level/c36_zero_bin_compatibility.json

docs/next_level/c36_tensor_network_interface.json
docs/next_level/c36_quantum_operator_interface.json

docs/next_level/c36_continuation_gate.json
docs/next_level/c36_capability_matrix.json
docs/next_level/c36_uncertainty_budget.json
docs/next_level/c36_remainder_separation.json

docs/next_level/c36_source_sufficiency_decision.json
docs/next_level/c36_no_go_decision_tree.json
docs/next_level/c36_missing_calculation_specification.md

docs/next_level/c36_holdout_report.json
docs/next_level/c36_injection_manifest.json
docs/next_level/c36_regression_report.json
docs/next_level/c36_unresolved_physics_gaps.md
```

Add ADRs for:

- retirement of finite-delta modified-delta as the microscopic regulator;
- selection of a gauge-invariant finite-rapidity family;
- paired collinear/soft replacement roots;
- spacelike Wilson-line geometry;
- auxiliary-field representation;
- exponential/finite-length alternatives;
- finite-regulator gauge covariance;
- tree reduction to C11;
- separation of universal soft and hadron TTN;
- selected-to-project conversion;
- overlap/zero-bin convention;
- exact continuation and no-go branches.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

All generated JSON must reproduce byte-for-byte.

Heavy symbolic expressions, auxiliary propagator tables, or continuum oracle arrays may remain outside Git under content-addressed runtime directories. Commit their schemas, hashes, dimensions, convention order, and deterministic reconstruction commands.

---

# 32. Acceptance criteria

C36/O4 is complete only when:

1. The exact C35 baseline reproduces before edits.
2. Historical C11-C35 roots and results remain immutable.
3. The C35 finite-delta gauge no-go remains explicit.
4. One physical replacement-regulator plan is selected before numerical comparison.
5. Mutually exclusive plans are not added.
6. Every retained source is version and hash locked.
7. The selected regulator preserves gauge covariance at finite regulator.
8. Complete Wilson path and transverse closure identities are explicit.
9. Paired B=1 collinear and B=0 soft roots are defined.
10. The roots share a common regulator but not a state vector.
11. Finite-rapidity directions and invariants follow an exact source convention.
12. Rapidity and lightlike/infinite-length limits have an explicit order.
13. The selected soft and collinear definitions are source audited.
14. Auxiliary-field status is distinguished from physical-scheme status.
15. Preliminary lattice results are not promoted.
16. Exponential and finite-length equivalences are used only at source scope.
17. At least tree and one-loop continuum oracles exist for the selected plan or fail closed.
18. The selected continuum oracle has an independent check.
19. Rapidity evolution and cusp consistency are defined.
20. The selected-to-project conversion is finite-order and source audited.
21. Hard-factor companion transformations are explicit.
22. Inverse and round-trip conversion are tested.
23. ART25 nonperturbative fit information does not enter the conversion.
24. The C36 operator reduces to C11 at tree level or fails with an exact branch.
25. Quark and positive-x antiquark identities remain separate.
26. One microscopic implementation relation is selected.
27. The universal soft factor is not inserted into the proton probability tensor.
28. One future finite-basis matching strategy is selected.
29. No hadron-level ratio is used as matching.
30. The overlap/zero-bin convention is explicit.
31. Historical off-shell equivalence is not assumed automatically.
32. C36 creates no microscopic proton TMD export.
33. C36 does not rerun the twelve-point bridge.
34. The continuation gate reflects exact achieved scope.
35. All remainder classes remain separate.
36. Unknown remainder remains nonzero-unknown.
37. All 642 ART25 identities and covariance remain unchanged.
38. `NO_JOINT_MEASURE`, ancestry, roles, and holdouts remain unchanged.
39. No fit, likelihood, posterior, optimization, reweighting, or emulator is created.
40. No process, deuteron, gluon, T-odd, inference, or production status is promoted.
41. Every no-go result includes an exact missing-calculation specification.
42. All inherited tests, builders, validators, requirements, injections, and manifests remain passing.
43. The production registry remains exactly 216 routes.
44. All eight authoritative artifacts remain byte-identical.
45. `MSHT20_REP/` remains outside Git.
46. At least 2,640 C36 semantic fault injections produce the expected diagnostics.
47. All C36 manifests reproduce byte-for-byte.
48. The working tree is clean except for the pre-existing untracked `MSHT20_REP/`.
49. A local completion commit is created and not pushed.

A rigorous selection of `O4-UNAVAILABLE` is valid. Do not weaken gauge covariance or scheme identity to issue a positive architecture.

---

# 33. Outcome branches

## Branch A: spacelike/Collins architecture closes

When:

```text
C36_SPACELIKE_FINITE_RAPIDITY_ARCHITECTURE_VALIDATED
C36_GAUGE_COVARIANT_COLLINEAR_SOFT_PAIR_VALIDATED
C36_SELECTED_TO_PROJECT_CONVERSION_VALIDATED
C36_C11_TREE_REDUCTION_VALIDATED
```

the exact next package is:

> **C37/R2 — spacelike finite-rapidity partonic collinear calculation, universal soft subtraction, and finite-basis LF-to-project matching**

## Branch B: auxiliary spacelike architecture closes

> **C37/A0 — auxiliary-field finite-rapidity soft calculation and finite-basis collinear interface**

## Branch C: exponential architecture closes

> **C37/E0 — exponential-regulator microscopic collinear/soft matching pilot**

## Branch D: continuum architecture closes but finite-basis compatibility remains open

> **C37/M0A — finite-basis collinear operator insertion and state-independent matching strategy**

## Branch E: tree reduction fails

> **C37/O1B — new microscopic collinear TMD operator root independent of C11**

## Branch F: conversion to the project scheme remains open

> **C37/C0 — selected-regulator-to-project continuum conversion completion**

## Branch G: no gauge-invariant replacement family closes

> **C37/O5 — gauge-invariant dressed-field or non-Wilson microscopic TMD redesign**

No branch automatically authorizes calibration or inference.

---

# 34. Allowed and forbidden statuses

The strongest permitted package statuses include:

```text
C36_REPLACEMENT_REGULATOR_AUDIT_COMPLETE
C36_REPLACEMENT_PLAN_DECIDED
C36_PAIRED_ROOT_ARCHITECTURE_AUDITED
C36_FINITE_RAPIDITY_GEOMETRY_VALIDATED
C36_FINITE_REGULATOR_GAUGE_COVARIANCE_DECIDED
C36_CONTINUUM_ORACLE_AUDITED
C36_RAPIDITY_EVOLUTION_AUDITED
C36_SELECTED_TO_PROJECT_CONVERSION_AUDITED
C36_C11_TREE_REDUCTION_DECIDED
C36_MICROSCOPIC_IMPLEMENTATION_PLAN_DECIDED
C36_FUTURE_MATCHING_STRATEGY_DECIDED
C36_CONTINUATION_GATE_DECIDED
C36_SOURCE_SUFFICIENCY_DECISION_COMPLETE
```

Issue only when exact gates pass:

```text
C36_SPACELIKE_FINITE_RAPIDITY_ARCHITECTURE_VALIDATED
C36_AUXILIARY_SPACELIKE_ARCHITECTURE_READY
C36_EXPONENTIAL_ARCHITECTURE_READY
C36_GAUGE_COVARIANT_COLLINEAR_SOFT_PAIR_VALIDATED
C36_SELECTED_TO_PROJECT_CONVERSION_VALIDATED
C36_C11_TREE_REDUCTION_VALIDATED
C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY
```

The following remain forbidden:

```text
C36_MICROSCOPIC_PROTON_TMD_EXPORTED
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

# 35. Final Codex response

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, injection, and fault-mode counts;
- exact primary sources and hashes;
- retained C35 finite-delta no-go;
- regulator candidates and decisions;
- selected physical regulator plan;
- selected representation plan;
- paired collinear/soft root identities;
- finite-rapidity vectors, invariants, and limit order;
- finite-regulator gauge and Ward results;
- transverse-link and endpoint status;
- selected soft and collinear operator definitions;
- auxiliary, exponential, finite-length, and dressed-field audit decisions;
- continuum tree/one-loop oracle residuals;
- rapidity-evolution and cusp status;
- selected-to-project conversion, inverse, round trip, and hard-companion status;
- C11 tree-reduction results;
- microscopic implementation relation;
- finite-basis compatibility and future matching strategy;
- overlap/zero-bin status;
- tensor-network and quantum-interface status;
- continuation-gate result;
- exact no-go and next branch where blocked;
- confirmation that no ART25 member, data, chi2, bridge residual, or proton-level ratio entered the work;
- confirmation that no microscopic TMD export, bridge rerun, fit, calibration, likelihood, posterior, optimization, reweighting, emulator, process promotion, or physical claim occurred;
- production/artifact integrity;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not describe a continuum regulator definition, a preliminary auxiliary-field extraction, or a tree-level reduction as a completed microscopic TMD matching calculation.
