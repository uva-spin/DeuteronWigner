# C5 Codex Work Package

> Revised for the fully formalism-integrated C4 baseline `62125f0857e597e8f9548f279ae70b1634764a24`.

## Validation-only one-gluon Wilson-line and light-front-cut pilot

### Baseline

Begin from the exact local C4 completion commit:

```text
62125f0857e597e8f9548f279ae70b1634764a24
```

Do not begin implementation unless:

1. the working tree is clean;
2. the current `HEAD` is the exact baseline above, or is a documentation-only descendant with that commit in its ancestry;
3. the complete formalism-integrated C4 regression reproduces:
   - `613/613` tests passing;
   - `9/9` acceptance/report builders passing;
   - `36/36` evidence rows passing;
   - `162/162` atlas pages rendering;
   - all `24/24` C3 negative injections passing;
   - all `40/40` C4 mismatch injections passing;
   - the C4 architecture manifest reporting exactly `25` covered requirements,
     `40` ordered mismatch injections, `16` validation-only provenance nodes,
     and `8` immutable authoritative hashes;
   - all eight authoritative artifacts byte-identical;
   - the accepted production reduction registry unchanged at 216 routes;
4. the C2 production provenance graph/default plan and the C3/C4 validation manifests reproduce exactly;
5. `references/formalism_volume_index.md` resolves Volumes 0, I, II, III, IV, and V to the repository copies used by the final C4 normative integration audit.

If the current commit differs, identify why, prove ancestry, reproduce the baseline, and record the discrepancy before proceeding. Do not silently reset, rewrite, or discard user work.

The repository is intentionally ahead of `origin/main`; do not use the remote branch as the C5 baseline. Do not push to any remote. Create one clean local completion commit only after every C5 acceptance gate passes.

---

## Normative sources

Use the repository copies of the formalism volumes and reports, in this order:

1. `references/algebraic_geometric_next_level_model_note_revised.tex` or the Volume 0 path recorded by `references/formalism_volume_index.md`;
2. `references/volume_i_regulated_light_front_foundations.tex`;
3. `references/volume_ii_common_nucleon_gtmd_overlaps.tex`;
4. `references/volume_iii_dynamical_wilson_lines.tex`;
5. `references/volume_iv_matched_spin1_nuclear_dynamics.tex` for the nuclear-interface, coherence, and no-double-counting gates that C5 must not cross;
6. `references/volume_v_matching_evolution_factorization.tex` for matching-status, closed-operator-basis, evolution, and process-factorization gates;
7. `docs/next_level/c3_implementation_report.md`;
8. `docs/next_level/c4_implementation_report.md`;
9. `docs/next_level/c4_normative_integration_report.md`;
10. `docs/next_level/c4_normative_source_integration.json`;
11. C1–C4 APIs, requirement-coverage files, manifests, ADRs, and regression reports.

Volume III is the primary normative source for C5. Implement only the first controlled Wilson-line pilot layer described below. Do not claim completion of all Volume III requirements.

Volumes 0–V are now available and indexed. Verify their resolved paths and record the exact source hashes used by C5. Do not modify a normative source merely to make an implementation test pass. If an indexed source is unexpectedly missing or differs from the final C4 source-integration manifest, record the discrepancy, preserve the C4 baseline, and continue only with requirements whose normative text is available and unambiguous.

---

## Scientific objective

Implement the first **dynamical**, but still validation-only, Wilson-line/rescattering pilot on top of the C3–C4 analytic common-parent infrastructure.

C5 must demonstrate that a link-odd phase can be generated from:

1. an explicitly oriented Wilson path;
2. a derived eikonal pole prescription;
3. a declared light-front intermediate-state denominator;
4. an explicit cut/discontinuity;
5. interference between identified helicity/OAM amplitude blocks;

rather than from an arbitrary imaginary coefficient or numerical broadening.

The central chain is

```text
C3/C4 analytic state and common overlap
    -> typed bare Wilson segment
    -> one-gluon eikonal vertex
    -> typed LF resolvent and explicit cut
    -> one-gluon rescattering kernel
    -> full antiunitary future/past adapter
    -> validation-only link-even/link-odd correlators
    -> distinct Sivers-like and Boer-Mulders-like projections
```

