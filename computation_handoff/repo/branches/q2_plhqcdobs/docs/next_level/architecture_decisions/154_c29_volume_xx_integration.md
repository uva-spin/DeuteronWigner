# ADR 154: Adopt Volume XX as the C29 bridge-geometry authority

## Decision

`references/volume_xx_source_reproducible_bridge_geometry.tex` is the
authoritative formal contract for the source-reproducible external/microscopic
bridge. Its supplied bytes are preserved and content addressed. All 53 stable
requirements are mapped to C29 evidence.

The C29 microscopic export explicitly retains the inherited C14 tensor-network
plan and treats bond dimension as a numerical/truncation axis, never as an
ART25 member or statistical replica.

## Consequences

- The formerly missing prompt-named Volume XX entry is replaced by the actual
  supplied authoritative filename and hash.
- C29 remains non-calibrating and fail-closed for numerical cross-root
  compatibility because its finite scheme adapter and common microscopic
  numerical vector remain unavailable.
- No process, inference, physical-input, deuteron, or production status is
  promoted.
- C30/B1 remains the next implementation package.

## Evidence

- `docs/next_level/c29_normative_source_integration.json`
- `docs/next_level/c29_volume_xx_requirement_crosswalk.json`
- `docs/next_level/c29_microscopic_axis_manifest.json`
- `scripts/validate_c29.py`
- `tests/test_c29_b0_bridge_contract.py`
