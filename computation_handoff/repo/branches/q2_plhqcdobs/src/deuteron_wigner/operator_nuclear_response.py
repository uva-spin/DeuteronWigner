"""Kinematic joint-spin nuclear response families for WP12."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np

from .canonical_parent_enrichment import (
    GluonJointSpinResponseMap,
    JointSpinResponseMap,
    gluon_polarized_tensor_response_map,
    joint_polarized_tensor_response_map,
)
from .gluon_correlator import Spin1GluonCorrelator
from .quark_correlator import Spin1QuarkCorrelator


class NuclearResponseMechanism(str, Enum):
    SHADOWING = "coherent_shadowing"
    ANTISHADOWING = "antishadowing"
    OFF_SHELL = "off_shell"
    MESONIC = "meson_exchange"
    SRC = "short_range_correlation"


@dataclass(frozen=True)
class NuclearResponseMember:
    label: str
    strength_scale: float
    correlation_group: str = "wp12_joint_nuclear_response"

    def __post_init__(self) -> None:
        if self.strength_scale < 0.0:
            raise ValueError("response strength scale cannot be negative")


MEMBERS = (
    NuclearResponseMember("weak", 0.65),
    NuclearResponseMember("central", 1.0),
    NuclearResponseMember("strong", 1.35),
)


def _base_strength(mechanism: NuclearResponseMechanism, x: float) -> float:
    if not 0.0 < x < 1.0:
        raise ValueError("nuclear response requires 0<x<1")
    if mechanism == NuclearResponseMechanism.SHADOWING:
        return 0.025 * np.exp(-0.5*(x/0.045)**2) if x < 0.1 else 0.0
    if mechanism == NuclearResponseMechanism.ANTISHADOWING:
        return 0.012 * np.exp(-0.5*((x-0.12)/0.045)**2)
    if mechanism == NuclearResponseMechanism.OFF_SHELL:
        return 0.018 * max(0.0, (x-0.25)/0.55)
    if mechanism == NuclearResponseMechanism.MESONIC:
        return 0.010 * np.exp(-0.5*((x-0.08)/0.06)**2)
    return 0.025 * max(0.0, (x-0.35)/0.45)


def quark_response_map(
    mechanism: NuclearResponseMechanism,
    x: float,
    member: NuclearResponseMember,
) -> JointSpinResponseMap:
    strength = member.strength_scale * _base_strength(mechanism, x)
    sign = 1.0 if mechanism in {
        NuclearResponseMechanism.ANTISHADOWING,
        NuclearResponseMechanism.MESONIC,
    } else -1.0
    u = 1.0 + sign*strength
    target_tensor = {
        NuclearResponseMechanism.SHADOWING: -0.55,
        NuclearResponseMechanism.ANTISHADOWING: 0.30,
        NuclearResponseMechanism.OFF_SHELL: -0.20,
        NuclearResponseMechanism.MESONIC: -0.80,
        NuclearResponseMechanism.SRC: 0.65,
    }[mechanism] * strength
    helicity = {
        NuclearResponseMechanism.SHADOWING: -0.20,
        NuclearResponseMechanism.ANTISHADOWING: 0.10,
        NuclearResponseMechanism.OFF_SHELL: -0.08,
        NuclearResponseMechanism.MESONIC: 0.0,
        NuclearResponseMechanism.SRC: 0.18,
    }[mechanism] * strength
    return joint_polarized_tensor_response_map(
        unpolarized_factor=u, target_vector=0.0,
        target_tensor=target_tensor, quark_helicity=helicity,
        label=f"{mechanism.value}:{member.label}",
    )


def gluon_response_map(
    mechanism: NuclearResponseMechanism,
    x: float,
    member: NuclearResponseMember,
) -> GluonJointSpinResponseMap:
    strength = member.strength_scale * _base_strength(mechanism, x)
    sign = 1.0 if mechanism in {
        NuclearResponseMechanism.ANTISHADOWING,
        NuclearResponseMechanism.MESONIC,
    } else -1.0
    # Gluon coherent response is expected to be stronger than the quark
    # response; the common member scales remain correlated.
    strength *= 1.35 if mechanism == NuclearResponseMechanism.SHADOWING else 1.0
    return gluon_polarized_tensor_response_map(
        unpolarized_factor=1.0 + sign*strength,
        target_vector=0.0,
        target_tensor=0.6*strength*sign,
        gluon_helicity=-0.18*strength,
        linear_polarization=0.12*strength,
        label=f"{mechanism.value}:{member.label}",
    )


def quark_response_correction(
    parent: Spin1QuarkCorrelator,
    mechanism: NuclearResponseMechanism,
    x: float,
    member: NuclearResponseMember,
) -> Spin1QuarkCorrelator:
    mapped = quark_response_map(mechanism, x, member).apply(parent)
    return Spin1QuarkCorrelator(
        mapped.vector-parent.vector, mapped.axial-parent.axial,
        mapped.transverse-parent.transverse,
    )


def gluon_response_correction(
    parent: Spin1GluonCorrelator,
    mechanism: NuclearResponseMechanism,
    x: float,
    member: NuclearResponseMember,
) -> Spin1GluonCorrelator:
    mapped = gluon_response_map(mechanism, x, member).apply(parent)
    return Spin1GluonCorrelator(mapped.values-parent.values)

