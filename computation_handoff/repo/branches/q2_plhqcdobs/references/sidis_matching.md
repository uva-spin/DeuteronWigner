# SIDIS W/Y matching policy

The process-level cross section is organized as

\[
 d\sigma = W + Y,\qquad
 Y=d\sigma^{\mathrm{FO}}-d\sigma^{\mathrm{ASY}},
\]

where \(W\) is the resummed low-\(q_T\) term and ASY is its expansion at the
same fixed order and in the same subtraction convention. The measured hadron
momentum obeys \(P_{hT}=-z_hq_T\).

The primary implementation reference is Boglione et al.,
[arXiv:1412.1383](https://arxiv.org/abs/1412.1383), especially Eqs. (1),
(22), and (23) and Sec. 3.3. That analysis demonstrates that standard
additive Y matching is not automatically reliable in low/intermediate-energy
SIDIS: the nonperturbative W term and the asymptotic result may lack a
same-sign overlap region, and the resulting W+Y curve need not approach the
fixed-order cross section.

Project policy:

- W-only results are restricted by an explicit low-\(q_T\) domain.
- A Y callable must identify the process, perturbative order, source, and
  asymptotic subtraction convention.
- High-\(q_T\) W+Y evaluation additionally requires a passed numerical
  overlap assessment: at least three contiguous same-sign points with
  W/ASY relative agreement inside the declared tolerance.
- No generic NLO remainder is inferred from a standalone TMD.
- At the current \(Q=5\) GeV JLab-like slice, matching remains unverified
  until a consistent fixed-order SIDIS calculation and fragmentation input
  are installed. This is a limitation, not permission to extrapolate W.

The implementation is in `w_y_matching.py`; focused tests are in
`test_w_y_matching.py`.

## Fixed-order backend audit

APFEL++ master was audited on 2026-07-25 from the official
`vbertone/apfelxx` repository. Its `inc/apfel/SIDIS.h` supplies collinear
double-convolution coefficient operators in \(x,z\), while its
`docs/latex/src/SIDISTMD.tex` and TMD builders supply the Fourier-Bessel
resummed \(W\) term and SIDIS hard factor. Neither layer supplies the
\(q_T\)-differential fixed-order SIDIS cross section together with the
same-order ASY expansion required for \(Y=\mathrm{FO}-\mathrm{ASY}\).
APFEL++ is therefore not installed as a Y backend. This is an evaluated
incompatibility, not a dependency failure.

The vendored arTeMiDe `TMDX_SIDIS` implementation was also inspected. It
provides the process-dependent TMD hard factor and resummed SIDIS term, not
the missing fixed-order remainder. A future backend must expose both FO and
ASY at an identical order, scheme, PDF/FF choice, and kinematic convention;
only then may `assess_matching_overlap` enable high-\(q_T\) evaluation.

## TMD-distribution versus observable boundary

A process-specific \(Y=\mathrm{FO}-\mathrm{ASY}\) remainder is part of a
specified differential observable, with its hard channel, charges/color
factors, and (for SIDIS) fragmentation input. It is not a universal additive
term in an intrinsic TMD distribution and must not be used to force a
TMD-only transverse marginal.

Accordingly, production TMD tables enforce this boundary: gauge-link
reversal and gluon f/d color composition are typed operations; W-only rows
carry a validity flag; the default domain is \(q_T\le1\) GeV and
\(q_T/Q\le0.25\); and high-\(q_T\) observable evaluation fails without a
sourced FO/ASY pair and numerical overlap test. The gluon atlas hatches its
outside-validity region. This verifies factorization enforcement for the TMD
model without claiming an unspecified high-\(q_T\) cross section.
