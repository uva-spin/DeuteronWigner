# C400.S2 Corrective Mathematical and Algorithmic Design

**Status:** ChatGPT corrective implementation lock, pre-integration
**Physical fit:** not authorized
**Physical rank:** not evaluated
**Historical evidence:** preserved; no P1/P1B/P1C file is rewritten

## 1. Purpose and scope

C400.S2 separates a successfully executed but nonphysical C144 diagnostic smoke path from the still-incomplete C396 Hamiltonian family.  The distinction is structural:

\[
H^{\mathrm{diag}}_{144,R}(\phi_m,\phi_g,\eta_0,\ldots,\eta_8)
\neq
H^{\mathrm{C396}}_{R}(\theta_R),
\]

where the C144 fixture has eleven numerical coordinates, while the C396 family declares nineteen K-local coordinates,

\[
\theta_R=
(\underbrace{\delta_1,\ldots,\delta_6}_{\text{counterterms}},
 \underbrace{n_1,\ldots,n_9}_{\text{source-null directions}},
 \underbrace{c_1,\ldots,c_4}_{\text{C117 finite directions}}).
\]

The patch proves only that the C144 fixture can be assembled, diagonalized, differentiated through a versioned diagnostic adapter, and replayed through invariant numerical comparisons.  It does not substitute C144 coordinates for C396 coordinates and does not claim that an unprojected lowest eigenpair is the physical deuteron.

## 2. Truthful status algebra

The historical P1C result is retained and superseded by the conjunction

\[
\begin{aligned}
&\texttt{C144\_DIAGNOSTIC\_EIGENSTATE\_SMOKE\_PATH\_READY},\\
&\texttt{C396\_19\_COORDINATE\_BINDING\_INCOMPLETE},\\
&\texttt{SECTOR\_IDENTITY\_UNVERIFIED},\\
&\texttt{RANK\_NOT\_EVALUATED},\\
&\texttt{PHYSICAL\_FIT\_NOT\_AUTHORIZED}.
\end{aligned}
\]

A field named `forward_map_ready` is no longer meaningful without naming its operator family, coordinate domain, state identity, current path, and observable range.

## 3. Versioned C144 derivative integrity

The historical C144 implementation is immutable.  C400.S2 reconstructs the derivative of the polynomial that the public C144 operator actually evaluates.

For the free term,

\[
H_{\mathrm{free}}(m) \supset m^2 P_q,
\qquad
\frac{\partial H_{\mathrm{free}}}{\partial m}=2mP_q.
\]

For the canonical vertex,

\[
H_{53}(g)=gV_{53},
\qquad
\frac{\partial H_{53}}{\partial g}=V_{53}.
\]

For the retained interaction terms as numerically implemented by C144,

\[
H_t(g,\eta)=g^2 V_t+\eta_{i(t)}P_t,
\qquad
\frac{\partial H_t}{\partial g}=2gV_t.
\]

The implementation uses `eta_0` for C112, `eta_1` for C127, and `eta_2` for both retained C129 terms.  Consequently,

\[
\frac{\partial H}{\partial \eta_2}=P_{129,G3}+P_{129,G4},
\]

rather than only one retained C129 contribution.  `eta_3` through `eta_8` have no numerical response in the C144 fixture API.  They are therefore labeled

`NUMERICALLY_UNBOUND_IN_C144_FIXTURE_API`,

not physically irrelevant.

The matrix audit compares the corrected derivative with a central finite difference,

\[
D_i^{\mathrm{FD}}(h)=
\frac{H(\theta+h e_i)-H(\theta-h e_i)}{2h},
\]

using Frobenius, maximum-entry, nonzero-pattern, and relative differences.  The historical derivative is separately compared with the corrected diagnostic derivative.  The generated audit covers all eleven fixture coordinates at K9, K11, and K13: 33 rows total.  All 33 corrected derivatives pass the declared numerical tolerance; six historical rows disagree, corresponding to `phi_coupling` and `eta_2` at all three resolutions.

This establishes only diagnostic C144 derivative integrity.  It makes no C396 derivative or physical-rank claim.

## 4. C396 binding ledger

For each resolution R in K9, K11, and K13, the patch emits nineteen rows with:

- coordinate and class;
- source and operator owner;
- exact resolution/basis identity;
- coefficient units/convention;
- sector support;
- Hermiticity authority;
- numerical apply and derivative status;
- cross-resolution status;
- exact smallest missing object.

The ledger has 57 rows.  No row currently has a complete numerical C396 apply path.  This is a result, not a failure of the ledger: symbolic ownership is distinguished from executable sparse/matrix-free realization.

The resolution record preserves the distinction

\[
K_2\in\{9,11,13\},
\qquad
K=K_2/2\in\{9/2,11/2,13/2\}.
\]

It also exposes, rather than resolves, the repository conflict between the C46 `bHO_GeV` authority and the later C396 field label `bHO_GeVinv`.

## 5. Sector-qualified state semantics

Let P be a candidate sector projector.  A state may be labeled `PROJECTED_SECTOR_STATE` only when P is numerically supplied and satisfies

\[
\|P-P^\dagger\|\le \epsilon_P,
\qquad
\|P^2-P\|\le \epsilon_P.
\]

The Hamiltonian is then restricted to the range of P,

\[
H_P=B^\dagger H B,
\]

where the columns of B span `range(P)`.  For a returned full-space eigenvector \(\psi\), the patch records

