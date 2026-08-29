# 2026 LFHEFT NNπ source audit

## Source

X. Cao, S. Cheng, Y. Duan, Y. Li, S. Xu, and X. Zhao,
“Non-perturbative flavor asymmetry in the nucleon and deuteron: The
light-front Hamiltonian effective field theory approach,”
arXiv:2601.13567, J. Subatomic Part. Cosmology 5 (2026) 100329.
The archived local source is
`references/arxiv_2601.13567_lfheft_nnpi.pdf`.

## What the source supplies

- A general LF Fock-space definition of constituent longitudinal momentum
  distributions through squared many-body LFWFs, Eqs. (1)--(7).
- A scalar-EFT nucleon calculation through \(N+3\pi\), with three- versus
  four-body truncation differences used as a convergence diagnostic.
- A preliminary scalar deuteron calculation beginning from
  \(|D\rangle=|NN\rangle+|NN\pi\rangle+\cdots\).
- A Wilson--Bloch effective two-body Hamiltonian, Eqs. (9)--(11), obtained by
  integrating out the three-body sector. At the physical 2.2 MeV binding it
  predicts a narrowly localized scalar nucleon LMD.

## What it does not supply

The authors explicitly state that dynamical pions have not yet been fully
integrated into the nuclear bound state and that the full four-body equation
is work in progress. The paper does not publish:

- a deuteron \(NN\pi\) three-body LFWF;
- nucleon/pion helicity amplitudes or spin-1 tensor projections;
- an off-forward overlap or transfer-sharing prescription;
- node-resolved virtuality correlations;
- machine-readable LFWF/LMD data or covariance;
- a deuteron pion GTMD/TMD.

The scalar Wilson--Bloch two-body solution cannot be relabeled as the
missing spin-resolved NNπ correlator. Its strong-binding examples at 200 and
500 MeV are sensitivity studies, not physical-deuteron defaults.

## Implementation consequence

The repository's sourced Miller forward NNπ splitting, exact Fock ledger,
conditional longitudinal recoil, and forward \(b_T\)-space recoil remain the
best-supported configurable default. They must remain explicitly
model-dependent in scalar-pion spin inheritance. Extending them off forward
with an arbitrary \(\exp(-B_\pi\Delta_T^2)\), fixed transfer fraction, or
scalar-Hamiltonian wave function would hide missing physics and is refused.

The replacement interface requires a versioned three-body amplitude

\[
\Psi_{NN\pi}^{\Lambda}
(\alpha_i,\boldsymbol{k}_{Ti},\lambda_1,\lambda_2;
 \text{isospin},\text{virtuality}),
\]

or equivalent initial/final spectral overlap. Required replacement tests
are forward reduction to the validated Miller moments, Hermiticity under
initial/final interchange, spin-1 polarization completeness, Fock
normalization, plus-momentum closure, and convergence in the declared
three-body basis.

