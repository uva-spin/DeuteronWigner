# C403: C117 `I2_density_projector` Finite-Axis and Spatial-Kernel Numerical Primitive

**Project:** DeuteronWigner
**Science owner:** User + ChatGPT
**Accepted local baseline:** `fce8842e5ddc6660c735b7f69723f63c9bff7073`
**Parent science lock:** C402 `ct_sector` semantics and C117 numerical-frontier audit
**Status:** `C403_C117_I2_FINITE_AXIS_AND_SPATIAL_KERNEL_NUMERICAL_PRIMITIVE_READY_FULL_C117_OPERATOR_UNAVAILABLE`
**Activation:** `NOT_READY`

## 1. Purpose

C401 supplied six complete K-local numerical C396 coordinate actions: the quark- and gluon-mass-squared directions at K9, K11, and K13. C402 then established that `ct_sector` cannot lawfully be represented by a canonical q↔qg vertex, a block identity, a spectator lift, or a zero operator. C402 selected the C117 `I2_density_projector` as the next numerical frontier, with a fail-closed fallback: when the complete coordinate action is unavailable, implement the smallest source-qualified numerical primitive and retain the full C117 direction as unavailable.

C403 executes that fallback. It closes two previously symbolic substructures:

1. an exact finite internal-member axis for the `I2_density_projector`, including exact admitted/rejected support; and
2. a numerical transverse-HO spatial kernel for every admitted internal HO mode at K9, K11, and K13.

C403 does **not** claim a complete numerical `c_C117_1` action. The C114 inverse/source factor, C119 current factors, spin/color/normalization contractions, target q/qg aggregation, and the C117 coefficient remain unbound.

## 2. Source-qualified finite-axis theorem

### 2.1 C45 and C47 basis domain

For each accepted resolution,

\[
K=\frac92,\frac{11}{2},\frac{13}{2},
\qquad
N_{\max}=8,10,12,
\qquad
b_{\mathrm{HO}}=0.40,0.45,0.50\ \mathrm{GeV},
\]

C45 uses two-dimensional HO labels `(n,m)` satisfying

\[
2n+|m|+1\le N_{\max}.
\]

Thus the one-particle candidate shell is

\[
N\equiv2n+|m|\le N_{\max}-1.
\]

C47 supplies strictly positive quark/gluon longitudinal fractions

\[
x_q=\frac{k_q}{K},\qquad x_g=\frac{k_g}{K},\qquad x_q+x_g=1.
\]

The qg product basis retained by the C47/C62 CM-relative construction satisfies

\[
N_q+N_g\le N_{\max}-2.
\]

### 2.2 Theorem

For every positive C47 longitudinal partition and either internal species,

\[
(n,m)\ \text{belongs to the C117 CM-ground preimage}
\quad\Longleftrightarrow\quad
2n+|m|\le N_{\max}-2.
\]

Equivalently, among the C45 one-particle candidates,

```text
ADMITTED  iff  2*n + abs(m) <= Nmax - 2
REJECTED  iff  2*n + abs(m)  = Nmax - 1
```

### 2.3 Necessity

If the selected one-particle mode has shell `Nmax-1`, then even a companion in its HO ground state has product shell

\[
N_{\mathrm{selected}}+N_{\mathrm{companion}}
\ge N_{\max}-1,
\]

which exceeds the qg product-shell cap `Nmax-2`. Such a mode cannot occur in any retained raw product state and is therefore exactly rejected. No magnitude threshold is involved.

### 2.4 Sufficiency and exact C62 witness

Let the selected internal mode have circular occupations

\[
N_+=n+\max(m,0),\qquad
N_-=n+\max(-m,0),
\]

so that

\[
N_++N_-=2n+|m|\equiv N.
\]

For a selected quark mode, choose the gluon companion in `(0,0)`, the CM output in `(0,0)`, and the relative output equal to the selected quark mode. Under the C62 oscillator transformation

\[
a_q^\dagger=\sqrt{x_q}\,a_{\mathrm{CM}}^\dagger+\sqrt{x_g}\,a_{\mathrm{rel}}^\dagger,
\]

