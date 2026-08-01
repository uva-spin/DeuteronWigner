# C22/M3 Codex Work Package

## Title

**Full source-audited rank-aware small-\(b_{\mathrm{TMD}}\) OPE, endpoint-distribution algebra, and collinear operator mixing across the supported twist-two microscopic TMD basis**

## Authoritative baseline

Start from the local C21/M2 completion commit:

```text
afe789a68b7394d1cb0165aa3b428b6e2d79f5bb
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C21 scientific baseline reproduces before any implementation changes.

Do not use `origin/main` as the scientific baseline when the local branch is ahead of the remote.

## Primary objective

C21 validates source-qualified anomalous dimensions, threshold transport, separate quark/gluon Collins–Soper interfaces, rank-preserving multi-\(Q\) evolution, and resolved nuclear evolution. Its capability matrix contains:

```text
540 stable C20 operator identities
492 reference-scale matching-executable identities
48 reference-scale matching-unavailable identities
438 fully evolvable identities at M2 scope
102 identities with incomplete evolution capability
```

C22 must determine, from the actual operator and perturbative literature rather than from TMD names, which of those identities admit a complete declared-order twist-two small-\(b_{\mathrm{TMD}}\) OPE and collinear evolution route.

The required chain is:

```text
C20 source-audited reference-scale matching
    -> C21 source-qualified two-scale evolution
    -> exact endpoint-distribution algebra
    -> source-audited twist-two matching coefficients
    -> source-audited collinear splitting/mixing blocks
    -> RG-consistent rank-aware small-b OPE
    -> updated 540-entry capability matrix
    -> threshold-qualified multi-Q microscopic TMD ensembles
```

C22 must increase capability only where the correct operator basis, matching coefficient, collinear evolution, threshold map, and rank transform are all demonstrated.

C22 must not make unsupported twist-three, T-odd, higher-twist, or spin-1 exotic channels executable merely to reduce the incomplete count.

## Scientific boundary

C22 is:

```text
validation-only
scheme-qualified at declared perturbative order
operator-level
rank-aware
source-audited
threshold-qualified
resolved in nuclear ancestry
```

C22 is not:

```text
a physical TMD extraction
an all-order OPE
a physical twist-three matching package
a process-factorization package
a W+Y package
a fragmentation-function fit
a global inference package
a production promotion
```

---

# 1. Completeness and autonomous execution

Completeness is the objective. Do not optimize for quickness.

Read all relevant code, APIs, reports, manifests, source files, tests, and roadmap entries before changing the repository. Continue autonomously until every C22 acceptance criterion is satisfied.

Do not stop for approval to:

- inspect repository content;
- run test, builder, evidence, atlas, and manifest commands;
- install routine local symbolic/numerical dependencies when permitted;
- download open primary papers and their ancillary files;
- preserve primary sources locally;
- build parsers for source ancillary data;
- generate independent symbolic or numerical oracles;
- rebuild deterministic JSON manifests.

If one optional primary source or ancillary file cannot be obtained reproducibly, record that limitation and leave the corresponding operator block unavailable. Complete the remainder of the package.

Do not push the final commit.

---

# 2. Normative repository sources

Read completely and hash-audit the actual repository versions of at least:

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c20_implementation_report.md
docs/next_level/c20_api.md
docs/next_level/c20_coefficient_library.json
docs/next_level/c20_matching_fit_manifest.json
docs/next_level/c20_requirement_coverage.json

docs/next_level/c21_implementation_report.md
docs/next_level/c21_api.md
docs/next_level/c21_anomalous_dimension_library.json
docs/next_level/c21_beta_threshold_library.json
docs/next_level/c21_cs_kernel_fit_manifest.json
docs/next_level/c21_evolution_capability_matrix.json
docs/next_level/c21_multiq_grid.json
docs/next_level/c21_evolution_accuracy_manifest.json
docs/next_level/c21_nuclear_evolution_manifest.json
docs/next_level/c21_uncertainty_manifest.json
docs/next_level/c21_holdout_report.json
docs/next_level/c21_regression_report.json

references/volume_v_matching_evolution_factorization.tex
references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex
references/volume_xvii_process_qualified_tmd_observables.tex
references/formalism_volume_index.md
handoff/ROADMAP.md
```

Use the actual filenames present when they differ slightly.

Record exact hashes and source roles in:

```text
docs/next_level/c22_normative_source_integration.json
```

If Volume XVI or XVII is absent, record that absence. Do not invent missing content. This prompt, Volume V, and the implemented C19-C21 interfaces remain sufficient to execute C22.

---

# 3. Primary-source audit

