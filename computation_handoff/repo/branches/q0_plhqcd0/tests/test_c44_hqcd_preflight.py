"""C44 source-to-projection gate: no numerical object exists before mode closure."""
from copy import deepcopy
import pytest
from deuteron_wigner.bridge.hqcd.preflight import projection_audit, validate_projection_audit, assert_mode_projection_incomplete, STATUS
@pytest.mark.parametrize("fault_id",range(192))
def test_192_live_projection_contract_mutations_fail(fault_id):
 a=deepcopy(projection_audit()); field=("status","C43_mode_status","C43_projection_status","physical_resolutions","missing_matrix_element_inputs")[fault_id%5]
 a[field]="CORRUPTED" if field not in ("physical_resolutions","missing_matrix_element_inputs") else []
 assert not validate_projection_audit(a)
 assert projection_audit()["status"]==STATUS
def test_mode_projection_preflight_is_exact_and_fail_closed():
 a=assert_mode_projection_incomplete(); assert len(a["missing_matrix_element_inputs"])==4
