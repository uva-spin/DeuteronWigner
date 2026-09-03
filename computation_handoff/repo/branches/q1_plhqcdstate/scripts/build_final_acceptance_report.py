#!/usr/bin/env python3
"""Build the requirement-by-requirement final project acceptance audit."""

from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "validation/final_acceptance_manifest.json"
OUT = ROOT / "outputs/validation/final_acceptance_report.json"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    match = re.search(r"(\d+) passed", run.stdout)
    passed_tests = None if match is None else int(match.group(1))
    wp8 = json.loads(
        (ROOT / "outputs/validation/wp8_acceptance_report.json").read_text()
    )
    wp10 = json.loads(
        (ROOT / "outputs/validation/wp10_acceptance_report.json").read_text()
    )
    criteria = []
    for item in manifest["criteria"]:
        evidence = (
            item["implementation_files"] + item["tests"]
            + item["artifacts"] + item["documentation"]
        )
        missing = [path for path in evidence if not (ROOT / path).exists()]
        criteria.append({
            **item,
            "missing_evidence": missing,
            "observed_status": (
                "verified"
                if not missing and run.returncode == 0
                and wp8["completion_ready"]
                and wp8["full_suite_passed_count"] == passed_tests
                and wp10["completion_ready"]
                and wp10["full_suite_passed_count"] == passed_tests
                else "missing_or_failed_evidence"
            ),
        })
    limitations = [
        {
            "classification": "model-dependent configured input",
            "item": "Nucleon off-forward GTMD boundary is rank-zero factorized; callback replacement is supported.",
            "scope_disposition": "inside model as declared configurable default, not claimed as a fit"
        },
        {
            "classification": "model-dependent configured inputs",
            "item": "The four spin-half gluon T-odd functions are constrained by the published full-vertex spectator hierarchy; spin-1 g1LT/g1TT use AV18 S-D coherence and a screened eikonal. The unavailable PVGlue20 replicas and Q=5 fit evolution prevent a statistical fit band.",
            "scope_disposition": "all six structures and full correlators are implemented, color/link resolved, positivity tested, and replaceable; the displayed band is explicitly model uncertainty"
        },
        {
            "classification": "external-data upgrade",
            "item": "Polarized/tensor DPDF covariance, Yang-2024 machine-readable replicas, and a fully coupled transverse NNpi amplitude are unavailable.",
            "scope_disposition": "named model scenarios and typed replacement interfaces are production members; no joint covariance is fabricated"
        },
        {
            "classification": "observable-specific extension",
            "item": "No universal high-qT Y term is attached to intrinsic TMDs.",
            "scope_disposition": "W validity is serialized; specified high-qT observables require sourced FO/ASY inputs"
        }
    ]
    verified = all(item["observed_status"] == "verified" for item in criteria)
    report = {
        "schema_version": manifest["schema_version"],
        "scope": manifest["scope"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": str(MANIFEST.relative_to(ROOT)),
        "python": sys.executable,
        "full_suite_returncode": run.returncode,
        "full_suite_passed_count": passed_tests,
        "wp8_completion_ready": wp8["completion_ready"],
        "wp8_full_suite_passed_count": wp8["full_suite_passed_count"],
        "wp10_completion_ready": wp10["completion_ready"],
        "wp10_full_suite_passed_count": wp10["full_suite_passed_count"],
        "criteria": criteria,
        "counts": {
            "verified": sum(x["observed_status"] == "verified" for x in criteria),
            "missing_or_failed_evidence": sum(
                x["observed_status"] != "verified" for x in criteria
            ),
        },
        "remaining_limitations": limitations,
        "unresolved_required_implementation": [],
        "completion_ready": verified,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUT.relative_to(ROOT)),
        "criteria": report["counts"],
        "tests": passed_tests,
        "wp8_completion_ready": wp8["completion_ready"],
        "completion_ready": report["completion_ready"],
    }, indent=2))
    if not verified:
        raise SystemExit("final acceptance audit failed")


if __name__ == "__main__":
    main()
