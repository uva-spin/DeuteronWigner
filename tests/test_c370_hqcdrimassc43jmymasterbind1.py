from deuteron_wigner.bridge import hqcdrimassc43jmymasterbind1 as c
def test_real():assert c.real_bindings()["count"]==6
def test_virtual():assert c.virtual_bindings()["count"]==5
def test_soft():assert c.soft_bindings()["count"]==2 and c.soft_bindings()["count_once"]
def test_gap():assert c.coefficient_gap()["indices_complete"] and not c.coefficient_gap()["scalar_master_coefficients_complete"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmymasterbind1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmymasterbind1(i)["pass"] for i in range(384))
