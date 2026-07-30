# C4 implementation report

## Scope and baseline

C4 begins from documentation-only commit
`e123848b2666e1c9db397e47b1c04c0b7146aae7`, with required C3 commit
`b0a18ce2d1017e102b2be0849abf4d31537874a8` in its ancestry. Before code
changes, 538/538 tests, all nine acceptance builders, 36/36 evidence rows,
162/162 atlas pages, C3 Benchmarks A--D, all 24 C3 injections, the 216-entry
production registry, and all eight authoritative hashes reproduced.

The requested Volume 0--IV TeX sources and
`references/model_construction_note.tex` are absent from this public
repository. Their contents were not invented. C4 uses the equations stated
in the preserved work-package prompt and the present C0--C3 reports, APIs,
manifests, ADRs, roadmap, and formal source.

## Benchmark E: explicit sea and gluon sectors

The sea family is the normalized direct sum
`sqrt(1-P_sea)|qqq> + sqrt(P_sea)|qqqq qbar>`. Its first member has an
explicit positive-x neutral `d dbar` pair. The antiquark density is exactly
zero at `P_sea=0` and its diagonal integrated density is exactly `P_sea`.
Net proton flavor, baryon number, charge, and plus momentum remain
`u=2`, `d=1`, `B=1`, `Q=1`, and one.

The gluon family is
`sqrt(1-P_g)|qqq> + sqrt(P_g)|qqqg>`. Its explicit transverse gluon carries
benchmark momentum fraction 0.2. The stored scalar is `H^g=xg`, so its
integrated EMT contribution is exactly `0.2 P_g` and vanishes structurally at
`P_g=0`.

The sea cluster tensor `epsilon_abc delta_de/sqrt(18)` has unit norm and zero
total-generator residual. It is a cluster basis, not a claim of complete
five-body antisymmetrization. The gluon tensor
`N epsilon_ijm(t^a)_km` uses the declared antisymmetric-pair `rho` octet and
has unit norm with maximum generator residual `5.551115123125783e-17`.
Omitting the adjoint generator or using a singlet times a free gluon fails.

## Common overlap and reductions

Sea, antiquark, and gluon members use the existing `ZeroSkewnessFrame`,
`SymmetricXiZeroRecoil`, and `AnalyticOverlapEvaluator`. No recoil formula or
overlap evaluator was duplicated. Active slots are positive-x typed records.
Wrong species, duplicate multiplicity, nonzero skewness, nonzero Wilson order,
and off-diagonal sectors without a named source fail closed.

One regulated analytic parent supplies TMD, regulated GPD, PDF, direct
double-integral, and current/EMT routes. Direct and sequential routes close
at the forward point and two nonzero transfers for a sea quark, antiquark,
and gluon. Residual categories remain separate. Quark vector moments use
`q-qbar`; gluon moments use `integral H^g` with `H^g=xg`.

This is common-parent algebraic closure. It is not full QCD link shortening,
UV/rapidity matching, soft subtraction, evolution, or physical GTMD/TMD
phenomenology.

## Benchmark F: finite Feshbach equivalence

The exact Hermitian two-sector model evaluates the energy-dependent
Hamiltonian, wave operator, norm kernel, and induced operator. The lower
eigenvalue is `0.14566036193848045`; energy and operator-equivalence residuals
are zero at reported precision. The norm kernel is `1.024104459303322`.
The nontrivial full-space matrix element is `-0.2051814270958522`, while
`POP=0`, directly demonstrating that Hamiltonian-only elimination is
insufficient.

Explicit sea/gluon sectors and their finite-model induced alternatives have
typed exclusion relations and explicit remainder nodes. Selecting both fails
before numerical evaluation.

## Isolation, validation, and limitations

The C4 graph contains only benchmark-only nodes and has no identity or edge
shared with production. The 216 production reductions, C2 graph/default
composition, C3 manifests, production builder, and authoritative outputs are
immutable regression gates. Forty mandatory injected faults have ordered
stable IDs and diagnostics.

Final validation before the normative-source integration pass was 609/609
tests, all nine acceptance/report builders,
36/36 evidence rows, and all 162/162 atlas pages. C3 Benchmarks A--D and all
24 C3 injections remain passing; all 40 C4 injections are detected.

Remaining limitations are intentional C4 boundaries: analytic widths and
probabilities are not fitted; the sector states are finite validation
fixtures rather than Hamiltonian eigenstates; the sea cluster basis is not
fully antisymmetrized; nonzero skewness, ERBL structure, dynamical Wilson
lines, naive-T-odd physics, physical QCD matching, evolution, and nuclear
dynamics are absent.

The exact next package, conditional on the final C4 regression, is a
validation-only one-gluon Wilson-line and light-front-cut pilot based on
Volume III. It must remain disconnected from accepted production.

## Post-completion source availability

On 2026-07-30 the supplied TeX sources for Volumes 0, I, II, III, IV, and V were
preserved under `references/` and indexed in
`references/formalism_volume_index.md`. This does not alter the historical C4
baseline: those sources were absent during C4 implementation.
The subsequent source-integration audit and four resulting corrections are
documented in `c4_normative_integration_report.md`; its post-integration test
count is recorded in the regenerated regression manifest.
