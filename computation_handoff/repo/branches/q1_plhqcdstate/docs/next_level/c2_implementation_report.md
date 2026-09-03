# C2 implementation report

## Scope

C2 migrates the accepted forward boundary to native typed reduction identities
and an enforceable provenance/composition layer. It adds no physical formula,
parameter, phase, width, response, evolution kernel, hard factor, positivity
repair, or nonzero-transfer model.

## Implementation

The C1 package is extended by:

* `formal/reduction.py`: `ReductionId`, `NativeReduction`,
  `ReductionRegistry`, reduction kinds, availability, and transform/moment
  validation;
* `formal/accepted_reductions.py`: deterministic accepted-boundary registry;
* `formal/provenance_graph.py`: typed nodes, relations, DAG checks,
  alternatives, replacements, exclusions, and `CompositionPlan`;
* `formal/trace.py`: metadata-only output/row/composition/reduction queries.

The registry contains 216 legal routes: 18 named functions × four
quark/antiquark flavors × two staple directions, plus 18 gluon functions ×
two staple directions × two color classes. The gluon TT trace/linear
degeneracy is represented by the accepted
`f1TT_minus_h1TTperp` combination rather than fabricating two separately
observable functions. All routes are honestly forward-only.

The graph contains canonical/resolved artifacts, component-plan nodes,
decorated-operator and named-projection nodes, 36 evidence nodes, central and
alternative mechanisms, ensemble semantics, link/color alternatives, and
validation consumers. The default plan selects the already accepted resolved
parent; it does not recompute or reorder its internal physics.

## Enforced rules

The validator rejects CP plus legacy response, direct plus screened phase,
duplicate NNpi, benchmark promotion, simultaneous wave functions, additive
Hessian partners, future plus past links, canonical f plus d addition,
replacer plus replacement target, duplicate CSB, unsupported hidden-color
promotion, ancestry cycles, orphan outputs, and duplicate reduction IDs.

## Normative sources

Present: corrected Volume 0 architecture note, model-construction note, C0
and C1 reports/manifests/ADRs, roadmap, context, and decision log. Absent:
the requested Volume I and Volume II TeX sources. Missing formal sources are
reported rather than silently reconstructed.

## Regression and limitations

The exact starting commit is
`4613318aa7e262e7482978c4198d8e72a4c73c09`. Pre-change validation reproduced
498/498 tests. The final suite passes 519/519 tests; all nine acceptance
builders, 36/36 evidence rows, and 162/162 atlas pages pass. All eight full
before/after hashes are stored in `c2_regression_report.json`. The final local
commit is recorded by `git rev-parse HEAD` and in the operational handoff
because a Git commit cannot contain its own hash.

Numerical kernels and writers remain legacy implementations behind typed
registry boundaries; private helpers still use arrays and scalar coordinates.
Nonzero-transfer reductions remain unavailable. These limitations are
architectural debt, not silently completed physics.

## Exact next package

**C3 — zero-skewness momentum-fiber, recoil-map, and analytic common-overlap
pilot.** Implement typed incoming/outgoing fibers, exact active/spectator
recoil, and a common quark/gluon overlap interface on analytic two- and
three-body benchmarks. Prove forward identity, transfer reversal, unit
Jacobian, Hermiticity, support, and commuting toy reductions while remaining
disconnected from accepted central artifacts.
