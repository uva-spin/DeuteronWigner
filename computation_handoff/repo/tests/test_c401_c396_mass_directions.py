from __future__ import annotations

from fractions import Fraction
import hashlib
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

from deuteron_wigner.bridge import c401_c396_mass_directions as c401
from deuteron_wigner.bridge.c401_c396_mass_directions import basis as c401_basis
from deuteron_wigner.bridge.c401_c396_mass_directions import operators as c401_ops
from deuteron_wigner.bridge.free2 import core as c128


def test_c401_exact_partitions_and_direct_sum_blocks() -> None:
    expected_first_xq = {"K9": Fraction(7, 9), "K11": Fraction(9, 11), "K13": Fraction(11, 13)}
    for resolution in c401.RESOLUTION_LABELS:
        record = c401.resolution_record(resolution)
        partitions = c401.canonical_partitions(resolution)
        assert partitions[0].xq == expected_first_xq[resolution]
        assert partitions[0].qg_direct_start == record["q_dimension"]
        assert partitions[-1].qg_direct_stop == record["direct_sum_dimension"]
        assert sum(partition.qg_state_count for partition in partitions) == record["qg_dimension"]
        assert all(partition.kq + partition.kg == Fraction(record["K_fraction"]) for partition in partitions)
        assert all(partition.xq > 0 and partition.xg > 0 for partition in partitions)
        assert all(partition.xq + partition.xg == 1 for partition in partitions)
        assert record["b_HO_unit"] == "GeV"
        assert record["C396_b_HO_metadata_field"] == "bHO_GeVinv"
        assert record["C396_b_HO_unit_label_conflict_retained"] is True
        assert record["mass_direction_depends_on_b_HO"] is False
        provenance = c401.basis_fraction_provenance(resolution)
        assert provenance["partition_major_order_verified"] is True
        assert provenance["all_fractions_positive"] is True
        assert provenance["all_fraction_sums_exactly_one"] is True


def test_c401_exposes_historical_c128_quark_fraction_defect_without_mutation() -> None:
    audit = c401.historical_c128_partition_defect_audit()
    assert audit["status"] == "HISTORICAL_C128_LONGITUDINAL_QUARK_FRACTION_IMPLEMENTATION_DEFECT_CONFIRMED"
    assert tuple(audit["affected_resolutions"]) == c401.RESOLUTION_LABELS
    assert audit["historical_files_modified"] is False
    assert audit["quark_mass_derivative_affected"] is True
    assert audit["gluon_fraction_affected"] is False
    for row in audit["rows"]:
        assert row["canonical"]["sum"] == "1"
        assert row["quark_fraction_match"] is False
        assert row["gluon_fraction_match"] is True
        assert Fraction(row["xq_residual"]) == Fraction(1, int(row["full_resolution_id"].split("_")[0][1:]))


def test_c401_mass_direction_values_and_sparse_shapes() -> None:
    for resolution in c401.RESOLUTION_LABELS:
        record = c401.resolution_record(resolution)
        dq = c401.operator_diagonal(resolution, c401.D_MU_Q_SQ)
        dg = c401.operator_diagonal(resolution, c401.D_DELTA_MU_G_SQ)
        assert dq.shape == dg.shape == (record["direct_sum_dimension"],)
        np.testing.assert_array_equal(dq[: record["q_dimension"]], np.ones(record["q_dimension"]))
        np.testing.assert_array_equal(dg[: record["q_dimension"]], np.zeros(record["q_dimension"]))
        for partition in c401.canonical_partitions(resolution):
            np.testing.assert_array_equal(
                dq[partition.qg_direct_start : partition.qg_direct_stop],
                np.full(partition.qg_state_count, float(1 / partition.xq)),
            )
            np.testing.assert_array_equal(
                dg[partition.qg_direct_start : partition.qg_direct_stop],
                np.full(partition.qg_state_count, float(1 / partition.xg)),
            )
        q_sparse = c401.sparse_coordinate_operator(resolution, c401.D_MU_Q_SQ)
        g_sparse = c401.sparse_coordinate_operator(resolution, c401.D_DELTA_MU_G_SQ)
        assert q_sparse["shape"] == g_sparse["shape"] == (
            record["direct_sum_dimension"],
            record["direct_sum_dimension"],
        )
        assert q_sparse["nnz"] == record["direct_sum_dimension"]
        assert g_sparse["nnz"] == record["qg_dimension"]
        assert q_sparse["Hermitian"] and g_sparse["Hermitian"]
        assert q_sparse["physical_value_selected"] is False
        assert g_sparse["physical_value_selected"] is False


