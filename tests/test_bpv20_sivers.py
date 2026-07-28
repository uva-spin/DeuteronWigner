from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.bpv20_sivers import (
    ARTEMIDE_CONSTANTS_PATH,
    ARTEMIDE_HARPY_PATH,
    BPV20ArtemideSivers,
    BPV20ReplicaMomentumGrid,
    BPV20ReplicaEnsemble,
)


def test_official_release_has_complete_500_replica_ensemble():
    fit = BPV20ReplicaEnsemble.load()
    assert fit.replicas.shape == (500, 14)
    np.testing.assert_array_equal(fit.technical_initial, fit.central)
    np.testing.assert_allclose(
        fit.central,
        [
            0.5362, 5.21724, 202.749, 0.0, 0.0, -0.01661, -0.35169,
            -3.90804, 0.37263, -0.70153, 8.97236, 0.75803, 2.46253,
            -0.47481,
        ],
        rtol=0.0,
        atol=0.0,
    )


def test_boundary_is_flavor_resolved_and_matches_fortran_fixture():
    fit = BPV20ReplicaEnsemble.load()
    values = {flavor: fit.boundary_shape(flavor, 0.1, 1.0) for flavor in (2, 1, -2, -1, 3)}
    np.testing.assert_allclose(
        [values[2], values[1], values[-2], values[-1], values[3]],
        [-0.27496193449393025, 0.3118649856922840, -0.01239225152858857,
         -0.01239225152858857, 0.019784120861430873],
        rtol=2.0e-13,
    )
    assert values[2] != values[1]
    assert values[-2] == values[-1]  # an explicit fit assumption, not u=d.


def test_boundary_profile_and_regulator_limits():
    fit = BPV20ReplicaEnsemble.load()
    assert fit.boundary_shape(2, 0.1, 0.0) != 0.0
    assert abs(fit.boundary_shape(2, 0.1, 5.0)) < abs(
        fit.boundary_shape(2, 0.1, 0.0)
    )
    assert fit.boundary_shape(21, 0.1, 1.0) == 0.0
    assert fit.b_star(0.0) == 0.0
    assert fit.b_star(1.0) < 1.0
    assert fit.mu_ope_gev(1.0e-6) == 1000.0


def test_parser_rejects_incomplete_replica_release(tmp_path: Path):
    source = tmp_path / "bad.rep"
    source.write_text("*C\n500\n*D\n-1," + ",".join(["0"] * 14) + "\n")
    with pytest.raises(ValueError, match="technical members"):
        BPV20ReplicaEnsemble.load(source)


@pytest.mark.skipif(
    not ARTEMIDE_CONSTANTS_PATH.exists()
    or not any(ARTEMIDE_HARPY_PATH.glob("artemide*.so")),
    reason="optional compiled arTeMiDe reference is not prepared",
)
def test_compiled_reference_evolution_and_nucleon_adapter():
    reference = BPV20ArtemideSivers()
    np.testing.assert_allclose(
        [
            reference.proton_value(flavor, 0.1, 0.5, 5.0)
            for flavor in (2, 1, -2, -1, 3)
        ],
        [-0.12820395309283922, 0.14541039679030607, -0.005778020279824971,
         -0.005778020279824971, 0.009224558692352150],
        rtol=3.0e-12,
    )
    fitted = reference.fitted_input()
    # Exact charge symmetry maps neutron u to proton d but does not identify
    # proton u and d.
    assert fitted.value("neutron", 2, 0.1, 0.5, 5.0) == pytest.approx(
        fitted.value("proton", 1, 0.1, 0.5, 5.0)
    )
    assert fitted.value("proton", 2, 0.1, 0.5, 5.0) != pytest.approx(
        fitted.value("proton", 1, 0.1, 0.5, 5.0)
    )
    assert fitted.value("proton", 2, 0.005, 0.5, 5.0) == 0.0


@pytest.mark.skipif(
    not ARTEMIDE_CONSTANTS_PATH.exists()
    or not any(ARTEMIDE_HARPY_PATH.glob("artemide*.so")),
    reason="optional compiled arTeMiDe reference is not prepared",
)
def test_optimal_scheme_rejects_inert_scale_variations():
    reference = BPV20ArtemideSivers()
    nominal = reference.proton_value(2, 0.1, 0.5, 5.0)
    with pytest.raises(NotImplementedError, match="optimal-TMD"):
        reference.set_scale_variation(c1=2.0, c3=1.0)
    reference.set_scale_variation()
    restored = reference.proton_value(2, 0.1, 0.5, 5.0)
    assert restored == pytest.approx(nominal, rel=2.0e-12, abs=2.0e-12)


@pytest.mark.skipif(
    not ARTEMIDE_CONSTANTS_PATH.exists()
    or not any(ARTEMIDE_HARPY_PATH.glob("artemide*.so")),
    reason="optional compiled arTeMiDe reference is not prepared",
)
def test_vectorized_replica_hankel_transform_matches_artemide():
    reference = BPV20ArtemideSivers()
    grid = BPV20ReplicaMomentumGrid.generate(
        reference,
        q_gev=5.0,
        x_axis=np.asarray([0.05, 0.1, 0.2]),
        k_axis_gev=np.asarray([0.1, 0.5, 1.0]),
    )
    for flavor in (2, 1, -2):
        transformed = grid.interpolate_all(
            flavor, np.asarray([0.1]), np.asarray([0.5])
        )[0, 0]
        direct = reference.proton_value(flavor, 0.1, 0.5, 5.0, member=1)
        assert transformed == pytest.approx(direct, rel=2.0e-12, abs=2.0e-12)


@pytest.mark.skipif(
    not ARTEMIDE_CONSTANTS_PATH.exists()
    or not any(ARTEMIDE_HARPY_PATH.glob("artemide*.so")),
    reason="optional compiled arTeMiDe reference is not prepared",
)
def test_replica_grid_roundtrip(tmp_path):
    reference = BPV20ArtemideSivers()
    grid = BPV20ReplicaMomentumGrid.generate(
        reference,
        q_gev=5.0,
        x_axis=np.array([0.08, 0.1]),
        k_axis_gev=np.array([0.4, 0.5]),
    )
    path = tmp_path / "grid.npz"
    grid.save(path)
    restored = BPV20ReplicaMomentumGrid.load(path)
    assert restored.flavors == grid.flavors
    assert restored.q_gev == grid.q_gev
    assert restored.evaluator == grid.evaluator
    np.testing.assert_array_equal(restored.values, grid.values)
