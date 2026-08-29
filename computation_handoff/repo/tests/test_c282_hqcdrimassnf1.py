from deuteron_wigner.bridge import hqcdrimassnf1 as c
def test_source():assert c.source_flavor_record()["flavor_class"]=="bilinear nonsinglet"
def test_nf():assert c.active_nf_record()["one_loop_mass_conversion_dependence"]=="ABSENT"
def test_separation():assert not c.separation_certificate()["flavor_average"] and c.separation_certificate()["route_mismatches"]==0
def test_ast():assert c.flavor_ast()["safe"] and not c.flavor_ast()["eval"]
def test_frontier():assert c.residual_frontier()["next"]=="C283/HQCDRIMASSGAUGEADAPTER1" and c.residual_frontier()["remaining_dependency_leaves"]==2
def test_release():assert c.release_manifest()["active_Nf_semantics_closed"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["Nf_selected"]==0
def test_reload():assert c.load_verified_hqcdrimassnf1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassnf1(i)["pass"] for i in range(384))
