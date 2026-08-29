# Codex Work Package C3

## Title

**Zero-skewness momentum-fiber, recoil-map, and analytic common-overlap pilot**

## Repository and immutable baseline

Repository: `uva-spin/DeuteronWigner`

Required C2 baseline commit:

```text
5063c002e763f3d6a0affc774ec6b124a539f0be
```

Required ancestry:

```text
4613318aa7e262e7482978c4198d8e72a4c73c09  # C1
5d4641f31d6a472c27ceed982856e65d0ff4c3cb  # C0
```

Begin from a clean repository state containing C2 commit `5063c002e763f3d6a0affc774ec6b124a539f0be`. If legitimate documentation-only commits have subsequently added Volumes I--III or updated the roadmap, retain them after verifying that the C2 commit is an ancestor and that the complete C2 regression baseline still passes. Do not reset, overwrite, or discard legitimate later work.

Before changing code, verify and record the complete C2 baseline:

- `519/519` tests pass;
- all nine acceptance/report builders pass;
- `36/36` evidence rows pass;
- all `162/162` atlas pages render;
- the complete C1 and C2 mismatch-injection suites pass;
- all eight authoritative parent/correlator files have the hashes recorded in `docs/next_level/c2_regression_report.json` and remain byte-identical to C1;
- the accepted native reduction registry contains exactly the C2 authoritative entries, reported as 216 reductions: 72 quark, 72 antiquark, and 72 gluon;
- the accepted provenance graph and deterministic default composition plan reproduce the C2 manifests;
- the production resolved-parent builder executes the native typed reduction registry without changing output bytes.

If the observed baseline differs, diagnose it before implementation. Do not weaken tests, schemas, graph restrictions, mismatch injections, evidence rules, tolerances, or hash checks to make the baseline pass.

## Normative sources

Read completely before implementation, using the actual repository paths if an established naming convention differs:

1. the corrected Volume 0 algebraic/geometric architecture specification;
2. `references/volume_i_regulated_light_front_foundations.tex`;
3. `references/volume_ii_common_nucleon_gtmd_overlaps.tex`;
4. `references/volume_iii_dynamical_wilson_lines.tex` only for the zero-rescattering handoff contract and strict non-goals;
5. `references/model_construction_note.tex`;
6. the original GTMD-first formalism note, if retained in `references/`;
7. `docs/next_level/stage0_repository_audit.md`;
8. `docs/next_level/stageA_migration_plan.md`;
9. all architecture decisions under `docs/next_level/architecture_decisions/`;
10. `docs/next_level/c1_implementation_report.md` and `docs/next_level/c1_api.md`;
11. all C1 machine-readable manifests and regression reports;
12. `docs/next_level/c2_implementation_report.md`;
13. `docs/next_level/c2_api.md`;
14. `docs/next_level/c2_reduction_registry.json`;
15. `docs/next_level/c2_provenance_graph.json`;
16. `docs/next_level/c2_composition_manifest.json`;
17. `docs/next_level/c2_regression_report.json`;
18. `docs/next_level/c2_requirement_coverage.json`;
19. `docs/next_level/c2_unresolved_formalism_gaps.md`;
20. the persistent roadmap and current handoff notes.

C2 reported that Volumes I and II were absent during its run. If any normative volume is still absent, do not invent its contents. Record the missing path, use the equations and requirements reproduced explicitly in this work package, and continue all work that is unambiguous. The final report must state which normative documents were actually present.

## Stable requirement identifiers

The stable requirement identifiers for this work package are:

- `C3.BASELINE`
- `C3.ISOLATE`
- `C3.FIBER`
- `C3.CONFIG`
- `C3.RECOIL`
- `C3.STATE`
- `C3.KERNEL`
- `C3.OVERLAP`
- `C3.BENCH_A`
- `C3.BENCH_B`
- `C3.BENCH_C`
- `C3.BENCH_D`
- `C3.HERMITICITY`
- `C3.NUMBER`
- `C3.COLOR`
- `C3.REDUCTION_BRIDGE`
- `C3.PROVENANCE`
- `C3.INJECT`
- `C3.CONVERGENCE`
- `C3.REGRESS`
- `C3.DOC`

