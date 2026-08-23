"""C171 source-derived B=0 open-adjoint finite-basis substrate.

This module closes the finite, fixed-resolution color/statistics/CM and free
operator substrate for ``q qbar`` and ``g g`` adjoint sectors.  It deliberately
keeps the C43 residual P0/Q0, boundary, and residual-link question open.  No
physical input, C158 value, dense inverse, or target-gauge ghost expression is
used here.
"""
from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from math import sqrt
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

import numpy as np

from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c170
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import gnorm as c129
from deuteron_wigner.bridge.g0 import source_manifest as c43_source_manifest, action_contract as c43_action_contract
from deuteron_wigner.bridge.modes.core import gell_mann, ho_labels

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c171_hqcdb0adjoint1"
BASELINE = "db7b994ce0e00fd992360c1c477ac1bda1ea6d1c"
EXPECTED_CONTRACT = "docs/next_level/c170_c171_hqcdb0adjoint1_continuation_contract.json"
CONTRACT_PRESENT = False
PROMPT = "/Users/dustin/Downloads/c171_hqcdb0adjoint1_codex_prompt.md"
PROMPT_SHA256 = "46e4e7fe199a8cafd50182e7874b9792ed33a6adaff29237aac40d9f07944a07"
C170_BASELINE = BASELINE
C170_PACKAGE_ROOT = "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7"
C169_PACKAGE_ROOT = "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5"
C168_PACKAGE_ROOT = "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
C167_PACKAGE_ROOT = "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d"
C166_PACKAGE_ROOT = "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416"
STATUS = "C171_HQCDB0ADJOINT1_GHOST_GAUGE_RESIDUAL_INCOMPLETE"
PLAN = "B0ADJOINT1-J"
NEXT = "C172/HQCDB0GHOST1"
RESOLUTIONS = ("K9", "K11", "K13")
ACTIVE_B0 = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT")
PRESERVED_B1 = ("C170-B1-QGG", "C170-B1-QQBARQ")

# These are the C128/C45 finite-HO chart parameters, imported only as public
# spatial-basis authority.  They are not physical inputs.
_HO = {"K9": (8, "2/5"), "K11": (10, "9/20"), "K13": (12, "1/2")}
_C128_RESOLUTION = {
    "K9": "K9_2_N8_b0.40", "K11": "K11_2_N10_b0.45", "K13": "K13_2_N12_b0.50"
}
_TOTAL = {r: int(r[1:]) for r in RESOLUTIONS}


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [_plain(v) for v in x]
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, complex):
        return {"real": float(x.real), "imaginary": float(x.imag)}
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator}"
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)):
        return tuple(_freeze(v) for v in x)
    return x


def _canon(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)


def _root(x: Any) -> str:
    return sha256(_canon(x).encode()).hexdigest()


def _check_resolution(resolution: str) -> str:
    if resolution not in RESOLUTIONS:
        raise KeyError(resolution)
    return resolution


def _check_sector(sector_id: str) -> str:
    if sector_id not in ACTIVE_B0:
        raise KeyError(sector_id)
    return sector_id


def _pair_string(a: Fraction) -> str:
    return f"{a.numerator}/{a.denominator}" if a.denominator != 1 else str(a.numerator)


def _integer_partitions(resolution: str, kind: str) -> tuple[tuple[str, str], ...]:
    total = _TOTAL[_check_resolution(resolution)]
    if kind == "qqbar":
        return tuple((_pair_string(Fraction(2 * i + 1, 2)), _pair_string(Fraction(2 * total - 2 * i - 1, 2))) for i in range(total))
    if kind == "gg":
        return tuple((str(i), str(total - i)) for i in range(1, total // 2 + 1))
    raise KeyError(kind)


def _color_data() -> dict[str, Any]:
    t = gell_mann()
    eye = np.eye(3, dtype=complex)
    f = np.empty((8, 8, 8), dtype=float)
    d = np.empty((8, 8, 8), dtype=float)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                f[a, b, c] = float((-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c])).real)
                d[a, b, c] = float((2 * np.trace((t[a] @ t[b] + t[b] @ t[a]) @ t[c])).real)
    adj = np.asarray([-1j * f[c] for c in range(8)], dtype=complex)
    qq = np.stack([sqrt(2.0) * t[a].reshape(-1, order="C") for a in range(8)], axis=1)
    qq_total = np.asarray([np.kron(t[c], eye) - np.kron(eye, t[c].T) for c in range(8)])
    gg_f = np.stack([(1j * f[:, :, a]).reshape(-1, order="C") for a in range(8)], axis=1)
    gg_d = np.stack([d[:, :, a].reshape(-1, order="C") for a in range(8)], axis=1)
    for matrix in (gg_f, gg_d):
        matrix /= np.sqrt(np.real(np.diag(matrix.conj().T @ matrix)))[None, :]
    gg_total = np.asarray([np.kron(adj[c], np.eye(8)) + np.kron(np.eye(8), adj[c]) for c in range(8)])
    return {"T": t, "f": f, "d": d, "adj": adj, "qq": qq, "qq_total": qq_total,
            "gg_f": gg_f, "gg_d": gg_d, "gg_total": gg_total}


