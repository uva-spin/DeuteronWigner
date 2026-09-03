# C21/M2 Codex Work Package

## Title

**Physical anomalous-dimension and Collins–Soper-kernel libraries, threshold-qualified common multi-\(Q\) evolution, and scheme-qualified microscopic TMD ensembles**

## Authoritative baseline

Start from the local C20/M1 completion commit:

```text
47a1e2108253a2e8181b0342530fd909359c1982
```

A documentation-only descendant is acceptable only if this commit remains in its ancestry and the complete C20 baseline reproduces before any code changes.

Do not use `origin/main` as the scientific baseline if the local branch is ahead of the remote.

## Primary objective

Implement the first source-audited, threshold-qualified, rank-aware two-scale evolution package for the complete C20 matched microscopic operator graph.

The required chain is:

```text
C18 microscopic nucleon/deuteron parent
    -> C19 closed LF/QCD matching basis
    -> C20 source-audited declared-order matching coefficients
    -> source-audited anomalous-dimension library
    -> quark/gluon Collins-Soper kernel plans
    -> threshold-qualified two-scale evolution
    -> resolved multi-Q microscopic TMD ensembles
```

C21 must preserve every microscopic, operator, rank, link, color, nuclear-sector, scheme, and member identity through the evolution.

C21 is not a process-factorization package, not a \(W+Y\) package, not a global inference package, and not a production promotion.

## Completeness and autonomy

Completeness is the objective. Do not optimize for quickness.

Read all relevant source, API, manifest, architecture-decision, roadmap, and test files before implementing. Continue autonomously until every C21 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect the repository;
- run tests, builders, and validators;
- install routine local dependencies when the environment permits;
- download openly available primary papers or ancillary source files;
- construct local symbolic or numerical verification tools;
- regenerate deterministic manifests.

If one optional external data source is unavailable or not machine-readable, record that limitation, keep the corresponding physical constraint fail-closed, and complete the rest of the package.

Do not push the final commit.

---

# 1. Normative repository sources

Read completely and hash-audit at least:

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_requirement_coverage.json
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_matching_fit_manifest.json
docs/next_level/c20_external_bundle_manifest.json
docs/next_level/c20_step_scaling_manifest.json
docs/next_level/c20_regression_report.json
references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use the actual filenames present in the repository when they differ slightly. Record all normative-source hashes in:

```text
docs/next_level/c21_normative_source_integration.json
```

If Volume XVI is not present, do not invent its contents. Use this work-package prompt, Volume V, and the implemented C19/C20 APIs as the executable specification, and record the missing source explicitly.

---

# 2. External primary-source audit

Use primary papers and their own ancillary files only. Search results, reviews, secondary summaries, and copied code are not formula authorities.

The initial source audit must include, where relevant:

```text
arXiv:2002.04617
    Cusp and collinear anomalous dimensions in four-loop QCD from form factors

arXiv:2205.02242
    The Four-Loop Rapidity Anomalous Dimension and Event Shapes to Fourth Logarithmic Order

arXiv:2205.02249
    The Four Loop QCD Rapidity Anomalous Dimension

arXiv:1803.11089
    Systematic analysis of double-scale evolution

arXiv:2402.06725
    Determination of the Collins-Soper kernel from Lattice QCD

arXiv:2511.22547
    Lattice QCD Determination of the Collins-Soper Kernel in the Continuum and Physical Mass Limits

arXiv:2509.26316
    Collins-Soper Kernel and Reduced Soft Function in Lattice QCD

arXiv:2607.24587
    First constraints on the nonperturbative gluon Collins-Soper kernel
```

The source audit may add other primary references required for:

- the QCD beta function;
- noncusp anomalous dimensions;
- heavy-flavor threshold matching;
- physical running coupling;
- quark and gluon TMD evolution in the selected scheme;
- collinear nonsinglet, singlet, helicity, and transversity evolution;
- the selected nonperturbative-kernel parameterization.

