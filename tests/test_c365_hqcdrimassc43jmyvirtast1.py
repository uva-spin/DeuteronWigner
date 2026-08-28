from deuteron_wigner.bridge import hqcdrimassc43jmyvirtast1 as c
def test_ast():assert c.virtual_parent_ast()["count"]==5 and all("numerator" in x for x in c.virtual_parent_ast()["rows"])
def test_contours():assert "+i0" in c.virtual_parent_ast()["rows"][1]["denominators"] and "-i0" in c.virtual_parent_ast()["rows"][1]["denominators"]
def test_binding():assert c.projector_binding()["count"]==5 and "epsilon_UV" in c.projector_binding()["MSbar"]
def test_gate():assert c.closure()["five_bare_parents_available"] and not c.closure()["scalar_poles_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyvirtast1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyvirtast1(i)["pass"] for i in range(384))