This package must remain completely disconnected from accepted production artifacts.

C5 is **not**:

- a physical TMD extraction;
- a fitted Sivers or Boer–Mulders model;
- a full soft-subtracted QCD TMD;
- a Collins–Soper evolution implementation;
- a complete non-Abelian Wilson-line resummation;
- a full gluon `f`/`d` naive-T-odd calculation;
- a nuclear rescattering calculation;
- a microscopic Hamiltonian eigenstate calculation;
- permission to modify any accepted production result.

### Downstream gates that remain closed

C5 does not satisfy the Volume IV nuclear-composition entry contract. No C5 result may be inserted into a deuteron or other nuclear parent until a later package supplies, at minimum:

- complete nucleon helicity-matrix exports rather than only selected scalar projections;
- correlated proton/neutron microscopic member identity;
- a phase and soft-overlap record compatible with the nuclear operator matching;
- covariance or shared-member propagation needed for nuclear composition;
- an explicit separation between the partonic Wilson staple and coherent nuclear rescattering.

C5 also does not satisfy the Volume V evolution/process entry contract. No C5 result may be evolved or used in a physical process object until a later package supplies:

- a closed regulated operator basis containing the relevant quark, antiquark, and gluon channels;
- an explicit LF-to-QCD matching map;
- ultraviolet, rapidity, soft-subtraction, and link-shortening completion;
- a declared TMD scheme and rank-aware evolution identity;
- a process-qualified link/color/Glauber map.

These gates must be represented in machine-readable status and tested fail-closed. They are not qualitative caveats.

Completeness and correctness are the objective. Do not optimize for quickness.

---

## Immutable physics and regression constraints

Do not change:

- any accepted quark, antiquark, or gluon parent value;
- the 216-entry production reduction registry;
- the C2 production provenance graph or default composition plan;
- any C3 or C4 benchmark result, manifest, parameter, or validation-only identity;
- the C4 formalism-integration coverage record: 25 requirements, 40 ordered mismatch injections, 16 validation-only provenance nodes, and 8 immutable hashes;
- any tensor-polarization sign convention;
- any coordinate, recoil, rank, mass, Fourier-phase, sector, path, scheme, or operator identity introduced in C1–C4;
- any authoritative CSV/JSON artifact, row order, numeric formatting, or hash;
- any production atlas or evidence status.

Do not add:

- an arbitrary imaginary constant;
- a fitted phase, TMD normalization, or transverse width;
- a finite `epsilon` broadening treated as physical absorptive dynamics;
- a universal phase copied across different operators;
- a direct proportionality between Sivers and Boer–Mulders projections;
- an implicit future/past sign toggle without an antiunitary operator map;
- a generic gluon T-odd array with lost ordered-link or color identity;
- soft subtraction, rapidity matching, or link shortening by assertion;
- any production fallback intended only to make tests pass.

---

## Required implementation strategy

### A. Reuse the existing formal identity spine

Do not create a second coordinate, rank, sector, Wilson-path, operator-identity, or map-class system.

Reuse and extend the existing C1 formal modules, including the actual repository equivalents of:

```text
src/deuteron_wigner/formal/coordinates.py
src/deuteron_wigner/formal/transverse_rank.py
src/deuteron_wigner/formal/sector_space.py
src/deuteron_wigner/formal/gauge_path.py
src/deuteron_wigner/formal/operator_identity.py
src/deuteron_wigner/formal/maps.py
src/deuteron_wigner/formal/diagnostics.py
```

Reuse the C3/C4 pilot state, recoil, overlap, reduction, and provenance infrastructure. Do not duplicate `ZeroSkewnessFrame`, `SymmetricXiZeroRecoil`, `AnalyticOverlapEvaluator`, active-slot selectors, gluon tensor projectors, or common-parent reduction routes.

The recommended implementation is a new validation-only subpackage such as

```text
src/deuteron_wigner/pilot/wilson_line/
```

but adapt the exact path to the current repository architecture. Record every new public object in `docs/next_level/c5_api.md`.