Use primary papers and their own ancillary files as formula authorities. Reviews, talks, search snippets, secondary code, and phenomenology packages may be comparison sources but cannot establish coefficients.

Preserve all sources and ancillaries used under:

```text
data/raw/c22_sources/
```

with exact SHA-256 hashes.

The initial audit must include, where relevant:

```text
arXiv:1702.06558
    Twist-2 matching of transverse momentum dependent distributions

arXiv:1805.07243
    Transverse momentum dependent transversely polarized distributions at NNLO

arXiv:1908.03831
    Transverse Parton Distribution and Fragmentation Functions at NNLO: the Quark Case

arXiv:1909.13820
    Transverse Parton Distribution and Fragmentation Functions at NNLO: the Gluon Case

arXiv:2006.05329
    Transverse momentum dependent PDFs at N3LO

arXiv:2509.01655
    The N3LO Twist-2 Matching of Helicity TMDs and SIDIS q_* Spectrum

arXiv:2509.01703
    The N3LO Twist-2 Matching of Linearly Polarized Gluon TMDs

arXiv:2509.17568
    The N3LO Twist-2 Matching of TMD Quark Transversity

arXiv:2603.04039
    NNLO DGLAP splitting functions from collinear matching of TMDs

arXiv:hep-ph/0403192
    The Three-Loop Splitting Functions in QCD: The Non-Singlet Case

arXiv:hep-ph/0404111
    The Three-Loop Splitting Functions in QCD: The Singlet Case

arXiv:1409.5131
    The Three-Loop Splitting Functions in QCD: The Helicity-Dependent Case

arXiv:1506.04517
    On gamma5 in higher-order QCD calculations and the NNLO evolution of the polarized valence distribution

arXiv:1908.03779
    The Polarized Three-Loop Anomalous Dimensions from On-Shell Massive Operator Matrix Elements

arXiv:2201.04875
    Gluon transversity and TMDs for spin-1 hadrons
```

Add any further primary paper needed for:

- source-scheme conversion;
- plus distributions and ancillary conventions;
- the unpolarized/helicity/transversity splitting functions;
- linearly polarized gluon coefficients;
- spin-1 double-helicity-flip gluon evolution;
- heavy-flavor operator matching;
- local-current and EMT moments.

## Source-disagreement rule

Recent sources do not automatically supersede earlier sources.

When two primary calculations disagree:

1. preserve both source records;
2. identify convention, scheme, gamma5, color, or distributional differences;
3. reproduce all shared lower-order limits;
4. use independent sum rules and RG constraints;
5. select an executable record only when the discrepancy is resolved;
6. otherwise leave the block `SOURCE_DISAGREEMENT_UNRESOLVED`.

Do not choose a result solely because it is newer or yields more executable entries.

---

# 4. Immutable C21 baseline

Before edits, reproduce and record:

```text
1,053 tests
all C21 builders and validators
36/36 evidence rows
162/162 atlas pages
900 C21 requirements
640 C21 negative injections

7 anomalous-dimension/beta records
4-loop beta record
3-loop threshold maps
exact evolution path residual approximately 1.7e-13
finite-order curl 0.0029
finite-order contour difference 0.0016
transitivity residual approximately 2.4e-12

Q grid:
1.6, 2, 3, 4, 5, 10, 20, 100

threshold:
4.18

rank 0-3 transform residuals:
2e-8 through 8e-8

540 LF identities
540 QCD identities
492 C20 matching-executable
48 C20 matching-unavailable
438 fully evolvable at M2 scope
102 incomplete at M2 scope

216 production routes
all eight authoritative production artifacts byte-identical
all pinned C15-C21 manifests byte-identical
deterministic C21 manifest reconstruction
```

Do not proceed when this baseline cannot be reproduced. Diagnose without changing accepted or prior microscopic physics.

C22 must not modify:

- C19/C20 operator identities;
- C20 coefficient source records except through versioned superseding records;
- C20 matching calibration/holdout roles;
- C21 anomalous dimensions, kernel plans, Q grid, threshold, or evolution paths;
- C21 capability statuses except by adding the new M3 capability layer;
- the 48 matching-unavailable identities;
- production registry, provenance, or composition;
- authoritative production artifacts;
- prior C3-C21 benchmark outputs.

---

# 5. Required architecture

Extend the existing C19-C21 type system. Do not create a parallel OPE or evolution framework.

Implement or extend objects equivalent to:

