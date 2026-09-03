# ADR 198: Adopt Volume XXI as the regulator-specific microscopic TMD authority

Status: accepted as a post-completion C33/S0 formal-source integration.

## Decision

Preserve the supplied
`references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex`
byte-for-byte and treat it as the normative contract for the regulator-specific
microscopic TMD operator chain, the disjoint B=1 collinear and B=0 vacuum-soft
roots, their joint-regulator and zero-bin interface, UV and rapidity
renormalization, finite-basis trajectories, partonic matching, and conditional
bridge export.

Extract all 65 stable `V21.*` requirements in source order and map them to
concrete C31--C33 evidence. The crosswalk must distinguish structural closure,
explicit fail-closed coverage, and work deferred to C34 or later. Source
availability is not numerical execution and authorizes no status promotion.

## Justification

Volume XXI was not available when C33/S0 was executed. C33 therefore derived
its architecture from the authoritative work-package prompt and primary
literature and recorded that it did not infer the missing volume's contents.
The later source agrees with the implemented separation of the proton and
vacuum roots, the four-line singlet soft operator, the modified-delta identity,
the count-once overlap interface, and the exact tree normalization. It also
states that a rigorous tree-level-only or structural no-go is a valid outcome.

The source does not contain the regulator-specific finite-basis one-loop mode
sums or evaluated counterterms. It therefore cannot close UV, rapidity,
trajectory, soft-collinear compatibility, zero-bin, matching, or export gates
by itself.

## Consequences

- `C33_SOFT_TREE_LEVEL_ONLY` remains the exact C33 outcome.
- C34/S0A remains the exact next package.
- The 65-requirement crosswalk is additive and non-promoting.
- C11, C32, all bridge roles and holdouts, `NO_JOINT_MEASURE`, all 642 ART25
  identities, the 216-route registry, and eight authoritative artifacts remain
  unchanged.
- No microscopic proton export, bridge rerun, fit, likelihood, inference, or
  physical claim is created.

## Evidence and affected files

- `references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex`
- `docs/next_level/c33_volume_xxi_requirement_crosswalk.json`
- `docs/next_level/c33_normative_source_integration.json`
- `docs/next_level/c33_implementation_report.md`
- `references/formalism_volume_index.md`
- `handoff/ROADMAP.md`
- `scripts/build_c33_manifests.py`
- `scripts/validate_c33.py`
- `tests/test_c33_s0.py`

## Revision trigger

Revise the scientific no-go only after C34/S0A evaluates the complete
finite-basis one-loop soft ledger and closes the dependent UV, rapidity, gauge,
trajectory, conversion, compatibility, and zero-bin gates. A formal source or
continuum oracle alone is insufficient.
