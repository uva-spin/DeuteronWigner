# C206/HQCDSTCTSOLVE1 Codex Work Package

## Mission

Complete `C197-ST-8`, **ST-compatible counterterm solution**, from the exact
committed C205 system. Solve the compatible finite-basis residual/Jacobian
system over the frozen six counterterm and nine null coordinates, publish the
entire conditional affine solution family, and distinguish every identified,
null, exact, closed, gauge/frame, boundary, and physical direction. Do not
select an unsupported physical null representative. Validate, commit locally,
generate the single successor contract and complete prompt, atomically update
persistent state, and continue immediately. Never push.

## Exact baseline and provenance

```text
baseline: f4822e301ced0e2996877d7ca359ca07effdad2f
completed package: C205/HQCDSTGLOBAL1
C205 package root: f8658cad5f3fec055efbbf56e137db0a03c76fd2a93b61ee214e22dfdb1990df
C205 status: C205_C204_GLOBAL_ORBIT_STABILIZER_IDENTITY_AUTHORITY_READY_PHYSICAL_VOLUME_NORMALIZATION_UNSELECTED
C205 plan: STGLOBAL1-B
contract: docs/next_level/c205_c206_hqcdstctsolve1_continuation_contract.json
contract SHA-256: 04431e5e70f9b5ded1fe698fbe87c14d6a640b374005fd5f4f282dd90229f363
```

Read the contract and all C198-C205 public system, coordinate, Jacobian,
cohomology, compatibility, replacement, solution-family, frontier,
completeness, readiness, and package-root records completely. Resolve omitted
roots and exact row/column orders only from committed APIs.

Preserve `handoff/ROADMAP.md`, all pre-existing untracked paths, the C134
quarantine, inherited C157 records/test, protected C69 prompt, C166 graphs,
C158 values, Q0/Q1/Q2, and all C164-C205 authorities. Never push.

## Frozen frontier and claim boundary

```text
C197-ST-1 through C197-ST-7: closed/read-only
C197-ST-8: ST-compatible counterterm solution — first exact object
C197-ST-9: target MOMq renormalization conditions
C197-ST-10: physical input
```

Keep exactly separate:

```text
six counterterm directions and their authenticated ordering;
nine null coordinates and their authenticated ordering;
identified finite-basis coordinates;
row space, right null space, and left null space;
compatible particular solutions and homogeneous families;
BRST-closed and BRST-exact directions;
field redefinitions and gauge-parameter directions;
boundary/link/holonomy/global-frame directions;
absolute gauge-volume normalization;
K9/K11/K13 resolutions;
every scheme and holonomy/BC class;
target MOMq conditions;
standard-scheme matching;
physical inputs and physical normalization.
```

A positive C206 may publish an exact conditional affine solution family and
prove which directions are fixed, redundant, exact, closed, irrelevant to
declared downstream Hamiltonian coordinates, or still require the next target
condition. It must not choose a physical representative, target coefficient,
coupling, mass/flavor input, physical holonomy/frame/volume, standard scheme,
Hamiltonian, state, spectrum, circuit, TMD, or production object.

## Mutually exclusive plans

Choose exactly one:

```text
STCTSOLVE1-A — complete exact conditional ST-compatible affine solution family ready;
STCTSOLVE1-B — compatible quotient solution ready with target-fixing directions explicit;
STCTSOLVE1-C — coordinate/row provenance incomplete;
STCTSOLVE1-D — exact compatibility or left-null certificate incomplete;
STCTSOLVE1-E — affine solve or route parity incomplete;
STCTSOLVE1-F — BRST cohomology/redundancy classification incomplete;
STCTSOLVE1-G — resolution/scheme/holonomy family mismatch;
STCTSOLVE1-H — Hamiltonian/observable relevance classification incomplete;
STCTSOLVE1-I — exact system inconsistency;
STCTSOLVE1-J — current-chain regression.
```

Rank deficiency and a nonunique affine family are expected mathematical
features, not blockers. Do not regularize, pseudoinvert, minimize norm, set
free coordinates to zero, or select a representative merely to continue.

## Scientific construction

### Freeze and authenticate the linear system

For every resolution/scheme/holonomy class, bind the exact ordered residual
vector, Jacobian, row IDs ST-1 through ST-7, six counterterm columns, nine null
columns, units/scales, source roots, rank, nullity, left nullity, independent
and dependent row bases, and exact compatibility certificate. Preserve all
unavailable entries as unavailable, never zero.

### Safe exact solve programs

Publish an immutable grammar with source-authorized equivalents of:

```text
LOAD_ST_RESIDUAL_VECTOR;
LOAD_EXACT_JACOBIAN;
LOAD_COUNTERTERM_AND_NULL_ORDER;
VERIFY_LEFT_NULL_COMPATIBILITY;
EXACT_ROW_REDUCE;
SOLVE_PARTICULAR_SYSTEM;
COMPUTE_RIGHT_NULL_BASIS;
COMPUTE_LEFT_NULL_BASIS;
FORM_AFFINE_SOLUTION_FAMILY;
CHANGE_NULL_BASIS;
PROJECT_BRST_CLOSED_EXACT_QUOTIENT;
CLASSIFY_FIELD_REDEFINITION;
CLASSIFY_BOUNDARY_GLOBAL_DIRECTION;
CLASSIFY_DOWNSTREAM_RELEVANCE;
RETURN_TYPED_CONDITIONAL_FAMILY.
```

