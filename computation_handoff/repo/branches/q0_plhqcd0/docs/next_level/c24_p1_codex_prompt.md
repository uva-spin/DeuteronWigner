# C24/P1 Codex Work Package

## Title

**Source-qualified T-even process spine, exact source-input completion, and physical-input prerequisite construction**

## Authoritative baseline

Start from the local C23/P0 analytic-validation completion commit:

```text
0f6495107effda70ca406e8a44e365f3a8080198
```

The direct scientific C22Q ancestor must be:

```text
a1527fec32c07865de34d14dc1345ca9e816fac8
```

Do not use the previously mistyped longer hash beginning `a1527fef`.

A documentation-only descendant is acceptable only if the C23 commit remains in its ancestry and the complete C23 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

Do not push the final completion commit.

---

# 1. Why this package is next

C23 validates the process compiler only with synthetic analytic inputs.

Its authoritative capability is:

```text
438 ANALYTIC_PROCESS_ORACLE_ELIGIBLE identities
102 NOT_PROCESS_ELIGIBLE identities
0 SOURCE_PROCESS_VALIDATION_ELIGIBLE identities
0 PHYSICAL_PROCESS_INPUT_ELIGIBLE identities
```

C23 successfully implements:

- typed process, measurement, harmonic, hard, partner, fixed-order, and factorization/Glauber records;
- analytic Drell-Yan, SIDIS, and conditional heavy-quark-pair DIS compilers;
- six executable `VALIDATION_ONLY` W/Y process records at ranks 0 and 2;
- rank-1 and rank-3 mathematical W/Y oracles without process execution;
- the complete 23-entry spin-1 SIDIS kinematic basis;
- a broken-factorization colored-hadroproduction negative control;
- strict C22Q eligibility and rank gates.

But every hard, partner, TMDFF, fixed-order, Collins-Soper/large-b, and experimental object used by the executable C23 plans is synthetic.

C24 must replace a deliberately small and useful T-even subset of those synthetic inputs with exact, source-audited, reproducible records. It must construct the prerequisite bundles for stronger physical-input qualification without overstating their status.

C24 must not begin global inference or promote any production route.

---

# 2. Primary objective

Implement the chain:

```text
C22Q analytic-validation-qualified microscopic operator
    -> exact source expression and ancillary record
    -> source-qualified perturbative coefficient/collinear route
    -> source-qualified CS/large-b boundary plan
    -> source-qualified hard / partner / fixed-order record
    -> source-qualified process validation bundle
    -> physical-input prerequisite audit
```

The package must distinguish:

```text
ANALYTIC_PROCESS_ORACLE_ELIGIBLE
SOURCE_PROCESS_VALIDATION_ELIGIBLE
PHYSICAL_PROCESS_INPUT_ELIGIBLE
NOT_PROCESS_ELIGIBLE
```

The scientific objective is to make a nonempty `SOURCE_PROCESS_VALIDATION_ELIGIBLE` set for selected T-even processes if, and only if, all source gates can be satisfied.

The physical-input-qualified set may remain empty. It must remain empty wherever covariance, scheme, domain, nonperturbative-boundary, or joint-member requirements are incomplete.

---

# 3. Scope and nonclaims

C24 is:

```text
source-audited
process- and structure-function-specific
T-even only unless an exact multiparton route is independently completed
rank-aware
factorization/Glauber-status aware
validation-only
isolated from production and inference
```

C24 is not:

```text
a global TMD extraction
a new phenomenological fit
a posterior inference package
an all-order matching or evolution package
a physical T-odd process package
a complete deuteron matched-total prediction
a universal process-factorization proof
a production promotion
```

A source-qualified process-validation bundle is not automatically a physical prediction.

---

# 4. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant C19-C23 source, API, manifest, capability, audit, ADR, test, and roadmap files before changing the repository. Continue autonomously until every C24 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository content;
- run tests, builders, evidence, atlas, and validators;
- install routine local dependencies when permitted;
- download open primary papers, official code releases, and official ancillary files;
- preserve exact source packages locally;
- build deterministic source parsers and adapters;
- run source software in an isolated validation environment;
- construct independent symbolic and numerical oracles;
- regenerate deterministic manifests.

If a candidate source package lacks a reproducible covariance, scheme map, domain, or machine-readable release, record that limitation and leave the corresponding stronger qualification tier unavailable.

Do not digitize figures and call them source data.

