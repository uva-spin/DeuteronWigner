# Reproducible development environment

The project uses Python 3.9 because the validated local LHAPDF 6.5.5
bindings are built for that interpreter. `environment.yml` is the
authoritative reproducible environment declaration.

Create and verify the environment from the repository root:

```text
conda env create -f environment.yml
conda activate deuteron-wigner
python -c "import numpy, scipy, pandas, matplotlib, lhapdf, pypdf, fitz, reportlab"
PYTHONPATH=src python -m pytest -q
```

The validated local interpreter required an explicit `pytest==8.4.2`
installation on 2026-07-25. It is already constrained by `environment.yml`
and the `analysis` optional dependency group; reproduce it with
`python -m pip install -e '.[analysis]'`.

Roles and provenance:

- NumPy and SciPy provide tensor algebra, quadrature, interpolation, and
  Fourier transforms.
- pandas provides long-form scientific output and validation tables.
- Matplotlib creates the TMD atlases.
- LHAPDF 6.5.5 supplies CT18NNLO and reads the project-local BDSSV24-NLO
  ensemble plus the paired MSHT20 QED proton/neutron ensembles used for
  numerical unpolarized CSB. Cite LHAPDF6, EPJ C75 (2015) 132, when
  publishing results.
- pypdf checks PDF structure; PyMuPDF 1.26+ is the rendering fallback when
  Poppler is unavailable.
- ReportLab 4.x generates reproducible scientific atlases.

The CT18NNLO set must be visible on the active LHAPDF search path.
BDSSV24-NLO is stored under `data/raw/lhapdf`; the polarized provider adds
that directory automatically. The code fails if a required PDF or
interpolation point is unavailable rather than silently extrapolating.

Install the public MSHT20 QED grids reproducibly:

```text
curl -L --max-time 120 \
  https://lhapdfsets.web.cern.ch/current/MSHT20qed_nnlo.tar.gz \
  -o /tmp/MSHT20qed_nnlo.tar.gz
curl -L --max-time 120 \
  https://lhapdfsets.web.cern.ch/current/MSHT20qed_nnlo_neutron.tar.gz \
  -o /tmp/MSHT20qed_nnlo_neutron.tar.gz
tar -xzf /tmp/MSHT20qed_nnlo.tar.gz -C data/raw/lhapdf
tar -xzf /tmp/MSHT20qed_nnlo_neutron.tar.gz -C data/raw/lhapdf
PYTHONPATH=src python scripts/audit_msht20qed_csb.py
```

Install the public JAM21 pion ensemble used by the tensor Sullivan
convolution:

```text
curl -L --max-time 120 \
  https://lhapdfsets.web.cern.ch/current/JAM21PionPDFnlo.tar.gz \
  -o /tmp/JAM21PionPDFnlo.tar.gz
tar -xzf /tmp/JAM21PionPDFnlo.tar.gz -C data/raw/lhapdf
PYTHONPATH=src python -m pytest -q tests/test_pion_exchange.py
PYTHONPATH=src python scripts/compare_b1_pion_exchange_to_hermes.py
```

The set contains 786 replicas and no distinguished central member:
production averages every replica. The AV18 coordinate-space wave function
under `data/raw/av18/deut.wf` is also required. See
`references/miller_pion_exchange_input.md` for physics provenance, scope,
and limitations.

Validated platform on 2026-07-25: macOS arm64, Conda 25.7, Python 3.9,
NumPy 1.26.3, SciPy 1.13.0, pandas 2.1.4, Matplotlib 3.8.2, LHAPDF 6.5.5,
pypdf 6.14.2, and PyMuPDF 1.26.5. Set `MPLCONFIGDIR` to a writable cache
such as `/private/tmp/deuteron-mpl` on restricted macOS workers.

Reproduce the endpoint-aware global-moment inputs and audit:

```text
PYTHONPATH=src python scripts/compute_all_parton_momentum_parent.py
PYTHONPATH=src python scripts/compute_gluon_helicity_parent_grid.py
PYTHONPATH=src python scripts/audit_parent_moment_coverage.py
PYTHONPATH=src python -m pytest -q tests/test_moment_ledger.py
```

The first command uses CT18NNLO for all active
\(\bar b,\bar c,\bar s,\bar u,\bar d,d,u,s,c,b,g\) flavors. The second uses
the project-local BDSSV24-NLO central member and resolved AV18
\(SS,SD,DS,DD\) retained-spin convolution. Both write provenance sidecars.