For every external record, store:

- title, authors, arXiv or DOI identity;
- version/date used;
- local source path;
- source SHA-256;
- exact equation, table, or ancillary-file locator;
- convention translation;
- implemented perturbative order;
- independent verification;
- known limitations.

Do not transcribe a formula from an abstract, search snippet, presentation, review, or software comment.

---

# 3. Immutable C20 baseline

Before editing, reproduce and record:

```text
1,040 existing tests
all C20 builders and validators
36/36 evidence rows
162/162 atlas pages
770 C20 requirements
560 C20 negative injections
540 LF operator identities
540 QCD operator identities
492 audited executable matching entries
48 explicitly unavailable entries
216 accepted production routes
all eight authoritative production artifacts byte-identical
all pinned C15-C20 manifests byte-identical
deterministic C20 JSON reconstruction
```

Do not proceed if the scientific baseline cannot be reproduced. Diagnose rather than repair by changing accepted physics.

C21 must not modify:

- the accepted 216-route production registry;
- production provenance or default composition;
- any authoritative parent/correlator artifact;
- C19 or C20 operator identities;
- C20 coefficient values or source records;
- C20 calibration/holdout roles;
- the 48 explicit unavailable entries;
- any previous C3-C20 benchmark result.

---

# 4. Scientific scope

C21 implements the following layers:

1. a source-audited anomalous-dimension and running-coupling library;
2. source-audited heavy-flavor threshold maps;
3. independent quark and gluon Collins-Soper kernel objects;
4. continuum/lattice/external kernel-constraint interfaces;
5. direct-contour, integrability-improved, and optional \(\zeta\)-prescription evolution;
6. finite-order curl, contour, and transitivity diagnostics;
7. rank-preserving multi-\(Q\) evolution of every supported matched operator;
8. resolved nucleon/deuteron and nuclear-component evolution;
9. correlated member and uncertainty propagation;
10. scheme-qualified validation-only TMD ensemble exports.

C21 does not implement:

- SIDIS, Drell-Yan, or other process cross sections;
- hard factors or fragmentation functions;
- fixed-order \(Y\) terms;
- process \(f/d\) gluon color weights;
- physical global fitting;
- posterior inference;
- production promotion;
- physical twist-three matching that C20 left unavailable;
- all-order evolution;
- physical Glauber or factorization completion.

---

# 5. Required software architecture

Extend the existing formal/matching packages rather than creating a parallel type system.

Implement or extend objects equivalent to:

```text
AnomalousDimensionRecord
AnomalousDimensionLibrary
BetaFunctionRecord
RunningCoupling
ThresholdMatchingRecord
ThresholdHistory
EvolutionAccuracyManifest

PerturbativeCSKernel
NonperturbativeCSKernel
CSKernelConstraintBundle
CSKernelPlan
CSKernelFitManifest

EvolutionEndpoint
EvolutionPath
EvolutionOneForm
EvolutionCurlReport
EvolutionOperator
EvolutionCapabilityMatrix

CollinearEvolutionKernel
CollinearEvolutionPlan
RankAwareEvolutionPlan
MultiQGrid

SchemeQualifiedTMDMember
SchemeQualifiedTMDBundle
EvolutionEnsembleStore
ResolvedNuclearEvolutionManifest
C21ClosureReport
```

Every object must be:

- immutable or frozen after construction;
- serializable with deterministic round trips;
- content addressed;
- explicit about source hashes and conventions;
- fail-closed on incomplete identity;
- isolated from production roots.

---

# 6. Source-audited anomalous-dimension library

## 6.1 Complete identity

Each anomalous-dimension record must contain:

```text
quantity
parton representation
color factors
nf
perturbative expansion convention
first nonzero order
implemented order
UV/rapidity/TMD scheme
logarithm convention
source
equation locator
source hash
transcription hash
independent oracle
uncertainty/remainder status
```

The initial library must distinguish:

```text
QUARK_CUSP
GLUON_CUSP
QUARK_TMD_NONCUSP
GLUON_TMD_NONCUSP
QUARK_RAPIDITY_ANOMALOUS_DIMENSION
GLUON_RAPIDITY_ANOMALOUS_DIMENSION
QCD_BETA_FUNCTION
```

Do not infer a gluon record from a quark record through Casimir scaling beyond the perturbative order and color structures for which the relation is explicitly verified.

Quartic-Casimir terms and generalized Casimir relations must remain visible.

## 6.2 Convention adapters

Implement explicit adapters for:

- \(\alpha_s/(4\pi)\) versus \(\alpha_s/\pi\);
- \(\ln\zeta\) versus \(\ln\sqrt{\zeta}\);
- sign conventions for \(\mathcal D\), \(K\), and the rapidity anomalous dimension;
- factors of two in cusp and rapidity equations;
- quark versus gluon representations;
- active-flavor number \(n_f\);
- threshold history.

A coefficient with a numerically identical array but a different convention is a different object.

## 6.3 Independent verification

For every implemented order:

- reproduce published lower-order limits;
- compare independent four-loop rapidity records where applicable;
- test exact color decompositions;
- test known Abelian and conformal limits where meaningful;
- verify the mixed-derivative relation at the implemented order;
- verify source transcription with symbolic and numerical oracles.

A single implementation copied into two APIs is not an independent oracle.

---

# 7. Running coupling and heavy-flavor thresholds

Implement a source-audited running-coupling object with:

- declared beta-function order;
- reference \(\alpha_s\) and scale;
- active-flavor history;
- quark-mass threshold scheme;
- forward and reverse threshold maps;
- uncertainty and order status.

The physical threshold map must transform together:

- \(\alpha_s\);
- anomalous dimensions;
- collinear operator basis;
- coefficient functions;
- evolution history;
- accuracy manifest.

Changing \(n_f\) without a threshold map must fail.

Required threshold benchmarks:

1. forward/reverse round trip;
2. conserved-moment continuity;
3. path consistency across the threshold;
4. failure when only \(\alpha_s\) is changed;
5. failure when quark and gluon kernels use incompatible histories.

Do not label a toy threshold map as physical. Separate:

```text
ANALYTIC_THRESHOLD_ORACLE
SOURCE_AUDITED_PHYSICAL_THRESHOLD
UNAVAILABLE_FOR_OPERATOR_BLOCK
```

---

# 8. Collins-Soper kernel architecture

## 8.1 Representation-level universality

The kernel is represented as:

\[
\mathcal D_a(b;\mu)
=
\mathcal D_a^{\mathrm{pert}}(b_\ast;\mu)
+
\mathcal D_a^{\mathrm{NP}}(b)
+
\delta\mathcal D_a^{\mathrm{match}}(b),
\qquad a=q,g.
\]

Quark and gluon kernels are separate objects.

The kernel may not be independently fitted for:

```text
u, d, ubar, dbar
proton, neutron, deuteron
U, L, T, LL, LT, TT
NN, NNPI, DeltaDelta, six-quark
each named TMD
each transverse rank
```

Those distinctions belong to the boundary and matching coefficients.

## 8.2 Kernel plans

Compile mutually exclusive plans such as:

```text
M2-PLAN-PERT-ORACLE
    source-audited perturbative kernel
    analytic validation-only large-b completion
    no physical external constraint

M2-PLAN-Q-LATTICE
    source-audited perturbative kernel
    compatible quark lattice constraint bundle
    low-dimensional common quark NP kernel

M2-PLAN-Q-HYBRID
    compatible quark lattice and phenomenological-style constraints
    source-audited perturbative kernel
    low-dimensional shared discrepancy basis

M2-PLAN-QG-EXPLORATORY
    quark kernel as above
    separate exploratory gluon constraint bundle
    no enforced nonperturbative Casimir scaling
```

