# ADR 193: Keep finite-basis soft conversion distinct from the continuum oracle

Status: accepted for the fail-closed C33/S0 completion.

## Decision

The continuum modified-delta soft expression is a source-qualified target
oracle. The finite-basis soft object is a separately calculated quantity. Their
conversion stores logarithmic cutoff terms, finite constants, power
corrections, endpoints, zero modes, and numerical remainder separately.

At tree level the conversion is the identity and its remainder is zero. At one
loop the conversion is unavailable and its value status is `NONZERO_UNKNOWN`;
the continuum expression may not be copied into the finite-basis field.

## Evidence

- C32's project oracle is source identified but not transcribed as a
  microscopic result.
- The C33 source audit distinguishes target-soft authorities from finite-
  regulator methodologies.
- No existing C5/C6/C12-C14 object depends simultaneously on `b`, `mu`,
  `delta+`, `delta-`, and the C33 soft resolution.

## Authority and status

- **Exact:** tree conversion `Z=1`, tree remainder `0`, inverse/round-trip
  identity, and state/hadron independence requirements.
- **Source-qualified:** continuum one-loop target coefficients.
- **Finite-regulator model:** C33 basis artifacts and power corrections.
- **Temporary/open:** one-loop conversion and trajectory; no matching status is
  issued under `C33_SOFT_TREE_LEVEL_ONLY`.

## Alternatives considered

- Copy the continuum soft function: rejected as provenance fraud.
- Tune a finite constant to the oracle: rejected as a fit.
- Use one resolution as the continuum: rejected.
- Use ART25 members or bridge residuals: forbidden.

## Consequences

- Oracle validation can close independently of microscopic conversion.
- Round-trip fields remain unavailable rather than fabricated.
- C34/S0A or a later trajectory package owns the first one-loop conversion.

## Affected files and tests

- `src/deuteron_wigner/bridge/s0/core.py`
- `docs/next_level/c33_continuum_soft_oracle.json`
- `docs/next_level/c33_continuum_soft_validation_report.json`
- `docs/next_level/c33_soft_regulator_matching_library.json`
- `docs/next_level/c33_soft_regulator_roundtrip_report.json`
- `docs/next_level/c33_soft_regulator_remainder.json`
- `tests/test_c33_s0.py` tree round-trip, oracle separation, and fit/data
  contamination rejection tests

## Revision triggers

Revise after three or more finite resolutions determine the predicted
logarithmic structure and independently validate the finite, power, endpoint,
and zero-mode pieces. Pointwise agreement is not sufficient.
