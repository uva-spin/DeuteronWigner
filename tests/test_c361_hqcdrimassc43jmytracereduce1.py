from deuteron_wigner.bridge import hqcdrimassc43jmytracereduce1 as c
def test_topology():assert not c.topology_audit()["scalar_reduction_safe"]
def test_missing_cut():assert any(x["final_quark_cut"] is False for x in c.topology_audit()["rows"])
def test_source():assert "CutPlus((p-k)^2)" in c.source_check()["C360_missing"] and not c.source_check()["mass_formula_reused"]
def test_fail_closed():assert not c.closure()["scalar_reduction_complete"] and c.reduction_hold()["ordinary_repair_continuation"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmytracereduce1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmytracereduce1(i)["pass"] for i in range(384))
