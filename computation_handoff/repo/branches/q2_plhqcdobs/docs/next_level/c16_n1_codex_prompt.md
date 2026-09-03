# C16/N1 Codex Work Package

## Title

**C16/N1 — Spin-resolved \(NN\pi\) light-front sector, pion-active and transition operators, internal-versus-exchange pion subtraction, Hamiltonian-consistent two-body currents, and a helicity-resolved coherent small-\(x\) pilot**

## Authoritative baseline

The authoritative physics and software baseline is:

```text
cd94d1199202a97bb451aee9085cfc6c0708b8f2
```

A documentation-only descendant is acceptable only when this commit remains in its ancestry and the complete C15/N0 baseline reproduces before any C16 code is changed.

Do **not** use `origin/main` as the scientific baseline. The authoritative work is local and intentionally unpushed.

## Primary objective

Extend the isolated C15/N0 \(NN\)-only deuteron validation root to the first normalized two-sector spin-1 nuclear state

\[
\mathcal H_{\mathrm{N1}}
=
\mathcal H_{NN}
\oplus
\mathcal H_{NN\pi},
\]

with one common state, current, partonic-operator, recoil, normalization, plus-momentum, and provenance system.

C16 must implement:

1. a spin-, isospin-, charge-, momentum-, and orbital-resolved \(NN\pi\) light-front sector;
2. a Hermitian \(NN\leftrightarrow NN\pi\) transition interaction and a controlled small resolution tower;
3. diagonal nucleon-active and pion-active partonic operators in the \(NN\pi\) sector;
4. \(NN\leftrightarrow NN\pi\) transition operators retained at amplitude level;
5. an explicit internal-nucleon-pion versus nuclear-exchange-pion overlap subtraction;
6. Hamiltonian-consistent one-body, pion-in-flight, transition/contact, and induced two-body currents;
7. a finite-basis nuclear continuity/Ward benchmark;
8. an amplitude-level helicity-resolved coherent double-scattering pilot at small \(x\);
9. an explicit partonic-Wilson versus nuclear-coherent overlap ledger;
10. a derived partial-trace completely positive map only after coherent amplitudes are formed;
11. exact/full-bond and reduced-bond nuclear tensor-network convergence;
12. a common microscopic deuteron GTMD parent that includes \(NN\), \(NN\pi\), transition, and optional coherent-pilot blocks without changing production.

This is a **validation-only N1 package**. It must not claim a physical deuteron prediction, a completed nuclear EFT, a physical pion GTMD, a complete shadowing calculation, a matched QCD TMD, evolution, a process cross section, or inference readiness.

## Normative sources

