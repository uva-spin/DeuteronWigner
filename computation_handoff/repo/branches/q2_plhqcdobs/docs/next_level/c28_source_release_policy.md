# C28 source release policy

## Boundary

C28 reproduces the public ART25 analysis with public `artemide-DataProcessor`
source and locally held scientific inputs. The public repository history,
dataset CSV files, source hashes, metadata, derived predictions, aggregate
statistics, and validation manifests may be published subject to their
upstream licenses.

`MSHT20_REP` DataVersion 3 was transferred directly by the ART25 author for
research validation. No explicit permission to redistribute the raw grids was
provided. Consequently the raw archive and extracted grids remain outside Git.
Their hashes, declared metadata, joint-member indices, and derived numerical
summaries are recorded so an authorized holder can reproduce the calculation.
This restriction does not block local reproduction, but it does block a claim
that a fresh public checkout is self-contained.

The MAPFF10NNLOPIp and MAPFF10NNLOKAp inputs are the exact public LHAPDF
DataVersion 1 archives already locked by C26. ARTEMIDE v3.01 and the ART25
DataProcessor commit are used unchanged. C28 neither relicenses upstream work
nor infers rights absent from the upstream records.

## Release checklist

Before releasing a C28 derivative:

1. exclude raw `MSHT20_REP` files and archives;
2. retain repository, commit, dataset, and derived-artifact hashes;
3. identify every output as source-regenerated, not author-frozen;
4. preserve the W-only and external-proton qualifications;
5. do not publish credentials, private correspondence, or machine-local paths;
6. obtain explicit permission before distributing transferred grids.

