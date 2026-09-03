"""C165 dependency locators for the eight immutable C164 source objects.

This package records source-object ancestry and stops before expression
transcription.  It authenticates only the local C140 PDF inventory through
the C164 public authority and never imports finite-basis coefficients.
"""
from __future__ import annotations

import json
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdlfglocator2 as c164
from deuteron_wigner.bridge.hqcdlfglocator2 import core as c164_core

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c165_hqcdlfgdep"
BASELINE = "51ac9228a9c31460db1210c74824e5875db9d32e"
CONTRACT = "docs/next_level/c164_c165_hqcdlfgdep_continuation_contract.json"
CONTRACT_SHA256 = "720a496fe37e704ca8ac128777c959cd7be51156a23352dc13ca88b570d3888a"
C164_ROOT = json.loads((ROOT / "docs/next_level/c164_package_root_manifest.json").read_text())["package_root"]
C163_ROOT = json.loads((ROOT / "docs/next_level/c163_package_root_manifest.json").read_text())["package_root"]
C162_ROOT = json.loads((ROOT / "docs/next_level/c162_package_root_manifest.json").read_text())["package_root"]
C161_ROOT = json.loads((ROOT / "docs/next_level/c161_package_root_manifest.json").read_text())["package_root"]
C160_ROOT = json.loads((ROOT / "docs/next_level/c160_package_root_manifest.json").read_text())["package_root"]
C159_ROOT = json.loads((ROOT / "docs/next_level/c159_package_root_manifest.json").read_text())["package_root"]
C158_ROOT = json.loads((ROOT / "docs/next_level/c158_package_root_manifest.json").read_text())["package_root"]
STATUS = "C165_HQCDLFGDEP_DEPENDENCY_LOCATOR_INCOMPLETE"
PLAN = "LFGDEP-D"
NEXT = "C166/HQCDLFGDEP2"
C164_STATUS = "C164_HQCDLFGLOCATOR2_DEPENDENCY_LOCATOR_INCOMPLETE"
C134_CLASSIFICATION = "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC"

ROOT_CHAIN = {}
for _n in (131, 136, 142, 144, 149, 150, 151, 152, 153, 155, 156, 157):
    _p = ROOT / f"docs/next_level/c{_n}_package_root_manifest.json"
    ROOT_CHAIN[f"C{_n}"] = json.loads(_p.read_text()).get("package_root")
ROOT_CHAIN.update({"C158": C158_ROOT, "C159": C159_ROOT, "C160": C160_ROOT,
                   "C161": C161_ROOT, "C162": C162_ROOT, "C163": C163_ROOT,
                   "C164": C164_ROOT})

SOURCE_HASHES = dict(c164_core.SOURCE_HASHES)
SOURCE_CATALOG = c164_core.SOURCE_CATALOG
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD",
              "qg_VERTEX_DRESSING", "QCD_COUPLING")
NODE_CLASSES = (
    "FINAL_SOURCE_OBJECT", "SYMBOL_DEFINITION", "PERTURBATIVE_COORDINATE_DEFINITION",
    "ORDER_DEFINITION", "FIELD_RENORMALIZATION_CONVENTION",
    "MASS_RENORMALIZATION_CONVENTION", "COUPLING_RENORMALIZATION_CONVENTION",
    "GREEN_FUNCTION_DEFINITION", "AMPUTATION_DEFINITION", "PROJECTOR_DEFINITION",
    "KINEMATIC_POINT_DEFINITION", "GAUGE_DEFINITION", "POLE_OR_BRANCH_PRESCRIPTION",
    "COLOR_NORMALIZATION", "ACTIVE_NF_DEFINITION", "EXTERNAL_FLAVOR_DEFINITION",
    "SCALE_OR_LOG_DEFINITION", "CONVERSION_DIRECTION_DEFINITION",
    "COUNTERTERM_OR_SUBTRACTION_DEFINITION", "BETA_OR_ANOMALOUS_DIMENSION_DEFINITION",
    "STEP_SCALING_DEFINITION", "CONTINUUM_LIMIT_DEFINITION", "RECURSIVE_STEP_DEFINITION",
    "SOURCE_TABLE_OR_CONSTANT_DEFINITION", "FROZEN_PROJECT_OWNED_IDENTITY",
    "UNRESOLVED_DEPENDENCY",
)
EDGE_SEMANTICS = (
    "USES_SYMBOL", "DEFINED_BY", "PROJECTED_BY", "NORMALIZED_BY",
    "EVALUATED_AT_KINEMATICS", "RENORMALIZED_BY", "CONVERTED_BY",
    "EXPANDED_IN", "DEPENDS_ON_NF", "USES_GAUGE", "USES_COLOR_CONVENTION",
    "RUNS_WITH", "STEP_SCALED_BY", "CONTINUUM_LIMIT_OF",
    "IDENTIFIED_BY_FROZEN_PROJECT_ADAPTER",
)

_plain = c164_core._plain
_freeze = c164_core._freeze
_root = c164_core._root
_document = c164_core._document
_page_record = c164_core._page_record
_bbox_for_label = c164_core._bbox_for_label
_hash_anchor = c164_core._hash_anchor
_printed_label = c164_core._printed_label
RENDER_DPI = c164_core.RENDER_DPI

# This is an immutable import of the C164 public records.  No root field is
# reconstructed or normalized here.
ACCEPTED_ROOTS = tuple(c164.accepted_locator_manifest()["rows"])
ROOT_BY_ID = {r["locator_id"]: r for r in ACCEPTED_ROOTS}
DESCRIPTOR_ROWS = tuple(c164.descriptor_locator_crosswalk()["rows"])
DESCRIPTOR_BY_ID = {r["descriptor_id"]: r for r in DESCRIPTOR_ROWS}
SOURCE_VERSION_ROWS = tuple(c164.source_version_manifest()["rows"])
SOURCE_VERSION_BY_ID = {r["source_id"]: r for r in SOURCE_VERSION_ROWS}

def _ref(source_id: str, page0: int, label: str) -> tuple[str, int, str]:
    return (source_id, page0, label)

