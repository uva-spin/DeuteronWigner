"""C181 first-omitted-shell boundary ownership tests."""

from deuteron_wigner.bridge import hqcdb0hoboundary3 as c


def test_contract_plan_and_domain():
    authority = c.verify_hqcd_b0hoboundary3_authority()
    assert authority["baseline"] == "1c952f135f47fca9b10de5647e62fe59a2cdbaa0"
    assert authority["contract_sha256"] == "92a4f86ea466ed58fb3a4a903dd4232189820019c67412d95c992d3ed7fa4fff"
    assert authority["C180_package_root_verified"] is True
    assert authority["C180_report_sha256"] == authority["C180_report_sha256_expected"]
    assert c.PLAN == "HOBOUNDARY3-B"
    assert c.FACTOR_DIMENSIONS == {"K9": 90, "K11": 132, "K13": 182}
    assert c.BOUNDARY_COUNTS == {"K9": 16, "K11": 20, "K13": 24}
    assert c.LEAKAGE_ENTRY_COUNTS == {"K9": 16, "K11": 20, "K13": 24}
    assert c.LEAKAGE_RANKS == {"K9": 8, "K11": 10, "K13": 12}


def test_boundary_modes_map_and_divergence():
    for resolution in c.RESOLUTIONS:
        rows = c.boundary_mode_manifest(resolution)["rows"]
        assert len(rows) == c.BOUNDARY_COUNTS[resolution]
        assert c.rank_boundary_mode(c.unrank_boundary_mode(resolution, len(rows) - 1)) == len(rows) - 1
        leak = c.leakage_map_manifest(resolution)["rows"]
        assert len(leak) == c.LEAKAGE_ENTRY_COUNTS[resolution]
        assert all(row["threshold_pruned"] is False for row in leak)
        assert len(c.boundary_divergence_manifest(resolution)["rows"]) == len(leak)
        action = c.apply_leakage_map(resolution, {})
        assert action["omitted_space_materialized"] is False
        assert c.apply_boundary_divergence(resolution, {})["C176_defect_separate"] is True


def test_programs_reconstruction_and_mixed_classes():
    assert c.boundary_program_schema()["row"]["eval"] is False
    assert len(c.boundary_degree1_manifest()["rows"]) == 360
    recon = c.linearized_reconstruction_manifest()
    assert len(recon["rows"]) == (36 + 55 + 78) * 3
    assert all(row["status"] == "LINEARIZED_ENDPOINT_RECONSTRUCTION_EXACT" for row in recon["rows"])
    cards = c.mixed_pair_manifest()["cardinalities"]
    assert cards["K9"]["PQ"] == cards["K9"]["QP"] == 1152
    assert cards["K9"]["QQ"] == 256
    assert c.mixed_degree2_manifest()["rows"][0]["symmetrized"] is False
    assert c.symmetric_ownership_manifest()["rows"][0]["status"] == "SYMMETRIC_DEGREE2_PATH_DIFFERENCE_EXACTLY_BOUNDARY_OWNED"
    assert c.order_sensitive_manifest()["rows"][0]["status"] == "ORDER_SENSITIVE_SOURCE_SCOPE_REMAINDER_NONZERO"


def test_release_requests_loader_and_mutations():
    assert c.b0_release_manifest()["row"]["decision"] == "B0_LINEARIZED_AND_SYMMETRIC_BOUNDARY_OWNERSHIP_READY_NONABELIAN_SOURCE_SCOPE_EXPLICIT"
    req = c.request_resolution_manifest()
    assert req["all_six_visible"] is True and req["active_count"] == 2
    assert c.load_verified_hqcd_b0hoboundary3_authority()["package_root"] == c.PACKAGE_ROOT
    assert c.static_isolation_guard()["pass"] is True
    for index in range(384):
        mutation = c.mutate_live_hqcdb0hoboundary3(index)
        assert mutation["positive_gate"] is False
        assert mutation["must_fail_or_change_root"] is True