```text
EndpointDistribution
PlusDistribution
DeltaEndpointTerm
RegularDistributionTerm
HarmonicPolylogRecord
DistributionConvention

CoefficientSourceRecord
TwistTwoCoefficientRecord
CoefficientBlock
CoefficientOrderManifest
CoefficientCapability

CollinearOperatorId
CollinearOperatorBasis
SplittingFunctionRecord
SplittingMatrix
Gamma5SchemeRecord
FiniteAxialRenormalization
CollinearEvolutionCapability

SmallBOPEMap
SmallBOPEBlock
SmallBOPECapabilityMatrix
OPEAccuracyManifest
OPERGConsistencyReport

MellinMomentOracle
XSpaceConvolutionEngine
MellinSpaceEvolutionOracle
EndpointLimitReport
ThresholdOPEMap

ResolvedNuclearOPEManifest
M3MultiQCapabilityMatrix
M3ClosureReport
```

Every object must be:

- immutable after construction;
- content addressed;
- serializable with deterministic round trip;
- source hashed;
- explicit about scheme and convention;
- fail-closed on missing identity;
- isolated from process and production roots.

---

# 6. Distribution algebra

## 6.1 Exact distribution types

Implement typed support for:

```text
delta(1-x)
regular functions on 0 < x < 1
[f(x)/(1-x)]_+
[ln^k(1-x)/(1-x)]_+
small-x logarithms
harmonic polylogarithms
rational and zeta-valued coefficients
matrix-valued distributions
```

A coefficient must not be represented only by samples on an x grid when its source is distributional.

## 6.2 Plus-distribution convention

Store explicitly:

- integration domain;
- test-function convention;
- endpoint subtraction;
- variable name;
- convolution convention;
- normalization of \(\delta(1-x)\).

Required identity:

\[
\int_0^1 dx\,[f(x)]_+\,\phi(x)
=
\int_0^1 dx\,f(x)\,[\phi(x)-\phi(1)].
\]

Generalize correctly to a lower convolution limit \(x_B\).

## 6.3 Independent routes

Every distributional coefficient must support:

1. symbolic or exact source representation where possible;
2. x-space convolution with smooth analytic test functions;
3. Mellin moments;
4. numerical grid evaluation away from endpoints;
5. endpoint-limit reports.

At least two of these routes must be independent implementations.

Do not evaluate plus distributions by inserting a small numerical cutoff and calling the cutoff physical.

## 6.4 Harmonic-polylogarithm handling

When source ancillaries contain harmonic polylogarithms:

- preserve the original basis;
- record weight and branch conventions;
- provide a numerical evaluator;
- compare with source sample points;
- test \(x\to0\) and \(x\to1\) expansions;
- record unsupported complex-continuation domains.

A black-box third-party evaluator may be used as one oracle, but the repository must retain source identity and an independent lower-weight or moment check.

---

# 7. Operator-level twist-two classification

Construct a complete classification for all 540 C20 operator identities.

For each identity determine:

```text
partonic species
flavor/singlet class
target channel
parton polarization
transverse rank
Wilson/link/color class
naive-T parity
local collinear operator
twist
coefficient family
first nonzero order
implemented order
collinear mixing block
threshold block
reason for unavailability
```

The classification is by operator, not by TMD name.

## 7.1 Supported twist-two families

Audit and implement, at their actually established orders and schemes:

```text
UNPOLARIZED_QUARK_NONSINGLET
UNPOLARIZED_QUARK_GLUON_SINGLET
HELICITY_QUARK_NONSINGLET
HELICITY_QUARK_GLUON_SINGLET
QUARK_TRANSVERSITY_NONSINGLET
LINEARLY_POLARIZED_GLUON_TO_UNPOLARIZED_COLLINEAR_BASIS
SPIN1_LL_UNPOLARIZED_TYPE_QUARK_GLUON_MATRIX_ELEMENTS
LOCAL_VECTOR_CURRENT_LIMIT
LOCAL_AXIAL_CURRENT_LIMIT
LOCAL_TENSOR_CURRENT_LIMIT where available
LOCAL_EMT_LIMIT
```

## 7.2 Target-state universality

Short-distance coefficients may be target independent when the local operator is the same.

For example, a spin-1 `LL` matrix element may use the same coefficient block as the corresponding unpolarized operator only after proving:

```text
same bilocal operator
same local twist-two operator
same species and color representation
same rank
same link and scheme
different target matrix element only
```

Do not copy an unpolarized coefficient into every tensor channel by name.

## 7.3 Pretzelosity

Preserve the source-audited result that the twist-two pretzelosity coefficient is zero through the demonstrated order.

Distinguish:

```text
ZERO_COEFFICIENT_AT_DECLARED_TWIST_AND_ORDER
```

from:

```text
PHYSICAL_TMD_ZERO
```

and from:

```text
HIGHER_TWIST_OPERATOR_REQUIRED
```

Pretzelosity must not be made twist-two executable by borrowing the transversity coefficient.

## 7.4 Rank-one and T-odd channels

