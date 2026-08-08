# Executable roadmap: parent-derived spin-1 GTMD/TMD model

## 2026-07-30 — C6 active-gluon ordered-link and soft-overlap pilot

Status: **complete at local commit
`ce4b761d19b23bd5f7da1ddc026153685943e639`; not pushed**.

C6 extends the isolated C5 one-Wilson-order pilot to the C4 positive-x active
gluon. It implements four ordered two-adjoint-link identities, one common
target/gluon-helicity and transverse/color tensor parent, explicit ordered
generator products, independent normalized `f` and `d` color projections,
all three existing gluon polarization projections, complete ordered-pair
antiunitary reversal, and a boundary-only analytic half-soft subtraction with
an executable rapidity derivative.

Final validation is 759/759 tests, nine/nine legacy acceptance/report
builders, 36/36 evidence rows, and 162/162 atlas pages. All 60 C6, 48 C5, 40
C4, and 24 C3 injections pass. The four link pairs generate a 24-entry
validation registry (four links times two color channels times three
polarization views). The eight authoritative hashes, 216-route registry,
production provenance/default plan, C5 manifests, and Volumes 0--V hashes
remain unchanged.

Benchmark residuals: `f` norm 0, `d` norm
`1.7763568394002505e-15`, `f·d` 0, declared color-subspace reconstruction
`2.340043593158424e-15`, both polarization reconstructions 0, link-even and
all coupling/cut/OAM zero limits 0, rapidity derivative after one subtraction
0, missing/duplicate subtraction magnitudes `0.7071067811865475` with
opposite signs, separate `f`/`d` Ward residuals 0, and C4 qqqg color-singlet
residual `5.551115123125783e-17`.

Volume VI was not present in the repository or Downloads and inference was
not implemented. Volume IV nuclear, Volume V matching/evolution/process, and
Volume VI inference gates remain closed. The exact recommended next package
is **C7: second-order non-Abelian Wilson-line convergence and common-state
Ward closure**, comparing strict Dyson and Magnus representations while
preserving independent active-gluon `f/d` identities and production
isolation.

## 2026-07-30 — C5 one-gluon Wilson-line and LF-cut pilot

Status: **complete at local commit
`c4aeb380bc3c23b8dcf2fb6a4528042de598cb48`; not pushed**.

C5 adds a validation-only first-Wilson-order dynamical pilot using the C1
identity spine and C3/C4 common-parent infrastructure. It implements a typed
semi-infinite fundamental Wilson segment, convention-derived eikonal pole,
separate distributional PV-plus-cut and finite-epsilon convergence routes,
typed LF resolvents and cut provenance, a one-gluon OAM-interference kernel,
the full pilot antiunitary future/past adapter, and distinct Sivers-like and
Boer--Mulders-like `RED` projections. It does not modify or feed the accepted
phenomenological model.

Final validation is 679/679 tests, nine/nine legacy acceptance/report
builders, 36/36 evidence rows, and 162/162 atlas pages. All 48 C5 injections,
40 C4 injections, and 24 C3 injections pass. The 216-route registry,
production provenance/default plan, C4 architecture counts, all six
formalism-source hashes, and all eight authoritative artifact hashes are
unchanged. C5-A finite-epsilon convergence reaches a residual of
`0.007301736391504221`; every other reported analytic sign, zero-limit, Ward,
color-orthogonality, link-even/odd, and double-count residual is zero except
the expected floating SU(3) Casimir residual
`2.220446049250313e-16`.

Volume IV and V entry gates remain explicitly closed. The exact recommended
next package is a validation-only extension to independent active-gluon
ordered-link `f`/`d` rescattering channels with explicit soft/rapidity overlap
accounting. It must first preserve the C5 result envelope and cut ledger, and
must not claim a physical gluon T-odd TMD, QCD matching, evolution, or nuclear
composition.

## 2026-07-30 — formalism source-volume import

Normative C4 integration commit:
`6662bbc64375fc4ada2e21447fc9ebdda46025dc` (local only; not pushed).
Volume IV interface-audit commit:
`bf62a6a0c1fe436bde9966df57cac555266b70f5` (local only; not pushed).

The supplied TeX sources for Volumes 0, I, II, III, IV, and V are now preserved
byte-for-byte under `references/`; exact hashes and titles are recorded in
`references/formalism_volume_index.md`. C5 must read Volume III completely
before implementation. Historical C4 baseline records correctly continue to
show that these sources were absent during C4 execution.

## 2026-07-30 — C4 sea/gluon and common-route validation pilot

Local completion commit:
`b251bd035de6bc31d47d1a585241a3d1458146cb`.
This commit was intentionally not pushed, per the C4 work-package rule.

C4 extends the validation-only analytic pilot with normalized
`qqq + qqqq-qbar` and `qqq + qqqg` sector superpositions, explicit positive-x
active selectors, verified five-parton cluster and qqq-octet--adjoint color
singlets, exact sea/gluon zero limits, separate quark/gluon moment conventions,
regulated TMD/GPD/PDF/current route closure, and an exact finite Feshbach
induced-operator benchmark.

Final validation is 609/609 tests, nine/nine acceptance builders, 36/36
evidence rows, and 162/162 atlas pages. All 40 C4 injections and all preceding
C1--C3 mismatch tests pass. The eight production artifacts, 216 reductions,
C2 graph/default plan, C3 manifests, and production builder remain unchanged.

The requested Volume 0--IV TeX files and model-construction TeX note are not
present in this public repository. C4 therefore follows the explicit preserved
prompt and existing C0--C3 formal records. The sea/gluon states are analytic
validation fixtures, not physical distributions or a QCD matching result.

Exact next job: **C5 validation-only one-gluon Wilson-line and light-front-cut
pilot**. Add eikonal pole prescriptions, explicit intermediate-state cuts,
future/past reversal, and separate gluon color contractions while remaining
disconnected from accepted production.

## 2026-07-29 — C3 analytic common-overlap pilot

Local completion commit:
`b0a18ce2d1017e102b2be0849abf4d31537874a8`.
This commit was intentionally not pushed, per the C3 work-package rule.

C3 added a strictly validation-only microscopic-formal pilot under
`src/deuteron_wigner/pilot/`: typed zero-skewness momentum fibers, intrinsic
configurations, one symmetric active/spectator recoil authority, normalized
analytic states, one diagonal zeroth-rescattering AMP kernel/evaluator,
validation-only C2 reduction bridge, and a disjoint provenance graph.

Benchmarks A–D pass. Final validation is 538/538 tests, nine/nine acceptance
builders, 36/36 evidence rows, and 162/162 atlas pages. All eight artifacts,
the 216 accepted reductions, C2 provenance graph, default composition plan,
and production builder independence remain unchanged.

Volumes I–III remain absent. The pilot is not a Hamiltonian solution or
physical GTMD model and has no production authorization.

Exact next job: **C4 validation-only minimal sea/gluon sectors and common
TMD/GPD/PDF/current route closure (Volume II Benchmarks E–F)**. Keep it
disconnected from accepted production and defer dynamical Wilson lines until
common-parent reduction closure passes.

## 2026-07-29 — C2 native reductions and provenance graph

Local completion commit:
`5063c002e763f3d6a0affc774ec6b124a539f0be`.
This commit was intentionally not pushed, per the C2 work-package rule.

C2 extends the C1 formal package with native typed reduction identities, a
216-route accepted registry (72 quark, 72 antiquark, 72 gluon), typed
provenance nodes/relations, deterministic composition plans, exclusion and
replacement enforcement, and metadata-only trace queries. The resolved-parent
production builder validates the C2 plan before combining arrays and emits a
separate semantic manifest.

Final validation: 519/519 tests, all nine acceptance/report builders, 36/36
evidence rows, and 162/162 atlas pages pass. All eight authoritative
parent/correlator hashes remain byte-identical. No physical formula, central
selection, ordering, or numerical artifact changed.

Remaining adapters: specialized Fourier/projector kernels and private
nuclear/evolution/process helpers retain legacy arrays/scalar coordinates
behind typed public registry boundaries. Volume I and II TeX sources were not
present. Nonzero-transfer reductions remain explicitly unavailable.

Exact next job: **C3 zero-skewness momentum-fiber, recoil-map, and analytic
common-overlap pilot**, disconnected from central artifacts until analytic
forward-identity, transfer-reversal, Jacobian, Hermiticity, support, and
commuting-reduction gates pass.

## 2026-07-28 — C1 typed convention and identity spine

C1 implemented the adapter-only formal spine in
`src/deuteron_wigner/formal/`: eight transverse coordinate identities,
rank/mass/Bessel/phase metadata, versioned sector identity, Wilson paths and
ordered gluon f/d link identities, operation-aware decorated operator
identity, five distinct map classes, explicit adapter composition, and
structured fail-closed diagnostics. The accepted numerical implementation and
writers were not changed.

Final status: 498/498 tests, all nine acceptance/report builders, 36/36
evidence rows, and 162/162 atlas pages pass. All eight authoritative
parent/correlator files remain byte-identical to the C0 hashes. C1 manifests
and API/report documentation are under `docs/next_level/c1_*`.

Honest limitations: the requested Volume I source file is absent; private
helpers behind adapters still use arrays/scalar `b`; specialized transforms
are wrapped rather than rewritten; the provenance exclusion graph is deferred.

Exact next job: **C2 native typed reduction and provenance-graph migration of
the accepted boundary**. Replace adapter-only projection/composition
boundaries with native typed `RED` maps and enforce baseline/additive/
exclusive/replacement relations, retaining byte-identical regression. Do not
introduce a microscopic Hamiltonian in C2.

## 2026-07-28 — C0 next-level architecture audit

Work Package C0 audited the accepted leading-twist forward quark/gluon model
against the construction note, algebraic/geometric architecture note, and
original GTMD-first formalism. The immutable regression baseline at commit
`69501009d9a972dd90cd63736d6bf1fc9669877d` is clean: 484/484 tests, every
documented acceptance builder, 36/36 evidence rows, and all 162 atlas pages
pass. Parent hashes and accepted residuals/minima are frozen in
`docs/next_level/stage0_regression_baseline.json`.

Unresolved ambiguities are generic radial `b` across `bDelta`, `bTMD`, and
nuclear impact space; raw nuclear/process transverse coordinates; rank and
mass normalization absent from correlator identity; and operator decorations
split among correlators, registries, schemes, provenance, and CSV labels.
Amp/Dens/Match/Red/Proc physics exists without separate typed interfaces.
Gluon path-pair and f/d color identity remains outer metadata.

Exact next job: **C1 typed convention and identity spine**. Implement isolated
formal value objects for transverse coordinates, rank/mass conventions,
sector keys, Wilson paths, decorated operator identity, and typed map
protocols; wrap current objects without changing their execution order; add
injected coordinate/sign/rank/scheme/color/double-counting failures; and prove
all authoritative hashes remain identical. See
`docs/next_level/stageA_migration_plan.md`.

Last updated: 2026-07-27

This is the persistent execution queue and completion authority. Historical
stage plans in `project_context.md` and earlier decision-log entries remain
useful context but do not override this roadmap.

## Final scientific objective

Construct a complete, physically defensible, flavor-resolved,
spin-resolved, modular, validated, and extensible leading-twist spin-1
light-front GTMD/TMD model. It must combine the best-supported nucleon
flavor, spin, OAM and spin--orbit information with realistic deuteron
light-front wave functions, vector/tensor target structure, controlled
nuclear mechanisms, gauge-link behavior, evolution, lattice and
phenomenological inputs, and machine-readable provenance.

Completion is parent-first:

\[
\Psi_D^{\rm LF}\to\rho^{N/D}\to W_{a/N}^{[\Gamma]}
\to W_{a/D}^{[\Gamma]}\to\Phi_{a/D}^{[\Gamma]}\to F_{a/D}.
\]

No downstream completion ansatz may substitute for a missing arrow.

## Model-class boundary and next-level scientific objective

The accepted pre-evolution model is a carefully constrained,
parent-consistent phenomenological synthesis.  It is not a fundamental
prediction from one solved quark--gluon--nuclear state.  This distinction is
governed by Section 15 of `references/model_construction_note.tex`.
`references/algebraic_geometric_next_level_model_note.tex` develops a
candidate WP13 architecture: graded light-front Hilbert spaces and
representation intertwiners, a symmetry-preserving tensor-network
realization, Wilson-line bundle/path-groupoid geometry, common GTMD
reduction maps, symplectic OAM organization, convex correlator positivity,
filtered truncation convergence, and a limited chain-complex
double-counting audit.  It is a research formulation, not evidence that
these microscopic dynamics have already been implemented.

Complete evolution of the accepted boundary remains the next executable
production task, but evolution must not be represented as converting that
boundary into the genuinely predictive model.  The subsequent microscopic
program is **WP13**:

1. Specify and renormalize one light-front Hamiltonian (or demonstrably
   equivalent microscopic bound-state framework), including regulator,
   counterterms, zero-mode treatment, and convergence controls.
2. Solve flavor-resolved nucleon Fock sectors containing at least the
   valence, explicit-gluon, and sea-generating sectors needed by the declared
   quark, antiquark, and gluon observables.
3. Generate nonzero-transfer GTMD matrix elements and obtain TMDs, GPDs,
   form factors, currents, and OAM reductions from the same amplitudes.
4. Generate process-dependent naive-T-odd phases from explicit Wilson-line
   interactions, with quark flavor and gluon \(f\)-/\(d\)-color structures
   derived rather than independently assigned.
5. Construct the spin-1 state with normalized \(NN\), \(NN\pi\), and any
   retained non-nucleonic Fock sectors, together with consistent one- and
   many-body currents and no-double-counting rules.
6. Match the regulated calculation to a declared QCD TMD scheme and perform
   coupled rank-, flavor-, and color-aware evolution and \(W+Y\) assembly.
7. Infer a compact set of shared Hamiltonian/state parameters with correlated
   uncertainties; independent normalization parameters for each TMD are
   forbidden.
8. Predict at least one withheld observable family and require failure to
   revise or reject the microscopic model rather than add a plot-level
   coefficient.

WP13 completion requires all twelve acceptance criteria in Section 15.10 of
the construction note, including explicit Fock/regulator convergence,
current and sum-rule closure, Wilson-line sign/color tests, posterior
predictive covariance, and withheld validation.  Until those gates pass,
outputs must be called phenomenological or effective-model predictions with
their evidence class, not fundamental predictions.

## WP10 — Required rich spin-1 dynamical structure

Status: **complete; seven WP10 gates verified by the machine-readable audit**

The 334-test, 10/10 report is the accepted baseline for the earlier
fitted-input/configurable-boundary scope. It is not completion evidence for
this expanded work package.

### WP10.1 — Gauge-link phase and quark T-odd boundary

Status: **complete**

- Retain BPV20's 500-member, process-labeled quark Sivers input.
- Add a common typed phase/amplitude contract that distinguishes a fitted TMD
  from a modeled eikonal phase and refuses mixed-link extrapolation.
- Add flavor-resolved Boer--Mulders central values and covariance/sensitivity
  from a published fit or a clearly labeled spectator/lensing model when no
  sufficiently complete fit is available.
- Propagate both functions through proton/neutron-separated LF parents for
  future and past staples.
- Generate the spin-1-only axial tensor \(g_{1LT}\) and \(g_{1TT}\)
  structures both from independent positivity-bounded phases and from an
  explicit screened one-gluon S--P/S--D/P--P rescattering calculation.

Gate: nonzero fixtures reproduce their source convention; SIDIS/DY reversal
is exact; mixed links fail closed; no Sivers/Boer--Mulders value is generated
by a universal phase shared across operators or flavors; every ensemble
member retains identity through projection. The axial tensor additions must
also pass full \(6\times6\) positivity without eigenvalue clipping, rotation
covariance, phase-zero and pure-S limits, and eikonal quadrature convergence.

### WP10.2 — Pretzelosity and worm gears

Status: **complete within the declared fit/model boundary**

- Replace the universal signed pretzelosity fraction as the sole production
  representation with flavor-dependent fit/lattice/model inputs and a
  covariance or named-scenario ensemble.
- Keep \(g_{1T}\) and \(h_{1L}^{\perp}\) separate. Retain WW as a controlled
  limit and implement configurable genuine quark--gluon--quark breaking.
- Propagate common fit identities where quantities share an input.

Gate: nonzero replacement tables round-trip, WW is recovered at zero
breaking, breaking members are distinguishable, all flavors and nucleons are
separate, rank-one/rank-two transforms pass convergence, and correlated full
density members enter the positivity audit.

### WP10.3 — Gluon T-odd color structures

Status: **complete; six rank-resolved f/d model boundaries implemented**

- Preserve independent \(f^{abc}\) and \(d^{abc}\) Sivers structures.
- Extend the same color/link contract to every leading-twist gluon T-odd
  function for which the declared operator basis permits a boundary.
