"""Verify C43 contains a matrix-element-ready physical mode contract before C44."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4]
STATUS="C44_MODE_PROJECTION_INCOMPLETE"
REQUIRED=("finite longitudinal cell length and normalization measure","explicit normalized 2D-HO mode functions and phase convention","source-derived spinor/polarization convention translated to basis overlaps","global-color/zero-mode projection compatible with colored matching probes")
def _read(name): return json.loads((ROOT/"docs/next_level"/name).read_text())
def projection_audit():
    mode=_read("c43_mode_expansion_contract.json"); contract=_read("c43_finite_basis_projection_contract.json"); plan=_read("c43_physical_resolution_plan.json")
    return {"status":STATUS,"C43_mode_status":mode["status"],"C43_projection_status":contract["status"],"physical_resolutions":plan["resolutions"],"missing_matrix_element_inputs":list(REQUIRED),"decision":"C43 freezes interfaces and resolutions, but does not supply the source-qualified finite-volume mode and global-constraint data needed to produce a unique numerical C44 overlap/matrix."}
def validate_projection_audit(a): return a==projection_audit()
def assert_mode_projection_incomplete():
    a=projection_audit(); assert a["status"]==STATUS and a["C43_projection_status"]=="COMPLETE_INTERFACE_ONLY" and len(a["missing_matrix_element_inputs"])==4
    return a
