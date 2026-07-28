# Persistent agent contract

Every agent or developer session must read, in order:

1. `handoff/project_context.md`
2. `handoff/ROADMAP.md`
3. the newest entries in `handoff/decisions.md`
4. the newest checkpoint in `handoff/worklog.md`
5. `references/production_tmd_architecture_audit.md`
6. `references/model_construction_note.tex`
7. `references/environment_setup.md`

## Governing objective

The objective is a fully self-consistent canonical quark--gluon model of
the leading-twist spin-1 light-front GTMD/TMD system, incorporating as much
physically known structure and every realistically supported contribution
available within the project scope. It is not a quick, minimal, merely
runnable, formally complete, or atlas-complete table.

The canonical model must select and compose mutually compatible nucleon,
nuclear, gauge-link, spin/OAM, evolution, mesonic, non-nucleonic, and
uncertainty components through one explicit parent-correlator chain. Named
TMDs must be projections or reductions of that common parent. Preserve
proton, neutron, flavor, operator, target-helicity, wave-function component,
gauge-link, color structure, and nuclear-mechanism identity until
process-specific observable assembly.

The present accepted pre-evolution implementation is a constrained
phenomenological synthesis, not a fundamental prediction from a solved QCD
state.  Section 15 of `references/model_construction_note.tex`,
“Requirements for a genuinely predictive next-level model,” governs the
next model-class transition.  A genuinely predictive claim requires a common
renormalized light-front Hamiltonian or equivalent microscopic state,
controlled Fock-sector convergence, GTMD overlaps at nonzero transfer,
dynamical Wilson-line phases, a microscopic spin-1 nuclear state with
consistent currents, QCD matching/evolution, correlated inference, and
withheld-observable validation.  Evolution of the present boundary is useful
but does not by itself satisfy these requirements.

Do not omit a realistic contribution merely because it is difficult or
poorly constrained. Do not artificially enhance it to make a visible curve.
When knowledge is incomplete, implement the best-supported replaceable
component, classify its evidence, propagate an honest sensitivity range,
and keep it out of the preferred central member unless a defensible
composition and normalization exist.

Never fill missing physics with an untraced universal amplitude. When an
input is unavailable, provide a replaceable interface, the best-supported
configurable default, machine-readable provenance and validity, a separate
uncertainty or sensitivity treatment, and a replacement test.

The files under `outputs/production_tmds/` are superseded exploratory
closure outputs and are not production physics predictions.
The same applies to the historical figures under
`outputs/figures/production_tmds/`; consult
`outputs/figures/figure_index.json` for the authoritative parent-derived
tables and vector atlases. The old plotting entry point fails closed.

## Execution rules

- Treat `handoff/ROADMAP.md` as the execution queue, not a design exercise.
- Do not declare completion while any required roadmap acceptance gate is
  open.
- Update roadmap status, decisions, validation results, defects, exact
  reproduction commands, and next executable action at every material
  checkpoint and before any handoff or context compaction.
- Preserve historical information but mark obsolete objectives and
  approximations as superseded.
- Maintain passing functionality and add tests that distinguish temporary
  approximations from their intended replacements.
- Use algebraic, geometric, representation-theoretic, topological, or
  quantum-simulation methods only when mapped to explicit physical spaces,
  operators, composition rules, or validation checks.

## Current accepted state

The former declared-scope completion at 334 tests is a preserved historical
checkpoint, not the current completion authority. On 2026-07-26 the user
expanded the required production scope to include nonzero, sourced or
explicitly modeled gauge-link phases; quark and gluon Sivers/Boer--Mulders
inputs; fit/lattice-informed pretzelosity and worm gears; separate gluon
f-type and d-type T-odd inputs; polarized and tensor shadowing; mesonic or
non-nucleonic correlators; and additional spin--orbit/OAM interference
amplitudes. These requirements are WP10 in `handoff/ROADMAP.md`.

WP10 is implemented, tested, and retained as the rich-member inventory.
WP11 subsequently closed the canonical integration gate at the declared
leading-twist forward scope. Decisions D-109--D-114 and
`references/wp11_final_acceptance_audit.md` govern interpretation. The
machine-readable completion authority is
`outputs/validation/wp11_final_acceptance.json`: C1--C7 pass and the complete
suite has 433 passing tests. The canonical gluon T-odd parent is the
project's own nucleon light-front overlap plus screened adjoint Wilson line,
followed by the retained-helicity nuclear convolution; external spectator
models are benchmark-only.

