# DeuteronWigner current project handoff

- Last reconciled: 2026-09-04
- Canonical checkout: `/Users/dustin/work/DeuteronWigner`
- Branch at reconciliation: `main`
- Initial audited code baseline: `186cc8164240f5d18c99fb56f29ba74d243849b5`
- Preceding handoff/document commit: `3cbfc0bcd1c78ceff2018a602cc333037b0ff7d1`
- Current committed worktree base: `7dad2691607e833c0c4718a02dc2047739ab8d41`
- Post-base working state: C411 exploratory-action, M2 H0/basis-map,
  integrated Q0--Q2 substrate, K9 invariant-projector, and fail-closed
  state/current-boundary work are present as reviewed working-tree changes and
  are not represented by the committed base alone.
- User-supplied theory-note baseline SHA-256: `609e5a9535227dde1c9dae5d3cf943694e0218aa6a154b2249b06f1ed1cfecea`

The user-supplied theory note and bibliography are preserved byte-for-byte at
`references/source_archives/DeuteronWigner_complete_theory_note_current.original_2026-09-03.tex`
and
`references/source_archives/DeuteronWigner_complete_theory_references.original_2026-09-03.bib`.
Their hashes are `609e5a9535227dde1c9dae5d3cf943694e0218aa6a154b2249b06f1ed1cfecea`
and `024e29d58181054c195886f7b22d54912f4623f780faec9c3166e9b59f04f5ec`.
The current working copies are separate and their pre-edit snapshots are
retained beside the originals. The backup and change record is
`references/source_archives/README.md`; no future update should overwrite the
original backup.

This is the first file a human or coding agent should read after `AGENTS.md`.
It replaces conversation history, stale controller state, and the historical
roadmap as the current operational handoff. The long files remain valuable as
history and evidence; they are not the fastest route back into the science.
The synchronized machine-readable index is
`references/DeuteronWigner_theory_state_current.json`. The TeX note is the
derivation authority; the JSON is a compact status/convention index, not a
second theory source.

## One-paragraph project objective

DeuteronWigner is building a complete spin-1 deuteron partonic framework whose
organizing objects are quark and gluon light-front GTMD correlators. TMDs,
GPDs, PDFs, Wigner distributions, local-current moments, and essentially every
observable accessible from the completed operator content should be reductions
or contractions of those parents. The construction keeps
proton/neutron identity, flavor, target and parton spin, orbital interference,
gauge-link structure, realistic deuteron motion, nuclear mechanisms, and
uncertainty lineage visible until the physical composition step. The current
phenomenological boundary is useful and operational. The longer-term objective
is a topology-constrained, quantum-enabled microscopic light-front Hamiltonian
and current whose physical parameters are identified across finite resolutions,
whose matching, conservation laws, and sum rules remain valid through the
required orders, and whose output closes on the same GTMD-first observable
layer.

## Governing scientific progression

This four-stage progression is the project's north star and should control
prioritization when local bookkeeping obscures the larger goal:

1. **Phenomenological basis -- established public starting point.** The public
   repository began as a deliberately simple, usable flavor- and spin-resolved
   light-front GTMD/TMD model for the deuteron. It established the common-parent
   projection architecture and a phenomenological boundary without claiming a
   common microscopic Hamiltonian. The foundational technical statement of this
   starting architecture is the repository-root file `Deuteron_GTMD.pdf`, *A
   GTMD-First Light-Front Wigner and SCET Framework for Spin-1 Deuteron TMDs*
   (8 July 2026).
2. **Comprehensive information-preserving light-front construct -- architecture
   established, implementation heterogeneous.** The project then expanded the
   starting model into a fully formed theoretical architecture intended to
   preserve the field's available wave-function, constituent, flavor, target
   and parton spin, orbital, tensor, gauge-link, color, transfer, nuclear,
   matching, and uncertainty information until a mathematically defined
   reduction is taken. This is broader than the original public phenomenology,
   although not every sector is equally constrained or numerically complete.
