# C10/H3 Codex Work Package

## Title

**C10/H3 — Fully antisymmetrized light-sea Fock sectors, chiral dynamics, axial/PCAC currents, explicit-versus-induced sea subtraction, and positive-x microscopic antiquark exports**

## Authoritative baseline

Begin from the local C9/H2 completion commit:

```text
31ae656da38a94432dd7f6c753d75e54170d9155
```

The required C9 commit must remain in the ancestry of the final C10 commit. The repository is intentionally ahead of `origin/main`; do **not** reset to, rebase onto, or otherwise replace the local scientific history with the remote branch.

A documentation-only descendant is acceptable before implementation if it only adds the missing normative sources listed below and leaves all executable artifacts unchanged.

Do not push. Complete the package locally, create one final local commit, and leave a clean working tree.

## Primary scientific objective

Extend the validated microscopic H2 state

\[
\mathcal H_{qqq}\oplus\mathcal H_{qqqg}
\]

to the first common interacting light-front state containing explicit light sea,

\[
\mathcal H_{\mathrm{H3}}
=
\mathcal H_{qqq}
\oplus
\mathcal H_{qqqg}
\oplus
\mathcal H_{qqqu\bar u}
\oplus
\mathcal H_{qqqd\bar d},
\]

with:

1. all three independent `qqqq-qbar` color-singlet multiplicities;
2. exact fermionic antisymmetry in the four-quark subsystem and the full creation-operator ordering;
3. separate positive-x `u-bar` and `d-bar` active-parton identities;
4. canonical `g <-> q qbar` pair creation/annihilation blocks and their generated adjoints;
5. a controlled chiral sector-changing interaction and a mutually exclusive induced-sea alternative;
6. sector-dependent renormalization for the three-, four-gluon-, and five-parton sectors;
7. Hamiltonian-consistent vector, axial, pseudoscalar, pair, and chiral exchange currents;
8. a finite-basis axial Ward/PCAC benchmark with term-by-term residuals;
9. exact, matrix-free Krylov, and symmetry-adapted coupled-sector TTN solutions;
10. positive-x microscopic antiquark density, helicity, OAM, GTMD, PDF, and current routes from the same eigenstate;
11. a Feshbach comparison between explicit pair sectors and induced sea operators, including a visible remainder;
12. the first validation-only common microscopic quark–antiquark–gluon parent bundle.

C10 is the first package that may demonstrate a common microscopic state with explicit quark, antiquark, and gluon degrees of freedom. It remains a finite-basis Hamiltonian-EFT validation benchmark. It is **not** a physical nucleon, a continuum-QCD solution, a matched PDF/GTMD/TMD, a complete chiral proof, a nuclear input, an evolution input, or an inference model.

## Normative sources

Before implementation, audit and record the exact hashes of all formalism sources available under `references/`. The primary sources for C10 are:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_i_regulated_light_front_foundations.tex
references/volume_ii_common_nucleon_gtmd_overlaps.tex
references/volume_vi_shared_inference_validation.tex
references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_ix_dynamical_gluon_fock_sectors.tex
references/model_construction_note.tex
```

If the revised algebraic/geometric note, Volume VIII, or Volume IX is absent, add the supplied source in a documentation-only commit before C10 code changes. Do not invent missing text. Record availability and hashes in:

```text
docs/next_level/c10_normative_source_integration.json
docs/next_level/c10_normative_integration_report.md
```

The supplied source hashes expected for the three previously missing documents are:

```text
29a75dac37fe695ab05e139c9872e3a4491fcf70b019dec386129a596eb10489  algebraic_geometric_next_level_model_note_revised.tex
8d9d53ba6ed007909abbb41e2ad93217ee42368fde43df24569b568990879c00  volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
3b90df86e9e426c15aea93a25e64223e9243108b4a9051eebf74f233ad72cc1c  volume_ix_dynamical_gluon_fock_sectors.tex
```

If the repository contains a different file at one of these names, stop that source from being treated as normative, report the mismatch, and continue only with the verified available sources and the equations stated in this work package.

## Completeness and autonomy

Completeness is the objective. Do not optimize for speed or minimize the physics.

Read the C7, C8, and C9 implementation reports, APIs, manifests, ADRs, tests, and handoff notes. Reuse their actual classes and interfaces. Do not create a parallel microscopic type system when an existing type can be extended safely.

Continue autonomously until every required deliverable and acceptance gate is complete. Do not stop to request routine permission for local inspection, tests, non-destructive tooling, dependency installation, or document generation when the environment permits those actions. If one optional tool is blocked, use another route and document the limitation.

## Immutable baseline gates

Before editing code, reproduce and record:

```text
865/865 existing tests
9/9 acceptance builders
36/36 evidence rows
162/162 atlas pages

