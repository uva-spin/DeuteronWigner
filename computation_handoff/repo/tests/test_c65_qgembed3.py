import pytest
from deuteron_wigner.bridge.qgembed3.core import preflight, mutate_live_c65, validate_c65

def test_c65_c64_import_passes_but_missing_c53_u3_blocks_embedding():
    value = preflight()
    assert value["C64_import"]["blocks"] == 733
    assert value["C64_import"]["coefficient_status_records"] == 171153
    assert value["C64_import"]["residue_certificates"] == 67920
    assert value["C53_triplet_import"]["runtime_paths_existing"] == []
    assert validate_c65(value)

@pytest.mark.parametrize("fault_id", range(320))
def test_c65_live_mutations_fail(fault_id):
    assert not validate_c65(mutate_live_c65(fault_id))
