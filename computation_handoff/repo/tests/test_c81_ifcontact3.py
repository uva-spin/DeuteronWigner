import pytest
from deuteron_wigner.bridge.ifcontact3 import core

def test_c81_public_composition_audit_is_fail_closed():
    audit=core.audit_pair_aggregation()
    assert audit['status']==core.STATUS
    assert audit['unavailable_supported_pairs']==154830
    assert all(row['projected_value_status']=='NOT_EVALUATED' for row in audit['by_resolution'].values())
    assert all(not row['total_coordinate_map_published'] for row in audit['by_resolution'].values())
    with pytest.raises(core.PairAggregationUnavailable): core.require_aggregatable_inputs()
