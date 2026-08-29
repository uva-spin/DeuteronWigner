import pytest
from deuteron_wigner.bridge.b1a.core import *

def test_three_layer_gate_fails_without_lf_matching():
    m=MatchingCapability('x',MatchingStrategy.UNAVAILABLE,False,False,False,False,False,False,'NO','NONZERO_UNKNOWN')
    assert not C31BridgeExecutionGate(m,True).execute
def test_tree_level_strategy_not_ready():
    m=MatchingCapability('x',MatchingStrategy.TREE_LEVEL_ONLY,False,False,False,False,False,True,'TREE','NONZERO_UNKNOWN')
    assert not m.ready
def test_regulator_not_silently_equivalent():
    r=MicroscopicRegulatorId('c11','finite','finite','finite','finite')
    assert not r.continuum_equivalence_proved
def test_adapter_is_member_independent():
    a=FiniteTMDSchemeTransformation('a','p','art','aligned','1','unchanged','formal','formal',True,True,'separate')
    assert a.member_independent
def test_injections_complete():
    rows=injection_rows(); assert len(rows)==1680 and len({x['injection_id'] for x in rows})==1680
def test_injections_detected():
    for row in injection_rows(): assert detect_injection(row['injection_id'])==row['expected_diagnostic']
def test_unknown_injection_rejected():
    with pytest.raises(ValueError): detect_injection('C31.INJECT.BAD.0001')
def test_content_hash_deterministic():
    x=ScaleMap('x','ZETA','a','b','OK'); assert content_hash(x)==content_hash(x)
