from deuteron_wigner.bridge import hqcdriquarkfixedkden1 as c
def test_schema():
 x=c.denominator_schema();assert not x["executable"] and not x["dense_inverse"]
def test_components():assert c.component_audit()["first_missing"]=="Q_R H0 Q_R"
def test_nonpromotion():
 x=c.retained_zero_nonpromotion_certificate();assert not x["promoted_to_omitted_domain"] and not x["contradiction"]
def test_release():assert c.next_handoff_contract()["next"]=="C222/HQCDRIQUARKFIXEDKFREE1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkden1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkden1(i)["pass"] for i in range(384))