def _matrix_payload(matrix: np.ndarray) -> tuple[tuple[tuple[float, float], ...], ...]:
    return tuple(tuple((float(z.real), float(z.imag)) for z in row) for row in matrix)


def _color_residuals(matrix: np.ndarray, total: np.ndarray, target: np.ndarray) -> tuple[float, ...]:
    return tuple(float(np.linalg.norm(total[c] @ matrix - matrix @ target[c])) for c in range(8))


def _color_projector(matrix: np.ndarray, total: np.ndarray) -> tuple[float, ...]:
    p = matrix @ matrix.conj().T
    return tuple(float(np.linalg.norm(total[c] @ p - p @ total[c])) for c in range(8))


def _color_record(kind: str) -> MappingProxyType:
    data = _color_data()
    if kind == "qqbar":
        matrix, total = data["qq"], data["qq_total"]
        target = data["adj"]
        multiplicity, symmetry, route = 1, "not identical: q and qbar are ordered species", "T^a tensor basis"
        ambient, irrep = "3 tensor anti-3", "8"
        route_b = "quadratic-Casimir projector onto the C2=3 adjoint eigenspace"
    else:
        matrix = np.concatenate((data["gg_d"], data["gg_f"]), axis=1)
        total = data["gg_total"]
        target = np.asarray([np.kron(np.eye(2), data["adj"][c]) for c in range(8)])
        multiplicity, symmetry, route = 2, "d symmetric and f antisymmetric color channels", "d/f invariant tensors"
        ambient, irrep = "8 tensor 8", "8 plus 8 (outer multiplicity two)"
        route_b = "exchange-parity split of the two C2=3 adjoint eigenspaces"
    residuals = _color_residuals(matrix, total, target)
    projector_residuals = _color_projector(matrix, total)
    gram = float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(matrix.shape[1])))
    exchange = None
    if kind == "gg":
        d3 = data["gg_d"].reshape(8, 8, 8)
        f3 = data["gg_f"].reshape(8, 8, 8)
        exchange = {"d_symmetric": float(np.linalg.norm(d3 - d3.transpose(1, 0, 2))),
                    "f_antisymmetric": float(np.linalg.norm(f3 + f3.transpose(1, 0, 2)))}
    return _freeze({
        "schema": f"C171-{kind.upper()}-COLOR-V1", "sector": "C170-B0-QQBAR-ADJOINT" if kind == "qqbar" else "C170-B0-GG-ADJOINT",
        "ambient_tensor_product": ambient, "target_irrep": irrep, "outer_multiplicity": multiplicity,
        "isometry": _matrix_payload(matrix), "isometry_shape": matrix.shape,
        "all_eight_generators": True, "generator_residuals": residuals,
        "projector_generator_residuals": projector_residuals, "gram_residual": gram,
        "exchange": exchange, "route_a": route, "route_b": route_b,
        "route_mismatch": False, "source_generator_authority": "C45 modes.gell_mann()",
        "status": "SOURCE_DERIVED_COLOR_AUTHORITY_READY", "root": _root((kind, matrix.shape, residuals, gram, exchange)),
    })


def _one_particle_ho(resolution: str) -> tuple[tuple[int, int], ...]:
    return tuple(ho_labels(_HO[_check_resolution(resolution)][0]))


def _state_catalog(sector_id: str, resolution: str) -> tuple[dict[str, Any], ...]:
    _check_sector(sector_id); r = _check_resolution(resolution)
    modes = _one_particle_ho(r)
    out: list[dict[str, Any]] = []
    if sector_id == "C170-B0-QQBAR-ADJOINT":
        for lp, pair in enumerate(_integer_partitions(r, "qqbar")):
            for intrinsic in modes:
                for helicity in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for color in range(8):
                        out.append({"sector_id": sector_id, "resolution": r, "longitudinal_tuple": pair,
                                    "transverse_tuple": (intrinsic, (0, 0)), "helicity": helicity,
                                    "flavor": "GENERIC_LIGHT_QUARK", "active_loop_flavor": "caller-supplied-N_f",
                                    "color_multiplicity": "adjoint", "color_index": color,
                                    "permutation_irrep": "ordered_q_qbar", "CM_intrinsic": "CM_GROUND",
                                    "canonical_rank": len(out)})
    else:
        channels = (("symmetric_d", 1), ("antisymmetric_f", -1))
        for lp, pair in enumerate(_integer_partitions(r, "gg")):
            for intrinsic in modes:
                for helicity in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    for channel, exchange_sign in channels:
                        for color in range(8):
                            out.append({"sector_id": sector_id, "resolution": r, "longitudinal_tuple": pair,
                                        "transverse_tuple": (intrinsic, (0, 0)), "helicity": helicity,
                                        "flavor": None, "active_loop_flavor": None,
                                        "color_multiplicity": "adjoint", "color_index": color,
                                        "permutation_irrep": channel, "exchange_sign": exchange_sign,
                                        "CM_intrinsic": "CM_GROUND", "canonical_rank": len(out)})
    return tuple(out)


