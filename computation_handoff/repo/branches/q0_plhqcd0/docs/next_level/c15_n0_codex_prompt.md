# C15/N0 Codex Work Package

## Matched spin-1 nuclear light-front state and microscopic deuteron GTMD composition

### Authoritative starting point

Begin from local commit:

```text
141b1d39604aecfb71bd877e2dfa6d2ce00ef803
```

This C14/H7 commit must remain in the ancestry of the final C15 commit. A documentation-only descendant is acceptable if and only if the complete C14 baseline reproduces before any C15 code is changed.

Do **not** reset to `origin/main`, merge from the remote, rebase away any local microscopic commits, or replace local work with a public-repository state. The authoritative branch is the local branch containing the commit above.

Do not push the final commit.

---

# 1. Objective

Implement the first matched spin-1 nuclear package, **C15/N0**, as an isolated validation root built on the completed H7 microscopic proton/neutron parents.

The central chain is

```text
correlated H7 proton/neutron microscopic members
    -> typed two-nucleon light-front spin-1 state
    -> one normalized NN deuteron member
    -> authoritative nuclear recoil and off-forward spectral amplitude
    -> matched one-body nuclear partonic operator
    -> microscopic deuteron quark/antiquark/gluon GTMD helicity parent
    -> U/L/T/LL/LT/TT reductions
    -> TMD/GPD/PDF/current/EMT/b1/tagged closures
    -> tensor-network and nuclear-resolution convergence manifests
```

C15 must construct a genuine **spin-1 nuclear amplitude and operator composition**, not multiply a nucleon TMD by a scalar deuteron correction.

The package must preserve the complete H7 microscopic identity:

- proton versus neutron;
- quark, antiquark, and gluon species;
- flavor;
- target and parton helicities;
- Fock-sector ancestry;
- OAM structure;
- H7 assumption plan;
- regulator and resolution;
- Wilson order;
- ordered gluon links;
- independent gluon `f` and `d` color channels;
- exact/full-bond/reduced-bond solver identity;
- common microscopic-member identity.

The N0 state is initially restricted to the normalized **nucleonic `NN` sector**. The following nuclear sectors and mechanisms remain typed but unavailable in C15:

```text
NNPI
DELTADELTA
SIX_QUARK
HIDDEN_COLOR
COHERENT_SHADOWING
ANTISHADOWING
NUCLEAR_GLAUBER_RESCATTERING
FULL_EXCHANGE_CURRENT_BASIS
```

Do not represent any unavailable mechanism by an arbitrary scalar correction, fitted ratio, Gaussian, or after-the-fact normalization.

---

# 2. Normative sources and authority hierarchy

