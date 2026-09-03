from deuteron_wigner.bridge.free2 import core as c


def test_c128_authority():
    r = c.verify_free_m2_authority()
    assert r["positive_gate"] is True
    assert r["route_f_a_route_f_b_mismatches"] == 0
    assert r["L_cancellation"] == 0
    assert r["P_plus_cancellation"] == 0
    assert r["C127_values_consumed"] == 0


def test_c128_entries_and_actions():
    for r in c.RESOLUTIONS:
        assert c.free_sparse_matrix(r)["dense_allocated"] is False
        assert c.free_entry(r, 0, 0)["expression"] == "m_q^2"
        assert c.free_entry(r, 0, 6)["status"] == "EXACT_ZERO_WITH_OPERATOR_PROOF"
        assert c.free_entry(r, 6, 6)["certified_bound"] is not None
        assert c.cross_sector_zero_certificate(r)["status"] == "EXACT_ZERO_WITH_OPERATOR_PROOF"
        assert c.cm_separation_certificate(r)["CM_excited_leakage"] == "0"


def test_c128_mutations():
    for i in range(384):
        assert c.mutate_live_free2(i)["positive_gate"] is False
