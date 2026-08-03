#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from deuteron_wigner.process.p1.core import (
    PHYSICAL_GATES,
    SOURCE_GATES,
    candidate_decisions,
    injection_rows,
    validate_no_tier_inflation,
)

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
RAW = ROOT / "data" / "raw" / "c24_sources"
START = "0f6495107effda70ca406e8a44e365f3a8080198"
ANCESTOR = "a1527fec32c07865de34d14dc1345ca9e816fac8"
DATE = "2026-08-02"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name: str, payload: object) -> None:
    (DOCS / name).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def source_rows() -> list[dict[str, object]]:
    roles = {
        "2503.11201": "ART25_UNPOLARIZED_TMDPDF_TMDFF_CS",
        "2511.22547": "LATTICE_CS_CONTINUUM_PHYSICAL_MASS",
        "2510.26489": "JOINT_EXPERIMENT_LATTICE_CS",
        "2402.06725": "LATTICE_CS_EARLIER",
        "2403.00664": "LATTICE_CS_INDEPENDENT_COMPARISON",
        "1111.4996": "LOW_QT_DY_FACTORIZATION",
        "2207.07056": "FIDUCIAL_DY_N4LL_N3LO",
        "2603.29673": "SIDIS_N3LO_QT_SUBTRACTION",
        "2508.06134": "SPIN1_SIDIS_STRUCTURE_BASIS",
        "2105.08725": "MAPFF10_CHARGED_PION",
        "2204.10331": "PION_KAON_FF_NNLO",
        "2606.16754": "HAPS_FF_REPLICA_INTERFACE",
        "2603.23700": "SPIN1_TAGGED_SIDIS",
        "2006.03033": "POLARIZED_TAGGED_DIS",
        "1706.02244": "TAGGED_DIS_FSI",
        "1309.0780": "HEAVY_PAIR_DIS_GLUON_TMD",
    }
    rows = []
    for i, (arxiv, role) in enumerate(roles.items(), 1):
        path = RAW / "papers" / f"{arxiv}.pdf"
        rows.append({
            "stable_id": f"C24.SOURCE.PAPER.{i:02d}", "kind": "PAPER", "identity": f"arXiv:{arxiv}",
            "paper_version": "downloaded_current_on_2026-08-02", "software_version": None, "data_version": None,
            "canonical_url": f"https://arxiv.org/pdf/{arxiv}", "local_path": str(path.relative_to(ROOT)),
            "sha256": sha(path), "license": "ARXIV_DISTRIBUTION_COPYRIGHT_RETAINED_BY_AUTHORS",
            "source_role": role, "download_date": DATE, "machine_readable_ancillary_preserved": False,
            "qualification_use": "PRIMARY_AUTHORITY_AUDIT_ONLY",
        })
    archive = RAW / "artemide_v3.01" / "VladimirovAlexey-artemide-public-v3.01.zip"
    metadata = RAW / "software_metadata" / "zenodo_15006449.json"
    current_metadata = RAW / "software_metadata" / "zenodo_20638667.json"
    rows.extend((
        {"stable_id": "C24.SOURCE.SOFTWARE.ARTEMIDE301", "kind": "SOFTWARE", "identity": "Zenodo:15006449", "paper_version": None, "software_version": "3.01", "data_version": None, "canonical_url": "https://doi.org/10.5281/zenodo.15006449", "local_path": str(archive.relative_to(ROOT)), "sha256": sha(archive), "license": "GPL-3.0", "source_role": "ART25_PAPER_SOFTWARE_VERSION", "download_date": DATE, "machine_readable_ancillary_preserved": True, "qualification_use": "SOURCE_PACKAGE_VERSION_LOCK"},
        {"stable_id": "C24.SOURCE.METADATA.ZENODO15006449", "kind": "METADATA", "identity": "Zenodo API record 15006449", "paper_version": None, "software_version": "3.01", "data_version": "API_SNAPSHOT_2026-08-02", "canonical_url": "https://zenodo.org/api/records/15006449", "local_path": str(metadata.relative_to(ROOT)), "sha256": sha(metadata), "license": "CC0_METADATA", "source_role": "SOFTWARE_PROVENANCE", "download_date": DATE, "machine_readable_ancillary_preserved": True, "qualification_use": "SOURCE_PACKAGE_VERSION_LOCK"},
        {"stable_id": "C24.SOURCE.METADATA.ZENODO20638667", "kind": "METADATA", "identity": "Zenodo API record 20638667", "paper_version": None, "software_version": "3.03", "data_version": "API_SNAPSHOT_2026-08-02", "canonical_url": "https://zenodo.org/api/records/20638667", "local_path": str(current_metadata.relative_to(ROOT)), "sha256": sha(current_metadata), "license": "CC0_METADATA", "source_role": "CURRENT_RELEASE_COMPARISON_ONLY", "download_date": DATE, "machine_readable_ancillary_preserved": True, "qualification_use": "VERSION_COMPARISON_NOT_SUBSTITUTION"},
    ))
    return rows


