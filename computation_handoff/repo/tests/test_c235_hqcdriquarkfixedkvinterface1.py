from deuteron_wigner.bridge import hqcdriquarkfixedkvinterface1 as c
def test_audit():assert c.interface_join_audit()["count"]==15 and c.interface_join_audit()["mapped"]==0
def test_labels():assert all(r["positional_join_forbidden"] and not r["published_endpoint_m"] for r in c.interface_join_audit()["rows"])
def test_radial():assert c.radial_authority_manifest()["families"]==8 and c.radial_authority_manifest()["interface_rows_with_all_keys"]==0
def test_release():assert c.release_manifest()["interfaces_audited"]==15 and c.release_manifest()["interfaces_mapped"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvinterface1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvinterface1(i)["pass"] for i in range(384))
