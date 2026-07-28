from pathlib import Path

import numpy as np
import pandas as pd


TABLE = Path("outputs/parent_tmds/gluon_todd_two_stage_predictions.csv")
MATRIX = TABLE.with_name(f"{TABLE.stem}.correlators.csv")


def test_prediction_table_is_dense_complete_and_link_resolved():
    frame = pd.read_csv(TABLE)
    assert set(frame.tmd) == {
        "h1Lperp", "f1Tperp", "h1", "h1Tperp", "g1LT", "g1TT"
    }
    assert frame.k_GeV.nunique() == 61
    assert set(frame.color_structure) == {
        "f_type_antisymmetric", "d_type_symmetric"
    }
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]", "[+,-]", "[-,+]"}
    assert np.isfinite(frame["F_GeV-2"]).all()
    nonzero = frame[frame.k_GeV.gt(0)].groupby("tmd")["F_GeV-2"].apply(
        lambda values: np.any(np.abs(values) > 0)
    )
    assert nonzero.all()
    assert frame.minimum_eigenvalue.min() >= -1e-10


def test_production_correlators_are_complete_hermitian_matrices():
    frame = pd.read_csv(MATRIX)
    key = [
        "scenario", "color_structure", "gauge_link", "k_GeV"
    ]
    assert (frame.groupby(key).size() == 36).all()
    for _, group in frame.groupby(key):
        matrix = np.zeros((6, 6), dtype=complex)
        for row in group.itertuples():
            left = int(row.target_out) * 2 + int(row.gluon_out)
            right = int(row.target_in) * 2 + int(row.gluon_in)
            matrix[left, right] = complex(row.real, row.imag)
        assert np.allclose(matrix, matrix.conj().T, atol=1e-11)
        assert np.linalg.eigvalsh(matrix)[0] >= -1e-10