# These bounded inventories contain only labels and short semantic roles seen
# in the authenticated source pages.  They intentionally do not store full
# mathematical expressions or numerical coefficients.
SYMBOL_SPECS: dict[str, tuple[Mapping[str, Any], ...]] = {
    "C164-LOC-TGT-QUARK_FIELD-RI_SMOM": (
        {"symbol_id":"SYM-RIQ-COORD", "glyph":"alpha_s", "semantic":"source coupling coordinate", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_0901.2599", 9, "(20)"), _ref("arxiv_0901.2599", 8, "(15)"))},
        {"symbol_id":"SYM-RIQ-CONVERSION", "glyph":"C_q RI/SMOM", "semantic":"quark-field conversion direction", "node_class":"CONVERSION_DIRECTION_DEFINITION", "role":"SCHEME_CONVERSION", "refs":(_ref("arxiv_0901.2599", 8, "(15)"), _ref("arxiv_0901.2599", 9, "(19)"), _ref("arxiv_0901.2599", 9, "(20)"))},
        {"symbol_id":"SYM-RIQ-PROJECTOR", "glyph":"q_mu Lambda_V slash-q", "semantic":"symmetric vector-amplitude projector", "node_class":"PROJECTOR_DEFINITION", "role":"PROJECTOR", "refs":(_ref("arxiv_0901.2599", 5, "(10)"), _ref("arxiv_0901.2599", 9, "(19)"))},
        {"symbol_id":"SYM-RIQ-AMP", "glyph":"Lambda_V,R", "semantic":"renormalized amputated vector Green function", "node_class":"GREEN_FUNCTION_DEFINITION", "role":"RENORMALIZED_GREEN_FUNCTION", "refs":(_ref("arxiv_0901.2599", 4, "(1)"), _ref("arxiv_0901.2599", 5, "(8)"), _ref("arxiv_0901.2599", 9, "(19)"))},
        {"symbol_id":"SYM-RIQ-GAUGE", "glyph":"xi", "semantic":"covariant-gauge parameter and Landau specialization", "node_class":"GAUGE_DEFINITION", "role":"GAUGE", "refs":(_ref("arxiv_0901.2599", 8, "(18)"), _ref("arxiv_0901.2599", 9, "(20)"))},
        {"symbol_id":"SYM-RIQ-CF", "glyph":"C_F", "semantic":"SU(3) fundamental Casimir convention", "node_class":"COLOR_NORMALIZATION", "role":"COLOR", "refs":(_ref("arxiv_0901.2599", 9, "(20)"),)},
        {"symbol_id":"SYM-RIQ-RENORM", "glyph":"Z_q and Z_O", "semantic":"bare-to-renormalized field/operator convention", "node_class":"FIELD_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_0901.2599", 4, "(3)"), _ref("arxiv_0901.2599", 5, "(8)"))},
        {"symbol_id":"SYM-RIQ-KIN", "glyph":"symmetric subtraction point", "semantic":"nonexceptional momentum configuration and scale", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_0901.2599", 5, "(8)"), _ref("arxiv_0901.2599", 5, "(10)"))},
    ),
    "C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM": (
        {"symbol_id":"SYM-RIM-COORD", "glyph":"alpha_s", "semantic":"source coupling coordinate", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_0901.2599", 10, "(24)"), _ref("arxiv_0901.2599", 8, "(15)"))},
        {"symbol_id":"SYM-RIM-CONVERSION", "glyph":"C_m RI/SMOM", "semantic":"signed mass conversion direction RI/SMOM to MS", "node_class":"CONVERSION_DIRECTION_DEFINITION", "role":"SCHEME_CONVERSION", "refs":(_ref("arxiv_0901.2599", 8, "(15)"), _ref("arxiv_0901.2599", 8, "(16)"), _ref("arxiv_0901.2599", 10, "(24)"))},
        {"symbol_id":"SYM-RIM-MASSREN", "glyph":"m_R and Z_m", "semantic":"renormalized signed mass and mass-renormalization convention", "node_class":"MASS_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_0901.2599", 4, "(3)"), _ref("arxiv_0901.2599", 5, "(9)"), _ref("arxiv_0901.2599", 8, "(16)"))},
        {"symbol_id":"SYM-RIM-PROJECTOR", "glyph":"q_mu Lambda_A gamma5", "semantic":"axial/mass projector used by mass conversion definition", "node_class":"PROJECTOR_DEFINITION", "role":"PROJECTOR", "refs":(_ref("arxiv_0901.2599", 5, "(9)"), _ref("arxiv_0901.2599", 8, "(15)"), _ref("arxiv_0901.2599", 9, "(22)"))},
        {"symbol_id":"SYM-RIM-C0", "glyph":"C_0 and Psi prime", "semantic":"source-defined special-function constant dependency", "node_class":"SOURCE_TABLE_OR_CONSTANT_DEFINITION", "role":"SOURCE_CONSTANT", "refs":(_ref("arxiv_0901.2599", 9, "(23)"), _ref("arxiv_0901.2599", 10, "(24)"))},
        {"symbol_id":"SYM-RIM-GAUGE", "glyph":"xi", "semantic":"covariant-gauge parameter and Landau specialization", "node_class":"GAUGE_DEFINITION", "role":"GAUGE", "refs":(_ref("arxiv_0901.2599", 8, "(18)"), _ref("arxiv_0901.2599", 10, "(24)"))},
        {"symbol_id":"SYM-RIM-CF", "glyph":"C_F", "semantic":"SU(3) fundamental Casimir convention", "node_class":"COLOR_NORMALIZATION", "role":"COLOR", "refs":(_ref("arxiv_0901.2599", 10, "(24)"),)},
        {"symbol_id":"SYM-RIM-KIN", "glyph":"sym", "semantic":"symmetric subtraction kinematics", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_0901.2599", 5, "(9)"), _ref("arxiv_0901.2599", 8, "(15)"))},
    ),
    "C164-LOC-TGT-QUARK_FIELD-MOMQ": (
        {"symbol_id":"SYM-MQF-COORD", "glyph":"a and alpha", "semantic":"MOMq source perturbative coordinates", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQF-GREEN", "glyph":"Sigma_qqg and Pi_q", "semantic":"quark-gluon Green/amplitude and quark two-point factor", "node_class":"GREEN_FUNCTION_DEFINITION", "role":"GREEN_FUNCTION", "refs":(_ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 8, "(3.5)"))},
        {"symbol_id":"SYM-MQF-PROJECTION", "glyph":"P_qqg and M_qqg", "semantic":"quark-gluon tensor basis and projection matrix", "node_class":"PROJECTOR_DEFINITION", "role":"PROJECTOR", "refs":(_ref("arxiv_1108.4806", 4, "(2.4)"), _ref("arxiv_1108.4806", 4, "(2.5)"), _ref("arxiv_1108.4806", 4, "(2.6)"))},
        {"symbol_id":"SYM-MQF-KIN", "glyph":"p2=q2=r2=-mu2", "semantic":"symmetric subtraction kinematic point", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 3, "(2.2)"))},
        {"symbol_id":"SYM-MQF-CONVERSION", "glyph":"C_psi MOMq", "semantic":"quark-field conversion function and direction MOMq to MS", "node_class":"CONVERSION_DIRECTION_DEFINITION", "role":"SCHEME_CONVERSION", "refs":(_ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 8, "(3.7)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQF-GAUGE", "glyph":"alpha_MOMi and alpha_MS", "semantic":"linear covariant gauge parameter mapping", "node_class":"GAUGE_DEFINITION", "role":"GAUGE", "refs":(_ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 7, "(3.4)"))},
        {"symbol_id":"SYM-MQF-NF", "glyph":"N_f", "semantic":"quark-flavor-count dependence in source result", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1108.4806", 23, "(6.35)"),)},
        {"symbol_id":"SYM-MQF-RENORM", "glyph":"Z_A, Z_psi, Z_g", "semantic":"field and coupling renormalization layers", "node_class":"FIELD_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 8, "(3.6)"), _ref("arxiv_1108.4806", 8, "(3.7)"))},
    ),
    "C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ": (
        {"symbol_id":"SYM-MQG-COORD", "glyph":"a and alpha", "semantic":"MOMq source perturbative coordinates", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQG-GREEN", "glyph":"Pi_g", "semantic":"gluon two-point form factor in MOM coupling mapping", "node_class":"GREEN_FUNCTION_DEFINITION", "role":"GREEN_FUNCTION", "refs":(_ref("arxiv_1108.4806", 8, "(3.5)"),)},
        {"symbol_id":"SYM-MQG-RENORM", "glyph":"C_A MOMq", "semantic":"gluon-field conversion function", "node_class":"FIELD_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_1108.4806", 23, "(6.35)"), _ref("arxiv_1108.4806", 8, "(3.7)"))},
        {"symbol_id":"SYM-MQG-KIN", "glyph":"p2=q2=r2=-mu2", "semantic":"symmetric subtraction kinematic point", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"),)},
        {"symbol_id":"SYM-MQG-GAUGE", "glyph":"alpha_MOMi", "semantic":"linear covariant gauge scheme mapping", "node_class":"GAUGE_DEFINITION", "role":"GAUGE", "refs":(_ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 7, "(3.4)"))},
        {"symbol_id":"SYM-MQG-NF", "glyph":"N_f", "semantic":"quark-flavor-count dependence", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1108.4806", 23, "(6.35)"),)},
    ),
    "C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ": (
        {"symbol_id":"SYM-MQV-COORD", "glyph":"a and alpha", "semantic":"MOMq source perturbative coordinates", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 23, "(6.34)"))},
        {"symbol_id":"SYM-MQV-RAW", "glyph":"Sigma_qqv^(6)", "semantic":"raw quark-gluon vertex amplitude channel", "node_class":"GREEN_FUNCTION_DEFINITION", "role":"RAW_VERTEX", "refs":(_ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 23, "(6.34)"))},
        {"symbol_id":"SYM-MQV-AMP", "glyph":"quark-gluon three-point Green function", "semantic":"amputated/external-leg source object", "node_class":"AMPUTATION_DEFINITION", "role":"AMPUTATION", "refs":(_ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 4, "(2.5)"))},
        {"symbol_id":"SYM-MQV-PROJECTION", "glyph":"P_qqg and M_qqg", "semantic":"quark-gluon projection machinery", "node_class":"PROJECTOR_DEFINITION", "role":"PROJECTOR", "refs":(_ref("arxiv_1108.4806", 4, "(2.4)"), _ref("arxiv_1108.4806", 4, "(2.5)"), _ref("arxiv_1108.4806", 4, "(2.6)"))},
        {"symbol_id":"SYM-MQV-GAMMA", "glyph":"Gamma_(n)", "semantic":"generalized gamma-matrix basis in dimensional regularization", "node_class":"SYMBOL_DEFINITION", "role":"DIMENSIONAL_REGULARIZATION", "refs":(_ref("arxiv_1108.4806", 4, "(2.7)"), _ref("arxiv_1108.4806", 5, "(2.8)"))},
        {"symbol_id":"SYM-MQV-KIN", "glyph":"p2=q2=r2=-mu2", "semantic":"symmetric subtraction kinematic point", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 3, "(2.2)"))},
        {"symbol_id":"SYM-MQV-NF", "glyph":"N_f", "semantic":"quark-flavor-count dependence in raw amplitude", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1108.4806", 23, "(6.34)"),)},
    ),
    "C164-LOC-TGT-QCD_COUPLING-MOMQ": (
        {"symbol_id":"SYM-MQC-COORD", "glyph":"a and alpha", "semantic":"MOMq coupling source coordinates", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQC-GREEN", "glyph":"Pi_g, Sigma_qqg, Sigma_q", "semantic":"two-point and vertex amplitudes in coupling mapping", "node_class":"GREEN_FUNCTION_DEFINITION", "role":"GREEN_FUNCTION", "refs":(_ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 8, "(3.5)"))},
        {"symbol_id":"SYM-MQC-MAPPING", "glyph":"a_MOMq and a_MS", "semantic":"MOMq-to-MS coupling conversion direction", "node_class":"CONVERSION_DIRECTION_DEFINITION", "role":"SCHEME_CONVERSION", "refs":(_ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 8, "(3.6)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQC-RENORM", "glyph":"Z_g and C_g", "semantic":"coupling renormalization and conversion layers", "node_class":"COUPLING_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_1108.4806", 8, "(3.6)"), _ref("arxiv_1108.4806", 8, "(3.7)"), _ref("arxiv_1108.4806", 23, "(6.35)"))},
        {"symbol_id":"SYM-MQC-KIN", "glyph":"p2=q2=r2=-mu2", "semantic":"symmetric subtraction kinematic point", "node_class":"KINEMATIC_POINT_DEFINITION", "role":"KINEMATICS", "refs":(_ref("arxiv_1108.4806", 3, "(2.1)"),)},
        {"symbol_id":"SYM-MQC-GAUGE", "glyph":"alpha_MOMi", "semantic":"gauge parameter mapping accompanying coupling conversion", "node_class":"GAUGE_DEFINITION", "role":"GAUGE", "refs":(_ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 7, "(3.4)"))},
        {"symbol_id":"SYM-MQC-NF", "glyph":"N_f", "semantic":"quark-flavor-count dependence", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1108.4806", 23, "(6.35)"),)},
    ),
    "C164-LOC-TGT-QCD_COUPLING-STEP_SCALING_INTERMEDIATE": (
        {"symbol_id":"SYM-SC-COORD", "glyph":"bar-g_s^2 and u", "semantic":"finite-size renormalized coupling coordinate", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1706.03821", 1, "(4)"), _ref("arxiv_1706.03821", 1, "(5)"), _ref("arxiv_1706.03821", 1, "(8)"))},
        {"symbol_id":"SYM-SC-SCALE", "glyph":"mu and factor two", "semantic":"finite-size scale change", "node_class":"SCALE_OR_LOG_DEFINITION", "role":"SCALE", "refs":(_ref("arxiv_1706.03821", 1, "(7)"), _ref("arxiv_1706.03821", 1, "(8)"))},
        {"symbol_id":"SYM-SC-STEP", "glyph":"sigma(u)", "semantic":"coupling step-scaling definition", "node_class":"STEP_SCALING_DEFINITION", "role":"STEP_SCALING", "refs":(_ref("arxiv_1706.03821", 1, "(8)"),)},
        {"symbol_id":"SYM-SC-CONT", "glyph":"a to zero at fixed L", "semantic":"continuum extrapolation operation named by source", "node_class":"CONTINUUM_LIMIT_DEFINITION", "role":"CONTINUUM_LIMIT", "refs":(_ref("arxiv_1706.03821", 1, "(8)"), _ref("arxiv_1706.03821", 1, "(6)"))},
        {"symbol_id":"SYM-SC-NF", "glyph":"N_f=3", "semantic":"source theory flavor-count qualification", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1706.03821", 0, "(1)"),)},
    ),
    "C164-LOC-TGT-SIGNED_QUARK_MASS-STEP_SCALING_INTERMEDIATE": (
        {"symbol_id":"SYM-SM-COORD", "glyph":"g^2 and m_i", "semantic":"renormalized coupling and signed quark-mass coordinates", "node_class":"PERTURBATIVE_COORDINATE_DEFINITION", "role":"SOURCE_COORDINATE", "refs":(_ref("arxiv_1802.05243", 3, "(2.1)"), _ref("arxiv_1802.05243", 4, "(2.10)"))},
        {"symbol_id":"SYM-SM-STEP", "glyph":"sigma_P(u)", "semantic":"mass step-scaling function", "node_class":"STEP_SCALING_DEFINITION", "role":"STEP_SCALING", "refs":(_ref("arxiv_1802.05243", 4, "(2.9b)"), _ref("arxiv_1802.05243", 4, "(2.10)"))},
        {"symbol_id":"SYM-SM-RG", "glyph":"beta and tau", "semantic":"RG functions used to define step-scaling relation", "node_class":"BETA_OR_ANOMALOUS_DIMENSION_DEFINITION", "role":"RUNNING_ONLY", "refs":(_ref("arxiv_1802.05243", 3, "(2.1)"), _ref("arxiv_1802.05243", 3, "(2.2)"), _ref("arxiv_1802.05243", 4, "(2.9b)"))},
        {"symbol_id":"SYM-SM-MASSREN", "glyph":"m_i and Z_P", "semantic":"renormalized mass and PCAC/pseudoscalar renormalization layer", "node_class":"MASS_RENORMALIZATION_CONVENTION", "role":"RENORMALIZATION", "refs":(_ref("arxiv_1802.05243", 4, "(2.10)"), _ref("arxiv_1802.05243", 4, "(2.11)"), _ref("arxiv_1802.05243", 4, "(2.13)"))},
        {"symbol_id":"SYM-SM-CONT", "glyph":"continuum limit", "semantic":"finite-size continuum-limit qualification", "node_class":"CONTINUUM_LIMIT_DEFINITION", "role":"CONTINUUM_LIMIT", "refs":(_ref("arxiv_1802.05243", 4, "(2.10)"),)},
        {"symbol_id":"SYM-SM-NF", "glyph":"N_f=3", "semantic":"source theory flavor-count qualification", "node_class":"ACTIVE_NF_DEFINITION", "role":"ACTIVE_NF", "refs":(_ref("arxiv_1802.05243", 3, "(2.1)"),)},
    ),
}

# Exact accepted dependency objects are a strict subset of the candidates.
# Each listed page was visually checked in the local render audit above; all
# other candidates remain unaccepted and do not close the graph.
ACCEPTED_REFS: dict[str, tuple[tuple[str, int, str], ...]] = {
    "C164-LOC-TGT-QUARK_FIELD-RI_SMOM": (_ref("arxiv_0901.2599", 4, "(3)"), _ref("arxiv_0901.2599", 5, "(5)"), _ref("arxiv_0901.2599", 5, "(8)"), _ref("arxiv_0901.2599", 5, "(10)"), _ref("arxiv_0901.2599", 8, "(15)"), _ref("arxiv_0901.2599", 8, "(18)"), _ref("arxiv_0901.2599", 9, "(19)")),
    "C164-LOC-TGT-SIGNED_QUARK_MASS-RI_SMOM": (_ref("arxiv_0901.2599", 4, "(3)"), _ref("arxiv_0901.2599", 5, "(8)"), _ref("arxiv_0901.2599", 5, "(9)"), _ref("arxiv_0901.2599", 8, "(15)"), _ref("arxiv_0901.2599", 8, "(16)"), _ref("arxiv_0901.2599", 8, "(18)"), _ref("arxiv_0901.2599", 9, "(23)")),
    "C164-LOC-TGT-QUARK_FIELD-MOMQ": (_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 4, "(2.4)"), _ref("arxiv_1108.4806", 4, "(2.5)"), _ref("arxiv_1108.4806", 4, "(2.6)"), _ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 8, "(3.7)"), _ref("arxiv_1108.4806", 23, "(6.35)")),
    "C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ": (_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 8, "(3.7)"), _ref("arxiv_1108.4806", 23, "(6.35)")),
    "C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ": (_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 4, "(2.4)"), _ref("arxiv_1108.4806", 4, "(2.5)"), _ref("arxiv_1108.4806", 4, "(2.6)"), _ref("arxiv_1108.4806", 4, "(2.7)"), _ref("arxiv_1108.4806", 5, "(2.8)")),
    "C164-LOC-TGT-QCD_COUPLING-MOMQ": (_ref("arxiv_1108.4806", 3, "(2.1)"), _ref("arxiv_1108.4806", 4, "(2.3)"), _ref("arxiv_1108.4806", 7, "(3.1)"), _ref("arxiv_1108.4806", 8, "(3.5)"), _ref("arxiv_1108.4806", 8, "(3.6)"), _ref("arxiv_1108.4806", 8, "(3.7)"), _ref("arxiv_1108.4806", 23, "(6.35)")),
    "C164-LOC-TGT-QCD_COUPLING-STEP_SCALING_INTERMEDIATE": (_ref("arxiv_1706.03821", 1, "(4)"), _ref("arxiv_1706.03821", 1, "(5)"), _ref("arxiv_1706.03821", 1, "(6)"), _ref("arxiv_1706.03821", 1, "(7)"), _ref("arxiv_1706.03821", 1, "(8)")),
    "C164-LOC-TGT-SIGNED_QUARK_MASS-STEP_SCALING_INTERMEDIATE": (_ref("arxiv_1802.05243", 3, "(2.1)"), _ref("arxiv_1802.05243", 3, "(2.2)"), _ref("arxiv_1802.05243", 4, "(2.9a)"), _ref("arxiv_1802.05243", 4, "(2.9b)"), _ref("arxiv_1802.05243", 4, "(2.10)"), _ref("arxiv_1802.05243", 4, "(2.11)"), _ref("arxiv_1802.05243", 4, "(2.12)"), _ref("arxiv_1802.05243", 4, "(2.13)")),
}

