# C7/H0 Codex Work Package

## Symmetry-complete microscopic basis and Hamiltonian-term spine

You are beginning **C7/H0** for the `uva-spin/DeuteronWigner` project.

This package begins the concrete microscopic Hamiltonian program specified in
**Volume VII: Concrete Microscopic Nucleon Hamiltonian and Renormalization
Program**. It is a validation-only basis, symmetry, and operator-assembly
package. It does **not** calibrate a nucleon, produce a physical eigenstate, or
modify the accepted phenomenological model.

---

## 1. Authoritative starting point

The required C6 ancestor is:

```text
ce4b761d19b23bd5f7da1ddc026153685943e639
```

Before making changes, verify:

```bash
git merge-base --is-ancestor ce4b761d19b23bd5f7da1ddc026153685943e639 HEAD
```

The implementation may start from that exact commit or from a descendant that
contains documentation-only additions of Volumes VI and VII. If `HEAD` differs
from C6 for any other reason, audit and report the difference before coding.
Do not reset, squash, rebase, or rewrite the completed C0--C6 history.

**Do not push.** Create one clean local completion commit only after every gate
in this prompt passes.

### Mandatory C6 baseline

Reproduce and record before editing:

- 759/759 tests;
- 9/9 legacy acceptance/report builders;
- 36/36 evidence rows;
- 162/162 atlas pages;
- 24/24 C3 injections;
- 40/40 C4 injections;
- 48/48 C5 injections;
- 60/60 C6 injections;
- four ordered active-gluon link pairs;
- 24 active-gluon validation channels;
- the accepted production registry fixed at 216 routes;
- production provenance and default composition unchanged;
- all eight authoritative artifacts byte-identical.

The authoritative artifact hashes are:

```text
09f596d73c4e6ffd7c2f58f97d5e82628310d0a5577bdc4ea280be02c1720b45
244a17bbd39852ac47922059815b0926adc3809bd73c60d4ab96be80d7fbd0f5
27dc1e043d087b79fb0fca026b82f234f0b12af165595127dda0744f472a8d89
92c631976766a647d9bf881883ebc10129c6140d3ba41f9970a31781a5bbf9a7
7e53f290510c7fea65876d8b45c2726a06377c3b844da0b306cff28f9f264b4b
48ceff976b76369942850d2da7f4ad61a9f992e2654ed1cc0f007cd37dbef65f
798a345bdb44c5a6447a3139704d1094d653c055aa8156fa4ce673eeaaf4d34b
465d8cd9d0d35aeffea23a795045051ad53061d334309cfb34a95b7ed0c5fdc3
```

If any baseline item fails, diagnose it. Do not repair a baseline failure by
changing accepted numerical physics.

---

## 2. Normative sources

Use the repository's formalism index and source hashes. The normative sequence
is Volumes 0--VII plus the canonical model-construction note and C0--C6
implementation reports.

If Volumes VI and VII are not yet in `references/`, add them in a
**documentation-only commit or documentation-only portion of the C7 commit**
before implementation. Their expected paths and SHA-256 hashes are:

```text
references/volume_vi_shared_inference_validation.tex
568979e0fa0015a70795a7c27c4c98b992848085c982a7ee4eca0374fec72570

references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
326fd902f648b760ee97add0bb30418b4f4843f1bc64c98afd752940d11ac6e1
```

Update `references/formalism_volume_index.md` deterministically if needed.
Do not alter the contents of any normative source during C7. Record all source
paths and hashes in the C7 normative-integration manifest.

Primary C7 requirements come from Volume VII, especially:

- the resolution-indexed Hamiltonian identity;
- the symmetry-adapted BLFQ basis;
- complete color-singlet multiplicities;
- exact fermionic antisymmetry;
- center-of-mass factorization;
- Benchmarks H-A, H-B, and H-C;
- the H0 staged implementation boundary.

C6 remains the authoritative one-Wilson-order active-gluon pilot. Do not modify
its paths, poles, cuts, link pairs, color projections, polarization projectors,
soft-overlap benchmark, phase budgets, or manifests in C7.

---

## 3. Scientific objective

Implement the first validation-only microscopic Hamiltonian layer:

