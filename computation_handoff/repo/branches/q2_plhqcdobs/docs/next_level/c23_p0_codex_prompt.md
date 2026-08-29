# C23/P0 Codex Work Package

## Title

**Process-qualified Drell–Yan, SIDIS, inclusive \(b_1\), tagged DIS, selected gluon-sensitive records, and rank-resolved \(W+Y\) validation**

## Authoritative baseline

Start from the local C22/M3 completion commit:

```text
12e1850d101b0d64de27ae0daaf4ae42772e2a22
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C22 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

## Primary objective

C23 implements the first process compiler above the microscopic, matching, evolution, and small-\(b_{\rm TMD}\) layers.

The required chain is:

```text
C18 microscopic nucleon/deuteron parent
    -> C20 source-audited reference matching
    -> C21 two-scale and threshold-qualified evolution
    -> C22 operator-specific small-b OPE and collinear mixing
    -> process-specific hard / partner / measurement records
    -> factorization and Glauber certificate
    -> rank-resolved W term
    -> same-order asymptotic expansion
    -> fixed-order reference
    -> rank-resolved Y term
    -> validation-only process observable bundle
```

The process layer must consume only identities that C22 classifies as fully M3 qualified.

The immutable C22 capability split is:

```text
438 M3-qualified
54 TMD-evolution-only
48 reference-matching-unavailable
```

C23 must not promote either of the latter two classes merely because a process formula contains a TMD with the same name.

## Scientific boundary

C23 is:

```text
process-qualified at declared order
source-audited
rank- and harmonic-resolved
factorization/Glauber-status aware
validation-only
isolated from inference and production
```

C23 is not:

```text
a global phenomenological fit
a physical TMD extraction
a complete physical fragmentation-function determination
a complete physical Collins-Soper-kernel determination
a universal process-factorization proof
a complete twist-three process package
an all-order W+Y implementation
a production promotion
```

---

# 1. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant reports, APIs, manifests, source records, formal volumes, tests, ADRs, and roadmap entries before changing code. Continue autonomously until every C23 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository content;
- run tests, builders, evidence, atlas, and manifest commands;
- install routine local dependencies when permitted;
- download openly available primary papers and official ancillary files;
- preserve external source files under versioned local paths;
- construct analytic or numerical fixed-order and asymptotic oracles;
- regenerate deterministic manifests.

If a physical hard, fragmentation, fixed-order, or covariance bundle cannot be obtained reproducibly, finish the typed interface and analytic validation route, but leave the physical process capability unavailable.

Do not digitize figures and call them physical source data.

Do not push the final commit.

---

# 2. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json

docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_evolution_capability_matrix.json
docs/next_level/c21_multiq_grid.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_nuclear_evolution_manifest.json

docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_splitting_function_library.json
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_accuracy_manifest.json
docs/next_level/c22_uncertainty_manifest.json
docs/next_level/c22_holdout_report.json
docs/next_level/c22_regression_report.json

references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual repository filenames when they differ.

Record exact hashes and source roles in:

```text
docs/next_level/c23_normative_source_integration.json
```

If Volume XVII or XVIII is absent, record that absence. Do not invent missing content. This prompt, Volume V, and the implemented C20-C22 APIs remain the executable specification.

---

# 3. Primary-source audit

Use primary papers and their own official ancillary or code releases as formula authorities.

Preserve all used source files under:

```text
data/raw/c23_sources/
```

with exact SHA-256 hashes.

The initial source audit must include, where relevant:

```text
arXiv:1111.4996
    Factorization Theorem for Drell-Yan at low qT and TMD distributions

arXiv:hep-ph/0204004
    Leading-twist single-transverse-spin asymmetries:
    Drell-Yan and deep-inelastic scattering

arXiv:2207.07056
    Fiducial Drell-Yan production at N4LL+N3LO

arXiv:2503.11201
    Unpolarized TMD distributions and fragmentation functions at N4LL

arXiv:2603.29673
    Two-dimensional qT subtraction and SIDIS at N3LO

arXiv:2510.00100
    Polarized neutral- and charged-current SIDIS at NNLO

arXiv:2508.06134
    SIDIS off a tensor-polarized spin-1 target

arXiv:2603.23700
    Polarized spin-1 SIDIS II: deuteron and spectator tagging

arXiv:2006.03033
    Polarized electron-deuteron DIS with spectator tagging

arXiv:1706.02244
    Tagged deuteron DIS with final-state interactions

arXiv:1309.0780
    Low-transverse-momentum heavy-quark-pair production in DIS

arXiv:1001.2977
    No generalized TMD factorization in back-to-back hadron hadroproduction
