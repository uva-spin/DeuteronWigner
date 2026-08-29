"""Common all-named-TMD controlled-limit audit through parent machinery."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from .gluon_nuclear_mechanisms import apply_gluon_nuclear_mechanisms
from .gtmd import GaugeLink
from .gtmd_convolution import OffForwardSpinQuadrature
from .light_front import (
    LFNormalization,
    SpinRotation,
    off_forward_active_component_densities,
)
from .nuclear_mechanisms import (
    AntishadowingInput,
    DiffractiveShadowingInput,
    NuclearCorrectionParameters,
    apply_nuclear_corrections,
)
from .nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    NUCLEON_QUARK_TMD_NAMES,
    NucleonTMDComponent,
)
from .parent_quark_tmd import (
    convolve_spin1_quark_correlator,
    convolve_spin1_quark_wave_components,
    project_parent_derived_quark_tmds,
)
from .quark_correlator import SPIN1_QUARK_TMD_NAMES
from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


@dataclass(frozen=True)
class ControlledLimitCheck:
    name: str
    maximum_absolute_residual: float
    tolerance: float
    passed: bool
    compared_named_tmds: int
    statement: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "maximum_absolute_residual",
            float(self.maximum_absolute_residual),
        )
        object.__setattr__(self, "tolerance", float(self.tolerance))
        object.__setattr__(self, "passed", bool(self.passed))


def _model(factor: float) -> FlavorResolvedNucleonQuarkModel:
    provenance = ComponentProvenance(
        name="controlled-limit complete nucleon fixture",
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.NUCLEON_IMPULSE,
        sources=("analytic all-18 test boundary",),
        assumptions=("distinct deterministic amplitude for every named TMD",),
        validity=ValidityDomain(0.01, 0.9, 1.0, 10.0, 2.0),
        uncertainty_kind="exact controlled fixture parameters",
        replaceable_interface="FlavorResolvedNucleonQuarkModel",
    )
    widths = {2: 0.23, 1: 0.31, -2: 0.27, -1: 0.35}
    components = {}
    for index, name in enumerate(NUCLEON_QUARK_TMD_NAMES):
        components[name] = NucleonTMDComponent(
            value=lambda flavor, x, q, i=index: (
                factor * (i + 1) * (1.0 + 0.03 * flavor) * (1.0 - x)
            ),
            width_gev2=widths,
            provenance=provenance,
        )
    return FlavorResolvedNucleonQuarkModel(components, 0.93891897)


def _single_node_components(
    spin_rotation: SpinRotation,
) -> dict[str, OffForwardSpinQuadrature]:
    densities = off_forward_active_component_densities(
        y=0.5,
        p_x=0.0,
        p_y=0.0,
        delta_x=0.0,
        delta_y=0.0,
        mass=0.93891897,
        radial=lambda k: (1.0, 0.0),
        normalization=LFNormalization.FLAT,
        spin_rotation=spin_rotation,
    )
    common = dict(
        y=np.asarray((0.5,)),
        p_x=np.asarray((0.0,)),
        p_y=np.asarray((0.0,)),
        weights=np.asarray((1.0,)),
        delta_x=0.0,
        delta_y=0.0,
    )
    return {
        label: OffForwardSpinQuadrature(
            **common, spectral=np.asarray((density,))
        )
        for label, density in densities.items()
    }


def _project(result) -> dict[str, dict[str, float]]:
    return project_parent_derived_quark_tmds(
        result,
        k_x_gev=0.31,
        k_y_gev=-0.17,
        deuteron_mass_gev=1.87561294257,
    )


def _dictionary_residual(
    left: dict[str, float], right: dict[str, float]
) -> float:
    if set(left) != set(SPIN1_QUARK_TMD_NAMES) or set(right) != set(
        SPIN1_QUARK_TMD_NAMES
    ):
        raise ValueError("controlled limit must compare the complete 18-TMD basis")
    return max(abs(left[name] - right[name]) for name in left)


def run_controlled_limit_audit(
    tolerance: float = 2.0e-11,
) -> tuple[ControlledLimitCheck, ...]:
    proton, neutron, zero = _model(1.0), _model(0.37), _model(0.0)
    melosh = _single_node_components(SpinRotation.MELOSH)
    identity = _single_node_components(SpinRotation.IDENTITY)
    arguments = dict(
        x=0.2,
        k_x=0.31,
        k_y=-0.17,
        scale=5.0,
        flavor=2,
        gauge_link=GaugeLink("+", "+"),
        momentum_unit_to_gev=1.0,
    )

    free_proton = convolve_spin1_quark_correlator(
        **arguments,
        proton=proton,
        neutron=zero,
        quadrature=melosh["SS"],
    )
    free_neutron = convolve_spin1_quark_correlator(
        **arguments,
        proton=zero,
        neutron=neutron,
        quadrature=melosh["SS"],
    )
    projected_p = _project(free_proton)
    projected_n = _project(free_neutron)

    wave = convolve_spin1_quark_wave_components(
        **arguments,
        proton=proton,
        neutron=neutron,
        quadratures=melosh,
    )
    ss_projection = _project(wave["SS"])["total"]
    zero_d_residual = max(
        max(
            np.max(np.abs(component.vector)),
            np.max(np.abs(component.axial)),
            np.max(np.abs(component.transverse)),
        )
        for label in ("SD", "DS", "DD")
        for component in (wave[label].total,)
    )

    melosh_parent = convolve_spin1_quark_correlator(
        **arguments,
        proton=proton,
        neutron=neutron,
        quadrature=melosh["SS"],
    )
    identity_parent = convolve_spin1_quark_correlator(
        **arguments,
        proton=proton,
        neutron=neutron,
        quadrature=identity["SS"],
    )
    melosh_residual = _dictionary_residual(
        _project(melosh_parent)["total"], _project(identity_parent)["total"]
    )

    zero_fraction = DiffractiveShadowingInput(
        fraction=lambda sector, x, q: 0.0,
        source="exact controlled zero",
        relative_uncertainty=0.0,
        classification=EvidenceClass.EXACT,
        applies_longitudinal_coherence=False,
    )
    zero_antishadowing = AntishadowingInput(
        enhancement=lambda x, q: 0.0,
        source="exact controlled zero",
        relative_uncertainty=0.0,
        compensation_fraction=0.0,
        lost_momentum=0.0,
        restored_momentum=0.0,
    )
    zero_corrected = apply_nuclear_corrections(
        proton_impulse=melosh_parent.proton,
        neutron_impulse=melosh_parent.neutron,
        x=0.2,
        scale_gev=5.0,
        parameters=NuclearCorrectionParameters(
            average_nucleon_virtuality=0.0
        ),
        diffractive_input=zero_fraction,
        antishadowing_input=zero_antishadowing,
    )
    quark_zero_residual = max(
        max(
            np.max(np.abs(item.vector)),
            np.max(np.abs(item.axial)),
            np.max(np.abs(item.transverse)),
        )
        for item in zero_corrected.corrections.values()
    )

    gluon_fixture = np.einsum(
        "IH,ij->IHij",
        np.eye(3, dtype=np.complex128),
        np.eye(2, dtype=np.complex128),
    )
    gluon_zero = apply_gluon_nuclear_mechanisms(
        proton_impulse=gluon_fixture,
        neutron_impulse=0.4 * gluon_fixture,
        x=0.2,
        scale_gev=5.0,
    )
    gluon_zero_residual = max(
        np.max(np.abs(item)) for item in gluon_zero.corrections.values()
    )

    checks = (
        ControlledLimitCheck(
            "free_proton_switch",
            _dictionary_residual(projected_p["total"], projected_p["proton"]),
            tolerance,
            False,
            len(SPIN1_QUARK_TMD_NAMES),
            "zero neutron input makes every parent TMD equal the retained proton term",
        ),
        ControlledLimitCheck(
            "free_neutron_switch",
            _dictionary_residual(projected_n["total"], projected_n["neutron"]),
            tolerance,
            False,
            len(SPIN1_QUARK_TMD_NAMES),
            "zero proton input makes every parent TMD equal the retained neutron term",
        ),
        ControlledLimitCheck(
            "pure_s_zero_d",
            zero_d_residual,
            tolerance,
            False,
            len(ss_projection),
            "pure-S radial input makes SD, DS, and DD parent correlators vanish",
        ),
        ControlledLimitCheck(
            "no_melosh_at_rest",
            melosh_residual,
            tolerance,
            False,
            len(SPIN1_QUARK_TMD_NAMES),
            "at y=1/2 and pT=0 the Melosh rotations reduce to identity",
        ),
        ControlledLimitCheck(
            "zero_quark_nuclear_corrections",
            quark_zero_residual,
            tolerance,
            False,
            len(SPIN1_QUARK_TMD_NAMES),
            "zero mechanism inputs leave the complete quark parent unchanged",
        ),
        ControlledLimitCheck(
            "zero_gluon_nuclear_corrections",
            gluon_zero_residual,
            tolerance,
            False,
            18,
            "empty gluon mechanism ledger leaves the complete gluon parent unchanged",
        ),
    )
    return tuple(
        ControlledLimitCheck(
            **{
                **asdict(check),
                "passed": check.maximum_absolute_residual <= check.tolerance,
            }
        )
        for check in checks
    )
