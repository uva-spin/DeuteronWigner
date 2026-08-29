# C11/H4 Codex Work Package

## Title

**C11/H4 — Microscopic nonzero-transfer quark, antiquark, and gluon GTMD helicity matrices; complete T-even projector closure; local-current, EMT, Wigner, and OAM consistency; and controlled replacement of the C3/C4 analytic common-parent pilots**

## Authoritative baseline

Begin from the local C10/H3 completion commit:

```text
b37a21245905629259bdebcdb9d1c6aebc4f073c
```

The C10 commit must remain in the ancestry of the final C11 commit. The repository is intentionally ahead of `origin/main`; do **not** reset to, rebase onto, or replace the local scientific history with the remote branch.

A documentation-only descendant is acceptable before code changes if it only adds or indexes the verified normative sources listed below and leaves all executable artifacts unchanged.

Do not push. Complete C11 locally, create one final local commit, and leave a clean working tree.

## Primary scientific objective

Use the completed common microscopic H3 eigenstate

\[
\mathcal H_{\mathrm{H3}}
=
\mathcal H_{qqq}
\oplus
\mathcal H_{qqqg}
\oplus
\mathcal H_{qqqu\bar u}
\oplus
\mathcal H_{qqqd\bar d}
\]

to construct the first **microscopic nonzero-transfer, zero-skewness GTMD parent** for quarks, antiquarks, and gluons from one interacting state bundle.

C11 must implement, validate, and cross-check:

1. typed incoming and outgoing nucleon momentum fibers at \(\xi=0\) and nonzero \(\bm\Delta_T\);
2. one authoritative symmetric-frame intrinsic recoil map for every active and spectator parton;
3. continuous momentum-space evaluation of the finite BLFQ/TTN state amplitudes at recoil-shifted intrinsic coordinates;
4. complete joint target–parton helicity matrices for \(u,d,\bar u,\bar d\), and the active gluon;
5. the complete sixteen-function twist-two quark GTMD projector system for every quark and antiquark flavor;
6. a complete generated leading-twist gluon GTMD tensor/helicity basis with trace, helicity-antisymmetric, and symmetric-traceless polarization sectors;
7. exact Hermiticity, parity, transfer reversal, and zeroth-rescattering time-reversal/link-parity tests;
8. forward TMD limits, regulated GPD/PDF limits, and local vector, axial, and energy–momentum moment closure from the same parent;
9. Wigner-space and transfer-derivative OAM/spin–orbit routes consistent with the direct H3 canonical ledgers;
10. forward Gram positivity and off-forward Cauchy–Schwarz bounds at their correct layers;
11. resolution-, Fock-, quadrature-, and TTN-bond convergence of the GTMD observables;
12. a scoped, reversible provenance replacement of the C3/C4 analytic common-parent pilots inside the microscopic validation branch only.

C11 is the first package that may issue a status equivalent to

```text
MICROSCOPIC_NONZERO_TRANSFER_COMMON_PARENT_VALIDATED
```

for a regulated finite-basis object. It remains **unmatched and validation-only**. It is not a physical GTMD, GPD, PDF, TMD, Wigner distribution, OAM decomposition in a continuum QCD scheme, nuclear input, evolved distribution, process prediction, or inference model.

## Normative sources

Before implementation, audit and record the exact hashes of all available formalism sources under `references/`. The primary C11 sources are:

```text
references/algebraic_geometric_next_level_model_note_revised.tex
references/volume_i_regulated_light_front_foundations.tex
references/volume_ii_common_nucleon_gtmd_overlaps.tex
references/volume_vii_concrete_microscopic_nucleon_hamiltonian.tex
references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
references/volume_ix_dynamical_gluon_fock_sectors.tex
references/volume_x_light_sea_chiral_pcac_antiquark_gtmds.tex
references/model_construction_note.tex
```

C10 reported that the revised architecture note and Volumes VIII and IX were unavailable. Add the supplied verified sources, together with Volume X, in a documentation-only commit if they remain absent. Do not invent or reconstruct missing text.

Expected hashes are:

```text
29a75dac37fe695ab05e139c9872e3a4491fcf70b019dec386129a596eb10489  algebraic_geometric_next_level_model_note_revised.tex
8d9d53ba6ed007909abbb41e2ad93217ee42368fde43df24569b568990879c00  volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex
3b90df86e9e426c15aea93a25e64223e9243108b4a9051eebf74f233ad72cc1c  volume_ix_dynamical_gluon_fock_sectors.tex
87734312114b57a5bc441484c8d81a08b91c75815a037ab579c0d20fde930c4a  volume_x_light_sea_chiral_pcac_antiquark_gtmds.tex
```

If a repository file at one of these paths has a different hash, do not silently treat it as the supplied normative source. Record the mismatch, preserve the existing file, and continue using only verified sources plus the equations explicitly stated in this work package.

Create:

```text
docs/next_level/c11_normative_source_integration.json
docs/next_level/c11_normative_integration_report.md
```

## Completeness and autonomy

Completeness is the objective. Do not optimize for speed or minimize the physics.

Read the C3–C10 implementation reports, APIs, manifests, ADRs, tests, and `handoff/ROADMAP.md`. Reuse the actual C1–C10 types and interfaces. In particular, do not create parallel definitions of coordinates, recoil, operator identity, rank, paths, active slots, state bundles, TTNs, reductions, Feshbach provenance, currents, or matching status when existing types can be extended safely.

