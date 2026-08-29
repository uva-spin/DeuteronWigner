# C35/S0C implementation report

## Scientific result

C35/S0C completes the requested regulator-definition audit with the rigorous
fail-closed selection

```text
selected plan:  S0C-UNAVAILABLE
primary no-go:  C35_DIRECT_EIKONAL_FOCK_GAUGE_COMPLETION_UNAVAILABLE
secondary no-go: C35_EXECUTABLE_SOFT_MODE_BASIS_UNAVAILABLE
outcome:        Branch G
next package:   C36/O4 — replacement regulator architecture for the
                microscopic TMD soft root
```

This is a source-supported negative result, not a numerical failure and not a
zero soft correction.  The present repository can fix the light-front
normalization, define exact real and virtual coordinate charts, transcribe the
modified-delta damping operator, and validate analytic cell and pole-treatment
oracles.  It cannot select a regulator-identical, gauge-complete finite-cell
field realization.  A finite-basis one-loop coefficient is therefore not
defined.  All unavailable quantities remain empty-not-zero or
`NONZERO_UNKNOWN`.

C35 did not start a coefficient evaluation after selecting
`S0C-UNAVAILABLE`.  It did not substitute the continuum modified-delta result,
solve counterterms, construct a microscopic proton TMD, rerun the bridge, or
create a fit, likelihood, posterior, optimizer, reweighting route, emulator,
process prediction, deuteron prediction, inference route, or production route.

## Baseline and immutable ancestry

The authoritative starting commit is

```text
6bdb44be2afc79e817f69ce0e35813da8a394db7
```

The clean C33 baseline, C32 operator-completion ancestor, and required C28
scientific ancestor remain, respectively,

```text
e0b34c74e8f39c9d42cf49cc598f1533d9353a7e
0d7b94a5e86882b23a56d4c1f11900d554756a18
52678312906bf5cc0bb8664e2486d5d676a6b723
```

The inherited roots remain distinct:

```text
C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION       B = 1
C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT    B = 0
C35_SOFT_REGULATOR_COMPLETION_DESCENDANT      B = 0
```

C35 does not place the vacuum soft state inside the C11 proton.  It does not
reinterpret C11 as a renormalized TMD, and it does not alter the exact C32 tree
reduction or the historical C33/C34 results.

The authoritative formal source remains

```text
references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex
SHA-256 613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4
```

The C35 prompt is preserved at
`docs/next_level/c35_s0c_codex_prompt.md`, SHA-256
`1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9`.
The modified-delta source used for the operator and gauge-property audit is
`data/raw/c31_sources/1511.05590.pdf`, SHA-256
`dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d`.
Every retained primary source is classified as
`NOT_OPERATOR_REGULATOR_IDENTICAL` to the inherited C33 finite-cell root.

## Gauge-plan decision

Four mutually exclusive candidates were compiled before any coefficient was
evaluated.

| Candidate | Decision | Exact obstruction |
|---|---|---|
| `S0C-COVARIANT-KREIN` | unavailable | No finite-cell BRST/Krein action, polarization metric, constraint complex, zero-mode sector, or transverse-boundary completion; the modified-delta Wilson operator does not retain the original Wilson operator's gauge properties at finite delta. |
| `S0C-LIGHT_FRONT-PHYSICAL` | unavailable | No complete instantaneous-gluon kernel, constrained zero modes, residual-gauge prescription, or proved map to the covariant modified-delta soft function. |
| `S0C-AUXILIARY-EIKONAL` | unavailable | Available methods use nonidentical Euclidean or spacelike operators; no lightlike Minkowski modified-delta, endpoint, or finite-regulator conversion has been proved. |
| `S0C-UNAVAILABLE` | selected | This is the only source-supported selection: no compatible gauge-complete, regulator-identical realization exists in the repository. |

The selection is a typed supersession of the C34 planned covariant
\(\xi_g\)-scan, not a silent switch of gauge.  In particular, C9's reduced
light-front instantaneous benchmark and C14's finite gauge ledger are not
promoted to BRST, Slavnov--Taylor, or regulator-identical soft-function
closure.

## Exact light-front convention

C35 removes the inherited \(\sqrt 2\) ambiguity using metric signature
\((+---)\) and

\[
 v^\pm=\frac{v^0\pm v^3}{\sqrt2},\qquad
 n^\mu=\frac{1}{\sqrt2}(1,0,0,1),\qquad
 \bar n^\mu=\frac{1}{\sqrt2}(1,0,0,-1).
\]

Thus

\[
 n^2=\bar n^2=0,\qquad n\!\cdot\!\bar n=1,
 \qquad n\!\cdot k=k^-,\qquad \bar n\!\cdot k=k^+,
\]

and

\[
 k^2=2k^+k^- - \bm k_T^2.
\]

The Fourier convention is

\[
 A(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ik\cdot x}A(k).
\]

Under the line rescaling

\[
 n\to\lambda n,\qquad
 \bar n\to\lambda^{-1}\bar n,
\]

the rapidity regulators transform as

