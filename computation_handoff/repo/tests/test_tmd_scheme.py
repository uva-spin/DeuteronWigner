import pytest

from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    MatchedGluonTMD,
)
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    OneLoopGluonCSSEvolution,
)
from deuteron_wigner.tmd_scheme import (
    DELTA_COLLINS_ZETA_SCHEME,
    TMDScheme,
    TMDScalePoint,
)


def test_scale_point_requires_physical_scales_and_identifies_canonical_line():
    point = TMDScalePoint.canonical(5.0)
    assert point.zeta_gev2 == 25.0
    assert point.is_canonical()
    assert not TMDScalePoint(5.0, 20.0).is_canonical()
    for args in ((0.0, 1.0), (1.0, 0.0), (float("nan"), 1.0)):
        with pytest.raises(ValueError, match="finite"):
            TMDScalePoint(*args)


def test_scheme_refuses_unsupported_rapidity_path():
    with pytest.raises(ValueError, match="canonical"):
        DELTA_COLLINS_ZETA_SCHEME.require_supported_path(
            TMDScalePoint(2.0, 3.0), TMDScalePoint.canonical(5.0)
        )


def test_evolution_refuses_mismatched_soft_or_uv_scheme():
    alternate = TMDScheme(
        soft_subtraction=DELTA_COLLINS_ZETA_SCHEME.soft_subtraction,
        rapidity_regulator=DELTA_COLLINS_ZETA_SCHEME.rapidity_regulator,
        rapidity_prescription=DELTA_COLLINS_ZETA_SCHEME.rapidity_prescription,
        uv_scheme="test-non-MSbar",
        source="controlled incompatibility fixture",
    )
    boundary = MatchedGluonTMD(
        lambda x, q: 1.0,
        lambda q: 0.25,
        config=GluonTMDMatchingConfig(scheme=alternate),
    )
    evolution = OneLoopGluonCSSEvolution(
        lambda q: 0.25,
        GluonCSSEvolutionConfig(scheme=DELTA_COLLINS_ZETA_SCHEME),
    )
    with pytest.raises(ValueError, match="incompatible"):
        EvolvedMatchedGluonTMD(boundary, evolution)


def test_evolved_values_expose_actual_mu_and_zeta_endpoints():
    model = EvolvedMatchedGluonTMD(
        MatchedGluonTMD(lambda x, q: 2.0, lambda q: 0.25),
        OneLoopGluonCSSEvolution(lambda q: 0.25),
    )
    values = model.values(0.2, 1.0, 5.0)
    assert values.initial_zeta_gev2 == pytest.approx(values.initial_scale**2)
    assert values.final_zeta_gev2 == pytest.approx(25.0)
    metadata = model.metadata
    assert (
        metadata["boundary"]["scheme"]
        == metadata["evolution"]["scheme"]
    )