The following remain fail-closed unless their correct multiparton operator basis and source-audited coefficients are independently implemented:

```text
Sivers / Qiu-Sterman
Boer-Mulders chiral-odd twist three
genuine g1T / worm-gear multiparton terms
genuine h1L-perp multiparton terms
tri-gluon f type
tri-gluon d type
tensor-polarized T-odd channels
```

A Wandzura-Wilczek approximation may be represented only as:

```text
APPROXIMATION_PLAN
```

with its own remainder and may not be registered as the exact small-b OPE.

## 7.5 Gluon double-helicity flip

Audit the spin-1 gluon double-helicity-flip collinear operator and its evolution separately.

Activate it only when:

- the operator identity is complete;
- the source-audited splitting kernel is available;
- the TMD-to-collinear coefficient is known in the project scheme;
- all color, rank, and target conventions are reconciled.

Otherwise retain a precise unavailable status.

---

# 8. Coefficient-library implementation

## 8.1 Source record

Every coefficient record must contain:

```text
source operator
target collinear operator
species/flavor block
target channel universality status
rank
twist
Wilson link and color class
UV/rapidity/soft scheme
gamma5 scheme when relevant
first nonzero order
implemented order
distributional expression
source citation
source equation/table/ancillary locator
source hash
ancillary hash
transcription hash
independent oracle
endpoint status
small-x status
known remainder
```

## 8.2 Order selection

Do not force every family to the same order.

The executable order for each block is the highest order for which:

- the coefficient is source audited;
- the project-scheme conversion is implemented;
- the collinear splitting kernel is available;
- the C21 anomalous dimensions are compatible;
- endpoint and Mellin checks pass;
- thresholds are supported.

The global accuracy remains limited by the least accurate required ingredient.

## 8.3 Ancillary ingestion

Prefer machine-readable ancillary files when published.

For every ancillary parser:

- preserve the original file;
- record its hash;
- parse deterministically;
- round-trip or reproduce source checksums when possible;
- compare with source equations at lower orders;
- reject silent missing terms or unsupported function syntax.

Do not hand-transcribe long N3LO expressions when an authoritative ancillary exists.

## 8.4 Color decomposition

Retain exact color structures, including:

```text
C_F
C_A
T_F n_f
d_F^{abcd} d_A^{abcd}
d_F^{abcd} d_F^{abcd}
d_A^{abcd} d_A^{abcd}
other source-declared quartic invariants
```

Do not collapse higher-order color structures into an effective Casimir factor.

---

# 9. Gamma5 and polarized-scheme handling

Helicity coefficients and splitting functions require an explicit dimensional-regularization and finite-renormalization convention.

Implement a `Gamma5SchemeRecord` containing:

```text
bare gamma5 prescription
projector definition
finite axial renormalization
singlet/nonsinglet distinction
anomaly treatment
source records
scheme-conversion matrix
moment constraints
```

Required checks include:

- nonsinglet axial-current normalization;
- first moments;
- source-to-project finite conversion;
- agreement of independent polarized splitting calculations after conversion;
- failure when an unpolarized coefficient is used without the helicity conversion;
- failure when singlet and nonsinglet finite renormalizations are aliased.

Do not hide gamma5 conversion inside a numerical coefficient array.

---

# 10. Collinear operator bases and splitting matrices

## 10.1 Unpolarized sector

Implement source-audited:

```text
nonsinglet evolution
2x2 singlet quark/gluon evolution
```

at the declared order supported by the primary sources and C21 threshold system.

Required sum rules:

\[
\int_0^1 dx\,P_{\mathrm{NS}}(x)=0
\]

for the relevant conserved nonsinglet number, and the singlet momentum constraints.

## 10.2 Helicity sector

Implement:

```text
helicity nonsinglet
helicity singlet quark/gluon mixing
```

with the explicit gamma5 scheme record and finite conversion.

Preserve axial-anomaly and first-moment status.

## 10.3 Transversity sector

Implement nonsinglet transversity evolution.

There is no leading-twist gluon transversity mixing for a spin-\(\tfrac12\) nucleon transversity operator.

Any spin-1 gluon double-flip operator is a distinct operator block and may not be inserted into the quark-transversity matrix.

## 10.4 Spin-1 LL sector

Where `LL` uses the same local unpolarized twist-two operator class, use the same singlet/nonsinglet splitting matrix on the tensor-polarized matrix element.

Prove this at the operator level and retain target-channel identity.

## 10.5 Numerical solvers

Provide:

1. an x-space convolution/evolution solver;
2. a Mellin-space or moment-space oracle;
3. deterministic interpolation;
4. threshold-aware evolution;
5. forward and reverse tests where numerically stable.