3. **Topological and quantum closure -- active construction program.** Topology
   and the project's quantum framework are to turn the information-preserving
   architecture into a closed calculation. They must encode admissible sectors,
   composition and matching maps, conservation laws, sum rules, and consistency
   across perturbative and resolution orders as structural constraints rather
   than late numerical repairs. This stage arose after the foundational draft.
   Its principal architecture sources include
   `references/algebraic_geometric_next_level_model_note_revised.tex`,
   `references/volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex`,
   `references/volume_ix_dynamical_gluon_fock_sectors.tex`, and
   `references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex`,
   together with the corresponding microscopic and bridge implementations.
4. **Predictive GTMD-level framework -- intended endpoint.** The completed
   framework is not a TMD calculator with extensions. It is a common predictive
   engine from which TMDs, GPDs, PDFs, Wigner distributions, form factors,
   currents, exclusive and inclusive reactions, and other observables supported
   by the completed operator content follow as controlled projections,
   contractions, moments, evolution, or matching limits at the GTMD level.

"Complete" at the endpoint therefore means closure of operator content,
state/current dynamics, matching and evolution, conservation and sum-rule
tests, calibration and uncertainty propagation, and observable reductions. It
does not mean that currently open inputs or unfinished numerical actions may be
treated as already solved.

### Foundational document that must remain in the pickup path

`Deuteron_GTMD.pdf` is a 29-page working note and the direct conceptual bridge
from the initial phenomenological model to the later comprehensive construct.
It establishes the GTMD-first parent hierarchy, the distinction between the
partonic and nuclear Wigner objects, quark/gluon operator separation, the
spin-1 helicity and tensor basis, the `b1` normalization anchor, GTMD-level
nuclear convolution, SCET soft subtraction and evolution, small-`b_T` matching,
rank-aware Fourier transforms, observable factorization, positivity, sum rules,
and the original staged implementation roadmap. A new human or agent should
read it after this handoff and before reinterpreting the project's original
scope. Its frozen SHA-256 is
`804756880dcf11e473a7fb190b555090c2c8eae042cb40608c20e1d8fbc48cf9`.
It does **not** contain the later algebraic/geometric, topology-aware tensor-
network, quantum-state, or quantum-computational construction and must not be
cited as the authority for Stage 3. Those additions are a subsequent evolution
of the project, not content retroactively present in the original note.

### Original comprehensive theory archive

The project owner's original formal-theory bundle is preserved unchanged at
`references/source_archives/Theory_of_the_Deuteron_GTMD.zip`, with SHA-256
`1d956f95ec14d6d17b0baf8df5055bd3240e3edeb90bd7c7e7a24d743dbaa443`.
It contains 22 flat TeX members, Volumes 0--XXI. Twenty-one members were
byte-identical to sources already under `references/`; the archive supplied
the previously absent
`references/volume_xvi_scheme_qualified_tmds_resolved_evolution.tex`
(SHA-256
`d3bf3a8621b74686b4c52a2a2e332a14119ebc8403cc80eaf8d6ec99e6856dea`).
The pre-existing Volume XVI PDF remains the authoritative historical render.
The archive comparison and pickup map are recorded in
`references/source_archives/README.md`.

The bundle confirms the scientific progression rather than changing it. Its
early volumes build the comprehensive information-preserving light-front
construct; Volumes VIII onward make the later tensor-network, topology-aware,
quantum, matching, evolution, and source-reproducibility program increasingly
explicit. In particular, Volume XVI specifies the post-M1 scheme-qualified
TMD/evolution bridge through exact formal identities and finite-order defect
tracking. It does not establish that all-order evolution, physical extraction,
complete T-odd matching, or process predictions have already been achieved.

## What the project is, and is not

There are two connected scientific layers:

1. **Operational correlator/phenomenology layer.** This contains the complete
   leading-twist spin-1 quark/antiquark basis, the 19-operator/18-identifiable
   gluon representation used by the project, light-front deuteron wave
   functions, nuclear convolution and mechanisms, TMD evolution interfaces,
   positivity and symmetry tests, and selected inclusive, SIDIS, elastic, and
   Wigner observables. Its evidence strength varies by channel and model.
