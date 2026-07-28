# Rich spin-1 dynamical extensions

This document is the provenance and validity map for WP10. It supplements,
but does not weaken, the parent-first architecture in `handoff/ROADMAP.md`.
Every item below is either a fitted input, a sourced model scenario, or an
explicit operator boundary. None is promoted to an exact QCD prediction.

## Quark gauge-link and T-odd inputs

- Sivers: BPV20 500-replica arTeMiDe input, with future-pointing SIDIS as
  the reference and exact future/past reversal.
- Boer--Mulders: flavor-dependent Barone--Melis--Prokudin-style
  proportionality composed with BPV20. Its coefficients are independent of
  the Sivers fit and constitute a model axis, not a joint fit covariance.
- `gauge_link_phase.py` provides an amplitude-level alternative in which
  Sivers and Boer--Mulders have independent operator/flavor phases. A common
  universal phase is prohibited.

Production evidence:
`quark_*_rich_medium.csv`, `rich_todd_parent_ensemble.csv`, and
`rich_spin1_todd_parent_atlas.pdf`.

The quark axial tensor functions \(g_{1LT}\) and \(g_{1TT}\) now have two
additional, separately identified production layers:

1. independent flavor/operator phase scenarios with a common full-density
   positivity cap;
2. a screened one-gluon transverse rescattering calculation coupled to the
   AV18 D probability and signed S--D radial overlap.

Their five-page comparison atlas and complete retained-helicity tables are
documented in `references/quark_axial_tensor_todd.md`. The explicit
rescattering prediction is orders of magnitude smaller than the direct phase
envelope; this hierarchy is retained rather than tuned away.

## Worm gears and pretzelosity

- \(g_{1T}\): Yang et al., arXiv:2403.12795 Eq. (46) and Table IV. The
  central \(u,d\) fit is active. The paper's sea-zero fit assumption is
  retained as a fit boundary, not interpreted as a physical null result.
  The published replica covariance is not available in machine-readable
  form, so this input is not assigned a fabricated confidence band.
- \(h_{1L}^{\perp}\): independent WW central boundary in the fit-informed
  scenario. `WWBreakingModel` supports separate genuine quark--gluon--quark
  breaking for both worm gears.
- Pretzelosity: independent \(u,d,\bar u,\bar d\) signed fractions of the
  transverse-moment positivity ceiling. This is a nonperturbative model
  scenario motivated by the vanishing massless-quark perturbative
  rank-two matching (arXiv:1808.10560), not a fit or lattice determination.

The alternative `pdf_anchored_oam` parent replaces all five structures with
explicit S/P-even/P-odd/D LF bilinears. It is an OAM sensitivity comparison,
not a statistical member of the fit-informed ensemble.

## Gluon f/d T-odd color structures

Independent CGI-GPM \(f^{abc}\) and \(d^{abc}\) gluon-Sivers components use
the numerical constraints and scenarios of D'Alesio et al.,
arXiv:1902.02425. The remaining five leading-twist spin-1 gluon T-odd
structures \(h_{1L}^{\perp}\), \(h_1\), \(h_{1T}^{\perp}\),
\(g_{1LT}\), and \(g_{1TT}\) are independent rank-scaled f/d model
amplitudes. They are not consequences of the Sivers fit. Observable-specific
hard color weights are deliberately not inferred at the universal-parent
stage. Future/past reversal is exact and the full \((3,3,2,2)\) correlator
is serialized for each member.

Production evidence:
`complete_gluon_todd_multiplet.csv`, its correlator table, and
`complete_gluon_todd_multiplet_atlas.pdf`.

That rank-scaled boundary is retained as a historical comparison. The
preferred source-informed prediction is now
`gluon_todd_two_stage_predictions.csv` with atlas
`gluon_todd_two_stage_prediction_atlas.pdf`. It uses the full-\(g_1+g_2\)
spectator hierarchy and published node structure of arXiv:2402.17556 for
the four spin-half structures. The spin-1-only \(g_{1LT}\) and \(g_{1TT}\)
use AV18 S--D interference and rank-one/rank-two screened adjoint-eikonal
moments.