Plans are alternative theories. They may be compared but never added.

## 8.3 Quark lattice constraints

Attempt to construct source-qualified quark-kernel bundles from compatible primary releases.

A physical bundle requires:

- machine-readable central values;
- covariance or a reproducible systematic model;
- \(b\) values and units;
- lattice spacings and mass information;
- continuum/chiral/infinite-momentum status;
- matching and renormalization scheme;
- source hashes;
- a declared usable domain.

If a paper does not supply a compatible machine-readable covariance bundle, do not digitize a figure and call it physical data. Record it as qualitative or holdout-only information.

The 2025 continuum/physical-mass determination may be considered a physical-source candidate only after the above interface requirements are verified.

## 8.4 Gluon lattice constraints

Treat the 2026 first gluon-kernel constraints as an exploratory source unless the primary release establishes all needed continuum, discretization, matching, covariance, and machine-readable-data requirements.

In particular:

- do not copy the quark kernel into the gluon sector;
- do not impose exact nonperturbative Casimir scaling;
- retain single-lattice-spacing limitations when present;
- retain close-to-physical rather than physical-mass status when applicable;
- retain source matching order and transverse-range limits;
- use the result as an exploratory constraint or holdout when a physical bundle is not justified.

## 8.5 Kernel fit

Use a low-dimensional, common representation-level parameterization such as a constrained spline, orthogonal basis, or physically motivated analytic form.

The fit must report:

- parameter ownership;
- prior/naturalness assumptions;
- Jacobian rank;
- singular values;
- null directions;
- covariance;
- calibration data;
- holdouts;
- perturbative-window overlap;
- large-\(b\) extrapolation;
- source tensions;
- model-discrepancy status.

Do not assign one parameter per data point or per TMD.

---

# 9. Two-scale evolution engine

Use the project convention:

\[
\frac{d}{d\ln\mu}\ln \widetilde F_a
=
\gamma_F^a(\mu,\zeta),
\]

\[
\frac{d}{d\ln\sqrt{\zeta}}\ln \widetilde F_a
=
-\mathcal D_a(b;\mu),
\]

with:

\[
\frac{\partial\gamma_F^a}{\partial\ln\sqrt{\zeta}}
=
-\Gamma_a,
\qquad
\frac{d\mathcal D_a}{d\ln\mu}
=
\Gamma_a.
\]

## 9.1 Evolution routes

Implement and compare:

```text
DIRECT_CONTOUR
INTEGRABILITY_IMPROVED
ZETA_PRESCRIPTION   # only if fully specified in the project convention
```

Each route must store:

- endpoints \((\mu_i,\zeta_i)\to(\mu_f,\zeta_f)\);
- contour/profile;
- perturbative orders;
- kernel plan;
- threshold history;
- numerical solver;
- curl-restoration prescription;
- source identities.

## 9.2 Curl and path dependence

Define the evolution one-form:

\[
\omega_a
=
\gamma_F^a\,d\ln\mu
-
\mathcal D_a\,d\ln\sqrt{\zeta}.
\]

Report:

- local curl;
- integrated contour difference;
- transitivity residual;
- scale-variation envelope;
- threshold contribution;
- numerical integration error.

The exact analytic oracle must be path independent.

The finite-order physical library may retain a nonzero curl. This is an uncertainty component, not a fit target.

Do not tune the nonperturbative kernel to erase a perturbative curl.

## 9.3 Composition and reversal

Test:

\[
R(C_2\circ C_1)=R(C_2)R(C_1)
\]

within the declared truncation and numerical errors.

Test reverse evolution and loop contours.

Evolution must preserve:

```text
T-even future/past equality
T-odd future/past sign reversal
ordered gluon-link identity
f/d color identity
transverse rank
target channel
parton polarization
microscopic member
nuclear ancestry
```

Using different evolution kernels for future and past links in the same representation must fail.

---

# 10. Collinear evolution library

For the C20-supported twist-two blocks, implement source-audited collinear evolution records for:

```text
unpolarized nonsinglet
unpolarized singlet q/g
helicity nonsinglet
helicity singlet q/g
transversity
spin-1 LL singlet q/g where the local operator class is shared
```

Each record must include:

- source and target basis;
- implemented perturbative order;
- scheme;
- splitting-function convention;
- plus distributions and endpoints;
- conserved moments;
- threshold map;
- source and transcription hashes;
- unavailable mixing blocks.

Do not create a twist-three collinear evolution route from a twist-two kernel.

The following remain unavailable unless independently source-audited and implemented:

```text
Qiu-Sterman / Sivers multiparton evolution
Boer-Mulders chiral-odd twist-three evolution
tri-gluon f-type evolution
tri-gluon d-type evolution
genuine worm-gear multiparton evolution
tensor-polarized T-odd multiparton evolution
```

A TMD evolution kernel may be formally available while the matched collinear boundary remains unavailable. The capability matrix must preserve this distinction.

---

# 11. Rank-aware multi-Q evolution

## 11.1 Capability matrix

Construct a complete `EvolutionCapabilityMatrix` for all 540 C20 identities.

For each identity record separately:

```text
reference-scale matching availability
small-b coefficient availability
collinear evolution availability
TMD anomalous-dimension availability
CS-kernel availability
threshold availability
rank-transform availability
multi-Q ensemble availability
reason for unavailability
```

Do not change the C20 count of 492 executable matching entries and 48 unavailable matching entries. C21 may have fewer fully evolvable entries than 492.

## 11.2 Q grid

Derive the reference point from the C20 scheme manifest.

Construct a deterministic validation grid containing at least:

- the reference \(Q_0\);
- one lower \(Q\) only if backward evolution is inside the validated domain;
- at least four higher \(Q\) values;
- at least one point on each side of a declared heavy-flavor threshold when the domain permits;
- a high-\(Q\) perturbative-window point.

The exact grid is part of the manifest and may not be changed after examining holdout results.

## 11.3 Rank preservation

For every supported rank \(m=0,1,2,3\):

- transform to \(b_{\mathrm{TMD}}\) space with \(J_{|m|}\);
- evolve without changing rank;
- invert to \(k_T\) space;
- report round-trip and evolution residuals;
- retain Fourier phase, extracted powers, and reference mass.

A scalar \(J_0\) route applied to a ranked object must fail.

## 11.4 Microscopic member identity

Each evolved member must retain one indivisible identity:

```text
Hamiltonian member
nucleon/deuteron member
nuclear plan
matching plan
coefficient member
CS-kernel member
scale/path member
threshold history
rank transform
numerical grid
```

Do not construct cross-observable covariance from independently sampled marginal bands.

---

# 12. Resolved nuclear evolution

Retain the complete C18 nuclear graph:

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

## 12.1 Impulse commutation

For scale-independent impulse kernels, verify numerically:

\[
P\otimes_x(S\otimes_x f)
=
S\otimes_x(P\otimes_x f).
\]

Test this for:

- proton-active and neutron-active pieces;
- quarks, antiquarks, and gluons;
- \(U,L,T,LL,LT,TT\);
- at least two ranks;
- several microscopic members;
- several Q values.

## 12.2 Independent many-body evolution

Pion, transition, coherent, DeltaDelta, compact, and two-body operators with independent scale dependence must receive:

- their own matching/evolution block;
- or an explicit unavailable status.

Do not evolve the matched total with a single scalar factor when its components have different operator content.

## 12.3 Hidden-color covariance

Apply at least two unitary rotations in the four-dimensional hidden-color complement.

The complete six-quark and matched evolved observables must remain invariant within tolerance.

Individual hidden-color basis components may change.

---

# 13. Uncertainty and accuracy manifests

## 13.1 Accuracy tuple

Use a machine-readable accuracy object containing at least:

```text
cusp order
noncusp order
rapidity order
beta-function order
matching-coefficient order
collinear-evolution order
CS perturbative order
CS nonperturbative source status
threshold order
rank-transform order/status
nuclear-operator order
Wilson order
```

Generate a human-readable logarithmic label only after checking the complete tuple.

No accuracy laundering is permitted. A four-loop cusp or rapidity anomalous dimension cannot upgrade a channel whose matching coefficient, collinear kernel, or kernel constraint is lower order or unavailable.

## 13.2 Separate uncertainty axes

Report separately:

```text
microscopic/Hamiltonian member uncertainty
basis and Fock truncation
Wilson-order truncation
C20 matching covariance
coefficient perturbative truncation
anomalous-dimension truncation
finite-order curl/path ambiguity
quark CS-kernel constraint uncertainty
gluon CS-kernel exploratory uncertainty
large-b extrapolation
threshold matching
nuclear many-body evolution
hidden-color/cluster matching
rank transform and quadrature
numerical ODE/integration
external-source covariance
missing-operator uncertainty
```

An optional combined summary may be supplied only after the separated axes are preserved.

---

# 14. Required benchmarks

Implement at least the following benchmark families with stable IDs.

## M2-A: anomalous-dimension source audit

- published lower-order values;
- four-loop quark/gluon cusp checks;
- independent four-loop rapidity checks;
- convention round trips;
- wrong-factor and wrong-sign injections.

## M2-B: running coupling and thresholds

- analytic running oracle;
- physical source-audited running;
- forward/reverse threshold;
- conserved moment;
- incompatible \(n_f\) histories fail.

## M2-C: exact integrable two-scale oracle

- zero curl;
- contour independence;
- transitivity;
- reverse evolution;
- loop contour returns identity.

## M2-D: finite-order physical evolution

- visible nonzero curl when expected;
- direct versus improved paths;
- scale variation;
- no fitting away the curl.

## M2-E: quark CS-kernel constraint

- compatible source ingestion or explicit unavailable status;
- perturbative overlap;
- holdout;
- covariance propagation;
- large-b extrapolation test.

## M2-F: gluon CS-kernel exploratory constraint

- independent gluon object;
- no silent quark copying;
- no exact NP Casimir assumption;
- source limitations retained;
- exploratory/holdout status.

## M2-G: rank 0-3 evolution

- forward/inverse transforms;
- rank preservation;
- Q-grid evolution;
- wrong-Bessel injection.

## M2-H: link and color preservation

- T-even future/past equality;
- T-odd sign reversal when a matched boundary exists;
- ordered gluon links preserved;
- f/d channels independent.

## M2-I: collinear nonsinglet/singlet evolution

- conserved nonsinglet moments;
- singlet momentum closure;
- helicity and transversity tests;
- wrong-kernel injections.

## M2-J: heavy-flavor threshold

- physical continuity;
- reverse map;
- threshold history in identity;
- mismatch failures.

## M2-K: resolved nuclear evolution

- impulse commutation;
- independent many-body status;
- matched-total reconstruction;
- no scalar collapse.

## M2-L: hidden-color covariance

- two hidden-basis rotations;
- complete observable invariant;
- basis component changes.

## M2-M: microscopic member covariance

- same-member evaluation across all observables;
- cross-flavor and nucleon/deuteron covariance;
- detection of shuffled member identities.

## M2-N: accuracy and bottleneck reporting

- full tuple;
- generated label;
- correct least-accurate bottleneck;
- accuracy-laundering failures.

## M2-O: multi-Q holdouts

Reserve before final tuning:

- at least one Q value;
- at least one rank;
- one quark channel;
- one gluon channel;
- one deuteron tensor channel;
- one threshold-crossing observable.

## M2-P: isolation and deterministic reproduction

- no route to process, \(W+Y\), inference, or production;
- deterministic manifests;
- byte-identical prior artifacts.

---

# 15. Negative injections

