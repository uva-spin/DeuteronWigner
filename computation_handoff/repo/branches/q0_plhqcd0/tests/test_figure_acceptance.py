import pandas as pd

from deuteron_wigner.figure_acceptance import (
    audit_ensemble_table,
    audit_flavor_traceability,
)


def test_parent_ensemble_tables_are_complete_and_bands_are_ordered():
    quark = pd.read_csv(
        "outputs/parent_tmds/ensemble/quark_parent_tmd_ensemble.csv"
    )
    gluon = pd.read_csv(
        "outputs/parent_tmds/ensemble/gluon_parent_tmd_ensemble.csv"
    )
    assert audit_ensemble_table(quark, "quark").passed
    assert audit_ensemble_table(gluon, "gluon").passed
    assert gluon.loc[gluon.k_GeV > 1.0, "factorization_valid"].eq(False).all()


def test_exact_isospin_total_does_not_erase_nucleon_flavor_sources():
    source = pd.read_csv("outputs/parent_tmds/quark_av18_fine.csv")
    audit = audit_flavor_traceability(source)
    assert audit["source_flavors"] == ["d", "dbar", "u", "ubar"]
    assert audit["mechanisms"] == ["neutron_impulse", "proton_impulse"]
    assert audit["flavor_resolved_before_assembly"]


def test_source_decomposition_atlas_table_covers_complete_quark_basis():
    table = pd.read_csv(
        "outputs/parent_tmds/ensemble/quark_flavor_source_decomposition.csv"
    )
    assert set(table["mechanism"]) == {
        "proton_impulse", "neutron_impulse", "impulse_total", "model_total"
    }
    assert table.groupby(
        ["flavor_label", "tmd", "target_channel"]
    ).ngroups == 72
    assert table.groupby(
        ["flavor_label", "tmd", "target_channel", "mechanism"]
    )["k_GeV"].nunique().eq(241).all()