### B. Keep map classes distinct

The following are different operations and must remain separately typed:

- path transport and interaction vertices: `AMP`;
- intermediate-state trace or selected cut measure where applicable: `DENS` only if a genuine reduced-state operation is performed;
- soft/rapidity or regulator conversion: `MATCH` — not implemented physically in C5;
- Sivers-like and Boer–Mulders-like projections: `RED`;
- process assembly: `PROC` — no physical process prediction in C5.

No implicit array-level composition across these map classes is allowed.

---

## C5.1 — Bare path and eikonal identity

Implement or extend a typed bare semi-infinite Wilson segment with at least:

```text
start_fiber
end_or_infinity_class
tangent_or_eikonal_velocity
orientation = FUTURE | PAST
representation = FUNDAMENTAL | ADJOINT
path_ordering
transverse_closure_identity
Fourier_convention
coupling_convention
rapidity_regulator_identity
Wilson_order
```

The existing decorated `WilsonPathId`/operator identity remains authoritative. The C5 object adds the dynamical data required to evaluate the path; it does not replace the C1 identity.

For the reference path

\[
\gamma_\eta(\lambda)=a+\eta\lambda v,
\qquad \lambda\ge 0,
\qquad \eta=+1\ \text{or}\ -1,
\]

use the Volume III convention

\[
D_\eta(\ell)=\frac{1}{v\!\cdot\!\ell-i0\eta}
=\operatorname{PV}\frac{1}{v\!\cdot\!\ell}
+i\eta\pi\delta(v\!\cdot\!\ell).
\]

The pole sign must be derived from the stored path orientation, Fourier convention, coupling convention, and momentum-flow convention. A caller may not provide an independent arbitrary sign.

Required bare-path properties:

\[
U_{\gamma_2\circ\gamma_1}=U_{\gamma_2}U_{\gamma_1},
\qquad
U_{\gamma^{-1}}=U_\gamma^\dagger,
\]

on compatible endpoint fibers. At first Wilson order, test the expected truncation defect rather than demanding exact all-order unitarity.

Stable package requirements:

```text
C5.PATH.1
C5.PATH.2
C5.POLE.1
C5.POLE.2
```

Map them explicitly to normative requirements `V3.PATH.1`, `V3.PATH.2`, `V3.POLE.1`, and the C5 subset of `V3.POLE.2`.

---

## C5.2 — Distributional pole evaluator

Implement two explicit, separately inspectable routes for integrals of

\[
\frac{F(\ell)}{x(\ell)+i0\sigma}:
\]

1. a principal-value plus cut-surface route,
   \[
   I_{\rm PV}=\operatorname{PV}\int d\ell\,\frac{F(\ell)}{x(\ell)},
   \]
   \[
   I_{\rm cut}=-i\sigma\pi
   \int_{x(\ell)=0}
   \frac{d\Sigma(\ell)}{|\nabla x(\ell)|}F(\ell);
   \]
2. a direct finite-`epsilon` complex integration sequence used only as a convergence oracle.

The finite-`epsilon` sequence must converge to the declared distributional result. `epsilon` is numerical regularization metadata, not a physical phase width.

Implement:

- compactly supported analytic test functions;
- odd-function principal-value cancellation;
- future/past equal PV parts and opposite cut parts;
- cut-surface Jacobian checks;
- deterministic refinement and convergence reports.

Stable package requirements:

```text
C5.DIST.1
C5.DIST.2
C5.DIST.3
```

---

## C5.3 — Light-front resolvent and cut provenance

Implement a typed light-front resolvent/intermediate-state structure:

\[
G_\sigma(P_i^-)
=\frac{1}{P_i^- - H_0 + i0\sigma},
\]

with an explicit spectral representation

\[
\mathcal A_\sigma
=\sum_X
\frac{N_X}{P_i^- - P_X^- + i0\sigma}.
\]

Each denominator must carry:

```text
initial_state_id
intermediate_state_id
initial_LF_energy
intermediate_LF_energy
pole_sign
source_vertex_id
target_operator_id
cut_support_id
finite_volume_or_continuum_rule
regulator_identity
```

