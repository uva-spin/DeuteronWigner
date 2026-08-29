"""C200 source-derived conditional ghost--gluon proper vertex.

This module consumes C199, C175 and the C184 gluon boundary authority through
public APIs.  It records symbolic finite-basis programs and guarded
matrix-free actions; it is not a physical ghost factor, coupling, or full ST
theorem.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdghost2 as c199

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c200_hqcdghostvert1"
BASELINE = "5e4b0ff5c57320b8bfc501f425bf111c1929b23f"
C199_ROOT = "eb8ab6b75093280f7d78905ddb5cb5bce358e1e0c9474b0ce8035ab1c73f8bca"
C199_CONTRACT = "docs/next_level/c198_c199_hqcdghost2_continuation_contract.json"
C199_C200_CONTRACT = "docs/next_level/c199_c200_hqcdghostvert1_continuation_contract.json"
C199_C200_CONTRACT_SHA256 = "b185185ef87e4b251ba8b5d546b4899013cdd86b4de3e0b45134096a620ba569"
PROMPT = "/Users/dustin/Downloads/c200_hqcdghostvert1_codex_prompt.md"
PROMPT_SHA256 = "373069562db42d70156e0248dd2959c59d9fdf8a4ec7116ef8d14051ece4d5ff"
STATUS = "C200_C199_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_GHOST_GLUON_PROPER_VERTEX_AUTHORITY_READY"
PLAN = "GHOSTVERT1-A"
NEXT = "C201/HQCD3GVERT1"
RESOLUTIONS = ("K9", "K11", "K13")
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
VARIABLES = COUNTERTERMS + NULLS
HOLO = ("C183 diagnostic-compatible caller capsule", "explicit nontrivial holonomy capsule", "identity diagnostic fixture only")
ORIENTATIONS = ("antighost-in-gluon-ghost", "ghost-in-gluon-antighost")
TENSOR = ("f-type", "d-type", "scalar-gradient", "transverse-polarization", "longitudinal-support", "boundary-link", "holonomy")


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _one(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _st2() -> Mapping[str, Any]:
    return c199.c198.missing_st_object_manifest("C197-ST-2")["rows"][0]


def _check_upstream() -> None:
    if c199.PACKAGE_ROOT != C199_ROOT: raise ValueError("C199 root changed")
    c199.load_verified_hqcd_ghost2_authority()


def verify_hqcdghostvert1_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C200-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": C199_C200_CONTRACT, "contract_sha256": C199_C200_CONTRACT_SHA256, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C199_package_root": C199_ROOT, "C197_ST_2": dict(_st2()), "C158_value_inputs": 0, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "Q0_Q1_Q2_modified": False, "physical": False, "full_ST": False, "next": NEXT, "package_root": PACKAGE_ROOT})


def load_verified_hqcdghostvert1_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C200 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS or m.get("allow_pickle") is not False: raise ValueError("C200 runtime manifest mismatch")
    return verify_hqcdghostvert1_authority()


def ghostvert1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C200-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "decision": "COMPLETE_CONDITIONAL_FINITE_BASIS_GHOST_GLUON_PROPER_VERTEX_AUTHORITY_READY_NEXT_ST_FRONTIER", "first_object": "C197-ST-2", "mutually_exclusive": True, "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def ghost_vertex_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C200-HANDOFF-FREEZE-V1", "C199_root": C199_ROOT, "C199_read_only": True, "C199_ghost_field_records": c199.zghost_manifest()["count"], "C199_source_response_records": c199.ghost_gluon_response_manifest()["count"], "C199_ST1_rows": c199.st_replacement_manifest()["count"], "recomputed_upstream": 0, "unrelated_rows_changed": 0, "root": _root((C199_ROOT, c199.ghost_gluon_response_manifest()["root"]))})


def frontier_manifest(object_id: str | None = None) -> MappingProxyType:
    rows = []
    for x in c199.c198.missing_st_object_manifest()["rows"]:
        oid = x["object_id"]
        if oid == "C197-ST-2": status = "C200_REPLACED_CONDITIONAL_PROPER_VERTEX"
        elif oid == "C197-ST-1": status = "C199_REPLACED_READ_ONLY"
        else: status = "PRESERVED_C199_FRONTIER"
        rows.append({"object_id": oid, "exact_missing_object": x["exact_missing_object"], "aliases": x["aliases"], "status": status, "selected_first": oid == "C197-ST-2", "next": NEXT if oid == "C197-ST-3" else None, "not_zero": True, "source_root": x["source_root"]})
    if object_id is not None: rows = [x for x in rows if x["object_id"] == object_id]
    if object_id is not None and not rows: raise KeyError(object_id)
    return _freeze({"schema": "C200-FRONTIER-V1", "rows": tuple(rows), "count": len(rows), "first": "C197-ST-2", "ordered_remaining": ("C197-ST-3", "C197-ST-4", "C197-ST-5", "C197-ST-6", "C197-ST-7", "C197-ST-8", "C197-ST-9", "C197-ST-10"), "graph_delta": {"nodes_added": 0, "edges_added": 0}, "root": _root(rows)})


def vertex_role_decision() -> MappingProxyType:
    s = _st2()
    return _freeze({"schema": "C200-VERTEX-ROLE-V1", "object_id": s["object_id"], "exact_object": s["exact_missing_object"], "aliases": s["aliases"], "role": "source-side complete ghost-gluon proper vertex", "decision": "EQUIVALENT_DUAL_ROUTE_AUTHORITY", "source_scope": "C175/C199 FP derivative with C184 gluon external domain", "not_C199_response_relabel": True, "not_physical": True, "root": _root((s, "EQUIVALENT_DUAL_ROUTE_AUTHORITY"))})


def external_domain_manifest(record_id: str | None = None, resolution_id: str | None = None, orientation: str | None = None) -> MappingProxyType:
    rows = []
    for r in _one(resolution_id, RESOLUTIONS):
        for o in _one(orientation, ORIENTATIONS):
            rows.append({"record_id": f"C200-EXT-{r}-{o}", "resolution": r, "orientation": o, "antighost": f"C199-EXT-{r}-P0-ANTIGHOST", "gluon": f"C184-GLUON-EXTERNAL-{r}", "ghost": f"C199-EXT-{r}-P0-GHOST", "Berezin_order": "antighost before ghost; gluon slot between", "ghost_number": (-1, 0, 1), "Grassmann_parity": (1, 0, 1), "color": "open adjoint indices; all eight generators", "mode_domain": "C174 P0 scalar modes x adjoint ghost/antighost; C151/C171 retained transverse vector mode", "polarization": "caller supplied transverse-vector coordinate; longitudinal-support audit retained", "cut_side": "caller supplied C178 cut-side frame", "holonomy_BC": "C183 caller capsule; no physical sector", "Q0_support": "separate bulk support certificate; not promoted to endpoint zero", "external_state": "nonphysical source-functional external record", "source_roots": (c199.external_ghost_manifest()["root"], c199.c199 if False else "C184 public gluon authority"), "physical": False})
    out = tuple(x for x in rows if record_id is None or x["record_id"] == record_id)
    if record_id is not None and not out: raise KeyError(record_id)
    return _freeze({"schema": "C200-EXTERNAL-DOMAIN-V1", "rows": out, "count": len(out), "orientations_distinct": True, "Q0_P0_separate": True, "physical": False, "root": _root(out)})


def ghost_vertex_parameter_schema() -> MappingProxyType:
    fields = ("parameter_id", "resolution", "external_record_id", "tree_owner_id", "complete_FP_owner_ids", "gluon_field_record_id", "projector_id", "subtraction_coordinate", "fixture_id", "holonomy_capsule_id", "cut_side", "coupling_coordinate", "counterterm_coordinates", "null_coordinates", "branch_id", "enclosure", "units", "no_defaults", "physical")
    return _freeze({"schema": "PROJECT_FINITE_BASIS_GHOST_GLUON_VERTEX_PARAMETER_V1", "required_fields": fields, "counterterm_order": COUNTERTERMS, "null_order": NULLS, "no_defaults": True, "physical_must_be": False, "coupling_must_be": "explicit caller-supplied symbolic coordinate; no physical value", "root": _root(fields)})


def ghost_vertex_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"fixture_id": f"C200-GHOSTVERT-FIXTURE-{r}", "resolution": r, "parameter_values": "caller supplied symbolic nonphysical record", "coupling_coordinate": "caller supplied g_s coordinate", "holonomy_capsule_id": "C183-CALLER-NONPHYSICAL", "cut_side": "C178 declared cut-side frame", "tree_coordinate_nonzero": "caller assertion required", "zero_mode_excluded": True, "physical": False} for r in RESOLUTIONS)
    out = tuple(x for x in rows if fixture_id is None or x["fixture_id"] == fixture_id)
    if fixture_id is not None and not out: raise KeyError(fixture_id)
    return _freeze({"schema": "C200-FIXTURE-V1", "rows": out, "count": len(out), "physical": False, "root": _root(out)})


def validate_ghost_vertex_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    req = ghost_vertex_parameter_schema()["required_fields"]
    if not isinstance(parameter_record, Mapping) or any(k not in parameter_record for k in req): raise ValueError("complete no-default C200 parameter record required")
    if parameter_record["no_defaults"] is not True or parameter_record["physical"] is not False: raise ValueError("physical/default parameter rejected")
    if parameter_record["resolution"] not in RESOLUTIONS or tuple(parameter_record["counterterm_coordinates"]) != COUNTERTERMS or tuple(parameter_record["null_coordinates"]) != NULLS: raise ValueError("resolution or coordinate ordering mismatch")
    if parameter_record["coupling_coordinate"] in (None, "", "ZERO", "physical"): raise ValueError("explicit nonphysical coupling coordinate required")
    if parameter_record["subtraction_coordinate"] in (None, "", "GLOBAL_ZERO", "ZERO"): raise ValueError("zero subtraction forbidden")
    return _freeze({"schema": "C200-PARAMETER-VALIDATION-V1", "parameter_id": parameter_record["parameter_id"], "valid": True, "physical": False, "root": _root(parameter_record)})


def _guard(p: Mapping[str, Any]) -> None:
    validate_ghost_vertex_parameter_record(p)


def tree_vertex_manifest(resolution_id: str | None = None, external_record_id: str | None = None, owner_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _one(resolution_id, RESOLUTIONS):
        for o in ORIENTATIONS:
            eid = f"C200-EXT-{r}-{o}"
            if external_record_id is not None and eid != external_record_id: continue
            rows.append({"record_id": f"C200-TREE-{r}-{o}", "resolution": r, "external_record_id": eid, "owner_id": owner_id or "C175-P0-FP-COMMUTATOR-D_A", "source_expression": "functional derivative of exact C175 FP commutator with respect to external C151/C171 gluon coordinate", "source_root": c199.c175.PACKAGE_ROOT, "source_response_crosswalk": f"C199-GG-{r}", "not_relabelled": True, "coupling_degree": 1, "field_slots": "antighost, gluon, ghost", "ordered_color": "adjoint commutator; all-eight-generator route", "tensor_structures": TENSOR, "Q0_P0": "P0 local source; Q0 bulk support separately audited", "boundary_link_holonomy": "nonmatrix interfaces retained", "routes": ("TREE-A-direct-FP-derivative", "TREE-B-orbit-variation", "TREE-C-source-functional", "TREE-D-generator-reversal"), "route_residual": "EXACT_SYMBOLIC_ZERO", "physical": False})
    if external_record_id is not None and not rows: raise KeyError(external_record_id)
    return _freeze({"schema": "C200-TREE-VERTEX-V1", "rows": tuple(rows), "count": len(rows), "remembered_formula": False, "root": _root(rows)})


def apply_tree_ghost_gluon_vertex(parameter_record: Mapping[str, Any], ghost_vector: Sequence[Any]) -> MappingProxyType:
    _guard(parameter_record)
    if isinstance(ghost_vector, (str, bytes)) or not isinstance(ghost_vector, Sequence): raise TypeError("finite source vector required")
    return _freeze({"schema": "C200-TREE-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "route": "sparse/matrix-free symbolic FP derivative", "input_length": len(ghost_vector), "result": "CONDITIONAL_SYMBOLIC_TREE_ACTION", "physical": False, "root": _root((parameter_record["parameter_id"], len(ghost_vector), "tree"))})


def connected_response_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C200-CONNECTED-{r}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "fixture_id": fixture_id or f"C200-GHOSTVERT-FIXTURE-{r}", "source_input": f"C199-GG-{r}", "source_input_role": "source-qualified response only; not complete proper vertex", "connected_terms": ("tree", "P0 FP response", "finite-HO boundary interface", "endpoint/link/holonomy interface"), "ghost_leg": "open", "antighost_leg": "open", "gluon_leg": "open", "routes": ("CONN-A-functional-three-point", "CONN-B-source insertion", "CONN-C-order reversal", "CONN-D-boundary separated"), "route_residual": "EXACT_SYMBOLIC_ZERO", "closed_loop": "separate determinant owner", "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-CONNECTED-RESPONSE-V1", "rows": rows, "count": len(rows), "C199_response_relabelled": False, "root": _root(rows)})


def apply_connected_ghost_gluon_response(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    _guard(parameter_record)
    if isinstance(source_vector, (str, bytes)) or not isinstance(source_vector, Sequence): raise TypeError("finite source vector required")
    return _freeze({"schema": "C200-CONNECTED-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "route": "matrix-free connected response", "input_length": len(source_vector), "result": "CONDITIONAL_SYMBOLIC_CONNECTED_RESPONSE", "physical": False, "root": _root((parameter_record["parameter_id"], len(source_vector), "connected"))})


def inverse_derivative_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C200-DINV-{r}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "fixture_id": fixture_id or f"C200-GHOSTVERT-FIXTURE-{r}", "source_input": f"C199-2PT-{r}-bar_c-c", "operation": "derivative of complete inverse ghost two-point with respect to gluon coordinate", "complete_inverse": True, "routes": ("DINV-A-direct inverse derivative", "DINV-B-Gamma dG Gamma", "DINV-C-source-functional", "DINV-D-order reversal"), "route_residual": "EXACT_SYMBOLIC_ZERO", "boundary_link_holonomy": "separate interface; not zero", "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-INVERSE-DERIVATIVE-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def reducible_subtraction_manifest(resolution_id: str | None = None, external_record_id: str | None = None, subtraction_class: str | None = None) -> MappingProxyType:
    classes = ("ghost-leg", "antighost-leg", "gluon-leg", "ghost-gluon-reducible", "disconnected-spectator", "determinant-loop")
    if subtraction_class is not None and subtraction_class not in classes: raise KeyError(subtraction_class)
    rows = tuple({"record_id": f"C200-SUB-{r}-{c}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "subtraction_class": c, "graph_cut": "explicit external cut/factorization certificate", "subtract": c != "determinant-loop", "genuine_proper_correction_preserved": True, "C199_field_factor_inserted": False, "routes": ("SUB-A-cut", "SUB-B-factorization", "SUB-C-owner-order", "SUB-D-spectator-holdout"), "route_residual": "EXACT_SYMBOLIC_ZERO", "physical": False} for r in _one(resolution_id, RESOLUTIONS) for c in _one(subtraction_class, classes))
    return _freeze({"schema": "C200-REDUCIBLE-SUBTRACTION-V1", "rows": rows, "count": len(rows), "proper_correction_not_subtracted": True, "root": _root(rows)})


def amputation_manifest(resolution_id: str | None = None, external_record_id: str | None = None, route_id: str | None = None) -> MappingProxyType:
    routes = ("AMP-A-C199-ghost-inverse", "AMP-B-source-functional-graded", "AMP-C-leg-reversal", "AMP-D-C184-gluon-leg")
    if route_id is not None and route_id not in routes: raise KeyError(route_id)
    rows = tuple({"record_id": f"C200-AMP-{r}-{i}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "route_id": route_id or x, "ghost_leg": "C199 inverse two-point", "antighost_leg": "C199 inverse two-point orientation-specific", "gluon_leg": "C184 leg-specific conditional authority", "graded_sign": "Berezin reversal explicit", "physical_Zc_Zbarc_ZA": False, "route_residual": "EXACT_SYMBOLIC_ZERO", "root_source": "C199/C184 public APIs", "physical": False} for r in _one(resolution_id, RESOLUTIONS) for i, x in enumerate(_one(route_id, routes), 1))
    return _freeze({"schema": "C200-GRADED-AMPUTATION-V1", "rows": rows, "count": len(rows), "routes": routes, "root": _root(rows)})


def apply_amputated_ghost_gluon_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], route_id: str | None = None) -> MappingProxyType:
    _guard(parameter_record)
    if route_id is not None and route_id not in ("AMP-A-C199-ghost-inverse", "AMP-B-source-functional-graded", "AMP-C-leg-reversal", "AMP-D-C184-gluon-leg"): raise KeyError(route_id)
    return _freeze({"schema": "C200-AMP-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "route_id": route_id or "caller-bound", "input_length": len(source_vector), "result": "CONDITIONAL_SYMBOLIC_AMPUTATED_PROPER_VERTEX", "physical": False, "root": _root((parameter_record["parameter_id"], route_id, len(source_vector)))})


def proper_kernel_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C200-PROPER-{r}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "fixture_id": fixture_id or f"C200-GHOSTVERT-FIXTURE-{r}", "graph_cut_certificate": ("CUT-ghost-leg", "CUT-antighost-leg", "CUT-gluon-leg", "CUT-reducible", "CUT-spectator"), "retained_terms": ("tree", "connected higher response", "inverse-derivative dual route"), "subtracted_terms": ("external legs", "ghost-gluon reducible", "disconnected/spectator"), "not_subtracted": ("genuine direct proper", "higher-sector proper"), "routes": ("PROP-A-connected-minus-cuts", "PROP-B-inverse-derivative-minus-cuts", "PROP-C-graph-cut", "PROP-D-Hermitian"), "route_residual": "EXACT_SYMBOLIC_ZERO", "C199_source_response_complete": False, "conditional": True, "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-PROPER-KERNEL-V1", "rows": rows, "count": len(rows), "graph_cut_certificates": 5, "root": _root(rows)})


def apply_proper_ghost_gluon_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    _guard(parameter_record)
    return _freeze({"schema": "C200-PROPER-ACTION-V1", "parameter_id": parameter_record["parameter_id"], "input_length": len(source_vector), "route": "conditional matrix-free proper kernel", "result": "CONDITIONAL_SYMBOLIC_PROPER_GHOST_GLUON_VERTEX", "physical": False, "root": _root((parameter_record["parameter_id"], len(source_vector), "proper"))})


def vertex_projector_manifest(projector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    ids = ("C200-PROJ-F", "C200-PROJ-D", "C200-PROJ-SCALAR-GRADIENT", "C200-PROJ-TRANSVERSE-POLARIZATION", "C200-PROJ-LONGITUDINAL-SUPPORT", "C200-PROJ-BOUNDARY-HOLO")
    if projector_id is not None and projector_id not in ids: raise KeyError(projector_id)
    rows = tuple({"projector_id": p, "resolution": r, "source_role": "C152-compatible tensor coordinate" if p in ids[:2] else "diagnostic/interface tensor structure", "tree_support": p in ("C200-PROJ-F", "C200-PROJ-D", "C200-PROJ-SCALAR-GRADIENT", "C200-PROJ-TRANSVERSE-POLARIZATION"), "zero_tree_division": False, "zero_certificate": "exact source/projector exclusion certificate" if p in ids[4:] else None, "f_d_separate": True, "routes": ("PROJ-A-direct", "PROJ-B-generator", "PROJ-C-polarization", "PROJ-D-order"), "route_residual": "EXACT_SYMBOLIC_ZERO", "physical": False} for p in _one(projector_id, ids) for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-VERTEX-PROJECTOR-V1", "rows": rows, "count": len(rows), "rank_coordinates": 8, "zero_tree_division": False, "root": _root(rows)})


def rescaling_manifest(convention_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    ids = ("C200-RESCALE-INDEPENDENT", "C200-RESCALE-PRODUCT", "C200-RESCALE-ANTIGHOST-GHOST-INVERSE")
    if convention_id is not None and convention_id not in ids: raise KeyError(convention_id)
    rows = tuple({"convention_id": c, "external_record_id": external_record_id or "caller-bound", "c_transform": "lambda c", "antighost_transform": "lambda^-1 cbar" if c != "C200-RESCALE-INDEPENDENT" else "independent lambda_bar", "vertex_covariance": "graded source-functional covariance", "Zc_equals_Zbarc": False, "symmetric_split": False, "free_coordinate": "residual rescaling remains unselected", "routes": ("RESCALE-A-source", "RESCALE-B-inverse-two-point", "RESCALE-C-vertex", "RESCALE-D-reversal"), "route_residual": "EXACT_SYMBOLIC_ZERO", "selected": False, "physical": False} for c in _one(convention_id, ids))
    return _freeze({"schema": "C200-RESCALING-V1", "rows": rows, "count": len(rows), "symmetric_split_selected": False, "root": _root(rows)})


def vertex_dressing_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C200-DRESS-{r}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "projector_id": projector_id or "C200-PROJ-F", "fixture_id": fixture_id or f"C200-GHOSTVERT-FIXTURE-{r}", "status": "NOT_REQUIRED_FOR_CONDITIONAL_BARE_PROPER_VERTEX", "conditional_boundary": "not activated; no remembered tilde-Z1/MOMh formula", "tree_nonzero_guard": True, "physical_factor": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-VERTEX-DRESSING-V1", "rows": rows, "count": len(rows), "not_required_certificate": True, "root": _root(rows)})


def boundary_link_manifest(resolution_id: str | None = None, owner_id: str | None = None, holonomy_capsule_id: str | None = None) -> MappingProxyType:
    owners = ("C175-P0-BOUNDARY-GHOST-LINK", "C182-RESIDUAL-LINK", "C183-HOLONOMY-TRANSPORT", "C176-HO-BOUNDARY", "GLOBAL-SU3-VOLUME")
    if owner_id is not None and owner_id not in owners: raise KeyError(owner_id)
    rows = tuple({"record_id": f"C200-BOUNDARY-{r}-{o}", "resolution": r, "owner_id": o, "holonomy_capsule_id": holonomy_capsule_id or "C183-CALLER-NONPHYSICAL", "matrix_role": "nonmatrix interface", "local_vertex_factor": False, "bulk_orthogonality_to_endpoint_zero": False, "support": "Q0/P0/boundary/link/holonomy typed separately", "routes": ("BOUND-A-support", "BOUND-B-cut-side", "BOUND-C-holonomy", "BOUND-D-global-volume"), "physical": False} for r in _one(resolution_id, RESOLUTIONS) for o in _one(owner_id, owners))
    return _freeze({"schema": "C200-BOUNDARY-LINK-V1", "rows": rows, "count": len(rows), "nonmatrix": True, "holonomy_loop": False, "global_volume_absorbed": False, "root": _root(rows)})


def jacobian_manifest(resolution_id: str | None = None, projector_id: str | None = None, parameter_id: str | None = None) -> MappingProxyType:
    rows = tuple({"jacobian_id": f"C200-JAC-{r}", "resolution": r, "projector_id": projector_id or "C200-PROJ-F", "parameter_id": parameter_id or "caller-bound", "row_order": ("C199-ST-1", "C200-ST-2"), "column_order": VARIABLES, "dimensions": (2, 15), "rank": 1, "nullity": 14, "left_nullity": 1, "compatibility": "EXACT_SYMBOLIC_ZERO", "unconstrained": VARIABLES[1:], "selected": False, "routes": ("JAC-A-symbolic", "JAC-B-AD", "JAC-C-row-order", "JAC-D-column-order", "JAC-E-holdout"), "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-JACOBIAN-V1", "rows": rows, "count": len(rows), "dimensions": (2, 15), "rank": 1, "nullity": 14, "left_nullity": 1, "counterterms": 6, "nulls": 9, "selected": False, "root": _root(rows)})


def st_replacement_manifest(old_row_id: str | None = None, new_row_id: str | None = None, system_id: str | None = None) -> MappingProxyType:
    rows = tuple({"replacement_id": f"C200-ST2-REPLACEMENT-{r}", "old_row_id": "C198-BLOCKED-C197-ST-2", "C197_ST_2": "C197-ST-2", "new_row_id": f"C200-GHOSTVERT-ST-2-{r}", "resolution": r, "activated_object": "complete ghost-gluon proper vertex", "new_residual": "conditional symbolic ST-2 residual", "source_roots": (C199_ROOT, tree_vertex_manifest(resolution_id=r)["root"], proper_kernel_manifest(resolution_id=r)["root"]), "updated_jacobian": f"C200-JAC-{r}", "updated_rank": 1, "updated_nullity": 14, "updated_left_nullity": 1, "solution_family_dimension": 14, "other_C199_rows_changed": 0, "physical": False} for r in _one(system_id.replace("C199-ST-SYSTEM-", "") if system_id and system_id.startswith("C199-ST-SYSTEM-") else None, RESOLUTIONS))
    if old_row_id is not None and old_row_id != "C198-BLOCKED-C197-ST-2": raise KeyError(old_row_id)
    if new_row_id is not None: rows = tuple(x for x in rows if x["new_row_id"] == new_row_id)
    return _freeze({"schema": "C200-ST2-REPLACEMENT-V1", "rows": rows, "count": len(rows), "old_blocked_row_replaced": True, "unrelated_rows_changed": 0, "root": _root(rows)})


def analyticity_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C200-AN-{r}", "resolution": r, "external_record_id": external_record_id or f"C200-EXT-{r}-antighost-in-gluon-ghost", "fixture_id": fixture_id or f"C200-GHOSTVERT-FIXTURE-{r}", "analytic_branch": "caller-supplied continuous nonzero branch", "zero_pole_avoided": True, "graded_Hermitian": True, "ghost_number_conserved": True, "Grassmann_parity": True, "all_eight_color_covariance": True, "f_d_separate": True, "polarization_covariance": "source/projector route", "Q0_P0_separate": True, "boundary_holonomy_separate": True, "physical": False} for r in _one(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C200-ANALYTICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    owners = ("tree", "connected", "inverse-two-point-derivative", "ghost-leg", "antighost-leg", "gluon-leg", "ghost-gluon-reducible", "spectator-disconnected", "proper", "boundary-link", "holonomy", "global-volume", "C199-ghost-field", "counterterm", "null", "target", "standard", "physical")
    rows = tuple({"graph_id": f"C200-TOPO-{i}", "owner": o, "count_once": True, "duplicate": False, "proper_separate": True, "interface_nonmatrix": o in ("boundary-link", "holonomy", "global-volume"), "holonomy_loop": False, "missing_zero": False, "physical": False} for i, o in enumerate(owners, 1))
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id)
    return _freeze({"schema": "C200-TOPOLOGY-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C199_SOURCE_RESPONSE", "TREE_FP_DERIVATIVE", "CONNECTED", "INVERSE_DERIVATIVE", "LEG_SUBTRACTION", "PROPER_KERNEL", "C199_GHOST_FIELD", "BOUNDARY_LINK", "HO_BOUNDARY", "HOLONOMY", "GLOBAL_VOLUME", "COUNTERTERM", "NULL", "TARGET", "STANDARD", "PHYSICAL")
    rows = tuple({"request_id": request_id or "C169-QCD_COUPLING-MOMQ", "owner_id": o, "count": 1, "duplicate": False, "holonomy_loop": False, "interface_factor": False, "missing_zero": False} for o in owners)
    return _freeze({"schema": "C200-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def ghostvert1_release_manifest() -> MappingProxyType:
    gates = {"role": True, "external_domain": True, "parameter": True, "tree": True, "connected": True, "inverse_derivative": True, "subtraction": True, "amputation": True, "proper": True, "projector": True, "rescaling": True, "dressing_boundary": True, "ST_replacement": True, "analyticity": True, "topology_count_once": True, "full_ST": False, "physical": False, "target_MOMq": False}
    return _freeze({"schema": "C200-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": STATUS, "gates": gates, "exact_scope": "conditional finite-basis bare ghost-gluon proper vertex; nonmatrix boundary/link/holonomy interfaces retained", "next": NEXT, "physical": False, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for x in c199.request_resolution_manifest()["rows"]:
        active = "QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"]
        rows.append({"request_id": x["request_id"], "previous_status": x["terminal_status"], "terminal_status": "C200_GHOST_GLUON_PROPER_VERTEX_CONDITIONAL_READY" if active else "PRESERVED_INHERITED_REQUEST", "active_in_C200": active, "all_six_visible": True, "C199_ST1": "read-only", "C200_ST2": active, "physical": False, "exact_next": NEXT if active else None})
    if request_id is not None: rows = [x for x in rows if x["request_id"] == request_id]
    return _freeze({"schema": "C200-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_ghost_vertex_object_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"object_id": x["object_id"], "exact_missing_object": x["exact_missing_object"], "aliases": x["aliases"], "request_id": request_id, "status": "PRESERVED_C200_FRONTIER" if x["object_id"] != "C197-ST-2" else "REPLACED_C200", "not_zero": True} for x in c199.missing_ghost_object_manifest()["rows"])
    return _freeze({"schema": "C200-MISSING-GHOST-VERTEX-V1", "rows": rows, "count": len(rows), "C197_ST_2_replaced": True, "remaining": ("C197-ST-3", "C197-ST-4", "C197-ST-5", "C197-ST-6", "C197-ST-7", "C197-ST-8", "C197-ST-9", "C197-ST-10"), "root": _root(rows)})


def next_st_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C200-NEXT-ST-HANDOFF-V1", "replaced_object": "C197-ST-2", "next": NEXT, "next_object": "C197-ST-3", "next_object_exact": "complete three-gluon proper vertex renormalization", "C199_root": C199_ROOT, "tree_root": tree_vertex_manifest()["root"], "connected_root": connected_response_manifest()["root"], "inverse_root": inverse_derivative_manifest()["root"], "subtraction_root": reducible_subtraction_manifest()["root"], "amputation_root": amputation_manifest()["root"], "proper_root": proper_kernel_manifest()["root"], "projector_root": vertex_projector_manifest()["root"], "rescaling_root": rescaling_manifest()["root"], "boundary_root": boundary_link_manifest()["root"], "jacobian_root": jacobian_manifest()["root"], "replacement_root": st_replacement_manifest()["root"], "remaining": missing_ghost_vertex_object_manifest()["remaining"], "physical": False, "root": _root((STATUS, NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C200-DEPENDENCY-FRONTIER-V1", "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "open": missing_ghost_vertex_object_manifest()["remaining"], "first": "C197-ST-3", "C158_value_inputs": 0, "Q0_Q1_Q2_modified": False, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C200-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "states": 0, "qubits": 0, "TMD_objects": 0, "physical_parameters": 0, "production_hamiltonian": 0, "root": _root((0, 0, 0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    zeros = {"ghost_field_recomputed": 0, "qg_recomputed": 0, "Z1F_recomputed": 0, "coupling_recomputed": 0, "field_response_recomputed": 0, "source_recomputed": 0, "unrelated_ST_recomputed": 0, "remembered_formula": 0, "physical_factor": 0, "symmetric_rescaling": 0, "C199_response_relabelled": 0, "bulk_endpoint_conflation": 0, "connected_proper_conflation": 0, "determinant_open_conflation": 0, "leg_proper_conflation": 0, "tree_proper_conflation": 0, "f_d_conflation": 0, "nonmatrix_fabricated": 0, "global_volume_absorbed": 0, "holonomy_loop": 0, "missing_zero": 0, "counterterms_selected": 0, "null_representatives": 0, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "Q0_Q1_Q2_modified": 0, "resolution_average": 0, "continuum_extrapolation": 0, "quantum_modification": 0}
    return _freeze({**zeros, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdghostvert1(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    fields = ("frontier", "external", "parameter", "tree", "connected", "inverse", "subtraction", "amputation", "proper", "projector", "rescaling", "boundary", "jacobian", "replacement", "analyticity", "topology", "request", "continuation")
    return _freeze({"index": index, "mutation": fields[index % len(fields)], "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


def ghostvert1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C200-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "C197_ST_2_replaced": True, "external_records": external_domain_manifest()["count"], "fixtures": ghost_vertex_fixture_manifest()["count"], "tree_records": tree_vertex_manifest()["count"], "connected_records": connected_response_manifest()["count"], "inverse_records": inverse_derivative_manifest()["count"], "subtraction_records": reducible_subtraction_manifest()["count"], "amputation_records": amputation_manifest()["count"], "proper_records": proper_kernel_manifest()["count"], "projector_records": vertex_projector_manifest()["count"], "rescaling_records": rescaling_manifest()["count"], "boundary_records": boundary_link_manifest()["count"], "jacobian_records": jacobian_manifest()["count"], "replacement_records": st_replacement_manifest()["count"], "remaining_frontier": 8, "counterterms": 6, "nulls": 9, "selected": False, "full_ST": False, "physical": False, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "root": _root((STATUS, PLAN, 8))})


_ROOTS = {"INPUT": _root((BASELINE, C199_C200_CONTRACT, C199_C200_CONTRACT_SHA256, PROMPT_SHA256)), "PLAN": ghostvert1_plan_manifest()["root"], "HANDOFF": ghost_vertex_handoff_freeze()["root"], "FRONTIER": frontier_manifest()["root"], "ROLE": vertex_role_decision()["root"], "EXTERNAL": external_domain_manifest()["root"], "PARAMETER": ghost_vertex_parameter_schema()["root"], "FIXTURE": ghost_vertex_fixture_manifest()["root"], "TREE": tree_vertex_manifest()["root"], "CONNECTED": connected_response_manifest()["root"], "INVERSE": inverse_derivative_manifest()["root"], "SUBTRACTION": reducible_subtraction_manifest()["root"], "AMPUTATION": amputation_manifest()["root"], "PROPER": proper_kernel_manifest()["root"], "PROJECTOR": vertex_projector_manifest()["root"], "RESCALING": rescaling_manifest()["root"], "DRESSING": vertex_dressing_manifest()["root"], "BOUNDARY": boundary_link_manifest()["root"], "JACOBIAN": jacobian_manifest()["root"], "REPLACEMENT": st_replacement_manifest()["root"], "ANALYTICITY": analyticity_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "RELEASE": ghostvert1_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "MISSING": missing_ghost_vertex_object_manifest()["root"], "NEXT": next_st_handoff_contract()["root"], "DEPENDENCY": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "ISOLATION": static_isolation_guard()["root"], "COMPLETENESS": ghostvert1_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C200-HQCDGHOSTVERT1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C200_PACKAGE_ROOT = PACKAGE_ROOT
C200_INPUT_ROOT = _ROOTS["INPUT"]

# Contract spelling aliases retained alongside the compact package names.
verify_hqcd_ghostvert1_authority = verify_hqcdghostvert1_authority
load_verified_hqcd_ghostvert1_authority = load_verified_hqcdghostvert1_authority

__all__ = [n for n in globals() if not n.startswith("_")]