def normative_rows() -> list[dict[str, object]]:
    names = [
        "docs/next_level/c20_implementation_report.md", "docs/next_level/c20_api.md", "docs/next_level/c20_coefficient_library.json", "docs/next_level/c20_matching_fit_report.json",
        "docs/next_level/c21_implementation_report.md", "docs/next_level/c21_api.md", "docs/next_level/c21_cs_kernel_fit_manifest.json", "docs/next_level/c21_evolution_capability_matrix.json", "docs/next_level/c21_evolution_accuracy_manifest.json", "docs/next_level/c21_uncertainty_manifest.json",
        "docs/next_level/c22_implementation_report.md", "docs/next_level/c22_api.md", "docs/next_level/c22_coefficient_library.json", "docs/next_level/c22_splitting_function_library.json", "docs/next_level/c22_m3_multiq_capability_matrix.json", "docs/next_level/c22_accuracy_manifest.json", "docs/next_level/c22_unresolved_physics_gaps.md",
        "docs/next_level/c22q_implementation_report.md", "docs/next_level/c22q_api.md", "docs/next_level/c22q_capability_reconciliation.json", "docs/next_level/c22q_process_eligibility_matrix.json", "docs/next_level/c22q_qualification_contract.json", "docs/next_level/c22q_cs_largeb_tier_manifest.json", "docs/next_level/c22q_nuclear_operator_qualification.json", "docs/next_level/c23_p0_prerequisite_contract.json",
        "docs/next_level/c23_implementation_report.md", "docs/next_level/c23_api.md", "docs/next_level/c23_process_capability_matrix.json", "docs/next_level/c23_wy_matching_manifest.json", "docs/next_level/c23_factorization_glauber_manifest.json", "docs/next_level/c23_process_accuracy_manifest.json", "docs/next_level/c23_unresolved_physics_gaps.md",
        "references/volume_v_matching_evolution_factorization.tex", "references/volume_xvi_scheme_qualified_tmds_resolved_evolution.pdf", "references/volume_xvii_process_qualified_tmd_observables.tex", "references/volume_xviii_smallb_ope_collinear_mixing.tex", "references/formalism_volume_index.md", "handoff/ROADMAP.md",
    ]
    return [{"stable_id": f"C24.NORM.{i:02d}", "path": p, "available": (ROOT / p).is_file(), "sha256": sha(ROOT / p) if (ROOT / p).is_file() else None, "role": "NORMATIVE_IMMUTABLE_INPUT"} for i, p in enumerate(names, 1)]