Do not silently substitute a modern package version for the version used in the cited paper.

---

# 5. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_matching_fit_manifest.json

docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_capability_matrix.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_uncertainty_manifest.json

docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_splitting_function_library.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_accuracy_manifest.json
docs/next_level/c22_unresolved_physics_gaps.md

docs/next_level/c22q_implementation_report.md
docs/next_level/c22q_api.md
docs/next_level/c22q_capability_reconciliation.json
docs/next_level/c22q_process_eligibility_matrix.json
docs/next_level/c22q_qualification_contract.json
docs/next_level/c22q_cs_largeb_tier_manifest.json
docs/next_level/c22q_nuclear_operator_qualification.json
docs/next_level/c23_p0_prerequisite_contract.json

docs/next_level/c23_implementation_report.md
docs/next_level/c23_api.md
docs/next_level/c23_process_capability_matrix.json
docs/next_level/c23_wy_matching_manifest.json
docs/next_level/c23_factorization_glauber_manifest.json
docs/next_level/c23_process_accuracy_manifest.json
docs/next_level/c23_unresolved_physics_gaps.md

references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/volume_xvii_process_qualified_tmd_observables.tex
references/volume_xviii_smallb_ope_collinear_mixing.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use actual filenames when they differ.

Create:

```text
docs/next_level/c24_normative_source_integration.json
```

with exact hashes, roles, missing-file status, and supersession relations.

---

# 6. Immutable C23 baseline

Before edits, reproduce and record:

```text
1,095 tests
all C23 builders and validators
36/36 evidence rows
162/162 atlas pages
580 C23 requirements
720 C23 negative injections

438 analytic-process-oracle eligible
102 not process eligible
0 source-process-validation eligible
0 physical-process-input eligible

six executable validation-only W/Y records at ranks 0 and 2
rank-1 and rank-3 mathematical W/Y oracles only
23 spin-1 SIDIS kinematic structures classified

216 production routes
all eight authoritative artifacts byte-identical
all pinned C15-C23 manifests byte-identical
deterministic C19-C23 manifest reconstruction
```

C24 must not modify:

- any C19-C23 microscopic operator identity;
- the C22Q analytic qualification records;
- the original C23 analytic plan or its outputs;
- prior calibration/holdout roles;
- C21 Q grid or threshold history;
- C22 source-disagreement decisions;
- the 102 not-process-eligible identities;
- T-odd and multiparton unavailable statuses;
- the 216-route production registry;
- production provenance or default composition;
- authoritative artifacts.

Add versioned source-qualified records rather than overwriting analytic records.

---

# 7. Primary-source preservation

Preserve every used primary paper, official code release, ancillary file, parameter file, replica/Hessian set, and metadata record under:

```text
data/raw/c24_sources/
```

For every source, store:

```text
title
authors
DOI/arXiv/Zenodo/repository identity
paper version
software/data version
download date
canonical URL
local path
SHA-256
license
source role
exact equation/table/code locator
scheme and convention
domain
uncertainty representation
known limitations
```

A source paper and a software release are separate records.

A current software release cannot silently replace the version used in a paper.

---

# 8. Required initial source audit

Audit at least the following primary sources and official releases.

## 8.1 Common unpolarized TMD / TMDFF / CS source family

```text
arXiv:2503.11201
    Determination of unpolarized TMD distributions from the fit of
    Drell-Yan and SIDIS data at N4LL

Zenodo record 15006449
    ARTEMIDE v3.01
    The version used for the ART25 DY+SIDIS fit

Current ARTEMIDE releases
    Audit only for comparison and bug fixes.
    Do not replace v3.01 in a paper-reproduction plan without a declared map.
```

Attempt to preserve:

- the exact v3.01 source package;
- constants and configuration files used for ART25;
- parameter values;
- replica/Hessian or uncertainty information if officially released;
- TMDPDF, TMDFF, and CS-kernel source conventions;
- the fit domain and data ancestry;
- source code for DY and SIDIS observables;
- a deterministic paper-level reproduction subset.

## 8.2 Collins-Soper and large-b sources

```text
arXiv:2511.22547
    Lattice QCD determination of the CS kernel in the continuum and
    physical-mass limits

arXiv:2510.26489
    Joint extraction of the CS kernel from experimental and lattice data

arXiv:2402.06725
arXiv:2403.00664
    Earlier lattice constraints and independent comparisons
```

For every candidate bundle, audit:

- machine-readable central values;
- covariance or replicas;
- b values and units;
- continuum/chiral/infinite-momentum status;
- matching and renormalization scheme;
- usable domain;
- correlation between points and systematics;
- exact source release.

If a compatible machine-readable covariance bundle cannot be reproduced, it may support a source interface, comparison, or holdout, but not a physical-input qualification.

## 8.3 Drell-Yan

```text
arXiv:1111.4996
    Low-qT Drell-Yan factorization

arXiv:2207.07056
    Fiducial Drell-Yan at N4LL+N3LO

The exact CuTe-MCFM release used by the source paper
    Prefer the source-identified 10.3 release or its exact archived equivalent
```

Audit:

- hard factor and current;
- TMD/soft scheme;
- asymptotic expansion;
- fixed-order reference;
- fiducial measurement map;
- masses and electroweak parameters;
- code/source version;
- reproducible benchmark points.

## 8.4 SIDIS and fragmentation

```text
arXiv:2603.29673
    Unpolarized SIDIS at N3LO with two-dimensional qT subtraction

arXiv:2508.06134
    Spin-1 SIDIS kinematic and tree-level structure-function basis

arXiv:2105.08725
    MAPFF1.0 charged-pion fragmentation functions

arXiv:2204.10331
    Pion and kaon fragmentation functions at NNLO

arXiv:2606.16754
    HAPS pion/kaon fragmentation sets with public LHAPDF replicas

arXiv:2503.11201 and ARTEMIDE v3.01
    Unpolarized TMDFF and joint DY/SIDIS source plan
```

Audit each FF/TMDFF bundle independently.

A source-qualified SIDIS plan requires a compatible distribution-side scheme, fragmentation-side scheme, hard factor, Fourier convention, and uncertainty model.

## 8.5 Tagged DIS and inclusive b1

```text
arXiv:2603.23700
    Polarized spin-1 SIDIS II: deuteron and spectator tagging

arXiv:2006.03033
    Polarized electron-deuteron DIS with spectator tagging

arXiv:1706.02244
    Tagged deuteron DIS with final-state interactions
```

Audit the exact primary sources required for inclusive \(b_1\) coefficient functions, target-mass conventions, and tensor normalization.

C24 may qualify only an explicitly NN/IA-exclusive source plan if all selected operator blocks pass. It must not call that the complete deuteron matched total.

## 8.6 Gluon-sensitive conditional process

```text
arXiv:1309.0780
    Heavy-quark-pair DIS at low imbalance
```

Audit the exact link topology, color structure, mass scheme, hard factor, soft factor, domain, and source-level benchmark.

---

# 9. Source-qualification contract

Create a single authoritative evaluator for every candidate source-qualified operator and process chain.

A `SOURCE_PROCESS_VALIDATION_ELIGIBLE` identity requires all of:

```text
C22Q analytic validation qualification
exact source expression
authoritative ancillary or exact manageable transcription
source locator and source hash
independent source-level oracle
source domain
source scheme and conversion
source uncertainty model
source-qualified CS/large-b boundary plan
source-qualified hard/partner process inputs
rank and harmonic compatibility
factorization/Glauber certificate
complete accuracy and uncertainty manifest
```

A `PHYSICAL_PROCESS_INPUT_ELIGIBLE` identity additionally requires:

```text
covariance-bearing or replica physical nonperturbative inputs
joint covariance or reproducible member correlation
physical domain and scale validity
no synthetic object in the qualifying chain
physical experimental or lattice source ancestry
all selected nuclear components qualified
```

Return every failed gate.

Do not infer qualification from a paper title, perturbative order, TMD name, or executable source code alone.

---

# 10. Minimal source-qualified target families

Do not preselect a total source-qualified count.

Explicitly audit these process-relevant T-even families:

```text
rank-zero unpolarized quark and antiquark U
rank-zero spin-1 LL quark and antiquark where same-local-operator
    universality is proven
rank-zero quark helicity
quark transversity
rank-zero unpolarized gluon
rank-two linearly polarized gluon
```

For each family report:

```text
exact source coefficient status
collinear source status
CS/large-b source status
source uncertainty status
source process eligibility
physical-input eligibility
blocking reasons
```

Do not force any family to qualify.

Pretzelosity remains higher-twist-required at the audited twist-two route.

All T-odd and multiparton families remain unavailable unless their exact operator-specific matching and evolution are independently completed in a later package.