```

Also audit the primary sources needed for:

- inclusive \(b_1\) coefficient functions and target-mass conventions;
- the selected Drell–Yan hard factor and fixed-order reference;
- the selected SIDIS hard factor and fixed-order reference;
- TMD fragmentation matching and evolution;
- collinear fragmentation functions;
- heavy-quark masses and schemes;
- QED electroweak normalization where used;
- the exact \(W+Y\) convention.

## Source-status rule

A paper establishing one process or one structure function does not establish another.

Examples:

- an unpolarized N3LO SIDIS calculation does not establish polarized or tensor N3LO SIDIS;
- a color-singlet Drell–Yan hard factor does not establish a gluon-sensitive colored-final-state process;
- a 23-function spin-1 kinematic basis does not make all 23 factorized or perturbatively complete;
- a process Wilson-line map is not by itself a Glauber-cancellation proof;
- a TMD fragmentation fit without machine-readable covariance is not a physical covariance-bearing input bundle.

---

# 4. Immutable C22 baseline

Before edits, reproduce and record:

```text
1,071 tests
all C22 builders and validators
36/36 evidence rows
162/162 atlas pages
980 C22 requirements
720 C22 negative injections

15 primary C22 papers preserved
438 M3-qualified identities
54 evolution-only identities
48 unavailable identities

immutable historical counts:
492/48 C20 reference matching
438/102 C21 M2 evolution

endpoint/HPL residual: 0
gamma5 conversion residual: 3.2e-12
x-space/Mellin residual: 4.2e-11
threshold residual: 3.4e-12
route-A/route-B residuals: 6.8e-4 through 1.3e-3
rank 0-3 residuals: 2e-8 through 8e-8
nuclear impulse residual: 3.2e-12
hidden-color covariance: <= 2.1e-12

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C22 manifests byte-identical
deterministic C22 manifest reconstruction
```

C23 must not modify:

- any C19-C22 operator identity;
- the 438/54/48 M3 capability split;
- C21 Q grid, threshold, evolution paths, or kernel plans;
- C22 coefficient or splitting-function records;
- C22 source-disagreement decisions;
- C22 holdout roles;
- prior microscopic or nuclear states;
- the accepted production registry, provenance, or composition;
- authoritative artifacts.

---

# 5. Required software architecture

Extend the existing typed formal, matching, evolution, and provenance systems.

Implement or extend objects equivalent to:

```text
ProcessId
ProcessKinematics
MeasurementRecord
MeasurementConvention
Spin1StructureFunctionId
Spin1StructureFunctionBasis

HardFactorRecord
ElectroweakPrefactorRecord
TMDFragmentationOperatorId
TMDFragmentationBundle
CollinearFragmentationBundle
PartnerFunctionBundle

ProcessLinkColorMap
FactorizationGlauberCertificate
PowerCountingRecord
ProcessAccuracyManifest
ProcessCapabilityEntry
ProcessCapabilityMatrix

FixedOrderReference
FixedOrderChannel
AsymptoticExpansion
WTerm
YTerm
WYMatchingManifest
TransitionProfile
PowerCorrectionRecord

ProcessPredictionPlan
ProcessObservableMember
ProcessObservableBundle
ExperimentalMapInterface
C23ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- deterministic in serialization;
- explicit about source hashes and schemes;
- complete in rank, angular, link, color, target, and member identity;
- fail-closed on unavailable ingredients;
- isolated from inference and production.

Do not create process-specific copies of C20-C22 TMD objects.

---

# 6. Process capability logic

## 6.1 Structure-function-level qualification

Process readiness is assessed per structure function, not per process name.

Each entry must separately record:

```text
M3 distribution identity
partner distribution or fragmentation identity
hard factor
soft scheme
measurement harmonic
rank/Bessel order
link map
color map
fixed-order reference
asymptotic expansion
Y-term availability
power-correction status
factorization status
Glauber status
kinematic domain
accuracy bottleneck
reason for unavailability
```

A process may contain a mixture of:

```text
PROCESS_FULL_WY_VALIDATION
PROCESS_W_ONLY_TMD_REGION
PROCESS_COLLINEAR_ONLY
PROCESS_INTERFACE_ONLY
PROCESS_CONDITIONAL
PROCESS_EXPLORATORY
PROCESS_BROKEN_FOR_UNIVERSAL_TMD_PRODUCT
PROCESS_UNAVAILABLE
```

## 6.2 M3 gate

Only C22 `M3_FULLY_QUALIFIED` identities may enter a process \(W\) term.

The 54 evolution-only identities remain unavailable because they lack a complete small-\(b\)/collinear route.

The 48 matching-unavailable identities remain unavailable.

No process formula may bypass this rule.

## 6.3 T-odd gate

C22 leaves exact multiparton matching unavailable for:

```text
Sivers / Qiu-Sterman
Boer-Mulders
genuine worm gears
tri-gluon f type
tri-gluon d type
tensor-polarized T-odd channels
```

Therefore C23 may create their:

```text
kinematic structure-function identity
link-reversal rule
process capability record
unavailable diagnostic
```

but may not execute their physical \(W\) term or \(Y\) term.

The existence of a microscopic link-odd C14 boundary does not override the missing C22 multiparton matching and collinear evolution.

---

# 7. Spin-1 structure-function basis

Implement a machine-readable spin-1 measurement basis that separates:

```text
U
L
T
LL
LT
TT
```

and stores, for every structure function:

- lepton polarization;
- target vector/tensor polarization;
- parton polarization;
- detected final-state polarization when relevant;
- azimuthal angles and Trento or other convention;
- harmonic \(m\);
- Bessel order \(J_{|m|}\);
- extracted mass powers;
- parity and naive-T status;
- twist and power counting;
- beam/target charge factors;
- binning definition.

For spin-1 SIDIS, ingest the complete 23-function kinematic basis from the primary source and classify all entries. Do not assume that the 21 tree-level nonzero functions are all M3-qualified or W+Y-ready.

A basis entry that is kinematically allowed but dynamically unavailable remains represented with a typed reason.

---

# 8. Drell-Yan process records

## 8.1 Base factorization record

Implement a source-audited color-singlet Drell–Yan record in the low-\(q_T\) region:

\[
W_A^{\rm DY}(q_T,Q)
=
\sum_{a,b}
H_{ab,A}^{\rm DY}(Q,\mu)
\int_0^\infty
\frac{b\,db}{2\pi}
J_{|m_A|}(bq_T)
\widetilde F_{a/h_1}^{[-]}
\widetilde F_{b/h_2}^{[-]}
\mathcal M_A^{\rm DY}.
\]

Retain:

- beam and target species;
- quark/antiquark ordering;
- past-pointing links;
- lepton angular convention;
- electroweak current;
- rapidity and scale relations;
- target spin-1 channel;
- rank/harmonic;
- fiducial or inclusive measurement;
- source-audited hard and fixed-order status.

## 8.2 Initial executable structures

Audit at least:

```text
DY_UU_UNPOLARIZED_RANK0
DY_U_LL_TENSOR_RANK0
DY_LL_HELICITY_RANK0 where both incoming blocks are qualified
DY_TT_TRANSVERSITY where both incoming transversity blocks are qualified
```

Do not presuppose that every item is executable. The capability matrix decides.

The following remain unavailable unless their exact C22 multiparton routes are added in a later package:

```text
Sivers single-spin DY
Boer-Mulders angular structures
tensor-polarized T-odd DY
tri-gluon f/d DY
```

## 8.3 Link reversal

The process record must map the microscopic link identity to the past-pointing Drell–Yan link.

Test the exact future/past sign relation at the operator-record level.

Do not implement sign reversal by multiplying a named function by \(-1\) without transforming its complete operator identity.

---

# 9. SIDIS process records

## 9.1 Current-fragmentation SIDIS identity

Implement current-fragmentation SIDIS separately from tagged target fragmentation:

```text
CURRENT_FRAGMENTATION_SIDIS
```

The base \(W\) term is:

\[
W_A^{\rm SIDIS}(P_{hT},Q)
=
\sum_q e_q^2
H_{q,A}^{\rm SIDIS}
\int_0^\infty
\frac{b\,db}{2\pi}
J_{|m_A|}\!\left(\frac{bP_{hT}}{z_h}\right)
\widetilde F_{q/D}^{[+]}
\widetilde D_{h/q}
\mathcal M_A^{\rm SIDIS}.
\]

Retain:

- future-pointing distribution link;
- TMD fragmentation scheme;
- time-like coefficient/evolution identity;
- \(z_h\)-dependent Fourier convention;
- hadron species and charge;
- favored/unfavored flavor structure;
- polarization and harmonic;
- current-fragmentation region;
- fixed-order and power-correction status.

## 9.2 Fragmentation interface

Implement a typed TMD fragmentation interface with the same source discipline as the TMD distribution side.

At minimum provide:

1. a synthetic exact covariance-bearing TMDFF oracle;
2. a source-audited perturbative TMDFF matching record where available;
3. a source-audited collinear FF interface;
4. an attempted compatible physical unpolarized TMDFF bundle;
5. explicit unavailable status when machine-readable covariance, scheme, or domain information is insufficient.

A physical bundle must contain:

```text
central members
covariance or reproducible replicas
z and b domains
hadron species and charge
UV/rapidity/soft scheme
reference scales
matching/evolution convention
source hashes
fit-data ancestry
validity domain
```