def test_c401_scipy_csr_and_linear_operator_routes_are_sparse_and_agree() -> None:
    for resolution in c401.RESOLUTION_LABELS:
        record = c401.resolution_record(resolution)
        for direction in c401.DIRECTIONS:
            csr = c401.coordinate_operator_csr(resolution, direction)
            linear = c401.coordinate_linear_operator(resolution, direction)
            assert csr.shape == linear.shape == (
                record["direct_sum_dimension"],
                record["direct_sum_dimension"],
            )
            assert csr.nnz == (
                record["direct_sum_dimension"]
                if direction == c401.D_MU_Q_SQ
                else record["qg_dimension"]
            )
            np.testing.assert_allclose((csr - csr.getH()).data, 0.0, rtol=0.0, atol=0.0)
            for _, vector in c401_ops.deterministic_validation_vectors(resolution):
                np.testing.assert_allclose(csr @ vector, linear @ vector, rtol=0.0, atol=0.0)


def test_c401_sparse_and_matrix_free_routes_agree() -> None:
    for resolution in c401.RESOLUTION_LABELS:
        result = c401.sparse_matrix_free_validation(resolution)
        assert result["pass"] is True
        assert result["maximum_relative_residual"] <= result["tolerance"]
        for direction in c401.DIRECTIONS:
            operator = c401.sparse_coordinate_operator(resolution, direction)
            for _, vector in c401_ops.deterministic_validation_vectors(resolution):
                np.testing.assert_allclose(
                    c401.apply_sparse_coordinate_operator(operator, vector),
                    c401.apply_mass_direction(resolution, direction, vector),
                    rtol=0.0,
                    atol=0.0,
                )


def test_c401_source_formula_holdout_does_not_reuse_operator_partition_adapter(monkeypatch) -> None:
    resolution = "K9"
    record = c401.resolution_record(resolution)
    vector = np.ones(record["direct_sum_dimension"], dtype=np.complex128)

    def forbidden(*_args, **_kwargs):
        raise AssertionError("operator-side canonical_partitions route was reused")

    monkeypatch.setattr(c401_ops, "canonical_partitions", forbidden)
    result = c401.source_mass_component_action(
        resolution,
        vector,
        mu_q_sq=0.31,
        delta_mu_g_sq=0.17,
    )
    assert result.shape == vector.shape
    assert np.all(np.isfinite(result))


def test_c401_source_formula_finite_differences_agree_at_multiple_steps() -> None:
    for resolution in c401.RESOLUTION_LABELS:
        result = c401.finite_difference_validation(
            resolution,
            steps=(1.0e-2, 1.0e-4, 1.0e-6),
        )
        assert result["pass"] is True
        assert result["maximum_relative_residual"] <= result["tolerance"]
        assert {row["step"] for row in result["rows"]} == {1.0e-2, 1.0e-4, 1.0e-6}
        assert result["diagnostic_base_point"]["physical"] is False
        assert result["historical_C128_numeric_implementation_used"] is False


def test_c401_historical_derivative_comparison_is_direction_specific() -> None:
    for resolution in c401.RESOLUTION_LABELS:
        result = c401.historical_c128_derivative_comparison(resolution)
        rows = {row["direction"]: row for row in result["rows"]}
        assert rows[c401.D_MU_Q_SQ]["entries_different"] == c401.resolution_record(resolution)["qg_dimension"]
        assert rows[c401.D_MU_Q_SQ]["relative_frobenius_difference"] > 0.1
        assert rows[c401.D_DELTA_MU_G_SQ]["material_entries_different"] == 0
        assert rows[c401.D_DELTA_MU_G_SQ]["historical_matches_source_corrected"] is True
        assert rows[c401.D_DELTA_MU_G_SQ]["relative_frobenius_difference"] <= 1.0e-15