```text
HamiltonianResolution
    -> typed one-particle modes
    -> complete color/permutation basis
    -> physical qqq / qqqg / qqqq-qbar Fock bases
    -> center-of-mass and exact-quantum-number blocks
    -> free invariant-mass operator
    -> canonical Hamiltonian-term interface
    -> one reduced qqq <-> qqqg vertex plus its adjoint
    -> Benchmarks H-A--H-C
```

This package establishes the **basis and matrix-element spine** on which later
canonical QCD kernels, sector-dependent renormalization, currents, GTMD
operators, and eigensolvers will operate.

C7 is complete only if the basis is physically typed and symmetry complete.
Generating arrays of the desired dimension is not sufficient.

---

## 4. Explicit non-objectives

C7 must not:

- fit the nucleon mass, radius, magnetic moment, axial charge, PDFs, GTMDs, or
  TMDs;
- claim a physical proton or neutron eigenstate;
- introduce a confining, chiral, spin-restoration, or phenomenological
  interaction as central physics;
- implement sector-dependent renormalization beyond typed interfaces;
- use an independent normalization, width, phase, or coupling for a named
  TMD;
- implement second- or higher-order Wilson lines;
- alter the C5/C6 one-gluon kernels or soft-overlap benchmark;
- promote any C3--C7 pilot object into the accepted 216-route model;
- perform LF-to-QCD matching, TMD evolution, nuclear composition, process
  factorization, or inference;
- treat a finite basis matrix as continuum QCD;
- push any commit.

The C6 recommendation to study strict Dyson/Magnus Wilson convergence remains
valid, but it is deferred until a dynamical microscopic state and the higher
Fock sectors needed by those orders exist. Do not combine that task with H0.

---

## 5. Frozen light-front and basis conventions

Use

\[
x^\pm=\frac{x^0\pm x^3}{\sqrt2},\qquad
p^2=2p^+p^- - \boldsymbol p_T^2,
\]

and therefore

\[
\mathcal M_{\rm LF}^2=2P^+P^- - \boldsymbol P_T^2.
\]

The free intrinsic invariant mass in sector \(\nu\) is

\[
\mathcal M_{0,\nu}^2
 =\sum_{i\in\nu}
 \frac{\boldsymbol\kappa_{iT}^2+m_i^2}{x_i},
\qquad
\sum_i x_i=1,
\qquad
\sum_i\boldsymbol\kappa_{iT}=0.
\]

A single-particle basis label is

\[
\alpha_i=(a_i,k_i,n_i,m_i,\lambda_i,f_i,c_i),
\]

with

\[
\sum_i k_i=K,\qquad x_i=k_i/K,
\]

and

\[
\sum_i(2n_i+|m_i|+1)\le N_{\max}.
\]

The exact kinematical angular-momentum label is

\[
J^z=\sum_i(m_i+\lambda_i).
\]

Use exact rational longitudinal modes, not floating-point surrogates.
The initial policy is:

- antiperiodic longitudinal modes for quarks and antiquarks;
- periodic **nonzero** modes for gluons;
- an explicit zero-mode policy recording excluded modes, constraint equations,
  induced zero-mode operators, endpoint regulator, and closure tests.

The oscillator scale \(b\), Hamiltonian similarity/resolution scale
\(\lambda_H\), endpoint regulator, numerical quadrature cutoffs, TMD
\(b_{\rm TMD}\), rapidity regulator, and Collins--Soper scales are different
types. No implicit conversion is permitted.

---

## 6. Required package structure

Create a new isolated package, preferably:

```text
src/deuteron_wigner/microscopic/h0/
```

or an equivalently clear package under `src/deuteron_wigner/microscopic/`.
Do not place H0 implementation inside production parent builders or the C3--C6
pilot modules.

The package must expose stable public APIs for the objects below. Private helper
names may differ, but the public responsibilities and serialized identities may
not.

### 6.1 `HamiltonianResolution`

It must contain at least:

```text
K
N_max
oscillator_scale_b
hamiltonian_resolution_lambda
endpoint_regulator
fock_sector_set
longitudinal_boundary_conditions
transverse_basis_id
zero_mode_policy_id
center_of_mass_policy_id
UV_interpretation
IR_interpretation
basis_version
```

Requirements:

