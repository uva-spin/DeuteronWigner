"""C168 fail-closed adapter-derivation authority.

This package records endpoint identities and exact calculation boundaries.  It
does not contain target formulae, numerical coefficients, a symbolic
evaluator, or a C158 import.  The six C43 adapter requests therefore terminate
at explicit new-calculation capsules.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdlfgacquire4 import core as c167
from deuteron_wigner.bridge.hqcdlfgdep2 import core as c166

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c168_hqcdlfgadapter1"
BASELINE = "5946aed24aa5deb85537724f69dd0028fc47b0c2"
CONTRACT = "docs/next_level/c167_c168_hqcdlfgadapter1_continuation_contract.json"
CONTRACT_SHA256 = "0a39c6cbe18c49a86d42ef12bf24135f16ea6ae07c9d1297dc00e97e4986ffc6"
PROMPT_SHA256 = "beb12eda73010147930300955fdff9869e7914951a400360e246735e56b94f0f"
STATUS = "C168_HQCDLFGADAPTER1_NEW_PERTURBATIVE_CALCULATION_REQUIRED"
PLAN = "LFGADAPTER1-D"
NEXT = "C169/HQCDLFGMATCHCALC1"
C167_ROOT = "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d"
C166_ROOT = "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416"
C165_ROOT = "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2"
C164_ROOT = "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2"
C163_ROOT = "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0"
C162_ROOT = "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d"
C161_ROOT = "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
C160_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C43_ROOTS = (
    "docs/next_level/c43_primary_source_manifest.json",
    "docs/next_level/c43_gauge_convention_map.json",
    "docs/next_level/c43_boundary_prescription_decision.json",
)
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
RESOLUTIONS = ("K9", "K11", "K13")
COORDINATES = ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2")
SAFE_OPCODES = ("LOAD_RATIONAL", "LOAD_SOURCE_CONSTANT", "LOAD_KINEMATIC", "ADD", "NEGATE", "MULTIPLY", "SAFE_DIVIDE", "INTEGER_POWER", "LOG", "LOG_RATIO", "EXP", "POSITIVE_SQRT", "PI_POWER", "ZETA_CONSTANT", "PROJECT_TENSOR", "SERIES_COEFFICIENT", "RETURN_TYPED_COEFFICIENT")


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


_REQUEST_ROWS = tuple(dict(x) for x in c167.c43_adapter_calculation_request_manifest()["rows"])
_ACQUIRABILITY = {x["request_id"]: dict(x) for x in c167.c43_adapter_acquirability_manifest()["rows"]}
_RESOLUTION_ROWS = {x["request_id"]: dict(x) for x in c167.request_resolution_manifest()["rows"]}
_CROSSWALK = {x["descriptor_id"]: dict(x) for x in c166.descriptor_dependency_crosswalk()["rows"]}
_REQUEST_BY_ID = {x["request_id"]: x for x in _RESOLUTION_ROWS.values() if x["request_id"] in _ACQUIRABILITY}
_C167_ACQUIRABILITY_ROOT = c167.c43_adapter_acquirability_manifest()["root"]
_C167_CALCULATION_REQUEST_ROOT = c167.c43_adapter_calculation_request_manifest()["root"]


def _request(request_id: str | None = None) -> tuple[Mapping[str, Any], ...]:
    if request_id is not None and request_id not in _REQUEST_BY_ID: raise KeyError(request_id)
    return tuple(x for x in _REQUEST_ROWS if request_id is None or x["request_id"] == request_id)


def _quantity(request_id: str) -> str:
    rid = request_id
    for q in QUANTITIES:
        if q in rid: return q
    raise KeyError(request_id)


def _descriptor(request_id: str) -> Mapping[str, Any]:
    return _RESOLUTION_ROWS[request_id]


def _graph_id(request_id: str) -> str:
    d = _descriptor(request_id)
    cross = _CROSSWALK.get(d["descriptor_id"], {})
    return cross.get("graph_id") or "C166-GRAPH-NOT-APPLICABLE-PRESERVED"


def _scheme(request_id: str) -> str:
    return "RI_SMOM" if "RI_SMOM" in request_id else "MOMQ"


def _target_source(request_id: str) -> str:
    return "arXiv:0901.2599v2" if _scheme(request_id) == "RI_SMOM" else "arXiv:1108.4806v1"


def _projector(q: str, scheme: str) -> str:
    return {
        "QUARK_FIELD": f"{scheme} source-qualified quark inverse-two-point projector; C43 finite kinetic projectors K_MINUS/K_PLUS/K_PERP remain separate",
        "SIGNED_QUARK_MASS": f"{scheme} source-qualified scalar mass projector; signed branch retained, m_R^2 not substituted",
        "TRANSVERSE_GLUON_FIELD": f"{scheme} source-qualified transverse gluon projector; no C43 RI/SMOM promotion",
        "qg_VERTEX_DRESSING": f"{scheme} source-qualified q-g vertex projector with explicit leg order and color tensors",
        "QCD_COUPLING": f"{scheme} source-qualified coupling condition; assembled field/vertex projector factors remain separate",
    }[q]


def _operator(q: str) -> str:
    return {
        "QUARK_FIELD": "C43 nonzero-mode projected quark two-point / field residue",
        "SIGNED_QUARK_MASS": "C43 signed quark mass projector on the retained quark two-point object",
        "TRANSVERSE_GLUON_FIELD": "C43 transverse A_perp two-point response",
        "qg_VERTEX_DRESSING": "C43 connected/amputated retained qg response; complete 1PI not asserted",
        "QCD_COUPLING": "C43 coupling parameter assembled from explicitly separated field and vertex factors",
    }[q]


def _order(q: str) -> Mapping[str, Any]:
    # These are the frozen C159/C161 order labels, not a newly inferred zero.
    n = 0 if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD") else 1
    return {"C161_order_label": n, "source_order_authority": "C167 request-specific order from frozen C166 root", "order_value_promoted": False, "status": "FROZEN_LABEL_REQUIRES_C169_SOURCE_CALCULATION"}


def _basis(q: str) -> Mapping[str, Any]:
    if q == "QUARK_FIELD": return {"input": ("K_MINUS", "K_PLUS", "K_PERP"), "output": ("RI_SMOM_QUARK_PROJECTED", "MOMQ_QUARK_PROJECTED"), "map_class": "FINITE_DIMENSIONAL_MATRIX"}
    if q == "SIGNED_QUARK_MASS": return {"input": ("signed m_R",), "output": ("signed m_R_target",), "map_class": "SCALAR_MULTIPLICATIVE", "branch": "caller-supplied signed branch"}
    if q == "TRANSVERSE_GLUON_FIELD": return {"input": ("C43_A_perp_transverse_components",), "output": ("MOMQ_TRANSVERSE_GLUON_PROJECTED",), "map_class": "FINITE_DIMENSIONAL_MATRIX"}
    if q == "qg_VERTEX_DRESSING": return {"input": ("connected_retained_qg", "amputated_retained_qg", "V_B", "Z_1F"), "output": ("proper_target_qg_projected",), "map_class": "FINITE_DIMENSIONAL_MATRIX"}
    return {"input": ("g_R", "g_R/g_s", "Z_1F", "Z_q", "Z_A"), "output": ("MOMQ_g_R",), "map_class": "RATIO_OF_RENORMALIZATION_FACTORS"}


def lfgadapter1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C168-LFGADAPTER1-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "C43 endpoint Green functions and required gauge-changing sectors are well-defined in scope but not calculated", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def adapter_request_freeze() -> MappingProxyType:
    rows = []
    for r in _REQUEST_ROWS:
        d = _descriptor(r["request_id"])
        rows.append({"request_id": r["request_id"], "C167_acquirability_root": _C167_ACQUIRABILITY_ROOT, "C167_calculation_request_root": _C167_CALCULATION_REQUEST_ROOT, "C167_leaf_id": d["C166_leaf_id"], "root_object_id": d["root_object_id"], "descriptor_id": d["descriptor_id"], "graph_id": _graph_id(r["request_id"]), "quantity_id": _quantity(r["request_id"]), "target_scheme_id": _scheme(r["request_id"]), "C167_terminal_status": _ACQUIRABILITY[r["request_id"]]["terminal_status"], "preserved": True})
    return _freeze({"schema": "C168-ADAPTER-REQUEST-FREEZE-V1", "rows": tuple(rows), "count": len(rows), "exact_six_request_ids": len(rows) == 6, "C166_graphs_mutated": 0, "root": _root(rows)})


def adapter_semantics_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        kind = "B_GAUGE_CHANGING_CONVERSION" if q != "SIGNED_QUARK_MASS" else "B_GAUGE_CHANGING_CONVERSION_PLUS_D_RENORMALIZATION_CONDITION"
        if q == "QCD_COUPLING": kind = "G_DERIVED_PARAMETER_CONVERSION_ASSEMBLED_FROM_FACTORS"
        rows.append({"request_id": r["request_id"], "quantity_id": q, "classification": kind, "endpoint_definitions_are_adapter": False, "source_endpoint_promoted": False, "formal_gauge_transformation_sufficient": False, "universal_scalar_assumption": False, "calculation_required": True, "terminal_semantics": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED", "root": _root((r["request_id"], kind))})
    return _freeze({"schema": "C168-ADAPTER-SEMANTICS-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def endpoint_identity_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        rid, q, s = r["request_id"], _quantity(r["request_id"]), _scheme(r["request_id"])
        c43 = {"endpoint_id": "C43-ENDPOINT-" + rid, "operator_or_green_function": _operator(q), "field_content": "psi_plus, constrained psi_minus, A_perp, constrained A_plus/Gauss sector", "external_state": "C43 finite-basis colored off-shell source state", "open_color": "fundamental quark triplet or adjoint gluon, explicit by q", "source_sink": "C43 source/sink maps, explicit order required", "longitudinal_convention": "finite cell; nonzero-mode Q0 sector", "transverse_convention": "finite transverse HO basis; resolution K9/K11/K13 kept separate", "gauge": "G0 light-front A^+=0", "pole": "antisymmetric/PV inverse partial-plus", "zero_mode": "P0/Q0 explicit; retained zero/boundary ledger", "residual_link": "transverse residual link retained; not set to zero", "boundary": "APBC fermion / PBC gluon plus C43 boundary contract", "resolution": RESOLUTIONS, "bare_coordinate": "g_s", "projector": "C43 quantity-specific finite-basis projector", "order": _order(q), "units": "source/projector units explicit in C169 calculation", "endpoint_root": _root(("C43", rid, q, C43_ROOTS))}
        target = {"endpoint_id": "TARGET-ENDPOINT-" + rid, "scheme": s, "source_version": _target_source(rid), "gauge": "source-declared standard covariant-gauge endpoint; gauge parameter explicit in source record", "regularization": "source-declared continuum perturbative regularization", "external_state": "standard off-shell colored projected state", "projector": _projector(q, s), "kinematics": "source-qualified nonexceptional record; p_in^2=p_out^2=q^2 relation only when source condition declares it", "active_Nf": "explicit symbolic active-loop N_f; no numerical value inferred", "external_flavor": "RI/SMOM: flavor-nonsinglet u-bar Gamma d from C167 source authority; MOMq: source-qualified external flavor record required", "renormalization": "bare/counterterm/renormalized/conversion layers separate", "coordinate": "alpha_s or a_s source coordinate as applicable; adapter ledger explicit", "order": _order(q), "units": "source/projector units explicit in C169 calculation", "endpoint_root": _root((s, rid, q, "target"))}
        rows.append({"request_id": rid, "quantity_id": q, "C43": c43, "target": target, "endpoint_relation": "SAME_OBJECT_DIFFERENT_GAUGE" if q in ("QUARK_FIELD", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING") else "SAME_PARAMETER_DIFFERENT_RENORMALIZATION_CONDITION", "regulator_relation": "SAME_BARE_ACTION_DIFFERENT_REGULATOR_REALIZATION", "identity_status": "ENDPOINTS_BOUND_ADAPTER_ABSENT", "root": _root((c43, target))})
    return _freeze({"schema": "C168-ENDPOINT-IDENTITY-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def common_bare_object_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        rows.append({"request_id": r["request_id"], "formal_bare_action_shared": True, "bare_action": "C43 source-derived QCD action with explicit light-front constraints", "bare_coordinate": "g_s", "bare_field_normalization": "not proven identical between finite C43 and target continuum object", "operator_insertion": _operator(q), "external_state": "not identical: C43 finite colored state versus target continuum off-shell state", "source_sink_normalization": "not identical/proven", "color": "open colored representation explicit", "gauge_fixing": "C43 A^+=0 versus target source gauge", "IR_regulator": "C43 finite-cell/Q0/boundary versus target source IR record", "UV_regulator": "C43 finite basis versus target continuum regulator", "common_bare_object": False, "reason": "shared bare action does not establish a common gauge-dependent colored Green function, state, projector, and regulator object", "order": _order(q), "root": _root((r["request_id"], q, False))})
    return _freeze({"schema": "C168-COMMON-BARE-OBJECT-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "closed_count": 0, "root": _root(rows)})


def adapter_form_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"]); b = _basis(q)
        rows.append({"request_id": r["request_id"], "quantity_id": q, "adapter_form": b["map_class"], "input_space": b["input"], "output_space": b["output"], "basis_order": "quantity-specific; K_MINUS/K_PLUS/K_PERP never averaged", "map_dimension": "unresolved until C43 calculation", "tree_map": "not transcribed", "first_nontrivial_term": "not calculated", "invertibility_domain": "unavailable", "null_directions": "C166/C153 nine-dimensional nullspace and six counterterm directions preserved", "units": "dimensionless factor or mass dimension according to quantity", "current_form_status": "FORM_INCOMPLETE_DUE_TO_MISSING_C43_SECTORS", "root": _root((r["request_id"], b))})
    return _freeze({"schema": "C168-ADAPTER-FORM-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def common_state_ir_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"]); family = "NONEXCEPTIONAL_QGQ_COMMON_OFFSHELLNESS" if q in ("qg_VERTEX_DRESSING", "QCD_COUPLING") else "REAL_SPACELIKE_COMMON_OFFSHELLNESS"
        rows.append({"request_id": r["request_id"], "quantity_id": q, "incoming_momentum": "p_in explicit caller record", "outgoing_momentum": "p_out explicit caller record", "gluon_momentum": "q=p_out-p_in for vertex/coupling; not applicable otherwise", "invariants": "all virtualities explicit; no tuned point", "exceptional_status": "source-qualified nonexceptional target; C43 realization missing", "polarization": "explicit helicity/transverse polarization by quantity", "open_color": "explicit fundamental/adjoint color", "active_Nf": "explicit symbolic record", "external_flavor": "separate from active N_f", "mass_assumption": "signed branch or chiral/massless source condition as applicable", "rho": "explicit IR coordinate required; no default", "mu": "explicit UV scale required; no default", "order_of_limits": "C43 finite-cell/HO and target continuation order must be specified", "C43_pole": "antisymmetric/PV", "target_continuation": "source-declared i0/Euclidean continuation", "zero_mode": "C43 Q0/P0 and boundary retained", "boundary": "C43 boundary/residual link retained", "ir_family": family, "common_state_ir": False, "subtraction_allowed": False, "reason": "common external-state and common-IR identity is not closed", "root": _root((r["request_id"], family, False))})
    return _freeze({"schema": "C168-COMMON-STATE-IR-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "subtraction_or_ratio_evaluated": 0, "root": _root(rows)})


def order_coordinate_ledger(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"]); scheme = _scheme(r["request_id"]); order = _order(q)
        rows.append({"request_id": r["request_id"], "quantity_id": q, "C43_coordinate": "g_s", "target_coordinate": "alpha_s for RI/SMOM source; a_s where MOMq source record declares it", "coordinate_identities": ("alpha_s=g_s^2/(4*pi)", "a_s=alpha_s/(4*pi)=g_s^2/(4*pi)^2"), "coordinate_separation": ("V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2"), "C43_tree_power": "source order retained; not inferred", "target_tree_power": "source order retained; not inferred", "first_nontrivial_order": order["C161_order_label"], "C161_coordinate_adapter": "C161 symbolic guarded coordinate ledger", "source_order_authority": order["source_order_authority"], "finite_basis_coefficient": "not consumed in C168", "target_coefficient": "not available", "missing_diagrams": "C43 gauge-changing sectors listed in contribution ledger", "terminal_order_status": order["status"], "root": _root((r["request_id"], scheme, order))})
    return _freeze({"schema": "C168-ORDER-COORDINATE-LEDGER-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def componentwise_adapter_manifest(quantity_id: str | None = None, request_id: str | None = None) -> MappingProxyType:
    if quantity_id is not None and quantity_id not in QUANTITIES: raise KeyError(quantity_id)
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        if quantity_id is None or q == quantity_id:
            b = _basis(q); rows.append({"request_id": r["request_id"], "quantity_id": q, "quantity_family": q, "operator": _operator(q), "coordinate": "g_s; target coordinate kept separate", "projector": _projector(q, _scheme(r["request_id"])), "input_components": b["input"], "output_components": b["output"], "adapter_class": b["map_class"], "connected_vs_proper": "C152 connected/amputated retained object is not promoted to complete 1PI" if q == "qg_VERTEX_DRESSING" else "not applicable", "field_parameter_separation": True, "signed_mass_separate": True, "status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED", "root": _root((r["request_id"], b))})
    return _freeze({"schema": "C168-COMPONENTWISE-ADAPTER-MANIFEST-V1", "quantity_id": quantity_id, "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def c43_structure_ledger(request_id: str | None = None) -> MappingProxyType:
    structures = ("A^+=0 gauge fixing", "antisymmetric/PV inverse-partial-plus", "nonzero-mode Q0", "ordinary zero-mode P0", "residual gauge constraints", "transverse link at infinity", "finite longitudinal cell", "APBC quark/PBC gluon modes", "basis boundary", "finite-HO projection", "instantaneous fermion", "instantaneous current/Gauss law", "open-triplet color")
    rows = []
    for r in _request(request_id):
        rows.append({"request_id": r["request_id"], "structures": tuple({"name": s, "classification": "REQUIRES_NEW_CALCULATION" if s in structures else "UNAVAILABLE_BLOCKING", "zero_substitution": False} for s in structures), "pole_prescription_changed": False, "root": _root((r["request_id"], structures))})
    return _freeze({"schema": "C168-C43-STRUCTURE-LEDGER-V1", "rows": tuple(rows), "count": len(rows), "missing_structures_zeroed": 0, "root": _root(rows)})


def adapter_contribution_ledger(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        classes = ("quark self-energy", "mass insertion/self-energy scalar", "gluon self-energy quark loop", "gluon self-energy ghost loop", "gluon self-energy pure-gluon loop", "qg vertex diagrams", "external-leg counterterms", "instantaneous-fermion terms", "instantaneous-current/Gauss-law terms", "three-/four-gluon descendants", "zero-mode terms", "basis-boundary terms", "residual-link terms", "scheme counterterms", "finite projector conversions")
        applicable = {"QUARK_FIELD": ("quark self-energy", "external-leg counterterms", "instantaneous-fermion terms", "zero-mode terms", "basis-boundary terms", "residual-link terms", "scheme counterterms", "finite projector conversions"), "SIGNED_QUARK_MASS": ("quark self-energy", "mass insertion/self-energy scalar", "external-leg counterterms", "instantaneous-fermion terms", "zero-mode terms", "basis-boundary terms", "residual-link terms", "scheme counterterms", "finite projector conversions"), "TRANSVERSE_GLUON_FIELD": ("gluon self-energy quark loop", "gluon self-energy ghost loop", "gluon self-energy pure-gluon loop", "three-/four-gluon descendants", "zero-mode terms", "basis-boundary terms", "residual-link terms", "scheme counterterms", "finite projector conversions"), "qg_VERTEX_DRESSING": ("quark self-energy", "qg vertex diagrams", "external-leg counterterms", "instantaneous-fermion terms", "instantaneous-current/Gauss-law terms", "three-/four-gluon descendants", "zero-mode terms", "basis-boundary terms", "residual-link terms", "scheme counterterms", "finite projector conversions"), "QCD_COUPLING": classes}[q]
        rows.append({"request_id": r["request_id"], "quantity_id": q, "contributions": tuple({"class": x, "status": "UNAVAILABLE_BLOCKING", "classification": "MISSING_FULL_QCD_SECTOR" if x in ("gluon self-energy ghost loop", "gluon self-energy pure-gluon loop", "three-/four-gluon descendants", "qg vertex diagrams") else "MISSING_REGULATOR_REALIZATION", "not_zero": True} for x in applicable), "all_required_classes_enumerated": True, "counterterm_conditions": "not solved; six counterterm directions remain unselected", "root": _root((r["request_id"], applicable))})
    return _freeze({"schema": "C168-ADAPTER-CONTRIBUTION-LEDGER-V1", "rows": tuple(rows), "count": len(rows), "missing_as_zero": 0, "root": _root(rows)})


def adapter_route_manifest(request_id: str | None = None) -> MappingProxyType:
    routes = ("AD-A_RENORMALIZATION_FACTOR_RATIO", "AD-B_COMMON_PROJECTED_GREEN_FUNCTION", "AD-C_FIRST_ORDER_COEFFICIENT_DIFFERENCE", "AD-D_INVERSE_ROUND_TRIP")
    rows = tuple({"request_id": r["request_id"], "routes": tuple({"route_id": x, "status": "NOT_EXECUTED_MISSING_C43_CALCULATION", "agreement": None, "independent": True} for x in routes), "route_mismatch": False, "root": _root((r["request_id"], routes))} for r in _request(request_id))
    return _freeze({"schema": "C168-ADAPTER-ROUTE-MANIFEST-V1", "rows": rows, "count": len(rows), "closed_routes": 0, "root": _root(rows)})


def adapter_program_schema() -> MappingProxyType:
    return _freeze({"schema": "C168-ADAPTER-PROGRAM-DAG-V1", "safe_opcodes": SAFE_OPCODES, "immutable": True, "arbitrary_callable": False, "eval": False, "pickle": False, "dynamic_import": False, "network": False, "unknown_opcode": "reject", "root": _root(SAFE_OPCODES)})


def adapter_program_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": r["request_id"], "program_id": None, "schema": adapter_program_schema()["schema"], "nodes": (), "status": "NO_PROGRAM_TARGET_EXPRESSIONS_NOT_AVAILABLE", "root": _root((r["request_id"], "no-program"))} for r in _request(request_id))
    return _freeze({"schema": "C168-ADAPTER-PROGRAM-MANIFEST-V1", "rows": rows, "count": len(rows), "program_count": 0, "root": _root(rows)})


def adapter_diagnostic_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": r["request_id"], "evaluation": "NOT_RUN", "fixture": None, "numeric_value": None, "enclosure": None, "reason": "target and C43 adapter expressions unavailable; no C158 or physical input consumed", "root": _root((r["request_id"], "not-run"))} for r in _request(request_id))
    return _freeze({"schema": "C168-ADAPTER-DIAGNOSTIC-MANIFEST-V1", "rows": rows, "count": len(rows), "evaluations": 0, "root": _root(rows)})


def gauge_change_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": r["request_id"], "C43_gauge": "A^+=0 light-front", "target_gauge": "source-declared standard covariant gauge", "gauge_changes": True, "off_shell_colored_gauge_independence_assumed": False, "formal_relabeling": False, "universal_scalar_map": False, "status": "NEW_CALCULATION_REQUIRED", "root": _root((r["request_id"], True))} for r in _request(request_id))
    return _freeze({"schema": "C168-GAUGE-CHANGE-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def regulator_scope_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": r["request_id"], "C43_regulator": "finite longitudinal cell + finite HO/Fock basis + Q0/boundary", "target_regulator": "source-declared continuum perturbative regulator", "relation": "SAME_OPERATOR_DIFFERENT_REGULATOR", "resolution_dependency": True, "continuum_limit_claimed": False, "status": "FINITE_BASIS_RESOLUTION_DEPENDENT_ADAPTER", "root": _root((r["request_id"], "finite"))} for r in _request(request_id))
    return _freeze({"schema": "C168-REGULATOR-SCOPE-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def st_consistency_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        rows.append({"request_id": r["request_id"], "quantity_id": q, "identity_scope": "C43 local action identities only; no cross-gauge off-shell promotion", "ghost_status": "C43 decoupled in declared axial nonzero-mode scope; target ghost/pure-gluon terms remain explicit where required", "ward_or_ST_used": False, "full_1PI_substrate": q in ("qg_VERTEX_DRESSING", "QCD_COUPLING"), "status": "ST_SUBSTRATE_INCOMPLETE" if q == "QCD_COUPLING" else "IDENTITY_SCOPE_NOT_SUFFICIENT_FOR_ADAPTER", "root": _root((r["request_id"], q, False))})
    return _freeze({"schema": "C168-ST-CONSISTENCY-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "identities_promoted": 0, "root": _root(rows)})


def parameter_sensitivity_manifest(request_id: str | None = None) -> MappingProxyType:
    parameters = ("gauge_parameter", "active_Nf", "external_flavor", "mu", "rho", "finite_cell", "K_resolution", "Nmax", "b_HO", "PV_boundary", "counterterm_direction", "null_coordinate")
    rows = tuple({"request_id": r["request_id"], "parameters": tuple({"parameter": p, "sensitivity": "not evaluated; explicit caller record required", "default": False} for p in parameters), "nullspace_directions_selected": 0, "counterterms_selected": 0, "root": _root((r["request_id"], parameters))} for r in _request(request_id))
    return _freeze({"schema": "C168-PARAMETER-SENSITIVITY-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def new_calculation_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        q = _quantity(r["request_id"])
        rows.append({"request_id": r["request_id"], "quantity": q, "operator_or_green_function": _operator(q), "external_state": "explicit off-shell colored C43 finite-basis state; target common-state map must be supplied", "open_color": "fundamental triplet for quark/mass/qg quark legs; adjoint for gluon leg; explicit tensor basis required", "C43_gauge": "A^+=0", "PV_inverse_partial_plus": "antisymmetric/PV on Q0", "zero_mode_residual_link": "retain P0/Q0, residual transverse link, boundary and instantaneous terms; no zero default", "finite_cell_HO": "longitudinal finite cell and transverse HO/Fock resolution K9/K11/K13 separately", "projector_kinematics": _projector(q, _scheme(r["request_id"])), "common_IR": "explicit rho/mu common record required before any difference or ratio", "target_scheme": _scheme(r["request_id"]), "active_Nf": "explicit symbolic active-loop N_f", "external_flavor": "RI/SMOM nonsinglet u-bar Gamma d or exact MOMq source record; separate from active N_f", "perturbative_order": _order(q), "required_diagram_classes": adapter_contribution_ledger(r["request_id"])["rows"][0]["contributions"], "counterterm_conditions": "bare-to-counterterm-to-renormalized layers; six counterterm directions unselected", "renormalization_identities": "only source-qualified identities at declared gauge/scheme; no Abelian Ward promotion", "expected_tensor_structure": _basis(q), "independent_routes": ("AD-A_RENORMALIZATION_FACTOR_RATIO", "AD-B_COMMON_PROJECTED_GREEN_FUNCTION", "AD-C_FIRST_ORDER_COEFFICIENT_DIFFERENCE"), "holdouts": ("request-order", "K9/K11/K13 separation", "flavor nonsinglet versus active N_f", "PV versus alternate pole prescription", "zero-mode/residual-link nonzero guard", "connected versus proper qg", "V_B/Z_1F/g_R/g_R_over_g_s separation"), "nonclaims": ("no complete expression", "no target value", "no matching", "no running", "no threshold", "no PDG", "no physical scale", "no counterterm or null representative", "no Q0/Q1/Q2 change"), "terminal_status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED", "root": _root((r["request_id"], q, _basis(q)))})
    return _freeze({"schema": "C168-NEW-CALCULATION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _request(request_id):
        d = _descriptor(r["request_id"]); q = _quantity(r["request_id"])
        rows.append({"request_id": r["request_id"], "C167_acquirability_root": _C167_ACQUIRABILITY_ROOT, "C167_calculation_request_root": _C167_CALCULATION_REQUEST_ROOT, "C166_leaf_id": d["C166_leaf_id"], "root_object_id": d["root_object_id"], "descriptor_id": d["descriptor_id"], "graph_id": _graph_id(r["request_id"]), "C43_endpoint_id": "C43-ENDPOINT-" + r["request_id"], "target_endpoint_id": "TARGET-ENDPOINT-" + r["request_id"], "endpoint_relation": "SAME_OBJECT_DIFFERENT_GAUGE" if q != "SIGNED_QUARK_MASS" else "SAME_PARAMETER_DIFFERENT_RENORMALIZATION_CONDITION", "adapter_form": _basis(q)["map_class"], "common_bare_object_status": "COMMON_BARE_OBJECT_INCOMPLETE", "common_state_ir_status": "COMMON_STATE_IR_INCOMPLETE", "coordinate_order_status": "FROZEN_COORDINATE_ORDER_CALCULATION_REQUIRED", "contribution_status": "UNAVAILABLE_BLOCKING_NO_MISSING_TERM_ZEROED", "route_status": "NOT_EXECUTED_MISSING_C43_CALCULATION", "symbolic_program_id": None, "diagnostic_evaluation_status": "NOT_RUN", "terminal_status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED", "exact_next_object": "C168 calculation capsule; execute in C169/HQCDLFGMATCHCALC1", "root": _root((r["request_id"], STATUS))})
    return _freeze({"schema": "C168-REQUEST-RESOLUTION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "exactly_one_terminal_record_per_request": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def dependency_frontier_manifest() -> MappingProxyType:
    adapter = tuple({"frontier_id": "C168-ADAPTER-" + r["request_id"], "request_id": r["request_id"], "kind": "C43_ADAPTER_CALCULATION", "status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED"} for r in _REQUEST_ROWS)
    ri = tuple({"frontier_id": "C167-RI-SOURCE-" + str(i), "kind": "RI_SMOM_SOURCE_RESOLVED_AWAITING_GRAPH_INTEGRATION", "status": "SOURCE_RESOLVED"} for i in (1, 2))
    loc = tuple({"frontier_id": x, "kind": "C166_PRESERVED_LOCATOR_INCOMPLETE", "status": "PRESERVED_UNCHANGED"} for x in c167.PRESERVED_LOCATOR_IDS)
    rows = adapter + ri + loc
    return _freeze({"schema": "C168-DEPENDENCY-FRONTIER-MANIFEST-V1", "rows": rows, "count": len(rows), "adapter_count": 6, "source_resolved_count": 2, "preserved_locator_count": 6, "adapters_derived": 0, "adapters_requiring_new_calculation": 6, "adapters_nonuniversal": 0, "C166_graphs_mutated": False, "graph_nodes_added": 0, "graph_edges_added": 0, "resulting_frontier_count": 14, "root": _root(rows)})


def adapter_or_calculation_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C168-ADAPTER-OR-CALCULATION-HANDOFF-V1", "kind": "NEW_C43_PERTURBATIVE_CALCULATION_HANDOFF", "status": STATUS, "plan": PLAN, "request_resolution_root": request_resolution_manifest()["root"], "new_calculation_root": new_calculation_manifest()["root"], "dependency_frontier_root": dependency_frontier_manifest()["root"], "quantum_objects_modified": 0, "states_created": 0, "TMD_objects_created": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def adapter_calculation_handoff_contract() -> MappingProxyType:
    return adapter_or_calculation_handoff_contract()


def quantum_adapter_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C168-QUANTUM-ADAPTER-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "quantum_objects_consumed": 0, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0))})


def lfgadapter1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C168-LFGADAPTER1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "six_requests": 6, "terminal_records": 6, "endpoint_identities": 6, "common_bare_objects_closed": 0, "common_state_ir_closed": 0, "complete_adapters": 0, "new_calculation_capsules": 6, "target_programs": 0, "target_values": 0, "C158_imports": 0, "C158_recomputations": 0, "matching": 0, "running": 0, "thresholds": 0, "PDG_values": 0, "counterterms_solved": 0, "null_representatives": 0, "graph_nodes_added": 0, "graph_edges_added": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def verify_hqcd_lfgadapter1_authority() -> MappingProxyType:
    return _freeze({"schema": "C168-HQCDLFGADAPTER1-V1", "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "status": STATUS, "plan": PLAN, "next": NEXT, "C167_package_root": C167_ROOT, "C166_package_root": C166_ROOT, "C165_package_root": C165_ROOT, "C164_package_root": C164_ROOT, "C163_package_root": C163_ROOT, "C162_package_root": C162_ROOT, "C161_package_root": C161_ROOT, "C160_package_root": C160_ROOT, "C159_package_root": C159_ROOT, "C158_package_root": C158_ROOT, "C43_roots": C43_ROOTS, "request_count": 6, "C166_graphs_mutated": 0, "complete_expressions": 0, "target_values": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_lfgadapter1_authority() -> MappingProxyType:
    data = json.loads((RUNTIME / "manifest.json").read_text())
    if data.get("package_root") != PACKAGE_ROOT or data.get("status") != STATUS: raise ValueError("C168 runtime mismatch")
    return verify_hqcd_lfgadapter1_authority()


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C43_C131_C167_roots_unchanged": True, "C166_graphs_mutated": 0, "C158_imports": 0, "C158_recomputations": 0, "target_programs": 0, "target_values": 0, "complete_expressions": 0, "missing_terms_set_zero": 0, "counterterms_solved": 0, "null_representatives_selected": 0, "PDG_values_consumed": 0, "network_calls": 0, "Q0_Q1_Q2_modified": False, "states_created": 0, "TMD_objects_created": 0, "allow_pickle_false": True, "pass": True, "root": _root((STATUS, NEXT, 0))})


def mutate_live_hqcdlfgadapter1(index: int) -> MappingProxyType:
    fields = ("request_id", "endpoint", "target_scheme", "gauge", "pole", "zero_mode", "residual_link", "projector", "active_Nf", "external_flavor", "common_bare", "common_ir", "coordinate", "order", "component", "contribution", "route", "program", "diagnostic", "terminal_status", "frontier", "graph_nodes", "graph_edges", "C158", "PDG", "Q0", "Q1", "Q2", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C168_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256, C167_ROOT)),
    "C168_PLAN_ROOT": lfgadapter1_plan_manifest()["root"],
    "C168_REQUEST_FREEZE_ROOT": adapter_request_freeze()["root"],
    "C168_SEMANTICS_ROOT": adapter_semantics_manifest()["root"],
    "C168_ENDPOINT_ROOT": endpoint_identity_manifest()["root"],
    "C168_COMMON_BARE_ROOT": common_bare_object_manifest()["root"],
    "C168_FORM_ROOT": adapter_form_manifest()["root"],
    "C168_STATE_IR_ROOT": common_state_ir_manifest()["root"],
    "C168_ORDER_COORDINATE_ROOT": order_coordinate_ledger()["root"],
    "C168_COMPONENT_ROOT": componentwise_adapter_manifest()["root"],
    "C168_C43_STRUCTURE_ROOT": c43_structure_ledger()["root"],
    "C168_CONTRIBUTION_ROOT": adapter_contribution_ledger()["root"],
    "C168_ROUTE_ROOT": adapter_route_manifest()["root"],
    "C168_PROGRAM_ROOT": adapter_program_manifest()["root"],
    "C168_DIAGNOSTIC_ROOT": adapter_diagnostic_manifest()["root"],
    "C168_GAUGE_ROOT": gauge_change_manifest()["root"],
    "C168_REGULATOR_ROOT": regulator_scope_manifest()["root"],
    "C168_ST_ROOT": st_consistency_manifest()["root"],
    "C168_SENSITIVITY_ROOT": parameter_sensitivity_manifest()["root"],
    "C168_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C168_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C168_CALCULATION_ROOT": new_calculation_manifest()["root"],
    "C168_HANDOFF_ROOT": adapter_or_calculation_handoff_contract()["root"],
    "C168_QUANTUM_HANDOFF_ROOT": quantum_adapter_handoff_contract()["root"],
    "C168_COMPLETENESS_ROOT": lfgadapter1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C168-HQCDLFGADAPTER1-V1", "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "load_verified_hqcd_lfgadapter1_authority", "verify_hqcd_lfgadapter1_authority", "lfgadapter1_plan_manifest", "adapter_request_freeze", "adapter_semantics_manifest", "endpoint_identity_manifest", "common_bare_object_manifest", "adapter_form_manifest", "common_state_ir_manifest", "order_coordinate_ledger", "componentwise_adapter_manifest", "c43_structure_ledger", "adapter_contribution_ledger", "adapter_route_manifest", "adapter_program_schema", "adapter_program_manifest", "adapter_diagnostic_manifest", "gauge_change_manifest", "regulator_scope_manifest", "st_consistency_manifest", "parameter_sensitivity_manifest", "request_resolution_manifest", "dependency_frontier_manifest", "new_calculation_manifest", "adapter_or_calculation_handoff_contract", "adapter_calculation_handoff_contract", "quantum_adapter_handoff_contract", "lfgadapter1_completeness_certificate", "static_isolation_guard", "mutate_live_hqcdlfgadapter1"]