Do not digitize published plots.

## 9.3 Initial SIDIS structures

Audit at least:

```text
SIDIS_UU_UNPOLARIZED_D1
SIDIS_LL_TENSOR_F1LL_D1
SIDIS_L_HELICITY_G1_D1 where beam/target record supports it
SIDIS_TRANSVERSITY_COLLINS_INTERFACE_ONLY
```

The transversity-Collins record remains interface-only unless a compatible Collins TMDFF bundle and process ingredients are source-qualified.

All Sivers, Boer-Mulders, and genuine worm-gear process terms remain unavailable under C22 capability.

## 9.4 Fixed-order status

The 2026 N3LO SIDIS calculation may qualify only the unpolarized fixed-order record and only when its observable definition, cuts, hadron definition, mass treatment, and source implementation are compatible.

It must not be assigned to polarized or tensor harmonics by analogy.

---

# 10. Inclusive \(b_1\)

Implement inclusive \(b_1\) as a distinct collinear process record:

\[
b_1(x,Q^2)
=
\frac12
\sum_q e_q^2
\left[
\delta_T q_D(x,Q^2)
+
\delta_T\bar q_D(x,Q^2)
\right]
+
\delta_{\alpha_s}
+
\delta_{\rm TMC}
+
\delta_{\rm HT}.
\]

Retain:

- tensor-helicity difference;
- \(f_{1LL}=-2\delta_Tf_1/3\) convention adapter;
- quark/antiquark charge weights;
- collinear coefficient order;
- target-mass status;
- higher-twist status;
- heavy-flavor status;
- nuclear-sector ancestry;
- Q-grid identity.

Required checks:

- direct tensor-helicity route;
- LL-projector route;
- GTMD/TMD/PDF route;
- collinear coefficient route;
- tensor sign convention;
- scale evolution;
- current/EMT and moment consistency where applicable.

Do not derive inclusive \(b_1\) by integrating an incomplete SIDIS implementation.

---

# 11. Tagged DIS

Implement:

```text
TARGET_FRAGMENTATION_TAGGED_DIS
```

as a process distinct from current-fragmentation SIDIS.

It must consume:

- the C15-C18 spin-resolved nuclear spectral amplitude;
- spectator momentum and helicity;
- active proton/neutron identity;
- tagged pole variable and residue;
- deuteron vector/tensor polarization;
- tagged-to-inclusive sum rules;
- final-state-interaction status;
- detector acceptance only through a separate experimental map.

Required process statuses:

```text
TAGGED_IA_VALIDATION
TAGGED_POLE_EXTRAPOLATION_VALIDATION
TAGGED_FSI_INTERFACE_ONLY
```

No ordinary TMD fragmentation function is used for spectator tagging.

A regular FSI model may distort the recoil distribution but cannot alter the nucleon-pole residue in the analytic benchmark.

---

# 12. Gluon-sensitive process records

## 12.1 Heavy-quark-pair DIS

Implement a `CONDITIONAL` heavy-quark-pair DIS record based on the source-audited one-loop TMD-factorization derivation.

Retain:

- heavy-quark mass scheme;
- pair invariant mass;
- imbalance and hard transverse momentum;
- gluon TMD scheme;
- process soft factor;
- hard factor;
- exact ordered-link topology derived from the source;
- color channel;
- factorization domain;
- fixed-order status.

Do not infer the link topology from a generic “DIS” label.

Do not assign a default \(f+d\) combination.

## 12.2 Other gluon channels

Create capability records for:

```text
DIS_DIJET
DIS_HEAVY_MESON_PAIR
QUARKONIUM_LOW_QT
HADRON_HADRON_BACK_TO_BACK_HADRONS
DIHADRON_HADROPRODUCTION
SMALL_X_DIFFRACTIVE_CHANNELS
```

Classify them honestly:

- `CONDITIONAL` when a process-specific factorization formula and soft/jet functions are established only in a declared domain;
- `EXPLORATORY` when the operator map or production model is incomplete;
- `BROKEN_FOR_UNIVERSAL_SEPARATE_HADRON_TMD_PRODUCT` for the known non-Abelian factorization-breaking hadroproduction class;
- `UNASSESSED` when no adequate primary factorization source is implemented.

A broken process record must not consume the project’s universal separate-hadron TMD bundles.

---

# 13. Factorization and Glauber certificate

Every process structure function receives:

```text
leading regions
hard scale hierarchy
soft decoupling
rapidity subtraction
Wilson-link map
color entanglement
Glauber cancellation/status
power corrections
proof source
domain
status
```

Use statuses:

```text
ESTABLISHED
CONDITIONAL
EXPLORATORY
BROKEN
UNASSESSED
```