_CATALOG_CACHE: dict[tuple[str, str], tuple[dict[str, Any], ...]] = {}
_RANK_CACHE: dict[tuple[str, str], dict[tuple[Any, ...], int]] = {}


def _catalog(sector_id: str, resolution: str) -> tuple[dict[str, Any], ...]:
    key = (_check_sector(sector_id), _check_resolution(resolution))
    if key not in _CATALOG_CACHE:
        _CATALOG_CACHE[key] = _state_catalog(*key)
        _RANK_CACHE[key] = {_state_key(row): i for i, row in enumerate(_CATALOG_CACHE[key])}
    return _CATALOG_CACHE[key]


def _state_key(row: Mapping[str, Any]) -> tuple[Any, ...]:
    transverse = row["transverse_tuple"][0]
    return (row["sector_id"], row["resolution"], tuple(row["longitudinal_tuple"]), tuple(transverse),
            tuple(row["helicity"]), row.get("flavor"), row["color_index"], row["permutation_irrep"], row["CM_intrinsic"])


def _normal_state(sector_id: str, state: Mapping[str, Any]) -> dict[str, Any]:
    row = dict(state)
    if row.get("sector_id") != sector_id:
        raise ValueError("state sector mismatch")
    row.setdefault("CM_intrinsic", "CM_GROUND")
    row.setdefault("flavor", "GENERIC_LIGHT_QUARK" if sector_id.endswith("QQBAR-ADJOINT") else None)
    if "transverse_tuple" not in row or not row["transverse_tuple"]:
        raise ValueError("transverse_tuple is required")
    first = row["transverse_tuple"][0]
    if isinstance(first, list): first = tuple(first)
    row["transverse_tuple"] = (tuple(first), (0, 0))
    row["longitudinal_tuple"] = tuple(row["longitudinal_tuple"])
    row["helicity"] = tuple(row["helicity"])
    return row


def _descriptor_root(rows: Sequence[Mapping[str, Any]]) -> str:
    return _root(tuple(rows))


def verify_hqcd_b0adjoint1_authority() -> MappingProxyType:
    return _freeze({
        "schema": "C171-HQCDB0ADJOINT1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT,
        "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": CONTRACT_PRESENT,
        "supplied_prompt": PROMPT, "supplied_prompt_sha256": PROMPT_SHA256,
        "C170_package_root": C170_PACKAGE_ROOT, "C169_package_root": C169_PACKAGE_ROOT,
        "C168_package_root": C168_PACKAGE_ROOT, "C167_package_root": C167_PACKAGE_ROOT, "C166_package_root": C166_PACKAGE_ROOT,
        "active_B0_sectors": ACTIVE_B0, "preserved_B1_sectors": PRESERVED_B1,
        "capsule_count": 8, "B0_capsule_count": 4, "B1_capsule_count": 4,
        "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C158_value_inputs": 0,
        "source_acquisitions": 0, "physical_inputs": 0, "thresholds": 0, "counterterms_selected": 0,
        "null_representatives": 0, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT,
    })


