# C12/H5 Codex Work Package

## Microscopic Wilson-line dynamics on the H4 helicity-matrix parent

**Package ID:** `C12_H5_MICROSCOPIC_WILSON_ON_H4`

**Authoritative physics baseline:**

```text
664fd5e70296590b910825e8a94d1d0377179566
```

A documentation-only descendant is acceptable only if the baseline commit remains in its ancestry and every C11 regression gate reproduces before implementation begins.

Do not use `origin/main` as the scientific baseline unless it resolves to the commit above. The local branch may be ahead of the remote.

Do not push the final commit.

---

## 1. Objective

Attach the validated C5/C6 Wilson-path, pole, resolvent, cut, ordered-link, color, phase-budget, and soft-overlap machinery to the **microscopic C11/H4 quark–antiquark–gluon helicity-matrix parent**.

C12 must implement, at zero skewness and first nontrivial Wilson order,

```text
H4 microscopic state and nonzero-transfer helicity parent
    -> oriented Wilson insertion
    -> declared spectral support
    -> distributional light-front cut
    -> antiunitary link reversal
    -> link-even/link-odd helicity matrices
    -> distinct quark Sivers and Boer–Mulders projections
    -> direct-antiquark link-odd projections
    -> active-gluon ordered-link f/d projections
    -> one-order soft/rapidity overlap accounting
    -> convergence, provenance, and replacement manifests
```

The new result is a **regulated finite-basis validation parent**. It is not a physical soft-subtracted TMD, not an evolved distribution, not a process prediction, and not a nuclear object.

The imaginary part must arise only from an explicitly declared spectral discontinuity or cut. A finite numerical epsilon is never physical support.

---

## 2. Normative sources

Read these files completely before editing code:

```text
docs/next_level/c11_h4_codex_prompt.md
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md

docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c6_benchmark_manifest.json

docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md

docs/next_level/c10_implementation_report.md
docs/next_level/c10_api.md

docs/next_level/c9_implementation_report.md
docs/next_level/c9_api.md

references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_iii_dynamical_wilson_lines.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_ix_dynamical_gluon_fock_sectors.tex
references/volume_x_light_sea_chiral_pcac_antiquark_gtmds.tex
references/volume_xi_microscopic_nonzero_transfer_gtmds.tex
```

If a normative source is missing, record that fact and its expected hash in the source-integration report. Do not invent its contents. This prompt contains the minimum indispensable equations and gates, so a missing optional document does not justify stopping the rest of the package.

Record exact source hashes in:

```text
docs/next_level/c12_normative_source_integration.json
```

---

## 3. Mandatory baseline reproduction

Before changing code, reproduce and record:

```text
893/893 tests
10/10 C11 builders and architecture validators
36/36 evidence rows
162/162 atlas pages
285 C11 requirements
104/104 C11 negative injections
all earlier C3–C10 injection suites
216 accepted production reductions
all eight authoritative artifacts byte-identical
production provenance and default composition unchanged
C3/C4 analytic parents unchanged
pinned C5/C6 manifests unchanged
```

Create a pre-edit baseline record. Do not proceed if a scientific regression is unexplained.

---

## 4. Immutable physics boundaries

C12 must not:

- modify the accepted 216-route phenomenological registry;
- alter any authoritative numerical artifact;
- retune C11 T-even GTMD coefficients to make a T-odd test pass;
- introduce a fitted Sivers, Boer–Mulders, antiquark, or gluon-T-odd normalization;
- impose a universal scalar phase on unrelated operators;
- use a process-name switch as the source of the future/past sign;
- use finite numerical epsilon as physical absorption;
- silently merge gluon ordered-link identity with the `f`/`d` color class;
- silently infer physical cut support from a discrete off-shell spectrum;
- claim complete ultraviolet matching, rapidity renormalization, soft subtraction, evolution, or factorization;
- enter nuclear composition, physical process maps, inference, or production.

The strongest result is a validation-only first-Wilson-order microscopic link-odd parent.

---

## 5. Required implementation package

Extend the existing formal and microscopic packages rather than creating a parallel type system. Suggested objects include:

```text
MicroscopicSpectralSupport
SpectralSupportRule
ContinuumCutMeasure
FiniteVolumeSpectralRule
SpectralThreshold
H4WilsonInsertion
MicroscopicResolventChannel
MicroscopicIntermediateState
MicroscopicCutLedger
FockOrderSupportManifest
LinkOddHelicityParent
QuarkLinkOddProjectorRegistry
AntiquarkLinkOddProjectorRegistry
GluonOrderedLinkColorParent
MicroscopicSoftOverlapAccount
H5PhaseBudget
H5ConvergenceManifest
H5ReplacementManifest
```

Use the actual C11, C10, C6, and C5 APIs discovered in the repository. Adapt names to the existing architecture, but preserve the responsibilities and fail-closed behavior defined here.

---

## 6. H4 input contract

Consume the actual C11 microscopic parent, not an independently generated scalar table.

For every result retain:

- H3/H4 assumption plan (`PLAN-A` or `PLAN-B`);
- proton or neutron target identity;
- microscopic member and resolution identity;
- exact/Krylov/TTN state representation identity;
- species and flavor (`u`, `d`, `ubar`, `dbar`, `g`);
- complete incoming and outgoing target–parton helicity indices;
- `x`, `kT`, `DeltaT`, and the authoritative recoil identity;
- operator, rank, mass, and Fourier conventions;
- Wilson path or ordered link-pair identity;
- color representation and outer multiplicity;
- cut-support, regulator, and phase-budget identity;
- convergence and readiness status.

C12 must act on the full 4x4 quark/antiquark matrices and complete gluon tensor/helicity parent **before** named scalar projections are formed.

---

## 7. Wilson-order declaration

The central C12 calculation is restricted to:

```text
WILSON_ORDER = 1
SKEWNESS = 0
H4_PARENT = microscopic C11 parent
```

The Wilson expansion is

\[
U_\gamma = 1 + U_\gamma^{(1)} + \mathcal O(g^2).
\]

Higher Wilson orders remain unavailable unless the required explicit Fock sectors or matched induced operators are present and validated.

Every result must carry a `FockOrderSupportManifest` recording whether each attachment is:

```text
EXPLICIT_FOCK_SUPPORTED
INDUCED_OPERATOR_SUPPORTED_WITH_REMAINDER
UNAVAILABLE_AT_THIS_FOCK_ORDER
```

Do not call a channel microscopically complete when a required `qqqgg` or `qqqqqbar g` intermediate sector is absent.

---

## 8. Oriented paths and derived poles

Reuse the C5/C6 path objects. For the reference convention,

\[
\gamma_\eta(\lambda)=a+\eta\lambda v,
\qquad \lambda\geq0,
\]

and

\[
D_\eta(\ell)
=
\frac{1}{v\!\cdot\!\ell-i0\,\eta}
=
\operatorname{PV}\frac{1}{v\!\cdot\!\ell}
+i\eta\pi\delta(v\!\cdot\!\ell).
\]

The pole sign must be derived from the stored path orientation, Fourier convention, momentum-flow convention, and coupling convention. It cannot be passed independently by a caller.

Test exact path composition, inversion, endpoint exchange, and full future/past transformation.

---

## 9. Genuine spectral support

C9 and C11 correctly return zero absorption for a discrete off-shell spectrum. C12 must add an explicit validation-level spectral rule rather than changing that behavior.

Implement at least two independent support routes:

### 9.1 Analytic continuum oracle

For a declared spectral density `rho_X(E)` and numerator `N_X(E)`, evaluate

\[
\mathcal A_\sigma(E_i)
=
\int dE\,
\frac{\rho_X(E)N_X(E)}{E_i-E+i0\sigma}.
\]

The cut contribution must satisfy

\[
\operatorname{Im}\mathcal A_\sigma(E_i)
=
-\sigma\pi\rho_X(E_i)N_X(E_i)
\]

when `E_i` lies in the declared support and must vanish exactly below threshold.

### 9.2 Finite-volume or discretized-continuum rule

Implement a typed sequence of finite-volume/discretized spectral measures that converges to the analytic continuum oracle. Report convergence versus volume, level spacing, smearing used only for quadrature, and threshold location.

Numerical smearing may approximate the distributional integral but cannot enter the physical result identity or create support where the spectral rule has none.

### 9.3 H4 microscopic support map

Map the supported H4 state blocks and Wilson attachments to the declared intermediate-state channels. Every channel must record:

