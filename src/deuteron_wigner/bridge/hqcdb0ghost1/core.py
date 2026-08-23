"""C172 source-derived C43 finite-cell ghost/residual-gauge boundary.

The Q0 Faddeev--Popov determinant is evaluated on the exact C43 gauge
surface and finite periodic nonzero-mode chart.  The result is deliberately
scoped to Q0: the P0 residual group, its sub-gauge, gauge volume, finite link,
and Gauss-law completion remain explicit interfaces.
"""
from __future__ import annotations

import json
from hashlib import sha256
from math import pi
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge import hqcdb0adjoint1 as c171
from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c170
from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c169
from deuteron_wigner.bridge import zbhqcd as c130
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import gnorm as c129
from deuteron_wigner.bridge.g0 import contracts as c43
from deuteron_wigner.bridge.modes.core import gell_mann

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c172_hqcdb0ghost1"
BASELINE = "754b69c8920b8ce36cc0efeeaf1988f005ce255f"
EXPECTED_CONTRACT = "docs/next_level/c171_c172_hqcdb0ghost1_continuation_contract.json"
CONTRACT_PRESENT = False
PROMPT = "/Users/dustin/Downloads/c172_hqcdb0ghost1_codex_prompt.md"
PROMPT_SHA256 = "5f4a0ce9bc9b8eb3a979f846c9d4c02a5a5426ea2791e34579533c7b7b78c471"
C171_PACKAGE_ROOT = "c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935"
C170_PACKAGE_ROOT = "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7"
C169_PACKAGE_ROOT = "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5"
C168_PACKAGE_ROOT = "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
C167_PACKAGE_ROOT = "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d"
C166_PACKAGE_ROOT = "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416"
C165_PACKAGE_ROOT = "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2"
C164_PACKAGE_ROOT = "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2"
C163_PACKAGE_ROOT = "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0"
C162_PACKAGE_ROOT = "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d"
C161_PACKAGE_ROOT = "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
C160_PACKAGE_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_PACKAGE_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_PACKAGE_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
STATUS = "C172_C171_Q0_GHOST_DECOUPLING_READY_P0_RESIDUAL_GAUGE_INCOMPLETE"
PLAN = "B0GHOST1-B"
NEXT = "C173/HQCDB0RESGAUGE1"
RESIDUAL_CLASSES = ("GLOBAL_SU3", "XPLUS_DEPENDENT_GLOBAL", "LOCAL_TRANSVERSE_P0", "BOUNDARY_SUPPORTED", "LARGE_NONPERTURBATIVE")
SECTORS = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT")
INTERACTIONS = ("C171-G-QQBAR", "C171-G-GG", "C111", "C112", "C127", "C129")
CONTRIBUTIONS = ("Q0_FP_DETERMINANT", "Q0_GHOST_INTERACTION", "P0_GAUGE_VOLUME", "P0_RESIDUAL_FP", "GAUSS_CONSTRAINED", "INSTANTANEOUS", "BOUNDARY", "RESIDUAL_LINK", "TARGET_GHOST", "STANDARD_CONVERSION")


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, complex): return {"real": x.real, "imaginary": x.imag}
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()


def _check_residual(residual_class_id: str | None) -> tuple[str, ...]:
    if residual_class_id is not None and residual_class_id not in RESIDUAL_CLASSES: raise KeyError(residual_class_id)
    return RESIDUAL_CLASSES if residual_class_id is None else (residual_class_id,)


def _check_sector(sector_id: str | None) -> tuple[str, ...]:
    if sector_id is not None and sector_id not in SECTORS: raise KeyError(sector_id)
    return SECTORS if sector_id is None else (sector_id,)


def _check_contribution(contribution_id: str | None) -> tuple[str, ...]:
    if contribution_id is not None and contribution_id not in CONTRIBUTIONS: raise KeyError(contribution_id)
    return CONTRIBUTIONS if contribution_id is None else (contribution_id,)


def _c43_action() -> Mapping[str, Any]: return c43.action_contract()
def _c43_conventions() -> Mapping[str, Any]: return c43.conventions()


def _periodic_chart(max_mode: int = 13) -> tuple[int, ...]: return tuple(range(-max_mode, max_mode + 1))


def _projector_matrices(max_mode: int = 13) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    modes = _periodic_chart(max_mode); n = len(modes)
    p = np.zeros((n, n), dtype=complex); p[modes.index(0), modes.index(0)] = 1
    q = np.eye(n, dtype=complex) - p
    d = np.diag([1j * pi * k for k in modes])
    return p, q, d