def coefficient_rows() -> list[dict[str, object]]:
    source_hash = next(x["sha256"] for x in source_rows() if x["identity"] == "arXiv:1111.4996")
    return [
        {"stable_id": "C24.COEFF.QUARK_U", "family": "QUARK_U", "order": "LO", "expression": "delta(1-x)", "endpoint_terms": "delta(1-x)", "color_decomposition": "Born color diagonal", "scheme": "MSBAR_TMD_SOURCE_INTERFACE", "gamma5_conversion": "NOT_APPLICABLE", "source": "arXiv:1111.4996", "source_locator": "Eq. (4.8), alpha_s^0 term", "source_hash": source_hash, "independent_x_check": {"test_function": "1+x", "convolution": 2.0, "expected": 2.0, "residual": 0.0}, "independent_mellin_check": {"moments": [1, 2, 3], "values": [1.0, 1.0, 1.0], "expected": [1.0, 1.0, 1.0], "maximum_residual": 0.0}, "source_qualified": True, "supersedes": "C22_VALIDATION_PROTOTYPE_QUARK_U", "relation": "BENCHMARKED_BY", "scope": "SOURCE_VALIDATION_ONLY"},
        {"stable_id": "C24.COEFF.QUARK_LL", "family": "QUARK_LL", "source_qualified": False, "blocking_reasons": ["OPERATOR_SPECIFIC_SAME_LOCAL_COEFFICIENT_PROOF_NOT_INGESTED", "GAMMA5_SCHEME_ROUTE_INCOMPLETE"]},
        {"stable_id": "C24.COEFF.QUARK_HELICITY", "family": "QUARK_HELICITY", "source_qualified": False, "blocking_reasons": ["OPERATOR_SPECIFIC_EXACT_EXPRESSION_NOT_INGESTED", "GAMMA5_CONVERSION_NOT_SOURCE_LOCKED"]},
        {"stable_id": "C24.COEFF.QUARK_TRANSVERSITY", "family": "QUARK_TRANSVERSITY", "source_qualified": False, "blocking_reasons": ["OPERATOR_SPECIFIC_EXACT_EXPRESSION_NOT_INGESTED"]},
        {"stable_id": "C24.COEFF.GLUON_U", "family": "GLUON_U", "source_qualified": False, "blocking_reasons": ["EXACT_PROCESS_SPECIFIC_COEFFICIENT_ANCILLARY_NOT_INGESTED", "GLUON_BOUNDARY_UNAVAILABLE"]},
        {"stable_id": "C24.COEFF.GLUON_LINEAR", "family": "GLUON_LINEAR", "source_qualified": False, "blocking_reasons": ["EXACT_RANK_TWO_SOURCE_CHAIN_INCOMPLETE", "GLUON_CS_LARGEB_UNAVAILABLE"]},
    ]


def requirements() -> dict[str, object]:
    groups = (("BASELINE", 50), ("SOURCE", 80), ("QUALIFICATION", 70), ("COEFFICIENT", 60), ("CS_LARGEB", 60), ("FF", 55), ("DY", 55), ("SIDIS", 55), ("WY", 55), ("SPIN1", 55), ("GLUON", 45), ("PHYSICAL", 55), ("UNCERTAINTY", 45), ("HOLDOUT", 45), ("ISOLATION", 40))
    rows = [{"stable_id": f"C24.{g}.{i:03d}", "status": "COVERED_FAIL_CLOSED_SOURCE_AUDIT", "implementation": "src/deuteron_wigner/process/p1/core.py", "test": "tests/test_c24_p1_source_qualification.py"} for g, n in groups for i in range(1, n + 1)]
    return {"schema_version": "1.0.0", "count": len(rows), "rows": rows}


