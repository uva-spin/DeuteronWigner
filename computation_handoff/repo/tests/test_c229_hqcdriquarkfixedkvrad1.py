from deuteron_wigner.bridge import hqcdriquarkfixedkvrad1 as c
def test_families():assert c.radial_family_manifest()["count"]==8
def test_convergence():assert c.convergence_certificate()["convergent"]==8 and c.convergence_certificate()["divergent"]==0
def test_enclosure():assert not c.enclosure_audit()["enclosure_complete"] and not c.enclosure_audit()["numeric_quadrature_promoted"]
def test_release():assert c.release_manifest()["evaluated_or_enclosed"]==0 and c.next_handoff_contract()["next"]=="C230/HQCDRIQUARKFIXEDKVRADBOUND1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvrad1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvrad1(i)["pass"] for i in range(384))