Implement an `IntermediateStateCut` and a `CutLedger`.

The `CutLedger` must distinguish:

- an eikonal pole cut;
- a light-front energy-denominator cut;
- whether two algebraically similar delta supports are physically the same contribution;
- an explicit subtraction/equivalence relation when the same on-shell support appears in two representations.

No deduplication may occur merely because two denominators have the same floating-point value. Conversely, the same physical cut may not be counted twice under different object IDs.

For a finite off-shell discrete spectrum, the absorptive part is exactly zero unless a declared finite-volume spectral rule or continuum density creates cut support. A Lorentzian numerical broadening is not a physical cut.

Stable package requirements:

```text
C5.CUT.1
C5.CUT.2
C5.CUT.3
```

These implement the C5 subset of `V3.CUT.1` and `V3.CUT.2`.

---

## C5.4 — One-gluon rescattering kernel

Implement a validation-only first-order rescattering kernel,

\[
\delta \mathcal A_\eta
=
\langle f|
V_{\rm eik}^{[\eta]}
\frac{1}{P_i^- - H_0 + i0\sigma_\eta}
\mathcal O_\Gamma
|i\rangle
+\text{declared companion ordering},
\]

using the smallest C3/C4 state space that supports the required test:

\[
\mathcal H_{\rm pilot}
=
\mathcal H_{\rm active+spectator}
\oplus
\mathcal H_{\rm active+spectator+g},
\]

with at least two OAM blocks, including `Lz=0` and one `|Lz|=1` block.

The implementation must:

- use the existing C3/C4 analytic state and common overlap objects;
- use the existing sector and active-slot identities;
- identify every interaction vertex and color factor;
- distinguish the eikonal denominator from the LF resolvent denominator;
- preserve quark flavor and positive-`x` antiquark identities;
- preserve the C4 ordered two-link gluon identity when an adjoint object is present;
- support `g -> 0`, cut-off, and OAM-block-off limits structurally;
- remain at `Wilson_order = 1`.

For the quark pilot, implement the fundamental color factor from explicit generators or contractions. For an adjoint algebraic check, implement the corresponding adjoint factor without claiming a full active-gluon T-odd TMD.

Do not fit the kernel. All masses, couplings, widths, and spectral weights are deterministic analytic benchmark parameters marked `VALIDATION_ONLY`.

Stable package requirements:

```text
C5.KERNEL.1
C5.KERNEL.2
C5.KERNEL.3
C5.WARD.1
```

The Ward test may be restricted to the declared analytic one-gluon pilot, but all attachments required by that pilot must be included. Record explicitly what has and has not been tested; do not claim full non-Abelian all-sector Ward closure.

---

## C5.5 — Full future/past antiunitary adapter

Implement a typed antiunitary link-reversal adapter that acts on the complete pilot identity and amplitude:

```text
complex conjugation
initial/final endpoint exchange
path orientation
path inverse or time-reversed path class
momentum reversal required by the convention
helicity/spin phase map
color representation/conjugation
ordered gluon-link transformation
operator projection identity
```

A raw subtraction of arrays labeled `FUTURE` and `PAST` is forbidden.

Define the validation-only link-even and link-odd combinations only after the full map:

\[
W_{\rm even}
=\frac12\left(
W^{[+]}+\Theta^{-1}W^{[-]}\Theta
\right),
\]

\[
W_{\rm odd}
=\frac12\left(
W^{[+]}-\Theta^{-1}W^{[-]}\Theta
\right).
\]

Required identities:

- future and past principal-value parts agree;
- cut/absorptive parts reverse sign;
- `W_even` is link even;
- `W_odd` is link odd;
- zero coupling, zero cut, or removal of the required OAM block gives exact zero for `W_odd` within the declared numerical tolerance.

Stable package requirements:

```text
C5.TIME.1
C5.TIME.2
C5.ZERO.1
```

These implement the pilot subset of `V3.TIME.1`, `V3.TIME.2`, and `V3.ZERO.1`.

---

## C5.6 — Distinct Sivers-like and Boer–Mulders-like projections

Using the shared rescattering kernel, implement two distinct validation projectors:

1. a **Sivers-like** target-transverse-spin/momentum projection;
2. a **Boer–Mulders-like** active-quark-transverse-spin/momentum projection.

They must differ in operator/helicity projection, even when they use the same radial state and rescattering kernel.

Use explicit validation-only names such as:

```text
SIVERS_LIKE_PILOT
BOER_MULDERS_LIKE_PILOT
```

Do not register them as physical `f1Tperp` or `h1perp` production TMDs.

For a minimal state

\[
\psi(\bm k_T)=u_0(k_T)+e^{i\phi_k}u_1(k_T),
\]

with a link-odd kernel `i eta K_01`, reproduce a benchmark of the form

\[
\mathcal I_{01}^{[\eta]}
=2\eta\,u_0u_1K_{01}\sin\phi_k.
\]

Mandatory zero tests:

- `u0 = 0`;
- `u1 = 0`;
- `K01 = 0`;
- `g = 0`;
- cut support disabled;
- wrong OAM block removed.

Mandatory distinction tests:

- the Sivers-like and Boer–Mulders-like projectors are not equal maps;
- swapping the projectors changes the result or fails a type check;
- no scalar `C(x,kT)` is introduced to impose proportionality;
- an operator lacking the required spin block cannot be projected successfully.

Stable package requirements:

```text
C5.QUARK.1
C5.QUARK.2
C5.OAM.1
```

These implement the pilot subset of `V3.QUARK.1`, `V3.QUARK.2`, and `V3.OAM.1`.

---

## C5.7 — Gluon identity and color algebra guardrails

C5 does **not** yet implement a complete active-gluon naive-T-odd calculation. It must nevertheless prove that the existing C4 gluon identity cannot be degraded by the Wilson pilot.

Retain and test:

- ordered two-link identity;
- adjoint representation;
- explicit `DIAGONAL_ADJOINT` status where that is the C4 identity;
- trace, helicity-antisymmetric, and symmetric-traceless projector identity;
- independent `f`- and `d`-type algebraic color projectors;
- `f^{abc} d^{abc} = 0` under the project normalization;
- link order and color class are independent fields.

A mixed ordered link pair may not be sorted canonically. Swapping it must either produce a different identity or fail where the operation is unsupported.

C5 must not produce one generic authoritative “gluon T-odd” table. Full dynamical active-gluon `f/d` projections are deferred to a later package.

Stable package requirements:

```text
C5.GLUON.1
C5.GLUON.2
```

These are guardrail-level subsets of `V3.GLUON.1` and `V3.GLUON.2`.

---

## C5.8 — Matching and scientific-status contract

Every C5 result must carry all unresolved physical matching requirements explicitly. At minimum:

```text
VALIDATION_ONLY
UNSUBTRACTED_REGULATED_PILOT
LINK_SHORTENING_REQUIRED
UV_MATCHING_REQUIRED
RAPIDITY_SOFT_MATCHING_REQUIRED
PHYSICAL_PROCESS_MAP_NOT_APPLIED
NO_EVOLUTION_APPLIED
WILSON_ORDER_1
```

Do not mark any of these complete.

Implement a minimal `PhaseBudget` or equivalent manifest with separate fields for:

```text
unsubtracted_hadronic_or_collinear_phase
soft_overlap_contribution
rapidity_counterterm_contribution
UV_matching_contribution
Glauber_or_process_contribution
unresolved_remainder
```

In C5, only the explicitly calculated unsubtracted pilot contribution is populated. The other fields remain typed unresolved quantities, not zeros unless a benchmark proves zero.

The C5 pilot must not be consumed by Volume IV nuclear composition, Volume V matching/evolution, a physical process object, or the production parent builder. The rejection reason must identify the first unsatisfied gate rather than returning a generic unsupported-operation error.

Stable package requirements:

```text
C5.STATUS.1
C5.STATUS.2
C5.SOFT.1
```

`C5.SOFT.1` establishes only that unresolved overlap is recorded and cannot be double counted. It does not claim full `V3.SOFT.1` completion.

---

## Analytic benchmark suite

### Benchmark C5-A — Semi-infinite Abelian line

