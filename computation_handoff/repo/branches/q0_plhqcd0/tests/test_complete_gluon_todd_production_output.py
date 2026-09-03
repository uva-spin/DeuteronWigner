from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gluon_todd import GLUON_TODD_RANKS


def test_complete_gluon_todd_production_is_rank_color_and_link_resolved():
    frame = pd.read_csv(
        Path("outputs/parent_tmds/complete_gluon_todd_multiplet.csv")
    )
    assert set(frame.tmd) == set(GLUON_TODD_RANKS)
    assert set(frame.color_structure) == {
        "f_type_antisymmetric",
        "d_type_symmetric",
    }
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]"}
    assert frame.scenario.nunique() == 3
    for keys, pair in frame.groupby(
        ["scenario", "color_structure", "tmd", "k_GeV"]
    ):
        assert len(pair) == 2, keys
        future = pair.loc[pair.gauge_link.eq("[+,+]"), "F_GeV-2"].iloc[0]
        past = pair.loc[pair.gauge_link.eq("[-,-]"), "F_GeV-2"].iloc[0]
        assert np.isclose(future, -past, atol=1e-13), keys
    nonzero = frame.loc[frame.k_GeV.gt(0.0)].groupby("tmd")["F_GeV-2"].apply(
        lambda values: np.any(np.abs(values) > 0.0)
    )
    assert nonzero.all()


def test_complete_gluon_todd_correlator_export_is_finite_and_hermitian():
    frame = pd.read_csv(
        Path(
            "outputs/parent_tmds/"
            "complete_gluon_todd_multiplet.correlators.csv"
        )
    )
    assert np.isfinite(frame[["real", "imag"]].to_numpy()).all()
    sample_keys = [
        "scenario",
        "color_structure",
        "gauge_link",
        "k_GeV",
    ]
    for _, block in frame.groupby(sample_keys):
        matrix = np.zeros((3, 3, 2, 2), dtype=complex)
        for row in block.itertuples():
            matrix[
                int(row.target_out),
                int(row.target_in),
                int(row.gluon_out),
                int(row.gluon_in),
            ] = row.real + 1j * row.imag
        adjoint = matrix.conj().transpose(1, 0, 3, 2)
        assert np.allclose(matrix, adjoint, atol=1e-12)
