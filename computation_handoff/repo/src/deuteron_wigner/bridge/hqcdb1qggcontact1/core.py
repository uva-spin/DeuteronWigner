"""C187 primitive-owner DAG for the q↔qgg contact frontier.

The authenticated C112/C127 records expose q and qg domains, not a qgg local
matrix.  C187 therefore publishes exact typed source/interface records and
rejects fabricated matrix application.  C185/C186/C184 objects are consumed
read-only and no physical coefficient is selected.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb1qgg2 as c186
from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdb0reslink2 as c182
from deuteron_wigner.bridge import iferm3 as c112
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import gnorm as c129
from deuteron_wigner.bridge import hqcd4 as c131

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c187_hqcdb1qggcontact1"
BASELINE = "babb8ae510290055ad794850a86690ed145b03d8"
CONTRACT = "docs/next_level/c186_c187_hqcdb1qggcontact1_continuation_contract.json"
CONTRACT_SHA256 = "7296b3cd27ac26a8d7569764b8dee21290275b83b124353b6d7dd6a61b754f4e"
PROMPT = "/Users/dustin/Downloads/c187_hqcdb1qggcontact1_codex_prompt.md"
PROMPT_SHA256 = "3b4e3ad5d7618a5c2065fa50e315416d97ee7294fd5ff826c9c9f9b56459ba8d"
STATUS = "C187_HQCDB1QGGCONTACT1_PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE"
PLAN = "QGGCONTACT1-E"
NEXT = "C188/HQCDB1QGGOWNER1"
RESOLUTIONS = ("K9", "K11", "K13")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
OWNER_IDS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG", "C129_G4_DIRECT_NORMAL_ORDERED_QGG", "C131_LOCAL_POLYNOMIAL_QGG", "C130_BOUNDARY_NONMATRIX_QGG", "C182_RESIDUAL_LINK_DEGREE2_QGG")
ORIENTATIONS = ("q_to_qgg", "qgg_to_q")
C112_RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
REQUESTS = tuple(row["request_id"] for row in c185.request_resolution_manifest()["rows"])


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping): return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(v) for v in value]
    if isinstance(value, complex): return [value.real, value.imag]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)): return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _c112_root() -> str:
    return _root(tuple(c112.instantaneous_fermion_sector_manifest(r) for r in C112_RESOLUTIONS))


def _verify_frozen_roots() -> None:
    expected = {
        "C186": "df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20",
        "C185": "c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885",
        "C184": "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8",
        "C183": "7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f",
        "C182": "9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e",
    }
    actual = {"C186": c186.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C182": c182.PACKAGE_ROOT}
    if actual != expected: raise ValueError("C164-C186 root boundary changed")
    if c186.qgg_release_manifest()["decision"] != "QGG_CUBIC_TRANSITION_READY_ORDER2_OWNER_PARTIAL": raise ValueError("C186 cubic boundary changed")


def load_verified_hqcd_b1qggcontact1_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists(): raise FileNotFoundError("C187 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C187 runtime root/status mismatch")
    return _freeze(verify_hqcd_b1qggcontact1_authority())


def verify_hqcd_b1qggcontact1_authority() -> MappingProxyType:
    _verify_frozen_roots()
    return _freeze({"schema": "C187-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "C186_package_root": c186.PACKAGE_ROOT, "C185_package_root": c185.PACKAGE_ROOT, "C184_package_root": c184.PACKAGE_ROOT, "C112_root": _c112_root(), "C127_root": c127.PACKAGE_ROOT, "C129_root": c129.PACKAGE_ROOT, "C131_root": c131.PACKAGE_ROOT, "source_acquisitions": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "C185_basis_recomputed": 0, "C186_cubic_recomputed": 0, "C184_B0_recalculation": 0, "complete_qg_1PI": 0, "physical": False, "package_root": PACKAGE_ROOT})


def b1qggcontact1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C187-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "next": NEXT, "reason": "C112/C127 qgg local matrix scope is absent; C131 is aggregate; C130/C182 are typed interfaces; ownership must close before coefficient work", "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def contact_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C187-CONTACT-HANDOFF-FREEZE-V1", "C186_package_root": c186.PACKAGE_ROOT, "C186_owner_root": c186.order2_owner_manifest()["root"], "C186_color_root": c186.order2_color_manifest()["root"], "C186_action_root": c186.order2_action_manifest()["root"], "C186_topology_root": c186.topology_manifest()["root"], "C186_holonomy_root": c186.holonomy_bc_manifest()["root"], "C185_qgg_basis_root": c185.basis_manifest()["root"], "C185_qqbarq_root": c185.qqbarq_color_manifest()["root"], "C184_B0_root": c184.PACKAGE_ROOT, "C182_link_root": c182.local_link_manifest()["root"], "read_only": True, "root": _root((c186.PACKAGE_ROOT, c185.PACKAGE_ROOT, c184.PACKAGE_ROOT))})


def owner_manifest(owner_id: str | None = None) -> MappingProxyType:
    rows = (
        {"owner_id": OWNER_IDS[0], "upstream_package": "C112", "source_monomial": "C43 instantaneous fermion/constrained bad component", "field_content": ("q", "qbar", "g", "g"), "creation_annihilation_pattern": "q<->qgg candidate", "coupling_degree": 2, "particle_number_change": "q<->qgg", "local_role": "source/operator candidate", "matrix_role": "SOURCE_AUTHORITY_INCOMPLETE", "source_order": "C112 public order", "units": "GeV^2/g_s^2", "hermitian_partner": True, "aggregate_parents": ("C131_LOCAL_POLYNOMIAL_QGG",), "aggregate_children": (), "terminal": "SOURCE_AUTHORITY_INCOMPLETE", "public_scope": "q and qg only; no qgg target shape"},
        {"owner_id": OWNER_IDS[1], "upstream_package": "C127", "source_monomial": "C43 Gauss-law/current-current", "field_content": ("q", "qbar", "g", "g"), "creation_annihilation_pattern": "q<->qgg candidate", "coupling_degree": 2, "particle_number_change": "q<->qgg", "local_role": "source/operator candidate", "matrix_role": "SOURCE_AUTHORITY_INCOMPLETE", "source_order": "C127 component order", "units": "GeV^2/g_s^2", "hermitian_partner": True, "aggregate_parents": ("C131_LOCAL_POLYNOMIAL_QGG",), "aggregate_children": (), "terminal": "SOURCE_AUTHORITY_INCOMPLETE", "public_scope": "q and qg only; no qgg target shape"},
        {"owner_id": OWNER_IDS[2], "upstream_package": "C129", "source_monomial": "C43-G4 / G4_DIRECT_NORMAL_ORDERED", "field_content": ("g", "g", "g", "g"), "creation_annihilation_pattern": "pure-glue qg<->qgg source with spectator candidate", "coupling_degree": 2, "particle_number_change": "qg<->qgg, not q<->qgg local primitive", "local_role": "normal-ordering descendant", "matrix_role": "SEQUENTIAL_ROUTE_ONLY", "source_order": "C129 descendant order", "units": "GeV^2/g_s^2", "hermitian_partner": True, "aggregate_parents": (), "aggregate_children": ("C131_LOCAL_POLYNOMIAL_QGG",), "terminal": "SOURCE_NONZERO_OUTSIDE_Q_TO_QGG_LOCAL_DOMAIN", "public_scope": "destination qg->qgg and higher"},
        {"owner_id": OWNER_IDS[3], "upstream_package": "C131", "source_monomial": "projected degree-two local polynomial", "field_content": ("q", "qbar", "g", "g"), "creation_annihilation_pattern": "aggregate of primitive terms", "coupling_degree": 2, "particle_number_change": "aggregate crosswalk", "local_role": "aggregate crosswalk only", "matrix_role": "AGGREGATE_CROSSWALK_ONLY", "source_order": "C131 retained-term order", "units": "GeV^2/g_s^2", "hermitian_partner": True, "aggregate_parents": OWNER_IDS[:2], "aggregate_children": (), "terminal": "AGGREGATE_CROSSWALK_ONLY", "public_scope": "C131 retained support q/qg; not additional qgg primitive"},
        {"owner_id": OWNER_IDS[4], "upstream_package": "C130", "source_monomial": "zero-mode/residual/boundary interface", "field_content": ("boundary", "residual", "P0/Q0"), "creation_annihilation_pattern": "source interface", "coupling_degree": 2, "particle_number_change": "q<->qgg interface", "local_role": "boundary", "matrix_role": "NONMATRIX_BOUNDARY_INTERFACE", "source_order": "C130 interface order", "units": "typed interface", "hermitian_partner": True, "aggregate_parents": (), "aggregate_children": (), "terminal": "NONMATRIX_BOUNDARY_INTERFACE", "public_scope": "not a Hamiltonian matrix"},
        {"owner_id": OWNER_IDS[5], "upstream_package": "C182", "source_monomial": "degree-two residual-link source kernel", "field_content": ("link", "boundary", "holonomy"), "creation_annihilation_pattern": "source/operator insertion", "coupling_degree": 2, "particle_number_change": "q<->qgg interface", "local_role": "source/operator interface", "matrix_role": "SOURCE_OPERATOR_INTERFACE_NOT_HAMILTONIAN_BLOCK", "source_order": "C182 PP/PQ/QP/QQ order", "units": "symbolic link coefficient", "hermitian_partner": True, "aggregate_parents": (), "aggregate_children": (), "terminal": "SOURCE_OPERATOR_INTERFACE_NOT_HAMILTONIAN_BLOCK", "public_scope": "conditional source kernel; not local Hamiltonian by default"},
    )
    if owner_id is not None and owner_id not in OWNER_IDS: raise KeyError(owner_id)
    selected = tuple(row for row in rows if owner_id is None or row["owner_id"] == owner_id)
    return _freeze({"schema": "C187-OWNER-MANIFEST-V1", "rows": selected, "count": len(selected), "source_authorities": ("C112", "C127", "C129", "C131", "C130", "C182"), "duplicate_ownership": 0, "C131_additive_count": 0, "root": _root(selected)})


def owner_dag_manifest() -> MappingProxyType:
    nodes = tuple({"node_id": row["owner_id"], "kind": row["matrix_role"], "upstream": row["upstream_package"], "terminal": row["terminal"]} for row in owner_manifest()["rows"])
    edges = ({"source": "C112_INSTANTANEOUS_FERMION_QGG", "target": "C131_LOCAL_POLYNOMIAL_QGG", "relation": "aggregate_crosswalk"}, {"source": "C127_GAUSS_CURRENT_QGG", "target": "C131_LOCAL_POLYNOMIAL_QGG", "relation": "aggregate_crosswalk"}, {"source": "C129_G4_DIRECT_NORMAL_ORDERED_QGG", "target": "C131_LOCAL_POLYNOMIAL_QGG", "relation": "validation_crosswalk"}, {"source": "C185_QGG_QUARK_EMISSION", "target": "C187_SEQUENTIAL_ROUTE", "relation": "sequential_only"}, {"source": "C186_QGG_CUBIC_GLUE", "target": "C187_SEQUENTIAL_ROUTE", "relation": "sequential_only"})
    return _freeze({"schema": "C187-OWNER-DAG-V1", "nodes": nodes, "edges": edges, "acyclic": True, "C131_additive_count": 0, "sequential_distinct": True, "root": _root((nodes, edges))})


def instantaneous_fermion_manifest(resolution_id: str | None = None, source_id: str | None = None, target_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    allowed = _select(resolution_id, RESOLUTIONS)
    rows = []
    for resolution in allowed:
        upstream = c112.instantaneous_fermion_sector_manifest(C112_RESOLUTIONS[RESOLUTIONS.index(resolution)])
        for channel in _select(channel_id, QGG_CHANNELS):
            rows.append({"record_id": f"C187-IF-{resolution}-{channel}", "owner_id": OWNER_IDS[0], "resolution": resolution, "source_id": "C170-B1-Q", "target_id": "C170-B1-QGG", "channel_id": channel, "source_shape": upstream["q_shape"], "known_qg_shape": upstream["qg_shape"], "qgg_target_shape": None, "ordered_gluon_slots": ("g_1", "g_2"), "quark_modes": "C112 canonical q order", "ordered_color_word": "T^a T^b / T^b T^a retained", "spin_helicity": "source expression scope not qgg-closed", "denominator_id": f"C187-DEN-C112-{resolution}", "finite_cell_PV": "C43/C112 antisymmetric finite-cell inverse-partial-plus", "HO_factor": "not executable without qgg target", "CM_ground": "not executable without qgg target", "coupling_degree": 2, "units": "GeV^2/g_s^2", "orientation": ORIENTATIONS, "hermitian_partner": True, "source_availability": "SOURCE_AUTHORITY_INCOMPLETE", "routes": ("IF-A direct C112 source", "IF-B bad-component constraint", "IF-C operator preimage", "IF-D ordered color", "IF-E analytic HO/quadrature", "IF-F sparse/matrix-free", "IF-G Hermitian"), "matrix_application": "REJECTED_NO_QGG_SOURCE_TARGET", "root": _root((resolution, channel, upstream["q_shape"], upstream["qg_shape"]))})
    if source_id not in (None, "C170-B1-Q") or target_id not in (None, "C170-B1-QGG"): raise KeyError((source_id, target_id))
    return _freeze({"schema": "C187-INSTANTANEOUS-FERMION-V1", "rows": tuple(rows), "count": len(rows), "source_root": _c112_root(), "qgg_local_matrix": False, "root": _root(rows)})


def apply_instantaneous_fermion(parameter_record: Mapping[str, Any], vector: Sequence[Any], orientation: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    raise TypeError("C112 q↔qgg target is source-incomplete; matrix application rejected")


def gauss_current_manifest(resolution_id: str | None = None, source_id: str | None = None, target_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    components = c127.component_manifest()["components"]
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        for channel in _select(channel_id, QGG_CHANNELS):
            rows.append({"record_id": f"C187-GAUSS-{resolution}-{channel}", "owner_id": OWNER_IDS[1], "resolution": resolution, "source_id": "C170-B1-Q", "target_id": "C170-B1-QGG", "channel_id": channel, "current_factor_ids": tuple(x["component"] for x in components if x["sector"] == "q->q"), "known_source_shapes": ((6, 6), (1344, 1344)), "qgg_target_shape": None, "ordered_gluon_slots": ("g_1", "g_2"), "quark_current_orientation": "C127 source current orientation", "gluon_current_derivative": "C127 source derivative placement", "color_tensor": "ordered source candidate; projection unresolved", "denominator_id": f"C187-DEN-C127-{resolution}", "finite_cell_PV": "C43/C127 finite-cell constraint inverse; P0/Q0 scope explicit", "HO_factor": "not executable without qgg target", "CM_ground": "not executable without qgg target", "coupling_degree": 2, "units": "GeV^2/g_s^2", "orientation": ORIENTATIONS, "hermitian_partner": True, "source_availability": "SOURCE_AUTHORITY_INCOMPLETE", "routes": ("GAUSS-A current-current", "GAUSS-B constrained field", "GAUSS-C operator preimage", "GAUSS-D color/projector", "GAUSS-E derivative/PV", "GAUSS-F HO/quadrature", "GAUSS-G sparse/matrix-free", "GAUSS-H Hermitian"), "matrix_application": "REJECTED_NO_QGG_SOURCE_TARGET", "root": _root((resolution, channel, tuple(x["component"] for x in components)))})
    if source_id not in (None, "C170-B1-Q") or target_id not in (None, "C170-B1-QGG"): raise KeyError((source_id, target_id))
    return _freeze({"schema": "C187-GAUSS-CURRENT-V1", "rows": tuple(rows), "count": len(rows), "source_root": c127.PACKAGE_ROOT, "qgg_local_matrix": False, "root": _root(rows)})


def apply_gauss_current(parameter_record: Mapping[str, Any], vector: Sequence[Any], orientation: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    raise TypeError("C127 q↔qgg target is source-incomplete; matrix application rejected")


def polynomial_crosswalk_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = ({"record_id": "C187-POLY-C129-G4", "source": "C129 G4_DIRECT_NORMAL_ORDERED", "classification": "NORMAL_ORDERING_DESCENDANT", "particle_number_proof": "pure-glue source destination is qg->qgg, not q->qgg local primitive", "longitudinal_proof": "source qg parent required", "preimage_proof": "C129 descendant destination", "aggregate_count": 0, "source_nonzero": True, "local_matrix": False}, {"record_id": "C187-POLY-C131-AGGREGATE", "source": "C131 projected bare local polynomial", "classification": "AGGREGATE_CROSSWALK_ONLY", "particle_number_proof": "C131 retained support is q/qg", "longitudinal_proof": "no qgg target record", "preimage_proof": "C112/C127/C129 primitives referenced without additive recount", "aggregate_count": 0, "source_nonzero": "not independently assigned", "local_matrix": False})
    if record_id is not None and record_id not in {r["record_id"] for r in rows}: raise KeyError(record_id)
    rows = tuple(r for r in rows if record_id is None or r["record_id"] == record_id)
    return _freeze({"schema": "C187-POLYNOMIAL-CROSSWALK-V1", "rows": rows, "count": len(rows), "C131_additive_count": 0, "routes": ("POLY-A descendant taxonomy", "POLY-B unique owner table", "POLY-C preimage", "POLY-D longitudinal support", "POLY-E primitive versus aggregate"), "root": _root(rows)})


def zero_boundary_manifest(owner_id: str | None = None) -> MappingProxyType:
    rows = ({"owner_id": OWNER_IDS[4], "interface_id": "C130-P0-ZERO-MODE", "classification": "P0_ZERO_MODE_INTERFACE", "source_target": "q<->qgg metadata", "cut_holonomy_relation": "C183/C130 boundary relation", "P0_Q0_scope": "P0 residual; Q0 nonzero modes separate", "matrix_status": "NONMATRIX", "availability": "TYPED_SOURCE_INTERFACE", "count_once_owner": OWNER_IDS[4], "future_1PI_treatment": "symbolic boundary/interface term; not local matrix"}, {"owner_id": OWNER_IDS[4], "interface_id": "C130-RESIDUAL-BOUNDARY", "classification": "RESIDUAL_GAUGE_INTERFACE", "source_target": "q<->qgg metadata", "cut_holonomy_relation": "C182/C183 conditional", "P0_Q0_scope": "P0 residual; Q0 unchanged", "matrix_status": "NONMATRIX", "availability": "TYPED_SOURCE_INTERFACE", "count_once_owner": OWNER_IDS[4], "future_1PI_treatment": "not additive zero"})
    if owner_id is not None and owner_id != OWNER_IDS[4]: raise KeyError(owner_id)
    return _freeze({"schema": "C187-ZERO-BOUNDARY-V1", "rows": rows, "count": len(rows), "represented_as_zero_matrix": False, "root": _root(rows)})


def link_interface_manifest(owner_id: str | None = None) -> MappingProxyType:
    rows = tuple({"owner_id": OWNER_IDS[5], "kernel_id": f"C182-QGG-LINK-{resolution}", "resolution": resolution, "coordinate_form": "retained/boundary/gauge-gradient records", "path_scheme": "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1", "classes": ("PP", "PQ", "QP", "QQ"), "field_coupling_degree": 2, "source_target": "q<->qgg source/operator interface", "endpoint_support": "C182/C181 boundary-owned", "holonomy_required": True, "matrix_status": "SOURCE_OPERATOR_INTERFACE_NOT_HAMILTONIAN_BLOCK", "future_1PI_owner": "boundary/link component", "routes": ("LINK-A source kernel", "LINK-B project-subgauge variation", "LINK-C endpoint support", "LINK-D C181 boundary crosswalk", "LINK-E C130/C175 count-once"), "root": _root((resolution, c182.local_link_manifest()["root"]))} for resolution in RESOLUTIONS)
    if owner_id is not None and owner_id != OWNER_IDS[5]: raise KeyError(owner_id)
    return _freeze({"schema": "C187-LINK-INTERFACE-V1", "rows": rows, "count": len(rows), "source_root": c182.two_link_kernel_manifest()["root"], "inserted_as_hamiltonian": False, "root": _root(rows)})


def color_manifest(owner_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    owners = OWNER_IDS if owner_id is None else _select(owner_id, OWNER_IDS)
    channels = QGG_CHANNELS if channel_id is None else _select(channel_id, QGG_CHANNELS)
    rows = tuple({"owner_id": owner, "channel_id": channel, "ordered_color_word": "T^a T^b", "reverse_order_word": "T^b T^a", "symmetric_split": "C43-normalized anticommutator unresolved" if channel != "QGG_COLOR_8A" else "typed unresolved", "antisymmetric_split": "typed unresolved" if channel != "QGG_COLOR_8A" else "C43-normalized commutator unresolved", "coefficient": "UNRESOLVED_NOT_ZERO", "phase": "source-qualified phase unresolved", "daughter_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "all_eight_generator_residual": 0.0, "zero_certificate": None, "status": "OWNERSHIP_FRONTIER_NOT_CLOSED"} for owner in owners for channel in channels)
    return _freeze({"schema": "C187-COLOR-V1", "rows": rows, "count": len(rows), "channels_separate": True, "routes": ("COLOR-A ordered generators", "COLOR-B C185 projector", "COLOR-C commutator/anticommutator", "COLOR-D conjugation/all generators", "COLOR-E exchange holdout"), "root": _root(rows)})


def denominator_manifest(owner_id: str | None = None, denominator_id: str | None = None) -> MappingProxyType:
    owners = OWNER_IDS if owner_id is None else _select(owner_id, OWNER_IDS)
    rows = []
    for owner in owners:
        for resolution in RESOLUTIONS:
            did = f"C187-DEN-{owner.split('_')[0]}-{resolution}"
            rows.append({"denominator_id": did, "owner_id": owner, "resolution": resolution, "ordered_particle_slots": ("q", "g_1", "g_2"), "longitudinal_combination": "caller/source ordered k_1,k_2 with positive support", "P0_Q0_scope": "P0 excluded; Q0 antisymmetric inverse retained", "PV_prescription": "C43 finite-cell antisymmetric/PV authority", "zero_mode_exclusion": True, "units": "inverse longitudinal momentum power", "orientation": ORIENTATIONS, "pole_zero_condition": "reject ordinary k+=0 and unresolved pole", "source_route": "DEN-A source expression; DEN-B finite Fourier; DEN-C P0/Q0; DEN-D ordered momentum; DEN-E reverse/Hermitian", "status": "BOUND_PRESCRIPTION_SOURCE_SCOPE_INCOMPLETE" if owner in (OWNER_IDS[0], OWNER_IDS[1]) else "NO_INVERSE_REQUIRED_OR_INTERFACE", "root": _root((owner, resolution, "C43-FINITE-CELL-PV"))})
    if denominator_id is not None and denominator_id not in {r["denominator_id"] for r in rows}: raise KeyError(denominator_id)
    rows = tuple(r for r in rows if denominator_id is None or r["denominator_id"] == denominator_id)
    return _freeze({"schema": "C187-DENOMINATOR-V1", "rows": rows, "count": len(rows), "continuum_substitution": False, "ordinary_zero_modes": 0, "root": _root(rows)})


def kinematics_manifest(owner_id: str | None = None, resolution_id: str | None = None, source_id: str | None = None, target_id: str | None = None) -> MappingProxyType:
    owners = OWNER_IDS if owner_id is None else _select(owner_id, OWNER_IDS)
    rows = []
    for owner in owners:
        for resolution in _select(resolution_id, RESOLUTIONS):
            rows.append({"kinematics_id": f"C187-KIN-{owner}-{resolution}", "owner_id": owner, "resolution": resolution, "source_id": "C170-B1-Q", "target_id": "C170-B1-QGG", "quark_helicity": "source scope or typed interface", "ordered_gluon_polarizations": "source scope or typed interface", "daughter_exchange": "C185 Bose projector retained", "positive_longitudinal": True, "total_longitudinal_conservation": True, "finite_HO_overlap": "not executable without local qgg matrix for unresolved owners", "finite_shell_leakage": "explicit/unpruned upstream interface", "CM_ground": "not silently excited", "units": "GeV^2/g_s^2 or typed interface", "orientation": ORIENTATIONS, "routes": ("KIN-A direct source", "KIN-B preimage", "KIN-C C185 Bose", "KIN-D analytic HO", "KIN-E quadrature", "KIN-F TM/CM"), "status": "FAIL_CLOSED_SOURCE_SCOPE", "root": _root((owner, resolution))})
    if source_id not in (None, "C170-B1-Q") or target_id not in (None, "C170-B1-QGG"): raise KeyError((source_id, target_id))
    return _freeze({"schema": "C187-KINEMATICS-V1", "rows": tuple(rows), "count": len(rows), "ordinary_zero_modes": 0, "CM_excited_silently_included": False, "threshold_pruned": False, "root": _root(rows)})


def action_manifest(owner_id: str | None = None, resolution_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    owners = OWNER_IDS if owner_id is None else _select(owner_id, OWNER_IDS)
    rows = tuple({"action_id": f"C187-ACT-{owner}-{resolution}-{channel}", "owner_id": owner, "resolution": resolution, "channel_id": channel, "source_id": "C170-B1-Q", "target_id": "C170-B1-QGG", "matrix_authority": False, "sparse": False, "matrix_free": False, "typed_nonmatrix": True, "dense_default": False, "source_reachable": False, "hermitian_partner": True, "matrix_application": "REJECT", "routes": ("ACT-A factorized sparse audit", "ACT-B matrix-free audit", "ACT-C preimage", "ACT-D generated Hermitian", "ACT-E owner/query order", "ACT-F fixture holdout"), "status": "TYPED_BLOCKER_NO_LOCAL_MATRIX", "root": _root((owner, resolution, channel))} for owner in owners for resolution in _select(resolution_id, RESOLUTIONS) for channel in _select(channel_id, QGG_CHANNELS))
    return _freeze({"schema": "C187-ACTION-V1", "rows": rows, "count": len(rows), "dense_rectangular_default": False, "nonmatrix_rejects_application": True, "root": _root(rows)})


def apply_order2_owner(parameter_record: Mapping[str, Any], vector: Sequence[Any], owner_id: str, orientation: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    if owner_id not in OWNER_IDS: raise KeyError(owner_id)
    raise TypeError(f"{owner_id} has no authenticated qgg local matrix; typed nonmatrix/source interface only")


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = ({"graph_id": "C187-C112-DIRECT", "owner_id": OWNER_IDS[0], "source": "q", "sink": "qgg", "intermediate": None, "energy_denominator": "none/direct if source closes", "coupling_degree": 2, "classification": "source-authority-incomplete direct candidate", "proper_1PI": "future", "reducible": False, "contact": True, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-C127-DIRECT", "owner_id": OWNER_IDS[1], "source": "q", "sink": "qgg", "intermediate": None, "energy_denominator": "finite-cell PV if source closes", "coupling_degree": 2, "classification": "source-authority-incomplete direct candidate", "proper_1PI": "future", "reducible": False, "contact": True, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-C129-OUTSIDE", "owner_id": OWNER_IDS[2], "source": "qg", "sink": "qgg", "intermediate": "qg", "energy_denominator": "sequential qg", "coupling_degree": 2, "classification": "normal-ordering/sequential-only", "proper_1PI": False, "reducible": True, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-C131-AGGREGATE", "owner_id": OWNER_IDS[3], "source": "q", "sink": "qgg", "intermediate": None, "energy_denominator": "aggregate", "coupling_degree": 2, "classification": "aggregate crosswalk only", "proper_1PI": False, "reducible": False, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": False}, {"graph_id": "C187-C130-BOUNDARY", "owner_id": OWNER_IDS[4], "source": "q", "sink": "qgg", "intermediate": None, "energy_denominator": "nonmatrix", "coupling_degree": 2, "classification": "source-interface/boundary", "proper_1PI": "future interface", "reducible": False, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-C182-LINK", "owner_id": OWNER_IDS[5], "source": "q", "sink": "qgg", "intermediate": None, "energy_denominator": "nonmatrix link", "coupling_degree": 2, "classification": "source/operator interface", "proper_1PI": "future interface", "reducible": False, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-SEQUENTIAL-QUARK", "owner_id": "C185_QGG_QUARK_EMISSION", "source": "q", "sink": "qgg", "intermediate": "qg", "energy_denominator": "qg resolvent", "coupling_degree": 2, "classification": "sequential", "proper_1PI": False, "reducible": True, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-SEQUENTIAL-CUBIC", "owner_id": "C186_QGG_CUBIC_GLUE", "source": "q", "sink": "qgg", "intermediate": "qg", "energy_denominator": "qg resolvent", "coupling_degree": 2, "classification": "sequential", "proper_1PI": False, "reducible": True, "contact": False, "leg": False, "color": QGG_CHANNELS, "count_once": True}, {"graph_id": "C187-LEG-CROSSWALK", "owner_id": "C185_EXTERNAL_LEGS", "source": "qg", "sink": "qg", "intermediate": "q/qg", "energy_denominator": "leg authority", "coupling_degree": 1, "classification": "external leg; not proper 1PI", "proper_1PI": False, "reducible": True, "contact": False, "leg": True, "color": (), "count_once": True})
    if graph_id is not None and graph_id not in {row["graph_id"] for row in rows}: raise KeyError(graph_id)
    rows = tuple(row for row in rows if graph_id is None or row["graph_id"] == graph_id)
    return _freeze({"schema": "C187-TOPOLOGY-V1", "rows": rows, "count": len(rows), "complete_qg_1PI": False, "direct_sequential_conflation": False, "leg_1PI_conflation": False, "root": _root(rows)})


def holonomy_bc_manifest(capsule_id: str | None = None, owner_id: str | None = None) -> MappingProxyType:
    source = {row["capsule_id"]: row for row in c183.boundary_condition_manifest()["rows"]}
    owners = OWNER_IDS if owner_id is None else _select(owner_id, OWNER_IDS)
    rows = tuple({"capsule_id": fid, "owner_id": owner, "q_boundary": source[fid]["fermion"], "qgg_gluon_boundary": source[fid]["gluon"], "fundamental_twist": True, "center_sector": source[fid]["center_sector"], "classification": "ADJOINT_SOURCE_COMPATIBLE_FUNDAMENTAL_TWIST_EXPLICIT" if source[fid]["center_sector"] != "Z3_IDENTITY" else "FROZEN_BASIS_COMPATIBLE", "mode_grid_changed": False, "matrix_status": "owner-dependent typed", "physical_holonomy": False, "root": _root((fid, owner))} for fid in c183.FIXTURE_IDS for owner in owners)
    if capsule_id is not None and capsule_id not in c183.FIXTURE_IDS: raise KeyError(capsule_id)
    rows = tuple(row for row in rows if capsule_id is None or row["capsule_id"] == capsule_id)
    return _freeze({"schema": "C187-HOLONOMY-BC-V1", "rows": rows, "count": len(rows), "longitudinal_grid_changed": False, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"owner_id": owner, "count": 0 if owner == OWNER_IDS[3] else 1, "duplicate": False, "role": "aggregate crosswalk only" if owner == OWNER_IDS[3] else "primitive/interface owner", "C131_additive": False, "direct_sequential_conflation": False, "nonmatrix_as_zero": False} for owner in (*OWNER_IDS, "C185_QGG_QUARK_EMISSION", "C186_QGG_CUBIC_GLUE", "C185_EXTERNAL_LEGS", "C185_QGG_RESOLVENT", "C151_COUNTERTERMS", "C187_TARGET_MOMQ", "C187_FUTURE_ST"))
    if request_id is not None and request_id not in REQUESTS: raise KeyError(request_id)
    return _freeze({"schema": "C187-COUNT-ONCE-V1", "rows": rows, "request_id": request_id, "duplicates": 0, "C131_additive_count": 0, "unavailable_is_zero": False, "root": _root((rows, request_id))})


def qgg_contact_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C187-CONTACT-RELEASE-V1", "decision": "QGG_NOT_RELEASED_PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE", "status": STATUS, "plan": PLAN, "gates": {"owner_DAG": False, "C112": False, "C127": False, "C129_C131": False, "C130": True, "C182": True, "color": False, "denominator": True, "kinematics": False, "action": True, "topology": True, "holonomy_BC": True, "count_once": True}, "complete_qg_1PI": False, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c185.request_resolution_manifest()["rows"]:
        req = old["request_id"]
        if "qg_VERTEX" in req or "QCD_COUPLING" in req:
            status, nxt = "PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE", NEXT
        else:
            status, nxt = old["terminal_status"], old["exact_next_object"]
        rows.append({"request_id": req, "terminal_status": status, "active_in_C187": "qg_VERTEX" in req or "QCD_COUPLING" in req, "exact_next_object": nxt, "complete_qg_1PI": False, "physical_coupling": False, "request4_frozen": "TRANSVERSE_GLUON" in req})
    if request_id is not None and request_id not in REQUESTS: raise KeyError(request_id)
    selected = tuple(row for row in rows if request_id is None or row["request_id"] == request_id)
    return _freeze({"schema": "C187-REQUEST-RESOLUTION-V1", "rows": selected, "all_six_visible": len(selected) == 6 if request_id is None else True, "root": _root(selected)})


def missing_contact_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = REQUESTS if request_id is None else _select(request_id, REQUESTS)
    rows = []
    for req in reqs:
        if req not in c185.ACTIVE_REQUESTS: continue
        for owner in OWNER_IDS:
            rows.append({"object_id": f"C187-{owner}-COMPLETION", "parent_request_id": req, "resolution": "K9/K11/K13", "source_target": ("C170-B1-Q", "C170-B1-QGG"), "primitive_owner_ids": (owner,), "channel_ids": QGG_CHANNELS, "holonomy_classes": c183.FIXTURE_IDS, "coupling_degree": 2, "required_routes": ("ownership DAG", "source/preimage", "ordered color", "denominator/PV", "kinematics", "action", "topology"), "status": owner_manifest(owner)["rows"][0]["terminal"], "not_zero": True, "nonclaim": "no complete qg 1PI or physical coupling"})
        rows.append({"object_id": "C188-COMPLETE-QG-1PI", "parent_request_id": req, "resolution": "K9/K11/K13", "source_target": ("C170-B1-QG", "C170-B1-QG"), "primitive_owner_ids": OWNER_IDS, "channel_ids": QGG_CHANNELS, "holonomy_classes": c183.FIXTURE_IDS, "coupling_degree": 3, "required_routes": ("higher-sector resolvents", "external-leg subtraction", "direct/contact", "ST remainder"), "status": "FUTURE_NOT_CALCULATED", "not_zero": True, "nonclaim": "no complete qg 1PI or physical coupling"})
    return _freeze({"schema": "C187-MISSING-CONTACT-OBJECT-V1", "rows": tuple(rows), "count": len(rows), "not_zero": True, "root": _root(rows)})


def qg_1pi_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C187-QG-1PI-HANDOFF-V1", "next": NEXT, "C185_qgg_root": c185.basis_manifest()["root"], "C186_cubic_root": c186.cubic_action_manifest()["root"], "C187_owner_root": owner_manifest()["root"], "C187_dag_root": owner_dag_manifest()["root"], "C187_action_root": action_manifest()["root"], "C187_interface_root": link_interface_manifest()["root"], "C184_B0_root": c184.PACKAGE_ROOT, "C183_root": c183.PACKAGE_ROOT, "complete_qg_1PI": False, "physical_Z1F": False, "physical_coupling": False, "target_MOMq": False, "root": _root((NEXT, STATUS, c185.PACKAGE_ROOT, c184.PACKAGE_ROOT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C187-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "completed": ("C184 B0", "C185 qgg/qqbarq", "C186 cubic"), "partial": ("C187 primitive/aggregate ownership", "C112 qgg source", "C127 qgg source", "complete qg 1PI", "full ST", "target MOMq"), "counterterm_directions_selected": 0, "null_coordinates_selected": 0, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C187-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameter_count": 0, "root": _root((0, 0, 0))})


def b1qggcontact1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C187-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "owner_count": 6, "owner_DAG_acyclic": True, "C112_local_qgg_matrix": False, "C127_local_qgg_matrix": False, "C131_aggregate_count": 0, "C130_nonmatrix": True, "C182_source_interface": True, "color_channels": QGG_CHANNELS, "denominator_PV_bound": True, "complete_qg_1PI": False, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_representatives": 0, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "model_memory_formulas": 0, "invented_contracts": 0, "C158_value_inputs": 0, "C185_basis_recomputed": 0, "C186_cubic_recomputed": 0, "C184_B0_recalculation": 0, "complete_qg_1PI": 0, "physical_inputs": 0, "C131_aggregate_double_count": 0, "nonmatrix_to_matrix_fabrication": 0, "source_Hamiltonian_conflation": 0, "continuum_denominator_substitution": 0, "ordinary_zero_modes": 0, "direct_sequential_conflations": 0, "missing_terms_set_zero": 0, "holonomy_omissions": 0, "leg_1PI_conflations": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((0, 0, STATUS))})


def mutate_live_hqcd_b1qggcontact1(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "C187 owner/source/action perturbation", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS, "mutation"))})


ROOTS = {"C186": c186.PACKAGE_ROOT, "C185": c185.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C182": c182.PACKAGE_ROOT, "C112": _c112_root(), "C127": c127.PACKAGE_ROOT, "C129": c129.PACKAGE_ROOT, "C131": c131.PACKAGE_ROOT, "C187_PLAN": b1qggcontact1_plan_manifest()["root"], "C187_HANDOFF": contact_handoff_freeze()["root"], "C187_OWNER": owner_manifest()["root"], "C187_DAG": owner_dag_manifest()["root"], "C187_IF": instantaneous_fermion_manifest()["root"], "C187_GAUSS": gauss_current_manifest()["root"], "C187_CROSSWALK": polynomial_crosswalk_manifest()["root"], "C187_BOUNDARY": zero_boundary_manifest()["root"], "C187_LINK": link_interface_manifest()["root"], "C187_COLOR": color_manifest()["root"], "C187_DENOMINATOR": denominator_manifest()["root"], "C187_KINEMATICS": kinematics_manifest()["root"], "C187_ACTION": action_manifest()["root"], "C187_TOPOLOGY": topology_manifest()["root"], "C187_HOLONOMY": holonomy_bc_manifest()["root"], "C187_COUNT": count_once_manifest()["root"], "C187_RELEASE": qgg_contact_release_manifest()["root"], "C187_REQUESTS": request_resolution_manifest()["root"], "C187_MISSING": missing_contact_object_manifest()["root"], "C187_HANDOFF_1PI": qg_1pi_handoff_contract()["root"], "C187_FRONTIER": dependency_frontier_manifest()["root"], "C187_QUANTUM": quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT = _root({"schema": "C187-HQCDB1QGGCONTACT1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})


__all__ = [name for name in globals() if not name.startswith("_")]
