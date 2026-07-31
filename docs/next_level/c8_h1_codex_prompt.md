# C8/H1 Codex Work Package

## Title

**Valence-sector Hamiltonian, renormalization-flow, current closure, state tracking, and symmetry-adapted tensor-network benchmark**

## Authoritative baseline

Begin from the completed C7/H0 commit:

```text
f3256cdacf746e8c9e0d3beaad68bc5d6b25f804
```

A documentation-only descendant is acceptable only if this commit remains in its ancestry and no C7 source, manifest, test, or immutable artifact has been modified. Do not use `origin/main` as the scientific baseline unless it points to this exact history.

C7/H0 established a validation-only microscopic basis and Hamiltonian-term spine. It did **not** establish a physical nucleon eigenstate, continuum or renormalized QCD, a GTMD parent, a microscopic Wilson line, nuclear matching, evolution, or inference. Preserve that boundary.

## Normative sources

Read these sources completely before coding:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_i_regulated_light_front_foundations.tex
references/volume_ii_common_nucleon_gtmd_overlaps.tex
references/volume_iii_dynamical_wilson_lines.tex
references/volume_iv_matched_spin1_nuclear_dynamics.tex
references/volume_v_matching_evolution_factorization.tex
references/volume_vi_shared_inference_validation.tex
references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
references/formalism_volume_index.md
references/model_construction_note.tex            # if present
```

Also read the actual implementation interfaces and reports:

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c7_api.md
docs/next_level/c7_regression_report.json
docs/next_level/c7_tolerance_manifest.json
docs/next_level/c6_api.md
docs/next_level/c6_implementation_report.md
handoff/ROADMAP.md
```

If a normative file is absent, do not invent its contents. Record the absence, use the equations and requirements reproduced in this prompt, and complete all work that does not depend on the missing text.

## Primary objective

Implement the first nontrivial **valence-only** light-front Hamiltonian and renormalization-flow benchmark on top of the exact C7/H0 basis:

```text
H0 symmetry-complete qqq basis
    -> controlled valence Hamiltonian terms
    -> induced-confinement and zero-confinement assumption branches
    -> shared renormalization conditions at several resolutions
    -> exact and matrix-free diagonalization
    -> symmetry-adapted tree-tensor-network representation and variational benchmark
    -> deterministic eigenstate tracking across the tower
    -> Hamiltonian-consistent electromagnetic current
    -> mass, charge, form-factor, rotational, and current-flow diagnostics
    -> versioned valence-only microscopic state bundle
```

C8/H1 is the first package that solves an interacting microscopic eigenproblem. It is still a finite, validation-only, valence-sector Hamiltonian EFT benchmark. It must not claim sea, gluon, GTMD, Wilson, nuclear, LF-to-QCD, evolution, process, or inference readiness.

## Scientific nonclaims and forbidden shortcuts

C8 must not:

- modify or feed the accepted phenomenological production model;
- create, replace, or extend the 216-route production TMD registry;
- claim a physical or converged nucleon from one small matrix;
- claim continuum QCD, a complete renormalization trajectory, or a physical model scale;
- claim antiquark or gluon distributions from a valence-only state;
- add a TMD-specific width, normalization, phase, or latent curve;
- fit an independent coefficient to each current component or observable;
- identify the oscillator scale `b`, Hamiltonian resolution `lambda`, TMD rapidity scale, Collins--Soper scale, or hard scale with one another;
- reuse the C5/C6 Wilson kernel as a Hamiltonian interaction;
- use DGLAP or TMD evolution to define the Hamiltonian scale;
- call an induced confining term a universal immutable QCD potential;
- freeze induced-confinement coefficients while changing the basis or Hamiltonian resolution;
- use a current imported from a different Hamiltonian;
- identify a state across resolutions only by eigenvalue ordering;
- treat a dense tensor with deleted forbidden entries as a symmetry-preserving tensor network;
- call an SVD compression of an exact state a variational tensor-network solver unless a Rayleigh-quotient optimization is also implemented and tested;
- push any commit or publish to the network.

## Immutable pre-edit gates

Before editing, reproduce and record the complete C7 baseline:

```text
834 tests passed
9 acceptance builders passed
36/36 evidence rows passed
162/162 atlas pages rendered
C3 injections: 24/24
C4 injections: 40/40
C5 injections: 48/48
C6 injections: 60/60
C7 injections: 48/48
C7 requirements covered: 74
production registry: 216 routes
all eight authoritative production artifacts byte-identical
all pinned C5/C6 manifests byte-identical
working tree clean
```

