import math,pytest
from deuteron_wigner.bridge.r0.core import *

def test_distribution_quark_number():
 d=DistributionResult(DeltaEndpointTerm(1.25),(PlusDistributionTerm(.5),),RegularDistributionTerm((.2,-.1)))
 assert abs(d.mellin(1)-1.4)<1e-11
def test_plus_annihilates_constant():assert abs(PlusDistributionTerm(1).action(lambda x:1))<1e-12
def test_plus_first_moment():assert abs(PlusDistributionTerm(1).action(lambda x:x)+1)<1e-11
def test_lower_limit_plus_is_finite():assert math.isfinite(PlusDistributionTerm(1).action(lambda x:x,.2))
def test_gate_fails_soft_obstruction():
 g=MatchingGate(True,True,False,False,False,False,False,False,False,False,False,False);assert not g.passes
def test_exact_c11_tree_reduction_uses_real_parents():
 r=exact_c11_tree_reduction_oracle();assert r['maximum_residual']==0 and len(r['rows'])==12 and all(x['nonvacuous_parent'] for x in r['rows'])
def test_regulator_content_hash_stable():
 r=LightFrontBasisRegulator('x',(13,2),12,.5,'e',1.73,.14,'z','b','ct');assert content_hash(r)==content_hash(r)
def test_injections_complete():
 x=injection_rows();assert len(x)==1840 and len({r['injection_id'] for r in x})==1840
def test_all_injections_detect():
 for r in injection_rows():assert detect_injection(r['injection_id'])==r['expected_diagnostic']
def test_unknown_injection_rejected():
 with pytest.raises(ValueError):detect_injection('C32.INJECT.BAD.0001')
