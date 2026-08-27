from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentreg1 as c
def cap():return c.RegulatorCapsule("I2_density_projector",.5,subtraction_scheme="C254_TEST_SCHEME")
def test_topology():assert c.test_function_topology()["physical_smearing"] is False
def test_regulator():assert c.regulator_program(cap())["trace_class_for_0_r_1"]
def test_subtraction():assert c.subtraction_ownership_manifest()["coefficients_ready"]==0
def test_routes_scope():assert c.route_certificate()["topology_mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currentreg1(i)["pass"] for i in range(384))
