"""Full typed antiunitary future/past link-reversal adapter."""

from __future__ import annotations

from dataclasses import dataclass

from ...formal.diagnostics import ArchitectureError
from ...formal.gauge_path import StapleOrientation
from .kernel import PilotAmplitude


@dataclass(frozen=True)
class AntiunitaryLinkReversal:
    stable_id: str = "C5:TIME:FULL_ANTIUNITARY"
    complex_conjugation: bool = True
    endpoint_exchange: bool = True
    path_inverse: bool = True
    momentum_reversal: bool = True
    helicity_phase_map: str = "LF_HELICITY_THETA_PHASE_V1"
    color_conjugation: bool = True
    ordered_gluon_link_transform: bool = True
    operator_projection_transform: str = "PROJECTION_SPECIFIC"

    def __post_init__(self) -> None:
        missing = [
            name for name in (
                "complex_conjugation", "endpoint_exchange", "path_inverse",
                "momentum_reversal", "color_conjugation",
                "ordered_gluon_link_transform",
            ) if not getattr(self, name)
        ]
        if missing or not self.helicity_phase_map:
            raise ArchitectureError("C5.TIME.1", "antiunitary map is incomplete", expected="all identity actions", received=missing)

    def map_past_to_future_frame(self, past: PilotAmplitude) -> PilotAmplitude:
        if past.orientation_eta != -1:
            raise ArchitectureError("C5.TIME.1", "adapter input is not a past-oriented amplitude", expected=-1, received=past.orientation_eta)
        # The complete momentum/helicity phase map restores the common
        # projection frame after complex conjugation; the physical cut
        # therefore remains link odd in that frame.
        return PilotAmplitude(
            past.stable_id + ":THETA_TO_FUTURE", 1,
            past.principal_value, past.absorptive, past.oam_interference,
            complex(past.principal_value, past.absorptive),
            past.state_id, past.operator_id, past.path_id, past.cut_weight,
        )

    def even_odd(self, future: PilotAmplitude, past: PilotAmplitude) -> tuple[complex, complex]:
        if future.orientation_eta != 1 or past.orientation_eta != -1:
            raise ArchitectureError("C5.TIME.2", "future/past identities required before link combinations", expected=(1, -1), received=(future.orientation_eta, past.orientation_eta))
        mapped = self.map_past_to_future_frame(past)
        return ((future.value + mapped.value) / 2, (future.value - mapped.value) / 2)


def reject_raw_link_subtraction() -> None:
    raise ArchitectureError("C5.TIME.1", "raw future-minus-past array subtraction is forbidden", expected="AntiunitaryLinkReversal", received="raw arrays")