2. **Microscopic Hamiltonian layer.** This contains the C43 finite-basis
   architecture, C43--JMY matching infrastructure, C396 coordinate directions,
   current adapters, diagnostic eigensolvers and state tracking, and Q0--Q2
   computational backends. It has not yet produced a physically identified
   deuteron Hamiltonian, state, spectrum, current, fit, or TMD prediction.

Do not collapse the first layer into a claim that the second layer is solved.
Do not freeze progress in the first layer while waiting for every object in the
second.

## Current repository state

The accepted local development chain after C400 is:

- C401: six K-local C396 mass-direction numerical actions became complete.
- C403--C409: the first C117 I2 direction acquired the finite axis/spatial,
  longitudinal/color, current-topology, normal-order, same-species,
  weight-routing, and derivative-density primitives.
- C410: the four retained connected products were aggregated at K9, K11, and
  K13 as

  \[
  \mathcal S_{1,K}^{(410)}
  =-\frac12\left(B_K^{qq}+B_K^{qg}+B_K^{gq}+B_K^{gg}\right).
  \]

- C411: an explicit finite-C43 adapter contract was added. It records the
  light-front conversion and can validate a future numerical mixing record,
  but it does not itself derive or supply the missing normalization/mixing.

Current numerical counts:

| Object | Current count/status |
| --- | --- |
| Complete C396 numerical apply paths | 6 |
| C117 source product primitives | 12 |
| Retained C117 aggregate shapes | 3, one per K resolution |
| Complete C117 numerical coordinate actions | 0 |
| Main-line exploratory C117 action paths | 3, one per K resolution; Lane-A only |
| Main-line exploratory operator-bundle seams | 1, explicit H0 + C396 + C117 interface |
| Main-line H0 basis-map contract | 1 schema plus exploratory C47-basis/M2-recurrence `q_rel^2` map instances at K9/K11/K13; no physical map supplied |
| M2 K9 low eigenspace | 1 named exploratory parameter point; stable sixfold q-sector projector, not a selected state |
| Physical response rank | not evaluated |
| Physical fit | not authorized or performed |
| Hamiltonian activation | not ready |

The current C411 record is
`docs/phases/c411_c117_i2_finite_c43_adapter/implementation_report.md`.
The older `handoff/C401_C410_REPOSITORY_HANDOFF.md` correctly describes the
C410 baseline but is now historical because it says C411 is absent.

The current Lane-A numerical substrate is
`src/deuteron_wigner/bridge/c411_c117_i2_finite_c43_adapter/exploratory.py`,
with focused tests in
`tests/test_c117_first_action_exploratory.py`. The main-line response seam is
`src/deuteron_wigner/quantum/operator_bundle.py`, which requires an explicit
caller-supplied (H_{0,K}) at its generic boundary; its mapped entry point now
accepts the tested M2 supply. Both routes require the two C401 mass
coefficients and the C411 exploratory C117 coefficient. Its response map uses
the exact sparse or matrix-free oracle and labels the singular spectrum as
diagnostic. The original focused test pair passes 14 tests. The recovered Q0--Q2 backend adds 33
focused tests; together the integration run passes 47 tests. The exact copied
backend-core hashes and environment details are recorded in
`docs/next_level/mainline_quantum_substrate_integration.md`. This is useful
conditional infrastructure, not a physical C117 completion or a physical
response rank.

The M2 H0 audit in `docs/next_level/m2_h0_boundary_audit.md` records that the
existing C7/C8 microscopic H0/H1 branch is validation infrastructure, not a
dimension-matched main-line `H_{0,K}`: its H1 valence dimensions are 4/7/10,
versus 1350/2706/4758 for the C401/C410 spaces. The M2 supply in
`src/deuteron_wigner/microscopic/h0/k_local.py` uses the C47 x-scaled basis,
normalization, exact CM projection, and diagonal `q_rel^2` functional, but it
does not attribute a complete sparse Hamiltonian matrix to C47. M2 assembles
the radial HO recurrence and cross-checks it against C128 `pperp2` only. The
focused check independently decodes every K9 C128 qg coordinate and verifies
the diagonal, raising/lowering radical arguments, orientation, Hermitian
partner, and forbidden selection rules while poisoning C128's historical free
routes. It
does not consume C128 longitudinal fractions or numerical free-matrix values:
the historical C128 quark-fraction defect affects its qg kinetic denominator.
The exact C47-to-C401/C410 shell-major-to-partition-major permutation remains
isometric, C7/C8 assumptions remain excluded, and C128/backups remain
preserved. The C401/C396 mass directions and C411 action remain separately
owned. Units, order, support, omissions, and ownership are in
`docs/next_level/m2_h0_basis_map_contract.md`.