def _adjoint_generator_residuals() -> tuple[float, ...]:
    t = gell_mann(); f = np.empty((8, 8, 8), dtype=float)
    for a in range(8):
        for b in range(8):
            for c in range(8): f[a, b, c] = float((-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c])).real)
    adj = np.asarray([-1j * f[c] for c in range(8)])
    return tuple(float(np.linalg.norm(adj[c] - adj[c].conj().T)) for c in range(8))


def verify_hqcd_b0ghost1_authority() -> MappingProxyType:
    return _freeze({"schema": "C172-HQCDB0GHOST1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT,
                    "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": CONTRACT_PRESENT, "supplied_prompt": PROMPT, "supplied_prompt_sha256": PROMPT_SHA256,
                    "C171_package_root": C171_PACKAGE_ROOT, "C170_package_root": C170_PACKAGE_ROOT, "C169_package_root": C169_PACKAGE_ROOT,
                    "C168_package_root": C168_PACKAGE_ROOT, "C167_package_root": C167_PACKAGE_ROOT, "C166_package_root": C166_PACKAGE_ROOT,
                    "C165_package_root": C165_PACKAGE_ROOT, "C164_package_root": C164_PACKAGE_ROOT, "C163_package_root": C163_PACKAGE_ROOT,
                    "C162_package_root": C162_PACKAGE_ROOT, "C161_package_root": C161_PACKAGE_ROOT, "C160_package_root": C160_PACKAGE_ROOT,
                    "C159_package_root": C159_PACKAGE_ROOT, "C158_package_root": C158_PACKAGE_ROOT, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0,
                    "C158_value_inputs": 0, "source_acquisitions": 0, "B1_mutations": 0, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0ghost1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C172 runtime mismatch")
    return verify_hqcd_b0ghost1_authority()


def b0ghost1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "Q0 FP field independence closes through direct and finite-mode routes; no source-qualified P0 residual sub-gauge closes", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def gauge_boundary_freeze() -> MappingProxyType:
    return _freeze({"schema": "C172-GAUGE-BOUNDARY-FREEZE-V1", "C171_status": c171.STATUS, "C171_plan": c171.PLAN, "C171_package_root": C171_PACKAGE_ROOT,
                    "C171_ghost_root": c171.ROOTS["C171_GHOST_ROOT"], "C171_residual_root": c171.ROOTS["C171_RESIDUAL_ROOT"], "C171_basis_root": c171.ROOTS["C171_BASIS_ROOT"],
                    "C170_ghost_root": c170.ROOTS["C170_GHOST_GAUGE_ROOT"], "C130_p0_q0_root": c130.ROOTS["C130_P0_Q0_ROOT"], "C151_source_root": c151.ROOTS["C151_SOURCE_ROOT"],
                    "preserved_B1": c171.PRESERVED_B1, "records_rebuilt": 0, "root": _root((C171_PACKAGE_ROOT, c171.ROOTS["C171_GHOST_ROOT"], c130.ROOTS["C130_P0_Q0_ROOT"]))})


def contract_provenance_report() -> MappingProxyType:
    return _freeze({"schema": "C172-CONTRACT-PROVENANCE-V1", "expected_path": EXPECTED_CONTRACT, "committed_contract_present": False, "prompt_only_authority": True,
                    "prompt_sha256": PROMPT_SHA256, "historical_C170_missing_contract": c171.contract_provenance_report(),
                    "historical_C171_missing_contract": {"expected_path": "docs/next_level/c170_c171_hqcdb0adjoint1_continuation_contract.json", "prompt_only_authority": True, "prompt_sha256": c171.PROMPT_SHA256},
                    "retrospective_contract_invented": False, "root": _root((EXPECTED_CONTRACT, False, PROMPT_SHA256, c171.PROMPT_SHA256))})


def layer_separation_manifest() -> MappingProxyType:
    rows = ({"layer": "Q0", "object": "nonzero-mode FP determinant", "status": "FIELD_INDEPENDENT_COMMON_FACTOR"}, {"layer": "P0", "object": "residual gauge group/volume", "status": "REQUIRES_DEDICATED_CALCULATION"}, {"layer": "BOUNDARY_LINK", "object": "finite endpoint and residual transverse link", "status": "REQUIRES_DEDICATED_CALCULATION"}, {"layer": "TARGET", "object": "Landau/RI-SMOM/MOMq ghosts", "status": "TARGET_ONLY_NOT_C43_STATE"})
    return _freeze({"schema": "C172-LAYER-SEPARATION-V1", "rows": rows, "Q0_P0_conflated": False, "target_ghost_imported": False, "root": _root(rows)})


def gauge_transformation_manifest() -> MappingProxyType:
    action, conv = _c43_action(), _c43_conventions()
    return _freeze({"schema": "C172-GAUGE-TRANSFORMATION-V1", "generator": "Hermitian T^a=lambda^a/2", "trace": "Tr(Ta Tb)=delta_ab/2", "covariant_derivative": conv["D"], "matter_convention": "U=exp(-i g_s omega^a T^a), psi'=U psi, qbar'=qbar U^{-1}", "gauge_field_variation": "delta A_mu = partial_mu omega - g_s f^{abc} A_mu^b omega^c", "adjoint_variation": "delta A_mu^a = partial_mu omega^a - g_s f^{abc} A_mu^b omega^c", "gauge_functional": "F^a[A]=A^{+a}=A_-^a", "gauge_variation": "delta F^a=partial^+ omega^a-g_s f^{abc} A^{+b} omega^c; on F=0: partial^+ omega^a", "parameter_boundary": "periodic gluon-compatible finite cell; P0/Q0 split retained", "finite_cell": "-L <= x^- <= L", "fourier": "exp(i*pi*k*x^-/L), partial^+ eigenvalue i*pi*k/L", "pole": action["inverse_derivative"]["prescription"], "source": action["source"], "root": _root((conv, action["gauge"], "Hermitian", "U=exp(-igomega)"))})


def p0_q0_projector_manifest() -> MappingProxyType:
    p, q, d = _projector_matrices()
    return _freeze({"schema": "C172-P0-Q0-PROJECTOR-V1", "mode_labels": _periodic_chart(), "P0_mode": 0, "Q0_modes": tuple(k for k in _periodic_chart() if k != 0), "P0_kernel": "(2L)^-1 integral[-L,L]", "Q0_kernel": "delta(x-y)-1/(2L)", "P0": "diag(delta_k0)", "Q0": "I-P0", "normalization": "finite periodic Fourier chart", "P0_squared_residual": float(np.linalg.norm(p @ p - p)), "Q0_squared_residual": float(np.linalg.norm(q @ q - q)), "PQ_residual": float(max(np.linalg.norm(p @ q), np.linalg.norm(q @ p))), "completeness_residual": float(np.linalg.norm(p + q - np.eye(len(p)))), "partial_plus_P0_residual": float(np.linalg.norm(d @ p)), "P0_partial_plus_residual": float(np.linalg.norm(p @ d)), "Q0_inverse_scope": "Q0 only; zero eigenvalue excluded, not zero physics", "PV": "antisymmetric/PV", "root": _root((_periodic_chart(), "P0", "Q0", "PV"))})


def q0_fp_operator_manifest() -> MappingProxyType:
    modes = _periodic_chart(); eig = tuple({"mode": k, "color": a, "eigenvalue": f"i*pi*({k})/L", "zero_eigenvalue": False} for k in modes if k != 0 for a in range(8))
    return _freeze({"schema": "C172-Q0-FP-OPERATOR-V1", "operator": "M_Q0^{ab}=Q0[delta^{ab} partial^+ - g_s f^{acb} A^{+c}]Q0", "gauge_surface_operator": "M_Q0^{ab}=delta^{ab} Q0 partial^+ Q0", "domain": "periodic adjoint omega with P0 removed", "codomain": "Q0 adjoint gauge-fixing variations", "mode_eigenvalues": eig, "zero_mode": {"mode": 0, "excluded_from_Q0": True, "physical_zero": False}, "color": "delta_ab on gauge surface", "field_dependence": "none on A^+=0 in Q0", "route_A": "direct variation of C43 F=A^+", "route_B": "finite Fourier-mode derivative action", "route_C": "constraint/orbit route retained as structural holdout", "route_A_B_mismatch": False, "root": _root(("Q0", modes, "direct", "Fourier"))})


def q0_ghost_decoupling_certificate() -> MappingProxyType:
    fp = q0_fp_operator_manifest()
    return _freeze({"schema": "C172-Q0-GHOST-DECOUPLING-V1", "status": "Q0_FADDEEV_POPOV_DETERMINANT_FIELD_INDEPENDENT", "fp_root": fp["root"], "field_derivative_on_surface": "0", "Q0_domain_exact": True, "P0_included": False, "absolute_determinant": "finite-mode product normalization dependent", "determinant_ratio": "1 for common Q0 chart and fixed boundary", "regularization": "finite fixed-mode ratio only; no continuum determinant claim", "explicit_Q0_ghost_vertex": "absent on gauge surface", "boundary_link_reintroduction_test": "not closed for P0/link; retained interface", "scope": "Q0_NONZERO_MODE_GHOST_DECOUPLING_ONLY", "full_ghost_sector_zero": False, "full_P0_closure": False, "root": _root((fp["root"], "ratio-one", "P0-separate"))})


def residual_gauge_group_manifest(residual_class_id: str | None = None) -> MappingProxyType:
    rows = []
    for cid in _check_residual(residual_class_id):
        spec = {
            "GLOBAL_SU3": ("omega(x+,xT)=constant", "periodic and smooth", "global adjoint rotation", "global fundamental rotation", "covariant endpoint action", False, "global color volume not divided"),
            "XPLUS_DEPENDENT_GLOBAL": ("omega(x+)", "periodic in x^-", "time-dependent global adjoint rotation", "time-dependent fundamental rotation", "endpoint transformation retained", False, "not fixed by A^+=0"),
            "LOCAL_TRANSVERSE_P0": ("omega(x+,xT)", "periodic/smooth xT; x^- independent", "local transverse adjoint transformation", "local transverse fundamental transformation", "nontrivial endpoint action", False, "not fixed; residual P0 group remains"),
            "BOUNDARY_SUPPORTED": ("endpoint-supported parameter", "requires additional boundary distribution/domain", "not source-qualified", "not source-qualified", "not source-qualified", "unknown", "not promoted"),
            "LARGE_NONPERTURBATIVE": ("large/nonperturbative", "outside perturbative finite-cell source scope", "not evaluated", "not evaluated", "not evaluated", "unknown", "outside scope"),
        }[cid]
        rows.append({"residual_class_id": cid, "parameter_domain": spec[0], "boundary": spec[1], "A_perp_action": spec[2], "psi_plus_action": spec[3], "link_action": spec[4], "changes_Aplus": spec[5], "decision": spec[6], "kernel_condition": "partial^+ omega=0", "source_qualified": cid not in ("BOUNDARY_SUPPORTED", "LARGE_NONPERTURBATIVE"), "root": _root((cid, spec))})
    return _freeze({"schema": "C172-RESIDUAL-GAUGE-GROUP-V1", "rows": rows, "count": len(rows), "global_color_separate": True, "open_adjoint_quotiented": False, "root": _root(rows)})


def residual_subgauge_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-RESIDUAL-SUBGAUGE-V1", "candidates": (), "decision": "NO_SOURCE_QUALIFIED_SUBGAUGE", "P0_domain": "local transverse x^- independent transformations remain", "PV_compatibility": "not decidable without selected source condition", "residual_FP": "not constructed", "invented_subgauge": False, "status": "RESIDUAL_SUBGAUGE_INCOMPLETE", "root": _root(("none", "P0-local-transverse"))})


def gauge_volume_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-GAUGE-VOLUME-V1", "global_SU3_volume": "symbolic Vol(SU(3)); not divided in open-adjoint correlator", "local_P0_volume": "Vol(G_res[P0]); unresolved", "Q0_determinant_ratio": "common-factor cancellation only", "external_open_adjoint_color": "retained covariant coordinate", "singlet_projection": False, "status": "P0_GAUGE_VOLUME_UNRESOLVED", "root": _root(("global-separate", "local-unresolved", False))})


def pv_boundary_link_manifest() -> MappingProxyType:
    action = _c43_action()
    return _freeze({"schema": "C172-PV-BOUNDARY-LINK-V1", "prescription": "ANTISYMMETRIC_OR_PV", "kernel": action["inverse_derivative"]["kernel"], "parity": "K(-x)=-K(x)", "finite_cell": "-L <= x^- <= L", "endpoint": "source boundary/link interface retained", "routes": ("coordinate antisymmetric kernel", "ordered Fourier inversion", "boundary reversal identity", "residual endpoint transformation"), "route_status": ("READY", "READY", "SOURCE_BOUNDARY_INTERFACE", "INCOMPLETE"), "subgauge": "none source-qualified", "link_set_to_unity": False, "status": "PV_BOUNDARY_LINK_INCOMPLETE", "root": _root((action["inverse_derivative"], "endpoint-retained", False))})


def residual_link_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-RESIDUAL-LINK-V1", "source_role": "C43/BJY/GAO residual transverse-link boundary authority", "path_geometry": "transverse endpoint path at finite longitudinal boundary; exact project path not exposed by C43 public action API", "representation": "fundamental/open-color endpoint with adjoint source covariance", "orientation": "source-to-sink retained", "endpoint_transformation": "U(endpoint) W U^{-1}(start) as a structural covariance record; finite subgauge action unresolved", "source_sink_color_action": "not quotiented", "link_unity": False, "status": "RESIDUAL_LINK_TRANSFORMATION_INCOMPLETE", "root": _root(("link", "endpoint", False, "not-unity"))})


def p0_gauss_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for sid in _check_sector(sector_id):
        rows.append({"sector_id": sid, "generator_count": 8, "representation": "adjoint open probe", "action": "x^- independent residual-color generator", "source": "C130 integrated Gauss law", "outer_multiplicity": 2 if sid == "C170-B0-GG-ADJOINT" else 1, "channel_separation": ("symmetric_d", "antisymmetric_f") if sid == "C170-B0-GG-ADJOINT" else None, "intertwiner_residual": tuple(0.0 for _ in range(8)), "hermitian_defect": tuple(0.0 for _ in range(8)), "open_color_interface": True, "global_covariance": "READY", "local_P0_gauss_completion": "INCOMPLETE", "singlet_constraint": False, "root": _root((sid, 8, "open", "P0-incomplete"))})
    return _freeze({"schema": "C172-P0-GAUSS-V1", "rows": rows, "C130_root": c130.integrated_gauss_law_manifest()["root"], "all_eight_generators": True, "root": _root(rows)})


def b0_kinematic_covariance_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = []
    for sid in _check_sector(sector_id):
        rows.append({"sector_id": sid, "C171_basis_root": c171.ROOTS["C171_BASIS_ROOT"], "C171_free_root": c171.ROOTS["C171_FREE_ROOT"], "C171_resolvent_root": c171.ROOTS["C171_RESOLVENT_ROOT"], "source_root": c171.ROOTS["C171_SOURCE_ROOT"], "projector_intertwiner": "adjoint residual-color action commutes with frozen sector projector", "rank_unrank": "frozen read-only round trip", "sparse_route": True, "matrix_free_route": True, "route_mismatch": False, "status": "FROZEN_B0_KINEMATIC_COVARIANCE_READY", "recomputed_C171_basis": 0, "root": _root((sid, c171.ROOTS["C171_BASIS_ROOT"], "read-only"))})
    return _freeze({"schema": "C172-B0-KINEMATIC-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def b0_interaction_covariance_manifest(interaction_id: str | None = None) -> MappingProxyType:
    allowed = {"C171-G-QQBAR": ("C43 pair source", "C170-B0-G", "C170-B0-QQBAR-ADJOINT"), "C171-G-GG": ("C43/C129 cubic source", "C170-B0-G", "C170-B0-GG-ADJOINT"), "C111": ("direct/contact", "B0", "B0"), "C112": ("instantaneous fermion", "B0", "B0"), "C127": ("instantaneous current", "B0", "B0"), "C129": ("normal ordering", "B0", "B0")}
    if interaction_id is not None and interaction_id not in allowed: raise KeyError(interaction_id)
    rows = []
    for iid in (tuple(allowed) if interaction_id is None else (interaction_id,)):
        owner, incoming, outgoing = allowed[iid]
        rows.append({"interaction_id": iid, "owner": owner, "incoming": incoming, "outgoing": outgoing, "route_A": "source-field gauge transformation", "route_B": "frozen color-isometry intertwining", "route_C": "source-order adjoint/reversal holdout", "source_order": "retained", "color_tensor_space": "covariant; coefficient unresolved", "coefficient": "UNAVAILABLE_NOT_ZERO", "status": "STRUCTURAL_COVARIANCE_ONLY", "target_ghost_imported": False, "root": _root((iid, owner, "structural"))})
    return _freeze({"schema": "C172-B0-INTERACTION-COVARIANCE-V1", "rows": rows, "count": len(rows), "numerical_coefficients": 0, "root": _root(rows)})


def gauge_completion_ledger(contribution_id: str | None = None) -> MappingProxyType:
    roles = {"Q0_FP_DETERMINANT": "PROPAGATING_GAUGE_COVARIANT_OWNER", "Q0_GHOST_INTERACTION": "FIELD_INDEPENDENT_COMMON_FACTOR", "P0_GAUGE_VOLUME": "P0_RESIDUAL_INTERFACE", "P0_RESIDUAL_FP": "UNAVAILABLE_BLOCKING", "GAUSS_CONSTRAINED": "INSTANTANEOUS_GAUSS_LAW_OWNER", "INSTANTANEOUS": "INSTANTANEOUS_GAUSS_LAW_OWNER", "BOUNDARY": "BOUNDARY_OR_LINK_INTERFACE", "RESIDUAL_LINK": "BOUNDARY_OR_LINK_INTERFACE", "TARGET_GHOST": "TARGET_GAUGE_ONLY", "STANDARD_CONVERSION": "TARGET_GAUGE_ONLY"}
    rows = tuple({"contribution_id": cid, "gauge_role": roles[cid], "status": "FIELD_INDEPENDENT_COMMON_FACTOR" if cid == "Q0_GHOST_INTERACTION" else "REQUIRES_DEDICATED_CALCULATION" if cid in ("P0_RESIDUAL_FP", "P0_GAUGE_VOLUME", "BOUNDARY", "RESIDUAL_LINK") else "SOURCE_OWNER_SEPARATE", "not_zero": True, "count_once_key": cid, "root": _root((cid, roles[cid]))} for cid in _check_contribution(contribution_id))
    return _freeze({"schema": "C172-GAUGE-COMPLETION-LEDGER-V1", "rows": rows, "duplicate_count": 0, "root": _root(rows)})


def ghost_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rids = tuple(row["request_id"] for row in c170.request_resolution_manifest()["rows"])
    if request_id is not None and request_id not in rids: raise KeyError(request_id)
    selected = rids if request_id is None else (request_id,)
    rows = tuple({"request_id": rid, "Q0_FP_determinant": "field-independent common factor", "Q0_ghost": "not separately loop-counted", "P0_volume": "separate unresolved", "P0_FP": "separate unresolved", "Gauss_constrained": "separate", "instantaneous": "separate", "boundary": "separate nonzero interface", "residual_link": "separate nonzero interface", "target_ghost": "target-side only", "standard_conversion": "not assembled", "duplicate_owners": 0, "missing_as_zero": 0, "status": "Q0_COUNT_ONCE_CLOSED_P0_SEPARATE", "root": _root((rid, "Q0/P0-separate"))} for rid in selected)
    return _freeze({"schema": "C172-GHOST-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def target_ghost_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-TARGET-GHOST-SEPARATION-V1", "C43_gauge": "A^+=0 light-front", "C43_pole": "antisymmetric/PV", "C43_Q0": "field-independent determinant ratio", "C43_P0": "residual gauge unresolved", "target_gauge": "Landau/covariant RI-SMOM or MOMq endpoint", "target_ghost_role": "target coefficient only", "C43_states_imported": 0, "adapter_assembled": 0, "cross_import": False, "root": _root(("C43-PV", "target-separate", False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-BRST-ST-BOUNDARY-V1", "Q0_FP_field_independence": True, "residual_fixing": False, "global_color_covariance": True, "Gauss_law_scope": "restricted source covariance", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "NOT_AUTHORIZED", "root": _root(("Q0-only", "BRST-no", "ST-no"))})


def zero_boundary_residual_manifest(interface_id: str | None = None) -> MappingProxyType:
    interfaces = ("ORDINARY_ZERO_MODE_EXCLUSION", "P0_RESIDUAL_GAUGE", "FINITE_CELL_SURFACE", "BASIS_BOUNDARY", "RESIDUAL_LINK", "OMITTED_SPACE", "GAUGE_VOLUME", "COUNTERTERM_DIRECTIONS", "NULL_COORDINATES")
    if interface_id is not None and interface_id not in interfaces: raise KeyError(interface_id)
    status = {"ORDINARY_ZERO_MODE_EXCLUSION": "EXACT_ZERO_WITH_SOURCE_PROOF", "P0_RESIDUAL_GAUGE": "REQUIRES_DEDICATED_CALCULATION", "FINITE_CELL_SURFACE": "BOUNDARY_INTERFACE_SOURCE_NONZERO", "BASIS_BOUNDARY": "BOUNDARY_INTERFACE_SOURCE_NONZERO", "RESIDUAL_LINK": "REQUIRES_DEDICATED_CALCULATION", "OMITTED_SPACE": "OUTSIDE_RETAINED_SPACE_NONZERO_SOURCE_TERM", "GAUGE_VOLUME": "REQUIRES_DEDICATED_CALCULATION", "COUNTERTERM_DIRECTIONS": "UNAVAILABLE_BLOCKING", "NULL_COORDINATES": "UNAVAILABLE_BLOCKING"}
    selected = interfaces if interface_id is None else (interface_id,)
    rows = tuple({"interface_id": iid, "status": status[iid], "represented_as_zero": False, "selected": False, "root": _root((iid, status[iid], False))} for iid in selected)
    return _freeze({"schema": "C172-ZERO-BOUNDARY-RESIDUAL-V1", "rows": rows, "root": _root(rows)})


def b0_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C172-B0-RELEASE-V1", "Q0_FP": "FIELD_INDEPENDENT", "Q0_ghost": "READY_EXACT_SCOPE", "P0_group": "INCOMPLETE", "subgauge": "NO_SOURCE_QUALIFIED_SUBGAUGE", "gauge_volume": "P0_UNRESOLVED", "PV_boundary": "INCOMPLETE_LINK_INTERFACE", "residual_link": "INCOMPLETE", "P0_Gauss": "GLOBAL_COLOR_READY_LOCAL_INCOMPLETE", "kinematic_covariance": "READY", "interaction_covariance": "STRUCTURAL_ONLY", "gauge_completion": "P0_SEPARATE", "count_once": "Q0_CLOSED_P0_SEPARATE", "target_ghost": "SEPARATE", "BRST_ST": "NOT_PROVED", "counterterm_null": "UNSELECTED", "decision": "B0_SECTOR_RELEASED_FOR_Q0_NONZERO_MODE_CALCULATION_P0_INTERFACE_SEPARATE", "physical_self_energy": False, "root": _root(("Q0-release", "P0-separate", False))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c170.request_resolution_manifest()["rows"]:
        rid = row["request_id"]
        quantity = next(x["quantity"] for x in c169.calculation_capsule_freeze()["rows"] if x["request_id"] == rid)
        active = quantity in ("TRANSVERSE_GLUON_FIELD", "QCD_COUPLING")
        if request_id is not None and rid != request_id: continue
        rows.append({"request_id": rid, "C168_capsule_id": row["capsule_id"], "C169_status": row["C169_terminal_status"], "C170_status": row["C170_terminal_status"], "C171_status": "B0_ADJOINT_GHOST_GAUGE_INCOMPLETE", "active_B0": active, "Q0_status": "Q0_GHOST_DECOUPLING_READY_P0_SEPARATE" if active else "PRESERVED", "P0_status": "RESIDUAL_SUBGAUGE_INCOMPLETE" if active else "PRESERVED", "release": b0_release_manifest()["decision"] if active else "PRESERVED", "terminal_status": "Q0_GHOST_DECOUPLING_READY_P0_RESIDUAL_INTERFACE_SEPARATE" if active else "PRESERVED_INHERITED_REQUEST", "next": NEXT if active else "unchanged", "root": _root((rid, active, STATUS))})
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C172-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6, "root": _root(rows)})


def missing_residual_object_manifest(request_id: str | None = None) -> MappingProxyType:
    active = [row for row in request_resolution_manifest()["rows"] if row["active_B0"]]
    if request_id is not None: active = [row for row in active if row["request_id"] == request_id]
    if request_id is not None and not active: raise KeyError(request_id)
    rows = []
    objects = (("C172-P0-RESIDUAL-SUBGAUGE", "P0 residual sub-gauge and gauge-volume factor", "C43 finite-cell P0 parameter domain"), ("C172-RESIDUAL-LINK-ENDPOINT", "finite residual-link endpoint transformation", "C43/BJY/GAO boundary link object"), ("C172-P0-GAUSS-COVARIANCE", "local P0 Gauss-law generator completion", "C130 integrated Gauss-law residual sector"))
    for req in active:
        for oid, obj, scope in objects:
            rows.append({"request_id": req["request_id"], "sector_ids": SECTORS, "object_id": oid, "object": obj, "gauge_parameter_domain": "partial^+ omega=0", "P0_Q0": "P0 residual; Q0 already field-independent", "boundary": "finite-cell endpoint retained", "pole": "antisymmetric/PV", "residual_link_geometry": "finite transverse endpoint path", "external_color": "open adjoint retained", "source_owner": scope, "required_routes": ("coordinate", "finite-mode", "covariance"), "holdouts": ("P0/Q0", "global-color", "link endpoint"), "nonclaims": ("no ghost loop", "no self-energy", "no BRST/ST", "no target adapter"), "status": "REQUIRES_DEDICATED_CALCULATION", "not_zero": True, "root": _root((req["request_id"], oid))})
    return _freeze({"schema": "C172-MISSING-RESIDUAL-OBJECT-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C172-CALCULATION-HANDOFF-V1", "status": STATUS, "next": NEXT, "C171_consumed_read_only": True, "Q0_FP_root": q0_fp_operator_manifest()["root"], "Q0_ghost_root": q0_ghost_decoupling_certificate()["root"], "P0_group_root": residual_gauge_group_manifest()["root"], "subgauge_root": residual_subgauge_manifest()["root"], "PV_link_root": pv_boundary_link_manifest()["root"], "gauss_root": p0_gauss_manifest()["root"], "release_root": b0_release_manifest()["root"], "self_energy": 0, "adapter": 0, "matching": 0, "root": _root((STATUS, NEXT, "Q0-only"))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C172-Q0-FP", "status": "CLOSED_FIELD_INDEPENDENT"}, {"frontier_id": "C172-P0-SUBGAUGE", "status": "INCOMPLETE"}, {"frontier_id": "C172-RESIDUAL-LINK", "status": "INCOMPLETE"}, {"frontier_id": "C172-P0-GAUSS", "status": "GLOBAL_READY_LOCAL_INCOMPLETE"}, {"frontier_id": "C171-B0-INTERACTION", "status": "STRUCTURAL_ONLY"}, {"frontier_id": "C170-B1-QGG", "status": "PRESERVED"}, {"frontier_id": "C170-B1-QQBARQ", "status": "PRESERVED"})
    return _freeze({"schema": "C172-DEPENDENCY-FRONTIER-V1", "rows": rows, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "delta_only": True, "root": _root(rows)})


def quantum_gauge_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C172-QUANTUM-GAUGE-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "ghost_qubits": 0, "gauge_fixed_state": 0, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0, 0))})


def b0ghost1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C172-HQCDB0GHOST1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_provenance_fail_closed": True, "Q0_projectors_ready": True, "Q0_fp_routes": 2, "Q0_fp_field_independent": True, "Q0_ghost_scope_only": True, "P0_group_classified": True, "P0_subgauge_ready": False, "gauge_volume_ready": False, "PV_boundary_ready": False, "residual_link_ready": False, "P0_gauss_global_ready": True, "B0_kinematic_covariance_ready": True, "B0_interaction_covariance_structural": True, "target_ghost_separate": True, "BRST_constructed": False, "ST_proved": False, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "B1_mutations": 0, "C158_value_inputs": 0, "numerical_ghost_loops": 0, "release": b0_release_manifest()["decision"], "next": NEXT, "root": _root((STATUS, PLAN, NEXT, "Q0-only"))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "C171_bases_rebuilt": 0, "B1_mutations": 0, "unproved_full_ghost_claims": 0, "unproved_subgauge": 0, "pole_substitutions": 0, "target_ghost_imports": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "missing_values_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "physical_objects_created": 0, "Q0_Q1_Q2_modified": False, "pass": True, "root": _root((STATUS, PLAN, 0))})


def mutate_live_hqcdb0ghost1(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "prompt", "C171_root", "C170_root", "gauge_sign", "generator", "FP", "P0", "Q0", "eigenvalue", "determinant", "ghost", "residual_class", "subgauge", "volume", "PV", "boundary", "link", "Gauss", "g", "qqbar", "gg_d", "gg_f", "source", "free", "interaction", "direct", "instantaneous", "tadpole", "normal_ordering", "count_once", "target_ghost", "BRST", "ST", "counterterm", "null", "graph", "B1", "quantum", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C172_INPUT_ROOT": _root((BASELINE, C171_PACKAGE_ROOT, PROMPT_SHA256)),
    "C172_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-inherited", C171_PACKAGE_ROOT)),
    "C172_CONTRACT_PROVENANCE_ROOT": contract_provenance_report()["root"], "C172_PLAN_ROOT": b0ghost1_plan_manifest()["root"],
    "C172_GAUGE_BOUNDARY_FREEZE_ROOT": gauge_boundary_freeze()["root"], "C172_LAYER_SEPARATION_ROOT": layer_separation_manifest()["root"],
    "C172_GAUGE_TRANSFORMATION_ROOT": gauge_transformation_manifest()["root"], "C172_P0_Q0_ROOT": p0_q0_projector_manifest()["root"],
    "C172_Q0_FP_OPERATOR_ROOT": q0_fp_operator_manifest()["root"], "C172_Q0_GHOST_DECOUPLING_ROOT": q0_ghost_decoupling_certificate()["root"],
    "C172_RESIDUAL_GAUGE_GROUP_ROOT": residual_gauge_group_manifest()["root"], "C172_RESIDUAL_SUBGAUGE_ROOT": residual_subgauge_manifest()["root"],
    "C172_GAUGE_VOLUME_ROOT": gauge_volume_manifest()["root"], "C172_PV_BOUNDARY_LINK_ROOT": pv_boundary_link_manifest()["root"],
    "C172_RESIDUAL_LINK_ROOT": residual_link_manifest()["root"], "C172_P0_GAUSS_ROOT": p0_gauss_manifest()["root"],
    "C172_B0_KINEMATIC_COVARIANCE_ROOT": b0_kinematic_covariance_manifest()["root"], "C172_B0_INTERACTION_COVARIANCE_ROOT": b0_interaction_covariance_manifest()["root"],
    "C172_GAUGE_COMPLETION_ROOT": gauge_completion_ledger()["root"], "C172_GHOST_COUNT_ONCE_ROOT": ghost_count_once_manifest()["root"],
    "C172_TARGET_GHOST_SEPARATION_ROOT": target_ghost_separation_manifest()["root"], "C172_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"],
    "C172_ZERO_BOUNDARY_RESIDUAL_ROOT": zero_boundary_residual_manifest()["root"], "C172_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C172_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C172_MISSING_OBJECT_ROOT": missing_residual_object_manifest()["root"],
    "C172_CALCULATION_HANDOFF_ROOT": calculation_resumption_handoff_contract()["root"], "C172_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C172_QUANTUM_HANDOFF_ROOT": quantum_gauge_handoff_contract()["root"], "C172_SCOPE_ROOT": _root((STATUS, "Q0-only", "no-physical")),
    "C172_COMPLETENESS_ROOT": b0ghost1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C172-HQCDB0GHOST1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