Read the following sources completely when present in the repository:

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
references/model_construction_note.tex
```

Also read:

```text
docs/next_level/c14_implementation_report.md
docs/next_level/c14_api.md
docs/next_level/c14_*manifest*.json
handoff/ROADMAP.md
```

Use this authority order:

1. exact equations and physical requirements in the formalism volumes;
2. typed APIs and validated identities in C1-C14;
3. immutable production-regression constraints;
4. existing implementation details that do not conflict with 1-3.

Record every normative source found, missing, or hash-mismatched in a machine-readable C15 source-integration manifest. Do not invent the content of a missing source.

Volume IV is the primary N0 physics specification. C14/H7 is the authoritative microscopic nucleon input.

---

# 3. Immutable baseline gates

Before edits, reproduce and record:

- `945` existing tests passing;
- every existing acceptance builder and architecture validator;
- `36/36` evidence rows;
- `162/162` atlas pages;
- all C3-C14 injection suites, including `184/184` C14 injections;
- all `390/390` C14 requirements;
- the production registry exactly at `216` routes;
- all eight authoritative output files byte-identical;
- all C13 generated manifests byte-identical;
- all pinned C5-C14 microscopic and Wilson manifests byte-identical;
- the production provenance graph and default composition plan unchanged.

The final C15 run must reproduce all of these gates in addition to the new C15 tests.

C15 must not change accepted numerical parents, production conventions, canonical registry names, production wave-function choices, evidence classifications, or output bytes.

---

# 4. Scientific scope and nonclaims

C15/N0 is a regulated finite-resolution **nuclear validation calculation**. It may issue qualified statuses for:

```text
NN_SPIN1_STATE_VALIDATED
NUCLEAR_RECOIL_VALIDATED
OFFFORWARD_SPECTRAL_AMPLITUDE_VALIDATED
MICROSCOPIC_DEUTERON_COMMON_PARENT_VALIDATED
SPIN1_PROJECTOR_CLOSURE_VALIDATED
IMPULSE_GTMD_REDUCTION_VALIDATED
DEUTERON_CURRENT_BENCHMARKED
B1_REDUCTION_BENCHMARKED
TAGGED_INCLUSIVE_CLOSURE_VALIDATED
NUCLEAR_TTN_VALIDATED
```

It must not issue:

```text
PHYSICAL_DEUTERON_EIGENSTATE
COMPLETE_NUCLEAR_HAMILTONIAN
FULL_TWO_BODY_CURRENT_READY
NNPI_READY
COHERENT_SHADOWING_READY
NUCLEAR_WILSON_READY
PHYSICAL_DEUTERON_GTMD
PHYSICAL_DEUTERON_TMD
LF_TO_QCD_MATCHING_READY
TMD_EVOLUTION_READY
PROCESS_PREDICTION_READY
INFERENCE_READY
PRODUCTION_READY
```

The N0 output remains unmatched and must retain at least:

```text
REGULATED_FINITE_BASIS_NUCLEAR_PARENT
LINK_SHORTENING_REQUIRED
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
CONTINUUM_NUCLEAR_CURRENT_INCOMPLETE
NO_COLLINS_SOPER_EVOLUTION
NO_PROCESS_MAP_APPLIED
NO_NUCLEAR_COHERENT_RESCATTERING
```

---

# 5. Required package structure

Extend the existing formal/microscopic architecture rather than creating a parallel type system. Add a package such as

```text
src/deuteron_wigner/nuclear/n0/
```

or an equivalently isolated, well-justified location.

Core objects must include, or extend existing equivalents of:

```text
NuclearResolution
NuclearAssumptionBundle
NuclearPredictionPlan
NuclearSectorId
NuclearMomentumFiber
NuclearRecoilMap
TwoNucleonBasisState
Spin1CouplingChannel
DeuteronLFState
NuclearStateTensorNetwork
NuclearMember
OffForwardSpectralAmplitude
NuclearOperatorId
MatchedOneBodyNuclearOperator
MatchedTwoBodyBenchmarkOperator
DeuteronPartonHelicityParent
Spin1ProjectorRegistry
DeuteronReductionRegistry
DeuteronCurrentOperator
DeuteronCurrentClosureManifest
B1ClosureManifest
TaggedSpectatorKernel
TaggedInclusiveClosureManifest
NuclearConvergenceManifest
NuclearProvenanceComplex
NuclearReadinessManifest
```

Reuse existing C1-C14 types for coordinates, rank, Wilson paths, operator identity, map classes, Fock sectors, microscopic state bundles, helicity matrices, GTMD parents, TTNs, cut ledgers, and provenance relations.

---

# 6. Nuclear assumption plans

Implement immutable, mutually exclusive nuclear plans. At minimum:

```text
N0-PLAN-A
    central high-quality NN S/D wave-function route
    preferred existing repository baseline, normally AV18 when available
    light-front spin rotation and exact recoil
    H7 PLAN-A correlated proton/neutron member
    one-body matched partonic operator
    minimal Hamiltonian-consistent two-body current benchmark

N0-PLAN-B
    alternative high-quality NN S/D wave-function route
    normally CD-Bonn when available
    otherwise the next fully available, documented high-quality repository member
    same operator and closure requirements
    H7 PLAN-A correlated proton/neutron member

N0-PLAN-C
    same central nuclear state as PLAN-A
    H7 PLAN-B nucleon dynamics
    used to expose microscopic-nucleon assumption dependence

N0-ANALYTIC-ORACLE
    normalized analytic weak-binding S/D state
    validation only
    never a production or calibration state
