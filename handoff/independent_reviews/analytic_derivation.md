# Independent analytic review: Norfolk N3LO isoscalar OPE magnetic moment

Date: 2026-07-24

Scope: independent derivation and direct radial evaluation of the deuteron
magnetic-moment contribution from Eqs. (2.12), (2.19), and (2.22) of
Schiavilla et al., Phys. Rev. C 99, 034005 (2019). This review did not use the
production angular-integration implementation.

## 1. Operator and zero-momentum limit

For nucleons 1 and 2, Eq. (2.12) is

\[
 {\bf j}_{\rm OPE}({\bf q}) =
 -i e^{i{\bf q}\cdot{\bf r}_1}\,
 {\boldsymbol\tau}_1\!\cdot{\boldsymbol\tau}_2
 \left[I_1(r){\boldsymbol\sigma}_2+
 I_2(r)({\boldsymbol\sigma}_2\!\cdot\widehat{\bf r})\widehat{\bf r}\right]
 \times {{\bf q}\over m_\pi} +(1\leftrightarrow2).
\]

For \({\bf q}=q\widehat{\bf x}\), \(({\bf A}\times{\bf q})_y=A_zq\).
Equation (3.5), \(F_M=-i(2m/q)\langle j_y\rangle\), therefore gives

\[
 \mu_{\rm OPE}=-{2m\over m_\pi}
 \left\langle {\boldsymbol\tau}_1\!\cdot{\boldsymbol\tau}_2
 \left[
 I_1(\sigma_{1z}+\sigma_{2z})+
 I_2\{({\boldsymbol\sigma}_1+{\boldsymbol\sigma}_2)
 \!\cdot\widehat{\bf r}\}\widehat r_z
 \right]\right\rangle .
\]

The phase factors do not contribute in this limit because their first
derivatives multiply the explicit factor of \(q\). The same result follows
from \(\boldsymbol\mu=-(i/2)\boldsymbol\nabla_q\times{\bf j}|_{q=0}\),
using \(\boldsymbol\nabla_q\times({\bf A}\times{\bf q})=2{\bf A}\), and
then converting to nuclear magnetons by multiplying by \(2m\).

For the deuteron \(T=0\),
\(\langle{\boldsymbol\tau}_1\cdot{\boldsymbol\tau}_2\rangle=-3\).
The exchange term changes \(\sigma_2\) to \(\sigma_1\); reversing
\(\widehat{\bf r}\) in the exchanged tensor term produces two minus signs,
so the tensor structure is unchanged. Consequently the complete conversion
factor multiplying the spin-angular radial integral is \(+6m/m_\pi\).

## 2. Independent partial-wave reduction

The standard stretched deuteron wave function is

\[
 \Psi_{11}={1\over r}\left[u(r){\cal Y}^{11}_{011}
 +w(r){\cal Y}^{11}_{211}\right],
\]

with

\[
 {\cal Y}^{11}_{211}={1\over\sqrt{10}}Y_{20}\chi_{11}
 -\sqrt{3\over10}Y_{21}\chi_{10}
 +\sqrt{3\over5}Y_{22}\chi_{1,-1}.
\]

Direct Clebsch--Gordan summation and spherical-harmonic integration give

\[
\begin{aligned}
\int d\Omega\,\Psi^\dagger(\sigma_{1z}+\sigma_{2z})\Psi\,r^2
 &=2u^2-w^2,\\
\int d\Omega\,\Psi^\dagger
 [({\boldsymbol\sigma}_1+{\boldsymbol\sigma}_2)\cdot\widehat{\bf r}]
 \widehat r_z\Psi\,r^2
 &={2\over3}u^2+{2\sqrt2\over3}uw+{1\over3}w^2.
\end{aligned}
\]

Thus the first-principles radial expression is

\[
\boxed{\displaystyle
\mu_{\rm OPE}={6m\over m_\pi}\int_0^\infty dr\,
\left[
I_1(r)(2u^2-w^2)+
I_2(r)\left({2\over3}u^2+{2\sqrt2\over3}uw+{1\over3}w^2\right)
\right].}
\]

This derivation includes both ordered nucleon terms exactly once.

## 3. Correlation functions and regulator

