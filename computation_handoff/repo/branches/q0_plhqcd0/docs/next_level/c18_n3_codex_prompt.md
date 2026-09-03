# C18/N3 Codex Work Package

## Title

**C18/N3 — Explicit \(\Delta\Delta\) and compact six-quark dynamics, hidden-color basis completion, transition currents, and count-once non-nucleonic deuteron composition**

## Authoritative baseline

Use the completed C17/N2 commit as the scientific and regression baseline:

```text
55ce70210121735a70f8b4124606274609732be8
```

A documentation-only descendant is acceptable only when this commit is in its ancestry and the complete C17 baseline reproduces before any scientific code is changed.

Do not use `origin/main` as the scientific baseline if it does not contain this commit. Nothing in this package may be pushed remotely.

## Normative sources

Read the following repository sources completely before implementation and record their exact SHA-256 hashes in the C18 normative-source manifest:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/model_construction_note.tex
references/volume_iv_matched_spin1_nuclear_dynamics.tex
references/volume_xii_microscopic_wilson_second_order.tex
references/volume_xiii_nnpi_pion_matching_coherent_nuclear.tex
references/volume_xiv_continuum_nnpi_exchange_currents.tex
```

Also read and reuse, rather than duplicate, the implemented APIs and manifests from C14–C17, especially:

```text
docs/next_level/c14_api.md
docs/next_level/c15_api.md
docs/next_level/c16_api.md
docs/next_level/c17_api.md
docs/next_level/c17_implementation_report.md
```

If a requested normative source is absent, do not invent its contents. Record the absence and proceed only from the equations and requirements explicitly contained in this work package and the available source tree.

## High-level objective

Extend the continuum-calibrated N2 nuclear validation state

\[
\mathcal H_{\mathrm{N2}}
=
\mathcal H_{NN}
\oplus
\mathcal H_{NN\pi}^{\mathrm{cont}}
\]

to the first sector-resolved non-nucleonic N3 state

\[
\boxed{
\mathcal H_{\mathrm{N3}}
=
\mathcal H_{NN}
\oplus
\mathcal H_{NN\pi}^{\mathrm{cont}}
\oplus
\mathcal H_{\Delta\Delta}
\oplus
\mathcal H_{6q}^{\mathrm{compact}}
}
\]

with:

1. a complete spin/isospin/orbital \(\Delta\Delta\) sector;
2. an exactly antisymmetrized six-quark color-singlet sector;
3. an explicit distinction between the cluster-singlet and hidden-color bases;
4. count-once matching between hadronic cluster sectors and the compact six-quark description;
5. Hamiltonian-consistent electromagnetic, axial, EMT, and partonic transition operators;
6. normalized diagonal and interference contributions to the microscopic deuteron GTMD parent;
7. upgraded helicity-resolved coherent and tensor diagnostics;
8. exact/full-bond/reduced-bond tensor-network convergence;
9. complete production isolation and unchanged accepted artifacts.

This package is the first explicit non-nucleonic nuclear-sector benchmark. It remains finite-resolution, validation-only, unmatched, unevolved, and disconnected from production.

## Scientific nonclaims

C18 must not claim:

```text
PHYSICAL_DELTADELTA_PROBABILITY
PHYSICAL_HIDDEN_COLOR_PROBABILITY
PHYSICAL_SIX_QUARK_DISTRIBUTION
PHYSICAL_DEUTERON_TMD
PHYSICAL_SHADOWING_READY
NUCLEAR_GLAUBER_READY
COMPLETE_CHIRAL_EFT
FULL_CONTINUUM_NONNUCLEONIC_THEORY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_READY
```

The \(\Delta\Delta\), compact-six-quark, and hidden-color amplitudes are resolution- and representation-dependent components of one validation state. Hidden color is not an independently additive physical sector.

---

# 1. Immutable regression baseline

Before making changes, reproduce and record:

- all **1,000** existing tests;
- all existing C17 builders and architecture validators;
- all **36/36** evidence rows;
- all **162/162** atlas pages;
- all **614** C17 requirements;
- all **340** C17 negative injections;
- every earlier C3–C16 injection suite;
- the accepted production registry at exactly **216 routes**;
- all eight authoritative production artifact hashes;
- all C15, C16, and C17 generated manifests byte-for-byte;
- a clean working tree.

No C18 object may alter the accepted production composition, production provenance, accepted registry, canonical parents, or any prior microscopic validation root.

---

# 2. Required package isolation

Create the N3 implementation under an isolated package such as

```text
src/deuteron_wigner/nuclear/n3/
```

or an equivalent location that cannot be imported by production through side effects.

The C18 provenance root must be disjoint from production. It may have read-only ancestry to C14–C17 objects but no route to:

```text
PRODUCTION_ROOT
MATCHING_ROOT
EVOLUTION_ROOT
PROCESS_ROOT
INFERENCE_ROOT
```

All new parameter values and state amplitudes must be marked `VALIDATION_ONLY`.

---

# 3. N3 assumption plans

Implement immutable, content-addressed plans. At minimum:

```text
N3-PLAN-A
    N2 NN + continuum NNPI
    explicit DELTADELTA
    compact six-quark absent