Continue the WP8/WP9 acceptance queue. The parent-derived quark/gluon figure
tables now pass complete-basis, ordered-band, dense-grid, and pre-assembly
flavor-traceability checks. Do not interpret exact-isospin inclusive
\(u_D=d_D\) or \(\bar u_D=\bar d_D\) as erased proton/neutron flavor
structure; the source terms are retained and numerically distinct. The
historical reduced-correlator figure tree is superseded and machine indexed.
The scheme-explicit LO rank-zero
quark \(b_T\) boundary and recoil-aware LF-parent adapter are implemented.
Production LF-order convergence and convention-tested rank-one WW transforms
now pass; do not relabel the existing gluon-only kernel or apply rank-zero
transforms to higher ranks. The rank-two pretzelosity adapter, disk-backed
rank-aware nucleon grid, and six-wave scenario propagation are implemented.
The smooth atlas, evolved-parent positivity, typed Collins/delta/zeta
subtraction-and-rapidity contract, and explicit low-k W+Y validity contract
are complete. APFEL++ and the vendored arTeMiDe were audited and do
not supply the required qT-differential FO/ASY pair; preserve the refusal
gate while seeking a compatible backend. The paired MSHT20 QED
proton/neutron Hessian sets now provide numerical unpolarized neutron CSB.
The central and all paired MSHT20 QED CSB members have been propagated
through all six evolved nuclear parents with shared contractions and a
correlated 38-pair Hessian. The Miller AV18 tensor-polarized Sullivan-pion
distribution is now a separate meson-exchange parent, convolved with all 786
JAM21 pion replicas and compared with HERMES \(b_1\). It is collinear and
tensor-only: do not mislabel it as a spin-averaged pion cloud or invent a
transverse pion profile. Its published helicity projections now also provide
the connected spin average; pion number, plus-momentum fraction, and the
1.004102 uncompensated sum are audited. Exact \(Z=1+N_\pi\) normalization
closes NN, NNπ-nucleon, and pion momentum; the minimal unchanged-shape NNπ
counterterm is retained only as a comparison diagnostic.  The preferred
collinear route now applies the exact conditional recoil
\(\alpha_N'=(1-yM_N/M_D)\alpha_N\) to an arbitrary-\(x\), fully
flavor/spin-resolved baseline correlator and closes nucleon number and
plus momentum.  The unintegrated retained-NN recoil
\(J_0(\alpha bq_T)\) is exposed and tested, but a full three-body NNπ
helicity/off-forward/virtuality amplitude remains required. The Miller
six-quark \(b_1\) equation is implemented
as a distinct observable scenario and passes its source table and sum rule;
it is not a correlator because the paper does not fix a flavor decomposition.
The Vpion19 100-replica nonperturbative pion boundary is now composed with
the unintegrated nuclear Sullivan recoil through the exact
\(J_0(zbq_T)\) factor and passes its \(b=0\) reduction. It is routed through
the current rank-zero CSS diagnostic. A preferred native arTeMiDe route now
uses Vpion19, NNLO matching, BSV19 NNNLO evolution, all 101 member
identities, and the same exact nuclear recoil. It remains non-production
because maintained JAM21 substitutes for unavailable JAM18 without a refit
and no fixed-order Y term exists. Production AV18 multi-\(x\) proton,
neutron, and total parent grids now supply the arbitrary-\(x\) contract using
validated log-\(x\) PCHIP; conditional recoil is propagated through all four
light flavors and the coarse/refined total is stable to 0.439% of curve
peak. These tables use the exact dimensionless \(b_T=0\) collinear
contraction; never substitute the momentum-space value at \(k_T=0\).
The exact-isospin deuteron equality is controlled, while nucleon
flavor differences remain explicit. All 786 JAM21 replicas now define the
ensemble-mean central, sample spread, quantiles, and member table. Do not
repeat the superseded active-nucleon-fraction task: the forward derivation
already proves
\(z\alpha=x_N/[2(1-\eta_\pi)]\), so \(\alpha\) cancels without an average and
the AV18 b=0 gate passes at \(2.91\times10^{-6}\). Never substitute
\(\alpha=1/2\) or omit the \(x_D=x_N/2\) factor. The native Vpion19 common
output is now Fock normalized and propagates all 100 physical profile members
through the nuclear kernel. The 2026 LFHEFT paper does not close the
off-forward gate: it integrates a scalar NNπ sector into an effective
two-body Hamiltonian and says the dynamical-pion solution remains future
work. Preserve the replacement interface; do not invent a transfer Gaussian.
Continue independent acceptance work and obtain/refit the collinear pion
input, while seeking a flavor-resolved
non-nucleonic correlator source. The 2026 effective cluster model was audited
and must not be assigned a hidden-color probability; prioritize released
helicity/color-resolved BLFQ amplitudes or a reproducible Hamiltonian
diagonalization. Its scalar holographic × 't Hooft LFWF and
momentum-dependent vector-current spin vertex are implemented, normalized,
and benchmarked against all three official LMDF vector paths. The
canonical-triplet plus unitary-Melosh limit remains an explicit
zero-\(f_{1LL}\) diagnostic. Keep this as a named cluster sensitivity
scenario. Its source-defined collinear NNPDF3.1 proton/neutron/flavor
convolution reproduces the published \(b_1\) moment, but it is not a
production TMD/color parent until a sourced transverse cluster-parton input,
color decomposition, and matching/evolution prescription are implemented.
Then continue
the concrete SIDIS hard-factor/asymptotic and observable-scale queue. The
multi-kinematic quark/gluon
production
\(b_T=0\) reductions are complete. Production-order quark-parent azimuthal
covariance is also complete and passes at
\(2.12\times10^{-9}\) maximum resolved relative residual. Official JAMDiFF
member identity and cross-x/flavor covariance reach all six nuclear \(h_1\)
and correlated WW \(h_{1L}^{\perp}\) outputs. The 500 BPV20 N3LO
Sivers replicas have
been propagated member by member through all six nuclear wave functions and
smooth, separated fit/wave-function bands are published. D-060 establishes
that standalone arTeMiDe scale knobs are inactive in BPV20's optimal-TMD
scheme; do not export nominal copies as a theory band. Next implement
observable-level hard-scale variations and the low-k W+Y matching requirement.
The H1-DPDF/FGS responses remain correlated named scenarios. Do not return to
the reduced-amplitude closure model, invent T-odd phases, or hide exact-isospin
deuteron cancellations by dropping the separately stored proton and neutron
contributions.

There is no incomplete required execution item at the accepted WP11
leading-twist forward scope.
The next scientifically useful actions are replacement upgrades: ingest a
public Yang-\(g_{1T}\) replica covariance, a fitted/lattice pretzelosity
grid, polarized/tensor DPDF information, a coupled transverse NNπ amplitude,
or fitted inputs for the five non-Sivers gluon T-odd structures when any
become available. Each is optional until promoted into scope and must replace
only its named interface, preserve the full correlator, and add manifest
evidence.

The full-matrix ledger, inclusive and polarized/tensor shadowing, named
diffractive members, momentum-compensating antishadowing, complete six-name
gluon T-odd f/d multiplet, pion/cluster correlators, and PDF-anchored OAM
scenario are implemented. Quark \(g_{1LT}\) and \(g_{1TT}\) additionally
have independent positivity-bounded phase members and an explicit screened
one-gluon AV18 S--D rescattering calculation; their stages must remain
non-additive. WP8 records 12 verified requirements and WP10
records seven verified criteria. The exact current regression count and
final project count must be read from the generated acceptance reports,
never copied from this narrative.

WP12 items 1--5 and the WP12-E evidence-parity gate now pass at the declared
pre-evolution scope. The gate requires every quark, antiquark, and gluon TMD
to have an
explicit proton input, neutron construction, flavor/color dependence,
data/lattice/model provenance, covariance or honest sensitivity ensemble,
shared-parent consistency, and channel-appropriate nuclear propagation.
An exact charge-symmetry neutron rotation is acceptable only when the
expected breaking has been quantitatively bounded and recorded.
Governing evidence is `outputs/validation/wp12e_acceptance.json`. Do not
reinterpret model sensitivities as fitted confidence regions. Complete
rank-aware multi-Q evolution is now the next executable item.

The canonical
spin-1 total is a closure projection, not the model state. Item 6 must
consume `outputs/parent_tmds/wp12_resolved_quark_parent.csv` and
`outputs/parent_tmds/wp12_resolved_gluon_parent.csv`, preserve their
proton-in-deuteron, neutron-in-deuteron, nucleon-sum, proton-minus-neutron,
nuclear-correction, and total labels through evolution, and verify closure
after evolution. It must not replace those resolved components by an
isoscalar projection. The corresponding full-correlator tables carry the
same basename with `.correlators.csv`. Do not evolve the legacy multi-x
`model_total` or add CP response members to the resolved total: that would
double count nuclear responses. Governing evidence is
`outputs/validation/wp12_scientific_inspection.json` together with
`outputs/validation/wp12_resolved_nuclear_parent.json`.

The authoritative narrative of how the original GTMD-first proposal became
the accepted pre-evolution model is the scientific LaTeX manuscript
`references/model_construction_note.tex`. Its rendered edition is
`output/pdf/model_construction_note.pdf`. The shorter Markdown summary is
superseded and historical. Future
changes to the physical boundary, evidence classification, or evolution
interface must update that note rather than create a competing model
summary.
