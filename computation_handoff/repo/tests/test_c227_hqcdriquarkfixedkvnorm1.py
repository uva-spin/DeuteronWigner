from deuteron_wigner.bridge import hqcdriquarkfixedkvnorm1 as c
def test_forms():
 x=c.normal_form_manifest();assert x["count"]==8 and x["complete"]==8 and x["conjugates_remaining"]==0
def test_branches():assert c.branch_certificate()["E_plus_m_positive"]
def test_routes():assert c.route_certificate()["helicity_count"]==8 and c.route_certificate()["structural_mismatches"]==0
def test_release():assert c.release_manifest()["normal_forms_ready"]==8 and c.next_handoff_contract()["next"]=="C228/HQCDRIQUARKFIXEDKVHO2"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvnorm1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvnorm1(i)["pass"] for i in range(384))