Every identifier must appear in a machine-readable coverage report with implementation locations, tests, status, residuals, and unresolved limitations.

## Primary objective

Implement the first **microscopic-formal analytic pilot** of the Volume II common-parent program:

1. typed incoming, outgoing, and average light-front momentum fibers at zero skewness;
2. one authoritative symmetric-`xi=0` active/spectator recoil map;
3. normalized analytic toy Fock states carrying species, flavor, color, helicity, OAM, sector, and member identity;
4. a common diagonal zeroth-rescattering overlap kernel;
5. analytic benchmarks A--D from Volume II;
6. a typed bridge from pilot overlap outputs to the existing C2 reduction and provenance infrastructure;
7. complete isolation from the accepted canonical production boundary until all analytic validation gates pass.

The mathematical parent is the regulated, zero-rescattering overlap

```text
W[a/N]^(0) = <N,out | O_a * U_gamma^(0) | N,in>,
U_gamma^(0) = identity,
```

with the full geometric Wilson-path identity retained but no dynamical eikonal phase introduced.

C3 is not yet a phenomenological replacement for any accepted TMD. It is an analytically controlled validation pilot for the future microscopic state.

## Completeness and autonomy

Completeness is the objective, not speed.

Continue autonomously until every acceptance criterion is satisfied. Read all relevant source, tests, manifests, and reports. Run routine non-destructive commands, local dependency installation, symbolic checks, test suites, report builders, schema validators, and rendering commands without stopping for approval when the environment permits them.

If one optional package or command is blocked, use an available alternative, document the limitation, and continue all unaffected work. Do not stop merely to ask whether to continue.

Do not perform network publication, credential changes, destructive history rewrites, or changes outside the repository. Create a local commit only after all acceptance criteria pass. Do not push.

## Strict non-goals

Do not implement in C3:

- a fitted or realistic microscopic nucleon Hamiltonian;
- Hamiltonian diagonalization or parameter calibration;
- nonzero skewness;
- a physical nonzero-transfer model for the accepted canonical parent;
- dynamical Wilson-line interactions, eikonal poles, rescattering phases, or naive-`T`-odd functions;
- Sivers, Boer--Mulders, or gluon `f/d` dynamics beyond retaining operator identity;
- sea or gluon higher-sector activation as authoritative physics;
- Volume II Benchmarks E or F as production claims;
- soft subtraction, rapidity renormalization, Collins--Soper evolution, or `W+Y` matching;
- nuclear convolution or deuteron composition;
- changes to the accepted 216-reduction registry unless a separate validation-only registry is used and the accepted registry remains exactly unchanged;
- changes to the accepted provenance default composition plan;
- new fit parameters, transverse widths, phases, normalizations, or evidence upgrades;
- changes to any accepted sign, rank, mass, Fourier, path, color, flavor, tensor, wave-function, uncertainty, or nuclear convention;
- positivity clipping or numerical repair;
- silent use of `UNSPECIFIED` for an operation that requires a field;
- connection of pilot arrays to the production resolved-parent builder;
- a claim that C3 produces physical nucleon GTMD phenomenology.

The Gaussian in Benchmark B is an analytic verification wave function only. It must never be presented as a universal TMD width or inserted into accepted central artifacts.

## Physics and numerical invariants

Do not change:

- any of the eight authoritative files, bytes, row order, columns, precision, formatting, or hashes;
- the 216 accepted native reductions or their stable identities;
- the accepted C2 provenance graph semantics and default composition plan;
- the production resolved-parent numerical route;
- any accepted quark, antiquark, or gluon parent value;
- proton/neutron and flavor resolution;
- target-polarization signs and the internal-to-physical `LL` adapter;
- transverse-rank, reference-mass, extracted-power, Bessel-order, and Fourier-phase conventions;
- Wilson-path and ordered gluon-link identity;
- gluon `f`- and `d`-type accepted content;
- evidence classifications or uncertainty semantics;
- acceptance tolerances used by the existing canonical model.

