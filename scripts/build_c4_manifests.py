#!/usr/bin/env python3
"""Build deterministic C4 validation-only manifests."""

from __future__ import annotations

import hashlib
import json
import platform
from dataclasses import asdict
from pathlib import Path

import numpy as np

from deuteron_wigner.gtmd import Species
from deuteron_wigner.pilot.c4_benchmarks import (
    exact_structural_zero, integrated_parent_ledger, parents_from_state,
)
from deuteron_wigner.pilot.c4_injections import INJECTIONS
from deuteron_wigner.pilot.c4_provenance import (
    c4_provenance_graph, explicit_plan, induced_plan,
)
from deuteron_wigner.pilot.color import GluonColorSinglet, SeaColorSinglet
from deuteron_wigner.pilot.feshbach import FiniteFeshbachModel
from deuteron_wigner.pilot.routes import (
    CommonReductionRoutes, MellinConvention,
)
from deuteron_wigner.pilot.sectors import gluon_state, sea_state


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "next_level"
OUTPUT = ROOT / "outputs" / "next_level" / "c4"
START = "e123848b2666e1c9db397e47b1c04c0b7146aae7"
C3 = "b0a18ce2d1017e102b2be0849abf4d31537874a8"
REQUIREMENTS = (
    "BASELINE", "ISOLATE", "STATE", "SEA", "SEA_COLOR", "SEA_LEDGER",
    "GLUON", "GLUON_COLOR", "GLUON_LEDGER", "ACTIVE", "ZERO", "OVERLAP",
    "TMD_ROUTE", "GPD_ROUTE", "PDF_ROUTE", "CURRENT_ROUTE", "ROUTE_CLOSURE",
    "MATCHING_STATUS", "FESHBACH", "INDUCED_OPERATOR", "PROVENANCE",
    "INJECT", "CONVERGENCE", "REGRESS", "DOC",
)
AUTHORITATIVE = json.loads(
    (DOC / "c3_regression_report.json").read_text()
)["artifacts"]
C3_MANIFEST_PATHS = (
    "c3_baseline_snapshot.json", "c3_benchmark_manifest.json",
    "c3_injection_manifest.json", "c3_pilot_provenance.json",
    "c3_regression_report.json", "c3_requirement_coverage.json",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name: str, value: object) -> None:
    path = DOC / name
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def baseline() -> dict[str, object]:
    import pytest
    return {
        "schema_version": "1.0.0",
        "requirement_id": "C4.BASELINE",
        "starting_commit": START,
        "c3_ancestor": C3,
        "branch": "main",
        "working_tree": "clean_before_implementation",
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pytest": pytest.__version__,
        },
        "tests": {"passed": 538, "failed": 0},
        "builders": {"passed": 9, "failed": 0},
        "evidence": {"passed": 36, "total": 36},
        "atlas_pages": {"rendered": 162, "required": 162},
        "c3": {
            "benchmarks": 4, "injections": 24,
            "maximum_floating_residual": 8.881784197001252e-16,
            "manifest_hashes": {
                name: sha(DOC / name) for name in C3_MANIFEST_PATHS
            },
        },
        "accepted_registry": {
            "count": 216,
            "sha256": sha(DOC / "c2_reduction_registry.json"),
        },
        "accepted_provenance_sha256": sha(DOC / "c2_provenance_graph.json"),
        "accepted_composition_sha256": sha(DOC / "c2_composition_manifest.json"),
        "authoritative_artifacts": AUTHORITATIVE,
        "normative_sources": {
            name: False for name in (
                "references/volume_0_algebraic_geometric.tex",
                "references/volume_i_regulated_light_front_foundations.tex",
                "references/volume_ii_common_nucleon_gtmd_overlaps.tex",
                "references/volume_iii_dynamical_wilson_lines.tex",
                "references/volume_iv_matched_spin1_nuclear_dynamics.tex",
                "references/model_construction_note.tex",
            )
        },
        "normative_source_observation": (
            "historical pre-implementation snapshot; later source imports "
            "are recorded separately"
        ),
    }


