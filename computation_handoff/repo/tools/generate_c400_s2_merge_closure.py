#!/usr/bin/env python3
"""Generate C400.S2M merge-closure evidence.

This stage does not alter the scientific status of C400.S2.  It proves that the
S2 current layer no longer depends on unmerged P1/P1B/P1C modules and that a
projected Ritz vector is not mislabeled as a verified sector eigenstate unless
the projected range is Hamiltonian invariant and the full-space eigenresidual
passes.
"""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
import ast
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.lf_current import current_from_form_factors
from deuteron_wigner.bridge.c400_s2_corrective.current_adapter import (
    CurrentAdapterError,
    CurrentConventions,
    CurrentRequest,
    CurrentRoute,
    UnifiedCurrentAdapter,
)
from deuteron_wigner.bridge.c400_s2_corrective.state_identity import (
    PROJECTED_RITZ_STATUS,
    PROJECTED_STATUS,
    SectorProjector,
    solve_c144_diagnostic,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/phases/c400_s2_merge_closure"
FORBIDDEN_IMPORT_PREFIXES = (
    "deuteron_wigner.bridge.c400_p1_mechanical_closure",
)
DEPENDENCY_SURFACE = tuple(
    sorted((ROOT / "src/deuteron_wigner/bridge/c400_s2_corrective").glob("*.py"))
) + (
    ROOT / "tests/test_c400_s2_corrective.py",
    ROOT / "tools/generate_c400_s2_corrective.py",
    ROOT / "tools/generate_c400_s2_merge_closure.py",
)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return jsonable(value.tolist())
    if isinstance(value, (np.floating, np.integer, np.bool_)):
        return value.item()
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, float) and not np.isfinite(value):
        return "Infinity" if value > 0 else "-Infinity" if value < 0 else "NaN"
    return value


def write_json(name: str, value: Any) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def dependency_closure_record() -> Mapping[str, Any]:
    rows = []
    all_clear = True
    for path in DEPENDENCY_SURFACE:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imports: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.append(node.module)
        hits = tuple(
            sorted(
                module
                for module in set(imports)
                if any(
                    module == prefix or module.startswith(prefix + ".")
                    for prefix in FORBIDDEN_IMPORT_PREFIXES
                )
            )
        )
        clear = not hits
        all_clear = all_clear and clear
        rows.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "import_modules": tuple(sorted(set(imports))),
                "forbidden_imports": hits,
                "dependency_closed": clear,
            }
        )
    return {
        "schema": "C400-S2M-DEPENDENCY-CLOSURE-V1",
        "status": "S2_CURRENT_LAYER_DEPENDENCY_CLOSED" if all_clear else "S2_DEPENDENCY_CLOSURE_FAILED",
        "rows": tuple(rows),
        "all_clear": all_clear,
        "unmerged_P1_P1B_P1C_required_for_S2_import": False if all_clear else None,
        "physical_claim": False,
    }


def projector_semantics_record() -> Mapping[str, Any]:
    dimension = 1350
    matrix = np.zeros((dimension, dimension), dtype=np.complex128)
    matrix[0, 0] = 1.0
    projector = SectorProjector(
        owner="C400-S2M-SYNTHETIC-NONINVARIANT-PROJECTOR",
        requested_sector=(("fixture-sector", "rank-one"),),
        matrix=matrix,
    )
    spectrum = solve_c144_diagnostic("K9", k=1, projector=projector)
    pair = spectrum.eigenpairs[0]
    passed = bool(
        pair.projector_membership_verified is True
        and spectrum.projector_invariant_subspace is False
        and pair.full_eigenstate_verified is False
        and pair.identity_status == PROJECTED_RITZ_STATUS
        and pair.spectral_status == PROJECTED_RITZ_STATUS
        and pair.identity_status != PROJECTED_STATUS
    )
    return {
        "schema": "C400-S2M-PROJECTED-STATE-SEMANTICS-V1",
        "status": "NONINVARIANT_PROJECTED_SUBSPACE_CLASSIFIED_AS_RITZ_ONLY" if passed else "PROJECTED_STATE_SEMANTICS_FAILED",
        "projector_owner": projector.owner,
        "projector_membership_verified": pair.projector_membership_verified,
        "projector_invariance_residual": spectrum.projector_invariance_residual,
        "projector_relative_invariance_residual": spectrum.projector_relative_invariance_residual,
        "projector_invariant_subspace": spectrum.projector_invariant_subspace,
        "eigenvalue_residual": pair.eigenvalue_residual,
        "relative_eigenvalue_residual": pair.relative_eigenvalue_residual,
        "identity_status": pair.identity_status,
        "spectral_status": pair.spectral_status,
        "full_eigenstate_verified": pair.full_eigenstate_verified,
        "pass": passed,
        "physical_sector_claim": False,
        "physical_state_claim": False,
    }