Record exact commands, environment versions, hashes, and baseline commit in:

```text
docs/next_level/c8_preimplementation_baseline.json
```

Stop only if the baseline cannot be reproduced after diagnosis. Do not repair a baseline failure by changing accepted physics or artifacts.

---

# Part I. C8 typed objects

Reuse C7 classes and identities. Do not build a parallel microscopic type system.

Implement or extend the following objects in an isolated package such as:

```text
src/deuteron_wigner/microscopic/h1/
```

or an equivalent location consistent with the repository architecture.

## 1. `H1AssumptionBundle`

A frozen, serializable declaration of the scientific choices used to construct one H1 branch. It must include at least:

```text
bundle_id
scope = C8_H1_VALIDATION_ONLY
fock_set = {qqq}
strong_isospin = exact | controlled_breaking
resolution_tower_id
confinement_route = INDUCED_REFIT | ZERO_CONFINEMENT
spin_interaction_route = EFFECTIVE_COLOR_SPIN | NONE
current_route = GAUGED_HAMILTONIAN
solver_routes = EXACT | KRYLOV | TREE_TENSOR_NETWORK
renormalization_conditions
calibration_partition
withheld_partition
operator_basis_version
provenance_root
```

The bundle is immutable after compilation. A changed assumption creates a new identity.

## 2. `H1PredictionPlan`

Compile an admissible `H1AssumptionBundle` into a typed directed plan:

```text
basis
 -> Hamiltonian terms
 -> counterterms / induced terms
 -> calibration conditions
 -> solver
 -> state tracking
 -> current construction
 -> observables and diagnostics
 -> state bundle
```

This is the first implementation of the project-level idea

```text
AssumptionBundle -> admissibility proof -> PredictionPlan
```

The C8 plan produces only valence state and current predictions. It cannot reach TMD, Wilson, nuclear, evolution, process, or inference roots.

## 3. `ValenceHamiltonianTerm`

Extend the C7 `HamiltonianTerm` contract. Every term must carry:

```text
term_id
operator_class
source_sector = qqq
target_sector = qqq
HamiltonianResolution
basis identity
coupling/parameter ownership
color, flavor, Jz, parity, permutation selection
kernel and regulator identity
Hermiticity partner or self-adjoint proof
canonical | induced | counterterm | discrepancy status
power counting / naturalness metadata
provenance and ablation relation
```

## 4. `ValenceHamiltonian`

The finite H1 mass-squared operator is

\[
\mathcal M_{r,\mathrm{H1}}^2
=
\mathcal M_{0,r}^2
+V_{\mathrm{conf},r}^{\mathrm{ind}}
+V_{\mathrm{spin},r}^{\mathrm{ind}}
+\delta\mathcal M_{\mathrm{ct},r}^2
+\Delta\mathcal M_{r}^{2,\mathrm{trunc}}.
\]

This is a valence effective Hamiltonian. The absence of explicit `qqqg` and `qqqq qbar` sectors must remain visible in its identity and discrepancy record.

## 5. `RenormalizationCondition`

Each condition must declare:

```text
condition_id
observable/operator
kinematics
reference value
reference provenance
calibration or holdout role
uncertainty / tolerance
parameter block it constrains
resolution points to which it applies
```

No condition may target a named TMD.

## 6. `RenormalizationTrajectory`

Stores the family

\[
\mathfrak R_r=
(\mathcal R_r,\theta_{\mathrm{bare}}^{(r)},
\delta\theta_{\mathrm{ct}}^{(r)},
\theta_{\mathrm{ind}}^{(r)},
\{\mathcal C_i\},\mathcal S_r,\mathcal Z_r,\Delta_r)
\]

at every tower point. It must retain parameter flow, condition residuals, naturalness diagnostics, covariance/Hessian information where available, and comparison maps between adjacent points.

## 7. `ValenceVectorCurrent`

The H1 current is

\[
J_r^\mu
=
J_{(1),r}^\mu
+J_{\mathrm{ind},r}^\mu
+\delta J_{\mathrm{ct},r}^\mu,
\]

with every term owned by and compatible with the same Hamiltonian identity. If an interaction current is not required by the chosen reduced benchmark, this must be demonstrated, not assumed.

