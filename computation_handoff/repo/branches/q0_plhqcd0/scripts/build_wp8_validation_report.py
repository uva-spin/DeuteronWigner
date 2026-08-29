#!/usr/bin/env python3
"""Build the authoritative machine-readable WP8 validation matrix."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "validation/wp8_manifest.json"
DEFAULT_OUTPUT = ROOT / "outputs/validation/wp8_acceptance_report.json"


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--python", default=sys.executable,
        help="interpreter whose pytest installation defines the validation run",
    )
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text())
    collect = run([args.python, "-m", "pytest", "--collect-only", "-q"])
    collected_nodes = {
        line.strip()
        for line in collect.stdout.splitlines()
        if line.startswith("tests/") and "::" in line
    }
    full = None
    passed_count = None
    if not args.skip_tests and collect.returncode == 0:
        full = run([args.python, "-m", "pytest", "-q"])
        match = re.search(r"(\d+) passed", full.stdout)
        passed_count = None if match is None else int(match.group(1))

    results = []
    for requirement in manifest["requirements"]:
        missing_tests = [
            prefix
            for prefix in requirement["test_prefixes"]
            if not any(node.startswith(prefix) for node in collected_nodes)
        ]
        missing_artifacts = [
            path for path in requirement["artifacts"]
            if not (ROOT / path).exists()
        ]
        missing_provenance = [
            path for path in requirement["provenance"]
            if not (ROOT / path).exists()
        ]
        evidence_complete = not (
            missing_tests or missing_artifacts or missing_provenance
        )
        suite_passed = (
            args.skip_tests
            or (full is not None and full.returncode == 0 and passed_count is not None)
        )
        declared = requirement["declared_status"]
        if not evidence_complete or collect.returncode != 0 or not suite_passed:
            observed = "missing_or_failed_evidence"
        elif declared == "implemented":
            observed = "verified"
        else:
            observed = declared
        results.append({
            **requirement,
            "observed_status": observed,
            "evidence_complete": evidence_complete,
            "missing_test_prefixes": missing_tests,
            "missing_artifacts": missing_artifacts,
            "missing_provenance": missing_provenance,
        })

    counts = {
        status: sum(item["observed_status"] == status for item in results)
        for status in ("verified", "partial", "open", "missing_or_failed_evidence")
    }
    report = {
        "schema_version": manifest["schema_version"],
        "scope": manifest["scope"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": str(args.manifest.relative_to(ROOT)),
        "python": args.python,
        "pytest_collection_returncode": collect.returncode,
        "collected_test_count": len(collected_nodes),
        "full_suite_executed": not args.skip_tests,
        "full_suite_returncode": None if full is None else full.returncode,
        "full_suite_passed_count": passed_count,
        "counts": counts,
        "completion_ready": (
            counts["partial"] == 0
            and counts["open"] == 0
            and counts["missing_or_failed_evidence"] == 0
        ),
        "requirements": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(args.output.relative_to(ROOT)),
        "counts": counts,
        "completion_ready": report["completion_ready"],
        "collected_tests": len(collected_nodes),
        "passed_tests": passed_count,
    }, indent=2))
    return 0 if collect.returncode == 0 and (args.skip_tests or full.returncode == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
