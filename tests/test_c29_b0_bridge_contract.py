import json
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.bridge.b0.core import (
    BridgeDiscrepancyComponent, BridgeMemberRelation, BridgeOperatorId,
    BridgeRootPairId, ExternalRootId, MicroscopicRootId,
    covariance_pushforward, detect_injection, nonlinear_memberwise, require_complete_match,
)

ROOT=Path(__file__).resolve().parents[1];D=ROOT/'docs/next_level'
def load(name):return json.loads((D/name).read_text())

def operator(flavor='u',rank=0,target='PROTON'):
    return BridgeOperatorId('OP', 'q', flavor, 'U', target, rank, 'EVEN',
        'STAPLE_EVEN','NONE',2,'MSBAR','DELTA','SQRT_SOFT',5.,25.,'D')

def test_roots_are_immutable_and_disjoint():
    pair=BridgeRootPairId(ExternalRootId(),MicroscopicRootId())
    assert pair.external.value!=pair.microscopic.value
    with pytest.raises(Exception): pair.external.value='x'
    with pytest.raises(ValueError): ExternalRootId('PROJECT_MICROSCOPIC_OPERATOR_ROOT')

def test_complete_operator_match_not_name_match():
    require_complete_match(operator(),operator())
    with pytest.raises(ValueError,match='rank'):
        require_complete_match(operator(),operator(rank=1))
    with pytest.raises(ValueError,match='target'):
        require_complete_match(operator(),operator(target='DEUTERON'))

def test_no_cross_root_index_pairing():
    relation=BridgeMemberRelation(BridgeRootPairId(ExternalRootId(),MicroscopicRootId()))
    with pytest.raises(ValueError,match='INDEX_PAIRING'):
        relation.pair_by_index(1,1)

def test_linear_and_nonlinear_covariance():
    rng=np.random.default_rng(29);a=rng.normal(size=(642,8));b=np.eye(8)[[0,3,7]]
    pushed,cov=covariance_pushforward(a,b)
    assert np.array_equal(pushed,a[:,[0,3,7]])
    assert np.max(np.abs(cov-pushed.T@pushed))==0
    mean,na,nc=nonlinear_memberwise(a[:,:2],lambda x:np.array([x[0]*x[1]]))
    assert mean.shape==(1,) and na.shape==(642,1) and nc.shape==(1,1)

def test_unknown_discrepancy_is_not_zero():
    with pytest.raises(ValueError,match='UNKNOWN_ZERO'):
        BridgeDiscrepancyComponent('D','BRIDGE','all','UNKNOWN','UNAVAILABLE','future',False,True,'ADDITIVE')

def test_frozen_roles_and_ancestry():
    grid=load('c29_frozen_bridge_grid.json');ancestry=load('c29_data_ancestry_graph.json')
    assert grid['frozen_before_microscopic_execution'] and all(x['frozen_before_diagnostics'] for x in grid['rows'])
    assert ancestry['retained_points']==1209 and ancestry['datasets']==46

def test_bridge_fails_closed_without_common_scheme():
    cap=load('c29_bridge_capability_matrix.json')
    assert cap['distribution_ready']==0 and cap['one_leg_ready']==0
    assert all(not x['future_calibration_readiness'] for x in cap['rows'])

def test_isolation_and_negative_controls():
    reg=load('c29_regression_report.json');inj=load('c29_injection_manifest.json')
    assert reg['production_registry']==216 and reg['all_artifacts_unchanged']
    assert inj['count']>=1400 and inj['all_detected']
    assert all(detect_injection(x['stable_id'])==x['expected_diagnostic']==x['actual_diagnostic'] for x in inj['rows'])

def test_volume_xix_formal_contract_is_complete_and_non_promoting():
    crosswalk=load('c29_volume_xix_requirement_crosswalk.json')
    normative=load('c29_normative_source_integration.json')
    assert crosswalk['count']==50 and crosswalk['all_mapped']
    assert not crosswalk['status_promotion_authorized']
    assert [x['stable_id'] for x in crosswalk['rows']]==[f'V19.{i:03d}' for i in range(1,51)]
    source=next(x for x in normative['records'] if x['path']==crosswalk['source_path'])
    assert source['available'] and source['sha256']==crosswalk['source_sha256']