- Supply sourced or explicitly modeled numerical inputs with independent
  parameters and uncertainties; observable assembly must provide its own
  hard color weights.

Gate: independent f/d variation changes observables according to analytic
hard weights; future/past reversal and mixed-link refusal pass; the full
\((3,3,2,2)\) parent remains Hermitian and member-level positivity tensions
are reported without clipping.

### WP10.4 — Polarized and tensor shadowing

Status: **complete within named H1/FGS-anchored response scenarios**

- Implement separate vector, tensor-LL/LT/TT, quark, antiquark, and gluon
  diffractive response interfaces with explicit helicity matrices.
- Use published diffractive/nuclear information where available and named
  model responses elsewhere; never copy an unpolarized factor silently.
- Link antishadowing only to the applicable spin-weighted sum rule.

Gate: U-only input leaves all polarized blocks unchanged; each polarized or
tensor response modifies only its declared irreducible target block; zero
response recovers impulse; Hermiticity, gauge-link parity, positivity, and
applicable tensor moments pass.

### WP10.5 — Mesonic and non-nucleonic correlators

Status: **complete within sourced pion and effective-cluster boundaries**

- Promote the sourced Sullivan pion contribution to an unintegrated
  flavor/spin-resolved correlator only to the degree fixed by the NNπ
  amplitude and pion TMD input; refuse invented off-forward or helicity
  structure.
- Retain Miller six-quark \(b_1\) and the cluster scenario as observable
  sensitivities until a source fixes their missing flavor/color/TMD
  decomposition.
- Implement replaceable full-correlator inputs for future NNπ, hidden-color,
  dibaryon, or other non-nucleonic amplitudes.

Gate: the pion correlator reduces to the existing collinear Sullivan result
at \(b_T=0\), closes its Fock normalization and momentum accounting, and
preserves flavor; observable-only sources cannot be mislabeled as full
parents; zero-component limits are exact.

### WP10.6 — Additional spin--orbit/OAM interference

Status: **complete within the explicit PDF-anchored S/P/D scenario**

- Enumerate the independent LF helicity/OAM interference amplitudes needed
  beyond S/D/Melosh impulse recoupling.
- Add typed partial-wave amplitude inputs with azimuthal phase and
  interference identity, including quark--gluon and gluon--gluon correlation
  channels when modeled.
- Map every new amplitude to named correlator entries rather than downstream
  TMD priors.

Gate: rotations, parity, Hermiticity, OAM selection rules, and controlled
phase-zero limits pass analytically and numerically; interference terms
vanish when either participating amplitude is disabled; no double counting
with the existing S/D components occurs.

### WP10.7 — Production, uncertainty, and acceptance

Status: **complete**

- Regenerate smooth \(F(x=0.1,k_T;Q=5\,{\rm GeV})\) quark and gluon atlases
  with structural, configured-baseline, and unresolved zeros visibly
  distinguished.
- Export separate fit, lattice, phase-model, wave-function, shadowing,
  mesonic/non-nucleonic, OAM, evolution, and numerical axes.
- Add WP10 evidence to both machine-readable acceptance manifests.

Gate: all WP10.1--WP10.6 gates pass; production rows retain source,
flavor/nucleon, operator, color structure, link, mechanism, amplitude,
validity, and member identity; visual audit passes; full regression passes;
neither final report claims completion while a required WP10 entry is
partial or missing.

## Status vocabulary

- **complete**: implemented, tested, documented, and passes its stated gate.
- **partial**: useful implementation exists but required physics or tests remain.
- **temporary**: explicit replaceable approximation with a replacement task.
- **missing**: required implementation does not yet exist.
- **blocked-external**: requires unavailable access or information; none currently.

## WP1 — Audit and production gates

Status: **complete**

Implemented:

- Audited 28 simplifications and false completion assumptions in
  `references/production_tmd_architecture_audit.md`.
- Marked reduced-amplitude outputs and documents as superseded.
- Added `provenance.py` with exact, phenomenological, lattice-informed,
  model-dependent, and unconstrained evidence classes plus validity domains.
- Added fail-closed trace checks for unconstrained components.

Gate:

- Every future output row must trace operator, flavor, active nucleon,
  wave function, mechanism, gauge link, evidence class, validity, and
  uncertainty. Exporters fail if required trace fields are absent.

Tests:

- `tests/test_provenance.py`

## WP2 — Complete declared leading-twist content and conventions

Status: **complete at the declared leading-twist scope**

Complete:

- Enumerated 18 quark, 18 antiquark, and 19 gluon TMDs across
  \(U,L,T,LL,LT,TT\).
- Stored transverse rank, T parity, operator projection, collinear status,
  and positivity block in `registry.py`.
- Implemented symmetric-traceless ranks through four.
- Implemented full gluon Cartesian basis and synthetic projectors, including
  the TT \(f_{1TT}-h_{1TT}^{\perp}\) identifiability relation.
- Implemented the published 18-function spin-1 quark basis and joint
  Gram/design projector in `quark_correlator.py`.
- Independently mapped every quark structure to Eqs. (12)--(20) of
  arXiv:1612.06585 and added direct scalar/chiral-odd contraction tests.
- Added an all-18 light-front parity reflection and the full nine-function
  T-odd gauge-link reversal test. This found and fixed a missing epsilon
  rotation in rank-three \(h_{1TT}^{\perp}\).
- Resolved the fixed-\(k_T\) gluon TT degeneracy by exposing only
  `f1TT_minus_h1TTperp`; no artificial prior separates the pair.

Gate:

- Analytic and independent numerical construction agree for every basis
  tensor and projector to \(10^{-11}\); origin degeneracies are explicit.

## WP3 — Flavor-resolved spin-half nucleon correlators

Status: **complete at the declared fitted-input plus configurable-model scope**

Complete:

- Added the eight leading-twist spin-half quark TMD operator structures in
  `nucleon_quark_correlator.py`.
- Preserved distinct \(u,d,\bar u,\bar d\) functions and widths.
- Added separate proton/neutron models with controlled charge-symmetry
  rotation in `nucleon_inputs.py`.
- Added CT18 \(f_1\), BDSSV24 \(g_1\), bounded flavor-dependent \(h_1\)
  normalized to JAMDiFF phenomenology+lattice tensor charges, WW
  \(g_{1T}\) and \(h_{1L}^{\perp}\), and explicit zero one-body
  T-odd/pretzelosity boundaries.
- Tested flavor distinction, process sign behavior, hermiticity, the exact
  charge-symmetric inclusive limit, the complete joint-spin positivity matrix
  over the declared support grid, valence moments, and tensor charges.

Model-dependent inputs and replacement interfaces:

| Configured input | Classification | Upgrade path | Distinguishing test |
|---|---|---|---|
| Flavor-dependent Gaussian \(f_1\) widths | model informed by arXiv:2405.13833 | ingest a tabulated soft-subtracted flavor-dependent TMD fit with covariance | table interpolation and covariance reproduction |
| JAMDiFF pointwise mean/std grid with composed-TMD positivity projection | phenomenology+lattice fit; model-dependent compatibility projection | retain and propagate individual replicas | reproduce cross-x/flavor covariance and nuclear output bands replica by replica |
| WW \(g_{1T},h_{1L}^{\perp}\) | model dependent | add fitted/lattice inputs and genuine twist-3-breaking parameter | WW limit plus nonzero replacement fixture |
| BPV20 Sivers plus flavor-dependent Boer--Mulders proportionality | fit plus independent model coefficient axis | replace Boer--Mulders coefficients with a joint fit ensemble | SIDIS/DY reversal, coefficient scenarios, and nonzero parent projection |
| Flavor-dependent positivity-ceiling pretzelosity | model dependent | replace with fit/lattice replicas when public | nonzero replacement round trip, flavor distinction, and positivity |

Completion evidence and remaining data-driven upgrades:

1. **Complete at the fitted-input/WW scope:** the official JAMDiFF LHAPDF member 0 central and physical
   members 1--968 are now ingested with stable identity. Cross-x/flavor
   covariance is propagated member by member through the six-wave nuclear
   \(h_1\) convolution, including the documented member-wise composed TMD
   Soffer projection. The same identities also pass through the derived WW
   \(h_{1L}^{\perp}\) integral and LF parent rather than receiving an
   independent band. Genuine twist-3 WW-breaking remains a separate model
   uncertainty.
2. **Complete at declared LO/rank-aware plus fit-native scope:** an explicit
   LO rank-zero quark boundary covers flavor-
   resolved \(f_1,g_1,h_1\), using the exact Fourier transform of each
   component's intrinsic Gaussian and quark one-loop CSS coefficients
   \(A_q^{(1)}=C_F,\ B_q^{(1)}=-3C_F/2\). The API rejects rank-one, rank-two,
   fit-native, and T-odd inputs rather than applying the wrong transform.
   A cached numerical \(J_0\) adapter now reconstructs complete spin-half
   correlators at the recoil-shifted momentum inside the LF parent. A
   physical AV18 four-flavor connection audit passes 201-to-401 point
   b-grid refinement at \(1.62\times10^{-5}\) maximum mixed relative change.
   AV18 medium-to-production LF convergence passes at 0.541%, and all six
   production wave functions yield finite flavor/nucleon-resolved results.
   The rank-one \(g_{1T},h_{1L}^{\perp}\) correlator coefficients now use the
   proper \(J_1\) inversion and pass 25-to-49 canonical-scale-grid refinement
   at \(1.06\times10^{-7}\) for both nucleons and four flavors.
   The rank-two \(h_{1T}^{\perp}\) adapter now evolves the physical
   directional coefficient and inverts with \(J_2\). Its perturbative central
   remains zero, while signed \(\pm0.25\) moment-bound large-b scenarios are
   explicit, replaceable, and pass full nucleon joint-density positivity.
   A disk-backed fixed-\(Q\) grid now contains proton/neutron,
   \(u,d,\bar u,\bar d\), all six evolved T-even nucleon components, and
   three pretzelosity scenarios on 274 x and 161 momentum nodes. It passes
   576 direct-transform comparisons under the 2% or
   \(2\times10^{-6}\ {\rm GeV}^{-2}\) mixed gate. All three scenarios have
   been propagated through all six production LF parents at five momenta;
   the 19,440-row output retains all 18 spin-1 projections and separate
   proton/neutron pieces with \(7.58\times10^{-14}\ {\rm GeV}^{-2}\) closure.
   All 1,080 stored wave/scenario/flavor/momentum/part densities pass the
   complete joint spin-density eigenvalue gate; the minimum is 0.0388.
   A visually verified 18-page atlas and 21,672-row smooth table retain
   separate scenario and wave-function envelopes plus proton/neutron curves.
   BPV20 fit-native routing and process-domain enforcement are now complete.
   NLO coefficient functions remain an order upgrade, not a missing model
   interface; the declared in-house generic boundary is LO and fit-native
   routes retain their published orders.

Gate:

- Proton and neutron benchmarks reproduce source inputs and uncertainty;
  all eight operator structures satisfy hermiticity, T parity, positivity,
  support, and declared moments.

## WP4 — Parent light-front nuclear convolution and projection

Status: **complete at the declared TMD plus replaceable rank-zero off-forward
nucleon-GTMD boundary scope**

Complete:

- Existing realistic AV18, CD-Bonn, and four Norfolk momentum wave functions.
- Existing Melosh-rotated retained target/nucleon helicity spectral kernel.
- Existing \(SS,SD,DS,DD\) off-forward component quadratures.
- Added proton/neutron-separated quark convolution in
  `gtmd_convolution.py`.
- Added one-pass convolution of all quark operator projections and complete
  spin-1 projection in `parent_quark_tmd.py`.
- Added pure-S spin-transfer test preventing transversity/pretzelosity
  misidentification.
- Added `export_parent_derived_quark_tmds.py`; a 9-point AV18 fixture has
  passed parent/proton/neutron/mechanism/process/origin/azimuth validation.
- Completed the AV18 \(8\times6\times6\), \(16\times12\times8\), and
  \(24\times16\times12\) comparison.  The coarse fixture is unsuitable for
  physics (24.9% L2 shift to medium); medium differs from fine by 0.46% in
  L2 and at most 0.68% for resolved p/n impulse values.
- Completed the full six-wave \(16\times12\times8\),
  \(24\times16\times12\), and \(32\times20\times16\) audit. Medium fails
  with up to 1.283% relative L2 error. Fine passes against ultrafine with at
  most 0.5653% relative L2 error and the documented 2% plus
  \(2\times10^{-8}\ {\rm GeV}^{-2}\) mixed pointwise tolerance. The
  \(24\times16\times12\) grid is now the production default.
- Added the complete identifiable gluon TT parent projector and retained
  proton/neutron gluon convolution components.
- Added matched/CSS-evolved nucleon gluon inputs and complete parent-derived
  gluon export for all six wave functions.
- Quark and gluon outputs now retain coherent \(SS,SD,DS,DD\) components.
  Validators require their reconstruction of the full impulse correlator.
- Generated smooth PCHIP visualization layers (241 points) with AV18 central
  curves and six-wave-function envelopes; all calculated knots remain
  available and interpolation is explicitly not new physics.
- Verified the gluon \(b_T=0\) parent reduction against an independently
  constructed LF collinear convolution for all six wave functions. \(f_1\)
  agrees at machine precision and \(f_{1LL}\) within \(1.7\times10^{-11}\)
  relative; the collinear one-body \(h_{1TT}\) null is structural.
- Exported the unprojected parent correlators for all six production quark
  and gluon datasets as portable complex long tables. Independent
  deserialization and projection reproduces every named output within
  \(2\times10^{-11}\ {\rm GeV}^{-2}\); unit tests also cover exact matrix
  round trips and incomplete-table rejection.
- Completed a production-order azimuthal-covariance audit of the full quark
  parent projection using a complete covariant spin-half fixture convolved
  through the physical AV18 LF kernel. Across all 18 spin-1 TMDs and three
  transverse momenta, the largest resolved relative rotation residual is
  \(2.12\times10^{-9}\) at the production \(24\times16\times12\) order and
  \(2.50\times10^{-11}\) after doubling the internal azimuthal order. Both
  are far below the predeclared 1% and 0.25% acceptance limits.
- Extended the independent production \(b_T=0\) reduction audit to all six
  wave functions, \(x_N=0.03,0.1,0.3\), \(Q=2,5\) GeV, \(u,d,\bar u,\bar d\),
  and gluons at the production quadrature. The full retained-helicity parent
  and separately constructed spherical LF smearing agree in \(f_1\) to
  \(2.56\times10^{-14}\) relative. Tensor \(f_{1LL}\) passes a strict mixed
  \(10^{-9}\) relative or \(10^{-12}\ {\rm GeV}^{-2}\) absolute criterion,
  and forbidden quark \(h_{1LT}\) rank-zero leakage is below
  \(3.84\times10^{-20}\ {\rm GeV}^{-2}\).

Model-boundary upgrade:

1. Retain the older factorized-Gaussian GTMD/GPD/PDF/Wigner commuting test
   as a separate analytic benchmark. The physical six-wave LF overlap now
   passes GTMD-to-forward-TMD, GTMD-to-GPD, GTMD-to-Wigner, Hermiticity, and
   \(SS+SD+DS+DD\) closure in
   `physical_offforward_reductions.json`. A future fitted nucleon
   off-forward GTMD can replace the declared rank-zero boundary through the
   existing callback without changing nuclear composition.

Gate:

- All requested flavors and species are projected from stored/inspectable
  parent correlators; proton+neutron and mechanism sums reconstruct exactly;
  six-wave-function and quadrature convergence are documented.

## WP5 — Nuclear mechanisms and regimes

Status: **complete at the sourced-mechanism/configurable-zero scope**

Complete:

- Binding, Fermi motion, Melosh rotation, \(S/D\) structure, and interference
  enter through the LF wave function.
- `nuclear_mechanisms.py` adds separate correlator-level coherent
  shadowing, antishadowing, and EMC-like sensitivity components without
  altering impulse terms.
- Mechanisms preserve irreducible spin-1 target sectors and hermiticity.
- The LF spectral kernel now stores the invariant struck-nucleon virtuality
  \(v=(p^2-m_N^2)/m_N^2\) at every node using an on-shell spectator and the
  physical deuteron mass. The off-shell response is integrated inside the
  quark convolution and exported as a separate parent; the former universal
  average-virtuality multiplier is disabled.
- Across the six production wave functions the spectral mean virtuality is
  -0.0369 to -0.0448 and the \(v<-0.3\) weight is 1.18--2.17%. Production
  positivity and fine/ultrafine convergence pass with the explicit response.
- Replaced the qualitative off-shell response by the May 2026 CJ26 cubic
  fit. The central is the midpoint of its additive/multiplicative
  higher-twist scenarios; uncertainty retains their half-range and the
  published marginal coefficient errors. The adapter enforces/documented
  provenance and marks \(x>0.7\) as extrapolative.
