# C1 implementation report

## Result

C1 adds a typed convention and operator-identity spine around the accepted
canonical model. It does not introduce a Hamiltonian, wave function, TMD
formula, fit parameter, evolution route, positivity repair, Wilson dynamics,
process factor, or provenance exclusion complex. Numerical arrays and
authoritative writers are unchanged.

The implementation lives in `src/deuteron_wigner/formal/`:

* `coordinates.py`: eight coordinate kinds and conjugacy validation;
* `transverse_rank.py`: rank, mass, Bessel and Fourier-phase identity;
* `sector_space.py`: versioned resolution/sector identity;
* `gauge_path.py`: Wilson paths and ordered gluon link/color identity;
* `operator_identity.py`: decorated identity and operation completeness;
* `maps.py`: five map classes, explicit composition and adapters;
* `diagnostics.py`: structured fail-closed diagnostics;
* `legacy_adapters.py`: read-only registry and radial-transform wrappers.

## Normative-source status

The corrected Volume 0 architecture note, construction note, C0 audit,
coverage/baseline/migration documents, five C0 ADRs, roadmap, project context,
and decision log were inspected. The prompt’s proposed
`references/volume_i_regulated_light_front_foundations.tex` is not present in
the repository; no substitute contents were invented. C1 therefore follows
the concrete Volume I requirements embedded in the supplied C1 work-package
prompt and records that missing source as documentation provenance, not as a
physics default.

## Integration and deliberate boundary

The accepted registries, `TMDScheme`, `TMDScalePoint`, Fourier conventions,
and radial Bessel implementation are consumed directly by read-only adapters.
Every accepted quark and antiquark registry entry is decorated for `u`, `d`,
`ubar`, and `dbar`; every gluon entry is decorated separately for `F_TYPE`
and `D_TYPE`. The resulting machine report contains 110 identities. Exact
known scheme and scale values are populated. Gluon flavor is explicitly
`NOT_APPLICABLE`, never `UNSPECIFIED`.

Internal private helpers still use arrays and scalar `b`. This is intentional
adapter-only migration: public construction/registry/transform composition
can obtain and validate typed identities, while changing specialized formulas
is excluded from C1. Native typed reductions and complete provenance edges
belong to C2.

## Negative injection coverage

`tests/test_c1_formal_spine.py` rejects:

1. `B_DELTA` at a `B_TMD` boundary;
2. partonic `K_T` as nuclear `P_T_NUCLEAR`;
3. `J0` for rank one and rank two;
4. absent mass, wrong mass units, and wrong Fourier phase;
5. future/past identification;
6. fundamental/adjoint interchange;
7. gluon `F_TYPE`/`D_TYPE` substitution and unruled link reversal;
8. unspecified production path metadata;
9. sector conflation by shape;
10. endpoint-incompatible and scheme-missing map composition;
11. an adapter lacking loss/remainder declarations;
12. incomplete production operator identity.

Every failure is an `ArchitectureError` containing its stable requirement ID,
expected identity, received identity, and suggested adapter field.

## Regression

The exact pre-change commit was
`5d4641f31d6a472c27ceed982856e65d0ff4c3cb`; it reproduced 484/484 tests.
`c1_regression_report.json` records row counts, column ordering, inferred
dtypes, and SHA-256 comparisons for all eight parents/correlator tables.
All are byte-identical. New metadata is stored only under `docs/next_level/`.

The final suite passes 498/498 tests. All nine documented acceptance/report
commands pass, 36/36 evidence rows pass, and all 162 required atlas pages
render. These counts and the artifact hashes are recorded in the regression
JSON.

## Remaining honest limitations

* Volume I source file is absent.
* Bare GTMD objects do not yet natively carry the decorated identity.
* Private nuclear, evolution, pion and process helpers retain untyped arrays
  and scalar coordinates behind the adapter boundary.
* Specialized rank-aware formulas are metadata-wrapped, not rewritten.
* The full replacement/exclusion provenance complex is intentionally deferred.

## Exact next package

**C2: native typed reduction and provenance-graph migration of the accepted
boundary.** Replace adapter-only projection/composition boundaries with native
typed `RED` maps and an enforceable baseline/additive/exclusive/replacement
graph, retaining byte-identical regression. Do not introduce a microscopic
Hamiltonian in C2.
