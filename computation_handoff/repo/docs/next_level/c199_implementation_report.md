# C199/HQCDGHOST2 implementation report

Starting C198 completion commit: abbreviated `9bd2752`, resolved to
`9bd27526e1f540cbd5ee3c134a03cba670287a8a`. Final commit is recorded after
this report is staged.

The committed contract
`docs/next_level/c198_c199_hqcdghost2_continuation_contract.json` was consumed
and hash-verified with SHA-256
`44b62eb9997243b48ab0c39f6b35f80fb4611028a0a284c5ca1285cb2b804b94`. The
prompt SHA-256 is
`19febcf5094a0f311ea0b2e94b2649e49da01a1b2f51a12b14b92e9f57eff750`.

## Result

C199 selected `GHOST2-A` and produced
`C199_C198_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_GHOST_FIELD_RENORMALIZATION_AUTHORITY_READY_NEXT_ST_FRONTIER`.
The package root is
`eb8ab6b75093280f7d78905ddb5cb5bce358e1e0c9474b0ce8035ab1c73f8bca`.
The exact continuation is `C200/HQCDGHOSTVERT1`; its frontier object is the
normalized C197 `C197-ST-2`, complete ghost-gluon proper vertex.

The exact C197-ST-1 record is bound from C198: `complete ghost-field
renormalization`, aliases `complete ghost-field renormalization` and
`GHOST_FIELD_RENORMALIZATION`, source-side role, and C197 source root
`6e9991693c54871c945c6eb0e0a16b7555029560f078fb590b2fa2a409a0e7d`. The
decision is `Q0_DECOUPLED_P0_CONDITIONAL_RENORMALIZATION`, not determinant
normalization and not a physical factor.

The decomposition contains 3 Q0, 3 P0, and separate global-sector records.
Q0 is restricted to typed nonzero longitudinal modes and bulk decoupling. P0
uses C174 local scalar modes times adjoint color, with dimensions 288/440/624
for K9/K11/K13. Global SU(3), gauge volume, holonomy, and open color remain
outside the local determinant/domain. External sources comprise 12 records:
both ghost species, both Q0/P0 sectors, and all three resolutions, with
explicit Berezin order, ghost number, parity, color, cut side, and orientation.

The strict no-default parameter schema has 19 required fields and 3 named
nonphysical fixtures. The FP ledger has 72 records: 18 matrix-owner records
and 54 typed nonmatrix boundary/link/cut/holonomy/global interfaces. No dense
inverse is constructed. Determinant, ratio, trace-log, closed loop, open
propagator, proper inverse, field factor, and ghost-gluon response remain
separate. The open two-point has 6 orientation-specific records and uses
guarded sparse/matrix-free symbolic solves. The C175 field-dependent
ghost-gluon response is used source-qualified in 3 resolution records; its
Q0 bulk orthogonality is not promoted to endpoint or link zero.

Boundary/link authority has 18 nonmatrix records. Scalar projector authority
has 9 records across three project finite-basis schemes and resolutions; zero
and global modes are excluded as subtraction points and zero-tree division is
rejected. The ghost convention exposes both product and separate-source
records: only a conditional ghost-antighost product is fixed, with explicit
residual rescaling freedom. `Z_c = Z_bar_c` and a symmetric split are not
assumed. The conditional factor family has 3 records, dimensionless exact
symbolic outward enclosures, six counterterm sensitivities, and nine null
sensitivities; no value is physical or selected.

The ghost-only sensitivity Jacobian is 1x15 with rank 0, nullity 15, and left
nullity 1. The incremental available-system crosswalk replaces exactly three
C198 blocked C197-ST-1 rows. The updated available qg/ST system retains rank
1, nullity 14, left nullity 2, compatibility, and 14-dimensional conditional
solution families. Nine exact C197-ST frontier records remain blocked, in
order from C197-ST-2 through C197-ST-10.

Analyticity, graded adjoint, ghost-number, parity, color covariance, Q0/P0
separation, zero/pole guards, cut/PV, holonomy, and boundary/link support are
recorded. Topology/count-once contains 19 owners with zero duplicates.

## Verification and nonclaims

The C199 suite passed 5 tests including 384 focused live mutations. The
C161--C199 targeted suite passed 214 tests; the C43/C53/C110--C131 and
C142--C153 source/field suite passed 467 tests. Two clean network-disabled
wheels were byte-identical, each 1,444,290 bytes, SHA-256
`f990d73dacab6ad82ee4b5bb5a284ccb4c5731b5adb71ec5a07cf6117b45c8d4`.
Reload, restart, sharding, paging, query-order, route-reversal, and safe-
loading checks passed.

The unrelated C134 quarantine remains untouched: isolated result 2 passed and
1 failed because the preserved expectation is `4` while the target manifest
is `115`. The inherited untracked C157 test, `handoff/ROADMAP.md`, C198 rows
other than the typed C197-ST-1 replacement, C166 graphs, Q0/Q1/Q2, and all
upstream authorities were preserved.

No qg proper vertex, Z1F, coupling, field response, source/contact/
higher-Fock, unrelated ST row, matching, physical ghost factor/coupling,
counterterm/null representative, target/standard condition, state, quantum
object, or TMD was created or recomputed. No remembered ghost formula was
used; Q0 bulk decoupling was not promoted to complete decoupling; bulk
orthogonality was not promoted to endpoint zero; determinant/open-line and
closed/open sign conflations were not made; no nonmatrix interface became a
matrix; global volume was not absorbed; no holonomy loop, resolution average,
continuum extrapolation, C158 value, graph mutation, or push occurred.