The accepted model remains the immutable regression oracle. The C3 pilot must live beside it, not inside it.

## Architecture rule

Build on the C1/C2 formal package and native registries. Do not create a second coordinate, rank, sector, path, operator-identity, reduction, map-class, or provenance type system.

Inspect the actual implementations and `c1_api.md`/`c2_api.md` before choosing module names. Extend existing immutable dataclasses, enums, protocols, validators, and structured diagnostics where semantically correct. Add a new microscopic or analytic-pilot package only for genuinely new state, fiber, recoil, and overlap objects.

Prefer:

- immutable dataclasses and enums;
- explicit generic protocols for analytic wave functions and active kernels;
- pure functions;
- exact or symbolic identities where practical;
- deterministic serialization and hashing;
- explicit source/target momentum fibers;
- versioned conventions;
- dependency-light numerical code;
- analytic formulas used as test oracles;
- structured diagnostics with stable error codes;
- a validation-only registry or namespace clearly separated from accepted production registries.

Avoid:

- stringly typed momentum labels;
- raw arrays whose roles are inferred by shape;
- one generic transverse vector class used without semantic role;
- duplicate recoil formulas in projectors or benchmarks;
- hidden normalization factors;
- global mutable pilot registries;
- implicit casts between `Amp`, `Dens`, `Match`, `Red`, and `Proc`;
- automatic promotion of a pilot object into an accepted production object;
- broad unrelated refactoring.

# C3.BASELINE — verify and freeze the C2 state

1. Record the exact starting commit, branch, and working-tree status.
2. Run and record the complete C2 validation baseline before modifications.
3. Load authoritative hashes and registry counts from the machine-readable C2 reports.
4. Verify deterministic regeneration of the C2 reduction registry, provenance graph, and composition manifest.
5. Record all commands and environment versions.
6. Create a C3 baseline snapshot without overwriting C0, C1, or C2 reports.
7. The final report must compare before/after tests, builders, evidence, atlases, registries, graph manifests, injections, and hashes.

# C3.ISOLATE — validation-only pilot boundary

The pilot must be disconnected from accepted central artifacts.

Implement an explicit status such as an existing equivalent of:

```text
VALIDATION_ONLY
ANALYTIC_PILOT
NOT_AUTHORIZED_FOR_PRODUCTION
```

Use the existing C1/C2 availability/evidence/provenance concepts when they can represent this status correctly. Do not add a parallel status system.

Requirements:

1. The accepted production reduction registry remains exactly the C2 registry.
2. The accepted default composition plan contains no C3 pilot node or edge.
3. The production resolved-parent builder cannot consume a C3 pilot result without a new explicit adapter and authorization that are outside this work package.
4. Importing the pilot package has no production side effects.
5. Pilot outputs are written only to a dedicated path such as `outputs/next_level/c3/` or another existing next-level validation location.
6. Tests deliberately attempting production promotion must fail closed with a structured diagnostic.
7. The pilot may be represented in a separate validation provenance graph or as inactive nodes that are provably unreachable from the accepted root; document and test the chosen design.

# C3.FIBER — typed zero-skewness momentum fibers

Implement or extend a native `MomentumFiber`-equivalent object using the C1 coordinate and convention types.

A fiber must contain at least:

```python
MomentumFiber(
    stable_id,
    role,                 # INCOMING, AVERAGE, OUTGOING
    p_plus,
    p_transverse,
    invariant_mass,
    light_front_convention,
    normalization_id,
    regulator_or_pilot_id,
    hilbert_space_id,
    sector_scope,
    version,
)
```

Use actual repository types and names rather than copying this sketch when the existing API already supplies a field.

The C3 frame is strictly:

```text
p  = P - Delta/2
p' = P + Delta/2
Delta^+ = 0
xi = 0
t = -Delta_T^2
```

Requirements:

1. `DeltaT` is the C1 off-forward transfer coordinate type, not `kT`, `bDelta`, `bTMD`, nuclear transfer, or measured `qT`.
2. Incoming and outgoing fibers have the same `P^+` and invariant mass and transverse momenta `-DeltaT/2` and `+DeltaT/2` in the symmetric frame.
3. The average fiber has transverse momentum zero unless a separately named frame convention is introduced outside this pilot.
4. Source and target fibers are part of overlap and operator identity.
5. A map between incompatible normalization, regulator, Hilbert-space, or frame identities fails closed.
6. Nonzero `Delta^+` or `xi` must be rejected with a stable diagnostic in C3.
7. Serialization and equality are deterministic and versioned.

# C3.CONFIG — intrinsic Fock configurations

Implement a typed intrinsic configuration for an `n`-constituent pilot state:

```text
{x_i, k_iT, species_i, flavor_i, color_i, helicity_i, Lz_i, basis_i}
```

with:

```text
x_i > 0,
sum_i x_i = 1,
sum_i k_iT = 0.
```

Requirements:

1. Momentum fractions and intrinsic transverse momenta are validated at construction.
2. Active average momentum `kT`, spectator intrinsic coordinates, and total transfer `DeltaT` remain distinct types.
3. Constituent order, identical-particle symmetry, and active-slot identity are explicit.
4. Sector identity uses the C1 `SectorId`/`SectorSpace` authority.
5. Color and flavor labels use represented types rather than free strings where existing enums are available.
6. A normalized state member retains a stable phase and member identity.
7. Invalid support, closure, duplicate constituent identity, or inconsistent sector content fails closed.

# C3.RECOIL — one symmetric-`xi=0` recoil authority

Implement one versioned recoil map `R_{j,Delta}^{(n)}` for active constituent `j`.

For active constituent `j`:

```text
kappa_jT^in  = k_jT - (1 - x_j) DeltaT / 2
kappa_jT^out = k_jT + (1 - x_j) DeltaT / 2
```

For every spectator `i != j`:

```text
kappa_iT^in  = k_iT + x_i DeltaT / 2
kappa_iT^out = k_iT - x_i DeltaT / 2
```

Longitudinal fractions are unchanged:

```text
x_i^in = x_i^out = x_i.
```

The typed identity must contain at least:

```text
SYMMETRIC_XI0, n, active index, fractions, DeltaT,
incoming fiber, outgoing fiber, Jacobian = 1, version.
```

Mandatory exact properties:

1. intrinsic closure in both incoming and outgoing configurations;
2. the active physical parton receives exactly `DeltaT`;
3. every spectator physical momentum is unchanged;
4. affine unit Jacobian;
5. `DeltaT -> -DeltaT` interchanges incoming and outgoing configurations;
6. `DeltaT = 0` gives the identity configuration;
7. permutation covariance under a simultaneous relabeling of constituents and active index;
8. the same recoil object is called by quark, antiquark, gluon, scalar, spinor, and color benchmarks;
9. no projector, benchmark, or overlap implementation may duplicate the shift formulas.

Use exact rational/symbolic checks where practical and high-precision numerical tests otherwise.

# C3.STATE — analytic pilot states

Implement a small analytic state protocol and concrete benchmark states. The protocol must expose:

- sector identity;
- constituent content;
- normalization convention;
- member/phase identity;
- amplitude evaluation on an intrinsic configuration;
- adjoint/conjugation;
- helicity, color, flavor, and OAM blocks;
- declared analytic normalization or numerical quadrature contract.

Do not attach one adjustable normalization per projected function. State normalization belongs to the state and active-current normalization belongs to the operator kernel.

At minimum implement:

1. a one-body point state;
2. a normalized two-body scalar-spectator state with an analytic Gaussian option;
3. a finite spinor/OAM toy state with `Lz = 0, +1, -1` blocks and real-amplitude and controlled-complex variants;
4. a normalized three-quark color-singlet proton benchmark with permutation-consistent spin-flavor-momentum content.

The Gaussian state is validation-only and must carry metadata that prohibits interpreting its width as a fitted physical TMD parameter.

# C3.KERNEL — common diagonal zeroth-rescattering overlap kernel