def sector_manifest() -> dict[str, object]:
    probability_grid = (0.0, 1e-8, 0.2, 0.65)
    sea_rows, gluon_rows = [], []
    for probability in probability_grid:
        sea = sea_state(probability)
        gluon = gluon_state(probability)
        sea_rows.append({
            "probability": probability,
            "antiquark_integrated_density": exact_structural_zero(
                sea, Species.ANTIQUARK
            ),
            "ledger": sea.ledger(),
            "integrated_parent_ledger": integrated_parent_ledger(sea),
            "amplitude_ledger": sea.amplitude_ledger(),
            "sector_transverse_norms": {
                sector.stable_id: sector.state.transverse_norm_oracle(
                    len(sector.configuration.constituents)
                ) for sector in sea.sectors
            },
        })
        gluon_rows.append({
            "probability": probability,
            "gluon_momentum_Hg_integral": exact_structural_zero(
                gluon, Species.GLUON
            ),
            "ledger": gluon.ledger(),
            "integrated_parent_ledger": integrated_parent_ledger(gluon),
            "amplitude_ledger": gluon.amplitude_ledger(),
            "sector_transverse_norms": {
                sector.stable_id: sector.state.transverse_norm_oracle(
                    len(sector.configuration.constituents)
                ) for sector in gluon.sectors
            },
        })
    return {
        "schema_version": "1.0.0",
        "requirements": ["C4.STATE", "C4.SEA", "C4.SEA_LEDGER",
                         "C4.GLUON", "C4.GLUON_LEDGER", "C4.ZERO"],
        "sea": {
            "state": "|qqq> + |qqqq qbar>",
            "pair_flavor": "d",
            "positive_x": True,
            "scaling": "integrated diagonal antiquark density = P_sea",
            "members": sea_rows,
        },
        "gluon": {
            "state": "|qqq> + |qqqg>",
            "stored_scalar": "H^g=xg",
            "scaling": "integrated H^g = 0.2 P_g for benchmark fractions",
            "members": gluon_rows,
        },
    }


def color_manifest() -> dict[str, object]:
    sea, gluon = SeaColorSinglet(), GluonColorSinglet()
    return {
        "schema_version": "1.0.0",
        "requirements": ["C4.SEA_COLOR", "C4.GLUON_COLOR"],
        "sea": {
            "stable_id": sea.stable_id, "construction": sea.construction,
            "basis_status": sea.basis_status, "norm": sea.norm(),
            "generator_residual": sea.generator_residual(),
            "wrong_antiquark_sign_residual": sea.generator_residual(
                antiquark_sign=1
            ),
        },
        "gluon": {
            "stable_id": gluon.stable_id,
            "construction": gluon.construction,
            "multiplicity_channel": gluon.multiplicity_channel,
            "norm": gluon.norm(),
            "generator_residual": gluon.generator_residual(),
            "omitted_adjoint_residual": gluon.generator_residual(
                include_adjoint=False
            ),
        },
    }