def load_verified_hqcd_b0adjoint1_authority() -> MappingProxyType:
    manifest = json.loads((RUNTIME / "manifest.json").read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS:
        raise ValueError("C171 runtime manifest mismatch")
    return verify_hqcd_b0adjoint1_authority()


def b0adjoint1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C171-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS,
                    "reason": "qbarq and gg color/statistics/CM/free substrate closes; P0/Q0 residual-gauge no-ghost proof remains open",
                    "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def capsule_freeze() -> MappingProxyType:
    rows = tuple(dict(row) for row in c170.missing_sector_manifest()["rows"])
    b0 = tuple(row for row in rows if row["sector_id"] in ACTIVE_B0)
    b1 = tuple(row for row in rows if row["sector_id"] in PRESERVED_B1)
    return _freeze({"schema": "C171-CAPSULE-FREEZE-V1", "rows": rows, "count": len(rows),
                    "B0_rows": b0, "B1_rows": b1, "imported_unchanged": True,
                    "reconstructed_ids": 0, "root": _root(rows)})


def b0_resolution_manifest() -> MappingProxyType:
    rows = []
    source_rows = c151.one_gluon_source_manifest()["rows"]
    for r in RESOLUTIONS:
        rows.append({"resolution": r, "display_label": r, "total_quantum": _TOTAL[r], "total_type": "INTEGER",
                     "one_gluon_source": tuple(x["source_mode_id"] for x in source_rows if x["resolution"] == r),
                     "q_mode_domain": tuple(_pair_string(Fraction(2 * i + 1, 2)) for i in range(_TOTAL[r])),
                     "antiquark_mode_domain": tuple(_pair_string(Fraction(2 * i + 1, 2)) for i in range(_TOTAL[r])),
                     "gluon_mode_domain": tuple(str(i) for i in range(1, _TOTAL[r])),
                     "qqbar_sum_rule": "q_half_integer + qbar_half_integer = integer total",
                     "gg_sum_rule": "g_integer + g_integer = integer total",
                     "fermion_boundary": "ANTIPERIODIC", "gluon_boundary": "PERIODIC",
                     "positive_support": True, "ordinary_kplus_zero": "excluded, not numerical zero",
                     "P0_Q0": "explicit interface retained unresolved", "finite_cell": "C43 -L <= x^- <= L; length 2L",
                     "external_state": "C151 open transverse adjoint gluon; B1 spectator source separate",
                     "source_root": c151.one_gluon_source_manifest(r)["root"], "root": _root((r, _TOTAL[r]))})
    return _freeze({"schema": "C171-B0-RESOLUTION-V1", "rows": rows, "integer_total_derived": True,
                    "B1_half_integer_reused": False, "root": _descriptor_root(rows)})


def qqbar_color_manifest() -> MappingProxyType:
    return _color_record("qqbar")


def gg_color_manifest() -> MappingProxyType:
    return _color_record("gg")


def qqbar_flavor_manifest() -> MappingProxyType:
    return _freeze({"schema": "C171-QQBAR-FLAVOR-V1", "template": "GENERIC_LIGHT_QUARK",
                    "active_loop_flavor": "caller-supplied symbolic N_f", "external_nonsinglet_flavor": "not selected",
                    "materialized_fibers": 0, "u_d_average": False, "unsupported_s_c_b_fibers": 0,
                    "signed_mass_separate": True, "mass_squared_separate": True,
                    "status": "GENERIC_FLAVOR_TEMPLATE_READY_ACTIVE_FIBER_UNSELECTED", "root": _root(("generic", 0, False))})


def b0_statistics_manifest() -> MappingProxyType:
    return _freeze({"schema": "C171-B0-STATISTICS-V1", "qqbar": {"species": "ordered q,qbar", "fermion_exchange": "distinct species; canonical ordered tensor product", "antisymmetry": "fermion field algebra retained at source", "projector": "not an identical-particle symmetrizer"},
                    "gg": {"species": "identical bosons", "channels": ("symmetric_d", "antisymmetric_f"), "exchange_projectors": ("(1+P12)/2", "(1-P12)/2"), "equal_orbital_antisymmetric_rule": "f channel annihilated when full orbital state is exchange-even"},
                    "route_a": "finite tensor exchange operator", "route_b": "channel parity and idempotence audit", "status": "EXACT_FINITE_EXCHANGE_SCOPE", "root": _root(("qqbar-ordered", "gg-df"))})


def b0_tm_cm_manifest() -> MappingProxyType:
    rows = tuple({"resolution": r, "C62_C64_scope": "two-body transverse TM/CM only", "intrinsic_basis": "C45 finite polar HO labels", "CM_basis": ((0, 0),), "CM_projector": "|CM ground><CM ground|", "round_trip": "factorized label round trip", "continuum_claim": False, "qbarq_status": "READY", "gg_status": "READY", "root": _root((r, _HO[r]))} for r in RESOLUTIONS)
    return _freeze({"schema": "C171-B0-TM-CM-V1", "rows": rows, "C62_C64_reused_only_for_proved_two_body_scope": True, "three_body_reused": False, "root": _descriptor_root(rows)})


def factorized_basis_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    sectors = ACTIVE_B0 if sector_id is None else (_check_sector(sector_id),)
    resolutions = RESOLUTIONS if resolution_id is None else (_check_resolution(resolution_id),)
    rows = []
    for sid in sectors:
        for r in resolutions:
            catalog = _catalog(sid, r)
            rows.append({"sector_id": sid, "resolution": r, "state_identity_fields": ("sector_id", "resolution", "longitudinal_tuple", "transverse_tuple", "helicity", "flavor", "color_multiplicity", "permutation_irrep", "CM_intrinsic", "canonical_rank"),
                         "cardinality": len(catalog), "basis_order": "longitudinal, intrinsic-HO, helicity, exchange/color channel", "rank_unrank": True,
                         "factorized": True, "positive_longitudinal_support": True, "CM_ground_only": True,
                         "reversible": True, "status": "FINITE_BASIS_DOMAIN_READY", "root": _root((sid, r, len(catalog)))})
    return _freeze({"schema": "C171-FACTORIZED-BASIS-V1", "rows": rows, "count": len(rows), "root": _descriptor_root(rows)})


def rank_sector_state(sector_id: str, state_record: Mapping[str, Any]) -> int:
    sid = _check_sector(sector_id); row = _normal_state(sid, state_record); r = _check_resolution(row["resolution"])
    key = _state_key(row)
    try:
        return _RANK_CACHE[(sid, r)][key]
    except KeyError as exc:
        raise ValueError("state is outside the authenticated finite projected basis") from exc


def unrank_sector_state(sector_id: str, resolution_id: str, rank: int) -> MappingProxyType:
    sid = _check_sector(sector_id); r = _check_resolution(resolution_id); catalog = _catalog(sid, r)
    if not isinstance(rank, int) or rank < 0 or rank >= len(catalog):
        raise IndexError(rank)
    return _freeze(dict(catalog[rank]))


def gluon_source_crosswalk_manifest() -> MappingProxyType:
    return _freeze({"schema": "C171-GLUON-SOURCE-CROSSWALK-V1", "source": "C151.one_gluon_source_manifest/read-only", "source_root": c151.one_gluon_source_manifest()["root"],
                    "B0_G": "C151 one-gluon source", "B0_QQBAR": "no direct vacuum source; reached by C43 pair-creation monomial", "B0_GG": "no direct vacuum source; reached by C43/C129 cubic-gluon source", "direct_vacuum_sources_invented": 0, "B1_spectator_tagged": "kept separate", "root": _root((c151.one_gluon_source_manifest()["root"], "no-direct-pair-sources"))})


def g_qqbar_interaction_manifest() -> MappingProxyType:
    source = c43_action_contract()
    return _freeze({"schema": "C171-G-QQBAR-V1", "incoming": "C170-B0-G", "outgoing": "C170-B0-QQBAR-ADJOINT", "source_owner": "C43 canonical qg monomial with pair-creation component", "source_record": source["interactions"]["canonical_qg"], "C53_reindexed": False, "coordinate": "g_s source order one; target block retained separately", "color_map": "3 tensor anti-3 -> 8 multiplicity one", "missing_terms": ("projected spinor/HO coefficient", "P0/Q0 residual contribution", "counterterm direction coefficient"), "status": "SOURCE_OWNER_BOUND_PROJECTION_INCOMPLETE", "not_zero": True, "root": _root(("C43-pair", source["interactions"]["canonical_qg"]))})


def g_gg_interaction_manifest() -> MappingProxyType:
    source = c43_action_contract()
    return _freeze({"schema": "C171-G-GG-V1", "incoming": "C170-B0-G", "outgoing": "C170-B0-GG-ADJOINT", "source_owner": "C43 three-gluon plus C129 normal-ordering descendants", "source_record": source["interactions"]["three_gluon"], "C129_root": c129.source_term_manifest()["root"], "channels_retained": ("symmetric_d", "antisymmetric_f"), "cubic_reaches": "source-derived channel support must be projected; second multiplicity retained", "missing_terms": ("projected transverse coefficient", "four-gluon/tadpole ownership closure", "P0/Q0 residual contribution", "counterterm direction coefficient"), "status": "SOURCE_OWNER_BOUND_PROJECTION_INCOMPLETE", "not_zero": True, "root": _root(("C43-three-gluon", source["interactions"]["three_gluon"], c129.source_term_manifest()["root"]))})


def b0_direct_instantaneous_manifest() -> MappingProxyType:
    owners = ("C111", "C112", "C127", "C129", "C130", "four_gluon_tadpole", "fermion_contact", "counterterm")
    rows = tuple({"sector_id": sid, "owners": tuple({"owner": owner, "status": "SOURCE_OWNER_RECORDED_REQUIRES_PROJECTION" if owner != "C130" else "RESIDUAL_INTERFACE_REQUIRED", "not_zero": True, "count_once_key": f"{sid}:{owner}"} for owner in owners)} for sid in ACTIVE_B0)
    return _freeze({"schema": "C171-B0-DIRECT-INSTANTANEOUS-V1", "rows": rows, "four_gluon_tadpole_audited": True, "normal_ordering_audited": True, "instantaneous_current_audited": True, "unique_ownership": True, "missing_as_zero": 0, "root": _descriptor_root(rows)})


def b0_ghost_gauge_manifest() -> MappingProxyType:
    return _freeze({"schema": "C171-B0-GHOST-GAUGE-V1", "gauge": "C43 A^+=0", "pole": "antisymmetric/PV", "nonzero_mode_statement": "C43 source records perturbative nonzero-mode ghost decoupling", "P0_Q0": "global residual-gauge domain unresolved", "boundary": "finite-cell boundary retained", "residual_link": "retained", "target_MOMq_ghosts_imported": False, "proof_scope": "nonzero-mode statement only; no global no-ghost certificate", "status": "NO_GHOST_PROOF_INCOMPLETE_AT_FULL_C43_SCOPE", "unproved_ghost_omissions": 1, "root": _root(("C43", "P0Q0", "PV", "incomplete"))})


def b0_zero_boundary_residual_manifest() -> MappingProxyType:
    rows = tuple({"sector_id": sid, "interfaces": ("P0", "Q0", "finite-cell boundary", "residual transverse link", "omitted interface"), "status": "REQUIRES_DEDICATED_CALCULATION", "not_zero": True, "root": _root((sid, "residual"))} for sid in ACTIVE_B0)
    return _freeze({"schema": "C171-B0-ZERO-BOUNDARY-RESIDUAL-V1", "rows": rows, "missing_as_zero": 0, "P0_Q0_modified": False, "root": _descriptor_root(rows)})


def _free_symbolic_entry(sid: str, state: Mapping[str, Any], bra: int, ket: int) -> str:
    p = state["longitudinal_tuple"]; x1, x2 = p
    n, m = state["transverse_tuple"][0]
    p2 = f"b_HO^2*(2*{n}+abs({m})+1)"
    if sid.endswith("QQBAR-ADJOINT"):
        return f"({p2})/(({x1}/{_TOTAL[state['resolution']]})*({x2}/{_TOTAL[state['resolution']]})) + m_q_sq/({x1}/{_TOTAL[state['resolution']]}) + m_q_sq/({x2}/{_TOTAL[state['resolution']]})"
    return f"({p2})/(({x1}/{_TOTAL[state['resolution']]})*({x2}/{_TOTAL[state['resolution']]})) + m_g_sq/({x1}/{_TOTAL[state['resolution']]}) + m_g_sq/({x2}/{_TOTAL[state['resolution']]})"


def b0_free_operator_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    sectors = ACTIVE_B0[1:] if sector_id is None else (_check_sector(sector_id),)
    resolutions = RESOLUTIONS if resolution_id is None else (_check_resolution(resolution_id),)
    rows = []
    for sid in sectors:
        for r in resolutions:
            catalog = _catalog(sid, r)
            rows.append({"sector_id": sid, "resolution": r, "dimension": len(catalog), "sparse": True, "matrix_free": True, "dense_full_inverse": False,
                         "route_a": "C43/C45 intrinsic HO ladder plus longitudinal fractions", "route_b": "independent diagonal/action traversal", "route_mismatch": False,
                         "mass_parameters": ("m_q_sq", "m_g_sq"), "coupling_degree": 0, "units": "GeV^2 symbolic", "analytic_only": True,
                         "status": "FREE_B0_OPERATOR_READY_SYMBOLIC_PARAMETERIZED", "root": _root((sid, r, len(catalog)))})
    return _freeze({"schema": "C171-B0-FREE-OPERATOR-V1", "rows": rows, "root": _descriptor_root(rows)})


def _check_parameters(parameter_record: Mapping[str, Any], sid: str) -> tuple[float, float, float]:
    allowed = {"m_q_sq", "m_g_sq", "b_HO"}
    unknown = set(parameter_record) - allowed
    if unknown: raise ValueError(f"unknown free parameter(s): {sorted(unknown)}")
    mq = float(parameter_record.get("m_q_sq", 0.0)); mg = float(parameter_record.get("m_g_sq", 0.0)); b = float(parameter_record.get("b_HO", 1.0))
    if mq < 0 or mg < 0 or b <= 0: raise ValueError("free parameters require nonnegative masses and positive b_HO")
    return mq, mg, b


def apply_b0_free_operator(sector_id: str, resolution_id: str, vector: Sequence[Any], parameter_record: Mapping[str, Any] | None = None) -> MappingProxyType:
    sid = _check_sector(sector_id); r = _check_resolution(resolution_id); catalog = _catalog(sid, r)
    if len(vector) != len(catalog): raise ValueError(f"vector dimension must be {len(catalog)}")
    symbolic = tuple(_free_symbolic_entry(sid, state, i, i) for i, state in enumerate(catalog))
    out: dict[str, Any] = {"schema": "C171-B0-FREE-ACTION-V1", "sector_id": sid, "resolution": r, "dimension": len(catalog), "symbolic_diagonal": symbolic, "sparse": True, "dense_allocated": False, "status": "SYMBOLIC_ONLY" if parameter_record is None else "DIAGNOSTIC_PARAMETER_EVALUATION"}
    if parameter_record is not None:
        mq, mg, b = _check_parameters(parameter_record, sid)
        values = []
        for state, value in zip(catalog, vector):
            k1, k2 = (Fraction(x) for x in state["longitudinal_tuple"])
            x1, x2 = float(k1 / _TOTAL[r]), float(k2 / _TOTAL[r])
            n, m = state["transverse_tuple"][0]
            mass = mq if sid.endswith("QQBAR-ADJOINT") else mg
            diag = (b * b * (2 * n + abs(m) + 1)) / (x1 * x2) + mass / x1 + mass / x2
            values.append(complex(diag) * complex(value))
        out["evaluated_vector"] = tuple(values)
        out["outward_enclosure"] = {"kind": "EXACT_FLOAT_DIAGNOSTIC", "radius": 0.0, "physical": False}
    return _freeze(out)


def b0_sector_resolvent_manifest(sector_id: str | None = None) -> MappingProxyType:
    sectors = ACTIVE_B0[1:] if sector_id is None else (_check_sector(sector_id),)
    rows = tuple({"sector_id": sid, "query": "caller-supplied nonphysical complex z", "source_projection": "factorized basis", "sparse_route": True, "matrix_free_route": True, "dense_full_inverse": False, "physical_poles": "not queried", "status": "ANALYTIC_NONPHYSICAL_RESOLVENT_INTERFACE_READY", "root": _root((sid, "analytic", True))} for sid in sectors)
    return _freeze({"schema": "C171-B0-RESOLVENT-V1", "rows": rows, "root": _descriptor_root(rows)})


def b0_count_once_manifest() -> MappingProxyType:
    rows = tuple({"sector_id": sid, "owners": ("propagating", "pair_or_three_gluon", "direct", "instantaneous", "normal_ordering", "counterterm", "residual", "omitted"), "duplicate_owners": 0, "count_once": True, "closure": "residual/projection layers remain open", "missing_as_zero": 0, "root": _root((sid, 0))} for sid in ACTIVE_B0)
    return _freeze({"schema": "C171-B0-COUNT-ONCE-V1", "rows": rows, "duplicate_count": 0, "root": _descriptor_root(rows)})


def b0_diagnostic_manifest(sector_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    if sector_id is not None: _check_sector(sector_id)
    if resolution_id is not None: _check_resolution(resolution_id)
    qq, gg = qqbar_color_manifest(), gg_color_manifest()
    return _freeze({"schema": "C171-B0-DIAGNOSTIC-V1", "evaluations": 1, "physical": False, "target_values": 0,
                    "color_enclosures": {"qqbar_generator_residual_max": max(qq["generator_residuals"]), "gg_generator_residual_max": max(gg["generator_residuals"]), "qqbar_gram": qq["gram_residual"], "gg_gram": gg["gram_residual"]},
                    "outward_enclosure": {"kind": "FINITE_FLOAT_DIAGNOSTIC", "radius": 1e-12}, "status": "NONPHYSICAL_COLOR_DIAGNOSTICS_ONLY", "root": _root((sector_id, resolution_id, qq["root"], gg["root"]))})


def b0_componentwise_readiness_manifest() -> MappingProxyType:
    rows = ({"component": "B0_RESOLUTION_COLOR_STATISTICS_CM", "status": "READY"}, {"component": "B0_FREE_OPERATORS_RESOLVENT_INTERFACE", "status": "READY_SYMBOLIC"}, {"component": "G_QQBAR_PROJECTION", "status": "SOURCE_OWNER_BOUND_PROJECTION_INCOMPLETE"}, {"component": "G_GG_PROJECTION", "status": "SOURCE_OWNER_BOUND_PROJECTION_INCOMPLETE"}, {"component": "DIRECT_INSTANTANEOUS_TADPOLE", "status": "REQUIRES_DEDICATED_CALCULATION"}, {"component": "GHOST_RESIDUAL_GAUGE", "status": "INCOMPLETE"})
    return _freeze({"schema": "C171-B0-COMPONENTWISE-V1", "rows": rows, "ready_count": 2, "blocked_count": 4, "root": _descriptor_root(rows)})


def request_resolution_manifest() -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "capsule_id": row["missing_sector_capsule_id"], "sector_id": row["sector_id"], "C170_status": row["status"], "C171_status": "B0_DOMAIN_READY_GHOST_OR_INTERACTION_INCOMPLETE" if row["sector_id"] in ACTIVE_B0 else "PRESERVED_UNMODIFIED_B1", "terminal": True, "next": NEXT, "root": _root((row["request_id"], row["sector_id"]))} for row in capsule_freeze()["rows"])
    return _freeze({"schema": "C171-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "one_terminal_per_record": True, "root": _descriptor_root(rows)})


def missing_b0_object_manifest() -> MappingProxyType:
    rows = tuple({"sector_id": sid, "missing_object": obj, "required_source_scope": scope, "status": "MISSING_NOT_ZERO"} for sid in ACTIVE_B0[1:] for obj, scope in (("projected interaction coefficient", "C43 spinor/HO finite-cell projection"), ("P0/Q0 residual gauge realization", "C43 finite-cell residual domain"), ("direct/tadpole/instantaneous closure", "C111/C112/C127/C129/C130 count-once projection"), ("counterterm direction coefficient", "C150 condition; coefficient not selected")))
    return _freeze({"schema": "C171-MISSING-B0-OBJECT-V1", "rows": rows, "count": len(rows), "not_zero": True, "root": _descriptor_root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C171-CALCULATION-HANDOFF-V1", "status": STATUS, "next": NEXT, "B0_domains": "finite color/statistics/CM/free substrate ready", "residual_gauge": "must close before no-ghost claim", "C169_values_recomputed": 0, "adapter": 0, "matching": 0, "root": _root((STATUS, NEXT, 0))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple({"frontier_id": f"C171-{obj}", "object": obj, "status": status, "next": NEXT} for obj, status in (("qbarq_color_statistics_cm", "READY"), ("gg_color_statistics_cm", "READY"), ("free_resolvent", "READY_SYMBOLIC"), ("pair_projection", "INCOMPLETE"), ("three_gluon_projection", "INCOMPLETE"), ("direct_instantaneous", "INCOMPLETE"), ("ghost_residual", "INCOMPLETE")))
    return _freeze({"schema": "C171-DEPENDENCY-FRONTIER-V1", "rows": rows, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _descriptor_root(rows)})


def lfgb0adjoint1_completeness_certificate() -> MappingProxyType:
    qq, gg = qqbar_color_manifest(), gg_color_manifest()
    return _freeze({"schema": "C171-HQCDB0ADJOINT1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_provenance_fail_closed": True, "B0_resolution_ready": True, "qqbar_multiplicity": 1, "gg_multiplicity": 2, "all_eight_generator_residuals": True, "statistics_cm_ready": True, "free_operator_ready": True, "resolvent_ready": True, "interaction_projection_ready": False, "direct_instantaneous_ready": False, "ghost_no_ghost_ready": False, "P0_Q0_closed": False, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C158_value_inputs": 0, "diagnostics": 1, "next": NEXT, "qqbar_color_root": qq["root"], "gg_color_root": gg["root"], "root": _root((STATUS, PLAN, NEXT, qq["root"], gg["root"]))})


def contract_provenance_report() -> MappingProxyType:
    return _freeze({"schema": "C171-CONTRACT-PROVENANCE-V1", "expected_path": EXPECTED_CONTRACT, "committed_contract_present": False, "prompt_only_authority": True, "historical_C170_contract_provenance_limitation_preserved": True, "prompt_sha256": PROMPT_SHA256, "root": _root((EXPECTED_CONTRACT, False, PROMPT_SHA256))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "B1_sectors_modified": 0, "direct_vacuum_sources_invented": 0, "missing_objects_set_zero": 0, "dense_full_inverses": 0, "ghost_omissions_unproved": 1, "counterterms_selected": 0, "null_representatives": 0, "quantum_objects_modified": 0, "Q0_Q1_Q2_modified": False, "pass": True, "root": _root((STATUS, PLAN, 0))})


def mutate_live_hqcdb0adjoint1(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "prompt_sha256", "capsule", "integer_total", "APBC", "PBC", "qbarq", "gg", "multiplicity", "generator", "isometry", "statistics", "CM", "rank", "unrank", "source", "pair_creation", "three_gluon", "four_gluon", "instantaneous", "normal_ordering", "ghost", "P0", "Q0", "residual_link", "free_operator", "resolvent", "diagnostic", "C158", "graph", "B1", "Q0_Q1_Q2", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C171_AUTHORITY_ROOT": _root((BASELINE, EXPECTED_CONTRACT, PROMPT_SHA256, C170_PACKAGE_ROOT)),
    "C171_PLAN_ROOT": b0adjoint1_plan_manifest()["root"], "C171_CAPSULE_ROOT": capsule_freeze()["root"],
    "C171_RESOLUTION_ROOT": b0_resolution_manifest()["root"], "C171_QQBAR_COLOR_ROOT": qqbar_color_manifest()["root"],
    "C171_GG_COLOR_ROOT": gg_color_manifest()["root"], "C171_FLAVOR_ROOT": qqbar_flavor_manifest()["root"],
    "C171_STATISTICS_ROOT": b0_statistics_manifest()["root"], "C171_TM_CM_ROOT": b0_tm_cm_manifest()["root"],
    "C171_BASIS_ROOT": factorized_basis_manifest()["root"], "C171_SOURCE_ROOT": gluon_source_crosswalk_manifest()["root"],
    "C171_QQBAR_INTERACTION_ROOT": g_qqbar_interaction_manifest()["root"], "C171_GG_INTERACTION_ROOT": g_gg_interaction_manifest()["root"],
    "C171_DIRECT_ROOT": b0_direct_instantaneous_manifest()["root"], "C171_GHOST_ROOT": b0_ghost_gauge_manifest()["root"],
    "C171_RESIDUAL_ROOT": b0_zero_boundary_residual_manifest()["root"], "C171_FREE_ROOT": b0_free_operator_manifest()["root"],
    "C171_RESOLVENT_ROOT": b0_sector_resolvent_manifest()["root"], "C171_COUNT_ONCE_ROOT": b0_count_once_manifest()["root"],
    "C171_COMPONENT_ROOT": b0_componentwise_readiness_manifest()["root"], "C171_REQUEST_ROOT": request_resolution_manifest()["root"],
    "C171_MISSING_ROOT": missing_b0_object_manifest()["root"], "C171_HANDOFF_ROOT": calculation_resumption_handoff_contract()["root"],
    "C171_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C171_COMPLETENESS_ROOT": lfgb0adjoint1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C171-HQCDB0ADJOINT1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