Implement one common diagonal `OverlapKernel`-equivalent object. It belongs to `Amp`, not `Red`, `Match`, `Dens`, or `Proc`.

Its identity must contain at least:

```text
active species and flavor,
active index,
source sector,
target sector,
active spin/helicity operator,
color operator,
spectator matching rule,
field/current normalization,
source and target momentum fibers,
recoil convention,
Wilson path identity,
Wilson order = ZERO,
operator identity,
version.
```

The pilot overlap is the diagonal canonical core:

```text
W = sum_sectors sum_active integral
    psi_out^*(R_out configuration)
    K_active,spectator
    psi_in(R_in configuration).
```

Requirements:

1. source and target sectors are equal in C3;
2. every spectator is matched in species, flavor, color, helicity, and physical momentum;
3. the active kernel is explicit and separate from state amplitudes;
4. field/current normalization is fixed by benchmark number/current closure, not fitted per output;
5. the Wilson path remains in operator identity but the dynamical transport is exactly the identity;
6. any nonzero Wilson/eikonal order is rejected in C3;
7. an off-diagonal Fock-sector block is rejected unless a named source exists; C3 supplies no such source;
8. the adjoint kernel and incoming/outgoing fiber exchange are explicit;
9. deterministic evaluation and serialization are required;
10. the pilot output is typed as a regulated analytic/model overlap, not as a renormalized QCD TMD.

# C3.OVERLAP — common overlap evaluator

Implement a common evaluator that can consume all C3 benchmark states and kernels without benchmark-specific recoil or contraction code.

The evaluator must return an immutable typed result containing:

- operator identity;
- source/target fibers;
- sector and active-slot ancestry;
- value or helicity/color matrix;
- analytic or numerical evaluation mode;
- normalization ledger;
- Hermiticity partner identity;
- residuals;
- provenance trace;
- validation-only status.

Requirements:

1. quark-vector benchmark contractions use the same evaluator as scalar and color benchmarks;
2. the evaluator preserves active-slot contributions before summation;
3. proton `u` and `d` counts emerge from active-slot sums;
4. constituent permutations do not change the total result;
5. no accepted production array is imported as a toy wave function;
6. no pilot result is written into an authoritative CSV.

# C3.BENCH_A — one-body point state

For `x_1 = 1` and `k_1T = 0`:

1. active recoil shifts vanish exactly;
2. incoming and outgoing intrinsic configurations are identical for any `DeltaT`;
3. the vector overlap reduces to the declared active-current matrix element;
4. state and current normalization close exactly or at machine precision;
5. there is no internal transverse structure;
6. invalid attempts to infer a physical transverse width fail.

# C3.BENCH_B — two-body scalar spectator

For a normalized scalar wave function `phi(x,kT)`, implement the analytic overlap

```text
W^(2)(x,kT,DeltaT)
 = N * phi^*(x, kT + (1-x) DeltaT/2)
       phi(x, kT - (1-x) DeltaT/2).
```

Mandatory tests:

```text
W(x,kT,DeltaT)^* = W(x,kT,-DeltaT)
W(x,kT,0) = N |phi(x,kT)|^2
```

For the validation Gaussian

```text
phi = N0 f(x) exp[-kT^2 / (2 beta^2 x(1-x))],
```

provide an independent analytic oracle for the `DeltaT` dependence and, if a Wigner transform is implemented, its analytic transform. The generic evaluator and analytic oracle must agree within a declared tolerance over a deterministic test grid.

The width `beta` is benchmark metadata only and must not enter accepted model configuration.

# C3.BENCH_C — spinor active constituent and OAM blocks

Construct a minimal active-spinor plus spectator state with `Lz = 0, +1, -1` components.

The benchmark must demonstrate:

1. rank-zero unpolarized projection;
2. rank-zero helicity projection;
3. a rank-one helicity--orbital interference structure;
4. exact vanishing of all phase-odd projections for a fully real state;
5. activation of a controlled imaginary interference only in a deliberately complex validation member, without calling it a physical Wilson-line phase;
6. reconstruction of the full `4 x 4` active-parton/target helicity matrix from its declared projector coordinates;
7. projector duality/Gram closure using the existing typed reduction/projector infrastructure where available;
8. removal of either participating OAM block eliminates the associated rank-one harmonic;
9. rank, reference mass, extracted power, and Fourier phase remain explicit.

