import json
from pathlib import Path
import pytest

from deuteron_wigner.bridge.b1.core import (
    AdapterStatus, BridgeSchemeId, BridgeSchemePlan, CapabilityStatus,
    DistributionBridgeCapability, FiniteSchemeAdapter, TMDDefinitionRecord,
    detect_injection,
)

ROOT=Path(__file__).resolve().parents[1];D=ROOT/'docs/next_level'
def load(n):return json.loads((D/n).read_text())

def test_definition_requires_two_sources_and_rank_zero():
    with pytest.raises(ValueError,match='INCOMPLETE'):
        TMDDefinitionRecord('x','r','o','p','u','direct','f','GeV^-1',0,'s',('one',))

def test_scheme_selection_is_frozen_before_residuals():
    with pytest.raises(ValueError,match='AFTER_RESIDUALS'):
        BridgeSchemePlan('p','a','b',False)

def test_missing_source_expression_adapter_fails_closed():
    a=FiniteSchemeAdapter('a','s','t','FUNDAMENTAL',AdapterStatus.SOURCE_EXPRESSION_UNAVAILABLE,None,'unknown',None,None,'NONZERO_UNKNOWN','d')
    with pytest.raises(ValueError,match='SOURCE_EXPRESSION_REQUIRED'):a.convert((1.,))

def test_false_capability_promotion_rejected():
    with pytest.raises(ValueError,match='FALSE_PROMOTION'):
        DistributionBridgeCapability('p','u',CapabilityStatus.READY,True,True,False,True,False,False,False,('blocked',))

def test_external_definition_and_flavor_semantics():
    d=load('c30_art25_tmd_definition_manifest.json');f=load('c30_art25_flavor_convention_manifest.json')
    assert d['object_kind'].startswith('evolved b-space') and f['stored_scalar']=='f_not_xf'
    assert f['flavor_indices']=={'u':7,'d':6,'ubar':3,'dbar':4}

def test_zero_ready_is_not_zero_physics():
    cap=load('c30_distribution_bridge_capability_matrix.json')
    assert cap['ready']==0 and cap['status_counts']=={'BRIDGE_COMMON_DOMAIN_ONLY':12}
    assert all(x['blocking_reasons'] for x in cap['rows'])

def test_covariance_members_and_isolation():
    c=load('c30_external_distribution_anomaly_factor_manifest.json');r=load('c30_regression_report.json')
    assert c['shape']==[642,0] and c['member_order_exact'] and c['status'].startswith('EMPTY_PROJECTION')
    assert r['production_registry']==216 and r['all_artifacts_unchanged'] and not r['status_promoted']

def test_ordered_injections_route():
    i=load('c30_injection_manifest.json');assert i['count']==1520 and i['all_detected']
    assert all(detect_injection(x['stable_id'])==x['expected_diagnostic'] for x in i['rows'])
