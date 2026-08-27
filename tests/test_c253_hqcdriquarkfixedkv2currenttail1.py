from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenttail1 as c
def test_classes():assert c.asymptotic_classification()["count"]==4 and c.asymptotic_classification()["summable_in_raw_scope"]==0
def test_routes():assert c.independent_route_certificate()["classification_mismatches"]==0
def test_majorant_unavailable():assert c.tail_majorant_program("CM_ground",1e-6)["status"]=="UNAVAILABLE_NOT_ZERO_IN_RAW_SCOPE"
def test_not_blocker_scope():assert not c.raw_scope_nonexistence_certificate()["blocker"] and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currenttail1(i)["pass"] for i in range(384))
