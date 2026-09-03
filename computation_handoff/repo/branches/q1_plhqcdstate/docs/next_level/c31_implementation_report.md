# C31/B1A implementation report

## Scientific result

C31 separates three objects that earlier architecture could too easily
conflate: the C11 finite-basis light-front overlap, the formally declared
project renormalized TMD, and the external ART25 optimal TMD. The source audit
finds no paper, theorem, or completed project calculation that matches the
specific C11 operator and finite-basis regulator to a UV-renormalized,
soft-subtracted, rapidity-renormalized TMD. The resulting decision is
`NO_SOURCE_QUALIFIED_LF_TO_TMD_MATCHING`.

The continuum audit does support a narrower result. Once a genuine project
square-root-soft renormalized TMD exists, its operator convention and the
EIS/modified-delta convention used by ART25 can be aligned using the published
continuum-definition equivalence. At the aligned definition the finite
operator factor is formally the identity; optimal-scale selection, the ζ
prescription, ordinary two-scale evolution, thresholds, the nonperturbative
boundary model, and the Collins--Soper kernel remain separate objects. This
formal adapter cannot act on C11 because the intermediate project TMD has not
been constructed.

Accordingly, the microscopic export is an empty unavailable vector rather
than a zero TMD, the C30 bridge is not rerun, and all twelve points remain
`BRIDGE_COMMON_DOMAIN_ONLY`.

## Microscopic operator and regulator

C11 is classified as a `REGULATED_MODEL_DENSITY`: a gauge-fixed finite-basis
wave-function overlap with Wilson order zero, positive-x antiquark slots, and
project-specific state/operator normalization. Its longitudinal modes,
transverse/OAM support, infrared scale, and endpoint support are regulator
data. No equivalence between that regulator and dimensional, modified-delta,
LaMET, lattice, or another continuum regulator is proved.

C14 supplies separate order-resolved Wilson and soft-overlap validation
content, but explicitly lacks UV-finite matching, the continuum soft
function, a physical TMD scheme, and Collins--Soper evolution. It is retained
as a convergence/parent axis and is neither added to nor silently substituted
for C11.

## Renormalization and matching audit

The component ledger covers quark-field and bilocal UV factors, Wilson-line
self energy and cusp terms, soft and square-root-soft allocation, zero-bin,
rapidity regulator/counterterm/anomalous dimension, UV anomalous dimension,
Hamiltonian/basis counterterms, regulator conversion, mixing, and power
corrections. C19--C22 supply validation oracles for selected continuum
anomalous dimensions and matching structures, not a C11 regulator matching.
Every C11-specific missing component remains blocking and nonzero-unknown.

The selected strategy is `P-E_UNAVAILABLE`. The direct-source and proved-
regulator-equivalence routes do not exist, and an operator-identical partonic
difference has not been calculated. The exact required external state,
diagrams, subtractions, counterterms, and closure tests are specified in the
missing-calculation note. A tree-level Wilson/soft/UV/rapidity identity is
validated only as `TREE_LEVEL_OPERATOR_LIMIT_VALIDATED`, with first omitted
order `O(alpha_s)` and a nonzero-unknown remainder.

## Primary sources

Fourteen version-locked PDFs are preserved under `data/raw/c31_sources/` with
SHA-256 hashes. The TMD-definition, soft, rapidity, scheme-equivalence,
ζ-prescription, evolution, and ART25 sources are direct or continuum
authorities at their stated scope. The BLFQ paper is a model-overlap comparison;
the LaMET and lattice papers demonstrate regulator-matching methodology. None
is operator/regulator-identical to C11.

## Isolation and validation

All 642 ART25 identities remain independent of the adapter, and the adapter
uses no ART25 member, FNP parameter, PDF/FF member, data point, chi2, bridge
residual, or holdout. The frozen eight-candidate/four-holdout split, data
ancestry, `NO_JOINT_MEASURE`, empty 642 x 0 projection, production registry,
and authoritative artifacts are unchanged. C31 creates no fit, calibration,
likelihood, posterior, optimizer, reweighting, emulator, process bridge, or
physical/deuteron/production status.

## Reproduction

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c31_manifests.py 1157
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c31.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

## Outcome branch

The exact next package is **C32/R0 — regulator-specific microscopic TMD
renormalization and partonic matching calculation**. It must calculate the
same operator with the C11 regulator and the target project TMD definition,
prove IR cancellation, and close UV, rapidity, soft, gauge, threshold, and
state-independence tests before any microscopic TMD export.
