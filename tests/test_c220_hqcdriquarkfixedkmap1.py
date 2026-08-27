from deuteron_wigner.bridge import hqcdriquarkfixedkmap1 as c
def test_domain():
 x=c.complement_domain_schema();assert x["count"]==3 and x["symbolic_complete"] and not x["finite_enumerator"]
def test_endpoints():
 x=c.endpoint_map_manifest();assert x["count"]==15 and x["domain_mapped"]==15 and x["endpoint_values_complete"]==0
 assert all(not r["represented_as_zero"] for r in x["rows"])
def test_denominator_routes():
 assert c.denominator_audit()["denominator"]=="UNAVAILABLE_NOT_ZERO"
 assert c.independent_route_certificate()["domain_mismatches"]==0
 assert c.hermiticity_projector_certificate()["source_sink_adjoint_pair"]
def test_release_handoff():
 assert c.release_manifest()["symbolic_domain_ready"] and not c.release_manifest()["denominator_ready"]
 assert c.next_handoff_contract()["next"]=="C221/HQCDRIQUARKFIXEDKDEN1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkmap1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdriquarkfixedkmap1(i)["pass"] for i in range(384))