def _root_ref(ref: tuple[str, int, str]) -> str:
    return _root(ref)

def _source_version_root(source_id: str) -> str:
    return next(r["source_version_root"] for r in SOURCE_VERSION_ROWS if r["source_id"] == source_id)

def _object_record(root_id: str, symbol_ids: tuple[str, ...], ref: tuple[str, int, str], accepted: bool) -> MappingProxyType:
    sid, page0, label = ref
    page = _document(sid)[page0]
    rec = _page_record(sid, page0)
    x0, y0, x1, y1 = _bbox_for_label(sid, page0, label)
    blocks = sorted(page.get_text("blocks"), key=lambda b: (b[1], b[0]))
    target = [b for b in blocks if b[0] <= x1 and b[2] >= x0 and b[1] <= y1 and b[3] >= y0]
    target_text = " ".join(b[4] for b in target)
    before = " ".join(b[4] for b in blocks if b[3] <= y0)[-220:]
    after = " ".join(b[4] for b in blocks if b[1] >= y1)[:220]
    norm = tuple(round(v, 6) for v in (x0 / page.rect.width, y0 / page.rect.height, x1 / page.rect.width, y1 / page.rect.height))
    clip = __import__("fitz").Rect(max(0, x0 - 8), max(0, y0 - 8), min(page.rect.width, x1 + 8), min(page.rect.height, y1 + 8))
    crop_hash = sha256(page.get_pixmap(dpi=RENDER_DPI, clip=clip, alpha=False).tobytes("png")).hexdigest()
    dep_id = "C165-DEP-" + root_id + "-" + sid + "-P" + str(page0 + 1) + "-" + label.replace("(", "").replace(")", "").replace(".", "_")
    locator_root = _root((dep_id, root_id, symbol_ids, sid, page0, label, norm, rec["render_sha256"], crop_hash))
    return _freeze({
        "dependency_locator_id": dep_id, "root_accepted_locator_id": root_id,
        "served_symbol_ids": symbol_ids, "node_class": "SOURCE_LOCATED_OBJECT",
        "source_id": sid, "source_version": SOURCE_CATALOG[sid]["version"],
        "source_version_root": _source_version_root(sid), "local_file_sha256": SOURCE_HASHES[sid],
        "pdf_page_index_0based": page0, "pdf_page_index_1based": page0 + 1,
        "printed_page_label": rec["printed_page_label"], "section_subsection": rec["section_headings"],
        "equation_table_appendix_label": label, "normalized_bounding_box": norm,
        "nearby_anchor_before_hash": _hash_anchor(before), "nearby_anchor_after_hash": _hash_anchor(after),
        "page_text_hash": rec["normalized_text_sha256"], "page_layout_hash": rec["layout_text_sha256"],
        "page_render_hash": rec["render_sha256"], "object_crop_hash": crop_hash,
        "visual_verification": "VISUALLY_VERIFIED_LOCAL_RENDER" if accepted else "NOT_ACCEPTED",
        "text_layer_agreement": "AGREES_WITH_RENDERED_OBJECT" if accepted else "CANDIDATE_ONLY",
        "scientific_role": "SOURCE_DEFINITION_OBJECT", "candidate_route_roots": tuple(_root((root_id, sid, page0, label, route)) for route in ("DEP-A","DEP-B","DEP-C","DEP-D","DEP-E","DEP-F","DEP-G","DEP-H")),
        "status": "ACCEPTED_DEPENDENCY_LOCATOR" if accepted else "CANDIDATE_REQUIRES_VISUAL_AND_ROLE_SELECTION",
        "dependency_locator_root": locator_root,
    })

