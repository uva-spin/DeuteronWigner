"""Truthful C400.S2 diagnostic forward-path status.

This wrapper deliberately keeps the executable C144 fixture smoke path separate
from the not-yet-executable C396 19-coordinate Hamiltonian family.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Mapping

from .coordinate_bindings import binding_summary, coordinate_binding_inventory
from .derivative_integrity import audit_all_c144_derivatives
from .state_identity import UNPROJECTED_STATUS, solve_c144_diagnostic
from .status import status_supersession_record


def diagnostic_forward_integrity_record(
    *,
    resolution: str = "K9",
    derivative_step: float = 1.0e-5,
    solver_tolerance: float = 1.0e-9,
    execute_numerical_smoke: bool = True,
    precomputed_spectrum: Any | None = None,
    precomputed_derivative_audit: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    spectrum = precomputed_spectrum if precomputed_spectrum is not None else (
        solve_c144_diagnostic(
            resolution=resolution,
            k=2,
            solver_tolerance=solver_tolerance,
            projector=None,
        )
        if execute_numerical_smoke
        else None
    )
    derivative_audit = precomputed_derivative_audit if precomputed_derivative_audit is not None else (
        audit_all_c144_derivatives(resolutions=(resolution,), step=derivative_step)
        if execute_numerical_smoke
        else {
            "schema": "C400-S2-C144-DERIVATIVE-INTEGRITY-AUDIT-V1",
            "status": "NOT_EXECUTED_IN_THIS_RECORD",
            "physical_derivative_claim": False,
            "C396_derivative_claim": False,
        }
    )
    inventory = coordinate_binding_inventory()
    state_rows = tuple(
        {
            "state_id": pair.state.state_id,
            "identity_status": pair.identity_status,
            "sector": pair.state.sector,
            "eigenvalue": pair.state.eigenvalue,
            "eigenvalue_residual": pair.eigenvalue_residual,
            "degeneracy_gap": pair.degeneracy_gap,
            "degeneracy_status": pair.degeneracy_status,
            "projector_owner": pair.projector_owner,
            "quantum_number_evidence": pair.quantum_number_evidence,
            "vector_sha256_incidental": pair.vector_sha256_incidental,
        }
        for pair in (spectrum.eigenpairs if spectrum is not None else ())
    )
    return {
        "schema": "C400-S2-DIAGNOSTIC-FORWARD-INTEGRITY-V1",
        "status": "PARTIAL_FORWARD_MAP",
        "status_supersession": status_supersession_record(),
        "executable_path": {
            "operator_family": "C144_DIAGNOSTIC_FIXTURE_11_COORDINATES",
            "resolution": resolution,
            "execution_status": "EXECUTED" if spectrum is not None else "NOT_EXECUTED_IN_THIS_RECORD",
            "parameter_root": spectrum.parameter_root if spectrum is not None else None,
            "matrix_shape": spectrum.matrix_shape if spectrum is not None else None,
            "matrix_nnz": spectrum.matrix_nnz if spectrum is not None else None,
            "hermiticity_residual": spectrum.hermiticity_residual if spectrum is not None else None,
            "solver_tolerance": spectrum.solver_tolerance if spectrum is not None else solver_tolerance,
            "state_identity": UNPROJECTED_STATUS,
            "states": state_rows,
            "derivative_audit": derivative_audit,
            "physical": False,
        },
        "C396_family": {
            "coordinates_per_resolution": inventory["coordinates_per_resolution"],
            "resolutions": inventory["resolutions"],
            "complete_numerical_apply_paths": inventory["complete_numerical_apply_paths"],
            "forward_map_ready": False,
            "binding_summary": binding_summary(),
        },
        "state_to_current_observable_path_ready": False,
        "sector_qualified_deuteron_state_ready": False,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
        "physical_activation_ready": False,
    }


__all__ = ["diagnostic_forward_integrity_record"]
