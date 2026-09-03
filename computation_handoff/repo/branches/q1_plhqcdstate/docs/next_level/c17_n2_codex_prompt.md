# C17/N2 Codex work package

## Title

**C17/N2 — Continuum-calibrated \(NN\pi\) transition dynamics and the complete Hamiltonian-consistent exchange-current basis at the declared nuclear order**

## Authoritative baseline

Begin from the local C16/N1 completion commit

```text
6d003279cb93c1a0ae574407ed32fb4594c3b714
```

The scientific C15 ancestor is

```text
cd94d1199202a97bb451aee9085cfc6c0708b8f2
```

A documentation-only descendant of the C16 commit is acceptable only if:

1. `6d003279cb93c1a0ae574407ed32fb4594c3b714` remains in the ancestry;
2. the complete C16 regression reproduces before any scientific edit;
3. no scientific code, manifest, benchmark, or accepted artifact changed in the documentation-only commit.

Do **not** use `origin/main` as the scientific baseline. The authoritative history is local. Do not push the final C17 commit.

## Required normative sources

Read completely and hash-audit the repository copies of:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_iv_matched_spin1_nuclear_dynamics.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_xii_microscopic_wilson_second_order.tex
references/volume_xiii_nnpi_pion_matching_coherent_nuclear.tex
references/model_construction_note.tex
references/formalism_volume_index.md
```

Also read all C15 and C16 reports, APIs, ADRs, manifests, schemas, tests, and handoff records, including at minimum:

```text
docs/next_level/c15_implementation_report.md
docs/next_level/c15_api.md
docs/next_level/c16_implementation_report.md
docs/next_level/c16_api.md
handoff/ROADMAP.md
```

If a named file has moved, locate it through the repository index. Do not invent missing formalism. Record every source path, hash, and availability result in the C17 normative-source manifest.

## Baseline that must reproduce before edits

Before changing code, reproduce and record:

- `982/982` tests;
- every documented C16 builder and validator;
- `36/36` evidence rows;
- `162/162` atlas pages;
- `516/516` C16 requirements;
- `308/308` C16 negative injections;
- every earlier C3–C15 injection suite;
- the unchanged `216`-route production registry;
- all eight authoritative production artifacts byte-identical;
- all sixteen C15 JSON artifacts byte-identical;
- all twenty C16 JSON artifacts byte-identical and deterministic on rebuild;
- the C15 and C16 source-hash and provenance manifests;
- a clean working tree.

If the baseline does not reproduce, diagnose and repair the baseline without changing accepted physics before beginning C17.

# 1. Scientific purpose

C16 established a normalized, spin-resolved

\[
\mathcal H_{N1}=\mathcal H_{NN}\oplus\mathcal H_{NN\pi}
\]

validation state with:

- complete `pn pi0`, `pp pi-`, and `nn pi+` charge content;
- exact charge \(+1\), isospin zero, and \(J^P=1^+\) quantum numbers;
- one three-body recoil authority and a separate number-changing transition map;
- nucleon-active, pion-active, and Hermitian transition operators;
- executable internal-versus-exchange pion subtraction;
- a Hamiltonian-consistent but deliberately incomplete current family;
- a helicity-resolved analytic coherent small-\(x\) pilot;
- separate partonic-Wilson and nuclear-coherent identities;
- complete deuteron helicity parents for \(u,d,\bar u,\bar d,g\) at partonic Wilson orders zero, one, and two.

C16 also left one explicit Jacobian null direction and unfitted transition, pion, tensor, and current holdouts. Its pion-active parent is still an analytic, unmatched oracle; its coherent kernel is not physical shadowing; and its exchange-current family is not complete at the declared nuclear order.

C17 must close that **N1-completion/N2-transition** boundary. It must not jump directly to \(\Delta\Delta\), compact six-quark, hidden-color, or general physical shadowing before the pion-transition and current operators are complete and continuum calibrated.

The central C17 chain is

```text
C16 finite NN + NNPI state
    -> continuum/finite-volume NNPI spectral representation
    -> calibrated NN <-> NNPI transition kernel
    -> Hamiltonian-generated current/operator basis
    -> pole, residue, continuity, angular, GTMD/current, and separator closure
    -> upgraded helicity-resolved coherent pilot
    -> N2 validation state bundle
