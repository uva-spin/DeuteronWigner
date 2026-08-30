#!/usr/bin/env python3
"""Generate C400.S2 corrective implementation-lock evidence.

Historical P1/P1B/P1C artifacts are never rewritten.  All outputs are versioned
under ``docs/phases/c400_s2_corrective_patch`` and remain diagnostic/nonphysical.
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass, replace
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.lf_current import current_from_form_factors
from deuteron_wigner.bridge.c400_s2_corrective.current_adapter import (
    CurrentConventions,
    CurrentRequest,
    CurrentRoute,
)
from deuteron_wigner.bridge.c400_s2_corrective.coordinate_bindings import (
    binding_summary,
    coordinate_binding_inventory,
)
from deuteron_wigner.bridge.c400_s2_corrective.current_compare import compare_current_requests
from deuteron_wigner.bridge.c400_s2_corrective.derivative_integrity import (
    audit_all_c144_derivatives,
)
from deuteron_wigner.bridge.c400_s2_corrective.forward_integrity import (
    diagnostic_forward_integrity_record,
)
from deuteron_wigner.bridge.c400_s2_corrective.replay_integrity import (
    dependency_failure_record,
    semantic_replay_record,
)
from deuteron_wigner.bridge.c400_s2_corrective.state_identity import (
    DiagnosticSpectrum,
    derivative_step_tolerance_scan,
    solve_c144_diagnostic,
)
from deuteron_wigner.bridge.c400_s2_corrective.status import status_supersession_record
from deuteron_wigner.bridge.c400_s2_corrective.tracking import (
    StateRecord,
    StateTracker,
    TrackingPolicy,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/phases/c400_s2_corrective_patch"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def progress(message: str) -> None:
    print(f"[C400.S2] {message}", file=sys.stderr, flush=True)


def jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set)):
        return [jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return jsonable(value.tolist())
    if isinstance(value, (np.floating, np.integer, np.bool_)):
        return value.item()
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, Path):
        try:
            return value.relative_to(ROOT).as_posix()
        except ValueError:
            return str(value)
    if isinstance(value, float) and not np.isfinite(value):
        return "Infinity" if value > 0 else "-Infinity" if value < 0 else "NaN"
    return value


def write_json(name: str, value: Any) -> Path:
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(jsonable(value), indent=2, sort_keys=True, ensure_ascii=True) + "\n")
    return path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def derivative_audit_in_fresh_process() -> Mapping[str, Any]:
    """Run the large sparse audit in a fresh process.

    On the review platform, repeated ARPACK calls followed by the all-resolution
    sparse audit can trigger severe SciPy/BLAS slowdown.  Isolating the audit is
    both deterministic and closer to the independent-route intent of this phase.
    """

    import tempfile

    with tempfile.TemporaryDirectory(prefix="c400_s2_derivatives_") as temporary:
        output = Path(temporary) / "derivatives.json"
        environment = dict(os.environ)
        environment["PYTHONPATH"] = str(ROOT / "src")
        environment.setdefault("OMP_NUM_THREADS", "1")
        environment.setdefault("OPENBLAS_NUM_THREADS", "1")
        environment.setdefault("MKL_NUM_THREADS", "1")
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--derivative-worker", str(output)],
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            timeout=180,
            check=False,
        )
        if result.returncode != 0 or not output.is_file():
            raise RuntimeError(
                "C400.S2 derivative worker failed: "
                f"exit={result.returncode}; stdout={result.stdout[-1000:]}; "
                f"stderr={result.stderr[-2000:]}"
            )
        return json.loads(output.read_text())


def numerical_evidence_in_fresh_process(derivatives: Mapping[str, Any]) -> Mapping[str, Any]:
    """Run eigensolver/scan evidence in a second clean worker process."""

    import tempfile

    with tempfile.TemporaryDirectory(prefix="c400_s2_numerical_") as temporary:
        work = Path(temporary)
        derivative_path = work / "derivatives.json"
        output = work / "numerical.json"
        derivative_path.write_text(json.dumps(jsonable(derivatives), sort_keys=True) + "\n")
        environment = dict(os.environ)
        environment["PYTHONPATH"] = str(ROOT / "src")
        environment.setdefault("OMP_NUM_THREADS", "1")
        environment.setdefault("OPENBLAS_NUM_THREADS", "1")
        environment.setdefault("MKL_NUM_THREADS", "1")
        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--numerical-worker",
                str(output),
                "--derivative-input",
                str(derivative_path),
            ],
            cwd=ROOT,
            env=environment,
            text=True,
            capture_output=True,
            timeout=180,
            check=False,
        )
        if result.returncode != 0 or not output.is_file():
            raise RuntimeError(
                "C400.S2 numerical worker failed: "
                f"exit={result.returncode}; stdout={result.stdout[-1000:]}; "
                f"stderr={result.stderr[-2000:]}"
            )
        return json.loads(output.read_text())


def _state(state_id: str, energy: float, vector, sector=(("J", "1"),)) -> StateRecord:
    return StateRecord(state_id, sector, energy, np.asarray(vector, dtype=np.complex128))


def _lf_conventions() -> CurrentConventions:
    return CurrentConventions(
        "Drell-Yan q+=0", "Q2=-(q_mu q^mu)>0", "J+", "I=J+/(2P+)",
        ("I++", "I+0", "I+-", "I00"), (1 + 0j,) * 4,
        "GC,GM,GQ Carlson-Ji spin-1 normalization", "GeV", "GeV", "omit_I00",
        "EXPLICIT_CALLER_BOUND", "EXPLICIT_CALLER_BOUND",
    )


def _lps_conventions() -> CurrentConventions:
    return CurrentConventions(
        "longitudinal Breit", "Q2=-(q_mu q^mu)>0", "J+/-/Jx",
        "LPS unnormalized free current", ("I++", "I+0", "I+-", "I00"),
        (1 + 0j,) * 4, "GC,GM,GQ LPS Eq.21 normalization", "GeV", "GeV",
        "LPS_EQ21", "EXPLICIT_CALLER_BOUND", "EXPLICIT_CALLER_BOUND",
    )


def current_fixture() -> Mapping[str, Any]:
    q, mass = 0.4, 1.8756
    tau = q**2 / (4.0 * mass**2)
    expected = np.asarray((0.7, 1.3, 12.0))
    lf = current_from_form_factors(
        eta=tau, charge=expected[0], magnetic=expected[1], quadrupole=expected[2]
    )
    lf_request = CurrentRequest(
        CurrentRoute.LIGHT_FRONT, _lf_conventions(), lf, tau, q, mass, "C400-S2-SAME-STATE"
    )
    zeta = 1.0 / (np.sqrt(2.0) * mass * np.sqrt(1.0 + tau))
    lps = np.zeros((4, 3, 3), dtype=np.complex128)
    lps[0, 0, 0] = (expected[0] - 2.0 * tau * expected[2] / 3.0) / zeta
    lps[0, 1, 1] = (expected[0] + 4.0 * tau * expected[2] / 3.0) / zeta
    lps[2, 0, 1] = np.sqrt(tau) * expected[1] / zeta
    lps[2, 1, 0] = -np.sqrt(tau) * expected[1] / zeta
    lps_request = CurrentRequest(
        CurrentRoute.COVARIANT_LPS, _lps_conventions(), lps, tau, q, mass,
        "C400-S2-SAME-STATE",
    )
    comparison = compare_current_requests(lf_request, lps_request)
    return {
        "schema": "C400-S2-CANONICAL-CURRENT-COMPARISON-FIXTURE-V1",
        "expected": tuple(expected),
        "comparison": comparison,
        "production_current_selected": False,
        "covariance_bound": False,
        "physical_agreement_claim": False,
    }


def tracking_fixture() -> Mapping[str, Any]:
    policy = TrackingPolicy(
        overlap_minimum=0.5,
        degeneracy_gap=0.1,
        assignment_tie_tolerance=1.0e-12,
        norm_tolerance=1.0e-8,
    )
    tracker = StateTracker(policy)
    rectangular = tracker.match(
        (_state("a", 0.0, (1, 0)),),
        (_state("a-now", 0.0, (1, 0)), _state("surplus", 0.05, (0, 1))),
    )
    cross_sector = tracker.match(
        (
            _state("J1-old", 0.0, (1, 0), (("J", "1"),)),
            _state("J2-old", 1.0, (0, 1), (("J", "2"),)),
        ),
        (
            _state("J1-new", 2.0, (1, 0), (("J", "1"),)),
            _state("J2-new", -1.0, (0, 1), (("J", "2"),)),
        ),
    )
    assignment_matrix = np.asarray([[0.9, 0.8], [0.8, 0.7]])
    rows, columns, best, second, ambiguous = tracker._assignment_with_ambiguity(assignment_matrix)
    return {
        "schema": "C400-S2-TRACKER-ADVERSARIAL-VALIDATION-V1",
        "rectangular_degenerate": rectangular,
        "cross_sector_energy_crossing": cross_sector,
        "complete_assignment_ambiguity": {
            "overlap": assignment_matrix,
            "rows": rows,
            "columns": columns,
            "best_objective": best,
            "second_best_objective": second,
            "ambiguous": ambiguous,
        },
        "physical_state_claim": False,
    }


def phase_rotated_spectrum(reference: DiagnosticSpectrum) -> DiagnosticSpectrum:
    pairs = []
    for index, pair in enumerate(reference.eigenpairs):
        phase = np.exp(1j * (index + 1) * 0.371)
        state = StateRecord(
            pair.state.state_id + "-replay",
            pair.state.sector,
            pair.state.eigenvalue,
            pair.state.vector * phase,
        )
        pairs.append(
            replace(
                pair,
                state=state,
                vector_sha256_incidental=hashlib.sha256(state.vector.tobytes()).hexdigest(),
            )
        )
    return replace(reference, eigenpairs=tuple(pairs))


def generate(
    *,
    derivatives: Mapping[str, Any],
    numerical: Mapping[str, Any],
) -> Mapping[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    started = now()
    progress("status and binding inventory")
    status = status_supersession_record()
    inventory = coordinate_binding_inventory()
    bindings = binding_summary()
    spectrum = numerical["spectrum"]
    step_scan = numerical["step_scan"]
    replay = numerical["replay"]
    forward = numerical["forward"]
    progress("current comparison fixture")
    current = current_fixture()
    progress("tracking adversarial fixtures")
    tracking = tracking_fixture()

    artifacts = {
        "status_supersession.json": status,
        "c396_coordinate_binding_inventory.json": inventory,
        "c396_binding_summary.json": bindings,
        "c144_derivative_integrity.json": derivatives,
        "c144_derivative_step_tolerance_scan.json": step_scan,
        "state_identity_validation.json": spectrum,
        "tracker_adversarial_validation.json": tracking,
        "current_canonical_comparison.json": current,
        "replay_integrity_validation.json": replay,
        "diagnostic_forward_integrity.json": forward,
        "scientific_nonclaims.json": {
            "schema": "C400-S2-SCIENTIFIC-NONCLAIMS-V1",
            "nonclaims": (
                "no C396 19-coordinate numerical forward map",
                "no numerical deuteron-sector identity without a projector",
                "no physical state selection",
                "no state-to-current production path",
                "no physical current selection",
                "no physical fit",
                "no physical rank",
                "no coordinate zeroing or minimum-norm representative",
                "no resolution averaging",
                "no Hamiltonian activation",
            ),
        },
    }
    progress("writing evidence artifacts")
    for name, value in artifacts.items():
        write_json(name, value)

    generated = sorted(
        path
        for path in OUT.iterdir()
        if path.is_file() and path.name != "generation_result.json"
    )
    result = {
        "schema": "C400-S2-GENERATION-RESULT-V1",
        "status": "CHATGPT_CORRECTIVE_PATCH_EVIDENCE_GENERATED",
        "started_at_utc": started,
        "finished_at_utc": now(),
        "output_directory": OUT.relative_to(ROOT).as_posix(),
        "artifact_count": len(generated),
        "artifacts": tuple(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in generated
        ),
        "C144_derivative_rows": derivatives["count"],
        "C144_corrected_derivatives_verified": derivatives["corrected_verified"],
        "C144_historical_derivative_mismatches": derivatives["historical_mismatches"],
        "C396_binding_rows": inventory["total_rows"],
        "C396_complete_numeric_apply_paths": inventory["complete_numerical_apply_paths"],
        "semantic_replay_pass": replay["pass"],
        "physical_fit_authorized": False,
        "rank_status": "RANK_NOT_EVALUATED",
    }
    write_json("generation_result.json", result)
    progress("complete")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--derivative-worker", default="")
    parser.add_argument("--numerical-worker", default="")
    parser.add_argument("--derivative-input", default="")
    parser.add_argument("--numerical-input", default="")
    parser.add_argument("--assemble", action="store_true")
    arguments = parser.parse_args()
    if arguments.derivative_worker:
        output = Path(arguments.derivative_worker)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(jsonable(audit_all_c144_derivatives(step=1.0e-5)), indent=2, sort_keys=True)
            + "\n"
        )
        return 0
    if arguments.numerical_worker:
        if not arguments.derivative_input:
            raise SystemExit("--numerical-worker requires --derivative-input")
        derivatives = json.loads(Path(arguments.derivative_input).read_text())
        progress("numerical worker: spectrum")
        spectrum = solve_c144_diagnostic("K9", k=2, solver_tolerance=1.0e-8)
        progress("numerical worker: step scan")
        step_scan = derivative_step_tolerance_scan(
            resolution="K9",
            coordinate_id="phi_mass",
            steps=(1.0e-3, 1.0e-4, 1.0e-5),
            solver_tolerances=(1.0e-8, 1.0e-9),
        )
        progress("numerical worker: dependency record")
        dependency = dependency_failure_record(
            FileNotFoundError(
                2,
                "No such file or directory",
                str(ROOT / "data/raw/c293_sources_hep-th-0101072.pdf"),
            ),
            repository_root=ROOT,
        )
        progress("numerical worker: semantic replay")
        replay = semantic_replay_record(
            spectrum,
            phase_rotated_spectrum(spectrum),
            dependency_reference=dependency,
            dependency_candidate=dependency,
            command=("PYTHONPATH=src", "python3", "tools/generate_c400_s2_corrective.py"),
            environment={
                "python": platform.python_version(),
                "platform": platform.platform(),
                "numpy": np.__version__,
            },
        )
        progress("numerical worker: forward integrity")
        forward = diagnostic_forward_integrity_record(
            resolution="K9",
            derivative_step=1.0e-5,
            solver_tolerance=1.0e-8,
            precomputed_spectrum=spectrum,
            precomputed_derivative_audit={
                **derivatives,
                "rows": tuple(row for row in derivatives["rows"] if row["resolution"] == "K9"),
                "count": 11,
            },
        )
        progress("numerical worker: serialize")
        Path(arguments.numerical_worker).write_text(
            json.dumps(
                jsonable(
                    {
                        "spectrum": spectrum,
                        "step_scan": step_scan,
                        "replay": replay,
                        "forward": forward,
                    }
                ),
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
        return 0
    if arguments.assemble:
        if not arguments.derivative_input or not arguments.numerical_input:
            raise SystemExit("--assemble requires --derivative-input and --numerical-input")
        derivatives = json.loads(Path(arguments.derivative_input).read_text())
        numerical = json.loads(Path(arguments.numerical_input).read_text())
        print(
            json.dumps(
                jsonable(generate(derivatives=derivatives, numerical=numerical)),
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    raise SystemExit(
        "Use tools/generate_c400_s2_corrective.sh, or select an explicit "
        "--derivative-worker, --numerical-worker, or --assemble mode."
    )


if __name__ == "__main__":
    raise SystemExit(main())
