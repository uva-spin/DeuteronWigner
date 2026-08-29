# Audit of recent light-front hidden-color deuteron models

## Kaur–Mondal–Zhao–Ji cluster model

The open-access model in Phys. Rev. D **113**, 054008 (2026),
arXiv:2507.09886, is directly relevant but cannot yet replace the production
non-nucleonic parent.

Useful implemented concepts in the paper include:

- a normalized two-cluster LFWF separated into light-front holographic
  transverse dynamics and a longitudinal 't Hooft equation;
- an explicit Melosh-rotated spin-1 cluster wave function;
- cluster \(f_1\), \(g_{1L}\), and \(f_{1LL}\) projections;
- the exact cluster sum rules
  \(\int f_1=1\) and \(\int f_{1LL}=0\);
- a flavor-resolved convolution with external cluster PDFs.

However, the paper explicitly states that its singlet–singlet versus
octet–octet decomposition cannot be identified. It treats clusters as
pointlike, retains only \(L=0\), does not supply antiquark/gluon
spin-resolved cluster correlators, does not implement QCD evolution, and
fits a deeply bound effective cluster mass corresponding to roughly
200 MeV binding rather than the physical 2.2 MeV deuteron. Consequently,
labeling its LFWF as a quantified hidden-color parent would overstate what
the calculation determines.

Its three central parameters are
\(m_{\cal C}=0.838\pm0.083\) GeV,
\(\kappa=0.13\pm0.013\) GeV, and
\(g=0.50\pm0.05\) GeV. A future implementation may retain it as a separate
deep-binding cluster sensitivity model, but it must not be mixed into the
physical NN parent or used to assign an octet probability.

## BLFQ six-quark calculations

arXiv:2503.21371 and arXiv:2505.12889 solve six-quark and
six-quark–one-gluon light-front Hamiltonians and explicitly analyze color
sectors. They are a more promising parent architecture. The publications do
not provide a versioned, machine-readable helicity-amplitude ensemble in the
repository audit performed on 2026-07-25. Production ingestion therefore
requires released basis coefficients/wave functions or an independently
reproducible Hamiltonian diagonalization with matching truncation and
renormalization.

## Decision

The Miller observable-only six-quark scenario remains separate. The 2026
cluster model is recorded as a model-comparison target, while a
flavor/spin/OAM-resolved BLFQ amplitude is the preferred replacement input.
No claimed hidden-color probability is inferred from either paper without
the corresponding amplitudes.