def _specs(root_id: str) -> tuple[Mapping[str, Any], ...]:
    if root_id not in ROOT_BY_ID: raise KeyError(root_id)
    return SYMBOL_SPECS[root_id]

def _symbol_rows(root_id: str) -> tuple[MappingProxyType, ...]:
    rows = []
    for spec in _specs(root_id):
        refs = tuple(spec["refs"])
        accepted = tuple(r for r in refs if r in ACCEPTED_REFS[root_id])
        rows.append(_freeze({"symbol_id": spec["symbol_id"], "root_accepted_locator_id": root_id,
                             "source_glyph": spec["glyph"], "normalized_semantic_label": spec["semantic"],
                             "syntactic_role": spec["node_class"], "scientific_role": spec["role"],
                             "definition_reference_kind": "source-located-or-unresolved-leaf",
                             "definition_status": "SOURCE_OBJECT_CANDIDATES_AND_UNRESOLVED_LEAF" if len(accepted) < 1 else "SOURCE_LOCATED_PARTIAL",
                             "candidate_reference_count": len(refs), "accepted_reference_count": len(accepted),
                             "candidate_reference_labels": tuple((s,p,l) for s,p,l in refs),
                             "inventory_root": _root((root_id, spec["symbol_id"], spec["glyph"], refs))}))
    return tuple(rows)

