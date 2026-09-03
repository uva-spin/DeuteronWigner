# DeuteronWigner current project handoff

- Last reconciled: 2026-09-03
- Canonical checkout: `/Users/dustin/work/DeuteronWigner`
- Branch at reconciliation: `main`
- Code baseline at reconciliation: `186cc8164240f5d18c99fb56f29ba74d243849b5`
- Preceding handoff/document commit: `02ece47c14b2442fcac315b221658cd37b128f75`
- User-supplied theory-note baseline SHA-256: `609e5a9535227dde1c9dae5d3cf943694e0218aa6a154b2249b06f1ed1cfecea`

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
| Physical response rank | not evaluated |
| Physical fit | not authorized or performed |
| Hamiltonian activation | not ready |

The current C411 record is
`docs/phases/c411_c117_i2_finite_c43_adapter/implementation_report.md`.
The older `handoff/C401_C410_REPOSITORY_HANDOFF.md` correctly describes the
C410 baseline but is now historical because it says C411 is absent.

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

The published `computation_handoff/repo/` tree is currently a valid C410
snapshot with internally consistent checksums, but its source marker remains
at `51d3919e4660f5709cc7bb94c576c8ec17c9de14`; it is stale relative to local
C411. Update it at a deliberate public milestone, not as a prerequisite for
each scientific experiment.

## Direction path

### Sprint 1 — derive and exercise the first C117 finite-basis direction

Goal: turn the C410 aggregate into a transparent K-local numerical response at
K9, then K11 and K13, without pretending an exploratory convention is a
physical matching result.

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

1. Combine the six existing C396 mass-direction actions with the first C117
   action at K9.
2. Use a clearly named diagnostic or exploratory state until a physical sector
   projector is available.
3. Evaluate mass and elastic-current responses through the existing current
   adapters. Compare the light-front and LPS routes; do not silently choose one
   as production.
4. Verify Hellmann--Feynman, matrix finite-difference, and observable
   finite-difference derivatives.
5. Compute the singular spectrum of this explicitly exploratory response map.
   Call it a diagnostic sensitivity rank, not the physical 19-coordinate rank.

Deliverable: the first end-to-end K9 response map connecting actual C396/C117
directions to observables.

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
- what milestone warrants refreshing the public computation handoff.

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

Start Sprint 1 with a source-level normalization derivation. The first output
should be a compact factor-ownership table and a determination of whether the
C411 4-by-4 mixing requirement is physically derived, merely a generic API
shape, or unnecessarily strong for the first C117 direction. Do not begin by
creating another phase package.
