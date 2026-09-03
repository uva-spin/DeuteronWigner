# Quark axial tensor T-odd boundary: \(g_{1LT}\) and \(g_{1TT}\)

## Status and operator content

The leading-twist spin-1 quark basis in arXiv:1612.06585 permits two
chiral-even T-odd axial tensor structures:

- \(g_{1LT}\), target-LT and transverse rank one;
- \(g_{1TT}\), target-TT and transverse rank two.

Their zeros in the real one-body parent were component limits, not QCD
predictions. Both enter the `gamma+gamma5` projection. A nonzero result
therefore requires an absorptive gauge-link amplitude correlated with the
spin-1 tensor density; copying the vector Sivers input is not allowed.

## Stage 1: independent axial phases

`AxialTensorTOddScenario` supplies independent coefficients for
\(u,d,\bar u,\bar d\) and for the two operators. Low, central, and high
members multiply the flavor-resolved AV18 parent \(f_1\) profile. The two
coefficients share no Sivers or Boer--Mulders phase.

At every \(k_T\), both corrections are composed into the full retained-spin
\(6\times6\) target–quark density. If the proposed pair would violate
positivity, one common bisection scale preserves their model ratio and moves
the pair inside the positive domain. No individual eigenvalue is clipped.

This stage is a conservative model envelope, not a fit.

## Stage 2: screened one-gluon rescattering

`EikonalAxialTensorModel` evaluates the transverse convolution

\[
 {\cal I}_n(k_T)=\frac{C_F\alpha_s}{2\pi}
 \int_0^{q_{\max}}\!q\,dq\,
 \frac{\left[\Lambda^2/(\Lambda^2+q^2)\right]^2}
      {q^2+\mu_g^2}
 \left(\frac{q}{M_D}\right)^n
 \left\langle\cos(n\phi)
 e^{-|\boldsymbol{k}-\boldsymbol q|^2/(2w)}\right\rangle_\phi ,
\]

for \(n=1,2\). The screened propagator is an infrared-regulated model of the
soft gluon exchanged with the remnant; the dipole factor controls unresolved
ultraviolet structure. One-gluon and eikonal final-state interactions as a
source of naive-T-odd light-front interference are established model
mechanisms; see arXiv:1012.3395, hep-ph/0406171, and arXiv:2204.06854.

The rank-one moment produces an imaginary S–P interference for \(g_{1LT}\).
The rank-two result contains imaginary S–D and P-even–P-odd terms for
\(g_{1TT}\). Nuclear tensor factors use the AV18 values

- \(P_D=0.0575985407\);
- normalized signed S–D radial overlap \(C_{SD}=0.3897991321\).

The kernel scenarios vary \(\alpha_s\), screening mass, and dipole scale
together. They are alternative model members, not a statistical covariance.

## Exact constraints and validation

- Future/past simple staples reverse both functions exactly.
- Mixed links fail closed.
- Disabling the imaginary P-odd amplitude makes both functions vanish.
- The rank-one/rank-two harmonics vanish from the correlator at the origin;
  production starts at resolved nonzero \(k_T\), rather than plotting an
  arbitrary origin coefficient.
- Hermiticity and the full target–quark density positivity are tested.
- The 48×56 versus 72×88 eikonal quadratures agree within the recorded
  tolerance in
  `outputs/validation/axial_tensor_eikonal_convergence.json`.

## Production

- Full projections:
  `outputs/parent_tmds/quark_axial_tensor_todd_stages.csv`
- Retained-helicity correlators:
  `outputs/parent_tmds/quark_axial_tensor_todd_stages.correlators.csv`
- Five-page dimensional-\(F\) atlas:
  `output/pdf/quark_g1lt_g1tt_two_stage_atlas.pdf`

The direct phase scenario is much larger than the screened one-gluon result.
This hierarchy is a model result and is displayed explicitly; the
rescattering curve is not inflated to match the phenomenological envelope.