def current_adapter_semantics_record() -> Mapping[str, Any]:
    q_gev = 0.4
    mass_gev = 1.8756
    tau = q_gev**2 / (4.0 * mass_gev**2)
    expected = np.asarray((0.7, 1.3, 12.0), dtype=float)
    zeta = 1.0 / (np.sqrt(2.0) * mass_gev * np.sqrt(1.0 + tau))
    current_gev = np.zeros((4, 3, 3), dtype=np.complex128)
    current_gev[0, 0, 0] = (expected[0] - 2.0 * tau * expected[2] / 3.0) / zeta
    current_gev[0, 1, 1] = (expected[0] + 4.0 * tau * expected[2] / 3.0) / zeta
    current_gev[2, 0, 1] = np.sqrt(tau) * expected[1] / zeta
    current_gev[2, 1, 0] = -np.sqrt(tau) * expected[1] / zeta

    def conventions(units: str = "GeV", *, order=("I++", "I+0", "I+-", "I00"), phases=(1 + 0j,) * 4):
        return CurrentConventions(
            "longitudinal Breit",
            "Q2=-(q_mu q^mu)>0",
            "J+/-/Jx",
            "LPS unnormalized free current",
            tuple(order),
            tuple(phases),
            "GC,GM,GQ LPS Eq.21 normalization",
            units,
            units,
            "LPS_EQ21",
            "EXPLICIT_CALLER_BOUND",
            "EXPLICIT_CALLER_BOUND",
        )

    adapter = UnifiedCurrentAdapter()
    gev_request = CurrentRequest(
        CurrentRoute.COVARIANT_LPS,
        conventions("GeV"),
        current_gev,
        tau,
        q_gev,
        mass_gev,
        "C400-S2M-CURRENT-UNIT-FIXTURE",
    )
    mev_request = CurrentRequest(
        CurrentRoute.COVARIANT_LPS,
        conventions("MeV"),
        current_gev * 1000.0,
        tau,
        q_gev * 1000.0,
        mass_gev * 1000.0,
        "C400-S2M-CURRENT-UNIT-FIXTURE",
    )
    fm_inverse_scale = 1.0 / 0.1973269804
    fm_inverse_request = CurrentRequest(
        CurrentRoute.COVARIANT_LPS,
        conventions("fm^-1"),
        current_gev * fm_inverse_scale,
        tau,
        q_gev * fm_inverse_scale,
        mass_gev * fm_inverse_scale,
        "C400-S2M-CURRENT-UNIT-FIXTURE",
    )
    gev = np.asarray(adapter.extract(gev_request), dtype=np.complex128)
    mev = np.asarray(adapter.extract(mev_request), dtype=np.complex128)
    fm_inverse = np.asarray(adapter.extract(fm_inverse_request), dtype=np.complex128)

    rejection: dict[str, bool] = {}
    try:
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            conventions(order=("I00", "I+-", "I+0", "I++")),
            current_gev,
            tau,
            q_gev,
            mass_gev,
            "C400-S2M-CURRENT-UNIT-FIXTURE",
        )
        rejection["noncanonical_spin_order"] = False
    except CurrentAdapterError:
        rejection["noncanonical_spin_order"] = True
    try:
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            conventions(phases=(1j, 1 + 0j, 1 + 0j, 1 + 0j)),
            current_gev,
            tau,
            q_gev,
            mass_gev,
            "C400-S2M-CURRENT-UNIT-FIXTURE",
        )
        rejection["noncanonical_spin_phase"] = False
    except CurrentAdapterError:
        rejection["noncanonical_spin_phase"] = True
    current_nan = np.array(current_gev, copy=True)
    current_nan[0, 0, 0] = np.nan
    try:
        CurrentRequest(
            CurrentRoute.COVARIANT_LPS,
            conventions(),
            current_nan,
            tau,
            q_gev,
            mass_gev,
            "C400-S2M-CURRENT-UNIT-FIXTURE",
        )
        rejection["nonfinite_current"] = False
    except CurrentAdapterError:
        rejection["nonfinite_current"] = True

    unit_invariant = bool(
        np.allclose(gev, expected, rtol=1.0e-13, atol=1.0e-13)
        and np.allclose(mev, expected, rtol=1.0e-13, atol=1.0e-13)
        and np.allclose(fm_inverse, expected, rtol=1.0e-13, atol=1.0e-13)
        and np.allclose(gev, mev, rtol=1.0e-13, atol=1.0e-13)
        and np.allclose(gev, fm_inverse, rtol=1.0e-13, atol=1.0e-13)
    )
    passed = bool(unit_invariant and all(rejection.values()))
    return {
        "schema": "C400-S2M-CURRENT-ADAPTER-SEMANTICS-V1",
        "status": "DIMENSIONAL_LPS_CURRENT_UNITS_AND_FIXED_SPIN_BASIS_VERIFIED" if passed else "CURRENT_ADAPTER_SEMANTICS_FAILED",
        "expected_GC_GM_GQ": tuple(float(value) for value in expected),
        "GeV_extraction": tuple(complex(value) for value in gev),
        "MeV_extraction": tuple(complex(value) for value in mev),
        "fm_inverse_extraction": tuple(complex(value) for value in fm_inverse),
        "unit_invariant": unit_invariant,
        "LPS_current_matrix_units": "same units as declared mass_units",
        "rejections": rejection,
        "pass": passed,
        "physical_current_claim": False,
        "production_current_selected": False,
    }


