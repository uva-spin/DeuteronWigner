"""Live C43 source/action-contract mutations must close the projection gate."""
from copy import deepcopy
import pytest
from deuteron_wigner.bridge.g0.contracts import source_manifest, action_contract, validate_contract, validate_source_manifest

@pytest.mark.parametrize("fault_id",range(128))
def test_128_source_convention_constraint_and_boundary_mutations_fail(fault_id):
    if fault_id%2==0:
        x=deepcopy(source_manifest()); row=x["rows"][(fault_id//2)%len(x["rows"])]
        key=("arxiv","pdf_sha256","archive_sha256","pdf_pages")[(fault_id//4)%4]
        row[key]="CORRUPTED" if key!="pdf_pages" else -1
        assert not validate_source_manifest(x)
    else:
        x=deepcopy(action_contract())
        options=[("gauge","G0-COVARIANT-GAUGE"),("fermion_constraint","OMITTED"),("gauss_law","OMITTED"),("inverse_derivative","OMITTED"),("interactions","OMITTED"),("ghost_status","C40_ALIAS")]
        key,value=options[(fault_id//2)%len(options)]
        x[key]=value
        with pytest.raises(AssertionError): validate_contract(x)

def test_c43_contract_is_symbolically_complete_but_matrix_free():
    assert validate_contract(action_contract())
    assert validate_source_manifest(source_manifest())
