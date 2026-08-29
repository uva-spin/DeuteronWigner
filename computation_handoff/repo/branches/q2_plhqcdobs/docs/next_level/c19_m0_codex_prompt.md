# C19/M0 Codex Work Package

## Title

**C19/M0 — Common-scheme light-front-to-QCD operator matching, small-\(b_{\mathrm{TMD}}\) OPE, and rank-aware two-scale evolution validation**

## Authoritative starting point

The scientific baseline is the completed C18/N3 commit:

```text
f11beac61a797f4c0aa3c420243484ad40b813dd
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the entire C18 baseline reproduces before any implementation change.

Do **not** use `origin/main` as the scientific baseline. The authoritative work is local. Do not reset, rebase away, squash away, or replace the C18 ancestry.

## Primary objective

Construct the first common, typed, fail-closed matching and evolution layer that maps the complete regulated microscopic nucleon/deuteron operator parent into a **declared validation QCD/TMD scheme**.

The central chain is

\[
\left\{
W^{\mathrm{LF,reg}}_{q,\bar q,g/N},
W^{\mathrm{LF,reg}}_{q,\bar q,g/D},
J^\mu_{\mathrm{LF}},
T^{\mu\nu}_{\mathrm{LF}}
\right\}
\]

\[
\xrightarrow{\quad \mathcal Z_{\mathrm{LF}\to\mathrm{QCD}}\quad}
\]

\[
\left\{
W^{\mathrm{QCD,ren}}_{q,\bar q,g/N},
W^{\mathrm{QCD,ren}}_{q,\bar q,g/D},
J^\mu_{\mathrm{QCD}},
T^{\mu\nu}_{\mathrm{QCD}}
\right\}_{\mu,\zeta,\mathfrak s}
\]

followed by

\[
\text{small-}b_{\mathrm{TMD}}\text{ OPE}
\quad\text{and}\quad
(\mu,\zeta)\text{ evolution}.
\]

The package must prove that one operator-basis matching system carries every supported:

- quark flavor;
- positive-\(x\) antiquark;
- gluon channel;
- proton and neutron member;
- deuteron target channel \(U,L,T,LL,LT,TT\);
- transverse rank;
- Wilson-link orientation;
- ordered gluon-link pair;
- \(f\)- or \(d\)-type gluon color class;
- \(NN\), \(NN\pi\), \(\Delta\Delta\), and compact six-quark contribution;
- microscopic member and assumption plan.

The matching is **not** one fitted normalization for every named TMD.

## Scientific boundary

C19/M0 is a validation-only matching and evolution package. It may establish a declared-order operator-matching pilot and a mathematically consistent two-scale evolution engine. It may not claim:

```text
PHYSICAL_TMD_EXTRACTION
GLOBAL_QCD_MATCHING_COMPLETE
ALL_ORDER_SOFT_FUNCTION_COMPLETE
ALL_ORDER_RAPIDITY_RENORMALIZATION
PHYSICAL_COLLINS_SOPER_KERNEL_DETERMINED
PROCESS_FACTORIZATION_READY
SIDIS_PREDICTION_READY
DRELL_YAN_PREDICTION_READY
GLUON_PROCESS_READY
W_PLUS_Y_READY
INFERENCE_READY
PRODUCTION_READY
```

No C19 object may become reachable from the accepted 216-route production root.

## Normative sources

Read and use the repository copies of the following as normative sources when present:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_i_regulated_light_front_foundations.tex
references/volume_ii_common_nucleon_gtmd_overlaps.tex
references/volume_iii_dynamical_wilson_lines.tex
references/volume_iv_matched_spin1_nuclear_dynamics.tex
references/volume_v_matching_evolution_factorization.tex
references/volume_vi_shared_inference_validation.tex
references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_ix_dynamical_gluon_fock_sectors.tex
references/volume_x_light_sea_chiral_pcac_antiquark_gtmds.tex
references/volume_xi_microscopic_nonzero_transfer_gtmds.tex
references/volume_xii_microscopic_wilson_second_order.tex
references/volume_xiii_nnpi_pion_matching_coherent_nuclear.tex
references/volume_xiv_continuum_nnpi_exchange_currents.tex
references/volume_xv_delta_delta_six_quark_hidden_color.tex
references/model_construction_note.tex
```

Record exact hashes and availability in a C19 source-integration manifest. Do not invent content from a missing source. The equations and requirements below remain mandatory even if a source is absent.

