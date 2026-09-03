"""C170 finite-basis sector boundary tests."""
import pytest

from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c


def test_authority_plan_and_six_requests():
    authority = c.verify_hqcd_lfgsectorcalc1_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "LFGSECTORCALC1-D"
    assert authority["C169_package_root"] == "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5"
    assert c.request_resolution_manifest()["count"] == 6
    assert c.missing_calculation_freeze()["imported_unchanged"] is True


def test_descendant_crosswalk_and_taxonomy():
    crosswalk = c.descendant_resolution_manifest()
    assert crosswalk["count"] == 6
    assert sum(row["status"] == "EXACT_DESCENDANT_AUTHORITY_SUPERSEDES_HISTORICAL_BLOCKER" for row in crosswalk["rows"]) == 2
    assert c.sector_taxonomy_manifest()["count"] == 7
    assert c.b0_gluon_sector_manifest()["pure_B0_separate_from_C151_B1"] is True
    assert all(row["historical_baryonic_sector_reused"] is False for row in c.b1_higher_fock_manifest()["rows"])


def test_fail_closed_sector_and_nonzero_controls():
    assert c.color_representation_manifest("C170-B0-GG-ADJOINT")["rows"][0]["outer_multiplicity"] is None
    assert c.zero_boundary_residual_manifest()["missing_as_zero"] == 0
    assert c.count_once_manifest()["duplicate_count"] == 0
    assert c.ghost_gauge_manifest()["unproved_ghost_omissions"] == 6
    assert c.sector_diagnostic_manifest()["evaluations"] == 0
    assert c.static_isolation_guard()["pass"] is True
    with pytest.raises(KeyError):
        c.sector_taxonomy_manifest(sector_id="unknown")
    with pytest.raises(KeyError):
        c.factorized_basis_manifest(resolution_id="bad")
    with pytest.raises(ValueError):
        c.apply_free_sector_operator("C170-B0-GG-ADJOINT", "K9", ())


def test_orders_reload_and_384_live_mutations():
    assert c.dependency_frontier_manifest()["root"] == c.dependency_frontier_manifest()["root"]
    assert c.request_resolution_manifest()["root"] == c.request_resolution_manifest()["root"]
    for index in range(384):
        mutation = c.mutate_live_hqcdlfgsectorcalc1(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