## 8. `ValenceStateTracker`

Tracks a physical state across the tower using:

- exact quantum numbers;
- comparison-map overlap;
- principal angles for near-degenerate subspaces;
- current fingerprints;
- basis/OAM content;
- deterministic phase convention.

Eigenvalue ordering alone is forbidden.

## 9. Symmetry-adapted tensor-network objects

Implement at least:

```text
SymmetryTensorIndex
BlockSparseTensor
ValenceCouplingTree
ValenceTTNState
ValenceTensorOperator
TTNOptimizationResult
BondDimensionManifest
```

The preferred first network is a binary tree tensor network aligned with the exact three-quark coupling tree, for example

```text
((q1, q2) -> intermediate color/flavor/spin/OAM irrep, q3) -> total nucleon block.
```

A different network is acceptable only if its physical index map and symmetry advantages are documented and benchmarked.

## 10. `ValenceMicroscopicStateBundle`

Export a versioned H1 bundle containing:

```text
Hamiltonian identity
assumption bundle and compiled plan
renormalization trajectory member
resolution and basis identities
mass and normalized eigenstate
exact and TTN representations
phase and state-tracking records
current operators and matrix elements
sector/color/permutation/OAM ledgers
solver and tensor-network residuals
parameter derivatives
convergence and defect reports
readiness statuses
```

The bundle must be explicitly marked `VALENCE_ONLY` and `C8_H1_VALIDATION_ONLY`.

---

# Part II. Nontrivial qqq basis tower

C7's `1 x 1` qqq benchmark blocks were sufficient for H0 architecture tests but are not sufficient for an interacting H1 eigenstate.

Construct at least three nested or explicitly compared qqq resolutions with nontrivial longitudinal, transverse, spin, and OAM content. The exact dimensions may be chosen from the available basis, but the tower must satisfy:

1. each retained `Jz = +/-1/2` proton/neutron block has dimension greater than one;
2. the dimension increases at least twice along the primary tower;
3. the largest exact-diagonalization oracle remains computationally tractable;
4. at least one independent trajectory varies `b` or `lambda` without merely repeating the same basis;
5. at least `Lz = 0` and `|Lz| = 1` content can mix where allowed;
6. exact color singletness, antisymmetry, center-of-mass gates, and longitudinal/transverse cutoffs remain inherited from H0.

Do not meet this requirement by duplicating identical states or by adding labels that the Hamiltonian never couples.

Produce:

```text
docs/next_level/c8_basis_tower_manifest.json
```

with dimensions, quantum-number blocks, basis hashes, comparison maps, and center-of-mass diagnostics.

---

# Part III. Valence interaction basis

## A. Induced confinement branch

Implement a resolution-dependent induced operator

\[
V_{\mathrm{conf},r}^{\mathrm{ind}}
=
\kappa_{T,r}^{4}\mathcal O_T^{\mathrm{conf}}
+
\kappa_{L,r}^{4}\mathcal O_L^{\mathrm{conf}}
+
\sum_{n>1}d_{n,r}^{\mathrm{conf}}\mathcal O_n^{\mathrm{conf}}.
\]

For H1, a harmonic or another smooth infrared operator in Jacobi variables is acceptable if:

- its matrix elements are derived and independently checked;
- it respects color, flavor, `Jz`, parity, and permutation symmetry;
- its center-of-mass behavior is controlled;
- its coefficients are resolution dependent;
- its provenance states which omitted infrared regions/sectors it represents;
- it is not described as a universal continuum QCD potential.

## B. Zero-confinement branch

The identical tower must also be evaluated with

\[
V_{\mathrm{conf},r}^{\mathrm{ind}}=0.
\]

Other allowed effective terms and counterterms must remain typed. This branch is not expected automatically to produce the same low-resolution spectrum; it is the required ablation trajectory.

## C. Effective color-spin branch

A reduced valence color-spin or hyperfine operator may be included as

\[
V_{\mathrm{spin},r}^{\mathrm{ind}}
=
\sum_{i<j}
C_{ij,r}\,
(T_i^aT_j^a)\,
\mathcal S_{ij,r}\,
\mathcal R_{ij,r},
\]

where the spin/helicity kernel, regulator, and parameter ownership are explicit. It must be labeled an induced/effective H1 operator, not a complete canonical one-gluon exchange calculation.

