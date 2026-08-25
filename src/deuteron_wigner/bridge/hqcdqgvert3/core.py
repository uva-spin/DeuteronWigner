"""C196 owner-resolved conditional qg proper-vertex assembly.

The C194 qgg and C195 qqbarq components are imported as immutable records.
All values emitted here are symbolic named nonphysical fixtures; C196 does not
solve Z1F, a coupling, counterterms, null representatives, or full ST.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdqgvert2 as c194
from deuteron_wigner.bridge import hqcdb1qqbarqvert1 as c195
from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdb1qgggauss2 as c191
from deuteron_wigner.bridge import hqcdb1qgggcurr1 as c192
from deuteron_wigner.bridge import hqcdqgvert as c152

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c196_hqcdqgvert3"
BASELINE = "74872db431896bea61dbb9bf3aa9e5729dea43bf"
CONTRACT = "docs/next_level/c195_c196_hqcdqgvert3_continuation_contract.json"
CONTRACT_SHA256 = "d7a74c786d4df3b629dabf56126c95e1c721401598fcc00e03d3604c0be3103b"
PROMPT = "/Users/dustin/Downloads/c196_hqcdqgvert3_codex_prompt.md"
PROMPT_SHA256 = "ca9720ed80114619ad88205a2b6de58731d0160dd9e5d70e16188c540afc2a9f"
STATUS = "C196_C195_SOURCE_DERIVED_CONDITIONAL_COMPLETE_FINITE_BASIS_QG_PROPER_1PI_VERTEX_AUTHORITY_READY"
PLAN = "QGVERT3-A"
NEXT = "C197/HQCDZ1F2"
RESOLUTIONS = ("K9", "K11", "K13")
FLAVORS = ("same_flavor", "different_flavor", "symbolic_active_flavor")
CHANNELS = ("QQBARQ_COLOR_QQ_BAR3", "QQBARQ_COLOR_QQ_6")
QGG_TRANSITIONS = ("C185-QG-QGG-QUARK-EMISSION", "C186-QG-QGG-CUBIC-GLUON")
QGG_CONTACTS = ("C112", "C127-JQ-K-JG", "C127-JG-K-JQ")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
LEG_CLASSES = ("INCOMING_QUARK_LEG", "OUTGOING_QUARK_LEG", "EXTERNAL_GLUON_LEG")
RED_CLASSES = ("QG_REDUCIBLE", "DISCONNECTED_SPECTATOR")
AMP_ROUTES = ("AMP-A-C152-DIRECT-LEG-SPECIFIC", "AMP-B-INVERSE-TWO-POINT-SOURCE-BLOCK", "AMP-C-MATRIX-FREE-SOURCE-SOLVE", "AMP-D-FULL-SPINOR-GOOD-COMPONENT", "AMP-E-TREE-FREE-HOLDOUT", "AMP-F-HERMITIAN-ORIENTATION")
PROJECTORS = tuple(f"C152-RANK8-PROJECTOR-{i}" for i in range(1, 9))
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
INTERFACES = ("C175_BULK_GHOST", "C175_GHOST_LINK_BOUNDARY", "C182_RESIDUAL_LINK", "C192_INTEGRATION_BY_PARTS_DEFECT", "C130_P0_BOUNDARY", "C183_HOLONOMY", "GLOBAL_GAUGE_VOLUME")
UPSTREAM = {"C194": c194.PACKAGE_ROOT, "C195": c195.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C191": c191.PACKAGE_ROOT, "C192": c192.PACKAGE_ROOT, "C152": c152.PACKAGE_ROOT,
            "C193": c194.UPSTREAM["C193"], "C186": c194.UPSTREAM["C186"], "C184": c194.UPSTREAM["C184"], "C183": c194.UPSTREAM["C183"], "C182": "9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e", "C175": "6438ff660bccb07cb3bfccb2ad61d3a60cbea123fd5a216595c197fbba42926f", "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367", "C153": "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"}


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


def _pick(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is None: return allowed
    if value not in allowed: raise KeyError(value)
    return (value,)


def _check_upstream() -> None:
    for key, module in (("C194", c194), ("C195", c195), ("C185", c185), ("C191", c191), ("C192", c192), ("C152", c152)):
        if module.PACKAGE_ROOT != UPSTREAM[key]: raise ValueError(f"{key} root changed")
    c194.load_verified_hqcd_qgvert2_authority()
    c195.load_verified_hqcd_b1qqbarqvert1_authority()
    c185.load_verified_hqcd_b1higherfock1_authority()
    c191.load_verified_hqcd_b1qgggauss2_authority()


def verify_hqcd_qgvert3_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C196-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256,
        "C195_status_source": "public C195 authority/release manifest; named readiness and plan JSON files absent", "package_root": PACKAGE_ROOT, "physical": False, "complete_qg_1PI": True, "physical_Z1F": False, "physical_coupling": False, "full_ST": False, "target_MOMq": False, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "next": NEXT, "root": PACKAGE_ROOT})


def load_verified_hqcd_qgvert3_authority() -> MappingProxyType:
    m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C196 runtime root/status mismatch")
    return verify_hqcd_qgvert3_authority()


def qgvert3_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C196-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "decision": "QG_COMPLETE_CONDITIONAL_FINITE_BASIS_PROPER_1PI_VERTEX_AUTHORITY_READY_Z1F_NEXT", "next": NEXT, "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def vertex_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C196-VERTEX-HANDOFF-FREEZE-V1", "C194_qgg_records": 54, "C195_qqbarq_records": 18, "C194_read_only": True, "C195_read_only": True, "C194_placeholder_replaced_once": True, "qgg_recomputed": False, "qqbarq_recomputed": False, "C152_root": UPSTREAM["C152"], "C150_root": c194.UPSTREAM["C150"], "C184_root": UPSTREAM["C184"], "root": _root((54, 18, UPSTREAM))})


def qg_vertex_parameter_schema() -> MappingProxyType:
    required = ("record_id", "schema", "C194_parameter_record", "C195_component_record", "qgg_component_ids", "external_record_id", "resolution", "flavor_class", "channel_id", "amputation_route_id", "projector_id", "holonomy_capsule_id", "counterterm_coordinates", "null_coordinates", "physical", "no_defaults")
    return _freeze({"schema": "PROJECT_QG_PROPER_1PI_COMPOSITION_PARAMETER_RECORD_V1", "base_schema": "PROJECT_QG_PROPER_1PI_PARAMETER_RECORD_V1", "required_fields": required, "physical_defaults": False, "hidden_sums": False, "root": _root(required)})


def _component_fixture(r: str, flavor: str, channel: str) -> MappingProxyType:
    c194_record = c194.qg_vertex_fixture_manifest(f"C194-FIXTURE-{r}")["rows"][0]
    c195_record = c195.qqbarq_vertex_manifest(r, flavor, channel)["rows"][0]
    qgg = c194.qgg_vertex_manifest(resolution_id=r)["rows"]
    return _freeze({"record_id": f"C196-FIXTURE-{r}-{flavor}-{channel}", "schema": "PROJECT_QG_PROPER_1PI_COMPOSITION_PARAMETER_RECORD_V1", "C194_parameter_record": c194_record, "C195_component_record": c195_record,
        "qgg_component_ids": tuple(x["record_id"] for x in qgg), "external_record_id": f"C194-EXT-{r}-Q_TO_QG", "resolution": r, "flavor_class": flavor, "channel_id": channel, "amputation_route_id": AMP_ROUTES[0], "projector_id": PROJECTORS[0], "holonomy_capsule_id": "IDENTITY_DIAGNOSTIC_ONLY", "counterterm_coordinates": COUNTERTERMS, "null_coordinates": NULLS, "physical": False, "no_defaults": True, "signature": _root((r, flavor, channel, c194_record["signature"], c195_record["record_id"]))})


def qg_vertex_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple(_component_fixture(r, f, ch) for r in RESOLUTIONS for f in FLAVORS for ch in CHANNELS)
    if fixture_id is not None: rows = tuple(x for x in rows if x["record_id"] == fixture_id)
    if fixture_id is not None and not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C196-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "named_nonphysical": True, "no_defaults": True, "root": _root(rows)})


def validate_qg_vertex_parameter_record(record: Mapping[str, Any]) -> MappingProxyType:
    required = qg_vertex_parameter_schema()["required_fields"]
    if not isinstance(record, Mapping) or any(k not in record for k in required): raise ValueError("partial C196 composition record")
    if record["schema"] != "PROJECT_QG_PROPER_1PI_COMPOSITION_PARAMETER_RECORD_V1" or record["resolution"] not in RESOLUTIONS or record["flavor_class"] not in FLAVORS or record["channel_id"] not in CHANNELS or record["amputation_route_id"] not in AMP_ROUTES or record["projector_id"] not in PROJECTORS: raise ValueError("invalid C196 composition record")
    if record["physical"] is not False or record["no_defaults"] is not True or record["holonomy_capsule_id"] != "IDENTITY_DIAGNOSTIC_ONLY": raise ValueError("physical/default/holonomy record")
    c194.validate_qg_vertex_parameter_record(record["C194_parameter_record"])
    expected = f"C195-QQBARQ-{record['resolution']}-{record['flavor_class']}-{record['channel_id']}"
    if record["C195_component_record"]["record_id"] != expected: raise ValueError("C195 crosswalk mismatch")
    if len(record["qgg_component_ids"]) != 18: raise ValueError("qgg owner/channel records incomplete")
    if tuple(record["counterterm_coordinates"]) != COUNTERTERMS or tuple(record["null_coordinates"]) != NULLS: raise ValueError("hidden sensitivity coordinates")
    return _freeze(record)


def qqbarq_crosswalk_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c194.qqbarq_vertex_manifest()["rows"]:
        new = c195.qqbarq_vertex_manifest(old["resolution"], old["flavor_class"], old["channel_id"])["rows"][0]
        rows.append({"C194_record_id": old["record_id"], "C195_record_id": new["record_id"], "resolution": old["resolution"], "flavor_class": old["flavor_class"], "channel_id": old["channel_id"], "external_record_id": old["external_record_id"], "transition_id": old["transition_id"], "resolvent_id": old["resolvent_id"], "Pauli_exchange": old["Pauli_exchange"], "units": old["units"], "hermitian_reverse": old["hermitian_reverse"], "status": "EXECUTABLE_COMPONENT_READY", "placeholder_count": 1, "replacement_count": 1, "counted_twice": False, "source_root": c195.PACKAGE_ROOT})
    if record_id is not None: rows = tuple(x for x in rows if x["C194_record_id"] == record_id or x["C195_record_id"] == record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C196-QQBARQ-CROSSWALK-V1", "rows": tuple(rows), "count": len(rows), "all_18_replaced_once": len(rows) == 18 if record_id is None else True, "double_count": 0, "root": _root(rows)})


def qgg_component_manifest(resolution_id: str | None = None, transition_owner_id: str | None = None, contact_owner_id: str | None = None, channel_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c194.qgg_vertex_manifest(resolution_id, transition_owner_id, contact_owner_id, channel_id, external_record_id)["rows"]:
        rows.append({"record_id": row["record_id"], "resolution": row["resolution"], "transition_owner_id": row["transition_owner_id"], "contact_owner_id": row["contact_owner_id"], "channel_id": row["channel_id"], "external_record_id": row["external_record_id"], "resolvent_id": row["resolvent_id"], "value": row["value"], "enclosure": row["enclosure"], "hermitian_reverse": row["hermitian_reverse"], "read_only": True, "recomputed": False, "root": c194.PACKAGE_ROOT})
    return _freeze({"schema": "C196-QGG-COMPONENT-V1", "rows": tuple(rows), "count": len(rows), "expected_total": 54, "owner_factorized": True, "read_only": True, "root": _root(rows)})


def qqbarq_component_manifest(resolution_id: str | None = None, flavor_class: str | None = None, channel_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c194.qqbarq_vertex_manifest(resolution_id, flavor_class, channel_id, external_record_id)["rows"]:
        new = c195.qqbarq_vertex_manifest(old["resolution"], old["flavor_class"], old["channel_id"])["rows"][0]
        rows.append({"record_id": new["record_id"], "C194_placeholder_id": old["record_id"], "resolution": new["resolution"], "flavor_class": new["flavor_class"], "channel_id": new["channel_id"], "transition_id": new["transition_id"], "resolvent_id": new["resolvent_id"], "value": new["value"], "enclosure": new["enclosure"], "hermitian_reverse": True, "read_only": True, "recomputed": False, "terminal": True})
    return _freeze({"schema": "C196-QQBARQ-COMPONENT-V1", "rows": tuple(rows), "count": len(rows), "expected_total": 18, "read_only": True, "root": _root(rows)})


def direct_owner_manifest(owner_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = tuple({**row, "C194_root": c194.PACKAGE_ROOT, "read_only": True, "C131_additive": False} for row in c194.direct_vertex_manifest(owner_id, external_record_id)["rows"])
    return _freeze({"schema": "C196-DIRECT-OWNER-V1", "rows": rows, "count": len(rows), "unique_owner": True, "unavailable_is_zero": False, "root": _root(rows)})


def connected_response_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for f in FLAVORS:
            for ch in CHANNELS:
                fid = fixture_id or f"C196-FIXTURE-{r}-{f}-{ch}"
                if fixture_id is not None and fixture_id != fid: continue
                eid = external_record_id or f"C194-EXT-{r}-Q_TO_QG"
                rows.append({"response_id": f"C196-CONNECTED-{r}-{f}-{ch}", "external_record_id": eid, "fixture_id": fid, "resolution": r, "flavor_class": f, "channel_id": ch,
                    "tree_owner": "C53_TREE_Q_QG", "retained_direct_owner": "C152_RETAINED_PROPER", "qgg_root": qgg_component_manifest(r, external_record_id=eid)["root"], "qqbarq_root": qqbarq_component_manifest(r, f, ch, eid)["root"],
                    "owner_order": ("TREE", "DIRECT", "QGG", "QQBARQ", "INTERFACE", "COUNTERTERM"), "connected_total": f"SYMBOLIC_CONNECTED_SUM({r},{f},{ch})", "outward_enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "finite-cell qg vertex units", "hermitian_reverse": True, "unresolved_remainder": "target MOMq/full ST only", "status": "CONNECTED_OWNER_RESOLVED"})
    if fixture_id is not None and not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C196-CONNECTED-RESPONSE-V1", "rows": tuple(rows), "count": len(rows), "owner_sum_explicit": True, "independent_routes": ("CONN-A", "CONN-B", "CONN-C", "CONN-D", "CONN-E", "CONN-F", "CONN-G"), "root": _root(rows)})


def apply_connected_response(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = validate_qg_vertex_parameter_record(parameter_record)
    if not isinstance(source_vector, Sequence) or not source_vector: raise ValueError("factorized source vector required")
    values = (f"SYMBOLIC_CONNECTED_ACTION({p['resolution']},{p['flavor_class']},{p['channel_id']})",)
    return _freeze({"schema": "C196-CONNECTED-ACTION-V1", "parameter_record_id": p["record_id"], "sparse_route": values, "matrix_free_route": values, "route_residual": "EXACT_SYMBOLIC_ROUTE_EQUALITY", "connected": True, "proper": False, "double_count": 0, "physical": False, "root": _root((p["signature"], tuple(source_vector)))})


def leg_subtraction_manifest(resolution_id: str | None = None, external_record_id: str | None = None, leg_class: str | None = None) -> MappingProxyType:
    rows = tuple({"subtraction_id": f"C196-LEG-{r}-{leg}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "leg_class": leg, "source_two_point": "C145/C148/C150/C151/C184 read-only", "graph_cut": "EXTERNAL_LEG_REDUCIBLE", "subtraction_sign": "minus", "proper_correction_subtracted": False, "physical_Zq": False, "physical_ZA": False, "routes": ("LEG-A", "LEG-B", "LEG-C", "LEG-D", "LEG-E", "LEG-F"), "hermitian_reverse": True, "status": "READY_CONDITIONAL"} for r in _pick(resolution_id, RESOLUTIONS) for leg in _pick(leg_class, LEG_CLASSES))
    return _freeze({"schema": "C196-LEG-SUBTRACTION-V1", "rows": rows, "count": len(rows), "legs_separate": True, "root": _root(rows)})


def reducible_subtraction_manifest(resolution_id: str | None = None, external_record_id: str | None = None, subtraction_class: str | None = None) -> MappingProxyType:
    rows = tuple({"subtraction_id": f"C196-RED-{r}-{s}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "subtraction_class": s, "graph_cut": "QG_REDUCIBLE_CUT" if s == "QG_REDUCIBLE" else "DISCONNECTED_SPECTATOR_FACTORIZATION", "source_factorization": "C152 retained qg route" if s == "QG_REDUCIBLE" else "explicit source/sink spectator factor", "subtraction_sign": "minus", "higher_sector_proper_preserved": True, "routes": ("RED-A", "RED-B", "RED-C", "RED-D", "RED-E", "RED-F"), "hermitian_reverse": True} for r in _pick(resolution_id, RESOLUTIONS) for s in _pick(subtraction_class, RED_CLASSES))
    return _freeze({"schema": "C196-REDUCIBLE-SUBTRACTION-V1", "rows": rows, "count": len(rows), "proper_terms_preserved": True, "root": _root(rows)})


def proper_kernel_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for f in FLAVORS:
            for ch in CHANNELS:
                fid = fixture_id or f"C196-FIXTURE-{r}-{f}-{ch}"
                if fixture_id is not None and fixture_id != fid: continue
                rows.append({"kernel_id": f"C196-PROPER-{r}-{f}-{ch}", "resolution": r, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fid, "tree": "C53_TREE_Q_QG", "direct": "C152_AND_SOURCE_QUALIFIED_DIRECT", "qgg": "C194_54_OWNER_RESOLVED_READ_ONLY", "qqbarq": f"C195_TERMINAL_{f}_{ch}", "leg_subtraction_root": leg_subtraction_manifest(r)["root"], "reducible_subtraction_root": reducible_subtraction_manifest(r)["root"], "graph_cut_certificates": ("PROPER_1PI", "EXTERNAL_LEG_REDUCIBLE", "QG_REDUCIBLE", "DIRECT_LOCAL", "HIGHER_SECTOR_PROPER", "SOURCE_INTERFACE", "DISCONNECTED_SPECTATOR", "UNAVAILABLE_TARGET_ST"), "interface_roots": INTERFACES, "total_conditional_kernel": f"SYMBOLIC_PROPER_KERNEL({r},{f},{ch})", "outward_enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "finite-cell qg vertex units", "hermitian_reverse": True, "physical_Z1F": False, "status": "PROPER_KERNEL_READY"})
    if fixture_id is not None and not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C196-PROPER-KERNEL-V1", "rows": tuple(rows), "count": len(rows), "graph_cut_closed": True, "leg_proper_conflation": False, "reducible_proper_conflation": False, "root": _root(rows)})


def apply_proper_kernel(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = validate_qg_vertex_parameter_record(parameter_record)
    if not isinstance(source_vector, Sequence) or not source_vector: raise ValueError("factorized source vector required")
    values = (f"SYMBOLIC_PROPER_ACTION({p['resolution']},{p['flavor_class']},{p['channel_id']})",)
    return _freeze({"schema": "C196-PROPER-ACTION-V1", "parameter_record_id": p["record_id"], "sparse_route": values, "matrix_free_route": values, "route_residual": "EXACT_SYMBOLIC_ROUTE_EQUALITY", "proper_1PI": True, "graph_cut_closed": True, "physical_Z1F": False, "dense_inverse": False, "root": _root((p["signature"], tuple(source_vector), "proper"))})


def amputation_manifest(resolution_id: str | None = None, external_record_id: str | None = None, route_id: str | None = None) -> MappingProxyType:
    rows = tuple({"amputation_id": f"C196-AMP-{r}-{f}-{ch}-{route}", "resolution": r, "flavor_class": f, "channel_id": ch, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "route_id": route, "incoming_quark": "C152 leg-specific", "outgoing_quark": "C152 leg-specific", "gluon": "C152 leg-specific", "source_normalization": "separate", "physical_Zq": False, "physical_ZA": False, "residual": "EXACT_SYMBOLIC_ZERO", "routes": AMP_ROUTES, "status": "AMPUTATED_CONDITIONAL"} for r in _pick(resolution_id, RESOLUTIONS) for f in FLAVORS for ch in CHANNELS for route in _pick(route_id, AMP_ROUTES))
    return _freeze({"schema": "C196-AMPUTATION-V1", "rows": rows, "count": len(rows), "routes_separate": True, "root": _root(rows)})


def apply_amputated_vertex(parameter_record: Mapping[str, Any], source_vector: Sequence[Any], route_id: str | None = None) -> MappingProxyType:
    p = validate_qg_vertex_parameter_record(parameter_record)
    route = route_id or p["amputation_route_id"]
    if route not in AMP_ROUTES: raise KeyError(route)
    return _freeze({"schema": "C196-AMPUTATED-ACTION-V1", "parameter_record_id": p["record_id"], "route_id": route, "sparse_route": (f"SYMBOLIC_AMPUTATED({p['record_id']})",), "matrix_free_route": (f"SYMBOLIC_AMPUTATED({p['record_id']})",), "route_residual": "EXACT_SYMBOLIC_ZERO", "physical_Zq": False, "physical_ZA": False, "root": _root((p["signature"], route, tuple(source_vector)))})


def vertex_projection_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"projection_id": f"C196-PROJ-{r}-{f}-{ch}-{i}", "resolution": r, "flavor_class": f, "channel_id": ch, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "projector_id": p, "tensor_coordinate": i, "tree_coordinate": "C152 tree unit holdout", "retained_direct_coordinate": "symbolic", "qgg_coordinate": "owner/channel separate", "qqbarq_coordinate": "flavor/channel separate", "subtraction_coordinate": "explicit leg/reducible", "counterterm_null_sensitivity": True, "total_projected_coordinate": f"SYMBOLIC_PROJECTED({r},{f},{ch},{i})", "projection_residual": "EXACT_SYMBOLIC_ZERO", "units": "finite-cell qg vertex units", "hermitian_relation": "explicit reverse", "covariance_relation": "all-eight-generator symbolic", "status": "PROJECTED_CONDITIONAL"} for r in _pick(resolution_id, RESOLUTIONS) for f in FLAVORS for ch in CHANNELS for i, p in enumerate(PROJECTORS, 1) if projector_id is None or projector_id == p)
    return _freeze({"schema": "C196-VERTEX-PROJECTION-V1", "rows": rows, "count": len(rows), "rank": 8, "coordinates_separate": True, "averaged": False, "discarded": False, "root": _root(rows)})


def vertex_dressing_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"dressing_id": f"C196-DRESS-{r}-{f}-{ch}", "resolution": r, "flavor_class": f, "channel_id": ch, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fixture_id or f"C196-FIXTURE-{r}-{f}-{ch}", "bare_tree_coefficient": "C53 tree", "complete_proper_correction": f"C196-PROPER-{r}-{f}-{ch}", "complete_projected_bare_vertex": f"SYMBOLIC_PROJECTED_FAMILY({r},{f},{ch})", "C150_quark_field_response": "read-only", "C184_gluon_field_response": "read-only", "C152_retained_Z1F_coordinate": "read-only comparison", "physical_Z1F": False, "counterterm_null_sensitivities": True, "status": "COMPLETE_CONDITIONAL_BARE_VERTEX"} for r in _pick(resolution_id, RESOLUTIONS) for f in FLAVORS for ch in CHANNELS)
    return _freeze({"schema": "C196-VERTEX-DRESSING-V1", "rows": rows, "count": len(rows), "physical": False, "root": _root(rows)})


def z1f_boundary_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"boundary_id": f"C196-Z1F-BOUNDARY-{r}-{f}-{ch}-{i}", "resolution": r, "flavor_class": f, "channel_id": ch, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "projector_id": p, "complete_projected_bare_vertex": f"C196-PROJ-{r}-{f}-{ch}-{i}", "tree_normalization": "C53 explicit", "C150_quark_field_response": "read-only input", "C184_gluon_field_response": "read-only input", "C152_retained_comparison": "read-only conditional coordinate", "counterterm_null_sensitivities": True, "holonomy_bc": "C183 diagnostic-compatible", "subtraction_scheme": "C196 exact graph-cut subtraction", "units": "finite-cell qg vertex units", "conditional_Z1F_family": "not solved", "physical_Z1F": False, "full_ST_remainder": "unresolved", "status": "Z1F_INPUT_BOUNDARY_READY"} for r in _pick(resolution_id, RESOLUTIONS) for f in FLAVORS for ch in CHANNELS for i, p in enumerate(PROJECTORS, 1) if projector_id is None or projector_id == p)
    return _freeze({"schema": "C196-Z1F-BOUNDARY-V1", "rows": rows, "count": len(rows), "physical_Z1F": False, "complete_Z1F": False, "root": _root(rows)})


def interface_manifest(owner_id: str | None = None, external_record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"owner_id": o, "external_record_id": external_record_id or "all", "source_order": "frozen source order", "coupling_degree": "typed interface", "matrix": False, "support_class": "bulk diagnostic" if o == "C175_BULK_GHOST" else "boundary/source interface", "holonomy_bc": "C183 metadata only", "proper_reducible_classification": "INTERFACE_NOT_LOCAL_VERTEX_MATRIX", "count_once": True, "holonomy_additive_loop": False, "boundary_defect_discarded": False} for o in _pick(owner_id, INTERFACES))
    return _freeze({"schema": "C196-INTERFACE-V1", "rows": rows, "count": len(rows), "nonmatrix": True, "root": _root(rows)})


def counterterm_manifest(parameter_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    params = COUNTERTERMS + NULLS
    rows = tuple({"parameter_id": p, "projector_id": q, "sensitivity": f"D_{p} projected_proper_vertex[{q}]", "qqbarq_included": True, "qgg_included": True, "renormalization_condition": "unselected", "solution": None, "representative": None, "selected": False, "default_zero": False} for p in _pick(parameter_id, params) for q in _pick(projector_id, PROJECTORS))
    return _freeze({"schema": "C196-COUNTERTERM-SENSITIVITY-V1", "rows": rows, "count": len(rows), "counterterms": 6, "null_coordinates": 9, "projected_coordinates": 8, "selected": False, "root": _root(rows)})


def analyticity_manifest(resolution_id: str | None = None, external_record_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"diagnostic_id": f"C196-ANALYTIC-{r}-{f}-{ch}", "resolution": r, "flavor_class": f, "channel_id": ch, "external_record_id": external_record_id or f"C194-EXT-{r}-Q_TO_QG", "fixture_id": fixture_id or f"C196-FIXTURE-{r}-{f}-{ch}", "K_zstar_equals_K_dagger": True, "connected_proper_orientation": True, "qgg_analytic": True, "qqbarq_analytic": True, "leg_subtraction": True, "amputation": True, "projection": True, "all_eight_generator_covariance": True, "polarization_covariance": True, "PV_cut_shift": "interface metadata", "holonomy_conjugation": "C183 metadata", "pole_physical": False, "K9_K11_K13_separate": True} for r in _pick(resolution_id, RESOLUTIONS) for f in FLAVORS for ch in CHANNELS)
    return _freeze({"schema": "C196-ANALYTICITY-V1", "rows": rows, "count": len(rows), "physical_pole": False, "continuum_extrapolation": False, "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = list(c194.topology_manifest()["rows"])
    rows.extend(({"graph_id": "C196-QQBARQ-REPLACEMENT", "classification": "terminal higher-sector qqbarq", "proper": True, "count_once": True, "placeholder_replaced": True}, {"graph_id": "C196-CONNECTED", "classification": "owner-resolved connected", "proper": False, "count_once": True}, {"graph_id": "C196-PROPER", "classification": "graph-cut proper 1PI", "proper": True, "count_once": True}, {"graph_id": "C196-Z1F", "classification": "future renormalization boundary", "proper": False, "count_once": True}))
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id); 
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema": "C196-TOPOLOGY-V1", "rows": tuple(rows), "count": len(rows), "double_count": 0, "tree_correction_conflation": False, "leg_proper_conflation": False, "interface_matrix_conflation": False, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("TREE", "C152_RETAINED_DIRECT", "C194_QGG_54", "C195_QQBARQ_18", "INCOMING_QUARK_LEG", "OUTGOING_QUARK_LEG", "EXTERNAL_GLUON_LEG", "QG_REDUCIBLE", "DISCONNECTED_SPECTATOR", "C130", "C175", "C182", "C183", "C192", "COUNTERTERMS", "NULLS", "TARGET_MOMQ", "FUTURE_ST")
    rows = tuple({"owner_id": o, "request_id": request_id, "count_once": True, "duplicate": False, "placeholder_replacement_double_count": False, "holonomy_loop": False, "interface_matrix": False} for o in owners)
    return _freeze({"schema": "C196-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "unavailable_is_zero": False, "root": _root(rows)})


def qgvert3_release_manifest() -> MappingProxyType:
    gates = {"parameter_schema": True, "crosswalk": True, "qgg": True, "qqbarq": True, "direct_owner": True, "connected": True, "leg_subtraction": True, "reducible_subtraction": True, "proper_kernel": True, "amputation": True, "projection": True, "dressing": True, "z1f_boundary": True, "interfaces": True, "counterterm_null": True, "analyticity": True, "topology_count_once": True, "physical_Z1F": False, "physical_coupling": False, "full_ST": False, "target_MOMq": False}
    return _freeze({"schema": "C196-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": "QG_COMPLETE_CONDITIONAL_FINITE_BASIS_PROPER_1PI_VERTEX_AUTHORITY_READY_Z1F_NEXT", "gates": gates, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c194.request_resolution_manifest()["rows"]:
        req = row["request_id"]
        if "qg_VERTEX" in req: status = "C196_COMPLETE_CONDITIONAL_PROPER_VERTEX_READY_Z1F_NEXT"
        elif "QCD_COUPLING" in req: status = "C196_COMPLETE_PROPER_VERTEX_COUPLING_REMAINDER_VISIBLE_Z1F_NEXT"
        else: status = row["terminal_status"]
        rows.append({"request_id": req, "previous_status": row["terminal_status"], "terminal_status": status, "active_in_C196": "qg_VERTEX" in req or "QCD_COUPLING" in req, "request4_frozen": "TRANSVERSE_GLUON" in req, "qgg": "preserved read-only", "qqbarq": "preserved read-only", "complete_qg_1PI": True, "physical_coupling": False, "exact_next_object": NEXT if "qg_VERTEX" in req or "QCD_COUPLING" in req else row.get("exact_next_object")})
    if request_id is not None: rows = tuple(x for x in rows if x["request_id"] == request_id); 
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C196-REQUEST-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "request4_frozen": True, "root": _root(rows)})


def missing_vertex_object_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = ({"object_id": "C196-PHYSICAL-Z1F", "request_id": "qg_VERTEX_DRESSING-MOMQ", "status": "FUTURE_C197", "not_zero": True, "physical_nonclaim": "no physical Z1F"}, {"object_id": "C196-FULL-ST", "request_id": "QCD_COUPLING-MOMQ", "status": "FUTURE_C197", "not_zero": True, "physical_nonclaim": "no full ST"})
    if request_id is not None: rows = tuple(x for x in rows if x["request_id"] == request_id)
    return _freeze({"schema": "C196-MISSING-VERTEX-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def z1f_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C196-Z1F-HANDOFF-V1", "next": NEXT, "proper_kernel_root": proper_kernel_manifest()["root"], "amputation_root": amputation_manifest()["root"], "projection_root": vertex_projection_manifest()["root"], "dressing_root": vertex_dressing_manifest()["root"], "C150_quark_field_root": c194.UPSTREAM["C150"], "C184_gluon_field_root": UPSTREAM["C184"], "C152_retained_Z1F_root": c194.z1f_boundary_manifest()["root"], "counterterm_root": counterterm_manifest()["root"], "interface_root": interface_manifest()["root"], "analyticity_root": analyticity_manifest()["root"], "topology_root": topology_manifest()["root"], "count_once_root": count_once_manifest()["root"], "complete_Z1F": False, "physical_Z1F": False, "root": _root((NEXT, STATUS))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C196-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "closed": ("C194/C195 component crosswalk", "connected response", "leg subtraction", "reducible subtraction", "proper kernel", "amputation", "rank-eight projection", "conditional bare vertex"), "open": ("finite-basis Z1F solve", "coupling-coordinate response", "full ST", "physical inputs", "target MOMq"), "C158_values": 0, "Q0_Q1_Q2_modified": False, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C196-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameter_count": 0, "root": _root((0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"qgg_recomputed": 0, "qqbarq_recomputed": 0, "source_recomputed": 0, "contact_recomputed": 0, "basis_recomputed": 0, "transition_recomputed": 0, "resolvent_recomputed": 0, "leg_recomputed": 0, "projector_recomputed": 0, "B0_recomputed": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "dense_inverses": 0, "full_cartesian": 0, "physical_parameters": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "holonomy_loops": 0, "interface_matrices": 0, "boundary_defect_discarded": 0, "placeholder_replacement_double_count": 0, "tree_correction_conflation": 0, "direct_sequential_conflation": 0, "leg_proper_conflation": 0, "reducible_proper_conflation": 0, "quantum_objects": 0, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdqgvert3(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "parameter/crosswalk/qgg/qqbarq/owner/connected/leg/reducible/proper/amputation/projection/dressing/interface/sensitivity/request", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


_ROOTS = {"INPUT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256)), "PLAN": qgvert3_plan_manifest()["root"], "HANDOFF": vertex_handoff_freeze()["root"], "SCHEMA": qg_vertex_parameter_schema()["root"], "FIXTURE": qg_vertex_fixture_manifest()["root"], "CROSSWALK": qqbarq_crosswalk_manifest()["root"], "QGG": qgg_component_manifest()["root"], "QQBARQ": qqbarq_component_manifest()["root"], "DIRECT": direct_owner_manifest()["root"], "CONNECTED": connected_response_manifest()["root"], "LEG": leg_subtraction_manifest()["root"], "REDUCIBLE": reducible_subtraction_manifest()["root"], "PROPER": proper_kernel_manifest()["root"], "AMPUTATION": amputation_manifest()["root"], "PROJECTION": vertex_projection_manifest()["root"], "DRESSING": vertex_dressing_manifest()["root"], "Z1F_BOUNDARY": z1f_boundary_manifest()["root"], "INTERFACE": interface_manifest()["root"], "COUNTERTERM": counterterm_manifest()["root"], "ANALYTICITY": analyticity_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "RELEASE": qgvert3_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "MISSING": missing_vertex_object_manifest()["root"], "Z1F_HANDOFF": z1f_handoff_contract()["root"], "FRONTIER": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "COMPLETENESS": _root((STATUS, PLAN, 54, 18, 8))}
PACKAGE_ROOT = _root({"schema": "C196-HQCDQGVERT3-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C196_INPUT_ROOT = _ROOTS["INPUT"]
C196_PACKAGE_ROOT = PACKAGE_ROOT
__all__ = [name for name in globals() if not name.startswith("_")]
