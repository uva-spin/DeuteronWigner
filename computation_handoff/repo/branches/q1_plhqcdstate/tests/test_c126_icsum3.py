from deuteron_wigner.bridge.icsum3 import core as c


def test_c126_authority():
    r = c.verify_current_witness_value_authority()
    assert r["positive_gate"] is True
    assert r["segments"] == 24 and r["logical_witnesses"] == 474533910576
    assert r["route_VA_route_VB_identity_mismatches"] == 0
    assert r["expression_mismatches"] == 0
    assert r["bound_program_mismatches"] == 0


def test_c126_value_lookup_and_target_span():
    for p in c.c125.PROGRAMS:
        for res in c.c125.RESOLUTIONS:
            v = c.witness_value_by_rank(p, res, 0)
            assert v["central_value"] is not None and v["certified_bound"] is not None
            assert v["units"]["pminus"] == "GeV/g_s^2"
            assert c.witness_value_by_id(v["witness_id"])["value_record_root"] == v["value_record_root"]
            assert c.matrix_target_value_span_manifest(p, res)["component_sums"] == 0


def test_c126_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        assert c.mutate_live_icsum3(i) is not None
