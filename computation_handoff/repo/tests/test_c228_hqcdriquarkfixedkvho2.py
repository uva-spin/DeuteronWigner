from deuteron_wigner.bridge import hqcdriquarkfixedkvho2 as c
def test_harmonics():assert c.angular_harmonic_manifest()["harmonics"]==(1,-1,2,0,0,-2,1,-1)
def test_projection():
 for m in range(-3,4): assert c.angular_projection_program(m)["matching"]==c.angular_harmonic_manifest()["harmonics"].count(m)
def test_routes_radial():assert c.angular_route_certificate()["mismatches"]==0 and c.radial_frontier_manifest()["count"]==8
def test_release():assert c.release_manifest()["angular_projections_complete"]==8 and c.next_handoff_contract()["next"]=="C229/HQCDRIQUARKFIXEDKVRAD1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvho2_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvho2(i)["pass"] for i in range(384))