\[
\|P\psi\|,
\qquad
\|(I-P)\psi\|,
\qquad
\|P(P\psi)-P\psi\|,
\qquad
\|H\psi-E\psi\|.
\]

Without P, the result is `UNPROJECTED_DIAGNOSTIC_EIGENPAIR` and carries only a C144 fixture-basis scope.  Text labels such as `J=1`, `color=singlet`, or `CM=ground` are not numerical evidence.

The one-dimensional projector case is supported explicitly; the dense restricted eigensolver permits \(k=\dim\operatorname{range}(P)\).

## 6. State tracking

Tracking is performed independently within exact conserved-sector keys.  For one sector, let

\[
M_{ij}=|\langle \psi_i^{\mathrm{old}}|\psi_j^{\mathrm{new}}\rangle|.
\]

The assignment maximizes the complete objective

\[
\max_{\pi}\sum_i M_{i,\pi(i)}
\]

using the Hungarian algorithm.  Ambiguity is evaluated against the best alternative complete assignment, obtained by forbidding each selected edge in turn.  It is not inferred solely from row-local overlap ties.

For a matched nondegenerate state, the phase is fixed by

\[
e^{i\alpha}=
\frac{\langle\psi_{\mathrm{old}}|\psi_{\mathrm{new}}\rangle}
{|\langle\psi_{\mathrm{old}}|\psi_{\mathrm{new}}\rangle|},
\qquad
\widetilde\psi_{\mathrm{new}}=e^{-i\alpha}\psi_{\mathrm{new}}.
\]

Near-degenerate states are grouped as disjoint connected components within the same conserved sector.  For orthonormal old and new bases U and V, C400.S2 reports singular values of

\[
U^\dagger V,
\]

principal angles

\[
\vartheta_i=\arccos \sigma_i,
\]

and spectral-projector distance

\[
\|UU^\dagger-VV^\dagger\|_F.
\]

For square matched subspaces, the Procrustes transport is applied and the aligned basis is returned.  Rectangular subspaces return both projectors and principal-angle diagnostics but do not pretend that a square transport exists.  Surplus states retain `SURPLUS_UNMATCHED`, even when they lie in a near-degenerate current component.  Eigenvalue crossings between different conserved sectors are not state swaps.

## 7. Canonical LF/LPS current comparison

Light-front and Lev–Pace–Salmè routes have different route-local frames, current components, and amplitude normalizations.  Those differences are expected.  Each request is first validated and extracted under its own convention contract.  The resulting named dimensionless observables are then mapped into

`C400_CANONICAL_DIMENSIONLESS_GC_GM_GQ`.

Comparison eligibility requires only:

\[
Q_1^2=Q_2^2,
\qquad
M_{d,1}=M_{d,2},
\qquad
\mathrm{state\_id}_1=\mathrm{state\_id}_2,
\]

within declared tolerances, plus successful route-local extraction and a recognized form-factor normalization.

The record includes componentwise absolute and relative differences, the LF angular-condition residual, route-local prescription spread, and all local assumptions.  It does not choose a production current, bind a current covariance, or claim physical agreement.

## 8. Semantic replay

Raw iterative-eigensolver vector hashes are retained only as incidental provenance.  Scientific replay identity is based on:

- eigenvalues within absolute/relative tolerances;
- residual norms;
- phase-invariant singleton overlaps;
- principal angles and spectral-projector distance for degenerate clusters;
- exact dependency exception type and first path named by the exception.

For a nondegenerate singleton, replay uses

\[
|\langle\psi^{(1)}|\psi^{(2)}\rangle|.
\]

For a degenerate cluster, an arbitrary unitary rotation inside the subspace is accepted when the spectral projector and singular values agree.  Thus a scientifically equivalent replay is not rejected because ARPACK returned a different phase or internal degenerate basis.

Dependency failures use `FileNotFoundError.filename` when present and otherwise parse source-like paths from the actual exception text.  The missing path is stored repository-relative, and the human-readable exception message replaces the checkout prefix with `<REPOSITORY_ROOT>` so evidence hashes do not depend on the local directory.  There is no fallback to a hard-coded C64 object.

## 9. Step-size and solver-tolerance evidence

The generated scan compares Hellmann–Feynman and tracked central finite-difference eigenvalue responses for `phi_mass` over

\[
h\in\{10^{-3},10^{-4},10^{-5}\},
\qquad
\epsilon_{\mathrm{eig}}\in\{10^{-8},10^{-9}\}.
\]

The result shows the expected cancellation/noise growth at the smallest step.  The record explicitly sets `single_step_certification=false`.  The scan establishes a diagnostic stability picture only; no physical or C396 derivative is certified.

## 10. Scientific boundary

C400.S2 does not establish:

- a C396 numerical Hamiltonian over all nineteen coordinates;
- a numerical deuteron-sector projector;
- a physical deuteron eigenstate;
- a state-to-current production observable path;
- a production current prescription;
- a physical likelihood or fit;
- a physical response rank;
- coordinate irrelevance;
- resolution averaging or Hamiltonian activation.

The smallest next mechanical frontier is the source-owned, K-local numerical realization of the matrix-valued C396 coordinates and an approved nonmatrix treatment for the vacuum, boundary, and truncation directions.  Integration into the live repository remains a Codex task; scientific interpretation and merge acceptance remain with the user and ChatGPT.