def test_c401_binding_overlay_completes_exactly_six_K_local_rows() -> None:
    inventory = c401.c396_binding_inventory_with_c401_mass_directions()
    assert inventory["total_rows"] == 57
    assert inventory["complete_numerical_apply_paths"] == 6
    assert inventory["expected_complete_numerical_apply_paths"] == 6
    assert inventory["C396_19_coordinate_forward_map_ready"] is False
    assert inventory["rank_status"] == "RANK_NOT_EVALUATED"
    ready = [row for row in inventory["rows"] if row["numerical_apply_path"]]
    assert len(ready) == 6
    assert {(row["resolution"], row["coordinate_id"]) for row in ready} == {
        (resolution, coordinate)
        for resolution in c401.RESOLUTION_LABELS
        for coordinate in ("ct_mass", "ct_gluon_mass")
    }
    assert all(row["selected"] is False and row["zeroed"] is False and row["physical"] is False for row in ready)
    reduction = inventory["coordinate_reduction"]
    assert reduction["maximum_candidate_matrix_dimension_per_resolution"] == 16
    assert reduction["candidate_dimension_is_rank"] is False
    assert reduction["maximum_candidate_matrix_dimension_status"] == "PROVISIONAL_UPPER_BOUND_NOT_RANK"


def test_c401_nonmatrix_slots_are_not_materialized() -> None:
    inventory = c401.c396_binding_inventory_with_c401_mass_directions()
    for row in inventory["rows"]:
        if row["coordinate_id"] in {"ct_vacuum_energy", "ct_boundary", "ct_truncation"}:
            assert row["numerical_apply_path"] is None
            assert row["C401_role"] in {
                "VACUUM_ONLY_OUTSIDE_RETAINED_Q_QG_DIRECT_SUM",
                "NONMATRIX_DOMAIN_OR_BOUNDARY_PARAMETER",
                "NONMATRIX_TRUNCATION_DISCREPANCY",
            }


def test_c401_no_c144_proxy_or_physical_selection() -> None:
    source = inspect.getsource(c401_ops) + inspect.getsource(c401_basis)
    assert "hqcdopapi" not in source
    assert "parameterized_sparse_operator" not in source
    assert "load_diagnostic_fixture" not in source
    inventory = c401.mass_direction_operator_inventory()
    assert inventory["physical_values_selected"] == 0
    assert inventory["rank_status"] == "RANK_NOT_EVALUATED"
    assert inventory["activation_gate_status"] == "NOT_READY"
    assert inventory["complete_numerical_apply_rows"] == 6


def test_c401_fail_closed_inputs() -> None:
    with pytest.raises(KeyError):
        c401.operator_diagonal("K15", c401.D_MU_Q_SQ)
    with pytest.raises(KeyError):
        c401.operator_diagonal("K9", "D_unknown")
    with pytest.raises(IndexError):
        c401.partition_for_direct_index("K9", -1)
    with pytest.raises(ValueError):
        c401.apply_mass_direction("K9", c401.D_MU_Q_SQ, np.zeros(3))
    with pytest.raises(ValueError):
        c401.source_mass_component_action(
            "K9", np.zeros(c128.DIRECT_DIMS[c128.RESOLUTIONS[0]]), mu_q_sq=np.nan, delta_mu_g_sq=0.0
        )
    with pytest.raises(ValueError):
        c401.finite_difference_validation("K9", steps=(0.0,))


def test_c401_complete_validation_summary() -> None:
    result = c401.all_validation_records()
    assert result["pass"] is True
    assert result["sparse_matrix_free_pass"] is True
    assert result["finite_difference_pass"] is True
    assert result["historical_quark_fraction_defect_exposed"] is True
    assert result["historical_gluon_fraction_unchanged"] is True


def test_c401_evidence_generator_is_deterministic_and_self_excluding(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    outputs = (tmp_path / "first", tmp_path / "second")
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(root / "src")
    environment.setdefault("OMP_NUM_THREADS", "1")
    environment.setdefault("OPENBLAS_NUM_THREADS", "1")
    environment.setdefault("MKL_NUM_THREADS", "1")
    for output in outputs:
        result = subprocess.run(
            [
                sys.executable,
                str(root / "tools/generate_c401_c396_mass_directions.py"),
                "--output-dir",
                str(output),
            ],
            cwd=root,
            env=environment,
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
        assert result.returncode == 0, result.stderr
    names_first = sorted(path.name for path in outputs[0].iterdir() if path.is_file())
    names_second = sorted(path.name for path in outputs[1].iterdir() if path.is_file())
    assert names_first == names_second
    for name in names_first:
        first = (outputs[0] / name).read_bytes()
        second = (outputs[1] / name).read_bytes()
        assert hashlib.sha256(first).digest() == hashlib.sha256(second).digest(), name
    generation = json.loads((outputs[0] / "generation_result.json").read_text())
    assert generation["validation_pass"] is True
    assert generation["complete_numerical_apply_paths"] == 6
    assert "generation_result.json" not in {row["path"] for row in generation["artifacts"]}
