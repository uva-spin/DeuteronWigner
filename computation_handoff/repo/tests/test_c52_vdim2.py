"""C52 component interface closes without splitting C50 numerically."""
import numpy as np
import pytest

from deuteron_wigner.bridge.vdim2.core import (
    COMPONENT_ID, STATUS, apply_colorless_vertex_components,
    assemble_colorless_component_family, component_vocabulary, mutate_live_c52,
    run_c52_checks, runtime_raw_tuple_poisoning, validate_c52,
)


def test_c52_source_component_is_one_action_level_bilinear():
    vocabulary=component_vocabulary()
    assert vocabulary["independent_components"][0]["id"] == COMPONENT_ID
    assert len(vocabulary["independent_components"]) == 1
    assert all(x["classification"] == "SUBTERM_NOT_SEPARATELY_GAUGE_OR_OPERATOR_MEANINGFUL" for x in vocabulary["subterms"])


def test_c52_recomposes_c50_and_retains_raw_tuple_independence():
    result=run_c52_checks()
    assert result["status"] == STATUS and result["pass"]
    assert runtime_raw_tuple_poisoning()["pass"]


def test_c52_matrix_free_colorless_action_is_not_stored_matrix_action():
    family=assemble_colorless_component_family("K9_2_N8_b0.40")
    vector=np.array([1+2j,-.4+.3j],complex); direct=apply_colorless_vertex_components(vector,"K9_2_N8_b0.40")["sum"]
    assert np.linalg.norm(direct-family["diagnostic_m2"].dot(vector)) < 2e-12


@pytest.mark.parametrize("fault_id",range(224))
def test_c52_224_live_component_mutations_fail(fault_id):
    assert not validate_c52(mutate_live_c52(fault_id))
