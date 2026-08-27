from deuteron_wigner.bridge import hqcdriquarkfixedk1 as c
def test_interfaces():
 x=c.fixed_k_interface_manifest();assert x["count"]==15 and x["executable"]==0
 assert len({r["interface_id"] for r in x["rows"]})==15
 assert all(r["contribution"]=="UNAVAILABLE_NOT_ZERO" for r in x["rows"])
def test_endpoint_audit():
 x=c.endpoint_domain_audit();assert not x["endpoint_basis"] and not x["energy_denominator"] and not x["missing_as_zero"]
def test_routes_residual():
 assert c.route_certificate()["classification_mismatches"]==0
 assert c.residual_frontier()["family_count"]==15
def test_release_handoff():
 assert not c.release_manifest()["fixed_k_contributions_complete"]
 assert c.next_handoff_contract()["next"]=="C220/HQCDRIQUARKFIXEDKMAP1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedk1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdriquarkfixedk1(i)["pass"] for i in range(384))
