# BPV20 Sivers input and reference implementation

The fitted quark Sivers boundary is the N3LO extraction of M. Bury,
A. Prokudin, and A. Vladimirov, JHEP 05 (2021) 151,
arXiv:2103.03270. The project vendors the public arTeMiDe v2.05 release at
commit `ea0af1a75e21e316c1ac4ece51933988836a6650`.

The official `BPV20(n3lo).rep` artifact contains a central member and 500
Monte Carlo replicas. Its SHA-256 is
`732e26be19e5b28995801183aa1116cfd9fab49316b9e7346a9be9c1833470cb`.
The model is flavor resolved for u, d, s, and a common fitted light-sea
component. Equality of ubar and dbar is therefore a published BPV20 fit
assumption; u and d are independent.

The NNPDF31 central grid required by the released constants is stored under
`data/raw/lhapdf/NNPDF31_nnlo_as_0118_1000`. The `.info` and member-0
SHA-256 values are respectively
`f5fc2f70655a00dd426dda9294d5b7a3c617aaec63f84b8ada79637745404fde`
and
`b367000f810148b25b1b1b65a4b37138d2d27dd4351497b6674283f834bd090d`.

## Reproducible toolchain

```sh
/Users/dustin/miniforge3/bin/conda env create \
  -p /Users/dustin/work/DeuteronWigner/.conda-artemide \
  -f environment-artemide.yml
/Users/dustin/miniforge3/bin/python3.9 tools/prepare_bpv20_artemide.py
/Users/dustin/miniforge3/bin/conda run \
  -p /Users/dustin/work/DeuteronWigner/.conda-artemide \
  make -C data/vendor/artemide-v2.05 \
  FCompilator=arm64-apple-darwin20.0.0-gfortran \
  Fpath=/Users/dustin/work/DeuteronWigner/.conda-artemide/bin/arm64-apple-darwin20.0.0-gfortran
```

Build `harpy` by replacing `make` with `make harpy` in the final command.
NumPy 1.26 f2py requires the pinned `setuptools==59.8.0` compatibility
layer for this historical Fortran release.

`tools/bpv20_boundary_fixture.f90` independently reproduces the published
FNP formula. At x=0.1 and b=1 GeV^-1, Python and Fortran agree to machine
precision. `tools/bpv20_artemide_probe.f90` checks the optimal, Q=5 evolved,
and k-space values against the compiled release.

The BPV20 paper explicitly reports violations of the parton-model Sivers
positivity inequality. The project therefore records proton/neutron
constituent eigenvalue tensions without silently clipping the fit, while
retaining positivity of the physical deuteron impulse and corrected totals
as a validation gate.