```

C17 remains validation-only. It is not a physical deuteron TMD, physical pion TMD, complete chiral EFT, physical shadowing/Glauber calculation, LF-to-QCD matching, evolution, process prediction, or inference result.

# 2. Nonnegotiable scientific principles

## 2.1 The continuum cannot be simulated by a fitted imaginary width

A nonzero transition discontinuity or absorptive contribution must arise from a declared spectral measure or a finite-volume/discretized-continuum sequence with a controlled continuum map. Numerical \(i\epsilon\) is only a convergence device and must never enter the physical identity.

## 2.2 “Complete exchange-current basis” has a declared scope

In C17, **complete** means:

> complete under gauging and operator matching of every retained C17 Hamiltonian term at the declared nuclear interaction/current order, regulator, Fock space, and model-space reduction.

It does not mean the complete continuum QCD or all-orders chiral-EFT current.

Every retained Hamiltonian term must have either:

1. all required current/charge attachments in the declared basis;
2. an explicit proof that the term is neutral under the relevant current;
3. or a typed unresolved-current record that prevents the status `DECLARED_ORDER_EXCHANGE_CURRENT_BASIS_COMPLETE`.

## 2.3 Hamiltonian and operators transform together

Any Feshbach, similarity, unitary, separator, or regulator transformation must act on:

- the Hamiltonian;
- charge density;
- electromagnetic current;
- axial and pseudoscalar operators where present;
- energy–momentum operator;
- pion-active and transition partonic operators;
- norm kernel;
- coherent and overlap operators.

Hamiltonian-only elimination is forbidden.

## 2.4 Internal pion, exchange pion, and induced contact descriptions are alternatives with overlap subtraction

The matched relation remains

\[
W_{\pi}^{\rm matched}
=
W_{\pi}^{\rm internal}
+
W_{\pi}^{\rm exchange}
-
W_{\pi}^{\rm overlap}.
\]

Changing the separation scale may move strength among the terms, but the matched sum must be stable within a declared truncation error. No second scalar pion correction may be added after the matched sum.

## 2.5 Partonic Wilson and nuclear coherent propagation remain different mechanisms

C17 must preserve the separate identities

```text
PARTONIC_WILSON_STAPLE
NUCLEAR_COHERENT_PROPAGATION
TAGGED_FINAL_STATE_INTERACTION
```

and retain an executable count-once overlap relation for a shared soft/Glauber region. The partonic Wilson phase budget may not be modified to simulate nuclear shadowing.

# 3. Required package location and reuse

Extend the existing microscopic nuclear package. Prefer a structure such as

```text
src/deuteron_wigner/microscopic/nuclear/n2/
```

or the repository’s established C15/C16 namespace.

Reuse, do not duplicate:

- C15/C16 `NuclearMember` identities;
- the N0 and N1 state bundles;
- the C15 spectator-preserving recoil map;
- the C16 three-body recoil authority;
- the C16 number-changing transition recoil map;
- spin-1 projector and tensor-sign adapters;
- microscopic H7 proton/neutron parents;
- Wilson-order/link/color identities;
- the C16 pion-overlap projector;
- current ledgers, provenance graph, TTN, CP-map, and coherent-kernel types;
- all formal coordinate, rank, operator, map-class, and diagnostic types.

Do not create a parallel type system.

# 4. Continuum-calibrated NNPI dynamics

## 4.1 Typed continuum channels

Implement a typed `NNPiContinuumChannel` carrying at least:

- charge channel (`pn_pi0`, `pp_pi_minus`, `nn_pi_plus`);
- total charge, isospin, \(J^P\), and \(J^z\);
- nucleon-pair spin and isospin;
- pion charge and intrinsic parity;
- Jacobi orbital labels and coupled partial waves;
- invariant energy or invariant mass;
- threshold identity;
- spectator and active-particle assignments;
- regulator and endpoint policy;
- finite-volume or continuum normalization convention;
- nuclear member and assumption-plan identity.

The continuum states obey a declared normalization such as

\[
\langle E',\alpha'|E,\alpha\rangle
=
\delta_{\alpha'\alpha}\,\delta(E'-E)
\]

or the explicitly documented finite-volume counterpart.

## 4.2 Continuum transition kernel

Implement the Hermitian transition family

\[
V_{NN\leftrightarrow NN\pi}(E)
\]

with generated adjoints and complete spin, isospin, charge, orbital, momentum, regulator, and member identity.

The transition kernel must support:

- the finite C16 basis as a controlled projection;
- an analytic continuum oracle;
- a finite-volume/discretized-continuum sequence;
- comparison and matching maps among them.

## 4.3 Spectral self-energy and pole residue

For \(P\) projecting to the \(NN\) sector and \(Q\) to \(NN\pi\), construct

\[
\Sigma(E)
=
PVQ\frac{1}{E-QHQ+i0}QVP,
\]

with

\[
\operatorname{Im}\Sigma(E)
=
-\pi\,PVQ\,\rho_{NN\pi}(E)\,QVP
\]

inside support and exact zero below threshold.

Track:

- the deuteron pole condition;
- the residue or wave-function-renormalization factor;
- the derivative \(\partial_E\Sigma\);
- principal-value and cut contributions separately;
- charge-channel and partial-wave decomposition;
- finite-volume-to-continuum convergence;
- regulator and threshold sensitivity.

A finite numerical width must not create physical support.

## 4.4 Calibration and holdouts

Use only a restricted calibration set, for example:

- the N1 pole or mass condition;
- one transition or spectral normalization condition;
- one low-energy charge/isospin condition;
- one current normalization condition already owned by the Hamiltonian.

Freeze before optimization at least:

- a second transition-energy point;
- one spectral moment or pole-residue observable;
- one pion-active partonic moment;
- one tensor transition observable;
- one current component;
- one angular-condition diagnostic;
- one coherent-amplitude observable.

Do not fit a separate coefficient to a pion TMD, tensor TMD, or named deuteron distribution.

# 5. Finite-volume/discretized-continuum route

Implement a controlled sequence of spectral approximations with increasing level count or volume. Each point must retain:

- volume or discretization identity;
- level energies and weights;
- threshold location;
- channel labels;
- map to the continuum spectral measure;
- quadrature/smearing parameter;
- convergence diagnostics.

The sequence must demonstrate convergence for:

- self-energy principal value;
- discontinuity/cut weight;
- pole shift and residue;
- transition matrix elements;
- one current matrix element;
- one pion-active partonic moment.

Do not call the map “Lüscher” or “Lellouch–Lüscher” unless all hypotheses and formulas of that construction are actually implemented. Otherwise use a neutral typed name such as `FiniteVolumeSpectralMap`.

# 6. Hamiltonian-generated exchange-current basis

## 6.1 Generate currents from the retained Hamiltonian

Implement a current-generation or gauging layer so that every retained C17 Hamiltonian term has a current attachment ledger. A suitable abstract relation is

\[
J^\mu
=
-\left.\frac{\delta H[A]}{\delta A_\mu}\right|_{A=0},
\]

supplemented by explicit gauging of nonlocal regulators, momentum-dependent kernels, and sector-changing vertices.

The implementation may use analytic formulas, automatic differentiation of gauged kernels, or a verified symbolic adapter, but it must not hand-assemble a numerically convenient current unrelated to the Hamiltonian.

## 6.2 Required operator families

At the declared C17 order, build and classify at least:

```text
NUCLEON_ONE_BODY_CHARGE_CURRENT
PION_IN_FLIGHT_CURRENT
NN_TO_NNPI_TRANSITION_CURRENT
NNPI_TO_NN_TRANSITION_CURRENT
CONTACT_OR_SEAGULL_CURRENT
PAIR_CURRENT
RECOIL_OR_RETARDATION_CURRENT
MOMENTUM_DEPENDENT_INTERACTION_CURRENT
REGULATOR_GAUGING_CURRENT
INDUCED_FESHBACH_CURRENT
CURRENT_COUNTERTERM
CHARGE_DENSITY_CORRECTION
EMT_ONE_BODY_AND_INTERACTION_TERMS
AXIAL_PSEUDOSCALAR_COMPANIONS_WHERE_SUPPORTED
```

The exact basis must be derived from the Hamiltonian and operator order. If one named class is absent because its source Hamiltonian term is absent, record that as a proof-backed omission, not as an assumed zero.

## 6.3 Current-completeness certificate

Create a machine-readable `CurrentBasisCompletenessCertificate` mapping every retained Hamiltonian term to:

- its charge assignment;
- all required current attachments;
- longitudinal versus transverse status;
- source and target sectors;
- regulator-gauging terms;
- contact partners;
- induced-operator partners;
- counterterms;
- Ward/continuity identities in which it participates;
- unresolved transverse low-energy constants, if any.

No `DECLARED_ORDER_EXCHANGE_CURRENT_BASIS_COMPLETE` status may be issued unless the certificate has no unexplained gap.

# 7. Continuity, Ward, and angular-condition closure

## 7.1 Finite-basis nuclear continuity identity

Require

\[
q_\mu J^\mu_{N2}
=
[H_{N2},\rho_{N2}]
+
\delta_{\rm trunc}.
\]

Decompose the signed residual into at least:

```text
ONE_BODY_NUCLEON
PION_IN_FLIGHT
TRANSITION
CONTACT_SEAGULL
PAIR
RECOIL_RETARDATION
MOMENTUM_DEPENDENT_INTERACTION
REGULATOR_GAUGING
INDUCED_FESHBACH
CURRENT_COUNTERTERM
BASIS_TRUNCATION
CONTINUUM_DISCRETIZATION
```

Removing every nonzero required contribution must produce a signed nonzero defect.

## 7.2 Blockwise identities

Test continuity separately in:

- `NN -> NN`;
- `NN -> NNPI`;
- `NNPI -> NN`;
- `NNPI -> NNPI`;
- each charge channel;
- each supported helicity/tensor block.

A cancellation visible only after summing incompatible channels is not sufficient.

## 7.3 Spin-1 current closure

Retain and improve:

- charge normalization;
- magnetic and quadrupole structures;
- direct-current versus GTMD/GPD moment closure;
- the spin-1 light-front angular condition;
- component-to-component consistency;
- pure-S, zero-D, zero-pion, and zero-transition limits.

Do not fit a separate coefficient for each current component or transfer.

# 8. Pion-active and transition partonic operators

## 8.1 Continuum-calibrated pion-active nuclear splitting amplitude

Replace the purely analytic C16 splitting amplitude within the C17 validation root by a continuum-calibrated nuclear pion-transition amplitude. Preserve the C16 analytic pion parent as an immutable oracle.

The continuum calibration concerns the **nuclear splitting/transition amplitude**. It does not by itself make the internal pion quark/gluon correlator a physical matched pion TMD.

## 8.2 Pion partonic parent status

The pion-active quark, antiquark, and gluon parent must retain:

```text
VALIDATION_ONLY
PION_PARTON_PARENT_UNMATCHED
LINK_SHORTENING_REQUIRED
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
NO_EVOLUTION_APPLIED
NO_PROCESS_MAP_APPLIED
```

No independent deuteron normalization may be fitted to it.

## 8.3 Transition operators

Construct continuum-aware

\[
\widehat{\mathcal O}_{NN\leftrightarrow NN\pi}
\]

for supported vector, axial, pseudoscalar, EMT, and partonic operator blocks. Retain source and target sector, continuum channel, transfer sharing, helicities, pion charge, Wilson order, and matching status.

# 9. Separator flow and explicit/induced equivalence

## 9.1 Separator trajectory

Introduce a typed separator or resolution parameter \(\Lambda_\pi\) controlling the division between:

- pion-like configurations internal to the microscopic nucleon;
- explicit inter-nucleon \(NN\pi\) configurations;
- induced contact/current operators.

For several separator values, report the flow of:

- internal pion contribution;
- exchange pion contribution;
- overlap subtraction;
- induced Hamiltonian term;
- induced current;
- pion-active partonic moment;
- transition tensor observable;
- matched total.

The matched total must be stable within the declared truncation error.

## 9.2 Feshbach equivalence with currents

Verify

\[
H_{\rm eff}(E)
=
PHP+PHQ(E-QHQ)^{-1}QHP
\]

and

\[
O_{\rm eff}(E',E)
=
P[1+\omega^\dagger(E')]O[1+\omega(E)]P
\]

for:

- vector charge/current;
- axial/pseudoscalar operator where supported;
- EMT operator;
- pion-active partonic operator;
- transition operator;
- norm kernel.

The correct provenance relation is

```text
EXPLICIT_CONTINUUM_NNPI
    EQUIVALENT_TO