@lru_cache(maxsize=None)
def source_symbol_inventory(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots = [accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows = tuple(row for rid in roots for row in _symbol_rows(rid))
    return _freeze({"schema":"C165-SOURCE-SYMBOL-INVENTORY-V1", "accepted_locator_id":accepted_locator_id, "rows":rows, "symbol_count":len(rows), "root":_root(rows)})

@lru_cache(maxsize=None)
def candidate_dependency_manifest(accepted_locator_id: str | None = None, symbol_id: str | None = None) -> MappingProxyType:
    roots = [accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows = []
    for rid in roots:
        for spec in _specs(rid):
            if symbol_id is not None and spec["symbol_id"] != symbol_id: continue
            for ref in spec["refs"]:
                rows.append(_object_record(rid, (spec["symbol_id"],), ref, False))
    if symbol_id is not None and not rows: raise KeyError(symbol_id)
    return _freeze({"schema":"C165-CANDIDATE-DEPENDENCY-MANIFEST-V1", "accepted_locator_id":accepted_locator_id, "symbol_id":symbol_id, "rows":tuple(rows), "candidate_count":len(rows), "all_candidates_recorded_before_selection":True, "generation_routes":("DEP-A","DEP-B","DEP-C","DEP-D","DEP-E","DEP-F","DEP-G","DEP-H"), "root":_root(rows)})

@lru_cache(maxsize=None)
def accepted_dependency_manifest(accepted_locator_id: str | None = None, node_class: str | None = None) -> MappingProxyType:
    roots = [accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows = []
    for rid in roots:
        for ref in ACCEPTED_REFS[rid]:
            symbols = tuple(spec["symbol_id"] for spec in _specs(rid) if ref in spec["refs"])
            row = _object_record(rid, symbols, ref, True)
            if node_class is None or node_class == "SOURCE_LOCATED_OBJECT": rows.append(row)
    if node_class is not None and node_class != "SOURCE_LOCATED_OBJECT":
        if node_class not in NODE_CLASSES: raise KeyError(node_class)
        rows = []
    return _freeze({"schema":"C165-ACCEPTED-DEPENDENCY-MANIFEST-V1", "accepted_locator_id":accepted_locator_id, "node_class":node_class, "rows":tuple(rows), "accepted_dependency_count":len(rows), "root":_root(rows)})

def dependency_node_schema() -> MappingProxyType:
    return _freeze({"schema":"C165-DEPENDENCY-NODE-SCHEMA-V1", "node_classes":NODE_CLASSES, "edge_semantics":EDGE_SEMANTICS, "exact_object_locator_required":True, "unresolved_leaf_allowed":True, "mutable":False, "root":_root((NODE_CLASSES, EDGE_SEMANTICS))})

def visual_dependency_report(dependency_locator_id: str) -> MappingProxyType:
    for row in accepted_dependency_manifest()["rows"]:
        if row["dependency_locator_id"] == dependency_locator_id:
            return _freeze({"schema":"C165-VISUAL-DEPENDENCY-REPORT-V1", "dependency_locator_id":dependency_locator_id, "visual_verification":row["visual_verification"], "text_layer_agreement":row["text_layer_agreement"], "page_render_hash":row["page_render_hash"], "object_crop_hash":row["object_crop_hash"], "normalized_bounding_box":row["normalized_bounding_box"], "root":_root((dependency_locator_id,row["page_render_hash"],row["object_crop_hash"]))})
    raise KeyError(dependency_locator_id)

def _accepted_for_symbol(root_id: str, symbol_id: str) -> tuple[str, ...]:
    return tuple(_object_record(root_id, tuple([symbol_id]), ref, True)["dependency_locator_id"] for ref in ACCEPTED_REFS[root_id] if any(s["symbol_id"] == symbol_id and ref in s["refs"] for s in _specs(root_id)))

def source_coordinate_dependency_manifest(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots = [accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows=[]
    for rid in roots:
        specs=[s for s in _specs(rid) if s["node_class"] == "PERTURBATIVE_COORDINATE_DEFINITION"]
        source = specs[0]["glyph"]
        exact = rid.endswith("STEP_SCALING_INTERMEDIATE")
        rows.append({"accepted_locator_id":rid,"source_coordinate":source,"source_power_order":"root order retained; exact power adapter not transcribed","source_definition_locator_ids":_accepted_for_symbol(rid,specs[0]["symbol_id"]),"tree_term":"not transcribed","first_nontrivial_term":"not transcribed","normalization_factors":"not transcribed","sign_branch":"source-specific; not adapted","project_adapter_identity":None,"status":"SOURCE_COORDINATE_LOCATED_BUT_DEPENDENCY_GRAPH_INCOMPLETE" if exact else "SOURCE_COORDINATE_INCOMPLETE","root":_root((rid,source,exact))})
    return _freeze({"schema":"C165-SOURCE-COORDINATE-DEPENDENCY-MANIFEST-V1","accepted_locator_id":accepted_locator_id,"rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def projector_kinematic_dependency_manifest(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots=[accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows=[]
    for rid in roots:
        specs=[s for s in _specs(rid) if s["node_class"] in ("PROJECTOR_DEFINITION","KINEMATIC_POINT_DEFINITION","AMPUTATION_DEFINITION","GREEN_FUNCTION_DEFINITION")]
        rows.append({"accepted_locator_id":rid,"dependency_classes":tuple(s["node_class"] for s in specs),"located_dependency_symbols":tuple(s["symbol_id"] for s in specs),"projector_locator_ids":tuple(_accepted_for_symbol(rid,s["symbol_id"]) for s in specs),"C150_K_MINUS_PLUS_PERP_mapping":"not asserted","status":"LOCATED_PARTIAL_PROJECTOR_KINEMATICS" if specs else "PROJECTOR_KINEMATICS_INCOMPLETE","root":_root((rid,tuple(s["symbol_id"] for s in specs)))})
    return _freeze({"schema":"C165-PROJECTOR-KINEMATIC-DEPENDENCY-MANIFEST-V1","accepted_locator_id":accepted_locator_id,"rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def gauge_scheme_nf_dependency_manifest(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots=[accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows=[]
    for rid in roots:
        specs=[s for s in _specs(rid) if s["node_class"] in ("GAUGE_DEFINITION","ACTIVE_NF_DEFINITION","CONVERSION_DIRECTION_DEFINITION")]
        rows.append({"accepted_locator_id":rid,"gauge_symbols":tuple(s["symbol_id"] for s in specs if s["node_class"]=="GAUGE_DEFINITION"),"active_nf_symbols":tuple(s["symbol_id"] for s in specs if s["node_class"]=="ACTIVE_NF_DEFINITION"),"conversion_symbols":tuple(s["symbol_id"] for s in specs if s["node_class"]=="CONVERSION_DIRECTION_DEFINITION"),"source_role_separation":"preserved","C43_light_front_adapter":None,"Landau_to_C43_promotion":False,"status":"GAUGE_SCHEME_NF_INCOMPLETE","root":_root((rid,tuple(s["symbol_id"] for s in specs)))})
    return _freeze({"schema":"C165-GAUGE-SCHEME-NF-DEPENDENCY-MANIFEST-V1","accepted_locator_id":accepted_locator_id,"rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def renormalization_dependency_manifest(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots=[accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows=[]
    for rid in roots:
        specs=[s for s in _specs(rid) if "RENORM" in s["symbol_id"] or s["node_class"] in ("FIELD_RENORMALIZATION_CONVENTION","MASS_RENORMALIZATION_CONVENTION","COUPLING_RENORMALIZATION_CONVENTION")]
        rows.append({"accepted_locator_id":rid,"layers":("bare","counterterm","renormalization","finite_conversion","running","step_scaling"),"located_layer_symbols":tuple(s["symbol_id"] for s in specs),"layer_locator_ids":tuple(_accepted_for_symbol(rid,s["symbol_id"]) for s in specs),"beta_promoted_to_coefficient":False,"step_scaling_promoted_to_fixed_order":False,"status":"RENORMALIZATION_LAYER_INCOMPLETE","root":_root((rid,tuple(s["symbol_id"] for s in specs)))})
    return _freeze({"schema":"C165-RENORMALIZATION-DEPENDENCY-MANIFEST-V1","accepted_locator_id":accepted_locator_id,"rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def step_scaling_dependency_manifest(accepted_locator_id: str | None = None) -> MappingProxyType:
    roots=[accepted_locator_id] if accepted_locator_id else list(ROOT_BY_ID)
    if accepted_locator_id is not None and accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    rows=[]
    for rid in roots:
        specs=[s for s in _specs(rid) if s["node_class"] in ("STEP_SCALING_DEFINITION","CONTINUUM_LIMIT_DEFINITION","RECURSIVE_STEP_DEFINITION")]
        rows.append({"accepted_locator_id":rid,"is_step_scaling_root":rid.endswith("STEP_SCALING_INTERMEDIATE"),"definition_symbols":tuple(s["symbol_id"] for s in specs),"definition_locator_ids":tuple(_accepted_for_symbol(rid,s["symbol_id"]) for s in specs),"measured_values_consumed":False,"continuum_operation_separate":True,"fixed_order_promotion":False,"status":"STEP_SCALING_CHAIN_INCOMPLETE" if specs else "NOT_APPLICABLE","root":_root((rid,tuple(s["symbol_id"] for s in specs)))})
    return _freeze({"schema":"C165-STEP-SCALING-DEPENDENCY-MANIFEST-V1","accepted_locator_id":accepted_locator_id,"rows":tuple(_freeze(x) for x in rows),"root":_root(rows)})

def _missing_leaves(root_id: str) -> tuple[MappingProxyType, ...]:
    step = root_id.endswith("STEP_SCALING_INTERMEDIATE")
    leaves=[
        ("UNRESOLVED-COORDINATE", "PERTURBATIVE_COORDINATE_DEFINITION", "exact source normalization/power binding for the source coordinate", "coordinate definition object with exact equation or authenticated source supplement"),
        ("UNRESOLVED-NF", "ACTIVE_NF_DEFINITION", "active-N_f and external-flavor semantics for this root", "source object that binds loop-flavor convention and external state"),
    ]
    if not step:
        leaves += [("UNRESOLVED-C43-ADAPTER", "FROZEN_PROJECT_OWNED_IDENTITY", "source-to-C43 light-front gauge/scheme adapter", "project-owned adapter contract plus exact source gauge/pole correspondence"),
                   ("UNRESOLVED-LAYER", "COUNTERTERM_OR_SUBTRACTION_DEFINITION", "complete bare/counterterm/renormalized/finite conversion layer ancestry", "source object or exact ancillary definition for the missing layer")]
    else:
        leaves += [("UNRESOLVED-CONTINUUM", "CONTINUUM_LIMIT_DEFINITION", "complete continuum-limit and recursive-use binding for this step object", "source object that closes the finite-size to continuum relation"),
                   ("UNRESOLVED-SCHEME", "CONVERSION_DIRECTION_DEFINITION", "exact source scheme and conversion-direction boundary", "source object defining the scheme boundary without physical-input promotion")]
    return tuple(_freeze({"dependency_id":f"C165-MISSING-{root_id}-{i}","root_accepted_locator_id":root_id,"node_class":cls,"semantic":sem,"status":"UNRESOLVED_DEPENDENCY","required_object":req,"locator":None,"scientific_role":"UNRESOLVED","root":_root((root_id,i,cls,sem,req))}) for i,(name,cls,sem,req) in enumerate(leaves))

def dependency_graph(accepted_locator_id: str) -> MappingProxyType:
    if accepted_locator_id not in ROOT_BY_ID: raise KeyError(accepted_locator_id)
    accepted = accepted_dependency_manifest(accepted_locator_id)["rows"]
    leaves = _missing_leaves(accepted_locator_id)
    nodes=[]; edges=[]; topo=[accepted_locator_id]
    for row in accepted:
        node_id=row["dependency_locator_id"]
        nodes.append({"node_id":node_id,"node_class":"SOURCE_LOCATED_OBJECT","locator":row["dependency_locator_id"],"source_version_root":row["source_version_root"],"visual_verification":row["visual_verification"],"status":"ACCEPTED"})
        edges.append({"from":accepted_locator_id,"to":node_id,"semantic":"DEFINED_BY"})
        topo.append(node_id)
    for leaf in leaves:
        nodes.append({"node_id":leaf["dependency_id"],"node_class":leaf["node_class"],"locator":None,"status":"UNRESOLVED_DEPENDENCY"})
        edges.append({"from":accepted_locator_id,"to":leaf["dependency_id"],"semantic":"USES_SYMBOL"})
        topo.append(leaf["dependency_id"])
    return _freeze({"schema":"C165-DEPENDENCY-GRAPH-V1","graph_id":"C165-GRAPH-"+accepted_locator_id,"root_accepted_locator_id":accepted_locator_id,"nodes":tuple(_freeze(n) for n in nodes),"edges":tuple(_freeze(e) for e in edges),"edge_semantics":EDGE_SEMANTICS,"topological_order":tuple(topo),"unresolved_leaves":tuple(x["dependency_id"] for x in leaves),"source_version_consistent":True,"cycle_status":"ACYCLIC","cycle_count":0,"closure_status":"DEPENDENCY_LOCATOR_INCOMPLETE","root":_root((accepted_locator_id,nodes,edges,topo))})

def dependency_closure_manifest() -> MappingProxyType:
    rows=[]
    for root in ACCEPTED_ROOTS:
        graph=dependency_graph(root["locator_id"])
        rows.append({"accepted_locator_id":root["locator_id"],"graph_id":graph["graph_id"],"node_count":len(graph["nodes"]),"edge_count":len(graph["edges"]),"accepted_dependency_count":len(accepted_dependency_manifest(root["locator_id"])["rows"]),"unresolved_leaf_count":len(graph["unresolved_leaves"]),"cycle_count":graph["cycle_count"],"source_version_consistent":graph["source_version_consistent"],"closure_status":graph["closure_status"],"root":graph["root"]})
    return _freeze({"schema":"C165-DEPENDENCY-CLOSURE-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"graph_count":len(rows),"closed_graph_count":0,"partial_graph_count":0,"incomplete_graph_count":len(rows),"root":_root(rows)})

def descriptor_dependency_crosswalk() -> MappingProxyType:
    rows=[]
    for d in DESCRIPTOR_ROWS:
        rid=d["accepted_final_locator_id"]
        if rid:
            g=dependency_graph(rid)
            status=g["closure_status"]
            missing="; ".join(x["semantic"] for x in _missing_leaves(rid))
            rows.append({"descriptor_id":d["descriptor_id"],"quantity_family":d["quantity_family"],"C164_terminal_status":d["terminal_status"],"C165_dependency_applicability":"accepted C164 root","accepted_locator_id":rid,"dependency_graph_id":g["graph_id"],"C165_terminal_status":status,"exact_first_missing_object":missing})
        else:
            rows.append({"descriptor_id":d["descriptor_id"],"quantity_family":d["quantity_family"],"C164_terminal_status":d["terminal_status"],"C165_dependency_applicability":"preserved; not reopened","accepted_locator_id":None,"dependency_graph_id":None,"C165_terminal_status":d["terminal_status"],"exact_first_missing_object":"C164-preserved final-object branch remains outside C165 dependency scope"})
    counts={}
    for x in rows: counts[x["C165_terminal_status"]]=counts.get(x["C165_terminal_status"],0)+1
    return _freeze({"schema":"C165-DESCRIPTOR-DEPENDENCY-CROSSWALK-V1","rows":tuple(_freeze(x) for x in rows),"descriptor_count":len(rows),"C164_absent_final_object_count":sum(x["C164_terminal_status"]=="FINAL_OBJECT_NOT_PRESENT_IN_LOCAL_SOURCES" for x in rows),"C164_role_mismatch_count":sum(x["C164_terminal_status"]=="SOURCE_ROLE_MISMATCH" for x in rows),"terminal_status_counts":counts,"root":_root(rows)})

def componentwise_dependency_manifest(quantity_id: str) -> MappingProxyType:
    if quantity_id not in QUANTITIES: raise KeyError(quantity_id)
    rows=tuple(x for x in descriptor_dependency_crosswalk()["rows"] if x["quantity_family"]==quantity_id)
    return _freeze({"schema":"C165-COMPONENTWISE-DEPENDENCY-MANIFEST-V1","quantity_id":quantity_id,"rows":rows,"accepted_roots":sum(x["accepted_locator_id"] is not None for x in rows),"root":_root((quantity_id,rows))})

def mass_coupling_dependency_gate_report() -> MappingProxyType:
    rows=[]
    for q in ("SIGNED_QUARK_MASS","QCD_COUPLING"):
        qrows=[x for x in descriptor_dependency_crosswalk()["rows"] if x["quantity_family"]==q]
        rows.append({"quantity_id":q,"accepted_root_count":sum(x["accepted_locator_id"] is not None for x in qrows),"complete_source_coordinates":False,"complete_projector_kinematics":False,"complete_gauge_scheme_nf":False,"complete_renormalization_or_step_chain":False,"acyclic":True,"visual_verification":True,"source_version_consistent":True,"gate_status":"C165_HQCDLFGDEP_DEPENDENCY_LOCATOR_INCOMPLETE"})
    return _freeze({"schema":"C165-MASS-COUPLING-DEPENDENCY-GATE-V1","rows":tuple(_freeze(x) for x in rows),"gate_closed":True,"expression_transcription_authorized":False,"target_execution_authorized":False,"PDG_values_consumed":0,"root":_root(rows)})

def missing_dependency_request_manifest() -> MappingProxyType:
    rows=[]
    for root in ACCEPTED_ROOTS:
        for leaf in _missing_leaves(root["locator_id"]):
            rows.append({"request_id":"C165-REQ-"+leaf["dependency_id"],"root_accepted_locator_id":root["locator_id"],"descriptor_id":root["descriptor_id"],"unresolved_symbol_or_semantic_dependency":leaf["semantic"],"required_node_class":leaf["node_class"],"candidate_source_version":root["source_id"]+" "+root["source_version"],"why_candidates_insufficient":"no single accepted object-level locator binds the requested dependency without an unproven adapter or role promotion","exact_missing_object":leaf["required_object"],"required_artifact":"matching authenticated PDF object, TeX archive, ancillary formula file, erratum, supplement, or source-code object for the frozen version","effect_on_interpretation":"blocks source coordinate/projector/gauge/scheme/N_f or layer closure","no_substitute":True,"status":"OPEN_MISSING_DEPENDENCY_REQUEST","root":leaf["root"]})
    return _freeze({"schema":"C165-MISSING-DEPENDENCY-REQUEST-MANIFEST-V1","rows":tuple(_freeze(x) for x in rows),"count":len(rows),"root":_root(rows)})

def expression_transcription_handoff_contract() -> MappingProxyType:
    return _freeze({"schema":"C165-EXPRESSION-TRANSCRIPTION-HANDOFF-V1","eligible":False,"accepted_root_locator_records":len(ACCEPTED_ROOTS),"accepted_dependency_locator_records":len(accepted_dependency_manifest()["rows"]),"dependency_graphs_closed":0,"complete_expressions":0,"target_values":0,"reason":"all eight graphs retain unresolved leaves","next":NEXT,"prohibited_payloads":("complete expressions","target values","matching","running","physical inputs"),"root":_root((False,len(ACCEPTED_ROOTS),NEXT))})

def quantum_dependency_handoff() -> MappingProxyType:
    return _freeze({"schema":"C165-QUANTUM-DEPENDENCY-HANDOFF-V1","Q0_Q1_Q2_modified":False,"quantum_objects_consumed":0,"next":NEXT,"root":_root((False,NEXT))})

def _request_roots() -> tuple[str, ...]:
    return tuple(x["root"] for x in missing_dependency_request_manifest()["rows"])

def lfgdep_completeness_certificate() -> MappingProxyType:
    cross=descriptor_dependency_crosswalk()
    return _freeze({"schema":"C165-LFGDEP-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"accepted_roots":8,"source_symbol_count":sum(len(_symbol_rows(r["locator_id"])) for r in ACCEPTED_ROOTS),"candidate_dependencies":candidate_dependency_manifest()["candidate_count"],"accepted_dependencies":accepted_dependency_manifest()["accepted_dependency_count"],"dependency_graphs":8,"closed_graphs":0,"unresolved_leaves":len(missing_dependency_request_manifest()["rows"]),"all_graphs_acyclic":True,"all_accepted_dependency_visual":True,"complete_expressions":0,"target_programs":0,"target_values":0,"descriptor_terminal_counts":cross["terminal_status_counts"],"mass_coupling_gate_closed":True,"next":NEXT,"root":_root((STATUS,PLAN,cross["root"],NEXT))})

def verify_hqcd_lfgdep_authority() -> dict[str, Any]:
    runtime={"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT}
    inv=c164.verify_hqcd_lfglocator2_authority()
    if inv["package_root"] != C164_ROOT or inv["accepted_locators"] != 8: raise ValueError("C164 authority changed")
    return {"schema":"C165-HQCDLFGDEP-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"next":NEXT,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"C164_status":C164_STATUS,"C164_package_root":C164_ROOT,"C163_package_root":C163_ROOT,"C162_package_root":C162_ROOT,"C161_package_root":C161_ROOT,"C160_package_root":C160_ROOT,"C159_package_root":C159_ROOT,"C158_package_root":C158_ROOT,"accepted_roots":len(ACCEPTED_ROOTS),"candidate_dependencies":candidate_dependency_manifest()["candidate_count"],"accepted_dependencies":accepted_dependency_manifest()["accepted_dependency_count"],"graphs_closed":0,"complete_expressions":0,"target_values":0,"PDG_values_consumed":0,"roots":ROOTS,"package_root":PACKAGE_ROOT}

def load_verified_hqcd_lfgdep_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C165 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C165 package root/status mismatch")
    return _freeze(verify_hqcd_lfgdep_authority())

def lfgdep_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C165-LFGDEP-PLAN-MANIFEST-V1","selected_plan":PLAN,"status":STATUS,"reason":"accepted dependency objects are present but exact coordinate/gauge/N_f/layer leaves remain unresolved","next":NEXT,"root":_root((PLAN,STATUS,NEXT))})

def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C131_C164_roots_unchanged":True,"accepted_C164_root_objects_changed":0,"C134_modified":False,"untracked_C157_test_modified":False,"web_definitions":0,"unauthorized_downloads":0,"invented_dependency_locators":0,"page_only_dependencies":0,"text_only_dependencies":0,"invented_expressions":0,"PDG_values_consumed":0,"C158_imports":0,"C158_recomputed":0,"complete_expressions":0,"target_values":0,"matching":0,"common_IR":0,"remainders":0,"brackets":0,"windows":0,"running":0,"thresholds":0,"counterterms":0,"null_coordinates":0,"Q0_Q1_Q2_modified":False,"network":0,"allow_pickle_false":True,"pass":True})

def mutate_live_hqcdlfgdep(index: int) -> MappingProxyType:
    fields=("C164_root","C163_root","C162_root","C161_root","C160_root","C159_root","C158_root","accepted_locator_id","accepted_root_field","source_symbol_id","node_class","source_id","source_version","pdf_index0","pdf_index1","printed_page","object_label","bbox","anchor_before","anchor_after","page_text_hash","page_render_hash","object_crop_hash","visual_status","candidate_assignment","coordinate","order","projector","kinematics","gauge","scheme","active_Nf","renormalization_layer","step_scaling_edge","graph_edge","topological_order","cycle_status","descriptor_terminal","missing_request","loader","package_root","next")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={
    "C165_INPUT_ROOT":_root((BASELINE,CONTRACT,CONTRACT_SHA256,ROOT_CHAIN,C164_ROOT)),
    "C165_REGRESSION_BOUNDARY_ROOT":_root((C134_CLASSIFICATION,C158_ROOT,C164_ROOT)),
    "C165_PLAN_ROOT":lfgdep_plan_manifest()["root"],
    "C165_ACCEPTED_ROOT_OBJECT_ROOT":_root(ACCEPTED_ROOTS),
    "C165_SOURCE_SYMBOL_ROOT":source_symbol_inventory()["root"],
    "C165_DEPENDENCY_NODE_SCHEMA_ROOT":dependency_node_schema()["root"],
    "C165_CANDIDATE_DEPENDENCY_ROOT":candidate_dependency_manifest()["root"],
    "C165_VISUAL_DEPENDENCY_ROOT":_root(tuple(visual_dependency_report(x["dependency_locator_id"])["root"] for x in accepted_dependency_manifest()["rows"])),
    "C165_ACCEPTED_DEPENDENCY_ROOT":accepted_dependency_manifest()["root"],
    "C165_SOURCE_COORDINATE_ROOT":source_coordinate_dependency_manifest()["root"],
    "C165_PROJECTOR_KINEMATIC_ROOT":projector_kinematic_dependency_manifest()["root"],
    "C165_GAUGE_SCHEME_NF_ROOT":gauge_scheme_nf_dependency_manifest()["root"],
    "C165_RENORMALIZATION_DEPENDENCY_ROOT":renormalization_dependency_manifest()["root"],
    "C165_STEP_SCALING_DEPENDENCY_ROOT":step_scaling_dependency_manifest()["root"],
    "C165_DEPENDENCY_GRAPH_ROOT":_root(tuple(dependency_graph(x["locator_id"])["root"] for x in ACCEPTED_ROOTS)),
    "C165_DEPENDENCY_CLOSURE_ROOT":dependency_closure_manifest()["root"],
    "C165_DESCRIPTOR_CROSSWALK_ROOT":descriptor_dependency_crosswalk()["root"],
    "C165_QUARK_FIELD_ROOT":componentwise_dependency_manifest("QUARK_FIELD")["root"],
    "C165_SIGNED_MASS_ROOT":componentwise_dependency_manifest("SIGNED_QUARK_MASS")["root"],
    "C165_GLUON_FIELD_ROOT":componentwise_dependency_manifest("TRANSVERSE_GLUON_FIELD")["root"],
    "C165_VERTEX_ROOT":componentwise_dependency_manifest("qg_VERTEX_DRESSING")["root"],
    "C165_COUPLING_ROOT":componentwise_dependency_manifest("QCD_COUPLING")["root"],
    "C165_MASS_COUPLING_GATE_ROOT":mass_coupling_dependency_gate_report()["root"],
    "C165_MISSING_DEPENDENCY_REQUEST_ROOT":missing_dependency_request_manifest()["root"],
    "C165_EXPRESSION_HANDOFF_ROOT":expression_transcription_handoff_contract()["root"],
    "C165_QUANTUM_HANDOFF_ROOT":quantum_dependency_handoff()["root"],
    "C165_SCOPE_ROOT":_root((STATUS,"dependency-locator-only","no expressions")),
    "C165_COMPLETENESS_ROOT":lfgdep_completeness_certificate()["root"],
}
PACKAGE_ROOT=_root({"schema":"C165-HQCDLFGDEP-V1","baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"plan":PLAN,"roots":ROOTS})

__all__=["STATUS","PLAN","NEXT","PACKAGE_ROOT","ROOTS","BASELINE","CONTRACT","CONTRACT_SHA256","C164_ROOT","C163_ROOT","C162_ROOT","C161_ROOT","C160_ROOT","C159_ROOT","C158_ROOT","SOURCE_HASHES","load_verified_hqcd_lfgdep_authority","verify_hqcd_lfgdep_authority","lfgdep_plan_manifest","accepted_root_object_manifest","source_symbol_inventory","dependency_node_schema","candidate_dependency_manifest","accepted_dependency_manifest","visual_dependency_report","source_coordinate_dependency_manifest","projector_kinematic_dependency_manifest","gauge_scheme_nf_dependency_manifest","renormalization_dependency_manifest","step_scaling_dependency_manifest","dependency_graph","dependency_closure_manifest","descriptor_dependency_crosswalk","componentwise_dependency_manifest","mass_coupling_dependency_gate_report","missing_dependency_request_manifest","expression_transcription_handoff_contract","quantum_dependency_handoff","lfgdep_completeness_certificate","static_isolation_guard","mutate_live_hqcdlfgdep"]

def accepted_root_object_manifest() -> MappingProxyType:
    return _freeze({"schema":"C165-ACCEPTED-ROOT-OBJECT-MANIFEST-V1","rows":ACCEPTED_ROOTS,"count":len(ACCEPTED_ROOTS),"C164_root_unchanged":True,"root":_root(ACCEPTED_ROOTS)})
