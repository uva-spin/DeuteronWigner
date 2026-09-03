from deuteron_wigner.bridge import hqcdrimassc43jmyexecgroup1 as c
def test_groups():assert c.group_ast()["counts"]=={"distribution":6,"fragmentation":6,"soft":4,"total":16}
def test_ct():assert c.counterterm_ast()["count"]==5 and c.counterterm_ast()["applied_after_region_projection"]
def test_assembly():assert c.assembly_validation()["all_terms_have_integral"] and c.assembly_validation()["mass_IR"]==0
def test_gate():assert c.closure()["group_AST_executable"] and not c.closure()["integration_or_expansion_performed"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyexecgroup1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyexecgroup1(i)["pass"] for i in range(384))
