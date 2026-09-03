from deuteron_wigner.bridge import hqcdrimassc43jmygroupmaster1 as c
def test_measure():assert "d^d ell" in c.measure_authority()["loop"] and "after UV" in c.measure_authority()["MSbar"]
def test_masters():assert c.master_family()["count"]==3
def test_maps():assert "Cutkosky" in c.parameter_maps()["rows"][0]["map"] and c.parameter_maps()["count"]==3
def test_gate():assert c.closure()["common_master_family"] and not c.closure()["masters_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmygroupmaster1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmygroupmaster1(i)["pass"] for i in range(384))
