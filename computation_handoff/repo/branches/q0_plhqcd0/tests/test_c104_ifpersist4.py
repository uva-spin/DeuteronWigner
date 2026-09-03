from deuteron_wigner.bridge.ifpersist4 import *
import pytest
PAIR='C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0|C78:QG:K9_2_N8_b0.40:KIN=19:TRIP=0'; RES='K9_2_N8_b0.40'
def test_authority_and_rank_unrank():
 assert verify_canonical_c82_coefficient_authority()['pass']; assert supported_pair_count()==154830
 for i in (0,1,323,canonical_record(PAIR,RES,0)['pair']['sequence']*0):
  r=canonical_record(PAIR,RES,i); assert rank_record_identity(PAIR,RES,r)==i; assert r['excluded'][0]=='C80_kernel_value'
 with pytest.raises(IndexError): canonical_record(PAIR,RES,324)
def test_page_cursor_and_immutability():
 p=canonical_record_page(PAIR,RES,limit=3); assert len(p['records'])==3
 q=canonical_record_page(PAIR,RES,cursor=p['next_cursor'],limit=3); assert q['records'][0]['pair_local_ordinal']==3
 with pytest.raises(TypeError): p['records'][0]['status']='x'
