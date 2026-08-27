from deuteron_wigner.bridge import hqcdrimassv0meshproject1 as c
def test_measure():assert c.measure_correction()["C296_square_integral"]==2 and c.measure_correction()["corrected_integral"]==1
def test_routes():assert len(c.measure_correction()["routes"])==3
def test_scan():assert not c.direct_sum_scan()["quadrature_converged"]
def test_drift():assert c.direct_sum_scan()["rows"][2]["rms"]>c.direct_sum_scan()["rows"][0]["rms"]
def test_mesh():assert not c.mesh_reconstruction()["full_values_recoverable"]
def test_projection():assert c.projection_certificate()["requested_result"].startswith("NO_REGULATOR")
def test_frontier():assert c.residual_frontier()["next"]=="C305/HQCDRIMASSV0FINITEPART1"
def test_reload():assert c.load_verified_hqcdrimassv0meshproject1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0meshproject1(i)["pass"] for i in range(384))