C3 injections: 24/24
C4 injections: 40/40
C5 injections: 48/48
C6 injections: 60/60
C7 injections: 48/48
C8 injections: 56/56
C9 injections: 83/83

157 C9 requirements covered
216 accepted production reductions
```

Verify that all eight authoritative artifacts remain byte-identical to C9 and that the production registry, production provenance graph, default composition plan, C7/C8 oracles, and pinned C5/C6 manifests are unchanged.

Do not modify any accepted numerical parent, accepted TMD value, sign, convention, ordering, evidence class, uncertainty member, atlas page, or production metadata.

## Required package location

Create or extend an isolated microscopic H3 package, preferably:

```text
src/deuteron_wigner/microscopic/h3/
```

The package may import H0/H1/H2 types and read-only results. It must have no path to the accepted production root.

## Required scientific implementation

### C10.1 — H3 Fock-space identity

Define a versioned H3 sector set:

```text
QQQ
QQQG
QQQUUBAR
QQQDDBAR
```

or equivalent unambiguous names.

Every sector identity must contain:

- exact parton content and ordered creation-operator convention;
- proton/neutron target identity;
- total charge, baryon number, isospin, and `Jz`;
- longitudinal resolution and positive support;
- transverse basis, radial/OAM labels, and center-of-mass policy;
- quark helicities, antiquark helicity, and gluon helicity where applicable;
- SU(3) representation, color outer multiplicity, and recoupling convention;
- permutation representation and antisymmetrizer identity;
- regulator, endpoint, zero-mode, and boundary-condition identities;
- microscopic member and assumption-plan identity.

The two light-pair sectors must remain separate. A generic unlabeled `qqqq-qbar` sector is insufficient for the H3 state and cannot be used for flavor-resolved predictions.

### C10.2 — Complete five-parton color-singlet basis

Retain all three independent color singlets in

\[
3\otimes3\otimes3\otimes3\otimes\bar3.
\]

For every independent kinematic/spin configuration, construct a complete orthonormal singlet basis and retain the outer-multiplicity label through:

- the basis state;
- Hamiltonian blocks;
- pair vertices;
- axial and pseudoscalar operators;
- the TTN virtual spaces;
- GTMD/antiquark exports;
- Feshbach elimination and provenance.

Required tests include:

1. common-nullspace dimension exactly three;
2. total SU(3) generator annihilation;
3. orthonormality and deterministic phase convention;
4. correct anti-fundamental action `-T^{aT}` on the antiquark;
5. unitary recoupling between at least two supported color fusion trees;
6. deliberate omission of each singlet channel produces an incomplete-basis failure;
7. a cluster-only baryon–meson color tensor is identified as one basis vector or subspace, never the complete five-parton color space.

### C10.3 — Exact fermionic antisymmetry

The `qqqq-qbar` sector must use exact creation-operator antisymmetry. The four quarks are fermions with flavor as an internal label; the implementation must preserve the anticommutation sign under exchanges of any quark creation operators, including exchanges across a visually chosen cluster partition.

Use an occupation-number basis, exact signed permutation representation, Young-projector construction, or another mathematically exact method. Post-diagonalization symmetrization is forbidden.

Required tests:

- Hermiticity and idempotence of any explicit antisymmetrizer;
- correct sign under all generating transpositions;
- deterministic canonical ordering;
- preservation of total flavor, color, spin, OAM, and momentum labels;
- Pauli-forbidden states absent before Hamiltonian assembly;
- independent oracle on small four-quark mode sets;
- injected wrong exchange sign and cluster-only antisymmetry fail.

### C10.4 — Coupled H3 Hamiltonian

Construct the block operator

\[
\mathcal M_{\mathrm{H3},r}^{2}
=
\begin{pmatrix}
M_{33,r}^{2} & V_{3\leftarrow4g,r} & V_{3\leftarrow5u,r} & V_{3\leftarrow5d,r}\\
V_{4g\leftarrow3,r} & M_{4g4g,r}^{2} & V_{4g\leftarrow5u,r} & V_{4g\leftarrow5d,r}\\
V_{5u\leftarrow3,r} & V_{5u\leftarrow4g,r} & M_{5u5u,r}^{2} & V_{5u\leftarrow5d,r}\\
V_{5d\leftarrow3,r} & V_{5d\leftarrow4g,r} & V_{5d\leftarrow5u,r} & M_{5d5d,r}^{2}
\end{pmatrix},
\]

with unsupported blocks absent or explicitly zero by a named symmetry/approximation rule, never merely left undefined.

The H2 `qqq <-> qqqg` block remains one authoritative implementation. Reuse it; do not duplicate it.

#### Canonical pair creation and annihilation

Implement a reduced but typed canonical

\[
g\leftrightarrow q\bar q
\]

vertex connecting `QQQG` with `QQQUUBAR` and `QQQDDBAR`. The pair vertex must retain:

- Hamiltonian-owned coupling identity;
- emitted/absorbed flavor;
- adjoint gluon color and fundamental/anti-fundamental pair color;
- all three final singlet multiplicities;
- gluon, quark, and antiquark helicities;
- longitudinal momentum conservation and endpoint policy;
- transverse overlap and OAM selection;
- fermion ordering signs;
- regulator and normalization identity;
- generated Hermitian-conjugate block.

A pair created by copying a scalar sea probability into the state is forbidden.

#### Chiral sector-changing interaction

Implement a controlled effective chiral interaction capable of coupling `QQQ` to the explicit `QQQQ-qbar` sectors through an isovector pseudoscalar/derivative channel. It may be a finite-basis effective kernel, but it must carry:

- operator and provenance identity;
- flavor/isospin Clebsch structure;
- parity and `Jz` selection;
- chiral scale, coupling, and regulator;
- a declared relation to the axial/pseudoscalar current;
- power-counting or naturalness metadata;
- resolution-dependent coefficient flow;
- an explicit statement that it is not a universal QCD potential.

The explicit pair sector plus its sector-changing chiral vertex is one route. An induced sea/pion-cloud correction with no explicit pair sector is another route. They are mutually exclusive unless an explicit overlap subtraction is supplied.

### C10.5 — Assumption plans

Compile at least these immutable branches:

```text
H3-PLAN-A
    explicit uubar and ddbar sectors
    canonical g <-> q qbar vertex
    explicit chiral sector-changing interaction
    resolution-refitted induced confinement
    H2 instantaneous partners retained
    no independent induced sea/pion-cloud correction

