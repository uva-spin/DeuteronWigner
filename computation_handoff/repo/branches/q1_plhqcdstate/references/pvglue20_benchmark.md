# PVGlue20 external benchmark boundary

Source acquired: 2026-07-26

Purpose: independent validation of the project's own nucleon light-front
gluon model. This source is not the canonical model and its fitted
normalization is not imported into project predictions.

## Authoritative sources

- Bacchetta, Celiberto, Radici, T-even gluon spectator model:
  arXiv:2005.02288.
- Bacchetta, Celiberto, Radici, T-odd one-gluon extension:
  arXiv:2402.17556.
- Official source endpoint:
  `https://export.arxiv.org/e-print/2005.02288`.

The downloaded official source archive had size 5,594,714 bytes and SHA-256
`24c377ee372d8ff0f44b222e2d57085c61b11e0d8d4af79f12e135e69f7cc3f0`.
It is not vendored because the project needs only reproducible equations and
benchmark conditions; the URL and extraction procedure are recorded here.

## Spectral benchmark

The source defines

\[
\rho_X(M_X)=\mu^{2a}\left[
 \frac{A}{B+\mu^{2b}}+
 \frac{C}{\pi\sigma}\exp\left(-\frac{(M_X-D)^2}{\sigma^2}\right)
\right],\qquad \mu^2=M_X^2-M^2,
\]

and

\[
F^g(x,k_T^2)=\int_M^\infty dM_X\,\rho_X(M_X)
\widehat F^g(x,k_T^2;M_X).
\]

Representative replica 11:

- \(A=6.0\), \(B=2.1\), \(a=0.78\), \(b=1.38\);
- \(C=346\), \(D=0.548\) GeV, \(\sigma=0.50\) GeV;
- \(\Lambda_X=0.448\) GeV;
- \(\kappa_1=1.46\) GeV2, \(\kappa_2=0.414\) GeV2.

The fit scale is \(Q_0=1.64\) GeV and the fitted range is
\(10^{-3}<x<0.7\). The 100 replicas are not in the arXiv source and are
available only from the authors according to the paper.

## Required qualitative tests of our model

1. A minimal Dirac-like vertex permits nonzero gluon Sivers and \(h_1^g\).
2. The Pauli/spin-orbit vertex activates \(h_{1L}^{\perp g}\) and
   \(h_{1T}^{\perp g}\); both vanish in the minimal-vertex limit.
3. Future/past links reverse every T-odd function.
4. f-type and d-type functions are independent in general. The published
   \(5/9\) relation is only the equal-vertex model boundary.
5. The full model has a node in \(h_{1L}^{\perp g}\) near
   \(k_T^2\simeq0.1\) GeV2 at \(x=0.1\); this is a useful benchmark, not an
   exact constraint on our LF amplitudes.
6. \(h_{1T}^{\perp g}\) is strongly suppressed relative to the rank-one
   functions in that model.

These checks constrain mechanism and hierarchy. They do not license copying
the PVGlue20 fit normalization, spectral parameters, or uncertainty band
into the canonical deuteron calculation.
