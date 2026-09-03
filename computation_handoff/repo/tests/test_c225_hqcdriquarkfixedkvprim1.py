from deuteron_wigner.bridge import hqcdriquarkfixedkvprim1 as c
def test_schema():
 x=c.symbolic_primitive_schema();assert not x["eval"] and not x["pickle"] and not x["callbacks"]
def test_programs():assert c.helicity_program_manifest()["count"]==8 and c.helicity_program_manifest()["exact_symbolic"]==8
def test_routes_ho():assert c.independent_route_certificate()["structural_mismatches"]==0 and not c.ho_projection_audit()["quadrature_promoted"]
def test_release():assert not c.release_manifest()["HO_projection_ready"] and c.next_handoff_contract()["next"]=="C226/HQCDRIQUARKFIXEDKVHO1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvprim1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedkvprim1(i)["pass"] for i in range(384))