H3-PLAN-B
    explicit uubar and ddbar sectors
    canonical g <-> q qbar vertex
    chiral sector-changing interaction disabled
    resolution-refitted induced confinement
    H2 instantaneous partners retained

H2-REFERENCE
    read-only C9/H2 state
    no explicit pair sectors
    no H3 pair prediction

H3-INDUCED-SEA-REFERENCE
    validation-only reduced-space comparison
    explicit pair sectors eliminated or absent
    induced sea/chiral operator plus declared remainder
    never additive with H3-PLAN-A or H3-PLAN-B
```

These plans are alternative complete theories at the declared truncation. They may be compared but never summed.

Every plan must have a content-addressed `AssumptionBundle`, compilation certificate, Hamiltonian identity, operator bundle, renormalization trajectory, state bundle, and provenance root.

### C10.6 — Sector-dependent renormalization

Define a trajectory

\[
\mathfrak R_r^{\mathrm{H3}}
=
\left(
\mathcal R_r,
\theta_{3,r},
\theta_{4g,r},
\theta_{5u,r},
\theta_{5d,r},
\delta g_{34,r},
\delta g_{45u,r},
\delta g_{45d,r},
\delta g_{\chi,r},
\{\mathcal C_i\},
\mathcal S_r,
\mathcal Z_r,
\Delta_r
\right).
\]

Use at least three nested benchmark resolutions, extending the actual C9 tower. The basis dimensions must increase nontrivially in every retained sector.

Preserve the C9 benchmark conditions at each resolution:

\[
M_N^2=0.7744\ \mathrm{GeV}^2,
\qquad
F_1^p(0)=1,
\qquad
F_1^n(0)=0,
\]

and add only a restricted H3 calibration set, for example:

- one pair-vertex matrix element or level splitting;
- one finite-basis PCAC condition at one kinematic point;
- one chiral-coupling/naturalness condition.

Freeze as holdouts before optimization:

- a second pair-vertex kinematic point;
- proton and neutron `g_A` or one axial-current combination not used in calibration;
- PCAC at a second momentum transfer;
- a Goldberger–Treiman-like residual or pion-pole diagnostic;
- `dbar-ubar` or another light-sea flavor observable;
- one sea momentum/helicity/OAM observable;
- a nonzero-transfer vector or axial current;
- a rotational diagnostic.

Do not add parameters merely to make these holdouts exact. Expose null directions, Jacobian rank, Hessian spectrum, naturalness combinations, and parameter correlations.

Sector-dependent bare masses are truncation-dependent renormalization data, not different physical quark masses. The physical light-quark mass and isospin conventions must remain explicit.

### C10.7 — Axial, pseudoscalar, and PCAC-consistent operators

Construct Hamiltonian-consistent operators:

\[
A_r^{\mu,a}
=
A_{(1),r}^{\mu,a}
+A_{\mathrm{pair},r}^{\mu,a}
+A_{\chi,r}^{\mu,a}
+\delta A_{\mathrm{ct},r}^{\mu,a},
\]

\[
P_r^a
=
P_{(1),r}^a
+P_{\mathrm{pair},r}^a
+P_{\chi,r}^a
+\delta P_{\mathrm{ct},r}^a.
\]

Implement a finite-basis axial Ward/PCAC benchmark of the declared form

\[
q_\mu A_r^{\mu,a}
=
2m_{q,r} P_r^a
+f_\pi m_\pi^2\Phi_r^a
+\delta_{\mathrm{PCAC},r},
\]

or an equivalent quark-level axial Ward–Takahashi identity, provided the exact convention is documented and all terms share one Hamiltonian, regulator, state normalization, and chiral interaction identity.

If no explicit pion Fock sector exists, `Phi_r^a` must be a typed induced pion-pole/interpolating operator. It may not be described as an explicit physical pion state.

The PCAC residual must be decomposed into at least:

```text
ONE_BODY_AXIAL
PAIR_AXIAL
CHIRAL_EXCHANGE
PSEUDOSCALAR_DENSITY
PION_POLE_OR_INDUCED_TERM
CURRENT_COUNTERTERM
REGULATOR
BASIS_TRUNCATION
```

Removing any required term must produce a signed nonzero residual. Passing this benchmark may issue:

```text
FINITE_BASIS_PCAC_BENCHMARKED
```

but must never issue:

```text
FULL_CHIRAL_SYMMETRY_PROVED
CONTINUUM_PCAC_PROVED
```

The vector-current and C9 Abelianized Ward benchmarks must continue to pass.

### C10.8 — Exact, Krylov, and tensor-network solvers

Solve every small H3 block by:

1. exact Hermitian diagonalization;
2. matrix-free Krylov application and eigensolution;
3. exact full-bond symmetry-adapted tensorization;
4. genuine variational coupled-sector TTN optimization.

The state network must contain explicit branches for:

```text
QQQ
QQQG
QQQUUBAR
QQQDDBAR
```

and must retain:

- all color outer multiplicities `1/2/3`;
- antiquark anti-fundamental identity;
- pair flavor;
- quark permutation representation;
- gluon and antiquark helicity;
- OAM and `Jz`;
- Fock-sector identity;
- regulator and resolution identity.

Full bond must reproduce the exact state to the declared tolerance. Nested variational spaces must obey the Rayleigh–Ritz bound.

Bond convergence must include, not merely energy:

\[
P_{qqqg},\quad
P_{u\bar u},\quad
P_{d\bar d},\quad
\langle x_g\rangle,\quad
\langle x_{\bar u}\rangle,\quad
\langle x_{\bar d}\rangle,\quad
\Delta\bar u,\quad
\Delta\bar d,\quad
L_{\bar q},\quad
g_A,\quad
\delta_{\mathrm{PCAC}}.
\]

At least one low-bond state must visibly lose a real sea-flavor, antiquark/OAM, axial, or PCAC feature while giving a deceptively reasonable energy.

### C10.9 — Microscopic state ledgers

For every state member, close and export:

#### State probability

\[
P_{qqq}+P_{qqqg}+P_{u\bar u}+P_{d\bar d}=1.
\]

#### Valence flavor

\[
\int_0^1 dx\,[u(x)-\bar u(x)]=2,
\qquad
\int_0^1 dx\,[d(x)-\bar d(x)]=1
\]

for the proton, with the exact isospin-partner relations for the neutron.

#### Charge and baryon number

\[
\frac23(N_u-N_{\bar u})
-
\frac13(N_d-N_{\bar d})=1,
\]

\[
\frac13\sum_q (N_q-N_{\bar q})=1.
\]

#### Longitudinal momentum

\[
\langle x_q\rangle
+
\langle x_{\bar q}\rangle
+
\langle x_g\rangle
=1.
\]

#### Canonical finite-basis spin/OAM

\[
\frac12
=
\frac12(\Delta\Sigma_q+\Delta\Sigma_{\bar q})
+\Delta G
+L_q+L_{\bar q}+L_g
+\delta_{J,r}.
\]

These are regulator- and truncation-dependent microscopic diagnostics. They are not yet matched QCD PDFs or a scheme-independent spin decomposition.

Export separate proton and neutron members with a shared microscopic parameter/member identity. Exact charge symmetry must map the sea sectors consistently. Do not impose `ubar=dbar` as a project-wide identity.

### C10.10 — Positive-x microscopic antiquark overlaps

Use the H3 eigenstate and the existing zero-skewness recoil/overlap authority to construct active-antiquark matrix elements directly from positive-x antiquark slots:

\[
W_{\bar q/N}^{[\Gamma]}(x,\bm k_T,\bm\Delta_T),
\qquad x>0.
\]

Do not generate the central antiquark result by copying negative-x quark data. A typed charge-conjugation adapter may be used as a convention check only if it also transforms endpoint order, Wilson path, color representation, Fourier phase, and helicity conventions.

Construct validation-level quark, antiquark, and gluon parents from the same state and test common regulated routes:

```text
GTMD -> TMD -> PDF
GTMD -> regulated GPD -> PDF at DeltaT=0
GTMD -> regulated GPD -> vector/axial/EMT moment
```

For positive-x quark and antiquark objects, vector moments must use `q - qbar`. Axial moments must use the declared axial convention. Gluon moments must retain the `H^g = x g` convention where used.

All results must carry explicit statuses such as:

```text
REGULATED_MICROSCOPIC_H3
LINK_SHORTENING_REQUIRED
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
NO_EVOLUTION_APPLIED
NO_PROCESS_MAP_APPLIED
```

The package may issue:

```text
MICROSCOPIC_Q_QBAR_G_COMMON_PARENT_VALIDATED
POSITIVE_X_ANTIQUARK_OVERLAP_VALIDATED
```

but not `PHYSICAL_PDF`, `PHYSICAL_GTMD`, `PHYSICAL_TMD`, or `MATCHING_COMPLETE`.

### C10.11 — Explicit-versus-induced sea comparison

Perform a finite Feshbach elimination of the explicit `QQQQ-qbar` sectors:

\[
H_{\mathrm{eff}}(E)
=
PHP
+
PHQ(E-QHQ)^{-1}QHP,
\]

with the corresponding transformed operators

\[
O_{\mathrm{eff}}(E',E)
=
P[1+\omega^\dagger(E')]O[1+\omega(E)]P.
\]

Compare the result with the read-only induced-sea/chiral reference. Record:

- induced Hamiltonian component;
- transformed vector, axial, pseudoscalar, and antiquark operators;
- norm kernel;
- exact finite-model equivalence residual;
- nonzero orthogonal/truncation remainder;
- energy dependence;
- singularity/conditioning diagnostics.

The provenance relation must be:

```text
explicit pair sectors
    EQUIVALENT_TO