## Autonomy and completeness

Completeness and scientific correctness are the objectives. Do not optimize for quickness.

Continue autonomously until every C19 acceptance criterion is satisfied. Do not stop to ask permission for routine local inspection, testing, documentation generation, non-destructive tooling, or dependency installation when the environment permits it. If one optional tool is unavailable, use another route and document the limitation. Do not abandon the rest of the work.

Do not push the final commit.

---

# 1. Immutable regression baseline

Before code changes, reproduce and record:

- all **1,015** existing tests;
- all C18 builders, validators, and benchmark families;
- **36/36** evidence rows;
- **162/162** atlas pages;
- all **762** C18 requirements;
- all **400** C18 negative injections;
- all prior C3–C17 injection suites;
- the accepted production registry at exactly **216** routes;
- all eight authoritative production artifacts byte-identically;
- all pinned C15–C18 manifests byte-identically;
- the clean working-tree state;
- the C18 ancestry.

If the baseline does not reproduce, diagnose it before implementing C19. Do not repair a baseline failure by changing accepted physics.

---

# 2. Package location and isolation

Implement the new package under a dedicated validation-only namespace such as

```text
src/deuteron_wigner/matching/m0/
```

or an equivalent isolated package consistent with the repository architecture.

C19 may import read-only microscopic objects from C11–C18. It must not modify their physical meaning, hashes, benchmark results, or provenance identities.

Create a disjoint C19 validation root. No C19 node may have a path to:

```text
PRODUCTION_ROOT
NUCLEAR_PHYSICAL_PREDICTION_ROOT
PROCESS_ROOT
INFERENCE_ROOT
```

The production resolved-parent builder must reject C19 objects.

---

# 3. Core typed objects

Implement or extend the following interfaces. Reuse existing C1–C18 types where appropriate; do not create parallel coordinate, rank, path, color, member, or provenance type systems.

## 3.1 `TMDSchemeId`

A complete immutable scheme identity containing at least:

```text
uv_renormalization_scheme
uv_scale_mu
rapidity_regulator
rapidity_scale_zeta
soft_factor_definition
soft_partition_rule
staple_and_cusp_convention
transverse_closure
color_representation
ordered_gluon_link_pair
gluon_f_or_d_class
fourier_convention
bTMD_coordinate_identity
rank_and_mass_convention
active_flavor_number_nf
threshold_history
perturbative_order_manifest
scheme_version
```

The scheme identity must distinguish \(\bm b_\Delta\) from \(\bm b_{\mathrm{TMD}}\). They may never alias.

## 3.2 `MatchingOperatorId`

A complete operator identity containing:

```text
parton_species
flavor
quark_dirac_or_gluon_lorentz_projection
source_and_target_momentum_fibers
target_species
target_polarization_channel
parton_polarization
twist
transverse_rank
bessel_order
reference_mass
extracted_kT_and_bT_powers
wilson_path
ordered_gluon_links
f_or_d_color_class
nuclear_sector_source
nuclear_sector_target
local_or_bilocal_status
current_or_EMT_moment_status
regulator_identity
microscopic_member
assumption_plan
```

## 3.3 `MatchingBasis`

A closed, versioned basis on both sides:

```text
LF regulated operator basis
QCD renormalized operator basis
mixing blocks
local-current and EMT reductions
collinear operator reductions
missing-operator statuses
power-remainder statuses
```

The basis must contain all operators needed to represent the declared C18 common parent at the C19 scope.

A missing operator must be recorded as one of:

```text
UNAVAILABLE_AT_THIS_TWIST
UNAVAILABLE_AT_THIS_MATCHING_ORDER
REQUIRES_MULTIPARTON_OPERATOR
REQUIRES_HIGHER_FOCK_SUPPORT
REQUIRES_NONZERO_SKEWNESS
REQUIRES_PROCESS_SPECIFIC_FACTOR
```

It may not be represented by a zero coefficient without a theorem.

## 3.4 `LFtoQCDMatchingMap`

A versioned linear/convolution map

\[
\widetilde{\bm W}^{\,\mathrm{QCD}}
=
\bm Z_{\mathrm{LF}\to\mathrm{QCD}}
\otimes_x
\widetilde{\bm W}^{\,\mathrm{LF}}
+
\bm\Delta_{\mathrm{trunc}}.
\]

It must retain:

```text
source_basis
target_basis
matching_conditions
shared_parameters
mixing_matrix
x_convolution
bTMD_dependence
step_scaling_links
local_current_constraints
lattice_or_external_constraints_if_used
discrepancy_operator_basis
power_remainders
calibration_and_holdout_records
```

No parameter may be attached directly to one named TMD unless it corresponds to a genuine operator or discrepancy block shared by every relevant projection.

## 3.5 `RenormalizedTMDOperator`

A scheme-qualified operator with:

```text
mu
zeta
scheme
link_and_color_identity
rank
target_channel
nuclear_sector
microscopic_member
matching_status
evolution_status
accuracy_manifest
```

## 3.6 Evolution objects

Implement:

```text
AnomalousDimensionSet
EvolutionPath
EvolutionOneForm
FiniteOrderCurlReport
CollinsSoperKernel
RankTransform
SmallBOPE
CollinearEvolution
ThresholdMatchingMap
EvolutionEnsembleStore
ClosureReport
AccuracyManifest
```

---

# 4. Declared validation schemes

Implement at least two finite-related validation schemes.

## 4.1 Reference scheme

Use the repository’s declared canonical scheme when it is complete enough for the C19 validation scope. Otherwise define a validation scheme with explicit identity such as:

```text
M0_REFERENCE:
    MSBAR UV
    declared delta-type rapidity regulator
    square-root soft partition
    explicit staple/cusp convention
    separate fundamental and adjoint soft objects
    declared Fourier and rank conventions
```

Do not call the scheme physical or complete unless every required element is implemented.

## 4.2 Finite-related comparison scheme

Define a second scheme related by a finite operator-basis transformation:

\[
\widetilde{\bm F}^{\,\mathfrak s'}
=
\bm R_{\mathfrak s'\leftarrow\mathfrak s}
\otimes_x
\widetilde{\bm F}^{\,\mathfrak s}.
\]

The inverse map must be implemented through the declared order.

Operator-level matrix elements and matched local moments must agree after converting both the operators and matching coefficients. Applying a scheme conversion to the TMD while leaving the coefficient/moment adapter unchanged must fail.

The two schemes are alternatives. They cannot be added.

---

# 5. Closed microscopic operator basis

Build the C19 matching basis from the actual C18 parent.

It must preserve the following identities.

## 5.1 Nucleon partonic structure

```text
u
d
ubar
dbar
gluon
proton
neutron
all supported helicity matrices
Wilson orders 0, 1, 2
future/past orientation
four ordered gluon link pairs
f-type and d-type color classes
```

## 5.2 Nuclear structure

```text
NN
continuum NNPI
DeltaDelta
compact six-quark
cluster complement
hidden-color basis covariance
all diagonal and supported transition blocks
U/L/T/LL/LT/TT
SS/SD/DS/DD ancestry
pion-active and transition ancestry
coherent-pilot ancestry
current and EMT ancestry
```

## 5.3 Local operators

Include all supported:

```text
vector currents
axial currents
pseudoscalar operators
energy-momentum operators
charge/magnetic/quadrupole combinations
canonical OAM diagnostics
tensor operators where actually available
```

Do not import an unavailable local tensor operator or external tensor charge to fill a basis gap.

## 5.4 Operator closure report

For every C18 parent projection, the report must identify:

- its LF operator source;
- its QCD target operator;
- mixing partners;
- local or collinear reductions;
- matching order;
- power remainder;
- missing coefficient status;
- whether it is executable in C19.

---

# 6. Matching strategies and assumption plans

Compile at least two mutually exclusive matching plans.

## 6.1 `M0-PLAN-A — perturbative-window validation`

Use a controlled analytic or finite-dimensional benchmark in which the LF cutoff and continuum matching scale provide a declared perturbative window.

Implement:

- an explicit matching matrix;
- one or more off-diagonal mixing entries;
- exact or analytic step scaling;
- local-current and EMT constraints;
- more independent matrix elements than free matching parameters;
- a nonzero holdout set.

This plan is a validation oracle. It is not evidence that the physical H7/N3 cutoff lies in the same perturbative window.

## 6.2 `M0-PLAN-B — hybrid step-scaling validation`

Use:

- LF-resolution step scaling;
- local current and EMT constraints;
- selected continuum/lattice-like analytic matrix-element oracles;
- a restricted shared discrepancy basis;
- explicit missing-operator remainders.

The same parameters must propagate through quark, antiquark, gluon, nucleon, deuteron, and local-moment projections whenever they belong to the same operator block.

The two plans may be compared but never summed.

---

# 7. Step scaling and matching trajectory

For resolutions \(r\preceq r'\), implement a step-scaling map

\[
\bm\Sigma_{r'\leftarrow r}.
\]

Test the cocycle relation

\[
\bm\Sigma_{r''\leftarrow r'}
\bm\Sigma_{r'\leftarrow r}
=
\bm\Sigma_{r''\leftarrow r}
+
\bm\delta_{r''r'r}.
\]

Report:

```text
cocycle_residual
operator_block
resolution_path
basis_conditioning
matching_parameter_flow
missing_operator_remainder
```

The matched observable, not the bare wave-function coefficient or Fock probability, is the convergence target.

A smooth result at one resolution is not a matching trajectory.

---

# 8. UV, rapidity, and soft identities

Keep the following contributions separate:

```text
unsubtracted microscopic matrix element
UV renormalization
rapidity renormalization
soft subtraction
finite scheme conversion
LF-to-QCD finite matching
Hamiltonian/Fock truncation remainder
```

At each supported Wilson order, implement the declared-order identity. For example, through first order:

\[
W_{\rm ren}^{(1)}
=
W_{\rm unsub}^{(1)}
-\frac12 S^{(1)}W^{(0)}
+R_{\rm rap}^{(1)}W^{(0)}
+Z_{\rm UV}^{(1)}W^{(0)}
+Z_{\rm LF\to QCD}^{(1)}\otimes W^{(0)}.
\]

Where the C14/C18 strict second-order data are consumed, use the declared strict second-order square-root-soft expansion and retain every cross term.

The benchmark must show:

```text
correct UV/rapidity/soft combination -> declared regulator cancellation
missing soft term                    -> signed residual
duplicate soft term                  -> opposite signed residual
missing rapidity factor              -> nonzero rapidity residual
wrong color representation           -> mismatch
wrong Wilson link pair               -> mismatch
UV scheme conversion on only one side -> mismatch
```

An unresolved finite coefficient must remain `UNRESOLVED_NOT_ZERO`.

---

# 9. Link shortening and marginal identities

The regulated LF staple operator is not automatically a collinear PDF/GPD/current operator.

Implement explicit typed adapters for:

```text
staple TMD/GTMD operator
    -> small-b collinear operator basis
straight-link GPD operator
    -> local-current/EMT moments
```

Every adapter must carry:

- path shortening or deformation status;
- cusp and soft-factor status;
- UV and rapidity scheme;
- operator mixing;
- power corrections;
- proof or matching condition.

A literal \(k_T\) integral of an unmatched soft-subtracted TMD may not be equated to a PDF or local current.

---

# 10. Rank-aware Fourier–Bessel transforms

Use the existing rank metadata. For harmonic \(m\),

\[
\widetilde F^{(m)}(x,b)
=
2\pi i^m
\int_0^\infty k\,dk\,
J_{|m|}(bk)
N_m(k)
F^{(m)}(x,k).
\]

Implement forward and inverse transforms with:

```text
harmonic m
Bessel order
Fourier phase
reference mass
extracted kT power
extracted bT power
quadrature identity
analytic oracle
round-trip residual
```

At minimum test ranks \(0,1,2\), and every higher rank already declared by the microscopic registry.

A scalar \(J_0\) transform applied to a nonzero-rank operator must fail.

Keep \(\bm b_\Delta\) and \(\bm b_{\mathrm{TMD}}\) distinct in all APIs and cache keys.

---

# 11. Small-\(b_{\mathrm{TMD}}\) OPE

Implement a typed OPE

\[
\widetilde F_A^{a/h}(x,b;\mu,\zeta)
=
\sum_{B,j}
C_{A\leftarrow B}^{a\leftarrow j}
\otimes_x
f_B^{j/h}(x;\mu)
+
\mathcal O\!\left((b\Lambda)^p\right).
\]

Every coefficient record must contain:

```text
source TMD/GTMD operator
target collinear operator
parton species
flavor
target channel
transverse rank
twist
Wilson-link and color class
lowest nonzero perturbative order
implemented order
scheme
power remainder
coefficient status
```

## 11.1 Required executable pilot channels

At minimum implement analytic or declared-order validation coefficients for:

- unpolarized quark and antiquark rank zero;
- quark helicity rank zero;
- quark transversity where supported;
- unpolarized gluon rank zero;
- gluon helicity rank zero;
- linearly polarized gluon through its first nonzero analytic pilot coefficient;
- deuteron \(LL\) tensor-polarized rank-zero quark and gluon channels;
- one nontrivial singlet quark–gluon mixing block.

## 11.2 T-odd and multiparton channels

Sivers, Boer–Mulders, and gluon \(f/d\) link-odd channels require twist-three or multi-parton operator bases.

C19 must:

- create their typed collinear operator basis;
- preserve \(f\)- and \(d\)-type tri-gluon distinctions;
- implement an analytic mixing oracle;
- mark any unavailable physical coefficient as unavailable;
- refuse to use a twist-two coefficient as a substitute.

No T-odd small-\(b\) channel may be declared physically matched merely because the microscopic Wilson parent exists.

## 11.3 Power remainder

The OPE must carry an explicit power-remainder estimate or status. A smooth \(b\)-space curve is not proof that the small-\(b\) expansion is valid.

---

# 12. Collinear evolution pilot

Implement validation-level evolution interfaces for:

```text
nonsinglet unpolarized
singlet quark-gluon
helicity
transversity
spin-1 tensor-polarized singlet
gluon double-helicity-flip
twist-three/multiparton placeholder or analytic oracle
```

At minimum, use exact or analytic kernels sufficient to test:

- conserved nonsinglet moments;
- singlet mixing;
- quark/gluon momentum conservation;
- helicity or transversity nonmixing where appropriate;
- tensor-channel use of the correct operator basis;
- failure on an unsupported twist-three kernel.

Do not claim full phenomenological DGLAP accuracy unless actual physical kernels and orders are implemented and audited.

---

# 13. Two-scale TMD evolution

Use the convention

\[
\frac{d}{d\ln\mu}
\ln \widetilde F_a
=
\gamma_F^a(\mu,\zeta),
\]

\[
\frac{d}{d\ln\sqrt\zeta}
\ln \widetilde F_a
=
-\mathcal D_a(b;\mu),
\]

with

\[
\frac{\partial\gamma_F^a}
{\partial\ln\sqrt\zeta}
=
-\Gamma_a,
\qquad
\frac{d\mathcal D_a}{d\ln\mu}
=
\Gamma_a.
\]

Implement:

```text
quark anomalous-dimension set
gluon anomalous-dimension set
fundamental Collins-Soper kernel
adjoint Collins-Soper kernel
evolution one-form
direct contour path
alternative contour path
optional integrability-restored path
finite-order curl report
transitivity report
scale-variation plan
```

## 13.1 Exact integrable oracle

Create an analytic benchmark for which the evolution one-form is closed and two distinct paths give the same result.

## 13.2 Finite-order curl benchmark

Create a controlled truncated benchmark with a nonzero curl. Report the path dependence instead of fitting it away.

## 13.3 Representation and target independence

The kernel may depend on the parton color representation. It must not acquire an independently fitted value for every target polarization or named TMD.

A target-channel-dependent kernel request must fail unless supported by a new operator-level theorem or matching result.

## 13.4 Rank preservation

Evolution is radial and may not change transverse rank.

## 13.5 Link reversal

Initialize

\[
F_{\rm even}^{[+]}=F_{\rm even}^{[-]},
\qquad
F_{\rm odd}^{[+]}=-F_{\rm odd}^{[-]}.
\]

Evolve future and past members with the same representation-level kernel and verify these identities at every scale. Using different kernels for future and past must fail.

---

# 14. Heavy-flavor threshold oracle

Implement a validation-only threshold map that changes \(n_f\) while matching:

- the coupling;
- collinear operators;
- anomalous dimensions;
- TMD matching coefficients;
- evolution history.

A conserved physical moment must remain continuous through the threshold.

Changing \(n_f\) without the threshold map must fail.

No physical charm or bottom phenomenology is claimed by this oracle.

---

# 15. Nuclear matching and evolution

The complete C18 nuclear parent must retain its resolved graph through matching and evolution:

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

## 15.1 Impulse commutation benchmark

For a scale-independent spectral kernel \(S\), test numerically and analytically that

\[
P\otimes_x(S\otimes_x f)
=
S\otimes_x(P\otimes_x f)
\]

within the declared scope.

## 15.2 Non-impulse operators

Pion-active, transition, coherent, \(\Delta\Delta\), compact, and two-body operators with their own scale dependence must receive distinct matching/evolution blocks or remain unavailable.

They may not be hidden inside a scalar nuclear correction transported with the one-body kernel.

## 15.3 Hidden-color covariance

Matching and evolution must preserve invariance of the complete six-quark observable under unitary rotations of the four-dimensional hidden-color basis.

Individual hidden-color basis weights may vary. Complete observables may not.

---

# 16. Matching calibration, holdouts, and identifiability

Use a restricted shared calibration set. Suitable validation conditions include:

- proton and neutron vector charges;
- selected axial matrix elements;
- nucleon and deuteron EMT moments;
- deuteron charge normalization;
- one quadrupole or angular-condition combination;
- selected step-scaling matrix elements.

Reserve holdouts such as:

- a second nonzero-transfer current point;
- another EMT component;
- one tensor-polarized moment;
- one antiquark or gluon matrix element;
- one \(\Delta\Delta\) or compact-sector moment;
- one link-odd color channel;
- one evolution-path or threshold observable.

The number of independent matching conditions must exceed the number of matching parameters in every benchmark intended to demonstrate predictivity.

Export:

```text
matching Jacobian
singular values
null directions
parameter correlations
profile residuals
holdout residuals
```

A null direction must remain visible. It may not be hidden by fitting one more named TMD.

---

# 17. Accuracy manifest

Each executable result must carry an accuracy tuple such as

\[
\mathfrak A
=
\left(
p_\Gamma,
p_{\gamma},
p_{\mathcal D},
p_C,
p_{\rm coll},
p_{\rm threshold},
p_{\rm num}
\right).
\]

The generated human-readable label must identify the bottleneck order.

A high-order cusp coefficient cannot upgrade a result whose small-\(b\) coefficient, collinear kernel, or matching map is lower order or unavailable.

---

# 18. Provenance and no-double-counting rules

Extend the provenance two-complex with:

```text
LF_REGULATED_OPERATOR
UV_RENORMALIZATION
RAPIDITY_RENORMALIZATION
SOFT_SUBTRACTION
FINITE_SCHEME_CONVERSION
LF_TO_QCD_MATCHING
SMALL_B_OPE
COLLINEAR_EVOLUTION
TMD_EVOLUTION
THRESHOLD_MATCHING
NUCLEAR_OPERATOR_BLOCK
```

Required executable relations include:

```text
unsubtracted + UV + rapidity - soft
    DERIVES
renormalized operator

explicit microscopic soft region
    OVERLAPS_WITH
soft factor region

scheme A operator
    EQUIVALENT_TO
scheme B operator + finite conversion

explicit nuclear sector
    ALTERNATIVE_TO
its fully induced replacement + remainder
```

Reject:

- duplicate soft subtraction;
- explicit and induced descriptions together;
- scheme A and B values added;
- bare and renormalized objects added;
- matching and OPE coefficients attached by TMD name instead of operator identity;
- evolution applied before matching;
- process assembly without a process record.

---

# 19. Required benchmark families

Implement at least the following C19 benchmark families with stable IDs.

## M0-A — scheme identity and round trip

Two finite-related schemes; forward and inverse conversion; exact declared-order round trip.

## M0-B — closed operator-basis reconstruction

Build and reconstruct a mixed quark/antiquark/gluon operator vector with local-current and EMT reductions.

## M0-C — overconstrained matching fit

More matrix elements than parameters; exact oracle recovery; explicit holdouts; visible Jacobian null direction in a separate underconstrained injection.

## M0-D — step-scaling cocycle

Three resolutions; direct versus composed step scaling; measured cocycle defect.

## M0-E — UV/rapidity/soft cancellation

Correct cancellation and signed missing/duplicate residuals in fundamental and adjoint representations.

## M0-F — link shortening and local moments

Regulated staple, straight-link, collinear, and local-current adapters; mismatched paths fail.

## M0-G — rank-aware Fourier–Bessel transforms

Ranks \(0,1,2\) and all additional declared ranks; analytic round trips; wrong Bessel order fails.

## M0-H — small-\(b\) OPE

Rank-zero, linearly polarized gluon, tensor \(LL\), singlet mixing, and twist-three typed-unavailable cases.

## M0-I — collinear evolution

Conserved nonsinglet moment; singlet momentum conservation; unsupported kernel rejection.

## M0-J — two-scale integrability

Exact closed one-form; two paths and transitivity agree.

## M0-K — finite-order curl

Nonzero controlled path dependence; no silent integrability repair.

## M0-L — link reversal under evolution

T-even equality and T-odd sign reversal preserved.

## M0-M — heavy-threshold continuity

Matched \(n_f\) transition; inverse route; missing threshold map fails.

## M0-N — nuclear impulse commutation

Match/evolve before versus after scale-independent impulse convolution.

## M0-O — non-impulse nuclear block separation

Pion, coherent, \(\Delta\Delta\), compact, and transition operators remain distinct or unavailable.

## M0-P — hidden-color basis covariance

Two hidden-color bases give the same complete matched/evolved six-quark observable.

## M0-Q — exact/full-bond and reduced-bond propagation

Matching/evolution of exact and TTN microscopic members; full bond closes; low bond retains its observable error.

## M0-R — accuracy bottleneck

Generated label follows the least accurate required ingredient; deliberate accuracy laundering fails.

---

# 20. Negative injections

Add at least **480 new ordered C19 negative injections** with stable IDs and structured diagnostics.

The suite must cover, at minimum:

## 20.1 Scheme and identity faults

- missing UV scheme;
- missing rapidity regulator;
- missing soft partition;
- wrong \(\mu\) or \(\zeta\);
- \(b_\Delta\) used as \(b_{\mathrm{TMD}}\);
- quark scheme applied to gluon;
- future/past path loss;
- ordered gluon-link loss;
- \(f/d\) color alias;
- wrong rank, Bessel order, phase, or mass convention.

## 20.2 Operator-basis faults

- incomplete mixing block;
- named-TMD-only matching coefficient;
- missing local-current partner;
- unavailable operator silently set to zero;
- quark/antiquark copy;
- missing nuclear sector identity;
- hidden-color basis treated as an additive sector.

## 20.3 Matching faults

- underconstrained fit declared unique;
- null direction hidden;
- one parameter per TMD;
- step-scaling cocycle violation;
- wrong resolution map;
- bare wave-function convergence used as matching evidence;
- holdout used in calibration without a new split.

## 20.4 UV/rapidity/soft faults

- missing half-soft term;
- duplicate soft subtraction;
- missing rapidity factor;
- physicalized numerical regulator;
- wrong representation soft factor;
- unresolved finite matching set to zero;
- microscopic soft region counted again in the soft factor.

## 20.5 Small-\(b\) faults

- scalar \(J_0\) used for rank one/two;
- wrong reference mass;
- twist-two coefficient used for Sivers;
- \(f\)-type coefficient used for \(d\)-type tri-gluon channel;
- unavailable physical coefficient declared complete;
- power remainder omitted.

## 20.6 Evolution faults

- target-dependent CS kernel without justification;
- future/past evolved with different kernels;
- rank changed by evolution;
- nonzero curl hidden;
- transitivity failure;
- quark kernel used for gluon;
- unsupported twist-three evolution executed;
- \(n_f\) changed without threshold matching.

## 20.7 Nuclear faults

- scalar nuclear response carrying all sectors;
- coherent or pion block evolved as impulse;
- cluster and full six-quark double counted;
- hidden-color basis dependence in the full observable;
- proton and neutron microscopic members decorrelated;
- Wilson order mixed inside one nuclear member.

## 20.8 Downstream leakage

- C19 object enters the 216-route registry;
- production artifact changes;
- physical TMD status issued;
- SIDIS or DY process constructed;
- \(W+Y\) constructed;
- inference or fit run;
- nuclear physical prediction status issued.

---

# 21. Required documentation and manifests

Create at least:

```text
docs/next_level/c19_implementation_report.md
docs/next_level/c19_api.md
docs/next_level/c19_normative_source_integration.json
docs/next_level/c19_regression_report.json
docs/next_level/c19_requirement_coverage.json
docs/next_level/c19_injection_manifest.json
docs/next_level/c19_scheme_manifest.json
docs/next_level/c19_matching_basis.json
docs/next_level/c19_matching_map_manifest.json
docs/next_level/c19_step_scaling_report.json
docs/next_level/c19_small_b_ope_manifest.json
docs/next_level/c19_rank_transform_report.json
docs/next_level/c19_collinear_evolution_report.json
docs/next_level/c19_two_scale_evolution_report.json
docs/next_level/c19_threshold_report.json
docs/next_level/c19_nuclear_matching_report.json
docs/next_level/c19_accuracy_manifest.json
docs/next_level/c19_unresolved_physics_gaps.md
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

when appropriate.

All generated manifests must rebuild deterministically and byte-for-byte.

---

# 22. Acceptance criteria

C19/M0 is complete only when all of the following hold.

1. The full C18 baseline reproduces before edits.
2. The complete C18 microscopic operator parent maps into a closed C19 matching basis or receives an explicit unavailable status.
3. No named TMD receives its own matching normalization.
4. At least two finite-related validation schemes round-trip correctly.
5. The LF-to-QCD matching pilot is overconstrained and has independent holdouts.
6. Step-scaling cocycle defects are reported and satisfy the declared tolerance.
7. UV, rapidity, soft, and finite-matching pieces remain separately identifiable.
8. Missing and duplicate soft/rapidity operations leave signed failures.
9. Link shortening and local-current reductions are explicit typed maps.
10. Rank-aware Fourier–Bessel transforms close for all supported ranks.
11. The small-\(b\) OPE uses the correct collinear operator basis and marks missing coefficients honestly.
12. Quark, antiquark, gluon, \(LL\), link-odd, and nuclear operator identities remain intact.
13. Nonsinglet and singlet collinear analytic benchmarks pass.
14. The exact two-scale oracle is path independent.
15. The finite-order curl benchmark reports nonzero path dependence.
16. Quark and gluon CS kernels remain separate representation objects.
17. Target polarization does not create one kernel per TMD.
18. T-even and T-odd link-reversal relations survive evolution.
19. Heavy-threshold continuity passes only with the threshold map.
20. Scale-independent impulse matching/evolution commutes within tolerance.
21. Non-impulse nuclear blocks remain separate or unavailable.
22. Hidden-color basis covariance survives matching and evolution.
23. Exact and full-bond TTN members agree; reduced-bond errors remain visible.
24. Every result carries an accuracy manifest with a bottleneck order.
25. All new C19 negative injections are detected.
26. All pre-existing tests, builders, evidence, atlas pages, requirements, injections, manifests, production routes, and authoritative artifacts remain unchanged.
27. Every C19 object remains unreachable from production, process, inference, and physical-prediction roots.
28. All C19 JSON artifacts rebuild byte-for-byte.
29. The working tree is clean after the final commit.
30. The final C19 commit is local and not pushed.

---

# 23. Allowed statuses

C19 may issue only scoped statuses such as:

```text
M0_TMD_SCHEME_IDENTITY_VALIDATED
M0_CLOSED_MATCHING_BASIS_VALIDATED
M0_LF_TO_QCD_MATCHING_PILOT_VALIDATED
M0_STEP_SCALING_VALIDATED
M0_UV_RAPIDITY_SOFT_ACCOUNTING_VALIDATED
M0_SMALL_B_OPE_PILOT_VALIDATED
M0_RANK_TRANSFORM_VALIDATED
M0_COLLINEAR_EVOLUTION_PILOT_VALIDATED
M0_TWO_SCALE_EVOLUTION_ENGINE_VALIDATED
M0_THRESHOLD_ORACLE_VALIDATED
M0_NUCLEAR_OPERATOR_GRAPH_PRESERVED
M0_VALIDATION_ONLY
```

The following remain forbidden:

```text
PHYSICAL_TMD
PHYSICAL_GTMD
PHYSICAL_DEUTERON_TMD
FULL_LF_TO_QCD_MATCHING_COMPLETE
ALL_ORDER_EVOLUTION
PHYSICAL_CS_KERNEL_DETERMINED
PROCESS_READY
W_PLUS_Y_READY
INFERENCE_READY
PRODUCTION_READY
```

---

# 24. Final response

At completion, report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection totals;
- production and artifact hash status;
- available normative sources and hashes;
- matching basis dimensions and missing-operator counts;
- matching parameter and condition counts;
- matching Jacobian rank and null directions;
- maximum matching and holdout residuals;
- step-scaling cocycle residual;
- scheme round-trip residual;
- UV/rapidity/soft residuals;
- rank-transform round-trip residuals;
- small-\(b\) OPE closure and missing-coefficient statuses;
- collinear sum-rule residuals;
- two-scale path, curl, and transitivity residuals;
- threshold residual;
- nuclear impulse-commutation residual;
- hidden-color basis-covariance residual;
- exact/full-bond and reduced-bond evolution differences;
- all unresolved physical gates;
- exact recommended C20 package.

Create a final local commit. Do not push it.
