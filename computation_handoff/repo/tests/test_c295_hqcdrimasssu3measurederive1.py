from deuteron_wigner.bridge import hqcdrimasssu3measurederive1 as c
def test_cartan():assert c.cartan_convention()["weyl_group"]=="S3 order 6"
def test_spectrum():assert c.fp_spectrum()["all_eight_generators"] and c.fp_spectrum()["nonzero_modes"]==6
def test_jacobian():assert c.jacobian_formula()["nonnegative"] and not c.jacobian_formula()["identity_default"]
def test_normalization():assert c.normalization_certificate()["constant_term"]==6 and c.normalization_certificate()["integral"]==1
def test_routes():assert c.normalization_certificate()["routes_agree"]
def test_density():assert c.evaluate_density(0,0)["jacobian"]==0 and c.evaluate_density(.4,.7)["full_torus_density"]>0
def test_frontier():assert c.residual_frontier()["next"]=="C296/HQCDRIMASSSU3MEASUREADAPTER1" and not c.residual_frontier()["blocker"]
def test_reload():assert c.load_verified_hqcdrimasssu3measurederive1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimasssu3measurederive1(i)["pass"] for i in range(384))
