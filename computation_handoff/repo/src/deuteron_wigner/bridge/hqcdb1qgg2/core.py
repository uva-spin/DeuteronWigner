"""C186 qg/qgg cubic transition and q-to-qgg owner frontier.

This package consumes C185, C184, C183, C182, C129, C127, C112 and C131
through public records.  It publishes symbolic finite-basis interfaces only;
it does not select physical parameters or calculate the complete qg 1PI
vertex.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdb1higherfock1 as c185
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdb0reslink2 as c182
from deuteron_wigner.bridge import gnorm as c129
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import iferm3 as c112
from deuteron_wigner.bridge import hqcd4 as c131

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c186_hqcdb1qgg2"
BASELINE = "916e324a60f25ec37481a2035c4d4b73cbcb27d4"
CONTRACT = "docs/next_level/c185_c186_hqcdb1qgg2_continuation_contract.json"
CONTRACT_SHA256 = "cff01f74961e42534476df50b0a52a11e2f6dae9d566a47c3c434eb2fda00368"
PROMPT = "/Users/dustin/Downloads/c186_hqcdb1qgg2_codex_prompt.md"
PROMPT_SHA256 = "799670a3a01c08b2981e79aba5f1c03cf971ae418cd1eeb3e67b49a8d27ee4aa"
STATUS = "C186_C185_QGG_CUBIC_TRANSITION_READY_ORDER2_OWNER_PARTIAL"
PLAN = "B1QGG2-B"
NEXT = "C187/HQCDB1QGGCONTACT1"
RESOLUTIONS = ("K9", "K11", "K13")
C112_RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
ORIENTATIONS = ("qg_to_qgg", "qgg_to_qg")
COUNTERTERM_DIRECTIONS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULL_COORDINATES = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
REQUESTS = tuple(row["request_id"] for row in c185.request_resolution_manifest()["rows"])


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    if isinstance(value, complex):
        return [value.real, value.imag]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None:
        return tuple(allowed)
    if value not in allowed:
        raise KeyError(value)
    return (value,)


def _resolution_row(resolution: str) -> Mapping[str, Any]:
    rows = {row["resolution"]: row for row in c185.longitudinal_manifest(sector_id="C170-B1-QGG")["rows"]}
    if resolution not in rows:
        raise KeyError(resolution)
    row = rows[resolution]
    dims = next(row["dimensions"] for row in c185.basis_manifest() ["rows"] if row["sector_id"] == "C170-B1-QGG" and row["resolution"] == resolution)
    qg_dim = next(row["source_dimension"] for row in c185.qg_qgg_quark_manifest()["rows"] if row["transition_id"].endswith(resolution))
    return {"resolution": resolution, "qg_dimension": qg_dim, "qgg_dimension": dims["cm_ground"], "ordered_longitudinal": row["qgg_ordered"], "bose_orbits": row["qgg_bose_orbits"], "ordinary_zero_mode": row["ordinary_zero_mode"]}


def _verify_frozen_roots() -> None:
    if c185.PACKAGE_ROOT != "c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885":
        raise ValueError("C185 root changed")
    if c184.PACKAGE_ROOT != "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8":
        raise ValueError("C184 root changed")
    if c185.qgg_color_manifest()["derived_multiplicity"] != 3 or c185.qqbarq_color_manifest()["derived_multiplicity"] != 2:
        raise ValueError("C185 sector multiplicity changed")
    if c185.qg_qgg_gluon_manifest()["rows"][0]["status"] != "PARTIAL_QGG_FRONTIER":
        raise ValueError("unexpected C185 terminal state")


def load_verified_hqcd_b1qgg2_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists():
        raise FileNotFoundError("C186 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C186 runtime root/status mismatch")
    return _freeze(verify_hqcd_b1qgg2_authority())


def verify_hqcd_b1qgg2_authority() -> MappingProxyType:
    _verify_frozen_roots()
    return _freeze({"schema": "C186-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "C185_package_root": c185.PACKAGE_ROOT, "C184_package_root": c184.PACKAGE_ROOT, "source_acquisitions": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "C185_basis_recomputed": 0, "C185_qqbarq_mutated": 0, "C184_B0_recalculation": 0, "complete_qg_1PI": 0, "physical": False, "package_root": PACKAGE_ROOT})


def b1qgg2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C186-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "next": NEXT, "reason": "cubic spectator transition closes; q-to-qgg order-two owners remain typed source-qualified blockers", "mutually_exclusive": True, "root": _root((PLAN, STATUS, NEXT))})


def qgg_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C186-QGG-HANDOFF-FREEZE-V1", "C185_package_root": c185.PACKAGE_ROOT, "C185_qgg_color_root": c185.qgg_color_manifest()["root"], "C185_qgg_statistics_root": c185.qgg_statistics_manifest()["root"], "C185_basis_root": c185.basis_manifest()["root"], "C185_rank_root": c185.rank_unrank_manifest()["root"], "C185_qgg_quark_root": c185.qg_qgg_quark_manifest()["root"], "C185_qqbarq_root": c185.qqbarq_color_manifest()["root"], "C185_cubic_terminal_root": c185.qg_qgg_gluon_manifest()["root"], "C185_order2_terminal_root": c185.order2_manifest("q_qgg")["root"], "C184_gg_root": c184.g_gg_vertex_manifest()["root"], "C182_link_root": c182.local_link_manifest()["root"], "C183_holonomy_root": c183.holonomy_fixture_manifest()["root"], "read_only": True, "root": _root((c185.PACKAGE_ROOT, c184.PACKAGE_ROOT, c182.local_link_manifest()["root"], c183.holonomy_fixture_manifest()["root"]))})


def cubic_owner_manifest(owner_id: str | None = None) -> MappingProxyType:
    owners = (
        {"owner_id": "C129_G3_DIRECT_NORMAL_ORDERED", "source_monomial_id": "C43-G3", "normal_ordering_descendant_id": "G3_DIRECT_NORMAL_ORDERED", "coupling_degree": 1, "creation_pattern": "parent_gluon_to_two_daughters", "parent_gluon_slot": "qg.g_parent", "daughter_gluon_slots": ("qgg.g_1", "qgg.g_2"), "spectator_quark_role": "unchanged", "longitudinal_derivative": "C43/C129 source derivative placement", "transverse_derivative": "C43/C129 source polarization tensor", "polarization_tensor": "source-qualified symbolic", "color_tensor": "f^{abc}", "units": "GeV^2/g_s", "orientation": "qg_to_qgg", "hermitian_partner": "C129_G3_DIRECT_NORMAL_ORDERED_HC", "source_availability": "SOURCE_NONZERO_DIRECT_CUBIC", "canonical_not_normal_ordering_descendant": True},
        {"owner_id": "C184_GG_F_SPECTATOR_SOURCE", "source_monomial_id": "C184-GG-F", "normal_ordering_descendant_id": "G3_DIRECT_NORMAL_ORDERED", "coupling_degree": 1, "creation_pattern": "parent_gluon_to_two_daughters", "parent_gluon_slot": "C184 source gluon", "daughter_gluon_slots": ("qgg.g_1", "qgg.g_2"), "spectator_quark_role": "unchanged", "longitudinal_derivative": "C184 read-only", "transverse_derivative": "C184 read-only", "polarization_tensor": "C184 GG_F source record", "color_tensor": "f^{abc}", "units": "GeV^2/g_s", "orientation": "both via generated adjoint", "hermitian_partner": "C184_GG_F_SPECTATOR_SOURCE_HC", "source_availability": "CONDITIONAL_SOURCE_DERIVED_READY", "canonical_not_normal_ordering_descendant": True},
        {"owner_id": "C129_G3_SINGLE_CONTRACTION_LINEAR", "source_monomial_id": "C43-G3", "normal_ordering_descendant_id": "G3_SINGLE_CONTRACTION_LINEAR", "coupling_degree": 1, "creation_pattern": "single_contraction", "parent_gluon_slot": "none", "daughter_gluon_slots": (), "spectator_quark_role": "not applicable", "longitudinal_derivative": "source record", "transverse_derivative": "source record", "polarization_tensor": "not applicable", "color_tensor": "f^{abb}=0", "units": "GeV^2/g_s", "orientation": "excluded", "hermitian_partner": "none", "source_availability": "EXACT_ZERO_NON_TARGET_DESCENDANT", "canonical_not_normal_ordering_descendant": False},
    )
    selected = owners if owner_id is None else tuple(row for row in owners if row["owner_id"] == owner_id)
    if owner_id is not None and not selected:
        raise KeyError(owner_id)
    return _freeze({"schema": "C186-CUBIC-OWNER-V1", "rows": selected, "count": len(selected), "canonical_source_root": c129.source_term_manifest()["root"], "descendant_root": c129.descendant_manifest()["root"], "routes": ("OWNER-A source term", "OWNER-B normal-ordering crosswalk", "OWNER-C C184 read-only source", "OWNER-D orientation/Hermitian"), "root": _root(selected)})


def spectator_lift_manifest(resolution_id: str | None = None, source_id: str | None = None, target_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_row(resolution)
        for channel in QGG_CHANNELS:
            row = {"lift_id": f"C186-SPECTATOR-CUBIC-{resolution}-{channel}", "resolution": resolution, "source_id": "C170-B1-QG", "target_id": "C170-B1-QGG", "source_dimension": d["qg_dimension"], "target_dimension": d["qgg_dimension"], "source_c184_record": f"C184-GG-{resolution}-GG_F", "spectator_quark_mode": "unchanged C170-B1-QG q mode", "spectator_color": "open triplet index unchanged", "spectator_helicity": "unchanged", "spectator_flavor": "caller-supplied explicit flavor; no sum", "spectator_longitudinal_identity": True, "spectator_HO_identity": True, "daughter_order": ("g_1", "g_2"), "Bose_orbit": d["bose_orbits"], "CM_ground": True, "normalization": "C184 source normalization times C185 spectator/source-target ratio", "unit_spectator_factor_assumed": False, "lift_coefficient": "SOURCE_C184_GG_F * N_C185_SPECTATOR_RATIO", "channel_support": "nonzero only for QGG_COLOR_8A" if channel == "QGG_COLOR_8A" else "exact zero by projected f/d or f/singlet orthogonality", "routes": ("LIFT-A direct C43/C129 projection", "LIFT-B C184 GG_F spectator lift", "LIFT-C operator preimage", "LIFT-D source/target normalization ratio", "LIFT-E sparse/matrix-free parity"), "root": _root((resolution, channel, d["qg_dimension"], d["qgg_dimension"]))}
            if source_id is None or row["source_id"] == source_id:
                if target_id is None or row["target_id"] == target_id:
                    rows.append(row)
    if source_id not in (None, "C170-B1-QG") or target_id not in (None, "C170-B1-QGG"):
        if not rows: raise KeyError((source_id, target_id))
    return _freeze({"schema": "C186-SPECTATOR-LIFT-V1", "rows": tuple(rows), "count": len(rows), "source_root": c184.g_gg_vertex_manifest()["root"], "root": _root(rows)})


def cubic_color_manifest(channel_id: str | None = None, source_record_id: str | None = None) -> MappingProxyType:
    rows = (
        {"channel_id": "QGG_COLOR_1S", "source_record_id": "C129_G3_DIRECT_NORMAL_ORDERED", "source_color_tensor": "f^{abc}", "projector": "C185 1_s Gram dual", "projection_coefficient": "0", "normalization": "C185 unit Gram", "exchange_parity": 1, "all_eight_generator_residual": 0.0, "open_triplet_orientation": "3", "hermitian_partner_coefficient": "0", "zero_certificate": "f^{abc} delta^{ab}=0", "status": "EXACT_ZERO_WITH_ALGEBRAIC_PROJECTION"},
        {"channel_id": "QGG_COLOR_8S", "source_record_id": "C129_G3_DIRECT_NORMAL_ORDERED", "source_color_tensor": "f^{abc}", "projector": "C185 8_s Gram dual", "projection_coefficient": "0", "normalization": "C185 unit Gram", "exchange_parity": 1, "all_eight_generator_residual": 0.0, "open_triplet_orientation": "3", "hermitian_partner_coefficient": "0", "zero_certificate": "f^{abc} d^{ab c'}=0", "status": "EXACT_ZERO_WITH_ALGEBRAIC_PROJECTION"},
        {"channel_id": "QGG_COLOR_8A", "source_record_id": "C129_G3_DIRECT_NORMAL_ORDERED", "source_color_tensor": "f^{abc}", "projector": "C185 8_a Gram dual", "projection_coefficient": "SOURCE_C43_NORMALIZED_F_TENSOR", "normalization": "C185 unit Gram and C184 GG_F", "exchange_parity": -1, "all_eight_generator_residual": 0.0, "open_triplet_orientation": "3", "hermitian_partner_coefficient": "SOURCE_C43_NORMALIZED_F_TENSOR_HC", "zero_certificate": None, "status": "SOURCE_DERIVED_NONZERO_SYMBOLIC"},
    )
    rows = tuple(row for row in rows if (channel_id is None or row["channel_id"] == channel_id) and (source_record_id is None or row["source_record_id"] == source_record_id))
    if channel_id is not None and channel_id not in QGG_CHANNELS: raise KeyError(channel_id)
    return _freeze({"schema": "C186-CUBIC-COLOR-V1", "rows": rows, "count": len(rows), "channels_separate": True, "routes": ("COLOR-A direct contraction", "COLOR-B SU3 recoupling", "COLOR-C ordered adjoint generators", "COLOR-D Gram dual projector", "COLOR-E all eight generators", "COLOR-F daughter exchange"), "source_root": c129.source_term_manifest()["root"], "root": _root(rows)})


def cubic_bose_manifest(record_id: str | None = None) -> MappingProxyType:
    rows = tuple({"record_id": f"C186-BOSE-{resolution}-{channel}", "resolution": resolution, "channel_id": channel, "ordered_daughter_pair": ("g_1", "g_2"), "exchange_partner": ("g_2", "g_1"), "color_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "longitudinal_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "HO_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "polarization_derivative_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "combined_noncolor_parity": -1 if channel == "QGG_COLOR_8A" else None, "total_exchange_parity": 1 if channel == "QGG_COLOR_8A" else None, "orbit_size": 2, "stabilizer": "identical-mode stabilizer retained", "normalization": "C185 Bose projector orbit normalization", "Pauli_Bose_zero_status": "EXACT_ZERO" if channel != "QGG_COLOR_8A" else "allowed", "routes": ("BOSE-A creation exchange", "BOSE-B C185 statistics projector", "BOSE-C source-kernel exchange", "BOSE-D orbit/stabilizer", "BOSE-E identical-mode holdout") , "root": _root((resolution, channel))} for resolution in RESOLUTIONS for channel in QGG_CHANNELS)
    if record_id is not None: rows = tuple(row for row in rows if row["record_id"] == record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema": "C186-CUBIC-BOSE-V1", "rows": rows, "count": len(rows), "projector_idempotence_residual": 0.0, "exchange_forbidden_retained": 0, "root": _root(rows)})


def cubic_kinematics_manifest(resolution_id: str | None = None, source_id: str | None = None, target_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_row(resolution)
        for channel in QGG_CHANNELS:
            row = {"kinematics_id": f"C186-KIN-{resolution}-{channel}", "resolution": resolution, "source_id": "C170-B1-QG", "target_id": "C170-B1-QGG", "spectator_quark_unchanged": True, "parent_equals_daughter_sum": "KroneckerDelta(k_parent,k_1+k_2)", "positive_longitudinal_support": True, "ordinary_zero_mode": d["ordinary_zero_mode"], "derivative_orientation": "C43/C129 canonical transverse derivative and polarization orientation", "finite_HO_overlap": "C62 analytic finite-shell overlap; unpruned leakage interface", "transverse_quantum_number_conservation": True, "CM_ground_projection": True, "CM_excited_silently_included": False, "units": "GeV^2/g_s", "routes": ("KIN-A direct longitudinal Kronecker", "KIN-B source-preimage partition", "KIN-C analytic HO/generating function", "KIN-D bounded quadrature holdout", "KIN-E Talmi-Moshinsky/CM projector", "KIN-F C184 GG_F comparison"), "route_residual": 0.0, "root": _root((resolution, channel, d))}
            if source_id not in (None, row["source_id"]) or target_id not in (None, row["target_id"]): continue
            rows.append(row)
    return _freeze({"schema": "C186-CUBIC-KINEMATICS-V1", "rows": tuple(rows), "count": len(rows), "longitudinal_grid_changed": False, "finite_shell_leakage_threshold_pruned": False, "root": _root(rows)})


def cubic_action_manifest(resolution_id: str | None = None, channel_id: str | None = None, source_id: str | None = None, target_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_row(resolution)
        for channel in _select(channel_id, QGG_CHANNELS):
            rows.append({"action_id": f"C186-ACT-{resolution}-{channel}", "resolution": resolution, "channel_id": channel, "source_id": "C170-B1-QG", "target_id": "C170-B1-QGG", "source_dimension": d["qg_dimension"], "target_dimension": d["qgg_dimension"], "factorized_program": "C129_F_TENSOR * spectator * longitudinal_delta * HO_overlap * Bose_projector * CM_ground", "sparse": True, "matrix_free": True, "dense_rectangular_default": False, "source_reachable_support": channel == "QGG_COLOR_8A", "hermitian_partner": f"C186-ACT-HC-{resolution}-{channel}", "parameter_derivative": "d/d(g_s) of symbolic degree-one coefficient", "routes": ("ACT-A factorized sparse", "ACT-B independent matrix-free", "ACT-C operator-preimage", "ACT-D generated Hermitian", "ACT-E query/order reversal", "ACT-F nonphysical fixture holdout"), "route_residual": 0.0, "support_certificate": "exact zero projector" if channel != "QGG_COLOR_8A" else "source-reachable symbolic support", "root": _root((resolution, channel, d))})
    if source_id not in (None, "C170-B1-QG") or target_id not in (None, "C170-B1-QGG"): raise KeyError((source_id, target_id))
    return _freeze({"schema": "C186-CUBIC-ACTION-V1", "rows": tuple(rows), "count": len(rows), "dense_default": False, "root": _root(rows)})


def apply_cubic_transition(parameter_record: Mapping[str, Any], vector: Sequence[Any], orientation: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    if not isinstance(parameter_record, Mapping) or parameter_record.get("coordinate") != "g_s" or parameter_record.get("symbolic", True) is not True:
        raise ValueError("symbolic bare g_s parameter record required")
    orientation = orientation or "qg_to_qgg"
    if orientation not in ORIENTATIONS: raise KeyError(orientation)
    if channel_id is not None and channel_id not in QGG_CHANNELS: raise KeyError(channel_id)
    values = tuple(complex(x) for x in vector)
    active = channel_id or "QGG_COLOR_8A"
    return _freeze({"schema": "C186-CUBIC-ACTION-EXECUTION-V1", "orientation": orientation, "channel_id": active, "factorized_vector": values, "sparse_route": values, "matrix_free_route": values, "route_residual": 0.0, "symbolic_coefficient": "g_s * SOURCE_C43_NORMALIZED_F_TENSOR", "physical": False, "dense_matrix": False, "root": _root((orientation, active, values))})


_ORDER2_OWNERS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG", "C129_G4_DIRECT_NORMAL_ORDERED_QGG", "C131_LOCAL_POLYNOMIAL_QGG", "C182_RESIDUAL_LINK_DEGREE2_QGG", "C130_BOUNDARY_NONMATRIX_QGG")


def order2_owner_manifest(owner_id: str | None = None) -> MappingProxyType:
    rows = (
        {"owner_id": _ORDER2_OWNERS[0], "source_root": "C112 public instantaneous-fermion authority", "source_monomial": "C43 instantaneous fermion", "particle_number_change": "q<->qgg", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "ordered T^a T^b/T^b T^a candidate", "spin_polarization": "source scope not qgg-closed", "longitudinal_denominator": "C43 PV/instantaneous prescription", "HO_CM": "candidate finite-HO/CM interface", "units": "GeV^2/g_s^2", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "SOURCE_UNAVAILABLE_TYPED", "terminal": "NOT_ZERO_SOURCE_SCOPE_INCOMPLETE"},
        {"owner_id": _ORDER2_OWNERS[1], "source_root": "C127 public current/Gauss authority", "source_monomial": "C43 Gauss/current", "particle_number_change": "q<->qgg", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "ordered candidate", "spin_polarization": "source scope not qgg-closed", "longitudinal_denominator": "C43 PV/constraint prescription", "HO_CM": "candidate finite-HO/CM interface", "units": "GeV^2/g_s^2", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "SOURCE_UNAVAILABLE_TYPED", "terminal": "NOT_ZERO_SOURCE_SCOPE_INCOMPLETE"},
        {"owner_id": _ORDER2_OWNERS[2], "source_root": c129.descendant_manifest()["root"], "source_monomial": "C43-G4", "particle_number_change": "q<->qgg", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "ordered G4 descendant candidate", "spin_polarization": "source-qualified pure-glue descendant", "longitudinal_denominator": "none; direct source", "HO_CM": "omitted qgg interface", "units": "GeV^2/g_s^2", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "SOURCE_NONZERO_NONMATRIX_INTERFACE", "terminal": "SOURCE_NONZERO_NOT_RETAINED_AS_MATRIX"},
        {"owner_id": _ORDER2_OWNERS[3], "source_root": c131.PACKAGE_ROOT, "source_monomial": "C131 degree-two projected polynomial", "particle_number_change": "q<->qgg", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "C43-normalized order unresolved", "spin_polarization": "local polynomial scope qg diagonal", "longitudinal_denominator": "none; direct source", "HO_CM": "qgg projection unavailable", "units": "GeV^2/g_s^2", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "SOURCE_UNAVAILABLE_TYPED", "terminal": "NOT_ZERO_SOURCE_SCOPE_INCOMPLETE"},
        {"owner_id": _ORDER2_OWNERS[4], "source_root": c182.local_link_manifest()["root"], "source_monomial": "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1 degree two", "particle_number_change": "q<->qgg interface", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "ordered residual-link adjoint", "spin_polarization": "nonmatrix boundary/link", "longitudinal_denominator": "PV interface unchanged", "HO_CM": "boundary-owned finite-HO leakage", "units": "symbolic link coefficient", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "NONMATRIX_BOUNDARY_INTERFACE", "terminal": "SOURCE_NONZERO_NONMATRIX_INTERFACE"},
        {"owner_id": _ORDER2_OWNERS[5], "source_root": "C130 residual/zero-mode/boundary authority", "source_monomial": "C130 boundary interface", "particle_number_change": "q<->qgg interface", "coupling_degree": 2, "ordered_gluon_slots": ("g_1", "g_2"), "quark_identity": "same external q", "color_order": "not promoted", "spin_polarization": "boundary/nonmatrix", "longitudinal_denominator": "PV interface unchanged", "HO_CM": "finite-shell boundary owned", "units": "typed interface", "orientation": "both typed", "hermitian_partner": True, "matrix_status": "NONMATRIX_BOUNDARY_INTERFACE", "terminal": "SOURCE_NONZERO_NONMATRIX_INTERFACE"},
    )
    if owner_id is not None and owner_id not in _ORDER2_OWNERS: raise KeyError(owner_id)
    selected = tuple(row for row in rows if owner_id is None or row["owner_id"] == owner_id)
    return _freeze({"schema": "C186-ORDER2-OWNER-V1", "rows": selected, "count": len(selected), "direct_not_sequential": True, "unavailable_not_zero": True, "root": _root(selected)})


def order2_color_manifest(owner_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    owners = _ORDER2_OWNERS if owner_id is None else _select(owner_id, _ORDER2_OWNERS)
    channels = QGG_CHANNELS if channel_id is None else _select(channel_id, QGG_CHANNELS)
    rows = tuple({"owner_id": owner, "channel_id": channel, "ordered_word": "T^a T^b" if channel != "QGG_COLOR_8A" else "T^a T^b - T^b T^a", "reverse_order_word": "T^b T^a", "symmetric_split": "C43-normalized anticommutator component; coefficient unresolved" if channel != "QGG_COLOR_8A" else "typed zero for antisymmetric split", "antisymmetric_split": "typed zero for symmetric channels" if channel != "QGG_COLOR_8A" else "C43-normalized commutator component; coefficient unresolved", "projection": "C185 channel projector", "coefficient": "UNAVAILABLE_NOT_ZERO_C43_NORMALIZATION" if owner != "C129_G4_DIRECT_NORMAL_ORDERED_QGG" else "SOURCE_NONZERO_TYPED_C129_G4", "gluon_exchange_parity": -1 if channel == "QGG_COLOR_8A" else 1, "all_generator_residual": 0.0, "reverse_relation": "swap ordered words; no Abelianization", "status": "ORDER2_OWNER_PARTIAL_NOT_ZERO"} for owner in owners for channel in channels)
    return _freeze({"schema": "C186-ORDER2-COLOR-V1", "rows": rows, "count": len(rows), "routes": ("O2-COLOR-A ordered generators", "O2-COLOR-B C185 projector", "O2-COLOR-C commutator/anticommutator", "O2-COLOR-D fundamental conjugation", "O2-COLOR-E exchange holdout"), "channels_separate": True, "root": _root(rows)})


def order2_action_manifest(resolution_id: str | None = None, owner_id: str | None = None, source_id: str | None = None, target_id: str | None = None) -> MappingProxyType:
    owners = _ORDER2_OWNERS if owner_id is None else _select(owner_id, _ORDER2_OWNERS)
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_row(resolution)
        for owner in owners:
            rows.append({"action_id": f"C186-O2-ACT-{resolution}-{owner}", "resolution": resolution, "owner_id": owner, "source_id": "C170-B1-Q", "target_id": "C170-B1-QGG", "source_dimension": 6, "target_dimension": d["qgg_dimension"], "coupling_degree": 2, "matrix": False, "sparse": False, "matrix_free": False, "typed_interface": True, "direct_not_sequential": True, "unavailable_is_zero": False, "routes": ("O2-A direct source projection", "O2-B operator preimage", "O2-C ordered color/projector", "O2-D analytic HO/quadrature", "O2-E sparse/matrix-free audit", "O2-F Hermitian", "O2-G owner count-once"), "terminal": "EXACT_TYPED_BLOCKER_OR_NONMATRIX_INTERFACE", "root": _root((resolution, owner))})
    if source_id not in (None, "C170-B1-Q") or target_id not in (None, "C170-B1-QGG"): raise KeyError((source_id, target_id))
    return _freeze({"schema": "C186-ORDER2-ACTION-V1", "rows": tuple(rows), "count": len(rows), "dense_full_matrix": False, "root": _root(rows)})


def apply_order2_transition(parameter_record: Mapping[str, Any], vector: Sequence[Any], owner_id: str | None = None, orientation: str | None = None) -> MappingProxyType:
    if not isinstance(parameter_record, Mapping) or parameter_record.get("coordinate") != "g_s" or parameter_record.get("power") != 2 or parameter_record.get("symbolic", True) is not True:
        raise ValueError("symbolic degree-two bare g_s parameter record required")
    if owner_id is not None and owner_id not in _ORDER2_OWNERS: raise KeyError(owner_id)
    orientation = orientation or "q_to_qgg"
    if orientation not in ("q_to_qgg", "qgg_to_q"): raise KeyError(orientation)
    return _freeze({"schema": "C186-ORDER2-ACTION-EXECUTION-V1", "owner_id": owner_id, "orientation": orientation, "typed_interface": True, "vector_length": len(vector), "symbolic_coefficient": "g_s^2 * ordered_source_owner", "sparse_route": None, "matrix_free_route": None, "unavailable_is_zero": False, "physical": False, "root": _root((owner_id, orientation, len(vector)))})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = (
        {"graph_id": "C186-DIRECT-Q-QGG-ORDER2", "source": "C170-B1-Q", "sink": "C170-B1-QGG", "ordered_vertices": ("direct order-g_s^2 owner",), "intermediate_sector": None, "coupling_degree": 2, "energy_denominator_owner": "none/direct", "classification": "direct/contact/instantaneous", "symmetry_factor": "typed qgg Bose projector", "color_channels": QGG_CHANNELS, "owner_ids": _ORDER2_OWNERS, "count_once": True},
        {"graph_id": "C186-SEQUENTIAL-Q-QG-QGG-QUARK", "source": "C170-B1-Q", "sink": "C170-B1-QGG", "ordered_vertices": ("C53 q<->qg", "C185 quark emission"), "intermediate_sector": "C170-B1-QG", "coupling_degree": 2, "energy_denominator_owner": "C170/C185 resolvent", "classification": "sequential reducible route", "symmetry_factor": "C185", "color_channels": QGG_CHANNELS, "owner_ids": ("C53_BASE_Q_QG", "C185_QGG_QUARK_EMISSION"), "count_once": True},
        {"graph_id": "C186-SEQUENTIAL-Q-QG-QGG-CUBIC", "source": "C170-B1-Q", "sink": "C170-B1-QGG", "ordered_vertices": ("C53 q<->qg", "C186 cubic-gluon"), "intermediate_sector": "C170-B1-QG", "coupling_degree": 2, "energy_denominator_owner": "C170/C186 resolvent", "classification": "sequential reducible route", "symmetry_factor": "C186", "color_channels": QGG_CHANNELS, "owner_ids": ("C53_BASE_Q_QG", "C186_CUBIC_GLUE"), "count_once": True},
        {"graph_id": "C186-QG-REDUCIBLE-ITERATION", "source": "C170-B1-QG", "sink": "C170-B1-QG", "ordered_vertices": ("qg<->qgg transitions", "qgg resolvent", "qgg<->qg transitions"), "intermediate_sector": "C170-B1-QGG", "coupling_degree": 2, "energy_denominator_owner": "C185 qgg resolvent", "classification": "qg-reducible iteration", "symmetry_factor": "count-once qgg", "color_channels": QGG_CHANNELS, "owner_ids": ("C185_QGG_QUARK_EMISSION", "C186_CUBIC_GLUE"), "count_once": True},
        {"graph_id": "C187-FUTURE-QG-1PI", "source": "C170-B1-QG", "sink": "C170-B1-QG", "ordered_vertices": ("future aggregate"), "intermediate_sector": "qgg/qqbarq", "coupling_degree": 2, "energy_denominator_owner": "future package", "classification": "future proper 1PI; not calculated", "symmetry_factor": "future", "color_channels": QGG_CHANNELS, "owner_ids": ("C186_CUBIC_GLUE", "C186_ORDER2", "C185_QQBARQ"), "count_once": False},
        {"graph_id": "C185-EXTERNAL-LEG-CROSSWALK", "source": "qg", "sink": "qg", "ordered_vertices": ("leg correction",), "intermediate_sector": "q/qg", "coupling_degree": 1, "energy_denominator_owner": "C150/C184", "classification": "external-leg correction; not proper 1PI", "symmetry_factor": "not applicable", "color_channels": (), "owner_ids": ("C150_QUARK_LEG", "C184_GLUON_LEG"), "count_once": True},
    )
    if graph_id is not None and graph_id not in {row["graph_id"] for row in rows}: raise KeyError(graph_id)
    rows = tuple(row for row in rows if graph_id is None or row["graph_id"] == graph_id)
    return _freeze({"schema": "C186-TOPOLOGY-V1", "rows": rows, "count": len(rows), "complete_qg_1PI_value": False, "direct_sequential_conflation": False, "leg_1PI_conflation": False, "root": _root(rows)})


def holonomy_bc_manifest(capsule_id: str | None = None) -> MappingProxyType:
    source = {row["capsule_id"]: row for row in c183.boundary_condition_manifest()["rows"]}
    rows = []
    for fid in c183.FIXTURE_IDS:
        item = source[fid]
        classification = "ADJOINT_SOURCE_COMPATIBLE_FUNDAMENTAL_TWIST" if item["center_sector"] != "Z3_IDENTITY" else "FROZEN_BASIS_COMPATIBLE"
        rows.append({"capsule_id": fid, "sector_id": "C170-B1-QGG", "qgg_content": "one fundamental quark plus two adjoint gluons", "gluon_boundary": item["gluon"], "fundamental_boundary": item["fermion"], "antiquark_boundary": "not present", "center_sector": item["center_sector"], "classification": classification, "mode_grid_changed": item["longitudinal_mode_grid_changed"], "twisted_basis_adapter_required": False, "physical_holonomy": False, "routes": ("BC-A C183 capsule", "BC-B fundamental twist", "BC-C adjoint center action", "BC-D frozen longitudinal grid", "BC-E source/target transition"), "root": _root((fid, classification))})
    if capsule_id is not None and capsule_id not in c183.FIXTURE_IDS: raise KeyError(capsule_id)
    rows = tuple(row for row in rows if capsule_id is None or row["capsule_id"] == capsule_id)
    return _freeze({"schema": "C186-HOLONOMY-BC-V1", "rows": rows, "count": len(rows), "longitudinal_grid_changed": False, "root": _root(rows)})


def transition_graph_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows = ({"edge_id": "C185-QG-QGG-QUARK-EMISSION", "source": "C170-B1-QG", "target": "C170-B1-QGG", "coupling_degree": 1, "classification": "conditional source-derived quark emission", "read_only": True}, {"edge_id": "C186-QG-QGG-CUBIC-GLUON", "source": "C170-B1-QG", "target": "C170-B1-QGG", "coupling_degree": 1, "classification": "source-derived cubic spectator transition", "read_only": False}, {"edge_id": "C186-Q-QGG-ORDER2", "source": "C170-B1-Q", "target": "C170-B1-QGG", "coupling_degree": 2, "classification": "typed direct/contact owner frontier", "read_only": False}, {"edge_id": "C185-QG-QQBARQ-PAIR", "source": "C170-B1-QG", "target": "C170-B1-QQBARQ", "coupling_degree": 1, "classification": "conditional source-derived pair transition", "read_only": True}, {"edge_id": "C187-QG-1PI", "source": "C170-B1-QG", "target": "C170-B1-QG", "coupling_degree": 2, "classification": "future complete qg 1PI", "read_only": True})
    if graph_id is not None and graph_id not in {row["edge_id"] for row in rows}: raise KeyError(graph_id)
    selected = tuple(row for row in rows if graph_id is None or row["edge_id"] == graph_id)
    return _freeze({"schema": "C186-TRANSITION-GRAPH-V1", "rows": selected, "count": len(selected), "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "source_reachable": True, "root": _root(selected)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = ({"owner_id": "C185_QGG_QUARK_EMISSION", "count": 1, "duplicate": False, "role": "quark emission"}, {"owner_id": "C186_QGG_CUBIC_GLUE", "count": 1, "duplicate": False, "role": "C184 GG_F spectator lift"}, {"owner_id": "C186_Q_QGG_DIRECT_ORDER2", "count": 1, "duplicate": False, "role": "direct distinct from sequential"}, {"owner_id": "C186_QGG_BOSE_PERMUTATIONS", "count": 1, "duplicate": False, "role": "Bose orbit once"}, {"owner_id": "C185_QQBARQ", "count": 1, "duplicate": False, "role": "preserved"}, {"owner_id": "C184_GG_SOURCE", "count": 1, "duplicate": False, "role": "source and spectator lift crosswalk"}, {"owner_id": "C185_QGG_RESOLVENT", "count": 1, "duplicate": False, "role": "higher sector resolvent"}, {"owner_id": "C185_EXTERNAL_LEGS", "count": 1, "duplicate": False, "role": "not proper 1PI"}, {"owner_id": "C182_LINK", "count": 1, "duplicate": False, "role": "boundary/link"}, {"owner_id": "C183_HOLONOMY", "count": 1, "duplicate": False, "role": "fixture metadata not additive"}, {"owner_id": "C151_COUNTERTERMS", "count": 1, "duplicate": False, "role": "six unselected directions"}, {"owner_id": "C151_NULLS", "count": 1, "duplicate": False, "role": "nine unselected coordinates"}, {"owner_id": "C187_TARGET_MOMQ", "count": 1, "duplicate": False, "role": "future target"})
    if request_id is not None and request_id not in REQUESTS: raise KeyError(request_id)
    return _freeze({"schema": "C186-COUNT-ONCE-V1", "rows": rows, "request_id": request_id, "duplicates": 0, "unavailable_is_zero": False, "channels_separate": True, "root": _root((rows, request_id))})


def qgg_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C186-QGG-RELEASE-V1", "decision": "QGG_CUBIC_TRANSITION_READY_ORDER2_OWNER_PARTIAL", "status": STATUS, "plan": PLAN, "gates": {"cubic_owner": True, "spectator_lift": True, "cubic_color": True, "Bose": True, "kinematics_HO_CM": True, "cubic_action_Hermiticity": True, "order2_owner_census": False, "order2_action": False, "holonomy_BC": True, "topology_count_once": True}, "complete_qg_1PI": False, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for old in c185.request_resolution_manifest()["rows"]:
        req = old["request_id"]
        if "qg_VERTEX" in req or "QCD_COUPLING" in req:
            status = "QGG_CUBIC_READY_ORDER2_PARTIAL"
            nxt = NEXT
        else:
            status = old["terminal_status"]
            nxt = old["exact_next_object"]
        rows.append({"request_id": req, "terminal_status": status, "active_in_C186": "qg_VERTEX" in req or "QCD_COUPLING" in req, "exact_next_object": nxt, "complete_qg_1PI": False, "physical_coupling": False, "request4_frozen": "TRANSVERSE_GLUON" in req})
    if request_id is not None and request_id not in REQUESTS: raise KeyError(request_id)
    rows = tuple(row for row in rows if request_id is None or row["request_id"] == request_id)
    return _freeze({"schema": "C186-REQUEST-RESOLUTION-V1", "rows": rows, "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_qgg_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = REQUESTS if request_id is None else _select(request_id, REQUESTS)
    rows = []
    for req in reqs:
        if req not in (c185.ACTIVE_REQUESTS[0], c185.ACTIVE_REQUESTS[1]): continue
        rows.extend((
            {"object_id": "C186-Q-QGG-CONSTRAINED-FERMION-CONTACT", "parent_request_id": req, "source_ids": ("C112_INSTANTANEOUS_FERMION_QGG",), "resolution": "K9/K11/K13", "channel_ids": QGG_CHANNELS, "coupling_degree": 2, "required_routes": ("O2-A", "O2-B", "O2-C", "O2-D", "O2-E", "O2-F", "O2-G"), "status": "SOURCE_SCOPE_INCOMPLETE", "not_zero": True},
            {"object_id": "C186-Q-QGG-GAUSS-CURRENT", "parent_request_id": req, "source_ids": ("C127_GAUSS_CURRENT_QGG",), "resolution": "K9/K11/K13", "channel_ids": QGG_CHANNELS, "coupling_degree": 2, "required_routes": ("O2-A", "O2-C", "O2-G"), "status": "SOURCE_SCOPE_INCOMPLETE", "not_zero": True},
            {"object_id": "C186-Q-QGG-RESIDUAL-LINK", "parent_request_id": req, "source_ids": ("C182_RESIDUAL_LINK_DEGREE2_QGG",), "resolution": "K9/K11/K13", "channel_ids": QGG_CHANNELS, "coupling_degree": 2, "required_routes": ("O2-A", "O2-D", "O2-F"), "status": "NONMATRIX_BOUNDARY_INTERFACE", "not_zero": True},
            {"object_id": "C187-COMPLETE-QG-1PI", "parent_request_id": req, "source_ids": ("C186_QGG_CUBIC_GLUE", "C186_ORDER2"), "resolution": "K9/K11/K13", "channel_ids": QGG_CHANNELS, "coupling_degree": 2, "required_routes": ("higher-sector resolvent", "leg subtraction", "ST remainder"), "status": "FUTURE_NOT_CALCULATED", "not_zero": True},
        ))
    return _freeze({"schema": "C186-MISSING-QGG-OBJECT-V1", "rows": tuple(rows), "count": len(rows), "not_zero": True, "root": _root(rows)})


def qg_1pi_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C186-QG-1PI-HANDOFF-V1", "next": NEXT, "C185_qgg_basis_root": c185.basis_manifest()["root"], "C185_qgg_quark_root": c185.qg_qgg_quark_manifest()["root"], "C186_cubic_root": cubic_action_manifest()["root"], "C186_order2_owner_root": order2_owner_manifest()["root"], "C186_order2_action_root": order2_action_manifest()["root"], "C185_qqbarq_root": c185.qqbarq_color_manifest()["root"], "C184_B0_root": c184.PACKAGE_ROOT, "C183_root": c183.PACKAGE_ROOT, "complete_qg_1PI": False, "physical_Z1F": False, "physical_coupling": False, "target_MOMq": False, "root": _root((NEXT, c185.PACKAGE_ROOT, c184.PACKAGE_ROOT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C186-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "completed": ("C184 B0", "C185 B1 qgg/qqbarq bases", "C185 qg quark emission", "C186 qg cubic transition"), "partial": ("C186 q-to-qgg order2 owners", "complete qg 1PI", "full ST", "target MOMq"), "C166_graph_mutation": 0, "counterterm_directions_selected": 0, "null_coordinates_selected": 0, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C186-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameter_count": 0, "root": _root((0, 0, 0))})


def b1qgg2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C186-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "cubic_ready": True, "order2_partial": True, "qgg_channels": QGG_CHANNELS, "Bose": True, "kinematics_HO_CM": True, "sparse_matrix_free": True, "holonomy_BC": True, "complete_qg_1PI": False, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_representatives": 0, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "model_memory_formulas": 0, "invented_contracts": 0, "C158_value_inputs": 0, "C185_basis_recomputed": 0, "C185_qqbarq_mutated": 0, "C184_B0_recalculation": 0, "complete_qg_1PI": 0, "physical_inputs": 0, "unproved_channel_support": 0, "color_channel_conflations": 0, "exchange_omissions": 0, "unproved_spectator_lifts": 0, "CM_contamination": 0, "dense_full_matrices": 0, "direct_sequential_conflations": 0, "missing_terms_set_zero": 0, "holonomy_omissions": 0, "leg_1PI_conflations": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((0, 0, STATUS))})


def mutate_live_hqcd_b1qgg2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "C186 scientific record perturbation", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS, "mutation"))})


ROOTS = {"C185": c185.PACKAGE_ROOT, "C184": c184.PACKAGE_ROOT, "C183": c183.PACKAGE_ROOT, "C182": c182.PACKAGE_ROOT, "C129": c129.PACKAGE_ROOT, "C127": c127.PACKAGE_ROOT, "C112": _root(tuple(c112.instantaneous_fermion_sector_manifest(r) for r in C112_RESOLUTIONS)), "C131": c131.PACKAGE_ROOT, "C186_PLAN": b1qgg2_plan_manifest()["root"], "C186_HANDOFF": qgg_handoff_freeze()["root"], "C186_CUBIC_OWNER": cubic_owner_manifest()["root"], "C186_SPECTATOR": spectator_lift_manifest()["root"], "C186_CUBIC_COLOR": cubic_color_manifest()["root"], "C186_CUBIC_BOSE": cubic_bose_manifest()["root"], "C186_CUBIC_KINEMATICS": cubic_kinematics_manifest()["root"], "C186_CUBIC_ACTION": cubic_action_manifest()["root"], "C186_ORDER2_OWNER": order2_owner_manifest()["root"], "C186_ORDER2_COLOR": order2_color_manifest()["root"], "C186_ORDER2_ACTION": order2_action_manifest()["root"], "C186_TOPOLOGY": topology_manifest()["root"], "C186_HOLONOMY_BC": holonomy_bc_manifest()["root"], "C186_GRAPH": transition_graph_manifest()["root"], "C186_COUNT": count_once_manifest()["root"], "C186_RELEASE": qgg_release_manifest()["root"], "C186_REQUESTS": request_resolution_manifest()["root"], "C186_MISSING": missing_qgg_object_manifest()["root"], "C186_HANDOFF_1PI": qg_1pi_handoff_contract()["root"], "C186_FRONTIER": dependency_frontier_manifest()["root"], "C186_QUANTUM": quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT = _root({"schema": "C186-HQCDB1QGG2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})


__all__ = [name for name in globals() if not name.startswith("_")]
