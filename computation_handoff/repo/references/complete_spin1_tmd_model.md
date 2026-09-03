# Complete constrained spin-1 TMD model

Date: 2026-07-25

> Superseded for production use by
> `references/production_spin1_tmd_model.md`. This document describes the
> earlier independent-prior completion retained for regression and
> comparison only.

## Delivered scope

The numerical catalog covers the complete leading-twist basis:

- 19 gluon TMDs;
- 18 quark TMDs and 18 antiquark TMDs for each included flavor;
- target sectors U, L, T, LL, LT, and TT;
- future-pointing (SIDIS) and past-pointing (DY) gauge links;
- \(x_N=0.02,0.05,0.1,0.2,0.4,0.6\);
- \(k_T=0,0.25,0.5,1.0,1.5\) GeV;
- \(Q=2,5,10\) GeV.

The central catalog and 95% model bands are in
`outputs/complete/spin1_tmd_phase_space.csv`. Every row identifies whether
the result is a derived anchor or a constrained completion.

## Physics layers

### Derived or anchored

- Gluon \(f_1^g\), \(g_1^g\), and \(h_1^{\perp g}\): small-\(b_T\) matched,
  one-loop CSS-evolved calculation with the intrinsic/Collins-Soper profile
  envelope.
- Quark, antiquark, and gluon \(f_1\): AV18 impulse convolution of CT18.
- Quark, antiquark, and gluon \(f_{1LL}\): AV18 tensor impulse convolution
  with the explicit \(f_{1LL}=-(2/3)\delta_Tf_1\) adapter.
- Quark and antiquark \(g_1\): BDSSV24 isoscalar input with the standard
  AV18 deuteron depolarization factor \(1-3P_D/2\).
- Quark and antiquark \(h_1\): 0.7 of the Soffer ceiling. This is a declared
  phenomenological closure assumption, not a transversity extraction.

### Constrained completion

All remaining functions use channel-correlated amplitude priors. Their
physical rank-weighted modulations are damped as

\[
R_r(k_T)=a\left(\frac{k_T}{\sqrt{\langle k_T^2\rangle}}\right)^r
\exp\left[-\frac{r k_T^2}{2\langle k_T^2\rangle}\right].
\]

This makes positive-rank modulations vanish kinematically at the origin and
remain bounded. The hierarchy tightens from vector to LL/LT and TT sectors.
The exceptional rank-zero quark \(h_{1LT}\) has a node factor that makes its
unweighted transverse integral exactly zero.

## Constraint enforcement

The implementation checks:

1. every rank-weighted modulation is below the unit positivity ceiling;
2. the sum of modeled modulations in each target-polarization block remains
   below a conservative unit budget;
3. all T-odd functions reverse sign exactly between SIDIS and DY links;
4. all positive-rank physical modulations vanish at \(k_T=0\);
5. the complete registry is returned with no missing functions;
6. the \(h_{1LT}\) transverse integral vanishes numerically.

These are conservative sufficient constraints, not a substitute for a
future fit of the complete spin-density matrix.

## Predictive coverage

There are 55 species-level functions: 31 T-even and 24 T-odd.

- 29 functions are sign-resolved at every nonzero point in the declared
  grid.
- 99.77% of nonzero T-even phase-space points are sign-resolved.
- Small T-even exceptions occur at high \(k_T\) in the gluon profile
  envelope, where the W-term-only calculation lacks a Y term.
- T-odd bands intentionally include zero. Process sign reversal is
  predicted, but absolute signs and magnitudes require gauge-link dynamics
  or process data.
- Across the full basis, 57.81% of nonzero phase-space points are
  sign-resolved.

Detailed coverage is in
`outputs/complete/spin1_tmd_predictive_coverage.csv` and its JSON summary.

## Interpretation boundary

“Complete” means every leading-twist spin-1 function has a finite,
process-labeled numerical prediction and uncertainty band. It does not mean
every function is first-principles derived.

The catalog is suitable for phase-space sensitivity studies, identifying
promising harmonics, testing sign reversals and null limits, and planning
which functions need data or lattice input. It is not a precision extraction
of T-odd amplitudes and does not describe high-\(k_T\) cross sections that
require a fixed-order Y term.
