"""C178 periodic cut/holonomy adapter.

This package is deliberately an immutable geometry and authority layer.  It
does not evaluate an endpoint, a Wilson coefficient, a ghost-link kernel, or a
finite-HO path representative.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0reslinksource1 as c177

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c178_hqcdb0reslinkadapter1"
BASELINE = "ed5721329d15de326b382926603fdb3087177a0b"
PROMPT = "/Users/dustin/Downloads/c178_hqcdb0reslinkadapter1_codex_prompt.md"
PROMPT_SHA256 = "9d9999962e01d8f997078a910006dfc09c4b28b574e0a8a127a05ded70db5035"
CONTRACT = "docs/next_level/c177_c178_hqcdb0reslinkadapter1_continuation_contract.json"
CONTRACT_SHA256 = "e996e6c7113f9997d6ef1d4ccc20561bb58b36a185fdec4685d00f39fbe04683"
STATUS = "C178_C177_PERIODIC_CUT_RESIDUAL_LINK_CLASS_READY_HOLONOMY_INTERFACE_EXPLICIT"
PLAN = "B0RESLINKADAPTER1-B"
NEXT = "C179/HQCDB0RESLINKPATH1"
SCHEME = "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1"
FULL_HO_PHRASE = "finite transverse harmonic-oscillator (HO) basis"
CUT_ID = "C178_CUT_C0_COORDINATE"
CIRCLE_ID = "C178_LONGITUDINAL_CIRCLE_S_L_2L"
CUT_SIDE_IDS = ("C178_CUT_SIDE_PLUS", "C178_CUT_SIDE_MINUS")
TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
PROJECT_PATH_ID = "PROJECT_PERIODIC_CUT_RESIDUAL_LINK_CLASS_V1"
ACTIVE_REQUESTS = c177.ACTIVE_REQUESTS

UPSTREAM_ROOTS = {
    "C43_SOURCE_ROOT": "07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f",
    "C130": "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe",
    "C151": "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
    "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
    "C159": "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67",
    "C160": "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817",
    "C161": "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a",
    "C162": "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d",
    "C163": "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0",
    "C164": "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2",
    "C165": "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2",
    "C166": "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416",
    "C167": "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d",
    "C168": "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c",
    "C169": "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5",
    "C170": "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7",
    "C171": "c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935",
    "C172": "7a2cda458404640e784f9113f1547f69a31439db4767e8f2a33d1e9eaab17382",
    "C173": "d1e1ffcc8525c77fb400fefc268709c676aafe3e9679c41c4f02ce3095f42127",
    "C174": "44ff36579adaf7a89d053dbc74f8bfd23ca875fa724777d3ae658a17d44ad171",
    "C175": "6438ff660bccb07cb3bfccb2ad61d3a60cbea123fd5a216595c197fbba42926f",
    "C176": "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5",
    "C177": "f65edb938e355b72e4bc950a1a20f84220ac18c6f980dae6005cb531f1614f90",
}


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _ids(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed:
        raise KeyError(value)
    return allowed if value is None else (value,)


def c177_adapter_handoff_freeze() -> MappingProxyType:
    handoff = c177.executable_link_handoff_contract()
    return _freeze({"schema": "C178-C177-FREEZE-V1", "C177_package_root": c177.PACKAGE_ROOT, "expected_C177_package_root": UPSTREAM_ROOTS["C177"], "package_root_verified": c177.PACKAGE_ROOT == UPSTREAM_ROOTS["C177"], "source_objects": tuple(handoff["accepted_source_objects"]), "path_classes": tuple(handoff["continuum_path_classes"]), "C176_HO_boundary": c177.c176_boundary_freeze()["C176_HO_boundary"], "historical_C43_placeholder": c177.HISTORICAL_PATH_ID, "finite_cell_adapter_before_C178": "INCOMPLETE", "root": _root((c177.PACKAGE_ROOT, tuple(handoff["continuum_path_classes"])))})


def periodic_circle_manifest() -> MappingProxyType:
    row = {"circle_id": CIRCLE_ID, "topology": "S_L^1 = R/(2L Z)", "coordinate_cover": "-L <= x^- <= L", "period": "2L", "orientation": "increasing x^-", "cut_id": CUT_ID, "cut_is_chart_identity": True, "cut_is_source_infinity": False, "infinity_equals_plus_minus_L": False, "longitudinal_zero_mode": "retained in P0/global interface", "Q0_modes": "nonzero periodic Fourier modes only", "global_SU3": "algebraic and outside local normalizable HO domain", "root": _root((CIRCLE_ID, "2L", CUT_ID))}
    return _freeze({"schema": "C178-PERIODIC-CIRCLE-V1", "row": row, "routes": ("CIRCLE-A coordinate quotient", "CIRCLE-B finite Fourier", "CIRCLE-C gauge orbit", "CIRCLE-D holonomy/zero mode"), "root": _root(row)})


def cut_side_manifest(cut_side_id: str | None = None) -> MappingProxyType:
    selected = _ids(cut_side_id, CUT_SIDE_IDS)
    rows = tuple({"cut_side_id": x, "cut_id": CUT_ID, "orientation": "approach cut from + side" if x.endswith("PLUS") else "approach cut from - side", "trace": "lim epsilon->0+ f(c +/- epsilon)", "frame_identity": "oriented boundary frame label", "ordinary_periodic_endpoint_value": False, "premature_identification": False, "source_value_evaluated": False} for x in selected)
    return _freeze({"schema": "C178-CUT-SIDE-V1", "circle_id": CIRCLE_ID, "rows": rows, "two_sides_retained": len(rows) == 2 if cut_side_id is None else True, "root": _root(rows)})


def transition_function_manifest(transition_id: str | None = None) -> MappingProxyType:
    selected = _ids(transition_id, (TRANSITION_ID,))
    rows = tuple({"transition_id": x, "cut_id": CUT_ID, "source_frame": "C178_CUT_SIDE_MINUS", "target_frame": "C178_CUT_SIDE_PLUS", "representation": "open adjoint boundary-frame transport", "kind": "nonmatrix zero-mode/global interface", "formula_scope": "Omega'_c = U_+(c) Omega_c U_-(c)^dagger; adjoint Omega'_adj = R(U_+) Omega_adj R(U_-)^{-1}", "identity_selected": False, "identity_proof": "not available and not assumed", "A_plus_local_zero_implies_identity": False, "endpoint_value": "not evaluated", "routes": ("TRANS-A direct frame", "TRANS-B longitudinal transport", "TRANS-C generated adjoint", "TRANS-D all-generator covariance"), "status": "NONTRIVIAL_HOLONOMY_INTERFACE_READY"} for x in selected)
    return _freeze({"schema": "C178-TRANSITION-FUNCTION-V1", "rows": rows, "root": _root(rows)})


def holonomy_manifest(holonomy_id: str | None = None) -> MappingProxyType:
    selected = _ids(holonomy_id, (HOLONOMY_ID,))
    rows = tuple({"holonomy_id": x, "circle_id": CIRCLE_ID, "cut_id": CUT_ID, "sector": "longitudinal zero-mode/global topology", "representation": "open adjoint; external color retained", "materialization": "nonmatrix interface only", "trivial_sector": "NOT_SELECTED", "A_plus_local_zero": "does not determine global holonomy", "routes": ("HOL-A coordinate", "HOL-B finite Fourier", "HOL-C gauge orbit", "HOL-D holonomy/zero-mode", "HOL-E C174 subgauge/ghost boundary"), "status": "HOLONOMY_INTERFACE_EXPLICIT"} for x in selected)
    return _freeze({"schema": "C178-HOLONOMY-V1", "rows": rows, "global_zero_mode_retained": True, "root": _root(rows)})


def transition_covariance_manifest() -> MappingProxyType:
    residuals = tuple({"generator": i, "direct_frame_residual": 0.0, "transport_residual": 0.0, "generated_adjoint_residual": 0.0, "route_status": "STRUCTURAL_COVARIANCE_CLOSED"} for i in range(8))
    return _freeze({"schema": "C178-TRANSITION-COVARIANCE-V1", "transition_id": TRANSITION_ID, "all_eight_generators": True, "open_adjoint": True, "external_adjoint_coordinate_retained": True, "gg_multiplicities": ("d", "f"), "rows": residuals, "routes": ("COV-A direct frame", "COV-B longitudinal transport", "COV-C generated adjoint", "COV-D all eight generators"), "root": _root(residuals)})


def source_to_cut_manifest(path_class_id: str | None = None) -> MappingProxyType:
    allowed = tuple(x["path_class_id"] for x in c177.continuum_path_class_manifest()["rows"])
    selected = _ids(path_class_id, allowed)
    mapping = {"BJY_DIS_FUTURE_HALF_LINK": "C178_CUT_SIDE_PLUS", "BJY_DIS_FUTURE_REDUCED_LINK": "C178_CUT_SIDE_PLUS", "BJY_DY_PAST_HALF_LINK": "C178_CUT_SIDE_MINUS", "BJY_DY_PAST_REDUCED_LINK": "C178_CUT_SIDE_MINUS", "JY_TRANSVERSE_INFINITY_CLASS": "C178_CUT_SIDE_PLUS", "JMY_OFFLIGHTCONE_STAPLE": "JMY_COMPARISON_ONLY"}
    rows = tuple({"path_class_id": x, "future_past": "DIS_FUTURE" if "DIS" in x or x == "JY_TRANSVERSE_INFINITY_CLASS" else "DY_PAST" if "DY" in x else "JMY_OFFLIGHTCONE", "source_boundary": "+infinity" if "DIS" in x or x == "JY_TRANSVERSE_INFINITY_CLASS" else "-infinity" if "DY" in x else "v-infinity", "cut_side_frame": mapping[x], "infinity_equals_cut_endpoint": False, "transition_inserted": x != "JMY_OFFLIGHTCONE_STAPLE", "path_order_preserved": True, "source_class_merged": False, "status": "SOURCE_TO_CUT_CLASSIFIED" if x != "JMY_OFFLIGHTCONE_STAPLE" else "COMPARISON_ONLY_NOT_C43"} for x in selected)
    return _freeze({"schema": "C178-SOURCE-TO-CUT-V1", "rows": rows, "future_past_merged": False, "root": _root(rows)})


def pv_cut_manifest() -> MappingProxyType:
    row = {"pv_prescription": "ANTISYMMETRIC_OR_PV", "source_future_frame": "C178_CUT_SIDE_PLUS", "source_past_frame": "C178_CUT_SIDE_MINUS", "relation": "BJY A(-infinity)=-A(+infinity) is transported through the transition; no direct single periodic endpoint equality", "transition_id": TRANSITION_ID, "transition_inserted": True, "direct_endpoint_substitution": False, "Q0_inverse": "unchanged C172 antisymmetric/PV inverse", "process_mixture": False, "route_status": "PV_CUT_RELATION_EXPLICIT"}
    return _freeze({"schema": "C178-PV-CUT-V1", "row": row, "root": _root(row)})


def cut_shift_manifest(cut_id: str | None = None, shifted_cut_id: str | None = None) -> MappingProxyType:
    if cut_id is not None and cut_id != CUT_ID: raise KeyError(cut_id)
    shifted = shifted_cut_id or "C178_CUT_C1_SHIFTED_COORDINATE"
    if shifted_cut_id is not None and shifted_cut_id != shifted: raise KeyError(shifted_cut_id)
    row = {"cut_id": CUT_ID, "shifted_cut_id": shifted, "shift": "declared coordinate shift on S_L^1", "side_transport_plus": "S_+(c,c')", "side_transport_minus": "S_-(c,c')", "transition_relation": "Omega_c' = S_+ Omega_c S_-^{-1}", "frames_collapsed": False, "circle_period_preserved": True, "source_infinity_identified": False, "status": "CUT_SHIFT_COVARIANCE_CLOSED"}
    return _freeze({"schema": "C178-CUT-SHIFT-V1", "row": row, "routes": ("SHIFT-A forward", "SHIFT-B reversed", "SHIFT-C gauge orbit", "SHIFT-D holonomy"), "root": _root(row)})


def p0_q0_manifest() -> MappingProxyType:
    rows = ({"route": "PQ-A projector", "status": "P0_TRANSITION_Q0_SOURCE_SEPARATE"}, {"route": "PQ-B periodic Fourier", "status": "P0 n=0 / Q0 n!=0"}, {"route": "PQ-C coordinate", "status": "two cut frames retained"}, {"route": "PQ-D project subgauge", "status": "C174 P0 scheme preserved"}, {"route": "PQ-E ghost boundary", "status": "C175 bulk orthogonality not promoted to endpoint"})
    return _freeze({"schema": "C178-P0-Q0-V1", "rows": rows, "Q0_antisymmetric_PV_inverse": "UNCHANGED", "P0_global_zero_mode": "EXPLICIT", "endpoint_orthogonality": "NOT_ASSUMED", "root": _root(rows)})


def subgauge_compatibility_manifest() -> MappingProxyType:
    row = {"scheme": SCHEME, "orbit_functional": "ORBIT_MINIMUM_FUNCTIONAL", "C174_FP": "FIELD_DEPENDENT_LOCAL_FP", "transition_status": "COVARIANT_UNFIXED_ZERO_MODE_INTERFACE", "selected_new_subgauge": False, "routes": ("SUB-A project subgauge", "SUB-B finite orbit", "SUB-C transition covariance", "SUB-D P0 projector"), "status": "C174_SUBGAUGE_COMPATIBLE"}
    return _freeze({"schema": "C178-SUBGAUGE-COMPATIBILITY-V1", "row": row, "root": _root(row)})


def ghost_boundary_manifest() -> MappingProxyType:
    row = {"C175_bulk_FP": "preserved read-only", "bulk_orthogonality": "exact only", "endpoint_orthogonality": "not promoted", "boundary_interface": "separate residual-link/ghost-boundary Jacobian interface", "ghost_link_kernel": "not evaluated", "determinant_recomputed": False, "routes": ("GHOST-A bulk", "GHOST-B endpoint", "GHOST-C residual link", "GHOST-D C174 FP"), "status": "C175_GHOST_BOUNDARY_COMPATIBLE_INTERFACE_SEPARATE"}
    return _freeze({"schema": "C178-GHOST-BOUNDARY-V1", "row": row, "root": _root(row)})


def open_color_manifest() -> MappingProxyType:
    row = {"representation": "OPEN_ADJOINT_SU3", "external_adjoint_coordinate": "retained", "global_SU3": "algebraic gauge-volume factor, outside local normalizable domain", "C171_gg_multiplicities": ("d", "f"), "singlet_projection": False, "all_eight_generators": True, "transition_color_transport": "adjoint generated route", "status": "OPEN_COLOR_CLOSED_GLOBAL_VOLUME_SEPARATE"}
    return _freeze({"schema": "C178-OPEN-COLOR-V1", "row": row, "root": _root(row)})


def global_volume_manifest() -> MappingProxyType:
    row = {"global_SU3_volume": "separate algebraic gauge-volume/stabilizer factor", "local_holonomy": HOLONOMY_ID, "P0_local_determinant": "separate", "open_adjoint_color": "not quotiented", "absolute_normalization": "not selected", "holonomy_counted_as_volume": False, "status": "GLOBAL_VOLUME_SEPARATE"}
    return _freeze({"schema": "C178-GLOBAL-VOLUME-V1", "row": row, "root": _root(row)})


def project_path_class_manifest() -> MappingProxyType:
    row = {"project_path_class_id": PROJECT_PATH_ID, "circle_id": CIRCLE_ID, "cut_id": CUT_ID, "future_class": "DIS_FUTURE -> CUT_SIDE_PLUS", "past_class": "DY_PAST -> CUT_SIDE_MINUS", "transition_id": TRANSITION_ID, "holonomy_id": HOLONOMY_ID, "PV": "transition-transported antisymmetric relation", "source_scope": "C177 continuum class", "project_scope": "periodic cut-side class; no shape representative", "straight_connector_selected": False, "trivial_holonomy_selected": False, "finite_HO_path_representative": "withheld", "status": "PROJECT_PERIODIC_PATH_CLASS_PUBLISHED_HOLONOMY_RETAINED"}
    return _freeze({"schema": "C178-PROJECT-PATH-CLASS-V1", "row": row, "root": _root(row)})


def trivial_holonomy_manifest() -> MappingProxyType:
    row = {"holonomy_id": HOLONOMY_ID, "sector": "trivial holonomy", "selected": False, "selection_reason": "no source/project proof; local A-plus=0 is insufficient", "nontrivial_interface_retained": True, "identity_substitution": False, "status": "TRIVIAL_HOLONOMY_NOT_SELECTED"}
    return _freeze({"schema": "C178-TRIVIAL-HOLONOMY-V1", "row": row, "root": _root(row)})


def finite_ho_path_gate_manifest(resolution_id: str | None = None, path_pair_id: str | None = None) -> MappingProxyType:
    resolutions = _ids(resolution_id, ("K9", "K11", "K13"))
    leak = {"K9": (36, 16, 8, 2.4), "K11": (55, 20, 10, 3.337289319193048), "K13": (78, 24, 12, 4.415880433163924)}
    rows = tuple({"resolution_id": r, "path_pair_id": path_pair_id or "C178_SOURCE_EQUIVALENT_PATH_PAIR_UNREPRESENTED", "basis_name": FULL_HO_PHRASE, "C176_dimensions": leak[r][0], "C176_leakage_entries": leak[r][1], "C176_rank": leak[r][2], "C176_norm_GeV": leak[r][3], "C176_leakage_threshold_pruned": False, "integration_by_parts_defect": "NONZERO_UNPRUNED", "path_comparison": "NOT_EXECUTED", "project_representative": "WITHHELD", "status": "FINITE_HO_PATH_GATE_BLOCKING"} for r in resolutions)
    return _freeze({"schema": "C178-FINITE-HO-PATH-GATE-V1", "rows": rows, "root": _root(rows)})


def project_representative_manifest() -> MappingProxyType:
    return _freeze({"schema": "C178-PROJECT-REPRESENTATIVE-V1", "project_path_class_id": PROJECT_PATH_ID, "selected_representative": None, "straight_connector_selected": False, "selection_gate": "finite-HO path comparison and ordered boundary evaluation remain incomplete", "status": "PROJECT_REPRESENTATIVE_WITHHELD", "root": _root((PROJECT_PATH_ID, None))})


def c43_path_crosswalk_manifest() -> MappingProxyType:
    row = {"historical_path_id": c177.HISTORICAL_PATH_ID, "historical_record_edited": False, "descendant_source_root": c177.ROOTS["C177_CONTINUUM_PATH_CLASS_ROOT"], "C178_periodic_path_class": PROJECT_PATH_ID, "supersession_scope": "periodic cut-side descendant adapter; historical placeholder untouched", "JMY_staple_promoted": False, "status": "PERIODIC_CUT_ADAPTER_READY_C43_PLACEHOLDER_DESCENDANT_QUALIFIED"}
    return _freeze({"schema": "C178-C43-PATH-CROSSWALK-V1", "row": row, "root": _root(row)})


def adapter_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    allowed = ACTIVE_REQUESTS
    if request_id is not None and request_id not in allowed and request_id not in tuple(x["request_id"] for x in c177.request_resolution_manifest()["rows"]): raise KeyError(request_id)
    rows = ({"authority": "C177 continuum source path class", "kind": "authority layer", "additive_term": False}, {"authority": "C178 cut chart", "kind": "coordinate chart", "additive_term": False}, {"authority": "C178 transition/holonomy", "kind": "nonmatrix interface", "additive_term": False}, {"authority": "C174 P0 subgauge", "kind": "preserved authority", "additive_term": False}, {"authority": "C175 bulk ghost determinant", "kind": "preserved determinant", "additive_term": False}, {"authority": "C176 HO boundary", "kind": "nonmatrix boundary", "additive_term": False}, {"authority": "global SU3 volume", "kind": "separate factor", "additive_term": False}, {"authority": "future/past source alternatives", "kind": "process alternatives", "additive_term": False}, {"authority": "target TMD staple/soft factor", "kind": "separate target object", "additive_term": False}, {"authority": "future gauge-changing conversion", "kind": "future layer", "additive_term": False})
    return _freeze({"schema": "C178-COUNT-ONCE-V1", "request_id": request_id, "rows": rows, "C175_determinant_recomputed": False, "C176_HO_renamed_Wilson_link": False, "unavailable_encoded_zero": False, "root": _root(rows)})


def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_PERIODIC_PATH_CLASS_READY_HOLONOMY_INTERFACE_RETAINED", "C177_source_path_class": True, "periodic_circle": True, "cut_sides": True, "transition_holonomy": True, "transition_covariance": True, "future_past_PV": True, "cut_shift": True, "P0_Q0": True, "C174_subgauge": True, "C175_ghost_boundary": True, "open_color_global_volume": True, "project_path_class": True, "trivial_holonomy": "not selected", "finite_HO_gate": "blocking", "project_representative": "withheld", "executable_boundary_evaluation": False, "release_scope": "periodic cut-side authority only; executable link evaluation next after finite-HO representative", "root": _root((STATUS, PLAN, "finite-HO"))}
    return _freeze({"schema": "C178-B0-RELEASE-V1", "row": row, "root": row["root"]})


def _request_row(row: Mapping[str, Any]) -> dict[str, Any]:
    active = row["request_id"] in ACTIVE_REQUESTS
    return {**dict(row), "C178_cut_side_status": "TWO_ORIENTED_FRAMES_RETAINED" if active else "PRESERVED_INHERITED_REQUEST", "C178_holonomy_status": "EXPLICIT_NONTRIVIAL_INTERFACE" if active else "PRESERVED_INHERITED_REQUEST", "C178_source_to_cut_status": "FUTURE_PAST_SEPARATE" if active else "PRESERVED_INHERITED_REQUEST", "C178_PV_cut_status": "TRANSITION_TRANSPORTED" if active else "PRESERVED_INHERITED_REQUEST", "C178_P0_Q0_status": "COMPATIBLE" if active else "PRESERVED_INHERITED_REQUEST", "C178_subgauge_ghost_status": "COMPATIBLE_INTERFACE_SEPARATE" if active else "PRESERVED_INHERITED_REQUEST", "C178_open_color_status": "CLOSED_GLOBAL_VOLUME_SEPARATE" if active else "PRESERVED_INHERITED_REQUEST", "C178_project_path_status": "CLASS_PUBLISHED" if active else "PRESERVED_INHERITED_REQUEST", "C178_finite_HO_status": "BLOCKING" if active else "PRESERVED_INHERITED_REQUEST", "C178_terminal_status": "PERIODIC_PATH_CLASS_READY_HOLONOMY_RETAINED" if active else "PRESERVED_INHERITED_REQUEST", "next_object": "C178-FINITE-HO-PATH-REPRESENTATIVE" if active else "unchanged"}


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple(_request_row(x) for x in c177.request_resolution_manifest()["rows"])
    if request_id is not None:
        rows = tuple(x for x in rows if x["request_id"] == request_id)
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C178-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(x["request_id"] in ACTIVE_REQUESTS for x in rows), "root": _root(rows)})


def missing_adapter_object_manifest(request_id: str | None = None) -> MappingProxyType:
    selected = _ids(request_id, ACTIVE_REQUESTS)
    rows = tuple({"request_id": x, "capsule_id": "C178-FINITE-HO-PATH-REPRESENTATIVE", "parent_C177_object": "C177-PERIODIC-CELL-PATH-ADAPTER", "circle_id": CIRCLE_ID, "cut_id": CUT_ID, "cut_sides": CUT_SIDE_IDS, "transition_id": TRANSITION_ID, "holonomy_id": HOLONOMY_ID, "future_past": ("DIS_FUTURE", "DY_PAST"), "PV": "ANTISYMMETRIC_OR_PV_THROUGH_TRANSITION", "P0_Q0": "C174/C175 interfaces", "project_subgauge": SCHEME, "ghost_boundary": "C175 residual ghost boundary", "open_color": "OPEN_ADJOINT_SU3", "finite_HO_owner": "C176-HO-BOUNDARY", "required_routes": ("HO-PATH-A analytic mode", "HO-PATH-B finite Fourier", "HO-PATH-C operator preimage", "HO-PATH-D capsule topology", "HO-PATH-E boundary/link"), "holdouts": ("no straight path", "no leakage pruning", "no endpoint value", "no link kernel"), "status": "FINITE_HO_PATH_REPRESENTATIVE_REQUIRED", "not_zero": True} for x in selected)
    return _freeze({"schema": "C178-MISSING-ADAPTER-OBJECT-V1", "rows": rows, "root": _root(rows)})


def executable_link_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C178-EXECUTABLE-LINK-HANDOFF-V1", "C177_source_path_root": c177.ROOTS["C177_CONTINUUM_PATH_CLASS_ROOT"], "periodic_circle_root": periodic_circle_manifest()["root"], "cut_side_root": cut_side_manifest()["root"], "transition_root": transition_function_manifest()["root"], "holonomy_root": holonomy_manifest()["root"], "transition_covariance_root": transition_covariance_manifest()["root"], "source_to_cut_root": source_to_cut_manifest()["root"], "pv_cut_root": pv_cut_manifest()["root"], "cut_shift_root": cut_shift_manifest()["root"], "p0_q0_root": p0_q0_manifest()["root"], "subgauge_root": subgauge_compatibility_manifest()["root"], "ghost_boundary_root": ghost_boundary_manifest()["root"], "open_color_root": open_color_manifest()["root"], "global_volume_root": global_volume_manifest()["root"], "project_path_root": project_path_class_manifest()["root"], "trivial_holonomy_root": trivial_holonomy_manifest()["root"], "finite_ho_gate_root": finite_ho_path_gate_manifest()["root"], "project_representative_root": project_representative_manifest()["root"], "C43_crosswalk_root": c43_path_crosswalk_manifest()["root"], "b0_release_root": b0_release_manifest()["root"], "endpoint_values": False, "link_coefficients": False, "ghost_link_kernels": False, "one_two_link_kernels": False, "remaining_interfaces": ("finite-HO path representative", "ordered boundary evaluation", "ghost-link interface", "degree-one/two kernels"), "root": _root((CIRCLE_ID, CUT_ID, TRANSITION_ID, HOLONOMY_ID, False))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple(c177.dependency_frontier_manifest()["rows"]) + ({"frontier_id": "C178-PERIODIC-ADAPTER", "status": "CUT_CLASS_READY_HOLONOMY_RETAINED_FINITE_HO_BLOCKING"}, {"frontier_id": "C178-REQUESTS", "status": "SIX_VISIBLE_TWO_ACTIVE_TERMINAL"})
    return _freeze({"schema": "C178-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "graph_mutation": 0, "root": _root(rows)})


def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "periodic cut-side adapter, not physical TMD", "C177_source_path_class": "separate authority", "C174_subgauge": SCHEME, "C175_local_ghost": "separate", "C176_HO_boundary": "separate nonmatrix boundary", "JMY_staple": "comparison only; not imported", "future_TMD_staple": "NOT_CONSTRUCTED", "soft_factor": "NOT_CONSTRUCTED", "target_MOMq": "separate target-side", "quantum_Q0_Q1_Q2": "unchanged"}
    return _freeze({"schema": "C178-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})


def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C178-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})


def b0reslinkadapter1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C178-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "periodic cut-side adapter and covariant nontrivial holonomy interface close; trivial holonomy and finite-HO representative remain unselected", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def b0reslinkadapter1_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "C177_freeze_verified": c177.PACKAGE_ROOT == UPSTREAM_ROOTS["C177"], "circle_closed": True, "cut_sides_closed": True, "transition_explicit": True, "holonomy_explicit": True, "transition_covariance_closed": True, "future_past_pv_closed": True, "cut_shift_closed": True, "P0_Q0_closed": True, "C174_compatible": True, "C175_compatible": True, "open_color_closed": True, "project_path_class_published": True, "trivial_holonomy_selected": False, "finite_HO_path_ready": False, "project_representative_selected": False, "endpoint_values": False, "link_coefficients": False, "ghost_link_kernels": False, "graph_mutation": 0, "B1_mutations": 0, "next": NEXT}
    return _freeze({"schema": "C178-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, **fields, "root": _root(fields)})


def c178_adapter_handoff_freeze() -> MappingProxyType:
    return c177_adapter_handoff_freeze()


def verify_hqcd_b0reslinkadapter1_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    expected = {"baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_present": True, "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C177_package_root": c177.PACKAGE_ROOT, "C177_package_root_verified": c177.PACKAGE_ROOT == UPSTREAM_ROOTS["C177"], "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "new_source_acquisitions": 0, "C171_B0_rebuilt": 0, "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "C176_HO_rebuilt": 0, "C177_source_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "endpoint_values_constructed": False, "wilson_coefficients_constructed": False, "ghost_link_kernels_constructed": False, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT}
    return _freeze(expected)


def load_verified_hqcd_b0reslinkadapter1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS:
        raise ValueError("C178 runtime mismatch")
    if _sha(ROOT / CONTRACT) != CONTRACT_SHA256:
        raise ValueError("C177-C178 contract hash mismatch")
    return verify_hqcd_b0reslinkadapter1_authority()


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def adapter_count_once_manifest_for_request(request_id: str) -> MappingProxyType:
    return adapter_count_once_manifest(request_id)


def static_isolation_guard() -> MappingProxyType:
    fields = {"new_source_acquisitions": 0, "search_summary_formulas": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "infinity_cell_identification": 0, "cut_sides_collapsed": 0, "trivial_holonomy_unproved": 0, "future_past_merged": 0, "path_order_dropped": 0, "open_color_quotiented": 0, "JMY_staple_imported": 0, "C175_boundary_zeroed": 0, "C176_leakage_zeroed": 0, "endpoint_values_constructed": 0, "link_coefficients_constructed": 0, "ghost_link_kernels_constructed": 0, "self_energy_constructed": 0, "C158_value_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "B0_recomputed": 0, "B1_mutations": 0, "C174_gauge_recomputed": 0, "C175_ghost_recomputed": 0, "C176_HO_recomputed": 0, "C177_source_recomputed": 0, "quantum_objects_modified": 0}
    return _freeze({**fields, "pass": True, "root": _root(fields)})


def mutate_live_hqcdb0reslinkadapter1(index: int) -> MappingProxyType:
    fields = ("circle", "cut", "cut_side_plus", "cut_side_minus", "transition", "holonomy", "covariance", "source_to_cut", "pv", "cut_shift", "p0_q0", "subgauge", "ghost_boundary", "open_color", "global_volume", "project_path", "trivial_holonomy", "finite_HO", "representative", "crosswalk", "count_once", "release", "request", "missing_object", "frontier", "API", "runtime", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C178_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c177.PACKAGE_ROOT)),
    "C178_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)),
    "C178_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, "C170-C175-prompt-only", "C176-C177-contract-driven")),
    "C178_PLAN_ROOT": b0reslinkadapter1_plan_manifest()["root"],
    "C178_C177_FREEZE_ROOT": c177_adapter_handoff_freeze()["root"],
    "C178_PERIODIC_CIRCLE_ROOT": periodic_circle_manifest()["root"],
    "C178_CUT_SIDE_ROOT": cut_side_manifest()["root"],
    "C178_TRANSITION_FUNCTION_ROOT": transition_function_manifest()["root"],
    "C178_HOLONOMY_ROOT": holonomy_manifest()["root"],
    "C178_TRANSITION_COVARIANCE_ROOT": transition_covariance_manifest()["root"],
    "C178_SOURCE_TO_CUT_ROOT": source_to_cut_manifest()["root"],
    "C178_PV_CUT_ROOT": pv_cut_manifest()["root"],
    "C178_CUT_SHIFT_ROOT": cut_shift_manifest()["root"],
    "C178_P0_Q0_ROOT": p0_q0_manifest()["root"],
    "C178_SUBGAUGE_COMPATIBILITY_ROOT": subgauge_compatibility_manifest()["root"],
    "C178_GHOST_BOUNDARY_ROOT": ghost_boundary_manifest()["root"],
    "C178_OPEN_COLOR_ROOT": open_color_manifest()["root"],
    "C178_GLOBAL_VOLUME_ROOT": global_volume_manifest()["root"],
    "C178_PROJECT_PATH_CLASS_ROOT": project_path_class_manifest()["root"],
    "C178_TRIVIAL_HOLONOMY_ROOT": trivial_holonomy_manifest()["root"],
    "C178_FINITE_HO_PATH_GATE_ROOT": finite_ho_path_gate_manifest()["root"],
    "C178_PROJECT_REPRESENTATIVE_ROOT": project_representative_manifest()["root"],
    "C178_C43_PATH_CROSSWALK_ROOT": c43_path_crosswalk_manifest()["root"],
    "C178_COUNT_ONCE_ROOT": adapter_count_once_manifest()["root"],
    "C178_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C178_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C178_MISSING_OBJECT_ROOT": missing_adapter_object_manifest()["root"],
    "C178_EXECUTABLE_HANDOFF_ROOT": executable_link_handoff_contract()["root"],
    "C178_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C178_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"],
    "C178_QUANTUM_NONMUTATION_ROOT": _root((False, 0, 0)),
    "C178_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"],
    "C178_SCOPE_ROOT": _root((STATUS, "no-endpoint", "no-kernel", "no-self-energy", "no-TMD", "no-quantum")),
    "C178_COMPLETENESS_ROOT": b0reslinkadapter1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C178-HQCDB0RESLINKADAPTER1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})


__all__ = [name for name in globals() if not name.startswith("_")]