- all scale fields use distinct typed identities;
- validation rejects inconsistent or incomplete resolution records;
- serialization is deterministic and versioned;
- two different resolution identities cannot serialize to the same ID;
- the approximate HO interpretations
  `Lambda_IR ~ b/sqrt(N_max)` and `Lambda_UV ~ b*sqrt(N_max)` are stored as
  diagnostics, not exact universal cutoffs;
- resolution identity is attached to every basis, term, matrix, and manifest.

### 6.2 `PartonBasisState`

Each one-particle state must retain:

```text
species
flavor
longitudinal_mode_exact
longitudinal_fraction_exact
transverse_n
transverse_m
light_front_helicity
color_representation
color_basis_label
statistics_class
charge
baryon_number
Jz_contribution
resolution_id
```

Quark, antiquark, and gluon representations must remain distinct. Antiquarks
use the anti-fundamental representation and generator

\[
T_{\bar 3}^A=-(t^A)^T.
\]

### 6.3 `FockSectorSpec` and `ManyBodyBasisState`

Support at least:

```text
qqq
qqqg
qqqq-qbar
```

The state must retain:

- ordered constituent creation labels;
- exact total longitudinal mode;
- exact `N_max` usage;
- total charge, baryon number, flavor, and \(J^z\);
- color-coupling multiplicity;
- permutation/antisymmetry identity;
- center-of-mass quantum number or factorization record;
- deterministic phase and ordering convention;
- resolution and sector IDs.

A state that violates any exact block quantum number is absent from the basis,
not accepted with a penalty.

### 6.4 `ColorSingletBasis`

Construct the complete singlet multiplicities for the retained sectors.
The expected SU(3) singlet multiplicities are:

```text
qqq          : 1
qqqg         : 2
qqqq-qbar    : 3
```

For `qqqg`, the two singlets arise from the two independent three-quark octet
multiplicities coupled to the adjoint gluon. A color-singlet `qqq` tensor
multiplied by a free gluon is invalid.

For `qqqq-qbar`, retain all three independent singlet channels. A single
baryon--meson cluster tensor is not a complete color basis.

For every sector, provide:

- normalized invariant tensors;
- exact or machine-precision total-generator annihilation;
- orthonormality matrix;
- multiplicity labels;
- deterministic phase convention;
- recoupling matrices between supported coupling trees;
- recoupling unitarity tests;
- serialization and content hashes.

Do not infer completeness from the number of arrays generated. Verify the
representation decomposition and rank of the invariant subspace.

### 6.5 `PermutationBasis`

Impose fermionic antisymmetry **before matrix assembly**.

A valid implementation may use canonical occupation-number/creation-operator
ordering, Young-projector machinery, or another exact construction, but it must:

- implement the correct sign under exchange of any two quark creation labels;
- preserve flavor, color, spin, longitudinal, and orbital internal labels;
- handle exchanges across apparent cluster partitions;
- expose multiplicity labels where the same permutation irrep appears more
  than once;
- prove idempotence and Hermiticity of any explicit antisymmetrizer;
- reject post-diagonalization symmetrization as an implementation strategy;
- serialize the convention deterministically.

### 6.6 `PhysicalFockBasis`

Build the physical basis by applying, in a declared order:

```text
longitudinal and N_max support
fermionic statistics
color-singlet projection
exact charge/baryon/flavor block
Jz block
residual-gauge/zero-mode policy
center-of-mass gate
```

At minimum generate small deterministic proton-like and neutron-like reference
blocks with \(J^z=\pm\tfrac12\), while keeping strong isospin as a represented
reference symmetry rather than assigning independent microscopic parameters.

The H0 proton/neutron labels are basis quantum-number blocks, not calibrated
physical states.

### 6.7 Center-of-mass factorization

Implement a typed center-of-mass policy using intrinsic Jacobi coordinates or a
Lawson construction,

\[
\mathcal M_{\beta}^2
 =\mathcal M^2
 +\beta_{\rm CM}(H_{\rm CM}-E_{{\rm CM},0}).
\]

Provide both:

- a direct center-of-mass factorization residual;
- a Lawson excitation diagnostic.

On small benchmark spaces, intrinsic levels must remain stable over a declared
range of \(\beta_{\rm CM}\), while spurious CM levels move. A basis cannot be
marked `MICROSCOPIC_BASIS_READY` when the CM residual exceeds tolerance.

### 6.8 `HamiltonianTerm`

Every term must declare:

