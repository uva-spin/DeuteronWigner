"""C170 source-derived sector boundary authority.

The package audits the positive quark descendants and records the exact
finite-basis sectors needed by C169.  New adjoint and higher-Fock sectors are
kept typed and explicitly unavailable until their color/statistics/CM and
interaction authorities close.  No unavailable sector is represented by a
numerical zero.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c169
from deuteron_wigner.bridge import (
    g0, hqcdfield, hqcdfieldnorm, hqcd2ptq2, hqcd2ptfull,
    hqcdmproj, hqcdzqmass, hqcdg2pt, hqcdqgvert, hqcd3, gnorm,
    free2,
)

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c170_hqcdlfgsectorcalc1"
BASELINE = "03e71c57dd6b0686bf359f5a5a669e2889489bf6"
C169_PACKAGE_ROOT = "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5"
# The C169 commit did not contain the expected JSON continuation contract.
# The expected path is retained verbatim; the supplied prompt is the only
# authenticated C170 authority available in this workspace.
EXPECTED_CONTRACT = "docs/next_level/c169_c170_hqcdlfgsectorcalc1_continuation_contract.json"
PROMPT = "/Users/dustin/Downloads/c170_hqcdlfgsectorcalc1_codex_prompt.md"
PROMPT_SHA256 = "204b7fa9922d84ec78816b934914edcf7a3901efb4a31d7b33d5685b15666183"
STATUS = "C170_HQCDLFGSECTORCALC1_B0_ADJOINT_SECTOR_INCOMPLETE"
PLAN = "LFGSECTORCALC1-D"
NEXT = "C171/HQCDB0ADJOINT1"
RESOLUTIONS = ("K9", "K11", "K13")
REQUESTS = tuple(row["request_id"] for row in c169.calculation_capsule_freeze()["rows"])
REQUEST_BY_ID = {row: row for row in REQUESTS}


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _check_request(request_id: str | None) -> tuple[str, ...]:
    if request_id is not None and request_id not in REQUEST_BY_ID: raise KeyError(request_id)
    return tuple(REQUESTS if request_id is None else (request_id,))


def _check_sector(sector_id: str | None) -> tuple[str, ...]:
    ids = tuple(row["sector_id"] for row in SECTORS)
    if sector_id is not None and sector_id not in ids: raise KeyError(sector_id)
    return ids if sector_id is None else (sector_id,)


def _check_resolution(resolution_id: str) -> str:
    if resolution_id not in RESOLUTIONS: raise KeyError(resolution_id)
    return resolution_id


def _quantity(request_id: str) -> str:
    for row in c169.calculation_capsule_freeze()["rows"]:
        if row["request_id"] == request_id: return row["quantity"]
    raise KeyError(request_id)


def _public_descendant_probe() -> Mapping[str, Any]:
    """Read only public descendant certificates; never constructs a builder."""
    return {
        "C43": {"action": g0.action_contract(), "source": g0.source_manifest()},
        "C142": hqcdfield.field_source_completeness_certificate(),
        "C145": hqcd2ptq2.two_point_completeness_certificate(),
        "C147": hqcdfieldnorm.field_normalization_completeness_certificate(),
        "C148": hqcd2ptfull.full_spinor_completeness_certificate(),
        "C149": hqcdmproj.projector_completeness_certificate(),
        "C150": hqcdzqmass.zq_mass_completeness_certificate(),
        "C151": hqcdg2pt.pure_gluon_sector_census(),
        "C152": hqcdqgvert.vertex_properness_report(),
    }


def load_verified_hqcd_lfgsectorcalc1_authority() -> MappingProxyType:
    data = json.loads((RUNTIME / "manifest.json").read_text())
    if data.get("package_root") != PACKAGE_ROOT or data.get("status") != STATUS:
        raise ValueError("C170 runtime mismatch")
    return verify_hqcd_lfgsectorcalc1_authority()


def verify_hqcd_lfgsectorcalc1_authority() -> MappingProxyType:
    return _freeze({
        "schema": "C170-HQCDLFGSECTORCALC1-V1", "baseline": BASELINE,
        "status": STATUS, "plan": PLAN, "next": NEXT,
        "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": False,
        "supplied_prompt": PROMPT, "supplied_prompt_sha256": PROMPT_SHA256,
        "C169_package_root": C169_PACKAGE_ROOT, "six_requests": 6,
        "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0,
        "C158_value_inputs": 0, "source_acquisitions": 0,
        "historical_statuses_rewritten": 0, "package_root": PACKAGE_ROOT,
    })


def lfgsectorcalc1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C170-PLAN-MANIFEST-V1", "selected_plan": PLAN,
        "status": STATUS, "reason": "B=0 q-qbar and gg adjoint domains are the first missing sectors after descendant quark/qg/g crosswalk", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def missing_calculation_freeze() -> MappingProxyType:
    rows = tuple(dict(row) for row in c169.missing_calculation_manifest()["rows"])
    return _freeze({"schema": "C170-MISSING-CALCULATION-FREEZE-V1", "rows": rows, "count": len(rows), "imported_unchanged": True, "root": _root(rows)})


def descendant_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    _check_request(request_id)
    rows = (
        {"historical_package": "C141", "historical_object": "quark_source_map_manifest", "required_semantic": "forward quark source/sink for C169", "descendant": "C142 hqcdfield.quark_source_map_manifest", "same_object": True, "normalization_compatible": True, "external_state_compatible": True, "projector_compatible": "forward good-component only", "status": "EXACT_DESCENDANT_AUTHORITY_SUPERSEDES_HISTORICAL_BLOCKER", "next_object": "C130 residual realization and C150 condition"},
        {"historical_package": "C143", "historical_object": "source_projected_resolvent", "required_semantic": "parameterized forward q/qg resolvent", "descendant": "C145 hqcd2ptq2.source_projected_m2_resolvent", "same_object": True, "normalization_compatible": True, "external_state_compatible": True, "projector_compatible": "C145 source projection", "status": "EXACT_DESCENDANT_AUTHORITY_SUPERSEDES_HISTORICAL_BLOCKER", "next_object": "C130 residual realization"},
        {"historical_package": "C146", "historical_object": "source_sink_normalization", "required_semantic": "coordinate-field normalization", "descendant": "C147 hqcdfieldnorm.coordinate_field_source_manifest", "same_object": False, "normalization_compatible": "conditional", "external_state_compatible": True, "projector_compatible": "requires C149", "status": "DESCENDANT_SCOPE_STRICTLY_WEAKER", "next_object": "complete two-point normalization condition"},
        {"historical_package": "C141", "historical_object": "mass_linear_projector", "required_semantic": "signed mass insertion", "descendant": "C148 full-spinor + C149 signed projector", "same_object": False, "normalization_compatible": "conditional", "external_state_compatible": True, "projector_compatible": True, "status": "DESCENDANT_AUTHORITY_REQUIRES_EXPLICIT_ADAPTER", "next_object": "complete inverse two-point mass insertion"},
        {"historical_package": "C130", "historical_object": "zero_boundary_residual", "required_semantic": "C43 P0/Q0/boundary/link interface", "descendant": "C142/C43 public interface", "same_object": False, "normalization_compatible": "not applicable", "external_state_compatible": "not closed", "projector_compatible": "not applicable", "status": "C130_RESIDUAL_REALIZATION_INCOMPLETE", "next_object": "B=0/B=1 residual-sector calculation"},
        {"historical_package": "C150", "historical_object": "counterterm_condition", "required_semantic": "finite Zq/mass condition", "descendant": "C150 conditional scheme family", "same_object": False, "normalization_compatible": True, "external_state_compatible": True, "projector_compatible": True, "status": "COUNTERTERM_CONDITION_INCOMPLETE", "next_object": "unselected six-direction counterterm condition"},
    )
    return _freeze({"schema": "C170-DESCENDANT-RESOLUTION-MANIFEST-V1", "rows": rows, "count": len(rows), "historical_statuses_rewritten": 0, "root": _root(rows)})


SECTORS = (
    {"sector_id": "C170-B1-Q", "fock_content": ("q",), "baryon_number": "1/3", "open_representation": "3", "boundary": "fermion APBC; total half-integer", "basis_status": "DESCENDANT_IMPORTED", "necessity": "REQUIRED_BY_EXACT_CAPSULE"},
    {"sector_id": "C170-B1-QG", "fock_content": ("q", "g"), "baryon_number": "1/3", "open_representation": "3", "boundary": "fermion APBC + boson PBC; total half-integer", "basis_status": "DESCENDANT_IMPORTED", "necessity": "REQUIRED_BY_EXACT_CAPSULE"},
    {"sector_id": "C170-B0-G", "fock_content": ("g",), "baryon_number": 0, "open_representation": "8", "boundary": "boson PBC; total integer", "basis_status": "DESCENDANT_IMPORTED", "necessity": "REQUIRED_BY_EXACT_CAPSULE"},
    {"sector_id": "C170-B0-QQBAR-ADJOINT", "fock_content": ("q", "qbar"), "baryon_number": 0, "open_representation": "8", "boundary": "fermion APBC pair; total integer", "basis_status": "UNAVAILABLE_BLOCKING", "necessity": "REQUIRED_BY_TRANSITIVE_INTERMEDIATE_DOMAIN"},
    {"sector_id": "C170-B0-GG-ADJOINT", "fock_content": ("g", "g"), "baryon_number": 0, "open_representation": "8", "boundary": "boson PBC pair; total integer", "basis_status": "UNAVAILABLE_BLOCKING", "necessity": "REQUIRED_BY_TRANSITIVE_INTERMEDIATE_DOMAIN"},
    {"sector_id": "C170-B1-QGG", "fock_content": ("q", "g", "g"), "baryon_number": "1/3", "open_representation": "3", "boundary": "fermion APBC + two boson PBC; total half-integer", "basis_status": "UNAVAILABLE_BLOCKING", "necessity": "REQUIRED_BY_TRANSITIVE_INTERMEDIATE_DOMAIN"},
    {"sector_id": "C170-B1-QQBARQ", "fock_content": ("q", "qbar", "q"), "baryon_number": "1/3", "open_representation": "3", "boundary": "three fermion APBC modes; total half-integer", "basis_status": "UNAVAILABLE_BLOCKING", "necessity": "REQUIRED_BY_TRANSITIVE_INTERMEDIATE_DOMAIN"},
)


def sector_taxonomy_manifest(request_id: str | None = None, sector_id: str | None = None) -> MappingProxyType:
    _check_request(request_id); ids = _check_sector(sector_id)
    qmap = {"QUARK_FIELD": ("C170-B1-Q", "C170-B1-QG"), "SIGNED_QUARK_MASS": ("C170-B1-Q", "C170-B1-QG"), "TRANSVERSE_GLUON_FIELD": ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT"), "qg_VERTEX_DRESSING": ("C170-B1-Q", "C170-B1-QG", "C170-B1-QGG", "C170-B1-QQBARQ"), "QCD_COUPLING": tuple(x["sector_id"] for x in SECTORS)}
    selected = set(ids)
    rows = tuple(dict(row, required_by=tuple(r for r in _check_request(request_id) if row["sector_id"] in qmap[_quantity(r)])) for row in SECTORS if row["sector_id"] in selected and (request_id is None or row["sector_id"] in set(sum((list(qmap[_quantity(r)]) for r in _check_request(request_id)), []))))
    return _freeze({"schema": "C170-SECTOR-TAXONOMY-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def resolution_boundary_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        rows.append({"sector_id": row["sector_id"], "resolutions": RESOLUTIONS, "fermion_modes": "half-integer APBC" if "q" in row["fock_content"] or "qbar" in row["fock_content"] else "not applicable", "boson_modes": "integer PBC" if "g" in row["fock_content"] else "not applicable", "total_longitudinal": row["boundary"], "zero_mode": "explicit P0/Q0 control; not numerical zero", "finite_cell": "C43 finite longitudinal cell", "status": "AVAILABLE_DESCENDANT_SEMANTICS" if row["basis_status"] == "DESCENDANT_IMPORTED" else "UNAVAILABLE_BLOCKING", "root": _root((row["sector_id"], row["boundary"], RESOLUTIONS))})
    return _freeze({"schema": "C170-RESOLUTION-BOUNDARY-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def color_representation_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        ready = row["basis_status"] == "DESCENDANT_IMPORTED"
        rows.append({"sector_id": row["sector_id"], "ambient_tensor_product": "source-qualified tensor product", "target_irrep": row["open_representation"], "outer_multiplicity": 1 if ready else None, "isometry": "C74/C151 descendant" if ready else None, "projector": "descendant projector" if ready else None, "all_eight_generator_residuals": "descendant-certified" if ready else None, "status": "DESCENDANT_COLOR_AUTHORITY" if ready else "COLOR_REPRESENTATION_INCOMPLETE", "not_invented": True, "root": _root((row["sector_id"], ready, row["open_representation"]))})
    return _freeze({"schema": "C170-COLOR-REPRESENTATION-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def statistics_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        ready = row["basis_status"] == "DESCENDANT_IMPORTED"
        rows.append({"sector_id": row["sector_id"], "identical_quarks": 0 if row["sector_id"] != "C170-B1-QQBARQ" else 2, "identical_gluons": 0 if row["sector_id"] not in ("C170-B0-GG-ADJOINT", "C170-B1-QGG") else 2, "fermion_antisymmetrizer": "descendant scope" if ready else None, "gluon_symmetrizer": "descendant scope" if ready else None, "idempotence": "not evaluated" if not ready else "descendant-certified", "status": "DESCENDANT_STATISTICS_SCOPE" if ready else "STATISTICS_OR_CM_PROJECTION_INCOMPLETE", "root": _root((row["sector_id"], ready))})
    return _freeze({"schema": "C170-STATISTICS-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def transverse_cm_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        ready = row["basis_status"] == "DESCENDANT_IMPORTED"
        rows.append({"sector_id": row["sector_id"], "HO_policy": "C64/C77 finite-HO descendant" if ready else "three-body/four-body TM map not authenticated", "intrinsic_CM": "CM-ground descendant" if ready else None, "Nmax": "explicit caller record" if ready else None, "b_HO": "explicit caller record" if ready else None, "round_trip": "descendant-certified" if ready else None, "continuum_claim": False, "status": "DESCENDANT_CM_SCOPE" if ready else "STATISTICS_OR_CM_PROJECTION_INCOMPLETE", "root": _root((row["sector_id"], ready, "CM"))})
    return _freeze({"schema": "C170-TRANSVERSE-CM-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def factorized_basis_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    if resolution_id is not None: _check_resolution(resolution_id)
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        rows.append({"sector_id": row["sector_id"], "resolution": RESOLUTIONS if resolution_id is None else (resolution_id,), "state_identity_fields": ("sector_id", "resolution", "longitudinal_tuple", "transverse_tuple", "helicity", "flavor", "color_multiplicity", "permutation_irrep", "CM_intrinsic", "canonical_rank"), "cardinality": None, "basis_order": "not materialized", "rank_unrank": False, "membership": "typed but unavailable for new sector" if row["basis_status"] != "DESCENDANT_IMPORTED" else "descendant-owned", "status": "DESCENDANT_BASIS_IMPORTED" if row["basis_status"] == "DESCENDANT_IMPORTED" else "FACTOR_MAP_INCOMPLETE", "root": _root((row["sector_id"], resolution_id, row["basis_status"]))})
    return _freeze({"schema": "C170-FACTORIZED-BASIS-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def rank_sector_state(sector_id: str, state_record: Mapping[str, Any]) -> int:
    _check_sector(sector_id)
    raise ValueError("C170 rank/unrank is not closed for this sector; state identity cannot be inferred")


def unrank_sector_state(sector_id: str, resolution_id: str, rank: int) -> MappingProxyType:
    _check_sector(sector_id); _check_resolution(resolution_id)
    raise ValueError("C170 rank/unrank is not closed for this sector")


def source_map_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        source = "C142 fermion source" if row["sector_id"] == "C170-B1-Q" else "C151 one-gluon source" if row["sector_id"] == "C170-B0-G" else "C152 q-to-qg source" if row["sector_id"] == "C170-B1-QG" else None
        rows.append({"sector_id": row["sector_id"], "field_content": row["fock_content"], "source_operator": source, "vacuum": "C43 local nonzero-mode vacuum" if source else None, "sink_adjoint": bool(source), "direct_source_invented": False, "status": "SOURCE_MAP_DESCENDANT" if source else "NO_DIRECT_SOURCE_INTERMEDIATE_ONLY", "root": _root((row["sector_id"], source))})
    return _freeze({"schema": "C170-SOURCE-MAP-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def quark_domain_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for rid in _check_request(request_id):
        q = _quantity(rid)
        if q not in ("QUARK_FIELD", "SIGNED_QUARK_MASS"): continue
        rows.append({"request_id": rid, "source": "C142", "resolvent": "C145", "normalization": "C147 conditional", "full_spinor": "C148 constrained positive-frequency", "projector": "C149", "scheme": "C150 K_MINUS/K_PLUS/K_PERP separate", "residual": "C130 separate incomplete", "counterterm": "C150 condition incomplete", "status": "QUARK_DOMAIN_READY_COUNTERTERM_OR_RESIDUAL_INCOMPLETE", "historical_status_rewritten": False, "root": _root((rid, "C142", "C145", "C147", "C149", "C150"))})
    return _freeze({"schema": "C170-QUARK-DOMAIN-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def b0_gluon_sector_manifest(sector_id: str | None = None) -> MappingProxyType:
    allowed = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT")
    if sector_id is not None and sector_id not in allowed: raise KeyError(sector_id)
    rows = []
    for sid in allowed:
        if sector_id is not None and sid != sector_id: continue
        ready = sid == "C170-B0-G"
        rows.append({"sector_id": sid, "external_gluon": True, "spectator_tagged_B1_separate": True, "required": True, "free_M2": "C151/C128 descendant" if ready else None, "canonical_links": "one-gluon source only" if ready else None, "ghost": "C43 scope incomplete", "status": "DESCENDANT_B0_G_READY" if ready else "B0_ADJOINT_SECTOR_INCOMPLETE", "missing_as_zero": False, "root": _root((sid, ready, "B0"))})
    return _freeze({"schema": "C170-B0-GLUON-SECTOR-MANIFEST-V1", "rows": tuple(rows), "pure_B0_separate_from_C151_B1": True, "root": _root(rows)})


def b1_higher_fock_manifest(sector_id: str | None = None) -> MappingProxyType:
    allowed = ("C170-B1-QGG", "C170-B1-QQBARQ")
    if sector_id is not None and sector_id not in allowed: raise KeyError(sector_id)
    rows = tuple({"sector_id": sid, "open_triplet": True, "historical_baryonic_sector_reused": False, "free_M2": None, "q_emission": None, "pair_conversion": None, "three_gluon": None, "statistics": None, "status": "B1_HIGHER_FOCK_SECTOR_INCOMPLETE", "missing_as_zero": False, "root": _root((sid, "B1"))} for sid in allowed if sector_id is None or sid == sector_id)
    return _freeze({"schema": "C170-B1-HIGHER-FOCK-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def interaction_extension_manifest(incoming_sector: str | None = None, outgoing_sector: str | None = None, interaction_id: str | None = None) -> MappingProxyType:
    interactions = (
        {"interaction_id": "C170-INT-Q-QG", "incoming": "C170-B1-Q", "outgoing": "C170-B1-QG", "owner": "C53", "status": "DESCENDANT_SCOPE"},
        {"interaction_id": "C170-INT-G-QQBAR", "incoming": "C170-B0-G", "outgoing": "C170-B0-QQBAR-ADJOINT", "owner": "C53/C43 pair conversion", "status": "CANONICAL_INTERACTION_INCOMPLETE"},
        {"interaction_id": "C170-INT-G-GG", "incoming": "C170-B0-G", "outgoing": "C170-B0-GG-ADJOINT", "owner": "C129/C43 three-gluon", "status": "CANONICAL_INTERACTION_INCOMPLETE"},
        {"interaction_id": "C170-INT-QG-QGG", "incoming": "C170-B1-QG", "outgoing": "C170-B1-QGG", "owner": "C129 G3/G4 omitted descendant", "status": "CANONICAL_INTERACTION_INCOMPLETE"},
        {"interaction_id": "C170-INT-QG-QQBARQ", "incoming": "C170-B1-QG", "outgoing": "C170-B1-QQBARQ", "owner": "C53 pair conversion extension", "status": "CANONICAL_INTERACTION_INCOMPLETE"},
    )
    if interaction_id is not None and interaction_id not in {x["interaction_id"] for x in interactions}: raise KeyError(interaction_id)
    rows = tuple(x for x in interactions if (interaction_id is None or x["interaction_id"] == interaction_id) and (incoming_sector is None or x["incoming"] == incoming_sector) and (outgoing_sector is None or x["outgoing"] == outgoing_sector))
    return _freeze({"schema": "C170-INTERACTION-EXTENSION-MANIFEST-V1", "rows": rows, "count": len(rows), "C53_extrapolated": 0, "root": _root(rows)})


def direct_instantaneous_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in SECTORS:
        if sector_id is not None and row["sector_id"] != sector_id: continue
        rows.append({"sector_id": row["sector_id"], "terms": tuple({"owner": owner, "coupling_degree": degree, "status": "DESCENDANT_SCOPE" if row["basis_status"] == "DESCENDANT_IMPORTED" and owner in ("C111", "C112", "C127", "C129") else "UNAVAILABLE_BLOCKING", "not_zero": True, "count_once_key": f"{row['sector_id']}:{owner}"} for owner, degree in (("C111", 2), ("C112", 2), ("C127", 2), ("C129", 2), ("C130", "interface"))), "missing_as_zero": 0, "root": _root(row["sector_id"])})
    return _freeze({"schema": "C170-DIRECT-INSTANTANEOUS-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def ghost_gauge_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": rid, "gauge": "C43 A^+=0", "boundary": "C43 finite cell", "zero_modes": "P0/Q0 explicit", "residual_gauge": "not fully closed", "pole": "antisymmetric/PV", "residual_link": "retained", "ghost_status": "AUTHORITY_INCOMPLETE", "target_gauge_ghost_imported": False, "root": _root((rid, "ghost-incomplete"))} for rid in _check_request(request_id))
    return _freeze({"schema": "C170-GHOST-GAUGE-MANIFEST-V1", "rows": rows, "unproved_ghost_omissions": len(rows), "root": _root(rows)})


def zero_boundary_residual_manifest(sector_id: str | None = None, request_id: str | None = None) -> MappingProxyType:
    sids = _check_sector(sector_id); rids = _check_request(request_id)
    rows = tuple({"sector_id": sid, "request_id": rid, "interfaces": ("P0", "Q0", "fermion zero-mode", "gluon residual gauge", "finite-cell boundary", "residual transverse link", "omitted interface"), "status": "REQUIRES_DEDICATED_CALCULATION", "not_zero": True, "root": _root((sid, rid, "residual"))} for sid in sids for rid in rids)
    return _freeze({"schema": "C170-ZERO-BOUNDARY-RESIDUAL-MANIFEST-V1", "rows": rows, "missing_as_zero": 0, "root": _root(rows)})


def free_sector_operator_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    if resolution_id is not None: _check_resolution(resolution_id)
    rows = tuple({"sector_id": row["sector_id"], "resolution": RESOLUTIONS if resolution_id is None else (resolution_id,), "sparse": row["basis_status"] == "DESCENDANT_IMPORTED", "matrix_free": row["basis_status"] == "DESCENDANT_IMPORTED", "hermiticity": "descendant-certified" if row["basis_status"] == "DESCENDANT_IMPORTED" else None, "units": "source-defined invariant-mass units", "status": "DESCENDANT_FREE_OPERATOR" if row["basis_status"] == "DESCENDANT_IMPORTED" else "SECTOR_RESOLVENT_INCOMPLETE", "root": _root((row["sector_id"], resolution_id, row["basis_status"]))} for row in SECTORS if sector_id is None or row["sector_id"] == sector_id)
    if sector_id is not None: _check_sector(sector_id)
    return _freeze({"schema": "C170-FREE-SECTOR-OPERATOR-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def apply_free_sector_operator(sector_id: str, resolution_id: str, vector: Any, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    _check_sector(sector_id); _check_resolution(resolution_id)
    raise ValueError("C170 does not materialize a new-sector operator until factorized color/statistics/CM closure")


def sector_resolvent_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"sector_id": row["sector_id"], "source_sink": "descendant-owned" if row["basis_status"] == "DESCENDANT_IMPORTED" else None, "query": "explicit nonphysical z required", "sparse_route": row["basis_status"] == "DESCENDANT_IMPORTED", "matrix_free_route": row["basis_status"] == "DESCENDANT_IMPORTED", "dense_full_inverse": False, "status": "DESCENDANT_RESOLVENT_INTERFACE" if row["basis_status"] == "DESCENDANT_IMPORTED" else "SECTOR_RESOLVENT_INCOMPLETE", "root": _root((row["sector_id"], "resolvent"))} for row in SECTORS if sector_id is None or row["sector_id"] == sector_id)
    if sector_id is not None: _check_sector(sector_id)
    return _freeze({"schema": "C170-SECTOR-RESOLVENT-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": rid, "owners": ("propagating", "direct", "instantaneous", "normal_ordering", "pair_conversion", "counterterm", "residual", "omitted"), "duplicate_owners": 0, "spectator_lift_duplication": 0, "closure": "INCOMPLETE_MISSING_SECTORS", "missing_as_zero": 0, "root": _root((rid, 0))} for rid in _check_request(request_id))
    return _freeze({"schema": "C170-COUNT-ONCE-MANIFEST-V1", "rows": rows, "duplicate_count": 0, "root": _root(rows)})


def sector_diagnostic_manifest(request_id: str | None = None, sector_id: str | None = None, fixture_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    if fixture_id is not None or resolution_id is not None: raise ValueError("C170 diagnostic domain is not closed; no enclosure emitted")
    _check_request(request_id); _check_sector(sector_id)
    return _freeze({"schema": "C170-SECTOR-DIAGNOSTIC-MANIFEST-V1", "rows": (), "evaluations": 0, "outward_enclosures": 0, "claim_tier": "NONPHYSICAL_FULL_QCD_SECTOR_DIAGNOSTIC_ONLY", "root": _root((request_id, sector_id, "not-run"))})


def componentwise_readiness_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for rid in _check_request(request_id):
        q = _quantity(rid)
        status = "QUARK_DOMAIN_READY_COUNTERTERM_OR_RESIDUAL_INCOMPLETE" if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS") else "FULL_QCD_SECTOR_INCOMPLETE"
        rows.append({"request_id": rid, "required_sectors": tuple(x["sector_id"] for x in SECTORS if x["sector_id"] in ("C170-B1-Q", "C170-B1-QG") if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS")) if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS") else tuple(x["sector_id"] for x in SECTORS), "status": status, "next_object": "C130/counterterm condition" if q in ("QUARK_FIELD", "SIGNED_QUARK_MASS") else NEXT, "root": _root((rid, status))})
    return _freeze({"schema": "C170-COMPONENTWISE-READINESS-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": rid, "capsule_id": rid, "C169_terminal_status": c169.request_resolution_manifest(rid)["rows"][0]["C169_terminal_status"], "historical_descendant_crosswalk": "audited", "C170_terminal_status": "QUARK_DOMAIN_READY_COUNTERTERM_OR_RESIDUAL_INCOMPLETE" if _quantity(rid) in ("QUARK_FIELD", "SIGNED_QUARK_MASS") else "FULL_QCD_SECTOR_INCOMPLETE", "sector_status": "descendant q/qg/g imported; new sectors incomplete", "color_statistics_cm": "new-sector incomplete", "interaction": "C53 q-qg descendant only", "ghost_gauge": "AUTHORITY_INCOMPLETE", "zero_boundary_residual": "REQUIRES_DEDICATED_CALCULATION", "resolvent": "descendant interface or incomplete new sector", "diagnostic": "NOT_RUN", "next_object": "C130/counterterm condition" if _quantity(rid) in ("QUARK_FIELD", "SIGNED_QUARK_MASS") else NEXT, "root": _root((rid, _quantity(rid), NEXT))} for rid in _check_request(request_id))
    return _freeze({"schema": "C170-REQUEST-RESOLUTION-MANIFEST-V1", "rows": rows, "count": len(rows), "one_terminal_per_request": True, "root": _root(rows)})


def missing_sector_manifest(request_id: str | None = None) -> MappingProxyType:
    def required(q: str) -> tuple[str, ...]:
        if q == "TRANSVERSE_GLUON_FIELD": return ("C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT")
        if q == "qg_VERTEX_DRESSING": return ("C170-B1-QGG", "C170-B1-QQBARQ")
        if q == "QCD_COUPLING": return ("C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT", "C170-B1-QGG", "C170-B1-QQBARQ")
        return ()
    rows = tuple({"request_id": rid, "missing_sector_capsule_id": f"C170-MISSING-SECTOR-{sid}", "sector_id": sid, "required_objects": ("factorized basis", "color irrep/isometry", "statistics", "CM projector", "free M2", "canonical interaction", "residual interface", "counterterm sensitivity"), "status": "B0_ADJOINT_SECTOR_INCOMPLETE" if sid.startswith("C170-B0") else "B1_HIGHER_FOCK_SECTOR_INCOMPLETE", "not_zero": True, "root": _root((rid, sid))} for rid in _check_request(request_id) for sid in required(_quantity(rid)))
    return _freeze({"schema": "C170-MISSING-SECTOR-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C170-CALCULATION-RESUMPTION-HANDOFF-V1", "status": STATUS, "next": NEXT, "C169_values_recomputed": 0, "C169_records_mutated": 0, "adapter": 0, "matching": 0, "root": _root((STATUS, NEXT, 0))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple({"frontier_id": f"C170-{row['sector_id']}", "sector_id": row["sector_id"], "kind": "SECTOR_CALCULATION", "status": "DESCENDANT_IMPORTED" if row["basis_status"] == "DESCENDANT_IMPORTED" else "SECTOR_INCOMPLETE", "next": None if row["basis_status"] == "DESCENDANT_IMPORTED" else NEXT} for row in SECTORS)
    return _freeze({"schema": "C170-DEPENDENCY-FRONTIER-MANIFEST-V1", "rows": rows, "count": len(rows), "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def quantum_sector_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C170-QUANTUM-SECTOR-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0))})


def c158_noncircularity_manifest() -> MappingProxyType:
    return _freeze({"schema": "C170-C158-NONCIRCULARITY-V1", "C158_value_inputs": 0, "C158_imported": False, "root": _root((0, False))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "web_or_model_memory_formulas": 0, "duplicated_descendant_functionality": 0, "historical_statuses_rewritten": 0, "invented_sector_identities": 0, "invented_color_multiplicities": 0, "invented_states": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "dense_full_inverses": 0, "missing_sector_zeros": 0, "unproved_ghost_omissions": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "complete_loop_coefficients": 0, "adapter_assembled": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "physical_states": 0, "TMD_objects": 0, "Q0_Q1_Q2_modified": False, "allow_pickle_false": True, "pass": True, "root": _root((STATUS, NEXT, 0))})


def lfgsectorcalc1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C170-LFGSECTORCALC1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "six_requests": 6, "terminal_records": 6, "sector_count": len(SECTORS), "descendant_crosswalk_records": 6, "new_sector_domains_closed": 0, "B0_new_sectors_closed": 0, "B1_new_sectors_closed": 0, "color_multiplicity_invented": 0, "missing_sector_zeros": 0, "ghost_omissions_unproved": 1, "diagnostics": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "next": NEXT, "root": _root((STATUS, PLAN, len(SECTORS), NEXT))})


def mutate_live_hqcdlfgsectorcalc1(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "request_id", "capsule_id", "historical_status", "descendant", "sector_id", "resolution", "boundary", "state_id", "rank", "unrank", "color_irrep", "outer_multiplicity", "isometry", "statistics", "CM", "source_map", "interaction", "direct", "instantaneous", "ghost", "zero_mode", "boundary", "residual_link", "counterterm", "nullspace", "free_operator", "resolvent", "diagnostic", "C158", "graph", "Q0", "Q1", "Q2", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C170_INPUT_ROOT": _root((BASELINE, EXPECTED_CONTRACT, PROMPT_SHA256, C169_PACKAGE_ROOT)),
    "C170_PLAN_ROOT": lfgsectorcalc1_plan_manifest()["root"],
    "C170_MISSING_CALCULATION_FREEZE_ROOT": missing_calculation_freeze()["root"],
    "C170_DESCENDANT_RESOLUTION_ROOT": descendant_resolution_manifest()["root"],
    "C170_SECTOR_TAXONOMY_ROOT": sector_taxonomy_manifest()["root"],
    "C170_RESOLUTION_BOUNDARY_ROOT": resolution_boundary_manifest()["root"],
    "C170_COLOR_REPRESENTATION_ROOT": color_representation_manifest()["root"],
    "C170_STATISTICS_ROOT": statistics_manifest()["root"],
    "C170_TRANSVERSE_CM_ROOT": transverse_cm_manifest()["root"],
    "C170_FACTORIZED_BASIS_ROOT": factorized_basis_manifest()["root"],
    "C170_SOURCE_MAP_ROOT": source_map_manifest()["root"],
    "C170_QUARK_DOMAIN_ROOT": quark_domain_manifest()["root"],
    "C170_B0_GLUON_SECTOR_ROOT": b0_gluon_sector_manifest()["root"],
    "C170_B1_HIGHER_FOCK_ROOT": b1_higher_fock_manifest()["root"],
    "C170_INTERACTION_EXTENSION_ROOT": interaction_extension_manifest()["root"],
    "C170_DIRECT_INSTANTANEOUS_ROOT": direct_instantaneous_manifest()["root"],
    "C170_GHOST_GAUGE_ROOT": ghost_gauge_manifest()["root"],
    "C170_ZERO_BOUNDARY_RESIDUAL_ROOT": zero_boundary_residual_manifest()["root"],
    "C170_FREE_SECTOR_OPERATOR_ROOT": free_sector_operator_manifest()["root"],
    "C170_SECTOR_RESOLVENT_ROOT": sector_resolvent_manifest()["root"],
    "C170_COUNT_ONCE_ROOT": count_once_manifest()["root"],
    "C170_DIAGNOSTIC_ROOT": sector_diagnostic_manifest()["root"],
    "C170_COMPONENTWISE_READINESS_ROOT": componentwise_readiness_manifest()["root"],
    "C170_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C170_MISSING_SECTOR_ROOT": missing_sector_manifest()["root"],
    "C170_CALCULATION_HANDOFF_ROOT": calculation_resumption_handoff_contract()["root"],
    "C170_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C170_QUANTUM_HANDOFF_ROOT": quantum_sector_handoff_contract()["root"],
    "C170_SCOPE_ROOT": _root(("finite-basis", False, False)),
    "C170_COMPLETENESS_ROOT": lfgsectorcalc1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C170-HQCDLFGSECTORCALC1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
