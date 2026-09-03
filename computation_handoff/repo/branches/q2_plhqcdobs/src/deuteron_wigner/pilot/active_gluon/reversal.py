"""Complete pilot antiunitary reversal for an ordered adjoint link pair."""

from __future__ import annotations

from dataclasses import dataclass

from ...formal.diagnostics import ArchitectureError
from .color import ColorChannel
from .identity import ActiveGluonOperatorId
from .parent import GluonPolarizationView


@dataclass(frozen=True)
class ActiveGluonProjectedAmplitude:
    value: complex
    operator_id: ActiveGluonOperatorId
    color_channel: ColorChannel
    polarization: GluonPolarizationView
    cut_id: str
    state_member_id: str


@dataclass(frozen=True)
class OrderedPairAntiunitaryReversal:
    stable_id: str = "C6:REV:FULL_ORDERED_PAIR_THETA"
    complex_conjugation: bool = True
    momentum_fiber_exchange: bool = True
    target_helicity_phase: str = "SPIN1_THETA_V1"
    gluon_helicity_phase: str = "GLUON_THETA_V1"
    transverse_momentum_reversal: bool = True
    transfer_reversal: bool = True
    endpoint_exchange: bool = True
    path_inversion: bool = True
    color_ordering_transform: bool = True
    tensor_index_transform: bool = True

    def __post_init__(self) -> None:
        booleans = (
            self.complex_conjugation, self.momentum_fiber_exchange,
            self.transverse_momentum_reversal, self.transfer_reversal,
            self.endpoint_exchange, self.path_inversion,
            self.color_ordering_transform, self.tensor_index_transform,
        )
        if not all(booleans) or not self.target_helicity_phase or not self.gluon_helicity_phase:
            raise ArchitectureError("C6.REV.1", "incomplete ordered-pair antiunitary map", expected="all path/color/spin/momentum/tensor actions", received=self)

    def transform_operator(self, operator: ActiveGluonOperatorId) -> ActiveGluonOperatorId:
        return ActiveGluonOperatorId(
            operator.link_pair.antiunitary_pair(),
            operator.source_state_member_id,
            operator.field_strength_left_index,
            operator.field_strength_right_index,
            operator.active_species, operator.color_status,
            operator.rapidity_regulator_id, operator.soft_route_id,
            operator.operator_scheme_status, operator.wilson_order,
            operator.stable_id + ":THETA",
        )

    def map_partner(
        self, partner: ActiveGluonProjectedAmplitude,
        reference: ActiveGluonProjectedAmplitude,
    ) -> ActiveGluonProjectedAmplitude:
        expected = self.transform_operator(reference.operator_id).link_pair.orientation_word
        if partner.operator_id.link_pair.orientation_word != expected:
            raise ArchitectureError("C6.REV.2", "link-pair partner does not match derived antiunitary identity", expected=expected, received=partner.operator_id.link_pair.orientation_word)
        if partner.color_channel != reference.color_channel or partner.polarization != reference.polarization:
            raise ArchitectureError("C6.REV.4", "color or polarization identity was lost under reversal", expected=(reference.color_channel, reference.polarization), received=(partner.color_channel, partner.polarization))
        return ActiveGluonProjectedAmplitude(
            partner.value, reference.operator_id, partner.color_channel,
            partner.polarization, partner.cut_id, partner.state_member_id,
        )

    def even_odd(
        self, reference: ActiveGluonProjectedAmplitude,
        partner: ActiveGluonProjectedAmplitude,
    ) -> tuple[complex, complex]:
        mapped = self.map_partner(partner, reference)
        return ((reference.value + mapped.value) / 2, (reference.value - mapped.value) / 2)