For

\[
A_\mu(x)=\epsilon_\mu e^{-i\ell\cdot x},
\]

verify

\[
U_\eta^{(1)}
=-g e^{-i\ell\cdot a}
\frac{v\cdot\epsilon}{v\cdot\ell-i0\eta},
\]

and

\[
U_+^{(1)}-U_-^{(1)}
=-2i\pi g e^{-i\ell\cdot a}
(v\cdot\epsilon)\delta(v\cdot\ell).
\]

This benchmark fixes path, Fourier, coupling, and pole signs independently of the hadron state.

### Benchmark C5-B — Two-state LF cut

For two states with energies `E0`, `E1` and real matrix-element product `o v`, evaluate

\[
\mathcal A_\sigma=\frac{ov}{E_0-E_1+i0\sigma}.
\]

Verify:

- no absorptive part for an off-shell discrete pair without declared cut support;
- the declared continuum/finite-volume spectral rule reproduces the explicit cut;
- future/past cut signs are opposite;
- numerical broadening does not survive as a physical parameter.

### Benchmark C5-C — Minimal OAM interference

Use the existing C3 spin/OAM pilot state or a strict adapter to it. Verify the analytic link-odd interference, all zero tests, and distinct Sivers-like/Boer–Mulders-like projections.

### Benchmark C5-D — Color and ordered-link algebra

Verify fundamental and adjoint one-gluon color factors, total singlet/color-charge closure in the relevant C3/C4 state, `f/d` orthogonality, and ordered-link identity preservation. This is an algebraic guardrail, not a full gluon T-odd result.

### Benchmark C5-E — Cut-ledger double-counting rejection

Construct a deterministic case in which one physical on-shell support is presented through both an eikonal denominator and an LF resolvent representation. Without an explicit equivalence/subtraction record, composition must fail before numerical evaluation. With the declared equivalence, the contribution is counted exactly once.

---

## Required negative injections

Create stable ordered injection IDs and tests for all 48 failures below:

1. future path with the past eikonal pole;
2. past path with the future eikonal pole;
3. independent manual pole sign supplied by a caller;
4. endpoint reversal without color-word adjoint/conjugation;
5. path inverse composed on incompatible endpoint fibers;
6. raw future-minus-past array subtraction without the antiunitary adapter;
7. complex conjugation without momentum reversal;
8. complex conjugation without the required spin/helicity map;
9. link reversal without ordered-gluon-link transformation;
10. nonzero link-odd result at `g=0`;
11. nonzero link-odd result with cut support disabled;
12. nonzero link-odd result after removing a required OAM block;
13. finite `epsilon` stored as a physical phase width;
14. failure of finite-`epsilon` convergence to PV-plus-cut;
15. omitted cut-surface Jacobian;
16. duplicate physical cut counted in both eikonal and LF-resolvent ledgers;
17. algebraically equal denominators incorrectly deduplicated despite distinct cut provenance;
18. off-shell discrete state assigned an absorptive part without a continuum/finite-volume rule;
19. Sivers-like route using the Boer–Mulders-like projector;
20. Boer–Mulders-like route using the Sivers-like projector;
21. imposed scalar proportionality between the two projections;
22. wrong active species or flavor slot;
23. negative-`x` quark silently substituted for the positive-`x` antiquark identity;
24. nonzero skewness accepted by the zero-skewness pilot;
25. off-diagonal Fock-sector overlap without the named one-gluon rescattering source;
26. Wilson order 0 with a nonzero phase;
27. Wilson order greater than 1 accepted by C5;
28. fundamental path used with an adjoint operator or vice versa;
29. ordered gluon link pair silently sorted or swapped;
30. `f` color identity relabeled as `d` or vice versa;
31. generic gluon T-odd output created without color/link identity;
32. unresolved soft/rapidity matching marked complete;
33. C5 result passed to the Volume V evolution route;
34. C5 result passed to a physical `PROC` map;
35. C5 result inserted into the production 216-route registry;
36. C5 provenance node connected to the accepted production root;
37. any authoritative artifact changed;
38. any C3 or C4 benchmark/manifest changed;
39. pilot parameters fitted or optimized against production data;
40. arbitrary imaginary constant introduced anywhere in the authoritative C5 kernel;
41. C5 result passed to Volume IV nuclear composition without complete helicity-matrix exports;
42. C5 result passed to Volume IV nuclear composition without correlated proton/neutron microscopic members;
43. C5 result passed to Volume IV nuclear composition without phase/soft and covariance records;
44. C5 result passed to Volume V matching/evolution without a closed regulated operator basis;
45. C5 result passed to Volume V matching/evolution without an LF-to-QCD matching map;
46. C5 result passed to a process object without a declared link/color/Glauber map;
47. a Volume 0–V normative source or formalism index entry modified by the C5 implementation;
48. the C4 architecture coverage counts or source-integration manifest changed.