INDUCED_NN_OPERATOR_SET
    + TRANSFORMED_CURRENTS
    + TRANSFORMED_PARTONIC_OPERATORS
    + VISIBLE_REMAINDER
```

Never `EXPLICIT_NNPI ADD_TO INDUCED_PION_CORRECTION`.

# 10. Coherent small-x upgrade

Upgrade the C16 analytic helicity pilot so that its elementary transition amplitudes may consume the continuum-calibrated N2 transition kernel.

The result must still be labeled a pilot unless physical diffractive inputs, normalization, and factorization are supplied.

Require:

- explicit helicity amplitudes;
- channel-resolved continuum intermediate states;
- propagation phases and longitudinal ordering;
- scalar, vector, and tensor projections after amplitude composition;
- exact zero when either elementary amplitude vanishes;
- ordering reversal;
- failure of a copied unpolarized ratio;
- separate partonic/nuclear overlap subtraction;
- amplitude combination before partial trace.

Do not claim physical shadowing or Glauber dynamics.

# 11. Completely positive reductions

Retain the amplitude embedding

\[
\mathcal E(\rho)
=
\operatorname{Tr}_{\rm unresolved}[V\rho V^\dagger]
\]

only after continuum, transition, and coherent amplitudes are combined.

Demonstrate that premature tracing changes at least one interference, tensor, or current observable. The CP/Kraus representation must agree with the explicit partial trace within tolerance.

# 12. Tensor-network and numerical realization

Extend the N1 TTN to represent the continuum/discretized-continuum branch without hiding it inside a scalar effective tensor.

Required identities include:

- sector root (`NN`, `NNPI_DISCRETE`, `NNPI_CONTINUUM_ORACLE`);
- charge channel;
- continuum energy/level index;
- partial wave and Jacobi orbital;
- pion charge/isospin;
- nucleon helicities;
- deuteron helicity;
- S/D ancestry;
- current/operator channel;
- separator and regulator;
- microscopic proton/neutron member;
- partonic Wilson order and link/color identity.

Compare:

1. exact small-space diagonalization;
2. matrix-free Krylov;
3. full-bond TTN;
4. at least two reduced-bond TTNs;
5. finite-volume/discretized-continuum sequences.

Report separate convergence for:

- energy/pole position;
- pole residue;
- \(Z_{NN\pi}\);
- transition matrix element;
- pion-active moment;
- each required current component;
- continuity residual;
- angular condition;
- tensor transition signal;
- coherent tensor pilot;
- separator-stable matched total.

At least one reduced-bond state must retain a deceptively good norm or energy while losing a real transition/current/tensor observable.

# 13. Assumption plans

Compile at least the following mutually exclusive plans:

```text
N2-PLAN-A
    continuum-calibrated NNPI transition
    full declared-order exchange-current basis
    AV18-derived NN branch
    H7 PLAN-A microscopic proton/neutron members
    explicit internal/exchange overlap subtraction