Read completely and use as normative sources, when present:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_iv_matched_spin1_nuclear_dynamics.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_xi_microscopic_nonzero_transfer_gtmds.tex
references/volume_xii_microscopic_wilson_second_order.tex
references/model_construction_note.tex
docs/next_level/c15_implementation_report.md
docs/next_level/c15_api.md
docs/next_level/c15_regression_report.json
docs/next_level/c15_*manifest*.json
handoff/ROADMAP.md
```

If Volume XII is not yet present, it may be added in a documentation-only commit before C16. Record every normative source path and SHA-256 hash in:

```text
docs/next_level/c16_normative_source_integration.json
```

Do not invent missing source content. When a normative source is absent, record the absence and use only equations and requirements explicitly reproduced in this work package and the available C15 interfaces.

## Immutable C15 baseline

Before editing code, reproduce and record:

```text
964/964 tests
all C15 builders and validators
36/36 evidence rows
162/162 atlas pages
462/462 C15 requirements
244/244 C15 negative injections
all earlier C3–C14 injections
216 accepted production reductions
all eight authoritative artifacts byte-identical
all 16 C15 generated JSON artifacts byte-identical
pinned C13/C14 manifests byte-identical
working tree clean
```

If the baseline does not reproduce, diagnose the baseline first. Do not repair a baseline failure by changing physics.

## Scientific nonclaims

C16 must not claim any of the following:

```text
PHYSICAL_DEUTERON_PREDICTION
COMPLETE_NUCLEAR_EFT
PHYSICAL_PION_GTMD_OR_TMD
COMPLETE_EXCHANGE_CURRENT_BASIS
PHYSICAL_COHERENT_SHADOWING
NUCLEAR_GLAUBER_RESCATTERING_READY
MATCHED_QCD_TMD
CONTINUUM_SOFT_COMPLETION
COLLINS_SOPER_EVOLUTION_READY
PROCESS_PREDICTION_READY
INFERENCE_READY
PRODUCTION_READY
```

The strongest permissible statuses are qualified finite-resolution N1 validation statuses defined later in this prompt.

---

# 1. Extend the C15 nuclear type system rather than creating a parallel implementation

C16 must reuse and extend the actual C15 APIs for:

- `NuclearResolution`;
- `NuclearMember`;
- `NuclearSectorId`;
- `NuclearRecoilMap`;
- `SpectralAmplitude`;
- `MatchedNuclearOperator`;
- `DeuteronGTMDParent`;
- `NuclearLedger`;
- spin-1 projectors;
- current and angular-condition diagnostics;
- tagged kernels;
- CP reductions;
- state and operator tensor networks;
- provenance and assumption plans.

Inspect `docs/next_level/c15_api.md` and the C15 source tree before choosing file names.

New objects may include, or be semantically equivalent to:

```text
ThreeBodyNuclearCoordinates
ThreeBodyNuclearRecoilMap
NNPiSectorSpec
NNPiBasisState
NNPiLightFrontAmplitude
PionNucleonVertex
NuclearTransitionOperator
PionActiveOperator
PionOverlapProjector
PionSubtractionMap
NuclearTwoBodyCurrent
NuclearContinuityLedger
DiffractiveHelicityAmplitude
CoherentPropagationKernel
PartonNuclearOverlapMap
CoherentAmplitudeBundle
N1NuclearStateBundle
```

Do not duplicate C15 coordinate, target-spin, partonic-Wilson, current, or provenance classes under different names.

Array-shape compatibility is never sufficient for composition. Every state, operator, and map must validate source/target sector, coordinate, spin, isospin, charge, parton species, Wilson order, link/color identity, regulator, member, and provenance compatibility.

---

# 2. Spin-resolved \(NN\pi\) Hilbert space

## 2.1 Sector definition

Introduce a typed sector

\[
\mathcal H_{NN\pi}
\]

with exact total deuteron quantum numbers at the charge-symmetric reference point:

\[
B=2,\qquad Q=+1,\qquad I=0,\qquad J^P=1^+.
\]

The charge channels must include the complete total-charge-\(+1\) isovector set needed by the selected isospin coupling, for example

\[
|pn\pi^0\rangle,\qquad
|pp\pi^-\rangle,\qquad
|nn\pi^+\rangle,
\]

combined with explicit Clebsch–Gordan coefficients into total \(I=0\). Do not retain only \(pn\pi^0\) and call the isospin basis complete.

At the isospin-symmetric reference point, the \(NN\) pair in the \(NN\pi\) sector must carry the isospin representation required to couple with \(I_\pi=1\) to total \(I=0\). Any charge-symmetry-breaking admixture must be a separate typed assumption branch.

## 2.2 Parity and angular momentum

The pion has intrinsic parity \(-1\). The retained orbital and spin couplings must therefore satisfy

\[
(-1)^{L_{NN}+L_{\pi}}(-1)=+1
\]

for the total \(J^P=1^+\) state.

The smallest retained benchmark space must contain the minimal odd total orbital parity needed for the \(NN\pi\) component, while preserving:

- nucleon helicities;
- pion charge/isospin;
- \(NN\) spin and isospin;
- Jacobi orbital labels;
- total \(J^z\);
- parity;
- regulator and resolution;
- exact proton/neutron identity.

A scalar pion probability without the spin–orbital amplitude is insufficient.

## 2.3 Three-body light-front coordinates

Use positive fractions

\[
y_1>0,\qquad y_2>0,\qquad y_\pi>0,\qquad
y_1+y_2+y_\pi=1,
\]

and intrinsic transverse momenta

\[
\bm\kappa_{1T}+\bm\kappa_{2T}+\bm\kappa_{\pi T}=0.
\]

Implement a declared three-body invariant measure. Store the exact normalization convention, endpoint policy, Jacobian, and Jacobi-coordinate map as part of the sector identity.

No coordinate is allowed to reuse the C15 two-body \(y,\bm p_T\) type without a typed adapter.

## 2.4 Complete state amplitude

The state is

\[
|D,\Lambda\rangle_{\mathrm{N1}}
=
|\Psi_{NN}^{\Lambda}\rangle
+
|\Psi_{NN\pi}^{\Lambda}\rangle,
\]

with one normalization,

\[
Z_{NN}+Z_{NN\pi}=1,
\]

and one plus-momentum ledger.

The \(NN\pi\) amplitude must retain:

- deuteron helicity;
- both nucleon helicities;
- pion charge/isospin;
- all retained Jacobi orbital labels;
- \(NN\) spin/isospin;
- charge channel;
- phase convention;
- nuclear member;
- resolution and regulator;
- source Hamiltonian and assumption plan.

Sector probabilities are resolution-dependent diagnostics, not observables.

---

# 3. Three-body recoil and transfer maps

## 3.1 Diagonal active-constituent recoil

For a number-preserving three-body matrix element with active constituent \(j\), use the general symmetric-frame map

\[
\bm\kappa_{jT}^{\rm in}
=
\bm k_{jT}
-\frac{1-y_j}{2}\bm\Delta_T,
\qquad
\bm\kappa_{jT}^{\rm out}
=
\bm k_{jT}
+\frac{1-y_j}{2}\bm\Delta_T,
\]

and for each spectator \(i\neq j\),

\[
\bm\kappa_{iT}^{\rm in}
=
\bm k_{iT}
+\frac{y_i}{2}\bm\Delta_T,
\qquad
\bm\kappa_{iT}^{\rm out}
=
\bm k_{iT}
-\frac{y_i}{2}\bm\Delta_T.
\]

Prove and test:

- intrinsic closure;
- unit Jacobian;
- full physical transfer to the active constituent;
- unchanged physical spectator momenta;
- transfer reversal;
- permutation covariance;
- forward identity.

Use one authoritative three-body recoil implementation for active nucleon and active pion cases.

## 3.2 Number-changing transition recoil

An \(NN\leftrightarrow NN\pi\) transition changes particle number. It cannot be evaluated using the diagonal one-body recoil map.

Implement a typed `TransitionRecoilMap` containing:

- source and target sectors;
- emitting or absorbing nucleon;
- pion momentum;
- external transfer partition;
- unchanged spectators;
- exact momentum conservation;
- Jacobian;
- endpoint and zero-mode policy;
- Hermitian reverse map.

The transition map must be derived from physical momentum conservation and tested independently. No local current or operator may rederive its factors.

---

# 4. Coupled \(NN\oplus NN\pi\) Hamiltonian benchmark

## 4.1 Block operator

Implement a validation Hamiltonian of the form

\[
\mathcal M_{\mathrm{N1}}^2
=
\begin{pmatrix}
\mathcal M_{NN}^2 & V_{NN\leftarrow NN\pi}\\
V_{NN\pi\leftarrow NN} & \mathcal M_{NN\pi}^2
\end{pmatrix},
\qquad
V_{NN\leftarrow NN\pi}
=
V_{NN\pi\leftarrow NN}^{\dagger}.
\]

The \(NN\) diagonal block must consume the immutable C15 wave-function/current family rather than replacing it.

The \(NN\pi\) diagonal block must include:

- the free three-body invariant mass;
- the selected finite-resolution interaction terms;
- sector counterterms and discrepancy records;
- exact charge, isospin, parity, and \(J^z\) blocks.

## 4.2 Pion–nucleon transition interaction

Use a controlled hadronic light-front benchmark interaction whose operator identity contains:

- coupling and normalization;
- isospin generator;
- spin/helicity structure;
- derivative or pseudoscalar character;
- pion charge;
- emitting nucleon;
- longitudinal and transverse momentum kernel;
- regulator and form-factor identity;
- endpoint and zero-mode policy;
- Hermitian-conjugate block;
- current/contact partners.

A pseudovector benchmark may be organized schematically from

\[
\mathcal L_{\pi NN}
=
\frac{g_A}{2f_\pi}
\bar N\gamma^\mu\gamma_5\tau^aN\,\partial_\mu\pi^a,
\]

but C16 must label the finite basis and regulator-specific realization honestly. It is not a complete continuum chiral EFT.

## 4.3 Renormalization and holdouts

At each N1 resolution point, refit only the declared calibration conditions, for example:

- the deuteron bound-state mass or binding benchmark;
- total charge;
- one \(NN\leftrightarrow NN\pi\) transition condition;
- one finite-basis continuity/current condition.

Retain holdouts including:

- a second transition kinematic point;
- \(Z_{NN\pi}\);
- a pion-active moment;
- a tensor observable;
- a nonzero-transfer current component;
- an angular-condition component;
- a pion-sensitive tagged observable.

Expose Jacobian singular values and null directions. Do not hide an unidentifiable parameter with another fitted observable.

---

# 5. Pion-active, nucleon-active, and transition partonic operators

## 5.1 Full operator block structure

The nuclear partonic operator must have sector blocks

\[
\widehat{\mathcal O}_a^{\mathrm{N1}}
=
\begin{pmatrix}
\widehat{\mathcal O}_{a,NN\to NN}
&
\widehat{\mathcal O}_{a,NN\pi\to NN}
\\
\widehat{\mathcal O}_{a,NN\to NN\pi}
&
\widehat{\mathcal O}_{a,NN\pi\to NN\pi}
\end{pmatrix}.
\]

The diagonal \(NN\pi\to NN\pi\) block must distinguish:

```text
ACTIVE_NUCLEON_WITH_PION_SPECTATOR
ACTIVE_PION_WITH_NN_SPECTATOR
```

The off-diagonal blocks are transition operators and must remain coherent until the physical observable no longer resolves their phase.

## 5.2 Nucleon-active diagonal block

Reuse the H7/C14 nucleon helicity parents through the C15 nuclear composition interfaces, with the three-body recoil map and pion spectator retained.

Preserve:

- quark, antiquark, and gluon species;
- nucleon helicity matrices;
- Wilson orders 0, 1, and 2;
- future/past path;
- ordered gluon links;
- independent \(f/d\) channels;
- correlated proton/neutron microscopic member;
- all H7 support and soft-overlap manifests.

## 5.3 Pion-active diagonal block

Introduce a typed spin-zero pion partonic parent or analytic oracle with:

- pion charge and isospin;
- direct positive-\(x\) quark and antiquark identities;
- gluon identity where supported;
- number and momentum ledgers;
- operator projection;
- regulator and matching status;
- exact source hash;
- no hidden fit to deuteron data.

The initial C16 pion parent may be validation-only and analytic. It must be labeled, for example:

```text
PION_PARTONIC_PARENT_ANALYTIC_ORACLE
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
NO_EVOLUTION_APPLIED
NO_PROCESS_MAP_APPLIED
```

It may not be called a physical pion GTMD/TMD.

The pion-active deuteron contribution must be generated by the \(NN\pi\) state and the pion operator. It may not receive an independent scalar normalization.

## 5.4 Transition operators

Implement at least one nontrivial \(NN\leftrightarrow NN\pi\) current/partonic transition benchmark that retains:

- source and target sectors;
- deuteron and nucleon helicities;
- pion charge and orbital state;
- active partonic operator;
- transition recoil;
- phase convention;
- Hermitian-conjugate relation;
- regulator and matching status.

The transition contribution to the deuteron parent is

\[
W^{\rm trans}
=
\langle\Psi_{NN\pi}|
\widehat{\mathcal O}_{NN\pi\leftarrow NN}
|\Psi_{NN}\rangle
+
\langle\Psi_{NN}|
\widehat{\mathcal O}_{NN\leftarrow NN\pi}
|\Psi_{NN\pi}\rangle.
\]

Dropping either term must break Hermiticity.

---

# 6. Full N1 deuteron GTMD parent

Construct the amplitude-level parent

\[
\begin{aligned}
W_{a/D}^{\mathrm{N1}}
={}&
\langle\Psi_{NN}|\widehat{\mathcal O}_{NN\to NN}|\Psi_{NN}\rangle
\\
&+
\langle\Psi_{NN\pi}|
\widehat{\mathcal O}_{NN\pi\to NN\pi}
|\Psi_{NN\pi}\rangle
\\
&+
\langle\Psi_{NN\pi}|
\widehat{\mathcal O}_{NN\pi\leftarrow NN}
|\Psi_{NN}\rangle
\\
&+
\langle\Psi_{NN}|
\widehat{\mathcal O}_{NN\leftarrow NN\pi}
|\Psi_{NN\pi}\rangle
\\
&+
W_{a/D}^{\mathrm{coh,pilot}}
\quad\text{when the coherent branch is explicitly selected}.
\end{aligned}
\]

Every contribution must retain:

- sector ancestry;
- species and flavor;
- deuteron and parton helicities;
- pion charge and isospin where present;
- Wilson order and path;
- gluon ordered links and \(f/d\) class;
- regulator and resolution;
- nuclear and nucleon member identity;
- current/operator identity;
- provenance and subtraction status.

Project to \(U,L,T,LL,LT,TT\) only after the complete spin recoupling and sector sum.

The N1 parent must close onto regulated TMD, GPD, PDF, current, EMT, Wigner, \(b_1\), and tagged reductions without named-function normalization.

---

# 7. Internal-nucleon pion versus nuclear-exchange pion subtraction

## 7.1 Distinguish the three physical descriptions

C16 must type separately:

```text
INTERNAL_NUCLEON_PSEUDOSCALAR_OR_PION_LIKE_REGION
EXPLICIT_NUCLEAR_NNPI_SECTOR
INDUCED_OR_CONTACT_PION_OPERATOR
```

The H7 nucleon contains microscopic pair/chiral structure and an induced pion-pole operator, but not an asymptotic explicit pion Fock state. The N1 \(NN\pi\) sector is a distinct nuclear-scale description.

## 7.2 Overlap projector and matched sum

Implement a declared resolution/separation map \(\mathcal P_{\pi,\mathrm{ov}}\) identifying the common asymptotic or low-momentum region represented by both descriptions.

The matched contribution is

\[
W_{\pi}^{\mathrm{matched}}
=
W_{\pi}^{\mathrm{internal}}
+
W_{\pi}^{\mathrm{exchange}}
-
W_{\pi}^{\mathrm{overlap}}.
\]

The overlap term must be computed from the same matching projection; it cannot be a fitted scalar subtraction.

Vary the separation scale or projector within a controlled range and demonstrate that individual components move while the matched sum is stable within the declared truncation error.

## 7.3 Provenance two-cell

Represent the relation as an executable two-cell:

```text
INTERNAL_PION_REGION
  + EXPLICIT_NNPI_SECTOR
  - OVERLAP_SUBTRACTION
  EQUIVALENT_TO