The paper's 100 fitted replicas were not released and its results are at
\(Q_0=1.64\) GeV without TMD evolution. Thus the Q=5 GeV normalization and
band are explicitly source-informed model scenarios, not a reproduction of
the paper's 68% interval. Positivity is imposed after composition with the
complete AV18 \(6\times6\) density. The f-type links are
\([+,+]/[-,-]\), while d-type links are \([+,-]/[-,+]\); their strengths
remain independently configurable and \(5/9\) is only the paper's
equal-vertex boundary.

## Polarized and tensor shadowing

The inclusive diffractive response anchors only target-U/gluon-trace or the
corresponding quark vector-U projection. Axial, transverse, circular,
linear, L/T, LL, LT, and TT responses are independent named model ratios.
The quark implementation uses H1 2007 Jets DPDF plus the FGS coherent
mechanism; the gluon scenario uses the same inclusive diffractive class with
separate target and gluon-polarization ratios.

Shadowing is evaluated at \(x_N=0.01\), where coherence is active. Its
configured response tends to zero at the standard \(x_N=0.1\) presentation
boundary. This is a regime statement, not a missing curve.

Quark projection plots and production rows are restricted to
\(k_T\leq1.2\) GeV at this small-\(x\) point. Beyond that boundary the
Gaussian parent is below numerical resolution and rank-conditioned inverse
projection amplifies roundoff; no high-rank tail is interpreted physically.

## Meson exchange

The pion correlator composes:

1. Miller's spin-resolved Sullivan NNπ recoil kernel
   (arXiv:1311.4561);
2. the Fock-normalized NN/NNπ probability and plus-momentum ledger;
3. JAM21 pion PDFs;
4. the Vpion19 intrinsic \(b_T\) profile;
5. a common rank-zero Fourier--Bessel transform.

Only vector U and LL structures, \(f_1\) and \(f_{1LL}\), are generated.
Axial, transversity, vector-target, and T-odd pion structures are exact
operator boundaries for a spin-zero pion in this component. The pion is
exported separately because a fully coupled transverse NNπ recoil
counterterm remains a replaceable nuclear mechanism.

## Effective non-nucleonic cluster

The Kaur et al. effective two-cluster vector-current LF wave
(arXiv:2507.09886) is composed with CT18 and BDSSV24 cluster PDFs.
Transverse momentum comes from cluster motion; intrinsic parton-in-cluster
\(k_T\) remains at its collinear boundary. The implemented correlator
supports \(f_1\), \(g_1\), and \(f_{1LL}\). It is a sensitivity to deeply
bound/non-nucleonic structure and is not interpreted as an extracted
hidden-color probability.

## OAM interference

`oam_interference.py` assigns definite transverse \(m\) to LF partial waves.
T-even TMDs are real bilinears; T-odd TMDs are imaginary bilinears with an
explicit staple sign. The PDF-anchored scenario contains:

- S, \(m=0\);
- real P-even, \(m=1\);
- imaginary P-odd/eikonal, \(m=1\);
- D-like, \(m=2\).

Wave-disable limits, azimuthal harmonics, OAM rank, and staple reversal are
tested. Coefficients remain independent model parameters. The scenario is
kept separate from the fit-informed central result to prevent double
counting.

## Reproduction

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_parent_derived_quark_tmds.py ...
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_nonnucleonic_cluster_tmds.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_spin_resolved_pion_tmds.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_polarized_tensor_gluon_shadowing_scenarios.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_complete_gluon_todd_multiplet.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_spectator_informed_gluon_todd.py
MPLCONFIGDIR=/private/tmp/deuteron-mpl PYTHONPATH=src \
  /Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_gluon_todd_two_stage_atlas.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_wp10_production_ledger.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_wp10_acceptance_report.py
```

The authoritative paths are in `outputs/figures/figure_index.json`. The
machine-readable current completion state is
`validation/wp10_manifest.json`; verified evidence and the exact regression
count are in `outputs/validation/wp10_acceptance_report.json`.