```

If the repository already supports Norfolk members, expose them as additional **alternative nuclear members**, not additive amplitudes.

A nuclear member identity must contain:

- nuclear plan ID;
- wave-function or nuclear-Hamiltonian source hash;
- H7 proton/neutron plan and member IDs;
- nuclear resolution;
- spin-rotation convention;
- current/operator identity;
- recoil-map version;
- Wilson-order support;
- solver and TTN identity;
- provenance and readiness status.

Reject:

- adding AV18 and CD-Bonn amplitudes together;
- mixing H7 PLAN-A proton with H7 PLAN-B neutron;
- mixing resolutions or Wilson orders inside one member;
- replacing the neutron by a copied proton array;
- assigning independent proton and neutron nuisance normalizations;
- treating a wave-function family as additive uncertainty.

---

# 7. Nuclear light-front kinematics

Use explicit deuteron and active-nucleon variables:

```text
x_D = k^+ / P_D^+
y   = p_N^+ / P_D^+
z   = x_D / y
```

Store the adapter to the project nucleon-scaled convention, for example `x_N = 2 x_D`, as an explicit typed conversion. Never infer it from a filename or grid.

At zero skewness:

\[
P_i=P-\frac{\Delta}{2},\qquad
P_f=P+\frac{\Delta}{2},\qquad
\Delta^+=0.
\]

The deuteron operator acts between distinct nuclear momentum fibers.

For an active nucleon of fraction `y`, define one authoritative spectator-preserving recoil map:

\[
\bm\kappa_T^{\rm in}
=
\bm p_T-\frac{1-y}{2}\bm\Delta_T,
\qquad
\bm\kappa_T^{\rm out}
=
\bm p_T+\frac{1-y}{2}\bm\Delta_T.
\]

The active nucleon receives the full physical transfer:

\[
p_f-p_i=\Delta,
\]

while the physical spectator momentum is unchanged.

The recoil object must also support typed transfer partition for a two-body operator. A local two-body routine may not silently invent a factor of `y`, `1-y`, or `1/2`.

Mandatory exact tests:

- intrinsic transverse closure;
- physical active transfer;
- unchanged spectator momentum;
- unit Jacobian;
- transfer reversal;
- proton-active/neutron-active covariance;
- forward identity;
- compatibility with tagged spectator variables;
- compatibility with the partonic shift inside the active nucleon.

---

# 8. Normalized spin-1 NN state

Construct

\[
|D,\Lambda\rangle_{NN}
=
\sum_{\lambda_p,\lambda_n}
\int
\frac{dy\,d^2\bm p_T}
{2(2\pi)^3y(1-y)}
\Psi^{D,\mathrm{LF}}_{\Lambda;\lambda_p\lambda_n}
(y,\bm p_T)
|p\,n\rangle .
\]

The rest-frame state contains at least

\[
\Psi^{\rm IF}_\Lambda
=
\Psi_{S,\Lambda}+\Psi_{D,\Lambda},
\]

with exact Clebsch-Gordan coupling of

```text
S=1, L=0 -> J=1
S=1, L=2 -> J=1
```

and a declared canonical-to-light-front spin transformation.

Do not replace the state by a scalar S-wave probability plus a D-state percentage. Retain amplitude-level:

```text
SS
SD
DS
DD
```

contributions and their signs.

The state must pass:

- normalization for each deuteron helicity;
- proton/neutron exchange and isospin checks;
- parity;
- total `J=1` and `J^z` closure;
- pure-S limit;
- zero-D limit;
- S-D interference sign tests;
- plus-momentum closure;
- center-of-mass consistency;
- spin-rotation unitarity;
- state-member serialization round trip.

C15 may use existing high-quality wave-function tables or implementations already in the repository. Do not download or invent missing wave-function data. If a requested member is unavailable, mark it unavailable and preserve the plan schema.

---

# 9. Nuclear tensor-network representation

Construct a symmetry-adapted nuclear state network with the coupling grammar

```text
H7 proton microscopic member
    x
H7 neutron microscopic member
    -> coupled nucleon spin S=1
    x
relative orbital L=0 or 2
    -> deuteron J=1, I=0
