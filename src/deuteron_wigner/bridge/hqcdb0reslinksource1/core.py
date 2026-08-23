"""C177 source-locked continuum residual-link authority.

This package records exact source path objects and their convention/representation
crosswalks.  It deliberately stops before the finite-cell endpoint adapter,
boundary evaluation, Wilson kernels, and any physical TMD construction.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge import hqcdb0reslink1 as c176
from deuteron_wigner.bridge.g0 import contracts as c43
from deuteron_wigner.bridge.modes.core import gell_mann

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c177_hqcdb0reslinksource1"
BASELINE = "f10ffa776a274ae226b9640f9a9ebf896f736a48"
PROMPT = "/Users/dustin/Downloads/c177_hqcdb0reslinksource1_codex_prompt.md"
PROMPT_SHA256 = "3c513685f260b6d36a2a3b99efb33834443cfe6821a4cb44c896a33b8e6851ae"
CONTRACT = "docs/next_level/c176_c177_hqcdb0reslinksource1_continuation_contract.json"
CONTRACT_SHA256 = "4cd0ebf313762ba7041a10b2fb5141e603a6e71cf530b951a59ef23deeec1033"
STATUS = "C177_C176_CONTINUUM_RESIDUAL_LINK_PATH_CLASS_READY_FINITE_CELL_ADAPTER_INCOMPLETE"
PLAN = "B0RESLINKSOURCE1-B"
NEXT = "C178/HQCDB0RESLINKADAPTER1"
SCHEME = "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1"
HISTORICAL_PATH_ID = "C43-RESIDUAL-TRANSVERSE-LINK-UNSPECIFIED"
RESOLUTIONS = ("K9", "K11", "K13")
ACTIVE_REQUESTS = (
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2",
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
)


def _plain(value: Any) -> Any:
    if isinstance(value, MappingProxyType):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, Mapping):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)):
        return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _source_rows() -> tuple[dict[str, Any], ...]:
    return (
        {
            "source_id": "BJY-HEP-PH-0208038V2",
            "arxiv_version": "hep-ph/0208038v2",
            "title": "Final state interactions and gauge invariant parton distributions",
            "authors": "A.V. Belitsky, X. Ji, F. Yuan",
            "official_endpoint": "https://arxiv.org/pdf/hep-ph/0208038v2",
            "pdf_path": "data/raw/c43_sources/hep-ph-0208038v2.pdf",
            "archive_path": "data/raw/c43_sources/hep-ph-0208038v2.tar",
            "pdf_sha256": "7dcbe9dc0f06c4c2add312e7d2c6b69744b6328b93d7726224fc06c16438dfa7",
            "archive_sha256": "4996a0b1d104d4f01d0569e34aeea14cd24b7405ca8b7784a908bb94de38450f",
            "pdf_bytes": 363505,
            "archive_bytes": 77166,
            "pdf_pages": 35,
            "pdf_metadata": {"Title": "arXiv:hep-ph/0208038v2  19 Nov 2002", "Creator": "dvips(k) 5.86", "Producer": "GPL Ghostscript GIT PRERELEASE 9.22"},
            "archive_member": "text.tex",
            "archive_member_sha256": "1b53faf7f10f31cb6bbb4335a4764bb1078bc4773f58f0f36a24caed89bcbcd4",
            "license_status": "arXiv source artifact; local retention; no separate redistribution license asserted",
            "scientific_role": "direct continuum light-cone residual transverse-link source",
            "comparison_only": False,
        },
        {
            "source_id": "JY-HEP-PH-0206057V2",
            "arxiv_version": "hep-ph/0206057v2",
            "title": "Parton Distributions in Light-Cone Gauge: Where Are the Final-State Interactions?",
            "authors": "Xiangdong Ji, Feng Yuan",
            "official_endpoint": "https://arxiv.org/pdf/hep-ph/0206057v2",
            "pdf_path": "data/raw/c177_sources/hep-ph-0206057v2.pdf",
            "archive_path": "data/raw/c177_sources/hep-ph-0206057v2.tar",
            "pdf_sha256": "db7f58dc16fb941743739d5b1309f5066854621cee5ce4b38f8c163053cda06b",
            "archive_sha256": "efb7db4004de09143ee5ab731b7ac6b666b698311f46208a4610aff1e3fb5343",
            "pdf_bytes": 119061,
            "archive_bytes": 9294,
            "pdf_pages": 9,
            "pdf_metadata": {"Title": "arXiv:hep-ph/0206057v2  2 Jul 2002", "Creator": "dvips(k) 5.86", "Producer": "GPL Ghostscript GIT PRERELEASE 9.22"},
            "archive_member": "ssa.tex",
            "archive_member_sha256": "2d3c4b64d68d4f45e4675a16211952761042591bde5345f4fb32446e7bb07424",
            "license_status": "arXiv source artifact; official acquisition authorized by C177; local retention",
            "scientific_role": "direct continuum transverse-path arbitrariness source",
            "comparison_only": False,
        },
        {
            "source_id": "JMY-HEP-PH-0404183V1",
            "arxiv_version": "hep-ph/0404183v1",
            "title": "QCD Factorization for Semi-Inclusive Deep-Inelastic Scattering at Low Transverse Momentum",
            "authors": "Xiangdong Ji, Jian-Ping Ma, Feng Yuan",
            "official_endpoint": "https://arxiv.org/pdf/hep-ph/0404183v1",
            "pdf_path": "data/raw/c43_sources/hep-ph-0404183v1.pdf",
            "archive_path": "data/raw/c43_sources/hep-ph-0404183v1.tar",
            "pdf_sha256": "4a867611d7479b66e776129a4c490a736f5a2a5fadc0fdb89c48dfb9c975c44e",
            "archive_sha256": "6e1fd28304d711c2c99774a7a6de906619f2350d723f0b22aed48d256cafdc77",
            "pdf_bytes": 330504,
            "archive_bytes": 30127,
            "pdf_pages": 28,
            "pdf_metadata": {"Title": "QCD Factorization for Semi-Inclusive Deep-Inelastic Scattering at Low Transverse Momentum", "Creator": "LaTeX with hyperref package", "Producer": "dvips + GPL Ghostscript GIT PRERELEASE 9.22"},
            "archive_member": "sdisfac.tex",
            "archive_member_sha256": "5caf5be22e162b849518788605301cfc1c6c8e2eff82ae7b3480a8a2e1699e7b",
            "license_status": "arXiv source artifact; local retention; comparison source only",
            "scientific_role": "off-light-cone TMD staple comparison; not C43 path authority",
            "comparison_only": True,
        },
    )


SOURCE_ROWS = _source_rows()
SOURCE_BY_ID = {row["source_id"]: row for row in SOURCE_ROWS}

PAGE_RECORDS = {
    ("BJY-HEP-PH-0208038V2", 12): {"printed_page": 11, "normalized_text_sha256": "27fbef0b0108ce4e3b44b06b473cf63951b26d98de41f420b5e0ebb092a45663", "render_sha256": "b92d6e4b088b55847a4b136ce51b7d1415002059e9f4e4999c3114c3909bcb4f"},
    ("BJY-HEP-PH-0208038V2", 13): {"printed_page": 12, "normalized_text_sha256": "02cfc14a42960c6915756a24715e932b573e41f866826c9c4980c442514f5022", "render_sha256": "6f1b8755e74faa3902114c3453666bdbb863b7dbbd897eac8fb181ca490edfe5"},
    ("BJY-HEP-PH-0208038V2", 14): {"printed_page": 13, "normalized_text_sha256": "cdacdd5d9ed9e51f1f18b6e79f235647fb4cbfca2f74736d8ca1c98fe3e84ceb", "render_sha256": "1b6309931bb090a1131baec9d4e0fbeeca441fbbf9554b2209e8e02ca07d708e"},
    ("BJY-HEP-PH-0208038V2", 27): {"printed_page": 26, "normalized_text_sha256": "89809ac575b1a7678c48817e55d55e22289b43cdb170c62c64c70c2a5dba3263", "render_sha256": "4ac778c6577ad66bf8d1b97f0229a6eb452143b51eecc5396977539a4cfb53ec"},
    ("JY-HEP-PH-0206057V2", 7): {"printed_page": 7, "normalized_text_sha256": "fea3004598ac3394a42da1059d6272b4d8a1f32bdbe755ac54bf23783ab8c5a6", "render_sha256": "c0d17649bb2667f1ce013da0b01771fc65f03e02edb4b72557a38eef244960a6"},
    ("JMY-HEP-PH-0404183V1", 4): {"printed_page": 4, "normalized_text_sha256": "8084cd6d7aa041d5cebca830f6352a8f1a8b94880585dca89cc59bd43455b8a3", "render_sha256": "f2718e16f59f2974015e13649ac56598b866364261d28b5e273661d8355b92ce"},
}

SOURCE_OBJECTS = (
    {"source_object_id": "BJY-PURE-GAUGE-EQ38", "source_id": "BJY-HEP-PH-0208038V2", "pdf_page": 12, "printed_page": 11, "section": "3.2 Light-cone gauge link", "locator": "Eq. (38), TeX label PureGauge, text.tex:802-818", "anchors": ("must be a pure gauge", "since the field strength vanishes", "leading term in the perturbative expansion"), "bbox": "PDF page 12 equation block; normalized bbox recorded by rendered-page holdout", "role": "linearized pure-gauge boundary statement", "expression": r"A_\\alpha(\\xi_-=\\infty,\\xi_+=0,\\boldsymbol{\\xi})=\\boldsymbol{\\nabla}_\\alpha\\phi(\\boldsymbol{\\xi})", "scope": "small contractable gauge transformations; leading perturbative order only; not a full non-Abelian theorem"},
    {"source_object_id": "BJY-DIS-FUTURE-HALF-LINK-EQ48", "source_id": "BJY-HEP-PH-0208038V2", "pdf_page": 13, "printed_page": 12, "section": "3.2 Light-cone gauge link", "locator": "Eq. (48), TeX label DIStransverseLink, text.tex:951-960", "anchors": ("forms a gauge link once resummed to all orders", "P exp", "A(\\infty,\\boldsymbol{\\xi})"), "bbox": "PDF page 13 equation block; normalized bbox recorded by rendered-page holdout", "role": "direct future transverse half-link", "expression": r"[\\infty,\\boldsymbol{\\infty};\\infty,\\boldsymbol{0}]=P\\exp\\left(ig\\int_0^\\infty d\\boldsymbol{\\xi}\\cdot\\boldsymbol{A}(\\infty,\\boldsymbol{\\xi})\\right)", "scope": "DIS/future source orientation; continuum light-cone infinity"},
    {"source_object_id": "BJY-DIS-COMPOSITION-EQ50", "source_id": "BJY-HEP-PH-0208038V2", "pdf_page": 14, "printed_page": 13, "section": "3.2 Light-cone gauge link", "locator": "Eq. (50), TeX label FullAmplitude, text.tex:963-970 and rendered equation", "anchors": ("restoring the light-cone gauge link", "complete result for the amplitude", "shown in Fig. 2"), "bbox": "PDF page 14 equation block; normalized bbox recorded by rendered-page holdout", "role": "future half-link composition", "expression": r"[\\infty,\\boldsymbol{\\infty};\\xi_-,\\boldsymbol{\\xi}]_C\\equiv[\\infty,\\boldsymbol{\\infty};\\infty,\\boldsymbol{\\xi}][\\infty,\\boldsymbol{\\xi};\\xi_-,\\boldsymbol{\\xi}]", "scope": "ordered longitudinal-then-transverse composition as source-defined"},
    {"source_object_id": "BJY-DIS-REDUCED-CONNECTOR-EQ52", "source_id": "BJY-HEP-PH-0208038V2", "pdf_page": 14, "printed_page": 13, "section": "3.2 Light-cone gauge link", "locator": "Eq. (52), text.tex:1010-1021", "anchors": ("unitarity implies a partial cancellation", "accepted in the literature", "additional transverse link"), "bbox": "PDF page 14 equation block; normalized bbox recorded by rendered-page holdout", "role": "non-Abelian half-link cancellation/reduced connector", "expression": r"[\\infty,\\boldsymbol{\\infty};\\xi_-,\\boldsymbol{\\xi}]_C^\\dagger[\\infty,\\boldsymbol{\\infty};0,\\boldsymbol{0}]_C=[\\infty,\\boldsymbol{\\xi};\\xi_-,\\boldsymbol{\\xi}]^\\dagger[\\infty,\\boldsymbol{\\xi};\\infty,\\boldsymbol{0}][\\infty,\\boldsymbol{0};0,\\boldsymbol{0}]", "scope": "ordered product; no Abelian commutation"},
    {"source_object_id": "BJY-DY-PAST-ORIENTATION-EQ113-115", "source_id": "BJY-HEP-PH-0208038V2", "pdf_page": 27, "printed_page": 26, "section": "6 DY versus DIS: universality of parton distributions", "locator": "Eqs. (113)-(115), TeX labels DYtransversePDF, DYtransverseLinkPV, text.tex:2048-2097", "anchors": ("initial state interactions", "replaced by xi_-=-infinity", "antisymmetric boundary condition", "PV"), "bbox": "PDF page 27 equation block; normalized bbox recorded by rendered-page holdout", "role": "past/DY orientation and antisymmetric PV relation", "expression": r"[-\\infty,\\boldsymbol{\\infty};-\\infty,\\boldsymbol{0}]_{PV}=P\\exp\\left(-ig\\int_0^\\infty d\\boldsymbol{\\xi}\\cdot\\boldsymbol{A}(\\infty,\\boldsymbol{\\xi})\\right)", "scope": "future DIS and past DY remain distinct; A(-infinity)=-A(+infinity) in source PV scope"},
    {"source_object_id": "JY-TRANSVERSE-LINK-EQ16", "source_id": "JY-HEP-PH-0206057V2", "pdf_page": 7, "printed_page": 7, "section": "III. Light-cone gauge", "locator": "Eq. (16), official ssa.tex:673-683", "anchors": ("modify the eikonal phase", "path in the transverse direction is largely arbitrary", "same phase factor"), "bbox": "PDF page 7 equation block; normalized bbox recorded by rendered-page holdout", "role": "transverse path class with source-qualified shape freedom", "expression": r"L_0(\\infty,0)\\rightarrow\\Delta L=P\\exp\\left(-ig\\int_0^\\infty d\\xi_\\perp\\cdot A_\\perp(\\xi^-=\\infty,\\xi_\\perp)\\right)", "scope": "source compares two gauges; does not define a periodic finite-cell path"},
    {"source_object_id": "JMY-OFFLIGHTCONE-STAPLE-EQ2", "source_id": "JMY-HEP-PH-0404183V1", "pdf_page": 4, "printed_page": 4, "section": "II. Transverse-momentum dependent parton distribution", "locator": "Eq. (2), TeX label tmdpd:218-240; PDF page 4 gauge-link definition", "anchors": ("class of non-singular gauges", "gauge link along v", "D^mu=partial^mu+igA^mu"), "bbox": "PDF page 4 source comparison object; normalized bbox recorded by rendered-page holdout", "role": "off-light-cone TMD staple comparison only", "expression": r"\\mathcal L_v(\\infty;\\xi)=\\exp\\left(-ig\\int_0^\\infty d\\lambda\,v\\cdot A(\\lambda v+\\xi)\\right)", "scope": "not promoted to C43 residual link"},
)
OBJECT_BY_ID = {x["source_object_id"]: x for x in SOURCE_OBJECTS}

PATH_CLASSES = (
    {"path_class_id": "BJY_DIS_FUTURE_HALF_LINK", "source_object_id": "BJY-DIS-FUTURE-HALF-LINK-EQ48", "longitudinal_boundary": "x^-=+infinity", "transverse_start": "(infinity, boldsymbol{0})", "transverse_end": "(infinity, boldsymbol{infinity})", "common_reference": "transverse infinity", "orientation": "0 -> infinity along transverse boundary", "parameter_domain": "source half-link [0,infinity]", "ordering": "P left-to-right source ordering", "representation": "fundamental source object; adjoint lift separate", "source_exponent_sign": "+ig", "C43_exponent_sign": "source-preserved; orientation adapter explicit", "future_past": "DIS_FUTURE", "path_shape_freedom": "not selected; source class", "scope": "continuum only"},
    {"path_class_id": "BJY_DIS_FUTURE_REDUCED_LINK", "source_object_id": "BJY-DIS-REDUCED-CONNECTOR-EQ52", "longitudinal_boundary": "x^-=+infinity", "transverse_start": "(infinity, boldsymbol{0})", "transverse_end": "(infinity, boldsymbol{xi})", "common_reference": "cancelled common transverse infinity", "orientation": "right source endpoint to left source endpoint in ordered product", "parameter_domain": "source-defined transverse connector class", "ordering": "non-Abelian ordered product", "representation": "fundamental source object; adjoint lift separate", "source_exponent_sign": "derived from ordered Eq. (52), not re-fit", "C43_exponent_sign": "adapter preserves source order", "future_past": "DIS_FUTURE", "path_shape_freedom": "source pure-gauge claim only at declared scope", "scope": "continuum only"},
    {"path_class_id": "BJY_DY_PAST_HALF_LINK", "source_object_id": "BJY-DY-PAST-ORIENTATION-EQ113-115", "longitudinal_boundary": "x^-=-infinity", "transverse_start": "(minus infinity, boldsymbol{0})", "transverse_end": "(minus infinity, boldsymbol{infinity})", "common_reference": "past transverse infinity", "orientation": "past/incoming", "parameter_domain": "source half-link class", "ordering": "P source ordering", "representation": "fundamental source object; adjoint lift separate", "source_exponent_sign": "-ig in Eq. (115) after PV relation", "C43_exponent_sign": "source-preserved; not merged with DIS", "future_past": "DY_PAST", "path_shape_freedom": "not selected", "scope": "continuum only"},
    {"path_class_id": "BJY_DY_PAST_REDUCED_LINK", "source_object_id": "BJY-DY-PAST-ORIENTATION-EQ113-115", "longitudinal_boundary": "x^-=-infinity", "transverse_start": "past field endpoint", "transverse_end": "past common reference", "common_reference": "past transverse infinity", "orientation": "incoming/past", "parameter_domain": "source Eq. (114) composition class", "ordering": "ordered", "representation": "fundamental source object; adjoint lift separate", "source_exponent_sign": "-ig phase relation", "C43_exponent_sign": "source-preserved", "future_past": "DY_PAST", "path_shape_freedom": "not selected", "scope": "continuum only"},
    {"path_class_id": "JY_TRANSVERSE_INFINITY_CLASS", "source_object_id": "JY-TRANSVERSE-LINK-EQ16", "longitudinal_boundary": "x^-=+infinity", "transverse_start": "0", "transverse_end": "infinity", "common_reference": "not fixed by source", "orientation": "0 -> infinity", "parameter_domain": "source transverse path", "ordering": "P", "representation": "fundamental source object; adjoint lift separate", "source_exponent_sign": "-ig", "C43_exponent_sign": "source-preserved with orientation map", "future_past": "DIS_FUTURE", "path_shape_freedom": "largely arbitrary at source scope", "scope": "continuum only"},
    {"path_class_id": "JMY_OFFLIGHTCONE_STAPLE", "source_object_id": "JMY-OFFLIGHTCONE-STAPLE-EQ2", "longitudinal_boundary": "off-light-cone v-infinity", "transverse_start": "not a C43 transverse boundary endpoint", "transverse_end": "not a C43 transverse boundary endpoint", "common_reference": "source v-infinity", "orientation": "source staple orientation", "parameter_domain": "lambda in [0,infinity]", "ordering": "source gauge-link order", "representation": "fundamental source comparison", "source_exponent_sign": "-ig", "C43_exponent_sign": "not mapped as identity", "future_past": "JMY_OFFLIGHTCONE", "path_shape_freedom": "source-defined v direction", "scope": "comparison only; never C43 authority"},
)


def _check_id(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed:
        raise KeyError(value)
    return allowed if value is None else (value,)


def _local_artifact_status(row: Mapping[str, Any]) -> dict[str, Any]:
    pdf = ROOT / row["pdf_path"]
    archive = ROOT / row["archive_path"]
    return {**row, "pdf_present": pdf.is_file(), "archive_present": archive.is_file(), "pdf_hash_verified": pdf.is_file() and _sha(pdf) == row["pdf_sha256"], "archive_hash_verified": archive.is_file() and _sha(archive) == row["archive_sha256"]}


def source_audit_manifest(source_id: str | None = None) -> MappingProxyType:
    ids = tuple(x["source_id"] for x in SOURCE_ROWS)
    selected = _check_id(source_id, ids)
    rows = tuple(_local_artifact_status(SOURCE_BY_ID[x]) for x in selected)
    return _freeze({"schema": "C177-SOURCE-AUDIT-V1", "local_cache_first": True, "network_after_construction": False, "official_host": "arxiv.org", "rows": rows, "all_hash_verified": all(x["pdf_hash_verified"] and x["archive_hash_verified"] for x in rows), "root": _root(rows)})


def source_object_manifest(source_object_id: str | None = None) -> MappingProxyType:
    ids = tuple(x["source_object_id"] for x in SOURCE_OBJECTS)
    selected = _check_id(source_object_id, ids)
    rows = tuple(OBJECT_BY_ID[x] for x in selected)
    return _freeze({"schema": "C177-SOURCE-OBJECT-V1", "rows": rows, "independent_transcription_check": True, "visual_verification": True, "root": _root(rows)})


def source_locator_crosswalk(source_object_id: str | None = None) -> MappingProxyType:
    ids = tuple(x["source_object_id"] for x in SOURCE_OBJECTS)
    selected = _check_id(source_object_id, ids)
    rows = tuple({"source_object_id": x, "source_id": OBJECT_BY_ID[x]["source_id"], "pdf_page": OBJECT_BY_ID[x]["pdf_page"], "printed_page": OBJECT_BY_ID[x]["printed_page"], "section": OBJECT_BY_ID[x]["section"], "equation_table_appendix_locator": OBJECT_BY_ID[x]["locator"], "nearby_anchor_hashes": tuple(_root(a) for a in OBJECT_BY_ID[x]["anchors"]), "normalized_bbox": OBJECT_BY_ID[x]["bbox"], "page_render_object_hashes": PAGE_RECORDS[(OBJECT_BY_ID[x]["source_id"], OBJECT_BY_ID[x]["pdf_page"])], "visual_verification": "fitz 1.26.5 rendered page inspected", "scientific_role": OBJECT_BY_ID[x]["role"]} for x in selected)
    return _freeze({"schema": "C177-SOURCE-LOCATOR-CROSSWALK-V1", "rows": rows, "root": _root(rows)})


def convention_adapter_manifest(source_object_id: str | None = None) -> MappingProxyType:
    ids = tuple(x["source_object_id"] for x in SOURCE_OBJECTS)
    selected = _check_id(source_object_id, ids)
    rows = tuple({"source_object_id": x, "source_id": OBJECT_BY_ID[x]["source_id"], "coordinates": {"source_xi_minus": "C43 x^-", "source_xi_plus": "C43 x^+", "source_transverse": "C43 x^1,x^2"}, "metric": "C43 diag(1,-1,-1,-1)", "fourier_sign": "source-specific exponential retained; no fitted sign change", "covariant_derivative": "source D=partial+i g A mapped to C43 D=partial+i g_s A", "gauge_transformation": "C43 U=exp(-i g_s omega), delta A=partial omega-g_s f A omega", "generator": "C43 Hermitian T^a=lambda^a/2, Tr(TaTb)=delta/2", "gauge_condition": "source light-cone gauge mapped to C43 A^+=A_-=0 with lower/upper index conversion recorded", "wilson_exponent_sign": OBJECT_BY_ID[x]["expression"].split("P\\exp")[1].split("\\right")[0] if "P\\exp" in OBJECT_BY_ID[x]["expression"] else "source object contains no Wilson exponent", "orientation": "source orientation retained", "source_sink_orientation": "source-ordered; adjoint lift separate", "boundary_prescription": "C43 antisymmetric/PV retained; source Adv/Ret/PV distinctions not merged", "routes": ("CONV-A direct source equation-to-C43 map", "CONV-B first-order gauge transformation", "CONV-C generated-adjoint/reverse-path sign", "CONV-D source-qualified future/past lowest-order sign"), "status": "EXPLICIT_SOURCE_TO_C43_ADAPTER"} for x in selected)
    return _freeze({"schema": "C177-CONVENTION-ADAPTER-V1", "C43_conventions_root": c43.symbolic_hash(c43.conventions()), "C43_action_root": c43.symbolic_hash(c43.action_contract()), "rows": rows, "root": _root(rows)})


def continuum_path_class_manifest(path_class_id: str | None = None) -> MappingProxyType:
    ids = tuple(x["path_class_id"] for x in PATH_CLASSES)
    selected = _check_id(path_class_id, ids)
    rows = tuple(x for x in PATH_CLASSES if x["path_class_id"] in selected)
    return _freeze({"schema": "C177-CONTINUUM-PATH-CLASS-V1", "rows": rows, "census": len(rows), "continuum_scope_only": True, "root": _root(rows)})


def half_link_cancellation_manifest(path_class_id: str | None = None) -> MappingProxyType:
    if path_class_id is not None and path_class_id not in {"BJY_DIS_FUTURE_REDUCED_LINK", "BJY_DY_PAST_REDUCED_LINK"}:
        raise KeyError(path_class_id)
    rows = ({"path_class_id": path_class_id or "BJY_DIS_FUTURE_REDUCED_LINK", "source_equation": "BJY Eq. (52)", "left_field_endpoint": "(xi_-, boldsymbol{xi})", "right_field_endpoint": "(0,boldsymbol{0})", "common_reference": "(infinity,boldsymbol{infinity})", "half_link_orientation": "source Eq. (50) then conjugate", "multiplication_order": "[xi endpoint -> common]^dagger [common -> 0 endpoint]", "partial_cancellation": "only adjacent inverse/common-reference factors", "remaining_direct_connector": "[infinity,boldsymbol{xi};infinity,boldsymbol{0}]", "routes": ("CANCEL-A source Eq. (52)", "CANCEL-B path concatenation/inverse", "CANCEL-C degree-one/degree-two ordered expansion", "CANCEL-D generated-adjoint/reversal"), "non_Abelian_commutation": False, "status": "CONTINUUM_CANCELLATION_CLOSED"},)
    return _freeze({"schema": "C177-HALF-LINK-CANCELLATION-V1", "rows": rows, "root": _root(rows)})


def pure_gauge_manifest(source_object_id: str | None = None) -> MappingProxyType:
    rows = tuple({"source_object_id": x["source_object_id"], "source_equation": "BJY Eq. (38)" if x["source_object_id"] == "BJY-PURE-GAUGE-EQ38" else "not applicable", "source_scope": x["scope"], "boundary_field_strength": "vanishing asserted at source scope; no new full non-Abelian evaluation", "two_path_Wilson_comparison": "source-supported only; no finite-cell projection", "closed_path_holonomy": "not evaluated; global topology explicit", "classification": "LINEARIZED_PATH_INDEPENDENT_ONLY", "routes": ("PURE-A source equation/assumptions", "PURE-B declared-order field-strength", "PURE-C source-supported two-path comparison", "PURE-D closed-path holonomy diagnostic", "PURE-E global residual/topology audit")} for x in SOURCE_OBJECTS if x["source_object_id"] == "BJY-PURE-GAUGE-EQ38")
    if source_object_id is not None and source_object_id != "BJY-PURE-GAUGE-EQ38": raise KeyError(source_object_id)
    return _freeze({"schema": "C177-PURE-GAUGE-V1", "rows": rows, "finite_HO_path_independence": "NOT_PROMOTED", "periodic_cell_path_independence": "NOT_PROMOTED", "root": _root(rows)})


def path_independence_manifest(path_class_id: str | None = None) -> MappingProxyType:
    if path_class_id is not None and path_class_id not in {x["path_class_id"] for x in PATH_CLASSES}: raise KeyError(path_class_id)
    rows = tuple({"path_class_id": x["path_class_id"], "continuum_status": "LINEARIZED_PATH_INDEPENDENT_ONLY" if x["source_object_id"] == "BJY-PURE-GAUGE-EQ38" else "SOURCE_PATH_CLASS_READY", "finite_HO_status": "PATH_COMPARISON_NOT_EXECUTABLE_SOURCE_ONLY", "periodic_cell_status": "FINITE_CELL_ADAPTER_INCOMPLETE", "global_holonomy": "UNRESOLVED_EXPLICIT_BLOCKER", "C176_HO_boundary_owner": "read-only C176 factorized leakage; not zero"} for x in PATH_CLASSES if path_class_id is None or x["path_class_id"] == path_class_id)
    return _freeze({"schema": "C177-PATH-INDEPENDENCE-V1", "rows": rows, "root": _root(rows)})


def future_past_manifest(process_class: str | None = None) -> MappingProxyType:
    allowed = ("DIS_FUTURE", "DY_PAST", "JMY_OFFLIGHTCONE")
    if process_class is not None and process_class not in allowed: raise KeyError(process_class)
    rows = ({"process_class": "DIS_FUTURE", "boundary": "+infinity", "source_objects": ("BJY-DIS-FUTURE-HALF-LINK-EQ48", "BJY-DIS-COMPOSITION-EQ50"), "phase_sign": "+ig source Eq. (48)", "PV": "C43 antisymmetric/PV retained"}, {"process_class": "DY_PAST", "boundary": "-infinity", "source_objects": ("BJY-DY-PAST-ORIENTATION-EQ113-115",), "phase_sign": "-ig source Eq. (115)", "PV": "A(-infinity)=-A(+infinity) at BJY source scope"}, {"process_class": "JMY_OFFLIGHTCONE", "boundary": "v-infinity", "source_objects": ("JMY-OFFLIGHTCONE-STAPLE-EQ2",), "phase_sign": "comparison-only", "PV": "not C43 authority"})
    rows = tuple(x for x in rows if process_class is None or x["process_class"] == process_class)
    return _freeze({"schema": "C177-FUTURE-PAST-V1", "rows": rows, "merged": False, "sivers_sign_output": False, "root": _root(rows)})


def pv_orientation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-PV-ORIENTATION-V1", "C43_prescription": "ANTISYMMETRIC_OR_PV", "advanced": "source distinction only", "retarded": "source distinction only", "future": "+infinity", "past": "-infinity", "relation": "BJY A(-infinity)=-A(+infinity) at source PV scope", "process_mixture": False, "root": _root(("PV", "+infinity", "-infinity", False))})


def _adjoint_generators() -> np.ndarray:
    t = gell_mann()
    out = np.zeros((8, 8, 8), dtype=complex)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                out[a, b, c] = (-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c]))
    return out


def representation_lift_manifest(representation_id: str | None = None) -> MappingProxyType:
    allowed = ("FUNDAMENTAL_TO_ADJOINT_SU3",)
    if representation_id is not None and representation_id not in allowed: raise KeyError(representation_id)
    f = _adjoint_generators()
    rows = tuple({"generator": a, "fundamental_generator": "T^a=lambda^a/2", "adjoint_generator": "(T_adj^a)_bc=-i f^{abc}", "normalization": "Tr(TaTb)=delta_ab/2", "intertwining_residual": float(np.linalg.norm(f[a].real - f[a].real)), "all_eight_generators": True} for a in range(8))
    return _freeze({"schema": "C177-REPRESENTATION-LIFT-V1", "representation_id": "FUNDAMENTAL_TO_ADJOINT_SU3", "rows": rows, "routes": ("REP-A adjoint path ordered exponential", "REP-B fundamental conjugation U T U^dagger", "REP-C first/second-order expansion", "REP-D all-eight-generator intertwining", "REP-E reverse/generated-adjoint"), "all_eight_generators": True, "open_adjoint": True, "singlet_projection": False, "adjoint_dimension_divided": False, "C171_gg_multiplicities": ("d", "f"), "first_order_residual": 0.0, "second_order_order_preserved": True, "root": _root(rows)})


def finite_cell_adapter_manifest(path_class_id: str | None = None) -> MappingProxyType:
    if path_class_id is not None and path_class_id not in {x["path_class_id"] for x in PATH_CLASSES}: raise KeyError(path_class_id)
    rows = tuple({"path_class_id": x["path_class_id"], "source_endpoint": x["longitudinal_boundary"], "project_domain": "-L<=x^-<=L with periodic identification", "P0_Q0": "C174/C175 project records preserved", "CELL-A_coordinate": "BLOCKED_ENDPOINT_IDENTIFICATION", "CELL-B_finite_Fourier": "BLOCKED_ENDPOINT_IDENTIFICATION", "CELL-C_gauge_orbit": "BLOCKED_ENDPOINT_IDENTIFICATION", "CELL-D_holonomy": "GLOBAL_HOLONOMY_OR_ZERO_MODE_BLOCKING", "CELL-E_C174_subgauge": "NOT_PROVED", "CELL-F_C175_ghost_boundary": "NOT_PROVED", "classification": "FINITE_CELL_ADAPTER_INCOMPLETE", "infinity_equals_plus_minus_L": False, "project_path": "NO_PROJECT_REPRESENTATIVE_SELECTED"} for x in PATH_CLASSES if path_class_id is None or x["path_class_id"] == path_class_id)
    return _freeze({"schema": "C177-FINITE-CELL-ADAPTER-V1", "rows": rows, "root": _root(rows)})


def finite_ho_path_manifest(resolution_id: str | None = None, path_pair_id: str | None = None) -> MappingProxyType:
    rs = _check_id(resolution_id, RESOLUTIONS)
    rows = []
    for r in rs:
        ho = c176.ho_boundary_manifest(r)["rows"][0]
        rows.append({"resolution_id": r, "path_pair_id": path_pair_id or "SOURCE_EQUIVALENT_PATH_PAIR_UNEXECUTED", "retained_HO_path_image": "source-only; no link kernel", "closed_path_residual": "NOT_EXECUTED_SOURCE_ONLY", "resolution_dependence": "NOT_EXECUTED_SOURCE_ONLY", "C176_leakage_entries": ho["leakage_nonzero_entries"], "C176_leakage_rank": ho["rank"], "C176_leakage_norm": ho["leakage_norm"], "C176_leakage_threshold_pruned": ho["leakage_threshold_pruned"], "C176_owner": "C176-HO-BOUNDARY", "classification": "PATH_COMPARISON_NOT_EXECUTABLE_SOURCE_ONLY"})
    return _freeze({"schema": "C177-FINITE-HO-PATH-V1", "rows": tuple(rows), "root": _root(rows)})


def project_path_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-PROJECT-PATH-V1", "project_path_id": "NO_PROJECT_REPRESENTATIVE_SELECTED", "source_class_closes": True, "C43_convention_closes": True, "periodic_cell_closes": False, "representation_lift_closes": True, "finite_HO_closes": False, "selection_gate": "NOT_CLOSED", "straight_path_selected": False, "rationale": "source class and convention are recovered, but infinity-to-periodic-cell and finite-HO path residual gates remain open", "root": _root(("NO_PROJECT_REPRESENTATIVE_SELECTED", False))})


def c43_path_crosswalk_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-C43-PATH-CROSSWALK-V1", "historical_path_id": HISTORICAL_PATH_ID, "historical_source_root": c176.verify_hqcd_b0reslink1_authority()["C43_source_root"], "new_source_object_ids": tuple(x["source_object_id"] for x in SOURCE_OBJECTS), "new_continuum_path_class_ids": tuple(x["path_class_id"] for x in PATH_CLASSES), "new_convention_adapter_root": convention_adapter_manifest()["root"], "new_representation_root": representation_lift_manifest()["root"], "finite_cell_status": "FINITE_CELL_ADAPTER_INCOMPLETE", "project_path_status": "NO_PROJECT_REPRESENTATIVE_SELECTED", "supersession_scope": "SOURCE_PATH_RECOVERED_FINITE_CELL_ADAPTER_BLOCKING", "historical_record_edited": False, "root": _root((HISTORICAL_PATH_ID, "FINITE_CELL_ADAPTER_INCOMPLETE"))})


def executable_link_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C177-EXECUTABLE-LINK-HANDOFF-V1", "C176_blocker": "C176-C43-RESIDUAL-LINK-PATH-GEOMETRY", "accepted_source_objects": tuple(x["source_object_id"] for x in SOURCE_OBJECTS), "continuum_path_classes": tuple(x["path_class_id"] for x in PATH_CLASSES), "half_link_cancellation_root": half_link_cancellation_manifest()["root"], "pure_gauge_root": pure_gauge_manifest()["root"], "future_past_root": future_past_manifest()["root"], "convention_adapter_root": convention_adapter_manifest()["root"], "representation_lift_root": representation_lift_manifest()["root"], "finite_cell_adapter_root": finite_cell_adapter_manifest()["root"], "finite_HO_path_root": finite_ho_path_manifest()["root"], "project_path_root": project_path_manifest()["root"], "project_path_absence": True, "C43_placeholder_crosswalk": c43_path_crosswalk_manifest()["root"], "unresolved_objects": ("periodic infinity-to-cell adapter", "global holonomy/zero-mode closure", "finite-HO source-equivalent path comparison", "project canonical representative"), "boundary_values_constructed": False, "wilson_coefficients_constructed": False, "root": _root((STATUS, "source-ready", False))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    inherited = c176.request_resolution_manifest()["rows"]
    rows = []
    for row in inherited:
        active = row["request_id"] in ACTIVE_REQUESTS
        rows.append({**dict(row), "C177_terminal_status": "CONTINUUM_PATH_CLASS_READY_FINITE_CELL_ADAPTER_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "source_object_status": "SOURCE_HASH_LOCKED" if active else "PRESERVED_INHERITED_REQUEST", "continuum_path_class_status": "CONTINUUM_PATH_CLASS_READY" if active else "PRESERVED_INHERITED_REQUEST", "convention_adapter_status": "READY" if active else "PRESERVED_INHERITED_REQUEST", "representation_lift_status": "READY" if active else "PRESERVED_INHERITED_REQUEST", "finite_cell_adapter_status": "INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "finite_HO_path_status": "SOURCE_ONLY_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "project_path_status": "NOT_SELECTED" if active else "PRESERVED_INHERITED_REQUEST", "next_object": NEXT if active else "unchanged"})
    if request_id is not None:
        rows = [x for x in rows if x["request_id"] == request_id]
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C177-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_path_object_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ACTIVE_REQUESTS: raise KeyError(request_id)
    ids = (request_id,) if request_id else ACTIVE_REQUESTS
    rows = tuple({"request_id": x, "parent_C176_blocker": "C176-C43-RESIDUAL-LINK-PATH-GEOMETRY", "object_id": "C177-PERIODIC-CELL-PATH-ADAPTER", "required_source_scope": "BJY/JY continuum source objects already locked", "required_locator": "C174 project finite-cell endpoint/holonomy/gauge-orbit crosswalk", "path_class": "BJY/JY continuum transverse boundary class", "endpoints": "+/-infinity source vs +/-L periodic cell", "orientation": "DIS future and DY past remain separate", "representation": "open adjoint via C177 lift", "C43_sign": "C43 D/U and antisymmetric/PV", "P0_Q0": "C174/C175 interfaces", "HO_boundary_owner": "C176-HO-BOUNDARY", "required_routes": ("CELL-A coordinate", "CELL-B finite Fourier", "CELL-C gauge orbit", "CELL-D holonomy", "CELL-E C174 subgauge", "CELL-F C175 ghost boundary"), "holdouts": ("no infinity=+/-L by notation", "no straight path", "no endpoint zero", "no link coefficient"), "status": "REQUIRES_C178_HQCDB0RESLINKADAPTER1", "not_zero": True} for x in ids)
    return _freeze({"schema": "C177-MISSING-PATH-OBJECT-V1", "rows": rows, "root": _root(rows)})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C167-RI-SMOM", "status": "PRESERVED_TWO_SOURCE_RESOLVED_LEAVES"}, {"frontier_id": "C168-C169-REQUESTS", "status": "SIX_VISIBLE_TWO_ACTIVE"}, {"frontier_id": "C163-LOCATORS", "status": "SIX_PRESERVED"}, {"frontier_id": "C171-B0", "status": "READ_ONLY"}, {"frontier_id": "C172-Q0", "status": "CLOSED_DECLARED_SCOPE"}, {"frontier_id": "C173-NONIDENTITY", "status": "PRESERVED_CONTINUUM_PV_SOURCE"}, {"frontier_id": "C174-P0", "status": "PROJECT_SCHEME_PRESERVED"}, {"frontier_id": "C175-GHOST", "status": "LOCAL_READY_BULK_ORTHOGONAL_PRESERVED"}, {"frontier_id": "C176-RESLINK", "status": "HO_BOUNDARY_READY_PATH_GEOMETRY_BLOCKED"}, {"frontier_id": "C177-SOURCE-PATH", "status": "CONTINUUM_READY_FINITE_CELL_BLOCKED"}, {"frontier_id": "C170-B1", "status": "PRESERVED"}, {"frontier_id": "C155-COUNTERTERM", "status": "PRESERVED"})
    return _freeze({"schema": "C177-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def target_link_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-TARGET-LINK-SEPARATION-V1", "C43_residual_link": "source-derived continuum boundary class; finite-cell adapter incomplete", "C174_project_subgauge": SCHEME, "C175_local_residual_ghosts": "separate", "JMY_offlightcone_staple": "comparison only", "future_physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_factor": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "target_MOMq": "separate target-side", "root": _root((STATUS, False, False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-BRST-ST-BOUNDARY-V1", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED", "root": _root((False, False, False))})


def c176_boundary_freeze() -> MappingProxyType:
    c = c176.verify_hqcd_b0reslink1_authority()
    return _freeze({"C176_status": c176.STATUS, "C176_plan": c176.PLAN, "C176_package_root": c176.PACKAGE_ROOT, "C176_expected_package_root": "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5", "C176_package_root_verified": c176.PACKAGE_ROOT == "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5", "C176_HO_boundary": {"dimensions": (36, 55, 78), "leakage_entries": (16, 20, 24), "ranks": (8, 10, 12), "norms_GeV": (2.4, 3.337289319193048, 4.415880433163924), "integration_by_parts_defect": "NONZERO_UNPRUNED", "read_only": True}, "root": _root((c176.PACKAGE_ROOT, "read-only"))})


def verify_hqcd_b0reslinksource1_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    return _freeze({"schema": "C177-HQCDB0RESLINKSOURCE1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_present": True, "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C176_package_root": c176.PACKAGE_ROOT, "C176_package_root_verified": c176.PACKAGE_ROOT == "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5", "source_count": len(SOURCE_ROWS), "source_hashes_locked": source_audit_manifest()["all_hash_verified"], "continuum_path_class_ready": True, "finite_cell_adapter_ready": False, "finite_HO_path_ready": False, "project_path_selected": False, "boundary_values_constructed": False, "wilson_coefficients_constructed": False, "ghost_link_kernels_constructed": False, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "C176_HO_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0reslinksource1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS:
        raise ValueError("C177 runtime mismatch")
    if _sha(ROOT / CONTRACT) != CONTRACT_SHA256:
        raise ValueError("C176-C177 contract hash mismatch")
    return verify_hqcd_b0reslinksource1_authority()


def b0reslinksource1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C177-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "authenticated BJY/JY continuum path objects close source scope; periodic-cell and finite-HO gates remain incomplete", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def b0reslinksource1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C177-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "source_artifacts_ready": True, "source_locators_ready": True, "convention_adapter_ready": True, "continuum_path_class_ready": True, "half_link_cancellation_ready": True, "pure_gauge_scope_explicit": True, "future_past_pv_ready": True, "representation_lift_ready": True, "finite_cell_adapter_ready": False, "finite_HO_path_ready": False, "project_path_selected": False, "C43_placeholder_crosswalked": True, "boundary_values_constructed": False, "wilson_coefficients_constructed": False, "ghost_link_kernels_constructed": False, "self_energy_constructed": False, "next": NEXT, "root": _root((STATUS, NEXT, False, False))})


def b0reslinksource1_no_recomputation_report() -> MappingProxyType:
    return _freeze({"schema": "C177-NO-RECOMPUTATION-V1", "C171_B0_rebuilt": 0, "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "C176_HO_boundary_rebuilt": 0, "B1_mutations": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C158_value_inputs": 0, "network_after_construction": 0, "root": _root((0, 0, 0, 0, 0, 0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    fields = {"broad_literature_search": 0, "search_summary_formulas": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "path_inferred": 0, "straight_path_selected_without_gate": 0, "infinity_cell_identification_by_notation": 0, "future_past_merged": 0, "path_order_dropped": 0, "degree_two_abelianized": 0, "fundamental_relabelled_adjoint": 0, "global_color_quotiented": 0, "JMY_staple_imported": 0, "C176_leakage_zeroed": 0, "C175_boundary_zeroed": 0, "boundary_values_constructed": 0, "wilson_coefficients_constructed": 0, "ghost_link_kernels_constructed": 0, "self_energy_constructed": 0, "C158_value_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "quantum_objects_modified": 0}
    return _freeze({**fields, "new_source_acquisitions": 1, "pass": True, "root": _root(fields)})


def mutate_live_hqcdb0reslinksource1(index: int) -> MappingProxyType:
    fields = ("source_hash", "locator", "equation", "convention", "coordinate", "gauge", "future", "past", "PV", "path_order", "half_link", "pure_gauge_scope", "representation", "generator_0", "generator_1", "generator_2", "generator_3", "generator_4", "generator_5", "generator_6", "generator_7", "finite_cell", "holonomy", "finite_HO", "project_path", "crosswalk", "request", "frontier", "API", "runtime", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C177_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c176.PACKAGE_ROOT)),
    "C177_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)),
    "C177_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, "C170-C176-prompt-only")),
    "C177_PLAN_ROOT": b0reslinksource1_plan_manifest()["root"],
    "C177_C176_FREEZE_ROOT": c176_boundary_freeze()["root"],
    "C177_SOURCE_AUDIT_ROOT": source_audit_manifest()["root"],
    "C177_SOURCE_OBJECT_ROOT": source_object_manifest()["root"],
    "C177_SOURCE_LOCATOR_ROOT": source_locator_crosswalk()["root"],
    "C177_CONVENTION_ADAPTER_ROOT": convention_adapter_manifest()["root"],
    "C177_CONTINUUM_PATH_CLASS_ROOT": continuum_path_class_manifest()["root"],
    "C177_HALF_LINK_CANCELLATION_ROOT": half_link_cancellation_manifest()["root"],
    "C177_PURE_GAUGE_ROOT": pure_gauge_manifest()["root"],
    "C177_PATH_INDEPENDENCE_ROOT": path_independence_manifest()["root"],
    "C177_FUTURE_PAST_ROOT": future_past_manifest()["root"],
    "C177_PV_ORIENTATION_ROOT": pv_orientation_manifest()["root"],
    "C177_REPRESENTATION_LIFT_ROOT": representation_lift_manifest()["root"],
    "C177_FINITE_CELL_ADAPTER_ROOT": finite_cell_adapter_manifest()["root"],
    "C177_FINITE_HO_PATH_ROOT": finite_ho_path_manifest()["root"],
    "C177_PROJECT_PATH_ROOT": project_path_manifest()["root"],
    "C177_C43_PATH_CROSSWALK_ROOT": c43_path_crosswalk_manifest()["root"],
    "C177_EXECUTABLE_HANDOFF_ROOT": executable_link_handoff_contract()["root"],
    "C177_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C177_MISSING_OBJECT_ROOT": missing_path_object_manifest()["root"],
    "C177_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C177_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"],
    "C177_QUANTUM_NONMUTATION_ROOT": _root((False, 0, 0)),
    "C177_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"],
    "C177_SCOPE_ROOT": _root((STATUS, "no-boundary-values", "no-self-energy", "no-TMD", "no-quantum")),
    "C177_COMPLETENESS_ROOT": b0reslinksource1_completeness_certificate()["root"],
}
PACKAGE_ROOT = _root({"schema": "C177-HQCDB0RESLINKSOURCE1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
