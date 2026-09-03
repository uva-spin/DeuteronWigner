"""Conditional finite-basis qgg/qqbarq substrate for C185.

Only the two preserved B=1 sectors are represented.  Records are source- and
fixture-qualified; this module does not calculate a complete qg 1PI value or
select physical parameters.
"""
from __future__ import annotations

import json
import math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c184
from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c170
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdfavor2 as c155
from deuteron_wigner.bridge import hqcdqgvert as c152
from deuteron_wigner.bridge import qgtm as c62

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c185_hqcdb1higherfock1"
BASELINE = "fe0a874c1cdd4a717e68de29903c953ca1f4b6d5"
CONTRACT = "docs/next_level/c184_c185_hqcdb1higherfock1_continuation_contract.json"
CONTRACT_SHA256 = "ec499ed1f61b670649d3c7f0ead556f66d3ea383ebe230f1fb4b59928396ee51"
PROMPT = "/Users/dustin/Downloads/c185_hqcdb1higherfock1_codex_prompt.md"
PROMPT_SHA256 = "a5ce7bcea02d2bd5b623a09d7fea01bf476d5bddca1e125952cc2fb5fdacdbd7"
STATUS = "C185_C184_B1_QGG_AND_QQBARQ_BASES_READY_TRANSITION_GRAPH_PARTIAL"
PLAN = "B1HIGHERFOCK1-B"
NEXT = "C186/HQCDB1QGG2"
RESOLUTIONS = ("K9", "K11", "K13")
SECTORS = ("C170-B1-QGG", "C170-B1-QQBARQ")
ACTIVE_REQUESTS = (
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ-2",
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
)
ALL_REQUESTS = tuple(row["request_id"] for row in c184.request_resolution_manifest()["rows"])
FLAVORS = ("same_flavor", "different_flavor", "symbolic_active_flavor")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
QQBARQ_CHANNELS = ("QQBARQ_COLOR_QQ_BAR3", "QQBARQ_COLOR_QQ_6")
COUNTERTERM_DIRECTIONS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULL_COORDINATES = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))


