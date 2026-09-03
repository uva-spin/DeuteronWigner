import pytest
from deuteron_wigner.bridge.icreg2 import *

def test_four_projectors_close():
    out=verify_current_projector_authority()
    assert out["status"] == STATUS
    assert out["missing_projectors"] == 0
    assert out["i2_route_residual"] == out["derivative_route_residual"] == 0
    assert out["cm_route_residual"] == out["triplet_route_residual"] == 0
    assert composed_physical_projector("cm_triplet") ["commutator"] == 0
    assert triplet_projector("triplet") ["anti_sextet_leakage"] == 0

def test_domains_and_pages():
    assert len(graph_manifest()["graphs"]) == 4
    assert internal_mode_domain("I2_density_projector")["status"] == "DOMAIN_CLOSED"
    for c in CLASSES:
        assert projector_record_page(c)["terminal"]
    assert contraction_regulator_manifest()["status"] == "TERMINAL_PROJECTOR_AUTHORITY"

def test_component_assembly_fail_closed_and_mutations():
    out=verify_current_projector_authority()
    assert out["component_assembly_complete"] is False
    with pytest.raises(RuntimeError): instantaneous_current_sparse_matrix("K9_2_N8_b0.40")
    assert static_isolation_guard()["pass"]
    assert sum(mutate_live_icreg2(i) != out for i in range(384)) == 384