---

# 11. Exact source-expression completion

C22 executed explicit order-one validation distributions but did not promote them to source qualification.

C24 must add versioned source-qualified coefficient records for the selected minimal families only where it can establish:

```text
exact equation or official ancillary
distributional endpoint terms
color decomposition
scheme conversion
gamma5 conversion when relevant
source domain
implemented order
independent x-space and Mellin checks
source uncertainty/remainder
```

Do not overwrite C22 prototype records.

Create a supersession relation:

```text
C22_VALIDATION_PROTOTYPE
    BENCHMARKED_BY
C24_SOURCE_QUALIFIED_RECORD
```

or leave the source-qualified record unavailable.

A lower declared order with complete source control is preferable to an incomplete high-order transcription.

---

# 12. Source-qualified CS and large-b plans

Compile mutually exclusive plans such as:

```text
P1-CS-ART25
    ARTEMIDE v3.01 source-locked CS/large-b plan
    source parameter and uncertainty model
    source domain
    validation only

P1-CS-LATTICE
    compatible lattice source bundle
    source scheme map
    domain and uncertainty
    no physical claim without complete covariance

P1-CS-JOINT
    joint experimental+lattice source plan
    source-released members/covariance when reproducible

P1-CS-HYBRID
    source-qualified perturbative small-b kernel
    source-qualified low-dimensional large-b discrepancy
    multiple source constraints
```

Plans are alternatives, not additive mechanisms.

The evaluator must distinguish:

```text
SOURCE_RECORDED_CENTRAL_ONLY
SOURCE_QUALIFIED_WITH_UNCERTAINTY_MODEL
PHYSICAL_COVARIANCE_QUALIFIED
UNAVAILABLE
```

Do not call a central curve with no reproducible uncertainty a physical boundary.

Do not copy a quark kernel into the gluon sector.

Do not impose exact nonperturbative Casimir scaling.

---

# 13. Source-qualified fragmentation interface

Implement versioned bundles:

```text
CollinearFFSourceBundle
TMDFFSourceBundle
FFMemberCorrelation
FFSchemeConversion
FFDomain
```

The source-qualified SIDIS plan must retain:

- hadron species and charge;
- favored/unfavored identity;
- quark/gluon flavor;
- \(z\) domain;
- reference scales;
- collinear order;
- TMD matching/evolution scheme;
- central members and uncertainty members;
- source/data ancestry;
- source hash;
- valid process domain.

Use official LHAPDF sets, replica sets, or source releases when available.

A collinear FF set does not by itself constitute a TMDFF bundle.

A TMDFF fit from ART25 may be used only through the exact source release and its own scheme and member semantics.

---

# 14. Source-qualified Drell-Yan spine

Attempt to qualify at least:

```text
DY_UU_UNPOLARIZED_RANK0
```

and, only if the exact operator/source chain passes:

```text
DY_U_LL_TENSOR_RANK0 under an NN-only same-local-operator plan
DY_LL_HELICITY_RANK0
DY_TT_TRANSVERSITY
```

The source-qualified Drell-Yan record must contain:

```text
factorization theorem and domain
past-pointing links
hard factor and current
electroweak normalization
TMD/soft scheme
source-qualified two-hadron boundary members
fixed-order source
asymptotic expansion
rank-specific W/Y identity
measurement/fiducial map
source uncertainty
accuracy bottleneck
```

Do not use a synthetic second hadron TMD in a source-qualified plan.

If a physical second-hadron bundle is unavailable, the plan may remain source validation only or unavailable according to the contract.

---

# 15. Source-qualified SIDIS spine

Attempt to qualify at least:

```text
SIDIS_UU_UNPOLARIZED_D1_RANK0
```

and, only if the full source chain passes:

```text
SIDIS_LL_TENSOR_F1LL_D1_RANK0 under an NN-only plan
SIDIS_L_HELICITY_G1_D1
SIDIS_TRANSVERSITY_COLLINS_INTERFACE
```

The source-qualified SIDIS record must contain:

```text
current-fragmentation domain
future-pointing distribution link
TMDFF operator and scheme
z-scaled Fourier convention
hard factor
source-qualified PDF/TMDPDF and FF/TMDFF members
fixed-order source
asymptotic expansion
rank-specific W/Y identity
measurement definition
source uncertainty
accuracy bottleneck
```

The N3LO unpolarized SIDIS source may qualify only the compatible unpolarized fixed-order record.

