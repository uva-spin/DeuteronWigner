# C9/H2 Codex Work Package

## Dynamical \(qqq\oplus qqqg\) microscopic state, sector-dependent renormalization, gauge-consistent currents, coupled-sector TTN, and microscopic Wilson reconnection

You are beginning **C9/H2** for the `uva-spin/DeuteronWigner` repository.

---

# 0. Authoritative baseline

Start from the local C8/H1 completion commit:

```text
6a95383694ed93bde8866127b7368d465e546b62
```

Its required C7 ancestor is:

```text
f3256cdacf746e8c9e0d3beaad68bc5d6b25f804
```

The local branch is ahead of `origin/main`. **Do not reset to, merge from, rebase onto, or otherwise use `origin/main` as the scientific baseline.**

A documentation-only descendant is acceptable only if:

1. `6a95383694ed93bde8866127b7368d465e546b62` remains an ancestor;
2. the exact C8 baseline reproduces before implementation;
3. intervening changes are limited to formalism sources, indices, prompts, or other documentation;
4. every intervening file and hash is recorded in the C9 baseline manifest.

Do not push. Create local commits only. The final working tree must be clean.

---

# 1. Normative sources

Use the repository copies of these sources when available:

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
references/model_construction_note.tex
```

Volume VII is the primary H2 dynamical specification. Volume VIII is the primary tensor-network, assumption-compiler, and provenance specification. Volumes I–III define the state, overlap, and Wilson interfaces. Volumes IV–VI define downstream gates that C9 must not cross.

If a source is absent, do not invent its content. Record the absence and use the equations and requirements in this prompt together with the preserved C0–C8 APIs, reports, ADRs, manifests, and roadmap.

Generate a deterministic normative-source manifest containing exact source hashes.

---

# 2. Baseline that must reproduce before edits

Before changing code, reproduce and record:

```text
852/852 tests
9/9 acceptance/report builders
36/36 evidence rows
162/162 atlas pages

C3 injections: 24/24
C4 injections: 40/40
C5 injections: 48/48
C6 injections: 60/60
C7 injections: 48/48
C8 injections: 56/56

