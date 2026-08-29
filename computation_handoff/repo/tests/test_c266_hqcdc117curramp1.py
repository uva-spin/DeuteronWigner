from deuteron_wigner.bridge import hqcdc117curramp1 as c
def test_current(): assert "J_q" in c.continuum_current_kernel()["current"] and c.continuum_current_kernel()["Hermitian"]
def test_packets(): assert all(c.packet_program(d)["width_rule"].startswith("parameters remain") for d in c.DIRECTIONS)
def test_capsules(): assert c.current_packet_capsules()["closed"]==4 and c.current_packet_capsules()["required"]==4
def test_routes(): assert c.two_route_derivation()["mismatches"]==0 and c.two_route_derivation()["current_identity_agreement"]
def test_executable(): assert c.executability_validation()["normalization_executable"] and c.executability_validation()["HO_expansion_executable"]
def test_frontier(): assert c.residual_frontier()["next"]=="C267/HQCDC117NONLOCALTARGET2"
def test_reload_scope(): assert c.static_isolation_guard()["pass"] and c.load_verified_hqcdc117curramp1_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117curramp1(i)["pass"] for i in range(384))
