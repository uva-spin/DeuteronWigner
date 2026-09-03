# ADR 192: Keep rapidity-renormalized soft and CS conventions source located

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The bare soft dependence, rapidity counterterm, renormalized soft factor,
rapidity anomalous dimension, and Collins-Soper/D-function convention are five
separate content-addressed records. The derivative sign and normalization must
be source located; a CS kernel cannot be inferred from a cancellation fixture
or from ART25.

At tree level the rapidity counterterm is one and the anomalous dimension is
zero. C33 records no one-loop value because the modified-delta bare factor and
counterterm are unavailable.

## Evidence

- C6's missing/duplicate half-soft derivatives test count-once algebra but has
  no assigned physical rapidity scheme.
- C19-C22 are project validation or downstream evolution oracles, not the C33
  finite-basis soft calculation.
- C32 leaves rapidity renormalization and the CS kernel unavailable.

## Authority and status

- **Exact:** tree rapidity factor `1`, tree anomalous dimension `0`, and
  separation of all five records.
- **Source-qualified:** derivative convention, continuum anomalous dimension,
  and cusp consistency target.
- **Finite-regulator model:** C33 rapidity-window realization.
- **Temporary/open:** one-loop cancellation, gauge independence, and cusp
  consistency. The validation status is not issued.

## Alternatives considered

- Copy an ART25 or C21 kernel: rejected as data/model contamination.
- Call the C6 algebraic cancellation a CS extraction: rejected.
- Merge UV and rapidity factors: rejected because their regulators and RG
  equations differ.

## Consequences

- `C33_SOFT_RAPIDITY_RENORMALIZATION_VALIDATED` remains closed.
- All one-loop values and residuals are null/unavailable, not numerical zero.
- The package remains `C33_SOFT_TREE_LEVEL_ONLY`.
- C34/S0A must compute the bare dependence before differentiating it.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_soft_rapidity_renormalization.json`
- `docs/next_level/c33_soft_rapidity_anomalous_dimension.json`
- `docs/next_level/c33_soft_collins_soper_kernel_oracle.json`
- `tests/test_c33_s0.py` tree convention, record separation, and copied-kernel
  rejection tests

## Revision triggers

Revise when the complete one-loop modified-delta soft factor, rapidity
counterterm, and source-located derivative convention jointly pass regulator,
gauge, resolution, and cusp checks.