Do not label the controlled complex member as Sivers or Boer--Mulders physics. It is an algebraic interference test only.

# C3.BENCH_D — three-quark color-singlet benchmark

Use

```text
C_abc = epsilon_abc / sqrt(6)
```

with a normalized permutation-consistent spin-flavor-momentum amplitude.

Mandatory tests:

1. color normalization is one;
2. the total color generator annihilates the singlet within tolerance;
3. active summation over a proton benchmark gives exactly `N_u = 2`, `N_d = 1`;
4. active-slot contributions remain traceable;
5. permutation-related representations give the same total overlap;
6. the neutron is obtained through an explicit represented isospin transformation, not by assigning equal `u` and `d` amplitudes;
7. the charge-symmetry adapter is reversible and preserves color, helicity, OAM, coordinate, path, and normalization identity;
8. an injected non-singlet color tensor fails the physical-state/color gate.

# C3.HERMITICITY — nonzero-transfer adjoint closure

For every pilot overlap, test the exact typed relation appropriate to the declared convention:

```text
W_{Lambda' Lambda}(x,kT,DeltaT)^*
 = W_{Lambda Lambda'}(x,kT,-DeltaT)
```

with source/target fibers, active indices, path inversion status, and operator adjoint transformed explicitly.

Requirements:

1. Hermiticity is tested before named-function projection;
2. the partner operation is generated from typed identities rather than hand-edited signs;
3. residuals are reported per benchmark and aggregate maximum;
4. failure cannot be repaired by symmetrizing or averaging the final result;
5. injected recoil-sign, fiber-role, helicity-phase, or adjoint mismatches fail.

# C3.NUMBER — current and number closure

Implement number/current ledgers for the pilot states.

At minimum report:

- one-body current normalization;
- scalar-state normalization;
- proton valence counts `u=2`, `d=1`;
- neutron counts after the explicit isospin adapter;
- sum over active slots;
- any quadrature residual.

Normalization must be generated by the state and operator definitions. Do not introduce post hoc per-function rescaling.

# C3.COLOR — represented color closure

Use the existing formal color/sector identities where available.

Requirements:

1. color is a represented degree of freedom, not filename metadata;
2. the three-quark benchmark passes singlet projection and generator tests;
3. active color kernels and spectator deltas are explicit;
4. no generic gluon `f/d` dynamics are implemented in C3;
5. ordered gluon-link and color-class fields remain carried by operator identity where applicable but unresolved fields cannot enter an operation that requires them;
6. non-singlet and mismatched-representation injections fail closed.

# C3.REDUCTION_BRIDGE — typed connection to C2 without production activation

Use the existing C2 native reduction interfaces to expose validation-only views of the pilot result.

At minimum support, on analytic benchmarks where mathematically defined:

- forward-limit declaration `DeltaT -> 0`;
- target/parton helicity projection;
- named validation coordinate or projector view;
- regulated transverse integral or current moment when analytically finite;
- optional analytic Wigner transform for Benchmark B;
- route trace from pilot overlap to validation result.

Rules:

1. the bridge uses the existing C2 `Red`/`ReductionId` authority;
2. no accepted reduction identity is overwritten or reinterpreted;
3. pilot reductions live in a separate validation registry or are marked unreachable from the accepted root;
4. no formal regulated integral is labeled as a matched physical PDF, GPD, TMD, or local current without an explicit matching object;
5. scheme-changing operations remain `Match`, not `Red`;
6. coordinate, rank, mass, phase, path, flavor, sector, and member identity are preserved;
7. the accepted production registry count and serialized manifest remain unchanged.

# C3.PROVENANCE — pilot ancestry and no-double-counting

Integrate with the C2 provenance authority without modifying the accepted composition.

Record:

