#!/usr/bin/env python3
"""Persist the common all-named-TMD controlled-limit audit."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path

from deuteron_wigner.controlled_limits import run_controlled_limit_audit


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/validation/controlled_limits.audit.json"


def main() -> None:
    checks = run_controlled_limit_audit()
    report = {
        "scope": (
            "complete 18-name quark parent basis plus full quark/gluon "
            "nuclear-correction matrices"
        ),
        "checks": [asdict(check) for check in checks],
        "passed": all(check.passed for check in checks),
        "maximum_absolute_residual": max(
            check.maximum_absolute_residual for check in checks
        ),
    }
    if not report["passed"]:
        raise RuntimeError("controlled-limit audit failed")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "checks": len(checks),
        "maximum_absolute_residual": report["maximum_absolute_residual"],
    }, indent=2))


if __name__ == "__main__":
    main()
