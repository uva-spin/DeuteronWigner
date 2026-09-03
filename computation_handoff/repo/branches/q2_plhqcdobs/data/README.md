# External physics inputs

This directory contains provenance-tracked physics inputs used by DeuteronWigner.

## Layout

- `raw/av18/` - files downloaded without modification from Robert Wiringa's Argonne theory
  pages.
- `raw/cd_bonn/` - primary CD-Bonn publication and, later, derived/tabulated radial functions.
- `raw/literature/` - immutable papers used for equation-level implementation comparisons.

Processed, interpolated, or convention-converted data must be written to a separate `processed/`
tree. Raw files are immutable inputs.

## Spin-1 TMD literature

- `raw/literature/1612.06585.pdf`
  - T. van Daal, "Quark and gluon TMD correlators in momentum and
    coordinate space," arXiv:`1612.06585`.
  - Authoritative definite-rank table for 18 quark and 19 gluon
    leading-twist spin-1 TMDs.
  - SHA-256: `72931e4bbe86cbc33fdb9ca49276cb4462e4932dc6cbf92d9cfced1912c3d21a`.

- `raw/literature/epja-2025-61-81.pdf`
  - J. Poudel et al., *Eur. Phys. J. A* 61, 81 (2025).
  - DOI: `10.1140/epja/s10050-025-01558-w`.
  - Downloaded 2026-07-24 from the Jefferson Lab publication record.
  - SHA-256: `f06e35fa516e754ba9ff7745fe7acc8c02708c3429efc671e6fc6455c8d771a0`.
- `raw/literature/2603.15224v1.pdf`
  - X. Xie, D.-Y. Chen, and Z. Lu,
    "Gluon TMDs for tensor polarized deuteron in a spectator model."
  - arXiv: `2603.15224v1`.
  - Downloaded 2026-07-24 from arXiv.
  - SHA-256: `32491014283b05c5d1bf6279b5d413c4a68252b52bcd74d9bddc2f4cc9bbd501`.

The equation-level comparison is recorded in
`references/tmd_literature_comparison_2025_2026.md`.

## Polarized proton PDFs

- `raw/lhapdf/BDSSV24-NLO/BDSSV24-NLO.info`
- `raw/lhapdf/BDSSV24-NLO/BDSSV24-NLO_0000.dat`
  - Project-local metadata and central member of the BDSSV24 NLO polarized
    proton PDF set from the official LHAPDF archive.
  - Reference: I. Borsa, D. de Florian, R. Sassot, M. Stratmann, and
    W. Vogelsang, *Phys. Rev. Lett.* 133, 151901 (2024),
    arXiv:`2407.11635`.
  - The set covers \(10^{-5}\le x\le1\) and
    \(1\le Q\le316.23\) GeV.
  - The complete local set is vendored: member 0 and all 600 uncertainty
    replicas. The directory contains 601 data files and occupies about
    479 MB.
  - SHA-256 metadata:
    `d37b087d2d5f7703cd08a63b46c434cc4bac9d4113c90cf658936d4000a056d7`.
  - SHA-256 member 0:
    `2bef49657250230507398ebdf4873d877c1c338b2b8948227592182b7c81d75b`.

## AV18

Downloaded 2026-07-23 from the Argonne National Laboratory theory site:

- `raw/av18/deut.wf`
  - URL: `https://www.phy.anl.gov/theory/research/av18/deut.wf`
  - Configuration-space reduced radial functions and derivatives.
  - SHA-256: `9a937c67aaed00b11399e05c72c781bef6c61cb1878c785efafa7fe4276d2f9a`
- `raw/av18/deut.wfk`
  - URL: `https://www.phy.anl.gov/theory/research/av18/deut.wfk`
  - Momentum-space \(S\)- and \(D\)-wave functions.
  - File convention states \(k\) in \(\mathrm{fm}^{-1}\), functions in
    \(\mathrm{fm}^{3/2}\), normalized by
    \(\int dk\,k^2[u(k)^2+w(k)^2]=1\).
  - SHA-256: `6bfe39d084e692c75a1bbbb921e13a7941c6ee5b7de7b71a24e010da9ab35523`
- `raw/av18/fdeut.av18`
  - URL: `https://www.phy.anl.gov/theory/research/deuteron/fdeut.av18`
  - Extended deuteron properties, wave-function tables, form-factor integrals, and impulse
    approximation observables.
  - SHA-256: `5d20de4b865e69da95a3c05d3815193e00ae8908610186dbbd7ebb1b2fd5dcb5`

Primary reference: R. B. Wiringa, V. G. J. Stoks, and R. Schiavilla, Phys. Rev. C 51, 38
(1995).

## CD-Bonn

- `raw/cd_bonn/nucl-th-0006014.pdf`
  - URL: `https://arxiv.org/pdf/nucl-th/0006014`
  - R. Machleidt, *The high-precision, charge-dependent Bonn nucleon-nucleon potential*,
    Phys. Rev. C 63, 024001 (2001).
  - Appendix C gives the analytic \(n=11\) deuteron wave-function parameterization, coefficient
    table, constraints, Fourier transform, and normalization.
  - SHA-256: `208c7a6aaf628b3060d594ca7bbb5551bb90e867892358cac24c40bbce9298de`