N2-PLAN-B
    finite-volume/discretized-continuum transition sequence
    same current-generation rules
    Norfolk-derived NN branch
    H7 PLAN-A microscopic proton/neutron members

N2-PLAN-C
    continuum-calibrated transition
    AV18-derived NN branch
    H7 PLAN-B microscopic proton/neutron members

N1-REFERENCE
    immutable C16 analytic-transition parent
    read-only comparison
```

The branches may be compared but never added. A continuum branch and its finite-volume approximation may be compared through a matching map, not treated as two physical mechanisms.

# 14. Required software objects

Implement or extend typed objects such as:

```text
N2Resolution
NNPiContinuumChannel
ContinuumSpectralDensity
FiniteVolumeSpectralMap
NNPiTransitionKernel
DeuteronPoleAndResidue
ContinuumCalibrationManifest
GaugedHamiltonianTerm
ExchangeCurrentOperator
CurrentBasisCompletenessCertificate
BlockContinuityLedger
SeparatorTrajectory
PionTransitionOperator
ExplicitInducedPionComparison
ContinuumCoherentKernel
N2StateBundle
N2TensorNetworkManifest
N2ConvergenceManifest
N2PredictionPlan
N2Provenance2Complex
```

Use established project naming when equivalent types already exist.

# 15. Required benchmark families

Create stable benchmark IDs and deterministic manifests for at least:

1. **N2-A — analytic separable continuum:** exact principal value, threshold, cut, pole shift, and residue.
2. **N2-B — finite-volume convergence:** discrete levels converge to the analytic continuum oracle.
3. **N2-C — charge-complete continuum channels:** `pn pi0`, `pp pi-`, `nn pi+` close charge, isospin, parity, and normalization.
4. **N2-D — transition-kernel Hermiticity:** emission and absorption are exact adjoints.
5. **N2-E — Hamiltonian gauging:** every retained Hamiltonian term has a certified current attachment or proof-backed neutral status.
6. **N2-F — blockwise continuity:** all sector and charge blocks satisfy the declared finite-basis identity.
7. **N2-G — current-component and angular closure:** charge, magnetic, quadrupole, angular condition, and GTMD/current moment routes.
8. **N2-H — separator flow:** internal, exchange, overlap, induced, and matched totals vary correctly.
9. **N2-I — Feshbach Hamiltonian/operator equivalence:** currents and partonic operators transform with the Hamiltonian and retain visible remainders.
10. **N2-J — continuum-calibrated pion-active route:** direct and sequential reductions close without a fitted pion normalization.
11. **N2-K — transition tensor signal:** one tensor observable requires the proper transition partial waves and vanishes under the correct ablation.
12. **N2-L — coherent continuum pilot:** zero, ordering, helicity, tensor, and overlap-subtraction limits.
13. **N2-M — CP reduction:** post-coherence partial trace agrees with Kraus form; premature trace fails.
14. **N2-N — exact/Krylov/TTN agreement:** full bond equals exact; reduced bond loses a real transition/current feature.
15. **N2-O — tagged-inclusive closure:** continuum/pion-resolved tagged integration recovers the inclusive parent.
16. **N2-P — holdout prediction:** at least one transition, current, tensor, pion, and coherent observable remains unfitted.
17. **N2-Q — provenance normalization:** explicit, induced, overlap, current, coherent, and CP paths are counted exactly once.
18. **N2-R — downstream gates:** production, physical matching, evolution, process, inference, and unsupported non-nucleonic sectors fail closed.

# 16. Negative-injection suite

Add at least **340 new ordered C17 negative injections**, each with a stable ID, expected failure class, and deterministic diagnostic.

The suite must cover at least:

## Continuum and spectral support

- support below threshold;
- physicalized numerical epsilon;
- wrong continuum normalization;
- duplicated level weight;
- omitted charge channel;
- incorrect threshold;
- wrong principal-value sign;
- wrong cut sign;
- missing pole-derivative term;
- incorrect residue normalization;
- finite-volume map used outside validity;
- false claim of a Lüscher-type map without its hypotheses;
- merged distinct partial waves;
- lost continuum channel identity.

## Hamiltonian and transition dynamics

- missing transition adjoint;
- inconsistent regulator between emission and absorption;
- wrong parity or orbital selection;
- charge/isospin mismatch;
- hidden refit of a holdout;
- duplicated transition kernel;
- continuum and analytic reference added together;
- mixed assumption plans;
- unresolved Jacobian direction silently fixed by a TMD coefficient.

## Exchange-current completeness

- retained Hamiltonian term with no current attachment;
- current attachment with no source Hamiltonian term;
- omitted pion-in-flight term;
- omitted transition term;
- omitted contact/seagull term;
- omitted pair term;
- omitted recoil/retardation term;
- omitted momentum-dependent interaction current;
- omitted regulator-gauging current;
- omitted induced Feshbach current;
- wrong charge density;
- independent current normalization per component;
- current from a different Hamiltonian identity;
- gauged kernel with mismatched regulator;
- false `COMPLETE` status with an unexplained current gap.

## Continuity and angular closure

- cancellation only after mixing incompatible charge channels;
- wrong commutator sign;
- missing block contribution;
- component-specific fit;
- angular condition repaired with an unrelated coefficient;
- current/GTMD moment mismatch hidden by normalization;
- pure-S or zero-pion limit failure.

## Pion separation and provenance

- internal plus exchange without subtraction;
- duplicate subtraction;
- explicit sector plus fully induced replacement;
- separator-dependent matched total outside tolerance;
- missing transformed current;
- missing norm kernel;
- hidden remainder;
- second scalar pion correction;
- analytic pion oracle promoted to physical pion TMD;
- independent pion normalization.

## Coherent and CP structure

- copied unpolarized shadowing ratio;
- coherent correction with one elementary amplitude zero;
- wrong longitudinal-order phase;
- partonic Wilson and nuclear coherent identity alias;
- missing parton–nuclear overlap subtraction;
- duplicate overlap subtraction;
- trace before amplitudes are combined;
- CP map used to replace resolved coherence;
- physical-shadowing status without physical diffractive input.

## Tensor-network and numerical convergence

- full-bond mismatch;
- reduced bond silently renormalized;
- energy-only convergence accepted despite transition/current loss;
- continuum-level index dropped from an edge;
- charge channel dropped from an edge;
- separator identity dropped;
- stale cache after current, regulator, or continuum change;
- non-deterministic manifest.

## Downstream and production isolation

- mutation of the 216-route production registry;
- mutation of any authoritative artifact;
- physical TMD/GTMD status;
- LF-to-QCD matching completion;
- Collins–Soper evolution;
- process hard factor;
- physical pion distribution;
- physical shadowing/Glauber status;
- \(\Delta\Delta\), six-quark, or hidden-color promotion;
- inference or calibration on production data;
- push to remote.

# 17. Required output manifests and documentation

Create deterministic machine-readable outputs, including at minimum:

```text
docs/next_level/c17_implementation_report.md
docs/next_level/c17_api.md
docs/next_level/c17_requirement_coverage.json
docs/next_level/c17_injection_manifest.json
docs/next_level/c17_regression_report.json
docs/next_level/c17_normative_source_integration.json
docs/next_level/c17_continuum_calibration_manifest.json
docs/next_level/c17_finite_volume_spectral_map.json
docs/next_level/c17_pole_residue_report.json
docs/next_level/c17_current_basis_certificate.json
docs/next_level/c17_continuity_closure_report.json
docs/next_level/c17_separator_trajectory.json
docs/next_level/c17_explicit_induced_pion_comparison.json
docs/next_level/c17_pion_active_closure_report.json
docs/next_level/c17_coherent_continuum_manifest.json
docs/next_level/c17_cp_reduction_report.json
docs/next_level/c17_tensor_network_manifest.json
docs/next_level/c17_convergence_manifest.json
docs/next_level/c17_provenance_complex.json
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

