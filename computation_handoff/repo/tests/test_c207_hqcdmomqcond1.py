from deuteron_wigner.bridge import hqcdmomqcond1 as c
def test_authority_audit():
 assert c.verify_hqcd_momqcond1_authority()["C206_package_root"]==c.C206_ROOT
 a=c.target_authority_audit();assert a["exactly_representable_in_C43"] is False
 assert a["target_coefficient_available"] is False
def test_missing_objects():
 m=c.missing_target_object_manifest();assert m["count"]==4
 assert all(x["status"]=="UNAVAILABLE_NOT_ZERO" for x in m["rows"])
def test_preservation_and_release():
 assert c.c206_preservation_manifest()["target_constraint_added"]==0
 assert c.momqcond1_release_manifest()["released"] is False
 assert c.next_target_handoff_contract()["next"]=="C208/HQCDMOMQSOURCE1"
def test_routes_topology():
 assert c.acquisition_route_manifest()["count"]==4
 assert c.topology_manifest()["count"]==7
def test_isolation_mutations():
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdmomqcond1(i)["pass"] for i in range(384))
