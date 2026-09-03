# JAMDiFF transversity input

Production quark parent tables use the authors' public JAMDiFF `wLQCD`
analysis from commit `2d601943b003ab03d261d492b565c1ebf54d07cc`:

- upstream library: <https://github.com/prokudin/JAMDiFF_library>
- physics source: Cocuzza et al., arXiv:2306.12998
- ensemble: LHAPDF member 0 central plus 968 physical replicas with lattice
  constraints
- retained table: `data/processed/jamdiff_wlqcd_transversity.csv`
- retained quantities: mean and standard deviation of \(x h_1\) for
  \(u,d,\bar u,\bar d\)
- grid: \(10^{-3}\le x\le0.99\) and
  \(Q^2=\{2,4,10,25,100\}\ {\rm GeV}^2\)

Reproduce the processed table after cloning the upstream repository:

```text
PYTHONPATH=src python scripts/extract_jamdiff_transversity.py \
  --jamdiff-library /path/to/JAMDiFF_library \
  --output data/processed/jamdiff_wlqcd_transversity.csv
```

The adjacent metadata JSON records the SHA-256 checksum. The adapter uses
shape-preserving interpolation in \(\log x\), linear interpolation in
\(\log Q^2\), and a zero endpoint continuation from \(x=0.99\) to 1.

JAMDiFF enforces the Soffer bound using the PDFs internal to that fit. This
project composes the result with CT18 \(f_1\), BDSSV24 \(g_1\), and distinct
Gaussian widths. Therefore the central \(h_1\) is projected onto the actual
TMD-level positivity interval of the composed boundary over
\(0\le k_T\le1.5\) GeV. A 0.5% interior margin avoids saturation roundoff.
The poorly constrained sea mean above \(x=0.5\) receives a configurable
\((1-x)^8\) endpoint factor before that projection. This is a documented
compatibility/model choice, not part of the JAMDiFF fit.

The original compact table retains only pointwise standard deviations. The
production replica path now vendors the exact upstream commit and reads
`JAMDiFF23-transversity_lo`: member 0 is the central curve and members 1--968
are the physical Monte Carlo ensemble. This assignment is independently
verified because member 0 reproduces the compact mean while the population
standard deviation of members 1--968 reproduces the compact standard
deviation.

Reproduce the member-preserving cache and nuclear bands:

```text
git clone https://github.com/prokudin/JAMDiFF_library.git \
  data/vendor/JAMDiFF_library
git -C data/vendor/JAMDiFF_library checkout \
  2d601943b003ab03d261d492b565c1ebf54d07cc
/Users/dustin/miniforge3/bin/python3.9 \
  scripts/generate_jamdiff_replica_grid.py --x-points 385
for wave in av18 cd-bonn nvia nvib nviia nviib; do
  /Users/dustin/miniforge3/bin/python3.9 \
    scripts/propagate_jamdiff_transversity_replicas.py \
    "outputs/parent_tmds/quark_${wave}_fine.csv" \
    --output \
    "outputs/parent_tmds/uncertainty/jamdiff_transversity_${wave}_fine.csv"
  /Users/dustin/miniforge3/bin/python3.9 \
    scripts/propagate_jamdiff_transversity_replicas.py \
    "outputs/parent_tmds/quark_${wave}_fine.csv" --tmd h1Lperp \
    --output \
    "outputs/parent_tmds/uncertainty/jamdiff_h1Lperp_${wave}_fine.csv"
done
/Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_jamdiff_transversity_atlas.py
/Users/dustin/miniforge3/bin/python3.9 \
  scripts/build_jamdiff_transversity_atlas.py --tmd h1Lperp
```

Every replica receives the same documented large-\(x\) sea endpoint and is
projected member by member onto the CT18+BDSSV Gaussian TMD Soffer interval
before the LF convolution. This is a model-dependent compatibility operation
required by composing fits that used different \(f_1,g_1\) inputs; raw source
members remain recoverable from the vendored LHAPDF set. The same member
identity is propagated through the derived WW \(h_{1L}^{\perp}\) functional,
so its band remains correlated with \(h_1\). This propagates fitted-input
uncertainty; it does not resolve genuine twist-3 WW-breaking uncertainty.
