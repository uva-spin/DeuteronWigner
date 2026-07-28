# Covariant light-front deuteron current references

## Lev, Pace, and Salme (2000)

- F. M. Lev, E. Pace, and G. Salme, *Poincare' Covariant Current Operator and
  Elastic Electron-Deuteron Scattering in the Front-form Hamiltonian Dynamics*,
  Phys. Rev. C **62**, 064004 (2000), arXiv:nucl-th/0006053.
- Local file: `data/raw/references/lev_pace_salme_2000.pdf`
- SHA-256:
  `49dfce2d563e7992d880e1074be95f82c555f56dc92cd1009aafbdab72258ae0`

Implemented ingredients:

- Eqs. (11) and (14): Hermitian auxiliary current and `J- = J+`;
- Eq. (21): extraction from `J+_11`, `J+_00`, and `Jx_10-Jx_01`;
- Eqs. (42)-(46): longitudinal-Breit constituent kernels, spectator mapping,
  and node-dependent nucleon momentum transfer.

The AV18 table stores half-isoscalar nucleon form factors, so its values are
multiplied by two where LPS require proton-plus-neutron sums. The transverse
kernel returns the magnetic moment in nucleon-magneton units; output `GM`
explicitly applies `GM=(M_D/m_N) mu_D`.

## Carbonell and Karmanov (1999)

- J. Carbonell and V. A. Karmanov, *Deuteron electromagnetic form factors in
  the Light-Front Dynamics*, Eur. Phys. J. A **6**, 9-19 (1999),
  arXiv:nucl-th/9902053.
- Local file: `data/raw/references/carbonell_karmanov_1999.pdf`
- SHA-256:
  `b910e65d1f69688d3e13350011ce0070a9f29ee05dcfedab72e1787398059671`

Their physical/spurious covariant separation shows that the magnetic form
factor requires current contractions beyond `J+`. Therefore the old
four-amplitude `J+` spread remains a diagnostic, not a microscopic uncertainty
band or a substitute for a transverse current.
