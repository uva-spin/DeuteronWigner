from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as m
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentproj1 as p
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentprojeval1 as c
def cap(k="I2_density_projector"):
 x=m.ComplementCurrentCoordinate("J_qJ_q","q->q","K9_2_N8_b0.40",(("q","5/2",0,0,-1,0),),(("q","5/2",0,0,-1,1),),k);return p.ComplementProjectorCapsule(k,x,(("q","3/2",0,0,-1,0),),.4)
def test_core():assert c.finite_core_evaluation(cap())["status"]=="FINITE_CORE_EXACT_SYMBOLIC"
def test_tail():assert c.tail_growth_audit()["majorants_ready"]==0
def test_not_zero():assert not c.core_tail_enclosure(cap())["represented_as_zero"]
def test_routes_scope():assert c.route_certificate(cap())["core_mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currentprojeval1(i)["pass"] for i in range(384))
