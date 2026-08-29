# C198/HQCDST2 implementation report

Starting commit: `94cefcdcb00144d56d0137308e9d0aeb0319933d`.

The committed C197-to-C198 contract was consumed from
`docs/next_level/c197_c198_hqcdst2_continuation_contract.json`; its SHA-256 is
`0226779f955dd03b88ac219a0d3130bc87a0e8ae85273319ab16fae34fe543f4`. The
prompt SHA-256 is `cf7ebbf73bec4d1fc0cc83c5c986cb8533083acce479850526a7267b4e76bc4a`.

## Result

C198 selected `ST2-A` and produced
`C198_C197_SOURCE_DERIVED_COMPLETE_AVAILABLE_FINITE_BASIS_ST_COUNTERTERM_SYSTEM_AND_CONDITIONAL_SOLUTION_FAMILY_AUTHORITY_READY`.
The package root is
`8b84fc1744ffc15c6b9fe2c9064f178974d4977a08095cc1d9d123e20017f709`.
The single continuation is `C199/HQCDGHOST2`, with contract
`docs/next_level/c198_c199_hqcdghost2_continuation_contract.json`.

The ten exact C197 missing-object records are imported and normalized as
`C197-ST-1` through `C197-ST-10`; none is encoded as zero. The first frontier
is `C197-ST-1`, complete ghost-field renormalization. The available system is
released only conditionally: full ST closure, target MOMq conditions,
standard-scheme conversion, physical input, physical coupling, selected
counterterms, and selected null representatives remain nonclaims.

The immutable public package is under
`src/deuteron_wigner/bridge/hqcdst2/` with compact runtime metadata in
`data/runtime/c198_hqcdst2/`. It imports C197 through its public loader and
does not recompute C196/C197 or any C150/C184/C175/C182/C183 authority. The
C166 dependency graph delta is zero and C158 value inputs are zero.

The registry contains 41 variables: six counterterm directions, nine null
coordinates, identified/source-renormalization/boundary roles, and separate
target, standard, and physical roles. It contains 345 typed identity rows,
including 324 qg rows, ten blocked missing-object rows, three B0 diagnostics,
five boundary/link diagnostics, and explicit target/standard/physical guards.
Ghost, pure-gluon, BRST, and boundary registries contain respectively 7, 5,
1, and 7 records. The residual registry has 13 records. K9/K11/K13 and all
scheme, projector, subtraction, and holonomy fixtures remain separate.

Each of the three resolution systems is a caller-bound 3-by-15 symbolic
Jacobian with rank 1, nullity 14, and left nullity 2. Compatibility is
certified with exact symbolic residual zero; the solution families have the
form `delta theta = delta theta_particular + N u`, with 14 free coordinates.
No representative or physical counterterm is selected.

Topology and count-once closure has 16 owners and zero duplicates. Defining
equations are not counted as independent constraints; external-leg effects,
interfaces, holonomy fixtures, missing rows, restricted coupling, and
retained/complete records remain typed and separate.

## Verification and nonclaims

The C198 suite passed 6 tests, including 384 focused live mutations. The
targeted C142--C153/C161--C198 sweep passed 249 tests, and the C43/C53/C110--
C131 source-owner sweep passed 427 tests. Two network-disabled clean wheels
were byte-identical with SHA-256
`772280cab1781f1b0ef3abbd61ee7fd579f52aa01c062a649316e63abaa492b0`.
Reload, restart, sharding, paging, query-order, route-reversal, and safe-
loading checks passed.

The unrelated pre-existing C134 quarantine remains untouched: its isolated
suite is 2 passed and 1 failed because the preserved legacy expectation is
`4` while the current preserved target manifest is `115`. The inherited
untracked C157 test and the user's unrelated `handoff/ROADMAP.md` modification
were not changed.

No full ST claim, target MOMq result, standard conversion, physical coupling,
physical input, selected counterterm/null representative, state, TMD, Q0/Q1/
Q2 modification, C166 graph mutation, C158 value import, or upstream
recomputation was performed. Nothing was pushed.