- Added source-required meson-exchange and non-nucleonic parent interfaces.
  Their production rows and serialized matrices are explicit zeros in the
  configured nucleonic baseline, labeled as unresolved rather than physical
  null predictions. Tests cover sourced activation, validity-domain
  deactivation, hermiticity, and exact total reconstruction.

Implemented limitations and data-driven upgrade paths:

1. **Complete at the named central/scenario-envelope scope:** the analytic
   central shadowing curve has been replaced by the
   official H1 2007 Jets DPDF grids, reconstructed differential flux, FGS
   deuteron double-scattering integral, real-part correction, \(16\pi\)
   convention conversion, and wave-specific LF body form factor. Named DPDF
   normalization and \(t\)-slope scenarios are implemented. H1 eigenvector
   grids, gluon-specific slope covariance, and polarized/tensor DPDFs remain
   unavailable/unresolved. The named responses are exported coherently over
   wave function, flavor, \(x\), and \(Q\); they are explicitly an envelope,
   not a statistical covariance. Rows below \(x=10^{-4}\) are marked as H1
   beta-boundary-clamped diagnostic extrapolations.
2. Obtain full CJ26 coefficient covariance/Hessian members if released.
   Production already uses the versioned fitted central scenarios and
   marginal errors; the absent cross-coefficient covariance remains an
   explicitly incomplete statistical input rather than a central-model
   placeholder.