```text
term_id
source_sector
target_sector
symmetry_signature
parameter_block_id
regulator_identity
zero_mode_and_endpoint_policy
apply(vector, resolution)
matrix_element(bra, ket)
adjoint_term_id
derivative(parameter_id)
provenance_node
approximation_status
```

A term without source/target sectors, regulator identity, parameter ownership,
or Hermitian partner cannot be assembled.

### 6.9 `FreeInvariantMassTerm`

Implement the free operator from the declared intrinsic mass formula.

Requirements:

- support both matrix-free application and explicit sparse assembly on small
  spaces;
- use the exact longitudinal fractions from the basis;
- evaluate the transverse kinetic operator consistently in the declared HO or
  intrinsic basis;
- validate analytic matrix elements against an independent quadrature or
  direct-integration oracle on small spaces;
- preserve all exact quantum-number blocks;
- report Hermiticity, sparsity, and matrix-free/assembled residuals;
- never identify effective/bare basis masses with MS-bar current masses.

Do not replace the free operator by an arbitrary diagonal spectrum merely to
make H-A easy.

### 6.10 Reduced canonical `qqq <-> qqqg` vertex benchmark

H0 validates the canonical term interface and Hermitian block pairing; it does
not yet claim the complete renormalized QCD vertex kernel.

Implement one **reduced analytic one-vertex benchmark** whose matrix element is
factorized into explicitly typed pieces:

```text
benchmark coupling
fundamental color generator t^a
exact longitudinal momentum conservation
transverse-mode overlap
helicity/Jz selection
regulator factor
basis normalization
```

The benchmark must:

- connect only symmetry-compatible `qqq` and `qqqg` states;
- use the complete `qqqg` singlet-multiplicity basis;
- retain which quark emitted/absorbed the gluon;
- retain all fermionic permutation signs;
- have one authoritative source-to-target implementation and a generated
  Hermitian-conjugate target-to-source term;
- use one shared benchmark coupling owned by the Hamiltonian term, not by an
  observable;
- expose its limitations as `REDUCED_CANONICAL_INTERFACE_BENCHMARK`;
- remain disconnected from C5/C6 Wilson couplings and from physical state
  calibration.

Do not label this reduced H0 vertex as a complete physical light-front QCD
matrix element. The full spinor, instantaneous, counterterm, and
sector-renormalized vertex belongs to H2.

---

## 7. Required benchmarks

### H-A — Free-sector spectrum

For `qqq`, `qqqg`, and `qqqq-qbar` at multiple small deterministic
`HamiltonianResolution` points:

1. assemble the free invariant-mass matrix;
2. apply it matrix free;
3. compare both routes on basis vectors and random vectors;
4. verify Hermiticity;
5. verify exact block quantum numbers;
6. verify color-singlet and permutation constraints;
7. verify expected free degeneracies where the declared basis has them;
8. verify center-of-mass factorization and Lawson behavior;
9. record basis dimension, sparsity, residuals, and content hashes.

A free-spectrum match in a basis lacking one color multiplicity or correct
antisymmetry is a failure.

### H-B — One-vertex Hermiticity

Using the reduced benchmark vertex and its generated adjoint, verify

\[
\langle\phi|V_{3,4g}|\psi\rangle
 =
\langle V_{4g,3}\phi|\psi\rangle^*
\]

for every allowed basis block and for deterministic random superpositions.

Inject and detect:

- missing adjoint block;
- conjugation error;
- one-way regulator mismatch;
- wrong color generator;
- omitted permutation sign;
- erased octet-multiplicity label;
- violated longitudinal momentum conservation;
- violated \(J^z\) selection;
- source/target basis mismatch.

### H-C — Color and permutation completeness

For all retained sectors:

1. verify singlet multiplicities `1, 2, 3` for `qqq`, `qqqg`, and
   `qqqq-qbar`;
2. verify total-generator annihilation;
3. verify orthonormality;
4. verify supported recoupling matrices are unitary;
5. verify exact fermionic antisymmetry;
6. verify deterministic phase and ordering conventions;
7. omit each singlet channel one at a time and require completeness failure;
8. use the wrong antiquark generator and require failure;
9. use `qqq singlet x free gluon` and require failure;
10. violate antisymmetry across a cluster partition and require failure.

---

## 8. Readiness and isolation

