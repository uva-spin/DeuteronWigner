from deuteron_wigner.bridge import hqcdrimasscoord1 as c
def test_source():assert c.source_record()["authenticated"] and len(c.source_record()["locators"])==6
def test_coord():assert c.coordinate_definition()["coordinate"]=="alpha_s/(4*pi)" and c.coordinate_definition()["first_omitted"]=="O(alpha_s^2)"
def test_orientation():assert "MSbar=C_m" in c.coordinate_definition()["orientation"]
def test_ast():assert c.coordinate_ast()["safe"] and not c.coordinate_ast()["eval"]
def test_routes():assert c.route_certificate()["mismatches"]==0
def test_frontier():assert c.residual_frontier()["next"]=="C282/HQCDRIMASSNF1" and c.residual_frontier()["remaining_dependency_leaves"]==3
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["numerical_alpha_s_selected"]==0
def test_reload():assert c.load_verified_hqcdrimasscoord1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimasscoord1(i)["pass"] for i in range(384))