With \(d'_9=d_2^S/m_\pi^2\), Eqs. (2.10), (2.11), and (2.19) give

\[
\begin{aligned}
I_1(r)&=K\,C_{R_L}(r)
 \left[-{(1+\mu)e^{-\mu}\over\mu^3}\right],\\
I_2(r)&=K\,C_{R_L}(r)
 { (3+3\mu+\mu^2)e^{-\mu}\over\mu^3},\\
K&={g_A\over16\pi}{m_\pi^2\over f_\pi^2}d_2^S,\qquad
\mu=m_\pi r ,
\end{aligned}
\]

where

\[
C_{R_L}(r)=1-\left[(r/R_L)^6e^{(r-R_L)/(R_L/2)}+1\right]^{-1}.
\]

The numerical constants were exactly those specified in the paper:
\(g_A=1.29\), \(f_\pi=92.4\) MeV, \(m_\pi=138.039\) MeV, and
\(m=938.9\) MeV. MeV were converted to inverse fm with
\(\hbar c=197.3269804\) MeV fm. The dimensionless ratios in \(K\) make the
choice of MeV versus inverse fm immaterial, provided it is consistent.

## 4. Direct evaluation of the public tables

The raw `fdeut.nv*` coordinate tables were parsed directly. No project
angular routines or interpolators were used. Simpson integration on their
native 0.005 fm mesh gives:

| model | table norm | \(I_1\) piece (n.m.) | \(I_2\) piece (n.m.) | sum (n.m.) | 2019 Table III |
|---|---:|---:|---:|---:|---:|
| Ia | 0.99999802 | +0.04640307 | -0.08661519 | -0.04021213 | +0.0042 |
| Ib | 0.99999805 | +0.02366418 | -0.04465633 | -0.02099214 | -0.0065 |
| IIa | 0.99999807 | +0.03417829 | -0.06361817 | -0.02943988 | +0.0026 |
| IIb | 0.99999812 | +0.08426663 | -0.15614144 | -0.07187481 | -0.0260 |

Inputs were \(d_2^S=(-0.06571,-0.02384,-0.04714,-0.07947)\) and
\(R_L=(1.2,1.0,1.2,1.0)\) fm for Ia, Ib, IIa, and IIb, respectively.

## 5. Convention audit

- **D-wave phase:** the positive relative \(S\)-\(D\) phase in the public
  tables is independently fixed by their quadrupole moments. The standard
  formula
  \[
  Q_d={1\over20}\int dr\,r^2w(\sqrt8u-w)
  \]
  gives 0.267585 fm2 for Ia, matching the header value 0.267588. Reversing
  the phase gives -0.300960 fm2. A hidden D-wave sign is therefore excluded.
- **Spin normalization:** Pauli matrices are required by Eq. (2.12).
  Replacing them by spin operators would introduce an erroneous factor 1/2.
  The stretched pure-S limit correctly gives
  \(\langle\sigma_{1z}+\sigma_{2z}\rangle=2\).
- **Isospin:** the normalized \(T=0\) state gives
  \(\tau_1\cdot\tau_2=-3\), not -3/4 (the latter would correspond to
  using isospin generators instead of the Pauli matrices printed in the
  current).
- **Exchange counting:** Eq. (2.12) contains two ordered terms. Their sum is
  the displayed \(\sigma_1+\sigma_2\); no additional pair factor is present.
- **Magnetic conversion and sign:** direct use of Eq. (3.5) gives
  \(-2m/m_\pi\) before the \(T=0\) isospin matrix element. This agrees with
  the curl definition and fixes both the sign and factor of two.
- **Fourier factors:** Eq. (2.12) is already a coordinate-space operator.
  With coordinate radial functions normalized as
  \(\int dr(u^2+w^2)=1\), no \((2\pi)^3\), \(r^2\), or \(\hbar c\) factor
  remains. The dimensions are also self-consistent.
- **Regulator:** Eq. (2.22) explicitly multiplies the already-derived
  \(I_1,I_2\) functions by \(C_{R_L}\). Differentiating the regulated Yukawa
  function instead is a different operator and is not the printed
  prescription.
- **Nucleon form factors:** any phenomenological dressing equals unity at
  \(q=0\), so it cannot affect this magnetic-moment benchmark.

## 6. Conclusion

An independent derivation from the printed equations reproduces the existing
project values, not Table III. The disagreement is not an unexpected result
of numerical angular integration: it is already present in the closed radial
formula above. In particular, the printed operator and LECs predict negative
contributions for all four models, while Table III reports positive values
for both `a` models.

The public wave functions are not the cause: they have the expected
normalization, their S--D phase reproduces the tabulated quadrupole moment,
and the paper states explicitly that the two-body Ia*/Ib*/IIa*/IIb*
Hamiltonians equal Ia/Ib/IIa/IIb. The remaining logical possibilities are
an unreported difference in the current/LECs used for the Monte Carlo
calculation, or an error in the published equation/LEC/table combination.
No scientifically defensible common normalization or phase adjustment maps
the first-principles result to the four published numbers.