```

The network must retain:

- proton and neutron identities;
- correlated microscopic member identity;
- nucleon helicities;
- deuteron helicity;
- S/D orbital channel;
- S-D interference;
- isospin;
- relative longitudinal and transverse modes;
- nuclear plan and resolution;
- partonic operator identity when contracted.

Implement:

1. direct wave-function contraction;
2. exact/full-bond TTN representation;
3. at least two reduced-bond nuclear TTNs.

Full bond must reproduce the direct state and all principal observables. Reduced-bond convergence must be evaluated for:

- normalization;
- D-state content;
- quadrupole-sensitive amplitude;
- `b1` or tensor-PDF projection;
- tagged tensor response;
- deuteron GTMD link-odd norm when the nucleon input has Wilson order 1 or 2.

At least one low bond must visibly lose a tensor or S-D interference observable while retaining a comparatively small norm or energy defect.

---

# 10. Off-forward spin-resolved spectral amplitude

Build the complete spectral amplitude

\[
\rho^{N/D}_{\Lambda'\Lambda;\lambda'\lambda}
(y,\bm p_T,\bm\Delta_T)
=
\sum_{\lambda_s}
\Psi^{*\,\lambda'\lambda_s}_{\Lambda'}
\left(y,\bm p_T+\frac{1-y}{2}\bm\Delta_T\right)
\Psi^{\lambda\lambda_s}_{\Lambda}
\left(y,\bm p_T-\frac{1-y}{2}\bm\Delta_T\right),
\]

with all normalization and spin-rotation factors declared.

This is a matrix in both deuteron and active-nucleon helicity spaces. A scalar smearing function is not an acceptable replacement.

Required tests:

- Hermiticity under transfer reversal;
- forward Gram positivity in the combined target-active-nucleon space;
- target trace and nucleon-number normalization;
- plus-momentum normalization;
- pure-S and zero-D limits;
- SS/SD/DS/DD reconstruction;
- irreducible spin-1 `K=0,1,2` reconstruction;
- nuclear Wigner Fourier round trip;
- exact/direct versus full-bond TTN equality;
- quadrature convergence.

---

# 11. Spin-1 irreducible projection system

Construct a machine-readable spin-1 target projector registry for

```text
U
L
T_x, T_y
LL
LT_x, LT_y
TT_x, TT_y
```

or an exactly equivalent irreducible spherical basis with a tested adapter.

The target basis must reconstruct every `3x3` deuteron helicity matrix. Store:

- Gram rank and conditioning;
- normalization;
- phase convention;
- relation to `delta_T` helicity differences;
- the project convention for `f1LL` and related LL functions.

At minimum test

\[
\delta_T F
=
F_{\Lambda=0}
-\frac12\left(F_{\Lambda=+1}+F_{\Lambda=-1}\right),
\]

and the declared adapter

\[
f_{1LL}=-\frac23\,\delta_T f_1
\]

when that is the project convention.

Do not infer tensor signs from a TMD name alone.

---

# 12. Matched nuclear operator identities

Create a complete `NuclearOperatorId` that decorates the inherited microscopic operator with:

- nuclear source and target sectors;
- one-body or two-body topology;
- active hadron identity;
- nuclear recoil and transfer-partition ID;
- deuteron and nucleon momentum fibers;
- target, nucleon, and parton helicity spaces;
- Wilson path and order;
- ordered gluon links and `f/d` color class;
- microscopic nucleon member;
- nuclear member;
- regulator, normalization, matching, and soft status;
- current/operator ownership;
- provenance and replacement information.

The N0 operator expansion is

\[
\widehat{\mathcal O}^{\rm N0}_a
=
\widehat{\mathcal O}^{(1)}_a
+
\widehat{\mathcal O}^{(2),\rm bench}_a,
\]

where the one-body block consumes the H7 microscopic nucleon parent and the two-body block is a **minimal analytic validation operator**, not a complete physical exchange-current model.

The package must carry typed unavailable placeholders for:

```text
PION_ACTIVE_OPERATOR
DELTA_ACTIVE_OPERATOR
COMPACT_SECTOR_OPERATOR
COHERENT_MULTIPLE_SCATTERING_OPERATOR
FULL_TWO_BODY_PARTONIC_OPERATOR_BASIS
```

No unavailable operator may be replaced by zero without a status and discrepancy record.

---

# 13. Microscopic deuteron GTMD parent

The primary N0 result is

\[
W^{[\Gamma,\gamma]}_{a/D,\Lambda'\Lambda}
=
\langle D,\Lambda'|
\widehat{\mathcal O}^{\rm N0,[\Gamma,\gamma]}_a
|D,\Lambda\rangle,
\]

restricted in C15 to the `NN` nuclear sector and declared one-/two-body benchmark operators.

The impulse contribution must be evaluated as

\[
\begin{aligned}
W^{(1)}_{a/D,\Lambda'\Lambda}
(x_D,\bm k_T,\bm\Delta_T)
={}&
\sum_{N=p,n}
\sum_{\lambda',\lambda}
\int\frac{dy}{y}
\frac{d^2\bm p_T}{(2\pi)^2}
\rho^{N/D}_{\Lambda'\Lambda;\lambda'\lambda}
(y,\bm p_T,\bm\Delta_T)
\\
&\times
W_{a/N,\lambda'\lambda}
\left(
\frac{x_D}{y},
\bm k_T-\frac{x_D}{y}\bm p_T,
\bm\Delta_T
\right)
J_D .
\end{aligned}
\]

Use the exact H7 microscopic nucleon parent and its complete helicity matrices. Do not project the nucleon to named TMDs before nuclear composition.

The result must retain:

- quark, antiquark, and gluon species;
- proton and neutron ancestry;
- correlated microscopic member;
- deuteron helicity matrix;
- parton helicity or gluon field indices;
- S/D ancestry;
- nuclear member;
- Wilson order and path identity;
- ordered gluon links and `f/d` color class;
- exact/full-bond/reduced-bond identities;
- all matching and readiness limitations.

---

# 14. Complete deuteron helicity parents

For quarks and antiquarks, construct the full joint deuteron-parton helicity matrix of dimension

```text
(3 target helicities x 2 parton helicities)
    by