Continue autonomously until every deliverable and acceptance gate is complete. Do not stop to request routine permission for local inspection, tests, non-destructive tooling, dependency installation, document generation, or local commits when the environment permits those actions.

## Immutable baseline gates

Before editing executable code, reproduce and record:

```text
876/876 existing tests
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
C10 injections: 90/90

210 C10 requirements covered
216 accepted production reductions
```

Verify that all eight authoritative production artifacts remain byte-identical to C10. Verify that the production registry, production provenance graph, default composition plan, C7–C9 microscopic oracles, C10 state/current/PCAC/common-parent manifests, and pinned C5/C6 Wilson manifests are unchanged.

Do not modify any accepted numerical parent, accepted TMD value, sign, convention, row ordering, evidence class, uncertainty member, atlas page, production metadata, or prior benchmark manifest.

## Required package location

Create or extend an isolated microscopic H4 package, preferably:

```text
src/deuteron_wigner/microscopic/h4/
```

It may import H0–H3 types and read-only results. It must have no path to the accepted production root.

## Scientific scope and explicit nonclaims

C11 is restricted to:

```text
xi = 0
nonzero transverse transfer allowed
positive-x active quark, antiquark, and gluon slots
zeroth rescattering / Wilson order 0 for the H4 parent
T-even microscopic parent and exact link-odd zero tests
finite BLFQ/TTN basis and finite quadrature domains
regulated LF operator identity
```

C11 must not claim or implement as complete:

- nonzero skewness or ERBL overlaps;
- number-changing GTMD overlaps without a named operator source;
- physical Wilson-line phases or T-odd TMD predictions;
- a soft-subtracted or rapidity-renormalized QCD GTMD/TMD;
- LF-to-QCD finite matching;
- DGLAP or TMD evolution;
- a deuteron/nuclear convolution;
- a physical process factorization map;
- a statistical posterior or uncertainty calibration;
- continuum, regulator-independent, or phenomenologically fitted nucleon predictions.

Every result must retain at least:

```text
VALIDATION_ONLY
REGULATED_MICROSCOPIC_GTMD
XI_ZERO
ZEROTH_RESCATTERING
LINK_SHORTENING_REQUIRED
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
NO_EVOLUTION_APPLIED
NO_PROCESS_MAP_APPLIED
NO_NUCLEAR_COMPOSITION_APPLIED
```

## Required scientific implementation

### C11.1 — H4 assumption and member identity

C11 must consume the immutable H3 assumption plans and correlated proton/neutron members rather than creating new hidden branches.

At minimum support:

```text
H4-PLAN-A
    derived from C10 H3 PLAN-A: C10:H3:PLAN:7c520ce5e2e04d2c7719
    explicit uubar and ddbar sectors
    canonical pair dynamics
    owned chiral interaction

H4-PLAN-B
    derived from C10 H3 PLAN-B: C10:H3:PLAN:b2efe73052d1c9d1004b
    explicit uubar and ddbar sectors
    canonical pair dynamics
    chiral interaction disabled
```

The H4 plan identity must contain:

- the exact H3 plan and state-bundle hashes;
- resolution and TTN-bond identity;
- operator and recoil conventions;
- Wilson order and path status;
- kinematic-grid and quadrature manifests;
- projector-basis version;
- matching/readiness status;
- provenance and replacement scope.

PLAN-A and PLAN-B are alternative theories. Their GTMDs may be compared but never added.

### C11.2 — Incoming and outgoing momentum fibers

Use the symmetric zero-skewness frame

\[
 p=P-\frac{\Delta}{2},
 \qquad
 p'=P+\frac{\Delta}{2},
 \qquad
 \Delta^+=0,
 \qquad
 \xi=0,
 \qquad
 t=-\bm\Delta_T^2.
\]

Implement or reuse a typed `MomentumFiber` whose identity includes:

- total \(P^+\), transverse momentum, and on-shell mass convention;
- incoming/outgoing role;
- target species, helicity, and microscopic member;
- resolution, regulator, and normalization identity;
- transfer and skewness convention;
- compatible physical Hilbert space and basis embedding.

An off-forward operator is a map

\[
\mathcal O(P',P):\mathcal H_P\rightarrow\mathcal H_{P'},
\]

not a nominal endomorphism of one momentum-independent array.

Required failures include incompatible masses, normalizations, resolutions, skewness, transfer types, target identities, and state members.

### C11.3 — Single authoritative symmetric recoil map

Reuse or extend the C3/C4 `SymmetricXiZeroRecoil` authority. Do not reimplement recoil formulas in H4 projectors or overlap kernels.

For active parton \(j\),

\[
\bm\kappa_{jT}^{\rm in}
=
\bm k_{jT}-\frac{1-x_j}{2}\bm\Delta_T,
\qquad
\bm\kappa_{jT}^{\rm out}
=
\bm k_{jT}+\frac{1-x_j}{2}\bm\Delta_T.
\]

For every spectator \(i\neq j\),

\[
\bm\kappa_{iT}^{\rm in}
=
\bm k_{iT}+\frac{x_i}{2}\bm\Delta_T,
\qquad
\bm\kappa_{iT}^{\rm out}
=
\bm k_{iT}-\frac{x_i}{2}\bm\Delta_T.
\]

The implementation must prove and test:

1. intrinsic transverse-momentum closure in both fibers;
2. active physical momentum transfer equals \(\Delta\);
3. spectator physical momenta are unchanged in the diagonal overlap;
4. unit Jacobian;
5. identity at \(\Delta_T=0\);
6. exchange of incoming and outgoing coordinates under \(\Delta_T\to-\Delta_T\);
7. constituent-permutation covariance;
8. compatibility with all four H3 Fock sectors.

Any local recoil formula or silent factor such as \((1-x)\), \(x\), or \(1/2\) outside the authoritative object must fail code review and tests.

### C11.4 — Microscopic momentum-space amplitude evaluator

The H3 eigenvectors and TTNs are stored in a finite longitudinal/transverse basis. C11 must implement a common evaluator

```text
MicroscopicWaveFunctionEvaluator
```

or equivalent that maps an H3 state bundle to complex momentum-space amplitudes

\[
\psi_{\nu,\Lambda}
\left(\{x_i,\bm\kappa_{iT},\lambda_i,c_i\}\right)
\]

at the incoming and outgoing recoil coordinates.

The evaluator must:

- use the actual BLFQ longitudinal and transverse basis functions;
- preserve all color, permutation, flavor, helicity, OAM, Fock-sector, and outer-multiplicity labels;
- support exact coefficient vectors and TTN states through one interface;
- use a declared center-of-mass projection and basis normalization;
- expose interpolation or quadrature error separately;
- reject continuous \(x\) queries unsupported by the finite longitudinal representation unless an explicit interpolation/basis-evaluation map exists;
- provide derivatives with respect to \(\bm\Delta_T\) where needed for OAM;
- have an independent direct-basis-sum oracle on small states.

Full-bond TTN and exact-vector amplitude evaluations must agree. Low-bond errors must be reported, not hidden by renormalization.

### C11.5 — Decorated microscopic GTMD operator identities

Construct or extend decorated operator IDs for:

#### Quarks and antiquarks

\[
\Gamma\in
\left\{
\gamma^+,
\gamma^+\gamma_5,
 i\sigma^{j+}\gamma_5
\right\}.
\]

Each ID must include:

- species and flavor;
- positive-x active-slot representation;
- incoming/outgoing fibers;
- \(x,\bm k_T,\bm\Delta_T,\xi\) convention;
- Dirac projection and spinor/gamma phase convention;
- fundamental or anti-fundamental color representation;
- operator path and Wilson order;
- ultraviolet, rapidity, soft, scale, and scheme status;
- transverse-rank and reference-mass convention;
- microscopic member and assumption plan.

Antiquarks must use direct positive-x active slots. A negative-x quark relation is permitted only through the existing typed charge-conjugation adapter with operator-specific sign, endpoint, path, and representation transformations.

#### Gluons

Use the field-strength operator with ordered adjoint links and transverse indices \(i,j\). At Wilson order 0 the diagonal adjoint identity is retained, but the operator identity must still contain the ordered-link pair and its unresolved physical path status.

The gluon identity must retain:

- active gluon slot;
- both H2/H3 color outer multiplicities;
- transverse field-strength indices;
- ordered adjoint link pair;
- diagonal-adjoint color status;
- normalization convention, including the `H^g = x g` convention where used;
- polarization and tensor-rank metadata.

### C11.6 — Common diagonal microscopic overlap kernel

Implement the canonical zero-skewness, zeroth-rescattering diagonal overlap for every supported sector:

\[
\begin{aligned}
W_{a/N,\Lambda'\Lambda}^{[J]}
(x,\bm k_T,\bm\Delta_T)
={}&
\sum_{\nu}\sum_{j\in a(\nu)}
\int[d\Gamma_\nu]\,
\delta(x-x_j)\,
\delta^{(2)}(\bm k_T-\bm k_{jT})
\\
&\times
\psi_{\nu,\Lambda'}^*
\left(\{x_i,\bm\kappa_{iT}^{\rm out}\}\right)
\mathcal P_{a,j}^{[J]}
\psi_{\nu,\Lambda}
\left(\{x_i,\bm\kappa_{iT}^{\rm in}\}\right),
\end{aligned}
\]

with explicit spectator helicity/color deltas, active multiplicity, fermionic signs, normalization, and source/target sector identity.

At \(\xi=0\), positive-x, and Wilson order 0, this kernel is diagonal in retained Fock number. An off-diagonal sector contribution must fail unless it carries a named operator source such as a Wilson expansion, induced operator, zero mode, or nonzero-skewness/ERBL mechanism.

The same overlap engine must serve quarks, antiquarks, and gluons through typed active kernels. No species-specific copy of the recoil or spectator logic is allowed.

### C11.7 — Joint target–parton helicity matrices

For every proton/neutron member and supported species, construct

\[
\mathcal M^a_{\lambda_a'\Lambda';\lambda_a\Lambda}
(x,\bm k_T,\bm\Delta_T),
\]

where the target and leading physical active-parton helicity spaces both have dimension two. The result is a full \(4\times4\) matrix at generic kinematics.

Required parents are:

```text
u quark
d quark
ubar antiquark
dbar antiquark
gluon
```

for both proton and neutron, with correlated microscopic member identity.

The matrix object must retain:

- all external and active helicities;
- complex phase convention;
- species/flavor and color multiplicity;
- kinematics and recoil ID;
- exact/TTN solver identity;
- operator and assumption-plan identity;
- numerical and truncation residuals.

A scalar coefficient table without the complete matrix is not an H4 parent.

### C11.8 — Complete quark and antiquark GTMD projector closure

At generic nondegenerate \((\bm k_T,\bm\Delta_T)\), implement the complete twist-two quark basis

\[
\{F_{1,n}\}_{n=1}^{4},
\qquad
\{G_{1,n}\}_{n=1}^{4},
\qquad
\{H_{1,n}\}_{n=1}^{8}.
\]

Construct the vector, axial, and chiral-odd basis tensors from the declared spinor, gamma-matrix, mass, \(\bm k_T\), \(\bm\Delta_T\), metric, and epsilon conventions. Generate dual projectors from the Gram matrix:

\[
G_{AB}=\langle B_A,B_B\rangle,
\qquad
\mathcal P_A=\sum_B(G^{-1})_{AB}B_B.
\]

Do not hand-code an inversion when the Gram construction can generate it.

Required tests:

1. generic rank exactly \(4+4+8=16\);
2. projector duality and complete helicity-matrix reconstruction;
3. agreement with an independently coded Meissner–Metz–Schlegel convention adapter on benchmark points;
4. deterministic phase and normalization conventions;
5. correct flavor and antiquark charge-conjugation signatures;
6. exact rank drop at degenerate kinematics;
7. use of the correct reduced basis at \(\Delta_T=0\) or collinear \(\bm k_T\parallel\bm\Delta_T\);
8. refusal to use a pseudoinverse to pretend that an unidentifiable coefficient is determined;
9. explicit orbital-support manifest for every scalar coefficient;
10. exact zero when a required H3 helicity/OAM block is disabled.

The complete **T-even** subspace must reconstruct the Wilson-order-zero microscopic parent. Link-odd coefficients must vanish within tolerance. A residual outside the declared T-even basis is a reported defect, not something to project away silently.

### C11.9 — Complete gluon tensor/helicity projector closure

Build the gluon parent first as

\[
\mathcal M^g_{\lambda_g'\Lambda';\lambda_g\Lambda}
\quad\text{or equivalently}\quad
W_{\Lambda'\Lambda}^{g,ij}.
\]

Use one common tensor parent and the existing executable transverse projectors:

\[
W_U=\delta_{T,ij}W^{ij},
\qquad
W_H=i\epsilon_{T,ij}W^{ij},
\qquad
W_L^{ij}=W^{(ij)}-\frac12\delta_T^{ij}W^k_{\ k}.
\]

Generate the complete leading-twist scalar basis algorithmically from:

- target-helicity tensors;
- active-gluon helicity or transverse-index tensors;
- \(\bm k_T\), \(\bm\Delta_T\), \(\delta_T^{ij}\), and \(\epsilon_T^{ij}\);
- Hermiticity, parity, power counting, and \(SO(2)\) weight.

The implementation must:

1. determine and record the generic Gram rank rather than assume it from array size;
2. reconstruct the full gluon helicity/tensor parent from dual projectors;
3. retain both microscopic `qqqg` color outer multiplicities;
4. distinguish trace, circular/helicity, and linear/symmetric-traceless sectors;
5. recover the complete forward spin-1/2 gluon TMD basis supported at Wilson order 0;
6. produce exact zeros for link-odd gluon TMD combinations at zeroth rescattering;
7. preserve the ordered two-link operator identity even though no physical staple dynamics is applied;
8. keep future `f`/`d` gluonic-pole channels unavailable rather than aliasing them to the diagonal parent;
9. report any orthogonal tensor component not represented by the declared basis.

### C11.10 — Discrete symmetries and transfer reversal

Implement operator-level tests before scalar projection.

#### Hermiticity

For quarks/antiquarks:

\[
\left[W_{\Lambda'\Lambda}^{[\Gamma]}
(x,\bm k_T,\bm\Delta_T;\gamma)\right]^*
=
W_{\Lambda\Lambda'}^{[\gamma^0\Gamma^\dagger\gamma^0]}
(x,\bm k_T,-\bm\Delta_T;\gamma^{-1}).
\]

For gluons:

\[
\left[W_{\Lambda'\Lambda}^{g,ij}
(x,\bm k_T,\bm\Delta_T;\gamma_1,\gamma_2)\right]^*
=
W_{\Lambda\Lambda'}^{g,ji}
(x,\bm k_T,-\bm\Delta_T;\gamma_2^{-1},\gamma_1^{-1}).
\]

#### Parity

Use the represented light-front parity map on momentum fibers, target and parton helicities, basis tensors, and operator identity. Do not implement parity as an untyped downstream sign.

#### Time reversal/link parity

At Wilson order 0, all link-odd/T-odd projections must vanish. Future/past labels may be represented as formal operator alternatives, but their zeroth-order T-even results must agree after the full antiunitary adapter.

Required tests include random complex states, exact/TTN states, transfer reversal, endpoint reversal, gluon index swap, and deliberate phase/sign mistakes.

### C11.11 — Forward TMD and regulated GPD/PDF reductions

All reductions must consume the same microscopic parent ID.

Define:

\[
\mathsf T[W](x,\bm k_T)=W(x,\bm k_T,\bm\Delta_T=0),
\]

\[
\mathsf G_{\rm reg}[W](x,\bm\Delta_T)
=
\int d^2\bm k_T\,W(x,\bm k_T,\bm\Delta_T),
\]

and

\[
\mathsf P_{\rm reg}[W](x)
=
\int d^2\bm k_T\,W(x,\bm k_T,0).
\]

Required closure:

1. direct forward overlap equals the \(\Delta_T\to0\) GTMD route;
2. GTMD \(\to\) TMD \(\to\) PDF equals GTMD \(\to\) regulated GPD \(\to\) PDF;
3. quark and antiquark remain separate positive-x objects;
4. gluon uses the declared `H^g=xg` convention where applicable;
5. rank-zero functions have the declared unweighted collinear limit;
6. positive-rank unweighted angular integrals vanish unless the registry explicitly defines a contracted scalar or weighted moment;
7. no named-function normalization correction is permitted.

These are regulated finite-basis reductions. Do not label them physical PDFs, GPDs, or TMDs.

### C11.12 — Local vector, axial, tensor-status, and EMT consistency

Compare moments of the H4 common parent against direct Hamiltonian-consistent operators from H3/H4.

#### Vector current

For each flavor,

\[
F_1^q(t)
=
\int_0^1 dx\,
\left[H^q(x,0,t)-H^{\bar q}(x,0,t)\right].
\]

Compare with the direct H3 vector-current matrix element at the same transfer and component.

#### Axial current

Use the operator-specific charge-conjugation signature:

\[
G_A^q(t)
=
\int_0^1 dx\,
\left[\widetilde H^q(x,0,t)+\widetilde H^{\bar q}(x,0,t)\right],
\]

and compare with the H3 axial current. Preserve the PCAC and induced-pion-pole identities; do not double count them in the GTMD moment.

#### Tensor current

If a Hamiltonian-consistent local tensor current is not yet implemented, its GTMD moment route must return `LOCAL_TENSOR_OPERATOR_UNAVAILABLE`. Do not normalize the chiral-odd GTMDs to an imported tensor charge. If C11 implements a finite-basis tensor operator, it must be owned by the H3/H4 Hamiltonian identity and validated independently.

#### Energy–momentum tensor

Implement or reuse a finite-basis plus-momentum/EMT operator consistent with the microscopic state. Compare:

\[
A_q(t)
=
\int_0^1 dx\,x\,[H^q+H^{\bar q}],
\qquad
A_g(t)
=
\int_0^1 dx\,H^g,
\]

under the declared gluon convention. The total forward route must reproduce the microscopic momentum ledger.

At least two nonzero-transfer points must be withheld from any normalization or coefficient tuning.

### C11.13 — Wigner transform and OAM/spin–orbit consistency

Retain the strict coordinate distinction:

\[
\bm b_\Delta\longleftrightarrow\bm\Delta_T,
\qquad
\bm b_{\rm TMD}\longleftrightarrow\bm k_T.
\]

Construct the regulated Wigner parent

\[
\rho_W(x,\bm k_T,\bm b_\Delta)
=
\int\frac{d^2\bm\Delta_T}{(2\pi)^2}
 e^{-i\bm b_\Delta\cdot\bm\Delta_T}
 W(x,\bm k_T,\bm\Delta_T).
\]

Evaluate OAM in two independent routes:

1. a Wigner moment,
   \[
   L_z^a
   =
   \int dx\,d^2\bm k_T\,d^2\bm b_\Delta\,
   (\bm b_\Delta\times\bm k_T)_z\,
   \rho_{LU}^a;
   \]
2. a transfer derivative at \(\Delta_T=0\), with the sign derived from the stored Fourier convention.

Compare these with the direct H3 finite-basis canonical OAM ledger for quarks, antiquarks, and gluons, within the declared truncation and operator convention.

Where the selected convention maps OAM or spin–orbit correlation to \(F_{1,4}\)- or \(G_{1,1}\)-type GTMD combinations, implement the adapter and verify it. Do not claim a scheme-independent canonical/kinetic identity.

Required tests:

- Wigner and derivative route agreement;
- analytic versus finite-difference derivative agreement;
- exact sign reversal under Fourier-phase inversion injection;
- vanishing when required \(L_z\) interference blocks are removed;
- exact/TTN agreement at full bond;
- visible low-bond loss of at least one OAM-sensitive GTMD while energy remains comparatively accurate.

### C11.14 — Positivity and off-forward bounds

At \(\Delta_T=0\), the complete forward helicity parent must admit the applicable Gram representation and remain positive semidefinite within tolerance.

Test positivity on the complete joint matrix, not by clipping named TMDs.

At nonzero transfer, do **not** require positive semidefiniteness. Instead test sector-resolved and total Cauchy–Schwarz/operator-norm bounds of the form

\[
|W_{\beta\alpha}(\Delta)|^2
\le
\|\mathcal K_{\beta\alpha}\|_{\rm op}^2
\|A_\beta^{\rm out}\|^2
\|A_\alpha^{\rm in}\|^2.
\]

Wigner functions are quasidistributions and may be negative. Any pointwise Wigner-positivity requirement must fail.

### C11.15 — Resolution, Fock, quadrature, and TTN convergence

For every common-parent observable, report separate residuals for:

- longitudinal resolution;
- transverse basis and ultraviolet support;
- infrared/basis-scale variation;
- Fock-sector content;
- OAM/helicity support;
- exact versus Krylov state;
- exact versus full-bond TTN;
- finite TTN bond dimension;
- \(\bm k_T\) quadrature;
- \(\bm\Delta_T\) grid and derivative resolution;
- Wigner-transform range and quadrature;
- basis Gram conditioning and projector rank.

Do not combine these into one band before reporting each category.

Use comparison maps between resolutions and track the same physical state. A smooth function at one resolution is not convergence.

At least one observable from each category must be included:

```text
rank-zero density
helicity observable
chiral-odd observable
gluon polarization observable
antiquark observable
OAM-sensitive nonzero-transfer observable
local-current or EMT moment
```

### C11.16 — Controlled replacement of C3/C4 analytic parents

C3 and C4 remain immutable analytic validation oracles. C11 must not delete, rewrite, or numerically tune to them.

Create a scoped provenance relation such as:

```text
C3_ANALYTIC_COMMON_PARENT
    BENCHMARKS
H4_MICROSCOPIC_COMMON_PARENT

C4_ANALYTIC_SEA_GLUON_PARENT
    BENCHMARKS
H4_MICROSCOPIC_COMMON_PARENT

H4_MICROSCOPIC_COMMON_PARENT
    REPLACES_WITHIN_SCOPE
C3/C4_ANALYTIC_PARENT
```

where `REPLACES_WITHIN_SCOPE` is valid only for:

- the H4 microscopic validation root;
- supported species and operators;
- zero skewness;
- supported nonzero-transfer and forward grids;
- Wilson order 0;
- the exact H3 assumption plan and state member;
- passed closure and convergence gates.

The relation does not enter production. The accepted 216-route phenomenological registry remains unchanged.

The replacement manifest must record:

- overlapping benchmark quantities;
- structural agreement tests;
- numerical differences without forcing equality;
- unavailable analytic or microscopic components;
- direction of replacement;
- rollback procedure;
- downstream readiness gates.

C3/C4 Gaussian widths and sector probabilities are validation parameters, not targets for H4 fitting.

### C11.17 — Downstream readiness gates

C11 may issue narrowly scoped statuses such as:

```text
MICROSCOPIC_NONZERO_TRANSFER_COMMON_PARENT_VALIDATED
MICROSCOPIC_QUARK_GTMD_PROJECTORS_VALIDATED
MICROSCOPIC_ANTIQUARK_GTMD_PROJECTORS_VALIDATED
MICROSCOPIC_GLUON_GTMD_PROJECTORS_VALIDATED
MICROSCOPIC_TEVEN_FORWARD_LIMIT_VALIDATED
MICROSCOPIC_CURRENT_EMT_ROUTE_VALIDATED
MICROSCOPIC_WIGNER_OAM_ROUTE_VALIDATED
ANALYTIC_PARENT_REPLACEMENT_VALIDATED_WITHIN_H4
NUCLEAR_HELICITY_INPUT_INTERFACE_VALIDATED
```

It must not issue:

```text
PHYSICAL_GTMD
PHYSICAL_GPD
PHYSICAL_PDF
PHYSICAL_TMD
WILSON_READY
T_ODD_PREDICTION_READY
NUCLEAR_MATCHING_READY
LF_TO_QCD_MATCHING_READY
EVOLUTION_READY
PROCESS_READY
INFERENCE_READY
PRODUCTION_REPLACEMENT_COMPLETE
```

The Volume IV nuclear gate remains closed because a complete correlated covariance/posterior, soft/phase completion, and matched nuclear operator interface are not yet available.

The Volume V matching/evolution gate remains closed because the regulated operator basis has not been matched to a declared soft-subtracted QCD scheme.

## Required computational objects

Implement or extend objects equivalent to:

```text
MicroscopicMomentumFiber
MicroscopicRecoilMap
MicroscopicWaveFunctionEvaluator
MicroscopicActivePartonSelector
MicroscopicOverlapKernel
MicroscopicGTMDOperatorId
GTMDHelicityMatrix
QuarkGTMDProjectorBasis
AntiquarkGTMDProjectorBasis
GluonGTMDProjectorBasis
OrbitalSupportManifest
MicroscopicCommonParentBundle
MicroscopicReductionMap
LocalMomentClosureReport
WignerTransformPlan
OAMConsistencyReport
GTMDConvergenceManifest
MicroscopicReplacementManifest
H4CapabilitySnapshot
```

Use the actual C1–C10 naming conventions when available. Do not create aliases that bypass type checks.

## Mandatory benchmark families

Implement at least the following deterministic benchmark families.

### H4-A — Fiber and recoil closure

- exact incoming/outgoing fibers;
- intrinsic and physical momentum closure;
- unit Jacobian;
- transfer reversal;
- all four H3 sectors;
- comparison with the independent C3 recoil oracle.

### H4-B — Microscopic amplitude evaluation

- direct basis-sum versus exact-vector evaluator;
- direct basis-sum versus full-bond TTN;
- analytic basis-function oracle on selected modes;
- normalization and derivative checks;
- finite-bond amplitude error.

### H4-C — Quark sixteen-function closure

- generic Gram rank 16;
- dual projector identity;
- helicity-matrix reconstruction;
- published-convention adapter;
- degenerate-rank handling;
- OAM-support zero tests.

### H4-D — Antiquark closure and charge conjugation

- direct positive-x `ubar` and `dbar` matrices;
- all three five-parton color multiplicities;
- vector/axial/chiral-odd charge-conjugation signatures;
- no negative-x copy;
- forward and nonzero-transfer closure.

### H4-E — Gluon tensor/helicity closure

- both `qqqg` color multiplicities;
- full transverse-tensor reconstruction;
- trace, helicity-antisymmetric, and symmetric-traceless routes;
- generic basis-rank manifest;
- forward TMD reduction;
- exact link-odd zero.

### H4-F — Hermiticity, parity, and zeroth-order link parity

- \(\Delta_T\leftrightarrow-\Delta_T\);
- target and parton helicity exchange;
- gluon index and ordered-link reversal;
- random complex state members;
- exact and TTN states;
- injected phase and endpoint errors.

### H4-G — Common TMD/GPD/PDF closure

- direct forward route;
- sequential routes;
- quark, antiquark, and gluon conventions;
- rank-zero and ranked moments;
- no named-function renormalization.

### H4-H — Local vector, axial, and EMT closure

- proton and neutron vector currents;
- flavor-separated axial current;
- correct quark/antiquark signs;
- gluon and total EMT moments;
- at least two nonzero-transfer holdouts.

### H4-I — Wigner, OAM, and spin–orbit closure

- Wigner versus derivative route;
- direct H3 OAM ledger;
- \(F_{1,4}\)/\(G_{1,1}\) convention adapters where supported;
- Fourier-sign injection;
- OAM-block removal;
- TTN bond sensitivity.

### H4-J — Positivity and off-forward bounds

- forward PSD for all species;
- off-forward Cauchy–Schwarz bounds;
- negative Wigner values allowed;
- deliberate positivity clipping rejected.

### H4-K — Multi-axis convergence

- all three H3 resolutions;
- exact/Krylov/full-bond agreement;
- nested TTN bonds;
- kinematic-grid and quadrature refinement;
- projector conditioning;
- observable-level convergence tables.

### H4-L — Analytic-pilot replacement

- C3/C4 remain byte-identical;
- H4 replacement activates only in the microscopic validation root;
- unsupported domains fail closed;
- structural benchmark comparison;
- rollback and provenance trace.

### H4-M — Assumption branches

- PLAN-A and PLAN-B compile independently;
- no branch summation;
- chiral effects propagate to sea and axial GTMDs;
- shared parameters affect every relevant projection;
- plan identity survives caching and serialization.

### H4-N — Downstream gates

- production promotion fails;
- nuclear composition without covariance/soft data fails;
- Wilson/T-odd request fails;
- QCD matching/evolution request fails;
- process and inference requests fail.

## Mandatory negative-injection programme

Create stable ordered IDs for at least **100 C11/H4 negative injections**. Cover, at minimum, the following categories:

1. wrong skewness or nonzero \(\Delta^+\);
2. incoming/outgoing fiber swap;
3. wrong active recoil sign;
4. wrong spectator recoil sign;
5. missing factor of one-half;
6. silent coordinate alias between \(\bD\) and \(\bM\);
7. nonunit recoil Jacobian;
8. broken intrinsic closure;
9. wrong state member in one fiber;
10. incompatible resolution or normalization;
11. continuous-x query without a declared basis map;
12. duplicated active slot;
13. wrong active species or flavor;
14. off-diagonal Fock overlap without a source;
15. missing fermion permutation sign;
16. dropped color outer multiplicity;
17. wrong antiquark anti-fundamental action;
18. negative-x antiquark copy;
19. incomplete operator identity;
20. wrong gamma/spinor phase convention;
21. wrong gluon field-strength normalization;
22. lost ordered-link identity;
23. implicit `f/d` assignment at Wilson order 0;
24. quark Gram rank not 16 at generic kinematics;
25. use of pseudoinverse at a degenerate point without reduced-basis status;
26. basis/projector phase mismatch;
27. missing mass factor or rank metadata;
28. wrong SO(2) weight;
29. nonreconstructing quark matrix;
30. nonreconstructing gluon tensor;
31. projection before retaining complete helicity matrix;
32. Hermiticity sign or endpoint error;
33. parity applied as a downstream scalar sign;
34. incomplete antiunitary link transformation;
35. nonzero T-odd result at Wilson order 0;
36. arbitrary imaginary coefficient;
37. numerical epsilon treated as physical;
38. wrong quark/antiquark vector sign;
39. wrong quark/antiquark axial sign;
40. gluon quark-like Mellin convention;
41. named-function normalization repair;
42. positive-rank unweighted integral incorrectly retained;
43. local current imported from another Hamiltonian;
44. tensor charge imported without an H4 tensor operator;
45. double-counted induced pion-pole term;
46. EMT route missing antiquark or gluon contribution;
47. Wigner Fourier sign error;
48. OAM derivative sign error;
49. \(\bD\)/\(\bM\) transform swap;
50. OAM inferred from a forward scalar density;
51. required OAM block removed but projection remains nonzero;
52. forward PSD failure;
53. eigenvalue clipping;
54. off-forward PSD incorrectly required;
55. pointwise Wigner positivity required;
56. Cauchy–Schwarz bound violation;
57. exact/full-bond TTN mismatch;
58. low-bond result labeled converged from energy alone;
59. grid convergence used to hide Fock convergence;
60. posterior-sized band used to hide matching uncertainty;
61. PLAN-A and PLAN-B added;
62. cache reused across plans;
63. cache reused across transfers or projectors;
64. stale C3/C4 result promoted as microscopic;
65. H4 result forced to equal analytic Gaussian pilot;
66. replacement edge active outside supported scope;
67. C3/C4 oracle modified;
68. production registry changed;
69. production provenance changed;
70. authoritative artifact changed;
71. C5/C6 manifest changed;
72. nuclear composition activated without required inputs;
73. Wilson/T-odd engine activated from zeroth-order parent;
74. physical GTMD/TMD status issued;
75. LF-to-QCD matching declared complete;
76. evolution applied;
77. process map applied;
78. inference/calibration applied;
79. nonzero-skewness request accepted;
80. ERBL request accepted;
81. unsupported strange/heavy flavor silently created;
82. unsupported local tensor route silently normalized;
83. microscopic member identity lost through reduction;
84. proton/neutron member decorrelated;
85. color multiplicity lost through TTN contraction;
86. active gluon helicity lost;
87. antiquark flavor lost;
88. transfer-grid interpolation outside validity;
89. Gram condition number ignored;
90. degenerate basis reported as complete;
91. quadrature error omitted;
92. derivative error omitted;
93. comparison-map identity omitted;
94. unresolved matching term set to zero;
95. T-even residual projected away;
96. off-forward orthogonal component discarded silently;
97. provenance path lacks source hashes;
98. output serialization changes physical identity;
99. final working tree dirty;
100. final commit not descended from C10.

Additional injections are encouraged where actual C10 APIs expose further failure modes.

## Required documentation and machine-readable outputs

Create at least:

```text
docs/next_level/c11_implementation_report.md
docs/next_level/c11_api.md
docs/next_level/c11_normative_source_integration.json
docs/next_level/c11_normative_integration_report.md
docs/next_level/c11_assumption_plan_manifest.json
docs/next_level/c11_kinematic_grid_manifest.json
docs/next_level/c11_gtmd_operator_registry.json
docs/next_level/c11_quark_antiquark_projector_manifest.json
docs/next_level/c11_gluon_projector_manifest.json
docs/next_level/c11_helicity_matrix_closure_report.json
docs/next_level/c11_current_emt_closure_report.json
docs/next_level/c11_wigner_oam_closure_report.json
docs/next_level/c11_convergence_manifest.json
docs/next_level/c11_microscopic_replacement_manifest.json
docs/next_level/c11_injection_manifest.json
docs/next_level/c11_requirement_coverage.json
docs/next_level/c11_regression_report.json
docs/next_level/c11_unresolved_physics_gaps.md
```

Update `handoff/ROADMAP.md` with:

- final commit;
- exact readiness statuses;
- principal residuals;
- unresolved matching/Wilson/nuclear/inference gates;
- exact next package.

All JSON must be deterministic and schema-versioned.

## Acceptance criteria

C11 is complete only when all of the following hold:

1. The full C10 baseline reproduces before edits.
2. All prior tests, builders, evidence rows, atlases, injections, and hashes remain passing and unchanged where required.
3. One authoritative recoil object is used by every H4 species and projector.
4. Exact-vector and full-bond TTN momentum-space amplitudes agree.
5. Full \(4\times4\) helicity matrices exist for \(u,d,\bar u,\bar d,g\) and correlated proton/neutron members.
6. The quark/antiquark generic projector rank is 16 and reconstructs the complete matrix.
7. Degenerate kinematics use an explicit reduced basis and never fake full identifiability.
8. The generated gluon basis reconstructs the complete declared tensor/helicity parent and records its generic rank.
9. Hermiticity, parity, transfer reversal, and zeroth-order link-parity tests pass.
10. Every link-odd/T-odd projection is zero at Wilson order 0.
11. TMD/GPD/PDF routes close from the same parent without named-function normalization.
12. Vector and axial moment routes agree with direct H3 currents within declared errors.
13. Gluon and total EMT/momentum routes close under the declared convention.
14. Wigner, transfer-derivative, and direct OAM routes agree within the declared finite-basis error.
15. Forward PSD and off-forward Cauchy–Schwarz tests pass at their correct layers.
16. Resolution, quadrature, and TTN-bond convergence are reported separately for representative GTMDs.
17. C3/C4 analytic pilots remain immutable and are replaced only inside the supported H4 microscopic validation scope.
18. PLAN-A and PLAN-B remain distinct and mutually exclusive.
19. At least 100 C11 negative injections are detected with stable diagnostics.
20. No production, Wilson/T-odd, nuclear, matching/evolution, process, or inference gate is crossed.
21. All eight authoritative artifacts remain byte-identical.
22. The production registry remains exactly 216 routes.
23. All required documentation and deterministic manifests exist and validate.
24. The final local commit descends from C10, nothing is pushed, and the working tree is clean.

## Recommended next package after C11

If C11 passes, the next package should be:

> **C12/H5 — microscopic Wilson-line dynamics on the H4 common GTMD parent: physical spectral support, quark/antiquark/gluon link-odd helicity matrices, shared Sivers/Boer–Mulders and active-gluon `f/d` projections, and higher-Wilson-order/Fock-order compatibility.**

C12 must use the actual H4 helicity matrices, OAM-support manifests, current identities, microscopic member propagation, and replacement provenance. It should not be written until the C11 implementation report is available.

A separate later package will perform LF-to-QCD matching and common rank-aware evolution; do not merge that work into C11 or C12.

## Final Codex response

Report:

- starting and final commit;
- test/builder/evidence/atlas/injection totals;
- species/flavor/helicity-matrix coverage;
- quark/antiquark and gluon projector ranks;
- maximum reconstruction, symmetry, current/EMT, OAM, positivity/bound, and convergence residuals;
- exact versus TTN and bond-convergence results;
- PLAN-A/PLAN-B comparison;
- analytic-pilot replacement scope;
- immutable production hashes and registry status;
- issued readiness statuses;
- unresolved physics gates;
- exact recommended C12 task.

Do not describe C11 as a physical GTMD/TMD prediction or as complete QCD matching.
