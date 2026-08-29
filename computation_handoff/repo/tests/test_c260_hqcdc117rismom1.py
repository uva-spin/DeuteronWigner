from deuteron_wigner.bridge import hqcdc117rismom1 as c
def test_basis_and_kinematics(): assert c.operator_basis()["dimension"]==4 and c.symmetric_kinematics()["nonexceptional"] and c.symmetric_kinematics()["gauge"]=="Landau xi=0"
def test_projector_routes(): assert c.projector_basis()["direct_contraction"]==c.projector_basis()["dual_contraction"] and c.tree_response_matrix()["route_residual"]==0
def test_full_rank(): assert c.tree_response_matrix()["rank"]==4 and c.tree_response_matrix()["condition_number"]==1 and not c.tree_response_matrix()["left_nullspace"]
def test_target_nonclaims(): assert c.tree_target_definition()["physical_observable_target"]=="UNAVAILABLE_NOT_ZERO" and c.tree_target_definition()["coefficient_values"]=="UNAVAILABLE_NOT_ZERO"
def test_mixing_conversion(): assert c.mixing_and_evanescent_convention()["gamma5"].startswith("NDR") and c.conversion_boundary()["conversion_matrix"]=="UNAVAILABLE_NOT_ZERO_C261"
def test_adapter_separation(): assert len(c.finite_C43_adapter_interface()["rows"])==3 and all(x["separate"] for x in c.finite_C43_adapter_interface()["rows"])
def test_reload_and_scope(): assert c.static_isolation_guard()["pass"] and c.load_verified_hqcdc117rismom1_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117rismom1(i)["pass"] for i in range(384))
