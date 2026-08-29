from deuteron_wigner.bridge import hqcdrimassc43heatkernel1 as c
def test_operators():assert c.operator_ledger()["count_once"] and c.operator_ledger()["rows"][2]["multiplicity"]==0
def test_uv():assert c.uv_certificate()["UV_finite"] and not c.uv_certificate()["local_holonomy_counterterm"]
def test_parity():assert c.route_parity()["agreement"] and c.route_parity()["theta_zero"] and c.route_parity()["conjugate_even"]
def test_frontier():assert c.residual_frontier()["next"]=="C337/HQCDRIMASSC43HEATEVAL1"
def test_reload():assert not c.load_verified_hqcdrimassc43heatkernel1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43heatkernel1(i)["pass"] for i in range(384))