all `N` excitations must enter the relative oscillator. The exact nonzero coefficient is

\[
C_q(N)=x_g^{N/2}.
\]

For a selected gluon mode, use a quark ground-state companion and the transformation

\[
a_g^\dagger=\sqrt{x_g}\,a_{\mathrm{CM}}^\dagger-\sqrt{x_q}\,a_{\mathrm{rel}}^\dagger.
\]

The exact nonzero coefficient is

\[
C_g(N)=(-1)^N x_q^{N/2}.
\]

Because `0<x_q,x_g<1`, neither coefficient vanishes. C403 verifies these closed forms against the independent exact C62 circular-occupation algebra for every retained partition, species, and candidate transverse mode.

### 2.5 Exhaustive support census

The cumulative number of two-dimensional HO modes with shell at most `S` is

\[
\sum_{N=0}^{S}(N+1)=\frac{(S+1)(S+2)}{2}.
\]

Therefore the candidate and admitted transverse counts are

\[
N_{\mathrm{candidate}}=\frac{N_{\max}(N_{\max}+1)}{2},
\qquad
N_{\mathrm{admitted}}=\frac{(N_{\max}-1)N_{\max}}{2}.
\]

Including positive longitudinal partitions, two helicities, and the fundamental/adjoint color dimensions gives the exact member counts emitted in `axis_summary.json`.

The exhaustive certificate contains:

```text
1774 partition/species/transverse-mode rows
1466 admitted exact nonzero witnesses
308 exact highest-shell exclusions
maximum exact/numerical residual = 0
```

The theorem removes the C64 runtime-artifact dependency only for this finite-support identity. It does not recreate the full C64 package or import C64 numerical coefficient arrays.

## 3. Numerical spatial primitive

### 3.1 Definition

For external transverse HO modes in the C47 intrinsic/relative qg basis

\[
a=(n_a,m_a),\qquad b=(n_b,m_b),
\]

and one contracted internal mode

\[
r=(n_r,m_r),
\]

The external matrix indices in this phase are restricted to the C47 intrinsic/relative qg transverse basis, `2n+|m|<=Nmax-2`.  C403 does not yet assemble the one-quark external C45 basis or the target-sector q/qg embedding.  This restriction is part of the primitive boundary, not a statement that the omitted q-sector matrix elements vanish.

C403 evaluates the C116 density-kernel primitive

\[
I_{ab;r}(b_{\mathrm{HO}})
=
\int d^2\mathbf{x}_\perp\,
\phi_a^*(\mathbf{x}_\perp;b_{\mathrm{HO}})
\phi_b(\mathbf{x}_\perp;b_{\mathrm{HO}})
\left|\phi_r(\mathbf{x}_\perp;b_{\mathrm{HO}})\right|^2.
\]

The implementation is derived directly from the C45 coordinate-space HO convention. C80 is not imported or reused: C116 limits C80 reuse to the `I4_local` spatial class and explicitly excludes it for `I2_density_projector`.

### 3.2 Analytic finite-sum form

Writing

\[
z=b_{\mathrm{HO}}^2 r^2,
\qquad
a_m=|m_a|=|m_b|,
\qquad a_r=|m_r|,
\]

the angular integral gives

\[
I_{ab;r}=0\qquad\text{when}\qquad m_a\ne m_b.
\]

For `m_a=m_b=m`,

\[
\begin{aligned}
I_{ab;r}
={}&\frac{b_{\mathrm{HO}}^2}{\pi}
(-1)^{n_a+n_b}
\sqrt{\frac{n_a!\,n_b!}{(n_a+|m|)!\,(n_b+|m|)!}}
\frac{n_r!}{(n_r+|m_r|)!}\\
&\times
\int_0^\infty dz\,e^{-2z}
 z^{|m|+|m_r|}
 L_{n_a}^{|m|}(z)
 L_{n_b}^{|m|}(z)
 \left[L_{n_r}^{|m_r|}(z)\right]^2.
\end{aligned}
\]

Every generalized Laguerre polynomial is finite. C403 expands the four-polynomial product with exact `Fraction` coefficients and evaluates each moment through