only as appropriate and without modifying normative sources except to add an explicitly supplied new volume.

All generated outputs must rebuild byte-for-byte.

# 18. Acceptance criteria

C17/N2 is complete only when all of the following pass:

1. The complete C16 baseline reproduces before edits.
2. Continuum and finite-volume spectral routes exist with typed normalization and support.
3. The finite-volume route converges to the analytic continuum oracle within a declared tolerance.
4. Pole position, residue, principal-value, and cut ledgers close.
5. Below-threshold absorption is exactly zero.
6. Numerical epsilon is absent from physical result identities.
7. The transition kernel is Hermitian with generated adjoints.
8. Every retained Hamiltonian term has a certified current attachment or proof-backed neutral status.
9. The declared-order exchange-current basis has no unexplained gap.
10. Blockwise continuity closes for all sectors and charge channels.
11. Charge, magnetic, quadrupole, current-component, and angular-condition diagnostics pass within declared tolerances.
12. Direct-current and GTMD/GPD-moment routes close without independent normalization.
13. The continuum-calibrated pion-active route closes and remains explicitly unmatched.
14. Internal, exchange, overlap, and induced pion descriptions form a stable matched sum under separator variation.
15. Feshbach elimination transforms Hamiltonian, currents, partonic operators, and norm kernel consistently with a visible remainder.
16. The upgraded coherent pilot is helicity resolved and remains explicitly nonphysical.
17. Partonic Wilson and nuclear coherent sectors remain distinct with count-once overlap subtraction.
18. CP/Kraus reduction is derived only after coherent amplitudes are combined.
19. Exact, Krylov, full-bond, reduced-bond, and continuum-discretization convergence are reported separately.
20. At least one transition, pion, tensor, current, and coherent holdout remains unfitted.
21. All new negative injections pass.
22. All previous C3–C16 injections remain passing.
23. The 216-route production registry and production provenance remain unchanged.
24. All eight authoritative artifacts remain byte-identical.
25. All C15 and C16 manifests remain byte-identical.
26. All C17 manifests rebuild deterministically.
27. The strongest statuses remain qualified and validation-only.
28. \(\Delta\Delta\), compact six-quark, hidden-color, physical matching, evolution, process, and inference gates remain closed.
29. The working tree is clean.
30. A final local commit is created and is not pushed.