C8 requirements: 104 covered
Production reduction registry: exactly 216 routes
```

Verify that:

- all eight authoritative artifacts remain byte-identical;
- production provenance and the default composition plan are unchanged;
- the C7 oracle remains byte-identical;
- the pinned C5/C6 manifests remain byte-identical;
- the C8 plan, trajectory, current, tensor-network, and regression manifests reproduce.

If the baseline does not reproduce, diagnose it. Do not repair it by changing accepted physics.

---

# 3. Scientific objective and boundary

C8 solved the first interacting valence-sector eigenproblem. C9 must enlarge that **same microscopic state and tensor architecture** to

\[
\mathcal H_{\mathrm{H2}}
=
\mathcal H_{qqq}
\oplus
\mathcal H_{qqqg},
\]

with

\[
|N,\Lambda\rangle_r
=
|\Psi_{qqq}^{\Lambda}\rangle_r
+
|\Psi_{qqqg}^{\Lambda}\rangle_r,
\]

and one normalization,

\[
1
=
P_{qqq}^{(r)}
+
P_{qqqg}^{(r)}.
\]

Implement:

1. complete \(qqqg\) color-singlet multiplicity and fermionic structure;
2. canonical reduced \(qqq\leftrightarrow qqqg\) interactions and Hermitian partners;
3. instantaneous partners with declared inverse-derivative and zero-mode policies;
4. Fock-sector-dependent mass and vertex renormalization;
5. a Hamiltonian-consistent vector current;
6. a controlled Abelianized Ward–Takahashi benchmark;
7. exact, matrix-free Krylov, and variational TTN solutions of the coupled space;
8. gluon momentum, helicity, OAM, and total-\(J^z\) ledgers;
9. a finite Feshbach comparison with the H1 effective color-spin branch;
10. a validation-only microscopic interface to the existing C5/C6 Wilson engine;
11. assumption-compiled H2 branches using the C8/Volume VIII compiler and TTN infrastructure.

This remains a finite, validation-only Hamiltonian-EFT benchmark. It is **not**:

- a physical nucleon determination;
- a continuum-QCD renormalization;
- full non-Abelian Ward or Slavnov–Taylor closure;
- a GTMD, PDF, or TMD extraction;
- a soft-subtracted QCD correlator;
- a nuclear state;
- an evolution input;
- an inference model;
- a process prediction.

---

# 4. Autonomy and completion discipline

Completeness is the goal. Do not optimize for speed.

Continue autonomously through repository inspection, implementation, testing, documentation, manifest generation, and local commits. Do not stop for approval for routine local actions permitted by the environment.

If one optional tool is unavailable, use another route and document the limitation. Do not abandon the package because one optional method fails.

Do not claim completion from test count alone. Every scientific acceptance gate must have machine-readable evidence.

---

# 5. Immutable physics and architecture rules

Do not:

- change any accepted production TMD, correlator, sign, convention, normalization, or ordering;
- alter the 216-route production registry;
- alter production provenance or the default composition plan;
- alter authoritative output bytes;
- add a TMD-specific coefficient;
- connect C9 outputs to production, nuclear, evolution, process, or inference roots;
- populate the sea sector;
- claim GTMD readiness;
- use the C5/C6 Wilson kernel as a Hamiltonian interaction;
- use finite numerical \(\epsilon\) as physical cut support;
- duplicate C1–C8 coordinate, path, operator, cut, color, map, or tensor types;
- silently identify oscillator scale \(b\), Hamiltonian resolution \(\lambda\), rapidity scale, Collins–Soper scale, or hard scale;
- keep the H1 effective color-spin interaction active in a plan with explicit \(qqqg\) dynamics unless an explicit overlap subtraction has first been implemented and validated;
- infer a physical gluon PDF from a finite-basis gluon occupation;
- claim full QCD gauge restoration from an Abelianized Ward benchmark.

---

# 6. Package location and reuse

Extend the existing microscopic packages rather than creating a parallel framework. A natural location is:

```text
src/deuteron_wigner/microscopic/h2/
```

Reuse and generalize, where needed:

```text
src/deuteron_wigner/microscopic/h0/
src/deuteron_wigner/microscopic/h1/
src/deuteron_wigner/formal/
src/deuteron_wigner/pilot/
```

C9 must consume the C8 assumption, state-bundle, TTN, solver, current, and comparison-map APIs. If an H1-specific interface must be generalized, provide a lossless migration adapter and prove that all H1 identities and numerical results remain unchanged.

Do not create:

- a second assumption compiler;
- a second tensor-network state representation;
- a second color basis;
- a second Wilson path or cut ledger;
- a second operator identity system.

---

# 7. H2 assumption compiler and plan identities

Generalize the C8 H1 compiler only as much as required to support H2.

A frozen H2 assumption bundle must include at least:

```text
bundle_schema_version
HamiltonianResolution tower
Fock sectors
basis and zero-mode policy
confinement branch
canonical qg vertex identity
instantaneous-kernel policy
sector-dependent renormalization conditions
current policy
TTN topology and bond policy
solver policy
state-tracking policy
Feshbach comparison policy
Wilson reconnection policy
calibration/holdout roles
normative source hashes
```

Compile at least these mutually exclusive plans:

```text
H2-PLAN-A
    qqq + explicit qqqg
    resolution-refitted induced confinement
    canonical reduced qg vertex
    instantaneous partners
    H1 effective color-spin disabled
    exact/Krylov/TTN solvers

H2-PLAN-B
    qqq + explicit qqqg
    zero confinement
    canonical reduced qg vertex
    instantaneous partners
    H1 effective color-spin disabled
    exact/Krylov/TTN solvers

H1-REFERENCE
    read-only C8 effective color-spin branch
    no explicit qqqg
    comparison only
