from deuteron_wigner.bridge.gnorm import core as c


def test_c129_authority():
    r = c.verify_gluon_normal_ordering_authority()
    assert r["positive_gate"] is True
    assert r["descendants"] == 7
    assert r["taxonomy_unclassified"] == 0
    assert r["route_N_A_N_B_mismatches"] == 0
    assert r["C128_values_consumed"] == 0


def test_c129_statuses_and_interfaces():
    for d in c.DESCENDANTS:
        for r in c.RESOLUTIONS:
            s = c.descendant_status(d, r)
            assert s["full_source_status"]
            assert s["retained_status"]
            assert c.contraction_domain_manifest(d, r)["route_mismatches"] == 0
    assert c.descendant_entry("G4_SINGLE_CONTRACTION_BILINEAR", c.RESOLUTIONS[0], 6, 6)["coupling_degree"] == 2
    assert c.descendant_entry("G3_SINGLE_CONTRACTION_LINEAR", c.RESOLUTIONS[0], 0, 6)["status"] == c.ZERO
    assert c.descendant_sparse_matrix("G3_DIRECT_NORMAL_ORDERED", c.RESOLUTIONS[0])["matrix"] is False
    assert c.omitted_sector_interface_manifest()["represented_as_zero"] is False


def test_c129_mutations():
    for i in range(384):
        assert c.mutate_live_gnorm(i)["positive_gate"] is False