(3 target helicities x 2 parton helicities)
```

that is, a `6x6` matrix at each kinematic point.

For gluons, retain both:

- the full deuteron-target `3x3` matrix with transverse field indices `i,j`;
- the equivalent `6x6` target-gluon-helicity matrix.

Do not store only named scalar spin-1 TMDs.

The parent must reconstruct exactly from the spin-1 target and parton-polarization projectors.

---

# 15. Wilson and rescattering separation

The H7 nucleon input supports explicit Wilson orders one and two for quarks, antiquarks, and gluons. N0 may compose these **partonic nucleon Wilson structures** through the nuclear amplitude.

It must keep separate:

```text
PARTONIC_WILSON_STAPLE
NUCLEAR_COHERENT_PROPAGATION
TAGGED_FINAL_STATE_INTERACTION
NUCLEAR_GLAUBER_RESCATTERING
```

Only `PARTONIC_WILSON_STAPLE` is available in C15.

Do not introduce nuclear shadowing, tagged final-state interactions, or a nuclear Glauber phase by multiplying the nucleon link-odd result by a scalar nuclear factor.

Required tests:

- future/past reversal survives nuclear convolution;
- quark/antiquark anti-fundamental identity survives;
- all four ordered gluon link pairs survive;
- independent `f` and `d` channels survive;
- no default process mixture appears;
- zero nucleon link-odd input gives zero deuteron link-odd result;
- pure-S and zero-D link-odd limits are reported separately;
- nuclear TTN bond truncation may not silently erase the OAM/S-D block supporting a T-odd tensor projection.

C15 must not claim `NUCLEAR_WILSON_READY`.

---

# 16. Common deuteron reductions

Expose typed reductions from the same deuteron parent:

\[
\mathsf T_D[W]
=
W(x_D,\bm k_T,\bm\Delta_T=0),
\]

\[
\mathsf G_D[W]
=
\int d^2\bm k_T\,W(x_D,\bm k_T,\bm\Delta_T),
\]

\[
\mathsf P_D[W]
=
\int d^2\bm k_T\,W(x_D,\bm k_T,0),
\]

and the appropriate local-current or EMT moments.

For every supported species and target channel, test:

```text
GTMD -> TMD -> PDF
GTMD -> GPD -> PDF at DeltaT=0
GTMD -> GPD -> current/EMT moment
GTMD -> Wigner -> momentum marginal
```

All routes must consume the same parent identity and nuclear member. Do not add a named-function normalization coefficient to repair a failed reduction.

Create a validation-only microscopic deuteron reduction registry covering the declared spin-1 quark/antiquark and gluon projections. It must be unreachable from the production 216-route registry.

---

# 17. Tensor PDF and b1 closure

For each quark and antiquark flavor define

\[
\delta_T q_D(x_D)
=
q_D^{\Lambda=0}(x_D)
-
\frac12\left[
q_D^{\Lambda=+1}(x_D)
+q_D^{\Lambda=-1}(x_D)
\right],
\]

and similarly for antiquarks.

Construct the leading-order tensor structure function

\[
b_1(x_D)
=
\frac12\sum_q e_q^2
\left[
\delta_T q_D(x_D)
+
\delta_T\bar q_D(x_D)
\right].
\]

C15 must test:

- pure-S tensor limit;
- zero-D limit;
- SS/SD/DS/DD decomposition;
- proton/neutron ancestry;
- quark and antiquark separation;
- `f1LL` sign adapter;
- direct helicity-difference route versus named LL projection;
- GTMD/TMD/PDF route closure;
- exact/full-bond TTN equality;
- reduced-bond tensor-signal loss;
- nuclear-plan variation.

This is a regulated microscopic impulse benchmark. Do not tune an independent tensor normalization to external `b1` data in C15.

---

# 18. Deuteron current, form factors, and angular condition

Implement a Hamiltonian/wave-function-owned nuclear current identity

\[
J_D^\mu
=
J_{(1)}^\mu
+
J_{(2),\rm bench}^\mu .
\]

The one-body part consumes the correlated H7 proton/neutron currents. The two-body part is a minimal analytic benchmark required to test co-matching and redistribution; it is not a complete physical exchange-current model.

Construct the spin-1 helicity current matrix and derive benchmark charge, magnetic, and quadrupole combinations or equivalent invariant form factors:

```text
G_C
G_M
G_Q
```

under one declared convention.

Required tests:

- charge closure at `Q^2=0`;
- proton/neutron current ancestry;
- current Hermiticity and parity;
- pure-S and zero-D quadrupole limits;
- angular-condition residual;
- direct current versus GTMD/GPD moment;
- current-component comparison;
- exact/full-bond TTN equality;
- resolution and wave-function-plan flow;
- failure when the current comes from an incompatible nuclear plan;
- failure when the two-body benchmark is included twice.

Do not fit one coefficient per current helicity component.

---

# 19. Unitary off-shell and two-body-operator benchmark

Implement a finite analytic benchmark showing that an off-shell one-body term is representation dependent.

For a unitary or Feshbach transformation,

\[
H' = UHU^\dagger,
\qquad
O' = UOU^\dagger,
\]

the complete matrix element must remain invariant while strength shifts between one-body and induced two-body terms.

The package must demonstrate:

```text
FULL_TRANSFORMED_MATRIX_ELEMENT == ORIGINAL_MATRIX_ELEMENT
ONE_BODY_TERM_ALONE            != INVARIANT_RESULT
```

Provenance relation:

```text
OFFSHELL_ONE_BODY_REPRESENTATION
    EQUIVALENT_TO