```

Each plan must have a distinct content-addressed identity, compilation certificate, Hamiltonian hash, renormalization trajectory, state-bundle identity, current identity, TTN manifest, and provenance normal form.

Results may be compared. They may not be added together.

Dependency closure may add required implementation objects, such as adjoint color representations or solver adapters. It may not silently add missing physical dynamics, matching schemes, or process assumptions.

---

# 8. Complete \(qqqg\) basis

Build a nontrivial resolution tower whose \(qqqg\) dimension grows with \(K\), \(N_{\max}\), and the retained orbital content. Do not reuse the C7 \(2\times2\) color benchmark as the final H2 sector.

The \(qqqg\) basis must retain:

- proton and neutron targets;
- \(J^z=\pm\tfrac12\);
- positive longitudinal modes;
- intrinsic transverse modes;
- gluon helicity \(\lambda_g=\pm1\);
- quark helicities;
- orbital labels sufficient for the retained \(J^z\) blocks;
- both independent three-quark color-octet multiplicities;
- coupling of each octet multiplicity with the adjoint gluon to a total singlet;
- full identical-quark antisymmetry before operator assembly;
- permutation multiplicities and signs;
- center-of-mass and Lawson metadata;
- regulator, endpoint, zero-mode, and resolution identity.

Where allowed by the benchmark resolutions, retain \(L_z=0,\pm1,\pm2\). If a low tower point cannot support one of these blocks, record it as unavailable at that resolution rather than predicting zero.

Mandatory basis checks:

1. both \(qqqg\) singlet multiplicities are present;
2. total color generators annihilate every physical state;
3. color basis is orthonormal;
4. recoupling maps preserve outer multiplicity and are unitary;
5. antisymmetrizer is Hermitian and idempotent;
6. longitudinal and transverse constraints close;
7. total \(J^z\) closes;
8. center-of-mass diagnostics close;
9. deterministic serialization and phase conventions hold.

A color-singlet \(qqq\) tensor times a free gluon must fail.

---

# 9. Coupled H2 Hamiltonian

Implement

\[
\mathcal M_{\mathrm{H2},r}^{2}
=
\begin{pmatrix}
\mathcal M_{3,r}^{2}
&
V_{3\leftarrow4g,r}
\\
V_{4g\leftarrow3,r}
&
\mathcal M_{4g,r}^{2}
\end{pmatrix},
\qquad
V_{3\leftarrow4g,r}
=
V_{4g\leftarrow3,r}^{\dagger}.
\]

The diagonal blocks contain:

- free invariant mass;
- the selected induced-confinement or zero-confinement branch;
- sector-appropriate counterterms;
- permitted instantaneous and induced interactions;
- a declared truncation-discrepancy operator.

The off-diagonal block must be a typed reduced canonical quark–gluon vertex derived from one Hamiltonian-owned interaction identity. It must include:

- one shared benchmark coupling;
- fundamental color generator action;
- both \(qqqg\) color multiplicities;
- longitudinal momentum conservation;
- transverse-mode overlap;
- helicity and total-\(J^z\) selection;
- emitting-quark identity;
- fermion permutation sign;
- endpoint and zero-mode policy;
- regulator and basis normalization;
- a generated Hermitian-conjugate absorption block.

Do not use an arbitrary dense random coupling as the physical implementation. A random matrix may be used only as an independent fault injection.

Do not label this finite reduced vertex a complete renormalized QCD quark–gluon vertex.

---

# 10. Instantaneous partners and constrained-field policy

Implement typed instantaneous interactions required by the selected light-front reduction, including the applicable benchmark forms of:

- instantaneous-fermion contributions;
- instantaneous-gluon or \(J^+(1/\partial^{+2})J^+\) contributions;
- interaction-current partners required by the Ward benchmark.

Every term must carry:

```text
source and target sectors
inverse-derivative prescription
endpoint regulator
zero-mode policy
color and spin structure
Hamiltonian identity
Hermitian partner
renormalization ownership
```

Changing the inverse-derivative, endpoint, or zero-mode prescription changes the Hamiltonian identity.

Do not insert an unexplained numerical contact term merely to reduce the Ward residual.

---

# 11. Fock-sector-dependent renormalization

Implement a versioned H2 renormalization datum

\[
\mathfrak R_r^{\mathrm{H2}}
=
\left(
\mathcal R_r,
\theta_{3,r}^{\mathrm{bare}},
\theta_{4,r}^{\mathrm{bare}},
\delta\theta_{3,r},
\delta\theta_{4,r},
\delta g_{34,r},
\{\mathcal C_i\},
\mathcal S_r,
\mathcal Z_r,
\Delta_r
\right).
\]

Sector-dependent bare parameters and counterterms are permitted only as elements of this declared trajectory. They may not be interpreted as different physical quark masses.

At every tower point, refit the same declared conditions:

1. benchmark nucleon pole condition
   \[
   M_N^2=0.7744~\mathrm{GeV}^2;
   \]
2. proton charge
   \[
   F_1^p(0)=1;
   \]
3. correlated neutron closure
   \[
   F_1^n(0)=0;
   \]
4. one renormalized \(qqq\leftrightarrow qqqg\) vertex condition at a fixed reference kinematic/symmetry point;
5. the Abelianized Ward condition below;
6. center-of-mass/Lawson closure.

If these conditions do not identify all parameter directions, expose the null directions through Jacobian, Hessian, profile, or singular-value diagnostics. Do not add hidden fitted observables solely to make the Hessian full rank.

Withhold at least:

- a second vertex kinematic point;
- a nonzero-transfer proton current;
- the correlated neutron nonzero-transfer current;
- a second current-component extraction;
- one \(qqqg\) probability or gluon-momentum observable;
- one rotational or multiplet diagnostic.

Export at every resolution:

```text
bare and counterterm parameters
renormalized coupling condition
sector probabilities
mass and charge residuals
Ward residuals
current-component defects
parameter Jacobian/Hessian spectrum
naturalness combinations
comparison-map identities
basis/Fock/discrepancy estimates
```

Do not claim continuum convergence from the small validation tower.

---

# 12. Hamiltonian-consistent current and Abelianized Ward benchmark

Construct

\[
J_r^\mu
=
J_{(1),r}^{\mu}
+
J_{qqqg,r}^{\mu}
+
J_{\mathrm{inst},r}^{\mu}
+
J_{\mathrm{ind},r}^{\mu}
+
\delta J_r^\mu
\]

with every term owned by the same Hamiltonian and regulator identity.

Do not import the C8 current unchanged if the H2 Hamiltonian requires sector or interaction-current terms. Do not fit separate normalizations by current component, momentum transfer, proton/neutron target, or Fock sector.

Implement a controlled Abelianized or commuting-generator Ward–Takahashi benchmark:

\[
q_\mu\Gamma_r^\mu(p+q,p)
=
S_r^{-1}(p+q)-S_r^{-1}(p)
+
\delta_{\mathrm{trunc},r},
\]

or the precisely corresponding finite-basis Hamiltonian identity.

The benchmark must:

- use the same propagating \(qqqg\) self-energy blocks as the H2 Hamiltonian;
- include the required instantaneous terms;
- include the vertex counterterm and residue information;
- test the \(q\to0\) relation between charge/vertex and self-energy renormalization;
- fail when a required attachment, instantaneous partner, counterterm, or regulator identity is wrong;
- report the finite-truncation defect;
- state explicitly that it is not a full non-Abelian Slavnov–Taylor proof.

Allowed readiness wording:

```text
ABELIANIZED_WARD_BENCHMARKED
FINITE_BASIS_CHARGE_CLOSURE
```

Forbidden wording:

```text
FULL_QCD_WARD_CLOSURE
```

---

# 13. Exact, Krylov, state-tracking, and TTN solvers

For every small H2 block:

1. assemble the Hermitian matrix;
2. implement matrix-free action;
3. compare deterministic random-vector actions;
4. solve by dense Hermitian diagonalization;
5. solve by matrix-free Krylov methods;
6. compare eigenvalues, eigenspaces, currents, sector probabilities, and OAM ledgers.

Track states across resolution and coupling flow using:

- exact quantum numbers;
- comparison-map overlaps;
- principal angles for near-degenerate subspaces;
- current fingerprints;
- \(qqqg\) probability and gluon-momentum fingerprints;
- deterministic phase conventions.

Include a controlled valence-like/gluon-rich avoided crossing. Eigenvalue-order tracking must fail while overlap/subspace/fingerprint tracking succeeds.

Extend the C8 TTN to

\[
\mathcal N_{\mathrm{state}}
=
\mathcal N_{qqq}
\oplus
\mathcal N_{qqqg}
\]

with an explicit Fock-sector/root edge. The sector-changing Hamiltonian must be an operator network that connects the sectors. Do not absorb \(qqqg\) amplitudes into a single effective valence tensor.

The \(qqqg\) fusion tree must retain:

- both three-quark color-octet multiplicities;
- adjoint gluon representation;
- gluon helicity;
- orbital and total-\(J^z\) labels;
- permutation and outer-multiplicity labels;
- regulator and resolution identity.

At full allowed bond dimension, exact tensorization must reproduce the exact state and tested observables.

Implement a genuine variational coupled-sector TTN solver. For nested bond spaces,

\[
E_{\chi_2}\le E_{\chi_1},
\qquad
E_\chi\ge E_{\mathrm{exact}}.
\]

Report versus bond policy:

```text
energy error
state/subspace overlap
qqqg probability error
gluon momentum/helicity/OAM errors
current and Ward errors
color-multiplicity reconstruction
discarded weight by symmetry sector
contraction cost
```

At least one low-rank policy must visibly miss a genuine gluon/OAM or current feature.

---

# 14. Gluon, momentum, helicity, and OAM exports

Export validation-only microscopic diagnostics from the same state:

\[
P_{qqq}+P_{qqqg}=1,
\]

\[
\langle x_q\rangle+\langle x_g\rangle=1,
\]

and the canonical finite-basis light-front spin ledger

\[
\frac12
=
\frac12\Delta\Sigma
+
\Delta G
+
L_q
+
L_g
+
\delta_{J,r}.
\]

This decomposition is gauge-, regulator-, and truncation-dependent. It is not yet a matched QCD spin decomposition.

Export:

```text
qqq and qqqg probabilities
gluon longitudinal-momentum fraction
gluon-helicity blocks
quark-helicity blocks
quark and gluon canonical OAM blocks
total Jz closure
field-strength operator blocks compatible with C6 projectors
both qqqg color-singlet multiplicities
correlated proton/neutron member identity
```

Do not call these physical gluon PDFs, GTMDs, or TMDs.

---

# 15. Feshbach comparison with the H1 effective branch

Construct a finite controlled comparison in which the explicit \(qqqg\) sector is eliminated:

\[
H_{\mathrm{eff}}(E)
=
PHP
+
PHQ\frac{1}{E-QHQ}QHP.
\]

Transform the selected current/operator consistently.

Compare the induced valence interaction with the H1 effective color-spin branch. Record:

- matched component;
- orthogonal remainder;
- energy dependence;
- energy and current equivalence residuals;
- the domain over which the comparison is meaningful.

Do not claim exact H1/H2 equivalence unless the remainder vanishes in the declared benchmark.

Encode the provenance relation as:

```text
explicit qqqg sector
    EQUIVALENT_TO
