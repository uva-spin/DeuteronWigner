# C5 validation-only Wilson-line API

All objects live in `deuteron_wigner.pilot.wilson_line`. They are isolated
from production and retain the C1 coordinate, path, operator, sector, and map
identity system.

## Path and pole

- `BareWilsonSegment`: dynamical data decorating the authoritative
  `WilsonPathId`. Its orientation, representation, Fourier convention,
  coupling convention, momentum flow, rapidity regulator, endpoint fibers,
  tangent, closure, ordering, and Wilson order serialize explicitly.
- `derived_eikonal_pole`: derives
  `1/(v·l-i0 eta) = PV(1/(v·l)) + i eta pi delta(v·l)` from the complete
  path/convention tuple. It rejects a caller-supplied sign.
- `DistributionalPoleEvaluator`: separately evaluates the PV-plus-cut
  distribution and a direct finite-epsilon refinement sequence. Epsilon is
  numerical metadata and is excluded from physical identity.

## Resolvent and cuts

- `LFResolventTerm`: typed initial/intermediate light-front energies, pole,
  vertices, operator, cut support, spectrum rule, and regulator.
- `IntermediateStateCut`: distinguishes eikonal and LF-energy cuts.
- `CutLedger`: requires explicit `DISTINCT`, `EQUIVALENT_COUNT_ONCE`, or
  `SUBTRACTED` relations. Floating-point equality is never a provenance key.

## Kernel and antiunitary map

- `PilotKernelInput`: binds the C3 `SpinorOAMState`, positive-x active
  quark/antiquark identity, fundamental path, resolvent, cut ledger, and
  deterministic validation parameters.
- `OneGluonPilotKernel`: first-order fundamental rescattering and a restricted
  three-attachment Ward check. It exposes the explicit SU(3) factor
  `C_F=4/3`; its adjoint algebraic guard uses `C_A=3`.
- `AntiunitaryLinkReversal`: complex conjugation, endpoint/path inversion,
  momentum reversal, LF-helicity phases, color conjugation, ordered-link
  transformation, and projection identity. Link-even/odd combinations cannot
  be formed from raw arrays.

## Reductions, status, and provenance

- `PilotProjector`: a typed `RED` map. `SIVERS_LIKE_PILOT` probes target
  transverse spin; `BOER_MULDERS_LIKE_PILOT` probes active-quark transverse
  spin. They are not production `f1Tperp` or `h1perp`.
- `PhaseBudget`: records the calculated unsubtracted phase separately from
  unresolved soft, rapidity, UV, Glauber/process, and remainder terms.
- `C5ResultEnvelope`: deterministic status/provenance wrapper with fail-closed
  production, Volume IV, and Volume V gates.
- `color_algebra_report`: verifies fundamental/adjoint Casimirs and independent
  antisymmetric `f` and symmetric `d` tensors without claiming an active-gluon
  T-odd result.

The public objects round-trip through their `to_dict()` representations; all
complex values serialize as ordered `[real, imaginary]` pairs.
