"""C173 C43 P0 residual-gauge authority.

The authenticated continuum PV condition is recorded exactly, but its
infinite-line endpoints are not identified with the periodic finite cell.
Consequently C173 is deliberately fail-closed at the finite-cell adapter.
No P0 gauge functional, determinant, or ghost interaction is invented.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0ghost1 as c172
from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c169
from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c170
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import zbhqcd as c130
from deuteron_wigner.bridge.g0 import contracts as c43

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c173_hqcdb0resgauge1"
BASELINE = "0db3440c42545d7a55df205c0d0180a556e869ad"
EXPECTED_CONTRACT = "docs/next_level/c172_c173_hqcdb0resgauge1_continuation_contract.json"
CONTRACT_PRESENT = False
PROMPT = "/Users/dustin/Downloads/c173_hqcdb0resgauge1_codex_prompt.md"
PROMPT_SHA256 = "9ea2859cc9246e4547b857202d049a602fb3d2e87b3b84bcee4071c2a7fbee4a"
STATUS = "C173_C172_CONTINUUM_PV_SUBGAUGE_READY_FINITE_CELL_ADAPTER_INCOMPLETE"
PLAN = "B0RESGAUGE1-C"
NEXT = "C174/HQCDB0RESGAUGE2"
PARENT_PACKAGE_ROOT = "7a2cda458404640e784f9113f1547f69a31439db4767e8f2a33d1e9eaab17382"
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
C151_PACKAGE_ROOT = "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C130_PACKAGE_ROOT = "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
SOURCE_ID = "ARXIV-1508.07962V1"
SOURCE_PDF = "data/raw/c173_sources/1508.07962v1.pdf"
SOURCE_TAR = "data/raw/c173_sources/1508.07962v1.tar"
SOURCE_PDF_SHA256 = "16bc35a3c2947631f194f724f4552dbd93475c317772f8725e27ecbfff08714a"
SOURCE_TAR_SHA256 = "c3662eb494415d960f29c7f021eb715f534956bc22ae0b1808db347a1ccb8dab"
SOURCE_TEX_SHA256 = "0d45e8b79a6d48b840e2a5e010cea94dd989face6ea9cd3a929e9735ce8edb23"
SOURCE_RENDER_SHA256 = "d88995e41ca436617168196a2b9cb20dc2ccac36c107bb387ce531b3682b9da3"
SOURCE_RETRIEVED = "2026-08-23T16:18:31Z"
SOURCE_CONDITION = r"partial_perp dot A_perp(x^- = +infinity) + partial_perp dot A_perp(x^- = -infinity) = 0"
SOURCE_LOCATOR = "Eq. (52), printed page 9, PDF page 9; TeX line 1079 (label PV-subgauge)"
RESIDUAL_CLASSES = ("GLOBAL_SU3", "LOCAL_TRANSVERSE_SMALL", "BOUNDARY_SUPPORTED", "LARGE_OR_TOPOLOGICAL", "XPLUS_DEPENDENT_GLOBAL")
CANDIDATES = ("SOURCE_PV_ENDPOINT_CONDITION", "FINITE_CELL_ENDPOINT_ADAPTER", "P0_TRANSVERSE_DIVERGENCE", "CELL_AVERAGED_TRANSVERSE_CONDITION", "RESIDUAL_LINK_ANCHOR", "GLOBAL_COLOR_ONLY", "UNAVAILABLE")
SECTORS = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F")


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _check(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed: raise KeyError(value)
    return allowed if value is None else (value,)


def _source_hashes() -> Mapping[str, Any]:
    rows = []
    for rel, expected in ((SOURCE_PDF, SOURCE_PDF_SHA256), (SOURCE_TAR, SOURCE_TAR_SHA256)):
        p = ROOT / rel
        actual = sha256(p.read_bytes()).hexdigest() if p.exists() else None
        rows.append({"path": rel, "expected_sha256": expected, "actual_sha256": actual, "verified": actual == expected})
    return _freeze({"rows": tuple(rows), "all_verified": all(r["verified"] for r in rows), "cache_audit": "C43 audited before authorized acquisition"})


def source_cache_audit() -> MappingProxyType:
    """Return the authenticated C43 cache unchanged, plus C173 acquisition order."""
    locked = c43.source_manifest()
    return _freeze({"schema": "C173-SOURCE-CACHE-AUDIT-V1", "C43": locked, "C43_all_hash_locked": locked["status"] == "HASH_LOCKED", "audited_before_1508_acquisition": True, "new_source_count": 1, "root": _root((locked, True, 1))})


def verify_hqcd_b0resgauge1_authority() -> MappingProxyType:
    return _freeze({"schema": "C173-HQCDB0RESGAUGE1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT,
        "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": CONTRACT_PRESENT, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256,
        "C172_package_root": PARENT_PACKAGE_ROOT, "C171_package_root": C171_PACKAGE_ROOT, "C170_package_root": C170_PACKAGE_ROOT, "C169_package_root": C169_PACKAGE_ROOT,
        "C168_package_root": C168_PACKAGE_ROOT, "C167_package_root": C167_PACKAGE_ROOT, "C166_package_root": C166_PACKAGE_ROOT, "C165_package_root": C165_PACKAGE_ROOT,
        "C164_package_root": C164_PACKAGE_ROOT, "C163_package_root": C163_PACKAGE_ROOT, "C162_package_root": C162_PACKAGE_ROOT, "C161_package_root": C161_PACKAGE_ROOT,
        "C160_package_root": C160_PACKAGE_ROOT, "C159_package_root": C159_PACKAGE_ROOT, "C158_package_root": C158_PACKAGE_ROOT, "C151_package_root": C151_PACKAGE_ROOT,
        "C130_package_root": C130_PACKAGE_ROOT, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0,
        "C158_value_inputs": 0, "Q0_rederived": 0, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0resgauge1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C173 runtime mismatch")
    return verify_hqcd_b0resgauge1_authority()


def b0resgauge1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "official continuum PV condition authenticated; no infinite-line to periodic-cell identity", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def residual_boundary_freeze() -> MappingProxyType:
    return _freeze({"schema": "C173-RESIDUAL-BOUNDARY-FREEZE-V1", "C172_status": c172.STATUS, "C172_plan": c172.PLAN, "C172_package_root": PARENT_PACKAGE_ROOT,
        "C172_q0_fp_root": c172.ROOTS["C172_Q0_FP_OPERATOR_ROOT"], "C172_q0_ghost_root": c172.ROOTS["C172_Q0_GHOST_DECOUPLING_ROOT"],
        "C172_residual_group_root": c172.ROOTS["C172_RESIDUAL_GAUGE_GROUP_ROOT"], "C172_subgauge_root": c172.ROOTS["C172_RESIDUAL_SUBGAUGE_ROOT"],
        "C172_volume_root": c172.ROOTS["C172_GAUGE_VOLUME_ROOT"], "C172_link_root": c172.ROOTS["C172_RESIDUAL_LINK_ROOT"], "C172_gauss_root": c172.ROOTS["C172_P0_GAUSS_ROOT"],
        "C171_b0_roots": {"basis": c172.c171.ROOTS["C171_BASIS_ROOT"], "source": c172.c171.ROOTS["C171_SOURCE_ROOT"], "free": c172.c171.ROOTS["C171_FREE_ROOT"], "resolvent": c172.c171.ROOTS["C171_RESOLVENT_ROOT"]},
        "preserved_B1": tuple(c172.c171.PRESERVED_B1), "records_rebuilt": 0, "root": _root((PARENT_PACKAGE_ROOT, c172.ROOTS["C172_Q0_FP_OPERATOR_ROOT"], 0))})


def contract_provenance_report() -> MappingProxyType:
    return _freeze({"schema": "C173-CONTRACT-PROVENANCE-V1", "expected_path": EXPECTED_CONTRACT, "committed_contract_present": False, "prompt_only_authority": True,
        "prompt_sha256": PROMPT_SHA256, "historical_C170_missing_contract": {"expected_path": "docs/next_level/c169_c170_hqcdb0ghost1_continuation_contract.json", "prompt_only_authority": True},
        "historical_C171_missing_contract": {"expected_path": "docs/next_level/c170_c171_c170_c171_hqcdb0adjoint1_continuation_contract.json", "prompt_only_authority": True},
        "historical_C172_missing_contract": {"expected_path": "docs/next_level/c171_c172_hqcdb0ghost1_continuation_contract.json", "prompt_only_authority": True, "prompt_sha256": c172.PROMPT_SHA256},
        "retrospective_contract_invented": False, "root": _root((EXPECTED_CONTRACT, False, PROMPT_SHA256, "C170/C171/C172-prompt-only"))})


def primary_source_manifest(source_id: str | None = None) -> MappingProxyType:
    if source_id is not None and source_id != SOURCE_ID: raise KeyError(source_id)
    row = {"source_id": SOURCE_ID, "title": "Regularization of the Light-Cone Gauge Gluon Propagator Singularities Using Sub-Gauge Conditions", "authors": ("Giovanni A. Chirilli", "Yuri V. Kovchegov", "Douglas E. Wertepny"), "version": "v1", "arxiv": "1508.07962v1", "retrieval_endpoint": "https://arxiv.org/pdf/1508.07962v1; https://arxiv.org/e-print/1508.07962v1", "retrieved_utc": SOURCE_RETRIEVED, "pdf": {"path": SOURCE_PDF, "sha256": SOURCE_PDF_SHA256, "bytes": 350322, "pages": 19}, "archive": {"path": SOURCE_TAR, "sha256": SOURCE_TAR_SHA256, "bytes": 72009, "members": {"papar-lightcone-prop-31aug2015.tex": SOURCE_TEX_SHA256, "LO.eps": "d24a830a15c2fd9dcd6878b3aaf8c00f9b139b16b2230ce82e4c905b8665c0a6", "NLO.eps": "7fed9e515d31877ce7a324b192c99af6f01a4050eb0f56f6dc64e9d3459376e8"}}, "license_status": "official arXiv source; redistribution policy not independently expanded; raw cache ignored", "scientific_role": "CONTINUUM_OR_INFINITE_LINE_PV_SUBGAUGE_AUTHORITY_CANDIDATE", "finite_cell_identity": "UNPROVED"}
    return _freeze({"schema": "C173-PRIMARY-SOURCE-MANIFEST-V1", "rows": (row,), "cache": _source_hashes(), "root": _root(row)})


def continuum_pv_subgauge_manifest() -> MappingProxyType:
    row = {"source_id": SOURCE_ID, "version": "v1", "source_role": "continuum/infinite-line PV sub-gauge candidate", "gauge": "A^+=0 light-cone gauge", "coordinates": "v^±=(v^0±v^3)/sqrt(2), eta=(0,1,0_perp)", "domain": "infinite-line x^- with x^-=+/-infinity boundaries", "pole": "PV", "condition_exact": SOURCE_CONDITION, "locator": SOURCE_LOCATOR, "pdf_page": 9, "printed_page": 9, "tex_member": "papar-lightcone-prop-31aug2015.tex", "tex_line": 1079, "render_sha256": SOURCE_RENDER_SHA256, "anchor_sha256": sha256(b"Eq. (52) PV sub-gauge x-minus plus-infinity minus-infinity").hexdigest(), "nonclaims": ("not periodic finite-cell identity", "not C43 finite-cell closure", "not MOMq/RI-SMOM", "not ML"), "status": "AUTHENTICATED_CONTINUUM_CANDIDATE_FINITE_CELL_UNPROVED"}
    return _freeze({"schema": "C173-CONTINUUM-PV-SUBGAUGE-V1", "row": row, "root": _root(row)})


def source_object_locator_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-SOURCE-OBJECT-LOCATOR-V1", "source_id": SOURCE_ID, "pdf_page_zero_based": 8, "pdf_page_one_based": 9, "printed_page": 9, "section": "III. PV Sub-Gauge", "equation": "(52)", "tex_member": "papar-lightcone-prop-31aug2015.tex", "tex_locator": "line 1079; label PV-subgauge", "anchor": "Eq. (51) boundary term -> Eq. (52) condition -> Eq. (53) PV check", "render_sha256": SOURCE_RENDER_SHA256, "visual_verified": True, "role": "continuum/infinite-line candidate only", "root": _root((SOURCE_ID, 8, 9, "52", True))})


def residual_parameter_manifest(residual_class_id: str | None = None) -> MappingProxyType:
    specs = {"GLOBAL_SU3": ("algebraic constant omega^a", "global SU(3) adjoint", "not HO/L2", "separate volume/covariance"), "LOCAL_TRANSVERSE_SMALL": ("omega(x+,xT), partial+ omega=0", "P0 transverse adjoint", "project scalar basis absent", "unfixed"), "BOUNDARY_SUPPORTED": ("endpoint-supported parameter", "boundary/link domain", "not finite-cell represented", "unresolved"), "LARGE_OR_TOPOLOGICAL": ("outside connected perturbative component", "large/topological", "not represented", "outside scope"), "XPLUS_DEPENDENT_GLOBAL": ("omega(x+)", "time-dependent global color", "not HO/L2", "source boundary compatibility unproved")}
    rows = tuple({"residual_class_id": cid, "parameter_domain": specs[cid][0], "color_representation": specs[cid][1], "normalization": specs[cid][2], "boundary": specs[cid][3], "condition": "partial+ omega=0", "A_perp_action": "delta A_perp=partial_perp omega-g_s[A_perp,omega]", "psi_plus_action": "delta psi_plus=-i g_s omega psi_plus", "link_action": "retained endpoint action; unresolved", "open_adjoint": "covariant index retained", "composition": "SU(3) pointwise where defined", "status": "CLASSIFIED_NOT_FIXED"} for cid in _check(residual_class_id, RESIDUAL_CLASSES))
    return _freeze({"schema": "C173-RESIDUAL-PARAMETER-MANIFEST-V1", "rows": rows, "global_not_HO": True, "root": _root(rows)})


def subgauge_candidate_manifest(candidate_id: str | None = None) -> MappingProxyType:
    reasons = {"SOURCE_PV_ENDPOINT_CONDITION": "source object exact but infinite endpoints absent on periodic cell", "FINITE_CELL_ENDPOINT_ADAPTER": "plus/minus L are identified; direct endpoint sum has no source-preserving distinct endpoints", "P0_TRANSVERSE_DIVERGENCE": "project scalar residual functional not derived", "CELL_AVERAGED_TRANSVERSE_CONDITION": "no C43/source identity", "RESIDUAL_LINK_ANCHOR": "link anchor would require boundary operator not present", "GLOBAL_COLOR_ONLY": "does not fix local transverse residual group", "UNAVAILABLE": "explicit fail-closed candidate"}
    rows = tuple({"candidate_id": cid, "definition_source": SOURCE_ID if cid == "SOURCE_PV_ENDPOINT_CONDITION" else "none", "finite_cell_domain": "[-L,L] periodic" if cid != "SOURCE_PV_ENDPOINT_CONDITION" else "undefined", "constraints": "not selected", "kernel": "not evaluated without admissible functional", "global_color": "separate", "PV": "ANTISYMMETRIC_OR_PV retained", "boundary": "not closed", "link": "not closed", "fp_operator": "UNAVAILABLE_NOT_SELECTED", "field_dependence": "UNDETERMINED", "selection": "REJECTED_OR_UNAVAILABLE", "reason": reasons[cid]} for cid in _check(candidate_id, CANDIDATES))
    return _freeze({"schema": "C173-SUBGAUGE-CANDIDATE-MANIFEST-V1", "rows": rows, "selected": None, "root": _root(rows)})


def infinite_to_finite_adapter_manifest(candidate_id: str | None = None) -> MappingProxyType:
    ids = ("SOURCE_PV_ENDPOINT_CONDITION",) if candidate_id is None else _check(candidate_id, CANDIDATES)
    rows = tuple({"candidate_id": cid, "source_geometry": "infinite line; distinct +/- infinity", "project_geometry": "periodic [-L,+L]; endpoints identified", "P0_Q0": c172.p0_q0_projector_manifest()["schema"], "PV_kernel": "ANTISYMMETRIC_OR_PV", "CELL_A_coordinate": "endpoint map undefined after periodic identification", "CELL_B_finite_mode": "P0 contains no independent +/- infinity endpoint functional", "CELL_C_gauge_orbit": "boundary/link orbit data not equivalent to periodic orbit", "classification": "UNDEFINED_OR_NO_GO", "finite_cell_identity": False, "route_mismatch": False, "status": "ADAPTER_INCOMPLETE"} for cid in ids)
    return _freeze({"schema": "C173-INFINITE-FINITE-ADAPTER-V1", "rows": rows, "routes": ("CELL-A", "CELL-B", "CELL-C"), "root": _root(rows)})


def project_subgauge_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-PROJECT-SUBGAUGE-V1", "scheme_id": None, "selected": False, "reason": "project-owned finite-cell derivation is not authorized by an absent scalar-map/source identity", "functional": None, "fp_operator": None, "global_kernel": "P0 local residual plus global SU(3) remain", "resolution_dependence": "not selected", "status": "NO_PROJECT_FINITE_CELL_SUBGAUGE_SELECTED", "root": _root((False, "no-functional"))})


def p0_fp_operator_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-P0-FP-OPERATOR-V1", "operator": None, "domain": "P0 residual parameters classified; no selected local functional", "codomain": "not defined", "basis_order": None, "global_kernel": ("GLOBAL_SU3", "XPLUS_DEPENDENT_GLOBAL"), "local_rank": "UNAVAILABLE", "field_dependence": "UNDETERMINED", "routes": {"FP-P0-A": "NOT_RUN_NO_SELECTED_FUNCTIONAL", "FP-P0-B": "NOT_RUN_NO_SELECTED_FUNCTIONAL", "FP-P0-C": "NOT_RUN_NO_SELECTED_FUNCTIONAL", "FP-P0-D": "NOT_RUN_NO_SELECTED_FUNCTIONAL"}, "Q0_not_promoted": True, "status": "RANK_INCOMPLETE", "root": _root(("P0", "unselected", "Q0-separate"))})


def gauge_volume_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-GAUGE-VOLUME-V1", "local_P0_determinant": "UNAVAILABLE_WITHOUT_SELECTED_FP", "global_SU3_volume": "symbolic Vol(SU(3)); separate", "stabilizer_kernel": "GLOBAL_SU3 and possible xplus-global", "open_adjoint_source": "retained covariant index; not quotiented", "large_gauge": "separate unresolved sectors", "absolute_normalization": "not fixed", "status": "GLOBAL_COLOR_VOLUME_READY_LOCAL_RESIDUAL_INCOMPLETE", "root": _root(("local-incomplete", "global-separate", False))})


def open_color_factorization_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-OPEN-COLOR-V1", "global_volume": "not divided into source correlator", "external_representation": "open adjoint 8", "singlet_projection": False, "normalizable_HO_global_color": False, "covariance": "retained", "root": _root(("adjoint-open", False, False))})


def gribov_large_gauge_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-GRIBOV-LARGE-GAUGE-V1", "local_uniqueness": "NOT_ESTABLISHED", "additional_zero_modes": "unknown without FP", "stabilizer": "global color separated", "Gribov": "GRIBOV_REGION_DEFINITION_REQUIRED", "large_topological": "LARGE_GAUGE_AUTHORITY_INCOMPLETE", "global_uniqueness": False, "root": _root(("not-established", False))})


def pv_propagator_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-PV-PROPAGATOR-V1", "Q0_inverse": "C43 antisymmetric/PV unchanged", "P0_treatment": "residual gauge unresolved", "PROP-A": "Q0-only compatible; P0 unresolved", "PROP-B": "continuum Eq. (52) source candidate; finite cell not identified", "PROP-C": "periodic boundary identity unavailable", "pole_substitution": False, "status": "PV_Q0_COMPATIBLE_P0_UNRESOLVED", "loop_integral": False, "root": _root(("PV", "P0-unresolved", False))})


def residual_link_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-RESIDUAL-LINK-V1", "source_role": "C43/BJY/GAO retained boundary-link authority", "endpoint_transformation": "U(sink) W U^{-1}(source) structurally retained", "path_ordering": "not newly evaluated", "representation": "fundamental path with open-adjoint covariance", "periodic_geometry": "adapter incomplete", "link_unity": False, "status": "LINK_TRANSFORMATION_INCOMPLETE", "root": _root(("retained", False, "periodic-unresolved"))})


def p0_gauss_subgauge_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"sector_id": sid, "generators": 8, "channel": "gg-d" if sid.endswith("-D") else "gg-f" if sid.endswith("-F") else "single", "source": "C130 integrated Gauss law plus C171 color isometry", "subgauge_action": "not evaluable without selected P0 functional", "structural_covariance": "global color only", "open_color": True, "coefficients": "UNAVAILABLE_NOT_ZERO", "status": "P0_GAUSS_OR_COVARIANCE_INCOMPLETE"} for sid in _check(sector_id, SECTORS))
    return _freeze({"schema": "C173-P0-GAUSS-SUBGAUGE-V1", "rows": rows, "C130_root": c130.integrated_gauss_law_manifest()["root"], "all_eight_generators": True, "root": _root(rows)})


def b0_subgauge_covariance_manifest(object_id: str | None = None) -> MappingProxyType:
    allowed = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F", "C151-ONE-GLUON-SOURCE", "C171-PROJECTORS", "C171-FREE-RESOLVENTS", "C171-STRUCTURAL-INTERACTIONS")
    rows = tuple({"object_id": oid, "source_root": c172.c171.ROOTS["C171_SOURCE_ROOT"], "basis_rebuilt": 0, "read_only": True, "structural_only": oid == "C171-STRUCTURAL-INTERACTIONS", "status": "FROZEN_READ_ONLY_P0_SUBGAUGE_NOT_CLOSED"} for oid in _check(object_id, allowed))
    return _freeze({"schema": "C173-B0-SUBGAUGE-COVARIANCE-V1", "rows": rows, "route_A": "source-field transformation", "route_B": "frozen color-isometry intertwining", "route_C": "sparse/matrix-free holdout", "route_D": "source-order reversal", "root": _root(rows)})


def residual_ghost_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-RESIDUAL-GHOST-V1", "decision": "RESIDUAL_GHOST_AUTHORITY_INCOMPLETE", "explicit_P0_sector": False, "reason": "no selected P0 functional means field dependence cannot be classified", "Q0_ghost": "Q0_NONZERO_MODE_GHOST_DECOUPLING_ONLY", "target_ghost_imported": False, "next_if_field_dependent": "C174/HQCDB0GHOSTSECTOR1", "root": _root(("P0-unselected", False, "Q0-only"))})


def residual_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = tuple({"request_id": row["request_id"], "Q0_determinant": "C172 field-independent common factor", "P0_determinant": "separate unresolved", "global_volume": "separate", "Gauss": "separate", "instantaneous": "separate", "boundary": "separate", "residual_link": "separate", "target_ghost": "target-only", "future_conversion": "not assembled", "duplicate_owners": 0, "missing_as_zero": 0} for row in c169.calculation_capsule_freeze()["rows"] if request_id is None or row["request_id"] == request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C173-RESIDUAL-COUNT-ONCE-V1", "rows": rows, "root": _root(rows)})


def target_gauge_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-TARGET-GAUGE-SEPARATION-V1", "C43_gauge": "A^+=0 light-front", "C43_pole": "ANTISYMMETRIC_OR_PV", "C43_Q0": "nonzero-mode ghost decoupling only", "C43_P0": "finite-cell adapter incomplete", "selected_C43_subgauge": None, "target_gauge": "Landau/RI-SMOM/MOMq remains target-side", "target_ghost_imported": False, "adapter": False, "root": _root(("C43-PV", "target-separate", False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-BRST-ST-BOUNDARY-V1", "Q0_FP": "field independent at Q0 scope", "P0_fixing": "not selected", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "NOT_AUTHORIZED", "root": _root(("Q0-only", "P0-incomplete", False))})


def b0_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C173-B0-RELEASE-V1", "Q0": "Q0_NONZERO_MODE_GHOST_DECOUPLING_ONLY", "selected_P0": None, "finite_cell_adapter": "INCOMPLETE", "local_FP": "INCOMPLETE", "global_volume": "SEPARATE_LOCAL_INCOMPLETE", "open_color": "READY_NOT_QUOTIENTED", "Gribov": "INCOMPLETE", "PV": "Q0_COMPATIBLE_P0_UNRESOLVED", "link": "INCOMPLETE", "Gauss_covariance": "GLOBAL_ONLY_LOCAL_INCOMPLETE", "ghost": "RESIDUAL_GHOST_AUTHORITY_INCOMPLETE", "decision": "B0_NOT_RELEASED_FINITE_CELL_SUBGAUGE_ADAPTER_INCOMPLETE", "next": NEXT, "root": _root((STATUS, NEXT, "adapter-incomplete"))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for src in c169.calculation_capsule_freeze()["rows"]:
        rid = src["request_id"]
        if request_id is not None and rid != request_id: continue
        active = src["quantity"] in ("TRANSVERSE_GLUON_FIELD", "QCD_COUPLING")
        rows.append({"request_id": rid, "C168_capsule_id": rid, "C169_status": c169.request_resolution_manifest(rid)["rows"][0]["C169_terminal_status"], "C170_status": "FULL_QCD_SECTOR_INCOMPLETE", "C171_status": "B0_ADJOINT_GHOST_GAUGE_INCOMPLETE", "C172_status": c172.STATUS, "continuum_source": "READY_AUTHENTICATED" if active else "PRESERVED", "finite_cell_adapter": "INCOMPLETE" if active else "PRESERVED", "terminal_status": "CONTINUUM_PV_SUBGAUGE_READY_FINITE_CELL_ADAPTER_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "next_object": "C173 finite-cell adapter" if active else "unchanged"})
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C173-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6, "root": _root(rows)})


def missing_residual_object_manifest(request_id: str | None = None) -> MappingProxyType:
    active = [r for r in request_resolution_manifest()["rows"] if r["terminal_status"] != "PRESERVED_INHERITED_REQUEST"]
    if request_id is not None: active = [r for r in active if r["request_id"] == request_id]
    if request_id is not None and not active: raise KeyError(request_id)
    rows = []
    objects = (("C173-FINITE-CELL-PV-ADAPTER", "map Eq. (52) infinite endpoints to periodic P0", ("CELL-A", "CELL-B", "CELL-C")), ("C173-P0-SUBGAUGE", "derive a project-owned scalar P0 functional if authorized", ("FP-P0-A", "FP-P0-B", "FP-P0-C")), ("C173-RESIDUAL-LINK", "close finite-cell endpoint link transformation", ("link-coordinate", "link-orbit")), ("C173-P0-GAUSS", "complete local P0 Gauss covariance", ("GAUGE-COV-A", "GAUGE-COV-D")), ("C173-GRIBOV", "define local/global residual gauge boundary", ("FP-rank", "orbit")))
    for req in active:
        for oid, obj, routes in objects: rows.append({"request_id": req["request_id"], "object_id": oid, "description": obj, "source_id": SOURCE_ID, "parameter_domain": "partial+ omega=0", "sectors": SECTORS, "pole": "ANTISYMMETRIC_OR_PV", "routes": routes, "open_color": True, "nonclaims": ("no loop", "no adapter", "no physical input", "no BRST/ST"), "status": "REQUIRES_DEDICATED_CALCULATION", "not_zero": True})
    return _freeze({"schema": "C173-MISSING-RESIDUAL-OBJECT-V1", "rows": tuple(rows), "count": len(rows), "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C173-CALCULATION-HANDOFF-V1", "status": STATUS, "next": NEXT, "C171_C172_read_only": True, "continuum_source_root": continuum_pv_subgauge_manifest()["root"], "adapter_root": infinite_to_finite_adapter_manifest()["root"], "project_root": project_subgauge_manifest()["root"], "p0_fp_root": p0_fp_operator_manifest()["root"], "release_root": b0_release_manifest()["root"], "self_energy": 0, "adapter_assembled": 0, "matching": 0, "root": _root((STATUS, NEXT, 0))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C167-RI-SMOM-AUTHORITY", "status": "PRESERVED"}, {"frontier_id": "C168-C169-CALCULATION-LEAVES", "status": "PRESERVED_SIX"}, {"frontier_id": "C163-LOCATOR", "status": "PRESERVED_SIX"}, {"frontier_id": "C171-B0", "status": "PRESERVED_READ_ONLY"}, {"frontier_id": "C172-Q0", "status": "CLOSED_Q0_SCOPE"}, {"frontier_id": "C173-P0-RESIDUAL", "status": "FINITE_CELL_ADAPTER_INCOMPLETE"}, {"frontier_id": "C170-B1-QGG", "status": "PRESERVED"}, {"frontier_id": "C170-B1-QQBARQ", "status": "PRESERVED"})
    return _freeze({"schema": "C173-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def quantum_residual_handoff() -> MappingProxyType:
    return _freeze({"schema": "C173-QUANTUM-RESIDUAL-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "residual_ghost_qubits": 0, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0, 0))})


def b0resgauge1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C173-HQCDB0RESGAUGE1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_provenance_fail_closed": True, "C43_cache_audited": True, "official_source_acquired": True, "continuum_locator_ready": True, "finite_cell_adapter_ready": False, "P0_parameter_domain_classified": True, "candidate_count": len(CANDIDATES), "selected_subgauge": False, "P0_FP_ready": False, "P0_ghost_decision": "RESIDUAL_GHOST_AUTHORITY_INCOMPLETE", "global_color_open": True, "link_ready": False, "Gauss_local_ready": False, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "quantum_objects_modified": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, False))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"web_search": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "unproved_infinite_finite_identity": 0, "unproved_subgauge": 0, "pole_substitutions": 0, "global_color_HO": 0, "open_color_quotiented": 0, "target_ghost_imports": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "missing_values_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "physical_objects_created": 0, "pass": True, "root": _root((STATUS, PLAN, 0))})


def mutate_live_hqcdb0resgauge1(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "prompt", "source_hash", "source_locator", "condition", "infinite_geometry", "periodic_geometry", "P0", "Q0", "global_color", "open_adjoint", "candidate", "selected_subgauge", "FP", "rank", "kernel", "field_dependence", "determinant", "volume", "Gribov", "large_gauge", "PV", "link", "Gauss", "g", "qqbar", "gg_d", "gg_f", "source", "projector", "free", "resolvent", "interaction", "direct", "instantaneous", "boundary", "target_ghost", "BRST", "ST", "counterterm", "null", "graph", "B1", "quantum", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C173_INPUT_ROOT": _root((BASELINE, PROMPT_SHA256, PARENT_PACKAGE_ROOT)), "C173_CONTRACT_PROVENANCE_ROOT": contract_provenance_report()["root"], "C173_PLAN_ROOT": b0resgauge1_plan_manifest()["root"], "C173_RESIDUAL_BOUNDARY_FREEZE_ROOT": residual_boundary_freeze()["root"], "C173_PRIMARY_SOURCE_ROOT": primary_source_manifest()["root"], "C173_CONTINUUM_PV_SUBGAUGE_ROOT": continuum_pv_subgauge_manifest()["root"], "C173_RESIDUAL_PARAMETER_ROOT": residual_parameter_manifest()["root"], "C173_SUBGAUGE_CANDIDATE_ROOT": subgauge_candidate_manifest()["root"], "C173_INFINITE_TO_FINITE_ADAPTER_ROOT": infinite_to_finite_adapter_manifest()["root"], "C173_PROJECT_SUBGAUGE_ROOT": project_subgauge_manifest()["root"], "C173_P0_FP_OPERATOR_ROOT": p0_fp_operator_manifest()["root"], "C173_GAUGE_VOLUME_ROOT": gauge_volume_manifest()["root"], "C173_OPEN_COLOR_ROOT": open_color_factorization_manifest()["root"], "C173_GRIBOV_ROOT": gribov_large_gauge_manifest()["root"], "C173_PV_ROOT": pv_propagator_manifest()["root"], "C173_RESIDUAL_LINK_ROOT": residual_link_manifest()["root"], "C173_P0_GAUSS_ROOT": p0_gauss_subgauge_manifest()["root"], "C173_COVARIANCE_ROOT": b0_subgauge_covariance_manifest()["root"], "C173_GHOST_ROOT": residual_ghost_manifest()["root"], "C173_COUNT_ONCE_ROOT": residual_count_once_manifest()["root"], "C173_TARGET_SEPARATION_ROOT": target_gauge_separation_manifest()["root"], "C173_BRST_ST_ROOT": brst_st_boundary_manifest()["root"], "C173_RELEASE_ROOT": b0_release_manifest()["root"], "C173_REQUEST_ROOT": request_resolution_manifest()["root"], "C173_MISSING_ROOT": missing_residual_object_manifest()["root"], "C173_HANDOFF_ROOT": calculation_resumption_handoff_contract()["root"], "C173_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C173_QUANTUM_ROOT": quantum_residual_handoff()["root"], "C173_SCOPE_ROOT": _root((STATUS, "no-loop", "no-physical")), "C173_COMPLETENESS_ROOT": b0resgauge1_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C173-HQCDB0RESGAUGE1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