At the named nonphysical `M2_K9_EXPLORATORY_BASELINE_V1` point, the exact
sparse H0+C401/C396+C411 bundle has a stable sixfold lowest q-sector subspace
at `0.194586374083865 GeV^2`, separated by `0.421163695550323 GeV^2`. It is
tracked as an invariant projector, not as a deuteron or individual state.
Sparse/matrix-free/linear actions agree to `8.33e-17`; subspace-averaged
Hellmann--Feynman and finite-difference derivatives agree to `2.64e-11`.
The three declared one-at-a-time sensitivity points remain diagnostic only.
The Q0 codec has exact K9 compact/padded round trips and zero leakage; its
Q1-style StatePrep sparse echo agrees through `1.19e-18`. Frozen Q1/Q2 APIs
remain fixture-only and were not given the external M2 Hamiltonian. The M2
focused suite passes 36 tests, with five invariant-projector and fail-closed
state-to-current boundary tests (41 total). The direct C47-plus-boundary run
passes 199 tests, and the current relevant C47/C128/C401/C411/M2 regression
passes 264. The project-local Python-3.11
quantum environment has status
`SELF_CONTAINED_EXISTING_ENVIRONMENT_VALIDATED`: it passes the frozen
Q0/Q1/Q2 regressions 15/4/14 with `PYTHONNOUSERSITE=1` and no `sys.path`
injection (SymPy 1.14.0 and mpmath 1.3.0 are local alongside
PennyLane/Lightning 0.38.0). Those two pure-Python packages were manually
seeded into the existing project-local environment after the package index was
unreachable. The declared online rebuild remains available, but
`FRESH_ENVIRONMENT_REBUILD_VERIFIED` is not claimed because it was not run.
This is not a physical Hamiltonian, deuteron state, current, fit, or response.

The M2 state-to-current audit is implemented at
`src/deuteron_wigner/quantum/m2_state_current_boundary.py`. It establishes a
precise color-intertwiner obstruction. C47 `q_basis` retains two open
fundamental triplets, and each of the 448 K9 noncolor qg tuples uses C47's
explicit `U_(3<-3x8)=T^b/sqrt(C_F)` triplet isometry. The M2 permutation
preserves them, so `H_M2,K9 = 450 * 3` and
`Hom_SU(3)(1,H_M2,K9) = {0}`. A six-versus-three observation only rules out an
isomorphism; it does not rule out an abstract embedding. The proven absence of
a color singlet rules out every nonzero color-singlet deuteron composition map
into the present M2 space. C405 has the matching direct-sum axis but its q
block is `UNAVAILABLE_NOT_ZERO_FOR_C117_I2`; C114 has no complete finite-HO
current block. Therefore neither the colored-subsystem diagnostic `P_f J_K9 P_i`
nor its normalized projector trace is evaluated; neither can be a deuteron
target current. No eigenvector is selected and neither current adapter is
called. The focused test also verifies projector invariance under an arbitrary
six-dimensional degenerate-basis rotation. The minimal next construction is
first an enlarged many-body/hadronic finite-K color-singlet Hilbert space with
spin-one deuteron composition and transfer, normalization, flavor, Fock,
orbital, and parity labels; only afterward can finite-K current intertwiners
be derived.

## Convention correction that must be preserved

The project uses symmetric light-front components

\[
p^\pm=\frac{p^0\pm p^3}{\sqrt2},
\qquad
p^2=2p^+p^- -p_\perp^2.
\]

Therefore the invariant mass operator and an interaction variation are

\[
M^2=2P^+P^- -P_\perp^2,
\qquad
\delta M^2=2P^+\delta P^-.
\]

For the finite longitudinal cell used by the C43/C117 chain,