If the implementation interprets it as a Feshbach image of the omitted `qqqg` sector, add an explicit provenance relation:

```text
EFFECTIVE_QQQ_COLOR_SPIN  ALTERNATIVE_TO  EXPLICIT_QQQG_DYNAMICS
```

and prohibit selecting both until an overlap subtraction/matching map exists.

## D. Counterterms and discrepancy

At minimum, implement a shared light-quark mass/counterterm block and any current normalization counterterm required by the declared conditions. Counterterms are resolution indexed and cannot be named-observable parameters.

The omitted `qqqg`, sea, higher-orbital, zero-mode, instantaneous, and basis components must appear in a typed `H1TruncationDiscrepancy` record. Unimplemented contributions are not zero.

---

# Part IV. Calibration and renormalization-flow benchmark

C8 is a benchmark of a renormalization trajectory, not a final physical fit.

## Mandatory calibration conditions

Use a small shared set fixed before optimization. At minimum:

1. one isospin-symmetric nucleon mass condition at each resolution;
2. proton vector charge normalization `F1p(0) = 1`;
3. neutron vector charge `F1n(0) = 0` as a prediction/closure test from the correlated isospin partner;
4. center-of-mass/Lawson condition;
5. one declared interaction or renormalization subproblem condition if needed to separate parameter directions.

A synthetic exactly known target is acceptable for the interaction subproblem and must be labeled `VALIDATION_ONLY`. If a physical nucleon mass value is used, record its source and do not imply that fitting the mass makes the valence state physical.

## Withheld quantities

Freeze before final optimization at least:

- one nonzero-transfer proton vector-current matrix element or radius proxy;
- one neutron current matrix element;
- one independent current-component extraction;
- one axial or tensor valence matrix element if implemented;
- one rotational/Pauli--Lubanski diagnostic;
- parameter-flow behavior on a resolution point not used in the initial fit.

A failed holdout may not be moved into calibration without creating a new model version and a new holdout.

## Parameter-flow requirements

For every tower point:

- refit the same declared renormalization conditions;
- record all bare, induced, and counterterm parameters;
- record the objective/Hessian/Jacobian and identifiability diagnostics;
- compare dimensionless naturalness combinations;
- report whether induced-confinement coefficients stabilize, decrease, or grow;
- do not infer a continuum limit from only one trajectory;
- separate numerical error from basis, regulator, interaction, and calibration uncertainty.

Implement Benchmark H-D using an exactly solvable self-energy toy model to verify that pole mass and charge remain fixed while sector/bare parameters flow.

---

# Part V. Hamiltonian-consistent current

Construct the vector current from the same H1 Hamiltonian and regulator. At minimum:

1. implement the one-body quark current with exact flavor charges;
2. implement any induced or counterterm current required by gauging the reduced interaction/regulator;
3. verify Hermiticity and charge normalization;
4. compare at least two independent current components or frames where the finite H1 model supports them;
5. report the current-component/rotational defect rather than forcing it to zero with one coefficient per component;
6. preserve proton/neutron correlated member identity;
7. verify that using a current from another Hamiltonian identity fails before evaluation.

The current normalization factor, if required, is shared across every matrix element in its operator block. It cannot be separately refitted at each transfer.

---

# Part VI. Solver hierarchy and state tracking

## Exact and Krylov solvers

For every small benchmark block:

- perform explicit Hermitian diagonalization;
- perform matrix-free Lanczos or an equivalent Krylov solution;
- compare low eigenvalues, eigenvectors/subspaces, residuals, and current matrix elements;
- retain deterministic ordering only after state identity is established.

The eigenpair residual is

\[
r_n=
\frac{\|\mathcal M_r^2\psi_n-M_{n,r}^2\psi_n\|}
{\|\mathcal M_r^2\|\|\psi_n\|+|M_{n,r}^2|\|\psi_n\|}.
\]

## State tracking

Implement Benchmark H-J with a controlled avoided crossing. Demonstrate that:

- eigenvalue-order tracking chooses the wrong branch;
- overlap plus current fingerprints recover the intended state;
- principal-angle tracking works for near-degenerate subspaces;
- the phase convention is deterministic and continuous;
- proton and neutron partners remain correlated.

---

# Part VII. Symmetry-adapted tensor-network benchmark

