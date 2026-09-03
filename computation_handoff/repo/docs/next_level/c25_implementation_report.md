# C25/P1A implementation report

## Result

C25 recovered and hash-locked the complete official ART25 model payload and its full correlated member file. The payload first appears in official commit `9ca8159e00ff2df159ab2ce4d7ffb13589af0c71`; the exact ARTEMIDE v3.01 engine remains commit `d873dc9fdcebba707df3bf9ae73061511fbf803f`. These are deliberately represented as a two-component source identity. No v3.02/v3.03 engine code was substituted.

The exact v3.01 engine and Python extension compile and import without a physics patch. All nine payload model sources are byte-identical to the model sources at the v3.01 tag. Runtime initialization and process reproduction remain fail-closed because the official constants file requests three custom collinear ensembles—`MSHT20_REP`, `MAPFF10NNLOPIp`, and `MAPFF10NNLOKAp`—that were not found in the official repository, Zenodo records, paper sources, DataProcessor repository, or audited public package inventory.

## Member semantics and reproduced evidence

The authoritative `.rep` header declares 642 stochastic replicas. It contains two additional technical records: initialization and the central/mean record. Thus there are 644 stored rows, but 642 rows define the resampling distribution. The older “500 replicas” prose is inconsistent with the released machine-readable payload and is recorded as such rather than silently forced onto the file.

Each row has 28 NP slots and three collinear indices. Twenty-two NP slots are fitted: two CS-kernel, ten TMDPDF, five pion-TMDFF, and five kaon-TMDFF parameters. Six fixed/model-control slots remain present in each typed record. The parser preserves all values, indices, row locations, roles, and the source hash. Independent NumPy calculations reproduce means, empirical 16/84 percentiles, central-versus-mean differences, and the numerical 22-parameter correlation matrix. Published table comparisons are limited by printed rounding; the figure-only correlation plot is a qualitative holdout.

## Source and physical gates

The unchanged C24 thirteen source gates and six physical-input gates were rerun. Recovering the ART25 payload closes the earlier payload and correlated-member ambiguity, but not the complete process chain. Source-process eligibility therefore remains 0, physical-input eligibility remains 0, analytic eligibility remains 438, and 102 identities remain not process eligible. No DY/SIDIS number, likelihood, fit, posterior, deuteron matched total, or production route was created.

The frozen benchmark grid covers fixed-target and collider/rapidity DY, HERMES-like pion SIDIS, COMPASS-like kaon SIDIS, and CS/TMDPDF/pion-TMDFF/kaon-TMDFF distribution points. Inputs were frozen, but numerical source comparisons are correctly marked unavailable rather than populated with substitutes.

## Validation and isolation

The exact C24 baseline passed 1,112 tests before C25 edits. C25 adds strict parsing, dropped-row rejection, independent statistics, 960 ordered negative injections, deterministic manifest validation, and immutable-artifact checks. The production registry remains exactly 216 and all eight authoritative artifacts remain byte-identical. The missing Volume XIX TeX reference is recorded explicitly; no normative content was invented.

## Exact next job

C26/P1B should ingest the three exact collinear member sets and frozen process outputs requested in `c25_art25_author_request.md`, verify their hashes and licenses, initialize the exact v3.01 engine without modifying the ART25 constants, and execute the already frozen central and 642-member DY/SIDIS grid. Until those inputs arrive, source-process qualification must remain closed.