The two routes must agree for analytic benchmark inputs.

A solver that shares the same discretized matrix in both routes is not independent.

---

# 11. OPE renormalization-group consistency

For the project convention, derive and implement the coefficient RG equation rather than copying a convention-mismatched formula.

Schematically, the coefficient matrix obeys a relation of the form:

\[
\frac{d}{d\ln\mu}
\bm C
=
\bm\gamma_{\mathrm{TMD}}\bm C
-
\bm C\otimes_x\bm P,
\]

with the appropriate cusp, noncusp, rapidity, and logarithmic terms in the declared convention.

## Required checks

- reconstruct all logarithmic terms from anomalous dimensions and splitting functions;
- compare source finite terms;
- check rapidity-scale dependence;
- check threshold consistency;
- check singlet matrix ordering;
- check gamma5 conversion;
- check Mellin moments;
- verify that matching then evolving agrees with evolving then rematching through the declared order.

Define two routes:

```text
ROUTE_A:
match at Q0 -> TMD evolve to Q

ROUTE_B:
collinear evolve to Q -> rematch at Q
```

In the perturbative small-b window:

\[
F_A(Q)-F_B(Q)
\]

must scale with the first omitted order plus declared numerical and power corrections.

Do not tune coefficients to force exact equality beyond their perturbative order.

---

# 12. Rank-aware small-b maps

For every supported rank \(m=0,1,2,3\), retain:

```text
Bessel order J_|m|
Fourier phase i^m
extracted kT/M powers
extracted bM powers
reference mass
tensor basis
derivative-moment convention
```

## Required behavior

- rank is not changed by matching;
- linearly polarized gluon matching remains rank two;
- rank-zero LL matching remains rank zero;
- transversity retains its declared tensor convention;
- coefficients whose leading small-b term vanishes remain explicitly zero at that order;
- no scalar \(J_0\) path is reused for a ranked object.

Perform:

1. k-space to b-space transform;
2. small-b matching;
3. collinear evolution;
4. C21 TMD evolution;
5. inverse transform;
6. multi-Q closure.

Report transform, OPE, collinear, TMD-evolution, and inverse-transform errors separately.

---

# 13. Heavy-flavor thresholds

Integrate with the immutable C21 threshold history and fixed Q grid:

```text
Q = 1.6, 2, 3, 4, 5, 10, 20, 100
threshold = 4.18
```

The threshold map must act consistently on:

- collinear operator basis;
- splitting matrices;
- matching coefficients;
- alpha_s;
- TMD anomalous dimensions;
- C21 evolution history;
- accuracy manifest.

Required checks:

- route A/route B consistency across threshold;
- nonsinglet conservation;
- singlet momentum continuity;
- forward/reverse threshold;
- rank preservation;
- quark/gluon threshold-history agreement.

Do not alter the C21 Q grid after examining holdouts.

---

# 14. Updated capability matrix

Construct `M3MultiQCapabilityMatrix` for all 540 identities.

For every identity report independently:

```text
C20 reference matching
C21 TMD evolution
twist classification
small-b coefficient
coefficient order
collinear operator
collinear mixing block
collinear evolution order
gamma5 conversion
threshold support
rank transform
route A/B consistency
fully qualified M3 multi-Q status
reason for incompleteness
```

Preserve:

```text
492 C20 matching-executable
48 C20 matching-unavailable
```

Report the new exact count of:

```text
M3 fully qualified
M3 coefficient-only
M3 collinear-only
M3 TMD-evolution-only
M3 higher-twist required
M3 source disagreement
M3 missing operator
M3 unavailable
```

Do not set a target count in advance.

The scientific objective is accurate classification and justified capability, not maximizing the executable count.

---

# 15. Resolved nuclear small-b OPE

Retain the C18 nuclear graph:

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

## 15.1 Target-independent coefficients

For the same local operator, perturbative coefficients act on each target/nuclear matrix element without erasing ancestry.

Test target-channel universality only where the operator identity proves it.

## 15.2 Impulse commutation

Where the impulse kernel is scale independent, test:

\[
C\otimes_x(P\otimes_x f)
=
P\otimes_x(C\otimes_x f)
\]

and the corresponding evolution associativity.

Test across:

- proton-active and neutron-active terms;
- U and LL;
- quarks, antiquarks, and gluons;
- rank zero and one supported nonzero rank;
- several Q values and microscopic members.

## 15.3 Independent many-body blocks

Pion-active, transition, coherent, DeltaDelta, compact, and two-body operators receive their own coefficient/evolution block or an explicit unavailable status.

Do not apply the nucleon impulse coefficient to a distinct many-body operator by array shape.

## 15.4 Hidden-color covariance