This section is mandatory. It begins the numerical realization of the original geometric/tensor architecture.

## A. Exact symmetry blocks

Every tensor index must carry physical or numerical meaning:

```text
parton slot
longitudinal mode
transverse mode / OAM
helicity
flavor/isospin
color irrep and multiplicity
permutation irrep
Jz
resolution identity
```

Forbidden symmetry blocks must be absent, not stored densely and clipped afterward.

## B. Coupling tree

Build a declared three-quark tree, for example:

\[
(q_1\otimes q_2)
\longrightarrow
(R_c,R_f,S,L_z,\alpha)
\quad\text{then}\quad
\otimes q_3
\longrightarrow
(I,J^z,\text{color singlet}).
\]

Alternative recoupling trees must be related by a tested unitary recoupling map.

## C. Exact-state tensorization

For small blocks, convert the exact eigenvector to the TTN representation using symmetry-resolved SVDs. Verify:

- exact reconstruction at full allowed bond dimension;
- norm and phase preservation;
- color and permutation closure;
- current matrix elements agree with the dense/sparse representation;
- discarded-weight accounting is block resolved.

## D. Variational TTN solver

Implement an actual Rayleigh-quotient optimization or sweep over the TTN tensors at fixed bond dimensions `chi`. A mere compression of an exact state is not sufficient.

Required checks:

- the optimized energy is variational relative to the exact ground state;
- energy is nonincreasing as the allowed bond dimension grows;
- overlap with the exact state improves or the subspace distance decreases;
- mass, charge, and withheld current errors are reported versus `chi`;
- convergence is evaluated separately in each symmetry block;
- at full bond dimension the TTN reproduces exact diagonalization within tolerance;
- at least one deliberately low-rank network fails to reproduce an OAM/current feature, demonstrating that tensor rank is a real truncation axis.

## E. Tensor-operator representation

Represent the H1 Hamiltonian as a symmetry-adapted tree tensor operator or an equivalent factorized contraction graph. Verify operator application against the H0/H1 matrix-free oracle on deterministic random states.

## F. Bond-dimension manifest

Create:

```text
docs/next_level/c8_tensor_network_manifest.json
```

recording tree topology, symmetry sectors, bond dimensions, discarded weights, energies, overlaps, current errors, contraction costs, and exact-oracle comparisons.

Do not claim that successful qqq TTN compression establishes low entanglement for the full QCD Fock state.

---

# Part VIII. Assumption-conditioned prediction planning

Implement the first limited assumption compiler so that the same code can evaluate scientifically distinct H1 branches without hidden switches.

At minimum compile these plans:

```text
H1-PLAN-A:
  induced confinement refitted at every resolution
  effective color-spin operator active
  exact/Krylov/TTN solvers

H1-PLAN-B:
  zero confinement
  effective color-spin operator active
  exact/Krylov/TTN solvers

H1-PLAN-C:
  induced confinement
  color-spin operator disabled
  exact/Krylov/TTN solvers
```

Each plan must produce its own Hamiltonian identity, parameter trajectory, state bundle, diagnostics, and provenance. Results may be compared, but mutually exclusive branches may not be added together.

The compiler must reject, before numerical evaluation:

- explicit `qqqg` dynamics together with an induced operator declared to replace it;
- frozen confinement coefficients across changing resolutions;
- current and Hamiltonian identities from different plans;
- a solver result whose basis or Hamiltonian hash differs from the plan;
- a TTN state whose symmetry or bond manifest does not match the Hamiltonian block;
- an H1 bundle requested for TMD, Wilson, nuclear, matching, evolution, process, or inference output.

---

# Part IX. Required benchmarks

Implement and document at least these Volume VII benchmarks:

## H-D. Fock-sector renormalization toy

Exactly solvable self-energy model with two and three retained sectors. Verify pole-mass and charge invariance under refitted sector counterterms while bare parameters flow.

## H-H. Rotational/current restoration benchmark

Compare independent current components or frames across the H1 tower. Quantify the defect and determine whether it decreases with basis enlargement or is associated with an induced operator. Do not fit each component separately.

## H-J. State tracking

Controlled avoided crossing with overlap/current tracking versus failed eigenvalue-order tracking.

## H-K. Confinement flow

Compare `INDUCED_REFIT` and `ZERO_CONFINEMENT` trajectories. Record masses, radii/current moments, OAM content, current defects, and coefficient flow. Distinguish infrared acceleration from a term that merely absorbs every omitted effect.