MATCHED_PION_DESCRIPTION
```

The graph must reject:

- internal plus explicit pion with no subtraction;
- duplicate overlap subtraction;
- a second scalar “pion correction”;
- explicit \(NN\pi\) plus its fully integrated-out contact replacement;
- silent promotion of a pion analytic oracle to a physical pion TMD.

The subtraction relation is not a probability decomposition.

---

# 8. Hamiltonian-consistent nuclear current

## 8.1 Current family

Construct a finite-resolution current

\[
J_{\mathrm{N1}}^\mu
=
J_N^\mu
+
J_\pi^\mu
+
J_{\mathrm{trans}}^\mu
+
J_{\mathrm{contact}}^\mu
+
J_{\mathrm{ind}}^\mu
+
\delta J_{\mathrm{ct}}^\mu.
\]

The current must use the same:

- \(NN\leftrightarrow NN\pi\) interaction;
- regulator and form factor;
- endpoint and zero-mode prescription;
- sector counterterms;
- pion charge/isospin convention;
- state normalization;
- operator transformation and Feshbach provenance.

Where the selected pseudovector benchmark requires them, include pion-in-flight and contact/Kroll–Ruderman-like partners as separately typed pieces.

## 8.2 Finite-basis continuity benchmark

Implement a nuclear continuity/Ward benchmark, schematically

\[
q_\mu J^\mu_{\mathrm{N1}}
=
[H_{\mathrm{N1}},\rho_{\mathrm{N1}}]
+
\delta_{\mathrm{trunc}}.
\]

Decompose the residual into at least:

```text
NUCLEON_ONE_BODY
PION_IN_FLIGHT
NN_TO_NNPI_TRANSITION
CONTACT_OR_SEAGULL
INDUCED_TWO_BODY
CURRENT_COUNTERTERM
REGULATOR_ENDPOINT
BASIS_TRUNCATION
```

The residual must close only when all required nonzero pieces are present. Removing any required term must produce a signed, stable defect.

The strongest permissible status is:

```text
FINITE_BASIS_NUCLEAR_CONTINUITY_BENCHMARKED
```

not a full gauge-invariance or chiral-EFT proof.

## 8.3 Elastic and angular-condition closure

Re-evaluate:

- charge normalization;
- magnetic and quadrupole benchmark structures;
- spin-1 angular condition;
- direct current versus GTMD/GPD moment closure;
- current-component holdouts.

Do not fit one coefficient per helicity amplitude or momentum transfer.

---

# 9. Helicity-resolved coherent small-\(x\) pilot

## 9.1 Amplitude-level construction

Implement a two-step coherent kernel of the form

\[
\delta W_{\Lambda'\Lambda}^{\mathrm{coh}}
\sim
\sum_X
\mathcal A_{\Lambda'\to X}^{\mathrm{diff}\,*}
\,
\mathcal G_X
\,
\mathcal A_{\Lambda\to X}^{\mathrm{diff}},
\]

with explicit:

- target and nucleon helicities;
- intermediate diffractive state;
- scattering order;
- longitudinal ordering;
- propagation phase;
- parton species and operator projection;
- nuclear member;
- factorization and Glauber status;
- parton–nuclear overlap-subtraction status.

The elementary diffractive amplitudes may be analytic validation oracles, but they must be helicity resolved and typed as unmatched.

## 9.2 Required coherent benchmarks

Demonstrate:

1. zero coherent correction when either elementary diffractive amplitude is zero;
2. phase reversal under interchange of longitudinal ordering;
3. distinct \(U\), vector, and tensor projections from explicit helicity amplitudes;
4. failure of a copied unpolarized shadowing ratio to reproduce the tensor result;
5. coherent amplitudes combine before any unresolved subsystem is traced;
6. the tensor result depends on the actual S/D and \(NN\pi\) spin structure;
7. no implicit universal coherent factor is multiplied onto every TMD.

## 9.3 Factorization status

Every coherent result must be labeled at most:

```text
HELICITY_RESOLVED_COHERENT_SMALLX_PILOT
DIFFRACTIVE_INPUT_ANALYTIC_ORACLE
NUCLEAR_GLAUBER_STATUS_UNASSESSED_OR_EXPLORATORY
PHYSICAL_SHADOWING_NOT_CLAIMED
```

Do not call the result a physical shadowing prediction.

---

# 10. Partonic Wilson versus nuclear coherent overlap

The C14/H7 parent already contains partonic Wilson rescattering through order two. C16 coherent propagation is a nuclear-scale amplitude.

Type them separately:

```text
PARTONIC_WILSON_STAPLE
NUCLEAR_COHERENT_PROPAGATION
TAGGED_FINAL_STATE_INTERACTION
```

Implement an analytic `PartonNuclearOverlapMap` for any shared soft/Glauber region used in the pilot.

The matched schematic structure is

\[
W^{\mathrm{matched}}
=
W^{\mathrm{partonic}}
+
W^{\mathrm{nuclear\ coherent}}
-
W^{\mathrm{parton\text{-}nuclear\ overlap}}.
\]

The overlap subtraction must be explicit and count-once. Missing or duplicate subtraction must leave equal-and-opposite signed residuals in the analytic benchmark.

Do not modify the C14 partonic phase budget in place. The nuclear overlap is a new typed matching layer.

---

# 11. Derived completely positive map

Construct an explicit amplitude embedding

\[
V:
\mathcal H_{\mathrm{resolved}}
\longrightarrow
\mathcal H_{\mathrm{retained}}
\otimes
\mathcal H_{\mathrm{unresolved}},
\]

and derive

\[
\mathcal E(\rho)
=
\operatorname{Tr}_{\mathrm{unresolved}}
\left[
V\rho V^\dagger
\right].
\]

Verify equivalence with the corresponding Kraus representation where the partial trace is physically justified.

Then retain a coherent \(NN\)-\(NN\pi\) or double-scattering superposition and demonstrate that tracing before amplitudes are combined produces the wrong interference observable.

Complete positivity is a property of the reduced density map, not of the amplitude map. The CP map may not replace unresolved coherent physics.

---

# 12. Tensor-network extension

Extend the C15 nuclear tensor network to

```text
NN_BRANCH
NNPI_BRANCH
```

with explicit edges for:

- deuteron helicity;
- nucleon helicities;
- pion charge/isospin;
- \(NN\) spin/isospin;
- Jacobi orbital labels;
- S/D ancestry;
- sector identity;
- nuclear resolution and plan;
- nucleon microscopic member;
- Wilson order and operator identity.

Represent the Hamiltonian and partonic/current operators as separate operator networks.

Full bond must reproduce direct diagonalization or the exact finite-sector benchmark.

Reduced-bond convergence must be reported for:

- \(Z_{NN\pi}\);
- pion-active quark/antiquark/gluon moments;
- \(NN\leftrightarrow NN\pi\) transition interference;
- \(b_1\) and tensor channels;
- two-body current matrix elements;
- angular-condition residual;
- coherent tensor correction;
- parton–nuclear overlap cancellation.

At least one low-rank network must retain a small norm or energy defect while losing a real pion-transition, tensor, current, or coherent feature.

---

# 13. Assumption-conditioned plans

Implement immutable, mutually exclusive plans such as:

```text
N1-PLAN-A
    AV18 NN state
    H7 PLAN-A correlated nucleons
    explicit spin-resolved NNPI sector
    pion-nucleon transition interaction enabled
    matched pion-overlap subtraction enabled
    coherent pilot disabled by default