- analytic state source;
- recoil convention;
- active slot;
- overlap kernel;
- benchmark identity;
- reduction route;
- validation status;
- normalization and residual reports.

Requirements:

1. the pilot is unreachable from the accepted canonical production root;
2. attempting to activate pilot and accepted central parents as additive alternatives fails unless a future explicit replacement decision exists;
3. pilot Gaussian, complex interference member, and color benchmark are `VALIDATION_ONLY`, not fit/model evidence for the accepted boundary;
4. duplicate normalization, duplicate active-slot summation, and simultaneous direct/derived versions of the same analytic overlap are detected;
5. provenance queries are metadata-only and deterministic;
6. a complete ancestry trace is available for every reported benchmark value.

# C3.INJECT — mandatory negative tests

Add deliberate mismatch tests for at least:

1. `bTMD` supplied where `DeltaT` is required;
2. nonzero `Delta^+` or `xi`;
3. momentum fractions that do not sum to one;
4. intrinsic transverse momenta that do not close;
5. invalid or duplicated active index;
6. wrong active recoil sign;
7. wrong spectator recoil sign;
8. omitted factor of one-half;
9. non-unit or inconsistent Jacobian metadata;
10. incompatible incoming/outgoing fibers;
11. mismatched normalization or regulator identities;
12. off-diagonal source/target sectors without a named source;
13. nonzero Wilson/eikonal order;
14. incomplete decorated operator identity;
15. rank/reference-mass/Fourier-phase mismatch in a projector bridge;
16. spectator flavor/color/helicity mismatch;
17. non-singlet three-quark color tensor;
18. hard-coded proton/neutron flavor equality instead of an isospin adapter;
19. duplicate active-slot contribution;
20. pilot result inserted into the production reduction registry;
21. pilot node made reachable from the accepted composition root;
22. pilot Gaussian width promoted to accepted model configuration;
23. final-result Hermiticity repair by averaging rather than fixing the source mismatch;
24. production resolved-parent builder asked to consume a pilot object.

Every injection must fail with a stable structured diagnostic and be included in a machine-readable injection manifest.

# C3.CONVERGENCE — numerical and analytic residuals

Although C3 is analytic, report independent residual categories:

- exact algebra/symbolic residual;
- floating-point evaluation residual;
- quadrature residual, if used;
- grid-refinement residual;
- finite-domain residual, if an integral is truncated;
- projector reconstruction residual;
- Hermiticity residual;
- color-singlet residual;
- number/current residual.

Do not combine these into one opaque score. The benchmark report must state which results are exact identities and which depend on numerical approximation.

Use tight tolerances appropriate to analytic toy models. Do not inherit loose phenomenological tolerances when machine-precision closure is available. Record the rationale for every tolerance.

# C3.REGRESS — immutable accepted boundary

After implementation:

1. run the complete test suite;
2. run all nine acceptance/report builders;
3. verify `36/36` evidence rows;
4. render all `162/162` atlas pages;
5. run every C1 and C2 mismatch injection;
6. run all C3 injections and analytic benchmarks;
7. regenerate C2 registries and manifests deterministically;
8. verify all eight authoritative artifacts are byte-identical to the C2 baseline;
9. verify the accepted reduction registry is unchanged;
10. verify the accepted default composition plan is unchanged;
11. verify the production resolved-parent builder imports no pilot result and produces the same bytes.

Do not update an authoritative hash merely because an output changed. Any accepted-byte change is a C3 failure.

# C3.DOC — required deliverables

Create at least:

1. `docs/next_level/c3_implementation_report.md`
2. `docs/next_level/c3_api.md`
3. `docs/next_level/c3_requirement_coverage.json`
4. `docs/next_level/c3_benchmark_manifest.json`
5. `docs/next_level/c3_injection_manifest.json`
6. `docs/next_level/c3_pilot_provenance.json`
7. `docs/next_level/c3_regression_report.json`
8. `docs/next_level/c3_unresolved_formalism_gaps.md`
9. architecture-decision records for:
   - zero-skewness momentum-fiber identity;
   - the single symmetric recoil authority;
   - pilot isolation from accepted production;
   - analytic state and overlap normalization;
   - the validation-only bridge to native C2 reductions.
