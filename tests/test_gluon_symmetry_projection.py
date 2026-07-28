import numpy as np

from deuteron_wigner.gluon_correlator import (
    compose_spin1_gluon_correlator,
    project_to_allowed_spin1_gluon_basis,
)


NAMES = (
    "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
    "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
    "h1LTperp", "f1TT_minus_h1TTperp", "g1TT", "h1TT",
    "h1TTperpperp",
)


def test_allowed_basis_projection_round_trips_all_coefficients():
    source = {name: 0.03*(index-7) for index, name in enumerate(NAMES)}
    parent = compose_spin1_gluon_correlator((0.41, 0.17), 1.876, source)
    projected, recovered, residual = project_to_allowed_spin1_gluon_basis(
        parent.values, (0.41, 0.17), 1.876
    )
    assert residual < 1e-13
    assert np.allclose(projected.values, parent.values, atol=1e-12)
    assert all(np.isclose(recovered[name], source[name]) for name in NAMES)


def test_forbidden_longitudinal_trace_is_removed_and_reported():
    source = {name: 0.0 for name in NAMES}
    source["f1"] = 2.0
    parent = compose_spin1_gluon_correlator((0.4, 0.2), 1.876, source)
    contaminated = parent.values.copy()
    contaminated[0, 0] += 0.01*np.eye(2)
    contaminated[2, 2] -= 0.01*np.eye(2)
    projected, _, residual = project_to_allowed_spin1_gluon_basis(
        contaminated, (0.4, 0.2), 1.876
    )
    assert residual > 0.0
    assert residual < 0.02
    assert np.allclose(projected.values, parent.values, atol=1e-12)