Introduce an H0 readiness record with statuses no stronger than:

```text
BASIS_TYPES_VALIDATED
COLOR_MULTIPLICITIES_VALIDATED
PERMUTATION_BASIS_VALIDATED
CENTER_OF_MASS_GATE_VALIDATED
FREE_OPERATOR_VALIDATED
TERM_INTERFACE_VALIDATED
```

The following must remain false or unavailable:

```text
PHYSICAL_NUCLEON_EIGENSTATE
RENORMALIZATION_TRAJECTORY_VALIDATED
CURRENT_READY
GTMD_OVERLAP_READY
WILSON_READY_FROM_MICROSCOPIC_STATE
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
INFERENCE_READY
```

C7 objects must have a disjoint validation provenance root. They may have
read-only ancestry to C1 coordinate/operator identities and C3--C6 validation
objects, but no edge may make them reachable from:

- the accepted production root;
- the 216-route registry;
- the production resolved-parent builder;
- C5/C6 process or evolution gates;
- Volume IV nuclear composition;
- Volume V matching/evolution;
- Volume VI calibration or inference.

Importing the H0 package must have no production side effects.

---

## 9. Mandatory C7 negative injections

Add stable IDs and structured diagnostics for at least the following 48 H0
fault classes. These are in addition to all earlier C3--C6 injections.

1. use `P+ P-` instead of `2 P+ P-`;
2. alias oscillator scale `b` to a physical TMD width;
3. alias Hamiltonian resolution `lambda_H` to a rapidity scale;
4. use a TMD rapidity regulator as a vertex cutoff;
5. omit the zero-mode policy from the resolution identity;
6. use floating longitudinal modes where exact rational modes are required;
7. violate `sum k_i = K`;
8. permit a gluon zero mode under the declared nonzero-mode policy;
9. violate the `N_max` truncation;
10. compute the wrong total `Jz`;
11. serialize two distinct resolutions to one ID;
12. use nondeterministic basis ordering without recording the permutation;
13. duplicate a many-body basis state under two orderings;
14. omit the `qqq` singlet;
15. report more than one independent `qqq` singlet;
16. omit either `qqqg` singlet multiplicity;
17. replace the `qqqg` basis by `qqq singlet x free gluon`;
18. omit any of the three `qqqq-qbar` singlets;
19. use the fundamental rather than anti-fundamental antiquark generator;
20. violate total-generator annihilation;
21. accept a nonunitary color recoupling matrix;
22. erase a color-multiplicity label during serialization;
23. violate identical-quark antisymmetry;
24. antisymmetrize only after matrix assembly or diagonalization;
25. violate antisymmetry across a cluster partition;
26. use a non-idempotent or non-Hermitian antisymmetrizer;
27. omit center-of-mass factorization and the Lawson diagnostic;
28. mark a basis ready with CM residual above tolerance;
29. let an intrinsic level move with `beta_CM` beyond tolerance;
30. use an arbitrary diagonal free spectrum instead of the declared operator;
31. mismatch matrix-free and explicitly assembled free operators;
32. use a basis/effective mass as an MS-bar mass without matching;
33. include a Hamiltonian term without source/target sectors;
34. include a term without a parameter owner;
35. include a term without a regulator identity;
36. include `qqq -> qqqg` without its adjoint;
37. use different regulators in the two vertex directions;
38. use the wrong color generator in the benchmark vertex;
39. erase the emitting-quark identity;
40. omit a fermionic permutation sign in the vertex;
41. violate longitudinal momentum conservation in the vertex;
42. violate `Jz` conservation in the vertex;
43. label the reduced vertex as a complete physical QCD kernel;
44. attach a TMD-specific coupling or normalization to the vertex;
45. connect the H0 vertex directly to the C5/C6 physical phase identity;
46. promote an H0 basis or matrix into the accepted production root;
47. mutate any authoritative artifact, production registry, provenance graph,
    or composition plan;
48. modify any Volume 0--VII normative source during implementation.

Also preserve and rerun every existing C3--C6 injection suite.

---

## 10. Tests and quantitative tolerances

Use exact arithmetic for discrete labels and group-theory counts wherever
possible. Use floating tolerances only for normalized tensors, sparse matrices,
and numerical integration.

Declare tolerances in one machine-readable manifest. At minimum report:

```text
max color-generator residual
max color orthonormality residual
max recoupling-unitarity residual
max permutation residual
max antisymmetrizer idempotence residual
max antisymmetrizer Hermiticity residual
max CM factorization residual
max Lawson intrinsic-level drift
max free-operator Hermiticity residual
max matrix-free/assembled residual
max independent-quadrature residual
max one-vertex Hermiticity residual
```

Do not broaden tolerances to hide a structural failure. If an analytic count or
identity is exact, test it exactly.

---

## 11. Required documentation and machine-readable deliverables

Create at least:

```text
docs/next_level/c7_implementation_report.md
docs/next_level/c7_api.md
docs/next_level/c7_requirement_coverage.json
docs/next_level/c7_normative_source_integration.json
docs/next_level/c7_basis_manifest.json
docs/next_level/c7_color_permutation_manifest.json
docs/next_level/c7_free_spectrum_manifest.json
docs/next_level/c7_vertex_manifest.json
docs/next_level/c7_injection_manifest.json
docs/next_level/c7_regression_report.json
```

Add architecture-decision records for:

```text
HamiltonianResolution and scale separation
exact longitudinal-mode representation
complete SU(3) singlet multiplicities
fermionic antisymmetry strategy
center-of-mass factorization policy
reduced H0 qqq<->qqqg vertex boundary
H0 isolation from production and C5/C6 dynamics
```

Update the persistent roadmap/handoff with:

- C7 starting commit;
- final local commit;
- source hashes;
- exact implemented APIs;
- benchmark residuals;
- basis dimensions at every benchmark resolution;
- unresolved H1/H2 physics;
- exact recommended next package.

All JSON output must be deterministic, schema validated, and stable under a
second clean generation.

---

## 12. Final acceptance gates

C7/H0 is complete only when all of the following hold:

1. The C6 baseline reproduces before edits.
2. Volumes 0--VII are indexed and source-hash audited.
3. `HamiltonianResolution` and every scale identity fail closed.
4. Exact rational longitudinal modes and the declared `K`/`N_max` rules are
   implemented.
5. Complete color-singlet multiplicities are obtained: `1, 2, 3`.
6. All color tensors pass generator, orthonormality, and recoupling tests.
7. Exact fermionic antisymmetry is imposed before matrix assembly.
8. Center-of-mass factorization and Lawson diagnostics pass.
9. H-A passes in all retained sectors.
10. H-B passes for all tested blocks and random superpositions.
11. H-C passes, including deliberate omitted-channel failures.
12. All C7 negative injections pass.
13. All C3--C6 injection suites still pass.
14. The full repository test suite passes.
15. All nine builders pass.
16. All 36 evidence rows pass.
17. All 162 atlas pages render.
18. The 216-route production registry is unchanged.
19. Production provenance and composition are unchanged.
20. All eight authoritative artifacts remain byte-identical.
21. C5/C6 manifests and residuals remain unchanged.
22. No H0 object is reachable from production, nuclear, evolution, process, or
    inference roots.
23. No physical nucleon, GTMD, TMD, or continuum-QCD claim is made.
24. The working tree is clean after one local completion commit.
25. Nothing is pushed.

---

## 13. Final response format

Report:

- starting commit and final local commit;
- whether anything was pushed;
- full test, builder, evidence, atlas, and injection counts;
- exact singlet multiplicities obtained in each sector;
- maximum color, permutation, CM, free-operator, and vertex residuals;
- benchmark basis dimensions and sparse-matrix sizes;
- files and APIs created;
- confirmation that all production artifacts and C5/C6 manifests are
  unchanged;
- explicit limitations and readiness statuses;
- exact next recommended package.

Do not declare C7 complete unless every acceptance gate passes.

### Recommended next package after successful C7

The default next Hamiltonian package should be:

```text
C8/H1 — valence-sector Hamiltonian and renormalization-flow benchmark
```

It should add the first `qqq` interaction/induced-confinement trajectories,
current operators, small-tower diagonalization, state tracking, and mass/current
flow, while remaining explicitly valence-only.

The C6 second-order Dyson/Magnus Wilson-convergence package remains deferred
until the microscopic `qqqg` state and the additional higher sectors required
by second Wilson order are present. It should not be implemented by deepening
only the analytic C6 pilot.
