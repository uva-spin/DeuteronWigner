"""C171 B=0 adjoint domain and fail-closed boundary tests."""

from deuteron_wigner.bridge import hqcdb0adjoint1 as c


def test_authority_freeze_and_prompt_only_provenance():
    authority = c.verify_hqcd_b0adjoint1_authority()
    assert authority["baseline"] == "db7b994ce0e00fd992360c1c477ac1bda1ea6d1c"
    assert authority["C170_package_root"] == c.C170_PACKAGE_ROOT
    assert authority["expected_contract_present"] is False
    assert c.capsule_freeze()["count"] == 8
    assert len(c.capsule_freeze()["B0_rows"]) == 4
    assert len(c.capsule_freeze()["B1_rows"]) == 4


def test_integer_resolution_and_color_multiplicities():
    rows = c.b0_resolution_manifest()["rows"]
    assert [row["total_quantum"] for row in rows] == [9, 11, 13]
    assert all(row["total_type"] == "INTEGER" for row in rows)
    assert all(row["fermion_boundary"] == "ANTIPERIODIC" for row in rows)
    assert all(row["gluon_boundary"] == "PERIODIC" for row in rows)
    qq, gg = c.qqbar_color_manifest(), c.gg_color_manifest()
    assert qq["outer_multiplicity"] == 1
    assert gg["outer_multiplicity"] == 2
    assert max(qq["generator_residuals"]) < 1e-12
    assert max(gg["generator_residuals"]) < 1e-12
    assert gg["exchange"]["d_symmetric"] == 0.0
    assert gg["exchange"]["f_antisymmetric"] == 0.0


def test_basis_round_trip_and_scope_separation():
    for sector in c.ACTIVE_B0[1:]:
        for resolution in c.RESOLUTIONS:
            row = c.unrank_sector_state(sector, resolution, 0)
            assert c.rank_sector_state(sector, row) == 0
    assert c.gluon_source_crosswalk_manifest()["direct_vacuum_sources_invented"] == 0
    assert c.b0_statistics_manifest()["gg"]["channels"] == ("symmetric_d", "antisymmetric_f")
    assert c.b0_zero_boundary_residual_manifest()["missing_as_zero"] == 0
    assert c.b0_ghost_gauge_manifest()["target_MOMq_ghosts_imported"] is False
    assert c.static_isolation_guard()["pass"] is True


def test_free_operator_is_symbolic_and_no_dense_inverse():
    manifest = c.b0_free_operator_manifest("C170-B0-QQBAR-ADJOINT", "K9")
    row = manifest["rows"][0]
    assert row["sparse"] is True and row["matrix_free"] is True
    assert row["dense_full_inverse"] is False
    state = c.unrank_sector_state("C170-B0-QQBAR-ADJOINT", "K9", 0)
    out = c.apply_b0_free_operator("C170-B0-QQBAR-ADJOINT", "K9", (1.0,) * row["dimension"])
    assert out["status"] == "SYMBOLIC_ONLY"
    assert len(out["symbolic_diagonal"]) == row["dimension"]
    assert c.b0_sector_resolvent_manifest()["rows"][0]["dense_full_inverse"] is False
    assert state["CM_intrinsic"] == "CM_GROUND"


def test_live_mutations_fail_closed():
    for index in range(384):
        mutation = c.mutate_live_hqcdb0adjoint1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
