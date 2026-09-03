#!/usr/bin/env python3
"""Build the machine-readable WP10 rich-dynamics acceptance audit."""

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "validation/wp10_manifest.json"
OUTPUT = ROOT / "outputs/validation/wp10_acceptance_report.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    match = re.search(r"(\d+) passed", run.stdout)
    passed = None if match is None else int(match.group(1))
    criteria = []
    for item in manifest["criteria"]:
        evidence = (
            item["implementation_files"]
            + item["tests"]
            + item["artifacts"]
            + item["documentation"]
        )
        missing = [path for path in evidence if not (ROOT / path).exists()]
        observed = (
            "verified"
            if item["status"] == "complete"
            and not item["remaining"]
            and not missing
            and run.returncode == 0
            and passed is not None
            else "missing_or_failed_evidence"
        )
        criteria.append({
            **item,
            "missing_evidence": missing,
            "observed_status": observed,
        })
    completion = (
        manifest["completion_ready"]
        and all(item["observed_status"] == "verified" for item in criteria)
    )
    report = {
        "schema_version": manifest["schema_version"],
        "scope": manifest["scope"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "python": sys.executable,
        "full_suite_returncode": run.returncode,
        "full_suite_passed_count": passed,
        "counts": {
            "verified": sum(x["observed_status"] == "verified" for x in criteria),
            "missing_or_failed_evidence": sum(
                x["observed_status"] != "verified" for x in criteria
            ),
        },
        "criteria": criteria,
        "declared_limitations": manifest["declared_limitations"],
        "unresolved_required_implementation": [],
        "completion_ready": completion,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "criteria": report["counts"],
        "tests": passed,
        "completion_ready": completion,
    }, indent=2))
    if not completion:
        raise SystemExit("WP10 acceptance audit failed")


if __name__ == "__main__":
    main()
