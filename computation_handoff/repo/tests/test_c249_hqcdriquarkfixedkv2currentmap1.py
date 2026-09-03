from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as c
def x():return c.ComplementCurrentCoordinate("J_qJ_g","qg->qg","K9_2_N8_b0.40",(("q","3/2",0,0,-1,0),("g","1",0,0,-1,0)),(("q","3/2",0,0,-1,1),("g","1",0,0,-1,1)),"derivative_density")
def test_coordinate():assert c.validate_coordinate(x())["K_prime"]=="5/2" and c.factor_program_coordinate(x())["retained_witness_id"] is None
def test_adjoint():assert c.adjoint_coordinate(x()).product=="J_gJ_q"
def test_interfaces():assert c.interface_applicability_manifest()["applicable"]==3
def test_routes_scope():assert c.route_certificate()["factor_mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currentmap1(i)["pass"] for i in range(384))
