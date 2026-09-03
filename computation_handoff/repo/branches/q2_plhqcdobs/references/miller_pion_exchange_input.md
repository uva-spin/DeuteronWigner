# Tensor-polarized pion-exchange input

## Implemented scope

`pion_exchange.py` implements the collinear tensor-polarized Sullivan-pion
contribution of G. A. Miller, *Phys. Rev. C* **89**, 045203 (2014),
arXiv:1311.4561. It evaluates the published AV18 \(S\)- and \(D\)-wave
radial integrals, the dipole \(\pi NN\) form factor, the tensor light-cone
distribution

\[
\delta f_\pi=f_{uu}^{0}+\frac{1}{\sqrt2}f_{uw}^{2}
              +f_{ww}^{0}-\frac14 f_{ww}^{2},
\]

and its convolution with an isoscalar pion PDF. This is a separate
`meson_exchange` parent and is not absorbed into impulse, off-shell, CSB, or
coherent terms.

The pion PDF is the public JAM21 NLO ensemble (`JAM21PionPDFnlo`,
arXiv:2108.05822). Every released member, including member 0, is marked as a
replica. Production therefore uses the mean of all 786 replicas as the
central prediction and their sample standard deviation as the PDF
uncertainty. Treating member 0 as a central fit is incorrect.

## Conventions and validation

- The isoscalar charge average is
  \(\tfrac12(q_{\pi^-}+\bar q_{\pi^-})\), hence the pion component has equal
  \(u,d,\bar u,\bar d\). This equality belongs only to this isoscalar meson
  component and does not identify nucleon flavors.
- The correlator adapter is purely tensor polarized:
  \(f_{1LL}=-2\delta_T/3\) in the repository convention. Its unpolarized,
  vector-polarized, axial, and transverse-spin pieces are zero.
- `strength=0` is an exact zero-meson limit.
- The radial \(q=0\) limits reproduce the AV18 \(S/D\) norms, the
  \(\delta f_\pi/y\) sum rule is tested numerically, and doubled quadrature
  changes the HERMES-bin result by at most \(2.61\times10^{-8}\).
- `scripts/compare_b1_pion_exchange_to_hermes.py` propagates all replicas and
  the published \(M_A=1.03\pm0.04\) GeV form-factor variation. The diagnostic
  experimental-error-only six-bin HERMES chi-square changes from 21.34
  (impulse) to 7.55 (impulse plus pion). This is a diagnostic comparison,
  not a parameter fit.
- The first two HERMES bins lie below the JAM21 \(Q_{\min}=1.14\) GeV grid
  and are explicitly evaluated at that boundary.

## Explicit limitations and replacement tasks

The individual published \(F_m\) formulas also determine the collinear spin
average \(\bar f_\pi=(f_\pi^{(0)}+2f_\pi^{(1)})/3\). The implementation
evaluates both helicity projections independently and verifies that they
reconstruct the spin average and tensor difference. The printed
\(F_0^{ww}\) equation repeats \(I_{ww2}\) in its first term; the code reads
that term as \(I_{ww0}\), as required by the channel definition and by the
paper's immediately following tensor identity.

Before Fock normalization the connected spin average gives pion number
0.02129174 and deuteron plus-momentum fraction 0.00410205. Exact
\(Z=1+N_\pi\) normalization gives NN probability 0.979152, NNπ probability
0.020848, pion momentum 0.0040165, and NNπ-nucleon momentum 0.0168313; the
three momentum entries sum to one exactly.

The unchanged-shape closure is retained only as a named comparison
diagnostic.  The preferred collinear implementation is
`NNPiLongitudinalRecoilConvolution`.  Conditional on a pion with source
variable \(y\), it uses

\[
\eta_\pi=yM_N/M_D,\qquad
\alpha_N'=(1-\eta_\pi)\alpha_N ,
\]

and evaluates the baseline correlator at the correspondingly shifted
partonic fraction.  It acts on the complete quark correlator matrices, so
flavor and all implemented vector, axial, and transverse-spin structures
remain distinct.  Tests verify exact nucleon-number and plus-momentum
closure, a nontrivial change of the nucleon \(x\) shape, and preservation of
conditional spin ratios for a scalar pion.

The source-level unintegrated spin average
\(d\bar f_\pi/dq_T^2\) is also exposed.  The retained NN subsystem has the
transverse recoil kernel \(J_0(\alpha bq_T)\), independently of the
pion-internal kernel \(J_0(zbq_T)\); both reduce exactly at \(b=0\).
For the retained nucleon parent, the repository uses
\(x_D=x_N/2\).  If the active residual-NN nucleon carries fraction
\(\alpha\), its parton fraction is
\(z=x_D/[\alpha(1-\eta_\pi)]\), so the physical recoil phase is

\[
z\alpha bq_T=\frac{x_N\,bq_T}{2(1-\eta_\pi)}.
\]