## H-TN. Tensor-network representation and variational solver

New C8 benchmark described in Part VII. Exact/Krylov/TTN agreement at full bond dimension and controlled errors at lower rank.

## H-PLAN. Assumption compiler

Compile and execute H1-PLAN-A/B/C with stable identities, deterministic manifests, no illegal cross-plan composition, and complete provenance.

---

# Part X. Readiness and fail-closed downstream gates

C8 may issue only scoped statuses such as:

```text
H1_VALENCE_BASIS_TOWER_VALIDATED
H1_VALENCE_HAMILTONIAN_BENCHMARKED
H1_RENORMALIZATION_FLOW_BENCHMARKED
H1_VECTOR_CURRENT_BENCHMARKED
H1_STATE_TRACKING_VALIDATED
H1_TTN_REPRESENTATION_VALIDATED
H1_TTN_VARIATIONAL_BENCHMARKED
H1_ASSUMPTION_COMPILER_VALIDATED
```

It may not issue:

```text
PHYSICAL_NUCLEON_EIGENSTATE
RENORMALIZATION_TRAJECTORY_VALIDATED   # unqualified production status
CURRENT_READY                         # production status
GTMD_OVERLAP_READY
WILSON_READY
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
INFERENCE_READY
TMD_PREDICTION_READY
```

Every attempted downstream use must fail with a structured diagnostic naming the missing sector, operator, matching, or convergence requirement.

---

# Part XI. Mandatory negative injections

Add at least 56 stable C8 injections. Include, at minimum:

1. same serialized ID for different assumption bundles;
2. current from a different Hamiltonian identity;
3. frozen induced-confinement coefficient across resolutions;
4. oscillator scale used as Hamiltonian resolution;
5. Hamiltonian resolution used as TMD rapidity scale;
6. omitted center-of-mass policy;
7. non-Hermitian confinement matrix;
8. color-spin operator violating color singletness;
9. spin operator violating `Jz`;
10. broken fermion permutation sign;
11. basis dimension artificially enlarged with duplicate states;
12. mass fit by a TMD-specific parameter;
13. charge fit by a separate factor at each transfer;
14. neutron state independently refitted from proton;
15. eigenstate tracked only by eigenvalue order;
16. omitted comparison map between tower points;
17. phase convention changed silently;
18. near-degenerate subspace treated as one vector without principal angles;
19. numerical solver residual omitted;
20. exact and Krylov matrices from different Hamiltonian hashes;
21. TTN index lacking physical identity;
22. forbidden symmetry block stored and clipped;
23. TTN full-bond reconstruction not exact;
24. TTN energy below exact ground-state energy beyond tolerance;
25. TTN energy increases with added bond capacity because of an optimizer bug;
26. SVD compression mislabeled as variational optimization;
27. TTN current evaluated with a dense state from another plan;
28. tree recoupling map not unitary;
29. discarded weight omitted;
30. low-rank OAM feature silently replaced by a fitted coefficient;
31. induced confinement and zero-confinement branches added together;
32. explicit qqqg dynamics selected with its induced replacement;
33. absent overlap subtraction declared complete;
34. unimplemented instantaneous/zero-mode effects set to zero;
35. physical continuum claim from one tower;
36. physical sea claim from qqq state;
37. physical gluon claim from qqq state;
38. GTMD readiness requested without nonzero-transfer operator exports;
39. Wilson readiness requested without qqqg state and vertex bundle;
40. nuclear readiness requested without correlated complete helicity matrices;
41. LF-to-QCD readiness requested without a closed operator basis;
42. inference readiness requested without covariance and frozen holdouts;
43. production registry mutation;
44. production provenance mutation;
45. authoritative artifact byte change;
46. C5/C6 manifest mutation;
47. normative Volume source mutation;
48. hidden change to C7 tolerance manifest;
49. calibration/holdout role changed after optimization;
50. parameter count equal to named observables by construction;
51. current-component defect forced to zero with independent coefficients;
52. counterterm labeled physical low-energy constant without provenance;
53. zero-confinement branch omitted;
54. H1 plan lacking a discrepancy record for omitted sectors;
55. assumption plan compiled nondeterministically;
56. state bundle missing resolution or Hamiltonian identity.