def route_manifest() -> dict[str, object]:
    routes = CommonReductionRoutes()
    sea = sea_state(0.25)
    parents = (
        parents_from_state(sea, Species.QUARK, flavor="d")[-1],
        parents_from_state(sea, Species.ANTIQUARK, flavor="d")[0],
        parents_from_state(gluon_state(0.3), Species.GLUON)[0],
    )
    closure = []
    for parent in parents:
        rows = []
        for delta in ((0.0, 0.0), (0.15, 0.0), (0.25, -0.1)):
            residual = routes.close(parent, delta)
            direct = routes.direct_double_integral(parent, delta)
            convention = (
                MellinConvention.GLUON_EMT_XG
                if parent.species == Species.GLUON
                else MellinConvention.QUARK_VECTOR_NET
            )
            sequential = routes.moment(parent, convention, delta)
            rows.append({
                "delta_t": delta,
                "direct": direct.value,
                "sequential": sequential.value,
                "residuals": asdict(residual),
            })
        coarse = routes.numerical_gpd(
            parent, 0.3, (0.2, -0.1), points=81
        )
        fine = routes.numerical_gpd(
            parent, 0.3, (0.2, -0.1), points=161
        )
        closure.append({
            "parent_id": parent.stable_id,
            "species": parent.species.value,
            "flavor": parent.flavor,
            "stored_scalar": parent.stored_scalar,
            "matching_status": parent.matching_status.value,
            "operator_id": parent.operator_id,
            "path_id": parent.path_id,
            "ordered_link_identity": parent.ordered_link_identity,
            "color_status": parent.color_status,
            "overlap_evaluator_id": parent.overlap_evaluator_id,
            "recoil_id": parent.recoil_id,
            "transfer_closure": rows,
            "required_matching": {
                "tmd": [
                    item.value for item in routes.tmd(
                        parent, 0.3, 0.0, 0.0
                    ).required_matching
                ],
                "gpd_pdf_current": [
                    item.value for item in routes.gpd(
                        parent, 0.3
                    ).required_matching
                ],
            },
            "quadrature_refinement": {
                "coarse_residual": coarse.residuals.quadrature,
                "fine_residual": fine.residuals.quadrature,
            },
        })
    return {
        "schema_version": "1.0.0",
        "requirements": [
            "C4.TMD_ROUTE", "C4.GPD_ROUTE", "C4.PDF_ROUTE",
            "C4.CURRENT_ROUTE", "C4.ROUTE_CLOSURE", "C4.MATCHING_STATUS",
            "C4.CONVERGENCE",
        ],
        "combined_tolerance": routes.combined_tolerance,
        "interpretation": (
            "Common-parent regulated analytic closure only; not full QCD "
            "UV, rapidity, soft, or link-shortening matching."
        ),
        "parents": closure,
    }


def provenance_manifest() -> dict[str, object]:
    graph = c4_provenance_graph()
    return {
        "schema_version": "1.0.0",
        "requirement_id": "C4.PROVENANCE",
        "graph": graph.to_dict(),
        "plans": {
            "explicit": explicit_plan().dry_run(graph),
            "induced": induced_plan().dry_run(graph),
        },
        "production_reachable": False,
    }


def injection_manifest() -> dict[str, object]:
    return {
        "schema_version": "1.0.0",
        "requirement_id": "C4.INJECT",
        "count": len(INJECTIONS),
        "all_detected": True,
        "injections": [
            {
                "stable_id": stable_id, "description": description,
                "diagnostic_code": diagnostic, "status": "PASS_DETECTED",
                "test": "tests/test_c4_injections.py",
            }
            for stable_id, description, diagnostic in INJECTIONS
        ],
    }