# 19. Allowed readiness statuses

C17 may issue only narrowly qualified statuses such as:

```text
N2_CONTINUUM_NNPI_TRANSITION_VALIDATED
N2_FINITE_VOLUME_TO_CONTINUUM_MAP_VALIDATED
N2_POLE_AND_RESIDUE_BENCHMARKED
N2_DECLARED_ORDER_EXCHANGE_CURRENT_BASIS_COMPLETE
N2_FINITE_BASIS_CONTINUITY_CLOSED
N2_SEPARATOR_STABILITY_VALIDATED
N2_PION_ACTIVE_ROUTE_VALIDATED_UNMATCHED
N2_COHERENT_CONTINUUM_PILOT_VALIDATED
N2_CP_REDUCTION_VALIDATED
N2_TTN_CONTINUUM_BRANCH_VALIDATED
N2_VALIDATION_ONLY
```

It must not issue:

```text
PHYSICAL_PION_TMD
PHYSICAL_DEUTERON_TMD
PHYSICAL_SHADOWING_READY
NUCLEAR_GLAUBER_READY
COMPLETE_CHIRAL_EFT
FULL_CONTINUUM_CURRENT_BASIS
DELTADELTA_READY
SIX_QUARK_READY
HIDDEN_COLOR_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

# 20. Final response and commit

Create a local commit with a clear message such as

```text
Implement C17 N2 continuum pion transitions and exchange currents
```

Do not push.

The final response must report:

- starting and final commits;
- complete regression counts;
- requirement and injection counts;
- continuum and finite-volume dimensions;
- thresholds and normalization conventions;
- pole and residue diagnostics;
- current-basis completeness status;
- maximum continuity and angular-condition residuals;
- separator-stability residual;
- Feshbach remainder norms;
- TTN and continuum-discretization convergence;
- holdout results;
- issued readiness statuses;
- all remaining physical limitations;
- the exact recommended next package.

## Recommended next package after successful C17

If the continuum-transition, exchange-current, separator, and coherent-overlap gates close, the next package should be:

> **C18/N3 — explicit \(\Delta\Delta\) and compact six-quark/hidden-color sectors, transition currents, normalized non-nucleonic interference, and upgraded coherent nuclear amplitudes.**

If any current-basis or separator-flow defect remains parametrically larger than the declared N2 truncation error, recommend a narrower C17-completion package instead of promoting additional sectors.