- initial state;
- intermediate sector and quantum numbers;
- energy denominator;
- support threshold;
- active and spectator attachments;
- color and helicity kernel;
- OAM interference;
- explicit or induced Fock support;
- cut identity.

If a microscopic channel lacks support, return a structured unavailable result. Do not silently borrow support from an unrelated analytic benchmark.

---

## 10. Cut ledger and no-double-counting

The `MicroscopicCutLedger` must distinguish:

- the eikonal delta contribution;
- the light-front resolvent cut;
- equivalent representations of the same physical on-shell support;
- genuinely distinct cuts with coincident numerical denominators;
- soft-overlap regions.

The graph must count equivalent support once through an explicit two-cell such as:

```text
EIKONAL_CUT
    EQUIVALENT_COUNT_ONCE
LF_RESOLVENT_CUT
```

It must not deduplicate distinct physical channels merely because their denominator values match.

Duplicate support without a relation must fail before numerical evaluation.

---

## 11. Quark and antiquark link-odd helicity matrices

Construct, before scalar projection,

\[
\mathcal M_{\rm odd}^{q}
=
\frac12\left[
\mathcal M_q^{[+]}
-
\Theta^{-1}\mathcal M_q^{[-]}\Theta
\right],
\]

and the corresponding direct positive-`x` antiquark matrix

\[
\mathcal M_{\rm odd}^{\bar q}.
\]

The antiunitary transformation must include:

- complex conjugation;
- incoming/outgoing fiber exchange;
- path reversal and endpoint exchange;
- transverse momentum reversal as required by the declared convention;
- target and parton helicity phases;
- fundamental versus anti-fundamental color action;
- operator charge-conjugation signature;
- exact H4 member identity.

Antiquarks must use

\[
t_{\bar3}^a=-(t_3^a)^T,
\qquad
U_{\bar3}[\gamma]=U_3[\gamma]^*.
\]

Do not generate antiquark results by copying the quark matrix or by a label-only sign change.

---

## 12. Sivers and Boer–Mulders projections

From the same quark or antiquark link-odd matrix, implement distinct projectors for:

\[
f_{1T}^{\perp q}
\sim
\operatorname{Tr}[P_{\rm Siv}\mathcal M_{\rm odd}^{q}],
\]

\[
h_1^{\perp q}
\sim
\operatorname{Tr}[P_{\rm BM}\mathcal M_{\rm odd}^{q}].
\]

The projectors act on different target/active-parton spin structures and select different OAM/helicity interference blocks.

The following is prohibited:

\[
h_1^{\perp q}=C_q f_{1T}^{\perp q}
\]

or any equivalent imposed proportionality.

Mandatory zero tests:

\[
g\to0 \Rightarrow \mathcal M_{\rm odd}=0,
\]

\[
\text{cut support removed} \Rightarrow \mathcal M_{\rm odd}=0,
\]

\[
L_z\text{ interference removed} \Rightarrow \mathcal M_{\rm odd}=0,
\]

\[
\text{future/past averaged} \Rightarrow \text{link-odd projection}=0.
\]

Report flavor, proton/neutron, sea, OAM, and assumption-plan dependence from the common microscopic state. Do not fit these dependencies independently.

---

## 13. Active-gluon ordered-link and color channels

Reuse the C6 ordered two-link and color machinery on the C11 microscopic gluon parent.

Retain all four ordered pairs:

```text
[+,+]
[-,-]
[+,-]
[-,+]
```

and independent color projections

\[
K_f=\frac{-if^{abc}K^{abc}}{24},
\qquad
K_d=\frac{d^{abc}K^{abc}}{40/3}.
\]

Require:

\[
f^{abc}d^{abc}=0,
\qquad
f^{abc}f^{abc}=24,
\qquad
d^{abc}d^{abc}=\frac{40}{3}.
\]

One microscopic gluon tensor parent must supply, independently in both color channels:

- trace/unpolarized projection;
- helicity-antisymmetric/circular projection;
- symmetric-traceless/linear-polarization projection;
- complete target-helicity matrix identity.

Do not create a default `f+d` mixture. Process color weights remain unavailable until a qualified process map exists.

Swapping the ordered links must not silently leave the operator identity unchanged.

---

## 14. Soft and rapidity overlap accounting

C12 remains an unsubtracted-regulated microscopic calculation but must connect the H4 result to the C6 phase-budget structure.