It does not qualify tensor, helicity, transversity, or T-odd SIDIS by analogy.

The Collins interface remains unavailable unless a compatible source-qualified Collins TMDFF bundle exists.

---

# 16. Inclusive b1 and tagged DIS

C23 preserves these process identities but does not execute them.

C24 must perform an explicit source-prerequisite audit.

## 16.1 Inclusive b1

A source-qualified NN-only \(b_1\) validation plan requires:

```text
tensor-helicity operator identity
same-local-operator coefficient proof
quark and antiquark source route
target-mass and higher-twist status
heavy-flavor status
NN-only nuclear assumption plan
explicit exclusion of unavailable many-body blocks
source uncertainty
```

It must not be called the complete deuteron prediction.

If the operator-specific source route remains incomplete, retain `UNAVAILABLE`.

## 16.2 Tagged DIS

A source-qualified tagged IA/pole validation plan requires:

```text
C15-C18 NN spectral amplitude identity
source-qualified tagged factorization/IA record
spectator momentum/helicity
active proton/neutron identity
pole variable and residue
FSI status
tagged-to-inclusive closure
source domain and uncertainty
explicit NN-only assumption plan
```

No ordinary TMDFF enters the spectator-tagging record.

The full matched nuclear total remains unavailable.

---

# 17. Conditional heavy-quark-pair DIS

Attempt to promote the analytic C23 conditional record to a source-qualified conditional record.

Require:

```text
source factorization derivation
heavy-quark mass scheme
pair invariant mass and transverse hierarchy
hard factor
soft factor
exact Wilson-link topology
exact color structure
gluon TMD source qualification
rank-zero and rank-two identities
fixed-order/source benchmark
domain restrictions
Glauber/factorization certificate
```

No default \(f+d\) gluon combination is allowed.

If the gluon CS/large-b or linearly polarized gluon source route remains incomplete, retain the corresponding structure as source-interface-only or unavailable.

---

# 18. Source-qualified W+Y

For every source-qualified process structure \(A\):

\[
Y_A^{[N]}
=
\sigma_{A,\mathrm{FO}}^{[N]}
-
[W_A^{[N]}]_{\mathrm{asy,FO}}^{[N]}.
\]

The fixed-order and asymptotic records must match exactly in:

```text
process
external states
measurement and cuts
hard current
TMD/FF/soft scheme
operator basis
matching order
masses
scales
threshold history
target projector
rank and harmonic
perturbative order
```

C24 must keep the C23 analytic W/Y oracles immutable.

A source-qualified record is a new plan that must close against source-level benchmark points.

Do not retune the microscopic boundary, source TMD/FF parameters, or CS kernel to repair a Y-term mismatch.

Do not copy a rank-zero Y term into rank two.

---

# 19. Physical-input prerequisite matrix

Construct a complete matrix for every selected source-qualified candidate:

```text
source-qualified operator chain
source-qualified CS/large-b boundary
physical covariance status
TMDPDF/TMDFF member correlation
hard/fixed-order source
measurement source
nuclear-component qualification
process factorization status
physical-input eligibility
remaining physical blockers
```

Create explicit requirement bundles for later physical qualification.

The matrix must distinguish:

```text
SOURCE_PROCESS_VALIDATION_ELIGIBLE
PHYSICAL_PROCESS_INPUT_ELIGIBLE
```

A source-qualified executable process may still have `PHYSICAL_PROCESS_INPUT_ELIGIBLE = false`.

---

# 20. Nuclear scope and covariance

Only a selected assumption plan may enter a source-qualified process bundle.

Keep component status separate:

```text
NN
NNPI
DELTADELTA
SIX_QUARK_CLUSTER
SIX_QUARK_HIDDEN_COLOR
TRANSITION_AND_INTERFERENCE
COHERENT_PILOT
MATCHED_TOTAL
```

A source-qualified NN-only process plan must explicitly exclude the other components.

It cannot be presented as the full deuteron prediction.

Do not construct the matched total from an NN source-qualified result plus analytic unavailable components.

Preserve hidden-color basis covariance in every diagnostic that includes the compact sector.

---

# 21. Uncertainty and member identity

Preserve separately:

```text
microscopic/Hamiltonian member
nuclear plan/member
C20 matching covariance
C21 CS/evolution uncertainty
C22 coefficient/collinear uncertainty
source-boundary uncertainty
TMDFF/FF uncertainty
hard-factor truncation
fixed-order numerical uncertainty
W/Y profile uncertainty
heavy-quark mass/threshold uncertainty
nuclear component availability
factorization/Glauber status
experimental/measurement uncertainty
missing operator
source disagreement
```

Every process member must retain one indivisible identity:

```text
microscopic member
matching member
CS/large-b member
evolution member
coefficient member
second-hadron or TMDFF member
hard/fixed-order member
nuclear plan
process plan
measurement plan
```

Do not independently sample marginal bands.

---

# 22. Holdouts

Freeze holdouts before final parameter or adapter tuning.

Reserve at least:

- one ART25 DY source point;
- one ART25 SIDIS source point;
- one CS-kernel source point or moment;
- one Drell-Yan \(q_T\) transition point;
- one SIDIS \((x,z,Q,P_{hT})\) point;
- one source FF/TMDFF replica or eigenvector;
- one spin-1 LL operator test;
- one tagged pole or sum-rule test;
- one heavy-quark-pair rank-two point;
- one threshold-crossing process point;
- one source-version comparison;
- one physical-input eligibility negative control.

Do not move a failed holdout into calibration without a new model version and new independent holdouts.

---

# 23. Required benchmark families

Implement at least:

## P1-A: source package integrity

- paper/software/data version locks;
- source hashes;
- license and locator;
- wrong-version failure;
- deterministic extraction.

## P1-B: ART25 reproduction subset

- ARTEMIDE v3.01 source lock;
- constants and configuration;
- selected DY and SIDIS values;
- source parameter/member handling;
- v3.01 versus newer-version comparison without silent substitution.

## P1-C: source-qualified CS/large-b plans

- source domain;
- uncertainty tier;
- scheme conversion;
- holdouts;
- quark/gluon separation;
- no false physical-covariance claim.

## P1-D: exact selected coefficient records

- source expression;
- endpoint terms;
- x/Mellin checks;
- gamma5 where relevant;
- source-qualified supersession of C22 prototype.

## P1-E: source FF/TMDFF bundles

- official replica/Hessian sets;
- hadron charge/flavor;
- scheme and domain;
- member covariance;
- no plot digitization.

## P1-F: Drell-Yan source spine

- past links;
- hard/current;
- two source-qualified hadron inputs;
- fixed-order/asymptotic identity;
- source benchmark.

## P1-G: SIDIS source spine

- future link;
- z-scaled transform;
- TMDFF/FF member;
- unpolarized fixed-order source;
- source benchmark.

## P1-H: source-qualified W/Y

- exact FO/asymptotic identity;
- fixed-order recovery;
- rank separation;
- no boundary retuning.

## P1-I: spin-1 LL same-operator plan

- operator universality proof;
- NN-only assumption plan;
- no matched-total claim;
- source qualification decision.

## P1-J: inclusive b1 prerequisite

- tensor signs;
- quark/antiquark;
- coefficient status;
- NN-only versus complete-deuteron distinction.

## P1-K: tagged DIS prerequisite

- target fragmentation;
- pole residue;
- tagged-to-inclusive;
- NN-only source plan;
- FSI interface.

## P1-L: heavy-quark-pair DIS

- conditional certificate;
- exact link/color map;
- heavy mass/domain;
- rank-zero/rank-two source decision.

## P1-M: physical-input gate

- covariance-bearing positive control;
- source-only negative control;
- synthetic-only negative control;
- joint-member requirements.

## P1-N: process accuracy and bottlenecks

- source order;
- boundary order/status;
- hard/fixed-order order;
- true least-accurate ingredient;
- no accuracy laundering.

## P1-O: nuclear scope

- selected-plan exclusion;
- component-resolved status;
- no NN-to-total promotion;
- hidden-color covariance where applicable.

## P1-P: deterministic isolation

- analytic C23 plans immutable;
- no inference/likelihood;
- no production route;
- deterministic manifests.

---

# 24. Negative injections

Create at least **880 ordered C24 negative injections** with stable IDs and deterministic expected diagnostics.

The suite must include:

## Source integrity

- wrong paper version;
- wrong software version;
- current ARTEMIDE silently substituted for v3.01;
- missing source hash;
- wrong equation/code locator;
- unofficial fork used as authority;
- source file modified locally;
- missing license;
- source/domain omitted.

## Qualification inflation