induced sea/chiral operator + transformed observables + declared remainder
```

Never:

```text
explicit pair sectors ADD_TO induced sea correction
```

Selecting both routes in one plan must fail before numerical evaluation.

### C10.12 — Chiral and sea-flavor diagnostics

Export at least the following validation-level observables:

- `N_ubar`, `N_dbar`;
- `dbar - ubar` number or moment diagnostic;
- `x_ubar`, `x_dbar`;
- `Delta ubar`, `Delta dbar`;
- `L_ubar`, `L_dbar`;
- proton/neutron isospin-partner checks;
- axial charge or axial-current matrix element;
- pseudoscalar/pion-pole matrix element;
- PCAC residual by term;
- one Goldberger–Treiman-like or pion-pole holdout diagnostic.

Do not fit the light-sea asymmetry separately. It must emerge from the shared H3 interactions and state. If the selected plan is flavor symmetric, report the resulting symmetry honestly rather than inserting an asymmetry by hand.

### C10.13 — Microscopic Wilson handoff

Extend the C9 handoff so that active antiquark slots can be passed to the existing C5/C6 path, pole, cut-ledger, phase-budget, and ordered-link infrastructure with complete microscopic identity.

The handoff must retain:

- H3 state-bundle identity;
- explicit antiquark flavor and helicity;
- all relevant color multiplicities;
- OAM and pair-sector ancestry;
- Hamiltonian coupling identity;
- regulator and zero-mode policy;
- cut-support status;
- charge-conjugation/link-reversal convention.

A discrete off-shell spectrum must continue to give exactly zero absorption unless a separately declared continuum or finite-volume spectral rule provides physical support. Numerical epsilon is not physical.

The highest permitted status is:

```text
MICROSCOPIC_ANTIQUARK_WILSON_INPUT_INTERFACE_VALIDATED
```

not `WILSON_READY`.

### C10.14 — Provenance two-complex

Extend the assumption/provenance system with 0-, 1-, and 2-cells for:

- explicit `uubar` and `ddbar` sectors;
- canonical gluon-splitting pair vertices;
- chiral pair vertices;
- induced sea operators;
- Feshbach equivalence plus remainder;
- axial/PCAC completion;
- current and operator transformations;
- positive-x antiquark projections;
- Wilson handoff;
- all downstream matching gates.

The compiler must reject:

- explicit pair sectors plus their induced replacement;
- explicit chiral sector plus an independent pion-cloud sea correction without overlap subtraction;
- H1 effective color-spin plus explicit H2 gluon dynamics when the H2 exclusion applies;
- `uubar` and `ddbar` identities merged before flavor projection;
- an antiquark copied from a quark function;
- a physical-TMD/evolution/nuclear/process/inference consumer.

Nontrivial unresolved cycles must be reported as audit failures or explicit alternatives, not assigned numerical amplitude values.

## Required benchmark families

Implement at least these benchmark families with stable IDs:

### H3-A — Five-parton color completeness

- exact singlet multiplicity three;
- generator annihilation;
- orthonormality;
- recoupling unitarity;
- wrong antiquark generator and missing-channel failures.

### H3-B — Four-quark antisymmetry

- exact signed exchanges;
- antisymmetrizer Hermiticity/idempotence;
- occupation-basis oracle;
- Pauli-forbidden-state rejection.

### H3-C — Pair-vertex Hermiticity

- `qqqg <-> qqqq-qbar` canonical vertex and adjoint;
- both flavors;
- all color multiplicities;
- deterministic random complex superpositions.

### H3-D — Chiral sector-changing benchmark

- isospin/parity/Jz selection;
- resolution flow;
- zero-coupling limit;
- explicit versus induced route distinction.

### H3-E — Sector-dependent renormalization

- at least three resolutions;
- mass/charge conditions;
- pair/chiral parameter flow;
- Jacobian and Hessian diagnostics;
- frozen holdouts.

### H3-F — Vector Ward preservation

- C9 Abelianized Ward benchmark remains closed;
- pair-sector attachments and counterterms included where required;
- term-removal signed residuals.

### H3-G — Axial/PCAC closure

- term-by-term PCAC residual;
- pair and chiral currents;
- pseudoscalar and pion-pole/induced term;
- second-point holdout.

### H3-H — Exact/Krylov/TTN agreement

- exact eigenstate;
- matrix-free residual;
- full-bond reconstruction;
- variational nested bond convergence.

### H3-I — Observable-sensitive compression

- low bond misses sea flavor, antiquark OAM/helicity, axial, or PCAC information;
- energy alone appears deceptively good.

### H3-J — Flavor, charge, momentum, and spin ledgers

- valence counts `2,1`;
- charge and baryon number;
- q/qbar/g momentum closure;
- canonical Jz closure;
- proton/neutron partner relations.

### H3-K — Positive-x antiquark common-parent closure

- direct active-antiquark overlap;
- TMD/GPD/PDF/current routes;
- no negative-x copy;
- quark/antiquark/gluon same-member identity.

### H3-L — Explicit/induced sea Feshbach comparison

- Hamiltonian and operator equivalence;
- norm kernel;
- nonzero remainder;
- double-counting rejection.

### H3-M — Chiral flavor asymmetry and holdouts

- plan-dependent `dbar-ubar` prediction;
- no independent normalization;
- axial or pion-pole holdout;
- failed holdout remains a model diagnostic.

### H3-N — Antiquark Wilson handoff

- full microscopic identity;
- charge-conjugation/link conventions;
- zero absorption without physical support;
- no production promotion.

### H3-O — Assumption-plan compiler

- PLAN-A, PLAN-B, H2 reference, and induced-sea reference compile deterministically;
- incompatible branches fail;
- plans are compared, never added.

## Mandatory negative injections

Add at least **88 new C10/H3 stable negative-test identities**. They must include, at minimum, the following failure classes:

1. missing one of the three five-parton singlets;
2. non-orthogonal color multiplicities;
3. wrong antiquark generator sign;
4. cluster tensor promoted to complete color basis;
5. lost color outer-multiplicity label;
6. wrong fermion exchange sign;
7. post-assembly antisymmetrization;
8. Pauli-forbidden basis state accepted;
9. `uubar` and `ddbar` sector identity merged;
10. negative or zero longitudinal support;
11. momentum closure violation;
12. wrong total charge;
13. wrong baryon number;
14. wrong `Jz`;
15. center-of-mass contamination without gate;
16. canonical pair vertex missing adjoint;
17. pair vertex wrong flavor;
18. pair vertex wrong color channel;
19. pair vertex wrong momentum conservation;
20. pair vertex wrong fermion sign;
21. chiral vertex wrong parity;
22. chiral vertex wrong isospin;
23. chiral coupling treated as universal QCD potential;
24. explicit pair plus induced sea selected together;
25. explicit chiral pair plus independent pion-cloud correction selected together;
26. H1 effective color-spin added to explicit H2 dynamics;
27. unsupported Hamiltonian block silently present;
28. sector counterterm assigned to wrong sector;
29. bare sector mass called a physical mass;
30. resolution parameter reused as TMD scale;
31. calibration/holdout leakage;
32. extra parameter added to fit `dbar-ubar`;
33. unresolved Jacobian null direction hidden;
34. vector current from wrong Hamiltonian;
35. pair current omitted;
36. chiral exchange current omitted;
37. pseudoscalar density omitted;
38. pion-pole/induced term omitted;
39. current counterterm omitted;
40. PCAC convention mismatch;
41. one-point PCAC fit advertised as continuum proof;
42. C9 Ward benchmark broken;
43. exact/Krylov mismatch;
44. matrix-free action mismatch;
45. full-bond TTN mismatch;
46. variational energy below exact oracle;
47. larger nested bond space gives higher optimized energy;
48. required sea color sector truncated by bond policy;
49. low-rank sea loss not reported;
50. state-tracking branch swap;
51. probability ledger failure;
52. valence `u-ubar` count failure;
53. valence `d-dbar` count failure;
54. charge ledger failure;
55. baryon ledger failure;
56. momentum ledger failure;
57. canonical Jz ledger failure;
58. proton/neutron microscopic-member mismatch;
59. `ubar=dbar` imposed globally;
60. antiquark generated by copying negative-x quark;
61. active slot wrong species;
62. duplicate antiquark active multiplicity;
63. off-diagonal Fock overlap without named source;
64. nonzero skewness passed to zero-skewness evaluator;
65. recoil convention duplicated or altered locally;
66. quark number-current convention applied to gluon;
67. quark and antiquark signs wrong in vector moment;
68. matching status falsely complete;
69. physical PDF/GTMD/TMD status asserted;
70. evolution attempted;
71. process map attempted;
72. nuclear composition attempted;
73. inference/calibration attempted;
74. Feshbach operator not transformed;
75. Feshbach norm kernel omitted;
76. nonzero Feshbach remainder hidden;
77. explicit and induced sea added;
78. singular Feshbach resolvent not detected;
79. provenance two-cell missing;
80. unresolved provenance cycle ignored;
81. antiquark Wilson handoff loses flavor;
82. antiquark Wilson handoff loses color multiplicity;
83. numerical epsilon treated as physical cut;
84. absorption without declared support;
85. C5/C6 path or phase types duplicated;
86. production registry mutation;
87. authoritative artifact mutation;
88. normative source mutation;
89. C9 state or manifest mutation;
90. accepted production provenance/composition mutation.

More injections are encouraged where needed to cover the actual implementation.

## Required software/API objects

Use actual repository naming conventions, but provide equivalent typed responsibilities for:

```text
H3SectorSpace
FivePartonColorBasis
FourQuarkAntisymmetry
PairCreationVertex
PairAnnihilationVertex
ChiralPairVertex
H3Hamiltonian
H3RenormalizationTrajectory
AxialCurrentOperator
PseudoscalarOperator
PionPoleOrInducedOperator
PCACClosureReport
H3MicroscopicStateBundle
SeaFlavorLedger
AntiquarkOverlapEvaluator
MicroscopicCommonParentBundle
ExplicitInducedSeaComparison
AntiquarkWilsonHandoff
H3TensorNetworkManifest
```

Do not create nominal wrappers without executable invariants and tests.

## Readiness statuses

C10 may issue only narrowly qualified statuses such as:

```text
H3_LIGHT_SEA_BASIS_VALIDATED
H3_PAIR_VERTEX_BENCHMARKED
H3_CHIRAL_INTERACTION_BENCHMARKED
H3_SECTOR_RENORMALIZATION_BENCHMARKED
FINITE_BASIS_PCAC_BENCHMARKED
H3_TTN_REPRESENTATION_VALIDATED
H3_TTN_VARIATIONAL_BENCHMARKED
POSITIVE_X_ANTIQUARK_OVERLAP_VALIDATED
MICROSCOPIC_Q_QBAR_G_COMMON_PARENT_VALIDATED
MICROSCOPIC_ANTIQUARK_WILSON_INPUT_INTERFACE_VALIDATED
H3_EXPLICIT_INDUCED_SEA_COMPARISON_VALIDATED
```

It must not issue:

```text
PHYSICAL_NUCLEON_EIGENSTATE
CONTINUUM_QCD_RENORMALIZED
FULL_CHIRAL_SYMMETRY_PROVED
FULL_SLAVNOV_TAYLOR_CLOSURE
PHYSICAL_PDF
PHYSICAL_GTMD
PHYSICAL_TMD
WILSON_READY
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_PREDICTION_READY
INFERENCE_READY
```

## Production isolation

C10 must remain unreachable from:

- the accepted 216-route registry;
- the production resolved-parent builder;
- production provenance and default composition;
- nuclear composition;
- LF-to-QCD matching or TMD evolution;
- a physical process map;
- inference or calibration of accepted outputs.

Importing the H3 package must have no production side effects.

## Required documentation and machine-readable deliverables

Create:

```text
docs/next_level/c10_implementation_report.md
docs/next_level/c10_api.md
docs/next_level/c10_normative_integration_report.md
docs/next_level/c10_normative_source_integration.json
docs/next_level/c10_requirement_coverage.json
docs/next_level/c10_injection_manifest.json
docs/next_level/c10_regression_report.json
docs/next_level/c10_tolerance_manifest.json
docs/next_level/c10_renormalization_trajectory.json
docs/next_level/c10_pcac_closure_report.json
docs/next_level/c10_tensor_network_manifest.json
docs/next_level/c10_sea_flavor_oam_ledger.json
docs/next_level/c10_common_parent_manifest.json
docs/next_level/c10_explicit_induced_sea_comparison.json
docs/next_level/c10_antiquark_wilson_handoff.json
docs/next_level/c10_unresolved_physics_gaps.md
```

Add ADRs for at least:

```text
five-parton color multiplicity
four-quark antisymmetry
explicit versus induced sea
chiral interaction ownership
finite-basis PCAC convention
positive-x antiquark representation
H3 assumption branches
```

Update `handoff/ROADMAP.md` with the exact final commit, validated scope, unresolved physics, and one unambiguous next package.

All JSON outputs must be deterministic, machine readable, and stable under repeated generation.

## Final acceptance criteria

C10/H3 is complete only when all of the following hold:

1. the C9 baseline reproduces before changes;
2. the H3 basis contains `qqq`, `qqqg`, explicit `uubar`, and explicit `ddbar` sectors;
3. all three five-parton color singlets are retained and validated;
4. exact four-quark antisymmetry passes before matrix assembly;
5. canonical pair vertices and adjoints are Hermitian and typed;
6. the chiral interaction has explicit ownership, selection rules, and provenance;
7. explicit and induced sea routes are mutually exclusive;
8. a multi-resolution sector-dependent renormalization trajectory is generated;
9. mass and vector-charge conditions close without fitting every holdout;
10. the C9 vector/Ward benchmark remains passing;
11. the finite-basis PCAC benchmark closes with a decomposed residual;
12. omission of each required PCAC term yields a signed failure;
13. exact, Krylov, and full-bond TTN states agree;
14. variational TTN convergence is demonstrated in sea/axial observables, not only energy;
15. state tracking is stable across the tower;
16. probability, valence flavor, charge, baryon, momentum, and canonical-Jz ledgers close;
17. proton and neutron remain correlated microscopic members;
18. positive-x `ubar` and `dbar` overlaps are evaluated directly from active antiquark slots;
19. quark, antiquark, and gluon regulated parents share one state/member identity;
20. TMD/GPD/PDF/current closure is demonstrated at the regulated level;
21. the explicit/induced Feshbach comparison includes transformed operators and a visible remainder;
22. the antiquark Wilson handoff preserves complete identity and returns zero absorption without physical support;
23. all H3 assumption plans compile deterministically and incompatible branches fail;
24. at least 88 new ordered C10 injections pass;
25. all previous C3–C9 injections remain passing;
26. the complete test suite, builders, evidence matrix, and atlas pass;
27. all eight authoritative artifacts remain byte-identical;
28. the 216-route production registry, production provenance, and composition remain unchanged;
29. C7/C8 oracles and pinned C5/C6/C9 manifests remain unchanged;
30. no H3 result is promoted to production, nuclear, evolution, process, or inference use;
31. all required documentation and JSON manifests are present and deterministic;
32. the working tree is clean and one local unpushed completion commit exists.

These criteria establish a validation-only microscopic state with explicit quark, antiquark, and gluon sectors. They do not establish continuum QCD or physical TMD predictions.

## Expected next package

If C10/H3 passes, the recommended next package is:

> **C11/H4 — microscopic nonzero-transfer quark, antiquark, and gluon GTMD helicity matrices from the common H3 eigenstate; complete T-even projector closure; local-current/OAM consistency; and microscopic replacement of the C3/C4 analytic common-parent pilots.**

The parallel formal volume should be:

> **Volume X: Light-Sea Fock Sectors, Chiral Symmetry, PCAC, and Microscopic Antiquark GTMDs.**

## Final response from Codex

Report:

- starting and final commits;
- whether anything was pushed;
- final test, builder, evidence, atlas, requirement, and injection counts;
- sector and basis dimensions at every resolution;
- color, antisymmetry, Hermiticity, Krylov, TTN, Ward, and PCAC residuals;
- renormalization parameter flow;
- state probability, sea flavor, momentum, helicity, and OAM ledgers;
- common-parent reduction residuals;
- explicit/induced sea remainder norms;
- holdout results, including any failures;
- readiness statuses issued;
- immutable-artifact verification;
- files created;
- exact unresolved limitations;
- exact recommended C11 package.

Do not declare C10 complete unless every acceptance criterion above is satisfied.