No eval, callbacks, pickle, hidden numerical defaults, pseudoinverse,
regularization, optimizer, minimum-norm choice, remembered formula, or
physical parameter selection.

### Independent solution routes

Require:

```text
SOLVE-A exact symbolic row reduction;
SOLVE-B independent fraction-free elimination;
SOLVE-C SVD/rank diagnostic only, never authority for exact zeros;
SOLVE-D left-null compatibility reconstruction;
SOLVE-E row/column reversal and null-basis change;
SOLVE-F automatic/symbolic/finite-difference Jacobian parity;
SOLVE-G K9/K11/K13, scheme, and holonomy holdouts;
SOLVE-H substitution of the affine family into every ST residual.
```

Publish a particular solution only in an authenticated coordinate gauge or as
a symbolic base point with all choices named. Publish the complete homogeneous
basis and reversible maps between original coordinates and identified-plus-
null coordinates. Prove residual zero for all affine parameters at the exact
conditional scope.

### Cohomology, redundancy, and relevance

Classify each direction as fixed, free, right-null, BRST-closed, BRST-exact,
field redefinition, gauge/sub-gauge variation, boundary/link, holonomy/frame,
global-volume normalization, target-sensitive, standard-matching-sensitive,
physical-input-sensitive, Hamiltonian-relevant, observable-relevant, or proven
irrelevant at the declared scope. Do not equate a null direction with a gauge
direction without an authenticated map. Do not call finite-candidate
cohomology a physical-state theorem.

### `C197-ST-8` replacement

Replace only the blocked ST-8 row/capsule with the exact conditional solution
family. Preserve ST-1 through ST-7 and unrelated rows. Publish updated system
shape, rank/nullity/left-nullity, compatibility, solution-family dimension,
quotient dimension, fixed/free direction census, and remaining frontier.
Never count a chosen coordinate gauge as an independent identity.

### Topology and count once

Separate identities, Jacobian sensitivities, compatibility equations,
particular base point, homogeneous basis, null-basis changes, BRST quotient,
field redefinitions, boundary/global directions, target conditions, physical
inputs, and downstream relevance. Each appears exactly once.

## Public API and roots

Implement preferably under:

```text
src/deuteron_wigner/bridge/hqcdstctsolve1/
data/runtime/c206_hqcdstctsolve1/
```

Expose immutable verified loaders plus plan/frontier, system freeze, parameter
schema/fixtures/validation, solve-program schema/programs, compatibility,
exact row reduction, particular solution, right/left null bases, affine family
construction/evaluation, basis transforms, cohomology/redundancy,
downstream-relevance, ST replacement, analyticity, topology/count-once,
release, requests, missing object, next handoff, dependency, quantum
nonmutation, isolation, mutations, and completeness. All NumPy loads use
`allow_pickle=False`; reject unknown IDs, partial records, hidden defaults,
mixed coordinate forms, silent row drops, or physical choices.

Publish distinct authenticated roots for every layer and the package. No root
may bind a physical representative, target MOMq condition, standard-scheme
value, physical input, Hamiltonian, or quantum object.

## Validation

Create complete `c206_*` contracts/manifests/validations and implementation,
readiness, root, runtime, safe-loading, determinism, restart, sharding, paging,
query-order, holdout, mutation, regression, isolation, nonmutation, and
completeness evidence.

Use `/Users/dustin/miniforge3/bin/python3.9` and pytest 8.4.2. Run the tracked
C157 replacement, C158 public regression without values, targeted C161-C205
tests, C198-C205 ST/BRST/global tests, and C206 focused tests. Require two
deterministic clean builds and order reversals across rows, columns, null bases,
resolutions, schemes, holonomies, boundary classes, fixtures, and queries.
Run at least 384 live mutations over actual roots, system entries, basis maps,
compatibility certificates, affine families, classifications, release, and
continuation. Repair ordinary failures autonomously.

## Release and continuation

A positive release closes ST-8 only as the exact compatible conditional
family/quotient authorized by evidence. Then read the frontier. If confirmed,
the next object is:

```text
C197-ST-9 — target MOMq renormalization conditions
alias TARGET_RENORMALIZATION_CONDITION
```

Create exactly one narrow prospective continuation. Do not jump past target
matching to physical input, Hamiltonians, PennyLane, or TMD work.

Commit locally exactly once, verify, generate/hash the complete successor
prompt, atomically increment state once, and continue immediately under the
persistent master instruction. Report exact commits, roots, system dimensions,
ranks, bases, classifications, tests/mutations, nonclaims, preserved paths,
and confirmation that nothing was pushed.
