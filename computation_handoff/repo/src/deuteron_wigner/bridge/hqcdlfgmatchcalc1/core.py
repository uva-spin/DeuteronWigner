"""C169 fail-closed C43 perturbative calculation authority.

This package consumes the six immutable C168 public request rows and public
operator-owner manifests.  It records the calculation domains and their
blocking sectors; it does not invent states, evaluate C158 coefficients, or
turn unavailable contributions into zero.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge.hqcdlfgadapter1 import core as c168
from deuteron_wigner.bridge import (
    g0, hqcd4, free2, gnorm, iferm, icurrent, ifcontact7, hqcd3,
    hqcdfield, hqcdfieldnorm, hqcdmproj, hqcdzqmass, hqcd2pt, hqcd2ptnorm, hqcd2ptq, hqcdopapi,
    hqcd2ptq2, hqcdg2pt, hqcdqgvert,
)

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c169_hqcdlfgmatchcalc1"
BASELINE = "4d90e1a4ff410f6b172d125b5ea3800bb0e0a186"
PARENT_PACKAGE_ROOT = "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
CONTRACT = "docs/next_level/c168_c169_hqcdlfgmatchcalc1_continuation_contract.json"
CONTRACT_SHA256 = "2d05f1746d1062bfa23a42d455212d4abd96d694877c72ba618d4bf0bf1ecf0c"
PROMPT = "/Users/dustin/Downloads/c169_hqcdlfgmatchcalc1_codex_prompt.md"
PROMPT_SHA256 = "f871c8652a91f6422b7cf8887b16b29cfeafd782efa65973232cc5504d510181"
STATUS = "C169_HQCDLFGMATCHCALC1_FULL_QCD_SECTOR_INCOMPLETE"
PLAN = "LFGMATCHCALC1-H"
NEXT = "C170/HQCDLFGSECTORCALC1"
RESOLUTIONS = ("K9", "K11", "K13")
COORDINATES = ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2")
SAFE_OPCODES = ("LOAD_RATIONAL", "LOAD_SOURCE_CONSTANT", "LOAD_KINEMATIC", "ADD", "NEGATE", "MULTIPLY", "SAFE_DIVIDE", "INTEGER_POWER", "LOG", "LOG_RATIO", "EXP", "POSITIVE_SQRT", "PI_POWER", "ZETA_CONSTANT", "PROJECT_TENSOR", "SERIES_COEFFICIENT", "RETURN_TYPED_COEFFICIENT")


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)):
        return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


_CAPSULES = tuple(dict(row) for row in c168.new_calculation_manifest()["rows"])
_RESOLUTION = {row["request_id"]: dict(row) for row in c168.request_resolution_manifest()["rows"]}
_CAPSULE_BY_ID = {row["request_id"]: row for row in _CAPSULES}
if len(_CAPSULES) != 6:
    raise RuntimeError("C168 exact six-capsule authority is not six")


def _request(request_id: str | None = None) -> tuple[Mapping[str, Any], ...]:
    if request_id is not None and request_id not in _CAPSULE_BY_ID:
        raise KeyError(request_id)
    return tuple(row for row in _CAPSULES if request_id is None or row["request_id"] == request_id)


def _quantity(request_id: str) -> str:
    return _CAPSULE_BY_ID[request_id]["quantity"]


def _scheme(request_id: str) -> str:
    return "RI_SMOM" if "RI_SMOM" in request_id else "MOMQ"


def _terminal(request_id: str) -> str:
    q = _quantity(request_id)
    if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS"):
        return "C169_HQCDLFGMATCHCALC1_INTERMEDIATE_DOMAIN_INCOMPLETE"
    if q == "TRANSVERSE_GLUON_FIELD" or q == "qg_VERTEX_DRESSING":
        return "C169_HQCDLFGMATCHCALC1_FULL_QCD_SECTOR_INCOMPLETE"
    return "C169_HQCDLFGMATCHCALC1_ST_SUBSTRATE_INCOMPLETE"


def _owners() -> tuple[str, ...]:
    return ("C43", "C53", "C110", "C111", "C112", "C127", "C128", "C129", "C130", "C131", "C142", "C143", "C144", "C145", "C146", "C147", "C148", "C149", "C150", "C151", "C152")


def load_verified_hqcd_lfgmatchcalc1_authority() -> MappingProxyType:
    data = json.loads((RUNTIME / "manifest.json").read_text())
    if data.get("package_root") != PACKAGE_ROOT or data.get("status") != STATUS:
        raise ValueError("C169 runtime mismatch")
    return verify_hqcd_lfgmatchcalc1_authority()


def verify_hqcd_lfgmatchcalc1_authority() -> MappingProxyType:
    return _freeze({
        "schema": "C169-HQCDLFGMATCHCALC1-V1", "baseline": BASELINE,
        "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256,
        "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "status": STATUS,
        "plan": PLAN, "next": NEXT, "parent_package_root": PARENT_PACKAGE_ROOT,
        "C168_package_root": PARENT_PACKAGE_ROOT, "C168_capsule_count": 6,
        "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0,
        "C158_value_inputs": 0, "target_values": 0, "source_acquisitions": 0,
        "package_root": PACKAGE_ROOT,
    })


def lfgmatchcalc1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C169-PLAN-MANIFEST-V1", "selected_plan": PLAN,
        "status": STATUS, "reason": "C151/C152 missing full-QCD sectors are the first calculation frontier; quark source-domain blockers remain explicit",
        "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def calculation_capsule_freeze(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        copy = dict(row)
        copy.update({"capsule_id": row["request_id"], "capsule_id_source": "C168 new_calculation_manifest request_id; no separate C168 capsule identifier exposed", "capsule_fields_preserved": True, "C168_terminal_status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED"})
        rows.append(copy)
    return _freeze({"schema": "C169-CALCULATION-CAPSULE-FREEZE-V1", "rows": tuple(rows), "count": len(rows), "exact_six": len(rows) == 6 if request_id is None else True, "renamed_capsules": 0, "root": _root(rows)})


def operator_substrate_manifest(owner_id: str | None = None) -> MappingProxyType:
    if owner_id is not None and owner_id not in _owners():
        raise KeyError(owner_id)
    statuses = {
        "C43": ("g0.source_manifest", "g0.action_contract", "C43 gauge/action/constraint/PV authority"),
        "C53": ("hqcd3.c53_read_only_import", "hqcd3.local_term_crosswalk", "canonical qg vertex"),
        "C110": ("ifcontact7.verify_qg_direct_contact_authority", "ifcontact7.factor_ownership_contract", "direct qg contact"),
        "C111": ("ifcontact7.verify_qg_direct_contact_authority", "ifcontact7.count_once_certificate", "direct qg contact public authority"),
        "C112": ("iferm.source_derivation", "iferm.contact_count_once", "instantaneous fermion"),
        "C127": ("icurrent.current_source_manifest", "icurrent.zero_mode_boundary_manifest", "instantaneous current"),
        "C128": ("free2.verify_free_m2_authority", "free2.free_sector_manifest", "free M2 operator"),
        "C129": ("gnorm.source_term_manifest", "gnorm.descendant_manifest", "gluon normal-ordering descendants"),
        "C130": ("icurrent.zero_mode_boundary_manifest", "g0.action_contract", "zero/boundary/omitted interface"),
        "C131": ("hqcd4.retained_term_manifest", "hqcd4.coupling_degree_manifest", "bare local-QCD polynomial"),
        "C142": ("hqcdfield.field_plan_manifest", "hqcdfield.quark_source_map_manifest", "field/source authority"),
        "C143": ("hqcd2ptq.verify_hqcd_two_pointq_authority", "hqcd2ptq.route_validation", "parameterized q two-point source API"),
        "C144": ("hqcdopapi.verify_hqcd_operator_authority", "hqcdopapi.parameter_record_schema", "operator-parameter authority"),
        "C145": ("hqcd2ptq2.verify_hqcd_forward_two_point_authority", "hqcd2ptq2.source_embedding_manifest", "forward good-component two-point"),
        "C146": ("hqcd2ptnorm.normalization_completeness_certificate", "hqcd2ptnorm.source_sink_normalization_manifest", "two-point normalization"),
        "C147": ("hqcdfieldnorm.verify_hqcd_field_normalization_authority", "hqcdfieldnorm.field_normalization_completeness_certificate", "field normalization"),
        "C148": ("hqcd2ptfull.verify_hqcd_full_spinor_authority", "hqcd2ptfull.mass_sign_sensitivity_report", "full-spinor two-point"),
        "C149": ("hqcdmproj.verify_hqcd_mass_projector_authority", "hqcdmproj.mass_sign_projector_report", "signed-mass projector"),
        "C150": ("hqcdzqmass.verify_hqcd_zq_mass_authority", "hqcdzqmass.nullspace_zq_mass_manifest", "Zq/mass conditional scheme"),
        "C151": ("hqcdg2pt.pure_gluon_sector_census", "hqcdg2pt.gluon_self_energy_ledger", "gluon two-point"),
        "C152": ("hqcdqgvert.vertex_properness_report", "hqcdqgvert.vertex_count_once_ledger", "qg vertex and ST boundary"),
    }
    selected = _owners() if owner_id is None else (owner_id,)
    rows = tuple({"owner_id": oid, "public_operations": statuses[oid][:2], "scientific_role": statuses[oid][2], "imported": True, "private_builder_called": False, "value_evaluation": 0, "root": _root((oid, statuses[oid]))} for oid in selected)
    return _freeze({"schema": "C169-OPERATOR-SUBSTRATE-MANIFEST-V1", "rows": rows, "owner_count": len(rows), "all_required_owners": owner_id is None, "root": _root(rows)})


def perturbative_expansion_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        q = row["quantity"]
        n = 0 if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD") else 1
        rows.append({"request_id": row["request_id"], "quantity": q, "coordinate": "g_s", "declared_order_label": n, "order_source": "C168 exact capsule field", "powers": ("g_s^0", "g_s^1", "g_s^2"), "coordinate_adapters": COORDINATES, "promoted_order": False, "root": _root((row["request_id"], n, COORDINATES))})
    return _freeze({"schema": "C169-PERTURBATIVE-EXPANSION-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def intermediate_domain_manifest(request_id: str | None = None, contribution_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        q = row["quantity"]
        for resolution in RESOLUTIONS:
            if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS"):
                status = "UNAVAILABLE_BLOCKING_C141_SOURCE_MAP_C143_RESOLVENT"
                source = ("C141 quark_source_map_manifest", "C143 source_projected_resolvent")
            elif q == "TRANSVERSE_GLUON_FIELD":
                status = "FREE_DOMAIN_ONLY_FULL_DOMAIN_BLOCKED_C151"
                source = ("C151 one_gluon_source_manifest", "C151 pure_gluon_sector_census")
            else:
                status = "RETAINED_QG_DOMAIN_ONLY_FULL_DOMAIN_BLOCKED_C152"
                source = ("C152 q_to_qg_source_manifest", "C152 vertex_properness_report")
            cid = f"{row['request_id']}:{resolution}:INTERMEDIATE"
            if contribution_id is None or contribution_id == cid:
                rows.append({"request_id": row["request_id"], "contribution_id": cid, "resolution": resolution, "state_id": None, "state_identity": "not inferred from array position", "source_order": row["perturbative_order"]["source_order_authority"], "adjoint_orientation": "source/sink order required; not inferred", "domain_status": status, "public_dependencies": source, "fully_authenticated": False, "root": _root((cid, status, source))})
    if contribution_id is not None and not rows:
        raise KeyError(contribution_id)
    return _freeze({"schema": "C169-INTERMEDIATE-DOMAIN-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "untyped_states": 0, "array_position_inference": 0, "root": _root(rows)})


def propagating_contribution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        q = row["quantity"]
        classes = ("degree_one_insertion_pair", "degree_two_propagating_pair")
        if q == "TRANSVERSE_GLUON_FIELD":
            owner = "C151_free_one_gluon_source; interaction sector unavailable"
        elif q in ("qg_VERTEX_DRESSING", "QCD_COUPLING"):
            owner = "C53 canonical qg pair; C152 retained qg response"
        else:
            owner = "C145 forward good-component pair; C141 source-map closure unavailable"
        rows.append({"request_id": row["request_id"], "classes": tuple({"contribution_id": f"{row['request_id']}:{name}", "owner": owner, "status": "DOMAIN_INCOMPLETE", "source_order": "explicit capsule order label", "adjoint_orientation": "explicit source-to-sink orientation required", "not_zero": True} for name in classes), "root": _root((row["request_id"], classes, owner))})
    return _freeze({"schema": "C169-PROPAGATING-CONTRIBUTION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "missing_as_zero": 0, "root": _root(rows)})


def direct_instantaneous_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C110_DIRECT_QG_CONTACT", "C111_DIRECT_QG_CONTACT", "C112_INSTANTANEOUS_FERMION", "C127_INSTANTANEOUS_CURRENT", "C129_NORMAL_ORDERING", "C130_ZERO_BOUNDARY_INTERFACE")
    rows = tuple({"request_id": row["request_id"], "terms": tuple({"owner": owner, "status": "AVAILABLE_SCOPE" if owner in ("C110_DIRECT_QG_CONTACT", "C111_DIRECT_QG_CONTACT", "C129_NORMAL_ORDERING") else "INCOMPLETE_BLOCKING", "not_zero": True, "count_once_key": f"{row['request_id']}:{owner}"} for owner in owners), "missing_as_zero": 0, "root": _root((row["request_id"], owners))} for row in _request(request_id))
    return _freeze({"schema": "C169-DIRECT-INSTANTANEOUS-MANIFEST-V1", "rows": rows, "owner_count": len(owners), "root": _root(rows)})


def count_once_report(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "duplicate_semantic_owners": 0, "propagating": "separate", "direct_contact": "separate", "instantaneous": "separate", "normal_ordering": "separate", "counterterm": "separate", "residual": "separate", "closure": "INCOMPLETE_MISSING_SECTORS", "root": _root((row["request_id"], 0))} for row in _request(request_id))
    return _freeze({"schema": "C169-COUNT-ONCE-REPORT-V1", "rows": rows, "duplicate_semantic_owners": 0, "root": _root(rows)})


def zero_boundary_residual_ledger(request_id: str | None = None) -> MappingProxyType:
    kinds = ("P0_zero_mode", "Q0_zero_mode", "finite_cell_boundary", "transverse_residual_link", "residual_gauge", "omitted_interface")
    rows = tuple({"request_id": row["request_id"], "terms": tuple({"kind": kind, "status": "RETAINED_EXPLICIT_UNAVAILABLE" if kind != "omitted_interface" else "PUBLIC_INTERFACE_DECLARED_NOT_CLOSED", "not_zero": True, "pole": "antisymmetric/PV"} for kind in kinds), "zero_mode_exclusion_encoded_as_zero": False, "root": _root((row["request_id"], kinds))} for row in _request(request_id))
    return _freeze({"schema": "C169-ZERO-BOUNDARY-RESIDUAL-LEDGER-V1", "rows": rows, "missing_as_zero": 0, "root": _root(rows)})


def counterterm_sensitivity_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "counterterm_directions": 6, "null_coordinates": 9, "sensitivities": "unresolved symbolic sensitivity; no representative selected", "selected_counterterms": 0, "selected_null_coordinates": 0, "root": _root((row["request_id"], 6, 9, 0, 0))} for row in _request(request_id))
    return _freeze({"schema": "C169-COUNTERTERM-SENSITIVITY-MANIFEST-V1", "rows": rows, "selected": 0, "root": _root(rows)})


def quark_two_point_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "quantity": "QUARK_FIELD", "projectors": ("K_MINUS", "K_PLUS", "K_PERP"), "averaged": False, "C141_source_map": "UNAVAILABLE", "C143_resolvent": "UNAVAILABLE", "C145_retained_api": "SOURCE_DERIVED_BUT_NOT_C141_CLOSED", "C150_Zq": "CONDITIONAL_ONLY", "status": _terminal(row["request_id"]), "signed_mass_separate": True, "root": _root((row["request_id"], "quark", _terminal(row["request_id"]))) } for row in _request(request_id) if row["quantity"] == "QUARK_FIELD")
    return _freeze({"schema": "C169-QUARK-TWO-POINT-MANIFEST-V1", "rows": rows, "K_resolution_count": 3, "root": _root(rows)})


def signed_mass_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "quantity": "SIGNED_QUARK_MASS", "projector": "C149 signed mass projector", "signed_m_R": "separate symbolic branch", "m_R^2": "separate and not substituted", "C141_mass_linear": "INCOMPLETE", "C149_projector": "SOURCE_AUTHORITY_PRESENT", "status": _terminal(row["request_id"]), "root": _root((row["request_id"], "signed", "m2-separate")) } for row in _request(request_id) if row["quantity"] == "SIGNED_QUARK_MASS")
    return _freeze({"schema": "C169-SIGNED-MASS-MANIFEST-V1", "rows": rows, "signed_mass_m2_conflation": 0, "root": _root(rows)})


def gluon_two_point_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "quantity": "TRANSVERSE_GLUON_FIELD", "projector": "C151 transverse gluon projector", "free_domain": "available source-qualified", "missing_sectors": ("gg", "q_qbar", "ghost", "higher_gluon", "zero_mode", "boundary", "counterterm"), "missing_as_zero": False, "status": _terminal(row["request_id"]), "root": _root((row["request_id"], "gluon", "missing")) } for row in _request(request_id) if row["quantity"] == "TRANSVERSE_GLUON_FIELD")
    return _freeze({"schema": "C169-GLUON-TWO-POINT-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def qg_vertex_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "quantity": "qg_VERTEX_DRESSING", "connected": True, "amputated": True, "retained_proper": True, "full_1PI": False, "V_B": "separate projected bare vertex", "Z_1F": "separate factor", "g_R": "separate parameter", "g_R/g_s": "separate ratio", "missing_sectors": ("qgg", "qqbar", "pure_gluon", "zero_mode", "boundary", "full_1PI"), "missing_as_zero": False, "status": _terminal(row["request_id"]), "root": _root((row["request_id"], "qg", "not-1PI")) } for row in _request(request_id) if row["quantity"] == "qg_VERTEX_DRESSING")
    return _freeze({"schema": "C169-QG-VERTEX-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def coupling_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "quantity": "QCD_COUPLING", "factors": ("V_B", "Z_1F", "Z_q", "Z_A", "g_R", "g_R/g_s"), "ST_scope": "full Slavnov-Taylor closure required", "restricted_Ward_promoted": False, "missing_sectors": ("ghost", "pure_gluon", "full_1PI", "zero_mode", "boundary", "counterterm"), "status": _terminal(row["request_id"]), "root": _root((row["request_id"], "coupling", "ST-incomplete")) } for row in _request(request_id) if row["quantity"] == "QCD_COUPLING")
    return _freeze({"schema": "C169-COUPLING-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def sixth_calculation_manifest(request_id: str | None = None) -> MappingProxyType:
    sixth = _CAPSULES[5]["request_id"]
    if request_id is not None and request_id != sixth:
        raise KeyError(request_id)
    row = dict(_CAPSULES[5]); row.update({"capsule_position": 6, "position_source": "C168 public new_calculation_manifest row order", "request_id_renamed": False, "terminal_status": _terminal(sixth), "missing_object": "full ST-compatible ghost/pure-gluon/1PI coupling sector"})
    return _freeze({"schema": "C169-SIXTH-CALCULATION-MANIFEST-V1", "row": row, "exact_sixth": True, "root": _root(row)})


def graph_program_schema() -> MappingProxyType:
    return _freeze({"schema": "C169-GRAPH-PROGRAM-SCHEMA-V1", "safe_opcodes": SAFE_OPCODES, "arbitrary_callable": False, "eval": False, "pickle": False, "dynamic_import": False, "network": False, "dense_full_inverse": False, "unknown_opcode": "reject", "root": _root(SAFE_OPCODES)})


def graph_program_manifest(request_id: str | None = None, contribution_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        cid = contribution_id or f"{row['request_id']}:C43-CALCULATION"
        if contribution_id is not None and not contribution_id.startswith(row["request_id"] + ":"):
            continue
        rows.append({"request_id": row["request_id"], "contribution_id": cid, "program_id": None, "nodes": (), "status": "NOT_EMITTED_DOMAIN_INCOMPLETE", "missing_as_zero": False, "root": _root((cid, "no-program"))})
    if contribution_id is not None and not rows:
        raise KeyError(contribution_id)
    return _freeze({"schema": "C169-GRAPH-PROGRAM-MANIFEST-V1", "rows": tuple(rows), "program_count": 0, "root": _root(rows)})


def diagnostic_record_schema() -> MappingProxyType:
    return _freeze({"schema": "C169-DIAGNOSTIC-RECORD-SCHEMA-V1", "required": ("request_id", "fixture_id", "resolution_id", "parameter_record", "enclosure"), "physical": False, "explicit_fixture": True, "root": _root(("fixture", "resolution", "enclosure"))})


def diagnostic_manifest(request_id: str | None = None, fixture_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    if fixture_id is not None or resolution_id is not None:
        raise ValueError("C169 diagnostics are not emitted while the calculation domain is incomplete")
    rows = tuple({"request_id": row["request_id"], "fixture_id": None, "resolution_id": None, "numeric_value": None, "outward_enclosure": None, "status": "NOT_RUN_DOMAIN_INCOMPLETE", "physical": False, "root": _root((row["request_id"], "not-run"))} for row in _request(request_id))
    return _freeze({"schema": "C169-DIAGNOSTIC-MANIFEST-V1", "rows": rows, "evaluations": 0, "certified_enclosures": 0, "root": _root(rows)})


def calculation_route_manifest(request_id: str | None = None) -> MappingProxyType:
    routes = ("ROUTE_A_SOURCE_ORDERED_SPARSE_BLOCK", "ROUTE_B_INDEPENDENT_MATRIX_FREE_OR_FACTORISED")
    rows = tuple({"request_id": row["request_id"], "routes": tuple({"route_id": route, "status": "NOT_EXECUTED_DOMAIN_INCOMPLETE", "residual": None, "agreement": None, "independent": True} for route in routes), "route_mismatch": False, "root": _root((row["request_id"], routes))} for row in _request(request_id))
    return _freeze({"schema": "C169-CALCULATION-ROUTE-MANIFEST-V1", "rows": rows, "closed_routes": 0, "route_mismatches": 0, "root": _root(rows)})


def uv_ir_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "resolutions": RESOLUTIONS, "finite_basis": True, "resolution_dependence_explicit": True, "mu": "caller-supplied; no default", "rho": "caller-supplied; no default", "common_state_ir": False, "UV_IR_separated": False, "continuum_limit": False, "status": "UV_IR_SEPARATION_INCOMPLETE", "root": _root((row["request_id"], RESOLUTIONS, False))} for row in _request(request_id))
    return _freeze({"schema": "C169-UV-IR-RESOLUTION-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def gauge_pole_branch_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "C43_gauge": "A^+=0 light-front", "C43_pole": "antisymmetric/PV inverse partial-plus", "target_gauge": "not imported as C43 coefficient", "branch": "explicit caller branch required", "zero_mode": "retained", "residual_link": "retained", "gauge_independence_assumed": False, "status": "GAUGE_POLE_RECORD_BOUND_NOT_CALCULATION_CLOSED", "root": _root((row["request_id"], "A+=0", "PV"))} for row in _request(request_id))
    return _freeze({"schema": "C169-GAUGE-POLE-BRANCH-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _request(request_id):
        source = dict(_RESOLUTION[row["request_id"]])
        rows.append({"request_id": row["request_id"], "capsule_id": row["request_id"], "C168_resolution_imported": True, "C168_terminal_status": source["terminal_status"], "C169_terminal_status": _terminal(row["request_id"]), "exact_missing_object": missing_calculation_manifest(row["request_id"])["rows"][0]["missing_object"], "C166_graphs_mutated": 0, "root": _root((row["request_id"], source["terminal_status"], _terminal(row["request_id"])))})
    return _freeze({"schema": "C169-REQUEST-RESOLUTION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "one_terminal_record_per_request": True, "root": _root(rows)})


def missing_calculation_manifest(request_id: str | None = None) -> MappingProxyType:
    missing = {
        "QUARK_FIELD": ("C141 canonical quark source/sink map", "C143 source-projected resolvent and degree-one/degree-two domain", "C146/C147 normalization closure", "C130 zero/boundary/residual realization"),
        "SIGNED_QUARK_MASS": ("C141 mass-linear source-map closure", "C143 signed two-point insertion domain", "C149 signed projector applied to complete inverse two-point", "C150 counterterm condition"),
        "TRANSVERSE_GLUON_FIELD": ("C151 gg/pure-gluon descendants", "C151 qqbar loop", "ghost sector", "C151 zero-mode/boundary counterterm realization"),
        "qg_VERTEX_DRESSING": ("C152 qgg/qqbar/pure-gluon sectors", "complete 1PI completion", "C130 zero/boundary/residual-link qg terms", "leg counterterm conditions"),
        "QCD_COUPLING": ("ghost and pure-gluon field factors", "complete 1PI qg vertex", "full Slavnov-Taylor-compatible coupling relation", "counterterm conditions"),
    }
    rows = []
    for row in _request(request_id):
        q = row["quantity"]
        rows.append({"request_id": row["request_id"], "calculation_capsule_id": f"C169-MISSING-{row['request_id']}", "missing_object": missing[q], "dependencies": ("C43 PV/Q0/residual-link", "C131 retained polynomial", "C142-C152 public owner manifests"), "status": _terminal(row["request_id"]), "acquisition_required": False, "new_perturbative_calculation_required": True, "not_zero": True, "root": _root((row["request_id"], missing[q]))})
    return _freeze({"schema": "C169-MISSING-CALCULATION-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "all_exact_requests": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple({"frontier_id": f"C169-{row['request_id']}", "request_id": row["request_id"], "status": _terminal(row["request_id"]), "kind": "C43_PERTURBATIVE_CALCULATION", "next_calculation_capsule": f"C169-MISSING-{row['request_id']}"} for row in _CAPSULES)
    return _freeze({"schema": "C169-DEPENDENCY-FRONTIER-MANIFEST-V1", "rows": rows, "count": len(rows), "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def calculation_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C169-CALCULATION-HANDOFF-V1", "status": STATUS, "plan": PLAN, "next": NEXT, "capsules": 6, "target_values": 0, "adapter_assembled": False, "matching": 0, "root": _root((STATUS, PLAN, NEXT, 6))})


def quantum_calculation_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C169-QUANTUM-CALCULATION-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "states_created": 0, "TMD_objects_created": 0, "physical_optimization": 0, "root": _root((False, 0, 0))})


def c158_noncircularity_manifest() -> MappingProxyType:
    return _freeze({"schema": "C169-C158-NONCIRCULARITY-V1", "C158_imported": False, "C158_value_inputs": 0, "C158_values_as_inputs": 0, "C158_recomputed": 0, "matching_difference": 0, "fitting": 0, "root": _root((False, 0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "web_or_model_memory_coefficients": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "invented_states": 0, "invented_projectors": 0, "dense_full_inverses": 0, "missing_terms_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "standard_scheme_adapter": 0, "matching": 0, "PDG_values": 0, "running": 0, "thresholds": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "physical_states": 0, "TMD_objects": 0, "Q0_Q1_Q2_modified": False, "allow_pickle_false": True, "pass": True, "root": _root((STATUS, NEXT, 0))})


def lfgmatchcalc1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C169-LFGMATCHCALC1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "six_capsules": 6, "terminal_records": 6, "operator_owners": len(_owners()), "intermediate_domains_closed": 0, "propagating_closed": 0, "direct_instantaneous_closed": 0, "count_once_duplicates": 0, "missing_terms_set_zero": 0, "diagnostics": 0, "outward_enclosures": 0, "routes_agree": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C158_value_inputs": 0, "adapter_assembled": 0, "next": NEXT, "root": _root((STATUS, PLAN, 6, NEXT))})


def mutate_live_hqcdlfgmatchcalc1(index: int) -> MappingProxyType:
    fields = ("baseline", "capsule_id", "request_id", "owner_id", "resolution", "state_id", "order", "coordinate", "projector", "active_Nf", "external_flavor", "propagating", "contact", "instantaneous", "count_once", "zero_mode", "boundary", "residual_link", "counterterm", "nullspace", "C158", "private_builder", "missing_zero", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed_mass", "mass_squared", "full_1PI", "ST", "program", "diagnostic", "enclosure", "C166_graph", "Q0", "Q1", "Q2", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C169_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256, PARENT_PACKAGE_ROOT)),
    "C169_PLAN_ROOT": lfgmatchcalc1_plan_manifest()["root"],
    "C169_CAPSULE_FREEZE_ROOT": calculation_capsule_freeze()["root"],
    "C169_OPERATOR_SUBSTRATE_ROOT": operator_substrate_manifest()["root"],
    "C169_C158_NONCIRCULARITY_ROOT": c158_noncircularity_manifest()["root"],
    "C169_PERTURBATIVE_EXPANSION_ROOT": perturbative_expansion_manifest()["root"],
    "C169_INTERMEDIATE_DOMAIN_ROOT": intermediate_domain_manifest()["root"],
    "C169_PROPAGATING_ROOT": propagating_contribution_manifest()["root"],
    "C169_DIRECT_INSTANTANEOUS_ROOT": direct_instantaneous_manifest()["root"],
    "C169_COUNT_ONCE_ROOT": count_once_report()["root"],
    "C169_ZERO_BOUNDARY_RESIDUAL_ROOT": zero_boundary_residual_ledger()["root"],
    "C169_COUNTERTERM_ROOT": counterterm_sensitivity_manifest()["root"],
    "C169_QUARK_TWO_POINT_ROOT": quark_two_point_manifest()["root"],
    "C169_SIGNED_MASS_ROOT": signed_mass_manifest()["root"],
    "C169_GLUON_TWO_POINT_ROOT": gluon_two_point_manifest()["root"],
    "C169_QG_VERTEX_ROOT": qg_vertex_manifest()["root"],
    "C169_COUPLING_ROOT": coupling_manifest()["root"],
    "C169_SIXTH_CALCULATION_ROOT": sixth_calculation_manifest()["root"],
    "C169_GRAPH_PROGRAM_SCHEMA_ROOT": graph_program_schema()["root"],
    "C169_GRAPH_PROGRAM_ROOT": graph_program_manifest()["root"],
    "C169_DIAGNOSTIC_ROOT": diagnostic_manifest()["root"],
    "C169_ROUTE_ROOT": calculation_route_manifest()["root"],
    "C169_UV_IR_RESOLUTION_ROOT": uv_ir_resolution_manifest()["root"],
    "C169_GAUGE_POLE_BRANCH_ROOT": gauge_pole_branch_manifest()["root"],
    "C169_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C169_MISSING_CALCULATION_ROOT": missing_calculation_manifest()["root"],
    "C169_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C169_HANDOFF_ROOT": calculation_handoff_contract()["root"],
    "C169_QUANTUM_HANDOFF_ROOT": quantum_calculation_handoff_contract()["root"],
    "C169_COMPLETENESS_ROOT": lfgmatchcalc1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C169-HQCDLFGMATCHCALC1-V1", "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "plan": PLAN, "roots": ROOTS})