Create at least **640 ordered C21 negative injections** with stable IDs, deterministic diagnostics, and machine-readable expected failures.

The suite must include, at minimum:

### Source and convention failures

- missing source hash;
- wrong paper version;
- wrong equation locator;
- copied secondary-source formula;
- \(\alpha_s/\pi\) versus \(\alpha_s/(4\pi)\);
- sign and factor-of-two errors;
- quark/gluon representation alias;
- invalid Casimir extrapolation;
- incompatible rapidity convention.

### Kernel failures

- one kernel per TMD;
- polarization-dependent kernel introduced without a new operator theorem;
- quark kernel copied to gluon;
- exact NP Casimir scaling imposed;
- physical lattice claim without covariance;
- figure digitization presented as source data;
- single-spacing gluon result labeled continuum;
- hidden data-domain extrapolation;
- overflexible point-per-parameter fit;
- missing holdout.

### Evolution failures

- wrong contour identity;
- ignored curl;
- tuned-away curl;
- broken transitivity;
- incorrect reverse evolution;
- mixed threshold histories;
- future and past evolved differently;
- rank changed by evolution;
- wrong Bessel order;
- wrong reference mass;
- evolution outside validated Q domain.

### Collinear failures

- twist-two kernel on twist-three operator;
- nonsinglet/singlet alias;
- helicity/unpolarized kernel alias;
- transversity mixed with gluon;
- momentum sum-rule failure;
- endpoint/plus-distribution errors;
- threshold without matching.

### Nuclear failures

- scalar evolution of the total only;
- collapse of NN/NNPI/DeltaDelta/6q ancestry;
- hidden-color basis dependence;
- early cluster sum;
- proton/neutron member shuffle;
- coherent pilot treated as physical shadowing;
- partonic and nuclear Wilson mechanisms aliased.

### Uncertainty and identity failures

- independently sampled marginal bands;
- lost matching covariance;
- lost lattice covariance;
- combined uncertainty before separated axes;
- wrong microscopic member;
- wrong nuclear plan;
- wrong scheme;
- wrong Q grid;
- accuracy laundering.

### Readiness leakage

- process record construction;
- hard factor execution;
- fragmentation execution;
- \(Y\)-term execution;
- global likelihood;
- posterior inference;
- production registry mutation;
- authoritative artifact mutation;
- promotion of unavailable T-odd channels.

---

# 16. Deliverables

Create at least:

```text
docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_requirement_coverage.json
docs/next_level/c21_normative_source_integration.json
docs/next_level/c21_anomalous_dimension_library.json
docs/next_level/c21_beta_threshold_library.json
docs/next_level/c21_cs_kernel_source_manifest.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_capability_matrix.json
docs/next_level/c21_multiq_grid.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_nuclear_evolution_manifest.json
docs/next_level/c21_uncertainty_manifest.json
docs/next_level/c21_holdout_report.json
docs/next_level/c21_regression_report.json
docs/next_level/c21_injection_manifest.json
docs/next_level/c21_unresolved_physics_gaps.md
```

Add API and architecture-decision records for:

- anomalous-dimension conventions;
- quark/gluon kernel separation;
- lattice/external-source admissibility;
- finite-order curl treatment;
- threshold history;
- rank-preserving evolution;
- resolved nuclear evolution;
- evolution capability versus matching capability;
- process-readiness isolation.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md   # documentation-only when needed
```

All generated JSON must be deterministic and byte-identical on rebuild.

---

# 17. Acceptance criteria

C21 is complete only when all of the following are satisfied:

1. The complete C20 baseline reproduces before edits.
2. Every anomalous-dimension record is source-audited and independently checked.
3. Quark and gluon cusp, noncusp, and rapidity identities remain separate.
4. Running coupling and threshold histories are typed and reversible at the declared order.
5. A quark CS-kernel plan is implemented with honest source status.
6. A separate gluon CS-kernel plan is implemented or remains explicitly unavailable/exploratory.
7. No polarization-, flavor-, target-, or TMD-specific CS kernel is introduced.
8. Direct, improved, and optional \(\zeta\)-prescription routes are compared where implemented.
9. Exact-oracle path independence closes.
10. Finite-order curl and path ambiguity are reported rather than fitted away.
11. Rank 0-3 transforms and evolution preserve rank and convention identity.
12. All supported matched operators receive a complete capability assessment.
13. Unsupported T-odd and twist-three channels remain fail-closed.
14. Nonsinglet and singlet collinear sum rules close.
15. Heavy-flavor threshold tests close.
16. Future/past and ordered-link identities survive evolution.
17. The resolved nuclear graph survives evolution without scalar collapse.
18. Hidden-color complete observables remain basis covariant.
19. Microscopic member identity and covariance survive every transformation.
20. Accuracy labels reflect the least accurate ingredient.
21. All uncertainty axes remain separately represented.
22. At least six genuine multi-Q holdouts remain outside calibration/tuning.
23. Every new negative injection is detected with the expected diagnostic.
24. All prior C3-C20 tests, requirements, injections, builders, and manifests remain passing.
25. The 216 production routes remain unchanged.
26. All eight authoritative artifacts remain byte-identical.
27. No process, \(W+Y\), inference, or production route is created.
28. All C21 manifests reproduce byte-for-byte.
29. The working tree is clean.
30. A local completion commit is created and not pushed.

---

# 18. Allowed and forbidden status labels

The strongest permissible statuses include:

```text
C21_ANOMALOUS_DIMENSION_LIBRARY_SOURCE_AUDITED
C21_RUNNING_COUPLING_AND_THRESHOLD_LIBRARY_VALIDATED
C21_QUARK_CS_KERNEL_CONSTRAINT_INTERFACE_VALIDATED
C21_GLUON_CS_KERNEL_EXPLORATORY_INTERFACE_VALIDATED
C21_TWO_SCALE_EVOLUTION_VALIDATED_AT_DECLARED_ORDER
C21_FINITE_ORDER_CURL_QUANTIFIED
C21_RANK_0_3_MULTIQ_EVOLUTION_VALIDATED
C21_THRESHOLD_QUALIFIED_EVOLUTION_VALIDATED
C21_RESOLVED_NUCLEAR_EVOLUTION_VALIDATED
C21_SCHEME_QUALIFIED_MICROSCOPIC_TMD_ENSEMBLE_VALIDATION_ONLY
C21_PROCESS_READINESS_INTERFACE_ONLY
```

The following remain forbidden:

```text
PHYSICAL_TMD_EXTRACTION
ALL_ORDER_TMD_EVOLUTION
PHYSICAL_CS_KERNEL_COMPLETE
UNIVERSAL_NONPERTURBATIVE_QUARK_GLUON_CASIMIR_SCALING
PHYSICAL_TODD_MATCHING_COMPLETE
PHYSICAL_SHADOWING_READY
PROCESS_FACTORIZATION_READY
W_PLUS_Y_READY
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 19. Final response

The final Codex response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- anomalous-dimension records and maximum source/oracle residual;
- beta-function and threshold orders;
- quark and gluon CS-kernel plan statuses;
- whether any compatible physical lattice bundle was actually consumed;
- kernel-fit parameter count, calibration count, holdouts, and null directions;
- exact and finite-order curl/path residuals;
- rank 0-3 evolution residuals;
- Q grid and threshold crossings;
- nonsinglet/singlet moment residuals;
- nuclear impulse and hidden-color covariance residuals;
- microscopic member/covariance checks;
- all unavailable operator families;
- all remaining physical gates;
- files created;
- local commit hash;
- confirmation that nothing was pushed.

Do not declare physical TMDs, a physical gluon kernel, all-order evolution, process readiness, or production readiness unless every corresponding formal and source-data condition is genuinely satisfied. Under the current work-package scope, those claims are expected to remain unavailable.