def generate() -> Mapping[str, Any]:
    started = now()
    dependency = dependency_closure_record()
    projector = projector_semantics_record()
    current_semantics = current_adapter_semantics_record()
    write_json("dependency_closure.json", dependency)
    write_json("projected_state_semantics.json", projector)
    write_json("current_adapter_semantics.json", current_semantics)
    write_json(
        "scientific_nonclaims.json",
        {
            "schema": "C400-S2M-SCIENTIFIC-NONCLAIMS-V1",
            "nonclaims": (
                "no C396 numerical forward map",
                "no physical deuteron-sector state",
                "no production current selection",
                "no physical fit or physical rank",
                "no resolution averaging",
                "no Hamiltonian activation",
                "no claim that the C64 runtime artifact gap is repaired",
            ),
        },
    )
    generated = sorted(
        path for path in OUT.iterdir()
        if path.is_file() and path.name != "generation_result.json"
    )
    passed = bool(
        dependency["all_clear"]
        and projector["pass"]
        and current_semantics["pass"]
    )
    result = {
        "schema": "C400-S2M-GENERATION-RESULT-V1",
        "status": "MERGE_CLOSURE_EVIDENCE_GENERATED" if passed else "MERGE_CLOSURE_EVIDENCE_FAILED",
        "started_at_utc": started,
        "finished_at_utc": now(),
        "dependency_closure_pass": dependency["all_clear"],
        "projected_state_semantics_pass": projector["pass"],
        "current_adapter_semantics_pass": current_semantics["pass"],
        "artifact_count_excluding_self": len(generated),
        "artifacts": tuple(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in generated
        ),
        "merge_closure_pass": passed,
        "next_owner": "CODEX_LIVE_INTEGRATION_THEN_USER_CHATGPT_MERGE_REVIEW",
        "physical_activation": False,
    }
    write_json("generation_result.json", result)
    return result


if __name__ == "__main__":
    print(json.dumps(jsonable(generate()), indent=2, sort_keys=True))
