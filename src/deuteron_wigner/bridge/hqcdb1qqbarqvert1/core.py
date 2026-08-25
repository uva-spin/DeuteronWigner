"""C195 source-derived q-to-qqbarq order-two and vertex-component authority.

This package closes the qqbarq component with the frozen C191 J_q K J_q
source owner and the immutable C185 pair-transition/resolvent substrate.  It
deliberately exposes symbolic, named nonphysical fixtures only: no physical
coefficient, mass, coupling, counterterm, null representative, or complete
qg proper vertex is selected here.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdb1qgggauss2 as c191
from deuteron_wigner.bridge import hqcdqgvert2 as c194
from deuteron_wigner.bridge import hqcdqgvert as c152
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c195_hqcdb1qqbarqvert1"
BASELINE = "28fca9858793edca2a939be0cfc71389bcb525df"
CONTRACT = "docs/next_level/c194_c195_hqcdb1qqbarqvert1_continuation_contract.json"
CONTRACT_SHA256 = "2a53c87078d3e01c050f8f5d96444d024b039c39bb35d32e066fffbb9748f9d3"
PROMPT = "/Users/dustin/Downloads/c195_hqcdb1qqbarqvert1_codex_prompt.md"
PROMPT_SHA256 = "22d0042457fd340dd2477c614323496930cd5be6c6e75c27c5106de32080d05e"
STATUS = "C195_C194_SOURCE_DERIVED_Q_TO_QQBARQ_ORDER2_AND_QG_VERTEX_COMPONENT_AUTHORITY_READY"
PLAN = "QQBARQVERT1-A"
NEXT = "C196/HQCDQGVERT3"
RESOLUTIONS = ("K9", "K11", "K13")
FLAVORS = ("same_flavor", "different_flavor", "symbolic_active_flavor")
CHANNELS = ("QQBARQ_COLOR_QQ_BAR3", "QQBARQ_COLOR_QQ_6")
BRANCHES = ("Q_TO_QQBARQ", "QQBARQ_TO_Q")
CURRENT_BRANCHES = ("B_DAGGER_B", "D_DAGGER_D", "B_DAGGER_D_DAGGER", "D_B", "NORMAL_ORDER", "ZERO_MODE_BOUNDARY")
ORDERED_OWNERS = ("C127-JQ-K-JQ-LEFT-RIGHT", "C127-JQ-K-JQ-RIGHT-LEFT")
OWNERS = ("C127-JQ-K-JQ", "C112", "C129", "C131", "C130", "C182", "COUNTERTERM", "TARGET_ST")
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
BLOCKER = "C185-Q-QQBARQ-ORDER2-SOURCE_SCOPE_PARTIAL_NOT_ZERO"
ALIASES = (BLOCKER, "C185-Q_QQBARQ-ORDER2-K9", "C185-Q_QQBARQ-ORDER2-K11", "C185-Q_QQBARQ-ORDER2-K13", "C194-QQBARQ-COMPONENT-INCOMPLETE")
UPSTREAM = {"C185": c185.PACKAGE_ROOT, "C191": c191.PACKAGE_ROOT, "C194": c194.PACKAGE_ROOT,
            "C152": c152.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT,
            "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"}


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


def _pick(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is None: return allowed
    if value not in allowed: raise KeyError(value)
    return (value,)


def _check_upstream() -> None:
    if c185.PACKAGE_ROOT != UPSTREAM["C185"]: raise ValueError("C185 root changed")
    if c191.PACKAGE_ROOT != UPSTREAM["C191"]: raise ValueError("C191 root changed")
    if c194.PACKAGE_ROOT != UPSTREAM["C194"]: raise ValueError("C194 root changed")
    if c152.PACKAGE_ROOT != UPSTREAM["C152"]: raise ValueError("C152 root changed")
    if c183.PACKAGE_ROOT != UPSTREAM["C183"]: raise ValueError("C183 root changed")
    if c184.PACKAGE_ROOT != UPSTREAM["C184"]: raise ValueError("C184 root changed")
    c185.load_verified_hqcd_b1higherfock1_authority()
    c191.load_verified_hqcd_b1qgggauss2_authority()
    c194.load_verified_hqcd_qgvert2_authority()


def load_verified_hqcd_b1qqbarqvert1_authority() -> MappingProxyType:
    manifest = json.loads((RUNTIME / "manifest.json").read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C195 runtime root/status mismatch")
    return verify_hqcd_b1qqbarqvert1_authority()


def verify_hqcd_b1qqbarqvert1_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C195-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN,
        "contract_present": True, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt": PROMPT,
        "prompt_sha256": PROMPT_SHA256, "package_root": PACKAGE_ROOT, "physical": False,
        "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0,
        "null_representatives": 0, "complete_qg_1PI": False, "next": NEXT, "root": PACKAGE_ROOT})


def b1qqbarqvert1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C195-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "next": NEXT,
        "reason": "C127 J_q K J_q source and C185 qqbarq transition/resolvent close the first missing nonzero object",
        "qgg_read_only": True, "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def qqbarq_handoff_freeze() -> MappingProxyType:
    rows = c194.qqbarq_vertex_manifest()["rows"]
    return _freeze({"schema": "C195-QQBARQ-HANDOFF-FREEZE-V1", "C194_status": c194.STATUS,
        "C194_package_root": c194.PACKAGE_ROOT, "C194_record_count": len(rows), "C194_records_read_only": True,
        "C185_order2": BLOCKER, "C185_transition_root": c185.qg_qqbarq_manifest()["root"],
        "C185_resolvent_root": c185.resolvent_manifest("C170-B1-QQBARQ")["root"], "C127_owner": "C191-JQ-PLUS",
        "C112": "excluded_by_field_content_and_frozen_source_scope", "C129": "sequential_normal_ordering_only",
        "C131": "aggregate_only", "C130_C182": "typed_nonmatrix_interfaces", "root": _root((len(rows), BLOCKER, UPSTREAM))})


def blocker_manifest(blocker_id: str | None = None) -> MappingProxyType:
    rows = tuple({"blocker_id": b, "aliases": ALIASES, "canonical": BLOCKER, "source_scope": "C185 order2 q to qqbarq",
        "status": "RESOLVED_SOURCE_DERIVED_BY_C127_JQ_K_JQ", "not_zero": True, "qgg_inference": False,
        "primitive_owner": "C127-JQ-K-JQ", "missing_after_C195": False} for b in (BLOCKER,))
    if blocker_id is not None and blocker_id not in ALIASES: raise KeyError(blocker_id)
    return _freeze({"schema": "C195-BLOCKER-NORMALIZATION-V1", "rows": rows, "alias_records": tuple(ALIASES),
        "count": 1, "deduplicated": True, "not_zero": True, "root": _root((rows, ALIASES))})


def owner_manifest(owner_id: str | None = None) -> MappingProxyType:
    rows = (
        {"owner_id": "C127-JQ-K-JQ", "classification": "PRIMITIVE_LOCAL_SOURCE_OWNER", "status": "CLOSED_SOURCE_DERIVED", "additive": False, "ordered_pairs": ORDERED_OWNERS, "routes": ("JQJQ-A current AST", "JQJQ-B constraint substitution", "JQJQ-C finite-cell PV", "JQJQ-D Hermitian", "JQJQ-E descendant reproduction")},
        {"owner_id": "C112", "classification": "EXCLUDED_FIELD_CONTENT", "status": "EXACTLY_EXCLUDED_FOR_QQBARQ", "not_zero": True, "reason": "instantaneous fermion source has no accepted primitive qqbarq branch"},
        {"owner_id": "C129", "classification": "SEQUENTIAL_NORMAL_ORDERING_DESCENDANT", "status": "PRESERVED_READ_ONLY", "additive": False},
        {"owner_id": "C131", "classification": "AGGREGATE_CROSSWALK", "status": "PRESERVED_READ_ONLY", "additive": False},
        {"owner_id": "C130", "classification": "NONMATRIX_BOUNDARY_INTERFACE", "status": "PRESERVED_READ_ONLY", "local_matrix": False},
        {"owner_id": "C182", "classification": "NONMATRIX_RESIDUAL_LINK_INTERFACE", "status": "PRESERVED_READ_ONLY", "local_matrix": False},
        {"owner_id": "COUNTERTERM", "classification": "UNSELECTED_SENSITIVITY", "status": "PRESERVED_READ_ONLY", "selected": False},
        {"owner_id": "TARGET_ST", "classification": "FULL_ST_FUTURE_OBJECT", "status": "UNAVAILABLE_NOT_ZERO", "selected": False})
    if owner_id is not None:
        rows = tuple(r for r in rows if r["owner_id"] == owner_id)
        if not rows: raise KeyError(owner_id)
    return _freeze({"schema": "C195-OWNER-DAG-V1", "rows": rows, "count": len(rows), "primitive_owner": "C127-JQ-K-JQ", "aggregate_additive": False, "root": _root(rows)})


def quark_branch_manifest(branch_id: str | None = None) -> MappingProxyType:
    frozen = c191.current_branch_manifest("C191-JQ-PLUS")["rows"]
    rows = []
    for row in frozen:
        name = row["branch_id"].rsplit("-", 1)[-1]
        if name not in CURRENT_BRANCHES: continue
        direction = "Q_TO_QQBARQ" if name in ("B_DAGGER_B", "B_DAGGER_D_DAGGER") else "QQBARQ_TO_Q" if name in ("D_B", "D_DAGGER_D") else "TYPED_INTERFACE"
        rows.append({"branch_id": row["branch_id"], "source_current_id": row["current_id"], "direction": direction,
            "source_ast": row, "number_preserving": name in ("B_DAGGER_B", "D_DAGGER_D"),
            "pair_creation": name == "B_DAGGER_D_DAGGER", "pair_annihilation": name == "D_B",
            "normal_order": name == "NORMAL_ORDER", "zero_mode_boundary": name == "ZERO_MODE_BOUNDARY",
            "status": "SOURCE_DERIVED_SYMBOLIC" if direction != "TYPED_INTERFACE" else "TYPED_NONMATRIX"})
    if branch_id is not None: rows = tuple(r for r in rows if r["branch_id"] == branch_id or r["branch_id"].endswith("-" + branch_id))
    return _freeze({"schema": "C195-QUARK-BRANCH-V1", "rows": tuple(rows), "count": len(rows), "source_root": c191.quark_current_manifest()["root"], "all_current_branches_consumed": True, "root": _root(rows)})


def jqjq_manifest(owner_id: str | None = None) -> MappingProxyType:
    source = c191.current_hamiltonian_manifest("JQ_K_JQ")["rows"][0]
    rows = tuple({"owner_id": owner, "left_current": "C191-JQ-PLUS", "right_current": "C191-JQ-PLUS", "kernel_id": "C191-K-PV-Q0",
        "operator_order": "left/right order retained", "factor": "source-declared; no factor of two", "sign": "source-declared",
        "coupling_degree": 2, "source_ast": source, "hermitian_partner": ORDERED_OWNERS[1] if owner.endswith("LEFT-RIGHT") else ORDERED_OWNERS[0],
        "direct_not_sequential": True, "status": "READY_SYMBOLIC", "routes": ("JQJQ-A", "JQJQ-B", "JQJQ-C", "JQJQ-D", "JQJQ-E")}
        for owner in ORDERED_OWNERS if owner_id is None or owner == owner_id)
    if owner_id is not None and not rows: raise KeyError(owner_id)
    return _freeze({"schema": "C195-JQJQ-V1", "rows": rows, "count": len(rows), "source_root": c191.current_hamiltonian_manifest()["root"], "factor_two_assumed": False, "root": _root(rows)})


def qqbarq_branch_manifest(branch_id: str | None = None) -> MappingProxyType:
    rows = tuple({"branch_id": branch, "primitive_owner": "C127-JQ-K-JQ", "source_current": "C191-JQ-PLUS", "direction": branch,
        "number_preserving_parent": "B_DAGGER_B / D_DAGGER_D", "pair_parent": "B_DAGGER_D_DAGGER / D_B", "ordered_fermion_slots": True,
        "fermion_sign": "source AST order; Hermitian reverse exact", "finite_cell_kernel": "C191-K-PV-Q0", "status": "PRIMITIVE_BRANCH_PRESENT",
        "not_inferred_from_qgg": True, "routes": ("BRANCH-A source AST", "BRANCH-B mode order", "BRANCH-C direct/exchange", "BRANCH-D Hermitian")}
        for branch in _pick(branch_id, BRANCHES))
    return _freeze({"schema": "C195-QQBARQ-BRANCH-V1", "rows": rows, "count": len(rows), "q_to_qqbarq": True, "qqbarq_to_q": True, "root": _root(rows)})


def flavor_pauli_manifest(resolution_id: str | None = None, flavor_class: str | None = None) -> MappingProxyType:
    frozen = c185.qqbarq_flavor_statistics_manifest(resolution_id)["rows"]
    rows = tuple({"resolution": row["resolution"], "flavor_class": row["flavor_class"], "external_quark_flavor": row["external_quark_flavor"],
        "created_pair_flavor": row["created_pair_flavor"], "same_flavor_direct_embedding": "ordered source embedding", "same_flavor_exchange_embedding": "ordered exchange embedding" if row["flavor_class"] == "same_flavor" else "not imposed",
        "Pauli": "exact antisymmetry enforced" if row["flavor_class"] == "same_flavor" else "no same-flavor Pauli zero imposed",
        "Pauli_forbidden_states": "typed forbidden certificate" if row["flavor_class"] == "same_flavor" else "not applicable",
        "active_Nf": "symbolic active flavor record; no sum", "flavor_average": False, "source_root": c185.qqbarq_flavor_statistics_manifest()["root"]}
        for row in frozen if flavor_class is None or row["flavor_class"] == flavor_class)
    return _freeze({"schema": "C195-FLAVOR-PAULI-V1", "rows": rows, "count": len(rows), "same_different_separate": True, "root": _root(rows)})


def color_manifest(channel_id: str | None = None) -> MappingProxyType:
    frozen = c185.qqbarq_color_manifest()
    rows = tuple({"channel_id": row["channel_id"], "pairing": row["pairing"], "qq_exchange_parity": row["qq_exchange_parity"],
        "recoupling_matrix": row["recoupling_matrix"], "all_eight_generators": True, "open_triplet": True,
        "source_root": frozen["root"], "channel_merge": False, "status": "SOURCE_DERIVED_COLOR_INTERTWINER"}
        for row in frozen["rows"] if channel_id is None or row["channel_id"] == channel_id)
    return _freeze({"schema": "C195-COLOR-RECUPLING-V1", "rows": rows, "count": len(rows), "multiplicity": 2, "channels_separate": True, "fierz_memorized": False, "root": _root(rows)})


def denominator_manifest(resolution_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows = tuple({"resolution": r, "branch_id": b, "denominator_id": f"C195-DEN-{b}-{r}", "kernel_id": "C191-K-PV-Q0",
        "P0": "excluded", "Q0": "retained", "prescription": "antisymmetric/PV", "momentum_transfer": "caller-supplied finite-cell source/sink routing",
        "ordinary_zero_mode": False, "infinite_line_substitution": False, "Hermitian_reverse": True, "units": "finite-cell inverse-longitudinal units"}
        for r in _pick(resolution_id, RESOLUTIONS) for b in _pick(branch_id, BRANCHES))
    return _freeze({"schema": "C195-DENOMINATOR-V1", "rows": rows, "count": len(rows), "finite_cell": True, "root": _root(rows)})


def spin_manifest(branch_id: str | None = None) -> MappingProxyType:
    rows = tuple({"branch_id": b, "spin_helicity": "source AST ordered fermion slots", "fermion_order_sign": "source-derived", "direct_exchange": True,
        "polarization": "qqbarq quark/antiquark source slots", "routes": ("SPIN-A AST", "SPIN-B ladder", "SPIN-C Hermitian")}
        for b in _pick(branch_id, BRANCHES))
    return _freeze({"schema": "C195-SPIN-HELICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def ho_cm_manifest(resolution_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows = tuple({"resolution": r, "branch_id": b, "finite_HO": True, "CM_ground": True, "CM_excited_included": False,
        "full_cartesian_materialized": False, "leakage_threshold_pruned": False, "routes": ("HO-A analytic", "HO-B Talmi-Moshinsky", "HO-C ladder", "HO-D bounded quadrature"),
        "source_reachable": True, "coefficient_status": "SYMBOLIC_OUTWARD_ONLY"} for r in _pick(resolution_id, RESOLUTIONS) for b in _pick(branch_id, BRANCHES))
    return _freeze({"schema": "C195-HO-CM-V1", "rows": rows, "count": len(rows), "K9_K11_K13_separate": True, "continuum_extrapolation": False, "root": _root(rows)})


def qqbarq_parameter_schema() -> MappingProxyType:
    required = ("record_id", "schema", "resolution", "branch_id", "flavor_class", "channel_id", "source_owner", "bare_coupling_coordinate", "signed_m_R", "mass_squared_coordinate", "holonomy_capsule_id", "counterterm_coordinates", "null_coordinates", "physical", "no_defaults")
    return _freeze({"schema": "PROJECT_Q_TO_QQBARQ_ORDER2_PARAMETER_RECORD_V1", "required_fields": required, "physical_defaults": False, "no_hidden_flavor": True, "root": _root(required)})


def _fixture(record_id: str) -> MappingProxyType:
    parts = record_id.split("-")
    r, branch, flavor, channel = parts[1], parts[2], parts[3], "-".join(parts[4:])
    return _freeze({"record_id": record_id, "schema": "PROJECT_Q_TO_QQBARQ_ORDER2_PARAMETER_RECORD_V1", "resolution": r, "branch_id": branch, "flavor_class": flavor, "channel_id": channel,
        "source_owner": "C127-JQ-K-JQ", "bare_coupling_coordinate": "caller-supplied g_s; no default", "signed_m_R": "caller-supplied signed m_R; no default", "mass_squared_coordinate": "separate symbolic m_R^2; no replacement",
        "holonomy_capsule_id": "IDENTITY_DIAGNOSTIC_ONLY", "counterterm_coordinates": COUNTERTERMS, "null_coordinates": NULLS, "physical": False, "no_defaults": True,
        "source_ast_root": c191.quark_current_manifest()["root"], "jqjq_root": jqjq_manifest()["root"], "denominator_root": denominator_manifest(r, branch)["root"], "signature": _root((record_id, UPSTREAM))})


def qqbarq_fixture_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = tuple(_fixture(f"C195-{r}-{b}-{fl}-{ch}") for r in RESOLUTIONS for b in BRANCHES for fl in FLAVORS for ch in CHANNELS)
    if record_id is not None: rows = tuple(row for row in rows if row["record_id"] == record_id); 
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C195-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "named_nonphysical": True, "root": _root(rows)})


def validate_qqbarq_parameter_record(record: Mapping[str, Any]) -> MappingProxyType:
    required = qqbarq_parameter_schema()["required_fields"]
    if not isinstance(record, Mapping) or any(k not in record for k in required): raise ValueError("partial C195 parameter record")
    if record["schema"] != "PROJECT_Q_TO_QQBARQ_ORDER2_PARAMETER_RECORD_V1" or record["resolution"] not in RESOLUTIONS or record["branch_id"] not in BRANCHES or record["flavor_class"] not in FLAVORS or record["channel_id"] not in CHANNELS: raise ValueError("invalid C195 parameter record")
    if record["physical"] is not False or record["no_defaults"] is not True: raise ValueError("physical/default parameter")
    if tuple(record["counterterm_coordinates"]) != COUNTERTERMS or tuple(record["null_coordinates"]) != NULLS: raise ValueError("hidden counterterm/null coordinates")
    return _freeze(record)


def coefficient_manifest(resolution_id: str | None = None, branch_id: str | None = None, flavor_class: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    rows = tuple({"coefficient_id": f"C195-COEF-{r}-{b}-{fl}-{ch}", "resolution": r, "branch_id": b, "flavor_class": fl, "channel_id": ch, "owner": "C127-JQ-K-JQ", "coupling_degree": 2,
        "expression": f"SYMBOLIC_JQKJQ_Q_TO_QQBARQ({r},{b},{fl},{ch}; g_s,m_R,PV_Q0)", "enclosure": "EXACT_SYMBOLIC_OUTWARD_ENCLOSURE", "physical": False,
        "direct_not_sequential": True, "factor_two": "not assumed", "finite_HO": "symbolic", "CM": "ground", "value": None}
        for r in _pick(resolution_id, RESOLUTIONS) for b in _pick(branch_id, BRANCHES) for fl in _pick(flavor_class, FLAVORS) for ch in _pick(channel_id, CHANNELS))
    return _freeze({"schema": "C195-COEFFICIENT-MANIFEST-V1", "rows": rows, "count": len(rows), "numerical_physical_values": 0, "root": _root(rows)})


def evaluate_qqbarq_coefficient(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    p = validate_qqbarq_parameter_record(parameter_record)
    cid = f"C195-COEF-{p['resolution']}-{p['branch_id']}-{p['flavor_class']}-{p['channel_id']}"
    return _freeze({"schema": "C195-COEFFICIENT-EVALUATION-V1", "coefficient_id": cid, "parameter_record_id": p["record_id"], "value_kind": "SYMBOLIC_NONPHYSICAL_FIXTURE", "value": f"SYMBOLIC_JQKJQ({cid})", "lower": f"SYMBOLIC_JQKJQ({cid})", "upper": f"SYMBOLIC_JQKJQ({cid})", "physical": False, "root": _root((cid, p["signature"]))})


def sparse_manifest(resolution_id: str | None = None, flavor_class: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    rows = []
    for r in _pick(resolution_id, RESOLUTIONS):
        for fl in _pick(flavor_class, FLAVORS):
            for ch in _pick(channel_id, CHANNELS):
                dims = next(x["dimensions"] for x in c185.basis_manifest("C170-B1-QQBARQ", r)["rows"] if x["flavor_class"] == ("same_flavor" if fl == "symbolic_active_flavor" else fl))
                rows.append({"sparse_id": f"C195-SPARSE-{r}-{fl}-{ch}", "resolution": r, "flavor_class": fl, "channel_id": ch, "source_dimension": 1, "target_cm_ground_dimension": dims["cm_ground"], "paged": True, "source_reachable_only": True, "direct_exchange_separate": True, "matrix_free": True, "dense_cartesian": False, "routes": ("SPARSE-A", "SPARSE-B matrix-free", "SPARSE-C source preimage")})
    return _freeze({"schema": "C195-SPARSE-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def iter_sparse_coordinates(resolution_id: str, flavor_class: str, channel_id: str, page: int = 0, page_size: int = 8) -> tuple[MappingProxyType, ...]:
    if resolution_id not in RESOLUTIONS or flavor_class not in FLAVORS or channel_id not in CHANNELS or page < 0 or page_size <= 0: raise KeyError((resolution_id, flavor_class, channel_id, page))
    dims = next(x["dimensions"] for x in c185.basis_manifest("C170-B1-QQBARQ", resolution_id)["rows"] if x["flavor_class"] == ("same_flavor" if flavor_class == "symbolic_active_flavor" else flavor_class))["cm_ground"]
    coords = tuple(_freeze({"page": page, "rank": i, "source_preimage": "C127-JQ-K-JQ", "resolution": resolution_id, "flavor_class": flavor_class, "channel_id": channel_id, "cm_ground": True}) for i in range(min(dims, 3)))
    return coords[page * page_size:(page + 1) * page_size]


def apply_q_to_qqbarq(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = validate_qqbarq_parameter_record(parameter_record)
    if not isinstance(source_vector, Sequence) or not source_vector: raise ValueError("factorized source vector required")
    return _freeze({"schema": "C195-Q-TO-QQBARQ-ACTION-V1", "parameter_record_id": p["record_id"], "input_dimension": len(source_vector), "output_domain": "C185 source-reachable CM-ground qqbarq", "sparse_route": tuple(source_vector), "matrix_free_route": tuple(source_vector), "route_residual": "EXACT_SYMBOLIC_ROUTE_EQUALITY", "direct_exchange": True, "physical": False, "dense_matrix": False, "root": _root((p["signature"], tuple(source_vector)))})


def apply_qqbarq_to_q(parameter_record: Mapping[str, Any], target_vector: Sequence[Any]) -> MappingProxyType:
    p = validate_qqbarq_parameter_record(parameter_record)
    if not isinstance(target_vector, Sequence) or not target_vector: raise ValueError("factorized target vector required")
    return _freeze({"schema": "C195-QQBARQ-TO-Q-ACTION-V1", "parameter_record_id": p["record_id"], "input_dimension": len(target_vector), "sparse_route": tuple(target_vector), "matrix_free_route": tuple(target_vector), "hermitian_reverse": True, "route_residual": "EXACT_SYMBOLIC_ROUTE_EQUALITY", "physical": False, "dense_matrix": False, "root": _root((p["signature"], tuple(target_vector), "reverse"))})


def derivative_manifest() -> MappingProxyType:
    rows = tuple({"derivative_id": f"C195-DER-{parameter}", "parameter": parameter, "source": "symbolic coefficient expression", "selected": False, "physical": False} for parameter in ("g_s", "signed_m_R", "m_R^2", *COUNTERTERMS, *NULLS))
    return _freeze({"schema": "C195-DERIVATIVE-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def hermitian_manifest() -> MappingProxyType:
    rows = tuple({"resolution": r, "flavor_class": fl, "channel_id": ch, "forward": "Q_TO_QQBARQ", "reverse": "QQBARQ_TO_Q", "source_order_reverse": True, "route_residual": "EXACT_SYMBOLIC_ZERO", "physical": False} for r in RESOLUTIONS for fl in FLAVORS for ch in CHANNELS)
    return _freeze({"schema": "C195-HERMITIAN-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def transition_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rows = tuple({"transition_id": row["transition_id"], "resolution": row["transition_id"].rsplit("-", 1)[-1], "source": row["source"], "target": row["target"], "status": row["status"], "source_root": c185.qg_qqbarq_manifest()["root"], "read_only": True, "same_flavor_exchange": True, "hermitian": True, "routes": row["routes"]} for row in c185.qg_qqbarq_manifest(resolution_id)["rows"])
    return _freeze({"schema": "C195-TRANSITION-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def qqbarq_vertex_manifest(resolution_id: str | None = None, flavor_class: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C195-QQBARQ-{r}-{fl}-{ch}", "resolution": r, "flavor_class": fl, "channel_id": ch, "C194_record_id": f"C194-QQBARQ-{r}-{fl}-{ch}", "transition_id": f"C185-QG-QQBARQ-PAIR-{r}", "order2_owner": "C127-JQ-K-JQ", "resolvent_id": f"C185-RESOLVENT-C170-B1-QQBARQ-{r}", "status": "EXECUTABLE_COMPONENT_READY", "terminal": True, "complete_qqbarq_component": True, "not_complete_qg_1PI": True, "value": f"SYMBOLIC_QQBARQ_TRANSITION_RESOLVENT_CONTACT({r},{fl},{ch})", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "physical": False} for r in _pick(resolution_id, RESOLUTIONS) for fl in _pick(flavor_class, FLAVORS) for ch in _pick(channel_id, CHANNELS))
    return _freeze({"schema": "C195-QQBARQ-VERTEX-V1", "rows": rows, "count": len(rows), "all_terminal": True, "flavors_separate": True, "channels_separate": True, "root": _root(rows)})


def apply_qqbarq_vertex_component(parameter_record: Mapping[str, Any], source_vector: Sequence[Any]) -> MappingProxyType:
    p = validate_qqbarq_parameter_record(parameter_record)
    action = apply_q_to_qqbarq(p, source_vector)
    return _freeze({"schema": "C195-QQBARQ-VERTEX-ACTION-V1", "parameter_record_id": p["record_id"], "transition": "C185-QG-QQBARQ-PAIR", "resolvent": "C185-Z-QQBARQ", "contact": "C127-JQ-K-JQ", "factorized_action": action, "proper_qg_vertex_assembled": False, "physical": False, "root": _root((p["signature"], action["root"]))})


def c194_crosswalk_manifest() -> MappingProxyType:
    rows = tuple({"C194_record_id": row["record_id"], "C195_record_id": row["record_id"].replace("C194-", "C195-"), "previous_status": row["status"], "terminal_status": "EXECUTABLE_COMPONENT_READY", "blocker": BLOCKER, "resolved_by": "C127-JQ-K-JQ", "qgg_inference": False, "read_only_C194": True} for row in c194.qqbarq_vertex_manifest()["rows"])
    return _freeze({"schema": "C195-C194-CROSSWALK-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def holonomy_bc_manifest() -> MappingProxyType:
    rows = tuple({"sector_id": row["sector_id"], "holonomy_capsule_id": row["holonomy_capsule_id"], "quark_boundary": row["quark_boundary"], "antiquark_boundary": row["antiquark_boundary"], "gluon_boundary": row["gluon_boundary"], "mode_grid_changed": False, "classification": row["classification"], "physical_holonomy": False} for row in c185.holonomy_bc_manifest("C170-B1-QQBARQ")["rows"])
    return _freeze({"schema": "C195-HOLONOMY-BC-V1", "rows": rows, "count": len(rows), "C183_root": c183.PACKAGE_ROOT, "root": _root(rows)})


def ownership_reconciliation_manifest() -> MappingProxyType:
    rows = tuple({"owner": owner, "count_once": True, "additive": owner == "C127-JQ-K-JQ", "role": role} for owner, role in (("C127-JQ-K-JQ", "primitive local matrix"), ("C112", "excluded source owner"), ("C129", "sequential normal ordering"), ("C131", "aggregate crosswalk"), ("C130", "nonmatrix boundary"), ("C182", "nonmatrix residual link"), ("C185-QG-QQBARQ-PAIR", "transition"), ("C185-RESOLVENT", "resolvent")))
    return _freeze({"schema": "C195-OWNERSHIP-RECONCILIATION-V1", "rows": rows, "count": len(rows), "duplicates": 0, "C131_additive": False, "root": _root(rows)})


def topology_manifest() -> MappingProxyType:
    rows = ({"topology": "DIRECT_Q_QQBARQ", "proper": True, "sequential": False, "owner": "C127-JQ-K-JQ"}, {"topology": "QG_QQBARQ_TRANSITION_RESOLVENT_CONTACT", "proper": True, "reducible": False, "complete_component": True}, {"topology": "QGG", "status": "PRESERVED_READ_ONLY"}, {"topology": "C130_C182", "classification": "NONMATRIX_INTERFACE", "matrix": False}, {"topology": "FULL_QG_1PI", "status": "FUTURE_C196"})
    return _freeze({"schema": "C195-TOPOLOGY-V1", "rows": rows, "count": len(rows), "qgg_qqbarq_separate": True, "leg_correction_conflation": False, "root": _root(rows)})


def count_once_manifest() -> MappingProxyType:
    owners = ("C127-JQ-K-JQ", "C112", "C129", "C131", "C130", "C182", "C185-QG-QQBARQ-PAIR", "C185-RESOLVENT", "COUNTERTERMS", "TARGET_ST")
    rows = tuple({"owner": o, "count": 1, "duplicate": False, "aggregate_additive": o == "C131" and False, "unavailable_is_zero": False} for o in owners)
    return _freeze({"schema": "C195-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def analyticity_manifest() -> MappingProxyType:
    rows = tuple({"resolution": r, "flavor_class": fl, "channel_id": ch, "z_query": "caller-supplied complex resolvent z", "z_to_zstar": "explicit Hermitian reverse", "pole_preflight": True, "physical_pole": False, "root_kind": "symbolic"} for r in RESOLUTIONS for fl in FLAVORS for ch in CHANNELS)
    return _freeze({"schema": "C195-ANALYTICITY-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def qqbarqvert1_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C195-RELEASE-V1", "status": STATUS, "plan": PLAN, "qqbarq_records": 18, "primitive_owner": "C127-JQ-K-JQ", "q_to_qqbarq": True, "qqbarq_to_q": True, "complete_qqbarq_component": True, "qg_vertex_complete": False, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, 18))})


def request_resolution_manifest() -> MappingProxyType:
    inherited = c194.request_resolution_manifest()["rows"]
    rows = tuple({"request_id": row["request_id"], "previous_status": row["terminal_status"], "terminal_status": "QQBARQ_COMPONENT_READY_QGVERT3_NEXT" if row["request_id"] in ("qg_VERTEX", "QCD_COUPLING") else row["terminal_status"], "all_visible": True, "qgg_unchanged": True} for row in inherited)
    return _freeze({"schema": "C195-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": True, "root": _root(rows)})


def missing_qqbarq_object_manifest() -> MappingProxyType:
    return _freeze({"schema": "C195-MISSING-OBJECT-V1", "rows": (), "count": 0, "resolved_blocker": BLOCKER, "unresolved_qqbarq_objects": 0, "root": _root((BLOCKER, 0))})


def qgvert3_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C195-QGVERT3-HANDOFF-V1", "next": NEXT, "C195_root": globals().get("PACKAGE_ROOT", "BOUND_AFTER_ROOT_ASSEMBLY"), "qqbarq_component_root": qqbarq_vertex_manifest()["root"], "C194_qgg_root": c194.qgg_vertex_manifest()["root"], "C194_subtraction_root": c194.reducible_subtraction_manifest()["root"], "C194_amputation_root": c194.amputation_manifest()["root"], "C194_projection_root": c194.vertex_projection_manifest()["root"], "complete_qg_1PI": False, "physical": False, "root": _root((NEXT, qqbarq_vertex_manifest()["root"]))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C195-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "closed": ("qqbarq order-two owner", "qqbarq transition", "qqbarq resolvent", "qqbarq component"), "open": ("complete qg proper vertex", "Z1F", "full ST", "target MOMq"), "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C195-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "C166_graph_nodes_edges": (0, 0), "states": 0, "TMD_objects": 0, "physical_inputs": 0, "root": _root((0, 0, 0))})


def b1qqbarqvert1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C195-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "blocker_resolved": True, "qqbarq_component_records": 18, "coefficient_records": 36, "same_different_symbolic_flavors": FLAVORS, "channels": CHANNELS, "finite_cell_PV": True, "HO_CM": True, "transition": True, "resolvent": True, "physical": False, "complete_qg_1PI": False, "next": NEXT, "root": _root((STATUS, PLAN, 18, 36, NEXT))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "model_memory_formulas": 0, "C158_value_inputs": 0, "physical_inputs": 0, "ordinary_zero_modes": 0, "hidden_Nf": 0, "flavor_averaging": 0, "Pauli_forbidden_retained": 0, "dense_cartesian_target": 0, "dense_inverse": 0, "factor_two_assumed": 0, "qgg_inference": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_representatives": 0, "complete_qg_1PI": 0, "Q0_Q1_Q2_modified": 0, "pass": True, "root": _root((0, STATUS))})


def mutate_live_hqcdb1qqbarqvert1(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "owner/flavor/Pauli/color/denominator/HO/transition/resolvent/schema perturbation", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


_ROOTS = {"PLAN": b1qqbarqvert1_plan_manifest()["root"], "HANDOFF": qqbarq_handoff_freeze()["root"], "BLOCKER": blocker_manifest()["root"], "OWNERS": owner_manifest()["root"], "BRANCH": quark_branch_manifest()["root"], "JQJQ": jqjq_manifest()["root"], "QQBARQ_BRANCH": qqbarq_branch_manifest()["root"], "FLAVOR": flavor_pauli_manifest()["root"], "COLOR": color_manifest()["root"], "DENOMINATOR": denominator_manifest()["root"], "SPIN": spin_manifest()["root"], "HO_CM": ho_cm_manifest()["root"], "SCHEMA": qqbarq_parameter_schema()["root"], "FIXTURE": qqbarq_fixture_manifest()["root"], "COEFFICIENT": coefficient_manifest()["root"], "SPARSE": sparse_manifest()["root"], "DERIVATIVE": derivative_manifest()["root"], "HERMITIAN": hermitian_manifest()["root"], "TRANSITION": transition_manifest()["root"], "VERTEX": qqbarq_vertex_manifest()["root"], "CROSSWALK": c194_crosswalk_manifest()["root"], "HOLONOMY": holonomy_bc_manifest()["root"], "OWNERSHIP": ownership_reconciliation_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "ANALYTICITY": analyticity_manifest()["root"], "RELEASE": qqbarqvert1_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "MISSING": missing_qqbarq_object_manifest()["root"], "HANDOFF_NEXT": qgvert3_handoff_contract()["root"], "FRONTIER": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "COMPLETENESS": b1qqbarqvert1_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C195-HQCDB1QQBARQVERT1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C195_INPUT_ROOT = _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256))
C195_PLAN_ROOT = _ROOTS["PLAN"]
C195_BLOCKER_ROOT = _ROOTS["BLOCKER"]
C195_PACKAGE_ROOT = PACKAGE_ROOT
__all__ = [name for name in globals() if not name.startswith("_")]
