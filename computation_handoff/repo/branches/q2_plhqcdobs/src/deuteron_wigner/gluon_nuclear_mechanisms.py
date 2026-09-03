"""Correlator-level non-impulse mechanisms for spin-1 gluon structure."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping

import numpy as np

from .gluon_correlator import DELTA_T, EPSILON_T, transverse_matrix_parts
from .nuclear_mechanisms import (
    AntishadowingInput,
    DiffractiveShadowingInput,
    NuclearCorrectionParameters,
    default_diffractive_shadowing_input,
    longitudinal_coherence_factor,
)
from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)
from .spin import project_matrix, spin_one_basis

Spin1GluonArray = np.ndarray
GluonComponent = Callable[
    [Spin1GluonArray, Spin1GluonArray, float, float], Spin1GluonArray
]

MECHANISM_LABELS: Mapping[str, Mechanism] = {
    "coherent_shadowing": Mechanism.COHERENT,
    "antishadowing": Mechanism.COHERENT,
    "off_shell": Mechanism.OFF_SHELL,
    "meson_exchange": Mechanism.MESON_EXCHANGE,
    "non_nucleonic": Mechanism.NON_NUCLEONIC,
}


def _validated_correlator(values: Spin1GluonArray, name: str) -> np.ndarray:
    array = np.asarray(values, dtype=np.complex128)
    if array.shape != (3, 3, 2, 2):
        raise ValueError(f"{name} gluon correlator must have shape (3,3,2,2)")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} gluon correlator must be finite")
    if not np.allclose(
        array, array.transpose(1, 0, 3, 2).conj(), atol=1.0e-11, rtol=0
    ):
        raise ValueError(f"{name} gluon correlator must be Hermitian")
    return array


@dataclass(frozen=True)
class AdditionalGluonNuclearComponentInput:
    """One sourced full-matrix gluon nuclear contribution."""

    component: GluonComponent
    source: str
    evidence: EvidenceClass
    mechanism: Mechanism
    validity: ValidityDomain
    uncertainty_description: str
    assumptions: tuple[str, ...] = ()
    uncertainty_components: Mapping[str, GluonComponent] | None = None

    def __post_init__(self) -> None:
        if not self.source or not self.uncertainty_description:
            raise ValueError("gluon component requires source and uncertainty")
        if self.uncertainty_components is not None and any(
            not name for name in self.uncertainty_components
        ):
            raise ValueError("uncertainty member names cannot be empty")

    def value(
        self,
        proton: Spin1GluonArray,
        neutron: Spin1GluonArray,
        x: float,
        scale_gev: float,
    ) -> np.ndarray:
        if not self.validity.contains(x=x, q_gev=scale_gev):
            return np.zeros((3, 3, 2, 2), dtype=np.complex128)
        return _validated_correlator(
            self.component(proton, neutron, x, scale_gev), "mechanism"
        )

    def member_values(
        self,
        proton: Spin1GluonArray,
        neutron: Spin1GluonArray,
        x: float,
        scale_gev: float,
    ) -> Mapping[str, np.ndarray]:
        if not self.validity.contains(x=x, q_gev=scale_gev):
            return {
                name: np.zeros((3, 3, 2, 2), dtype=np.complex128)
                for name in (self.uncertainty_components or {})
            }
        return {
            name: _validated_correlator(
                component(proton, neutron, x, scale_gev),
                f"mechanism uncertainty member {name}",
            )
            for name, component in (self.uncertainty_components or {}).items()
        }


@dataclass(frozen=True)
class MechanismResolvedGluonCorrelator:
    proton_impulse: Spin1GluonArray
    neutron_impulse: Spin1GluonArray
    corrections: Mapping[str, Spin1GluonArray]
    provenance: Mapping[str, ComponentProvenance]
    uncertainty_corrections: Mapping[str, Mapping[str, Spin1GluonArray]]

    def __post_init__(self) -> None:
        _validated_correlator(self.proton_impulse, "proton impulse")
        _validated_correlator(self.neutron_impulse, "neutron impulse")
        if set(self.corrections) != set(MECHANISM_LABELS):
            raise ValueError("gluon correction ledger has missing or extra mechanisms")
        if set(self.provenance) != set(MECHANISM_LABELS):
            raise ValueError("gluon provenance ledger must match corrections")
        if set(self.uncertainty_corrections) != set(MECHANISM_LABELS):
            raise ValueError("gluon uncertainty ledger must match corrections")
        for label, values in self.corrections.items():
            _validated_correlator(values, label)
        for label, members in self.uncertainty_corrections.items():
            for name, values in members.items():
                _validated_correlator(values, f"{label} member {name}")

    @property
    def impulse(self) -> np.ndarray:
        return np.asarray(self.proton_impulse) + np.asarray(self.neutron_impulse)

    @property
    def total(self) -> np.ndarray:
        return self.impulse + sum(
            self.corrections.values(),
            np.zeros((3, 3, 2, 2), dtype=np.complex128),
        )


def build_inclusive_gluon_shadowing_input(
    *,
    diffractive_input: DiffractiveShadowingInput | None = None,
    parameters: NuclearCorrectionParameters = NuclearCorrectionParameters(),
) -> AdditionalGluonNuclearComponentInput:
    """Build the constrained inclusive U/trace gluon shadowing term.

    Inclusive diffractive information constrains neither target-polarized
    sectors nor circular/linear gluon polarization. Those components are
    therefore left unchanged rather than assigned the quark response.
    """

    diffractive = diffractive_input or default_diffractive_shadowing_input()
    target_u = spin_one_basis()["U"]

    def make_component(
        fraction: Callable[[str, float, float], float]
    ) -> GluonComponent:
        def component(
            proton: np.ndarray, neutron: np.ndarray, x: float, scale_gev: float
        ) -> np.ndarray:
            impulse = _validated_correlator(
                proton, "proton"
            ) + _validated_correlator(neutron, "neutron")
            strength = float(fraction("gluon", x, scale_gev))
            if not np.isfinite(strength) or strength < 0.0:
                raise ValueError(
                    "diffractive gluon uncertainty response must be nonnegative"
                )
            if diffractive.applies_longitudinal_coherence:
                strength *= longitudinal_coherence_factor(
                    x,
                    nucleon_mass_gev=parameters.nucleon_mass_gev,
                    radius_fm=parameters.deuteron_coherence_radius_fm,
                )
            # Coefficient of the target-U matrix for every transverse index.
            target_u_gluon = np.asarray(
                [
                    [
                        project_matrix(impulse[:, :, i, j], target_u)
                        for j in range(2)
                    ]
                    for i in range(2)
                ],
                dtype=np.complex128,
            )
            trace, _, _ = transverse_matrix_parts(target_u_gluon)
            return -strength * np.einsum(
                "IH,ij->IHij", target_u, trace * DELTA_T
            )

        return component

    return AdditionalGluonNuclearComponentInput(
        component=make_component(diffractive.fraction),
        source=diffractive.source,
        evidence=diffractive.classification,
        mechanism=Mechanism.COHERENT,
        validity=ValidityDomain(
            1.0e-4,
            parameters.shadowing_x_max,
            2.0,
            100.0,
            1.5,
            "inclusive diffractive gluon shadowing",
        ),
        uncertainty_description=(
            f"diffractive relative uncertainty "
            f"{diffractive.relative_uncertainty:g}; polarized gluon and "
            "target-spin responses unresolved"
        ),
        assumptions=(
            "inclusive DPDF response applies only to target-U/gluon-trace",
            "Gaussian longitudinal coherence when not included by input",
        ),
        uncertainty_components={
            name: make_component(member)
            for name, member in (
                diffractive.uncertainty_members or {}
            ).items()
        },
    )


def build_polarized_tensor_gluon_shadowing_input(
    *,
    diffractive_input: DiffractiveShadowingInput | None = None,
    parameters: NuclearCorrectionParameters = NuclearCorrectionParameters(),
    target_group_ratios: Mapping[str, float] | None = None,
    gluon_polarization_ratios: Mapping[str, float] | None = None,
) -> AdditionalGluonNuclearComponentInput:
    """Build a replaceable irreducible-response gluon shadowing model.

    The inclusive diffractive gluon fraction anchors only U/trace.  Every
    other target and gluon-polarization response is an explicit, independently
    configurable model ratio.  This prevents an inclusive constraint from
    being silently copied into helicity, linear, vector-target, or
    tensor-target sectors.
    """

    diffractive = diffractive_input or default_diffractive_shadowing_input()
    target_ratios = dict(
        target_group_ratios
        or {"U": 1.0, "L": 0.65, "T": 0.65, "LL": 1.35, "LT": 1.0, "TT": 1.0}
    )
    gluon_ratios = dict(
        gluon_polarization_ratios
        or {"trace": 1.0, "circular": 0.65, "linear": 0.80}
    )
    if set(target_ratios) != {"U", "L", "T", "LL", "LT", "TT"}:
        raise ValueError("target ratios must cover U,L,T,LL,LT,TT")
    if set(gluon_ratios) != {"trace", "circular", "linear"}:
        raise ValueError("gluon ratios must cover trace,circular,linear")
    if any(
        not np.isfinite(value)
        for value in (*target_ratios.values(), *gluon_ratios.values())
    ):
        raise ValueError("gluon shadowing response ratios must be finite")

    basis = spin_one_basis()

    def target_group(label: str) -> str:
        if label.startswith("T_"):
            return "T"
        if label.startswith("LT_"):
            return "LT"
        if label.startswith("TT_"):
            return "TT"
        return label

    def make_component(
        fraction: Callable[[str, float, float], float]
    ) -> GluonComponent:
        def component(
            proton: np.ndarray, neutron: np.ndarray, x: float, scale_gev: float
        ) -> np.ndarray:
            impulse = _validated_correlator(proton, "proton") + _validated_correlator(
                neutron, "neutron"
            )
            strength = float(fraction("gluon", x, scale_gev))
            if not np.isfinite(strength) or strength < 0.0:
                raise ValueError("diffractive gluon response must be nonnegative")
            if diffractive.applies_longitudinal_coherence:
                strength *= longitudinal_coherence_factor(
                    x,
                    nucleon_mass_gev=parameters.nucleon_mass_gev,
                    radius_fm=parameters.deuteron_coherence_radius_fm,
                )
            correction = np.zeros((3, 3, 2, 2), dtype=np.complex128)
            for label, target_tensor in basis.items():
                projected = np.asarray(
                    [
                        [
                            project_matrix(impulse[:, :, i, j], target_tensor)
                            for j in range(2)
                        ]
                        for i in range(2)
                    ],
                    dtype=np.complex128,
                )
                trace, circular, linear = transverse_matrix_parts(projected)
                transverse_response = (
                    gluon_ratios["trace"] * trace * DELTA_T
                    + gluon_ratios["circular"] * circular * (1j * EPSILON_T)
                    + gluon_ratios["linear"] * linear
                )
                correction -= (
                    strength
                    * target_ratios[target_group(label)]
                    * np.einsum("IH,ij->IHij", target_tensor, transverse_response)
                )
            return correction

        return component

    return AdditionalGluonNuclearComponentInput(
        component=make_component(diffractive.fraction),
        source=(
            f"{diffractive.source}; polarized/tensor irreducible-response "
            "extension with explicit target and gluon-polarization ratios"
        ),
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.COHERENT,
        validity=ValidityDomain(
            1.0e-4,
            parameters.shadowing_x_max,
            2.0,
            100.0,
            1.5,
            "polarized and tensor gluon shadowing response model",
        ),
        uncertainty_description=(
            "inclusive U/trace anchor plus independent target U,L,T,LL,LT,TT "
            "and gluon trace/circular/linear response scenarios"
        ),
        assumptions=(
            "inclusive diffraction fixes only the U/trace normalization",
            "default polarized and tensor response ratios are model dependent",
            "Gaussian longitudinal coherence when not included by input",
        ),
        uncertainty_components={
            name: make_component(member)
            for name, member in (diffractive.uncertainty_members or {}).items()
        },
    )


def build_inclusive_gluon_antishadowing_input(
    antishadowing_input: AntishadowingInput,
) -> AdditionalGluonNuclearComponentInput:
    """Apply a momentum-compensating gluon enhancement only to U/trace."""

    target_u = spin_one_basis()["U"]

    def component(
        proton: np.ndarray, neutron: np.ndarray, x: float, scale_gev: float
    ) -> np.ndarray:
        impulse = _validated_correlator(proton, "proton") + _validated_correlator(
            neutron, "neutron"
        )
        strength = antishadowing_input.value(x, scale_gev)
        target_u_gluon = np.asarray(
            [
                [
                    project_matrix(impulse[:, :, i, j], target_u)
                    for j in range(2)
                ]
                for i in range(2)
            ],
            dtype=np.complex128,
        )
        trace, _, _ = transverse_matrix_parts(target_u_gluon)
        return float(strength) * np.einsum(
            "IH,ij->IHij", target_u, trace * DELTA_T
        )

    return AdditionalGluonNuclearComponentInput(
        component=component,
        source=antishadowing_input.source,
        evidence=EvidenceClass.PHENOMENOLOGY,
        mechanism=Mechanism.COHERENT,
        validity=ValidityDomain(
            0.06, 0.25, 1.3, 100.0, 1.5,
            "momentum-compensating inclusive gluon antishadowing",
        ),
        uncertainty_description=(
            f"relative uncertainty {antishadowing_input.relative_uncertainty:g}; "
            f"restores fraction {antishadowing_input.compensation_fraction:g} "
            "of configured gluon shadowing momentum"
        ),
        assumptions=(
            "enhancement normalization supplied by explicit gluon momentum sum",
            "inclusive response applies only to target-U/gluon-trace",
        ),
    )


def apply_gluon_nuclear_mechanisms(
    *,
    proton_impulse: Spin1GluonArray,
    neutron_impulse: Spin1GluonArray,
    x: float,
    scale_gev: float,
    inputs: Mapping[str, AdditionalGluonNuclearComponentInput] | None = None,
) -> MechanismResolvedGluonCorrelator:
    """Compose named gluon mechanisms without implicit quark-sector reuse."""

    if not 0.0 < x <= 1.0 or scale_gev <= 0.0:
        raise ValueError("x and scale must be physical")
    proton = _validated_correlator(proton_impulse, "proton impulse")
    neutron = _validated_correlator(neutron_impulse, "neutron impulse")
    configured = dict(inputs or {})
    unknown = set(configured) - set(MECHANISM_LABELS)
    if unknown:
        raise ValueError(f"unknown gluon mechanisms: {sorted(unknown)}")
    for label, source in configured.items():
        if source.mechanism != MECHANISM_LABELS[label]:
            raise ValueError(f"{label} input has inconsistent mechanism identity")

    zero = np.zeros((3, 3, 2, 2), dtype=np.complex128)
    corrections = {
        label: (
            zero.copy()
            if label not in configured
            else configured[label].value(proton, neutron, x, scale_gev)
        )
        for label in MECHANISM_LABELS
    }
    uncertainty_corrections = {
        label: (
            {}
            if label not in configured
            else configured[label].member_values(
                proton, neutron, x, scale_gev
            )
        )
        for label in MECHANISM_LABELS
    }
    common_validity = ValidityDomain(1.0e-4, 0.9, 1.3, 100.0, 1.5)
    provenance = {}
    for label, mechanism in MECHANISM_LABELS.items():
        source = configured.get(label)
        provenance[label] = ComponentProvenance(
            name=f"gluon {label.replace('_', ' ')} contribution",
            evidence=EvidenceClass.UNCONSTRAINED if source is None else source.evidence,
            mechanism=mechanism,
            sources=(
                f"inactive: no sourced {label} gluon input configured",
            ) if source is None else (source.source,),
            assumptions=(
                "zero is configuration state, not physical absence",
            ) if source is None else source.assumptions,
            validity=common_validity if source is None else source.validity,
            uncertainty_kind=(
                "unconstrained parameter/component; source-required activation"
                if source is None
                else source.uncertainty_description
            ),
            replaceable_interface="AdditionalGluonNuclearComponentInput",
        )
    return MechanismResolvedGluonCorrelator(
        proton, neutron, corrections, provenance, uncertainty_corrections
    )