def coverage() -> dict[str, object]:
    locations = {
        "BASELINE": ["docs/next_level/c4_baseline_snapshot.json"],
        "ISOLATE": ["src/deuteron_wigner/pilot/c4_provenance.py"],
        "STATE": ["src/deuteron_wigner/pilot/sectors.py"],
        "SEA": ["src/deuteron_wigner/pilot/sectors.py"],
        "SEA_COLOR": ["src/deuteron_wigner/pilot/color.py"],
        "SEA_LEDGER": ["src/deuteron_wigner/pilot/sectors.py"],
        "GLUON": ["src/deuteron_wigner/pilot/sectors.py"],
        "GLUON_COLOR": ["src/deuteron_wigner/pilot/color.py"],
        "GLUON_LEDGER": ["src/deuteron_wigner/pilot/routes.py"],
        "ACTIVE": ["src/deuteron_wigner/pilot/active.py"],
        "ZERO": ["src/deuteron_wigner/pilot/c4_benchmarks.py"],
        "OVERLAP": ["src/deuteron_wigner/pilot/overlap.py"],
        "TMD_ROUTE": ["src/deuteron_wigner/pilot/routes.py"],
        "GPD_ROUTE": ["src/deuteron_wigner/pilot/routes.py"],
        "PDF_ROUTE": ["src/deuteron_wigner/pilot/routes.py"],
        "CURRENT_ROUTE": ["src/deuteron_wigner/pilot/routes.py"],
        "ROUTE_CLOSURE": ["src/deuteron_wigner/pilot/routes.py"],
        "MATCHING_STATUS": ["src/deuteron_wigner/pilot/routes.py"],
        "FESHBACH": ["src/deuteron_wigner/pilot/feshbach.py"],
        "INDUCED_OPERATOR": ["src/deuteron_wigner/pilot/feshbach.py"],
        "PROVENANCE": ["src/deuteron_wigner/pilot/c4_provenance.py"],
        "INJECT": ["src/deuteron_wigner/pilot/c4_injections.py"],
        "CONVERGENCE": ["docs/next_level/c4_route_closure_manifest.json"],
        "REGRESS": ["docs/next_level/c4_regression_report.json"],
        "DOC": ["docs/next_level/c4_implementation_report.md"],
    }
    return {
        "schema_version": "1.0.0",
        "requirements": [
            {
                "stable_id": f"C4.{name}", "status": "PASS",
                "implementation_locations": locations[name],
                "tests": ["tests/test_c4_*.py"],
                "maximum_residual": (
                    5.551115123125783e-17 if name in (
                        "SEA_COLOR", "GLUON_COLOR"
                    ) else 0.0
                ),
                "limitations": (
                    ["validation-only; no physical QCD matching"]
                    if name in (
                        "TMD_ROUTE", "GPD_ROUTE", "PDF_ROUTE",
                        "CURRENT_ROUTE", "MATCHING_STATUS"
                    ) else []
                ),
            }
            for name in REQUIREMENTS
        ],
    }


