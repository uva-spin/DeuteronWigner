from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as m
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenteval1 as c
def x(graph="I4_local"):return m.ComplementCurrentCoordinate("J_qJ_q","q->q","K9_2_N8_b0.40",(("q","5/2",0,0,-1,0),),(("q","5/2",0,0,-1,1),),graph)
def test_i4():assert c.direct_evaluation(x())["status"]=="EXACT_SYMBOLIC_EVALUATED"
def test_missing_not_zero():assert c.direct_evaluation(x("I2_density_projector"))["status"]=="SPATIAL_PROJECTOR_UNAVAILABLE_NOT_ZERO"
def test_routes():assert c.route_certificate(x())["mismatches"]==0
def test_scope():assert c.evaluator_scope_manifest()["ready"]==1 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currenteval1(i)["pass"] for i in range(384))
