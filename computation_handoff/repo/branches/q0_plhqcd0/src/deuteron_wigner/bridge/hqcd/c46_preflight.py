"""C46 fail-closed audit for physical q/qg action projection.

C45 intentionally supplied a one-particle library.  This audit distinguishes
that valid result from the additional x-scaled, centre-of-mass and action
normalization contracts needed before it can define regulator-identical
many-body QCD matrices.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STATUS = "C46_PHYSICAL_BASIS_ASSEMBLY_INCOMPLETE"
BASELINE = "C45_SOURCE_DERIVED_MODE_PROJECTION_READY"


def _read(name: str) -> dict:
    return json.loads((ROOT / "docs/next_level" / name).read_text())


def source_to_matrix_audit() -> dict:
    c43_projection = _read("c43_finite_basis_projection_contract.json")
    c43_modes = _read("c43_mode_expansion_contract.json")
    c45_ho = _read("c45_transverse_ho_contract.json")
    c45_interface = _read("c45_c46_projection_interface.json")
    c45_kernel = _read("c45_spinor_polarization_overlap.json")
    c45_zero = _read("c45_zero_mode_projection_contract.json")
    c45_matrix = _read("c45_projection_contract_matrix.json")
    rows = {x["row"]: x["status"] for x in c45_matrix["rows"]}
    missing = [
        {
            "id": "C46.MULTIBODY_X_SCALED_HO",
            "source_requirement": "1311.2980v1 Eq. (7): x-dependent transverse argument p_perp/sqrt(x) and normalization",
            "observed": c45_ho["momentum_formula"],
            "blocking_reason": "The C45 evaluator is explicitly a one-particle b-basis with no x argument, so it cannot supply the physical qg product/CM overlap required at unequal longitudinal partitions.",
            "required_correction": "Source-derive and validate x-scaled momentum and coordinate HO modes plus their unequal-x overlap functional before forming a qg basis.",
        },
        {
            "id": "C46.CENTER_OF_MASS_PROJECTOR",
            "source_requirement": "C43 physical resolution plan: zero CM quantum; 1311.2980v1 discussion following Eqs. (10)-(12)",
            "observed": c45_interface["selection_rules"],
            "blocking_reason": "C45 delegates the centre-of-mass condition to C46 but supplies neither a source-derived many-body CM operator nor a normalized zero-CM isometry.",
            "required_correction": "Derive a finite, x-scaled BLFQ CM operator and its zero-CM projector/isometry for every qg longitudinal partition.",
        },
        {
            "id": "C46.FREE_OPERATOR_REPRESENTATION",
            "source_requirement": "C46 requires C43 to select P^- or invariant-mass-squared before projection",
            "observed": c43_projection["interfaces"],
            "blocking_reason": "C43 records Hq/Hqg as interfaces only and does not choose a projected free-operator representation, normalization, or symbolic L factorization.",
            "required_correction": "Freeze the C43-to-finite-basis free P^- or M^2 projection convention, including field normalization and L treatment.",
        },
        {
            "id": "C46.CANONICAL_VERTEX_MODE_KERNEL",
            "source_requirement": "SB canonical term with full finite-volume mode expansion and C45 source-to-basis kernel",
            "observed": c45_kernel["scope"],
            "blocking_reason": "The committed C45 kernel is a frozen 2x2x2 local numerator test array and explicitly omits longitudinal delta, SU(3), and physical multi-mode overlap normalization; it is not an all-mode q->qg matrix-element functional.",
            "required_correction": "Derive an x-scaled, finite-volume three-mode canonical matrix-element functional and independently validate it before assembling V_qg<-q.",
        },
        {
            "id": "C46.BOUNDARY_GLOBAL_ZERO_MODE",
            "source_requirement": "C43 retained residual boundary and zero-mode policy applied to the C45 open-color module",
            "observed": {"C43_global": _read("c43_zero_mode_contract.json")["rows"]["global_color"], "C45_global": c45_zero["statuses"]["global_color_gauss"]},
            "blocking_reason": "The C45 record retains the global color label externally and defers Wilson-endpoint cancellation, but no local finite-basis boundary/zero-mode matrix functional is supplied. C46 cannot silently set it to zero before the projection is derived.",
            "required_correction": "Derive the local action-owned residual-boundary/zero-mode operator and reconcile it with the open-color external-module constraint.",
        },
    ]
    return {
        "status": STATUS,
        "baseline_status": BASELINE,
        "baseline_checks": {
            "C43_mode_status": c43_modes["status"],
            "C43_projection_status": c43_projection["status"],
            "C45_contract_rows": rows,
            "C45_interpretation": "one-particle mode library remains valid; its C46 assembly interface is not sufficient for regulator-identical q/qg matrices",
        },
        "missing_physical_matrix_element_contracts": missing,
        "prohibited_response": "Do not use C40 toy arrays, diagonal expectations, fitted textures, or a full 3x8 product space to fill these gaps.",
        "decision": "No physical q/qg basis or local QCD matrix is generated. The first blocker is physical many-body basis assembly.",
        "next": "C47/BASIS1 — x-scaled BLFQ many-body/CM projection and finite-volume vertex normalization closure",
    }


def validate_source_to_matrix_audit(value: dict) -> bool:
    expected = source_to_matrix_audit()
    return value == expected and value["status"] == STATUS and len(value["missing_physical_matrix_element_contracts"]) == 5


def assert_physical_basis_assembly_incomplete() -> dict:
    audit = source_to_matrix_audit()
    assert validate_source_to_matrix_audit(audit)
    assert audit["baseline_checks"]["C45_contract_rows"] == {
        "LONGITUDINAL_CELL_AND_MEASURE": "SOURCE_COMPLETE_EXECUTABLE",
        "TRANSVERSE_2D_HO_AND_PHASE": "SOURCE_COMPLETE_EXECUTABLE",
        "SPINOR_POLARIZATION_OVERLAP": "SOURCE_COMPLETE_EXECUTABLE",
        "GLOBAL_COLOR_ZERO_MODE_PROJECTION": "SOURCE_COMPLETE_EXECUTABLE",
    }
    return audit
