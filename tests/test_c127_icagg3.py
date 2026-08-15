from deuteron_wigner.bridge.icagg3 import core as c


def test_c127_authority():
    r = c.verify_instantaneous_current_authority()
    assert r["positive_gate"] is True
    assert r["components_terminal"] == 8
    assert r["logical_witnesses"] == 474533910576
    assert r["census_mismatches"] == 0
    assert r["target_level_scale_cancellations"] == 0


def test_c127_entry_and_factorized_actions():
    for product in c.PRODUCTS:
        for sector in c.SECTORS:
            for resolution in c.RESOLUTIONS:
                e = c.component_entry(product, sector, resolution, 0, 0)
                assert e["status"] == "AVAILABLE_SOURCE_QUALIFIED"
                assert e["certified_bound"] is not None
                assert c.target_aggregation_certificate(product, sector, resolution, 0, 0)["status"] == "CLOSED"
                assert c.component_sparse_matrix(product, sector, resolution)["dense_allocated"] is False


def test_c127_isolation_and_mutations():
    assert c.static_isolation_guard()["pass"] is True
    for i in range(384):
        assert c.mutate_live_icagg3(i) is not None
