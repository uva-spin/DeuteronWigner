# C401 — Reduced Numerical C396 Forward-Map Science Lock

**Project:** DeuteronWigner
**Scientific owner:** user + ChatGPT
**Accepted repository baseline:** `ada80920fb51617333c9b87a40d6538a0b0de915`
**Status:** `SCIENCE_LOCK_READY_FOR_FIRST_NUMERICAL_OPERATOR_IMPLEMENTATION`
**Physical fit:** forbidden
**Physical rank:** not evaluated
**Activation:** not ready

## 1. Scientific objective

Construct the first source-faithful numerical path for the actual C396 Hamiltonian family,

\[
\vartheta_K
\longmapsto
H_K(\vartheta_K;\beta_K)
\longmapsto
P_{d,K}H_KP_{d,K}
\longmapsto
\lvert\Psi_{d,K}\rangle
\longmapsto
J_K^\mu
\longmapsto
\bigl(G_C,G_M,G_Q\bigr)_K,
\]

without substituting the C144 diagnostic fixture for a C396 owner, selecting physical coordinate values, or reporting an identifiability rank before the numerical forward map exists.

The first implementation target is not all nineteen raw C396 slots at once. The raw slot registry mixes matrix coefficients, vacuum-only directions, basis/domain choices, and truncation-discrepancy terms. The coordinate ontology must be reduced before numerical implementation.

## 2. Raw C396 slot registry

At each resolution \(K\in\{K9,K11,K13\}\), the C396 record exposes

\[
\Theta_K^{\rm raw}
=
\bigl(
 c_{m,K},
 c_{{\rm vac},K},
 c_{g,K},
 c_{{\rm sec},K},
 c_{{\rm bdry},K},
 c_{{\rm trunc},K},
 n_{1,K},\ldots,n_{9,K},
 d_{1,K},\ldots,d_{4,K}
\bigr),
\]

where the six \(c\)-slots are the C396 counterterm labels, the nine \(n_i\) are the source-side null labels, and the four \(d_a\) are the C117 finite directions.

This nineteen-slot count is a registry count. It is not a numerical operator rank and is not the number of independent measured constants.

## 3. Mandatory coordinate reduction

### 3.1 Vacuum-energy direction

The source-side C131/C136 construction classifies the vacuum direction as nonmatrix and excluded from the retained fixed-particle projected Hamiltonian. Let \(P_{0,K}\) project onto the vacuum sector and \(P_{d,K}\) onto the positive-\(P^+\), fixed-particle deuteron sector. With

\[
P_{d,K}P_{0,K}=0,
\]

a vacuum-only operator \(V_{{\rm vac},K}=P_{0,K}V_{{\rm vac},K}P_{0,K}\) satisfies

\[
P_{d,K}V_{{\rm vac},K}P_{d,K}=0.
\]

Therefore `ct_vacuum_energy` is not to be represented by an invented identity shift in the retained deuteron Hamiltonian. Its provisional C401 status is

```text
VACUUM_ONLY_OUTSIDE_RETAINED_Q_QG_DIRECT_SUM
```

subject to an explicit numerical projector certificate once \(P_{d,K}\) is implemented.

### 3.2 Boundary direction

`ct_boundary` is a boundary/domain interface, not an additive sparse matrix coefficient. It enters through the definition of the domain, boundary action, longitudinal mode set, zero-mode policy, or holonomy sector:

\[
H_K = H_K(\vartheta_K;\beta_K),
\]

where \(\beta_K\) is a separately typed structural record. It is excluded from the linear operator Jacobian \(\partial H/\partial\vartheta_i\).

Status:

```text
NONMATRIX_DOMAIN_OR_BOUNDARY_PARAMETER
```

### 3.3 Truncation direction

`ct_truncation` is not to be fabricated as a Hamiltonian insertion. Truncation uncertainty is represented in observable space,

\[
O_K = O_\infty + \delta_K,
\]

or through a declared discrepancy/covariance model after numerical multi-resolution evidence exists.

Status:

```text
NONMATRIX_TRUNCATION_DISCREPANCY
```

### 3.4 Mass direction

The separate bare-mass and mass-counterterm slots are not independently physical. The numerical parameterization must use the source-identified renormalized mass-squared combination, denoted

\[
\mu_{q,K}^2,
\]

with any orthogonal bare/counterterm split treated as a renormalization-scheme coordinate. The C401 numerical operator is therefore

\[
D_{q,K}=\frac{\partial H_K}{\partial \mu_{q,K}^2},
\]

not an independently fitted `ct_mass` proxy.

Status:

```text
IDENTIFIED_RENORMALIZED_MASS_SQUARED_DIRECTION
```

### 3.5 Maximum candidate numerical dimension

After moving the vacuum, boundary, and truncation slots out of the additive matrix-coordinate vector, the maximum candidate matrix-affecting set is

\[
\vartheta_K^{\rm candidate}
=
\bigl(
 \mu_{q,K}^2,
 c_{g,K},
 c_{{\rm sec},K},
 n_{1,K},\ldots,n_{9,K},
 d_{1,K},\ldots,d_{4,K}
\bigr),
\]

with maximum dimension

\[
1+1+1+9+4=16.
\]