A Wilson-line map is necessary but not sufficient for `ESTABLISHED`.

Preserve the distinctions:

```text
PARTONIC_WILSON_STAPLE
PROCESS_SOFT_FUNCTION
NUCLEAR_COHERENT_PROPAGATION
TAGGED_FINAL_STATE_INTERACTION
```

Shared soft regions require an explicit overlap/subtraction record.

---

# 14. Hard-factor and fixed-order libraries

## 14.1 HardFactorRecord

Every executable hard factor must contain:

```text
process
partonic channel
current
structure function/harmonic scope
scheme
renormalization scale
implemented order
first nonzero order
mass treatment
electroweak normalization
source citation
equation/code locator
source hash
transcription/build hash
independent oracle
known remainder
```

Do not apply an unpolarized hard factor to a polarized/tensor channel without proving hard-factor universality for the same current and leading-power operator.

## 14.2 FixedOrderReference

Every fixed-order reference must contain:

```text
observable definition
phase-space variables
cuts
binning
masses
PDF/FF scheme
renormalization/factorization scales
perturbative order
partonic channels
source/code identity
numerical tolerance
fiducial/inclusive status
```

An inclusive fixed-order result cannot be used as a fiducial reference without an explicit measurement map.

A source paper without reproducible code or sufficient analytic ingredients may support an interface/source record but not an executable physical fixed-order oracle.

---

# 15. Rank-resolved \(W+Y\)

For every supported structure function \(A\):

\[
\frac{d\sigma_A}{d\mathcal P}
=
W_A^{[N]}
+
Y_A^{[N]}
+
\delta_{A,\rm power},
\]

with

\[
Y_A^{[N]}
=
\sigma_{A,\rm FO}^{[N]}
-
\left[W_A^{[N]}\right]_{\rm asy,FO}^{[N]}.
\]

## 15.1 Same-identity rule

The fixed-order and asymptotic terms must use the same:

```text
process
measurement
kinematics and cuts
hard factor
operator basis
matching coefficients
TMD/FF/soft scheme
masses
scale choices
threshold history
spin-1 projector
rank and harmonic
perturbative order
```

A mismatch fails before numerical evaluation.

## 15.2 Analytic oracle

Implement a rank-\(0\) through rank-\(3\) analytic W+Y oracle with:

- known small-\(q_T\) singular terms;
- known regular fixed-order term;
- exact asymptotic subtraction;
- fixed-order recovery;
- profile independence at the declared order;
- harmonic-specific Bessel kernels.

This oracle is validation only.

## 15.3 Source-qualified physical records

Attempt at minimum:

```text
unpolarized Drell-Yan rank-zero W+Y
unpolarized SIDIS rank-zero W+Y
```

A physical/source-qualified record is executable only if the complete fixed-order and asymptotic ingredients are reproducible in the same scheme.

For tensor, helicity, transversity, and higher-rank harmonics, create W-only or unavailable records unless a matching fixed-order reference is independently source qualified.

Do not copy the unpolarized scalar \(Y\) term into another harmonic.

## 15.4 Transition profile

Store the transition/profile function and profile-variation plan separately from:

- TMD boundary uncertainty;
- perturbative scale uncertainty;
- fixed-order numerical uncertainty;
- power corrections.

The microscopic TMD boundary may not be retuned to repair an incomplete \(Y\) term.

---

# 16. Experimental-map interface

Represent measured observables as:

\[
\sigma_{\rm measured}
=
\mathcal A_{\rm det}
\circ
\mathcal R_{\rm QED}
\circ
\mathcal B_{\rm bin}
[\sigma_{\rm theory}].
\]

Implement typed interfaces for:

```text
bin integration
fiducial cuts
detector acceptance/efficiency
QED radiative corrections
resolution smearing
normalization and polarization nuisance maps
```

These maps remain external to the TMD, FF, nuclear amplitude, and process factorization theorem.

A C23 process prediction may use an analytic measurement oracle, but it may not claim an experimental prediction without a source-qualified measurement map.

---

# 17. Process plans

Compile exclusive plans such as:

```text
P0-DY-ANALYTIC
    analytic hard/fixed-order oracle
    M3-qualified TMDs
    rank-resolved W+Y validation

P0-DY-SOURCE
    source-audited color-singlet DY hard/fixed-order record
    C21/C22 TMD ensemble
    no global fit

P0-SIDIS-ANALYTIC
    synthetic exact TMDFF bundle
    analytic fixed-order oracle
    spin-1 structure-function compiler

P0-SIDIS-SOURCE
    compatible source-qualified unpolarized TMDFF/FF bundle
    source-audited hard/fixed-order record
    only supported structure functions

P0-B1
    inclusive collinear tensor record

P0-TAGGED
    target-fragmentation tagged IA/pole validation

P0-GLUON-HQPAIR
    conditional heavy-quark-pair DIS factorization record

P0-BROKEN-HADROPRODUCTION
    negative-control record proving universal-product rejection
```

