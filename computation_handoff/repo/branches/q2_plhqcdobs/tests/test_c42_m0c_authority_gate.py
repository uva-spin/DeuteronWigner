"""C42 has no derivation arrays: test the live source-authority gate instead."""
from copy import deepcopy
import pytest
from deuteron_wigner.bridge.m0c.authority import authority_audit, assert_gauge_action_incomplete, validate_authority_records, STATUS

@pytest.mark.parametrize("fault_id",range(160))
def test_160_source_authority_mutations_close_the_gate(fault_id):
    records=deepcopy(authority_audit()["records"]); row=records[fault_id%3]
    field=("identifier","expected_repository_path","present","sha256","status")[fault_id%5]
    row[field]="CORRUPTED_"+str(fault_id) if field not in ("present",) else not row[field]
    assert not validate_authority_records(records)
    assert authority_audit()["status"]==STATUS

def test_missing_primary_authorities_prevent_gauge_derivation():
    audit=assert_gauge_action_incomplete()
    assert audit["missing_required"]==["hep-ph/9705477","hep-ph/0208038"]