N1-PLAN-B
    Norfolk NN state
    H7 PLAN-A correlated nucleons
    explicit spin-resolved NNPI sector
    pion-nucleon transition interaction enabled
    matched pion-overlap subtraction enabled
    coherent pilot disabled by default

N1-PLAN-C
    AV18 NN state
    H7 PLAN-B correlated nucleons
    explicit spin-resolved NNPI sector
    pion-nucleon transition interaction enabled
    matched pion-overlap subtraction enabled
    coherent pilot disabled by default

N1-COHERENT-PILOT
    one chosen N1 state plan
    helicity-resolved analytic diffractive input
    explicit parton-nuclear overlap subtraction
    validation-only

N0-REFERENCE
    read-only C15 NN-only plan
    no NNPI sector
```

The coherent pilot is an additive operator mechanism only when its full typed overlap subtraction is present. Nuclear wave-function plans and H7 nucleon plans remain exclusive theories and may not be summed.

---

# 14. Ledgers and closures

C16 must close, separately and together:

## State

\[
Z_{NN}+Z_{NN\pi}=1.
\]

## Baryon number

\[
B_D=2.
\]

## Charge

\[
Q_D=+1
\]

across all pion charge channels.

## Plus momentum

Within each sector and in the full state,

\[
\sum_i y_i=1.
\]

## Isospin and parity

At the reference point,

\[
I=0,\qquad J^P=1^+.
\]

## Current

Charge, finite-basis continuity, current-component, and angular-condition residuals remain separately visible.

## Partonic

Quark, antiquark, gluon, pion-active, transition, and coherent contributions preserve number/momentum conventions and common operator identities.

## Tensor

The \(\delta_T\) and \(f_{1LL}=-(2/3)\delta_T f_1\) routes agree after convention adaptation. \(SS\), \(SD\), \(DS\), \(DD\), \(NN\pi\), transition, and coherent ancestries remain separately available.

## Tagged/inclusive

Any new tagged or pion-tagged validation kernel must integrate to the appropriate inclusive N1 parent.

## Provenance

Internal pion, exchange pion, overlap subtraction, transition operators, coherent amplitudes, CP reduction, and partonic/nuclear soft regions are counted exactly once.

---

# 15. Required benchmark families

Implement at least the following benchmark families with stable IDs.

## N1-A — Three-body kinematics and recoil

- three-body support and intrinsic closure;
- active nucleon and active pion recoil;
- unit Jacobian;
- unchanged physical spectators;
- transfer reversal;
- transition recoil conservation;
- independent algebraic oracle.

## N1-B — \(NN\pi\) spin/isospin/parity basis

- complete charge-channel reconstruction;
- total \(I=0\);
- total \(J^P=1^+\);
- orthonormality;
- exact nucleon exchange symmetry;
- pion charge and orbital identity;
- deliberate omission of one charge channel fails.

## N1-C — Coupled Hamiltonian

- block Hermiticity;
- generated adjoint;
- exact versus matrix-free action;
- exact/Krylov agreement;
- normalization and phase tracking;
- resolution flow;
- parameter null-direction reporting.

## N1-D — Pion-active diagonal operator

- direct active-pion slot;
- quark/antiquark/gluon analytic-parent ledgers;
- exact zero when \(Z_{NN\pi}=0\);
- no copied nucleon distribution;
- forward and nonzero-transfer closure.

## N1-E — Transition operator

- \(NN\leftrightarrow NN\pi\) matrix elements;
- Hermitian pair;
- interference sign and phase;
- exact zero when the transition coupling is disabled;
- recoil and charge closure.

## N1-F — Internal/exchange pion subtraction

- three-term matched sum;
- separation-scale variation;
- missing subtraction failure;
- duplicate subtraction failure;
- explicit plus induced/contact double-counting rejection;
- stable matched total within truncation error.

## N1-G — Nuclear current and continuity

- nucleon, pion-in-flight, transition/contact, induced, and counterterm pieces;
- exact closure in the analytic benchmark;
- signed ablations for each required contribution;
- charge and angular-condition closure;
- current/GTMD moment agreement.

## N1-H — Full N1 deuteron parent

- \(NN\), \(NN\pi\) diagonal, and transition contributions;
- complete \(6\times6\) quark/antiquark target–parton matrices;
- complete gluon target/field-index parent;
- all Wilson orders 0, 1, 2 preserved from the nucleon;
- spin-1 projector reconstruction;
- TMD/GPD/PDF/current/EMT/Wigner closure.

## N1-I — \(b_1\) and tensor ancestry

- direct helicity difference;
- LL projector route;
- GTMD-to-PDF route;
- separate S/D, pion-active, transition, and coherent-pilot contributions;
- pure-S, zero-D, zero-pion, and zero-transition limits.

## N1-J — Coherent double scattering

- zero elementary-amplitude limits;
- longitudinal-order reversal;
- explicit scalar/vector/tensor projections;
- copied-unpolarized-ratio failure;
- coherent-before-trace requirement.

## N1-K — Parton/nuclear overlap subtraction

- one correct subtraction closes;
- omitted and duplicate subtraction give signed residuals;
- partonic path identity remains immutable;
- nuclear coherent identity remains distinct.

## N1-L — Derived CP map

- amplitude embedding;
- partial trace versus Kraus equality;
- positivity and trace closure;
- early trace fails a coherent interference observable.

## N1-M — Tensor-network convergence

- exact/full-bond equality;
- reduced-bond convergence;
- observable-sensitive loss in pion, transition, current, tensor, or coherent channels.

## N1-N — Assumption compiler and provenance

- all plans compile independently;
- mixed wave-function or H7 plans fail;
- internal/exchange pion without subtraction fails;
- coherent pilot without overlap map fails;
- unsupported nuclear mechanisms remain unavailable;
- rollback removes the N1 validation root without affecting C15 or production.

---

# 16. Mandatory negative injections

Create stable, ordered C16 injection IDs. Include at least **280 new C16 injections**. They must cover at minimum:

## Baseline and source integrity

- wrong C15 ancestry;
- modified C15 manifest;
- missing normative source without an absence record;
- altered authoritative artifact;
- changed 216-route registry.

## Three-body coordinates

- nonpositive momentum fraction;
- fractions not summing to one;
- transverse momenta not closing;
- two-body coordinate reused without adapter;
- wrong active-pion recoil;
- wrong spectator shift;
- nonunit Jacobian;
- transition recoil treated as diagonal recoil;
- wrong transfer partition;
- local reimplementation of recoil.

## Quantum numbers

- incomplete pion charge channels;
- wrong total charge;
- wrong total isospin;
- wrong parity;
- wrong \(J^z\);
- missing pion orbital parity;
- broken nucleon exchange;
- copied proton/neutron state;
- mixed microscopic members.

## Hamiltonian

- missing adjoint;
- mismatched regulator;
- mismatched pion form factor;
- unsupported block treated as zero;
- double-counted induced interaction;
- hidden parameter null direction;
- independently normalized sectors;
- post-hoc state renormalization.

## Pion operators

- pion parent copied from nucleon;
- negative-\(x\) antiquark copied into positive-\(x\);
- pion-active normalization fitted independently;
- missing pion charge;
- pion oracle promoted to physical TMD;
- unsupported gluon pion channel silently filled;
- transition operator missing reverse block.

## Pion overlap subtraction

- internal plus exchange without subtraction;
- duplicate subtraction;
- subtraction from unrelated projector;
- separation scale absent from identity;
- explicit \(NN\pi\) plus integrated-out contact selected together;
- scalar pion correction added after matched sum;
- overlap remainder hidden.

## Current

- pion-in-flight omitted;
- contact term omitted;
- transition current omitted;
- induced current omitted;
- current regulator differs from Hamiltonian;
- one coefficient per helicity amplitude;
- one normalization per momentum transfer;
- continuity defect clipped;
- angular condition fitted away.

## Coherent pilot

- scalar unpolarized ratio copied into tensor sector;
- elementary amplitude missing but nonzero result returned;
- early partial trace;
- missing longitudinal phase;
- wrong order reversal;
- untyped diffractive input;
- physical shadowing status claimed;
- coherent amplitude multiplied onto all TMDs;
- unsupported Glauber status promoted.

## Partonic/nuclear overlap

- partonic Wilson and nuclear propagation aliased;
- missing overlap subtraction;
- duplicate overlap subtraction;
- C14 phase budget mutated in place;
- tagged FSI identified with coherent propagation;
- process color mixture assigned.

## CP maps

- CP map applied before coherence resolved;
- non-CP amplitude map called a channel;
- incomplete Kraus set called trace preserving;
- negative state clipped;
- CP map used to replace transition interference.

## Tensor network

- lost sector edge;
- lost pion charge;
- lost isospin;
- lost orbital parity;
- low bond accepted on energy alone;
- full bond differs from exact state;
- operator network merged with state network;
- recoupling changes result without certificate.

## Downstream gates

- production promotion;
- physical deuteron claim;
- physical pion TMD claim;
- nuclear Glauber readiness;
- LF-to-QCD matching claim;
- evolution request;
- process request;
- inference request;
- hidden-color, \(\Delta\Delta\), or six-quark sector silently activated.

Every injection must produce a structured diagnostic, not a generic exception.

---

# 17. Production isolation and immutable regression

C16 must remain unreachable from:

```text
the 216-route production registry
production provenance root
production default composition plan
production resolved-parent builder
LF-to-QCD matching
TMD evolution
physical process maps
inference/calibration
```

All eight authoritative artifacts must remain byte-identical.

C15 plans and manifests remain immutable. C16 may read them but may not rewrite them.

The N1 validation root must be removable as one scoped provenance branch, restoring the exact C15 state.

---

# 18. Required documentation and machine-readable deliverables

Create at least:

```text
docs/next_level/c16_implementation_report.md
docs/next_level/c16_api.md
docs/next_level/c16_normative_source_integration.json
docs/next_level/c16_requirement_coverage.json
docs/next_level/c16_injection_manifest.json
docs/next_level/c16_regression_report.json
docs/next_level/c16_nnpi_state_manifest.json
docs/next_level/c16_nnpi_basis_manifest.json
docs/next_level/c16_three_body_recoil_manifest.json
docs/next_level/c16_hamiltonian_flow.json
docs/next_level/c16_pion_active_operator_manifest.json
docs/next_level/c16_transition_operator_manifest.json
docs/next_level/c16_pion_subtraction_manifest.json
docs/next_level/c16_two_body_current_closure.json
docs/next_level/c16_coherent_smallx_manifest.json
docs/next_level/c16_parton_nuclear_overlap_manifest.json
docs/next_level/c16_cp_reduction_manifest.json
docs/next_level/c16_deuteron_parent_manifest.json
docs/next_level/c16_tensor_network_manifest.json
docs/next_level/c16_provenance_complex.json
docs/next_level/c16_tolerance_manifest.json
docs/next_level/c16_unresolved_physics_gaps.md
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md
```

when the relevant normative source has been added.

All generated JSON must be deterministic. Rebuild it and verify byte-identical hashes before the final commit.

---

# 19. Acceptance criteria

C16/N1 is complete only when all of the following are satisfied:

1. The complete C15 baseline reproduces before modification.
2. A typed, normalized \(NN\oplus NN\pi\) spin-1 state exists.
3. The \(NN\pi\) basis has complete charge/isospin content and correct \(J^P=1^+\).
4. Three-body and transition recoil maps pass independent closure tests.
5. The coupled Hamiltonian is Hermitian and solved by exact and matrix-free routes.
6. The state, baryon, charge, plus-momentum, isospin, and parity ledgers close.
7. Pion-active, nucleon-active, and transition operators are distinct and reconstruct the full N1 parent.
8. The N1 parent retains complete quark, antiquark, gluon, Wilson-link, and spin-1 matrix identity.
9. The pion-active contribution is generated by the \(NN\pi\) amplitude and not independently normalized.
10. The internal/exchange pion overlap subtraction is executable and stable under the declared separation variation.
11. Explicit and induced pion descriptions cannot be selected simultaneously without the matching two-cell.
12. The Hamiltonian-consistent current closes the finite-basis continuity benchmark only with all required pieces.
13. Current, angular-condition, and GTMD/GPD moment routes close within declared tolerances.
14. \(b_1\) and tensor routes retain S/D, pion-active, transition, and coherent ancestry.
15. The coherent pilot uses helicity amplitudes and cannot be reproduced by a copied unpolarized ratio.
16. Partonic Wilson and nuclear coherent dynamics remain distinct and have an explicit overlap ledger.
17. The CP map is derived after coherent combination and early tracing demonstrably fails.
18. Full-bond TTN reproduces exact N1 observables.
19. Reduced-bond errors are reported on pion, current, tensor, and coherent observables.
20. All C16 plans compile independently and incompatible plans fail closed.
21. At least 280 C16 injections pass.
22. All prior tests, builders, evidence rows, atlas pages, requirements, and injection suites remain passing.
23. The 216-route production registry and production provenance/composition remain unchanged.
24. All eight authoritative artifacts and all 16 C15 JSON artifacts remain byte-identical.
25. All new manifests reproduce byte-for-byte.
26. The final documentation states the remaining unavailable sectors and does not overclaim readiness.
27. The working tree is clean after a local commit.
28. Nothing is pushed.

---

# 20. Permitted readiness statuses

C16 may issue only qualified statuses such as:

```text
N1_NNPI_STATE_VALIDATED
N1_THREE_BODY_RECOIL_VALIDATED
N1_PION_ACTIVE_OPERATOR_VALIDATED
N1_TRANSITION_OPERATOR_VALIDATED
N1_PION_SUBTRACTION_BENCHMARKED
N1_FINITE_BASIS_CONTINUITY_BENCHMARKED
N1_COHERENT_HELICITY_PILOT_VALIDATED
N1_PARTON_NUCLEAR_OVERLAP_BENCHMARKED
N1_CP_REDUCTION_VALIDATED
N1_COMMON_DEUTERON_PARENT_VALIDATED
N1_TTN_CONVERGENCE_BENCHMARKED
```

It must continue to refuse:

```text
PHYSICAL_DEUTERON_PREDICTION
PHYSICAL_PION_TMD
COMPLETE_SHADOWING
NUCLEAR_GLAUBER_READY
COMPLETE_EXCHANGE_CURRENT_BASIS
DELTADELTA_READY
SIX_QUARK_READY
HIDDEN_COLOR_READY
LF_TO_QCD_MATCHING_READY
TMD_EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

---

# 21. Final response

At completion, report:

- starting and final commits;
- push status and working-tree status;
- complete test/builder/evidence/atlas counts;
- C16 requirement and injection counts;
- N1 tower dimensions;
- \(Z_{NN}\) and \(Z_{NN\pi}\) flow;
- three-body recoil and normalization residuals;
- charge/isospin/parity residuals;
- Hamiltonian and solver residuals;
- pion-active and transition closure;
- pion subtraction and separation-variation residuals;
- current/continuity and angular-condition residuals;
- coherent-pilot and parton/nuclear overlap residuals;
- exact/full-bond and reduced-bond tensor-network results;
- all new manifest hashes;
- immutable production and C15 regression status;
- unresolved sectors and exact recommended C17 package.

Do not declare completion until every acceptance criterion passes.

Do not push the final commit.
