# C6 Codex Work Package

## Validation-only active-gluon ordered-link \(f/d\) rescattering and soft/rapidity-overlap pilot

### Authoritative baseline

Begin from the exact local C5 completion commit:

```text
c4aeb380bc3c23b8dcf2fb6a4528042de598cb48
```

The C5 starting ancestor was:

```text
62125f0857e597e8f9548f279ae70b1634764a24
```

Do not begin implementation unless:

1. the working tree is clean;
2. `HEAD` is the exact C5 commit above, or a documentation-only descendant with that commit in its ancestry;
3. the complete C5 regression reproduces exactly:
   - `679/679` tests passing;
   - `9/9` legacy acceptance/report builders passing;
   - `36/36` evidence rows passing;
   - `162/162` atlas pages rendering;
   - all `48/48` C5 negative injections passing;
   - all `40/40` C4 negative injections passing;
   - all `24/24` C3 negative injections passing;
   - all eight authoritative artifacts byte-identical;
   - the accepted production reduction registry unchanged at exactly `216` routes;
   - the production provenance graph and default composition plan unchanged;
4. the C5 benchmark manifest reproduces the recorded C5-A through C5-E residuals and identities;
5. the C5 validation graph remains disjoint from accepted production;
6. `references/formalism_volume_index.md` resolves the normative formalism sources used by C5.

The repository is intentionally ahead of `origin/main`. Do not use the remote branch as the baseline. Do not reset, rebase, squash, rewrite, or discard local user work. Do not push to any remote. Create one clean local completion commit only after every C6 acceptance gate passes.

If the current commit differs, identify the difference, prove that the C5 commit is an ancestor, reproduce the exact C5 baseline, and record the discrepancy before proceeding.

---

## Normative sources

Use the repository copies of the formalism and implementation records in this order:

1. Volume 0 architecture specification, resolved through `references/formalism_volume_index.md`;
2. `references/volume_i_regulated_light_front_foundations.tex`;
3. `references/volume_ii_common_nucleon_gtmd_overlaps.tex`;
4. `references/volume_iii_dynamical_wilson_lines.tex` — the primary physics specification for C6;
5. `references/volume_iv_matched_spin1_nuclear_dynamics.tex` — only for nuclear-interface gates that C6 must not cross;
6. `references/volume_v_matching_evolution_factorization.tex` — for matching, soft/rapidity, evolution, and process gates;
7. `docs/next_level/c5_api.md`;
8. `docs/next_level/c5_implementation_report.md`;
9. `docs/next_level/c5_normative_source_integration.json`;
10. all C1–C5 APIs, ADRs, manifests, requirement-coverage files, provenance files, and regression reports.

If Volume VI is present, index and hash it, but do not implement inference in C6.

Record the exact path and SHA-256 hash of every normative source used. The expected source hashes for the supplied TeX versions are:

```text
Volume III: 7abe76b5866fe6349b98dbe435303ee72d55ce539faf535d18d03691c8ddf5b7
Volume IV:  eec34c5520b7a23e89411d6688ede2a7f46784ca41cbe8b088e2cecbc4b81734
Volume V:   57fed5853e5983c83a4f675b8d218897c377e0713923e1d22f89d91468022e51
Volume VI:  568979e0fa0015a70795a7c27c4c98b992848085c982a7ee4eca0374fec72570
```

If repository hashes differ, do not overwrite them. Record the difference, compare content, and use the indexed authoritative repository source unless it is demonstrably stale or incomplete.

Do not modify a normative source merely to make a test pass.

---

## Scientific objective

C6 extends the validated C5 quark-like one-gluon Wilson-line/cut pilot to an **active-gluon correlator with two ordered adjoint gauge links and independent \(f^{abc}\)- and \(d^{abc}\)-type color channels**. It also implements the first executable, validation-only accounting of the soft/rapidity overlap at one Wilson order.

The required chain is

```text
C4 qqqg analytic state and active-gluon slot
    -> C5 bare Wilson segments, derived poles, LF resolvents, and cut ledgers
    -> two ordered adjoint Wilson-link legs
    -> active-gluon one-gluon rescattering kernel
    -> explicit three-adjoint color kernel
    -> independent normalized f- and d-type projections
    -> existing gluon trace / helicity-antisymmetric / symmetric-traceless projectors
    -> full antiunitary link-pair reversal
    -> validation-only link-even and link-odd active-gluon results
    -> one-loop analytic soft-overlap subtraction and rapidity-budget closure
```