\[
\ell_-=2L,\qquad
P^+=\frac{\pi K}{L}=\frac{2\pi K}{\ell_-}
=\frac{\pi K_2}{\ell_-},
\qquad
\delta M^2=\frac{2\pi K}{L}\delta P^-
=\frac{4\pi K}{\ell_-}\delta P^-.
\]

The current executable C45/C46/C114/C142/C172 convention uses the cell
`[-L,L]`, so `L` is its half-length and `ell_-` is the circumference. Older
C43 manifests wrote `[-L/2,L/2]` and used their `L` for the full
circumference. Translate `L_old = ell_- = 2 L_executable` before combining
their factors. This historical notation collision is a mandatory C117
normalization check.

The earlier theory note wrote `P^+P^- - P_T^2`; that is inconsistent with the
declared symmetric convention and is corrected in the synchronized current
theory note. The remaining scientific question is whether this conversion has
already been consumed by the source-reduced C410 object, and where any residual
finite-cell/state normalization belongs. It must be traced, not guessed.

The C411 metadata also labels both source and target shapes as `GeV^2` while
leaving application of the `P^- -> M^2` factor certificate-owned. That label
does not establish where the conversion occurred. The next derivation must
resolve this ownership explicitly.

## First-C117 factor ownership at handoff

| Factor or operation | Current status |
| --- | --- |
| Source coefficient `-1/2` | applied exactly once by C410 |
| Ordered `qq`, `qg`, `gq`, `gg` products | retained exactly once each |
| Nonzero-transfer `Q0` and inverse-derivative shape | represented in the C403--C410 chain |
| Disconnected external-quark/gluon-vacuum descendant | preserved and routed to the nonmatrix vacuum owner; not declared physically zero |
| `g_s^2` | factored, not numerically applied |
| `P^- -> M^2` | formula fixed; application owner unresolved |
| Field-mode and external Fock-state normalization | unresolved, not zero |
| Residual finite-cell and wave-packet normalization | unresolved, not zero |
| C260 RI/SMOM-to-finite-C43 mixing | unresolved, not zero |
| Physical `c_C117_1` and `g_s` | external and unselected |

The C411 API's 4-by-4 matrix is a generic future container. The current
first-action implementation reads only its first target row and ultimately
uses only the `(1,1)` entry after rejecting unsupported entries for the three
missing source shapes. Do not mistake the container shape for a derivation
that generic four-direction physical mixing is required.

## Why development slowed

The C-phase chain successfully protected provenance and prevented accidental
promotion of missing inputs to physical results. It also accumulated a large
amount of generated schema, hash, mutation, and fail-closed bookkeeping. In
several places the bookkeeping object became the deliverable, even when the
next useful scientific step was a derivation or a controlled numerical
experiment.

The correction is not to weaken scientific honesty. It is to separate three
levels of work so that publication-grade authority is demanded only when a
publication-grade claim is made.

### Lane A: exploratory science

Allowed:

- derive under explicit conventions;
- introduce named provisional parameters for unknown finite terms;
- select finite sensitivity ranges and compare alternatives;
- use diagnostic states and currents when they are labeled as such;
- produce plots, Jacobians, and convergence studies that are explicitly
  exploratory.

Required:

- state the assumptions near the result;
- preserve dimensions, Hermiticity, symmetry, and count-once ownership;
- never label the result physical, fitted, or activated.

### Lane B: validated model development

Required:

- coherent equations and units;
- a declared convention and parameterization;
- direct unit/limit/route-comparison tests;
- source qualification for external inputs that materially determine the
  model;
- sensitivity to important provisional choices.

This lane may produce useful scientific model results before every microscopic
coefficient has a first-principles derivation.

### Lane C: physical claims and inference

Required:

- source-qualified physical inputs and state/current definitions;
- covariance and nuisance ownership;
- no double counting of data and fitted parameterizations;
- K9/K11/K13 or other declared regulator-resolution checks;
- reproducible end-to-end calculation and honest uncertainty reporting.

This lane remains fail-closed. A missing Lane C object does not close Lanes A
or B.

## Minimal development bookkeeping from now on

For a normal scientific change, create only:

1. the derivation or short design note when the mathematics changes;
2. the implementation;
3. focused direct tests or a numerical comparison;
4. a brief update to this handoff stating the result and next step.

Do not automatically create a new C-number, generator, schema family,
checksum forest, mutation campaign, mirrored phase directory, or published
snapshot. Use those mechanisms only when they protect a concrete reusable
scientific artifact or release. Test counts and content hashes are engineering
evidence, not independent physics evidence.

The public GitHub `computation_handoff/repo/` tree remains a valid C410
snapshot at public commit `4075976deab34f1360278c41c16faf972038c017` until
the prepared 2026-09-04 local refresh is reviewed, committed, and published.
The local refresh preserves the old review surface as a checksummed archive,
mirrors the current source, tests, reports, theory note, machine state, and
roadmap, and keeps the large historical branch/history/controller payloads
unchanged. Do not describe the public page as current before publication, and
do not make snapshot refreshes a prerequisite for ordinary scientific work.

## Direction path

### Sprint 1 — derive and exercise the first C117 finite-basis direction

Goal: turn the C410 aggregate into a transparent K-local numerical response at
K9, then K11 and K13, without pretending an exploratory convention is a
physical matching result.

Status: the parameter-explicit exploratory action exists and is tested at
K9/K11/K13. The source-qualified normalization, finite-cell ownership, and
physical mixing/renormalization interpretation remain open.

1. Trace the full normalization chain from the continuum/source `P^-`
   interaction through field mode expansions, finite-cell factors, Fock-state
   normalization, basis projection, the C410 `-1/2`, factored `g_s^2`, and the
   `P^- -> M^2` conversion.
2. Produce a dimension-and-ownership table showing which factor is already in
   C410 and which factor remains outside it.
3. Determine from the represented source and target bases whether the first
   C117 direction is diagonal, mixes with the other three directions, or is
   only identifiable as a linear combination. Do not assume either identity
   mixing or a generic 4-by-4 matrix.
4. Keep the current strict C411 certificate route for physical claims. Add a
   separate exploratory adapter that accepts explicit named normalization and
   mixing parameters and stamps every result as exploratory.
5. Build the K9 action first and verify units, Hermiticity, sparsity,
   count-once aggregation, and agreement of independent application routes.
6. Repeat at K11 and K13 and inspect the compound-resolution dependence.

Deliverable: one derivation note, one executable adapter/action path, focused
tests, and a small numerical response table. No new phase machinery is needed.

### Sprint 2 — assemble the smallest useful state-to-observable response

1. **Completed:** combine the six existing C396 mass-direction actions with
   the first exploratory C117 action and mapped M2 H0 at K9.
2. **Completed:** track the lowest object as a six-dimensional invariant
   projector, not an individual eigenvector or deuteron state; verify energy
   and matrix-derivative routes.
3. **Completed as a negative boundary result:** prove
   `H_M2,K9 = 450 * 3` and `Hom_SU(3)(1,H_M2,K9) = {0}` with fail-closed
   projector/isometry/intertwiner/Casimir checks. The existing colored M2
   space cannot receive a nonzero color-singlet deuteron composition.
4. **Next:** introduce or bind an enlarged finite-K many-body/hadronic
   color-singlet Hilbert space `H_D,K` with explicit spin-one, transfer,
   charge/flavor, Fock, orbital/parity, and normalization ownership.
5. Derive finite-K current intertwiners on `H_D,K`; keep C405/C114 as
   incomplete interaction-current/topology ingredients and keep C7/C8
   separate absent an explicit basis map.
6. Only then evaluate light-front and LPS target-current diagnostics,
   observable finite differences, and a diagnostic sensitivity spectrum.

Deliverable: the first end-to-end K9 response map from actual C396/C117
directions through a lawful color-singlet spin-one state/current construction
to observables. The existing colored-subsystem projector is an input and
diagnostic oracle, not that deliverable by itself.

### Sprint 3 — physical calibration and resolution study

After Sprint 2 works:

1. choose the production current and state/sector definition explicitly;
2. begin with the minimal low-energy anchors: deuteron mass, magnetic moment,
   quadrupole moment, charge radius, and a small non-duplicated elastic subset;
