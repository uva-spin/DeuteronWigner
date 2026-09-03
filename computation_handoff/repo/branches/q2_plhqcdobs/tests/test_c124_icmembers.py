from deuteron_wigner.bridge.icmembers import *


def _key(domain="I2_density_projector", species="GLUON"):
    return {"resolution": RESOLUTIONS[0], "graph": domain, "species": species, "helicity": -1, "color": 0}


def test_c124_member_routes_and_projectors():
    out = verify_current_member_authority()
    assert out["status"] == STATUS
    assert len(out["domain_audits"]) == 24
    assert out["route_A_route_B_identity_mismatches"] == 0
    assert out["order_mismatches"] == 0
    assert out["cardinality_mismatches"] == 0
    assert out["weight_mismatches"] == 0
    assert out["orientation_mismatches"] == 0
    assert out["logical_witnesses"] == 0
    assert out["matrix_targets"] == 0
    assert out["positive_gate"]
    for domain in DOMAINS:
        p = projector_reproduction_certificate(domain, _key(domain))
        assert p["route_mismatches"] == 0
        assert p["status"] == "CLOSURE_CERTIFIED_SYMBOLIC_NO_NUMERICAL_VALUES"


def test_c124_member_rank_page_compatibility():
    d = member_domain_manifest(DOMAINS[0], _key())
    assert d["member_count"] > 0
    x = member_by_rank(DOMAINS[0], _key(), 0)
    assert member_rank(DOMAINS[0], _key(), x["member_id"]) == 0
    p = member_page(domain_id=DOMAINS[0], conditioning_key=_key(), limit=5)
    assert len(p["records"]) == 5 and p["next_cursor"] is not None
    p2 = member_page(domain_id=DOMAINS[0], conditioning_key=_key(), cursor=p["next_cursor"], limit=5)
    assert p2["first_rank"] == 5
    assert member_compatibility(DOMAINS[0], _key(), x["member_id"])["threshold"] is False
    assert member_ancestry(DOMAINS[0], _key(), x["member_id"])["member_id"] == x["member_id"]


def test_c124_safe_isolation_and_mutations():
    out = load_verified_current_member_authority()
    assert static_isolation_guard()["pass"]
    assert out["witness_values"] == 0 and out["component_sums"] == 0
    assert sum(mutate_live_icmembers(i) != out for i in range(384)) == 384