At first Wilson order, implement the accounting identity

\[
W_{\rm sub}^{(1)}
=
W_{\rm unsub}^{(1)}
-\frac12 S^{(1)}W^{(0)}
+R_{\rm rap}^{(1)}W^{(0)}
+Z_{\rm UV}^{(1)}W^{(0)}.
\]

For the executable validation route, a shared rapidity-sensitive overlap must cancel exactly once. Demonstrate:

```text
one declared subtraction       -> rapidity derivative closes
missing subtraction            -> nonzero signed residual
duplicate subtraction          -> equal-and-opposite residual
```

Keep the following unresolved and explicit:

```text
UV_FINITE_MATCHING_REQUIRED
PHYSICAL_TMD_SCHEME_NOT_ASSIGNED
CONTINUUM_SOFT_FUNCTION_INCOMPLETE
NO_COLLINS_SOPER_EVOLUTION
NO_PROCESS_FACTOR_APPLIED
```

The mutually exclusive routes remain:

```text
BOUNDARY_ONLY_RESCATTERING
JOINT_MICROSCOPIC_SOFT_SECTOR
```

Do not execute both for one result. If the joint route is not fully implemented, keep it unavailable rather than emulating it with another subtraction.

---

## 15. Exact and TTN paths

Evaluate every principal H5 benchmark with:

- the exact H3/H4 eigenvector;
- the full-bond TTN;
- at least two reduced-bond TTNs.

Full bond must reproduce exact link-even/link-odd matrices and projectors within declared numerical tolerances.

Report finite-bond convergence separately for:

- total link-odd matrix norm;
- Sivers projection;
- Boer–Mulders projection;
- antiquark link-odd projection;
- active-gluon `f` and `d` channels;
- OAM interference;
- cut weight;
- Ward/color residuals;
- soft-overlap cancellation.

A reduced bond that preserves energy but erases a link-odd OAM interference must be reported as unconverged for that observable.

---

## 16. Convergence axes

Report independent convergence and discrepancy components for at least:

1. H3/H4 resolution level;
2. Fock support;
3. OAM support;
4. exact/Krylov state path;
5. exact/full-bond TTN;
6. finite TTN bond;
7. `kT` quadrature;
8. `DeltaT` grid and derivative;
9. principal-value quadrature;
10. continuum spectral quadrature;
11. finite-volume/discretized spectral resolution;
12. threshold location;
13. Wilson-path quadrature;
14. color and ordered-link reconstruction;
15. soft-overlap subtraction;
16. Gram/projector conditioning.

Do not combine these into one generic error bar.

---

## 17. Scoped replacement of C5/C6 pilots

C5 and C6 remain immutable analytic oracles.

Create scoped relations such as:

```text
C5_ANALYTIC_QUARK_WILSON_PILOT
    BENCHMARKS
H5_MICROSCOPIC_QUARK_WILSON_PARENT

C6_ANALYTIC_ACTIVE_GLUON_PILOT
    BENCHMARKS
H5_MICROSCOPIC_GLUON_WILSON_PARENT

H5_MICROSCOPIC_*_PARENT
    REPLACES_WITHIN_SCOPE
C5/C6_ANALYTIC_PILOT
```

The replacement scope must include:

- H4 assumption plan and member;
- species/flavor;
- Wilson order one;
- zero skewness;
- supported transfer and transverse-momentum domain;
- declared spectral support rule;
- explicit or induced Fock support;
- passed cut, symmetry, color, soft-overlap, and convergence gates.

Do not require numerical equality with the analytic pilots. Their role is algebraic and sign/convention validation.

Rollback must be the removal of the H5 validation root.

---

## 18. Readiness statuses

Permitted statuses include:

```text
H5_SPECTRAL_SUPPORT_BENCHMARKED
H5_MICROSCOPIC_QUARK_LINK_ODD_PARENT_VALIDATED
H5_MICROSCOPIC_ANTIQUARK_LINK_ODD_INTERFACE_VALIDATED
H5_MICROSCOPIC_GLUON_FD_LINK_ODD_PARENT_VALIDATED
H5_SIVERS_BOER_MULDERS_PROJECTORS_VALIDATED
H5_SOFT_OVERLAP_ACCOUNTED_AT_WILSON_ORDER_1
H5_EXACT_TTN_WILSON_CLOSURE_VALIDATED
H5_SCOPED_C5_C6_REPLACEMENT_VALIDATED
```

