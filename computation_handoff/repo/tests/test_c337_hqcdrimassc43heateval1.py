from deuteron_wigner.bridge import hqcdrimassc43heateval1 as c
def test_determinant():assert all(abs(x)<1e6 for x in c.determinant_components(.4,1.1,2.,.01).values())
def test_projection():assert c.convergence_enclosure()["boson_truncation_residual_retained"] and c.convergence_enclosure()["fermion_residual_nonzero"] and c.convergence_enclosure()["fermion_residual_exceeds_boson"]
def test_center():assert c.symmetry_certificate()["boson_center_invariant"] and not c.symmetry_certificate()["fermion_center_invariant"]
def test_frontier():assert c.residual_frontier()["next"]=="C338/HQCDRIMASSC43CENTERBASIS1"
def test_reload():assert not c.load_verified_hqcdrimassc43heateval1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43heateval1(i)["pass"] for i in range(384))