Plans may be compared but never added.

---

# 18. Process capability matrix

Construct a deterministic `ProcessCapabilityMatrix`.

At minimum, classify every C22 M3-qualified identity against:

```text
Drell-Yan
current-fragmentation SIDIS
inclusive b1
tagged DIS
heavy-quark-pair DIS
selected gluon channels
```

Report independently:

```text
kinematic structure exists
M3 TMD/PDF identity available
partner/FF available
hard factor available
link/color map available
factorization certificate
fixed-order reference
asymptotic expansion
W term
Y term
full process status
reason for incompleteness
```

Do not set a target number of process-ready entries.

The count is a scientific output.

---

# 19. Accuracy and uncertainty

## 19.1 Process accuracy manifest

Each structure function records at least:

```text
microscopic Wilson order
reference matching order
small-b coefficient order
collinear evolution order
TMD cusp/noncusp/rapidity orders
CS-kernel source status
hard-factor order
partner/FF matching/evolution order
fixed-order order
asymptotic subtraction order
threshold order
nuclear operator order
process factorization status
Glauber status
power-correction status
```

The process accuracy is bounded by the least accurate required ingredient.

Do not label a process N3LO or N4LL merely because its unpolarized fixed-order or cusp ingredients reach that order.

## 19.2 Separate uncertainty axes

Preserve separately:

```text
microscopic/Hamiltonian and nuclear member
basis/Fock/Wilson truncation
C20 matching covariance
C21 CS-kernel uncertainty
C21 evolution curl/path ambiguity
C22 coefficient and collinear uncertainty
fragmentation-function uncertainty
hard-factor truncation
fixed-order numerical uncertainty
W+Y profile/transition uncertainty
power corrections
heavy-quark mass and threshold
factorization/Glauber status
experimental-map uncertainty
rank transform/quadrature
missing operator
source disagreement
```

Do not combine them before storage.

---

# 20. Holdouts

Freeze process holdouts before final tuning.

Reserve at least:

- one Drell–Yan \(Q\) or rapidity point;
- one Drell–Yan \(q_T\) transition point;
- one SIDIS \((x,z,Q,P_{hT})\) point;
- one spin-1 LL SIDIS structure function;
- one inclusive \(b_1\) moment or Q point;
- one tagged tensor observable;
- one heavy-quark-pair angular structure;
- one rank-two or rank-three analytic W+Y harmonic;
- one process-link reversal test;
- one threshold-crossing process point;
- one nuclear-plan/member variation;
- one factorization-negative-control process.

Do not move a failed holdout into calibration without creating a new version and new independent holdouts.

---

# 21. Required benchmark families

Implement at least:

## P0-A: process identity and measurement conventions

- deterministic process IDs;
- angle-convention adapters;
- spin-1 projector reconstruction;
- wrong-convention failures.

## P0-B: Drell–Yan factorization record

- color-singlet source record;
- past links;
- quark/antiquark ordering;
- hard-factor and scale checks.

## P0-C: Drell–Yan W+Y

- analytic ranks 0-3;
- source-qualified rank-zero route if reproducible;
- fixed-order recovery;
- wrong-order and wrong-cut failures.

## P0-D: spin-1 SIDIS basis

- all 23 kinematic structures represented;
- 21 tree-level nonzero source statuses;
- per-structure capability classification;
- no automatic executability.

## P0-E: TMD fragmentation interface

- synthetic exact bundle;
- source provenance;
- covariance;
- scheme round trip;
- physical-bundle availability decision.

## P0-F: SIDIS W and Y

- unpolarized rank-zero validation;
- LL tensor validation;
- \(z\)-dependent Fourier factor;
- no unpolarized Y copying.

## P0-G: inclusive \(b_1\)

- helicity difference;
- LL adapter;
- coefficient/evolution route;
- independent SIDIS status.

## P0-H: tagged DIS

- target-fragmentation identity;
- pole residue;
- tagged-to-inclusive closure;
- no ordinary FF.

## P0-I: heavy-quark-pair DIS

- conditional certificate;
- heavy mass;
- exact link/color source map;
- kinematic-domain tests.

## P0-J: factorization-breaking negative control

- back-to-back hadroproduction record marked broken;
- attempted universal TMD product rejected.

## P0-K: factorization/Glauber certificates

- established, conditional, exploratory, broken, unassessed;
- proof domain;
- shared-soft subtraction.

## P0-L: link/color preservation