TRANSFORMED_ONE_BODY + INDUCED_TWO_BODY + REMAINDER
```

Never expose a standalone off-shell scalar as a physical deuteron correction.

---

# 20. Tagged spectator benchmark

Implement a validation-only tagged kernel for

```text
e + D -> e' + X + spectator
```

with the spectator momentum and helicity retained.

At minimum test:

- tagged-to-inclusive sum rule;
- exact spectator-preserving recoil;
- proton-active and neutron-active channels;
- tensor tagging sensitivity to S-D and D-D blocks;
- an analytic nucleon-pole structure or equivalent benchmark;
- separation of detector acceptance from the nuclear amplitude;
- zero tagged final-state-interaction status;
- exact/full-bond TTN equality;
- reduced-bond loss of a tagged tensor observable.

The C15 tagged object is an impulse validation kernel, not a physical tagged cross section.

---

# 21. Completely positive reduction benchmark

Construct the nuclear amplitude first. Only after a physically declared subsystem becomes unresolved may a reduced map be formed:

\[
\mathcal E_D(\rho_N)
=
\operatorname{Tr}_{\rm unresolved}
\left[
V_D\rho_NV_D^\dagger
\right].
\]

Test:

- complete positivity;
- trace preservation only when all declared outcomes are retained;
- equality with the amplitude-level reduction in the benchmark domain;
- failure when coherent amplitudes are traced before interference;
- failure when a CP map is used to represent unavailable shadowing or exchange-current coherence.

The CP map is a derived representation, not the primary nuclear dynamics.

---

# 22. Global nuclear ledgers

C15 must close, within declared tolerances:

- deuteron-state normalization;
- proton number and neutron number;
- baryon number;
- electric charge;
- hadronic plus momentum;
- partonic quark/antiquark/gluon momentum after convolution;
- deuteron `J^z`;
- S/D amplitude normalization;
- current and angular-condition ledgers;
- tensor/`b1` ledger;
- tagged-to-inclusive ledger;
- Wilson link/color ledger;
- provenance count-once ledger.

A normalized final table may not hide a failed underlying state or operator ledger.

---

# 23. Common-member covariance and uncertainty identity

Every deuteron result must preserve one common member identity:

```text
nucleon microscopic plan/member
nuclear wave-function plan/member
nuclear operator/current member
resolution and solver
Wilson order/path/color
numerical quadrature member
```

Even if C15 does not perform Bayesian inference, it must make member-wise covariance propagation possible.

Do not combine independently sampled proton, neutron, wave-function, current, and Wilson members after projection.

Produce deterministic sensitivity and finite-difference derivatives for at least:

- D-wave amplitude or controlled tensor parameter;
- nuclear transverse scale or quadrature parameter;
- one nucleon microscopic parameter exposed by H7;
- TTN bond capacity;
- one two-body benchmark coefficient.

Keep physical parameter, nuclear-model, Fock, matching, Wilson, and numerical axes separate.

---

# 24. Provenance and no-double-counting complex

Extend the general provenance two-complex with nuclear cells.

At minimum include 0-cells and relations for:

```text
H7 proton parent
H7 neutron parent
NN nuclear state
one-body nuclear operator
two-body benchmark operator
deuteron GTMD parent
deuteron current
tagged kernel
CP reduction
```

Required relations include:

```text
PROTON_PARENT + NEUTRON_PARENT
    COMPOSE_IN_AMPLITUDE
NN_SPIN1_STATE

FULL_NUCLEAR_AMPLITUDE
    REDUCES_TO
IMPULSE_PARENT

OFFSHELL_ONE_BODY
    EQUIVALENT_TO
TRANSFORMED_ONE_BODY + INDUCED_TWO_BODY + REMAINDER

AMPLITUDE_EMBEDDING
    REDUCES_TO
