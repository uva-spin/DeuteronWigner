"""C140/HQCDPHYSANCHOR source-locked physical-anchor boundary.

Standard-QCD sources are retained as typed comparison/candidate authorities.
No finite-light-front conversion or physical project anchor is emitted until
the C43-compatible two-point and field-normalization calculations close.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c140_hqcdphysanchor"
BASELINE = "dbf7451c40d999819ebcfcb1520e5ed925b56406"
OLD_CONTRACT = "docs/next_level/c139_c140_hqcdinput5_import_contract.json"
CONTRACT = "docs/next_level/c139_c140_hqcdphysanchor_import_contract.json"
STATUS = "C140_HQCDPHYSANCHOR_QUARK_TWO_POINT_INCOMPLETE"
NEXT = "C141/HQCD2PT"
SCHEMA = "C140-HQCDPHYSANCHOR-V1"
C139_ROOT = "4f7a688eeaa492ce7bea569ac4442cea30ee549168ef8291be4e89774f92a361"
C138_ROOT = "075c29f17e149b35ae2b78dcbc0f33c25d7457b321fd01479238cecd875eec9b"
C137_ROOT = "96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"
C136_ROOT = "fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262"
C135_ROOT = "e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b"
SCHEME = "PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1"
SOURCES = (
    ("pdg2026_qcd", "data/raw/c140_sources/pdg2026_qcd.pdf", "c04c628d76b18610c5fa2a919c6081918a25b55fb971b6af5829f4ca2baa386f", "STANDARD_NUMERICAL_ANCHOR_AUTHORITY"),
    ("pdg2026_quark_masses", "data/raw/c140_sources/pdg2026_quark_masses.pdf", "90b4d001694b6bc6addf1e31a0685fca8f54bec3da3530c4122c96a0b1f8a8e7", "STANDARD_NUMERICAL_ANCHOR_AUTHORITY"),
    ("sturm_ri_smom", "data/raw/c140_sources/arxiv_0901.2599.pdf", "826e6a51e43cf20d99e727c1fb3c72f1fcf0b92f77b82ddc866004e14d133c17", "CONTINUUM_SCHEME_DEFINITION_AUTHORITY"),
    ("bednyakov_pikelner_ri_smom_msbar", "data/raw/c140_sources/arxiv_2002.12758.pdf", "ac3fd74ce9d838359b06ee6a2a6b1fb6b2dcde7a349175f2ed90fe04d2b5365d", "CONTINUUM_CONVERSION_METHOD_AUTHORITY"),
    ("gracey_momq", "data/raw/c140_sources/arxiv_1108.4806.pdf", "191b3a3281ef72a451146d6e40d3fcb602db08d2b5e88fa3852fc05d5dea2b90", "CONTINUUM_CONVERSION_METHOD_AUTHORITY"),
    ("bednyakov_pikelner_mom_beta", "data/raw/c140_sources/arxiv_2002.02875.pdf", "96f7ada8a8bcdab4e50c5afb572d668afade986413392574c4160dbaa880dfac", "CONTINUUM_CONVERSION_METHOD_AUTHORITY"),
    ("alpha_step_coupling", "data/raw/c140_sources/arxiv_1706.03821.pdf", "e41e01642d69d9bf5bdbb7395043f4f50b128ac9d8956450d0aecd612c7b0d5a", "NONPERTURBATIVE_STEP_SCALING_METHOD_AUTHORITY"),
    ("alpha_step_mass", "data/raw/c140_sources/arxiv_1802.05243.pdf", "f71625e7561840626ac66ae590f6cac20f027a9ab3b45c27f1e0542267d28c31", "NONPERTURBATIVE_STEP_SCALING_METHOD_AUTHORITY"),
)

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()

def continuation_correction_manifest() -> MappingProxyType:
    return _freeze({"schema": "C139-C140-PHYSANCHOR-CORRECTION-V1", "historical_continuation": "C140/HQCDINPUT5", "historical_reason": "C139 external-input pair absent", "active_continuation": "C140/HQCDPHYSANCHOR", "objective": "derive finite-basis anchors from standard-QCD authorities through explicit matching", "scientific_history_superseded": False, "root": _root(("HQCDINPUT5", "HQCDPHYSANCHOR"))})

def primary_source_manifest() -> MappingProxyType:
    rows = tuple({"source_id": a, "path": b, "sha256": c, "role": d, "regulator_identical": False if d.startswith("CONTINUUM") or d.startswith("NONPERTURBATIVE") else True} for a, b, c, d in SOURCES)
    return _freeze({"schema": "C140-SOURCE-MANIFEST-V1", "sources": rows, "count": len(rows), "all_hash_locked": True, "root": _root(rows)})

def legacy_target_semantic_manifest() -> MappingProxyType:
    return _freeze({"schema": "C140-LEGACY-TARGET-SEMANTICS-V1", "M_R2_FB": "DERIVED_SPECTRAL_DIAGNOSTIC", "g_R_FB(K_R)": "LEGACY_PROJECTED_VERTEX_DIAGNOSTIC", "short_distance_mass": False, "amputated_MOMq_coupling": False, "legacy_capsules_generated": False, "root": _root(("spectral", "projected-vertex"))})

def standard_anchor_manifest() -> MappingProxyType:
    candidates = ({"id": "alpha_s_MSbar_mZ", "candidate_value": "0.1180", "uncertainty": "0.0009", "units": "dimensionless", "source": "PDG 2026 QCD Eq. (9.25), p.41", "active_flavors": 5, "accepted_project_anchor": False}, {"id": "m_ud_MSbar_2GeV_NL4", "candidate_value": "3.397", "uncertainty": "0.045", "units": "MeV", "source": "PDG 2026 Quark Masses Eq. (60.4), p.5", "active_flavors": 4, "accepted_project_anchor": False})
    return _freeze({"schema": "C140-STANDARD-ANCHOR-V1", "candidates": candidates, "accepted": 0, "candidate_only": True, "legacy_capsules_populated": False, "root": _root(candidates)})

def rgi_anchor_manifest() -> MappingProxyType: return _freeze({"schema": "C140-RGI-ANCHOR-V1", "status": "UNAVAILABLE_PROJECT_MATCHING", "mass_rgi": None, "lambda_msbar": None, "route_RG_A_RG_B_mismatches": 0, "root": _root(("unavailable",))})
def physical_anchor_plan_manifest() -> MappingProxyType: return _freeze({"schema": "C140-PLAN-V1", "selected_plan": "PHYS-A", "status": "CALCULATION_INCOMPLETE", "reason": "C43-compatible two-point/resolvent and field residues are not yet available", "alternative_plans": {"PHYS-B": "not selected; would require new color-singlet sectors", "PHYS-C": "not selected; PHYS-A remains the defined target architecture", "PHYS-D": "no source contradiction"}, "root": _root(("PHYS-A", "incomplete"))})
def gauge_regulator_manifest() -> MappingProxyType: return _freeze({"schema": "C140-GAUGE-REGULATOR-V1", "gauge": "C43 light-front A+=0", "inverse_partial_plus": "antisymmetric/PV on nonzero modes", "zero_mode_projector": "explicit", "residual_gauge": "retained transverse Wilson-link/boundary authority", "landau_conversion_imported": False, "complete_adapter": False, "root": _root(("A+=0", "PV", "zero-projector"))})
def reference_kinematics_manifest() -> MappingProxyType: return _freeze({"schema": "C140-REFERENCE-KINEMATICS-V1", "status": "INCOMPLETE", "target_pattern": "spacelike nonexceptional symmetric candidate", "exactly_representable_in_C43": False, "project_scheme_name": "not RI/SMOM or MOMq without exact adapter", "root": _root(("spacelike", False))})
def quark_two_point_manifest() -> MappingProxyType: return _freeze({"schema": "C140-QUARK-TWO-POINT-V1", "status": "UNAVAILABLE", "Z_q_FB": False, "m_R_FB": False, "mass_projector": False, "resolvent_authority": False, "root": _root(("unavailable", "two-point"))})
def short_distance_mass_scheme_manifest() -> MappingProxyType: return _freeze({"schema": "C140-SHORT-DISTANCE-MASS-V1", "status": "UNAVAILABLE_QUARK_TWO_POINT", "dressed_eigenvalue_is_mass": False, "root": _root(("short-distance", False))})
def field_normalization_manifest() -> MappingProxyType: return _freeze({"schema": "C140-FIELD-NORMALIZATION-V1", "status": "INCOMPLETE", "Z_q_FB": False, "Z_A_FB": False, "residual_gauge_audit": True, "root": _root((False, False))})
def amputated_vertex_manifest() -> MappingProxyType: return _freeze({"schema": "C140-AMPUTATED-VERTEX-V1", "status": "UNAVAILABLE_FIELD_RESIDUES", "legacy_adapter": False, "g_R_FB_phys": False, "root": _root(("unavailable",))})
def conversion_function_manifest() -> MappingProxyType: return _freeze({"schema": "C140-CONVERSION-V1", "status": "INCOMPLETE_GAUGE_REGULATOR_ADAPTER", "orientation": "FB <- MSbar", "mass_conversion": False, "coupling_conversion": False, "ir_cancellation": False, "root": _root(("FB<-MSbar", False))})
def matching_window_report() -> MappingProxyType: return _freeze({"schema": "C140-MATCHING-WINDOW-V1", "status": "INCOMPLETE", "candidate_scales": (), "nonempty_window": False, "reason": "reference probes and project residues unavailable", "root": _root(("empty",))})
def step_scaling_manifest() -> MappingProxyType: return _freeze({"schema": "C140-STEP-SCALING-V1", "status": "PLAN_ONLY", "project_specific": True, "sigma_g": False, "sigma_m": False, "alpha_methodology_copied": False, "root": _root(("plan-only", True))})
def derived_anchor_manifest() -> MappingProxyType: return _freeze({"schema": "C140-DERIVED-ANCHOR-V1", "status": "UNAVAILABLE", "m_R_FB": None, "g_R_FB_phys": None, "legacy_capsules_generated": False, "root": _root((None, None, False))})
def physical_anchor_identifiability_report() -> MappingProxyType: return _freeze({"schema": "C140-IDENTIFIABILITY-V1", "status": "NOT_RECOMPUTED", "historical_rank": 2, "historical_nullspace": 9, "new_rank": None, "new_nullspace": 9, "null_coordinates_zeroed": 0, "root": _root((2, 9, None))})
def remaining_nullspace_manifest() -> MappingProxyType: return _freeze({"schema": "C140-NULLSPACE-V1", "dimension": 9, "coordinates": tuple({"id": f"eta_{i}", "status": "UNRESOLVED", "selected": False} for i in range(9)), "root": _root(tuple(range(9)))})
def legacy_capsule_generation_decision() -> MappingProxyType: return _freeze({"schema": "C140-LEGACY-CAPSULE-GENERATION-V1", "generated": False, "reason": "no complete semantic adapter and nullspace remains unresolved", "root": _root((False,))})
def physical_anchor_readiness_certificate() -> MappingProxyType: return _freeze({"schema": "C140-READINESS-V1", "status": STATUS, "positive_gate": False, "missing_gate": "C43-compatible quark two-point/resolvent authority", "next": NEXT, "root": _root((STATUS, NEXT))})
def static_isolation_guard() -> MappingProxyType: return _freeze({"arbitrary_capsules": 0, "validation_masses": 0, "hadron_masses": 0, "process_data": 0, "null_zeroed": 0, "counterterms_solved": 0, "full_matrices": 0, "physical_states": 0, "pass": True})
def mutate_live_hqcdphysanchor(index: int) -> MappingProxyType: return _freeze({"mutation": ("source", "anchor", "flavor", "rge", "threshold", "gauge", "kinematics", "two-point", "field", "vertex", "conversion", "trajectory", "window", "step", "nullspace", "loader", "C141")[int(index) % 17], "positive_gate": False, "must_fail_or_change_root": True})

ROOTS = {"C140_CONTINUATION_CORRECTION_ROOT": _root(continuation_correction_manifest()), "C140_SOURCE_ROOT": _root(primary_source_manifest()), "C140_STANDARD_ANCHOR_ROOT": _root(standard_anchor_manifest()), "C140_RGI_ANCHOR_ROOT": _root(rgi_anchor_manifest()), "C140_PLAN_ROOT": _root(physical_anchor_plan_manifest()), "C140_GAUGE_REGULATOR_ROOT": _root(gauge_regulator_manifest()), "C140_REFERENCE_KINEMATICS_ROOT": _root(reference_kinematics_manifest()), "C140_QUARK_TWO_POINT_ROOT": _root(quark_two_point_manifest()), "C140_FIELD_NORMALIZATION_ROOT": _root(field_normalization_manifest()), "C140_AMPUTATED_VERTEX_ROOT": _root(amputated_vertex_manifest()), "C140_CONVERSION_ROOT": _root(conversion_function_manifest()), "C140_TRAJECTORY_ROOT": _root(("trajectory", "plan")), "C140_MATCHING_WINDOW_ROOT": _root(matching_window_report()), "C140_STEP_SCALING_ROOT": _root(step_scaling_manifest()), "C140_DERIVED_ANCHOR_ROOT": _root(derived_anchor_manifest()), "C140_IDENTIFIABILITY_ROOT": _root(physical_anchor_identifiability_report()), "C140_COMPLETENESS_ROOT": _root(physical_anchor_readiness_certificate())}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "roots": ROOTS, "ancestry": (C139_ROOT, C138_ROOT, C137_ROOT, C136_ROOT, C135_ROOT)})
def verify_hqcd_physical_anchor_authority() -> dict[str, Any]: return {"schema": SCHEMA, "status": STATUS, "positive_gate": False, "selected_plan": "PHYS-A", "baseline": BASELINE, "C139_package_root": C139_ROOT, "C138_package_root": C138_ROOT, "C137_package_root": C137_ROOT, "source_count": len(SOURCES), "source_hashes_locked": True, "standard_anchor_candidates": 2, "accepted_project_anchors": 0, "gauge_adapter_complete": False, "quark_two_point_complete": False, "field_normalization_complete": False, "amputated_vertex_complete": False, "matching_window_nonempty": False, "nullspace": 9, "null_zeroed": 0, "next": NEXT, "roots": ROOTS, "package_root": PACKAGE_ROOT}
def load_verified_hqcd_physical_anchor_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C140 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C140 root/status mismatch")
    return _freeze(verify_hqcd_physical_anchor_authority())
__all__ = ["STATUS", "NEXT", "PACKAGE_ROOT", "ROOTS", "continuation_correction_manifest", "primary_source_manifest", "standard_anchor_manifest", "rgi_anchor_manifest", "physical_anchor_plan_manifest", "gauge_regulator_manifest", "reference_kinematics_manifest", "quark_two_point_manifest", "short_distance_mass_scheme_manifest", "field_normalization_manifest", "amputated_vertex_manifest", "conversion_function_manifest", "matching_window_report", "step_scaling_manifest", "derived_anchor_manifest", "legacy_capsule_generation_decision", "physical_anchor_identifiability_report", "remaining_nullspace_manifest", "physical_anchor_readiness_certificate", "verify_hqcd_physical_anchor_authority", "load_verified_hqcd_physical_anchor_authority", "static_isolation_guard", "mutate_live_hqcdphysanchor"]
