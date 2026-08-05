# C29/B0 implementation report

## Scientific result

C29 implements a typed, immutable bridge contract between
`ART25_EXTERNAL_SOURCE_ROOT` and `PROJECT_MICROSCOPIC_OPERATOR_ROOT`. The two
roots remain disjoint. The bridge cannot replace a microscopic state with an
ART25 member, infer a cross-root member correlation, identify phenomenological
deuterium with the microscopic deuteron, or identify an NN-only plan with the
complete matched nuclear total.

This is a validation and future-calibration contract. It is not a fit,
likelihood, posterior, replica reweighting, calibration, emulator, process
qualification, physical deuteron prediction, or production route.

## Operator and target audit

Fourteen minimum operator families are crosswalked using species, flavor,
polarization, target, twist, transverse rank, naive-T parity, Wilson-link and
color class, UV/rapidity/soft scheme, reference scales, and common domain.
The rank-zero unpolarized u, d, ubar, and dbar entries have a common validation
domain, but no complete finite ART25-to-microscopic scheme adapter or
scheme-qualified microscopic numerical vector. They are therefore not called
distribution-ready. The quark Collins-Soper kernel is diagnostic only. Gluon,
spin-1 LL, helicity, transversity, and all T-odd/multiparton candidates remain
unavailable for this bridge.

The target crosswalk separately represents proton, neutron, antiproton,
phenomenological deuterium, microscopic NN deuteron, and matched-total
deuteron identities. Every nuclear component remains explicit: NN, NNPI,
DeltaDelta, six-quark cluster, six-quark hidden color, transition/interference,
coherent pilot, and matched total.

## Frozen grid and covariance

The 34-point bridge grid was frozen before microscopic export or compatibility
diagnostics. It contains distribution, Collins-Soper, DY one-leg, SIDIS
target-leg, domain-boundary, target, provenance, nuclear, and covariance-null
controls. Calibration-candidate and holdout-candidate are roles only; C29 does
not execute calibration.

An exact selector projects the authoritative C28 anomaly factor from
642 x 1209 to ten frozen process coordinates plus one declared linearly
dependent null-space control. Member identities remain
ordered 1 through 642 and normalization remains sqrt(641). Dense direct and
factor covariance reconstruction agree to floating-point precision, symmetry
closes exactly, and the positive-semidefinite and null-space diagnostics are
reported without clipping or ridge regularization. A nonlinear point-ratio
oracle is evaluated memberwise and empirically recentered.

## Microscopic export and compatibility boundary

Twenty C11 microscopic operator identities are exported with their plan,
member, target, species, Wilson order, matching, evolution, scheme, numerical,
and evidence status. Their assumption axes remain separate and are never
treated as posterior replicas. Because no common scheme-qualified numerical
microscopic TMD vector exists, cross-root numerical compatibility diagnostics
are fail-closed. The implemented rank-aware whitening calculation is exercised
only as an external technical-record covariance oracle and is explicitly not a
cross-root comparison, likelihood, chi-square probability, or p-value.

## Data ancestry and discrepancies

The ancestry graph contains all 46 ART25 datasets and all 1,209 retained point
identities. Future use of the compressed ART25 ensemble is mutually exclusive
with treating its underlying data as independent likelihood evidence. The
four future plans are alternatives, not additive evidence.

Thirteen discrepancy components are typed. Two have presently auditable
separate numerical/source information; eleven remain nonzero-unknown. Unknown
discrepancy is never set to zero and external covariance is not inflated to
hide a target, scheme, matching, nuclear, or missing-Y mismatch.

## Reproduction

```bash
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/build_c29_manifests.py <test-count>
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 scripts/validate_c29.py
PYTHONPATH=src /Users/dustin/miniforge3/bin/python3.9 -m pytest -q
```

The heavy projected arrays are reconstructed under
`data/runtime/c29_bridge/external_bridge_projection.npz`; the committed
manifest records their schema, hash, dimensions, coordinates, and member
order. Raw transferred MSHT20_REP files remain outside public Git.

## Exact next job

C30/B1 should close a genuinely common numerical distribution-level bridge
for rank-zero proton quark and antiquark TMDs: supply a source-audited finite
scheme adapter and a scheme-qualified microscopic numerical export with
convergence and discrepancy inputs. It must validate that bridge before any
calibration or inference package is authorized.
