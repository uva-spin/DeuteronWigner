#!/usr/bin/env python3
"""Materialize the C35 Branch-G no-go result as an ignored runtime bundle.

The script name mirrors the eventual soft-calculation entry point, but the
authoritative C35 plan is unavailable.  Therefore this executable is allowed
to write only a content-addressed, empty-not-zero no-go record.  It never
evaluates or serializes a finite-basis one-loop coefficient.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any, Mapping

from deuteron_wigner.bridge.s0c import core as c35


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUNTIME_ROOT = ROOT / "data" / "runtime" / "c35" / "branch_g"


def _canonical_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _within_runtime_root(path: Path) -> bool:
    try:
        path.resolve().relative_to((ROOT / "data" / "runtime").resolve())
    except ValueError:
        return False
    return True


def _assert_ignored(path: Path) -> None:
    relative = path.resolve().relative_to(ROOT.resolve())
    result = subprocess.run(
        ("git", "check-ignore", "--quiet", "--", str(relative)),
        cwd=ROOT,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError("C35_RUNTIME_TARGET_IS_NOT_GIT_IGNORED")


def build_no_go_payload() -> dict[str, Any]:
    plan = c35.default_gauge_plan_selection()
    closure = c35.default_closure_report()
    contributions = c35.fail_closed_contribution_ledger()
    payload = {
        "schema_version": "1.0.0",
        "bundle_id": "C35.BRANCH_G.NO_GO.RUNTIME.v1",
        "scope": c35.C35_SCOPE,
        "baseline_commit": c35.C35_BASELINE_COMMIT,
        "soft_root": c35.C33_SOFT_ROOT,
        "collinear_root": c35.C32_COLLINEAR_ROOT,
        "cross_root_relation": "NO_JOINT_MEASURE",
        "selected_plan": plan.selected.value,
        "plan_frozen_before_coefficient": plan.frozen_before_coefficient,
        "coefficient_attempted": plan.coefficient_attempted,
        "primary_no_go": closure.primary_no_go,
        "secondary_no_go": closure.secondary_no_go,
        "outcome_branch": closure.outcome_branch,
        "exact_next_package": closure.exact_next_package,
        "finite_basis_one_loop": {
            "value": None,
            "value_semantics": c35.NONZERO_UNKNOWN,
            "coefficient_issued": False,
            "continuum_coefficient_substituted": False,
        },
        "contributions": [
            {
                "contribution_id": row.contribution_id,
                "contribution_class": row.contribution_class,
                "status": row.status.value,
                "value": None,
                "value_semantics": row.expression,
                "blocking": row.blocking,
                "exact_missing_calculation": row.exact_missing_calculation,
            }
            for row in contributions
        ],
        "counterterms": {
            "bare_coefficient_available": False,
            "uv": None,
            "rapidity": None,
            "residual_line_mass": None,
            "status": c35.EMPTY_NOT_ZERO,
        },
        "soft_side_zero_bin": {
            "value": None,
            "status": c35.EMPTY_NOT_ZERO,
            "operator_identical_test_ready": False,
        },
        "microscopic_proton_export": {
            "shape": [0],
            "values": None,
            "status": c35.EMPTY_NOT_ZERO,
        },
        "bridge_rerun": False,
        "art25_consumed": False,
        "inference_reachable": False,
        "production_reachable": False,
        "generator": {
            "path": "scripts/run_c35_soft_calculation.py",
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
    }
    if len(payload["contributions"]) != 18:
        raise RuntimeError("C35_RUNTIME_CONTRIBUTION_COUNT_MISMATCH")
    if any(row["value"] is not None for row in payload["contributions"]):
        raise RuntimeError("C35_RUNTIME_COEFFICIENT_FORBIDDEN")
    return payload


def write_no_go_bundle(runtime_root: Path = DEFAULT_RUNTIME_ROOT) -> Path:
    runtime_root = runtime_root.resolve()
    if not _within_runtime_root(runtime_root):
        raise RuntimeError("C35_RUNTIME_OUTPUT_MUST_REMAIN_UNDER_DATA_RUNTIME")
    _assert_ignored(runtime_root)
    payload = build_no_go_payload()
    digest = _canonical_hash(payload)
    record = dict(payload)
    record["content_hash"] = digest
    encoded = json.dumps(record, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False) + "\n"
    target_dir = runtime_root / digest
    target = target_dir / "c35_branch_g_no_go.json"
    target_dir.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if target.read_text() != encoded:
            raise RuntimeError("C35_RUNTIME_CONTENT_ADDRESS_COLLISION")
    else:
        target.write_text(encoded)
    _assert_ignored(target)
    reloaded = json.loads(target.read_text())
    recorded = reloaded.pop("content_hash")
    if recorded != digest or _canonical_hash(reloaded) != digest:
        raise RuntimeError("C35_RUNTIME_CONTENT_HASH_MISMATCH")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runtime-root",
        type=Path,
        default=DEFAULT_RUNTIME_ROOT,
        help="Ignored output directory below data/runtime (default: %(default)s)",
    )
    args = parser.parse_args()
    path = write_no_go_bundle(args.runtime_root)
    print("C35_BRANCH_G_RUNTIME_BUNDLE_PASS", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