C6 must prove that:

1. ordered link identity and color-contraction identity remain independent;
2. the active-gluon imaginary part comes only from a derived pole and declared cut support;
3. \(f\)- and \(d\)-type amplitudes are independently generated, projected, serialized, and tested;
4. trace, helicity-antisymmetric, and symmetric-traceless active-gluon projections are executable views of one common tensor parent;
5. future/past reversal acts on the full ordered pair and all color, spin, momentum, and operator data;
6. the soft/rapidity overlap is represented explicitly and subtracted exactly once in an analytic benchmark;
7. no C6 output is promoted to a physical QCD TMD, evolution input, nuclear object, or process prediction.

Completeness and correctness are the objective. Do not optimize for quickness.

---

## C6 is not

C6 is not:

- a fitted gluon TMD model;
- a physical gluon Sivers extraction;
- a universal process-level \(f/d\) mixture;
- a complete non-Abelian Wilson-line resummation;
- a second-order Wilson calculation;
- a complete Collins–Soper kernel calculation;
- a physical soft-subtracted TMD in a named continuum scheme;
- an LF-to-QCD matching calculation;
- a small-\(x\) odderon replacement for moderate-\(x\) dynamics;
- a nuclear rescattering or coherent-shadowing calculation;
- a process prediction;
- permission to modify the accepted phenomenological boundary.

The C6 result must remain validation-only and disconnected from accepted production.

---

## Immutable physics and regression constraints

Do not change:

- any accepted quark, antiquark, or gluon parent value;
- the 216-entry production reduction registry;
- the C2 production provenance graph or default composition plan;
- any C3, C4, or C5 benchmark result, manifest, parameter, type identity, or validation-only output;
- the C1–C5 coordinate, recoil, rank, mass, Fourier, sector, path, operator, scheme, or map-class conventions;
- the accepted gluon tensor decomposition;
- any tensor-polarization sign convention;
- any authoritative CSV/JSON artifact, row order, formatting, or hash;
- any evidence classification or atlas output.

Do not add:

- one generic “gluon T-odd” scalar or array;
- an implicit alias between one link pair and one color class;
- a process-level \(C_f\) or \(C_d\) weight;
- an arbitrary imaginary coefficient;
- a fitted phase, normalization, or transverse width;
- physical significance for finite numerical \(\epsilon\);
- an asserted soft subtraction with no overlap record;
- an asserted rapidity cancellation with no regulator derivative test;
- a default sum \(F_g^{(f)}+F_g^{(d)}\);
- a physical small-\(x\) odderon claim;
- a production fallback intended only to make tests pass.

---

## Required implementation strategy

### Reuse the existing type spine

Do not create a second coordinate, rank, sector, path, operator, map, active-slot, recoil, overlap, gluon-projector, cut-ledger, phase-budget, or provenance system.

Reuse the actual C1–C5 repository APIs, including the repository equivalents of:

```text
formal.coordinates
formal.transverse_rank
formal.sector_space
formal.gauge_path
formal.operator_identity
formal.maps
formal.diagnostics
pilot zero-skewness frame and recoil authority
pilot analytic qqqg state and active-gluon records
pilot common overlap evaluator
C4 gluon trace/helicity/symmetric-traceless projectors
C5 bare Wilson segments
C5 derived pole prescriptions
C5 distributional integration
C5 LF resolvents and intermediate-state cuts
C5 CutLedger
C5 OneGluonPilotKernel
C5 AntiunitaryLinkReversal
C5 PhaseBudget
```

A new validation-only subpackage such as

```text
src/deuteron_wigner/pilot/active_gluon/
```

is recommended, but adapt to the actual repository architecture. Document every public API.

### Keep map classes distinct

Maintain the Volume 0 map separation:

- state amplitudes, Wilson vertices, color couplers, and rescattering kernels: `AMP`;
- a genuine partial trace or selected incoherent outcome only: `DENS`;
- soft-overlap subtraction and regulator conversion: `MATCH`;
- gluon polarization and color projections: `RED`;
- process color weighting or cross-section assembly: `PROC`, which remains forbidden in C6.

No implicit array-level composition across map classes is permitted.

---

# C6.1 — Ordered two-link active-gluon identity

Implement or extend a typed active-gluon operator identity representing