- future/past maps;
- ordered gluon links;
- independent f/d channels;
- no default mixture.

## P0-M: process accuracy

- true bottleneck;
- no accuracy laundering;
- channel-specific order.

## P0-N: resolved nuclear process ancestry

- NN/NNPI/DeltaDelta/6q identities;
- hidden-color covariance;
- no scalar nuclear collapse.

## P0-O: experimental map separation

- binning/acceptance/QED outside theory object;
- analytic measurement oracle;
- no detector factor inside TMD.

## P0-P: deterministic isolation

- no likelihood or inference;
- no production route;
- deterministic manifests;
- prior artifacts unchanged.

---

# 22. Negative injections

Create at least **800 ordered C23 negative injections** with stable IDs, deterministic diagnostics, and machine-readable expected failures.

The suite must include:

## Process identity

- wrong process;
- wrong external state;
- wrong current;
- wrong beam/target polarization;
- wrong angular convention;
- wrong rank or harmonic;
- wrong fiducial/inclusive identity;
- wrong Q grid or threshold history.

## Capability bypass

- evolution-only identity used in W;
- matching-unavailable identity used in W;
- T-odd microscopic boundary used without C22 multiparton matching;
- unsupported many-body operator promoted;
- unavailable gluon double-flip process promoted.

## Drell–Yan

- future link used;
- sign reversal by name only;
- quark/antiquark ordering lost;
- hard factor from wrong current;
- unpolarized Y copied into tensor harmonic;
- mismatched fixed-order cuts.

## SIDIS/fragmentation

- tagged DIS treated as SIDIS;
- missing \(1/z\) Fourier factor;
- wrong TMDFF scheme;
- FF covariance dropped;
- physical FF claim from digitized plot;
- Collins FF substituted for D1;
- favored/unfavored identity lost;
- unpolarized N3LO fixed order assigned to tensor SIDIS.

## Inclusive b1

- wrong tensor sign;
- quark-only without antiquarks;
- SIDIS integration used as sole definition;
- target-mass/higher-twist omissions hidden;
- independent b1 normalization added.

## Tagged DIS

- spectator treated as current fragmentation;
- pole residue changed by regular FSI;
- tagged-to-inclusive failure;
- detector acceptance inserted into spectral amplitude.

## Gluon/factorization

- default f+d mixture;
- quark-like sign assigned to mixed gluon links;
- heavy-quark factorization used outside domain;
- conditional process marked established;
- broken hadroproduction universal product executed;
- Wilson map treated as Glauber proof.

## W+Y

- mismatched perturbative orders;
- mismatched schemes;
- mismatched masses;
- mismatched cuts;
- missing asymptotic subtraction;
- duplicate subtraction;
- scalar Y reused for ranked harmonic;
- boundary retuned to repair Y;
- profile uncertainty merged into TMD uncertainty;
- fixed-order recovery overstated.

## Accuracy/uncertainty

- N4LL label with order-one C22 bottleneck hidden;
- physical CS-kernel claim;
- missing FF uncertainty;
- factorization status omitted;
- independently sampled marginal members;
- nuclear ancestry dropped;
- hidden-color basis dependence;
- holdout reused for tuning.

## Readiness leakage

- global likelihood construction;
- posterior sampling;
- production registry mutation;
- authoritative artifact mutation;
- physical T-odd process claim;
- all-process readiness claim;
- experimental prediction without measurement map.

---

# 23. Deliverables

Create at least:

```text
docs/next_level/c23_implementation_report.md
docs/next_level/c23_api.md
docs/next_level/c23_requirement_coverage.json
docs/next_level/c23_normative_source_integration.json
docs/next_level/c23_primary_source_manifest.json
docs/next_level/c23_process_basis_manifest.json
docs/next_level/c23_spin1_structure_function_basis.json
docs/next_level/c23_hard_factor_library.json
docs/next_level/c23_fragmentation_interface_manifest.json
docs/next_level/c23_factorization_glauber_manifest.json
docs/next_level/c23_fixed_order_reference_manifest.json
docs/next_level/c23_wy_matching_manifest.json
docs/next_level/c23_process_capability_matrix.json
docs/next_level/c23_process_accuracy_manifest.json
docs/next_level/c23_uncertainty_manifest.json
docs/next_level/c23_holdout_report.json
docs/next_level/c23_injection_manifest.json
docs/next_level/c23_regression_report.json
docs/next_level/c23_unresolved_physics_gaps.md
```

Add ADRs for:

- process versus structure-function readiness;
- M3-only process consumption;
- Drell–Yan link mapping;
- SIDIS versus tagged DIS;
- fragmentation-source admissibility;
- rank-resolved W+Y;
- fixed-order/asymptotic identity;
- factorization/Glauber status;
- gluon process color maps;
- experimental-map separation.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md  # documentation only if needed
```

All generated JSON must reproduce byte-for-byte.

---

# 24. Acceptance criteria

C23 is complete only when all of the following hold:

1. The complete C22 baseline reproduces before edits.
2. All primary process sources used are preserved and hash audited.
3. Process readiness is evaluated per structure function.
4. Only 438 M3-qualified identities can enter W terms.
5. The 54 evolution-only and 48 unavailable identities remain fail-closed.
6. No physical T-odd process term bypasses the missing C22 multiparton route.
7. The full spin-1 structure-function basis is represented and convention checked.
8. Drell–Yan links, quark/antiquark ordering, and hard identity are correct.
9. SIDIS and tagged DIS are distinct process classes.
10. The TMD fragmentation interface passes synthetic end-to-end tests.
11. A physical fragmentation bundle is consumed only if source/covariance/scheme requirements pass.
12. Inclusive \(b_1\) closes independently of SIDIS.
13. Tagged-to-inclusive and pole-residue benchmarks close.
14. Heavy-quark-pair DIS is conditional and domain restricted.
15. Broken generalized-TMD hadroproduction is rejected.
16. Every process has a factorization/Glauber certificate.
17. W+Y analytic ranks 0-3 close.
18. Every executable physical/source W+Y route uses identical FO/asymptotic definitions.
19. No scalar Y term is copied into another rank or harmonic.
20. Fixed-order recovery closes through the declared order.
21. Process accuracy reports the true least-accurate ingredient.
22. Nuclear ancestry and hidden-color covariance survive process assembly.
23. Microscopic member identity survives all process contractions.
24. Experimental maps remain external to TMD/nuclear/process theory objects.
25. All frozen holdouts remain outside tuning.
26. Every C23 negative injection produces the expected diagnostic.
27. All prior C3-C22 tests, builders, requirements, injections, and manifests remain passing.
28. The 216 production routes remain unchanged.
29. All eight authoritative artifacts remain byte-identical.
30. No likelihood, posterior, inference, or production route is created.
31. All C23 manifests reproduce byte-for-byte.
32. The working tree is clean.
33. A local completion commit is created and not pushed.

---

# 25. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C23_PROCESS_STRUCTURE_FUNCTION_COMPILER_VALIDATED
C23_DRELL_YAN_FACTORIZATION_RECORD_SOURCE_AUDITED
C23_SIDIS_CURRENT_FRAGMENTATION_INTERFACE_VALIDATED
C23_TAGGED_DIS_TARGET_FRAGMENTATION_RECORD_VALIDATED
C23_INCLUSIVE_B1_PROCESS_RECORD_VALIDATED
C23_TMD_FRAGMENTATION_INTERFACE_VALIDATED
C23_HEAVY_QUARK_PAIR_DIS_CONDITIONAL_RECORD_VALIDATED
C23_FACTORIZATION_GLAUBER_CERTIFICATES_VALIDATED
C23_RANK_RESOLVED_WY_ANALYTIC_VALIDATED
C23_SOURCE_QUALIFIED_WY_RECORDS_VALIDATED_AT_DECLARED_ORDER
C23_PROCESS_CAPABILITY_MATRIX_COMPLETE
C23_PROCESS_OBSERVABLE_BUNDLES_VALIDATION_ONLY
```

The following remain forbidden:

```text
GLOBAL_PROCESS_FIT
PHYSICAL_TODD_PROCESS_PREDICTION
ALL_SPIN1_SIDIS_STRUCTURE_FUNCTIONS_READY
UNIVERSAL_GLUON_FD_PROCESS_MIXTURE
ALL_PROCESS_FACTORIZATION_PROVEN
PHYSICAL_SHADOWING_READY
ALL_ORDER_W_PLUS_Y
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 26. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- primary process sources preserved;
- process and structure-function counts;
- number of process entries by readiness status;
- confirmation that only 438 M3-qualified identities were eligible;
- Drell–Yan executable/unavailable structures and reasons;
- SIDIS executable/interface/unavailable structures and reasons;
- whether a compatible physical TMDFF bundle was consumed;
- inclusive \(b_1\) residuals;
- tagged-to-inclusive and pole residuals;
- heavy-quark-pair DIS status and domain;
- broken/unassessed process records;
- hard-factor and fixed-order source statuses;
- W+Y residuals by rank and process;
- fixed-order recovery residuals;
- factorization/Glauber statuses;
- process accuracy bottlenecks;
- nuclear and hidden-color covariance residuals;
- holdout results;
- all remaining physical gates;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim physical process predictions, physical T-odd process readiness, universal gluon process mixing, all-order W+Y, inference readiness, or production readiness under this package.