10. a deterministic validation script for the C3 JSON/document package;
11. an update to the persistent roadmap and handoff notes.

The machine-readable benchmark manifest must include, for every benchmark:

```text
stable benchmark ID,
state/member ID,
sector content,
operator ID,
source/target fibers,
recoil convention,
active slots,
analytic oracle,
numerical result,
residual categories,
tolerances,
pass/fail,
provenance root,
production authorization = false.
```

## Required tests and quality checks

Add focused unit, property-based, integration, determinism, serialization, and regression tests.

At minimum include:

- fiber construction and mismatch tests;
- configuration support and closure tests;
- recoil algebra and permutation covariance;
- one-body point benchmark;
- scalar-spectator analytic benchmark over multiple deterministic kinematic points;
- spinor/OAM zero and activation tests;
- helicity-matrix/projector reconstruction;
- three-quark color-singlet and number tests;
- neutron isospin-adapter tests;
- Hermiticity at nonzero `DeltaT`;
- pilot reduction-route traces;
- pilot provenance isolation;
- serialization/hash determinism;
- all negative injections;
- complete immutable-production regression.

Do not reduce test coverage by replacing precise tests with snapshots alone.

## Acceptance criteria

C3 is complete only when all of the following hold:

1. The exact C2 baseline is reproduced before edits.
2. The pilot is structurally and operationally disconnected from accepted production.
3. One typed zero-skewness momentum-fiber authority is used throughout.
4. One typed recoil-map authority satisfies closure, physical assignment, unit Jacobian, involution, forward identity, and permutation covariance.
5. One common diagonal overlap evaluator runs Benchmarks A--D.
6. Benchmark A closes state/current normalization.
7. Benchmark B agrees with an independent analytic overlap oracle and satisfies Hermiticity and the forward limit.
8. Benchmark C reconstructs the helicity matrix, produces the required rank structure, and gives exact phase-odd zeroes for real amplitudes.
9. Benchmark D is a represented color singlet and gives exact proton valence counts with an explicit neutron isospin adapter.
10. Every overlap retains complete operator, fiber, sector, active-slot, path, member, and provenance identity.
11. No off-diagonal sector or nonzero Wilson-order contribution is silently accepted.
12. The C2 typed reduction bridge works only in validation mode and leaves the accepted registry unchanged.
13. Every mandatory injection fails with the expected structured diagnostic.
14. All C3 reports and JSON manifests are deterministic and validate.
15. The full final test suite passes.
16. All nine acceptance/report builders pass.
17. Evidence remains `36/36`.
18. All `162/162` atlas pages render.
19. All eight authoritative files remain byte-identical.
20. The accepted C2 reduction registry, provenance graph, and default composition plan remain unchanged.
21. The production resolved-parent builder remains numerically and architecturally independent of the pilot.
22. Remaining formalism gaps are explicit and the next package is stated precisely.
23. A local commit is created only after all gates pass and is not pushed.

## Likely next package

Do not implement the next package in C3. Based on the result, recommend one exact follow-on package. The likely sequence is:

1. extend the common overlap to minimal explicit sea and gluon sectors and common TMD/GPD/PDF/current route closure (Volume II Benchmarks E--F and remaining `V2.*` gates);
2. only after the zero-rescattering common parent is stable, begin the Volume III dynamical Wilson-line engine.

The final C3 report must decide the next boundary from actual implementation evidence rather than assuming a package name in advance.

## Final response

Report:

- starting and final commit hashes;
- whether anything was pushed;
- complete baseline and final validation counts;
- modules and APIs created or extended;
- benchmark A--D results and maximum residuals by category;
- negative-injection status;
- pilot-isolation proof;
- accepted-registry/provenance/composition invariance;
- authoritative artifact hashes;
- documentation created;
- unresolved formalism gaps;
- the exact recommended next package.

Do not declare C3 complete unless every acceptance criterion is satisfied.