3. construct the covariance and normalization nuisance model once;
4. infer resolution-local coefficients at K9;
5. repeat the same physical conditions at K11 and K13 without forcing equal
   bare coefficients;
6. assess predictions and discrepancy in observable space;
7. add the remaining C117 directions only when the source derivation or
   observable sensitivity requires them.

### Sprint 4 — reconnect the microscopic and correlator programs

Use the calibrated state/current to calculate local moments and the first
partonic matching observables. Compare them with the operational
phenomenological GTMD/TMD boundary. Promote only the channels with a complete
operator, matching, evolution, and uncertainty chain; retain the others as
model comparisons.

### Parallel phenomenology track

The correlator-level program should continue while the microscopic work
advances. High-value work includes rank-aware multi-Q evolution, improved
tensor/gluon source inputs, observable-specific gauge-link treatment,
nonzero-transfer GTMD predictions, and data-facing EIC/JLab observable studies.
These tasks do not need to wait for Hamiltonian activation when their model
status is explicit.

The literature boundary now includes the published 2026 T-even spectator
calculation (13 functions) and the July 2026 T-odd follow-up (six functions,
arXiv:2607.23692). The current repository uses these as structural benchmarks;
it does not yet reproduce either fitted spectator model numerically.

## Decisions that require the user/theory lead

An agent should surface, rather than silently choose, genuinely inequivalent
physics decisions:

- production light-front versus LPS current prescription and discrepancy
  treatment;
- physical sector projector/state definition;
- C43 intermediate renormalization condition if not derivable from the source;
- prior or allowed range for a genuinely free finite term;
- calibration corpus and covariance model;
- when the reviewed local computation-handoff refresh should be committed and
  published to the public branch.

Ordinary implementation details, exploratory parameterizations, focused tests,
and reversible diagnostics should proceed without manufacturing a blocker.

## Frozen or historical material

- `handoff/ROADMAP.md` is a valuable chronological development record but is
  no longer the sole operational queue.
- `handoff/C401_C410_REPOSITORY_HANDOFF.md` is the authoritative historical
  C401--C410 reconstruction, not the present C411 status.
- `.yolo/state/AUTOPILOT_STATE.json` points to the old C399 blocker.
- `.yolo/phase_mode/state/PHASE_MODE_STATE.json` points to C400.P1 awaiting
  review.
- Q0, Q1, and Q2 are frozen diagnostic backend branches. They do not authorize
  physical states, spectra, fits, hardware claims, or phenomenology.
- Untracked C157 materials and the modified `handoff/ROADMAP.md` are existing
  user work. Preserve them.

## Fast pickup checklist

1. Read `AGENTS.md` and this file.
2. Read the status chapter in
   `references/DeuteronWigner_complete_theory_note_current.tex`.
3. Read `references/DeuteronWigner_theory_state_current.json` for the compact
   machine status and verify it against the TeX/source for the task at hand.
4. Inspect `git status --short` and preserve unrelated work.
5. Read only the source modules and phase reports directly relevant to the
   selected sprint; do not repeat a full-repository audit.
6. State whether the work is exploratory, validated-model, or physical-claim.
7. Implement the smallest end-to-end scientific result.
8. Run focused direct tests and record numerical comparisons.
9. Update the current-status and next-step portions of this file.

## Current next action

The exploratory K9 state-to-current boundary is complete and proves that the
present M2 space cannot receive a nonzero color-singlet deuteron composition.
The next executable M2 action is first to introduce or bind an enlarged
many-body/hadronic finite-K color-singlet Hilbert space with spin-one
composition, including initial/final transfer, charge/flavor, Fock,
orbital/parity, and normalization ownership. Only then derive finite-K current
intertwiners and consider light-front or LPS diagnostics. In parallel, keep
tracing the first C117 source normalization and mixing ownership. Do not
select a physical sector/vector, use frozen Q1/Q2 fixture APIs as an
M2-operator sink, or claim a current response, physical fit, response rank,
or activation.

Do not create another phase package merely to record this work. The original
theory archive and foundational PDF remain unchanged and are still the
reference points for any later documentation update.
