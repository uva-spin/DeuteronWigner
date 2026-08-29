# CJ26 off-shell input

Production uses the cubic, flavor-independent leading-twist off-shell
function released with CJ26 v1:

\[
\delta f(x)=a_{\rm off}^{0}+a_{\rm off}^{1}x+
             a_{\rm off}^{2}x^2+a_{\rm off}^{3}x^3 .
\]

Primary source: Accardi et al., *CJ26 Global QCD Analysis with Large-x
Jefferson Lab 6 and 12 GeV Data*, arXiv:2605.31424v1, Eq. (14) and the
source-package parameter tables. The archived paper is
`references/arxiv_2605.31424_cj26.pdf`.

| Higher-twist treatment | a0 | a1 | a2 | a3 |
|---|---:|---:|---:|---:|
| additive | -0.474(90) | 3.9(1.3) | -15.1(5.2) | 16.2(5.6) |
| multiplicative | -0.408(88) | 5.2(1.1) | -20.6(4.4) | 20.5(4.4) |

The production central value is the pointwise midpoint of these two
higher-twist treatments. Its uncertainty combines in quadrature:

1. the larger scenario's diagonal propagation of the published marginal
   coefficient errors; and
2. the additive/multiplicative central-value half-range.

This is not a full statistical covariance because CJ26 v1 does not publish
the off-shell coefficient covariance matrix or Hessian members separately
from the fit products. The limitation is explicit in metadata and WP8.

CJ26 states that data constrain the shape through approximately `x <= 0.7`;
the behavior above `x ~= 0.75` is parametrization-driven extrapolation. The
adapter records `constrained_x_max=0.7`. It is used flavor-independently, as
in the fit, and currently multiplies every quark spin projection equally.
That latter extension from inclusive unpolarized DIS to polarized TMD
correlators remains model dependent and must be varied or replaced when
spin-dependent off-shell information becomes available.

At each nuclear LF node, the implementation evaluates

\[
F_N^*(z,k_T,Q;v)=F_N(z,k_T,Q)\,[1+v\,\delta f(z)]
\]

with the node's invariant virtuality. It therefore follows the fitted
partonic argument `z=x_D/y`, not the external `x_N`, and does not use an
average-virtuality rescaling.
