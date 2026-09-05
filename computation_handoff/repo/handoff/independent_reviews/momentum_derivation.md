# Independent review: momentum-space N3LO isoscalar OPE moment

Date: 2026-07-24

Scope: independent derivation and numerical evaluation of the deuteron
magnetic-moment contribution from the N3LO isoscalar one-pion-exchange
current.  This review did not import the project's current or wave-function
modules and made no changes to production code.

## Starting current and kinematics

The momentum-space current in Eq. (3) of Kölling, Epelbaum, and Phillips is

\[
 {\bf j}_{12} =
 {2 i e g_A d'_9\over f_\pi^2}\,
 {\boldsymbol\tau}_1\mathbin{\cdot}{\boldsymbol\tau}_2
 {\boldsymbol\sigma}_2\mathbin{\cdot}{\bf q}_2\over
 q_2^2+m_\pi^2}
 ({\bf q}_1\times{\bf q}) +(1\leftrightarrow2).
\]

For a photon along \(x\), take the zero-transfer limit only after retaining
both diagrams.  At \(q=0\), \({\bf q}_1={\bf k}\) and
\({\bf q}_2=-{\bf k}\), so the coefficient of \(q_x\) in \(j_y\) is
proportional to

\[
 -{[(\boldsymbol\sigma_1+\boldsymbol\sigma_2)\cdot{\bf k}]k_z
 \over k^2+m_\pi^2}.
\]

Using

\[
 \mu_d=-i{2m_N\over q}\langle j_y(q\hat{\bf x})\rangle,\qquad
 \langle T=0|\boldsymbol\tau_1\cdot\boldsymbol\tau_2|T=0\rangle=-3,
\]

shows that the exchanged diagram is already responsible for replacing the
single spin by \(\boldsymbol\sigma_1+\boldsymbol\sigma_2\).  There is no
additional pair factor.  In the conventions of Schiavilla et al. the final
conversion multiplying the dimensionless coordinate operator is
\(6m_N/m_\pi\).

## Fourier transform and local regulator

With

\[
 \int {d^3k\over(2\pi)^3}{e^{i{\bf k}\cdot{\bf r}}\over k^2+m_\pi^2}
 ={e^{-m_\pi r}\over4\pi r},
\]

the \(k_a k_b\) numerator becomes a Hessian of the Yukawa function.  This
gives Eq. (2.12) and its two radial functions

\[
 I_1=K C_{R_L}(r)\left[-{(1+\mu)e^{-\mu}\over\mu^3}\right],
 \quad
 I_2=K C_{R_L}(r)
 { (3+3\mu+\mu^2)e^{-\mu}\over\mu^3},
\]

\[
 K={g_A\over16\pi}{m_\pi^2\over f_\pi^2}d_2^S,\qquad
 \mu=m_\pi r,
\]

where \(d'_9=d_2^S/m_\pi^2\).  I used the regulator exactly as prescribed
in Eqs. (2.22)-(2.23): it multiplies the already transformed correlation
functions.

The genuinely momentum-space representation of this *locally regulated*
operator is not the bare pion propagator times a scalar cutoff.  Defining

\[
 O_{ab}({\bf r})=I_1(r)\delta_{ab}+I_2(r)\hat r_a\hat r_b ,
\]

its momentum-transfer kernel is

\[
 \widetilde O_{ab}({\bf p})=4\pi\int dr\,r^2\left\{
 I_1j_0(pr)\delta_{ab}
I_2\left[{j_0(pr)+j_2(pr)\over3}\delta_{ab}
-j_2(pr)\hat p_a\hat p_b\right]\right\}.
\]

Thus the momentum-space matrix element is a convolution of this tensor
kernel with initial and final wave functions.  A Cartesian discrete
convolution (implemented by FFT) gives the same numbers as the direct
coordinate integral to \(9\times10^{-14}\) n.m. on the existing \(96^3\)
benchmark grid.  This is Parseval/Fourier equivalence, but the tensor-kernel
derivation above independently fixes what must be transformed and rules out
a scalar-regulator shortcut.

## Independent partial-wave reduction

Direct spin-angular algebra for the stretched deuteron gives

\[
 \langle \Sigma_z\rangle_r=2u^2-w^2,
\]

\[
 \langle(\boldsymbol\Sigma\cdot\hat{\bf r})\hat r_z\rangle_r
 ={1\over3}\left(2u^2+2\sqrt2\,uw+w^2\right).
\]

Consequently,

\[
 \mu_{\rm OPE}={6m_N\over m_\pi}\int_0^\infty dr\left[
 I_1(2u^2-w^2)+{I_2\over3}
 (2u^2+2\sqrt2\,uw+w^2)\right].
\]

I evaluated this expression with a fresh parser over the 10,000
coordinate-space rows in each public Norfolk file and SciPy Simpson
quadrature.  The raw norms were \(0.99999805\)--\(0.99999813\).  Inputs were
\(g_A=1.29\), \(f_\pi=92.4\) MeV, \(m_\pi=138.039\) MeV,
\(\hbar c=197.3269804\) MeV fm, \(m_N=938.9\) MeV; \(R_L=1.2\) fm for
models a and \(1.0\) fm for models b; and the 2019 Table-I \(d_2^S\) values.

| Model | \(I_1\) part (n.m.) | \(I_2\) part (n.m.) | Sum (n.m.) | 2019 Table III |
|---|---:|---:|---:|---:|
| NV2-Ia | +0.04640307 | -0.08661519 | -0.04021213 | +0.0042 |
| NV2-Ib | +0.02366418 | -0.04465633 | -0.02099214 | -0.0065 |
| NV2-IIa | +0.03417829 | -0.06361817 | -0.02943988 | +0.0026 |
| NV2-IIb | +0.08426663 | -0.15614144 | -0.07187481 | -0.0260 |

## Conclusions

1. A derivation beginning with the momentum-space current reproduces the
   printed coordinate operator, including the exchange, isospin, magnetic
   conversion, Fourier normalization, and units.
2. Independent raw-table quadrature reproduces the project's reported
   results to the shown digits.
3. The Fourier-space tensor kernel and Cartesian convolution reproduce the
   same result, so moving between coordinate and momentum space does not
   resolve the discrepancy.
4. With the 2019 printed equations, regulator prescription, public Norfolk
   wave functions, and Table-I LECs, all four OPE sums are negative.  They
   cannot reproduce the Table-III a/b sign pattern.
5. The disagreement is therefore not evidence that the first-principles
   contraction is impossible.  It is evidence that the published numerical
   table used at least one input or mapping not represented by that printed
   set.  This is consistent with the later disclosure that the 2019
   contact-basis mapping and fitted LEC tables required correction.

The strongest next independent check would start from an independently
implemented spin-coupled momentum-space Norfolk wave function and evaluate
the six-dimensional convolution with \(\widetilde O_{ab}\) by deterministic
quadrature, rather than FFT.  It should reproduce the values above; if it
does not, its discrepancy can be localized to wave-function Fourier phases
or convolution normalization.