Apply at least two unitary rotations of the four-dimensional hidden-color complement.

Complete six-quark and matched OPE/evolved observables must remain invariant.

Individual hidden-color basis components may change.

---

# 16. Uncertainty and accuracy

## 16.1 Separate uncertainty axes

Preserve and extend:

```text
microscopic/Hamiltonian
basis/Fock/regulator
Wilson order
C20 matching covariance
C21 CS-kernel uncertainty
anomalous-dimension truncation
finite-order curl/path ambiguity
coefficient perturbative truncation
endpoint/numerical distribution evaluation
collinear splitting truncation
gamma5 scheme conversion
threshold matching
small-b power correction
large-b model boundary
nuclear many-body operator availability
hidden-color/cluster matching
rank transform/quadrature
missing operator
source disagreement
```

Do not combine these before storing them separately.

## 16.2 Accuracy manifest

Every fully qualified identity receives:

```text
matching order
small-b coefficient order
collinear splitting order
TMD cusp/noncusp/rapidity orders
CS-kernel status
threshold order
rank-transform status
Wilson order
nuclear operator order
b-domain
Q-domain
first omitted order
bottleneck
```

The generated accuracy label is limited by the least accurate required ingredient.

A high N3LO coefficient does not upgrade an NNLO collinear kernel or an exploratory CS kernel.

---

# 17. Holdouts

Freeze holdouts before final tuning.

At minimum reserve:

- one unpolarized coefficient moment;
- one helicity coefficient moment;
- one transversity coefficient moment;
- one linearly polarized gluon point or moment;
- one singlet mixing observable;
- one LL tensor matrix element;
- one route-A/route-B multi-Q point;
- one threshold-crossing point;
- one nuclear tensor channel;
- one hidden-color-rotated complete observable;
- one endpoint asymptotic coefficient;
- one source-disagreement diagnostic if applicable.

Do not move a failed holdout into calibration without creating a new model version and new independent holdouts.

---

# 18. Required benchmarks

Implement stable benchmark families at least as follows.

## M3-A: endpoint distribution algebra

- plus-distribution identities;
- delta endpoints;
- lower convolution limits;
- analytic test functions;
- cutoff-independence;
- wrong-subtraction injections.

## M3-B: harmonic-polylogarithm source parsing

- ancillary hash;
- deterministic parser;
- source sample points;
- small-x and large-x expansions;
- unsupported branch failure.

## M3-C: unpolarized N3LO coefficient block

- quark/gluon channels;
- source color decomposition;
- Mellin moments;
- RG log reconstruction;
- source-disagreement handling.

## M3-D: helicity N3LO block

- gamma5 scheme;
- nonsinglet/singlet;
- finite axial conversion;
- first moments;
- independent splitting-function comparison.

## M3-E: transversity block

- N3LO coefficient where source audited;
- NNLO collinear kernel;
- no gluon mixing;
- tensor-current limit;
- wrong-singlet injection.

## M3-F: linearly polarized gluon block

- rank-two identity;
- first nonzero order;
- quark/gluon collinear parents;
- N3LO source if fully audited;
- no rank-zero alias.

## M3-G: pretzelosity classification

- zero twist-two coefficient through the demonstrated order;
- no physical-zero claim;
- higher-twist-required status;
- transversity-copy failure.

## M3-H: spin-1 LL universality

- same local operator proof;
- separate target matrix elements;
- singlet q/g mixing;
- wrong tensor-channel copying failure.

## M3-I: unpolarized collinear evolution

- nonsinglet number;
- singlet momentum;
- x-space/Mellin agreement;
- threshold continuity.

## M3-J: helicity collinear evolution

- gamma5 conversion;
- nonsinglet moment;
- singlet mixing;
- source cross-check.

## M3-K: route A versus route B

- several b and Q points;
- threshold crossing;
- first-omitted-order scaling;
- no overfitting.

## M3-L: rank 0-3 OPE transport

- correct Bessel orders;
- rank preservation;
- transform/OPE/evolution/inverse residual separation.

## M3-M: resolved nuclear OPE

- impulse commutation;
- independent many-body status;
- matched-total reconstruction;
- no scalar collapse.

## M3-N: hidden-color covariance

- two basis rotations;
- component variation;
- complete-observable invariance.

## M3-O: capability and accuracy

- all 540 entries classified;
- bottleneck accuracy;
- unavailable reasons;
- accuracy-laundering failures.

## M3-P: deterministic isolation

- prior manifests byte-identical;
- no process, W+Y, inference, or production route;
- deterministic rebuild.

---

# 19. Negative injections

Create at least **720 ordered C22 negative injections** with stable IDs and deterministic expected diagnostics.