Additional injections are encouraged when they expose real failure modes.

---

# Part XII. Regression and isolation gates

After implementation, rerun and preserve:

```text
all pre-existing tests plus new C8 tests
9/9 acceptance builders
36/36 evidence rows
162/162 atlas pages
C3 24/24 injections
C4 40/40 injections
C5 48/48 injections
C6 60/60 injections
C7 48/48 injections
216 production routes
all eight authoritative artifacts byte-identical
all pinned C5/C6 manifests byte-identical
production provenance and default composition unchanged
```

C8 must remain unreachable from every accepted production root.

---

# Part XIII. Required documentation and machine-readable deliverables

Create at least:

```text
docs/next_level/c8_implementation_report.md
docs/next_level/c8_api.md
docs/next_level/c8_requirement_coverage.json
docs/next_level/c8_regression_report.json
docs/next_level/c8_tolerance_manifest.json
docs/next_level/c8_basis_tower_manifest.json
docs/next_level/c8_hamiltonian_term_manifest.json
docs/next_level/c8_renormalization_trajectory.json
docs/next_level/c8_current_closure_report.json
docs/next_level/c8_state_tracking_manifest.json
docs/next_level/c8_tensor_network_manifest.json
docs/next_level/c8_assumption_plan_manifest.json
docs/next_level/c8_injection_manifest.json
docs/next_level/c8_unresolved_physics_gaps.md
```

Add ADRs for:

```text
valence interaction basis
induced versus zero-confinement branches
current construction and normalization
state tracking and phase convention
TTN topology and symmetry indices
bond-dimension convergence
assumption-bundle compilation
H1 readiness/status vocabulary
```

Update `handoff/ROADMAP.md` with the exact completion state and next package.

All JSON must be deterministic, schema checked, and stable under repeated generation.

---

# Part XIV. Acceptance criteria

C8/H1 is complete only when all of the following hold:

1. The complete C7 baseline is reproduced before edits.
2. A nontrivial qqq basis tower with increasing dimensions is generated.
3. Exact H0 color, statistics, center-of-mass, and quantum-number gates remain exact.
4. The valence Hamiltonian has typed free, induced, counterterm, and discrepancy blocks.
5. Induced-confinement and zero-confinement trajectories both execute.
6. Shared renormalization conditions are refitted at every tower point.
7. Pole/mass and charge conditions close within declared tolerances.
8. Parameter and counterterm flows are recorded without hidden freezing.
9. The vector current is compatible with the Hamiltonian identity.
10. At least one independent current/form-factor quantity remains withheld.
11. Exact and matrix-free Krylov eigenpairs agree.
12. Avoided-crossing state tracking succeeds while eigenvalue-only tracking fails.
13. A symmetry-adapted TTN exactly represents the full-bond state.
14. A genuine variational TTN solver is implemented and benchmarked.
15. Bond-dimension convergence is recorded for energy and current observables.
16. At least one low-rank network visibly misses an OAM/current feature.
17. H1-PLAN-A/B/C compile deterministically and remain mutually exclusive.
18. A versioned valence microscopic state bundle is exported.
19. No prohibited readiness status is issued.
20. At least 56 C8 negative injections pass.
21. All legacy and C3--C7 tests/injections remain passing.
22. Production registry, provenance, composition, artifacts, and pinned manifests remain unchanged.
23. All documentation/manifests are deterministic and internally consistent.
24. The working tree is clean after one local completion commit.
25. Nothing is pushed.

Do not declare C8 complete if any acceptance criterion is unmet.

---

# Final response format

Report:

- starting and final commits;
- branch/push status and clean-tree status;
- total tests, builders, evidence rows, atlas pages, and injection counts;
- basis dimensions at each tower point;
- Hamiltonian terms and calibrated/shared parameters;
- induced and zero-confinement parameter/mass/current flows;
- exact/Krylov/TTN residuals and overlaps;
- bond-dimension convergence;
- state-tracking and avoided-crossing results;
- current and rotational defects;
- assumption-plan identities;
- immutable artifact and manifest hashes;
- all unresolved physics limitations;
- exact recommended C9/H2 package.

The expected next package is **C9/H2: dynamical qqqg sector, sector-dependent renormalization, instantaneous partners, Ward closure, gluon/OAM exports, and microscopic reconnection to the C5/C6 Wilson engine**. Do not implement C9 work inside C8.
