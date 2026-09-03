# C169/HQCDLFGMATCHCALC1 implementation report

Status: `C169_HQCDLFGMATCHCALC1_FULL_QCD_SECTOR_INCOMPLETE`  
Plan: `LFGMATCHCALC1-H`  
Next: `C170/HQCDLFGSECTORCALC1`

## Authority and boundary

C169 consumed the committed contract
`docs/next_level/c168_c169_hqcdlfgmatchcalc1_continuation_contract.json`
(SHA-256 `2d05f1746d1062bfa23a42d455212d4abd96d694877c72ba618d4bf0bf1ecf0c`)
and the supplied prompt `/Users/dustin/Downloads/c169_hqcdlfgmatchcalc1_codex_prompt.md`
(SHA-256 `f871c8652a91f6422b7cf8887b16b29cfeafd782efa65973232cc5504d510181`).
The requested starting commit `4d90e1a4ff410f6b172d125b5ea3800bb0e0a186`
is present. The workspace entered C169 at amended equivalent commit
`5224f533336bae824ee4ec0c8705e9a163ee5cc7`; its only difference from that
baseline is the already-recorded C163 package-root correction in the C168
authority. No C168 scientific record was changed by C169.

The C168 public `new_calculation_manifest()` and
`request_resolution_manifest()` supplied all six rows. No C158 module or
value API is imported. C166 graph nodes and edges added: 0 and 0.

## Exact capsules

The six preserved request/capsule IDs are:

1. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QUARK_FIELD-RI_SMOM-2`
2. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM-2`
3. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QUARK_FIELD-MOMQ-2`
4. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2`
5. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ-2`
6. `C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2`

The sixth record is selected from the C168 public row order and is not
renamed or inferred from its quantity. Each receives exactly one C169
terminal record. The first two are
`C169_HQCDLFGMATCHCALC1_INTERMEDIATE_DOMAIN_INCOMPLETE`; the gluon and qg
vertex records are `C169_HQCDLFGMATCHCALC1_FULL_QCD_SECTOR_INCOMPLETE`; the
coupling record is `C169_HQCDLFGMATCHCALC1_ST_SUBSTRATE_INCOMPLETE`.

## Calculation substrate

The public owner census contains 21 owners: C43, C53, C110, C111, C112,
C127, C128, C129, C130, C131, and C142--C152. Their roles remain separate:
canonical qg, direct contacts, instantaneous fermion/current, free M²,
normal-ordering descendants, local polynomial, source/two-point/projector,
gluon, and vertex authorities. No private upstream builder was called.

The declared coordinate and order records preserve `g_s`, `g_s^2`, `alpha_s`,
`a_s`, `V_B`, `Z_1F`, `g_R`, `g_R/g_s`, signed `m_R`, and `m_R^2` as distinct
typed coordinates. K9, K11, and K13 remain separate. No order label was
promoted into a coefficient.

Propagating insertion pairs are recorded with explicit source-order and
adjoint-orientation requirements. No untyped intermediate state is created:
C141/C143 block quark source/resolvent closure; C151 exposes only a free
gluon domain; C152 exposes only the retained connected/amputated qg domain.
Direct/contact and instantaneous ledgers retain C110/C111, C112, C127, C129,
C130, and all missing terms as unavailable and nonzero—not as zero.
Count-once duplicate ownership is zero, but transitive closure is incomplete.

P0/Q0 zero modes, finite-cell boundaries, residual gauge/link terms, and
omitted interfaces remain explicit. The C43 antisymmetric/PV inverse-
partial-plus prescription is unchanged. Six counterterm directions and nine
null coordinates remain unselected.

Quark field and signed mass remain separate; signed `m_R` is never replaced
by `m_R^2`. Connected, amputated, retained-proper, and complete 1PI qg
vertices remain separate, as do `V_B`, `Z_1F`, `g_R`, and `g_R/g_s`. Restricted
Ward identities are not promoted to Slavnov--Taylor closure.

## Blockers and exact next-calculation capsules

- The RI/SMOM quark-field capsule requires the C141 canonical source/sink
  map, C143 projected resolvent, C146/C147 normalization closure, and the
  C130 residual realization.
- The RI/SMOM signed-mass capsule requires C141 mass-linear source closure,
  C143 signed insertion domain, C149 application to a complete inverse
  two-point object, and C150 counterterm conditions.
- The MOMq quark-field capsule has the same C141/C143 source-domain and
  normalization blockers.
- The MOMq transverse-gluon capsule requires C151 `gg`, `q_qbar`, ghost,
  higher-gluon, zero-mode, boundary, and counterterm sectors.
- The MOMq qg-vertex capsule requires C152 `qgg`, `q_qbar`, pure-gluon,
  complete-1PI, zero/boundary/residual-link, and leg-counterterm sectors.
- The MOMq coupling capsule requires ghost and pure-gluon field factors, a
  complete 1PI qg vertex, full ST-compatible coupling conditions, and
  counterterm conditions.

These are calculation requests, not source-acquisition requests. No absent
sector is encoded as zero, no target coefficient is transcribed, and no
diagnostic is emitted because no complete C169 scientific domain closes.

## Validation and isolation

The package is `src/deuteron_wigner/bridge/hqcdlfgmatchcalc1/` with runtime
metadata in `data/runtime/c169_hqcdlfgmatchcalc1/`. Its package root is
`d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5`.
Public records are immutable mapping proxies; unknown IDs fail closed; the
graph schema rejects arbitrary callables, eval, pickle, dynamic imports,
network access, dense full inverses, and unknown opcodes. No NumPy loading is
performed by C169.

The focused C169 suite passes 4 tests, including 384 live mutations. The
broader C43/C110--C169, C142--C152, C158, C161--C168, clean-build, reload,
request-order, route-order, and protected-boundary checks are recorded in the
companion JSON validation records. The C134 diagnostic remains quarantined;
the inherited untracked C157 replacement test and protected quantum/source
paths remain untouched.

No source was acquired; no web/model-memory coefficient, PDG value, C158
value, physical state, running, threshold, matching window, standard-scheme
adapter, counterterm solution, null representative, Q0/Q1/Q2 mutation, or
TMD/process object was created. Nothing was pushed.