The internal \(\alpha\) cancels exactly; this is not an average-\(\alpha\)
ansatz.  The complete-matrix `nucleon_correction_b` implementation transports
the vector, axial, and transverse projections and reduces to the collinear
conditional correction at \(b=0\).  On the actual AV18 24-by-16-by-12 LF
smearing grid at \(x_N=0.1,Q=5\) GeV, its maximum \(b=0\) residual against
the independently serialized collinear parent is \(2.91\times10^{-6}\).

The conditional convolution is now propagated through a production
24-by-16-by-12 AV18 light-front parent grid at \(Q=5\) GeV.  The serialized
grid contains 19 anchor and 18 refinement nodes for each of
\(u,d,\bar u,\bar d\), with proton, neutron, and total correlators stored
separately. It uses the exact \(b_T=0\) collinear LF contraction, not the
dimensionful momentum-space value at \(k_T=0\). Complete matrices are
interpolated by PCHIP in \(\ln x\);
linear-\(x\) interpolation was tested and rejected because it failed the
small-\(x\) refinement audit.  The refined conditional total is stable to
0.439% of each curve peak, while the small conditional-minus-minimal
correction is stable to 6.93% of its own peak (below 0.1% of the dominant
total scale).

In the declared exact-isospin CT18 baseline the inclusive deuteron total
correctly has \(u_D=d_D\) and \(\bar u_D=\bar d_D\).  This is not a flavor
collapse: the stored proton \(u-d\) and sea-flavor matrix distances are
28.78 and 16.00 in the table's units, with the neutron pieces separately
retained.  The project's MSHT20QED parent provides the replaceable
charge-symmetry-breaking extension.

All 786 JAM21 members are propagated through the refined conditional model.
Because the LHAPDF set labels every member as a replica, the production
central is their ensemble mean and the uncertainty is the sample standard
deviation; 16th and 84th percentiles and every member prediction are also
stored. A 160-node fixed Gauss propagation agrees with the adaptive member-0
convolution to \(1.21\times10^{-5}\) relative for \(f_1\) and
\(1.91\times10^{-5}\) for \(f_{1LL}\). The JAM21 uncertainty affects the
pion-supported \(f_1\) and \(f_{1LL}\); the conditional nucleon \(g_1,h_1\),
and \(h_{1LT}\) pieces are replica independent.

The source still does **not** determine a pion GTMD or the detailed NNπ
nucleon helicity amplitude, virtuality response, or off-forward spectral
shape. The separately documented Vpion19 boundary supplies a non-Gaussian
transverse scenario with nuclear recoil, but is not a joint refit.  A
three-body NNπ light-front amplitude must ultimately replace the current
conditional scalar-pion spin inheritance and complete the off-forward
transverse coupling.

Reproduce:

```text
PYTHONPATH=src python -m pytest -q tests/test_pion_exchange.py
PYTHONPATH=src python scripts/compare_b1_pion_exchange_to_hermes.py
PYTHONPATH=src python scripts/audit_spin_averaged_pion.py
PYTHONPATH=src python scripts/export_nnpi_collinear_parent_grid.py \
  --grid coarse --output outputs/parent_tmds/nnpi/av18_collinear_parent_coarse.csv
PYTHONPATH=src python scripts/export_nnpi_collinear_parent_grid.py \
  --grid refined \
  --reuse outputs/parent_tmds/nnpi/av18_collinear_parent_coarse.csv \
  --output outputs/parent_tmds/nnpi/av18_collinear_parent_refined.csv
PYTHONPATH=src python scripts/compare_nnpi_recoil_parent_models.py \
  --parent outputs/parent_tmds/nnpi/av18_collinear_parent_refined.csv \
  --output outputs/figures/pion/nnpi_recoil_av18_refined.csv
PYTHONPATH=src python scripts/validate_nnpi_xgrid_convergence.py \
  --coarse outputs/figures/pion/nnpi_recoil_av18_coarse.csv \
  --refined outputs/figures/pion/nnpi_recoil_av18_refined.csv \
  --output outputs/figures/pion/nnpi_recoil_av18_xgrid_convergence.json
PYTHONPATH=src python scripts/propagate_nnpi_jam21_replicas.py \
  --comparison outputs/figures/pion/nnpi_recoil_av18_refined.csv \
  --bands outputs/figures/pion/nnpi_recoil_av18_jam21_bands.csv \
  --members outputs/figures/pion/nnpi_recoil_av18_jam21_members.csv
PYTHONPATH=src python scripts/plot_nnpi_jam21_bands.py \
  --input outputs/figures/pion/nnpi_recoil_av18_jam21_bands.csv \
  --output outputs/figures/pion/nnpi_recoil_av18_jam21_bands.pdf
PYTHONPATH=src python scripts/export_nnpi_nucleon_bspace_recoil.py \
  --x-n 0.1 --scale 5 --b-max 5 --n-b 21 \
  --parent outputs/parent_tmds/nnpi/av18_collinear_parent_refined.csv \
  --output outputs/figures/pion/nnpi_nucleon_bspace_av18_x010.csv
```

Outputs are
`output/pdf/b1_ia_pion_vs_hermes.pdf`,
`outputs/figures/b1/b1_ia_pion_vs_hermes.csv`, all 786 replica predictions,
and a machine-readable validation report in the same output directory.
