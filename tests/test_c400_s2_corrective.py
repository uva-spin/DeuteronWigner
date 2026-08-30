"""Adversarial acceptance tests for the C400.S2 corrective implementation lock."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

import numpy as np
import pytest

from deuteron_wigner.lf_current import current_from_form_factors
from deuteron_wigner.bridge.c400_s2_corrective.current_adapter import (
    CurrentAdapterError,
    CurrentConventions,
    CurrentRequest,
    CurrentRoute,
    UnifiedCurrentAdapter,
)
from deuteron_wigner.bridge.c400_s2_corrective.coordinate_bindings import (
    binding_summary,
    coordinate_binding_inventory,
)
from deuteron_wigner.bridge.c400_s2_corrective.current_compare import (
    compare_current_requests,
)
from deuteron_wigner.bridge.c400_s2_corrective.derivative_integrity import (
    DerivativeIntegrityError,
    audit_derivative,
)
from deuteron_wigner.bridge.c400_s2_corrective.forward_integrity import (
    diagnostic_forward_integrity_record,
)
from deuteron_wigner.bridge.c400_s2_corrective.replay_integrity import (
    compare_eigensystems,
    dependency_failure_record,
    semantic_replay_record,
)
from deuteron_wigner.bridge.c400_s2_corrective.state_identity import (
    PROJECTED_RITZ_STATUS,
    PROJECTED_STATUS,
    UNPROJECTED_STATUS,
    SectorProjector,
    StateIdentityError,
    derivative_step_tolerance_scan,
    solve_c144_diagnostic,
)
from deuteron_wigner.bridge.c400_s2_corrective.status import (
    C144_DIAGNOSTIC_STATUS,
    C396_BINDING_STATUS,
    FIT_STATUS,
    RANK_STATUS,
    SECTOR_STATUS,
    status_supersession_record,
)
from deuteron_wigner.bridge.c400_s2_corrective.tracking import (
    StateRecord,
    StateTracker,
    TrackingPolicy,
)


def _state(state_id: str, eigenvalue: float, vector, sector=(("J", "1"),)) -> StateRecord:
    return StateRecord(state_id, sector, eigenvalue, np.asarray(vector, dtype=np.complex128))


def _lf_conventions() -> CurrentConventions:
    return CurrentConventions(
        "Drell-Yan q+=0",
        "Q2=-(q_mu q^mu)>0",
        "J+",
        "I=J+/(2P+)",
        ("I++", "I+0", "I+-", "I00"),
        (1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j),
        "GC,GM,GQ Carlson-Ji spin-1 normalization",
        "GeV",
        "GeV",
        "omit_I00",
        "EXPLICIT_CALLER_BOUND",
        "EXPLICIT_CALLER_BOUND",
    )


def _lps_conventions() -> CurrentConventions:
    return CurrentConventions(
        "longitudinal Breit",
        "Q2=-(q_mu q^mu)>0",
        "J+/-/Jx",
        "LPS unnormalized free current",
        ("I++", "I+0", "I+-", "I00"),
        (1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j),
        "GC,GM,GQ LPS Eq.21 normalization",
        "GeV",
        "GeV",
        "LPS_EQ21",
        "EXPLICIT_CALLER_BOUND",
        "EXPLICIT_CALLER_BOUND",
    )


def _matched_current_requests(*, q: float = 0.4, mass: float = 1.8756, state_id: str = "same-state"):
    tau = q**2 / (4.0 * mass**2)
    expected = np.asarray((0.7, 1.3, 12.0), dtype=float)
    lf_current = current_from_form_factors(
        eta=tau,
        charge=expected[0],
        magnetic=expected[1],
        quadrupole=expected[2],
    )
    lf_request = CurrentRequest(
        CurrentRoute.LIGHT_FRONT,
        _lf_conventions(),
        lf_current,
        tau,
        q,
        mass,
        state_id,
    )
    zeta = 1.0 / (np.sqrt(2.0) * mass * np.sqrt(1.0 + tau))
    lps_current = np.zeros((4, 3, 3), dtype=np.complex128)
    lps_current[0, 0, 0] = (expected[0] - 2.0 * tau * expected[2] / 3.0) / zeta
    lps_current[0, 1, 1] = (expected[0] + 4.0 * tau * expected[2] / 3.0) / zeta
    lps_current[2, 0, 1] = np.sqrt(tau) * expected[1] / zeta
    lps_current[2, 1, 0] = -np.sqrt(tau) * expected[1] / zeta
    lps_request = CurrentRequest(
        CurrentRoute.COVARIANT_LPS,
        _lps_conventions(),
        lps_current,
        tau,
        q,
        mass,
        state_id,
    )
    return expected, lf_request, lps_request


def test_status_supersession_is_truthful_and_keeps_historical_record_immutable():
    record = status_supersession_record()
    assert record["historical_record"]["preserved_immutable"] is True
    assert record["superseding_interpretation"]["C144_diagnostic_smoke_path"] == C144_DIAGNOSTIC_STATUS
    assert record["superseding_interpretation"]["C396_forward_map"] == C396_BINDING_STATUS
    assert record["superseding_interpretation"]["sector_identity"] == SECTOR_STATUS
    assert record["superseding_interpretation"]["rank"] == RANK_STATUS
    assert record["superseding_interpretation"]["physical_fit"] == FIT_STATUS
    assert record["superseding_interpretation"]["physical_activation_ready"] is False


def test_c396_binding_ledger_is_complete_but_has_no_c144_proxy_or_numeric_claim():
    inventory = coordinate_binding_inventory()
    assert inventory["resolutions"] == ("K9", "K11", "K13")
    assert inventory["coordinates_per_resolution"] == 19
    assert inventory["total_rows"] == 57
    assert inventory["complete_numerical_apply_paths"] == 0
    assert inventory["C396_19_coordinate_forward_map_ready"] is False
    assert inventory["C144_proxy_substitution_allowed"] is False
    for resolution in inventory["resolutions"]:
        rows = [row for row in inventory["rows"] if row["resolution"] == resolution]
        assert len(rows) == 19
        assert len({row["coordinate_id"] for row in rows}) == 19
        assert all(row["c144_proxy_forbidden"] for row in rows)
        assert all(not row["selected"] and not row["zeroed"] and not row["physical"] for row in rows)
        assert all(row["smallest_missing_object"] for row in rows)
    assert binding_summary()["status"] == C396_BINDING_STATUS


def test_resolution_semantics_preserve_fractional_K_and_expose_bho_unit_conflict():
    inventory = coordinate_binding_inventory()
    semantics = inventory["resolution_semantics"]
    assert [semantics[key]["K2"] for key in ("K9", "K11", "K13")] == [9, 11, 13]
    assert [semantics[key]["K_fraction"] for key in ("K9", "K11", "K13")] == ["9/2", "11/2", "13/2"]
    assert all("CONFLICT" in semantics[key]["unit_status"] for key in semantics)
    assert inventory["basis_unit_conflict_unresolved"] is True


@pytest.mark.parametrize("coordinate", ("phi_coupling", "eta_2"))
def test_versioned_derivative_repairs_known_historical_mismatches(coordinate):
    audit = audit_derivative("K9", coordinate, step=1.0e-5)
    assert audit.corrected_derivative_verified is True
    assert audit.response_status == "VERIFIED_C400_DIAGNOSTIC_DERIVATIVE"
    assert audit.historical_derivative_matches is False
    assert audit.historical_vs_corrected.frobenius_norm > 1.0
    assert audit.physical_derivative_claim is False
    assert audit.C396_derivative_claim is False


@pytest.mark.parametrize("coordinate", tuple(f"eta_{index}" for index in range(3, 9)))
def test_zero_response_fixture_coordinates_are_unbound_not_physically_irrelevant(coordinate):
    audit = audit_derivative("K9", coordinate)
    assert audit.response_status == "NUMERICALLY_UNBOUND_IN_C144_FIXTURE_API"
    assert audit.corrected_nnz == 0
    assert audit.finite_difference_nnz == 0
    with pytest.raises(DerivativeIntegrityError):
        audit_derivative("K9", coordinate + "-unknown")


def test_unprojected_smoke_state_has_no_deuteron_quantum_number_claim():
    spectrum = solve_c144_diagnostic("K9", k=2, solver_tolerance=1.0e-8)
    assert spectrum.projected is False
    assert spectrum.physical_state_selected is False
    assert spectrum.C396_19_coordinate_state is False
    for pair in spectrum.eigenpairs:
        assert pair.identity_status == UNPROJECTED_STATUS
        assert pair.requested_sector is None
        assert pair.projector_owner is None
        assert pair.quantum_number_evidence.startswith("none")
        assert pair.state.sector == (("basis_scope", "C144_UNPROJECTED_FIXTURE"),)
        assert pair.eigenvalue_residual < 1.0e-6


def test_rank_one_projector_without_hamiltonian_invariance_is_ritz_only():
    dimension = 1350
    matrix = np.zeros((dimension, dimension), dtype=np.complex128)
    matrix[0, 0] = 1.0
    projector = SectorProjector("SYNTHETIC_TEST_PROJECTOR", (("test-sector", "one"),), matrix)
    spectrum = solve_c144_diagnostic("K9", k=1, projector=projector)
    pair = spectrum.eigenpairs[0]
    assert pair.identity_status == PROJECTED_RITZ_STATUS
    assert pair.identity_status != PROJECTED_STATUS
    assert pair.spectral_status == PROJECTED_RITZ_STATUS
    assert pair.projector_owner == "SYNTHETIC_TEST_PROJECTOR"
    assert pair.projector_membership_verified is True
    assert pair.full_eigenstate_verified is False
    assert spectrum.projector_invariant_subspace is False
    assert spectrum.projector_relative_invariance_residual > projector.hamiltonian_invariance_tolerance
    assert pair.relative_eigenvalue_residual > max(100.0 * spectrum.solver_tolerance, 1.0e-10)
    assert "membership only" in pair.quantum_number_evidence
    assert pair.projection_norm == pytest.approx(1.0)
    assert pair.projection_leakage == pytest.approx(0.0)
    assert pair.projector_residual == pytest.approx(0.0)
    with pytest.raises(StateIdentityError):
        SectorProjector("bad", (("x", "y"),), np.asarray([[1.0, 1.0], [0.0, 0.0]]))
    with pytest.raises(StateIdentityError):
        SectorProjector(
            "bad tolerance",
            (("x", "y"),),
            np.eye(2),
            hamiltonian_invariance_tolerance=0.0,
        )


def test_tracker_preserves_surplus_status_and_ignores_cross_sector_energy_crossings():
    policy = TrackingPolicy(overlap_minimum=0.5, degeneracy_gap=0.1, assignment_tie_tolerance=1e-10)
    tracker = StateTracker(policy)
    rectangular = tracker.match(
        (_state("a", 0.0, (1, 0)),),
        (_state("a-now", 0.0, (1, 0)), _state("surplus", 0.05, (0, 1))),
    )
    assert rectangular.surplus_current_state_ids == ("surplus",)
    assert rectangular.individual_identity_status["surplus"] == "SURPLUS_UNMATCHED"
    diagnostic = rectangular.subspace_diagnostics[("a-now", "surplus")]
    assert diagnostic.rectangular is True
    assert diagnostic.old_projector.shape == diagnostic.current_projector.shape == (2, 2)
    assert diagnostic.aligned_current_basis is None

    previous = (
        _state("J1-old", 0.0, (1, 0), (("J", "1"),)),
        _state("J2-old", 1.0, (0, 1), (("J", "2"),)),
    )
    current = (
        _state("J1-new", 2.0, (1, 0), (("J", "1"),)),
        _state("J2-new", -1.0, (0, 1), (("J", "2"),)),
    )
    crossing = tracker.match(previous, current)
    assert crossing.assignments == (("J1-old", "J1-new"), ("J2-old", "J2-new"))
    assert crossing.swap_detected is False
    assert crossing.swap_sectors == ()


def test_tracker_uses_complete_assignment_objective_for_ambiguity():
    tracker = StateTracker(TrackingPolicy(assignment_tie_tolerance=1.0e-12))
    overlap = np.asarray([[0.9, 0.8], [0.8, 0.7]])
    rows, columns, best, second, ambiguous = tracker._assignment_with_ambiguity(overlap)
    assert set(zip(rows.tolist(), columns.tolist())) in ({(0, 0), (1, 1)}, {(0, 1), (1, 0)})
    assert best == pytest.approx(1.6)
    assert second == pytest.approx(1.6)
    assert ambiguous is True


def test_matched_lf_and_lps_routes_compare_in_canonical_observable_space():
    expected, lf_request, lps_request = _matched_current_requests()
    result = compare_current_requests(lf_request, lps_request)
    assert result.status == "CANONICAL_OBSERVABLE_COMPARISON"
    assert result.incomparability_reasons == ()
    assert result.route_local_extraction_passed is True
    np.testing.assert_allclose(
        (result.first.GC, result.first.GM, result.first.GQ), expected, atol=2.0e-14
    )
    np.testing.assert_allclose(
        (result.second.GC, result.second.GM, result.second.GQ), expected, atol=2.0e-14
    )
    assert max(value for value in result.absolute_differences.values() if value is not None) < 2.0e-14
    assert result.first.route != result.second.route
    assert result.first.route_conventions["frame"] != result.second.route_conventions["frame"]
    assert result.production_current_selected is False
    assert result.physical_agreement_claim is False


def test_canonical_current_comparison_fails_closed_on_invariant_mismatch():
    _, lf_request, _ = _matched_current_requests(state_id="first")
    _, _, lps_request = _matched_current_requests(state_id="second")
    result = compare_current_requests(lf_request, lps_request)
    assert result.status == "INCOMPARABLE_INVARIANTS"
    assert "state identifiers differ" in result.incomparability_reasons
    assert result.physical_agreement_claim is False




def test_lps_dimensional_current_is_unit_invariant_across_supported_units():
    expected, _, lps_gev = _matched_current_requests()
    adapter = UnifiedCurrentAdapter()
    reference = adapter.extract(lps_gev)
    unit_scales = {
        "MeV": 1000.0,
        "fm^-1": 1.0 / 0.1973269804,
    }
    for units, source_units_per_gev in unit_scales.items():
        conventions = CurrentConventions(
            "longitudinal Breit",
            "Q2=-(q_mu q^mu)>0",
            "J+/-/Jx",
            "LPS unnormalized free current",
            ("I++", "I+0", "I+-", "I00"),
            (1 + 0j,) * 4,
            "GC,GM,GQ LPS Eq.21 normalization",
            units,
            units,
            "LPS_EQ21",
            "EXPLICIT_CALLER_BOUND",
            "EXPLICIT_CALLER_BOUND",
        )
        request = CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            conventions,
            np.asarray(lps_gev.current) * source_units_per_gev,
            lps_gev.eta,
            lps_gev.momentum_transfer * source_units_per_gev,
            lps_gev.deuteron_mass * source_units_per_gev,
            lps_gev.state_id,
        )
        converted = adapter.extract(request)
        np.testing.assert_allclose(converted, expected, rtol=1.0e-13, atol=1.0e-13)
        np.testing.assert_allclose(converted, reference, rtol=1.0e-13, atol=1.0e-13)


def test_lps_rejects_unapplied_spin_order_or_phase_metadata():
    _, _, lps_request = _matched_current_requests()
    base = lps_request.conventions
    with pytest.raises(CurrentAdapterError, match="fixed canonical m"):
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            CurrentConventions(
                base.frame,
                base.momentum_transfer_sign,
                base.current_component,
                base.amplitude_normalization,
                ("I00", "I+-", "I+0", "I++"),
                base.helicity_phases,
                base.form_factor_normalization,
                base.momentum_transfer_units,
                base.mass_units,
                base.extraction_prescription,
                base.zero_mode_policy,
                base.interaction_current_policy,
            ),
            lps_request.current,
            lps_request.eta,
            lps_request.momentum_transfer,
            lps_request.deuteron_mass,
            lps_request.state_id,
        )
    with pytest.raises(CurrentAdapterError, match="fixed canonical spin-phase"):
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            CurrentConventions(
                base.frame,
                base.momentum_transfer_sign,
                base.current_component,
                base.amplitude_normalization,
                base.helicity_order,
                (1j, 1 + 0j, 1 + 0j, 1 + 0j),
                base.form_factor_normalization,
                base.momentum_transfer_units,
                base.mass_units,
                base.extraction_prescription,
                base.zero_mode_policy,
                base.interaction_current_policy,
            ),
            lps_request.current,
            lps_request.eta,
            lps_request.momentum_transfer,
            lps_request.deuteron_mass,
            lps_request.state_id,
        )


def test_current_adapter_rejects_nonfinite_lf_and_lps_inputs():
    expected, lf_request, lps_request = _matched_current_requests()
    bad_lf = current_from_form_factors(
        eta=lf_request.eta,
        charge=expected[0],
        magnetic=expected[1],
        quadrupole=expected[2],
    )
    bad_lf = type(bad_lf)(np.nan + 0j, bad_lf.plus_zero, bad_lf.plus_minus, bad_lf.zero_zero)
    with pytest.raises(CurrentAdapterError, match="finite complex values"):
        CurrentRequest(
            CurrentRoute.LIGHT_FRONT,
            lf_request.conventions,
            bad_lf,
            lf_request.eta,
            lf_request.momentum_transfer,
            lf_request.deuteron_mass,
            lf_request.state_id,
        )

    bad_lps = np.asarray(lps_request.current, dtype=np.complex128).copy()
    bad_lps[0, 0, 0] = np.nan
    with pytest.raises(CurrentAdapterError, match="finite complex values"):
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            lps_request.conventions,
            bad_lps,
            lps_request.eta,
            lps_request.momentum_transfer,
            lps_request.deuteron_mass,
            lps_request.state_id,
        )


def test_dependency_failure_reports_actual_path_and_never_substitutes_c64(tmp_path):
    missing = tmp_path / "data/raw/c293_sources_hep-th-0101072.pdf"
    try:
        missing.read_bytes()
    except FileNotFoundError as error:
        record = dependency_failure_record(error, repository_root=tmp_path)
    assert record.first_missing_path == "data/raw/c293_sources_hep-th-0101072.pdf"
    assert "c64" not in record.message.lower()
    assert str(tmp_path) not in record.message
    assert "<REPOSITORY_ROOT>/data/raw/c293_sources_hep-th-0101072.pdf" in record.message
    assert record.hardcoded_substitution_used is False


def test_semantic_eigensystem_replay_accepts_phases_and_degenerate_rotations():
    eigenvalues = (1.0, 1.0)
    reference = np.eye(2, dtype=np.complex128)
    angle = np.pi / 4.0
    rotation = np.asarray(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]],
        dtype=np.complex128,
    )
    candidate = reference @ rotation
    result = compare_eigensystems(
        eigenvalues,
        reference,
        (1e-12, 1e-12),
        eigenvalues,
        candidate,
        (2e-12, 2e-12),
        degeneracy_tolerance=1e-6,
    )
    assert result.pass_all is True
    assert result.raw_vector_hashes_compared is False
    assert result.clusters[0].projector_frobenius_distance < 1e-12
    assert min(result.clusters[0].singular_values) > 1.0 - 1e-12


def test_step_tolerance_scan_does_not_certify_one_step_or_physical_c396_derivative():
    scan = derivative_step_tolerance_scan(
        resolution="K9",
        coordinate_id="phi_mass",
        steps=(1.0e-3,),
        solver_tolerances=(1.0e-8,),
    )
    assert len(scan["rows"]) == 1
    assert scan["rows"][0]["same_state_verified"] is True
    assert scan["single_step_certification"] is False
    assert scan["physical_derivative_claim"] is False
    assert scan["C396_derivative_claim"] is False


def test_s2_current_adapter_is_dependency_closed_without_p1_imports():
    import inspect
    import deuteron_wigner.bridge.c400_s2_corrective.current_adapter as current_adapter_module
    import deuteron_wigner.bridge.c400_s2_corrective.current_compare as current_compare_module

    assert CurrentRequest.__module__ == (
        "deuteron_wigner.bridge.c400_s2_corrective.current_adapter"
    )
    assert "c400_p1_mechanical_closure" not in inspect.getsource(current_adapter_module)
    assert "c400_p1_mechanical_closure" not in inspect.getsource(current_compare_module)




def test_generated_s2_state_identity_evidence_matches_current_schema():
    import json

    path = Path("docs/phases/c400_s2_corrective_patch/state_identity_validation.json")
    record = json.loads(path.read_text(encoding="utf-8"))
    for key in (
        "projector_invariance_residual",
        "projector_relative_invariance_residual",
        "projector_invariant_subspace",
    ):
        assert key in record, (
            "S2 state-identity evidence is stale relative to the current state-identity schema; "
            "rerun tools/generate_c400_s2_corrective.sh before merge"
        )
    for pair in record["eigenpairs"]:
        for key in (
            "relative_eigenvalue_residual",
            "spectral_status",
            "projector_membership_verified",
            "full_eigenstate_verified",
        ):
            assert key in pair, (
                "S2 state-identity evidence is stale relative to the current state-identity schema; "
                "rerun tools/generate_c400_s2_corrective.sh before merge"
            )


def test_forward_integrity_record_cannot_be_mistaken_for_c396_forward_map():
    record = diagnostic_forward_integrity_record(
        resolution="K9",
        derivative_step=1.0e-5,
        solver_tolerance=1.0e-8,
        execute_numerical_smoke=False,
    )
    assert record["status"] == "PARTIAL_FORWARD_MAP"
    assert record["executable_path"]["operator_family"] == "C144_DIAGNOSTIC_FIXTURE_11_COORDINATES"
    assert record["executable_path"]["state_identity"] == UNPROJECTED_STATUS
    assert record["executable_path"]["execution_status"] == "NOT_EXECUTED_IN_THIS_RECORD"
    assert record["C396_family"]["forward_map_ready"] is False
    assert record["C396_family"]["complete_numerical_apply_paths"] == 0
    assert record["state_to_current_observable_path_ready"] is False
    assert record["rank_status"] == "RANK_NOT_EVALUATED"
    assert record["physical_fit_authorized"] is False
