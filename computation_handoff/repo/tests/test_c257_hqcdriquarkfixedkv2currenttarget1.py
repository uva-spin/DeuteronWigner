from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenttarget1 as c
def test_discovery():assert c.discovery_inventory()["qualified_capsules"]==0
def test_rejections():assert c.candidate_rejection_ledger()["accepted"]==0
def test_resolution():assert c.capsule_resolution()["status"]=="UNAVAILABLE_NOT_ZERO" and len(c.capsule_resolution()["uncovered_directions"])==4
def test_routes_scope():assert c.route_certificate()["mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currenttarget1(i)["pass"] for i in range(384))
