from deuteron_wigner.bridge import hqcdrimassc43jmykinematicast1 as c
def test_metric():assert c.dot(c.vector(3,0),c.vector(0,2))==6
def test_invariants():assert not c.invariant_ast()["physical_components_selected"]
def test_cut():assert c.cut_substitutions()["q2"]=="-kT2/(1-x)"
def test_gate():assert c.projector_substitutions()["count"]==4 and c.closure()["parameter_reduction_ready"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmykinematicast1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmykinematicast1(i)["pass"] for i in range(384))
