# MSHT20 QED charge-symmetry-breaking input

The numerical unpolarized neutron charge-symmetry-breaking (CSB) input uses
the paired public LHAPDF sets `MSHT20qed_nnlo` DataVersion 2 and
`MSHT20qed_nnlo_neutron` DataVersion 3. The physics source is T. Cridge,
L. A. Harland-Lang, A. D. Martin, and R. S. Thorne, *Eur. Phys. J. C* 82
(2022) 90, [arXiv:2111.05357](https://arxiv.org/abs/2111.05357). The fit
includes QED-corrected DGLAP evolution and supplies 38 Hessian eigenvector
pairs at 68% confidence level.

For neutron flavor \(q\), the adapter defines

\[
\delta_q^n(x,Q)=
\frac{q_{\mathrm{MSHT20QED}}^n(x,Q)}
     {q_{\mathrm{MSHT20QED}}^p{}_{\mathrm{\,isospin\ partner}}(x,Q)}-1.
\]

This same-fit ratio isolates neutron CSB rather than importing the unrelated
difference between the project's CT18 baseline and MSHT20. Proton
corrections are zero in this mechanism component. The paired proton/neutron
member identity is retained when propagating the Hessian uncertainty.

Scope and limitations:

- The numerical correction applies only to the unpolarized \(f_1\)
  amplitude. No correction is inferred for helicity, transversity,
  rank-one/rank-two, T-odd, or transverse-width inputs.
- The multiplicative interface is declared for
  \(10^{-5}\le x\le0.4\), \(1\le Q\le100\) GeV. The released central anti-up
  grid changes sign near \(x=0.458\) at \(Q=5\) GeV, so extending a positive
  multiplicative density correction beyond \(x=0.4\) would be unjustified.
- Large relative sea corrections near the upper boundary can multiply very
  small absolute sea densities; consumers must retain absolute as well as
  relative uncertainty.
- Exact isospin remains a separately tested switchable limit.

Implementation: `src/deuteron_wigner/csb_inputs.py`. Reproduce the input and
validation table with:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/audit_msht20qed_csb.py
```

The report is
`outputs/nucleon_inputs/msht20qed_csb_Q5.validation.json`.

The central nuclear propagation is reproduced with:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_msht20qed_csb_parent.py
```

It writes `outputs/parent_tmds/msht20qed_csb_parent.csv` and its validation
report. The paired Hessian propagation is:

```text
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 \
  scripts/export_msht20qed_csb_parent_hessian.py
```

The member table retains all 77 paired members (166,320 rows); the band table
contains the correlated 38-pair Hessian at every wave/flavor/TMD/momentum
point. The vectorized member-0 result agrees with the independent central
convolution to \(2.01\times10^{-13}\) GeV\(^{-2}\), and the mechanism
correlators are Hermitian to machine precision.
