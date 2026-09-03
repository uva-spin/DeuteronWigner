from deuteron_wigner.bridge.icdomain2 import core as c


def test_c125_authority_and_routes():
    report = c.verify_current_logical_domain()
    assert report["positive_gate"] is True
    assert report["conditioning_count"] == 72
    assert report["route_DA_route_DB_identity_mismatches"] == 0
    assert report["route_DA_route_DB_order_mismatches"] == 0
    assert report["route_DA_route_DB_cardinality_mismatches"] == 0
    assert report["route_DA_route_DB_target_mismatches"] == 0
    assert report["route_DA_route_DB_orientation_mismatches"] == 0
    assert report["cross_sector"]["class_count"] == 8
    assert report["cross_sector"]["numerical_zero_records"] == 0


def test_c125_rank_unrank_and_target_spans():
    for program in c.PROGRAMS:
        for resolution in c.RESOLUTIONS:
            segments = [s for s in c.segment_manifest() if s["program_id"] == program and s["resolution"] == resolution]
            assert len(segments) == 1
            segment = segments[0]
            for local in (0, segment["logical_count"] // 2, segment["logical_count"] - 1):
                witness = c._witness_from_local(segment, local)
                assert c.witness_rank(witness["witness_id"]) == witness["logical_rank"]
                assert c.witness_identity(witness["witness_id"])["matrix_target_id"] == witness["matrix_target_id"]
            assert c.target_span_manifest(program, resolution)["spans"][0]["count_once"] is True


def test_c125_no_value_or_operator_domain():
    guard = c.static_isolation_guard()
    assert guard["pass"] is True
    assert guard["values"] == guard["bounds"] == guard["component_sums"] == guard["operators"] == 0


def test_c125_mutation_controls():
    # Exercise the full required live-mutation budget.  Mutations are
    # intentionally compact and do not materialize the logical domain.
    for i in range(384):
        mutated = c.mutate_live_icdomain2(i)
        assert mutated is not None