CP_MAP_AFTER_TRACE
```

Reject before numerical evaluation:

- mixing nuclear plans;
- mixing uncorrelated proton/neutron members;
- one-body current plus its transformed replacement;
- explicit and induced two-body benchmark simultaneously;
- partonic Wilson and a copied nuclear rescattering factor;
- unavailable coherent/shadowing or pion mechanisms promoted to central;
- CP map and underlying amplitude counted together;
- tagged and inclusive results treated as independent calibration data without ancestry.

Nontrivial unresolved cycles must be reported, not silently normalized away.

---

# 25. Analytic benchmark suite

Implement at least the following benchmark families.

## N0-A: scalar weak-binding two-body state

- exact normalization;
- recoil closure;
- one-body convolution with an independent analytic oracle;
- TMD/GPD/PDF/current reductions;
- tagged-to-inclusive closure.

## N0-B: analytic spin-1 S-D model

- full `3x3` target matrix;
- `U/L/T/LL/LT/TT` reconstruction;
- pure-S and zero-D limits;
- SS/SD/DS/DD decomposition;
- nonzero tensor projection from the declared interference;
- direct versus TTN equality.

## N0-C: current and angular condition

- charge normalization;
- benchmark magnetic/quadrupole structures;
- current Hermiticity;
- angular-condition closure;
- current-moment equality.

## N0-D: unitary off-shell redistribution

- invariant full matrix element;
- noninvariant one-body piece;
- induced two-body completion;
- visible remainder and provenance cell.

## N0-E: microscopic H7 impulse parent

For `u`, `d`, `ubar`, `dbar`, and gluon:

- complete deuteron helicity parents;
- proton/neutron ancestry;
- generic and forward kinematics;
- exact/full-bond equality;
- all common reductions.

## N0-F: Wilson inheritance

- future/past reversal after nuclear convolution;
- quark and antiquark link-odd matrices;
- all four ordered gluon links;
- separate `f/d` channels;
- zero nuclear rescattering status;
- no process mixture.

## N0-G: b1 and tensor closure

- direct helicity-difference and LL-adapter agreement;
- S/D origin ledger;
- quark/antiquark sum;
- exact/full-bond equality;
- controlled reduced-bond signal loss.

## N0-H: tagged spectator benchmark

- inclusive recovery;
- spectator recoil;
- analytic pole or equivalent oracle;
- tensor S-D selectivity.

## N0-I: derived CP map

- positivity;
- trace closure;
- equality with amplitude reduction where valid;
- rejection before coherent interference is resolved.

## N0-J: assumption compiler

- all nuclear plans compile deterministically;
- branches remain mutually exclusive;
- H7 nucleon plan identity remains visible;
- failed readiness produces minimal structured certificates.

---

# 26. Required negative injections

Add at least **200** stable, ordered C15 injections. Use machine-readable IDs.

They must include failure families for:

### Baseline and source integrity

- wrong C14 ancestor;
- missing or changed normative source hash;
- changed authoritative artifact;
- changed production registry or composition;
- nondeterministic manifest output.

### Nuclear kinematics

- `x_D`, `x_N`, and `y` aliasing;
- wrong active-nucleon recoil factor;
- wrong spectator shift;
- local reimplementation of recoil;
- failed Jacobian;
- transfer reversal failure;
- active proton/neutron mapping swap;
- tagged recoil mismatch.

### State and spin

- unnormalized deuteron state;
- missing deuteron helicity;
- incorrect S/D Clebsch-Gordan coefficient;
- lost SD or DS interference;
- incorrect D-wave sign;
- nonunitary light-front spin rotation;
- mixed nuclear plans;
- proton and neutron copied or uncorrelated;
- wrong isospin channel;
- TTN bond removes required tensor block without warning.

### Spectral amplitude

- scalar smearing substituted for helicity matrix;
- failed Hermiticity;
- failed forward positivity;
- failed nucleon-number or momentum ledger;
- Wigner transform uses `bTMD` instead of `bDelta`;
- unsupported pseudoinverse of a degenerate projector.

### Operator identity and composition

- incomplete nuclear operator identity;
- one-body operator uses incompatible H7 member;
- missing Wilson or gluon color identity;
- process color weight inserted;
- two-body transfer partition omitted;
- unavailable mechanism treated as zero;
- named-TMD-level convolution instead of helicity-parent composition.

### Reductions

- GTMD/TMD/PDF routes use different parent IDs;
- named-function normalization repair;
- quark and antiquark sign error;
- gluon `H^g=xg` convention lost;
- rank or Bessel metadata lost;
- moment/current mismatch hidden by rescaling.

### Tensor and b1

- wrong `delta_T` sign;
- wrong `f1LL` adapter;
- S-wave produces unsupported tensor signal;
- D-wave tensor block removed silently;
- independent `b1` normalization fitted;
- proton/neutron ancestry erased.

### Currents and off-shell representation

- current from incompatible nuclear plan;
- current coefficient per helicity component;
- one-body and transformed current counted together;
- induced two-body term omitted;
- off-shell scalar promoted to observable;
- angular defect hidden by fit;
- quadrupole signal without D or two-body source.

### Wilson separation

- nuclear shadowing scalar multiplies Sivers or Boer-Mulders;
- partonic Wilson and nuclear Glauber labels aliased;
- `f/d` channels merged;
- ordered gluon links lost;
- future/past reversal broken;
- link-odd signal from Wilson-order-zero input;
- Wilson order three accepted;
- spectral/soft readiness overstated.

### Tagged and CP maps

- tagged and inclusive double counted;
- detector acceptance inserted into nuclear amplitude;
- CP reduction performed before coherent amplitude completion;
- trace preservation claimed with omitted outcomes;
- CP map and amplitude contribution both active.

### Provenance and downstream gates

- explicit and induced mechanisms selected together;
- unavailable `NNPI`, coherent, Delta, six-quark, or hidden-color sector promoted;
- production route consumes N0 parent;
- LF-to-QCD matcher consumes unmatched N0 parent;
- evolution consumes unmatched N0 parent;
- process map consumes N0 parent;
- inference consumes N0 parent;
- result falsely marked physical or nuclear-complete.

Every injected failure must produce a stable diagnostic code and fail before or at the correct architectural boundary.

---

# 27. C15 deliverables

Create at least:

```text
docs/next_level/c15_implementation_report.md
docs/next_level/c15_api.md
docs/next_level/c15_requirement_coverage.json
docs/next_level/c15_injection_manifest.json
docs/next_level/c15_regression_report.json
docs/next_level/c15_normative_source_integration.json
docs/next_level/c15_nuclear_plan_manifest.json
docs/next_level/c15_nuclear_recoil_manifest.json
docs/next_level/c15_spin1_state_manifest.json
docs/next_level/c15_spectral_amplitude_manifest.json
docs/next_level/c15_deuteron_parent_manifest.json
docs/next_level/c15_spin1_projector_manifest.json
docs/next_level/c15_current_closure_report.json
docs/next_level/c15_b1_closure_report.json
docs/next_level/c15_tagged_closure_report.json
docs/next_level/c15_ttn_convergence_report.json
docs/next_level/c15_provenance_complex.json
docs/next_level/c15_readiness_manifest.json
docs/next_level/c15_unresolved_physics_gaps.md
```

Add architecture-decision records for at least:

```text
nuclear recoil authority
correlated proton/neutron member identity
spin-1 projector convention
partonic versus nuclear Wilson separation
one-body/two-body operator co-matching
off-shell representation covariance
NN-only N0 scope and unavailable sectors
```

Update `handoff/ROADMAP.md` with:

- final C15 commit;
- exact validated scope;
- numerical residual maxima;
- readiness statuses;
- unresolved nuclear sectors and operator blocks;
- exact recommended C16 task.

All generated JSON must be deterministic and byte-reproducible.

---

# 28. Acceptance criteria

C15/N0 is complete only when all of the following pass:

1. The complete C14 baseline reproduces before changes.
2. All prior tests, builders, evidence rows, atlas pages, requirements, and injections remain passing.
3. Production remains exactly unchanged at 216 routes and eight authoritative artifacts.
4. Correlated proton/neutron H7 members are consumed without copying or early isoscalar collapse.
5. The nuclear recoil map passes all exact closure tests and is used everywhere.
6. A normalized spin-1 NN state with explicit S/D amplitudes and interference is implemented.
7. The nuclear TTN full-bond state reproduces the direct state and principal observables.
8. The off-forward spectral amplitude retains complete deuteron and active-nucleon helicities.
9. The microscopic deuteron quark, antiquark, and gluon helicity parents are constructed from H7 parents.
10. Spin-1 `U/L/T/LL/LT/TT` projector reconstruction closes.
11. TMD/GPD/PDF/current/EMT reductions close from the same deuteron parent.
12. `b1` and LL-adapter routes close without an independent tensor normalization.
13. Current, angular-condition, and GTMD-moment benchmarks close within declared tolerances.
14. The unitary off-shell benchmark demonstrates operator co-transformation.
15. Tagged-to-inclusive closure and the tagged tensor benchmark pass.
16. The CP map is derived only after a valid amplitude trace and passes positivity/trace tests.
17. Partonic Wilson structures survive nuclear composition without being confused with nuclear rescattering.
18. All nuclear ledgers and provenance count-once rules pass.
19. At least 200 C15 negative injections are detected with stable diagnostics.
20. Exact/direct and full-bond TTN routes agree; reduced-bond tensor losses remain visible.
21. N0 remains unreachable from production, matching, evolution, process, and inference roots.
22. All C15 manifests reproduce byte-for-byte.
23. The working tree is clean after the final local commit.
24. Nothing is pushed.

Do not declare C15 complete merely because an impulse convolution produces arrays. The state, recoil, helicity, current, tensor, tagged, provenance, and convergence gates must all pass.

---

# 29. Final response required from Codex

Report:

- starting and final commit;
- full test/builder/evidence/atlas counts;
- all prior and C15 injection counts;
- nuclear plan identities;
- state and grid dimensions;
- maximum normalization, recoil, spectral, projector, current, angular, b1, tagged, CP, TTN, and provenance residuals;
- exact/full-bond and reduced-bond tensor-observable comparison;
- status of quark, antiquark, and gluon deuteron parents at Wilson orders 0, 1, and 2;
- source hashes and reproducibility status;
- immutable-production confirmation;
- exact unresolved physics gates;
- exact next recommended package.

The expected next package after a successful N0 is normally:

```text
C16/N1
    spin-resolved NNPI sector
    pion-active and transition operators
    internal-versus-exchange pion subtraction
    Hamiltonian-consistent two-body currents
    coherent helicity-resolved small-x pilot
```

Do not begin C16 inside C15.

Continue autonomously until every C15 acceptance criterion is satisfied. Install routine local dependencies when permitted. Do not stop to ask for approval for ordinary local analysis or testing. Do not push.
