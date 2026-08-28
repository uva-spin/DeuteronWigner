from deuteron_wigner.bridge import hqcdrimassc43jmytraceast1 as c
def test_traces():assert c.trace_ast()["count"]==6 and all("expr" in x and "den" in x for x in c.trace_ast()["rows"])
def test_ct():assert c.counterterm_ast()["count"]==5 and all("UVPart" in x["expr"] or "Cross" in x["expr"] for x in c.counterterm_ast()["rows"])
def test_measurement():assert "z^(-2+2epsilon)" in c.measurement_ast()["fragmentation"]
def test_gate():assert c.validation()["all_nodes_executable"] and not c.closure()["scalar_reduction_complete"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmytraceast1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmytraceast1(i)["pass"] for i in range(384))
