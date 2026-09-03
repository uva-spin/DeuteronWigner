from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as m
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentproj1 as c
def coord():return m.ComplementCurrentCoordinate("J_qJ_g","qg->qg","K9_2_N8_b0.40",(("q","3/2",0,0,-1,0),("g","1",0,0,-1,0)),(("q","3/2",0,0,-1,1),("g","1",0,0,-1,1)),"derivative_density")
def cap(k="derivative_density"):return c.ComplementProjectorCapsule(k,coord(),(("g","1",0,0,-1,0),),.4)
def test_programs():assert c.program_inventory()["programs_ready"]==4 and c.projector_program(cap())["caller_capsule_exact"]
def test_unbounded_not_zero():assert c.projector_program(cap())["unbounded_completion"]=="UNAVAILABLE_NOT_ZERO"
def test_composition():assert c.composition_program(cap("CM_ground"))["retained_ids"] is False
def test_routes_scope():assert c.route_certificate()["program_mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currentproj1(i)["pass"] for i in range(384))
