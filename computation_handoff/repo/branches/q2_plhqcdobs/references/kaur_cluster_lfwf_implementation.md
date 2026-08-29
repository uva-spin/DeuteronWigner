# Effective two-cluster light-front implementation

## Scientific classification

`hidden_color_cluster_lfwf.py` reproduces the effective two-cluster model of
Kaur, Mondal, Zhao, and Ji, Phys. Rev. D 113, 054008 (2026),
arXiv:2507.09886. It is a deep-binding non-nucleonic sensitivity scenario.
It is **not** a probability for hidden color: the source explicitly does not
resolve singlet-singlet and octet-octet components.

## Implemented parent machinery

1. The equal-mass principal-value 't Hooft longitudinal Hamiltonian is
   discretized on Gauss-Legendre nodes. Multiplication by square roots of the
   quadrature weights produces an explicitly real-symmetric eigenproblem.
2. The ground state is normalized as
   \(\int_0^1 dz\,|\chi(z)|^2=1\), is positive, and is exchange symmetric.
3. The \(n=L=0,\ J=1\) holographic transverse state is transformed to
   momentum space and normalized with
   \(\int dz\,d^2k_\perp/(16\pi^3)|\Psi|^2=1\).
4. Lepage-Brodsky light-front spinors, rest-frame spin-1 polarization
   vectors, and the source vertex
   \[
   {\bar v(1-z,-k_\perp)\over\sqrt{1-z}}\,
   \gamma\!\cdot\!\epsilon^{\Lambda *}\,
   {u(z,k_\perp)\over\sqrt z}\,\Psi
   \]
   generate the helicity amplitudes. The complex conjugate is required for
   the incoming polarization ket and reproduces the source helicity sign.
5. Longitudinal and transverse states are normalized independently.
   Number-density projections then produce \(f_1\), \(g_{1L}\), and
   \(f_{1LL}\) from the same helicity amplitudes.
6. `EffectiveClusterCollinearConvolution` implements the source's
   proton-plus-neutron convolution through replaceable unpolarized and
   polarized PDF providers. Quark and antiquark flavors remain separate.
   The physical LO hard prefactors are \(F_2=x\sum e_q^2q\) and
   \(g_1,b_1=\frac12\sum e_q^2(\Delta q,\delta_Tq)\).

The separate canonical-triplet plus unitary-Melosh implementation is retained
only as a limiting diagnostic. It preserves equal pointwise total density for
all target helicities and therefore has exactly zero \(f_{1LL}\); it must not
replace the vector-current construction.

## Validation evidence

- Clifford algebra and on-shell Dirac equations pass at machine precision.
- Spin-1 polarization vectors are orthonormal in the Minkowski metric.
- Helicity-summed densities are azimuthally covariant and transverse
  helicities obey parity.
- The central model gives \(M=1.87457545\) GeV.
- \(\int_0^1 dz\,f_1(z)=1\) and
  \(\int_0^1 dz\,f_{1LL}(z)=0\) within numerical tolerance.
- Local \(f_{1LL}(z,k_\perp)\) is nonzero.
- The three vector paths were extracted directly from the official
  `pdfs.pdf`, not raster-digitized. On \(0.05\le z\le0.90\), maximum absolute
  residuals are 0.01199 for \(z f_1\), 0.01163 for \(z g_{1L}\), and 0.00165
  for \(z f_{1LL}\).
- With NNPDF3.1 member 0 as the source-specified cluster PDF,
  \(\int_{0.02}^{0.85}dx\,b_1=0.003615\), reproducing the paper's
  \(0.0036\pm0.0003\). Omitting the standard tensor factor \(1/2\) gives
  exactly twice this value and is rejected by a dedicated convention test.

The proton and neutron providers remain distinct. Exact charge symmetry
makes the **isoscalar cluster scenario's** final \(u=d\) and
\(\bar u=\bar d\) averages where the inputs are exchanged partners. This is
a controlled consequence of the explicit \((p+n)/2\) source convolution,
not an identification of proton \(u,d\) or sea flavors. The provider
interface permits CSB or non-isoscalar cluster inputs without architectural
changes.

Reproduce with:

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q \
  tests/test_hidden_color_cluster_lfwf.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/compare_kaur_cluster_lmdfs.py
LHAPDF_DATA_PATH=data/raw/lhapdf PYTHONPATH=src \
  /Users/dustin/miniforge3/bin/python3.9 \
  scripts/compare_kaur_cluster_b1_to_hermes.py
```

The source-vector extractor is:

```bash
/Users/dustin/miniforge3/bin/python3.9 \
  scripts/extract_kaur_cluster_lmdf_benchmark.py /path/to/pdfs.pdf
```

## Uncertainty and production boundary

The comparison output varies \(m_{\mathcal C}=0.838\pm0.083\) GeV,
\(\kappa=0.130\pm0.013\) GeV, and \(g=0.50\pm0.05\) GeV one at a time.
The envelope is a parameter-sensitivity band, not a confidence interval,
because the fit covariance is not published.

The source provides cluster momentum distributions but does not fix a
flavor-resolved cluster PDF/TMD, color decomposition, QCD evolution,
finite-size cluster structure, higher orbital components, or physical
deuteron binding. Consequently this scenario may be compared separately
with the impulse, pion, and Miller six-quark scenarios, but it remains gated
out of the production flavor-resolved deuteron correlator until an explicit
cluster parton input and matching/evolution prescription are supplied.

Outputs:

- `data/benchmarks/kaur_2026_cluster_lmdf.csv`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_lmdf_model.csv`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_lmdf_comparison.pdf`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_lmdf_comparison.png`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_lmdf.validation.json`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_b1_vs_hermes.csv`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_b1_vs_hermes.pdf`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_b1_vs_hermes.png`
- `outputs/figures/hidden_color_cluster/kaur_2026_cluster_b1_vs_hermes.validation.json`
