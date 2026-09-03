"""Matched and CSS-evolved spin-half gluon boundary for nuclear convolution."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .fourier import gluon_tmd_b_to_k
from .gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from .pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from .tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)
from .tmd_models import InterpolatedSpinHalfGluonGTMD


@dataclass(frozen=True)
class EvolvedGluonBoundaryConfig:
    """Numerical and scheme choices for the tabulated nucleon boundary."""

    scale_GeV: float = 5.0
    x_min: float = 0.05
    x_points: int = 20
    b_max_GeV_inverse: float = 8.0
    b_points: int = 241
    k_max_GeV: float = 5.0
    k_points: int = 121
    intrinsic_profile: LargeBProfile = LargeBProfile.CENTRAL
    cs_profile: NonperturbativeCSProfile = NonperturbativeCSProfile.CENTRAL

    def __post_init__(self) -> None:
        if self.scale_GeV <= 0.0:
            raise ValueError("scale must be positive")
        if not 0.0 < self.x_min < 1.0:
            raise ValueError("x_min must lie in (0,1)")
        if min(self.x_points, self.b_points, self.k_points) < 3:
            raise ValueError("all interpolation grids require at least 3 points")
        if self.b_max_GeV_inverse <= 0.0 or self.k_max_GeV <= 0.0:
            raise ValueError("b and k maxima must be positive")


@dataclass(frozen=True)
class EvolvedGluonBoundary:
    """Callable boundary plus complete provenance for replacement/auditing."""

    model: InterpolatedSpinHalfGluonGTMD
    metadata: dict[str, object]


def build_evolved_gluon_boundary(
    unpolarized: LHAPDFProvider,
    polarized: PolarizedLHAPDFProvider,
    *,
    config: EvolvedGluonBoundaryConfig = EvolvedGluonBoundaryConfig(),
    momentum_unit_to_GeV: float = 1.0,
    nucleon_mass_GeV: float = 0.93891897,
) -> EvolvedGluonBoundary:
    """Build the production nucleon boundary from matching and CSS evolution.

    The result is a strict interpolator: nuclear convolution points outside
    the declared ``x`` or ``k_T`` domain fail rather than extrapolate
    silently.
    """

    matching_config = GluonTMDMatchingConfig(
        profile=config.intrinsic_profile
    )
    boundary = MatchedGluonTMD(
        unpolarized.gluon,
        unpolarized.alpha_s,
        helicity_gluon_pdf=polarized.gluon,
        quark_singlet_pdf=unpolarized.quark_singlet,
        config=matching_config,
    )
    evolution_config = GluonCSSEvolutionConfig(
        cs_profile=config.cs_profile
    )
    evolved = EvolvedMatchedGluonTMD(
        boundary,
        OneLoopGluonCSSEvolution(unpolarized.alpha_s, evolution_config),
    )
    x_axis = np.concatenate(
        (np.geomspace(config.x_min, 0.9, config.x_points - 1), (1.0,))
    )
    b_axis = np.linspace(0.0, config.b_max_GeV_inverse, config.b_points)
    k_axis = np.linspace(0.0, config.k_max_GeV, config.k_points)
    tables = {
        name: np.empty((len(x_axis), len(k_axis)), dtype=np.float64)
        for name in ("f1", "g1", "h1perp")
    }
    for index, x in enumerate(x_axis):
        values = [
            evolved.values(float(x), float(b), config.scale_GeV)
            for b in b_axis
        ]
        transformed = gluon_tmd_b_to_k(
            b_axis,
            np.asarray([value.f1 for value in values]),
            np.asarray([value.g1 for value in values]),
            np.asarray([value.h1perp for value in values]),
            k_axis,
            nucleon_mass=nucleon_mass_GeV,
        )
        tables["f1"][index] = transformed.f1.real
        tables["g1"][index] = transformed.g1.real
        tables["h1perp"][index] = transformed.h1perp.real
    model = InterpolatedSpinHalfGluonGTMD(
        x_axis=x_axis,
        k_axis_GeV=k_axis,
        f1=tables["f1"],
        g1=tables["g1"],
        h1perp=tables["h1perp"],
        nucleon_mass_GeV=nucleon_mass_GeV,
        momentum_unit_to_GeV=momentum_unit_to_GeV,
    )
    return EvolvedGluonBoundary(
        model=model,
        metadata={
            **evolved.metadata,
            "classification": "phenomenology plus perturbative matching/evolution",
            "unpolarized_PDF": unpolarized.set_name,
            "polarized_PDF": polarized.set_name,
            "scale_GeV": config.scale_GeV,
            "intrinsic_profile": config.intrinsic_profile.value,
            "CS_profile": config.cs_profile.value,
            "x_grid": [float(x_axis[0]), float(x_axis[-1]), len(x_axis)],
            "b_grid_GeV_inverse": [
                float(b_axis[0]), float(b_axis[-1]), len(b_axis)
            ],
            "k_grid_GeV": [
                float(k_axis[0]), float(k_axis[-1]), len(k_axis)
            ],
            "strict_no_extrapolation": True,
            "spin_half_content": ["f1g", "g1g", "h1perpg"],
            "missing_spin_half_content": [
                "Sivers and other gauge-link-odd gluon structures",
                "nucleon transverse-spin gluon structures",
            ],
        },
    )