induced valence operator + declared remainder
```

not as an unconditional identity. Selecting the explicit sector and its induced replacement simultaneously must fail before numerical evaluation.

---

# 16. Controlled microscopic reconnection to C5/C6

Implement a typed adapter such as:

```text
MicroscopicWilsonInputAdapter
MicroscopicRescatteringInput
```

It may expose only:

```text
H2 state-bundle identity
qqqg amplitudes and both color multiplicities
Hamiltonian-owned qg vertex/coupling
OAM and helicity blocks
ordered-link/color capabilities
regulator identity
cut-support status
phase/soft matching status
```

Reuse the existing C5/C6 path, pole, cut-ledger, color, ordered-link, phase-budget, and soft-overlap types. Do not duplicate them.

Required behavior:

1. a finite off-shell discrete H2 spectrum with no declared physical cut support gives exactly zero absorption;
2. a separately declared finite-volume or continuum spectral rule may activate the existing cut machinery;
3. finite numerical \(\epsilon\) cannot become physical support;
4. the Wilson coupling comes from the H2 Hamiltonian identity;
5. a separately supplied scalar coupling fails;
6. the C4 analytic \(qqqg\) state and H2 microscopic \(qqqg\) state are mutually exclusive inputs;
7. the adapter remains validation-only and does not make the state `WILSON_READY`.

Highest allowed status:

```text
MICROSCOPIC_WILSON_INPUT_INTERFACE_VALIDATED
```

---

# 17. Required benchmark families

Implement at least:

### H2-A — coupled-block Hermiticity and selection rules

Test diagonal/off-diagonal adjoints, quantum numbers, both singlet multiplicities, longitudinal conservation, permutation signs, and random complex superpositions.

### H2-B — sector-dependent renormalization flow

Use a finite exact oracle in which bare masses, sector counterterms, and vertex counterterms flow while pole mass, charge, and the declared renormalized vertex remain stable.

### H2-C — instantaneous and Abelianized Ward closure

Demonstrate closure with propagating, instantaneous, and counterterm pieces. Omitting each required piece must generate a signed nonzero residual.

### H2-D — exact/Krylov/TTN coupled-sector agreement

Verify full-bond exact reconstruction and variational convergence. Include an observable-sensitive low-rank failure.

### H2-E — gluon and angular-momentum ledgers

Verify probability, momentum, helicity, OAM, and total-\(J^z\) closure.

### H2-F — explicit-sector/Feshbach comparison

Verify Hamiltonian and transformed-operator equivalence in the controlled finite model and retain a nonzero remainder when the H1 effective interaction is incomplete.

### H2-G — microscopic Wilson reconnection

Verify adapter identity, zero absorption for an off-shell discrete spectrum, activation only through declared support, and exact reuse of C5/C6 types.

### H2-H — state tracking through a sector avoided crossing

Show eigenvalue-order tracking fails while overlap/subspace/current/gluon-content tracking succeeds.

### H2-I — assumption compiler and provenance normal form

Compile all plans, reject forbidden combinations, normalize explicit/induced alternatives, and reproduce deterministic certificates.

---

# 18. Readiness statuses and downstream gates

C9 may issue only qualified statuses such as:

```text
H2_QQQG_BASIS_VALIDATED
H2_COUPLED_HAMILTONIAN_BENCHMARKED
H2_SECTOR_RENORMALIZATION_FLOW_BENCHMARKED
H2_ABELIANIZED_WARD_BENCHMARKED
H2_COUPLED_TTN_VALIDATED
H2_GLUON_OAM_EXPORTS_VALIDATED
H2_ASSUMPTION_COMPILER_VALIDATED
MICROSCOPIC_WILSON_INPUT_INTERFACE_VALIDATED
```

It may not issue:

```text
PHYSICAL_NUCLEON_EIGENSTATE
CONTINUUM_QCD_RENORMALIZED
FULL_QCD_WARD_CLOSURE
GTMD_OVERLAP_READY
PHYSICAL_GLUON_PDF_READY
WILSON_READY
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
TMD_EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
TMD_PREDICTION_READY
```

C9 outputs must remain unreachable from production, nuclear composition, Volume V evolution, physical process maps, and inference roots.

---

# 19. Mandatory negative-injection suite

Add at least **72 stable C9 injection IDs** with ordered diagnostics. Include all of these failure classes.

## Compiler and plan failures

1. H1 effective color-spin plus explicit \(qqqg\);
2. silent physical-sector insertion by dependency closure;
3. C4 analytic and C9 microscopic \(qqqg\) selected together;
4. missing compilation certificate;
5. identity-changing H1 migration;
6. stale capability snapshot;
7. adding mutually exclusive plans as amplitudes;
8. unstructured compiler failure;
9. missing unresolved-physics record.

## Basis, color, and permutation failures

10. merge the two \(qqqg\) singlet multiplicities;
11. singlet \(qqq\) times free gluon;
12. omit the adjoint generator;
13. break quark antisymmetry;
14. omit a gluon-helicity block;
15. violate total \(K\);
16. violate total \(J^z\);
17. identify incompatible \(L_z\) blocks;
18. lose outer-multiplicity identity.

## Hamiltonian and vertex failures

19. arbitrary dense random qg block;
20. missing absorption adjoint;
21. different emission/absorption couplings;
22. longitudinal nonconservation;
23. vertex from another Hamiltonian hash;
24. H1 color-spin retained in H2 plan;
25. oscillator scale used as coupling scale;
26. endpoint policy changed without identity change;
27. missing truncation-discrepancy operator.

## Instantaneous and Ward failures

28. omit required instantaneous-fermion term;
29. omit required instantaneous-gluon term;
30. silently change inverse-derivative prescription;
31. include a forbidden zero mode;
32. use the unchanged C8 current when H2 terms are required;
33. fit independent current-component normalizations;
34. fit proton and neutron charges independently;
35. set the Ward residual to zero manually;
36. claim full non-Abelian closure.

## Renormalization failures

37. freeze sector counterterms across resolutions;
38. interpret sector bare masses as physical masses;
39. change renormalization conditions at one tower point;
40. hide an unidentifiable parameter direction;
41. fit a withheld vertex point;
42. fit a withheld gluon observable;
43. compare bare wavefunctions as regulator-independent observables;
44. omit comparison-map identity;
45. claim continuum convergence from the finite tower.

## Solver and TTN failures

46. mix exact and Krylov results from different Hamiltonians;
47. track only by eigenvalue order;
48. fail to track a near-degenerate subspace;
49. omit the Fock-sector root edge;
50. absorb \(qqqg\) into one effective \(qqq\) tensor;
51. drop an outer-multiplicity edge label;
52. fail full-bond reconstruction;
53. variational energy below exact energy beyond tolerance;
54. nonmonotone optimized nested bond spaces;
55. prune the only block supporting a requested gluon/OAM observable;
56. evaluate a current with a TTN from another plan;
57. omit discarded-weight reporting by symmetry sector.

## Gluon/OAM ledger failures

58. violate \(P_{qqq}+P_{qqqg}=1\);
59. violate quark-plus-gluon momentum closure;
60. use an inconsistent gluon-helicity convention;
61. omit one color multiplicity from exports;
62. call the finite-basis spin ledger a matched QCD decomposition;
63. promote a field-strength block to a gluon TMD;
64. lose correlated proton/neutron member identity;
65. hide a \(J^z\) defect in a generic band.

## Feshbach, provenance, and downstream failures

66. select explicit \(qqqg\) and induced replacement together;
67. claim exact H1/H2 equivalence with nonzero remainder;
68. omit transformed-current terms under elimination;
69. deduplicate distinct paths because matrices coincide;
70. discard an unresolved provenance cycle;
71. interpret homology as an amplitude;
72. alter production provenance or default composition.

Also add stable IDs for:

- separately supplied Wilson coupling;
- finite \(\epsilon\) used as cut support;
- off-shell discrete absorption;
- duplicated C5/C6 types;
- lost ordered gluon-link identity;
- collapsed \(f/d\) channels;
- false `WILSON_READY`;
- nuclear/evolution/process/inference promotion;
- production registry mutation;
- authoritative artifact mutation;
- normative-source mutation.

The final count should exceed 72 if necessary to cover these additional gates.

---

# 20. Required documentation and manifests

Create at least:

```text
docs/next_level/c9_implementation_report.md
docs/next_level/c9_api.md
docs/next_level/c9_requirement_coverage.json
docs/next_level/c9_baseline_manifest.json
docs/next_level/c9_normative_source_integration.json
docs/next_level/c9_compiler_manifest.json
docs/next_level/c9_hamiltonian_manifest.json
docs/next_level/c9_renormalization_trajectory.json
docs/next_level/c9_ward_closure_report.json
docs/next_level/c9_tensor_network_manifest.json
docs/next_level/c9_gluon_oam_ledger.json
docs/next_level/c9_feshbach_comparison.json
docs/next_level/c9_wilson_reconnection_manifest.json
docs/next_level/c9_injection_manifest.json
docs/next_level/c9_regression_report.json
docs/next_level/c9_unresolved_physics_gaps.md
```

Add ADRs for:

```text
general H2 assumption/compiler identity
explicit qqqg versus effective color-spin exclusivity
sector-dependent renormalization
instantaneous-kernel prescription
Abelianized Ward benchmark
sector-resolved TTN topology
microscopic Wilson reconnection boundary
```

Update `handoff/ROADMAP.md` without overwriting historical reports.

All JSON must be deterministic, schema validated, and content-addressed where appropriate.

---

# 21. Final validation gates

C9 is complete only if:

1. the exact C8 baseline reproduces;
2. all existing and new tests pass;
3. all 9 builders pass;
4. all 36 evidence rows pass;
5. all 162 atlas pages render;
6. all C3–C8 injections remain passing;
7. at least 72 C9 injections pass;
8. production registry remains 216 routes;
9. all eight authoritative artifacts remain byte-identical;
10. production provenance and default composition remain unchanged;
11. the C7 oracle, C8 manifests, and pinned C5/C6 manifests remain unchanged;
12. H1 plan and bundle identities remain backward compatible;
13. both \(qqqg\) singlet multiplicities are present;
14. coupled Hamiltonian Hermiticity closes;
15. exact and matrix-free actions agree;
16. exact and Krylov eigenspaces and tested observables agree;
17. full-bond TTN agrees with exact diagonalization;
18. variational TTN satisfies upper-bound and nested-space tests;
19. renormalization conditions close at every tower point;
20. the Abelianized Ward benchmark closes and fails under required term removal;
21. probability, momentum, helicity, OAM, and total-\(J^z\) ledgers close;
22. Feshbach comparison reports its remainder honestly;
23. Wilson adapter reuses C5/C6 identities and remains validation-only;
24. H2 outputs have no path to production, nuclear, evolution, process, or inference roots;
25. the final working tree is clean;
26. a local final commit exists;
27. nothing is pushed.

Every gate must have a stable coverage entry.

---

# 22. Final response format

Report:

- starting and final commits;
- push and working-tree status;
- total tests, builders, evidence rows, atlas pages, and injection counts;
- requirement coverage count;
- \(qqq\) and \(qqqg\) basis dimensions at each resolution;
- both singlet multiplicities and maximum color/permutation residuals;
- Hamiltonian, vertex, instantaneous, and Hermiticity residuals;
- sector-dependent parameter flow and identifiability diagnostics;
- charge, Ward, current-component, and rotational residuals;
- exact/Krylov/TTN comparisons and bond convergence;
- \(qqqg\) probability, gluon momentum, helicity, and OAM ledgers;
- Feshbach comparison and remainder;
- microscopic Wilson-reconnection status;
- plan IDs and compiler-certificate hashes;
- production and immutable-artifact status;
- files created;
- unresolved physics;
- exact recommended next package.

The expected next package is:

> **C10/H3 — fully antisymmetrized light-sea sectors, chiral dynamics, axial/PCAC currents, explicit/induced sea subtraction, and positive-\(x\) microscopic antiquark exports.**

Do not implement C10 work inside C9.
