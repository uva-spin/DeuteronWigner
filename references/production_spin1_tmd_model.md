# Superseded exploratory spin-1 TMD closure model

Date: 2026-07-25

> This reduced-amplitude model is not derived from the project's
> light-front GTMD parent and is superseded as a production result. See
> `references/production_tmd_architecture_audit.md`. Its outputs are retained
> only as exploratory closure and plotting regression fixtures.

## Delivered model

`ReducedCorrelatorTMDModel` replaces the legacy independent-prior
completion for production studies. It generates the full leading-twist
spin-1 basis from six shared reduced helicity structures:

1. longitudinal parton helicity;
2. quark transversity or gluon linear polarization;
3. nuclear spin--orbit interference;
4. diagonal tensor polarization;
5. tensor--orbital interference;
6. double-helicity-flip coherence.

The named TMDs are fixed linear projections of those reduced structures.
They are therefore correlated within a species and flavor. There is no
independent random amplitude or uncertainty prior attached to an
individual missing TMD.

The nuclear orbital scale is

\[
\omega_D=\sqrt{P_D(1-P_D)}
\]

with the AV18 baseline \(P_D=0.0578\). Tensor and double-flip structures
scale with the same \(D\)-state and tensor-coherence parameters. All T-odd
functions share a single Wilson-line/lensing phase and reverse sign
exactly between future-pointing SIDIS and past-pointing DY links.

For an entry of definite transverse rank \(r\), the named coefficient has
the regular radial form

\[
F_r(k_T)=c_r f_1(k_T)
\left(\frac{M_D}{\sqrt{\langle k_T^2\rangle}}\right)^r
\exp\!\left[-\frac{r k_T^2}{2\langle k_T^2\rangle}\right].
\]

Consequently its physical correlator modulation
\((k_T/M_D)^rF_r/f_1\) vanishes at the origin for every \(r>0\) and remains
bounded. The exceptional rank-zero T-odd quark \(h_{1LT}\) uses the
zero-marginal radial node required by its absence from the collinear basis.

## Phenomenological anchors

The baseline transfers the already calculated \(x_N=0.1,Q=5\) GeV
normalizations from
`outputs/complete/spin1_tmd_phase_space.csv`:

- CT18NNLO plus AV18 impulse normalization for quark, antiquark, and gluon
  \(f_1\);
- BDSSV24-NLO isoscalar helicity with deuteron depolarization for \(g_1\);
- AV18 tensor impulse convolution for \(f_{1LL}\);
- the declared 0.7-Soffer phenomenological quark transversity anchor;
- the evolved gluon W-term origin normalization for the gluon baseline.

The last item is an origin-value normalization transfer to the production
Gaussian, not a new extraction of the gluon collinear integral.

## Production grid and products

The dense table
`outputs/production_tmds/spin1_tmds_x010_q5.csv` contains:

- gluon, \(u,d,\bar u,\bar d\);
- all 91 species/flavor TMD functions;
- SIDIS and DY links;
- 241 points over \(0\le k_T\le2\) GeV;
- dimensional \(F(x,k_T;Q)\) in GeV\(^{-2}\);
- supplemental rank-weighted ratios to \(f_1\);
- separate lower and upper columns for seven uncertainty or sensitivity
  studies.

The separate components are:

- PDF/anchor normalization;
- deuteron \(D\)-state and tensor-coherence dependence;
- transverse-profile width;
- evolution broadening;
- common gauge-link phase;
- shared correlator-mechanism parameters;
- numerical tolerance.

No combined confidence band is defined. These components do not all have
probabilistic interpretations.

The figure tree `outputs/figures/production_tmds/` contains a central
atlas, one band atlas for every separate component, and a supplemental
ratio atlas for each requested species/flavor. PDF files are the
publication vector products; PNG files support rapid visual inspection.

## Validation

`outputs/production_tmds/validation.json` records successful checks of:

- complete basis and dense common grid;
- finite and ordered component envelopes containing the central member;
- exact SIDIS/DY sign reversal for every T-odd function;
- process invariance for every T-even function;
- positive-rank origin limits;
- unit physical-modulation bounds;
- the zero transverse marginal of quark and antiquark \(h_{1LT}\);
- numerical smoothness of every central curve.

The full repository suite passes 161 tests in the configured LHAPDF
environment.

## Interpretation and limitations

This is a complete, coherent phenomenological baseline for model and
sensitivity studies. It is not a global TMD fit, and its separate bands are
not experimental confidence intervals. The common reduced-amplitude
construction supplies symmetry correlations and model predictions for all
functions, but current data do not independently determine every reduced
structure.

The projector is an algebraic representation of the allowed discrete
symmetries and transverse-rank sectors. No additional topological
invariant is introduced because this real radial baseline has no
nontrivial bundle, winding, or patching obstruction. The gauge-link phase
is globally single-valued. Adding topology merely as ornament would not
add a physical constraint here.

PennyLane is not used in this phase: a quantum simulation would reproduce
finite-dimensional helicity linear algebra already evaluated exactly and
would not add empirical information or a stronger validation.
