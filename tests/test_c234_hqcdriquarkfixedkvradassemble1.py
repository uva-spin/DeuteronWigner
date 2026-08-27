from deuteron_wigner.bridge import hqcdriquarkfixedkvradassemble1 as c
def test_manifest():assert c.assembly_manifest()["count"]==c.assembly_manifest()["unique_ids"]==8
def test_record():
 rid=c.assembly_manifest()["rows"][0]["radial_id"];r=c.assembled_radial_record(rid,1)
 assert r["total_bound"]=="B_core+B_tail" and r["value_kind"].startswith("CERTIFIED")
def test_routes():assert c.route_certificate()["coverage_mismatches"]==0
def test_release():assert c.release_manifest()["assembled_families"]==8 and c.release_manifest()["mapped_interfaces"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvradassemble1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvradassemble1(i)["pass"] for i in range(384))