\[
 \delta^-\to\lambda\delta^-,\qquad
 \delta^+\to\lambda^{-1}\delta^+,
\]

so \(\delta^+\delta^-\) is invariant.  The source convention with
\(n\cdot\bar n=2\) maps to the project normalization through
\(\delta^\pm_{\rm project}=\delta^\pm_{\rm source}/\sqrt2\).  These exact
relations validate convention conversion; they do not define a gauge-field
mode basis.

## Coordinate and measure oracles

### Real on-shell chart

C35 defines the exact massless chart

\[
 k^+=\frac{\kappa e^y}{\sqrt2},\qquad
 k^-=\frac{\kappa e^{-y}}{\sqrt2},\qquad
 k_x=\kappa\cos\phi,\qquad
 k_y=\kappa\sin\phi,
\]

with \(\kappa>0\), finite \(y\), \(0\leq\phi<2\pi\), positive energy
\(k^0=\kappa\cosh y\), and

\[
 d\Pi_{\rm real}
 =\frac{\kappa\,d\kappa\,dy\,d\phi}{2(2\pi)^3}.
\]

The mass-shell residual \(2k^+k^- - \bm k_T^2\) vanishes analytically.

### Virtual chart

The virtual geometric chart uses independent
\((k^+,k^-,k_x,k_y)\) and

\[
 d\Pi_{\rm virtual}
 =\frac{dk^+\,dk^-\,dk_x\,dk_y}{(2\pi)^4},\qquad
 k^2+i0=2k^+k^- - \bm k_T^2+i0.
\]

The coordinate change and measure are exact.  No regulator-identical contour,
pole-crossing rule, or virtual finite-cell collection is available, so the
virtual chart is geometric rather than a physical loop quadrature.

### Limited cell and singular-integral oracles

A normalized scalar top-hat cell can be generated on the real chart and its
normalization checked exactly.  This proves a scalar measure convention only;
it is not a normalized gauge mode and is not one of the missing R1--R3 mode
collections.  C35 also implements the analytic identity

\[
 \frac{1}{x\mp i0}=\operatorname{PV}\frac1x\pm i\pi\delta(x)
\]

and a finite-delta logarithmic comparison on a prototype pole-containing
interval.  Center sampling of a singular cell is forbidden.  No physical
finite-basis pole cell or virtual contour was integrated.

## Modified-delta operator and the decisive gauge limitation

For a finite longitudinal segment of length \(L\), mode frequency \(\omega\),
and positive damping parameter \(\delta\), C35 records the operator-level
factor

\[
 I_L(\omega,\delta)
 =\int_0^L ds\,e^{(-\delta+i\omega)s}
 =\frac{e^{(-\delta+i\omega)L}-1}{-\delta+i\omega},
\]

with infinite-segment limit

\[
 I_\infty(\omega,\delta)=\frac{1}{\delta-i\omega}.
\]

The damping belongs inside the path-ordered Wilson operator, not as metadata
or a factor applied after integration.  The source also states that the
modified-delta Wilson lines do not possess the gauge properties of the
original Wilson operator at finite \(\delta\); those properties are recovered
only in the prescribed regulator-removal limit, with power-divergent delta
terms discarded according to the source prescription.  C35 keeps the
resulting finite-delta Ward defect explicit.  It does not call this defect
gauge closure, tune it away, or use the \(\delta\to0\) target to certify an
undefined finite-cell action.

Because the inherited finite-cell root supplies neither a gauge-restoring
completion nor an alternative regulator with a proved conversion, this source
fact blocks all three positive gauge candidates.

## Mode, Wilson, and trajectory status

The inherited R1--R3 dimensions remain 3,841, 30,721, and 103,681.  They are
support descriptors, not materialized mode collections.  C35 creates no heavy
mode arrays and claims no gauge-mode normalization or completeness.  Missing
remain:

- the gauge metric or physical-polarization completeness relation;
- complete cell boundaries, mode functions, commutators, nodes, and weights;
- a partition of unity between the \(n\) and \(\bar n\) rapidity regions;
- nested refinement maps;
- a regulator-identical virtual contour and zero-mode sector;
- an executable finite-volume representation of every longitudinal segment
  and the transverse link at infinity.

Nine factorized regulator axes are typed—UV extent, IR extent, rapidity
window, rapidity-cell size, transverse extent, transverse-cell size,
zero-mode cutoff, line-length cutoff, and quadrature order—but have no
evaluated points.  No trajectory fit or continuum extrapolation is performed.

## Status of all eighteen one-loop contributions

The contribution matrix is complete as an inventory and incomplete as
physics.  Every entry is `UNRESOLVED_BLOCKING` with value semantics
`NONZERO_UNKNOWN`:

| Contribution | C35 status |
|---|---|
| `N_NBAR_EXCHANGE` | `UNRESOLVED_BLOCKING` |
| `CONJUGATE_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` |
| `SAME_DIRECTION_LINE_EXCHANGE` | `UNRESOLVED_BLOCKING` |
| `REAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` |
| `VIRTUAL_ONE_SOFT_GLUON` | `UNRESOLVED_BLOCKING` |
| `WILSON_LINE_SELF_ENERGY` | `UNRESOLVED_BLOCKING` |
| `CUSP_ENDPOINT` | `UNRESOLVED_BLOCKING` |
| `TRANSVERSE_CLOSURE` | `UNRESOLVED_BLOCKING` |
| `AUXILIARY_FIELD_SELF_ENERGY` | `UNRESOLVED_BLOCKING` |
| `SOFT_VACUUM_ENERGY` | `UNRESOLVED_BLOCKING` |
| `LIGHT_FRONT_INSTANTANEOUS` | `UNRESOLVED_BLOCKING` |
| `GAUGE_FIXING` | `UNRESOLVED_BLOCKING` |
| `GHOST` | `UNRESOLVED_BLOCKING` |
| `ZERO_MODE` | `UNRESOLVED_BLOCKING` |
| `BASIS_BOUNDARY` | `UNRESOLVED_BLOCKING` |
| `RAPIDITY_COUNTERTERM` | `UNRESOLVED_BLOCKING` |
| `UV_COUNTERTERM` | `UNRESOLVED_BLOCKING` |
| `RESIDUAL_LINE_MASS_COUNTERTERM` | `UNRESOLVED_BLOCKING` |

No entry is assigned zero from dimensional-regularization scalelessness,
topology name, ghost folklore, or an unselected gauge action.  No direct
Wilson expansion, real/cut plus virtual assembly, or count-once residual is
available.

## Bare result, renormalization, and continuum conversion

The exact tree identity remains

\[
 S_{\rm FB}^{(0)}(b_T)=1.
\]

The declared one-loop convention remains

\[
 S_{\rm FB}^{\rm bare}
 =1+a_s C_F S_{\rm FB}^{[1],\rm bare}+\mathcal O(a_s^2),
 \qquad a_s=\frac{\alpha_s}{4\pi}=\frac{g_s^2}{(4\pi)^2},
 \qquad C_F=\frac43.
\]

There is no value for \(S_{\rm FB}^{[1],\rm bare}\).  Its status is
`NONZERO_UNKNOWN`.  Consequently the UV, rapidity, and residual-line-mass
counterterms are empty-not-zero and were not solved.  There is no renormalized
finite-basis soft function, gauge or cusp residual, finite-basis-to-continuum
conversion, inverse, round trip, or continuum trajectory.

The continuum result from arXiv:1511.05590 remains a source transcription.
C35 does not provide the requested independent graph-level or direct-integral
second reconstruction.  It is not substituted for the missing finite-basis
coefficient.

## Zero mode, boundary, and C32 continuation

The inherited policy

```text
EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL / AUDIT_REQUIRED
```

does not make the zero-mode contribution vanish.  Its Ward, line-energy,
rapidity, transverse-link, and conversion-constant effects remain
`NONZERO_UNKNOWN`.  Basis-boundary, cusp/endpoint, and transverse-infinity
junction contributions remain separately auditable and unresolved.

`SOFT_LIMIT_C35` is an explicit empty-not-zero soft-side object.  No exact map
to the frozen C32 spacelike-off-shell collinear regulator is available, and
soft/zero-bin equality is not inferred from a continuum citation.  Therefore
the C32 continuation gate is false and no microscopic proton export exists.

## Reproducibility and isolation

Machine-readable identities and exact residuals are generated by
`scripts/build_c35_manifests.py` and validated independently by the C35 test
and validation layer.  Final test, builder, requirement, injection,
determinism, ancestry, production-registry, and immutable-artifact results are
reported in `docs/next_level/c35_regression_report.json` rather than duplicated
as mutable prose here.

The C35 layer consists of 53 frozen formal architecture classes, 61
content-addressed JSON deliverables, four explanatory reports, 326 distinct
coverage rows, 93 distinct negative fault modes, and 2,511 executed semantic
fault--target injections.  Those injections cover every architecture class,
all eighteen contribution slots, and all twenty-seven frozen holdouts.

The C35 provenance graph records hard-false consumption of ART25 members,
process data, bridge residuals, inference, and production.  The 216-route
registry and all eight authoritative artifacts remain immutable.
`MSHT20_REP/` remains outside Git and untouched.

One descendant-only maintenance guard was required in
`scripts/build_c34_manifests.py`.  C34 had hashed the current bytes of the
append-only roadmap and formalism index, so the mandated C35 handoff entries
made C34's historical reconstruction nondeterministic.  The guard now hashes
the versions stored in the C34 completion commit whenever C34 is rebuilt.
This changes no C34 physics or manifest: all 52 C34 JSON deliverables still
reproduce byte-for-byte.  The other 72 audited C34 package paths and all 74
C33 paths remain byte-identical.

## Exact continuation

The exact next package is

```text
C36/O4 — replacement regulator architecture for the microscopic TMD soft root
```

C36/O4 must select or construct a gauge-complete, regulator-identical soft
architecture before another finite-basis coefficient attempt.  It must not
continue by filling the eighteen slots inside the incompatible inherited
descriptor or by importing the continuum coefficient as a substitute.