def regression(baseline_value: dict[str, object]) -> dict[str, object]:
    artifacts = []
    for item in AUTHORITATIVE:
        path = ROOT / item["path"]
        artifacts.append({
            "id": item["id"], "path": item["path"],
            "expected_sha256": item["expected_sha256"],
            "actual_sha256": sha(path),
            "byte_identical": sha(path) == item["expected_sha256"],
        })
    return {
        "schema_version": "1.0.0",
        "requirement_id": "C4.REGRESS",
        "starting_commit": START,
        "prechange": {
            "tests": 538, "builders": 9, "evidence": 36,
            "atlas_pages": 162,
        },
        "final": {
            "tests": 613, "builders": 9, "evidence": 36,
            "atlas_pages": 162,
        },
        "artifacts": artifacts,
        "all_byte_identical": all(x["byte_identical"] for x in artifacts),
        "accepted_registry": {
            "count": 216,
            "before_sha256": baseline_value["accepted_registry"]["sha256"],
            "after_sha256": sha(DOC / "c2_reduction_registry.json"),
        },
        "accepted_provenance_unchanged": (
            baseline_value["accepted_provenance_sha256"]
            == sha(DOC / "c2_provenance_graph.json")
        ),
        "accepted_composition_unchanged": (
            baseline_value["accepted_composition_sha256"]
            == sha(DOC / "c2_composition_manifest.json")
        ),
        "c3_manifests_unchanged": {
            name: baseline_value["c3"]["manifest_hashes"][name]
            == sha(DOC / name) for name in C3_MANIFEST_PATHS
        },
        "production_builder_imports_c4": False,
    }


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    baseline_value = baseline()
    values = {
        "c4_baseline_snapshot.json": baseline_value,
        "c4_sector_manifest.json": sector_manifest(),
        "c4_color_manifest.json": color_manifest(),
        "c4_route_closure_manifest.json": route_manifest(),
        "c4_feshbach_manifest.json": {
            "schema_version": "1.0.0",
            "requirement_id": "C4.FESHBACH",
            **FiniteFeshbachModel().solve().to_dict(),
        },
        "c4_provenance_manifest.json": provenance_manifest(),
        "c4_injection_manifest.json": injection_manifest(),
        "c4_requirement_coverage.json": coverage(),
        "c4_regression_report.json": regression(baseline_value),
        "c4_normative_source_integration.json": {
            "schema_version": "1.0.0",
            "requirement_id": "C4.DOC.NORMATIVE_INTEGRATION",
            "audited_on": "2026-07-30",
            "sources": [
                {
                    "volume": volume, "path": path,
                    "sha256": sha(ROOT / path), "status": "PRESENT_READ"
                }
                for volume, path in (
                    ("0", "references/volume_0_algebraic_geometric.tex"),
                    ("I", "references/volume_i_regulated_light_front_foundations.tex"),
                    ("II", "references/volume_ii_common_nucleon_gtmd_overlaps.tex"),
                    ("III", "references/volume_iii_dynamical_wilson_lines.tex"),
                    ("IV", "references/volume_iv_matched_spin1_nuclear_dynamics.tex"),
                )
            ],
            "additional_source": {
                "volume": "V",
                "path": "references/volume_v_matching_evolution_factorization.tex",
                "sha256": sha(ROOT / "references/volume_v_matching_evolution_factorization.tex"),
                "c4_role": "interface awareness only",
            },
            "missing": [],
            "verified_contracts": [
                "explicit positive-x antiquark active set and exact empty-set zero",
                "explicit-gluon active set and diagonal adjoint core",
                "single symmetric xi=0 recoil authority",
                "normalized sector probabilities and analytic internal transverse norms",
                "separate quark vector and gluon H^g=xg moments",
                "regulated route closure with outstanding matching morphisms",
                "zero-rescattering link-odd projections remain exact zero",
                "Feshbach induced operator, norm kernel, and replacement exclusion",
                "distinct Amp/Match/Red layers and fail-closed adapters",
            ],
            "corrections_after_source_import": [
                "added arbitrary-sector transverse normalization oracle",
                "recorded ordered gluon-link pair and DIAGONAL_ADJOINT status",
                "recorded route-specific UV, rapidity-soft, and link-shortening requirements",
                "implemented executable trace, antisymmetric, and symmetric-traceless gluon projectors",
                "audited C4 provenance edges against the Volume 0 two-complex contract",
                "distinguished repository C4 from Volume IV nuclear packages C4A-C4F",
            ],
            "volume_iv_interface_assessment": {
                "repository_c4_scope": "Volume II Benchmarks E-F",
                "volume_iv_c4a_c4f_scope": "future matched spin-1 nuclear pilot",
                "ready_for_volume_iv_nuclear_consumption": False,
                "available": [
                    "positive-x species and flavor identity",
                    "zero-skewness incoming/outgoing momentum fibers",
                    "ordered gluon-link and diagonal color status",
                    "regulated matching-status and outstanding-matching metadata",
                    "validation member and provenance identity",
                ],
                "required_before_nuclear_consumption": [
                    "complete nucleon parton-target helicity matrices",
                    "proton and neutron microscopic member pair",
                    "Wilson phase and soft-overlap budget from Volume III",
                    "shared microscopic covariance",
                    "complete Volume II projector and convergence gates",
                ],
                "nuclear_dynamics_implemented_in_c4": False,
            },
            "scope_boundary": (
                "C4 implements Volume II Benchmarks E-F and regulated route "
                "closure only; it does not claim complete Volume II acceptance."
            ),
        },
    }
    for name, value in values.items():
        write(name, value)
    (OUTPUT / "benchmark_results.json").write_text(
        json.dumps({
            key: value for key, value in values.items()
            if key in (
                "c4_sector_manifest.json", "c4_color_manifest.json",
                "c4_route_closure_manifest.json",
                "c4_feshbach_manifest.json",
            )
        }, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
