# C170/HQCDLFGSECTORCALC1 implementation report

Status: `C170_HQCDLFGSECTORCALC1_B0_ADJOINT_SECTOR_INCOMPLETE`
Plan: `LFGSECTORCALC1-D`
Next: `C171/HQCDB0ADJOINT1`

## Contract provenance

The expected committed continuation path
`docs/next_level/c169_c170_hqcdlfgsectorcalc1_continuation_contract.json`
was searched in the C169 commit, the repository, and the local Downloads
directory and is absent. The supplied prompt
`/Users/dustin/Downloads/c170_hqcdlfgsectorcalc1_codex_prompt.md` was read
completely and is the only available C170 authority. Its SHA-256 is
`204b7fa9922d84ec78816b934914edcf7a3901efb4a31d7b33d5685b15666183`.
This absence is recorded fail-closed; no replacement contract was silently
invented and no C169 record was rewritten.

C170 began at `03e71c57dd6b0686bf359f5a5a669e2889489bf6`. C169 package root
`d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5` and all
six C169 request/capsule and missing-calculation records were imported through
the C169 public API. C166 graph nodes and edges added: 0 and 0.

## Historical descendant audit

The C141 source-map blocker is superseded for the forward quark scope by the
C142 source/sink map. The C143 forward projected resolvent is superseded by
C145’s source-derived q/qg resolvent. C146 normalization is only partially
covered by C147 coordinate-field normalization, so it remains a weaker-scope
crosswalk. C141’s mass-linear object requires the C148 full-spinor plus C149
projector crosswalk. C130 residual/zero-mode/boundary realization and C150
counterterm conditions remain genuine blockers. Historical statuses were not
edited.

## Sector taxonomy

The exact C169 topology audit yields seven sector IDs:

- `C170-B1-Q`, inherited C142/C145 q domain;
- `C170-B1-QG`, inherited C152 retained qg domain;
- `C170-B0-G`, inherited C151 one-gluon source domain;
- `C170-B0-QQBAR-ADJOINT`, required by the C151 quark-pair loop;
- `C170-B0-GG-ADJOINT`, required by the C151 pure-gluon sector;
- `C170-B1-QGG`, required by complete qg-vertex higher-Fock support;
- `C170-B1-QQBARQ`, required by qg pair-conversion/full-1PI support.

B=0 uses bosonic periodic integer modes; q\bar q has an integer total. B=1
uses fermionic antiperiodic half-integer modes; q, qg, qgg, and q\bar q q
retain half-integer total semantics. K9/K11/K13 remain separate labels. New
three-body/four-body color, statistics, and CM maps are not asserted: their
multiplicities, isometries, projectors, rank/unrank maps, and free operators
remain unavailable rather than guessed.

The inherited q, qg, and g domains retain descendant source maps, free-operator
interfaces, and source-order semantics. No direct source is created for the
intermediate-only q\bar q, gg, qgg, or q\bar q q domains. Historical baryonic
QQQ sectors are not reused.

## Interactions and boundaries

The C53 q↔qg link is retained only in its proved scope. g↔q\bar q, g↔gg,
qg↔qgg, and qg↔q\bar q q are explicit calculation capsules. C111, C112,
C127, C129, and C130 terms have unique owners and remain nonzero when
unavailable. Count-once duplicate ownership is zero, but closure is false.

Ghost nonapplicability is not proved over the complete C43 finite-cell,
zero-mode, residual-gauge, PV-pole, and residual-link scope. C170 therefore
retains ghost/gauge authority as incomplete and imports no target-gauge ghost
loop as a C43 state. P0/Q0, boundary, residual-link, and omitted-space
interfaces remain explicit. Six counterterm directions and nine null
coordinates remain unselected.

No dense inverse, numerical sector diagnostic, C169 coefficient, adapter,
physical input, state, TMD, running, threshold, or C158 value is created.

## Validation

The public package is
`src/deuteron_wigner/bridge/hqcdlfgsectorcalc1/`; runtime metadata is under
`data/runtime/c170_hqcdlfgsectorcalc1/`. Package root:
`d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7`.

The focused C170 suite passes 4 tests and 384 live mutations. Public records
are immutable, unknown IDs fail closed, descendant order and sector order are
query-order independent, and the loader performs no network access or repair.
The C134 diagnostic and inherited untracked C157 test remain untouched.

The next frontier contains eight exact sector capsules: B=0 q\bar q and gg
for the transverse-gluon request, B=1 qgg and q\bar q q for the qg request,
and both pairs for QCD coupling/ST. Nothing was pushed.