The suite must include:

## Source/provenance

- missing source hash;
- wrong paper version;
- secondary source used as authority;
- wrong equation locator;
- missing ancillary term;
- parser silently dropping a color structure;
- unresolved source disagreement ignored;
- source order overstated.

## Distribution algebra

- wrong plus prescription;
- missing delta endpoint;
- duplicate delta endpoint;
- endpoint cutoff treated as physical;
- wrong lower convolution limit;
- HPL branch error;
- small-x log omitted;
- matrix order reversed in singlet convolution.

## Operator classification

- TMD-name matching without operator identity;
- U coefficient copied to incompatible tensor operator;
- LL universality asserted without same-operator proof;
- rank-one channel labeled twist two without source;
- Sivers given unpolarized coefficient;
- Boer-Mulders given transversity coefficient;
- worm gear given helicity coefficient;
- tri-gluon f/d merged;
- gluon double-flip aliased to linearly polarized gluon.

## Gamma5/polarized

- no finite axial conversion;
- singlet/nonsinglet alias;
- wrong gamma5 scheme;
- unpolarized splitting function used for helicity;
- axial first moment violated;
- anomaly status lost.

## Collinear evolution

- nonsinglet/singlet alias;
- wrong matrix ordering;
- transversity/gluon mixing;
- wrong endpoint term;
- sum-rule failure;
- threshold without operator matching;
- x-space and Mellin-space implementations sharing the same faulty matrix.

## Rank/OPE

- J0 used for rank 1-3;
- Fourier phase lost;
- reference mass changed;
- linearly polarized gluon demoted to rank zero;
- pretzelosity promoted from zero coefficient to transversity;
- OPE outside b-domain;
- route A/B compared at mismatched schemes.

## Nuclear

- coefficient applied to final matched total only;
- ancestry collapsed;
- pion operator given nucleon coefficient;
- hidden-color basis dependence;
- cluster and compact double counting;
- proton/neutron member shuffle;
- coherent pilot promoted to physical shadowing.

## Accuracy/uncertainty

- N3LO label with NNLO bottleneck hidden;
- coefficient covariance dropped;
- source disagreement combined as statistical error;
- power correction absorbed into numerical error;
- independently sampled marginal members;
- holdout reused for calibration.

## Readiness leakage

- process record execution;
- fragmentation-function execution;
- hard-factor execution;
- W-term cross section;
- Y-term construction;
- global likelihood;
- posterior inference;
- production registry mutation;
- authoritative artifact mutation;
- physical T-odd matching claim;
- all-order claim.

---

# 20. Deliverables

Create at least:

```text
docs/next_level/c22_implementation_report.md
docs/next_level/c22_api.md
docs/next_level/c22_requirement_coverage.json
docs/next_level/c22_normative_source_integration.json
docs/next_level/c22_primary_source_manifest.json
docs/next_level/c22_distribution_algebra_manifest.json
docs/next_level/c22_coefficient_library.json
docs/next_level/c22_coefficient_source_audit.json
docs/next_level/c22_gamma5_scheme_manifest.json
docs/next_level/c22_splitting_function_library.json
docs/next_level/c22_collinear_evolution_manifest.json
docs/next_level/c22_ope_rg_consistency_report.json
docs/next_level/c22_smallb_capability_matrix.json
docs/next_level/c22_m3_multiq_capability_matrix.json
docs/next_level/c22_nuclear_ope_manifest.json
docs/next_level/c22_accuracy_manifest.json
docs/next_level/c22_uncertainty_manifest.json
docs/next_level/c22_holdout_report.json
docs/next_level/c22_injection_manifest.json
docs/next_level/c22_regression_report.json
docs/next_level/c22_unresolved_physics_gaps.md
```

Add ADRs for:

- endpoint-distribution convention;
- coefficient source selection;
- source-disagreement handling;
- gamma5 scheme;
- LL target-state universality;
- pretzelosity twist classification;
- rank-aware OPE;
- route A/B consistency;
- nuclear operator-specific OPE;
- capability versus matching/evolution availability.

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md  # documentation only when appropriate
```

All generated JSON must reproduce byte-for-byte.

---

# 21. Acceptance criteria

C22 is complete only when all of the following hold:

1. The complete C21 baseline reproduces before edits.
2. All primary coefficient and splitting sources are locally preserved and hash audited.
3. Distributional coefficients have exact typed endpoint representations.
4. Plus distributions, delta terms, and lower-limit convolutions pass independent analytic tests.
5. Ancillary parsers are deterministic and source checked.
6. Every executable coefficient has complete operator, scheme, rank, order, and source identity.
7. Unpolarized singlet/nonsinglet coefficient and evolution blocks pass.
8. Helicity blocks pass with explicit gamma5 conversion.
9. Transversity passes with no false gluon mixing.
10. Linearly polarized gluon matching remains rank two and passes its source checks.
11. Pretzelosity is classified honestly at the demonstrated twist/order.
12. Spin-1 LL universality is proven only for same-operator blocks.
13. Unsupported twist-three and T-odd channels remain fail-closed.
14. OPE logarithms satisfy the project RG equation at the declared order.
15. Route A and route B agree through the first omitted order in the small-b domain.
16. Nonsinglet number, singlet momentum, and supported helicity/tensor moments close.
17. Threshold matching closes for coefficients and splitting blocks.
18. Rank 0-3 identities and transforms remain intact.
19. All 540 identities receive an M3 capability classification.
20. The 492/48 C20 reference-matching counts remain unchanged.
21. The 438/102 C21 M2 counts remain recorded as immutable baseline values.
22. The new M3 capability counts are reported without a preselected target.
23. Resolved nuclear ancestry survives OPE and collinear evolution.
24. Hidden-color complete observables remain basis covariant.
25. Matching, coefficient, splitting, TMD evolution, and numerical uncertainties remain separate.
26. Accuracy labels report the true bottleneck.
27. All frozen holdouts remain outside calibration.
28. Every C22 negative injection is detected with the expected diagnostic.
29. All prior C3-C21 tests, builders, requirements, injections, and manifests remain passing.
30. The production registry remains exactly 216 routes.
31. All eight authoritative artifacts remain byte-identical.
32. No process, W+Y, inference, or production route is created.
33. All C22 manifests reproduce byte-for-byte.
34. The working tree is clean.
35. A local completion commit is created and not pushed.

---

# 22. Allowed and forbidden statuses

The strongest permitted statuses include:

```text
C22_ENDPOINT_DISTRIBUTION_ALGEBRA_VALIDATED
C22_PRIMARY_TWIST2_COEFFICIENT_LIBRARY_SOURCE_AUDITED
C22_UNPOLARIZED_SMALLB_OPE_VALIDATED_AT_DECLARED_ORDER
C22_HELICITY_SMALLB_OPE_VALIDATED_AT_DECLARED_ORDER
C22_TRANSVERSITY_SMALLB_OPE_VALIDATED_AT_DECLARED_ORDER
C22_LINEAR_GLUON_SMALLB_OPE_VALIDATED_AT_DECLARED_ORDER
C22_SPIN1_LL_OPERATOR_UNIVERSALITY_VALIDATED
C22_PRETZELOSITY_TWIST2_ZERO_STATUS_SOURCE_AUDITED
C22_COLLINEAR_NONSINGLET_SINGLET_MIXING_VALIDATED
C22_GAMMA5_SCHEME_CONVERSION_VALIDATED
C22_ROUTE_A_ROUTE_B_RG_CONSISTENCY_VALIDATED
C22_RANK_AWARE_M3_MULTIQ_CAPABILITY_VALIDATED
C22_RESOLVED_NUCLEAR_SMALLB_OPE_VALIDATED
C22_SCHEME_QUALIFIED_TWIST2_TMD_ENSEMBLE_VALIDATION_ONLY
```

The following remain forbidden:

```text
PHYSICAL_TMD_EXTRACTION
ALL_TMD_SMALLB_COEFFICIENTS_KNOWN
PHYSICAL_TODD_MATCHING_COMPLETE
TWIST3_EVOLUTION_COMPLETE
PHYSICAL_PRETZELOSITY_ZERO
ALL_ORDER_OPE
ALL_ORDER_EVOLUTION
PROCESS_FACTORIZATION_READY
W_PLUS_Y_READY
GLOBAL_INFERENCE_READY
PRODUCTION_READY
```

---

# 23. Final Codex response

The final response must report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- source papers and ancillary files preserved;
- coefficient families and declared orders;
- distribution-algebra maximum residual;
- gamma5 scheme and conversion residuals;
- x-space/Mellin-space evolution residuals;
- nonsinglet, singlet, helicity, transversity, and LL sum-rule residuals;
- route-A/route-B residuals by family;
- threshold residuals;
- rank 0-3 OPE/transform residuals;
- immutable baseline counts 492/48 and 438/102;
- new M3 capability counts by status;
- all still-unavailable operator families and reasons;
- nuclear impulse and hidden-color covariance residuals;
- holdout residuals;
- accuracy bottlenecks;
- deterministic manifest status;
- files created;
- local completion commit;
- confirmation that nothing was pushed.

Do not claim process readiness, W+Y readiness, physical T-odd matching, all-order OPE/evolution, inference readiness, or production readiness under this package.