The CD-Bonn tables generated from Appendix C are derived data, not raw author-supplied tables.
Their generator and numerical validation against the paper's normalization, \(D\)-state
probability, and selected tabulated values must accompany them.

## Norfolk local chiral interactions and currents

- `raw/norfolk/fdeut.nvia`, `fdeut.nvib`, `fdeut.nviia`, and `fdeut.nviib`
  are the Argonne author tables for the four NV2 deuteron wave functions.
  Models a/b use \((R_S,R_L)=(0.8,1.2)/(0.7,1.0)\) fm; classes I/II fit
  NN data through 125/200 MeV.
- `raw/references/schiavilla_et_al_2018.pdf`
  is R. Schiavilla et al., *Local chiral interactions and magnetic structure
  of few-nucleon systems*, arXiv:1809.10180. It supplies the matched
  configuration-space current, regulators, LECs, and Table III magnetic-moment
  benchmarks.
  SHA-256:
  `2adbf0e79891c5a9faccf8e1b5e4047c22dfd681accba1b9734c0dd86a304628`.

## HERMES tensor DIS

- `raw/hermes_b1/hep-ex-0506018.pdf`
  - URL: `https://arxiv.org/pdf/hep-ex/0506018`
  - HERMES Collaboration, A. Airapetian et al., *First Measurement of the Tensor Structure
    Function \(b_1\) of the Deuteron*, Phys. Rev. Lett. 95, 242001 (2005).
  - SHA-256: `c206088c28436697e62058079696f8ac60888aaddbb9c53a60ae398b13b189b4`
- `processed/hermes_b1/table_ii.csv`
  - Manual transcription of Table II.
  - The paper reports \(A_{zz}^d\), \(b_1^d\), and both statistical and systematic errors in
    units of \(10^{-2}\); the CSV stores ordinary dimensionless values after applying that factor.
  - Transcription was checked visually against rendered PDF page 4 on 2026-07-23.
  - Statistical and systematic errors remain separate; no covariance matrix is supplied by the
    publication.

The HERMES points span \(Q^2=0.51\) to \(4.69\ \mathrm{GeV}^2\). Low-\(Q^2\) points are not
automatically valid leading-twist PDF comparison points and must carry a kinematic-validity flag.

## Collinear deuteron convolution reference

- `raw/references/1702.05337.pdf`
  - URL: `https://arxiv.org/pdf/1702.05337`
  - W. Cosyn, Yu-Bing Dong, S. Kumano, and M. Sargsian, *Tensor-polarized structure function
    \(b_1\) in the standard convolution description of the deuteron*.
  - Used to disambiguate experimental and target scaling variables: the HERMES table uses
    \(x=Q^2/(2M_N\nu)\), while \(x_D=Q^2/(2P_D\cdot q)\), so \(x\simeq2x_D\).
    Its active-nucleon fraction \(\alpha\), centered near one, corresponds to \(2y\) when this
    project's constituent fraction is \(y=p_N^+/P_D^+\), centered near one half.
  - SHA-256: `d84a8673f834823f619b632e7f7ffbd203130cf6ca7034aa9f606e79ff1c4923`

## Light-front angular condition

- `raw/references/hep-ph-0301213.pdf`
  - URL: `https://arxiv.org/pdf/hep-ph/0301213`
  - C. E. Carlson and C.-R. Ji, *Angular Conditions, Relations between Breit and Light-Front
    Frames, and Subleading Power Corrections*, Phys. Rev. D 67, 116002 (2003).
  - Supplies the light-front parity/time-reversal relations, normalized nucleon \(J^+\)
    helicity amplitudes, and the spin-1 angular condition used by the current diagnostics.
  - SHA-256: `0ae200ea9612f0fd4fcf7908b3b931511e39515416308b2d12ced52479be8eab`

## Covariant light-front current

- `raw/references/lev_pace_salme_2000.pdf`
  - Primary source for the longitudinal-Breit current, Hermitian completion,
    and unambiguous spin-1 form-factor extraction.
  - SHA-256:
    `49dfce2d563e7992d880e1074be95f82c555f56dc92cd1009aafbdab72258ae0`.

- `raw/references/carbonell_karmanov_1999.pdf`
  - Primary source for separating physical and light-front-orientation-dependent
    spin-1 form factors and the need for non-`J+` contractions in \(G_M\).
  - SHA-256:
    `b910e65d1f69688d3e13350011ce0070a9f29ee05dcfedab72e1787398059671`.

- `raw/references/kolling_epelbaum_phillips_2012.pdf`
  - S. Kolling, E. Epelbaum, and D. R. Phillips, *The magnetic form factor of
    the deuteron in chiral effective field theory*, arXiv:1209.0837.
  - Source for the first isoscalar two-body magnetic current at \(O(eP^4)\):
    the \(\bar d_9\) one-pion term and \(L_2\) M1 contact term.
  - SHA-256:
    `fa056a402ec8b7d5d0d7e89cbc4e8b65c47abbc5bb0530a3f62797760003a339`.
