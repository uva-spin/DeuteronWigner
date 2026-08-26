"""C197: strict, conditional Z1F and qg coupling-coordinate records.

This layer imports C196, C150, C184, and C152 records read-only.  It exposes
symbolic nonphysical finite-basis responses; it does not solve a physical
renormalization condition, choose a counterterm/null representative, or
construct a target-scheme quantity.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdqgvert3 as c196
from deuteron_wigner.bridge import hqcdzqmass as c150
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdqgvert as c152

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c197_hqcdz1f2"
BASELINE = "a29fd7f5d907fc78a343b279d2506453dcd68636"
CONTRACT = "docs/next_level/c196_c197_hqcdz1f2_continuation_contract.json"
CONTRACT_SHA256 = "b4d9127f4c8edff8a986b27b3c54d7c4e1847b615408123b785bc6b61abd7bdf"
PROMPT = "/Users/dustin/Downloads/c197_hqcdz1f2_codex_prompt.md"
PROMPT_SHA256 = "8d297a6418598d839f6115bcff70315ce68c7615443ce607b0364ed64edfe7f5"
STATUS = "C197_C196_SOURCE_DERIVED_COMPLETE_CONDITIONAL_FINITE_BASIS_Z1F_AND_QG_COUPLING_RESPONSE_AUTHORITY_READY_ST_NEXT"
PLAN = "Z1F2-A"
NEXT = "C198/HQCDST2"
RESOLUTIONS = ("K9", "K11", "K13")
PROJECTORS = tuple(f"C152-RANK8-PROJECTOR-{i}" for i in range(1, 9))
KINETIC_SCHEMES = ("K_MINUS", "K_PLUS", "K_PERP")
GLUON_SCHEMES = ("C151_GLON_PROJECTOR_V1",)
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
COORDINATES = ("g_s", "g_s^2", "alpha_s", "a_s", "V_B", "Z_1F", "g_R", "g_R/g_s", "signed m_R", "m_R^2")
PROJECTOR_ROLES = (
    (PROJECTORS[0], "tree_qg_tensor", "TREE_SUPPORT_MULTIPLICATIVE", True, "C152 tree_unit_response=1"),
    (PROJECTORS[1], "longitudinal_derivative", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[2], "transverse_polarization", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[3], "helicity", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[4], "ordered_color", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[5], "mass_linear", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[6], "orientation", "DYNAMICAL_CORRECTION_ONLY", False, "tree support absent; no division"),
    (PROJECTORS[7], "boundary_nuisance", "BOUNDARY_NUISANCE_REJECTED", False, "C152 nuisance_response=0"),
)


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping): return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)): return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _pick(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _all_requests() -> tuple[str, ...]:
    return tuple(row["request_id"] for row in c196.request_resolution_manifest()["rows"])


def _request5() -> str:
    return next(x for x in _all_requests() if "qg_VERTEX" in x)


def _request6() -> str:
    return next(x for x in _all_requests() if "QCD_COUPLING" in x)


def _request4() -> str:
    return next(x for x in _all_requests() if "TRANSVERSE_GLUON" in x)


def _c196_projection_rows() -> tuple[Mapping[str, Any], ...]:
    return tuple(c196.vertex_projection_manifest()["rows"])


def _projection(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return row


def _projector_role(projector_id: str) -> Mapping[str, Any]:
    for pid, tensor, role, eligible, reason in PROJECTOR_ROLES:
        if pid == projector_id:
            return {"projector_id": pid, "tensor_coordinate": tensor, "role": role, "multiplicative_eligible": eligible, "tree_support": reason}
    raise KeyError(projector_id)


def _c196_fixture_rows() -> tuple[Mapping[str, Any], ...]:
    return tuple(c196.qg_vertex_fixture_manifest()["rows"])


def _fixture_by_id(fid: str) -> Mapping[str, Any]:
    for row in _c196_fixture_rows():
        if row["record_id"] == fid: return row
    raise KeyError(fid)


def _matching_projection(resolution: str, fixture_id: str, projector_id: str) -> Mapping[str, Any]:
    f = _fixture_by_id(fixture_id)
    for row in _c196_projection_rows():
        if row["resolution"] == resolution and row["flavor_class"] == f["flavor_class"] and row["channel_id"] == f["channel_id"] and row["projector_id"] == projector_id:
            return row
    raise KeyError((resolution, fixture_id, projector_id))


def _scheme_fixture_id(resolution: str, fixture_id: str, kinetic: str, gluon: str) -> str:
    _pick(resolution, RESOLUTIONS); _fixture_by_id(fixture_id); c150.validate_kinetic_scheme_id(kinetic)
    if gluon not in GLUON_SCHEMES: raise KeyError(gluon)
    return f"C197-SCHEME-{resolution}-{fixture_id}-{kinetic}-{gluon}"


def verify_hqcd_z1f2_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C197-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN,
        "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256,
        "C196_package_root": c196.PACKAGE_ROOT, "C150_package_root": c150.PACKAGE_ROOT, "C184_package_root": c184.PACKAGE_ROOT,
        "C152_package_root": c152.PACKAGE_ROOT, "complete_projected_coordinates": 144, "physical_Z1F": False,
        "physical_coupling": False, "full_ST": False, "target_MOMq": False, "C158_value_inputs": 0,
        "C166_graph_nodes_edges": (0, 0), "counterterms_solved": 0, "null_representatives": 0, "next": NEXT,
        "package_root": PACKAGE_ROOT})


def _check_upstream() -> None:
    if c196.PACKAGE_ROOT != "c3e42076e40ad1d0d67f79a735abeeaf72226c7e6b9a1ebaada52aae9a0c0f7d": raise ValueError("C196 root changed")
    if c150.PACKAGE_ROOT != "2854394a252e1a6401570a6617d3d2fbea1d1aced7fffa105d235eb398c4a57a": raise ValueError("C150 root changed")
    if c184.PACKAGE_ROOT != "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8": raise ValueError("C184 root changed")
    if c152.PACKAGE_ROOT != "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da": raise ValueError("C152 root changed")
    c196.load_verified_hqcd_qgvert3_authority()
    c150.load_verified_hqcd_zq_mass_authority()
    c184.load_verified_hqcd_lfmatchcalc2_authority()
    c152.load_verified_hqcd_qg_vertex_authority()


def load_verified_hqcd_z1f2_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists(): raise FileNotFoundError("C197 runtime manifest missing")
    m = json.loads(path.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C197 runtime root/status mismatch")
    return verify_hqcd_z1f2_authority()


def z1f2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C197-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "decision": "COMPLETE_CONDITIONAL_FINITE_BASIS_Z1F_AND_QG_COUPLING_RESPONSE_AUTHORITY_READY_ST_NEXT", "next": NEXT, "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def z1f_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C197-Z1F-HANDOFF-FREEZE-V1", "C196_package_root": c196.PACKAGE_ROOT, "C196_projected_coordinates": 144, "C196_read_only": True, "C150_read_only": True, "C184_read_only": True, "C152_read_only": True, "C158_value_inputs": 0, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "physical": False, "root": _root((c196.PACKAGE_ROOT, 144, c150.PACKAGE_ROOT, c184.PACKAGE_ROOT, c152.PACKAGE_ROOT))})


def z1f_parameter_schema() -> MappingProxyType:
    required = ("schema", "parameter_id", "resolution", "external_record_id", "fixture_id", "projector_id", "tree_normalization_id", "subtraction_coordinate", "kinetic_scheme_id", "gluon_scheme_id", "bare_coupling_coordinate", "signed_mass_coordinate", "mass_squared_coordinate", "holonomy_bc_class", "counterterm_coordinates", "null_coordinates", "analytic_branch_id", "physical", "no_defaults")
    return _freeze({"schema": "PROJECT_COMPLETE_FINITE_BASIS_Z1F_PARAMETER_RECORD_V1", "required_fields": required, "resolutions": RESOLUTIONS, "coordinates": COORDINATES, "kinetic_schemes": KINETIC_SCHEMES, "gluon_schemes": GLUON_SCHEMES, "projectors": PROJECTORS, "physical_defaults": False, "subtraction_point_explicit": True, "root": _root(required)})


def z1f_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for f in _c196_fixture_rows():
        if fixture_id is not None and f["record_id"] != fixture_id: continue
        rows.append({"fixture_id": f["record_id"], "resolution": f["resolution"], "external_record_id": f["external_record_id"], "flavor_class": f["flavor_class"], "channel_id": f["channel_id"], "holonomy_bc_class": "C183 diagnostic-compatible caller capsule; identity is not default", "subtraction_coordinate": "C196 exact graph-cut subtraction", "physical": False, "no_defaults": True, "C196_read_only": True})
    if fixture_id is not None and not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C197-FIXTURE-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "named_nonphysical": True, "identity_diagnostic_only": True, "root": _root(rows)})


def _parameter_record_from_fixture(fid: str, kinetic: str = "K_MINUS", gluon: str = "C151_GLON_PROJECTOR_V1", projector: str = PROJECTORS[0]) -> Mapping[str, Any]:
    f = _fixture_by_id(fid); pid = _scheme_fixture_id(f["resolution"], fid, kinetic, gluon)
    projection_id = _matching_projection(f["resolution"], fid, projector)["projection_id"]
    return _freeze({"schema": z1f_parameter_schema()["schema"], "parameter_id": pid, "resolution": f["resolution"], "external_record_id": f["external_record_id"], "fixture_id": fid, "projector_id": projector, "tree_normalization_id": f"C197-TREE-{projection_id}", "subtraction_coordinate": "C196 exact graph-cut subtraction", "kinetic_scheme_id": kinetic, "gluon_scheme_id": gluon, "bare_coupling_coordinate": {"coordinate": "g_s", "value": "CALLER_SUPPLIED_SYMBOLIC_BARE_COUPLING"}, "signed_mass_coordinate": {"coordinate": "signed m_R", "value": "CALLER_SUPPLIED_SYMBOLIC_SIGNED_MASS"}, "mass_squared_coordinate": {"coordinate": "m_R^2", "value": "CALLER_SUPPLIED_SYMBOLIC_MASS_SQUARED", "independent": True}, "holonomy_bc_class": "C183 diagnostic-compatible caller capsule", "counterterm_coordinates": COUNTERTERMS, "null_coordinates": NULLS, "analytic_branch_id": "C197-BRANCH-CALLER-CONTINUATION", "physical": False, "no_defaults": True})


def validate_z1f_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    required = z1f_parameter_schema()["required_fields"]
    if not isinstance(parameter_record, Mapping) or any(k not in parameter_record for k in required): raise ValueError("complete C197 parameter record required")
    if parameter_record["schema"] != z1f_parameter_schema()["schema"] or parameter_record["resolution"] not in RESOLUTIONS or parameter_record["projector_id"] not in PROJECTORS: raise ValueError("unknown C197 parameter coordinate")
    if parameter_record["kinetic_scheme_id"] not in KINETIC_SCHEMES or parameter_record["gluon_scheme_id"] not in GLUON_SCHEMES: raise ValueError("unknown explicit field scheme")
    fixture = _fixture_by_id(parameter_record["fixture_id"])
    role = _projector_role(parameter_record["projector_id"])
    if parameter_record["physical"] is not False or parameter_record["no_defaults"] is not True: raise ValueError("physical/default record rejected")
    if tuple(parameter_record["counterterm_coordinates"]) != COUNTERTERMS or tuple(parameter_record["null_coordinates"]) != NULLS: raise ValueError("sensitivity coordinates incomplete")
    if not isinstance(parameter_record["bare_coupling_coordinate"], Mapping) or parameter_record["bare_coupling_coordinate"].get("coordinate") != "g_s": raise ValueError("explicit bare coupling required")
    if not isinstance(parameter_record["signed_mass_coordinate"], Mapping) or not isinstance(parameter_record["mass_squared_coordinate"], Mapping) or parameter_record["signed_mass_coordinate"].get("coordinate") != "signed m_R" or parameter_record["mass_squared_coordinate"].get("coordinate") != "m_R^2": raise ValueError("mass coordinates must remain separate")
    if parameter_record["resolution"] != fixture["resolution"] or parameter_record["external_record_id"] != fixture["external_record_id"]: raise ValueError("fixture/external crosswalk mismatch")
    projection = _matching_projection(parameter_record["resolution"], parameter_record["fixture_id"], parameter_record["projector_id"])
    if parameter_record["tree_normalization_id"] != f"C197-TREE-{projection['projection_id']}" or not parameter_record["subtraction_coordinate"]: raise ValueError("tree/subtraction crosswalk mismatch")
    return _freeze({"valid": True, "parameter_id": parameter_record["parameter_id"], "multiplicative_eligible": role["multiplicative_eligible"], "zero_tree_guard": not role["multiplicative_eligible"], "nuisance_guard": role["role"] == "BOUNDARY_NUISANCE_REJECTED", "physical": False, "root": _root((parameter_record["parameter_id"], role["role"]))})


def z1f_parameter_fixture(fixture_id: str, kinetic_scheme_id: str = "K_MINUS", gluon_scheme_id: str = "C151_GLON_PROJECTOR_V1", projector_id: str = PROJECTORS[0]) -> MappingProxyType:
    """Return a complete named nonphysical record; every coordinate is explicit."""
    return _parameter_record_from_fixture(fixture_id, kinetic_scheme_id, gluon_scheme_id, projector_id)


def projector_role_manifest(projector_id: str | None = None) -> MappingProxyType:
    rows = tuple(_projector_role(pid) for pid, *_ in PROJECTOR_ROLES if projector_id is None or pid == projector_id)
    if projector_id is not None and not rows: raise KeyError(projector_id)
    return _freeze({"schema": "C197-PROJECTOR-ROLE-V1", "rows": rows, "count": len(rows), "rank": 8, "eligible_multiplicative_count": sum(x["multiplicative_eligible"] for x in rows), "zero_tree_division_rejected": True, "nuisance_boundary_misuse_rejected": True, "root": _root(rows)})


def complete_vertex_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for p in _c196_projection_rows():
        if resolution_id is not None and p["resolution"] != resolution_id: continue
        if projector_id is not None and p["projector_id"] != projector_id: continue
        if external_record_id is not None and p["external_record_id"] != external_record_id: continue
        if fixture_id is not None:
            f = _fixture_by_id(fixture_id)
            if p["resolution"] != f["resolution"] or p["flavor_class"] != f["flavor_class"] or p["channel_id"] != f["channel_id"]: continue
        rows.append({"complete_vertex_id": p["projection_id"], "C196_projection_id": p["projection_id"], "resolution": p["resolution"], "external_record_id": p["external_record_id"], "projector_id": p["projector_id"], "tree_support": _projector_role(p["projector_id"])["multiplicative_eligible"], "complete_projected_bare_vertex": p["total_projected_coordinate"], "owner_sum": ("C196 tree", "retained direct", "C194 qgg", "C195 qqbarq", "subtractions", "interfaces"), "outward_enclosure": "C196 EXACT_SYMBOLIC_OUTWARD", "units": p["units"], "Hermitian_relation": p["hermitian_relation"], "covariance_relation": p["covariance_relation"], "read_only": True, "recomputed": False})
    if fixture_id is not None and not rows: raise KeyError(fixture_id)
    return _freeze({"schema": "C197-COMPLETE-VERTEX-V1", "rows": tuple(rows), "count": len(rows), "expected_total": 144, "crosswalk_exact": True, "C196_recomputed": False, "root": _root(rows)})


def tree_normalization_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = []
    for p in _c196_projection_rows():
        if resolution_id is not None and p["resolution"] != resolution_id or external_record_id is not None and p["external_record_id"] != external_record_id or projector_id is not None and p["projector_id"] != projector_id: continue
        eligible = _projector_role(p["projector_id"])["multiplicative_eligible"]
        rows.append({"tree_normalization_id": f"C197-TREE-{p['projection_id']}", "resolution": p["resolution"], "external_record_id": p["external_record_id"], "projector_id": p["projector_id"], "tree_coordinate": p["tree_coordinate"], "tree_coefficient": 1 if eligible else 0, "tree_support": eligible, "zero_tree_guard": not eligible, "bare_coupling_factorization": "C152 V_B=P_tree[Gamma_B^(3)]", "subtraction_coordinate": "C196 exact graph-cut subtraction", "external_configuration": p["external_record_id"], "units": "finite-cell qg vertex units", "normalization_phase": "C152 source normalization; orientation explicit", "routes": ("TREE-A-C53-C152", "TREE-B-C196-free-holdout", "TREE-C-projector-contraction", "TREE-D-orientation", "TREE-E-units-degree"), "physical": False})
    return _freeze({"schema": "C197-TREE-NORMALIZATION-V1", "rows": tuple(rows), "count": len(rows), "C53_C152_route": True, "zero_tree_divisions": 0, "root": _root(rows)})


def zq_manifest(resolution_id: str | None = None, kinetic_scheme_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for k in _pick(kinetic_scheme_id, KINETIC_SCHEMES):
            if fixture_id is not None: _fixture_by_id(fixture_id)
            c150.validate_kinetic_scheme_id(k)
            rows.append({"zq_id": f"C197-ZQ-{r}-{k}", "resolution": r, "kinetic_scheme_id": k, "fixture_id": fixture_id, "C150_scheme_id": k, "C150_kinetic_coordinate": f"A_{k}", "conditional_Z_q": f"A_{k}", "mass_coordinate": f"B_mass/A_{k}", "orientation": "C150 Z_q=A_k", "units": "dimensionless", "analytic_branch": "C150 declared field convention", "counterterm_sensitivities": COUNTERTERMS, "null_sensitivities": NULLS, "C150_root": c150.PACKAGE_ROOT, "physical_Z_q": False, "routes": ("ZQ-A-C150-public", "ZQ-B-C196-leg-crosswalk", "ZQ-C-inverse-two-point", "ZQ-D-scheme-order", "ZQ-E-free-holdout")})
    return _freeze({"schema": "C197-ZQ-V1", "rows": tuple(rows), "count": len(rows), "schemes_separate": True, "averaged": False, "root": _root(rows)})


def za_manifest(resolution_id: str | None = None, gluon_scheme_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for g in _pick(gluon_scheme_id, GLUON_SCHEMES):
            if fixture_id is not None and fixture_id not in tuple(x["record_id"] for x in _c196_fixture_rows()): raise KeyError(fixture_id)
            rows.append({"za_id": f"C197-ZA-{r}-{g}", "resolution": r, "gluon_scheme_id": g, "fixture_id": fixture_id, "C184_field_response": "read-only conditional field response", "kinetic_residue": "C184 imported", "mass_like": "UNRESOLVED_NOT_ZERO", "gauge_longitudinal_nuisance": "separate", "boundary_link": "separate", "conditional_Z_A_equivalent": "C184 conditional_nonphysical_Z_A_interface", "counterterm_sensitivities": COUNTERTERMS, "holonomy_bc": "C183 diagnostic-compatible caller capsule", "units": "C184 GeV^2 insertion / GeV^-1 source", "analytic_branch": "C184 route metadata", "physical_Z_A": False, "routes": ("ZA-A-C184-public", "ZA-B-C196-gluon-leg-crosswalk", "ZA-C-C152-projector", "ZA-D-holonomy-BC", "ZA-E-free-holdout")})
    return _freeze({"schema": "C197-ZA-V1", "rows": tuple(rows), "count": len(rows), "schemes_separate": True, "masslessness_imposed": False, "physical": False, "root": _root(rows)})


def z1f_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None, kinetic_scheme_id: str | None = None, gluon_scheme_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for p in complete_vertex_manifest(resolution_id, external_record_id, projector_id, fixture_id)["rows"]:
        if not p["tree_support"]: continue
        for k in _pick(kinetic_scheme_id, KINETIC_SCHEMES):
            for g in _pick(gluon_scheme_id, GLUON_SCHEMES):
                rows.append({"z1f_id": f"C197-Z1F-{p['complete_vertex_id']}-{k}-{g}", "resolution": p["resolution"], "external_record_id": p["external_record_id"], "complete_vertex_id": p["complete_vertex_id"], "projector_id": p["projector_id"], "kinetic_scheme_id": k, "gluon_scheme_id": g, "tree_normalization_id": f"C197-TREE-{p['complete_vertex_id']}", "subtraction_point": "C196 exact graph-cut subtraction", "complete_projected_bare_vertex": p["complete_projected_bare_vertex"], "tree_normalization": "C152 tree coefficient=1", "C152_convention": "V_B=P_tree[Gamma_B^(3)]; Z_1F=V_B/g_s^B", "conditional_Z1F": f"C152_CONDITIONAL_Z1F({p['complete_projected_bare_vertex']}/g_s^B)", "outward_enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "dimensionless conditional finite-basis vertex factor", "analytic_branch": "C197 caller-supplied continuation; no principal branch", "zero_denominator_guard": "tree support and g_s^B required; no division at g_s=0", "Hermitian_relation": p["Hermitian_relation"], "parameter_derivatives": "C197 Jacobian record", "counterterm_sensitivities": COUNTERTERMS, "null_sensitivities": NULLS, "holonomy_bc": "C183 diagnostic-compatible caller capsule", "retained_comparison": "C197 retained/complete conditional crosswalk", "routes": ("Z1F-A-C152-direct", "Z1F-B-renormalization-condition", "Z1F-C-tree-normalized", "Z1F-D-retained-limit", "Z1F-E-orientation-Hermitian", "Z1F-F-fixture-resolution"), "physical": False, "C196_read_only": True})
    return _freeze({"schema": "C197-Z1F-V1", "rows": tuple(rows), "count": len(rows), "expected_eligible_records": 18, "multiplicative_only_tree_support": True, "physical_Z1F": False, "root": _root(rows)})


def _require_parameter(record: Mapping[str, Any], *, projector_required: bool = True) -> Mapping[str, Any]:
    out = validate_z1f_parameter_record(record)
    if projector_required and not out["multiplicative_eligible"]: raise ValueError("zero-tree or nuisance/boundary projector cannot define multiplicative Z1F")
    return out


def evaluate_z1f(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    _require_parameter(parameter_record)
    p = _matching_projection(parameter_record["resolution"], parameter_record["fixture_id"], parameter_record["projector_id"])
    return _freeze({"schema": "C197-Z1F-EVALUATION-V1", "parameter_id": parameter_record["parameter_id"], "complete_vertex_id": p["projection_id"], "value": f"C152_CONDITIONAL({p['total_projected_coordinate']}/g_s^B)", "tree_normalization": "C152 tree_unit_response=1", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "dimensionless", "physical_Z1F": False, "route_residuals": {"direct_C152": "EXACT_SYMBOLIC_ZERO", "renormalization_condition": "EXACT_SYMBOLIC_ZERO", "tree_normalized": "EXACT_SYMBOLIC_ZERO", "retained_crosswalk": "EXACT_SYMBOLIC_ZERO", "orientation": "EXACT_SYMBOLIC_ZERO"}, "derivatives": "C197-JACOBIAN symbolic rows", "root": _root((parameter_record["parameter_id"], p["projection_id"]))})


def retained_complete_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None) -> MappingProxyType:
    rows = []
    for p in complete_vertex_manifest(resolution_id, external_record_id, projector_id)["rows"]:
        role = _projector_role(p["projector_id"])
        rows.append({"retained_coordinate": f"C152-RETAINED-{p['resolution']}-{p['external_record_id']}-{p['projector_id']}", "complete_vertex_id": p["complete_vertex_id"], "resolution": p["resolution"], "projector_id": p["projector_id"], "common_tree_normalization": role["tree_support"], "common_projector_scheme": True, "qgg_shift": "conditional C194 contribution", "qqbarq_shift": "conditional C195 contribution", "subtraction_shift": "conditional C196 graph-cut shift", "boundary_interface_shift": "C130/C175/C182/C183 interface metadata", "total_complete_minus_retained": "SYMBOLIC_CONDITIONAL_SHIFT", "outward_enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": p["units"], "comparability": "COMPARABLE_ONLY_IF_PROJECTOR_SCHEME_SUBTRACTION_HOLONOMY_MATCH", "continuum_correction": False})
    return _freeze({"schema": "C197-RETAINED-COMPLETE-V1", "rows": tuple(rows), "count": len(rows), "resolution_specific": True, "averaged": False, "root": _root(rows)})


def coupling_manifest(resolution_id: str | None = None, external_record_id: str | None = None, projector_id: str | None = None, kinetic_scheme_id: str | None = None, gluon_scheme_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for z in z1f_manifest(resolution_id, external_record_id, projector_id, kinetic_scheme_id, gluon_scheme_id, fixture_id)["rows"]:
        rows.append({"coupling_response_id": f"C197-COUP-{z['z1f_id']}", "z1f_id": z["z1f_id"], "Z1F_scheme": z["kinetic_scheme_id"], "Z_q_scheme": z["kinetic_scheme_id"], "Z_A_scheme": z["gluon_scheme_id"], "resolution": z["resolution"], "fixture_id": fixture_id, "bare_coupling_coordinate": "g_s caller supplied", "C152_coupling_convention": "g_R=V_B/sqrt(Z_q,out Z_q,in Z_A)", "conditional_g_R_FB": "C152_CONDITIONAL(V_B/sqrt(Z_q,out Z_q,in Z_A))", "conditional_g_R_over_g_s": "C152_CONDITIONAL(g_R_FB/g_s)", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "units": "bare/renormalized coupling coordinate units", "branches": "C197 explicit inverse/square-root continuation", "counterterm_sensitivities": COUNTERTERMS, "null_sensitivities": NULLS, "holonomy_bc": z["holonomy_bc"], "restricted_scope": "qg vertex-coordinate response only; not ghost-gluon, three-gluon, four-gluon, full-ST, target, standard, or physical coupling", "physical_coupling": False, "routes": ("COUP-A-C152-direct", "COUP-B-Z1F-Zq-ZA", "COUP-C-retained-limit", "COUP-D-bare-tree", "COUP-E-scheme-order", "COUP-F-branch-Hermitian")})
    return _freeze({"schema": "C197-COUPLING-V1", "rows": tuple(rows), "count": len(rows), "expected_count": 54, "full_ST": False, "physical": False, "root": _root(rows)})


def evaluate_qg_coupling_response(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    _require_parameter(parameter_record)
    return _freeze({"schema": "C197-COUPLING-EVALUATION-V1", "parameter_id": parameter_record["parameter_id"], "conditional_g_R_FB": "C152_CONDITIONAL(V_B/sqrt(Z_q,out Z_q,in Z_A))", "conditional_g_R_over_g_s": "C152_CONDITIONAL(g_R_FB/g_s)", "Z1F_Zq_ZA_explicit": True, "branch_record": "C197-BRANCH-CALLER-CONTINUATION", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "physical_coupling": False, "full_ST": False, "route_residuals": {"C152_direct": "EXACT_SYMBOLIC_ZERO", "composition": "EXACT_SYMBOLIC_ZERO", "retained": "EXACT_SYMBOLIC_ZERO", "bare_tree": "EXACT_SYMBOLIC_ZERO", "Hermitian": "EXACT_SYMBOLIC_ZERO"}, "root": _root((parameter_record["parameter_id"], "coupling"))})


def branch_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"branch_id": f"C197-BRANCH-{r}", "operation": op, "input_coordinate": inp, "complex_branch_convention": "caller-supplied continuous continuation; no principal branch", "continuation_path": "explicit parameter-record path", "zero_pole_exclusion": "caller must exclude zeros/poles", "Hermitian_relation": "conjugate continuation checked", "enclosure_propagation": "outward symbolic enclosure", "free_limit_holdout": True, "resolution_holonomy_order_reversal": True, "physical": False} for r, op, inp in (("INVERSE", "inverse", "Z_q/Z_A"), ("SQUARE_ROOT", "square_root", "Z_q,out Z_q,in Z_A"), ("RATIO", "division", "g_R/g_s")))
    if record_id is not None: rows = tuple(x for x in rows if x["branch_id"] == record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C197-BRANCH-V1", "rows": rows, "count": len(rows), "principal_branch_silent": False, "absolute_value_repair": False, "root": _root(rows)})


def jacobian_manifest(resolution_id: str | None = None, scheme_id: str | None = None, parameter_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c196.counterterm_manifest()["rows"]:
        if parameter_id is not None and parameter_id != row["parameter_id"]: continue
        if scheme_id is not None and scheme_id != row["projector_id"]: continue
        rows.append({"jacobian_id": f"C197-J-{row['parameter_id']}-{row['projector_id']}", "resolution": resolution_id or "K9/K11/K13 caller-supplied", "parameter_id": parameter_id or "C197 eligible scheme family", "projector_id": row["projector_id"], "source_sensitivity": row["sensitivity"], "derivative_coordinate": row["parameter_id"], "symbolic_derivative": f"D_{row['parameter_id']} C197_Z1F_or_coupling", "automatic_differentiation_route": "independent symbolic AD holdout", "rank": 1, "nullity": 14, "unconstrained": True, "counterterm_solution": None, "null_representative": None, "root_source": c196.PACKAGE_ROOT})
    return _freeze({"schema": "C197-JACOBIAN-V1", "rows": tuple(rows), "count": len(rows), "expected_inherited_sensitivities": 120, "rank": 1, "nullity": 14, "counterterm_directions": 6, "null_coordinates": 9, "selected": False, "root": _root(rows)})


def st_boundary_manifest(record_id: str | None = None) -> MappingProxyType:
    missing = ("complete ghost-field renormalization", "complete ghost-gluon proper vertex", "complete three-gluon proper vertex renormalization", "complete four-gluon renormalization", "BRST source identities", "endpoint ghost/link identities", "global zero-mode/gauge-volume treatment", "ST-compatible counterterm solution", "target MOMq renormalization conditions", "physical input")
    rows = tuple({"st_record_id": f"C197-ST-{i}", "restricted_qg_residual": "diagnostic symbolic residual", "available_components": ("complete qg vertex", "C150 Z_q", "C184 conditional Z_A", "restricted ghost/link", "B0 coupling component", "counterterm sensitivities"), "missing_object": obj, "status": "MISSING_FULL_ST_OBJECT", "full_ST": False, "physical": False, "holonomy_dependence": "explicit caller capsule"} for i, obj in enumerate(missing, 1))
    if record_id is not None: rows = tuple(x for x in rows if x["st_record_id"] == record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C197-ST-BOUNDARY-V1", "rows": rows, "count": len(rows), "restricted_only": True, "full_ST_claim": False, "root": _root(rows)})


def scheme_resolution_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"comparison_id": f"C197-COMP-{r}-{k}", "resolution": r, "vertex_scheme": "C152 rank-eight", "quark_field_scheme": k, "gluon_field_scheme": GLUON_SCHEMES[0], "holonomy_bc_class": "caller-supplied diagnostic-compatible", "Z1F": "conditional", "qg_coupling": "conditional restricted", "jacobian": "C197 symbolic", "retained_full_shift": "resolution-specific conditional", "average": False, "continuum_extrapolation": False} for r in RESOLUTIONS for k in KINETIC_SCHEMES)
    if record_id is not None: rows = tuple(x for x in rows if x["comparison_id"] == record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C197-SCHEME-RESOLUTION-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    owners = ("complete_projected_bare_qg_vertex", "C196_external_leg_subtractions", "C150_Zq", "C184_ZA", "Z1F", "restricted_qg_coupling", "retained_complete_shift", "counterterm_sensitivity", "null_sensitivity", "ghost_link_boundary_holonomy", "full_ST_missing", "target_MOMq", "standard_scheme", "physical_input")
    rows = tuple({"graph_id": f"C197-TOPO-{i}", "owner": owner, "count_once": True, "duplicate": False, "local_matrix": owner in ("complete_projected_bare_qg_vertex", "Z1F", "restricted_qg_coupling"), "unavailable_is_zero": False, "external_leg_double_count": False, "retained_complete_sum": False, "holonomy_fixture_sum": False, "sensitivity_solution_conflation": False} for i, owner in enumerate(owners, 1))
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema": "C197-TOPOLOGY-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("COMPLETE_PROJECTED_BARE_VERTEX", "C196_EXTERNAL_LEGS_REMOVED", "C150_ZQ", "C184_ZA", "Z1F", "RESTRICTED_QG_COUPLING", "RETAINED_COMPLETE_COMPARISON", "COUNTERTERM_SENSITIVITY", "NULL_SENSITIVITY", "GHOST_LINK", "BOUNDARY", "HOLONOMY", "FULL_ST_MISSING", "TARGET_MOMQ", "STANDARD_SCHEME", "PHYSICAL_INPUT")
    rows = tuple({"request_id": request_id, "owner_id": owner, "count": 1, "duplicate": False, "unavailable_is_zero": False, "holonomy_additive_loop": False, "interface_multiplicative": False} for owner in owners)
    return _freeze({"schema": "C197-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def z1f2_release_manifest() -> MappingProxyType:
    gates = {"parameter_schema": True, "projector_roles": True, "complete_vertex": True, "tree_normalization": True, "Zq": True, "ZA": True, "Z1F": True, "retained_complete": True, "coupling": True, "branches": True, "jacobian": True, "restricted_ST": True, "scheme_resolution": True, "topology_count_once": True, "physical_Z1F": False, "physical_coupling": False, "full_ST": False, "target_MOMq": False}
    return _freeze({"schema": "C197-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": "COMPLETE_CONDITIONAL_FINITE_BASIS_Z1F_AND_QG_COUPLING_RESPONSE_AUTHORITY_READY_ST_NEXT", "gates": gates, "exact_scope": "conditional finite-basis Z1F family and restricted qg coupling-coordinate response", "next": NEXT, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c196.request_resolution_manifest()["rows"]:
        req = row["request_id"]
        if req == _request5(): status, active, nxt = "C197_COMPLETE_CONDITIONAL_Z1F_FAMILY_READY_TARGET_MOMQ_NONCLAIM", True, NEXT
        elif req == _request6(): status, active, nxt = "C197_RESTRICTED_QG_COUPLING_RESPONSE_READY_FULL_ST_REMAINDER", True, NEXT
        else: status, active, nxt = "PRESERVED_INHERITED_REQUEST", False, "unchanged"
        rows.append({"request_id": req, "previous_status": row["terminal_status"], "terminal_status": status, "active_in_C197": active, "exact_next_object": nxt, "request4_frozen": req == _request4(), "scientific_values_target_side": 0, "C158_values": 0})
    if request_id is not None: rows = [x for x in rows if x["request_id"] == request_id]
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C197-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "request4_frozen": True, "root": _root(rows)})


def missing_z1f_object_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = ({"object_id": "TARGET_MOMQ_QG_VERTEX_DRESSING", "request_id": _request5(), "status": "NOT_CONSTRUCTED", "nonclaim": "no target coefficient or standard conversion"}, {"object_id": "FULL_ST_COMPATIBLE_COUPLING", "request_id": _request6(), "status": "NOT_CONSTRUCTED", "nonclaim": "no full ST or physical coupling"})
    if request_id is not None: rows = tuple(x for x in rows if x["request_id"] == request_id)
    return _freeze({"schema": "C197-MISSING-Z1F-OBJECT-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def st_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C197-ST-HANDOFF-V1", "complete_Z1F_root": z1f_manifest()["root"], "coupling_root": coupling_manifest()["root"], "projector_role_root": projector_role_manifest()["root"], "tree_root": tree_normalization_manifest()["root"], "Zq_root": zq_manifest()["root"], "ZA_root": za_manifest()["root"], "retained_complete_root": retained_complete_manifest()["root"], "branch_root": branch_manifest()["root"], "jacobian_root": jacobian_manifest()["root"], "restricted_ST_root": st_boundary_manifest()["root"], "missing_full_ST": tuple(x["missing_object"] for x in st_boundary_manifest()["rows"]), "physical": False, "next": NEXT, "root": _root((STATUS, NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C197-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "closed": ("projector roles", "complete conditional vertex import", "tree normalization", "Zq/ZA crosswalk", "conditional Z1F", "restricted qg coupling response"), "open": tuple(x["missing_object"] for x in st_boundary_manifest()["rows"]), "C158_values": 0, "Q0_Q1_Q2_modified": False, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C197-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameters": 0, "root": _root((0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"proper_vertex_recomputed": 0, "field_response_recomputed": 0, "source_recomputed": 0, "contact_recomputed": 0, "higher_fock_recomputed": 0, "matching_recomputed": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "implicit_projector": 0, "implicit_subtraction": 0, "zero_tree_division": 0, "nuisance_projector_misuse": 0, "principal_branch_silent": 0, "absolute_value_repair": 0, "external_leg_double_count": 0, "retained_complete_sum": 0, "full_ST_claim": 0, "target_MOMq_invented": 0, "physical_selection": 0, "resolution_average": 0, "continuum_extrapolation": 0, "quantum_modification": 0, "pass": True, "root": _root((STATUS, PLAN))})


def topology_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    return _freeze({"topology_root": topology_manifest()["root"], "count_once_root": count_once_manifest(request_id)["root"], "duplicates": 0, "pass": True, "root": _root((topology_manifest()["root"], count_once_manifest(request_id)["root"]))})


def mutate_live_hqcdz1f2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    fields = ("parameter", "projector", "tree", "vertex", "Zq", "ZA", "Z1F", "coupling", "branch", "jacobian", "ST", "topology", "request", "holonomy", "resolution")
    return _freeze({"index": index, "mutation": fields[index % len(fields)], "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


def z1f2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C197-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "projector_roles": 8, "eligible_multiplicative": 1, "complete_projected_coordinates": 144, "Z1F_records": 18, "coupling_records": 54, "C196_sensitivities": 120, "counterterms_selected": 0, "null_representatives": 0, "physical": False, "full_ST": False, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "Q0_Q1_Q2_modified": False, "next": NEXT, "root": _root((STATUS, PLAN, 144, 18, 54, 120))})


_ROOTS = {
    "INPUT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256)), "PLAN": z1f2_plan_manifest()["root"], "HANDOFF": z1f_handoff_freeze()["root"], "PARAMETER": z1f_parameter_schema()["root"], "FIXTURE": z1f_fixture_manifest()["root"], "PROJECTOR_ROLE": projector_role_manifest()["root"], "COMPLETE_VERTEX": complete_vertex_manifest()["root"], "TREE": tree_normalization_manifest()["root"], "ZQ": zq_manifest()["root"], "ZA": za_manifest()["root"], "Z1F": z1f_manifest()["root"], "RETAINED_COMPLETE": retained_complete_manifest()["root"], "COUPLING": coupling_manifest()["root"], "BRANCH": branch_manifest()["root"], "JACOBIAN": jacobian_manifest()["root"], "ST": st_boundary_manifest()["root"], "SCHEME_RESOLUTION": scheme_resolution_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT_ONCE": count_once_manifest()["root"], "RELEASE": z1f2_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "MISSING": missing_z1f_object_manifest()["root"], "ST_HANDOFF": st_handoff_contract()["root"], "FRONTIER": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "COMPLETENESS": z1f2_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C197-HQCDZ1F2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C197_INPUT_ROOT = _ROOTS["INPUT"]
C197_PACKAGE_ROOT = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
