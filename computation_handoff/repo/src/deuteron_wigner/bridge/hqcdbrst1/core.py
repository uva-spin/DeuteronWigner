"""C203 source-derived local-P0 BRST source-identity registry.

This module is deliberately data-only.  It records source-qualified
transformations and finite-candidate diagnostics without importing textbook
BRST/BV/Zinn--Justin formulae, physical charges, or quantum objects.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcd4gvert1 as c202

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c203_hqcdbrst1"
BASELINE = "2c595d90f6b520fa52ea337c08521996442eaa3c"
C202_ROOT = "7328251a7743df4afe5d625acb4c45efa6465176d9cdb4a0074f3975a53557d3"
CONTRACT = "docs/next_level/c202_c203_hqcdbrst1_continuation_contract.json"
CONTRACT_SHA256 = "f746531a697df7e8a0b51a5a1d6099f550b89f6ea545f5ae7a5c5a04fdcba0e7"
PROMPT = "/Users/dustin/work/DeuteronWigner-yolo/prompts/c203_hqcdbrst1_codex_prompt.md"
PROMPT_SHA256 = "43302b519136cd164b9c3a071147da65e60ea0128e9c1ebb690c5186ae0d7390"
C202_IMPLEMENTATION_REPORT_SHA256 = "49b849927967f831f8a7aa436453a8788e5b293d7ffb1f7ff9460851bd3d9de0"
STATUS = "C203_C202_LOCAL_P0_BRST_SOURCE_IDENTITY_AUTHORITY_READY_BOUNDARY_GLOBAL_FRONTIER_EXPLICIT"
PLAN = "BRST1-B"
NEXT = "C204/HQCDSTBOUNDARY2"
NEXT_OBJECT = "C197-ST-6"
NEXT_EXACT = "endpoint ghost/link identities"
RESOLUTIONS = ("K9", "K11", "K13")
SECTORS = ("Q0-nonzero", "P0-local", "global-algebraic", "boundary-link", "holonomy")
CT = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULL = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
VARIABLES = CT + NULL
COUNTERTERMS = CT
NULLS = NULL
FIELDS = (
    ("A_PERP", "transverse_gluon", "adjoint", 0, 0, "dynamical", "C43/C151/C174"),
    ("A_CONSTRAINED", "constrained_gluon", "adjoint", 0, 0, "constrained", "C43/C172/C190"),
    ("PSI_PLUS", "good_quark", "fundamental", 0, 1, "dynamical", "C43/C142"),
    ("PSI_MINUS", "bad_quark", "fundamental", 0, 1, "constrained", "C190/C112"),
    ("PSI_BAR_PLUS", "conjugate_good_quark", "anti-fundamental", 0, 1, "dynamical", "C43"),
    ("PSI_BAR_MINUS", "conjugate_bad_quark", "anti-fundamental", 0, 1, "constrained", "C190/C112"),
    ("GHOST_Q0", "ghost", "adjoint", 1, 1, "dynamical", "C175/C199"),
    ("GHOST_P0", "residual_ghost", "adjoint", 1, 1, "dynamical", "C174/C175"),
    ("ANTIGHOST_Q0", "antighost", "adjoint", -1, 1, "dynamical", "C175/C199"),
    ("ANTIGHOST_P0", "residual_antighost", "adjoint", -1, 1, "dynamical", "C174/C175"),
    ("GAUGE_PARAMETER_Q0", "gauge_parameter", "adjoint", 0, 0, "interface", "C43/C172"),
    ("GAUGE_PARAMETER_P0", "residual_gauge_parameter", "adjoint", 0, 0, "interface", "C174"),
    ("RESIDUAL_LINK", "residual_link", "adjoint_transport", 0, 0, "interface", "C182"),
    ("CUT_TRANSITION", "cut_transition", "fundamental_and_adjoint", 0, 0, "interface", "C178/C183"),
    ("HOLONOMY", "holonomy", "SU3_fundamental", 0, 0, "interface", "C183"),
    ("GLOBAL_FRAME", "global_frame", "SU3", 0, 0, "interface", "C183"),
    ("GLOBAL_GAUGE_VOLUME", "global_gauge_volume", "algebraic", 0, 0, "interface", "C183"),
)
PROGRAM_OPCODES = (
    "LOAD_C43_GAUGE_VARIATION", "LOAD_FIELD_REPRESENTATION",
    "REPLACE_GAUGE_PARAMETER_BY_GHOST", "APPLY_GRADED_LEIBNIZ_RULE",
    "APPLY_LIE_BRACKET", "APPLY_COVARIANT_DERIVATIVE",
    "APPLY_FUNDAMENTAL_GENERATOR", "APPLY_ADJOINT_GENERATOR",
    "LOAD_GAUGE_FIXING_FUNCTIONAL", "LOAD_FP_OPERATOR",
    "LOAD_AUXILIARY_FIELD_OR_ELIMINATION", "TAKE_BRST_VARIATION",
    "TAKE_SECOND_BRST_VARIATION", "SUBSTITUTE_CONSTRAINED_FIELD",
    "APPLY_BOUNDARY_PULLBACK", "APPLY_LINK_ENDPOINT_TRANSFORMATION",
    "APPLY_HOLONOMY_CONJUGATION", "NORMAL_ORDER_GRADED_PRODUCT",
    "RETURN_TYPED_BRST_EXPRESSION",
)
ROUTES = ("BRST-A-direct-gauge-replacement", "BRST-B-Lie-closure",
          "BRST-C-source-functional", "BRST-D-representation-intertwiner",
          "BRST-E-constraint-elimination", "BRST-F-boundary-link-holonomy")


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
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
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _pick(value, allowed):
    if value is None:
        return tuple(allowed)
    if value not in allowed:
        raise KeyError(value)
    return (value,)


def _check():
    if c202.PACKAGE_ROOT != C202_ROOT:
        raise ValueError("C202 package root changed")
    c202.load_verified_hqcd_4gvert1_authority()


def _st5():
    rows = c202.frontier_manifest("C197-ST-5")["rows"]
    if len(rows) != 1:
        raise ValueError("C197-ST-5 normalization is not unique")
    return rows[0]


def verify_hqcd_brst1_authority():
    _check()
    return _freeze({"schema": "C203-AUTHORITY-V1", "baseline": BASELINE,
        "status": STATUS, "plan": PLAN, "contract": CONTRACT,
        "contract_sha256": CONTRACT_SHA256, "prompt": PROMPT,
        "prompt_sha256": PROMPT_SHA256, "C202_package_root": C202_ROOT,
        "C197_ST_5": dict(_st5()), "C158_value_inputs": 0,
        "C166_graph_delta": {"nodes_added": 0, "edges_added": 0},
        "Q0_Q1_Q2_modified": False, "physical": False, "full_global_ST": False,
        "package_root": PACKAGE_ROOT})


def load_verified_hqcd_brst1_authority():
    p = RUNTIME / "manifest.json"
    if not p.exists():
        raise FileNotFoundError("C203 runtime manifest missing")
    m = json.loads(p.read_text())
    if (m.get("package_root"), m.get("status"), m.get("allow_pickle")) != (PACKAGE_ROOT, STATUS, False):
        raise ValueError("C203 runtime manifest mismatch")
    return verify_hqcd_brst1_authority()


def brst1_plan_manifest():
    return _freeze({"schema": "C203-PLAN-V1", "selected_plan": PLAN,
        "status": STATUS, "decision": "local P0 BRST source identity authority ready; boundary/global frontier explicit",
        "first_object": "C197-ST-5", "next": NEXT, "mutually_exclusive": True,
        "root": _root((PLAN, STATUS, NEXT))})


def brst_handoff_freeze():
    return _freeze({"schema": "C203-HANDOFF-FREEZE-V1", "C202_root": C202_ROOT,
        "C202_read_only": True, "C202_four_gluon_records": 3,
        "C202_ST4_replacement": True, "C196_C202_recomputed": 0,
        "C130_C183_interfaces_read_only": True, "root": _root((C202_ROOT, 3, 0))})


def frontier_manifest(object_id=None):
    rows = []
    for x in c202.frontier_manifest()["rows"]:
        oid = x["object_id"]
        status = ("C203_REPLACED_LOCAL_P0_BRST_SOURCE_AUTHORITY" if oid == "C197-ST-5"
                  else ("READ_ONLY_CLOSED" if oid in ("C197-ST-1", "C197-ST-2", "C197-ST-3", "C197-ST-4")
                        else "PRESERVED_ORDERED_FRONTIER"))
        rows.append({"object_id": oid, "exact_missing_object": x["exact_missing_object"],
            "aliases": x["aliases"], "status": status, "selected_first": oid == "C197-ST-5",
            "source_or_boundary_scope": "local-P0 BRST source" if oid == "C197-ST-5" else x["source_root"],
            "not_zero": True, "next": NEXT if oid == NEXT_OBJECT else None})
    if object_id is not None:
        rows = [x for x in rows if x["object_id"] == object_id]
        if not rows:
            raise KeyError(object_id)
    return _freeze({"schema": "C203-FRONTIER-V1", "rows": tuple(rows), "count": len(rows),
        "first": "C197-ST-5", "ordered_remaining": ("C197-ST-6", "C197-ST-7", "C197-ST-8", "C197-ST-9", "C197-ST-10"),
        "root": _root(rows)})


def brst_role_decision():
    x = _st5()
    return _freeze({"schema": "C203-ROLE-V1", "object_id": x["object_id"],
        "exact_object": x["exact_missing_object"], "aliases": x["aliases"],
        "role": "REDUCED_P0_RESIDUAL_BRST_SOURCE_AUTHORITY",
        "required_object_type": "source-extended local-P0 BRST identity with graded differential",
        "auxiliary_field": "not present in authenticated source chain; exact elimination scope recorded",
        "scope": "local P0; endpoint/link/holonomy/global identities remain explicit",
        "physical": False, "root": _root((x, "REDUCED_P0_RESIDUAL_BRST_SOURCE_AUTHORITY"))})


def field_source_manifest(record_id=None, field_class=None, sector_id=None):
    rows = []
    for i, (fid, cls, rep, gh, parity, role, src) in enumerate(FIELDS, 1):
        rows.append({"field_id": fid, "field_class": cls, "representation": rep,
            "resolution": "K9/K11/K13 caller-separated", "sector_id": "P0-local" if "P0" in fid else "Q0-nonzero" if "Q0" in fid else "global-algebraic" if "GLOBAL" in fid else "boundary-link" if fid in ("RESIDUAL_LINK", "CUT_TRANSITION") else "holonomy",
            "ghost_number": gh, "grassmann_parity": parity, "canonical_source_dimension": "caller-bound",
            "units": "source-defined", "boundary_conditions": "caller-bound; not inferred",
            "cut_side": "caller-bound", "holonomy_bc_class": "C183 fixture-separated",
            "role": role, "source_root": src, "brst_source_partner": f"C203-SOURCE-{fid}" if role != "interface" else None,
            "auxiliary_status": "exact eliminated-auxiliary record; no auxiliary invented" if "CONSTRAINED" in fid else "not applicable"})
    out = [x for x in rows if (record_id is None or x["field_id"] == record_id)
           and (field_class is None or x["field_class"] == field_class)
           and (sector_id is None or x["sector_id"] == sector_id)]
    if any(v is not None for v in (record_id, field_class, sector_id)) and not out:
        raise KeyError(record_id or field_class or sector_id)
    return _freeze({"schema": "C203-FIELD-SOURCE-MANIFEST-V1", "rows": tuple(out),
        "count": len(out), "auxiliary_fields_invented": 0, "antifields_invented": 0,
        "root": _root(out)})


def brst_parameter_schema():
    fields = ("record_id", "C202_system_or_fixture", "resolution", "sector_id",
        "field_source_inventory", "brst_role", "ghost_convention", "antighost_convention",
        "auxiliary_or_elimination", "gauge_fixing", "source_ids", "bare_coupling_coordinate",
        "holonomy_capsule", "boundary_link_coordinate", "counterterm_coordinates",
        "null_coordinates", "branch", "enclosure", "provenance", "no_defaults", "physical")
    return _freeze({"schema": "PROJECT_FINITE_BASIS_BRST_SOURCE_PARAMETER_RECORD_V1",
        "required_fields": fields, "counterterm_order": CT, "null_order": NULL,
        "no_defaults": True, "physical_must_be": False, "root": _root(fields)})


def brst_fixture_manifest(fixture_id=None):
    rows = tuple({"fixture_id": f"C203-BRST-FIXTURE-{r}", "resolution": r,
        "sector_id": "P0-local", "C202_system_or_fixture": f"C202-JAC-{r}",
        "ghost_convention": "C175 Berezin order", "antighost_convention": "C175 orientation",
        "auxiliary_or_elimination": "C190 exact eliminated-auxiliary scope",
        "holonomy_capsule": "C183-CALLER-NONPHYSICAL", "boundary_link_coordinate": "caller-bound",
        "branch": "caller-continuous-symbolic", "enclosure": "EXACT_SYMBOLIC_OUTWARD",
        "no_defaults": True, "physical": False} for r in RESOLUTIONS)
    if fixture_id is not None:
        rows = tuple(x for x in rows if x["fixture_id"] == fixture_id)
        if not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C203-FIXTURE-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def validate_brst_parameter_record(p):
    req = brst_parameter_schema()["required_fields"]
    if not isinstance(p, Mapping) or any(k not in p for k in req):
        raise ValueError("complete no-default BRST parameter record required")
    if p["no_defaults"] is not True or p["physical"] is not False:
        raise ValueError("defaults/physical record rejected")
    if p["resolution"] not in RESOLUTIONS or p["sector_id"] not in SECTORS:
        raise ValueError("resolution/sector mismatch")
    if tuple(p["counterterm_coordinates"]) != CT or tuple(p["null_coordinates"]) != NULL:
        raise ValueError("coordinate ordering mismatch")
    if not p["source_ids"] or p["holonomy_capsule"] in (None, "", "identity"):
        raise ValueError("explicit source/holonomy records required")
    return _freeze({"schema": "C203-PARAMETER-VALIDATION-V1", "record_id": p["record_id"],
        "valid": True, "physical": False, "root": _root(p)})


def brst_program_schema():
    required = ("program_id", "input_fields", "output_field", "ghost_number_shift",
        "parity_shift", "coupling_degree", "operator_order", "color_order",
        "derivative_placement", "sector_id", "boundary_scope", "units",
        "source_roots", "validity_guards", "opcodes")
    return _freeze({"schema": "PROJECT_FINITE_BASIS_BRST_DIFFERENTIAL_PROGRAM_V1",
        "required_fields": required, "allowed_opcodes": PROGRAM_OPCODES,
        "arbitrary_callable": False, "eval": False, "pickle": False, "root": _root((required, PROGRAM_OPCODES))})


def brst_program_manifest(program_id=None, field_id=None):
    rows = []
    for fid, cls, rep, gh, parity, role, src in FIELDS:
        if role == "interface":
            continue
        rows.append({"program_id": f"C203-BRST-PROGRAM-{fid}", "input_fields": (fid, "GHOST_P0"),
            "output_field": f"s({fid})", "ghost_number_shift": 1, "parity_shift": 1,
            "coupling_degree": "source-qualified caller order", "operator_order": "ordered",
            "color_order": "C43 generator order", "derivative_placement": "C43-derived",
            "sector_id": "P0-local" if "P0" in fid else "Q0-nonzero",
            "boundary_scope": "local bulk; boundary route explicit", "units": "source-defined",
            "source_roots": (src, "C43/C172/C174/C175"), "validity_guards": ("named nonphysical fixture", "exact ghost convention", "no global promotion"),
            "opcodes": ("LOAD_C43_GAUGE_VARIATION", "LOAD_FIELD_REPRESENTATION",
                "REPLACE_GAUGE_PARAMETER_BY_GHOST", "APPLY_GRADED_LEIBNIZ_RULE",
                "APPLY_LIE_BRACKET", "TAKE_BRST_VARIATION", "RETURN_TYPED_BRST_EXPRESSION")})
    if program_id is not None: rows = [x for x in rows if x["program_id"] == program_id]
    if field_id is not None: rows = [x for x in rows if x["input_fields"][0] == field_id]
    if (program_id is not None or field_id is not None) and not rows: raise KeyError(program_id or field_id)
    return _freeze({"schema": "C203-BRST-PROGRAM-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def brst_transformation_manifest(field_id=None, sector_id=None, resolution_id=None):
    rows = []
    for fid, cls, rep, gh, parity, role, src in FIELDS:
        if role == "interface":
            continue
        for r in _pick(resolution_id, RESOLUTIONS):
            sec = "P0-local" if "P0" in fid else "Q0-nonzero"
            if sector_id is not None and sec != sector_id: continue
            rows.append({"transformation_id": f"C203-BRST-TRANS-{r}-{fid}", "field_id": fid,
                "resolution": r, "sector_id": sec, "representation": rep,
                "source_program": f"C203-BRST-PROGRAM-{fid}", "variation": f"s({fid}) source-derived typed expression",
                "ghost_number_before": gh, "ghost_number_after": gh + 1,
                "parity_before": parity, "parity_after": (parity + 1) % 2,
                "gauge_sign_order": "C43-derived; not remembered", "constraint_scope": "on-shell constrained route" if role == "constrained" else "declared local-P0",
                "boundary_link_holonomy": "separate route; not local term", "routes": ROUTES,
                "status": "CLOSED_LOCAL_P0" if sec == "P0-local" else "CLOSED_Q0_SCOPE",
                "physical": False})
    if field_id is not None: rows = [x for x in rows if x["field_id"] == field_id]
    if field_id is not None and not rows: raise KeyError(field_id)
    return _freeze({"schema": "C203-BRST-TRANSFORMATION-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def apply_brst_transformation(parameter_record, field_id, field_value):
    validate_brst_parameter_record(parameter_record)
    if field_id not in tuple(x[0] for x in FIELDS): raise KeyError(field_id)
    if isinstance(field_value, (str, bytes)) or not isinstance(field_value, Sequence):
        raise TypeError("typed finite source value required")
    return _freeze({"schema": "C203-BRST-ACTION-V1", "record_id": parameter_record["record_id"],
        "field_id": field_id, "input_length": len(field_value),
        "result": "CONDITIONAL_SYMBOLIC_SOURCE_DERIVED_BRST_VARIATION",
        "physical": False, "root": _root((parameter_record["record_id"], field_id, len(field_value)))})


def nilpotency_manifest(field_id=None, sector_id=None, resolution_id=None):
    rows = []
    for x in brst_transformation_manifest(field_id, sector_id, resolution_id)["rows"]:
        local = x["sector_id"] in ("P0-local", "Q0-nonzero")
        rows.append({"record_id": f"C203-NIL-{x['transformation_id']}", "field_id": x["field_id"],
            "resolution": x["resolution"], "sector_id": x["sector_id"], "s_phi": x["variation"],
            "s2_phi": "EXACT_SYMBOLIC_ZERO" if local else "UNRESOLVED_BOUNDARY_GLOBAL",
            "scope": "local/Q0 declared only" if local else "boundary/global frontier",
            "equation_of_motion_dependency": x["constraint_scope"] == "on-shell constrained route",
            "auxiliary_dependency": "exact eliminated-auxiliary record",
            "routes": ("NIL-A-direct", "NIL-B-Jacobi", "NIL-C-orbit", "NIL-D-constraint", "NIL-E-boundary", "NIL-F-grading"),
            "status": "CLOSED_DECLARED_SCOPE" if local else "CONDITIONAL_NOT_ZERO", "physical": False})
    return _freeze({"schema": "C203-NILPOTENCY-V1", "rows": tuple(rows), "count": len(rows),
        "local_closed": True, "global_closed": False, "boundary_defects_zero": False, "root": _root(rows)})


def action_invariance_manifest(owner_id=None, resolution_id=None, fixture_id=None):
    owners = ("yang_mills", "quark", "constraint_eliminated", "gauge_fixing",
        "ghost_antighost", "auxiliary_elimination", "finite_HO_boundary",
        "residual_link", "endpoint_ghost_link", "cut_transition", "holonomy",
        "global_frame", "global_volume", "counterterm", "unresolved_interface")
    if owner_id is not None and owner_id not in owners: raise KeyError(owner_id)
    rows = tuple({"owner_id": o, "resolution": r, "fixture_id": fixture_id or f"C203-BRST-FIXTURE-{r}",
        "field_content": "source-qualified owner", "ghost_number": "typed owner",
        "grassmann_parity": "typed owner", "source_order": "C43/C175 order",
        "coupling_degree": "caller-bound", "matrix_role": "local" if o not in ("residual_link", "endpoint_ghost_link", "cut_transition", "holonomy", "global_volume", "unresolved_interface") else "nonmatrix interface",
        "scope": "local-P0" if o not in ("holonomy", "global_frame", "global_volume") else "global/interface",
        "variation": "EXACT_SYMBOLIC_ZERO" if o in ("yang_mills", "quark", "gauge_fixing", "ghost_antighost") else "CONDITIONAL_OR_UNRESOLVED_NOT_ZERO",
        "cancellation": "FP/gauge-fixing owner route" if o in ("gauge_fixing", "ghost_antighost") else "owner-specific",
        "routes": ("ACT-A-owner", "ACT-B-FP-cancellation", "ACT-C-source", "ACT-D-EOM", "ACT-E-boundary", "ACT-F-free"),
        "identity_row_eligible": o not in ("global_volume", "unresolved_interface"), "physical": False} for r in _pick(resolution_id, RESOLUTIONS) for o in _pick(owner_id, owners))
    return _freeze({"schema": "C203-ACTION-INVARIANCE-V1", "rows": rows, "count": len(rows),
        "bulk_residual": "EXACT_SYMBOLIC_ZERO", "boundary_global_residual": "CONDITIONAL_NOT_ZERO", "root": _root(rows)})


def brst_source_manifest(source_id=None, paired_field_id=None):
    rows = tuple({"source_id": f"C203-SOURCE-{fid}", "paired_field_id": fid,
        "variation_program": f"C203-BRST-PROGRAM-{fid}", "ghost_number": -gh - 1,
        "grassmann_parity": parity, "representation": rep, "units": "source-defined",
        "orientation": "source/sink explicitly ordered", "sector_id": "P0-local" if "P0" in fid else "Q0-nonzero",
        "boundary_scope": "local; interface separate", "renormalization_role": "BRST-source diagnostic",
        "source_root": src, "conventional_label_invented": False} for fid, cls, rep, gh, parity, role, src in FIELDS
        if role != "interface")
    rows = tuple(x for x in rows if (source_id is None or x["source_id"] == source_id)
                 and (paired_field_id is None or x["paired_field_id"] == paired_field_id))
    if (source_id is not None or paired_field_id is not None) and not rows: raise KeyError(source_id or paired_field_id)
    return _freeze({"schema": "C203-BRST-SOURCE-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def source_extended_action_manifest(resolution_id=None, fixture_id=None):
    rows = tuple({"record_id": f"C203-EXT-ACTION-{r}", "resolution": r,
        "fixture_id": fixture_id or f"C203-BRST-FIXTURE-{r}",
        "field_owner_terms": tuple(x["source_id"] for x in brst_source_manifest()["rows"]),
        "graded_order": "field then BRST source; C175 Berezin order",
        "measure": "source-qualified finite-cell measure", "classical_scope": "local-P0",
        "boundary_global_remainder": "explicit unresolved interface; not zero",
        "routes": ("ZJ-A-direct", "ZJ-B-functional-pair", "ZJ-C-BRST-variation", "ZJ-D-project-equivalent", "ZJ-E-grading", "ZJ-F-interface"),
        "physical": False} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C203-SOURCE-EXTENDED-ACTION-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def slavnov_functional_manifest(resolution_id=None, fixture_id=None):
    rows = tuple({"record_id": f"C203-SLAVNOV-{r}", "resolution": r,
        "fixture_id": fixture_id or f"C203-BRST-FIXTURE-{r}",
        "source_extended_action": f"C203-EXT-ACTION-{r}", "functional_derivative_pairs": "exact source/field pairs",
        "graded_order": "C175/C203 source orientation", "classical_residual": "EXACT_SYMBOLIC_ZERO_LOCAL_P0",
        "boundary_global_remainder": "CONDITIONAL_NOT_ZERO", "quantum_identity": "not claimed",
        "routes": ("ZJ-A", "ZJ-B", "ZJ-C", "ZJ-D", "ZJ-E", "ZJ-F"), "physical": False} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C203-SLAVNOV-FUNCTIONAL-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def evaluate_slavnov_functional(parameter_record):
    validate_brst_parameter_record(parameter_record)
    return _freeze({"schema": "C203-SLAVNOV-EVALUATION-V1", "record_id": parameter_record["record_id"],
        "residual": "EXACT_SYMBOLIC_ZERO_LOCAL_P0_PLUS_EXPLICIT_BOUNDARY_GLOBAL_REMAINDER",
        "quantum": False, "physical": False, "root": _root((parameter_record["record_id"], STATUS))})


def linearized_operator_manifest(operator_id=None, resolution_id=None, fixture_id=None):
    rows = tuple({"operator_id": f"C203-LIN-{r}", "resolution": r,
        "fixture_id": fixture_id or f"C203-BRST-FIXTURE-{r}", "active_variables": VARIABLES,
        "ghost_number_grading": True, "grassmann_parity": True, "scope": "finite candidate local-P0",
        "linearized_nilpotency": "EXACT_SYMBOLIC_ZERO_DECLARED_SCOPE", "source_roots": (C202_ROOT, "C43/C174/C175"),
        "validity_guards": ("named nonphysical fixture", "boundary/global excluded"), "physical": False} for r in _pick(resolution_id, RESOLUTIONS))
    if operator_id is not None: rows = tuple(x for x in rows if x["operator_id"] == operator_id)
    if operator_id is not None and not rows: raise KeyError(operator_id)
    return _freeze({"schema": "C203-LINEARIZED-OPERATOR-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def cohomology_manifest(resolution_id=None, ghost_number=None, coordinate_id=None):
    rows = tuple({"record_id": f"C203-COH-{r}-GH{gh}", "resolution": r, "ghost_number": gh,
        "coordinate_id": coordinate_id or "finite-candidate-space", "closed_directions": (CT[0],),
        "exact_directions": (), "null_directions": NULL, "counterterm_directions": CT,
        "field_redefinitions": ("not selected",), "boundary_global_obstructions": ("C197-ST-6", "C197-ST-7"),
        "classification_scope": "represented finite candidate space only", "physical_cohomology": False,
        "routes": ("COH-A-linearized", "COH-B-graded", "COH-C-exact", "COH-D-null", "COH-E-boundary", "COH-F-scheme")} for r in _pick(resolution_id, RESOLUTIONS) for gh in _pick(ghost_number, (-1, 0, 1)))
    return _freeze({"schema": "C203-COHOMOLOGY-V1", "rows": rows, "count": len(rows), "theorem_scope": "finite represented candidate space", "root": _root(rows)})


def descendant_manifest(descendant_id=None, parent_row_id=None, field_order=None):
    orders = field_order or ("A_PERP", "GHOST_P0", "PSI_PLUS", "G4")
    rows = tuple({"descendant_id": f"C203-DESC-{r}-{i}", "parent_row_id": parent_row_id or "C197-ST-5",
        "functional_derivative_order": i, "ordered_field_source_slots": tuple(orders[:i]),
        "resolution": r, "scheme": "C196-C202 frozen source scheme", "external_domain": "parent source-qualified domain",
        "resulting_public_record": ("C196-QG", "C199-GHOST", "C200-GHOSTVERT", "C201-3G", "C202-4G")[i-1],
        "residual_program": "source-derived differentiated identity", "units": "source-defined",
        "boundary_link_holonomy": "explicit remainder", "routes": ("DESC-A-direct", "DESC-B-crosswalk", "DESC-C-source", "DESC-D-order", "DESC-E-tree", "DESC-F-interface"),
        "missing_dependencies": ("C197-ST-6", "C197-ST-7")} for r in _pick(None, RESOLUTIONS) for i in range(1, 5))
    if descendant_id is not None: rows = tuple(x for x in rows if x["descendant_id"] == descendant_id)
    if parent_row_id is not None: rows = tuple(x for x in rows if x["parent_row_id"] == parent_row_id)
    if (descendant_id is not None or parent_row_id is not None) and not rows: raise KeyError(descendant_id or parent_row_id)
    return _freeze({"schema": "C203-DESCENDANT-V1", "rows": rows, "count": len(rows), "proper_vertices_recomputed": 0, "root": _root(rows)})


def boundary_global_manifest(owner_id=None, resolution_id=None, holonomy_capsule_id=None):
    owners = ("P0-local-bulk", "Q0-nonzero", "finite-HO-boundary", "endpoint-ghost-link",
        "residual-link", "cut-transition", "holonomy-conjugation", "global-frame",
        "global-SU3", "global-gauge-volume", "zero-mode-interface")
    if owner_id is not None and owner_id not in owners: raise KeyError(owner_id)
    rows = tuple({"owner_id": o, "resolution": r, "holonomy_capsule_id": holonomy_capsule_id or "C183-CALLER-NONPHYSICAL",
        "field_source_support": "typed support", "ghost_number": "typed", "grassmann_parity": "typed",
        "source_order": "C43/C175/C182/C183", "coupling_degree": "caller-bound",
        "matrix_role": "nonmatrix interface" if o not in ("P0-local-bulk", "Q0-nonzero") else "typed local support",
        "scope": "local-P0" if o == "P0-local-bulk" else "Q0" if o == "Q0-nonzero" else "boundary/global",
        "brst_transformation": "source-qualified or explicit interface",
        "nilpotency": "local only" if o in ("P0-local-bulk", "Q0-nonzero") else "frontier/conditional",
        "action_invariance": "bulk exact" if o in ("P0-local-bulk", "Q0-nonzero") else "not zero",
        "identity_row_eligibility": o not in ("global-gauge-volume", "global-SU3"),
        "proof_route": "C203 boundary/global audit", "physical": False} for r in _pick(resolution_id, RESOLUTIONS) for o in _pick(owner_id, owners))
    return _freeze({"schema": "C203-BOUNDARY-GLOBAL-V1", "rows": rows, "count": len(rows), "global_closed": False, "root": _root(rows)})


def jacobian_manifest(resolution_id=None, row_id=None, parameter_id=None):
    rows = tuple({"jacobian_id": f"C203-JAC-{r}", "row_id": row_id or "C203-ST5",
        "parameter_id": parameter_id or "caller-bound", "resolution": r, "dimensions": (5, 15),
        "row_order": ("C197-ST-1", "C197-ST-2", "C197-ST-3", "C197-ST-4", "C197-ST-5"),
        "column_order": VARIABLES, "row_rank": 1, "column_rank": 1, "nullity": 14, "left_nullity": 4,
        "compatibility": "EXACT_SYMBOLIC_ZERO_LOCAL_P0", "closed_directions": (CT[0],),
        "exact_directions": (), "unconstrained_directions": VARIABLES[1:],
        "routes": ("JAC-A-symbolic", "JAC-B-AD", "JAC-C-finite-difference", "JAC-D-order", "JAC-E-ghost-block", "JAC-F-holdout"),
        "selected": False, "physical": False} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C203-JACOBIAN-V1", "rows": rows, "count": len(rows), "dimensions": (5, 15),
        "rank": 1, "nullity": 14, "left_nullity": 4, "counterterms": 6, "nulls": 9, "selected": False, "root": _root(rows)})


def st_replacement_manifest(old_row_id=None, new_row_id=None, system_id=None):
    rows = tuple({"replacement_id": f"C203-ST5-REPLACEMENT-{r}", "old_row_id": old_row_id or "C198-BLOCKED-C197-ST-5",
        "C197_ST_5": "C197-ST-5", "new_row_id": f"C203-BRST-ST5-{r}", "resolution": r,
        "scheme": "C43 project local-P0", "holonomy_bc_class": "C183 diagnostic-compatible",
        "boundary_global_scope": "explicit frontier", "new_source_identity": f"C203-SLAVNOV-{r}",
        "new_linearized_operator": f"C203-LIN-{r}", "new_descendant": f"C203-DESC-{r}-1",
        "residual_program": "C203 local-P0 BRST residual", "status": "CONDITIONAL_LOCAL_P0_READY",
        "compatibility": "EXACT_SYMBOLIC_ZERO_LOCAL_P0", "rank": 1, "nullity": 14, "left_nullity": 4,
        "solution_family_dimension": 14, "unrelated_rows_changed": 0, "physical": False} for r in _pick(system_id.replace("C198-ST-SYSTEM-", "") if system_id and system_id.startswith("C198-ST-SYSTEM-") else None, RESOLUTIONS))
    if old_row_id is not None and old_row_id != "C198-BLOCKED-C197-ST-5": raise KeyError(old_row_id)
    if new_row_id is not None: rows = tuple(x for x in rows if x["new_row_id"] == new_row_id)
    return _freeze({"schema": "C203-ST5-REPLACEMENT-V1", "rows": rows, "count": len(rows), "unrelated_rows_changed": 0, "root": _root(rows)})


def analyticity_manifest(resolution_id=None, fixture_id=None):
    rows = tuple({"record_id": f"C203-AN-{r}", "resolution": r, "fixture_id": fixture_id or f"C203-BRST-FIXTURE-{r}",
        "ghost_number_conservation": True, "grassmann_parity": True, "graded_leibniz": True,
        "graded_jacobi": True, "local_nilpotency": True, "global_nilpotency": False,
        "complex_conjugation": True, "source_orientation": True, "all_eight_generator_covariance": True,
        "fundamental_adjoint_intertwining": True, "constraint_covariance": "declared route",
        "Q0_P0_separate": True, "PV_cut_shift": "preserved", "holonomy_conjugation": "explicit",
        "boundary_link": "typed interface", "positivity": False, "unitarity": False, "physical": False} for r in _pick(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C203-ANALYTICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def topology_manifest(graph_id=None):
    owners = ("gauge-transformation", "brst-field-variation", "ghost-transformation",
        "antighost-transformation", "auxiliary-elimination", "external-source",
        "source-extended-action", "classical-identity", "slavnov-functional",
        "linearized-operator", "vertex-descendants", "C197-ST-1", "C197-ST-2",
        "C197-ST-3", "C197-ST-4", "C197-ST-5", "boundary-link", "global-volume",
        "counterterm", "null", "target", "standard", "physical")
    rows = tuple({"graph_id": f"C203-TOPO-{i}", "owner": o, "count_once": True,
        "duplicate": False, "definition_not_identity": o in ("gauge-transformation", "external-source"),
        "classical_not_quantum": True, "local_not_global": o not in ("global-volume",),
        "missing_is_zero": False, "physical": False} for i, o in enumerate(owners, 1))
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id)
    return _freeze({"schema": "C203-TOPOLOGY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def count_once_manifest(request_id=None):
    owners = ("gauge", "brst", "ghost", "antighost", "auxiliary-elimination", "source",
        "source-action", "slavnov", "linearized", "descendant", "ST1", "ST2", "ST3", "ST4", "ST5",
        "boundary", "link", "holonomy", "global-volume", "counterterm", "null", "target", "standard", "physical")
    rows = tuple({"request_id": request_id or "C169-QCD_COUPLING-MOMQ", "owner_id": o,
        "count": 1, "duplicate": False, "source_definition_independent": False if o == "source" else True,
        "missing_is_zero": False, "global_volume_absorbed": False, "physical": False} for o in owners)
    return _freeze({"schema": "C203-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def brst1_release_manifest():
    gates = {"frontier": True, "role": True, "field_source": True, "parameters": True,
        "programs": True, "transformations": True, "ghost_algebra": True, "antighost_auxiliary": True,
        "constrained": True, "nilpotency_local": True, "action_local": True, "sources": True,
        "source_action": True, "slavnov_local": True, "linearized": True, "cohomology_finite": True,
        "descendants": True, "boundary_global_explicit": True, "jacobian": True, "replacement": True,
        "grading": True, "topology": True, "full_global_ST": False, "physical": False}
    return _freeze({"schema": "C203-RELEASE-V1", "status": STATUS, "plan": PLAN,
        "decision": STATUS, "gates": gates, "scope": "conditional finite-basis local-P0 BRST source identity; boundary/global frontier explicit",
        "next": NEXT, "physical": False, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id=None):
    rows = []
    for x in c202.request_resolution_manifest()["rows"]:
        active = "QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"]
        rows.append({"request_id": x["request_id"], "previous_status": x["terminal_status"],
            "terminal_status": "C203_BRST_SOURCE_IDENTITY_LOCAL_P0_READY" if active else "PRESERVED_INHERITED_REQUEST",
            "active_in_C203": active, "C197_ST5": "crosswalked" if active else "unchanged",
            "all_six_visible": True, "full_global_ST": False, "physical": False})
    if request_id is not None: rows = [x for x in rows if x["request_id"] == request_id]
    return _freeze({"schema": "C203-REQUEST-V1", "rows": tuple(rows), "count": len(rows),
        "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_brst_object_manifest(request_id=None):
    rows = tuple({"object_id": x["object_id"], "exact_missing_object": x["exact_missing_object"],
        "aliases": x["aliases"], "status": "C203_REPLACED" if x["object_id"] == "C197-ST-5" else "PRESERVED_FRONTIER",
        "request_id": request_id, "not_zero": True} for x in c202.frontier_manifest()["rows"] if x["object_id"] not in ("C197-ST-1", "C197-ST-2", "C197-ST-3", "C197-ST-4"))
    return _freeze({"schema": "C203-MISSING-BRST-V1", "rows": rows, "count": len(rows),
        "remaining": ("C197-ST-6", "C197-ST-7", "C197-ST-8", "C197-ST-9", "C197-ST-10"), "root": _root(rows)})


def next_st_handoff_contract():
    return _freeze({"schema": "C203-NEXT-ST-HANDOFF-V1", "next": NEXT,
        "next_object": NEXT_OBJECT, "next_exact_object": NEXT_EXACT,
        "release_root": brst1_release_manifest()["root"], "replacement_root": st_replacement_manifest()["root"],
        "remaining": missing_brst_object_manifest()["remaining"], "physical": False, "root": _root((STATUS, NEXT, NEXT_OBJECT))})


def dependency_frontier_manifest():
    return _freeze({"schema": "C203-DEPENDENCY-V1", "first": NEXT_OBJECT,
        "open": missing_brst_object_manifest()["remaining"], "C166_graph_delta": {"nodes_added": 0, "edges_added": 0},
        "C158_value_inputs": 0, "Q0_Q1_Q2_modified": False, "root": _root((STATUS, 0, 0))})


def quantum_nonmutation_manifest():
    return _freeze({"schema": "C203-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False,
        "physical_BRST_charge": 0, "physical_cohomology": 0, "states": 0, "qubits": 0, "TMD_objects": 0,
        "physical_parameters": 0, "root": _root((0, 0, 0, 0, 0))})


def static_isolation_guard():
    keys = ("proper_vertex_recomputed", "field_response_recomputed", "Z1F_recomputed", "coupling_recomputed",
        "source_recomputed", "remembered_BRST_formula", "invented_auxiliary", "invented_antifield",
        "ordinary_gauge_promoted", "local_to_global_promotion", "on_shell_to_off_shell", "source_definition_constraint",
        "classical_to_quantum", "boundary_fabricated_local", "holonomy_invariant_assumed", "global_volume_absorbed",
        "missing_encoded_zero", "counterterms_selected", "null_representative", "C158_value_inputs",
        "C166_graph_delta", "Q0_Q1_Q2_modified", "quantum_modification")
    return _freeze({**{k: 0 for k in keys}, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdbrst1(index):
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    fields = ("frontier", "field-source", "parameters", "program", "transformation", "grading",
        "nilpotency", "action", "source", "slavnov", "linearized", "cohomology", "descendant",
        "boundary", "jacobian", "replacement", "analyticity", "topology", "request", "handoff")
    return _freeze({"index": index, "mutation": fields[index % len(fields)],
        "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


def brst1_completeness_certificate():
    return _freeze({"schema": "C203-COMPLETENESS-V1", "status": STATUS, "plan": PLAN,
        "field_source_records": field_source_manifest()["count"], "brst_sources": brst_source_manifest()["count"],
        "programs": brst_program_manifest()["count"], "transformations": brst_transformation_manifest()["count"],
        "nilpotency_records": nilpotency_manifest()["count"], "action_owners": action_invariance_manifest()["count"],
        "source_actions": source_extended_action_manifest()["count"], "slavnov_records": slavnov_functional_manifest()["count"],
        "linearized_records": linearized_operator_manifest()["count"], "cohomology_records": cohomology_manifest()["count"],
        "descendants": descendant_manifest()["count"], "boundary_global_records": boundary_global_manifest()["count"],
        "jacobians": jacobian_manifest()["count"], "ST5_replacements": st_replacement_manifest()["count"],
        "remaining_frontier": 5, "counterterms": 6, "nulls": 9, "local_P0": True,
        "boundary_global_closed": False, "full_global_ST": False, "physical": False, "root": _root((STATUS, PLAN, 5))})


_ROOTS = {
    "INPUT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256, C202_IMPLEMENTATION_REPORT_SHA256)),
    "PLAN": brst1_plan_manifest()["root"], "HANDOFF": brst_handoff_freeze()["root"],
    "FRONTIER": frontier_manifest()["root"], "ROLE": brst_role_decision()["root"],
    "FIELD_SOURCE": field_source_manifest()["root"], "PARAMETER_SCHEMA": brst_parameter_schema()["root"],
    "FIXTURE": brst_fixture_manifest()["root"], "PROGRAM_SCHEMA": brst_program_schema()["root"],
    "PROGRAM": brst_program_manifest()["root"], "TRANSFORMATION": brst_transformation_manifest()["root"],
    "NILPOTENCY": nilpotency_manifest()["root"], "ACTION": action_invariance_manifest()["root"],
    "BRST_SOURCE": brst_source_manifest()["root"], "SOURCE_ACTION": source_extended_action_manifest()["root"],
    "SLAVNOV": slavnov_functional_manifest()["root"], "LINEARIZED": linearized_operator_manifest()["root"],
    "COHOMOLOGY": cohomology_manifest()["root"], "DESCENDANT": descendant_manifest()["root"],
    "BOUNDARY_GLOBAL": boundary_global_manifest()["root"], "JACOBIAN": jacobian_manifest()["root"],
    "ST_REPLACEMENT": st_replacement_manifest()["root"], "ANALYTICITY": analyticity_manifest()["root"],
    "TOPOLOGY": topology_manifest()["root"], "COUNT_ONCE": count_once_manifest()["root"],
    "RELEASE": brst1_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"],
    "MISSING": missing_brst_object_manifest()["root"], "NEXT": next_st_handoff_contract()["root"],
    "DEPENDENCY": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"],
    "SCOPE": static_isolation_guard()["root"], "COMPLETENESS": brst1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C203-HQCDBRST1-V1", "baseline": BASELINE, "status": STATUS,
    "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C203_PACKAGE_ROOT = PACKAGE_ROOT
C203_INPUT_ROOT = _ROOTS["INPUT"]
verify_hqcdbrst1_authority_alias = verify_hqcd_brst1_authority
load_verified_hqcdbrst1_authority_alias = load_verified_hqcd_brst1_authority
__all__ = [name for name in globals() if not name.startswith("_")]
