"""C401 overlay of the C400.S2 C396 coordinate-binding inventory."""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping

from deuteron_wigner.bridge.c400_s2_corrective.coordinate_bindings import (
    coordinate_binding_inventory as c400_coordinate_binding_inventory,
)

from .basis import RESOLUTION_LABELS, content_root, historical_c128_partition_defect_audit
from .operators import D_DELTA_MU_G_SQ, D_MU_Q_SQ, mass_direction_operator_inventory

_STATUS = "C396_FIRST_SIX_K_LOCAL_NUMERICAL_BINDINGS_READY_DIAGNOSTIC_ONLY"


def coordinate_reduction_record() -> dict[str, Any]:
    payload = {
        "schema": "C401-C396-COORDINATE-REDUCTION-V1",
        "status": _STATUS,
        "raw_slots_per_resolution": 19,
        "resolutions": RESOLUTION_LABELS,
        "reclassification": (
            {
                "raw_id": "ct_mass",
                "implementation_coordinate": "mu_q_sq",
                "new_role": "IDENTIFIED_RENORMALIZED_MASS_SQUARED_DIRECTION",
                "numerical_matrix_candidate": True,
                "numerical_apply_ready": True,
            },
            {
                "raw_id": "ct_vacuum_energy",
                "new_role": "VACUUM_ONLY_OUTSIDE_RETAINED_Q_QG_DIRECT_SUM",
                "numerical_matrix_candidate": False,
                "projector_certificate_pending": True,
            },
            {
                "raw_id": "ct_gluon_mass",
                "implementation_coordinate": "delta_mu_g_sq",
                "new_role": "K_LOCAL_GLUON_ONE_BODY_MASS_SQUARED_DIRECTION",
                "numerical_matrix_candidate": True,
                "numerical_apply_ready": True,
            },
            {
                "raw_id": "ct_sector",
                "new_role": "MATRIX_DIRECTION_OWNER_NORMALIZATION_REQUIRED",
                "numerical_matrix_candidate": True,
                "numerical_apply_ready": False,
            },
            {
                "raw_id": "ct_boundary",
                "new_role": "NONMATRIX_DOMAIN_OR_BOUNDARY_PARAMETER",
                "numerical_matrix_candidate": False,
            },
            {
                "raw_id": "ct_truncation",
                "new_role": "NONMATRIX_TRUNCATION_DISCREPANCY",
                "numerical_matrix_candidate": False,
            },
            {
                "raw_id_pattern": "null_1...null_9",
                "new_role": "SOURCE_OWNER_CLASSIFICATION_REQUIRED",
                "count": 9,
                "numerical_matrix_candidate": "UNRESOLVED",
            },
            {
                "raw_id_pattern": "c_C117_1...c_C117_4",
                "new_role": "SOURCE_QUALIFIED_MATRIX_DIRECTION_APPLY_REQUIRED",
                "count": 4,
                "numerical_matrix_candidate": True,
            },
        ),
        "maximum_candidate_matrix_dimension_per_resolution": 16,
        "candidate_dimension_is_rank": False,
        "maximum_candidate_matrix_dimension_status": "PROVISIONAL_UPPER_BOUND_NOT_RANK",
        "numerically_ready_matrix_directions_per_resolution": 2,
        "unresolved_candidate_matrix_directions_per_resolution": 14,
        "complete_K_local_apply_rows": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


def c396_binding_inventory_with_c401_mass_directions() -> Mapping[str, Any]:
    previous = deepcopy(c400_coordinate_binding_inventory())
    rows = [deepcopy(row) for row in previous["rows"]]
    operator_inventory = mass_direction_operator_inventory()
    ready = {
        (row["resolution"], row["raw_C396_coordinate"]): row
        for row in operator_inventory["rows"]
    }
    changed_rows = 0
    ready_rows = 0
    for row in rows:
        key = (row["resolution"], row["coordinate_id"])
        if key in ready:
            operator = ready[key]
            direction = (
                D_MU_Q_SQ if row["coordinate_id"] == "ct_mass" else D_DELTA_MU_G_SQ
            )
            row.update(
                {
                    "C401_role": (
                        "IDENTIFIED_RENORMALIZED_MASS_SQUARED_DIRECTION"
                        if direction == D_MU_Q_SQ
                        else "K_LOCAL_GLUON_ONE_BODY_MASS_SQUARED_DIRECTION"
                    ),
                    "implementation_coordinate_id": operator["implementation_coordinate"],
                    "numerical_apply_status": (
                        "K_LOCAL_SPARSE_AND_MATRIX_FREE_READY_DIAGNOSTIC_ONLY"
                    ),
                    "numerical_apply_path": operator["matrix_free_apply_path"],
                    "sparse_apply_path": operator["sparse_apply_path"],
                    "derivative_status": "C401_SOURCE_FORMULA_AND_FINITE_DIFFERENCE_VERIFIED",
                    "smallest_missing_object": "",
                    "C128_historical_fraction_defect_superseded": True,
                    "physical": False,
                    "selected": False,
                    "zeroed": False,
                }
            )
            changed_rows += 1
            ready_rows += 1
        elif row["coordinate_id"] == "ct_vacuum_energy":
            row.update(
                {
                    "C401_role": "VACUUM_ONLY_OUTSIDE_RETAINED_Q_QG_DIRECT_SUM",
                    "numerical_apply_status": "NONMATRIX_VACUUM_DIRECTION_IN_RETAINED_Q_QG_SPACE",
                    "smallest_missing_object": (
                        "numerical deuteron-sector projector certificate P_d P_0 = 0"
                    ),
                }
            )
            changed_rows += 1
        elif row["coordinate_id"] == "ct_boundary":
            row.update(
                {
                    "C401_role": "NONMATRIX_DOMAIN_OR_BOUNDARY_PARAMETER",
                    "numerical_apply_status": "NONMATRIX_DOMAIN_PARAMETER",
                }
            )
            changed_rows += 1
        elif row["coordinate_id"] == "ct_truncation":
            row.update(
                {
                    "C401_role": "NONMATRIX_TRUNCATION_DISCREPANCY",
                    "numerical_apply_status": "NONMATRIX_OBSERVABLE_DISCREPANCY",
                }
            )
            changed_rows += 1
    payload = {
        "schema": "C401-C396-COORDINATE-BINDING-INVENTORY-V1",
        "status": _STATUS,
        "supersedes_inventory_schema": previous["schema"],
        "total_rows": len(rows),
        "rows": tuple(rows),
        "changed_rows": changed_rows,
        "complete_numerical_apply_paths": ready_rows,
        "expected_complete_numerical_apply_paths": 6,
        "coordinate_reduction": coordinate_reduction_record(),
        "historical_C128_partition_defect": historical_c128_partition_defect_audit(),
        "C396_19_coordinate_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }
    return {**payload, "root": content_root(payload)}


def binding_update_summary() -> Mapping[str, Any]:
    inventory = c396_binding_inventory_with_c401_mass_directions()
    payload = {
        "schema": "C401-C396-BINDING-UPDATE-SUMMARY-V1",
        "status": _STATUS,
        "previous_complete_numerical_apply_paths": 0,
        "current_complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
        "total_symbolic_rows": inventory["total_rows"],
        "first_completed_directions": (
            "D_mu_q_sq at K9/K11/K13",
            "D_delta_mu_g_sq at K9/K11/K13",
        ),
        "remaining_candidate_matrix_directions_per_resolution": 14,
        "next_operator_frontier": (
            "ct_sector owner normalization, then four C117 insertions, then source-null classification"
        ),
        "full_C396_forward_map_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "activation_gate_status": "NOT_READY",
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "coordinate_reduction_record",
    "c396_binding_inventory_with_c401_mass_directions",
    "binding_update_summary",
]