Additional injections are encouraged where they expose real repository-specific failure modes.

---

## Provenance and isolation

Create a C5-only provenance subgraph whose nodes and edges are disjoint from the production graph and from the immutable C3/C4 benchmark graphs except through explicit read-only ancestry references.

The graph must represent at least:

```text
analytic state
DERIVES_FROM common C3/C4 state definition

one-gluon kernel
ACTS_ON analytic state
USES bare Wilson path
USES eikonal pole
USES LF resolvent
USES cut ledger

link-odd correlator
DERIVES_FROM future amplitude
DERIVES_FROM time-reversed past amplitude

Sivers-like projection
PROJECTS_FROM link-odd correlator
ALTERNATIVE_OPERATOR_PROJECTION_TO Boer-Mulders-like projection

unsubtracted pilot
REQUIRES_MATCHING UV
REQUIRES_MATCHING RAPIDITY_SOFT
REQUIRES_MATCHING LINK_SHORTENING
EXCLUDED_FROM production root
```

The existing C4 provenance graph is sufficient for its Benchmark-F exclusions but is not the general Volume 0 `Provenance2Complex`. Do not mislabel the C5 extension as completing that general object. Record exactly which equivalence/subtraction two-cells are executable in C5 and which remain future work.

---

## Required code and documentation deliverables

Create or update, with exact paths adapted to the repository:

### Code

- validation-only bare Wilson/eikonal objects;
- pole/distribution evaluator;
- LF resolvent and intermediate-state cut objects;
- cut ledger;
- one-gluon rescattering kernel;
- full antiunitary future/past adapter;
- distinct Sivers-like and Boer–Mulders-like validation projectors;
- C5-only phase/matching-status manifest;
- C5-only provenance and isolation checks.

### Documentation

```text
docs/next_level/c5_implementation_report.md
docs/next_level/c5_api.md
docs/next_level/c5_requirement_coverage.json
docs/next_level/c5_benchmark_manifest.json
docs/next_level/c5_injection_manifest.json
docs/next_level/c5_cut_ledger_manifest.json
docs/next_level/c5_phase_budget.json
docs/next_level/c5_provenance_graph.json
docs/next_level/c5_regression_report.json
docs/next_level/c5_normative_integration_report.md
docs/next_level/c5_normative_source_integration.json
```

### ADRs

Create architecture decisions covering at least:

```text
c5-derived-eikonal-pole-sign
c5-explicit-cut-versus-numerical-broadening
c5-cut-provenance-and-double-counting
c5-full-antiunitary-link-reversal
c5-distinct-sivers-boer-mulders-projections
c5-validation-only-matching-status
c5-production-isolation
c5-volume-iv-nuclear-entry-gate
c5-volume-v-matching-evolution-entry-gate
```

### Persistent planning/handoff

Update the roadmap and handoff with:

- baseline and final commit;
- exact normative requirements covered;
- analytic benchmark residuals;
- all unresolved Volume III requirements;
- exact Volumes 0–V source paths and hashes consumed by C5;
- machine-readable status of the still-closed Volume IV nuclear and Volume V matching/evolution gates;
- exact recommended next package.

---

## Determinism and serialization

Every exported C5 object must serialize deterministically and retain:

```text
state/member identity
C3/C4 recoil and overlap identity
operator identity
path identity
representation
Wilson order
pole identity
intermediate-state identity
cut identity and ledger status
OAM/helicity block identity
projector identity
matching/scientific status
regulators and numerical tolerances
source commit and configuration hash
```

Round-trip serialization tests are mandatory. A complex array without this manifest is not an authoritative C5 result.

---

## Acceptance criteria

C5 is complete only when all of the following hold:

1. The exact formalism-integrated C4 baseline at `62125f0857e597e8f9548f279ae70b1634764a24` is reproduced before edits.
2. The complete final repository suite passes, including every C1–C4 test and injection.
3. All nine acceptance/report builders pass.
4. All 36 evidence rows pass.
5. All 162 atlas pages render.
6. The accepted registry remains exactly 216 routes.
7. The production provenance graph/default composition plan remain byte-identical or deterministically identical to C4.
8. All eight authoritative artifacts remain byte-identical.
9. C3 Benchmarks A–D and C4 Benchmarks E–F remain unchanged and passing.
10. C5 Benchmarks A–E pass with separately reported analytic, algebraic, cut, quadrature, and serialization residuals.
11. The eikonal pole sign is derived from path/Fourier/momentum-flow identity and cannot be independently overridden.
12. Direct finite-`epsilon` integration converges to the explicit PV-plus-cut result; `epsilon` is absent from physical output identity.
13. The two-state LF benchmark has zero absorptive part unless declared cut support exists.
14. The cut ledger rejects duplicate physical on-shell support.
15. Future/past principal-value parts agree and absorptive parts reverse sign after the full antiunitary map.
16. Zero coupling, zero cut, or removal of the required OAM block removes every link-odd pilot result.
17. Sivers-like and Boer–Mulders-like outputs are distinct projections of one kernel and have no imposed proportionality.
18. Ordered gluon links and color identities survive unchanged; no generic gluon T-odd production object is created.
19. Every C5 output retains unresolved UV, rapidity/soft, and link-shortening requirements.
20. No C5 object is reachable from the accepted production root or consumable by production, Volume IV nuclear-composition, Volume V matching/evolution, or physical process builders.
21. The Volume IV gate remains closed with explicit missing fields for helicity matrices, correlated proton/neutron members, phase/soft information, covariance, and partonic-versus-nuclear rescattering separation.
22. The Volume V gate remains closed with explicit missing fields for a closed regulated operator basis, LF-to-QCD matching, completed UV/rapidity/soft/link-shortening treatment, scheme/evolution identity, and process link/color/Glauber status.
23. The C4 architecture record remains exactly 25 requirements, 40 mismatch injections, 16 validation-only provenance nodes, and 8 immutable hashes.
24. `references/formalism_volume_index.md` still resolves Volumes 0–V, and the normative sources are byte-identical to the C4 source-integration baseline.
25. All 48 mandatory C5 negative injections fail with stable, structured diagnostics; any additional repository-specific injections are separately enumerated.
26. Documentation, JSON manifests, generated reports, and the C5 source-integration manifest are deterministic and internally consistent.
27. The working tree is clean after a local completion commit.
28. Nothing is pushed to a remote.

Do not declare C5 complete if any criterion is waived, downgraded, or replaced by a qualitative statement.

---

## Required final response from Codex

Report:

1. starting and final commit hashes;
2. push status;
3. exact test/builder/evidence/atlas/injection counts;
4. byte-regression status for all eight authoritative artifacts;
5. registry and production-provenance invariance;
6. files and public APIs created;
7. analytic results and maximum residuals for C5 Benchmarks A–E;
8. the exact mechanism producing the imaginary part;
9. proof that finite numerical broadening is not being treated as physics;
10. future/past and zero-limit results;
11. evidence that Sivers-like and Boer–Mulders-like projections are distinct;
12. unresolved matching and scientific limitations;
13. explicit Volume IV and Volume V gate status;
14. Volumes 0–V source paths/hashes used;
15. exact recommended next package.

The recommended next package should normally be a validation-only extension to independent active-gluon ordered-link and `f/d` rescattering channels plus soft/rapidity overlap accounting, but Codex must base its final recommendation on the actual C5 result and unresolved Volume III coverage.
