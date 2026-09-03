import numpy as np
import pandas as pd
import pytest

from deuteron_wigner.correlator_io import (
    TabulatedQuarkCorrelatorProvider,
    deserialize_gluon_correlator,
    deserialize_quark_correlator,
    gluon_correlator_rows,
    quark_correlator_rows,
)
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator


def _hermitian(rng, size):
    values = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    return values + values.conj().T


def test_quark_long_table_round_trip():
    rng = np.random.default_rng(17)
    source = Spin1QuarkCorrelator(
        _hermitian(rng, 3),
        _hermitian(rng, 3),
        np.stack((_hermitian(rng, 3), _hermitian(rng, 3))),
    )
    rows = quark_correlator_rows(source, {"mechanism": "test"})
    restored = deserialize_quark_correlator(pd.DataFrame(rows))
    np.testing.assert_array_equal(restored.vector, source.vector)
    np.testing.assert_array_equal(restored.axial, source.axial)
    np.testing.assert_array_equal(restored.transverse, source.transverse)


def test_tabulated_quark_provider_interpolates_full_hermitian_parent():
    rows = []
    for x in (0.1, 0.3, 0.6):
        source = Spin1QuarkCorrelator(
            np.diag([x, 2.0 * x, 3.0 * x]),
            np.diag([x**2, -x**2, 0.5 * x**2]),
            np.stack((
                np.diag([1.0 + x, 2.0 + x, 3.0 + x]),
                np.diag([-x, 0.0, x]),
            )),
        )
        rows.extend(quark_correlator_rows(
            source, {"x_N": x, "Q_GeV": 5.0}
        ))
    provider = TabulatedQuarkCorrelatorProvider.from_frame(
        pd.DataFrame(rows), scale_gev=5.0, parton_sector="valence"
    )
    at_node = provider(0.3, 5.0, "valence")
    np.testing.assert_allclose(at_node.vector, np.diag([0.3, 0.6, 0.9]))
    middle = provider(0.2, 5.0, "valence")
    assert middle.is_target_hermitian()
    assert 0.1 < middle.vector[0, 0].real < 0.3
    outside = provider(0.8, 5.0, "valence")
    np.testing.assert_array_equal(outside.vector, np.zeros((3, 3)))


def test_tabulated_quark_provider_rejects_scale_and_sector_mismatch():
    values = np.zeros((2, 4, 3, 3), dtype=np.complex128)
    provider = TabulatedQuarkCorrelatorProvider(
        np.array([0.1, 0.2]), values, 5.0, "sea"
    )
    with pytest.raises(ValueError, match="scale"):
        provider(0.15, 4.0, "sea")
    with pytest.raises(ValueError, match="sector"):
        provider(0.15, 5.0, "valence")


def test_gluon_long_table_round_trip():
    rng = np.random.default_rng(23)
    joint = _hermitian(rng, 6)
    source = joint.reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
    rows = gluon_correlator_rows(source, {"mechanism": "test"})
    restored = deserialize_gluon_correlator(pd.DataFrame(rows))
    np.testing.assert_array_equal(restored, source)


def test_deserializer_rejects_missing_entry():
    source = Spin1QuarkCorrelator(
        np.eye(3), np.eye(3), np.zeros((2, 3, 3))
    )
    rows = quark_correlator_rows(source, {"mechanism": "test"})
    with pytest.raises(ValueError, match="requires 36 entries"):
        deserialize_quark_correlator(pd.DataFrame(rows[:-1]))