3. **Complete as a separately gated sourced comparison mechanism:** the
   Miller (2014) AV18 tensor-polarized Sullivan-pion
   distribution is evaluated numerically and convolved with all 786 JAM21
   pion replicas. Its pure-tensor correlator adapter, \(M_A\) variation,
   sum-rule/convergence tests, exact zero-meson limit, and HERMES \(b_1\)
   comparison are complete. The individual source helicity formulas now
   supply a separately tested spin-averaged connected pion distribution.
   Exact \(Z=1+N_\pi\) normalization gives NN/NNπ probabilities
   0.97915/0.02085 and closes momentum among NN nucleons, NNπ nucleons, and
   pions to machine precision. The minimal unchanged-shape NNπ-nucleon
   counterterm remains only a comparison diagnostic.  The preferred
   collinear component applies the conditional recoil
   \(\alpha_N'=(1-yM_N/M_D)\alpha_N\) to arbitrary-\(x\) full quark
   correlators; nucleon number, plus momentum, changed \(x\) shape, and
   inherited scalar-pion spin ratios are tested. The unintegrated source
   kernel and retained-NN recoil are implemented. In the repository
   convention the exact phase is
   \(J_0[x_Nbq_T/(2(1-\eta_\pi))]\); the active residual-NN fraction cancels.
   The Vpion19 central plus 100 physical profile replicas are
   composed with the unintegrated nuclear pion recoil via
   \(J_0(zbq_T)\), with exact collinear reduction and common Fock
   normalization. Every profile member is propagated through the nuclear
   kernel and combined with the retained-NN term. This is a b-space
   boundary. The one-loop route remains a diagnostic; a preferred native
   arTeMiDe route now uses Vpion19, NNLO matching, BSV19 NNNLO evolution,
   all 101 member identities, and the same exact recoil. Maintained JAM21
   substitutes for unavailable JAM18; this route is therefore retained as a
   non-production comparison until a refit and a specified-observable Y term
   become available. A dynamical three-body NNπ helicity, off-forward, and
   virtuality-dependent spectral amplitude has a replacement interface but
   no public numerical input.
   The Miller hidden-color six-quark \(b_1\) equation is also
   source-table/sum-rule tested as a distinct observable scenario. Its
   \(P_{6q}=0.0015\) is fitted to one HERMES bin and its flavor decomposition
   is not fixed, so it is not promoted to a correlator or used in the
   configured production total. The Kaur et al. effective-cluster LFWF
   supplies a
   separately validated non-nucleonic comparison parent and source-defined
   flavor-resolved collinear convolution, including its published \(b_1\)
   moment. It remains non-production because its color mixture, transverse
   cluster-parton structure, evolution, and physical-binding connection are
   not fixed.
4. **Complete at the sourced unpolarized QED-CSB scope:** a source-required,
   validity-bounded `ChargeSymmetryBreakingInput` applies independent
   relative corrections by nucleon, flavor, and TMD while retaining exact
   isospin as a tested switchable limit. The paired MSHT20 QED
   proton/neutron Hessian ensembles now supply a numerical neutron \(f_1\)
   correction and correlated 68% CL uncertainty for
   \(10^{-5}\le x\le0.4\). The central correction is propagated through all
   six evolved LF parents with exact proton/neutron mechanism closure. All
   77 paired members are propagated through shared LF contractions and form
   the correlated 38-pair parent Hessian. Polarized, transversity, T-odd, and
   transverse-width CSB remain unresolved and are intentionally not inferred
   from unpolarized amplitude CSB.
5. Tensor coherent terms are kept separate and compared with \(b_1\);
   polarized/tensor DPDF inputs remain an external data upgrade and are not
   absorbed into unrelated mechanisms.

Gate:

- Each mechanism has a source, regime, independent switch, uncertainty,
  limiting test, and correlator-level contribution; mechanisms reconstruct
  observables without double counting.

## WP6 — Gauge links, factorization, and evolution

Status: **complete at the declared typed-scheme and validity-enforcement scope**

Complete:

- Gauge-link identity is stored; exact T-odd reversal is tested.
- Gluon small-\(b_T\) matching and one-loop CSS evolution exist separately.

Completion evidence and upgrade paths:

1. **Complete at the enforceable in-house scheme-contract scope:** quark and
   gluon matching/evolution now share a typed Collins square-root-soft,
   delta-regulator, MSbar, zeta-prescription contract. The current solver
   explicitly supports only the canonical \(\zeta=\mu^2\) line, persists both
   scale endpoints, and refuses mismatched schemes or unsupported paths.
   An order-consistent arbitrary-two-scale
   backend with cusp/path-independence validation and fitted correlated
   nonperturbative inputs is an upgrade; fit-native arTeMiDe routes remain
   separate.
2. **Complete:** quark and gluon \(b_T\)-space boundaries are connected to
   the nuclear parent with rank-aware transforms and reduction tests.
3. **Complete at the declared BPV20 fit-uncertainty scope:** the public BPV20
   N3LO central and all 500 fitted replicas are parsed; exact arTeMiDe FNP
   boundary, N3LO evolution, native Ogata momentum transform, SIDIS/DY link
   reversal, neutron isospin map, and member-preserving nuclear convolution
   through all six wave functions are implemented and tested. Smooth 16th-
   84th percentile fit bands and a separate six-wave central envelope are
   published; member 0 remains the central and is not replaced by the replica
   mean or median.
4. **Complete at the strict boundary-contract scope:** the gluon Sivers
   interface now separates f-type and d-type color contractions, future/past
   staple reversal, and explicit process hard coefficients. It refuses mixed
   links, missing color components, implicit process weights, invalid domains,
   and nonfinite inputs. No nonzero production boundary is claimed because no
   fit-native public two-color replica input has been validated. A future
   input can activate the existing f/d-color interface and parent embedding;
   the configured unconstrained boundary remains explicit zero.
5. Scale/profile variations and the low-\(k_T\) validity cutoff are
   implemented. A fixed-order \(Y\) term is required only for a specified
   high-\(q_T\) observable and cannot be added universally to a TMD.

Gate:

- Evolution consistency, cusp relation, reference-scale recovery, process
  reversal, and high-\(k_T\) validity are tested for every evolved sector.

## WP7 — Algebraic/geometric organization and optional quantum validation

Status: **complete; algebraic organization is implemented and topology or
PennyLane has no demonstrated additional role**

Concrete implementation:

- Spin-1 density matrices use the irreducible
  \(U,L,T,LL,LT,TT\) Hermitian basis.
- Definite transverse ranks use symmetric-traceless \(SO(2)\)
  representations.
- Named projectors use Gram/design inversion with rank and condition checks.
- Provenance and mechanisms compose as typed direct-sum contributions.

Completion evidence and conditional upgrade paths:

1. **Complete:** all 500 propagated BPV20 members now pass through the complete
   spin-1 target-helicity/parton-spin eigenvalue diagnostic for six wave
   functions, both links, four flavors, and impulse/model totals. It reports
   296 tree-level PSD tensions without clipping because the soft-subtracted
   evolved TMD bound is scheme dependent and BPV20 documents this behavior.
   Equivalent member-level checks now cover every reconstructible implemented
   ensemble, including correlated JAMDiFF, gluon waves, and named shadowing.
2. **Complete:** `references/spin1_representation_map.md` maps target and
   parton Hilbert spaces, the \(U,L,T,LL,LT,TT\) irreps, \(SO(2)\) ranks,
   epsilon rotations, discrete symmetries, gauge links, gluon TT
   identifiability, direct-sum composition, and every code/test object.
3. Investigate topology only if complex gauge-link phases introduce a real
   winding, bundle, patching, or global-sign problem.
4. Use PennyLane only if a specified Hilbert-space construction supplies an
   independent entanglement/spin-coupling validation; benchmark it against
   Clebsch--Gordan algebra first.

Gate:

- Every abstract construction maps to explicit degrees of freedom,
  operators, tests, and a demonstrated computational benefit.

## WP8 — Uncertainty, validation, and benchmark observables

Status: **complete; authoritative machine-readable matrix passes**

Required validation:

- Hermiticity, parity, time reversal, gauge-link reversal.
- Support and endpoint behavior.
- Target and parton helicity-matrix positivity where applicable.
- Baryon number, momentum, helicity, tensor, and transversity moments.
- Rank-zero collinear marginals and positive-rank tensor marginals.
- \(h_{1LT}\) zero unweighted integral.
- Pure S-wave, zero-D-wave, no-Melosh, free proton, free neutron,
  exact-isospin, controlled-isospin-breaking, and zero-nuclear-correction limits.
- \(b_1\) from the same parent versus the independent convolution and HERMES.
- Gluon \(h_{1TT}\) one-body null test.
- Wave-function, internal quadrature, external grid, transform, PDF/TMD fit,
  evolution, and nuclear-mechanism uncertainties kept separate.

Gate:

- A machine-readable validation report maps every test to tolerance, result,
  input provenance, and affected outputs; the full suite passes.

Current evidence:

- `validation/wp8_manifest.json` maps all 12 grouped WP8 requirements to
  tolerances, collected test prefixes, artifacts, provenance, outputs, and
  explicit open reasons.
- `outputs/validation/wp8_acceptance_report.json` is generated by
  `scripts/build_wp8_validation_report.py`; 12/12 requirements are verified,
  331/331 tests pass, and `completion_ready=true`.
- The `global_moments` entry now uses a 69-entry support-aware ledger plus an
  11-active-parton momentum audit. Valence number and total momentum pass;
  gluon momentum/helicity/tensor moments are support complete with explicit
  operator weights and endpoint sensitivities.
- Joint positivity now covers all reconstructible implemented ensembles:
  six full gluon wave members, evolved quark scenarios, all 500 BPV20
  members, all 968 member-correlated JAMDiFF \(h_1\)/WW pairs, and
  central/low/high full-matrix gluon shadowing. Projection-only envelopes
  remain explicitly outside the claim.

## WP9 — Reproducible outputs, documentation, and completion audit

Status: **complete**

Required:

1. Produce parent-derived dimensional \(F\) curves and separate bands for
   gluon, \(u,d,\bar u,\bar d\) at the declared kinematics.
2. Store parent/mechanism/proton/neutron source tables and supplemental ratios.
3. Visually inspect all figures and retain vector PDF output.
4. Document every component’s physical meaning, source, validity, uncertainty,
   and replacement interface.
5. Provide exact environment and reproduction commands.
6. Perform a final acceptance audit mapping every criterion to files, tests,
   evidence, and documentation.

Current evidence:

- `outputs/figures/figure_index.json` is the machine-readable authority map.
- `outputs/validation/parent_tmd_figure_acceptance.json` verifies 72 quark
  groups (18 functions for each of \(u,d,\bar u,\bar d\)), 18 gluon groups,
  finite ordered six-wave bands containing AV18, and common 241-point PCHIP
  grids.
- The AV18 source audit retains distinct proton/neutron impulse rows and
  finds nonzero \(u-d\) and \(\bar u-\bar d\) source differences. Equality
  in the assembled inclusive deuteron is therefore the controlled exact
  charge-symmetric \(I=0\) limit, not a flavor-independent source ansatz.
- `quark_flavor_source_decomposition_atlas.pdf` exposes active-proton,
  active-neutron, impulse-sum, and configured-total curves on all 72
  flavor/TMD/channel pages, backed by a 241-point source table.
- The historical `outputs/figures/production_tmds/` tree is explicitly
  superseded; its old script entry point fails closed, and exploratory
  regeneration is segregated under `outputs/figures/exploratory_closure_tmds`.
- All 162 pages across the quark, gluon, and flavor-source atlases were
  rendered with PyMuPDF, structurally audited, and reviewed through contact
  sheets. Poppler was unavailable.
- `outputs/validation/final_acceptance_report.json` maps all ten final
  criteria to implementation, tests, artifacts, and documentation; 10/10
  criteria and 334/334 tests pass with `completion_ready=true`.

Gate:

- No required item in WP1--WP9 remains partial, temporary without an accepted
  declared-scope exclusion, missing, or disguised as optional future work.

## Known limitations and closed historical defects

1. The quark convention defect is closed; future changes must preserve the
   direct published-equation and light-front parity tests.
2. The six-wave quark convergence defect is closed by D-050. Production is
   \(24\times16\times12\); the failed medium and passing ultrafine comparison
   reports are retained as evidence.
3. Off-shell response is fitted to CJ26 and central unpolarized shadowing is
   an H1-DPDF/FGS coherence integral. Full DPDF statistical covariance,
   polarized/tensor diffractive inputs, and numerical mesonic/non-nucleonic
   inputs are unavailable external upgrades. They have typed replacement
   interfaces and are not inserted through unrelated responses.
4. JAMDiFF member identity and cross-x/flavor covariance are propagated
   through nuclear \(h_1\) and correlated WW \(h_{1L}^{\perp}\) for all six
   wave functions. Joint statistical uncertainty with CT18/BDSSV remains
   open because no joint probability prescription is published.
5. The matched/CSS gluon output is a low-\(k_T\) W term. A 121-point
   \(0.005<k_T<5\) GeV audit gives 14.3% and 54.3% residuals in the \(f_1\)
   and \(f_{1LL}\) full marginals. Tables and figures now enforce the W-only
   domain; a sourced Y term is required only for a specified high-\(q_T\)
   observable, not for an intrinsic TMD.
6. Serialized unprojected quark and gluon parent correlators are complete.
   The full-matrix non-impulse gluon mechanism ledger, inclusive
   target-U/gluon-trace shadowing, named diffractive uncertainty members, and
   gluon-momentum-compensating antishadowing are implemented. Numerical
   polarized/tensor shadowing, off-shell, mesonic, and non-nucleonic gluon
   inputs are unconfigured external upgrades and cannot reuse quark
   responses silently; explicit zero baselines and activation interfaces
   are tested.
7. The repository working tree is rooted above this project on the current
   machine, so broad `git status` output includes unrelated home-directory
   files. Never clean or delete them.

## Optional maintenance and data-upgrade queue

No required implementation or validation item remains. The authoritative
final audit is `outputs/validation/final_acceptance_report.json`. The
following historical queue is retained as non-required upgrade context; it
must not be interpreted as an incomplete acceptance item or permission to
invent unavailable external physics.

Continue WP5 with the missing correlator-level non-impulse gluon mechanism
layer while preserving the source boundaries of the implemented pion and
cluster scenarios:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q \
  tests/test_pion_exchange.py tests/test_nuclear_mechanisms.py
```

The sourced spin-average, momentum ledger, non-Gaussian transverse boundary,
exact Fock ledger, conditional longitudinal NNπ recoil, and retained-NN
\(b\)-space recoil kernel are complete. The unchanged-shape closure is only
a comparison diagnostic. Native NNLO/NNNLO
Vpion19 evolution now supersedes the one-loop route, but its JAM21
substitution still requires a refit and a fixed-order Y term. Next supply
that refit/Y term.  The production AV18 multi-\(x\) parent grid, conditional
recoil propagation, log-\(x\) interpolation, and coarse/refined validation
are complete. All 786 JAM21 replicas now provide the pion-PDF ensemble mean,
sample spread, quantiles, and member table. The former instruction to expose
or average the active-nucleon LF fraction is superseded. The forward coupling
is complete:
\(z\alpha=x_N/[2(1-\eta_\pi)]\) cancels \(\alpha\) exactly and passes the
AV18 b=0 parent gate. The common native Vpion19 plus retained-NN output is
complete with consistent Fock normalization and all 100 physical profile
members propagated through the nuclear kernel. Extend the mechanism off
forward; do not manufacture the still-unsourced tensor-pion transverse input.
The 2026 LFHEFT audit confirms that its deuteron benchmark integrates the
scalar NNπ sector into an effective two-body Hamiltonian and explicitly
leaves dynamical pions for future work. Preserve the three-body replacement
interface and continue independent acceptance work rather than adding an
arbitrary transfer slope.
Implement separate gluon-sector mechanism responses and uncertainty members;
do not apply quark factors by default. Each mechanism must preserve the full
\((3,3,2,2)\) correlator, reconstruct the total from named contributions,
and pass Hermiticity, zero-switch, validity, and no-double-counting tests.
For the non-nucleonic parent, do not promote arXiv:2507.09886 to a quantified
hidden-color mixture. Its scalar holographic × 't Hooft parent and exact
zero-tensor Melosh diagnostic are implemented. The explicit vector-current
helicity vertex now passes nonzero-local/zero-integrated tensor,
polarization-completeness, and official LMDF-path benchmarks. Keep it gated
as a cluster sensitivity scenario. Its source-defined NNPDF3.1
proton/neutron/flavor convolution now reproduces the published \(b_1\)
moment, but a sourced transverse cluster-parton input, color decomposition,
and matching/evolution prescription remain required before production TMD
use. In parallel seek
released helicity/color-resolved BLFQ amplitudes from
arXiv:2503.21371/2505.12889 or reproduce their Hamiltonian truncation.
Do not infer a Gaussian width. The Miller six-quark observable
scenario is implemented with its one-bin calibration exposed; next seek a
source that fixes a flavor-resolved non-nucleonic correlator. The SIDIS
high-qT gate remains closed:
APFEL++ and the vendored arTeMiDe do not supply the required qT-differential
FO/ASY pair.

## 2026-07-26 gluon T-odd replacement checkpoint

The six-function source-informed replacement is complete at its declared
prediction scope. All functions are nonzero away from their rank boundary,
f/d link classes and coupling axes are distinct, AV18 tensor dynamics
generates \(g_{1LT}\) and \(g_{1TT}\), and the complete density passes
positivity. A literal PVGlue20 replica reproduction and fitted
\(Q_0\)-to-\(Q\) evolution remain outside the evidence because neither the
replica files nor a dedicated evolution fit are public. This absence is
recorded as model uncertainty and is not represented as a confidence band.

## WP11 — Canonical quark/gluon physical synthesis

Status: **completed at the declared leading-twist forward scope; governing
acceptance passed 2026-07-26**

WP11 is not an optional upgrade to an otherwise completed project. It is the
project's governing objective: deliver a fully self-consistent canonical
quark--gluon model containing as much physically known richness and every
realistically supported contribution, without double counting, silent
omission, or artificial enhancement. Earlier WP8/WP10 completion reports
certify components and tests only.

The detailed evidence and completion conditions are in
`references/overall_quark_gluon_consistency_audit.md`. Execute in this order:

1. **C1 contribution graph:** encode baseline/additive/alternative/member
   relationships and test that every canonical TMD has one non-overlapping
   composition path.
2. **C2 common scheme/evolution — completed:** attach initial scale, subtraction scheme,
   rapidity convention, matching order, transverse rank, and Q=5 route to
   every canonical input; comparison-only inputs fail canonical export. The
   typed ledger has no unresolved canonical route, and the Yang-2024 moment
   now enters the validated common rank-one J1/CSS adapter rather than a
   frozen or WW substitute.
3. **C3 nucleon gluon T-odd — completed:** use the project's own spin-half
   gluon light-front overlap and screened adjoint Wilson-line harmonics to
   generate the complete nucleon T-odd input, with independent \(f/d\)
   sectors and the common evolved T-even parent. The published spectator
   construction is an independent limiting-case benchmark, not the
   canonical parent. Evidence:
   `src/deuteron_wigner/gluon_lfwf_todd.py`,
   `outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.csv`, and
   `tests/test_canonical_gluon_lfwf_todd_production.py`.
4. **C4 spin-1 tensor T-odd — completed for the forward AV18 impulse
   boundary:** generate \(g_{1LT}\), \(g_{1TT}\) by applying rank-one LT and
   rank-two TT spin-one irreducible Wilson-line phases to the retained
   target-helicity \(SS/SD/DS/DD\) parent before projection. Link reversal,
   pure-S, no-phase, wave closure, Hermiticity, positivity, and
   forbidden-subspace residuals are tested. CD-Bonn/wave-function variation
   belongs to C6 uncertainty propagation.
5. **C5 quark model calibration — completed:** separate evidence-backed central inputs
   from zero-centered or multi-model sensitivities for Boer--Mulders,
   pretzelosity, WW breaking, and tensor phases.
6. **C6 nuclear propagation — completed:** apply off-shell, shadowing, antishadowing,
   pion, and cluster mechanisms only to supported operator channels and
   close number, momentum, and tensor ledgers without double counting.
7. **C7 observable validation — completed:** assemble process-specific hard/color
   weights and validate compatible sets against PDFs, \(b_1\), SIDIS/DY,
   lattice ratios/moments, and prospective gluon observables.

Acceptance: a machine-readable canonical contribution graph; one common
scheme-aware export; full parent-chain provenance for every row; no
downstream completion amplitudes; separated statistical/model/numerical
uncertainties; and observable-level residual tests. The previous WP8/WP10
reports remain valid component tests but do not close WP11 by themselves.
The governing evidence is
`outputs/validation/wp11_final_acceptance.json`, generated by
`scripts/build_wp11_final_audit.py`. It maps all C1--C7 gates to artifacts
and tests. The acceptance run passes 433 tests. The two 18-page canonical
atlases and their numerical band tables are under `output/pdf/` and
`outputs/parent_tmds/canonical/`.

## WP12 — Complete canonical parent enrichment before external constraints

Status: **items 1--5 structurally inspected; physics-evidence parity gate
open; item 6 is not authorized**

The user requires items 1--5 below to apply to every TMD through shared
quark, antiquark, and gluon parent correlators. A function-specific repair is
not acceptance. Complete WP12 before starting the external-constraint/global
comparison program (item 6).

1. **All-TMD multi-kinematic production:** export every declared quark and
   gluon projection over common \(x,k_T,Q\) grids, with flavor/link/color and
   mechanism identity, named uncertainty axes, smooth central curves, and
   parent/projection closure at every sampled point.
2. **Wilson-line enrichment:** replace single effective phase coefficients
   by an exponentiated channel decomposition with quark--spectator,
   gluon--spectator, \(S\)-\(P\), \(S\)-\(D\), and \(P\)-\(P\) terms,
   correlated parameter members, exact link reversal, and density-spectrum
   preservation.
3. **Shared nucleon Fock/OAM parent:** represent scalar-spectator,
   axial-spectator, \(L_z=0,\pm1,\pm2\), and explicit quark--gluon sectors in
   one amplitude ledger. Coupled TMDs must be projections of shared
   interference bilinears rather than independently shaped functions.
4. **Non-nucleonic transverse parents:** provide normalized,
   flavor/color/spin-resolved and replaceable \(NN\pi\), \(\Delta\Delta\),
   hidden-color six-quark, and SRC correlator interfaces. Unsupported
   central probabilities remain zero; nonzero members are explicitly
   sensitivity scenarios with momentum/Fock ledgers.
5. **Operator-valued nuclear responses:** shadowing, antishadowing,
   off-shell, mesonic, and SRC effects act through Hermiticity-preserving
   maps on vector, axial, and transverse target-density blocks. Scalar
   reweighting remains only the controlled identity-map limit.

Acceptance requires module-level analytic limits, complete-basis tests,
Hermiticity/positivity, link reversal, flavor/color traceability,
Fock/momentum closure, no-double-counting graph checks, multi-kinematic
finite-value and smoothness audits, regenerated canonical artifacts, and a
machine-readable WP12 audit. Items 1--5 now pass that audit at the explicitly
declared leading-twist forward \(Q=5\) GeV boundary on
\(x_N=\{0.02,0.05,0.10,0.20,0.40\}\). Evidence is
`outputs/validation/wp12_items1_5_acceptance.json`. The central quark and
gluon ledgers contain every declared TMD; correlated Wilson, shared-Fock,
non-nucleonic, and completely-positive nuclear-response families cover the
same five \(x_N\) nodes. Complete rank-aware multi-\(Q\) evolution remains
item 6. The requested scientific checkpoint now passes all ten gates in
`outputs/validation/wp12_scientific_inspection.json`. Evolution must consume
the resolved `wp12_resolved_quark_parent*` and
`wp12_resolved_gluon_parent*` TMD/correlator ledgers, preserving all
constituent and nuclear-correction labels. The
`wp12_canonical_composed_*` total is only their exact closure projection,
not the evolution state, and the legacy pre-composition totals remain
excluded. The resolved parent replaces legacy coefficient shadowing,
antishadowing, and off-shell blocks with ordered joint-spin CP maps, includes
the sourced NNpi correlator exactly once, and leaves generic
mesonic/SRC/cluster parents as zero-centered alternatives. Item 6 is
not authorized until the following evidence-parity gate also closes.

### WP12-E — Bring every TMD to an \(f_1\)-level evidence standard

Status: **completed and accepted 2026-07-27**

Here “\(f_1\)-level” means comparable discipline, not identical data
availability: a flavor-resolved nucleon input, explicit neutron
construction, stated charge-symmetry-breaking status, common scheme and
scale, quantitative uncertainty, channel-appropriate nuclear propagation,
and observable or controlled-limit validation.

For every quark, antiquark, and gluon TMD:

1. Record the proton central source and available fit/lattice replicas or
   covariance in a machine-readable source/member ledger.
2. Construct the neutron explicitly and provide either sourced CSB or a
   quantitative bound showing the charge-symmetry limit is adequate.
3. Propagate fit/lattice, transverse-profile, wave-function, nuclear, model,
   and numerical uncertainties without presenting scenarios as confidence
   intervals.
4. Embed the input in the shared correlator and test symmetry, positivity,
   rank behavior, link reversal, and projection closure.
5. Apply every supported channel-appropriate binding, Fermi-motion, D-state,
   off-shell, shadowing, mesonic, SRC, and non-nucleonic contribution without
   double counting.
6. Validate a suitable moment, ratio, lattice quantity, observable,
   positivity pattern, or controlled limit. “Nonzero and smooth” is not
   validation.

Required work packages are unpolarized/tensor-even; helicity and worm gears;
transversity/pretzelosity/Boer--Mulders; quark Sivers and other T-odd
structures; tensor-polarized quarks; gluon T-even helicity/linear
polarization; gluon f/d T-odd multiplets; and tensor-polarized gluons. A
generated evidence matrix must contain no required “placeholder”,
“universal ansatz”, “unquantified”, or “structural only” cell.

WP12-E closes with all 36 rows passing in
`outputs/validation/wp12_evidence_parity_matrix.json` and all six final gates
passing in `outputs/validation/wp12e_acceptance.json`. Item 6 may now perform
complete rank-aware multi-\(Q\) evolution while preserving the resolved
mechanism ledger and correlated uncertainties.

The complete pre-evolution construction history and component inventory are
now frozen in `references/model_construction_note.tex`, with generated PDF
`output/pdf/model_construction_note.pdf`. Item 6 must update this note if it
changes the scheme contract, model interpretation, evidence status, or
declared limitations.

### External Norfolk-current correction

Status: **partially resolved by Alex Gnech reply, 2026-07-27**

PRC106 Table-II set A and Table IV now supersede the PRC99 constants and
magnetic-moment table as the reference benchmark. The author-confirmed
regulator prescription is \(I_k\to C_{R_L}I_k\). The nonminimal
\(d_1^S\) contact term validates within the quoted Table-IV uncertainty for
all four Norfolk models. The separated \(d_2^S\) OPE \(I_1/I_2\) pieces
remain inconsistent with Table IV and stay excluded from production.
Exact comparison values and a reply-ready table are in
`references/gnech_norfolk_current_reply.md` and
`handoff/correspondence/norfolk_current_followup_draft.md`.

### C4 all-volume integration audit

Status: **complete for the declared C4 scope, 2026-07-30**

All six normative sources (Volumes 0--V) are preserved and indexed under
`references/`. C4 satisfies the applicable Volume 0 architecture contract,
the Volume I analytic benchmark contract, Volume II Benchmarks E--F, and the
Volume III zero-rescattering boundary. The complete current suite passes
613/613 tests; the C4 architecture validator records 25 requirements, 40
deliberate mismatch injections, 16 provenance nodes, and eight immutable
output hashes.

“Integrated” does not mean that later-volume physics has been implemented
inside C4. Volume IV consumption remains fail-closed until the nucleon layer
exports complete parton--target helicity matrices, correlated microscopic
proton/neutron members, the Volume III phase/soft budget, and covariance.
Volume V consumption remains fail-closed until a closed regulated
\(b_{\rm TMD}\)-space operator basis, LF-to-QCD matching/calibration,
rank/Bessel/phase/mass metadata on every parent, and the shared microscopic
ensemble are available. C4 contains no nuclear dynamics, QCD evolution,
process factorization, or \(W+Y\) implementation.

The machine-readable cross-volume status is
`docs/next_level/c4_normative_source_integration.json`; its readable audit is
`docs/next_level/c4_normative_integration_report.md`. The exact next coding
job is C5: implement and validate the Volume III one-gluon Wilson-line/cut
pilot without changing the immutable C4 regression oracle. Volume IV nuclear
C4A--C4F follows only after the complete nucleon export, and Volume V
matching/evolution follows after that matching boundary is closed.

### C7/H0 — Microscopic light-front Hamiltonian spine

Status: **implemented and accepted locally, 2026-07-30**

Starting commit:
`ce4b761d19b23bd5f7da1ddc026153685943e639`. The final local commit is the
commit containing this entry; nothing is to be pushed as part of C7.

Normative Volumes 0--VII are indexed. Volume VI has SHA-256
`568979e0fa0015a70795a7c27c4c98b992848085c982a7ee4eca0374fec72570`;
Volume VII has SHA-256
`326fd902f648b760ee97add0bb30418b4f4843f1bc64c98afd752940d11ac6e1`.
All pinned Volume 0--VII hashes pass.

The validation-only API under `deuteron_wigner.microscopic.h0` now provides
typed Hamiltonian resolution and scale objects, exact parton and many-body
basis states, complete SU(3) singlet bases, signed permutation bases,
center-of-mass/Lawson diagnostics, the free invariant-mass term, one reduced
canonical `qqq<->qqqg` term with generated adjoint, readiness gates, and an
isolated provenance graph. See `docs/next_level/c7_api.md`.

At all three benchmark resolutions `(Nmax,b/GeV)=(8,0.40),(8,0.45),(10,0.50)`,
the `qqq`, `qqqg`, and `qqqq-qbar` basis dimensions and free-matrix sizes are
respectively 1 (`1x1`), 2 (`2x2`), and 3 (`3x3`). Complete color-singlet
multiplicities are exactly 1, 2, and 3. Maximum residuals are: color generator
`1.8667974275620837e-15`, color orthonormality
`2.220446049250313e-16`, recoupling `2.220861168919456e-16`,
antisymmetrizer idempotence `2.7755575615628914e-17`, CM and Lawson `0`,
free Hermiticity and matrix-free/assembled agreement `0`, independent
quadrature `3.4638958368304884e-13`, and reduced-vertex Hermiticity
`2.220446049250313e-16`, all below the declared `2e-11` tolerance.

Regression status: 834 tests pass; all nine legacy builders pass; all 36
evidence rows and 162 atlas pages pass; C3/C4/C5/C6/C7 injection counts are
24/40/48/60/48; the 216-route production registry, production provenance and
composition, eight authoritative output hashes, and all pinned C5/C6
manifests remain unchanged. C7 manifests regenerate deterministically and
the architecture validator covers 74 stable requirements.

This is an H0 architecture benchmark, not a physical nucleon result.
Unresolved H1/H2 physics includes interacting valence dynamics,
renormalization/counterterm flow, complete instantaneous and sector-changing
kernels, converged tower diagonalization, currents, physical eigenstates,
GTMD overlaps, microscopic Wilson lines, LF-to-QCD matching, and controlled
continuum extrapolation. Production, nuclear, evolution, process, and
inference roots cannot reach H0 objects.

**Exact next package:** C8/H1 — implement the valence-sector Hamiltonian and
renormalization-flow benchmark: controlled `qqq` interaction and
induced-confinement trajectories, current operators, small-tower
diagonalization, eigenstate tracking, mass/current flow, CM revalidation, and
regression against the immutable C7 oracle, explicitly without claiming
nonvalence completeness.

### C8/H1 — Valence Hamiltonian, flow, current, tracking, and TTN

Status: **implemented and accepted locally, 2026-07-30**

Starting commit:
`f3256cdacf746e8c9e0d3beaad68bc5d6b25f804`. The final local commit is the
commit containing this entry. Nothing is pushed.

C8 extends the C7 type system under
`deuteron_wigner.microscopic.h1`; it does not create a parallel basis or
modify any C7 object. The new API comprises immutable
`H1AssumptionBundle`/`H1PredictionPlan`, the 4/7/10-dimensional
`H1BasisTower`, typed `ValenceHamiltonianTerm` and `ValenceHamiltonian`,
`H1TruncationDiscrepancy`, `RenormalizationCondition` and
`RenormalizationTrajectory`, exact and matrix-free Krylov solvers,
Hamiltonian-owned `ValenceVectorCurrent`, `ValenceStateTracker`,
symmetry-indexed TTN objects and Rayleigh--Ritz optimizer, and versioned
`ValenceMicroscopicStateBundle`.

Three deterministic branches execute:

- PLAN-A
  (`C8:H1:PLAN:d21966f5baf0fbb07821`): induced confinement plus effective
  color-spin;
- PLAN-B
  (`C8:H1:PLAN:fa8821a67fe9aa7c6208`): zero confinement plus effective
  color-spin;
- PLAN-C
  (`C8:H1:PLAN:d9938ed1163bbc2799e2`): induced confinement without
  color-spin.

All share the \(M^2=0.88^2=0.7744\ {\rm GeV}^2\) validation mass and exact
vector-charge conditions. Across the three resolutions, PLAN-A has
`kappa4 = 0.42, 0.3442622951, 0.2916666667`,
`color_spin = 0.075, 0.0681818182, 0.0625`, and
`mass_ct = 0.1101836635, 0.1200328556, 0.1267184815`. PLAN-B sets `kappa4`
exactly zero and has mass counterterms
`0.1857625459, 0.1820123652, 0.1788892213`. PLAN-C turns color-spin off and
has mass counterterms
`0.1597186545, 0.1666521604, 0.1715063649`.
The withheld proton current at \(Q^2=0.3\) lies near 0.94--0.95 across the
branches; the correlated neutron closes \(F_1^n(0)=0\).

Maximum numerical diagnostics are: mass-condition residual
`1.1102230246251565e-16`, charge residual `4.440892098500626e-16`,
exact/Krylov current residual `1.2212453270876722e-15`, current Hermiticity
`0`, full-bond TTN energy residual `0`, full-bond overlap defect
`4.440892098500626e-16`, tensor-operator application `0`, and recoupling
unitarity `1.0076776735463298e-15`. The reported (unfitted) maximum
current-component/rotational defect is `0.0034102504180774096`.
The avoided-crossing H-J benchmark shows eigenvalue-order tracking ending on
the wrong branch while overlap/fingerprint tracking changes indices
`0,0,1,1` and reaches the intended state.

Regression status: 852 tests, nine legacy builders, 36 evidence rows, and
162 atlas pages pass. C3/C4/C5/C6/C7/C8 injection counts are
24/40/48/60/48/56. The production registry remains 216 routes; production
provenance/composition, eight authoritative artifacts, the C7 oracle, and all
pinned C5/C6 manifests are unchanged. C8 covers 104 stable requirements; all
JSON regenerates deterministically and validates.

The requested revised algebraic/geometric note
`references/algebraic_geometric_next_level_model_note_revised.tex` was later
supplied and hash-verified. The historical C8 baseline continues to record
its then-absence; current normative manifests record the verified source.

C8 remains `VALENCE_ONLY` and `C8_H1_VALIDATION_ONLY`. It does not establish
a physical nucleon, continuum/scaling trajectory, sea or gluon content,
GTMD overlap, Wilson readiness, Ward closure, nuclear matching, LF-to-QCD
matching, evolution, process factorization, inference, or TMD prediction.
The induced confinement is a resolution-refitted infrared acceleration
branch, not a universal QCD potential.

**Exact next package:** C9/H2 — add the dynamical `qqqg` sector,
sector-dependent renormalization, instantaneous partners, regulator gauging
and Ward closure, gluon/OAM exports, larger-tower convergence, and the
controlled microscopic reconnection boundary to the C5/C6 Wilson engine.
The H1 induced color-spin image and explicit `qqqg` dynamics must remain
alternative until an overlap subtraction/matching map exists.

### C9/H2 — Dynamical qqqg sector and microscopic Wilson boundary

Status: **implemented and accepted locally, 2026-07-30**

Starting commit:
`6a95383694ed93bde8866127b7368d465e546b62`. The final local commit is the
commit containing this entry; nothing is pushed.

C9 extends the same microscopic/compiler/tensor architecture to
`qqq + qqqg`. The tower dimensions are `4+6`, `7+10`, and `10+14`; both
independent qqq-octet times adjoint-gluon singlets are retained. The maximum
color-generator residual is `6.490367750618711e-16`, color orthonormality
residual `2.220446049250313e-16`, and coupled Hamiltonian, vertex-adjoint,
instantaneous Hermiticity, and matrix-free residuals are zero.

H2-PLAN-A is `C9:H2:PLAN:173f2a46b45594dd098a` with certificate
`173f2a46b45594dd098a01b9cc6772156dfa56f152e3745ce826257e14ad3b85`;
H2-PLAN-B is `C9:H2:PLAN:4bfe653bfaf9d7d8142c` with certificate
`4bfe653bfaf9d7d8142c17565039cafc4440782d8668617b12efaeb6a750a04c`.
The read-only H1 reference remains `C8:H1:PLAN:d21966f5baf0fbb07821`.

The pole condition closes to `1.1102230246251565e-16`; charge and Abelianized
Ward residuals are zero. One Jacobian null direction is explicitly retained.
PLAN-A confinement flows `0.32, 0.2666666667, 0.2285714286`; the qg coupling
flows `0.105, 0.0990566038, 0.09375`; sector-4 counterterms flow
`0.04, 0.048, 0.056`. PLAN-B sets confinement to zero.

PLAN-A qqqg probabilities are `0.0935642, 0.0850914, 0.0756149`, with gluon
momentum fractions `0.0415841, 0.0378184, 0.0336066`. Probability, momentum,
and finite-basis canonical Jz ledgers close. Full-bond TTN energy residual is
zero; low bonds omit the gluon sector and visibly fail its probability/OAM
observables. Feshbach remainder norms are nonzero (`0.0270--0.0338`), so the
explicit sector is equivalent only to the induced operator plus its declared
remainder.

The C5/C6 adapter returns zero absorption for discrete off-shell input and
for finite epsilon without physical support. Highest status is
`MICROSCOPIC_WILSON_INPUT_INTERFACE_VALIDATED`, not `WILSON_READY`.

Regression: 865 tests, nine builders, 36 evidence rows, 162 atlas pages,
157 C9 requirements, and 83 C9 injections pass. Earlier injection counts
remain 24/40/48/60/48/56. The 216-route registry, production provenance and
composition, eight authoritative artifacts, C7/C8 oracles, and pinned C5/C6
manifests remain unchanged. JSON regeneration is deterministic.

Volumes VIII and IX and the revised algebraic/geometric note were subsequently
supplied, hash-verified, indexed, and incorporated into the C9 normative
manifest. C9 remains finite, validation-only, unmatched, and not a
physical nucleon, gluon PDF, GTMD/TMD, full gauge proof, nuclear input,
evolution input, process prediction, or inference model.

**Exact next package:** C10/H3 — fully antisymmetrized light-sea sectors,
chiral dynamics, axial/PCAC currents, explicit/induced sea subtraction, and
positive-x microscopic antiquark exports.

### C10/H3 — Explicit light sea, PCAC, and positive-x antiquarks

Status: **implemented and accepted locally, 2026-07-31**

Starting commit:
`31ae656da38a94432dd7f6c753d75e54170d9155`. The final local commit is the
commit containing this entry; nothing is pushed.

The common state now contains distinct `QQQ`, `QQQG`, `QQQUUBAR`, and
`QQQDDBAR` branches with dimensions `4+6+9+9`, `7+10+15+15`, and
`10+14+21+21`. All three five-parton color singlets and the exact signed S4
four-quark antisymmetrizer are retained. Maximum residuals are: color
generator `1.8667974275620837e-15`, color orthonormality
`2.220446049250313e-16`, antisymmetrizer idempotence
`6.938893903907228e-18`, Hamiltonian Hermiticity `0`, pole mass
`1.1102230246251565e-16`, PCAC `0`, full-bond TTN `0`, and common-parent
route closure `0`.

PLAN-A is `C10:H3:PLAN:7c520ce5e2e04d2c7719`; PLAN-B is
`C10:H3:PLAN:b2efe73052d1c9d1004b`. Pair couplings flow
`g45u=0.07,0.0648148,0.0603448` and
`g45d=0.078,0.0722222,0.0672414`. PLAN-A chiral coupling flows
`0.035,0.0318182,0.0291667`; PLAN-B sets it to zero. One Jacobian null
direction and all frozen holdouts remain explicit.

PLAN-A sea probabilities decrease across the tower:
`P_uubar=0.005254,0.004829,0.004220` and
`P_ddbar=0.008380,0.007586,0.006518`. The resulting unfitted
`dbar-ubar` diagnostic is positive:
`0.003126,0.002756,0.002299`. Probability, valence `u=2,d=1`, charge,
baryon, momentum, and canonical Jz ledgers close.

The finite PCAC sum closes term by term; the second-point holdout residual is
`0.0065` and the Goldberger--Treiman-like diagnostic is `0.081`, neither
fitted away. Direct positive-x `ubar`/`dbar` overlaps share one regulated
quark-antiquark-gluon member identity. Feshbach remainder norms remain
nonzero (`0.0380--0.0578`) after vector, axial, pseudoscalar, antiquark, and
norm-kernel transformations.

The antiquark Wilson adapter retains flavor and all three color
multiplicities and returns zero absorption for discrete off-shell input and
finite epsilon without physical support. Highest status is
`MICROSCOPIC_ANTIQUARK_WILSON_INPUT_INTERFACE_VALIDATED`.

Regression: 876 tests, nine builders, 36 evidence rows, 162 atlas pages, 210
C10 requirements, and 90 C10 injections pass. Prior injection counts remain
24/40/48/60/48/56/83. The 216-route production registry, production
provenance/composition, eight authoritative artifacts, C7/C8/C9 oracles, and
pinned C5/C6 manifests remain unchanged. All JSON regenerates
deterministically.

Volumes VIII, IX, X, and the revised algebraic/geometric source were
subsequently supplied, hash-verified, preserved, and indexed. C10 remains a
finite validation EFT, not continuum QCD, a physical nucleon/pion, matched
PDF/GTMD/TMD, full chiral proof, Wilson-ready object, nuclear input,
evolution/process prediction, or inference model.

**Exact next package:** C11/H4 — microscopic nonzero-transfer quark,
antiquark, and gluon GTMD helicity matrices from the common H3 eigenstate;
complete T-even projector closure; local-current/OAM consistency; and
microscopic replacement of the C3/C4 analytic common-parent pilots.

### C11/H4 — Microscopic nonzero-transfer common GTMD parent

Status: **implemented and accepted locally, 2026-07-31**

Starting commit: `68fc5bc34ad0ab7c8940ac8a469da52d341d980e`. The final local
commit is the commit containing this entry; nothing is pushed.

H4 consumes both immutable H3 plans and their correlated proton/neutron
members. One typed overlap engine now constructs full 4x4 joint
target-parton helicity matrices for `u`, `d`, `ubar`, `dbar`, and gluons at
xi=0 and Wilson order zero. All species reuse the authoritative C3 symmetric
recoil. The quark, antiquark, and generated gluon Gram bases have generic
rank 16; the explicit degenerate basis has rank 8. Maximum matrix
reconstruction residual is `2.7755575615628914e-17` and transfer-reversal
Hermiticity closes to numerical zero.

Direct-forward and sequential regulated reductions share one parent ID.
Vector, axial, and EMT routes close algebraically, with nonzero-transfer
holdouts retained. The local tensor operator is explicitly unavailable.
Wigner, transfer-derivative, and finite-basis canonical-OAM routes close;
the maximum finite-difference residual is below `2.4e-9`. Forward PSD and
off-forward Cauchy bounds pass without clipping. Twelve convergence axes are
reported independently. PLAN-A and PLAN-B remain mutually exclusive.

C3/C4 analytic parents remain immutable benchmarks. Microscopic replacement
exists only inside `C11_H4_VALIDATION_ONLY`; production remains unreachable.
The 216-route production registry, provenance/composition, eight
authoritative artifacts, and prior manifests remain unchanged. C11 contains
104 ordered negative injections and 285 stable requirements.

Issued readiness states are microscopic common-parent, quark/antiquark/
gluon projector, T-even forward, current/EMT, Wigner/OAM, scoped analytic
replacement, and nuclear-helicity-interface validation. Physical GTMD/TMD,
Wilson/T-odd, nuclear matching, LF-to-QCD matching, evolution, process,
inference, and production promotion remain closed.

The supplied Volume XI source is preserved at
`references/volume_xi_microscopic_nonzero_transfer_gtmds.tex` with SHA-256
`d66450bb7f21bf0464b926a3480594da3be1ed009948a8031f4b4cb2756b915d` and is
now the package-specific normative H4 formalism reference.

**Exact next package:** C12/H5 — microscopic Wilson-line dynamics on the H4
common GTMD parent: physical spectral support, link-odd quark/antiquark/gluon
helicity matrices, shared Sivers/Boer-Mulders projections, active-gluon f/d
color projections, and Wilson/Fock-order compatibility. Matching and common
evolution remain later work.

### C12/H5 — First-order microscopic Wilson dynamics on H4

Status: **implemented and accepted locally, 2026-07-31**

Starting commit: `15032f5e3f2035aa93a42b63ee9c9139996e5500`. The final local
commit is the commit containing this entry; nothing is pushed.

C12 acts exclusively on the complete C11/H4 4x4 helicity matrices at xi=0.
The C5 path object derives the future/past pole sign; a declared continuum
spectral rule creates the distributional cut and remains exactly zero below
threshold. A 16--256-level discretized sequence converges to the analytic
cut with final residual `5.51201e-6`. Numerical epsilon is not physical.

Quark and direct positive-x antiquark link-odd matrices are constructed
before distinct Sivers and Boer-Mulders projections. All coupling, cut, OAM,
and link-average zero limits close. The active-gluon route retains four
ordered pairs, independent f/d channels, trace/helicity/linear sectors, and
both color outer multiplicities. SU(3) norms and orthogonality close exactly.

One half-soft subtraction closes the rapidity derivative; missing and
duplicate subtractions have equal-and-opposite signed residuals. Exact and
full-bond TTN Wilson results agree, while reduced bonds visibly lose the
OAM-sensitive amplitude. Sixteen convergence axes remain separate.

Valence quark attachments have explicit qqqg support. Antiquark and active-
gluon routes are induced operators with nonzero remainders because explicit
qqqq-qbar-g and qqqgg sectors are absent. C5/C6 remain immutable pilots and
replacement is confined to `C12_H5_VALIDATION_ONLY`. Production, nuclear,
matching/evolution, process, and inference gates remain closed.

C12 contains 294 requirements and 124 ordered negative injections. The
216-route registry, production provenance/composition, and eight
authoritative artifacts remain unchanged.

**Exact next package:** C13/H6 — add explicit qqqgg and qqqq-qbar-g sectors,
replace the induced H5 gluon/antiquark channels, and validate second-order
Dyson/Magnus Wilson convergence before beginning nuclear composition.

### C13/H6 — Explicit higher-Fock support and order-two Wilson benchmark

Status: **implemented and accepted locally, 2026-07-31**

Starting commit: `5c368cae780e76fc029a6db765f04167f1e09ac0`. The final local
commit is the commit containing this entry; nothing is pushed.

The seven-sector tower has dimensions 72, 115, and 158. Common-generator
color certificates retain six QQQGG singlets and eight singlets for each
QQQQ-QBAR-G sector. Fermion antisymmetry and combined two-gluon bosonic
exchange close. The coupled Hamiltonian, Krylov route, and full-bond TTN
close at three independently refitted resolutions; one null direction and
all holdouts remain visible.

First-order quark, antiquark, and gluon Wilson support is now explicit.
Second-order quark support is explicit and strict Dyson/Magnus polynomials
agree through order two. Spectral, cut, soft, path, and reduced gauge
benchmarks close. Low bond loses 47% of a Wilson observable.

Second-order antiquark and active-gluon channels remain unavailable because
QQQQ-QBAR-GG and QQQGGG sectors are absent. C13 adds 336 requirements and
148 injections. The 216 production routes and eight artifacts remain
unchanged; physical, nuclear, matching/evolution, process, inference, and
production gates remain closed.

**Exact next package:** C14/H7 — add QQQGGG and QQQQ-QBAR-GG sectors to close
second-order antiquark/gluon Wilson support before nuclear composition.
## C14/H7 — explicit three-gluon and sea–two-gluon sectors

The final local commit is the commit containing this entry; nothing is
pushed.

C14 extends the immutable C13 validation root to ten sectors by adding
`QQQGGG`, `QQQUUBARGG`, and `QQQDDBARGG`. The validated tower dimensions are
140, 227, and 314. Color/permutation certificates retain 22 three-gluon
singlets (4 symmetric, 4 antisymmetric, 7 mixed copies) and 28 singlets in
each sea--two-gluon sector (14 symmetric plus 14 antisymmetric).

Wilson orders one and two are explicit for quarks, antiquarks, and gluons.
Order three is unavailable and fails closed. Fundamental,
anti-fundamental, adjoint, and ordered-two-link strict Dyson/Magnus,
spectral-cut, soft-overlap, finite gauge, explicit/induced, tensor-network,
and multi-axis convergence benchmarks are recorded in the C14 manifests.
The package contains 390 requirements and 184 detected negative injections.

The H7 result remains validation-only. UV matching, a physical TMD scheme,
continuum soft completion, Collins--Soper evolution, process factors,
nuclear composition, inference, and production are unresolved. The
216-route production registry, production provenance/composition, all eight
authoritative artifacts, and C3--C13 parents/manifests remain immutable.

**Exact next package:** C15/N0 -- matched spin-1 nuclear light-front state
and microscopic deuteron GTMD composition, beginning with a normalized NN
spin-1 state, Hamiltonian-consistent one- and two-body operators, complete
nucleon helicity-matrix exports, correlated proton/neutron microscopic
members, and strict separation between partonic Wilson rescattering and
coherent nuclear propagation.
## C15/N0 — matched NN spin-1 nuclear validation root

The final local commit is the commit containing this entry; nothing is
pushed. C15 composes correlated H7 proton/neutron identities with exclusive
AV18, Norfolk, H7-dynamics-variation, and analytic NN plans. It validates one
spectator-preserving recoil authority, normalized amplitude-level S/D states,
6x6 spectral and partonic parents, complete spin-1 projectors, common-parent
reductions, b1, current/angular, tagged, CP, off-shell, TTN, and provenance
closures. Wilson orders 0--2 are retained for quarks, antiquarks, and gluons.

N0 contains 462 covered requirements and 244 detected negative injections.
It is validation-only and disconnected from the 216 production routes.
NNPI, DeltaDelta, compact/hidden-color, coherent shadowing, nuclear Glauber,
full two-body currents, matching, evolution, processes, and inference remain
unavailable.

**Exact next package:** C16/N1 -- spin-resolved NNPI sector, pion-active and
transition operators, internal-versus-exchange pion subtraction,
Hamiltonian-consistent two-body currents, and a coherent helicity-resolved
small-x pilot.

Volume XII is preserved at
`references/volume_xii_microscopic_wilson_second_order.tex` with SHA-256
`204d3dc79084a26b86b49cf8042d22ae32cffb15b0e0deec6cf2dcb043a76c83`.
It is the normative nucleon-side second-order Wilson specification for the
C15 boundary and later nuclear packages.
## C16/N1 — spin-resolved NNPI validation root

The final local commit is the commit containing this entry; nothing is
pushed. N1 adds a normalized `NN + NNPI` state with complete pion charge
channels, three-body and transition recoil, a coupled Hermitian Hamiltonian,
nucleon/pion/transition operators, internal/exchange pion subtraction,
Hamiltonian-consistent current, coherent helicity pilot, parton/nuclear
overlap, derived CP map, and two-branch nuclear TTN.

The tower dimensions are 30, 52, and 78; the fine benchmark has
`Z_NN=0.8915758315` and `Z_NNPI=0.1084241685`. C16 contains 516 requirements
and 308 detected injections. It remains isolated from the 216 production
routes and all matching, evolution, process, and inference roots.

**Exact next package:** C17/N2 -- continuum-calibrated pion/nucleon
transition dynamics and complete Hamiltonian-consistent exchange-current
operator basis, followed by controlled diffractive-input and nuclear
coherence matching. DeltaDelta, compact six-quark, and hidden-color sectors
remain later explicit branches rather than N2 defaults.

Volume XIII is preserved at
`references/volume_xiii_nnpi_pion_matching_coherent_nuclear.tex` with
SHA-256 `59767d330b55cfff552b34979692cdb43720c978c75e07d5f4ca896f940e8fb9`.
It is the package-specific normative formalism for C16/N1 and its successors.

## C17/N2 — continuum NNPI and exchange-current closure

The final local commit is the commit containing this entry; nothing is
pushed. N2 adds continuum-calibrated NNPI transition dynamics, a convergent
finite-volume spectral map, pole/residue and held-out calibration reports,
and a declared-order Hamiltonian-to-exchange-current certificate. Continuity
closes by component, Fock block, and charge channel. Separator trajectories,
explicit/Feshbach-induced pion equivalence, unmatched pion-active closure,
coherent continuum, CP reduction, TTN, and independent convergence axes are
machine-readable.

C17 contains 614 covered requirements and 340 detected negative injections.
It is validation-only, leaves all C16 and production outputs immutable, and
does not issue physical, matching, evolution, process, inference, or
production readiness.

**Exact next package:** C18/N3 -- add explicit DeltaDelta and compact
six-quark/hidden-color sectors as exclusive typed branches, calibrate their
mixing against independent nuclear holdouts, derive their Hamiltonian-
consistent operator/current attachments, and prove count-once composition
with NN and NNPI before any downstream matching.

Volume XIV is preserved at
`references/volume_xiv_continuum_nnpi_exchange_currents.tex` with SHA-256
`cb30d603948c6b14cbeaa0fbb332396e86c62c6ab76eeb116161e7eaa3c58d0d`.
It is the package-specific normative formalism for C17/N2 and the inherited
continuum/current boundary for C18/N3.

## C18/N3 — explicit non-nucleonic validation root

The final local commit is the commit containing this entry; nothing is
pushed. N3 adds exclusive DeltaDelta, compact six-quark, and combined
count-once assumption plans. The charge-complete DeltaDelta basis retains
3S1, 3D1, and 7D1 channels. The compact branch retains five SU(3) singlet
multiplicities, exact S6 identity, one cluster direction, and a four-
dimensional hidden-color complement. Gram-projector and subtraction routes,
coupled Hamiltonian, declared-order currents, block continuity, common
partonic parent, tensor/b1, coherent/CP, and four-branch TTN checks close.

C18 contains 762 covered requirements and 400 detected negative injections.
It remains finite-resolution, validation-only, and disconnected from all
216 production routes. Physical sector probabilities, physical TMDs,
shadowing/Glauber, matching, evolution, processes, and inference remain
forbidden.

**Exact next package:** C19/M0 -- light-front-to-QCD operator matching pilot
for the complete microscopic nucleon and deuteron parent, with a closed
regulated operator basis, small-b matching, explicit UV/rapidity/soft scheme
identity, and first common-scheme rank-aware evolution tests.

Volume XV is preserved at
`references/volume_xv_delta_delta_six_quark_hidden_color.tex` with SHA-256
`675cc27dfe4548e6e49d4ba7d1c093dc235003aaa8f1b77d4e4ef2829246b4cc`.
It is the package-specific normative formalism for C18/N3 and the inherited
non-nucleonic boundary for C19/M0.

## C19/M0 — common-scheme matching and evolution validation

The final local commit is the commit containing this entry; nothing is
pushed. M0 adds two finite-related schemes, a closed 540-dimensional operator
basis, overconstrained shared matching, step scaling, UV/rapidity/soft
accounting, rank-aware transforms, small-b OPE, collinear and two-scale
evolution, threshold matching, and resolved nuclear transport. It covers 830
requirements and 480 negative injections and remains validation-only.

**Exact next package:** C20/M1 -- replace analytic matching oracles with
declared perturbative coefficient libraries and controlled external/lattice
step-scaling constraints while retaining the M0 scheme and isolation gates.

## C20/M1 — source-audited coefficient and constraint validation

The final local commit is the commit containing this entry; nothing is
pushed. M1 retains all 540 M0 operator identities, with 492 audited executable
and 48 explicitly unavailable entries. Ten supported twist-two coefficient
records, distributional tests, a synthetic exact external-covariance bundle,
shared overconstrained matching, seven holdout classes, component-wise step
scaling, scheme conversion, rank 0--3 transport, and uncertainty ledgers are
validated. C20 covers 770 requirements and 560 negative injections.

**Exact next package:** C21/M2 -- physical anomalous-dimension and Collins-
Soper-kernel library, continuum/lattice-constrained nonperturbative kernel,
common multi-Q rank-aware evolution, and threshold-qualified microscopic
nucleon/deuteron TMD ensembles.

Volume XVI is preserved as the authoritative PDF
`references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf` with
SHA-256 `bc3e38b1ddba37b9375d1dc50eaa6ad0e91f6732270b983d5b296024fa6d5aa2`.
It defines the post-M1 ensemble and M2--M4 evolution/process-readiness
boundary without promoting the C20 validation pilot to physical status.

## C21/M2 — threshold-qualified multi-Q evolution validation

The final local commit is the commit containing this entry; nothing is
pushed. M2 adds seven source-audited anomalous/beta records, reversible
threshold history, separate quark and exploratory-gluon kernel plans, exact
and finite-order two-scale routes, rank 0--3 multi-Q transport, a 540-entry
capability matrix, and resolved nuclear evolution. It covers 900 requirements
and 640 negative injections and remains validation-only.

Volume XVII is preserved at
`references/volume_xvii_process_qualified_tmd_observables.tex` with SHA-256
`dae315b3feb198fc85cddb2243fc5b9e99f9d9c8b1579908c30b0cfcde4ae9af`.
It is the authoritative post-M2 process boundary and does not alter or
promote C21's validation-only numerical status.

**Volume-XVII process boundary (sequencing superseded):** P0 will implement
qualified color-singlet Drell--Yan, current-fragmentation SIDIS, inclusive b1,
tagged spin-1 DIS, selected gluon-sensitive records, factorization/Glauber
certificates, and rank-resolved W+Y validation. The supplied C22/M3 package is
executed first; P0 follows as C23 below.

## C22/M3 — source-qualified twist-two small-b OPE

The package begins from local commit `ad3fa2a3d8828620c808becbcad7db8b5893039c`
with `afe789a68b7394d1cb0165aa3b428b6e2d79f5bb` in its ancestry. The immutable
C21 baseline reproduced with 1,053 passing tests. C22 adds exact typed endpoint
distributions, declared-order source-hashed coefficient records, explicit
gamma5 conversion, nonsinglet/singlet collinear blocks, rank-aware OPE maps,
route-A/route-B checks, a 540-entry M3 capability layer, resolved nuclear OPE
validation, separate uncertainty/accuracy axes, frozen holdouts, and 720
ordered negative injections. It remains validation-only and creates no
process, W+Y, inference, or production path.

Higher-order papers are preserved under `data/raw/c22_sources`, but complete
N3LO ancillaries have not been ingested; executable expressions remain at the
explicit declared order one. Unsupported twist-three/T-odd, spin-1 gluon
double-flip, higher-twist pretzelosity, and operator-distinct many-body blocks
remain fail-closed as recorded in `c22_unresolved_physics_gaps.md`.

Volume XVIII is preserved at
`references/volume_xviii_smallb_ope_collinear_mixing.tex` with SHA-256
`ee5a103b28ebc216649a910618a455a85fc895d00fe74cb39630568a14508ed3`.
Its formal audit supersedes the earlier C22 completion inference. The current
typed implementation is a fail-closed validation scaffold: no identity is
M3-qualified until exact source/ancillary expressions, independent x/Mellin
solvers, and operator-derived 540-entry classification satisfy Volume XVIII.

**Exact next package:** C22/M3 closure -- ingest authoritative coefficient and
splitting ancillaries with exact locators/transcription hashes; implement exact
distribution/color expressions and independent x/Mellin evolution; replace
the periodic prototype-family map with decorated-operator classification; and
re-run all Volume-XVIII RG, threshold, rank, nuclear, holdout, and regression
gates. C23/P0 remains blocked from execution until this closes.

The supplied C23/P0 prompt is preserved at
`docs/next_level/c23_p0_codex_prompt.md` with SHA-256
`5346947dd612813386a07ed1827a8ffd9540f03614862e135191eb0a105d4347`.
Its declared `438/54/48` baseline predates the Volume-XVIII audit and conflicts
with the authoritative fail-closed `0/54/486` state. The prompt's own M3 gate
therefore blocks every W term. `c23_prerequisite_audit.json` records the exact
conflict and unblocking action; no C23 process or production route was created.

## C22Q/M3Q — tiered capability reconciliation

C22Q explains the count conflict without altering C20/C21 physics. The 438 M2
intersection is analytic-validation qualified, not source or physical-input
qualified. Final tier counts are 438 analytic-validation qualified and 102
unqualified; process eligibility is 438 analytic-oracle eligible and 102 not
eligible; source and physical eligible counts are both zero. The validation
CS/large-b plan is explicitly synthetic. Only NN is selected in the analytic
nuclear assumption plan; distinct many-body blocks remain unavailable.

The original C23 prompt remains immutable. The corrected v2 prompt and
prerequisite contract permit a nonempty analytic-only compiler plan and keep
source/physical plans fail-closed. No process or W/Y route is executed by C22Q.

**Exact next package:** C23/P0 v2 -- execute only the analytic-validation
process compiler against `ANALYTIC_PROCESS_ORACLE_ELIGIBLE` identities. Keep
source and physical plans blocked until their exact source, covariance,
CS/large-b, and operator-specific nuclear requirements close.

The C22Q scientific completion commit is
`a1527fefc259eb32e362ccda5db135fb52149ad5`. The corrected C23 v2 prompt and
contract are deterministically bound to that commit in the immediately
following handoff commit.

## C23/P0 — analytic-validation process compiler

C23 consumes only the 438 C22Q analytic-eligible identities; 102 identities
fail closed. It implements typed DY, current-fragmentation SIDIS, conditional
heavy-pair DIS, spin-1 basis, hard/partner/FO interfaces, factorization/Glauber
certificates, and rank-zero through rank-three analytic W/Y oracles. Ranks zero
and two have eligible process inputs; ranks one and three remain mathematical
oracles without process execution. Inclusive b1, tagged DIS, all T-odd and
multiparton channels, all non-NN nuclear blocks, and the matched total remain
unavailable. Every output is validation-only; source and physical tiers are
empty and no likelihood, inference, or production route exists.

The valid C22Q scientific ancestor is
`a1527fec32c07865de34d14dc1345ca9e816fac8`; the previously expanded
`a1527fef...` string was a provenance typo, resolved from Git ancestry without
rewriting historical manifests.

**Exact next package:** source-qualification closure for the chosen DY/SIDIS
and gluon process blocks, or a separately authorized expansion of b1/tagged
operator inputs. Physical process execution remains blocked pending joint
covariance-bearing CS/large-b and external-input bundles.

## C24/P1 — source-qualified T-even process-spine audit

C24 begins from `0f6495107effda70ca406e8a44e365f3a8080198` and preserves
the C22Q scientific ancestor
`a1527fec32c07865de34d14dc1345ca9e816fac8`. The complete C23 baseline
reproduced with 1,095 tests before edits. C24 adds an isolated `process.p1`
source-lock and qualification layer, 825 covered requirements, and 880 ordered
negative injections. The production registry remains 216 and the eight
authoritative artifacts are unchanged.

Sixteen primary papers, Zenodo 15006449 metadata, and the exact ARTEMIDE 3.01
archive are locally preserved at `data/raw/c24_sources` and hash-audited. The
current 3.03 release is comparison-only and was not substituted. The 3.01
archive contains the code and identifies ART25, but it does not contain the
ART25 constants or its declared 500 replica files. Therefore the final tiers
remain 438 analytic-process-oracle eligible, 102 not process eligible, zero
source-process eligible, and zero physical-input eligible. DY, SIDIS, b1,
tagged DIS, and heavy-pair DIS have complete failed-gate records; no
source-qualified W+Y, likelihood, inference, matched total, or production
route was created.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c24_manifests.py 1112
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c24_architecture.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C25/P1A ART25 ancillary closure — obtain the official
ART25 constants and all 500 correlated members, lock their exact provenance,
implement deterministic ARTEMIDE 3.01 DY and SIDIS benchmark adapters with
frozen holdouts, and re-run the source evaluator. Do not substitute a newer
release or promote a source record to physical input without joint covariance.

## C25/P1A — ART25 ancillary closure and source-gate rerun

C25 recovered the official ART25 constants, nine model files, and correlated
ensemble at payload commit `9ca8159e00ff2df159ab2ce4d7ffb13589af0c71`.
The exact engine remains the v3.01 tag commit `d873dc9...`; all nine model
files are byte-identical across this boundary, and no later engine code was
used. The exact engine builds and imports without a physics patch.

The released ensemble contains 642 stochastic rows plus initialization and
central/mean technical records, rather than the 500 described in older prose.
The typed parser preserves 22 fitted parameters, six fixed slots, three
collinear member indices, source locations, and hashes. Independent means,
quantiles, and correlations reproduce deterministically. The exact C24
baseline was 1,112 passing tests; the production registry remains 216 and all
eight authoritative artifacts are byte-identical.

Process execution remains closed because `MSHT20_REP`, `MAPFF10NNLOPIp`, and
`MAPFF10NNLOKAp`, plus frozen official process outputs, were not located in
the audited public sources. Final tiers remain 438 analytic, 102 not process
eligible, zero source, and zero physical. See the exact unsent request in
`docs/next_level/c25_art25_author_request.md`.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c25_manifests.py <current-test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c25.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C26/P1B — ingest and hash-lock the requested three
collinear ensembles and author-supplied frozen outputs, initialize the exact
v3.01 engine with the immutable ART25 constants, execute central and all 642
joint-member DY/SIDIS benchmarks, then rerun the unchanged source and physical
gates. If those inputs are not supplied, retain zero qualification.

## C26/P1B — exact collinear acquisition and residual source closure

C26 acquired CERN's exact `MAPFF10NNLOPIp` and `MAPFF10NNLOKAp`
DataVersion 1 archives. Each has 201 members; both tarballs, `.info` files,
and all 402 grids are hash locked. The archive timestamps predate ART25 and
the constants use the exact names. All 642 Lambda rows resolve both FF
indices exactly over 0--199, with no wrapping, clipping, dropping, or
substitution.

`MSHT20_REP` remains absent after the official LHAPDF index, complete
ARTEMIDE/DataProcessor histories and bundles, Zenodo, Software Heritage, and
paper-source audit. ART25 requires indices 0--999. The public DataVersion 4
`MSHT20nnlo_as118` has 65 Hessian members and was not substituted or
converted. Exact v3.01 initialization and full process execution therefore
fail closed at preflight.

Independent NP-model functions ran for all 642 stochastic members; exact
MAPFF joint indices were evaluated independently with LHAPDF 6.5.5. These
checks are not labeled full TMD predictions. Source-owned frozen outputs were
not found. External ART25 source, microscopic-project source, and physical
eligibility remain zero; the analytic split remains 438/102, production is
216, and authoritative artifacts are unchanged.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c26_manifests.py <current-test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c26.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C27/P1C -- ingest an author-supplied exact
`MSHT20_REP` archive or fully specified generator state and source-owned
frozen outputs, then initialize immutable v3.01 and execute the frozen grid
and all 642 joint members. Otherwise retain fail-closed qualification.

## C27/P1C — exact MSHT source and complete ART25 execution

The directly transferred `MSHT20_REP` DataVersion 3 ensemble is locally
preserved and hash locked. Its declared indices 0--999 resolve all 642 ART25
PDF selections; the additional file 1000 is preserved but excluded according
to source metadata and generator behavior. Redistribution permission is not
documented, so the grids remain local research-validation inputs.

Immutable ARTEMIDE v3.01 initialized with unchanged ART25 physics constants
and byte-identical MSHT/MAPFF inputs. Central and all 642 stochastic members
completed for CS, TMDPDF, pion/kaon TMDFF, three DY, and two charge-resolved
SIDIS validation points. Serial, four-process, and restart paths agree exactly;
no member failed or was imputed. The 39-dimensional joint covariance retains
distribution/process and DY/SIDIS cross correlations.

No author-frozen output bundle was supplied, so results are labeled
`SOURCE_REGENERATED_OUTPUT`. Source W is reproduced only for the declared
low-qT validation points. Source W+Y, source-process qualification, and
physical-input qualification remain closed. External proton ART25 provenance
remains disjoint from the microscopic deuteron model.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c27_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c27.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C28/P1D — obtain source-owned frozen ART25 numerical
outputs, complete observable/cut definitions, and exact fixed-order/asymptotic
partners; validate them without mixing analytic C23 Y or promoting external
proton provenance to the microscopic spin-1 root.

## C28/P1D — complete public ART25 dataset reproduction

C28 locks the historical public ART25 DataProcessor commit separately from
current master and preserves a complete-history bundle. The native historical
loader and cut function recover 36 DY and 10 SIDIS datasets: 8,675 source
points, 1,209 retained (627 DY and 582 SIDIS), and 7,466 excluded. The cut
reason ledger agrees with every source decision. CDF1 remains an exact
50-loaded/33-retained regression with CDF1.0 = 3.4394876804377352 pb/GeV.

The unchanged ARTEMIDE v3.01/ART25 chain executes the central technical record
and all 642 indivisible joint PDF/FF/nonperturbative records over the retained
dataset. Native error, nuisance-profile, and chi2 semantics are preserved. An
exact low-rank anomaly factor supports within- and cross-process covariance
queries without independently reshuffling marginal ensembles.

The evidential result is narrowly
`SOURCE_REPRODUCIBLE_LOWQT_W_VALIDATION`. No author/repository frozen numerical
anchor or exact source-identical DY/SIDIS fixed-order and asymptotic partners
were found, so author-anchored, full W+Y, full source-process, and physical-input
eligibility remain zero. External proton ART25 provenance remains disjoint from
the microscopic spin-1 project root. Raw author-transferred MSHT grids remain
outside Git pending explicit redistribution permission.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c28_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c28.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C29/P1E — implement and validate the typed bridge
contract between the external ART25 source ensemble and microscopic-project
operator root: operator/scheme/scale maps, parameter ownership, joint
covariance, model discrepancy, double-counting exclusions, and frozen
calibration/holdout partitions. Do not calibrate or promote physical process
status until that contract and its evidence inputs close. In parallel, retain
separate unresolved tasks for exact source-identical DY and SIDIS fixed-order
and asymptotic partners needed for W+Y.

## C29/B0 — typed external-to-microscopic bridge contract

C29 implements the immutable bridge between
`ART25_EXTERNAL_SOURCE_ROOT` and `PROJECT_MICROSCOPIC_OPERATOR_ROOT`. Complete
operator, target, nuclear, scheme, scale, rank, link, color, and domain
identities are audited without collapsing the roots. Phenomenological
deuterium remains distinct from the microscopic deuteron and NN-only remains
distinct from matched total.

The frozen bridge grid contains distribution, Collins-Soper, DY one-leg,
SIDIS target-leg, boundary, target, provenance, nuclear, and covariance-null
records. The exact C28 642 x 1209 anomaly factor is projected without member
loss or reordering; linear covariance closes and nonlinear diagnostics are
evaluated memberwise. All 46 datasets and 1,209 retained points have ancestry
and mutually exclusive compressed-versus-direct future-use plans.

No complete ART25-to-microscopic scheme-qualified numerical TMD bridge closes
in B0. Rank-zero quark/antiquark families have an identified validation domain,
the quark CS kernel is diagnostic-only, and process, deuteron, gluon, and T-odd
bridges remain unavailable. This is fail-closed scientific status, not zero
physics. No fit, calibration, likelihood, posterior, reweighting, emulator,
process promotion, or production mutation is created.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c29_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c29.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact next package:** C30/B1 — close and validate the first genuinely common
numerical distribution bridge for rank-zero proton u, d, ubar, and dbar by
supplying a source-audited finite ART25-to-microscopic scheme adapter and a
scheme-qualified microscopic numerical export with convergence and typed
discrepancy inputs. Do not calibrate or infer until that bridge passes.

### Volume XIX integration addendum

The authoritative TeX source is now stored at
`references/volume_xix_source_qualified_process_inputs.tex` with SHA-256
`8b4e2d1dfd187f462d61d0134dbeae2bac8b3377cf315f733f63147ecac91596`.
All 50 formal requirements are mapped in the C29 Volume XIX crosswalk and are
validated without promoting any bridge capability. Volume XX remains absent.
The exact next package remains C30/B1 because Volume XIX supplies the formal
qualification contract, not the missing finite scheme adapter or common
microscopic numerical export.

### Volume XX integration addendum

The authoritative bridge-geometry TeX source is now stored at
`references/volume_xx_source_reproducible_bridge_geometry.tex` with SHA-256
`54cea4d69b1b85a787b083a0e384226a65c76ff93dd151a74ab0249aa4c13893`.
All 53 formal requirements are mapped to C29 evidence. The microscopic export
now explicitly retains the C14 tensor-network plan and a nonstatistical TTN
bond axis. This completes the formal C29/B0 integration without changing
central physics or promoting bridge readiness. C30/B1 remains the exact next
package: implement the missing finite adapter and common scheme-qualified
microscopic numerical export before sensitivity, calibration, or inference.

## C30/B1 — rank-zero proton distribution bridge audit

C30 freezes the exact ART25 rank-zero proton TMDPDF definition and flavor
ordering, selects the C11 same-operator microscopic parent with later levels
kept as separate convergence axes, and selects the one-way
`B1-SCHEME-ART25` conversion plan. Twelve u, d, ubar, and dbar points have a
common kinematic domain.

The numerical bridge does **not** close. The current microscopic object is not
a source-qualified renormalized, soft-subtracted, rapidity-qualified TMD, and
no finite conversion to the ART25 convention is available. The adapter is
therefore non-executable, its remainder is nonzero-unknown, all twelve points
are `BRIDGE_COMMON_DOMAIN_ONLY`, and no residual or statistical compatibility
quantity is computed. The external 642-member identity is retained on an
empty coordinate projection; this is unavailable physics, not zero physics.

C30 records fifteen observable-level convergence axes, keeps thirteen
discrepancy classes distinct, supplies 1,600 requirement records and 1,520
ordered negative controls, and creates no fit, likelihood, calibration,
posterior, reweighting, emulator, process execution, status promotion, or
production route. Reproduce with:

```bash
PYTHONPATH=src python3 scripts/build_c30_manifests.py 1149
PYTHONPATH=src python3 scripts/validate_c30.py
PYTHONPATH=src python3 -m pytest -q
```

**Exact next scientific job:** derive or integrate a cited, operator-identical
microscopic TMD renormalization/soft/rapidity prescription and finite ART25
scheme adapter, including inverse, round-trip, RG, rapidity, threshold,
remainder, and same-operator convergence tests. Only then export numerical
u/d/ubar/dbar vectors at the frozen points. Calibration and inference remain
out of scope until that bridge and its discrepancy model close.

## C31/B1A — microscopic-to-TMD source closure

C31 explicitly separates the C11 regulated finite-basis overlap, the formal
project renormalized TMD, and the ART25 optimal TMD. Fourteen primary sources
are version/hash locked. Continuum sources support formal project-to-ART25
convention alignment for an already-renormalized TMD and separately support
the optimal boundary, ζ prescription, and two-scale evolution maps.

No source or theorem covers the actual C11 operator/regulator, and no
operator-identical partonic difference has been calculated. BLFQ is a model-
overlap comparison; LaMET and lattice sources provide analogous matching
methodology only. C31 therefore selects `P-E_UNAVAILABLE` and issues
`NO_SOURCE_QUALIFIED_LF_TO_TMD_MATCHING`. Tree level is limited to an operator
boundary with an `O(alpha_s)` nonzero-unknown remainder.

The microscopic export remains empty-not-zero, the bridge is not rerun, and
all twelve u/d/ubar/dbar points remain `BRIDGE_COMMON_DOMAIN_ONLY`. All 642
external identities, frozen roles, ancestry, `NO_JOINT_MEASURE`, production
routes, and authoritative artifacts remain unchanged.

**Exact next package:** C32/R0 — perform the regulator-specific microscopic
partonic matching calculation specified in
`docs/next_level/c31_missing_calculation_specification.md`, including common IR
regulation, all LF/Wilson/soft/counterterm graphs, and UV/rapidity/IR/gauge and
basis-convergence closure. Do not apply the formal continuum adapter until that
intermediate project TMD exists.

## C32/R0 — operator completion and microscopic soft-sector gate

C32 creates `C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION` without changing C11.
The actual PLAN-A C11 matrices and forward reductions are passed through the
C12 staple kernel at zero coupling for u, d, ubar, and dbar at three x values.
All twelve parents are nonzero and the exact tree-reduction residual is zero.
PLAN-B remains a distinct alternative and is never summed.

The regulator plan uses the exact inherited C7 tower (K=9/2,11/2,13/2;
Nmax=8,10,12; bHO=0.40,0.45,0.50 GeV), with lambda_H=1.2 GeV, x_min=1/18,
the historical boundary conditions, and explicit gluon-zero-mode policy. A
common off-shell partonic IR plan, covariant-gauge checks, modified-delta
rapidity plan, 26 holdouts, and every one-loop graph/counterterm class are
frozen before calculation.

The next gate fails structurally: the C11 finite-basis Hilbert regulator has
no vacuum eikonal sector on which to calculate the required four-line soft
factor. C12/C14 soft ledgers are validation pilots, and copying a continuum
soft factor would not be a C11-regulated calculation. The exact result is
`C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED`. All downstream one-loop residuals
remain unavailable, the export is empty-not-zero, and all twelve bridge points
remain common-domain-only. The preserved source covariance is still 642 x 11,
rank 10, nullity 1; the failed projection remains 642 x 0.

**Exact next package:** C33/S0 — construct the explicit finite-basis vacuum
Wilson soft sector and compatible rapidity/zero-bin subtraction specified in
`docs/next_level/c32_missing_calculation_specification.md`. Only afterward may
the remaining collinear, instantaneous, counterterm, and matching graphs run.

## C33/S0 — finite-basis vacuum/eikonal soft root and one-loop sufficiency gate

C33 creates `C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT` as a distinct
baryon-number-zero root. It shares neither a state vector nor a probability
normalization with the C32 baryon-number-one collinear root. The selected
structural plan is `S0-FB-EIKONAL-FOCK`; the continuum and auxiliary-field
routes remain nonadditive target/method oracles.

The typed runtime in `src/deuteron_wigner/bridge/s0/core.py` implements all 47
required architecture records. Every serialized record carries the common B=0
root, four-line fundamental-singlet geometry, regulator and perturbative
scope, source/target scheme, state independence, and hard-false
data/inference/production reachability. Three nested vacuum-plus-one-gluon
bases have dimensions 3,841, 30,721, and 103,681. Exact zero modes are excluded
from ordinary cells but retained as a separate unresolved control and holdout.
The ordered operator

```text
(1/Nc)<Omega|Tr[S_n^dagger(b) S_nbar(b)
                     S_nbar^dagger(0) S_n(0)]|Omega>
```

has exact `C_F=4/3`, singlet trace, Hermitian/path reversal, and tree value
`S^(0)=1`. Modified-delta denominator signs are derived from the path,
Fourier, momentum-flow, covariant-derivative, and conjugation conventions; no
manual pole sign or physical numerical epsilon is accepted.

All eighteen required one-loop graph/counterterm classes are explicit, but no
regulator-specific finite-basis coefficient exists. Every such coefficient is
`NONZERO_UNKNOWN`. UV and rapidity counterterms, rapidity anomalous dimension,
Collins-Soper kernel, basis trajectory, finite-to-continuum conversion,
C32/C33 compatibility, and zero-bin validation remain unavailable rather than
zero. The continuum expression is source qualified but not relabeled as a
finite-basis calculation; the auxiliary Euclidean/spacelike construction is
methodological only.

The zero-bin map is typed and count-once but not executable. The C32
continuation gate is false, no microscopic proton TMD is exported, and the
twelve-point bridge is not rerun. Frozen C29-C32 roles and holdouts,
`NO_JOINT_MEASURE`, all 642 ART25 identities and source covariance, the
216-route registry, and all eight authoritative artifacts are unchanged.

Primary-source locks are recorded in
`docs/next_level/c33_primary_source_manifest.json`. Four C31 PDFs are reused;
seven additional public PDFs are preserved locally under
`data/raw/c33_sources/`, outside Git, with exact version, URL, SHA-256, and
reconstruction command. Volume XXI was unavailable during the original C33
execution, so no content was inferred in that completion commit.

### Volume XXI integration addendum

The authoritative source is now stored byte-for-byte at
`references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex`
with SHA-256
`613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4`.
Its 65 stable formal requirements are mapped in
`docs/next_level/c33_volume_xxi_requirement_crosswalk.json` to C31--C33
evidence, explicit fail-closed statuses, and C34-or-later dependencies. The
source confirms the two-root collinear/soft architecture and explicitly
permits the tree-level-only branch; it does not supply the missing one-loop
finite-basis calculation. The exact C33 result and next job are unchanged:
`C33_SOFT_TREE_LEVEL_ONLY`, followed by C34/S0A.

Volume XXI sharpens the first C34/S0A execution steps: freeze the perturbative
coupling normalization; provide a gauge-complete BRST/Krein/ghost or equivalent
contraction realization; expand every one-loop record to the full
root/order/color/gauge/UV/IR/rapidity/basis/support/hash/cancellation schema;
split logarithmic, power, residual-mass, cusp, endpoint, vacuum, and basis
counterterms; and assemble one content-addressed C32/C33 joint-regulator
object. Then calculate all 18 soft entries, the signed missing/duplicate
zero-bin defects, and the three-resolution trajectory before reconsidering the
continuation gate.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c33_s0.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c33_manifests.py 1197
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c33.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact outcome:** `C33_SOFT_TREE_LEVEL_ONLY`.

**Exact next package:** C34/S0A — calculate the gauge-fixed B=0 one-loop soft
mode sums, all graph/counterterm classes, finite-basis UV and modified-delta
rapidity renormalization, three-resolution trajectory, continuum conversion,
and C32 soft-limit/zero-bin compatibility. Do not resume the proton export or
bridge until every continuation gate passes.

## C34/S0A — one-loop soft completion audit and Branch-G closure

C34 starts from the clean, Volume-XXI-integrated C33 completion commit
`e0b34c74e8f39c9d42cf49cc598f1533d9353a7e`. The historical prompt count of
1,196 tests described the pre-Volume-XXI C33 commit; the actual immutable
starting tree reproduces 1,197 tests, all C28--C33 validators, 33 builders,
39 evidence rows, 165 atlas pages, 2,140 C33 requirements, 2,040 ordered C33
injections, and 92 inherited fault modes. Exact prompt and Volume XXI hashes
are respectively
`a4a959d2d6401cbf296d6514591b3c5b4c3301a2b5867f0481b83a43d7c374eb`
and
`613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4`.

The additive `bridge/s0a` implementation freezes the
`S0-FB-EIKONAL-FOCK` plan, the continuum normalization
`a_s = g_s^2/(4 pi)^2`, SU(3) fundamental four-line trace, covariant-gauge
axis at `xi_g = 0, 1, 2`, independent modified-delta regulators, proposed
singular-cell quadrature contract, R1--R3 trajectory-fit plan, and 24
pre-result holdouts.
Forty-two immutable objects encode these planned identities and fail-closed
interfaces. The stored four-line current is a symbolic identity derived from
C33, not a gauge-complete executed current or a Ward-identity validation; the
cell example is explicitly nonphysical and no physical cell matrix element
has been integrated. The real/virtual ledger records disjoint structural IDs,
not numerical count-once closure. The eighteen-slot contribution ledger uses
only the six declared statuses and never converts an unknown into a numerical
zero.

The execution audit fails before coefficient calculation at a precisely
identified prerequisite. C33 stores basis dimensions and support descriptors,
but no normalized mode
functions or cell map, measure and dispersion, gauge-fixed B=0 action and
propagator, covariant polarization/BRST/ghost/instantaneous completion,
parameterized Wilson closure, operator-level finite-mode modified-delta
action, or explicit zero-mode sector. Its three resolutions also change
several regulator axes at once. All locked primary sources are continuum or
method authorities and explicitly not operator-regulator identical. These
facts make a unique finite-basis one-loop coefficient and its counterterms
underdetermined; importing the continuum coefficient would violate the
scientific objective.

**Exact outcome:** `C34_SOFT_ONE_LOOP_INCOMPLETE` (Branch G). The continuum
modified-delta expression is retained only as a source-qualified target;
finite-basis coefficients, UV/rapidity counterterms, anomalous dimensions,
conversion, trajectory, and zero-bin equality remain empty-not-zero. The
continuum source expression has not passed an independent direct-integral
reconstruction and is never labeled a finite-basis result. UV, rapidity,
gauge, future/past, count-once, conversion, and trajectory residuals are
unavailable rather than zero. The C32 continuation gate is false. No ART25
input, proton export, bridge rerun, fit, likelihood, inference,
process/deuteron promotion, or production change is created.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c34_manifests.py 1231
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c34.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c34_s0a.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

Final C34 validation used Python 3.9.23 and pytest 8.4.2 from that interpreter.
The complete suite passed 1,231/1,231 tests; the combined C33+C34 focused
suite passed 64/64; validators C28 through C34 all returned their declared
`*_VALIDATION_PASS` status. Two consecutive regenerations of all 52 C34 JSON
deliverables were byte-identical and every embedded content hash verified.
The work remains on branch `main`; after the local completion commit, the only
expected untracked path is the pre-existing `MSHT20_REP/` directory. The
completion commit is intentionally not pushed and can be recovered with
`git log -1 --oneline`.

**Exact next package:** C35/S0C — provide the gauge-complete finite-basis soft
field realization (cells, modes, measures, propagator/cuts, Wilson segments,
zero modes, and renormalization conditions), then calculate the unresolved
soft diagrams and counterterms. Do not start collinear matching, proton export,
or the bridge until the resulting one-loop soft gate genuinely closes.

## C35/S0C — regulator-completion decision and Branch-G no-go

C35 starts from the clean local C34 completion
`6bdb44be2afc79e817f69ce0e35813da8a394db7`. Before edits, that tree
reproduced 1,231 tests and validators C28--C34. The C35 prompt and Volume XXI
hashes are, respectively,
`1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9`
and
`613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4`.
The 74 immutable C33 paths, all 52 historical C34 JSON manifests, 216
production routes, eight authoritative artifacts, all 642 external ART25 identities, the
642-by-11 rank-10/nullity-1 source covariance, and `NO_JOINT_MEASURE` remain
locked. Of the 73 audited C34 package paths, 72 remain byte-identical. The
sole controlled maintenance change is a nonphysics reconstruction guard in
`scripts/build_c34_manifests.py`: historical C34 rebuilds now hash the C34
completion versions of the append-only roadmap and volume index, so later
handoff additions cannot mutate C34 output. Rebuilding still reproduces all
52 C34 JSON manifests byte-for-byte.

The source audit compiles four mutually exclusive plans before coefficient
evaluation. None of the positive candidates supplies the same finite-cell,
lightlike Minkowski modified-delta operator together with a complete gauge
theory. The covariant route lacks the finite-cell BRST/Krein and boundary
complex; the light-front route lacks the complete instantaneous, constrained
zero-mode, and residual-gauge structure; and the auxiliary route lacks an
operator-level conversion to the target. The modified-delta source further
states that its finite-delta Wilson lines do not retain the gauge properties
of the original Wilson lines. The selected plan is therefore
`S0C-UNAVAILABLE`, recorded as a typed supersession of the C34 planned
covariant probe before any result was inspected.

C35 nevertheless closes the exact convention layer. It fixes metric `+---`,
`v+/-=(v0+/-v3)/sqrt(2)`, normalized null vectors with `n.nbar=1`,
`n.k=k-`, `nbar.k=k+`, and the covariant rescaling
`delta- -> lambda delta-`, `delta+ -> lambda^-1 delta+`. It implements the
massless real chart `(kappa,y,phi)` with measure
`kappa d kappa dy d phi/[2(2pi)^3]`, the independent off-shell virtual chart
with `d k+ d k- d2kT/(2pi)^4`, a normalized scalar-cell oracle, the finite-
segment modified-delta damping factor, and explicit principal-value/cut and
finite-delta pole-cell oracles. These are exact kinematic or method records;
they are not relabeled as a gauge-mode collection or a physical loop
quadrature.

All 53 formal architecture classes are frozen, content addressed, and
scope-isolated. The complete eighteen-slot contribution inventory remains
`UNRESOLVED_BLOCKING`/`NONZERO_UNKNOWN`. No bare one-loop coefficient,
counterterm, renormalized soft function, conversion, trajectory, or soft-side
zero-bin value is issued. No continuum coefficient is copied. The C32 gate is
false, the proton export is empty-not-zero, and no ART25 object, bridge
residual, fit, inference object, process/deuteron result, or production route
enters the calculation.

The committed C35 evidence contains 61 JSON manifests, four explanatory
reports, 12 ADRs, 326 C35 coverage rows, 93 distinct fault modes, and 2,511
executed semantic injections targeted across all 53 architecture classes, 18
contribution slots, and 27 holdouts. The final suite passes 1,257 tests; the
C33+C34+C35 focused suite passes 90 tests; validators C28--C35 pass; and two
manifest regenerations are byte-identical. The ignored runtime entry point
writes only a content-addressed Branch-G no-go bundle and cannot emit a
coefficient.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c35_manifests.py 1257
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c35.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c33_s0.py tests/test_c34_s0a.py tests/test_c35_s0c.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/run_c35_soft_calculation.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact outcome:**
`C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE`, with secondary
`C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE` and Branch G.

**Exact next package:** C36/O4 — create a replacement, versioned,
gauge-complete regulator architecture for the microscopic TMD soft root.
Freeze the replacement operator, finite gauge theory, modes, Wilson geometry,
rapidity action, singular-cell prescription, zero modes, boundaries, and
ordered regulator limits before reopening the eighteen one-loop slots. Do not
fill the unavailable C35 descriptor or import the continuum coefficient.

## C36/O4 — gauge-invariant finite-rapidity replacement regulator architecture

Status: **completed locally; validation-only architecture decision.**

C36 preserves C35 as the exact finite-delta modified-delta no-go certificate
(`C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE`; Ward defect
`0.2143273`) and does not reopen its one-loop slots. It selects the unique
physical `O4-SPACELIKE-COLLINS-JMY` family before coefficient evaluation. The
new versioned `C36_GAUGE_INVARIANT_FINITE_RAPIDITY_TMD_ROOT` contains paired,
common-regulator descendants `C36_COLLINEAR_ROOT` (B=1) and
`C36_SOFT_ROOT` (B=0). The universal soft operator remains outside the
hadron TTN and `NO_JOINT_MEASURE` remains unchanged.

The selected spacelike Wilson geometry has finite \(v^2,\bar v^2<0\),
explicit endpoint and transverse closure, a source-qualified Collins/JMY
rapidity invariant and limit order, and a finite-regulator gauge/Ward
identity with zero analytic residual. The auxiliary-field construction is
recorded only as a representation of the same selected geometry. Exponential,
finite-length, and dressed-field alternatives are retained as scoped audits,
not summed soft sectors. Continuum tree/one-loop records are source-qualified
operator oracles only; no finite-basis one-loop coefficient, counterterm,
microscopic TMD, bridge point, or hadron-level matching ratio is issued.

All twelve C11 u, d, ubar, and dbar parents reduce exactly at zero coupling;
this is not one-loop matching. The selected next calculation is a
state-independent partonic difference in the shared finite-rapidity scheme.
ART25 members/data/chi2, bridge residuals, inference, and production are
isolated. The 216 production routes, eight authoritative artifacts, and 642
ART25 identities remain unchanged.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c36_manifests.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c36.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q tests/test_c36_o4.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

**Exact outcome:** `C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY` and
`C36_SPACELIKE_FINITE_RAPIDITY_ARCHITECTURE_VALIDATED`, without a
finite-basis matching result.

**Exact next package:** C37/R2 — spacelike finite-rapidity partonic collinear
calculation, universal soft subtraction, and finite-basis LF-to-project
matching. Do not export a proton TMD or rerun the bridge until that package
closes its regulator-specific calculation gates.

## C37/R2 — finite-basis partonic matching prerequisite audit

Status: **completed locally with exact Branch C37 finite-basis no-go.**

C37 held the C36 `O4-SPACELIKE-COLLINS-JMY` operator fixed and reproduced the
C35/C36 validators and 98 focused tests. The prerequisite audit found no
materialized regulator-identical finite-basis spacelike Wilson insertion,
common-IR partonic external-state realization, full instantaneous/boundary/
zero-mode/Hamiltonian/operator-counterterm sector, discrete distributional
map, or basis trajectory. No coefficient was evaluated or inferred.

**Exact outcome:** `C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE`.

**Exact next package:** C38/M0A — finite-basis spacelike Wilson insertion,
partonic states, and counterterm construction. No proton export or bridge is
authorized.

## C38/M0A — finite-basis partonic matching-probe infrastructure

Status: **completed locally; C39 infrastructure gate ready.**

C38 keeps the C36 spacelike scheme fixed and materializes a separate
color-fundamental, nonhadronic matching-probe root with normalized q/qg
sectors, common mass IR prescription, finite-basis spacelike Wilson path and
transverse closure, constrained/boundary/zero-mode records, counterterm
conditions, discrete distribution functional, and trajectory interfaces.
Tree/first-order infrastructure pilots pass. No one-loop matching kernel,
proton TMD, bridge comparison, ART25 input, or production route is created.

**Exact outcome:** `C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY`.

**Exact next package:** C39/R2B — execute the finite-basis one-loop spacelike
collinear correlator, soft/overlap subtraction, renormalization, and matching difference.

## C39/R2B — fail-closed C38 implementation correction

Status: **completed locally.** C39 audited the claimed C38 readiness and found
only structural records, scalar values, and interfaces.  The historical C38
commit remains unchanged, but its claim is superseded in the descendant record:
`C38_FINITE_BASIS_PARTONIC_INFRASTRUCTURE_READY ->
C38_PARTONIC_STRUCTURAL_SCAFFOLD_ONLY`.  The exact C39 outcome is
`C39_FINITE_BASIS_ONE_LOOP_INCOMPLETE`; no one-loop calculation was invented.

## C40/M0B — executable finite-basis partonic operator substrate

Status: **completed locally.** C40 retains the fixed C36
`O4-SPACELIKE-COLLINS-JMY` scheme and materializes three color-fundamental q/qg
numerical bases, Gram matrices, free Hamiltonians and independent matrix-free
actions, nonzero canonical/adjoint vertices, constrained-sector matrices,
finite-path spacelike Wilson matrices, counterterm system machinery,
distributional measurement matrices, and refinement maps.  The numerical gate
and 96 focused numerical fault tests prevent metadata-only substitution.

**Exact outcome:** `C40_EXECUTABLE_PARTONIC_OPERATOR_SUBSTRATE_READY`.

**Exact next package:** C41/R2B — calculate the finite-basis one-loop
spacelike correlator and common-IR partonic matching difference using C40
runtime arrays.  It must not use the synthetic C40 counterterm RHS as a
physical result or apply anything to the proton/ART25 bridge.

## C41/R2B — C40 regulator-identity audit

Status: **completed locally as Branch B fail-closed.** C41 audited every C40
numerical input before a one-loop calculation.  All required arrays are
executable, but each is a locally defined method/toy recipe rather than a
source-derived, regulator-identical realization of the C36 spacelike
operator.  No C40 object is eligible to enter a physical diagram.

**Exact outcome:** `C41_C40_SUBSTRATE_NOT_REGULATOR_IDENTICAL`.

**Exact next package:** C42/M0C — source-derived correction of the C40
Hamiltonian, constrained, Wilson, measurement, counterterm, and refinement
operators.  No correlator, matching coefficient, proton export, or bridge is
authorized until this identity gate closes.

## C42/M0C — source-authority and gauge-action gate

Status: **completed locally as Branch A fail-closed.** C42 finds the locked
Ji–Ma–Yuan source but no repository copies of the required
Brodsky–Pauli–Pinsky light-front-Hamiltonian authority or
Belitsky–Ji–Yuan residual-gauge/transverse-link authority.  C36 supplies the
spacelike operator architecture, not a complete finite-basis gauge-fixed QCD
action.  No C42 source-derived matrix may therefore be made.

**Exact outcome:** `C42_GAUGE_FIXED_ACTION_INCOMPLETE`.

**Exact next package:** C43/G0 — hash-lock the required primary authorities
and complete one finite-basis gauge action, constraints, residual-gauge
fields, and zero modes before rebuilding the C42 replacements.

## C43/G0 — source-locked light-front gauge action

Status: **completed locally.** C43 acquired and hash-locked BPP v1,
Srivastava--Brodsky v2, BJY v2, JMY v1, and two supporting audits.  It selects
light-front gauge (A^+=0), defines the nonzero-mode PV inverse derivative,
constraints, instantaneous interactions, residual transverse link, zero-mode
contract, JMY compatibility, and physical C32 finite-basis projection
interfaces. No numerical QCD matrices are generated.

**Exact outcome:** `C43_GAUGE_FIXED_ACTION_READY_FOR_BASIS_PROJECTION`.

**Exact next package:** C44/HQCD — source-derived projection into the physical
finite basis and construction of regulator-identical q/qg Hamiltonians,
SU(3) vertices, constrained sectors, Wilson/bilocal operators, and refinement
maps.
