from deuteron_wigner.bridge import hqcdriquarkfixedkvendpointqn1 as c
def test_applicability():assert c.applicability_manifest()["count"]==15 and c.applicability_manifest()["V1_applicable"]==3
def test_qn():assert c.endpoint_quantum_map()["count"]==24 and c.endpoint_quantum_map()["channels_per_interface"]==8
def test_nonv1():assert all("NOT_APPLICABLE" in r["classification"] for r in c.applicability_manifest()["rows"] if not r["V1_applicable"])
def test_release():assert c.release_manifest()["interfaces_classified"]==15 and c.release_manifest()["endpoint_channel_records"]==24
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvendpointqn1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvendpointqn1(i)["pass"] for i in range(384))