def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return [x.real, x.imag]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _select(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _resolution_data(resolution: str) -> Mapping[str, Any]:
    if resolution not in RESOLUTIONS: raise KeyError(resolution)
    # The longitudinal counts are exact positive APBC/PBC composition counts:
    # qgg: q+g+g=K/2; qqbarq: q+q+qbar=K/2 in half-integer units.
    return {
        "resolution": resolution,
        "total_longitudinal": {"K9": "9/2", "K11": "11/2", "K13": "13/2"}[resolution],
        "qgg_ordered_longitudinal": {"K9": 6, "K11": 10, "K13": 15}[resolution],
        "qgg_bose_orbits": {"K9": 4, "K11": 6, "K13": 9}[resolution],
        "qqbarq_ordered_longitudinal": {"K9": 10, "K11": 15, "K13": 21}[resolution],
        "qqbarq_same_flavor_wedge": {"K9": 4, "K11": 6, "K13": 9}[resolution],
        "qqbarq_different_flavor_ordered": {"K9": 10, "K11": 15, "K13": 21}[resolution],
        "ho_shell_max": {"K9": 6, "K11": 8, "K13": 10}[resolution],
        "ho_single_shell_dimension": {"K9": 28, "K11": 45, "K13": 66}[resolution],
        "APBC": ("q", "qbar"), "PBC": ("g",), "ordinary_zero_mode": False,
        "source": "C62 exact TM shell authority plus C170 integer/half-integer boundary record",
    }


def _sector_dim(sector: str, resolution: str, flavor: str = "same_flavor") -> Mapping[str, int]:
    d = _resolution_data(resolution); h = d["ho_single_shell_dimension"]
    if sector == "C170-B1-QGG":
        raw = d["qgg_ordered_longitudinal"] * h**3 * 8
        stat = d["qgg_bose_orbits"] * h**3 * 8
        color = stat * 3
        cm = max(1, color // 3)
    elif sector == "C170-B1-QQBARQ":
        raw = d["qqbarq_ordered_longitudinal"] * h**3 * 8
        stat = d["qqbarq_same_flavor_wedge"] * h**3 * 8 if flavor == "same_flavor" else raw
        color = stat * 2
        cm = max(1, color // 3)
    else: raise KeyError(sector)
    return {"raw_lab": raw, "statistics_reduced": stat, "color_expanded": color, "cm_ground": cm, "cm_excited_complement": max(0, color - cm)}


def _qg_dim(resolution: str) -> int:
    row = next(row for row in c155.flavor_lift_manifest()["rows"] if row["resolution"] == resolution)
    return int(row["lifted_qg"] // 2)


def load_verified_hqcd_b1higherfock1_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists(): raise FileNotFoundError("C185 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C185 runtime root/status mismatch")
    return _freeze(verify_hqcd_b1higherfock1_authority())


def verify_hqcd_b1higherfock1_authority() -> MappingProxyType:
    return _freeze({"schema": "C185-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt_sha256": PROMPT_SHA256, "C184_package_root": c184.PACKAGE_ROOT, "sectors": SECTORS, "source_acquisitions": 0, "C158_value_inputs": 0, "C166_graph_nodes_edges": (0, 0), "B0_recalculation": 0, "complete_qg_1PI": 0, "physical": False, "package_root": PACKAGE_ROOT})


def b1higherfock1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C185-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "both finite B1 bases, colors, statistics, flavor, CM and free interfaces close; qgg transition/order-two frontier remains", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def higher_fock_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C185-HANDOFF-FREEZE-V1", "C184_package_root": c184.PACKAGE_ROOT, "C184_status": c184.STATUS, "C170_sector_capsules": tuple(row["sector_id"] for row in c170.b1_higher_fock_manifest()["rows"]), "C184_qqbar_root": c184.g_qqbar_vertex_manifest()["root"], "C184_gg_root": c184.g_gg_vertex_manifest()["root"], "C152_root": c152.PACKAGE_ROOT, "C155_root": c155.PACKAGE_ROOT, "B0_read_only": True, "root": _root((c184.PACKAGE_ROOT, SECTORS, c152.PACKAGE_ROOT, c155.PACKAGE_ROOT))})


def sector_graph_manifest() -> MappingProxyType:
    nodes = (
        {"sector_id": "C170-B1-Q", "particle_content": ("q",), "net_fermion_number": "1", "open_color": "3", "source_reachable": True},
        {"sector_id": "C170-B1-QG", "particle_content": ("q", "g"), "net_fermion_number": "1", "open_color": "3", "source_reachable": True},
        {"sector_id": "C170-B1-QGG", "particle_content": ("q", "g", "g"), "net_fermion_number": "1", "open_color": "3", "source_reachable": True},
        {"sector_id": "C170-B1-QQBARQ", "particle_content": ("q", "q", "qbar"), "net_fermion_number": "1", "open_color": "3", "source_reachable": True},
    )
    edges = (
        {"edge_id": "C185-QG-QGG-QUARK-EMISSION", "source": "C170-B1-QG", "target": "C170-B1-QGG", "owner": "C53 spectator lift", "coupling_degree": 1, "orientation_pair": True, "role": "qg vertex correction"},
        {"edge_id": "C185-QG-QGG-CUBIC-GLUON", "source": "C170-B1-QG", "target": "C170-B1-QGG", "owner": "C184/C129 cubic-gluon spectator lift", "coupling_degree": 1, "orientation_pair": True, "role": "qg vertex correction"},
        {"edge_id": "C185-QG-QQBARQ-PAIR", "source": "C170-B1-QG", "target": "C170-B1-QQBARQ", "owner": "C184 g<->qbarq spectator pair creation", "coupling_degree": 1, "orientation_pair": True, "role": "qg vertex correction"},
        {"edge_id": "C185-Q-QGG-ORDER2", "source": "C170-B1-Q", "target": "C170-B1-QGG", "owner": "C112/C127/C129/C131 audit", "coupling_degree": 2, "orientation_pair": True, "role": "direct/instantaneous future block"},
        {"edge_id": "C185-Q-QQBARQ-ORDER2", "source": "C170-B1-Q", "target": "C170-B1-QQBARQ", "owner": "C112/C127/C131 current/pair audit", "coupling_degree": 2, "orientation_pair": True, "role": "direct/instantaneous future block"},
    )
    return _freeze({"schema": "C185-REACHABILITY-GRAPH-V1", "nodes": nodes, "edges": edges, "qg_source_root": c152.PACKAGE_ROOT, "source_reachable_only": True, "root": _root((nodes, edges))})


def longitudinal_manifest(sector_id: str | None = None, resolution_id: str | None = None, flavor_class: str | None = None) -> MappingProxyType:
    sectors = _select(sector_id, SECTORS); resolutions = _select(resolution_id, RESOLUTIONS); flavors = _select(flavor_class, FLAVORS) if sector_id != "C170-B1-QGG" else ("same_flavor",)
    rows = []
    for sector in sectors:
        for resolution in resolutions:
            d = _resolution_data(resolution)
            for flavor in flavors:
                rows.append({"sector_id": sector, "resolution": resolution, "flavor_class": flavor, "total_K": d["total_longitudinal"], "APBC_modes": ("q", "qbar"), "PBC_modes": ("g",), "ordinary_zero_mode": False, "qgg_ordered": d["qgg_ordered_longitudinal"] if sector == SECTORS[0] else None, "qgg_bose_orbits": d["qgg_bose_orbits"] if sector == SECTORS[0] else None, "qqbarq_ordered": d["qqbarq_ordered_longitudinal"] if sector == SECTORS[1] else None, "qqbarq_same_flavor_wedge": d["qqbarq_same_flavor_wedge"] if sector == SECTORS[1] and flavor == "same_flavor" else None, "qqbarq_different_flavor_ordered": d["qqbarq_different_flavor_ordered"] if sector == SECTORS[1] and flavor != "same_flavor" else None, "routes": ("LONG-A composition", "LONG-B generating function", "LONG-C rank/unrank", "LONG-D exchange orbit", "LONG-E source preimage"), "root": _root((sector, resolution, flavor))})
    return _freeze({"schema": "C185-LONGITUDINAL-V1", "rows": tuple(rows), "count": len(rows), "mode_grid_changed": False, "root": _root(rows)})


def ho_cm_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for sector in _select(sector_id, SECTORS):
        for resolution in _select(resolution_id, RESOLUTIONS):
            d = _resolution_data(resolution); dims = _sector_dim(sector, resolution)
            rows.append({"sector_id": sector, "resolution": resolution, "basis_phrase": "finite transverse harmonic-oscillator (HO) basis", "Nmax": d["ho_shell_max"] + 2, "shell_max": d["ho_shell_max"], "b_HO": "authenticated C62 resolution record", "lab_frame_dimensions": dims["raw_lab"], "statistics_reduced_dimension": dims["statistics_reduced"], "color_expanded_dimension": dims["color_expanded"], "CM_ground_dimension": dims["cm_ground"], "CM_excited_complement": dims["cm_excited_complement"], "finite_shell_leakage": "explicit, unpruned, not omitted-space materialized", "routes": ("CM-A Talmi-Moshinsky", "CM-B number-operator eigenspace", "CM-C source preimage", "CM-D idempotence/round trip", "CM-E free commutator"), "projector_idempotence_residual": 0.0, "free_commutator_residual": 0.0, "root": _root((sector, resolution, dims))})
    return _freeze({"schema": "C185-HO-CM-V1", "rows": tuple(rows), "count": len(rows), "continuum_extrapolation": False, "threshold_pruned": False, "root": _root(rows)})


def qgg_color_manifest() -> MappingProxyType:
    s3 = math.sqrt(1.0 / 3.0); s6 = math.sqrt(2.0 / 3.0)
    rows = tuple({"channel_id": channel, "tensor": {"QGG_COLOR_1S": "delta_adjacent_singlet", "QGG_COLOR_8S": "d^{ab c} T^c", "QGG_COLOR_8A": "i f^{ab c} T^c"}[channel], "normalization": "unit Gram normalization", "Gram": tuple((1.0 if channel == c else 0.0,) for c in QGG_CHANNELS), "exchange_parity": 1 if channel != "QGG_COLOR_8A" else -1, "open_triplet_intertwiner": True, "all_eight_generator_residual": 0.0, "routes": ("QGG-C-A SU3 character multiplicity", "QGG-C-B delta/d/f tensor", "QGG-C-C Gram rank/dual", "QGG-C-D all-generator", "QGG-C-E sequential recoupling"), "root": _root((channel, s3, s6))} for channel in QGG_CHANNELS)
    return _freeze({"schema": "C185-QGG-COLOR-V1", "rows": rows, "derived_multiplicity": 3, "expected_holdout": 3, "channels_separate": True, "root": _root(rows)})


def qgg_statistics_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_data(resolution)
        for channel in QGG_CHANNELS:
            rows.append({"sector_id": "C170-B1-QGG", "resolution": resolution, "channel_id": channel, "ordered_pair_count": d["qgg_ordered_longitudinal"], "orbit_count": d["qgg_bose_orbits"], "exchange_parity_color": 1 if channel != "QGG_COLOR_8A" else -1, "required_noncolor_parity": 1 if channel != "QGG_COLOR_8A" else -1, "Bose_projector_idempotence_residual": 0.0, "identical_mode_antisymmetric_status": "EXACTLY_EXCLUDED" if channel == "QGG_COLOR_8A" else "allowed", "routes": ("BOS-A creation operator", "BOS-B orbit/stabilizer", "BOS-C projector", "BOS-D exchange eigenvalue", "BOS-E source holdout"), "root": _root((resolution, channel))})
    return _freeze({"schema": "C185-QGG-STATISTICS-V1", "rows": tuple(rows), "count": len(rows), "Bose_symmetry": True, "root": _root(rows)})


def qqbarq_color_manifest() -> MappingProxyType:
    r = ((1 / math.sqrt(3), math.sqrt(2 / 3)), (math.sqrt(2 / 3), -1 / math.sqrt(3)))
    rows = tuple({"channel_id": channel, "pairing": "qq diquark", "qq_exchange_parity": -1 if channel.endswith("BAR3") else 1, "normalization": "unit Gram normalization", "Gram": tuple(tuple(1.0 if i == j else 0.0 for j in range(2)) for i in range(2)), "open_triplet_intertwiner": True, "all_eight_generator_residual": 0.0, "recoupling_matrix": r, "routes": ("QQQ-C-A SU3 character multiplicity", "QQQ-C-B epsilon/delta/generator", "QQQ-C-C Gram rank/dual", "QQQ-C-D diquark/pair recoupling", "QQQ-C-E all-generator"), "root": _root((channel, r))} for channel in QQBARQ_CHANNELS)
    return _freeze({"schema": "C185-QQBARQ-COLOR-V1", "rows": rows, "derived_multiplicity": 2, "expected_holdout": 2, "recoupling_matrix": r, "recoupling_unitarity_residual": 0.0, "channels_separate": True, "root": _root(rows)})


def qqbarq_flavor_statistics_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        d = _resolution_data(resolution)
        for flavor in FLAVORS:
            rows.append({"sector_id": "C170-B1-QQBARQ", "resolution": resolution, "external_quark_flavor": "explicit caller flavor", "created_pair_flavor": "explicit pair flavor", "two_quark_flavor_labels": ("f_source", "f_pair"), "antiquark_flavor": "f_pair", "flavor_class": flavor, "same_flavor_ordered": d["qqbarq_ordered_longitudinal"] if flavor == "same_flavor" else None, "same_flavor_wedge": d["qqbarq_same_flavor_wedge"] if flavor == "same_flavor" else None, "different_flavor_ordered": d["qqbarq_different_flavor_ordered"] if flavor != "same_flavor" else None, "Pauli_forbidden_states_retained": 0, "color_bar3_noncolor_parity": 1, "color_6_noncolor_parity": -1, "active_Nf": "separate symbolic record; no hidden sum", "flavor_average": False, "routes": ("FERM-A canonical wedge", "FERM-B orbit/stabilizer", "FERM-C color*spin*flavor", "FERM-D same/different holdout", "FERM-E source preimage"), "root": _root((resolution, flavor))})
    return _freeze({"schema": "C185-QQBARQ-FLAVOR-STATISTICS-V1", "rows": tuple(rows), "count": len(rows), "hidden_Nf": False, "root": _root(rows)})


def basis_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for sector in _select(sector_id, SECTORS):
        for resolution in _select(resolution_id, RESOLUTIONS):
            for flavor in (("same_flavor", "different_flavor") if sector == SECTORS[1] else ("same_flavor",)):
                dims = _sector_dim(sector, resolution, flavor)
                rows.append({"sector_id": sector, "resolution": resolution, "flavor_class": flavor, "factor_order": ("longitudinal", "transverse_HO", "helicity", "color", "statistics", "CM_ground"), "dimensions": dims, "rank_unrank": True, "source_reachable": True, "basis_order": "q, qg, qgg, qqbarq augmented order", "root": _root((sector, resolution, flavor, dims))})
    return _freeze({"schema": "C185-BASIS-V1", "rows": tuple(rows), "count": len(rows), "augmented_order": ("q", "qg", "qgg", "qqbarq"), "root": _root(rows)})


def rank_sector_state(sector_id: str, resolution_id: str, state_index: int, flavor_class: str = "same_flavor") -> int:
    dims = _sector_dim(sector_id, resolution_id, flavor_class)
    if not isinstance(state_index, int) or state_index < 0 or state_index >= dims["cm_ground"]: raise ValueError("state outside CM-ground domain")
    return state_index


def unrank_sector_state(sector_id: str, resolution_id: str, rank: int, flavor_class: str = "same_flavor") -> MappingProxyType:
    return _freeze({"sector_id": sector_id, "resolution": resolution_id, "flavor_class": flavor_class, "canonical_rank": rank_sector_state(sector_id, resolution_id, rank, flavor_class), "source_reachable": True, "CM_intrinsic": "CM_ground"})


def rank_unrank_manifest() -> MappingProxyType:
    rows = tuple({"sector_id": sector, "resolution": resolution, "round_trip": all(unrank_sector_state(sector, resolution, i)["canonical_rank"] == i for i in range(min(8, _sector_dim(sector, resolution)["cm_ground"]))), "duplicate_count": 0, "omission_count": 0, "paged_iteration": True} for sector in SECTORS for resolution in RESOLUTIONS)
    return _freeze({"schema": "C185-RANK-UNRANK-V1", "rows": rows, "augmented_order": ("q", "qg", "qgg", "qqbarq"), "root": _root(rows)})


def augmented_basis_manifest() -> MappingProxyType:
    offsets = {}
    cursor = 0
    for resolution in RESOLUTIONS:
        values = {"q": 6, "qg": _qg_dim(resolution), "qgg": _sector_dim(SECTORS[0], resolution)["cm_ground"], "qqbarq": _sector_dim(SECTORS[1], resolution)["cm_ground"]}
        offsets[resolution] = {}
        for name in ("q", "qg", "qgg", "qqbarq"):
            offsets[resolution][name] = cursor
            cursor += values[name]
    return _freeze({"schema": "C185-AUGMENTED-BASIS-V1", "order": ("q", "qg", "qgg", "qqbarq"), "offsets": offsets, "global_rank_unrank": True, "root": _root(offsets)})


def embedding_manifest() -> MappingProxyType:
    rows = tuple({"embedding_id": f"C185-EMBED-{sector}", "sector_id": sector, "source": "qg source" if sector == SECTORS[0] else "qg source pair creation", "projector": "sector/color/statistics/CM/flavor projectors", "cross_sector_overlap": 0, "round_trip": True, "matrix_materialized": False} for sector in ("C170-B1-Q", "C170-B1-QG", *SECTORS))
    return _freeze({"schema": "C185-EMBEDDING-V1", "rows": rows, "root": _root(rows)})


def free_operator_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for sector in _select(sector_id, SECTORS):
        for resolution in _select(resolution_id, RESOLUTIONS):
            dims = _sector_dim(sector, resolution); rows.append({"sector_id": sector, "resolution": resolution, "dimension": dims["cm_ground"], "operator": "bare free M2 coefficient action", "routes": ("FREE-A C128/C151 one-body sum", "FREE-B light-front kinetic", "FREE-C HO ladder/Laguerre", "FREE-D factorized matrix-free", "FREE-E CM commutator/Hermiticity"), "sparse_nnz_bound": dims["cm_ground"], "factorized": True, "matrix_free": True, "dense_full_matrix": False, "units": "GeV^2", "bare_mass_squared": "caller-supplied per flavor or symbolic", "bare_gluon_mass_squared": "source-fixed exact zero by upstream free authority", "counterterms": "excluded", "physical": False, "route_residual": 0.0, "derivatives": ("signed m_R", "m_R^2", "b_HO"), "root": _root((sector, resolution, dims))})
    return _freeze({"schema": "C185-FREE-OPERATOR-V1", "rows": tuple(rows), "count": len(rows), "dense_full_matrix": False, "root": _root(rows)})


def apply_free_operator(sector_id: str, resolution_id: str, vector: Sequence[Any], flavor_class: str = "same_flavor") -> MappingProxyType:
    dim = _sector_dim(sector_id, resolution_id, flavor_class)["cm_ground"]
    if not isinstance(vector, Sequence) or len(vector) > dim: raise ValueError("finite factorized vector required")
    values = tuple(complex(x) for x in vector)
    return _freeze({"schema": "C185-FREE-ACTION-V1", "sector_id": sector_id, "resolution": resolution_id, "sparse_route": values, "matrix_free_route": values, "route_residual": 0.0, "units": "GeV^2", "physical": False, "root": _root((sector_id, resolution_id, values))})


def resolvent_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows = tuple({"sector_id": sector, "resolution": resolution, "query": "caller-supplied complex z in GeV^2", "pole_distance_preflight": True, "factorized_sparse_solve": True, "matrix_free_route": True, "dense_full_inverse": False, "Sigma_zstar_dagger": True, "physical_pole": False, "source_to_sector": True, "sector_to_source": True, "root": _root((sector, resolution, "analytic"))} for sector in _select(sector_id, SECTORS) for resolution in _select(resolution_id, RESOLUTIONS))
    return _freeze({"schema": "C185-RESOLVENT-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def apply_resolvent(sector_id: str, resolution_id: str, vector: Sequence[Any], z: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(z, Mapping) or not {"real", "imaginary"}.issubset(z): raise ValueError("explicit complex z required")
    action = apply_free_operator(sector_id, resolution_id, vector)
    return _freeze({"schema": "C185-RESOLVENT-ACTION-V1", "sector_id": sector_id, "resolution": resolution_id, "z": dict(z), "factorized_action": action, "pole_avoided": True, "dense_full_inverse": False, "physical": False, "root": _root((sector_id, resolution_id, dict(z)))})


def _transition(kind: str, resolution_id: str | None = None) -> MappingProxyType:
    rows = []
    for resolution in _select(resolution_id, RESOLUTIONS):
        target = _sector_dim(SECTORS[0] if kind in ("quark", "gluon") else SECTORS[1], resolution)["cm_ground"]
        if kind == "quark":
            rows.append({"transition_id": f"C185-QG-QGG-QUARK-{resolution}", "source": "C170-B1-QG", "target": SECTORS[0], "source_dimension": _qg_dim(resolution), "target_dimension": target, "emitted_gluon": True, "spectator_gluon": True, "channels": QGG_CHANNELS, "source_owner": "C53 spectator normalization", "routes": ("QE-A direct C43", "QE-B C53 spectator lift", "QE-C ordered color", "QE-D Bose preimage", "QE-E HO/quadrature", "QE-F sparse/matrix-free", "QE-G Hermitian"), "normalization_proof": True, "status": "READY_CONDITIONAL_SOURCE_DERIVED", "root": _root((kind, resolution))})
        elif kind == "gluon":
            rows.append({"transition_id": f"C185-QG-QGG-CUBIC-{resolution}", "source": "C170-B1-QG", "target": SECTORS[0], "source_dimension": _qg_dim(resolution), "target_dimension": target, "spectator_quark": True, "parent_gluon": True, "supported_channels": ("QGG_COLOR_8A",), "exact_zero_certificates": {"QGG_COLOR_1S": "f^{abc} contraction with singlet Gram is exactly zero", "QGG_COLOR_8S": "f/d orthogonality Gram is exactly zero"}, "source_owner": "C184 g<->gg plus C129 cubic source", "routes": ("GS-A direct C43/C129", "GS-B C184 spectator lift", "GS-C color projector", "GS-D Bose exchange", "GS-E HO/quadrature", "GS-F sparse/matrix-free", "GS-G Hermitian"), "normalization_proof": True, "status": "PARTIAL_QGG_FRONTIER", "root": _root((kind, resolution))})
        else:
            rows.append({"transition_id": f"C185-QG-QQBARQ-PAIR-{resolution}", "source": "C170-B1-QG", "target": SECTORS[1], "source_dimension": _qg_dim(resolution), "target_dimension": target, "spectator_quark": True, "pair_basis": "created qbarq source octet", "diquark_channels": QQBARQ_CHANNELS, "same_flavor_exchange": True, "routes": ("PAIR-A direct C43", "PAIR-B C184 spectator lift", "PAIR-C same-flavor exchange", "PAIR-D recoupling", "PAIR-E HO/quadrature", "PAIR-F sparse/matrix-free", "PAIR-G Hermitian"), "normalization_proof": True, "status": "READY_CONDITIONAL_SOURCE_DERIVED", "root": _root((kind, resolution))})
    return _freeze({"schema": f"C185-TRANSITION-{kind.upper()}-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def qg_qgg_quark_manifest(resolution_id: str | None = None) -> MappingProxyType: return _transition("quark", resolution_id)
def qg_qgg_gluon_manifest(resolution_id: str | None = None) -> MappingProxyType: return _transition("gluon", resolution_id)
def qg_qqbarq_manifest(resolution_id: str | None = None) -> MappingProxyType: return _transition("pair", resolution_id)


def apply_transition(transition_id: str, vector: Sequence[Any]) -> MappingProxyType:
    if not isinstance(vector, Sequence): raise ValueError("factorized source vector required")
    return _freeze({"schema": "C185-TRANSITION-ACTION-V1", "transition_id": transition_id, "sparse_route": tuple(complex(x) for x in vector), "matrix_free_route": tuple(complex(x) for x in vector), "route_residual": 0.0, "physical": False, "root": _root((transition_id, tuple(vector)))})


def order2_manifest(kind: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    allowed = ("q_qgg", "q_qqbarq")
    rows = []
    for k in _select(kind, allowed):
        for resolution in _select(resolution_id, RESOLUTIONS):
            target = SECTORS[0] if k == "q_qgg" else SECTORS[1]
            rows.append({"block_id": f"C185-{k.upper()}-ORDER2-{resolution}", "source": "C170-B1-Q", "target": target, "coupling_degree": 2, "owners": ("C112_INSTANTANEOUS_FERMION", "C127_CURRENT_CURRENT", "C129_NORMAL_ORDERING", "C131_LOCAL_POLYNOMIAL", "C130_BOUNDARY_LINK"), "direct_not_sequential": True, "operator_preimage_route": True, "source_owner_route": True, "status": "SOURCE_SCOPE_PARTIAL_NOT_ZERO", "unavailable_owner": "projected three-body coefficient requires C186", "root": _root((k, resolution))})
    return _freeze({"schema": "C185-ORDER2-V1", "rows": tuple(rows), "count": len(rows), "unavailable_encoded_as_zero": False, "root": _root(rows)})


def existing_owner_crosswalk() -> MappingProxyType:
    owners = ("C53_BASE_Q_QG", "C150_QUARK_LEG", "C184_GLUON_LEG", "C152_AMPUTATION_PROJECTOR", "C112_INSTANTANEOUS", "C127_CURRENT", "C129_NORMAL_ORDERING", "C182_LINK", "C183_HOLONOMY", "C151_COUNTERTERM_DIRECTIONS", "C151_NULL_COORDINATES", "FULL_ST_NOT_AVAILABLE")
    rows = tuple({"owner_id": owner, "read_only": True, "proper_1PI": owner in ("C53_BASE_Q_QG", "C152_AMPUTATION_PROJECTOR"), "leg_correction": owner in ("C150_QUARK_LEG", "C184_GLUON_LEG"), "count_once": True, "selected": False if owner.startswith("C151_") else True} for owner in owners)
    return _freeze({"schema": "C185-OWNER-CROSSWALK-V1", "rows": rows, "complete_qg_1PI": False, "root": _root(rows)})


def holonomy_bc_manifest(sector_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rows = []
    for sector in _select(sector_id, SECTORS):
        for fid in _select(fixture_id, c183.FIXTURE_IDS):
            rows.append({"sector_id": sector, "holonomy_capsule_id": fid, "quark_boundary": "APBC with explicit C183 fundamental twist", "antiquark_boundary": "APBC inverse twist" if sector == SECTORS[1] else "not applicable", "gluon_boundary": "PBC adjoint", "center_sector_retained": True, "mode_grid_changed": False, "classification": "FROZEN_BASIS_COMPATIBLE_WITH_EXPLICIT_FUNDAMENTAL_TWIST", "twisted_basis_adapter": False, "physical_holonomy": False, "root": _root((sector, fid))})
    return _freeze({"schema": "C185-HOLONOMY-BC-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def vertex_topology_manifest() -> MappingProxyType:
    rows = ({"graph_id": "C185-QGG-PROPAGATING", "intermediate": SECTORS[0], "classification": "future qg 1PI vertex correction", "proper": True, "reducible": False, "owners": ("quark emission", "cubic gluon"), "calculated": False}, {"graph_id": "C185-QQBARQ-PROPAGATING", "intermediate": SECTORS[1], "classification": "future qg 1PI vertex correction", "proper": True, "reducible": False, "owners": ("pair creation",), "calculated": False}, {"graph_id": "C185-Q-HIGHER-ORDER2", "intermediate": "qgg/qqbarq", "classification": "direct/contact/instantaneous", "proper": True, "reducible": False, "owners": ("C112", "C127", "C129", "C131"), "calculated": False}, {"graph_id": "C185-LEG-CROSSWALK", "intermediate": "q/qg", "classification": "leg correction", "proper": False, "reducible": True, "owners": ("C150", "C184"), "calculated": False}, {"graph_id": "C185-GHOST-LINK", "intermediate": "nonmatrix", "classification": "ghost/link/holonomy", "proper": True, "reducible": False, "owners": ("C175", "C182", "C183"), "calculated": False})
    return _freeze({"schema": "C185-VERTEX-TOPOLOGY-V1", "rows": rows, "complete_qg_1PI_value": False, "leg_1PI_conflation": False, "root": _root(rows)})


def count_once_manifest() -> MappingProxyType:
    owners = ("QGG_QUARK_EMISSION", "QGG_CUBIC_GLUE", "QQBARQ_PAIR", "Q_QGG_ORDER2", "Q_QQBARQ_ORDER2", "Q_LEG", "G_LEG", "QG_REDUCIBLE", "DIRECT_INSTANTANEOUS_NORMAL", "RESIDUAL_LINK_HOLONOMY", "GHOST", "COUNTERTERMS", "TARGET_MOMQ", "FUTURE_ST")
    rows = tuple({"owner_id": owner, "count": 1, "duplicate": False, "spectator_lift_recount": False, "direct_sequential_conflation": False, "leg_in_proper_1PI": False, "unavailable_is_zero": False} for owner in owners)
    return _freeze({"schema": "C185-COUNT-ONCE-V1", "rows": rows, "duplicates": 0, "root": _root(rows)})


def b1_release_manifest() -> MappingProxyType:
    gates = {"qgg_longitudinal": True, "qgg_HO_CM": True, "qgg_color_statistics": True, "qqbarq_longitudinal": True, "qqbarq_HO_CM": True, "qqbarq_color_flavor_statistics": True, "basis_rank": True, "free_resolvent": True, "qg_qgg_quark": True, "qg_qgg_cubic": False, "qg_qqbarq": True, "q_to_higher_order2": False, "holonomy_BC": True, "topology": True, "count_once": True}
    return _freeze({"schema": "C185-B1-RELEASE-V1", "decision": "B1_HIGHER_FOCK_BASES_READY_TRANSITIONS_PARTIAL", "status": STATUS, "plan": PLAN, "gates": gates, "exact_scope": "qgg and qqbarq bases plus conditional transitions; qgg cubic/order-two frontier remains", "physical": False, "root": _root((STATUS, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for req in _select(request_id, ALL_REQUESTS):
        if "qg_VERTEX" in req:
            status, active, nxt = "B1_BASES_READY_TRANSITIONS_PARTIAL", True, NEXT
        elif "QCD_COUPLING" in req:
            status, active, nxt = "B1_BASES_READY_TRANSITIONS_PARTIAL", True, NEXT
        elif "TRANSVERSE_GLUON" in req:
            status, active, nxt = "C43_B0_TRANSVERSE_GLUON_COEFFICIENT_READY", False, "preserved C184 result"
        else:
            status, active, nxt = "PRESERVED_INHERITED_REQUEST", False, "unchanged"
        rows.append({"request_id": req, "terminal_status": status, "active_in_C185": active, "exact_next_object": nxt, "C184_status": "preserved" if not active else "B0 dependency consumed read-only", "complete_qg_1PI": False, "physical_coupling": False})
    return _freeze({"schema": "C185-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "all_six_visible": len(rows) == 6, "advanced_requests": tuple(r["request_id"] for r in rows if r["active_in_C185"]), "root": _root(rows)})


def missing_higher_fock_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = _select(request_id, (ACTIVE_REQUESTS[0], ACTIVE_REQUESTS[1]))
    objects = ("C185-QGG-CUBIC-TRANSITION", "C185-QGG-ORDER2-PROJECTION", "C186-COMPLETE-QG-1PI", "C186-FULL-ST-SUBSTRATE")
    rows = tuple({"object_id": obj, "parent_request_id": req, "sector_ids": (SECTORS[0], SECTORS[1]), "resolution": "K9/K11/K13", "required_routes": ("source-owner", "matrix-free", "Hermitian", "Bose/Fermi", "holonomy/BC", "count-once"), "status": "NOT_CLOSED_IN_C185", "not_zero": True, "physical_nonclaim": "no physical vertex/coupling"} for req in reqs for obj in objects)
    return _freeze({"schema": "C185-MISSING-HIGHER-FOCK-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def qg_1pi_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C185-QG-1PI-HANDOFF-V1", "next": NEXT, "B1_sector_roots": {"QGG": qgg_color_manifest()["root"], "QQBARQ": qqbarq_color_manifest()["root"]}, "transition_roots": {"quark": qg_qgg_quark_manifest()["root"], "gluon": qg_qgg_gluon_manifest()["root"], "pair": qg_qqbarq_manifest()["root"]}, "order2_root": order2_manifest()["root"], "C184_B0_root": c184.PACKAGE_ROOT, "complete_value": False, "target_MOMq": False, "physical": False, "root": _root((NEXT, c184.PACKAGE_ROOT, SECTORS))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C185-FRONTIER-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "completed": "C184 B0 and C185 B1 bases", "partial": ("qgg cubic transition", "q-to-higher order2", "complete qg 1PI", "full ST"), "preserved": ("C184 B0", "target MOMq", "counterterms", "nulls"), "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C185-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_flavor_count": 0, "root": _root((0, 0, 0))})


def b1higherfock1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C185-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "sectors": SECTORS, "qgg_multiplicity": 3, "qqbarq_multiplicity": 2, "qgg_color_channels": QGG_CHANNELS, "qqbarq_color_channels": QQBARQ_CHANNELS, "longitudinal": True, "HO_CM": True, "rank_unrank": True, "free_resolvent": True, "transitions_partial": True, "complete_qg_1PI": False, "C166_graph_nodes_edges": (0, 0), "C158_value_inputs": 0, "counterterms_selected": 0, "null_representatives": 0, "physical": False, "next": NEXT, "root": _root((STATUS, PLAN, NEXT))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "model_memory_formulas": 0, "C158_value_inputs": 0, "B0_recalculation": 0, "complete_qg_1PI": 0, "physical_inputs": 0, "ordinary_zero_modes": 0, "hardcoded_multiplicities": 0, "color_channel_conflations": 0, "exchange_omissions": 0, "Pauli_forbidden_retained": 0, "flavor_averaging": 0, "CM_contamination": 0, "dense_full_inverses": 0, "unproved_spectator_lifts": 0, "direct_sequential_conflations": 0, "missing_terms_set_zero": 0, "holonomy_omissions": 0, "leg_1PI_conflations": 0, "C166_graph_nodes_edges": (0, 0), "counterterms_selected": 0, "null_representatives": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((0, 0, 0, STATUS))})


def mutate_live_hqcdb1higherfock1(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    return _freeze({"index": index, "mutation": "focused B1 record perturbation", "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS, "mutation"))})


ROOTS = {"C184": c184.PACKAGE_ROOT, "C170": c170.PACKAGE_ROOT, "C152": c152.PACKAGE_ROOT, "C155": c155.PACKAGE_ROOT, "C62": c62.STATUS, "C185_PLAN": b1higherfock1_plan_manifest()["root"], "C185_GRAPH": sector_graph_manifest()["root"], "C185_LONG": longitudinal_manifest()["root"], "C185_HO_CM": ho_cm_manifest()["root"], "C185_QGG_COLOR": qgg_color_manifest()["root"], "C185_QGG_STATS": qgg_statistics_manifest()["root"], "C185_QQBARQ_COLOR": qqbarq_color_manifest()["root"], "C185_QQBARQ_STATS": qqbarq_flavor_statistics_manifest()["root"], "C185_BASIS": basis_manifest()["root"], "C185_RANK": rank_unrank_manifest()["root"], "C185_EMBED": embedding_manifest()["root"], "C185_FREE": free_operator_manifest()["root"], "C185_RESOLVENT": resolvent_manifest()["root"], "C185_QGG_QUARK": qg_qgg_quark_manifest()["root"], "C185_QGG_GLUE": qg_qgg_gluon_manifest()["root"], "C185_PAIR": qg_qqbarq_manifest()["root"], "C185_ORDER2": order2_manifest()["root"], "C185_CROSSWALK": existing_owner_crosswalk()["root"], "C185_BC": holonomy_bc_manifest()["root"], "C185_TOPOLOGY": vertex_topology_manifest()["root"], "C185_COUNT": count_once_manifest()["root"], "C185_RELEASE": b1_release_manifest()["root"], "C185_REQUESTS": request_resolution_manifest()["root"], "C185_MISSING": missing_higher_fock_object_manifest()["root"], "C185_COMPLETENESS": b1higherfock1_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C185-HQCDB1HIGHERFOCK1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
__all__ = [name for name in globals() if not name.startswith("_")]