\[
\Gamma_g^{ij[U,U']}
\sim
\langle P'|
F_a^{+i}(a)\,U_{ab}[a,b]\,
F_b^{+j}(b)\,U'_{ba}[b,a]
|P\rangle.
\]

The identity must contain at least:

```text
active_species = GLUON
field_strength_left_index
field_strength_right_index
left_adjoint_path_id
right_adjoint_path_id
ordered_pair_id
left_orientation
right_orientation
left_endpoint_fibers
right_endpoint_fibers
left_transverse_closure
right_transverse_closure
trace_closure_identity
representation = ADJOINT
color_status = DIAGONAL_ADJOINT
Wilson_order = 1
rapidity_regulator_id
soft_route_id
operator_scheme_status
source_state_member_id
```

The ordered pair is not a set. Swapping the paths, reversing only one path, or changing one closure creates a different operator identity.

Support the simple validation link pairs

\[
[+,+],\qquad[-,-],\qquad[+,-],\qquad[-,+],
\]

without aliasing them to a color class.

Required stable identifiers:

```text
C6.GLID.1  ordered pair is part of operator identity
C6.GLID.2  both legs are adjoint and endpoint-compatible
C6.GLID.3  pair swap and one-leg reversal change identity
C6.GLID.4  serialization preserves exact order and closures
```

---

# C6.2 — Active-gluon analytic state and common tensor parent

Reuse the C4 `qqqg` validation family and its normalized color-octet-times-adjoint singlet construction. Extend only the validation fixture as needed so that the active gluon carries:

- a positive longitudinal momentum fraction;
- transverse momentum;
- helicity \(\lambda_g=\pm1\);
- at least \(L_z=0\) and \(|L_z|=1\) amplitude blocks;
- explicit active-gluon slot identity;
- source and target Fock-sector identity;
- the existing common microscopic member identity.

Do not replace the C4 color state. Do not create a singlet `qqq` state times a free gluon.

Construct one common active-gluon tensor parent

\[
K^{ij;abc}_{\Lambda'\Lambda}
(x,\bm k_T,\bm\Delta_T;[U,U'])
\]

before any color or polarization projection. The parent must retain:

- target helicities;
- active-gluon helicities;
- transverse indices \(i,j\);
- three adjoint color indices needed for one gluonic-pole insertion;
- ordered link-pair identity;
- cut identity;
- Wilson order;
- OAM block ancestry;
- regulator and phase-budget identity.

No projected named object may become the stored parent.

Stable identifiers:

```text
C6.STATE.1 active-gluon slot is explicit and positive-x
C6.STATE.2 common tensor parent precedes all RED maps
C6.STATE.3 OAM and helicity blocks remain inspectable
C6.STATE.4 C4 normalization/color ledgers remain unchanged
```

---

# C6.3 — One-gluon active-gluon rescattering kernel

Extend the C5 one-gluon kernel to the active-gluon operator. Both Wilson legs and all declared spectator/endpoint attachments required by the analytic benchmark must be represented explicitly.

Every contribution must retain:

```text
source_state
intermediate_state
active_gluon_slot
emitted_or_exchanged_gluon
left_or_right_link_attachment
color_ordering
LF_energy_denominator
orientation-derived eikonal denominator
pole_prescription
cut_support_id
OAM_interference_id
Ward_attachment_set
```

The absorptive contribution is nonzero only when all of the following are present:

1. nonzero one-gluon coupling;
2. declared physical cut support;
3. a nonzero active-gluon color kernel;
4. the required \(L_z=0\)/\(|L_z|=1\) interference;
5. a complete ordered-link attachment set.

Removing any item must give exact zero.

Finite numerical broadening remains a convergence oracle only. It may not enter the physical result identity or uncertainty envelope.

Stable identifiers:

```text
C6.DYN.1 active-gluon pole is derived from path data
C6.DYN.2 physical cut support is required
C6.DYN.3 OAM removal gives exact zero
C6.DYN.4 incomplete link attachment fails Ward closure
C6.DYN.5 epsilon is never physical
```

---

# C6.4 — Independent \(f\)- and \(d\)-type color channels

For \(SU(3)\), use

\[
\mathcal C_f^{abc}=if^{abc},
\qquad
\mathcal C_d^{abc}=d^{abc},
\]

with

\[
f^{abc}d^{abc}=0,
\qquad
f^{abc}f^{abc}=24,
\qquad
d^{abc}d^{abc}=\frac{40}{3}.
\]

For a three-adjoint kernel \(K^{abc}\), implement the normalized projections

\[
K_f=\frac{-if^{abc}K^{abc}}{24},
\qquad
K_d=\frac{d^{abc}K^{abc}}{40/3}.
\]

If the benchmark kernel is declared to lie in the \(f/d\) subspace, verify reconstruction:

\[
K^{abc}_{\parallel}
=if^{abc}K_f+d^{abc}K_d.
\]

Always report the orthogonal residual

\[
K_\perp=K-K_{\parallel}.
\]

Do not force a general three-adjoint tensor into the two-channel subspace silently.

The implementation must distinguish:

1. ordered link topology;
2. color ordering at the one-gluon attachments;
3. normalized \(f/d\) projection;
4. later process weights, which are not implemented.

Construct the antisymmetric and symmetric color-ordering benchmarks from explicit ordered color products or commutator/anticommutator couplers. Do not insert `f_amplitude` and `d_amplitude` as unrelated fitted scalar inputs.

At minimum, generate independent validation records for both \(f\) and \(d\) channels. A channel not generated by a particular color-flow benchmark must be marked `NOT_GENERATED_BY_THIS_BENCHMARK`, not assigned a copied value.

Stable identifiers:

```text
C6.COLOR.1 exact SU(3) norms and f-d orthogonality
C6.COLOR.2 normalized f projection
C6.COLOR.3 normalized d projection
C6.COLOR.4 reconstruction plus orthogonal residual
C6.COLOR.5 link identity and color identity remain independent
C6.COLOR.6 no default f+d mixture
```

---

# C6.5 — Gluon polarization projectors from one common parent

Reuse the executable C4 projectors for the transverse gluon tensor:

- trace / unpolarized part;
- helicity-antisymmetric part;
- symmetric-traceless / linear-polarization part.

Apply them after the active-gluon rescattering tensor and color projections are formed. Do not create separate dynamical kernels for each projector.

For each supported ordered-link and color channel, expose validation-only projections such as:

```text
GLUON_TRACE_LINK_ODD_F_PILOT
GLUON_TRACE_LINK_ODD_D_PILOT
GLUON_HELICITY_ANTISYMMETRIC_LINK_ODD_F_PILOT
GLUON_HELICITY_ANTISYMMETRIC_LINK_ODD_D_PILOT
GLUON_SYMMETRIC_TRACELESS_LINK_ODD_F_PILOT
GLUON_SYMMETRIC_TRACELESS_LINK_ODD_D_PILOT
```

These are algebraic pilot labels, not production TMD names.

Verify exact tensor reconstruction:

\[
\Gamma^{ij}
=\Gamma_{\rm tr}^{ij}
+\Gamma_{\rm asym}^{ij}
+\Gamma_{\rm ST}^{ij}.
\]

Verify that changing the polarization projector does not change path, cut, color, state-member, or phase-budget identity.

Stable identifiers:

```text
C6.POL.1 common tensor parent supplies all projections
C6.POL.2 trace/asym/ST reconstruction closes
C6.POL.3 projector identities are serialized
C6.POL.4 no scalar phase copied across projectors
```

---

# C6.6 — Full antiunitary reversal of an ordered link pair

Extend the C5 antiunitary adapter to the two-link gluon operator. It must transform:

- complex conjugation;
- incoming/outgoing momentum fibers;
- target and active-gluon helicity phases;
- \(\bm k_T\) and \(\bm\Delta_T\);
- left and right endpoints;
- each path orientation;
- path inversion;
- pair order where required by the operator definition;
- adjoint representation;
- trace closure;
- color ordering;
- \(f/d\) projection identity;
- transverse tensor indices.

For the simple reference pairs, verify the typed transformations

```text
[+,+] <-> [-,-]
[+,-] <-> [-,+]
```

under the declared convention. Do not hard-code only these strings; derive the transformed pair from the path objects.

Define link-even and link-odd results only after the complete adapter:

\[
W_{\rm even}^{[U,U'];c}
=\frac12\left(
W^{[U,U'];c}+\Theta^{-1}W^{[U_\Theta,U'_\Theta];c}\Theta
\right),
\]

\[
W_{\rm odd}^{[U,U'];c}
=\frac12\left(
W^{[U,U'];c}-\Theta^{-1}W^{[U_\Theta,U'_\Theta];c}\Theta
\right).
\]

Required exact zero limits:

\[
g\to0 \Rightarrow W_{\rm odd}=0,
\]

\[
\text{cut support}\to0 \Rightarrow W_{\rm odd}=0,
\]

\[
L_z\text{ interference removed}\Rightarrow W_{\rm odd}=0.
\]

Stable identifiers:

```text
C6.REV.1 complete two-link antiunitary transformation
C6.REV.2 exact future/past pairing
C6.REV.3 exact zero-coupling/cut/OAM limits
C6.REV.4 color and polarization identities survive reversal
```

---

# C6.7 — Soft-overlap and rapidity-budget accounting

C6 does not perform full physical QCD matching. It must nevertheless make the first-order soft/rapidity overlap executable and auditable.

Implement typed records such as:

```text
RapidityRegulatorSpec
ModeRegionId
SoftOverlapRegion
UnsubtractedFirstOrderTerm
SoftFactorFirstOrderTerm
RapidityCounterterm
UVStatus
OverlapSubtractionRelation
SoftRouteId
GluonPhaseBudgetEntry
GluonPhaseBudget
```

At first order, represent

\[
W_{\rm sub}^{(1)}
=W_{\rm unsub}^{(1)}
-\frac12 S^{(1)}W^{(0)}
+R_{\rm rap}^{(1)}W^{(0)}
+Z_{\rm UV}^{(1)}W^{(0)}.
\]

For C6, use an analytic validation regulator and coefficients, not a claim of a completed continuum scheme. The benchmark must contain an explicit rapidity-sensitive overlap term shared by the unsubtracted collinear object and soft factor. It must verify:

1. the overlap is present in both sources with explicit ancestry;
2. it is subtracted exactly once;
3. the subtracted benchmark is independent of the analytic rapidity-log variable to the declared order;
4. a missing half-soft subtraction leaves a nonzero regulator derivative;
5. a duplicate subtraction leaves the opposite nonzero residual;
6. color-channel and polarization labels survive the subtraction;
7. any unresolved UV finite matching is recorded as unresolved, not set to zero.

Define a residual such as

\[
\epsilon_{\rm rap}
=\left\|
\frac{\partial}{\partial L_{\rm rap}}
W_{\rm sub}^{(1)}
\right\|,
\]

and require exact or analytic-tolerance closure for the toy benchmark.

Implement the two Volume III soft-route identities:

```text
BOUNDARY_ONLY_RESCATTERING
JOINT_MICROSCOPIC_SOFT_SECTOR
```

C6 must implement the validation-only boundary-only route. The joint route may be represented as `NOT_IMPLEMENTED`, but selecting both routes or composing them without an explicit overlap matching map must fail closed.

Every result must retain at least:

```text
VALIDATION_ONLY
UNSUBTRACTED_ACTIVE_GLUON_PILOT
SOFT_OVERLAP_ACCOUNTED_ANALYTICALLY
RAPIDITY_CANCELLATION_BENCHMARKED
UV_MATCHING_REQUIRED
PHYSICAL_TMD_SCHEME_NOT_ASSIGNED
LINK_SHORTENING_REQUIRED
NO_EVOLUTION_APPLIED
NO_PROCESS_MAP_APPLIED
WILSON_ORDER_1
```

Do not label the result `RENORMALIZED_TMD` or `MATCHING_COMPLETE`.

Stable identifiers:

```text
C6.SOFT.1 explicit overlap region and ancestry
C6.SOFT.2 half-soft subtraction exactly once
C6.RAP.1 analytic rapidity derivative closes
C6.RAP.2 missing/duplicate subtraction is detected
C6.ROUTE.1 boundary-only and joint-soft routes are exclusive
C6.STATUS.1 unresolved matching status remains fail-closed
```

---

# C6.8 — Cut ledger, overlap ledger, and finite two-cells

Extend the C5 `CutLedger` and C2/C4/C5 provenance infrastructure rather than creating a parallel graph.

The implementation must distinguish:

- two representations of the same physical cut: `EQUIVALENT_COUNT_ONCE`;
- a collinear/soft mode overlap: `OVERLAP_SUBTRACT`;
- mutually exclusive soft routes: `ALTERNATIVE_TO`;
- a true additive contribution: `ADDS_TO` only when physically independent;
- an unresolved matching remainder: `REMAINDER_OF`.

A numerical equality between two terms is not enough to deduplicate them. Conversely, different object IDs do not make the same physical overlap independent.

Provide executable finite two-cells showing that:

1. the same on-shell support is counted once;
2. the same soft region is subtracted once;
3. \(f\) and \(d\) channels are never deduplicated merely because their scalar benchmark values happen to agree;
4. left- and right-link attachments are not merged when they are physically distinct;
5. a boundary-only rescattering contribution cannot also enter a joint microscopic Collins–Soper kernel without an explicit relation.

State clearly that this remains a finite executable subset of the general Volume 0 `Provenance2Complex`, not its completion.

Stable identifiers:

```text
C6.PROV.1 cut equivalence is explicit
C6.PROV.2 soft overlap subtraction is explicit
C6.PROV.3 f/d channels remain independent
C6.PROV.4 soft routes are exclusive
C6.PROV.5 provenance trace reaches state, path, cut, color, and overlap terms
```

---

# C6.9 — Active-gluon Ward and color closure

Extend the restricted C5 Ward benchmark to the active-gluon two-link operator.

The analytic pilot must include all attachments required by its declared truncation, including both ordered link legs and the retained spectator/color couplers. Replacing the exchanged-gluon polarization by its momentum must give a residual that closes to analytic tolerance:

\[
\epsilon_{\rm Ward}
=\left\|\sum_i \ell_\mu\mathcal K_i^{\mu a}\right\|.
\]

Required tests:

- complete attachment set closes;
- deleting the left-link attachment fails;
- deleting the right-link attachment fails;
- omitting the adjoint generator fails;
- replacing the C4 color-singlet `qqqg` state by singlet `qqq` times a free gluon fails;
- color-singlet total-generator closure remains unchanged;
- the Ward test is evaluated separately in \(f\) and \(d\) channels;
- soft-overlap bookkeeping does not repair a failed hard/color Ward identity.

Do not claim full all-sector QCD Ward closure. Record the exact pilot scope.

Stable identifiers:

```text
C6.WARD.1 complete pilot attachment set closes
C6.WARD.2 missing attachments fail
C6.WARD.3 color-singlet state is required
C6.WARD.4 f/d Ward residuals are reported separately
```

---

# C6.10 — Analytic benchmark suite

Implement at least the following deterministic benchmark families.

## C6-A: ordered two-link algebra

Verify:

- exact storage and round-trip serialization of `[+,+]`, `[-,-]`, `[+,-]`, `[-,+]`;
- pair swap changes identity;
- one-leg reversal changes identity;
- full antiunitary reversal maps the declared pairs correctly;
- both links remain adjoint and endpoint compatible.

## C6-B: \(SU(3)\) \(f/d\) projection and reconstruction

Use synthetic kernels constructed from explicit antisymmetric and symmetric color orderings. Verify:

- \(f\cdot d=0\);
- norms \(24\) and \(40/3\);
- exact normalized projection;
- exact reconstruction inside the \(f/d\) subspace;
- nonzero reported orthogonal residual for an injected tensor outside that subspace;
- no implicit link/color alias.

## C6-C: active-gluon absorptive kernel

Using the common C4/C5 analytic state and cut machinery, verify:

- nonzero link-odd result only with coupling, cut, color, and OAM support;
- exact zero when each required ingredient is removed;
- opposite future/past sign after the full two-link adapter;
- finite-\(\epsilon\) convergence without physical \(\epsilon\) identity.

## C6-D: gluon tensor projection

Verify:

- trace, antisymmetric, and symmetric-traceless projections from one common parent;
- exact reconstruction;
- separate \(f\) and \(d\) records;
- projector change does not modify state/path/cut/color ancestry.

## C6-E: analytic soft-overlap subtraction

Construct an explicit first-order benchmark with a shared rapidity-sensitive overlap. Verify:

- one half-soft subtraction removes the overlap exactly;
- missing subtraction leaves nonzero \(\epsilon_{\rm rap}\);
- duplicate subtraction leaves nonzero residual with opposite sign;
- the finite boundary remains color- and polarization-resolved;
- unresolved UV matching remains marked unresolved.

## C6-F: soft-route exclusivity

Verify:

- boundary-only route is executable;
- joint-soft route is represented but not silently implemented;
- selecting both fails;
- transferring a boundary-only ladder into a Collins–Soper kernel without an overlap relation fails.

## C6-G: Ward and provenance closure

Verify:

- complete analytic attachment set closes;
- missing link attachment fails;
- duplicate physical cut is counted once only with an explicit two-cell;
- duplicate soft region is subtracted once only with an explicit two-cell;
- \(f\) and \(d\) channels are never deduplicated.

All benchmark residuals, tolerances, formulas, and exact/approximate classifications must be written to a machine-readable manifest.

---

# C6.11 — Mandatory negative-injection suite

Implement at least **56** ordered, stable-ID negative injections. Include at minimum:

1. swapped ordered link pair accepted as identical;
2. one-leg reversal accepted as the same identity;
3. fundamental representation used for an active-gluon Wilson leg;
4. missing trace closure;
5. incomplete endpoint fiber;
6. invalid `DIAGONAL_ADJOINT` status;
7. generic gluon T-odd object with no ordered pair;
8. generic gluon T-odd object with no color class;
9. implicit `[+,+] -> f` enum alias;
10. implicit `[+,-] -> d` enum alias;
11. default \(f+d\) mixture;
12. wrong \(f\) normalization;
13. wrong \(d\) normalization;
14. nonzero claimed \(f\cdot d\);
15. forced reconstruction of a tensor with nonzero orthogonal residual;
16. color scalar inserted instead of explicit color ordering;
17. singlet `qqq` times free gluon;
18. omitted adjoint generator;
19. duplicate active-gluon slot;
20. wrong active species;
21. nonpositive active-gluon \(x\);
22. nonzero skewness accepted;
23. unsupported off-diagonal Fock transition;
24. Wilson order other than one accepted silently;
25. arbitrary imaginary coefficient;
26. finite \(\epsilon\) marked physical;
27. nonzero absorption with no cut support;
28. nonzero link-odd result with zero coupling;
29. nonzero link-odd result with OAM block removed;
30. incomplete antiunitary reversal;
31. future/past labels subtracted without transforming the operator;
32. color class lost during reversal;
33. polarization projector changes path identity;
34. independent kernels constructed separately for trace/asym/ST;
35. tensor reconstruction failure hidden by clipping;
36. missing soft-overlap ancestry;
37. missing half-soft subtraction;
38. duplicate soft subtraction;
39. rapidity derivative not checked;
40. regulator-dependent result declared complete;
41. unresolved UV term silently set to zero;
42. boundary-only and joint-soft routes selected together;
43. boundary rescattering counted again in a microscopic CS kernel;
44. physical TMD scheme assigned without matching;
45. link shortening declared complete;
46. evolution attempted;
47. physical process map attempted;
48. process \(C_f/C_d\) weights assigned;
49. nuclear composition attempted;
50. partonic rescattering identified with coherent nuclear rescattering;
51. duplicate cut with no equivalence relation;
52. distinct cuts deduplicated by numerical equality;
53. \(f\) and \(d\) channels deduplicated by equal scalar values;
54. missing left-link Ward attachment;
55. missing right-link Ward attachment;
56. production promotion attempted;
57. accepted registry modified;
58. production provenance modified;
59. authoritative artifact modified;
60. normative source modified to pass a test.

More than 56 is acceptable. The final manifest must enumerate every injection, expected diagnostic code, observed result, and stable ordering.

---

# C6.12 — Downstream gates that remain closed

## Volume IV nuclear gate

No C6 result may enter deuteron/nuclear composition until a later package supplies:

- complete nucleon helicity-matrix exports;
- correlated proton/neutron microscopic members;
- compatible phase/soft records;
- covariance/shared-member propagation;
- an explicit subtraction separating the partonic staple from coherent nuclear rescattering;
- matched nuclear operators and currents.

## Volume V QCD matching/evolution gate

No C6 result may be evolved or used in a physical process until a later package supplies:

- a closed regulated operator basis;
- LF-to-QCD matching;
- UV renormalization;
- rapidity and soft completion in a declared scheme;
- link shortening where appropriate;
- a rank-aware evolution identity;
- a process-qualified link/color/Glauber map;
- hard factors and fixed-order subtraction.

## Volume VI inference gate

No C6 parameter may be calibrated to data until a later package supplies:

- shared parameter ownership;
- a typed likelihood;
- correlated covariance and discrepancy models;
- a calibration/holdout split;
- a posterior-member store preserving all color/path/state identities.

Represent every gate in machine-readable status and test it fail-closed.

---

# Required deliverables

Create at least:

```text
docs/next_level/c6_implementation_report.md
docs/next_level/c6_api.md
docs/next_level/c6_requirement_coverage.json
docs/next_level/c6_normative_source_integration.json
docs/next_level/c6_active_gluon_channel_registry.json
docs/next_level/c6_ordered_link_manifest.json
docs/next_level/c6_color_projection_manifest.json
docs/next_level/c6_soft_overlap_manifest.json
docs/next_level/c6_phase_budget_manifest.json
docs/next_level/c6_benchmark_manifest.json
docs/next_level/c6_injection_manifest.json
docs/next_level/c6_regression_report.json
```

Add ADRs covering at least:

```text
active-gluon ordered two-link identity
independence of link topology and f/d color projection
common tensor parent before polarization projection
analytic boundary-only soft-overlap route
rapidity-regulator benchmark status
finite two-cell cut/overlap accounting
```

Update the persistent roadmap/handoff with:

- starting and final commits;
- exact tests/builders/evidence/atlas counts;
- benchmark residuals;
- injection count;
- all eight artifact hashes;
- source hashes;
- unresolved Volume III/IV/V/VI gates;
- the exact recommended C7 package.

All JSON outputs must be deterministic, machine-readable, schema-versioned, and stable under repeated generation.

---

# Final acceptance criteria

C6 is complete only when all of the following are satisfied:

1. The exact C5 baseline reproduces before edits.
2. The full existing regression remains passing.
3. All eight authoritative artifacts remain byte-identical.
4. The production registry remains exactly 216 routes.
5. Production provenance and default composition remain unchanged.
6. C3, C4, and C5 benchmark and injection manifests remain unchanged and passing.
7. An active-gluon common tensor parent exists before color or polarization projection.
8. Two ordered adjoint links are retained in every active-gluon identity.
9. Link topology and color class are independent fields.
10. \(f\)- and \(d\)-type projections are normalized, orthogonal, independently serialized, and reconstruct their declared subspace.
11. The orthogonal color residual is reported rather than discarded.
12. Trace, helicity-antisymmetric, and symmetric-traceless projectors reconstruct the common tensor.
13. The active-gluon imaginary part comes only from derived poles, declared cuts, and identified OAM interference.
14. All zero-coupling, zero-cut, and zero-OAM limits are exact.
15. Full two-link antiunitary reversal passes.
16. The analytic soft-overlap is subtracted exactly once.
17. The rapidity-regulator derivative closes for the benchmark.
18. Missing and duplicate subtraction tests fail with stable diagnostics.
19. Boundary-only and joint-soft routes are mutually exclusive.
20. The active-gluon Ward benchmark closes only with the complete attachment/color set.
21. At least 56 mandatory negative injections pass.
22. Every result remains validation-only and carries unresolved UV/matching/evolution/process status.
23. Nuclear, evolution, process, and inference gates fail closed.
24. Documentation and JSON manifests are complete, deterministic, and internally consistent.
25. The working tree is clean after one local completion commit.
26. Nothing is pushed.

Do not declare C6 complete if any criterion is unmet.

---

# Recommended exact next package after C6

If C6 passes, recommend **C7: second-order non-Abelian Wilson-line convergence and common-state Ward closure**, still validation-only. C7 should compare strict Dyson and Magnus representations through second order, include connected non-Abelian color structures, test eikonal-order convergence, extend the phase budget beyond one gluonic pole, and preserve the independent active-gluon \(f/d\) channels.

Do not begin C7 inside C6.

---

# Final response format

Report:

1. starting commit and final local commit;
2. whether anything was pushed;
3. full tests/builders/evidence/atlas counts;
4. C3/C4/C5/C6 injection counts;
5. ordered-link and active-gluon channel counts;
6. \(f/d\) projection and reconstruction residuals;
7. polarization reconstruction residuals;
8. future/past and all zero-limit residuals;
9. soft-overlap and rapidity-budget residuals;
10. Ward residuals;
11. all eight artifact hashes and whether they are byte-identical;
12. confirmation that the 216-route production registry and production provenance are unchanged;
13. files created;
14. remaining formalism gaps;
15. the exact recommended C7 task.

Do not use language implying that C6 is a physical gluon TMD prediction, a completed TMD scheme, or a complete Volume III implementation.