N3-PLAN-B
    N2 NN + continuum NNPI
    compact six-quark with cluster/hidden-color decomposition
    explicit DELTADELTA integrated out or absent

N3-PLAN-C
    N2 NN + continuum NNPI
    explicit DELTADELTA
    orthogonal compact six-quark complement
    explicit count-once cluster matching

N2-REFERENCE
    immutable C17 state
    no DELTADELTA
    no compact six-quark
```

The plans are alternative complete theories at this truncation. They may be compared, but they may never be summed.

`N3-PLAN-C` may include both \(\Delta\Delta\) and compact six-quark amplitudes only after the cluster overlap has been removed by an explicit orthogonalization or subtraction map. The compiler must reject a naive direct sum that double counts the same cluster state.

---

# 4. Explicit \(\Delta\Delta\) sector

## 4.1 Quantum numbers

Construct a typed \(\Delta\Delta\) light-front sector with

```text
BARYON_NUMBER = 2
TOTAL_CHARGE = +1
TOTAL_ISOSPIN = 0
TOTAL_J = 1
TOTAL_PARITY = +
```

The charge-complete \(I=0\) basis must be generated by exact Clebsch–Gordan coupling from

```text
Delta++ Delta-
Delta+  Delta0
Delta0  Delta+
Delta-  Delta++
```

rather than by an unverified hand-entered sign pattern.

## 4.2 Exchange symmetry

Each \(\Delta\) is a spin-\(3/2\), isospin-\(3/2\) fermion. The complete two-\(\Delta\) state must be antisymmetric under interchange.

At the declared positive-parity truncation with even relative \(L\) and \(I=0\), retain the allowed odd-spin channels. The initial required partial-wave basis is

```text
3S1
3D1
7D1
```

with higher even-\(L\) channels typed unavailable unless explicitly implemented.

The code must derive and test the exchange parity of every spin, isospin, and orbital block. It may not enforce antisymmetry only after matrix assembly.

## 4.3 Continuum status

Represent the \(\Delta\Delta\) branch by a typed spectral record. At the deuteron pole, physical absorptive support must vanish below the declared \(\Delta\Delta\) threshold. A numerical width or \(i\epsilon\) cannot create physical support.

Allow a stable-\(\Delta\) analytic oracle and a continuum/discretized spectral route, but preserve their distinction in operator identity and provenance.

---

# 5. Compact six-quark sector and hidden color

## 5.1 Exact color singlet multiplicity

Derive the color-singlet subspace as the common nullspace of the total SU(3) generators in

\[
3^{\otimes 6}.
\]

The required multiplicity is

\[
\boxed{
\dim\operatorname{Inv}_{SU(3)}(3^{\otimes6})=5
}
\]

and corresponds to the \(S_6\) Young symmetry \([2,2,2]\) in color.

The implementation must retain all five orthonormal color-singlet multiplicities with deterministic phase and recoupling conventions.

## 5.2 Cluster and hidden-color bases

For a declared \(3+3\) cluster partition, identify one color-singlet-times-color-singlet cluster vector and a four-dimensional orthogonal complement.

The four-dimensional complement may be called a hidden-color basis, but:

- hidden color is a basis decomposition inside \(\mathcal H_{6q}^{\mathrm{compact}}\), not an independently additive Fock sector;
- its individual basis probabilities are convention and resolution dependent;
- unitary rotations within the hidden-color subspace must leave all complete observables invariant;
- no hidden-color probability may be fitted directly to one TMD.

Implement at least two unitary hidden-color basis choices and prove basis-invariant complete matrix elements.

## 5.3 Full six-quark antisymmetry

Impose exact signed \(S_6\) antisymmetry before Hamiltonian or operator assembly.

The implementation must preserve exchange signs across all quark labels:

```text
flavor
color
helicity
longitudinal mode
transverse/orbital mode
cluster partition
```

A product of two separately antisymmetric three-quark clusters is not sufficient for the compact six-quark sector.

## 5.4 Physical quantum numbers

The retained six-quark basis must carry

```text
B = 2
Q = +1
I = 0
J^P = 1+
```

and explicit longitudinal, transverse, OAM, spin, permutation, color-multiplicity, regulator, resolution, and assumption-plan identities.

---

# 6. Cluster matching and count-once composition

The hadronic \(NN\), \(\Delta\Delta\), and microscopic six-quark descriptions overlap in cluster regions. C18 must make this overlap executable.

## 6.1 Cluster embedding

Implement typed embeddings

\[
V_{NN\to6q},
\qquad
V_{\Delta\Delta\to6q}
\]

that map the hadronic cluster states into the full six-quark Hilbert space, including spin, isospin, orbital, color, and permutation structure.

Construct the Gram matrix of the embedded cluster states and an orthogonal projector

\[
P_{\mathrm{cluster}}
\]

onto their span.

Define the compact complement

\[
Q_{\mathrm{compact}}=I-P_{\mathrm{cluster}}.
\]

In `N3-PLAN-C`, only the orthogonal compact complement may be added directly to the explicit hadronic sectors.

## 6.2 Alternative matched representation

Also implement a subtraction representation,

\[
W_{\mathrm{matched}}
=
W_{NN}
+
W_{\Delta\Delta}
+
W_{6q}
-
W_{\mathrm{cluster\ overlap}},
\]

and verify agreement with the orthogonal-complement route within the declared numerical and truncation tolerance.

## 6.3 Provenance rules

The provenance complex must represent:

```text
EXPLICIT_DELTADELTA
    ALTERNATIVE_TO