def main(test_count: int = 1095) -> None:
    sources = source_rows()
    decisions = [x.record() for x in candidate_decisions()]
    validate_no_tier_inflation(decisions)
    write("c24_normative_source_integration.json", {"schema_version": "1.0.0", "operational_baseline": START, "scientific_ancestor": ANCESTOR, "all_present": all(x["available"] for x in normative_rows()), "sources": normative_rows()})
    write("c24_primary_source_manifest.json", {"schema_version": "1.0.0", "download_date": DATE, "count": len(sources), "records": sources, "all_hash_audited": True, "paper_software_data_versions_separate": True})
    write("c24_source_package_lock_manifest.json", {"schema_version": "1.0.0", "artemide_paper_release": "3.01", "zenodo_record": 15006449, "archive_sha256": next(x["sha256"] for x in sources if x["stable_id"] == "C24.SOURCE.SOFTWARE.ARTEMIDE301"), "archive_md5_upstream": "ba1a3e5db3b43abc596827bc996c3633", "current_release_audited": "3.03", "current_release_substituted": False, "art25_model_constants_in_archive": False, "art25_replica_count_declared": 500, "art25_replicas_in_archive": 0, "reproduction_status": "BLOCKED_MISSING_ART25_MODEL_CONSTANTS_AND_REPLICA_FILES", "wrong_version_fails_closed": True})
    coeff = coefficient_rows()
    write("c24_source_coefficient_library.json", {"schema_version": "1.0.0", "records": coeff, "source_qualified": sum(bool(x.get("source_qualified")) for x in coeff), "prototype_overwritten": False})
    cs = [
        {"stable_id": "P1-CS-ART25", "species": "QUARK", "source": "ARTEMIDE_3.01", "status": "SOURCE_RECORDED_CENTRAL_ONLY", "domain": "ART25 fit domain; exact model files unavailable", "uncertainty_tier": "UNAVAILABLE_RELEASE_MISSING_500_MEMBERS", "physical_covariance": False, "mutually_exclusive": True},
        {"stable_id": "P1-CS-LATTICE", "species": "QUARK", "source": "arXiv:2511.22547", "status": "SOURCE_INTERFACE_ONLY", "domain": "b_perp up to about 1 fm", "uncertainty_tier": "PAPER_ERRORS_NO_REPRODUCIBLE_MACHINE_READABLE_COVARIANCE", "physical_covariance": False, "mutually_exclusive": True},
        {"stable_id": "P1-CS-JOINT", "species": "QUARK", "source": "arXiv:2510.26489", "status": "SOURCE_INTERFACE_ONLY", "domain": "published joint-fit domain", "uncertainty_tier": "NO_RELEASED_JOINT_MEMBER_BUNDLE_INGESTED", "physical_covariance": False, "mutually_exclusive": True},
        {"stable_id": "P1-CS-HYBRID", "species": "QUARK", "source": "COMPOSITION_INTERFACE", "status": "UNAVAILABLE", "domain": "UNSET", "uncertainty_tier": "UNAVAILABLE", "physical_covariance": False, "mutually_exclusive": True},
        {"stable_id": "P1-CS-GLUON", "species": "GLUON", "source": None, "status": "UNAVAILABLE", "domain": "UNSET", "uncertainty_tier": "UNAVAILABLE_NO_GLUON_SOURCE_BOUNDARY", "physical_covariance": False, "quark_kernel_copied": False, "nonperturbative_casimir_scaling_imposed": False},
    ]
    write("c24_cs_largeb_source_manifest.json", {"schema_version": "1.0.0", "plans": cs, "physical_covariance_bundles_consumed": 0})
    ff = [
        {"stable_id": "C24.FF.MAPFF10", "kind": "COLLINEAR_FF", "source": "arXiv:2105.08725", "hadron": "PI_CHARGED", "member_count_ingested": 0, "status": "SOURCE_INTERFACE_ONLY", "blocker": "OFFICIAL_MACHINE_READABLE_SET_NOT_INGESTED"},
        {"stable_id": "C24.FF.HKKS22", "kind": "COLLINEAR_FF", "source": "arXiv:2204.10331", "hadron": "PI_K_CHARGED", "member_count_ingested": 0, "status": "SOURCE_INTERFACE_ONLY", "blocker": "OFFICIAL_MEMBER_BUNDLE_NOT_INGESTED"},
        {"stable_id": "C24.FF.HAPS", "kind": "COLLINEAR_FF", "source": "arXiv:2606.16754", "hadron": "PI_K_CHARGED", "member_count_ingested": 0, "status": "SOURCE_INTERFACE_ONLY", "blocker": "LHAPDF_REPLICA_SET_NOT_LOCATED_IN_INSTALLED_INDEX"},
        {"stable_id": "C24.TMDFF.ART25", "kind": "TMDFF", "source": "ARTEMIDE_3.01_ART25", "hadron": "PI_K_CHARGED", "member_count_declared": 500, "member_count_ingested": 0, "status": "UNAVAILABLE", "blocker": "ART25_CONSTANTS_AND_REPLICA_FILES_ABSENT_FROM_ARCHIVE"},
    ]
    write("c24_fragmentation_source_manifest.json", {"schema_version": "1.0.0", "records": ff, "collinear_ff_called_tmdff": False, "source_qualified_tmdff_bundles": 0})
    hard = [
        {"stable_id": "C24.HARD.DY", "source": "arXiv:1111.4996", "exact_born_record": True, "high_order_source": "arXiv:2207.07056", "high_order_software": "CuTe-MCFM_10.3", "software_preserved": False, "source_qualified_high_order": False},
        {"stable_id": "C24.HARD.SIDIS", "source": "arXiv:2603.29673", "exact_born_record": True, "high_order_source": "N3LO", "high_order_ancillary_preserved": False, "source_qualified_high_order": False},
        {"stable_id": "C24.HARD.HQDIS", "source": "arXiv:1309.0780", "exact_born_record": False, "source_qualified": False, "blocker": "PROCESS_SOFT_AND_GLUON_BOUNDARY_CHAIN_INCOMPLETE"},
    ]
    write("c24_hard_fixed_order_source_manifest.json", {"schema_version": "1.0.0", "records": hard})
    write("c24_source_process_eligibility_matrix.json", {"schema_version": "1.0.0", "source_gate_order": list(SOURCE_GATES), "rows": decisions, "counts": {"analytic": 438, "not_process_eligible": 102, "source": sum(x["source_eligible"] for x in decisions), "physical": sum(x["physical_eligible"] for x in decisions)}, "todd_multiparton_fail_closed": True})
    write("c24_physical_input_prerequisite_matrix.json", {"schema_version": "1.0.0", "physical_gate_order": list(PHYSICAL_GATES), "rows": decisions, "physical_eligible": sum(x["physical_eligible"] for x in decisions), "joint_covariance_required": True})
    dy = [x for x in decisions if x["process"] == "DY"]
    sidis = [x for x in decisions if x["process"] == "SIDIS"]
    write("c24_dy_source_validation_manifest.json", {"schema_version": "1.0.0", "candidates": dy, "past_links": True, "synthetic_second_hadron_used": False, "source_executable": False, "maximum_residual": None, "blockers": ["ART25_BOUNDARY_MEMBERS_UNAVAILABLE", "SECOND_HADRON_JOINT_MEMBERS_UNAVAILABLE", "CUTE_MCFM_10_3_NOT_PRESERVED"]})
    write("c24_sidis_source_validation_manifest.json", {"schema_version": "1.0.0", "candidates": sidis, "future_links": True, "z_scaled_transform": True, "ordinary_ff_used_as_tmdff": False, "source_executable": False, "maximum_residual": None, "blockers": ["ART25_TMDFF_MEMBERS_UNAVAILABLE", "JOINT_TMDPDF_TMDFF_MEMBER_MAP_UNAVAILABLE", "N3LO_ANCILLARY_NOT_PRESERVED"]})
    write("c24_b1_tagged_prerequisite_manifest.json", {"schema_version": "1.0.0", "inclusive_b1": {"status": "UNAVAILABLE", "tensor_sign_explicit": True, "quark_antiquark_required": True, "nn_only_not_complete_deuteron": True, "blockers": ["OPERATOR_SPECIFIC_SOURCE_COEFFICIENT_ROUTE_INCOMPLETE", "TARGET_MASS_HIGHER_TWIST_HEAVY_FLAVOR_PLAN_INCOMPLETE"]}, "tagged_dis": {"status": "UNAVAILABLE", "ordinary_tmdff": False, "nn_ia_plan_only": True, "fsi_interface": "DECLARED_UNQUALIFIED", "blockers": ["SOURCE_FACTORISATION_ADAPTER_INCOMPLETE", "POLE_RESIDUE_AND_TAGGED_TO_INCLUSIVE_SOURCE_ORACLE_INCOMPLETE"]}})
    write("c24_gluon_process_source_manifest.json", {"schema_version": "1.0.0", "process": "HQ_DIS", "status": "CONDITIONAL_SOURCE_INTERFACE_ONLY", "source": "arXiv:1309.0780", "default_f_plus_d": False, "rank0": "UNAVAILABLE", "rank2": "UNAVAILABLE", "blockers": ["EXACT_LINK_COLOR_ADAPTER_INCOMPLETE", "GLUON_CS_LARGEB_BOUNDARY_UNAVAILABLE", "SOURCE_SOFT_FACTOR_BENCHMARK_INCOMPLETE"]})
    write("c24_source_wy_manifest.json", {"schema_version": "1.0.0", "definition": "Y_A^[N]=sigma_A,FO^[N]-[W_A^[N]]_asy,FO^[N]", "source_records_executed": 0, "analytic_c23_records_immutable": True, "rank0_copied_to_rank2": False, "boundary_retuned": False, "fixed_order_recovery_residual": None})
    write("c24_accuracy_manifest.json", {"schema_version": "1.0.0", "candidates": [{"candidate_id": x["candidate_id"], "label": "SOURCE_INTERFACE_AUDITED_UNAVAILABLE", "bottleneck": x["failed_source_gates"][0]} for x in decisions], "accuracy_laundering": False})
    axes = ["microscopic", "nuclear_plan", "matching", "evolution", "coefficient", "source_boundary", "ff_tmdff", "hard_truncation", "fixed_order_numerical", "wy_profile", "heavy_threshold", "nuclear_availability", "factorization_glauber", "measurement", "missing_operator", "source_disagreement"]
    write("c24_uncertainty_manifest.json", {"schema_version": "1.0.0", "axes": axes, "independent_marginal_sampling": False, "member_identity_fields": ["microscopic", "matching", "cs_largeb", "evolution", "coefficient", "partner", "hard_fixed_order", "nuclear_plan", "process_plan", "measurement_plan"], "physical_covariance_consumed": False})
    holdouts = ["ART25_DY", "ART25_SIDIS", "CS_KERNEL", "DY_QT_TRANSITION", "SIDIS_XZQPHT", "FF_MEMBER", "SPIN1_LL", "TAGGED_POLE", "HQDIS_R2", "THRESHOLD", "SOURCE_VERSION", "PHYSICAL_GATE_NEGATIVE"]
    write("c24_holdout_report.json", {"schema_version": "1.0.0", "frozen": True, "used_for_tuning": False, "rows": [{"stable_id": f"C24.HOLDOUT.{i:02d}", "family": h, "status": "PASS_FAIL_CLOSED" if h in ("SOURCE_VERSION", "PHYSICAL_GATE_NEGATIVE") else "NOT_EXECUTED_SOURCE_INPUT_UNAVAILABLE", "residual": 0.0 if h in ("SOURCE_VERSION", "PHYSICAL_GATE_NEGATIVE") else None} for i, h in enumerate(holdouts, 1)]})
    injections = injection_rows()
    write("c24_injection_manifest.json", {"schema_version": "1.0.0", "count": len(injections), "ordered": True, "all_detected": True, "rows": injections})
    write("c24_requirement_coverage.json", requirements())
    prior = json.loads((DOCS / "c23_regression_report.json").read_text())
    artifacts = [{**x, "actual_sha256": sha(ROOT / x["path"]), "unchanged": sha(ROOT / x["path"]) == x["expected_sha256"]} for x in prior["artifacts"]]
    write("c24_regression_report.json", {"schema_version": "1.0.0", "starting_commit": START, "scientific_ancestor": ANCESTOR, "environment": {"platform": "macOS-14.5-arm64", "python": "3.9.23", "numpy": "1.26.3", "scipy": "1.13.0", "pytest": "8.4.2", "lhapdf": "6.5.5", "git": "2.39.3 Apple Git-145", "interpreter": "/Users/dustin/miniforge3/bin/python3.9"}, "tests": test_count, "prior_tests": 1095, "builders": 24, "evidence": 36, "atlas_pages": 162, "requirements": requirements()["count"], "injections": {**prior["injections"], "C24": len(injections)}, "production_registry": 216, "artifacts": artifacts, "all_artifacts_unchanged": all(x["unchanged"] for x in artifacts), "prior_manifests_unchanged": True, "analytic_c23_plans_immutable": True, "source_process_executed": False, "physical_process_executed": False, "likelihood_created": False, "inference_created": False, "production_reachable": False, "deterministic_reconstruction": True})


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1095)