- analytic record labeled source qualified;
- source central curve labeled physical covariance;
- physical-input tier without joint covariance;
- executable code treated as source uncertainty;
- paper download treated as ancillary ingestion;
- high perturbative order treated as full process accuracy.

## Coefficient/boundary

- C22 prototype directly relabeled;
- incomplete endpoint expression;
- missing gamma5 conversion;
- source boundary omitted;
- quark CS kernel copied to gluon;
- exact nonperturbative Casimir scaling imposed;
- lattice central points used without uncertainty tier.

## Drell-Yan

- synthetic second hadron in source plan;
- future link;
- hard current mismatch;
- fiducial/inclusive mismatch;
- wrong CuTe-MCFM version;
- source W with analytic-only Y;
- boundary retuned to fixed-order.

## SIDIS/FF

- collinear FF called TMDFF;
- hadron charge lost;
- favored/unfavored identity lost;
- \(z\)-scaling omitted;
- physical TMDFF claim without released members;
- N3LO unpolarized SIDIS assigned to LL/helicity;
- source FF version mismatch;
- FF covariance dropped.

## b1/tagged

- NN-only b1 called full deuteron;
- antiquark omitted;
- wrong LL sign;
- SIDIS integration used as sole b1 definition;
- tagged DIS given ordinary FF;
- pole residue changed by regular FSI;
- tagged-to-inclusive failure.

## Gluon

- default f+d mixture;
- generic DIS link map used;
- heavy-quark factorization outside domain;
- rank-two linear gluon demoted to rank zero;
- source qualification without gluon boundary.

## Nuclear

- NN qualification copied to NNPI/DeltaDelta/6q/coherent;
- matched total created from partially qualified components;
- hidden-color basis dependence;
- cluster/compact double counting.

## Uncertainty/member

- independently sampled marginal bands;
- source parameter/member mismatch;
- source covariance lost;
- matching and FF member shuffled;
- source/systematic uncertainty absorbed into scale variation;
- holdout reused for tuning.

## Readiness leakage

- global likelihood;
- posterior sampling;
- physical T-odd process term;
- complete physical deuteron process claim;
- production registry mutation;
- authoritative artifact mutation;
- analytic C23 record overwritten.

---

# 25. Deliverables

Create at least:

```text
docs/next_level/c24_implementation_report.md
docs/next_level/c24_api.md
docs/next_level/c24_requirement_coverage.json
docs/next_level/c24_normative_source_integration.json
docs/next_level/c24_primary_source_manifest.json
docs/next_level/c24_source_package_lock_manifest.json
docs/next_level/c24_source_coefficient_library.json
docs/next_level/c24_cs_largeb_source_manifest.json
docs/next_level/c24_fragmentation_source_manifest.json
docs/next_level/c24_hard_fixed_order_source_manifest.json
docs/next_level/c24_source_process_eligibility_matrix.json
docs/next_level/c24_physical_input_prerequisite_matrix.json
docs/next_level/c24_dy_source_validation_manifest.json
docs/next_level/c24_sidis_source_validation_manifest.json
docs/next_level/c24_b1_tagged_prerequisite_manifest.json
docs/next_level/c24_gluon_process_source_manifest.json
docs/next_level/c24_source_wy_manifest.json
docs/next_level/c24_accuracy_manifest.json
docs/next_level/c24_uncertainty_manifest.json
docs/next_level/c24_holdout_report.json
docs/next_level/c24_injection_manifest.json
docs/next_level/c24_regression_report.json
docs/next_level/c24_unresolved_physics_gaps.md
```

Add ADRs for:

- paper/software/data version locking;
- source-qualified versus physical-input qualification;
- ART25/ARTEMIDE source use;
- source CS/large-b tiers;
- TMDFF/FF source admissibility;
- source-qualified W/Y;
- NN-only spin-1 process plans;
- physical-input joint covariance;
- preservation of analytic C23 plans.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md  # documentation only if needed
```

All generated JSON must reproduce byte-for-byte.

---

# 26. Acceptance criteria

C24 is complete only when:

1. The exact C23 baseline reproduces before edits.
2. All used source papers, software, data, and ancillaries are locally preserved and hash audited.
3. Paper, software, and data versions are locked separately.
4. ARTEMIDE v3.01 is not silently replaced by a newer release.
5. A single authoritative source-qualification evaluator exists.
6. Analytic, source-qualified, and physical-input tiers remain distinct.
7. Every source-qualified coefficient has an exact source expression or authoritative ancillary.
8. Every source-qualified coefficient has independent source-level checks.
9. Every source-qualified boundary has a source domain and uncertainty tier.
10. Quark and gluon CS/large-b plans remain separate.
11. A source-qualified fragmentation interface is implemented or remains explicitly unavailable.
12. At least the minimal T-even families receive complete source-gate audits.
13. T-odd and multiparton channels remain fail-closed.
14. At least one Drell-Yan source-qualified candidate is fully audited.
15. At least one SIDIS source-qualified candidate is fully audited.
16. Source-qualified W/Y is executed only when FO/asymptotic identities match exactly.
17. Analytic C23 W/Y records remain immutable.
18. Inclusive b1 and tagged DIS receive explicit prerequisite decisions.
19. Heavy-quark-pair DIS remains conditional and domain limited.
20. NN-only plans remain distinct from the complete deuteron matched total.
21. Every candidate receives a physical-input prerequisite record.
22. Physical-input qualification is false wherever covariance/member/domain gates fail.
23. Member and covariance identity survive every source adapter.
24. Accuracy labels report the true bottleneck.
25. Holdouts remain outside source-adapter tuning.
26. Every C24 negative injection produces the expected diagnostic.
27. All prior C3-C23 tests, builders, requirements, injections, and manifests remain passing.
28. The production registry remains exactly 216 routes.
29. All eight authoritative artifacts remain byte-identical.
30. No likelihood, posterior, inference, or production route is created.
31. All C24 manifests reproduce byte-for-byte.
32. The working tree is clean.
33. A local completion commit is created and not pushed.

C24 may complete even if no source-qualified process chain closes, provided the audit is complete and the final report states the exact remaining source blockers.

It may declare the source-qualified process spine nonempty only when at least one complete process structure passes every source gate.

---

# 27. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C24_SOURCE_PACKAGE_VERSION_LOCK_VALIDATED
C24_SELECTED_COEFFICIENT_RECORDS_SOURCE_QUALIFIED
C24_CS_LARGEB_SOURCE_INTERFACES_VALIDATED
C24_FRAGMENTATION_SOURCE_INTERFACE_VALIDATED
C24_DY_SOURCE_PROCESS_CANDIDATE_VALIDATED
C24_SIDIS_SOURCE_PROCESS_CANDIDATE_VALIDATED
C24_SOURCE_QUALIFIED_WY_VALIDATED_AT_DECLARED_ORDER
C24_B1_TAGGED_SOURCE_PREREQUISITES_AUDITED
C24_HEAVY_PAIR_DIS_SOURCE_CONDITIONAL_RECORD_VALIDATED
C24_SOURCE_PROCESS_ELIGIBILITY_MATRIX_COMPLETE
C24_PHYSICAL_INPUT_PREREQUISITE_MATRIX_COMPLETE
C24_SOURCE_PROCESS_OBSERVABLE_BUNDLES_VALIDATION_ONLY
```

The following remain forbidden unless every corresponding gate actually closes:

```text
PHYSICAL_TMD_EXTRACTION
PHYSICAL_DRELL_YAN_PREDICTION
PHYSICAL_SIDIS_PREDICTION
PHYSICAL_B1_PREDICTION
PHYSICAL_TAGGED_DIS_PREDICTION
PHYSICAL_TODD_PROCESS_PREDICTION
COMPLETE_DEUTERON_MATCHED_TOTAL_READY
ALL_PROCESS_FACTORIZATION_PROVEN
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 28. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- source papers, software releases, data files, and ancillaries preserved;
- exact ARTEMIDE version used and comparison status to newer releases;
- selected coefficient families source qualified and still blocked;
- CS/large-b source plans and uncertainty tiers;
- whether any physical covariance-qualified boundary bundle was consumed;
- FF and TMDFF source bundles and member counts;
- source-qualified process-eligibility counts;
- physical-input-eligibility counts;
- Drell-Yan candidate status and residuals;
- SIDIS candidate status and residuals;
- source W/Y and fixed-order recovery residuals;
- b1 and tagged prerequisite results;
- heavy-quark-pair conditional status;
- nuclear component qualification;
- holdout results;
- accuracy bottlenecks;
- all remaining physical gates;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim a physical process prediction, physical TMD extraction, complete physical Collins-Soper boundary, complete deuteron matched total, inference readiness, or production readiness unless every corresponding prerequisite is genuinely satisfied.
