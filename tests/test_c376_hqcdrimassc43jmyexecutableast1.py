from deuteron_wigner.bridge import hqcdrimassc43jmyexecutableast1 as c
def test_ast():assert c.denominator_ast()["count"]==4 and c.numerator_ast()["count"]==12
def test_master():assert c.master_ast()["total_graph_terms"]==15
def test_eval():assert c.evaluate(c.A(c.N(2),c.M(c.N(3),c.S("x"))),{"x":4})==14
def test_validation():assert c.validation()["schema_evaluation"] and c.validation()["prose_nodes"]==0
def test_reload():assert not c.load_verified_hqcdrimassc43jmyexecutableast1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyexecutableast1(i)["pass"] for i in range(384))
