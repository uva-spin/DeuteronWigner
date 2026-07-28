from pathlib import Path

import numpy as np
import pandas as pd


TABLE = Path(
    "outputs/parent_tmds/gluon_av18_canonical_lfwf_todd.csv"
)
MATRICES = TABLE.with_name(f"{TABLE.stem}.correlators.csv")
T_ODD = {
    "h1Lperp", "f1Tperp", "h1", "h1Tperp", "g1LT", "g1TT",
}
ALL_TMD = {
    "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
    "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
    "h1LTperp", "f1TT_minus_h1TTperp", "g1TT", "h1TT",
    "h1TTperpperp",
}


def test_canonical_table_is_complete_flavor_color_link_and_wave_resolved():
    frame = pd.read_csv(TABLE)
    assert set(frame.tmd) == ALL_TMD
    assert frame.k_GeV.nunique() == 31
    assert set(frame.color_structure) == {
        "f_type_antisymmetric", "d_type_symmetric",
    }
    assert set(frame.gauge_link) == {"[+,+]", "[-,-]", "[+,-]", "[-,+]"}
    assert set(frame.mechanism) == {
        "proton_impulse", "neutron_impulse", "impulse_total",
        "wave_SS", "wave_SD", "wave_DS", "wave_DD",
        "coherent_shadowing", "antishadowing", "off_shell",
        "meson_exchange", "non_nucleonic", "model_total",
    }
    assert np.isfinite(
        frame[["F_GeV-2", "physical_ratio_to_f1"]].to_numpy()
    ).all()
    assert (
        frame.loc[frame.mechanism.eq("impulse_total"),
                  "symmetry_projection_residual"].max()
        < 1.0e-2
    )


def test_all_todd_functions_are_generated_and_reverse_with_the_staple():
    frame = pd.read_csv(TABLE)
    total = frame[
        frame.mechanism.eq("impulse_total") & frame.tmd.isin(T_ODD)
    ]
    nonzero = total.groupby("tmd")["F_GeV-2"].apply(
        lambda values: np.any(np.abs(values) > 1.0e-14)
    )
    assert set(nonzero.index) == T_ODD
    assert nonzero.all()
    pairs = (
        ("f_type_antisymmetric", "[+,+]", "[-,-]"),
        ("d_type_symmetric", "[+,-]", "[-,+]"),
    )
    for color, future, past in pairs:
        left = total[
            total.color_structure.eq(color) & total.gauge_link.eq(future)
        ]
        right = total[
            total.color_structure.eq(color) & total.gauge_link.eq(past)
        ]
        joined = left.merge(right, on=["k_GeV", "tmd"], suffixes=("_f", "_p"))
        assert np.allclose(
            joined["F_GeV-2_f"], -joined["F_GeV-2_p"],
            rtol=1.0e-7, atol=5.0e-12,
        )


def test_wave_component_closure_and_rank_weighted_sizes_are_natural():
    frame = pd.read_csv(TABLE)
    for _, block in frame.groupby(["color_structure", "gauge_link"]):
        values = block.pivot_table(
            index=["k_GeV", "tmd"],
            columns="mechanism",
            values="F_GeV-2",
        )
        wave_sum = (
            values.wave_SS + values.wave_SD
            + values.wave_DS + values.wave_DD
        )
        assert np.allclose(values.impulse_total, wave_sum, atol=3.0e-12)
        mechanism_sum = (
            values.impulse_total + values.coherent_shadowing
            + values.antishadowing + values.off_shell
            + values.meson_exchange + values.non_nucleonic
        )
        assert np.allclose(values.model_total, mechanism_sum, atol=3.0e-12)
    assert (
        frame.loc[frame.mechanism.eq("antishadowing"), "F_GeV-2"].abs().max()
        > 0.0
    )
    assert (
        frame.loc[frame.mechanism.eq("meson_exchange"), "F_GeV-2"].abs().max()
        > 0.0
    )
    total = frame[
        frame.mechanism.eq("impulse_total") & frame.tmd.isin(T_ODD)
    ]
    # High-rank TMD coefficients can be large near kT=0; the correlator
    # contains the dimensionless rank-weighted combination tested here.
    assert total.physical_ratio_to_f1.abs().max() < 0.05
    tensor = total[total.tmd.isin({"g1LT", "g1TT"})]
    assert tensor.physical_ratio_to_f1.abs().max() < 1.0e-3


def test_exported_parent_matrices_are_complete_hermitian_and_positive():
    frame = pd.read_csv(MATRICES)
    keys = ["color_structure", "gauge_link", "k_GeV"]
    assert (frame.groupby([*keys, "mechanism"]).size() == 36).all()
    for _, block in frame.groupby([*keys, "mechanism"]):
        matrix = np.zeros((6, 6), dtype=complex)
        for row in block.itertuples():
            left = int(row.target_out) * 2 + int(row.gluon_out)
            right = int(row.target_in) * 2 + int(row.gluon_in)
            matrix[left, right] = complex(row.real, row.imag)
        assert np.allclose(matrix, matrix.conj().T, atol=1.0e-12)
        # Additive response/counterterm blocks are signed corrections and
        # are not density matrices by themselves. Positivity applies to the
        # complete retained impulse and composed totals.
        mechanism = str(block["mechanism"].iloc[0])
        if mechanism in {"impulse_total", "model_total"}:
            assert np.linalg.eigvalsh(matrix)[0] >= -1.0e-10