INDUCED_DELTADELTA_CONTACT

EXPLICIT_SIX_QUARK
    ALTERNATIVE_TO
INDUCED_SHORT_RANGE_OPERATOR

HIDDEN_COLOR_BASIS
    MEMBER_OF
SIX_QUARK_COLOR_SINGLET_SPACE

HADRONIC_CLUSTER_SUBSPACE
    OVERLAPS_WITH
SIX_QUARK_CLUSTER_SUBSPACE

ORTHOGONAL_COMPACT_COMPLEMENT
    COUNT_ONCE_WITH
EXPLICIT_NN_AND_DELTADELTA
```

The compiler must reject:

- explicit \(\Delta\Delta\) plus its fully induced replacement;
- explicit six-quark plus its fully induced short-range replacement;
- hidden color as an independent additive probability sector;
- full six-quark plus explicit cluster sectors without orthogonalization or overlap subtraction;
- duplicate overlap subtraction.

A visible remainder must be retained in every explicit-versus-induced comparison.

---

# 7. Coupled N3 Hamiltonian

Construct the sector matrix

\[
H_{\mathrm{N3}}
=
\begin{pmatrix}
H_{NN} & V_{NN\leftarrow NN\pi} & V_{NN\leftarrow\Delta\Delta} & V_{NN\leftarrow6q}\\
V_{NN\pi\leftarrow NN} & H_{NN\pi} & V_{NN\pi\leftarrow\Delta\Delta} & V_{NN\pi\leftarrow6q}\\
V_{\Delta\Delta\leftarrow NN} & V_{\Delta\Delta\leftarrow NN\pi} & H_{\Delta\Delta} & V_{\Delta\Delta\leftarrow6q}\\
V_{6q\leftarrow NN} & V_{6q\leftarrow NN\pi} & V_{6q\leftarrow\Delta\Delta} & H_{6q}
\end{pmatrix}.
\]

Only physically supported blocks need be nonzero, but every unsupported block must carry a typed reason such as:

```text
FORBIDDEN_BY_QUANTUM_NUMBERS
BEYOND_DECLARED_ORDER
INDUCED_ONLY_AT_THIS_RESOLUTION
NOT_IMPLEMENTED_BLOCKS_COMPLETENESS_STATUS
```

Every nonzero off-diagonal block must have a generated Hermitian adjoint. The assembled and matrix-free Hamiltonians must agree.

The retained C17 continuum \(NN\pi\) self-energy, pole/residue, separator flow, and current basis must remain unchanged unless a declared N3 coupling requires a consistently transformed extension.

---

# 8. Renormalization and calibration discipline

Implement an N3 renormalization trajectory over at least three resolution points.

The calibration set may include only a restricted shared set such as:

- deuteron pole or binding condition;
- charge normalization;
- one \(NN\leftrightarrow\Delta\Delta\) transition condition;
- one \(NN/\Delta\Delta\leftrightarrow6q\) short-range condition;
- one current-continuity condition.

Keep as holdouts:

- a second transition point;
- magnetic and quadrupole combinations;
- one angular condition;
- \(b_1\) or another tensor observable;
- one hidden-color-sensitive but basis-invariant observable;
- one compact-sector quark moment;
- one coherent tensor observable;
- one nonzero-transfer current;
- one separator or recoupling variation.

Do not fit \(Z_{\Delta\Delta}\), \(Z_{6q}\), hidden-color basis weights, or any named TMD directly.

Expose all Jacobian null directions and parameter correlations. Sector probabilities are diagnostics, not measured observables.

---

# 9. Hamiltonian-consistent currents and local operators

Extend the C17 declared-order completeness certificate to include every retained N3 Hamiltonian term.

The current/operator basis must include, where generated by the selected plan:

```text
DELTADELTA_ELASTIC_CURRENT
NN_TO_DELTADELTA_TRANSITION_CURRENT
DELTADELTA_TO_NN_TRANSITION_CURRENT
SIX_QUARK_ONE_BODY_CURRENT
SIX_QUARK_INTERACTION_CURRENT
NN_TO_SIX_QUARK_TRANSITION_CURRENT
DELTADELTA_TO_SIX_QUARK_TRANSITION_CURRENT
CLUSTER_OVERLAP_SUBTRACTION_CURRENT
REGULATOR_GAUGING_CURRENT
INDUCED_FESHBACH_CURRENT
CURRENT_COUNTERTERM
AXIAL_TRANSITION_PARTNERS
PSEUDOSCALAR_TRANSITION_PARTNERS
EMT_INTERACTION_TERMS
PARTONIC_OPERATOR_TRANSITION_BLOCKS
```

For each Hamiltonian term, the completeness certificate must identify:

1. all required current attachments;
2. all required charge-density terms;
3. all required EMT or partonic-operator partners;
4. whether the term is neutral;
5. whether a gap remains.

Any unexplained retained-Hamiltonian gap blocks the status `N3_DECLARED_ORDER_CURRENT_BASIS_COMPLETE`.

Test the continuity identity blockwise for every supported sector pair. A cancellation that appears only after summing incompatible sectors is not sufficient.

---

# 10. N3 partonic operators and deuteron GTMD parent

Construct the full sector-resolved operator matrix

\[
\widehat{\mathcal O}_{a}^{\mathrm{N3}}
=
\left(
\widehat{\mathcal O}_{a,\alpha\beta}
\right)_{\alpha,\beta\in\{NN,NN\pi,\Delta\Delta,6q\}}.
\]

The complete parent is

\[
W_{a/D}^{\mathrm{N3}}
=
\sum_{\alpha,\beta}
\langle\Psi_{\alpha}|
\widehat{\mathcal O}_{a,\alpha\beta}
|\Psi_{\beta}\rangle.
\]

It must retain:

- all three deuteron helicities;
- parton helicity or gluon transverse indices;
- species and flavor;
- source and target nuclear sectors;
- diagonal or transition ancestry;
- Wilson order, ordered gluon links, and \(f/d\) class;
- microscopic proton/neutron member;
- \(\Delta\Delta\) member;
- six-quark color multiplicity and cluster/hidden-color basis;
- regulator, resolution, assumption plan, and separator identity.

## 10.1 \(\Delta\)-sector parton parent

Implement a validation-only spin-\(3/2\) \(\Delta\) parton-parent interface sufficient to build the declared \(\Delta\Delta\) diagonal and transition blocks. It must retain all four \(\Delta\) helicities and explicit charge/isospin identity.

Do not label it a physical \(\Delta\) GTMD or TMD unless an LF-to-QCD matching route is later supplied.

## 10.2 Six-quark parton parent

Direct quark one-body operators are explicit in the six-quark sector. Antiquark and gluon contributions remain unavailable or induced-with-remainder unless the corresponding higher six-quark Fock support is implemented.

The support manifest must distinguish:

```text
DIRECT_SIX_QUARK_QUARK_OPERATOR
INDUCED_SIX_QUARK_GLUON_OPERATOR_WITH_REMAINDER
ANTIQUARK_UNAVAILABLE_AT_SIX_QUARK_ONLY_ORDER
```

No missing partonic species may be reported as a physical zero.

## 10.3 Transition operators

Retain all supported

```text
NN <-> DELTADELTA
NN <-> SIX_QUARK
DELTADELTA <-> SIX_QUARK
```

partonic transition blocks. Their interference may be signed and cannot be represented as probabilities.

---

# 11. Spin-1 tensor, \(b_1\), and exotic-channel diagnostics

Project only after full sector composition onto

\[
U,\quad L,\quad T,\quad LL,\quad LT,\quad TT.
\]

Preserve the convention-stable tensor difference

\[
\delta_TF
=
F_{\Lambda=0}
-
\frac12(F_{\Lambda=+1}+F_{\Lambda=-1}),
\]

and apply the named adapter

\[
f_{1LL}=-\frac23\delta_T f_1
\]

only afterward.

Compute and report separately:

```text
NN contribution
NNPI contribution
DELTADELTA contribution
SIX_QUARK cluster contribution
SIX_QUARK hidden-color contribution
all allowed transition/interference contributions
matched total
```

The hidden-color subtotal is basis dependent and may be shown only as a diagnostic. The complete six-quark and full matched observables must be invariant under hidden-color basis rotations.

Do not fit an independent \(b_1\), tensor-TMD, gluon-transversity, or hidden-color normalization.

Include at least one validation channel in which the one-body nucleon baseline is suppressed and the \(\Delta\Delta\), compact, or coherent sector produces the leading nonzero tensor signal.

---

# 12. Upgraded coherent amplitude

Extend the C17 helicity-resolved coherent pilot to allow typed \(\Delta\Delta\) and compact-sector intermediate channels:

\[
\delta W_{\Lambda'\Lambda}^{\mathrm{coh,N3}}
=
\sum_{X\in\{NN\pi,\Delta\Delta,6q,\ldots\}}
\mathcal A_{\Lambda'\to X}^{*}
\mathcal G_X
\mathcal A_{\Lambda\to X}.
\]

Retain channel, helicity, longitudinal ordering, propagation phase, threshold, spectral support, and sector identity.

Required exact limits:

- zero when either elementary amplitude vanishes;
- zero when the selected intermediate channel is removed;
- reversal under longitudinal-order exchange where applicable;
- distinct scalar/vector/tensor projections;
- failure of a copied unpolarized ratio;
- no tracing before coherent amplitudes are combined;
- count-once overlap with the explicit sector amplitudes.

This remains an analytic continuum pilot, not physical shadowing or nuclear Glauber dynamics.

---

# 13. Completely positive reduction

Derive CP maps only after all resolved \(NN\), \(NN\pi\), \(\Delta\Delta\), six-quark, and coherent amplitudes have been combined.

The implementation must demonstrate that an early partial trace destroys at least one real transition or hidden-color interference observable.

Hidden-color basis rotations must not alter the Choi spectrum or complete reduced observable.

---

# 14. N3 tensor-network implementation

Extend the nuclear state tensor network to four primary branches:

```text
NN_BRANCH
NNPI_CONTINUUM_BRANCH
DELTADELTA_BRANCH
SIX_QUARK_BRANCH
```

The \(\Delta\Delta\) branch must retain:

```text
Delta helicities
I=0 charge coupling
S=1,3
L=0,2
J=1
exchange parity
continuum/stable-oracle identity
```

The six-quark branch must retain:

```text
five color-singlet multiplicities
cluster versus hidden-color decomposition
exact S6 permutation identity
spin/flavor/isospin/OAM labels
resolution and regulator
```

Full bond must reproduce exact/Krylov results. Reduced-bond studies must report loss in:

- \(Z_{\Delta\Delta}\);
- \(Z_{6q}\);
- transition-current matrix elements;
- quadrupole and \(b_1\) signals;
- basis-invariant hidden-color-sensitive observables;
- coherent tensor amplitudes;
- cluster-overlap subtraction;
- current-continuity residuals.

At least one low-bond state must retain a deceptively small energy or norm defect while losing a substantial non-nucleonic tensor or current signal.

---

# 15. N3 ledgers

The state must close

\[
Z_{NN}+Z_{NN\pi}+Z_{\Delta\Delta}+Z_{6q}=1,
\]

with independent ledgers for:

```text
charge
baryon number
isospin
parity
plus momentum
Jz
sector probability
cluster overlap
current continuity
EMT momentum
partonic number/momentum
spin-1 tensor normalization
```

Hidden-color basis weights are not added as a separate normalization line. They sum internally within \(Z_{6q}\).

---

# 16. Required analytic and finite benchmarks

Implement at least the following benchmark families with stable IDs:

```text
N3-A  DeltaDelta isospin/charge Clebsch closure
N3-B  DeltaDelta exchange symmetry and partial waves
N3-C  Six-quark color-singlet multiplicity five
N3-D  Exact S6 antisymmetry
N3-E  Cluster/hidden-color basis rotation invariance
N3-F  Cluster embedding and orthogonal compact complement
N3-G  Orthogonal-complement versus subtraction equivalence
N3-H  Coupled Hamiltonian Hermiticity and matrix-free action
N3-I  Pole/threshold behavior for closed DeltaDelta channel
N3-J  Current-basis completeness and blockwise continuity
N3-K  Direct/induced operator equivalence with remainder
N3-L  Complete sector-summed GTMD parent closure
N3-M  b1 and tensor-interference decomposition
N3-N  Coherent DeltaDelta/six-quark pilot
N3-O  CP reduction after coherence
N3-P  Exact/Krylov/full-bond TTN agreement
N3-Q  Observable-sensitive reduced-bond loss
N3-R  Assumption-plan compiler and count-once provenance
```

Add further benchmarks where the implemented architecture requires them.

---

# 17. Mandatory negative injections

Create at least **400** new ordered C18 fault injections with stable IDs and structured diagnostics. Cover at minimum:

## DeltaDelta

- incomplete charge basis;
- wrong \(I=0\) Clebsch signs;
- forbidden even-spin channel for even \(L\);
- broken exchange antisymmetry;
- wrong parity;
- missing partial-wave multiplicity;
- physical cut below threshold;
- numerical epsilon promoted to physical width.

## Six-quark color and statistics

- color singlet count not equal to five;
- dropped color multiplicity;
- nonorthogonal color basis;
- wrong total-generator action;
- broken S6 antisymmetry;
- cluster-only antisymmetry;
- hidden color added as a separate Fock sector;
- hidden-color basis rotation changes a complete observable;
- cluster vector missing from the five-dimensional space.

## Matching and provenance

- explicit DeltaDelta plus induced Delta contact;
- explicit six-quark plus induced SRC/contact replacement;
- full six-quark plus NN/DeltaDelta without overlap removal;
- missing overlap subtraction;
- duplicate overlap subtraction;
- hidden-color probability fitted directly;
- explicit/induced comparison with no remainder;
- invalid cross-plan addition.

## Hamiltonian and currents

- missing generated adjoint;
- matrix-free mismatch;
- unexplained current-basis gap;
- omitted transition current;
- omitted cluster-subtraction current;
- blockwise continuity failure hidden by total cancellation;
- wrong regulator-gauging current;
- current from a different Hamiltonian plan;
- independent current normalization per sector.

## Partonic operators

- scalar smearing substituted for helicity matrix;
- missing Delta helicity state;
- missing six-quark color multiplicity;
- unsupported antiquark/gluon six-quark output declared zero;
- transition interference clipped or made positive;
- Wilson order/link/color identity lost;
- proton/neutron microscopic members mixed;
- tensor sign inferred from name.

## Coherent and CP

- copied unpolarized shadowing ratio;
- early partial trace;
- missing channel identity;
- partonic Wilson phase aliased to nuclear propagation;
- duplicate coherent/explicit sector contribution;
- hidden-color basis changes Choi spectrum.

## TTN and convergence

- full-bond mismatch;
- missing DeltaDelta branch;
- missing six-quark color multiplicity;
- low-bond observable loss hidden by energy;
- recoupling nonunitarity;
- wrong fermionic swap ledger;
- convergence axes combined into one band.

## Readiness and isolation

- physical DeltaDelta probability claim;
- physical hidden-color probability claim;
- physical TMD claim;
- production registry mutation;
- production provenance edge;
- matching/evolution/process/inference promotion;
- normative-source mutation;
- authoritative-artifact mutation.

Every injected fault must be detected before or at the mathematically appropriate stage. No test may pass merely because the affected amplitude was numerically zero.

---

# 18. Required deliverables

Create deterministic, machine-readable deliverables including at least:

```text
docs/next_level/c18_implementation_report.md
docs/next_level/c18_api.md
docs/next_level/c18_requirement_coverage.json
docs/next_level/c18_injection_manifest.json
docs/next_level/c18_regression_report.json
docs/next_level/c18_normative_source_integration.json
docs/next_level/c18_assumption_plans.json
docs/next_level/c18_delta_delta_manifest.json
docs/next_level/c18_six_quark_color_manifest.json
docs/next_level/c18_hidden_color_basis_manifest.json
docs/next_level/c18_cluster_matching_manifest.json
docs/next_level/c18_hamiltonian_manifest.json
docs/next_level/c18_current_completeness_certificate.json
docs/next_level/c18_continuity_report.json
docs/next_level/c18_partonic_parent_manifest.json
docs/next_level/c18_tensor_b1_manifest.json
docs/next_level/c18_coherent_manifest.json
docs/next_level/c18_cp_reduction_manifest.json
docs/next_level/c18_ttn_convergence_manifest.json
docs/next_level/c18_provenance_complex.json
docs/next_level/c18_unresolved_physics_gaps.md
```

Update `handoff/ROADMAP.md` with:

- final commit;
- achieved status;
- exact unresolved gates;
- the next recommended package.

All generated JSON must reproduce byte-for-byte on rebuild.

---

# 19. Acceptance criteria

C18/N3 is complete only when all of the following hold:

1. The full C17 baseline reproduces before edits.
2. The \(\Delta\Delta\) charge/isospin/spin/orbital basis is complete at the declared scope.
3. The two-\(\Delta\) Pauli constraint passes exactly.
4. The six-quark color-singlet multiplicity is exactly five.
5. Exact six-quark antisymmetry passes.
6. Hidden-color basis rotations leave complete observables invariant.
7. Cluster embeddings and Gram projectors are explicit.
8. Orthogonal-complement and subtraction routes agree within tolerance.
9. No hadronic/compact double counting survives the provenance gates.
10. The coupled Hamiltonian is Hermitian and assembled/matrix-free actions agree.
11. Exact and Krylov eigenstates agree within tolerance.
12. Full-bond TTN reproduces the exact state and principal observables.
13. Reduced-bond non-nucleonic observable loss is reported honestly.
14. Normalization, charge, baryon, isospin, parity, plus-momentum, and \(J^z\) ledgers close.
15. The declared-order current completeness certificate has no unexplained retained-Hamiltonian gap.
16. Continuity closes blockwise in every supported sector pair.
17. The full sector-summed deuteron GTMD parent closes its regulated reductions.
18. \(b_1\), tensor, current, and EMT routes use the common parent with no named-function normalization.
19. Hidden-color and transition pieces remain signed amplitude contributions, not probabilities.
20. Coherent amplitudes are combined before any CP trace.
21. The CP/Kraus reduction closes after coherence.
22. Explicit-versus-induced comparisons retain visible remainders.
23. All new and inherited negative injections pass.
24. The accepted 216-route production registry is unchanged.
25. All eight authoritative artifacts remain byte-identical.
26. All C15–C17 manifests remain byte-identical.
27. All C18 manifests rebuild byte-for-byte.
28. The working tree is clean.
29. A final local commit is created.
30. Nothing is pushed.

---

# 20. Allowed readiness statuses

The strongest permitted statuses are:

```text
N3_DELTADELTA_BASIS_VALIDATED
N3_DELTADELTA_CONTINUUM_ORACLE_VALIDATED
N3_SIX_QUARK_COLOR_BASIS_VALIDATED
N3_SIX_QUARK_ANTISYMMETRY_VALIDATED
N3_HIDDEN_COLOR_BASIS_INVARIANCE_VALIDATED
N3_CLUSTER_MATCHING_VALIDATED
N3_COUPLED_STATE_VALIDATED
N3_DECLARED_ORDER_CURRENT_BASIS_COMPLETE
N3_BLOCKWISE_CONTINUITY_CLOSED
N3_NONNUCLEONIC_PARTONIC_PARENT_VALIDATED_UNMATCHED
N3_TENSOR_AND_B1_DECOMPOSITION_VALIDATED
N3_COHERENT_NONUCL_PILOT_VALIDATED
N3_TTN_CONVERGENCE_VALIDATED
N3_VALIDATION_ONLY
```

The forbidden statuses listed under Scientific nonclaims remain forbidden.

---

# 21. Expected next package

If C18 closes the \(\Delta\Delta\), compact-six-quark, cluster-matching, current, tensor, and coherent gates, the preferred next package is:

> **C19/M0 — light-front-to-QCD operator matching pilot for the complete microscopic nucleon and deuteron parent, including a closed regulated operator basis, small-\(b\) matching, ultraviolet/rapidity/soft scheme identity, and first common-scheme rank-aware evolution tests.**

If C18 instead exposes a large unresolved cluster-overlap, current, or six-quark partonic-operator defect, recommend a narrower N3-completion package before beginning matching.

## Final response required from Codex

Summarize:

- baseline and final commit;
- tests, builders, evidence, atlas, requirements, and injections;
- sector dimensions and probabilities;
- \(\Delta\Delta\) basis and exchange residuals;
- six-quark color and antisymmetry residuals;
- hidden-color basis-invariance residual;
- cluster-overlap and subtraction residuals;
- current-completeness and block-continuity status;
- principal tensor/\(b_1\)/coherent results;
- TTN convergence and observable loss;
- explicit/induced remainders;
- immutable production status;
- exact unresolved gates;
- exact recommended next package.

Do not declare physical hidden-color content, a physical deuteron TMD, physical shadowing, or QCD matching readiness.
