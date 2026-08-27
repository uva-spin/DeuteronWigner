from deuteron_wigner.bridge import hqcdriquarkfixedkvinterface2 as c
def test_join():
 m=c.interface_enclosure_manifest();assert m["count"]==m["unique"]==24 and m["join_mismatches"]==0
def test_shape():assert c.interface_enclosure_manifest()["interfaces"]==3 and c.interface_enclosure_manifest()["channels_per_interface"]==8
def test_nonv1():assert c.nonV1_preservation_manifest()["count"]==12 and c.nonV1_preservation_manifest()["zeroed"]==0
def test_release():assert c.release_manifest()["joined_records"]==24 and c.release_manifest()["contribution_enclosures"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvinterface2_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvinterface2(i)["pass"] for i in range(384))