This is an upper bound on candidate numerical directions, not a physical rank. The dimension may decrease after the nine source-null directions are assigned exact operator semantics or proven redundant/nonmatrix.

## 4. First source-faithful numerical operator pair

The C128 free invariant-mass operator supplies exact source-owned dependence on quark and gluon mass-squared parameters. For a one-quark basis state \(\lvert q,\alpha\rangle\),

\[
M_{0,K}^2\lvert q,\alpha\rangle
=
\mu_{q,K}^2\lvert q,\alpha\rangle
+\text{transverse contribution}.
\]

For a quark-gluon basis state \(\lvert qg,\alpha\rangle\) with longitudinal fractions \(x_q(\alpha)\) and \(x_g(\alpha)\),

\[
M_{0,K}^2\lvert qg,\alpha\rangle
=
\left[
\frac{k_{\perp,\alpha}^2+\mu_{q,K}^2}{x_q(\alpha)}
+
\frac{k_{\perp,\alpha}^2+\mu_{g,K}^2}{x_g(\alpha)}
\right]
\lvert qg,\alpha\rangle
+\text{HO radial mixing}.
\]

The mass derivatives are independent of the transverse-HO mixing:

\[
D_{q,K}\lvert q,\alpha\rangle=\lvert q,\alpha\rangle,
\qquad
D_{g,K}\lvert q,\alpha\rangle=0,
\]

\[
D_{q,K}\lvert qg,\alpha\rangle
=\frac{1}{x_q(\alpha)}\lvert qg,\alpha\rangle,
\qquad
D_{g,K}\lvert qg,\alpha\rangle
=\frac{1}{x_g(\alpha)}\lvert qg,\alpha\rangle.
\]

Both operators are diagonal, Hermitian, K-local, and dimensioned so that their coefficients carry GeV\(^2\). The gluon counterterm primitive is represented by the same source-owned gluon bilinear derivative as an additive shift in \(\mu_{g,K}^2\); no physical value is selected.

These are the first two lawful C396 numerical apply paths to implement at K9 and then reproduce at K11 and K13.

## 5. Required implementation behavior

The numerical layer must provide, for each resolution:

1. a sparse-coordinate representation of \(D_{q,K}\) and \(D_{g,K}\);
2. an independent matrix-free application route;
3. exact q/qg basis-order ownership;
4. exact longitudinal-fraction provenance for every diagonal entry;
5. finite, positive fractions satisfying \(x_q+x_g=1\) on qg states;
6. Hermiticity and dimensional checks;
7. sparse-versus-matrix-free equality;
8. finite-difference agreement with an independent C43/C47 source-mass functional (as amended below);
9. no use of C144 diagnostic entry-value rules;
10. no physical mass or counterterm value.

Completion of this first slice changes the C396 numerical binding count from zero to six complete K-local rows:

\[
2\ \text{operators}\times3\ \text{resolutions}=6.
\]

It does not establish a physical state or physical rank.

## 6. Next operator order

After the two mass-bilinear operators pass:

1. **Sector counterterm `ct_sector`.** Determine the exact source normalization and whether its operator is an independent q\(\leftrightarrow\)qg vertex direction or a renormalization of the canonical C53 vertex. No proportionality is assumed before proof.
2. **Four C117 directions.** Implement the four graph-local insertions using their C117/C259 operator identities and finite-basis support, preserving mixing and scheme labels.
3. **Nine source-null directions.** Resolve each C151 owner into matrix, nonmatrix, exact redundancy, omitted-space interface, zero-mode, or normalization class. Do not create nine arbitrary matrices from ordinal labels.
4. **Numerical deuteron-sector projector.** Establish a source-owned, Hermitian, idempotent projector and verify \((I-P)HP\) before assigning deuteron-sector state status.
5. **State-to-current path.** Connect the verified projected state to the accepted LF/LPS diagnostic-current interface.

## 7. Acceptance conditions for the first slice

The first numerical-operator slice is accepted only if:

```text
C43/C47 source mass dependence used directly; C128 retained only for accepted dimensions/order
D_q sparse/matrix-free routes agree at K9/K11/K13
D_g sparse/matrix-free routes agree at K9/K11/K13
finite differences agree for multiple step sizes
all operators are Hermitian
all basis dimensions and orderings agree with source records
vacuum/boundary/truncation slots are not materialized as fake matrices
no C144 proxy is used
no coordinate value is selected
physical rank remains RANK_NOT_EVALUATED
activation remains NOT_READY
```

## 8. Scientific nonclaims

This science lock does not establish:

- the complete C396 Hamiltonian;
- numerical realizations for `ct_sector`, the nine source-null directions, or the four C117 directions;
- a sector-qualified physical deuteron state;
- a production current;
- physical coordinate values;
- a likelihood fit;
- a physical response rank;
- K9/K11/K13 convergence;
- Hamiltonian activation.

## 9. Immediate project outcome

The immediate project target is now precise:

> Implement and verify the exact K-local quark- and gluon-mass-squared operator directions, while formally removing vacuum, boundary, and truncation slots from the additive matrix-coordinate problem. This is the first numerical reduction of the C396 frontier and the first step from a 57-row symbolic inventory toward a genuine state-to-observable forward map.