The following remain forbidden:

```text
PHYSICAL_TMD
MATCHED_GTMD
WILSON_ALL_ORDERS_READY
FULL_NONABELIAN_GAUGE_CLOSURE
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

An antiquark or gluon result supported only through an induced omitted-sector operator must say so in its status and carry the nonzero remainder.

---

## 19. Mandatory benchmarks

Implement at least the following benchmark families.

### H5-A: analytic spectral cut

- exact threshold behavior;
- exact distributional imaginary part;
- zero below threshold;
- opposite future/past sign;
- finite-volume/discretized convergence.

### H5-B: microscopic quark link reversal

- full 4x4 matrix transformation;
- exact link-even/link-odd decomposition;
- Hermiticity and parity;
- coupling, cut, and OAM zero limits.

### H5-C: direct antiquark transformation

- positive-`x` active antiquark slot;
- anti-fundamental generator;
- charge-conjugation signature;
- no quark-copy shortcut;
- explicit/induced Fock-support status.

### H5-D: Sivers versus Boer–Mulders

- shared kernel;
- distinct projectors;
- distinct interference ancestry;
- no imposed proportionality;
- flavor and proton/neutron dependence from the state.

### H5-E: microscopic active-gluon `f/d`

- all ordered link pairs;
- exact `f` and `d` norms and orthogonality;
- independent color channels;
- trace/helicity/linear reconstruction;
- no process mixture.

### H5-F: soft/rapidity overlap

- one subtraction closes the rapidity derivative;
- missing and duplicate subtractions give signed residuals;
- unresolved UV finite matching remains nonzero/unresolved.

### H5-G: exact/TTN convergence

- full-bond equality;
- observable-sensitive low-bond failure;
- separate convergence of quark, antiquark, and gluon link-odd channels.

### H5-H: cut-ledger and provenance

- equivalent support counted once;
- distinct support retained;
- Fock-support status enforced;
- explicit and induced routes mutually exclusive unless matched with a remainder.

### H5-I: scoped C5/C6 replacement

- analytic pilots unchanged;
- microscopic result active only inside H5 scope;
- no path to production or downstream physical layers.

### H5-J: Wilson-order/Fock-order compatibility

- unsupported higher-order channel rejected;
- missing `qqqgg` or `qqqqqbar g` support reported honestly;
- no false all-orders status.

---

## 20. Required negative injections

Add at least **120 stable C12 negative-test identities** with deterministic diagnostics. They must include, at minimum:

### Spectral and cut failures

- physical phase generated by finite epsilon;
- support below threshold;
- omitted spectral-rule identity;
- wrong cut sign;
- duplicate equivalent cut;
- accidental deduplication of distinct cuts;
- mismatched initial/intermediate energy;
- spectral support borrowed from an unrelated channel;
- nonconvergent finite-volume rule accepted;
- threshold changed without identity change.

### Path and antiunitary failures

- caller-supplied independent pole sign;
- future/past label-only subtraction;
- missing complex conjugation;
- missing endpoint exchange;
- missing momentum reversal;
- wrong target-helicity phase;
- wrong parton-helicity phase;
- incomplete ordered-link reversal;
- path inversion without operator transformation.

### Quark/antiquark failures

- antiquark copied from quark;
- wrong anti-fundamental generator sign;
- lost positive-`x` antiquark identity;
- Sivers and Boer–Mulders projectors aliased;
- fitted scalar phase;
- universal flavor phase;
- missing OAM block accepted as physical zero;
- quark and antiquark current signatures mixed.

### Gluon failures

- ordered link pair collapsed;
- `f`/`d` class inferred from link topology;
- default `f+d` mixture;
- wrong color normalizations;
- nonzero `f dot d` accepted;
- trace/helicity/linear pieces generated from separate parents;
- color outer multiplicity erased;
- process color weight applied without process map.

### Soft/matching failures

- missing half-soft subtraction;
- duplicate subtraction;
- UV matching silently set to zero;
- physical TMD scheme assigned without a matching map;
- boundary-only and joint-soft routes selected together;
- rapidity cancellation claimed without derivative test;
- Collins–Soper evolution applied to the unmatched object.

### Fock/order failures

- Wilson order two accepted with order-one Fock support;
- missing `qqqgg` support hidden;
- missing pair-plus-gluon sector hidden;
- induced operator used without remainder;
- explicit and induced support added together;
- discrete off-shell state given absorption.

### Isolation failures

- mutation of the 216-route registry;
- mutation of production provenance;
- mutation of an authoritative artifact;
- C5/C6 pilot changed;
- H5 result reaches nuclear composition;
- H5 result reaches evolution, process, inference, or production;
- missing normative-source mutation detection.

---

## 21. Documentation and machine-readable deliverables

Create at least:

```text
docs/next_level/c12_implementation_report.md
docs/next_level/c12_api.md
docs/next_level/c12_normative_source_integration.json
docs/next_level/c12_requirement_coverage.json
docs/next_level/c12_regression_report.json
docs/next_level/c12_spectral_support_manifest.json
docs/next_level/c12_cut_ledger.json
docs/next_level/c12_quark_antiquark_link_odd_manifest.json
docs/next_level/c12_gluon_fd_manifest.json
docs/next_level/c12_soft_overlap_report.json
docs/next_level/c12_fock_order_support_manifest.json
docs/next_level/c12_convergence_manifest.json
docs/next_level/c12_replacement_manifest.json
docs/next_level/c12_unresolved_physics_gaps.md
```

Update:

```text
handoff/ROADMAP.md
references/formalism_volume_index.md   # only when needed for newly added sources
```

All JSON must be deterministic, versioned, and validated by a repository script.

---

## 22. Final acceptance criteria

C12 is complete only when all of the following hold:

1. The complete C11 baseline reproduces before and after implementation.
2. The H4 common helicity parent is the sole microscopic input.
3. The pole sign is derived from path/Fourier/momentum-flow data.
4. Physical absorption occurs only under a declared spectral rule.
5. Analytic and finite-volume spectral routes agree within declared convergence errors.
6. Numerical epsilon is absent from physical identity.
7. The cut ledger counts equivalent support once and distinct support separately.
8. Quark and antiquark link-odd matrices are constructed before scalar projection.
9. Direct positive-`x` antiquark identity and anti-fundamental color action are retained.
10. Sivers and Boer–Mulders arise from one kernel and distinct projectors.
11. All coupling/cut/OAM/link-average zero limits close.
12. The active-gluon parent retains ordered links, both color channels, and all polarization sectors.
13. `f` and `d` norms, orthogonality, and reconstruction close.
14. One soft-overlap subtraction closes the analytic rapidity derivative.
15. Missing and duplicate subtraction tests fail with signed residuals.
16. Fock-order support is explicit for every channel.
17. Unsupported higher Wilson orders fail closed.
18. Full-bond TTN reproduces exact Wilson results.
19. Finite-bond observable loss remains visible.
20. C5/C6 analytic pilots remain immutable and are replaced only within H5 scope.
21. The 216-route production registry and all authoritative artifacts remain unchanged.
22. Nuclear, matching/evolution, process, inference, and production gates remain closed.
23. At least 120 ordered C12 negative injections pass.
24. All new manifests are deterministic and schema validated.
25. A clean local final commit is created and not pushed.

Do not declare completion if any criterion is unmet.

---

## 23. Final response format

Report:

- starting and final commits;
- test, builder, evidence, atlas, requirement, and injection counts;
- spectral-support routes and convergence residuals;
- maximum cut, symmetry, link-reversal, color, projector, and soft-overlap residuals;
- quark, antiquark, and gluon channel coverage;
- Fock-support statuses and visible remainders;
- exact/full-bond and finite-bond results;
- readiness statuses issued;
- immutable-regression confirmation;
- unresolved physics;
- exact recommended next package.

Do not push the final commit.

---

## 24. Expected next package

If C12 passes, recommend one of the following based on the actual unresolved gates:

```text
C13/N0
    matched spin-1 nuclear light-front state and deuteron GTMD composition
```

as the preferred route toward the project’s deuteron objective, or, if first-order Wilson completeness is blocked by missing microscopic sectors,

```text
C13/H6
    qqqgg and qqqq-qbar-g support plus second-order Dyson/Magnus convergence
```

Do not choose automatically. Base the recommendation on the C12 Fock-support and convergence manifests.