\[
\int_0^\infty dz\,z^p e^{-2z}
=\frac{p!}{2^{p+1}}.
\]

This exact-rational radial stage prevents false nonzero residues from cancellation in higher-order polynomial sums.

### 3.3 Independent numerical route

A separate generalized Gauss--Laguerre calculation uses weight

\[
e^{-t}t^{|m|+|m_r|}
\]

after the change `t=2z`. It does not call the analytic finite-sum evaluator. Three deterministic representative internal modes at each resolution are compared element by element across the complete external basis.

The largest observed analytic/quadrature difference is approximately

\[
4.08\times10^{-17}\ \mathrm{GeV}^2.
\]

### 3.4 Operator properties

For fixed internal mode `r`, the matrix is Hermitian because the multiplier `|phi_r|^2` is real. For any coefficient vector `c`,

\[
\sum_{ab}c_a^*I_{ab;r}c_b
=
\int d^2\mathbf{x}_\perp
\left|\sum_a c_a\phi_a(\mathbf{x}_\perp)\right|^2
|\phi_r(\mathbf{x}_\perp)|^2
\ge0.
\]

Thus every single-member kernel is positive semidefinite. C403 checks Hermiticity and the full eigenvalue spectrum for all 139 admitted internal modes across K9, K11, and K13.

An explicit weighted aggregate is provided only when the caller supplies a nonempty finite real weight map. No default, unit-weight, or minimum-norm aggregate exists. Positive semidefiniteness of an aggregate is claimed only when all supplied weights are nonnegative.

### 3.5 Units and scale

C45 defines `b_HO` as a momentum scale in GeV. The coordinate-space HO wavefunction carries one power of `b_HO`, so the four-wavefunction density integral has units

\[
[I_{ab;r}]=\mathrm{GeV}^2
\]

and scales as `b_HO^2`. C403 verifies the ground-state identity

\[
I_{00;0}=\frac{b_{\mathrm{HO}}^2}{2\pi}
\]

and exact quadratic scale behavior. The historical C396 metadata label `bHO_GeVinv` is not used to reinterpret the C45 source convention.

## 4. C396 binding effect

C403 updates the three K-local binding records for

```text
c_C117_1 / I2_density_projector
```

with:

- exact finite-axis access;
- exact support classification;
- numerical single-member spatial kernels;
- sparse CSR and independently evaluated matrix-free actions;
- Hermiticity, PSD, quadrature, and scale validation.

The full coordinate action remains unavailable. Consequently,

```text
complete C396 numerical coordinate actions before C403: 6
complete C396 numerical coordinate actions after C403:  6
complete numerical C117 coordinate actions:              0
```

The three updated binding rows are primitive-level advances, not complete apply paths and not rank information.

## 5. Smallest remaining object

The next source-faithful object required to complete `c_C117_1` is the K-local contraction joining:

1. the C114 source coefficient and nonzero-transfer `(i\partial^+)^{-2}` factor;
2. the C119 current-factor leaves;
3. the C115 spin, polarization, color, state-normalization, and `M^2` factors;
4. the C403 exact internal axis and spatial kernel;
5. the target q/qg matrix-target mapping and count-once aggregation;
6. the Hermitian reverse action.

The C117 coefficient remains factored and unselected. Missing factors remain unavailable, not zero.

## 6. Explicit nonclaims

C403 does not establish:

- a complete numerical C117 `I2_density_projector` coordinate action;
- a value, interval, or prior for `c_C117_1`;
- a numerical C114/C119/C115 contraction;
- a sector-qualified physical deuteron state;
- a production-current prescription;
- a physical response rank;
- a physical fit;
- equality of coefficients across K9, K11, and K13;
- a complete C396 forward map;
- Hamiltonian activation.

## 7. Decision

```text
C403 finite-axis paths:                    6
C403 spatial-kernel paths:                 3
C403 updated C117 primitive binding rows:  3
complete numerical C117 actions:           0
complete numerical C396 actions:           6
rank:                                      RANK_NOT_EVALUATED
physical fit:                              NOT_AUTHORIZED
activation:                                NOT_READY
```
