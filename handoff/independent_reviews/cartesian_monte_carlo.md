# Independent Cartesian / quasi-Monte-Carlo review of the Norfolk OPE moment

Date: 2026-07-24

## Scope and independence

I independently evaluated the \(q\rightarrow0\) isoscalar N3LO OPE magnetic
moment for all four public Norfolk deuteron wave functions. I did not import
the project's current implementation, partial-wave coefficients, Norfolk
parser, or FFT benchmark. The review calculation is isolated in
`handoff/independent_reviews/cartesian_direct.py` and makes no production-code
changes.

The calculation reads the coordinate-space `u(r),w(r)` columns directly from
the four raw `fdeut.*` files. It constructs the two-nucleon Pauli matrices as
Kronecker products and generates the stretched \(J=1,M=1\) D wave from
SymPy's Clebsch--Gordan coefficients
\(\langle 2m_L,1m_S|11\rangle\) and SciPy spherical harmonics. Thus neither
the spin-angular wave function nor its reduced radial coefficients are copied
from the existing implementation.

## Operator derived from Eq. (2.12)

Writing Eq. (2.12) as

\[
 {\bf j}({\bf q})=-i\,e^{i{\bf q}\cdot{\bf r}_i}
 \boldsymbol{\mathcal O}\times {\bf q}/m_\pi+(i\leftrightarrow j),
\]

the phase does not contribute at \(q=0\), because the remaining current is
already linear in \({\bf q}\). Since
\(\nabla_q\times(\boldsymbol{\mathcal O}\times{\bf q})=
2\boldsymbol{\mathcal O}\), the magnetic operator in nuclear magnetons is

\[
 -{2m_N\over m_\pi}\,\tau_1\!\cdot\!\tau_2
 \left[
 I_1(r)(\sigma_{1z}+\sigma_{2z})+
 I_2(r)\hat r_z(\boldsymbol{\sigma}_1+\boldsymbol{\sigma}_2)
 \!\cdot\!\hat{\bf r}
 \right].
\]

I used \(\tau_1\cdot\tau_2=-3\), \(m_N=938.9\) MeV,
\(m_\pi=138.039\) MeV, \(g_A=1.29\), \(f_\pi=92.4\) MeV, the published
\(d_2^S\) values, and the printed long-range regulator with
\(R_L=1.2\) fm for models a and \(1.0\) fm for models b.

## Direct angular and radial integration

The full four-component spin wave function was evaluated at Sobol points
uniform in solid angle. At every direction the code applies the Cartesian
matrix operator to that spinor before taking the inner product. The solid-angle
integral is combined with a Simpson integral over all 10,000 tabulated radii
from 0.01 to 100 fm. The raw radial norms obtained independently are
0.99999805--0.99999813.

Although no reduced coefficients are assumed, the numerical angular integration
recovers the following bilinears in the \((u^2,uw,w^2)\) ordering:

\[
 (2.000000000,\,0,\,-1.000000000)
\]

for \(\sigma_{1z}+\sigma_{2z}\), and

\[
 (0.666666667,\,0.942809042,\,0.333333333)
\]

for
\(\hat r_z(\boldsymbol{\sigma}_1+\boldsymbol{\sigma}_2)\cdot\hat{\bf r}\).
The middle tensor number is \(2\sqrt2/3\). This independently reproduces the
analytic coefficients found previously.

## Results and convergence

| Sobol points | Ia (n.m.) | Ib (n.m.) | IIa (n.m.) | IIb (n.m.) |
|---:|---:|---:|---:|---:|
| 1,024 | -0.0402121270 | -0.0209921443 | -0.0294398771 | -0.0718748061 |
| 4,096 | -0.0402121270 | -0.0209921443 | -0.0294398771 | -0.0718748061 |
| 16,384 | -0.0402121270 | -0.0209921443 | -0.0294398771 | -0.0718748061 |
| 65,536 | -0.0402121270 | -0.0209921443 | -0.0294398771 | -0.0718748061 |
| 262,144 | -0.0402121270 | -0.0209921443 | -0.0294398771 | -0.0718748061 |

The unusually rapid angular convergence is expected: the integrands are
low-order spherical polynomials, which the balanced Sobol nets integrate very
efficiently. The last displayed digit is stable over the complete sequence.

The earlier production calculation gave, respectively,
`-0.04021212699`, `-0.02099214435`, `-0.02943987708`, and
`-0.07187480608` n.m. The independent calculation agrees to the displayed
precision.

For comparison, the 2019 Table III values are
\(+0.0042,-0.0065,+0.0026,-0.0260\) n.m. The independent calculation therefore
does **not** reproduce Table III.

## Assessment

This review confirms that the unexpected result is not caused by the existing
code's partial-wave reduction, Clebsch--Gordan table, angular quadrature,
Norfolk parser, or FFT normalization. Starting from the printed Eq. (2.12),
the printed regulator and constants, and the public coordinate wave functions,
a direct Cartesian spin calculation gives the same four negative moments.

The discrepancy must therefore lie upstream of these numerical steps. The
remaining plausible categories are:

1. the LEC values associated with the published table are not the values
   actually used for that table;
2. the operator/current convention used numerically differs from printed
   Eq. (2.12), including a possible unreported regulator or LEC mapping;
3. Table III or its labels contain values from a different calculation
   revision.

Changing a global sign or normalization cannot solve the issue because Table
III changes sign between model classes while the independently calculated
radial matrix element has the same sign for all four. This supports retaining
the OPE term as unvalidated until corrected inputs or an independently
published benchmark are available.
