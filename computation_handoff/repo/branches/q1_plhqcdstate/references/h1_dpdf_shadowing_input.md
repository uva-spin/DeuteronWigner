# H1 DPDF / FGS deuteron shadowing input

## Implemented source and convention

Production quark shadowing uses the official H1 2007 Jets DPDF v1.0
parameterization (04/06/2009), cited as H1 Collaboration,
JHEP 0710 (2007) 042, arXiv:0708.3217. The vendored release contains the
Pomeron singlet and gluon grids in the published \(z f_{i/\mathbb P}(z,Q^2)\)
convention and the H1 Pomeron flux normalized by
\(x_{\mathbb P} f_{\mathbb P/p}(x_{\mathbb P}=0.003)=1\), integrated over
\(-1<t<t_{\min}\).

The nuclear calculation implements the deuteron double-scattering expression
of Frankfurt, Guzey, and Strikman, arXiv:hep-ph/0601123, Eq. (4). It includes:

- H1 bilinear interpolation in \(\log z,\log Q^2\), including its official
  boundary-clamping convention;
- the differential H1 flux reconstructed before its \(t\) integration;
- the \(16\pi\) HERA-diffraction to forward-rescattering conversion;
- \(2(1-\eta^2)/(1+\eta^2)\), with
  \(\eta=\pi[\alpha_{\mathbb P}(0)-1]/2\);
- \(x_{\mathbb P,\max}=0.1\) for quarks and 0.03 for gluons;
- the wave-function-specific normalized LF body form factor evaluated at
  the FGS argument \(4[q_T^2+(x_{\mathbb P}m_N)^2]\).

The H1 light-flavor singlet is shared equally among
\(u,\bar u,d,\bar d,s,\bar s\), as in the fit. Flavor-dependent nuclear
fractions still arise from division by the corresponding CT18 proton-plus-
neutron inclusive density.

## Uncertainty and limitations

Named members vary the DPDF normalization by \(\pm20\%\), following the FGS
assessment of the diffractive input, and the quark \(t\)-slope by
\(\pm1.1\ {\rm GeV}^{-2}\). Each slope member is renormalized to the H1 flux
condition, so it is a shape variation rather than a hidden normalization
variation. These members are physics scenarios, not an H1 Hessian
reconstruction. The public v1.0 files used here do not contain eigenvector
grids. Gluon-specific slope scenarios and polarized/tensor diffractive PDFs
remain model-dependent requirements.

The official NLO singlet grid has signed values at its extreme small-\(z\),
low-\(Q^2\) boundary. They are retained rather than clipped. The final
physical shadowing fraction must be finite and nonnegative.

At \(x=10^{-2},Q=5\) GeV, the AV18/CT18 u-quark calculation gives a 1.54%
central suppression, independently recovering the established deuteron
benchmark. The production slice is \(x_N=0.1\), where the coherent term
vanishes by the declared quark \(x_{\mathbb P}\) cutoff, but the integrated
shadowing loss still fixes the antishadowing normalization.

## Vendored artifacts

Source directory: `data/raw/h1_2007_dpdf/`

- `readme_h12007.txt`: `ab983d6295c8bb17aa4569b748b9028af5a7f045c256588b6a2175e1b004ba6c`
- `h12007jetsdpdf_prcoeff.f`: `1a11d4d5affa161200b61e68582fa580ab4e72b8df3716a304891d3ecb24a864`
- `h12007jetsdpdf_singlet.f`: `3bab5894f4cca158e61f2de81f4fb54a6b2325d578f065541c66eec144548469`
- `h12007jetsdpdf_gluon.f`: `c7f9f9ee35c315c53db4a7fcb1328d2231990f50f733d03689e9d60267d5d7ba`
- `h12007jetsdpdf_singlet.data`: `becaa12df40c468a32347ecde398c07320d458cc5892de52c7b451864188bbf1`
- `h12007jetsdpdf_gluon.data`: `aa46f7806264c411f6966bb99ac0f885ed2f998cbea377c44beac519c48a19c7`

Primary implementation: `src/deuteron_wigner/diffractive_shadowing.py`.
Validation: `tests/test_diffractive_shadowing.py`.
