"""C180 full-mode ordered finite-HO path-scheme tests."""

from deuteron_wigner.bridge import hqcdb0reslinkscheme1 as c


def test_contract_freeze_and_status():
    authority = c.verify_hqcd_b0reslinkscheme1_authority()
    assert authority["baseline"] == "d8991371414259c977a6a1e413478ffafbdd7918"
    assert authority["contract_sha256"] == "714a2f1ad8784155660f524e1e2513a32cb4ce591a4ed78b0257a50ebc7f7da3"
    assert authority["C179_package_root"] == "7cc1089eb36fffac5240666b7e6b03bf5bf3feca6a422c6644689f218fa836d2"
    assert authority["new_source_acquisitions"] == 0
    assert authority["C176_boundary_rebuilt"] == 0
    assert c.PLAN == "B0RESLINKSCHEME1-H"


def test_full_vector_modes_and_reversible_pairs():
    assert c.VECTOR_DIMENSIONS == {"K9": 72, "K11": 110, "K13": 156}
    for resolution, dimension in c.VECTOR_DIMENSIONS.items():
        for rank in (0, dimension // 2, dimension - 1):
            mode = c.unrank_vector_mode(resolution, rank)
            assert c.rank_vector_mode(mode) == rank
        assert c.ordered_pair_manifest(resolution_id=resolution)["rows"][0]["ordered_pair_count"] == dimension * dimension
        for rank in (0, dimension * dimension - 1):
            pair = c.unrank_ordered_pair(resolution, rank)
            assert c.rank_ordered_pair(pair) == rank
            assert pair["symmetrized"] is False


def test_safe_programs_degree_and_shuffle():
    schema = c.path_program_schema()["row"]
    assert schema["schema_id"] == "FINITE_HO_PATH_SIGNATURE_PROGRAM_V1"
    assert schema["eval"] is False and schema["dynamic_import"] is False
    assert len(c.degree1_manifest()["rows"]) == 2028
    assert c.path_program_manifest(degree=2)["summary"]["degree2_factorized_full_mode_count"] == 249720
    assert all(row["symmetrized"] is False for row in c.degree2_manifest(resolution_id="K9", ordered_pair_id=c.unrank_ordered_pair("K9", 0)["ordered_pair_id"])["rows"])
    assert all(row["status"] == "SHUFFLE_IDENTITY_CLOSED_SYMBOLIC" for row in c.shuffle_manifest()["rows"])


def test_reference_holdouts_conversion_and_boundary():
    assert c.reference_scheme_certificate()["row"]["scheme_id"] == c.PROJECT_REPRESENTATIVE
    assert c.alternative_holdout_manifest()["rows"]
    assert all(row["status"] == "C180_ALTERNATIVE_CONVERSION_PARTIAL_BOUNDARY_REFINEMENT" for row in c.conversion_manifest()["rows"])
    owners = c.boundary_ownership_manifest()
    assert owners["C176_recomputed"] is False
    assert all(row["finite_HO_leakage_threshold_pruned"] is False for row in owners["rows"])
    assert c.b0reslinkscheme1_completeness_certificate()["boundary_ownership_complete"] is False


def test_requests_loader_and_mutations():
    assert c.load_verified_hqcd_b0reslinkscheme1_authority()["package_root"] == c.PACKAGE_ROOT
    requests = c.request_resolution_manifest()
    assert requests["all_six_visible"] is True
    assert requests["active_count"] == 2
    assert c.static_isolation_guard()["pass"] is True
    for index in range(384):
        row = c.mutate_live_hqcdb0reslinkscheme1(index)
        assert row["positive_gate"] is False
        assert row["must_fail_or_change_root"] is True
